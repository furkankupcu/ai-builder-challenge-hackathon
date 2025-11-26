import pytest
import sys
from unittest.mock import AsyncMock, MagicMock, patch
from src.main import CalculatorAgent, interactive_mode, single_command_mode, main
from src.schemas.models import CalculationResult
from src.utils.exceptions import (
    SecurityViolationError,
    InvalidInputError,
    AgentModuleNotFoundError,
    CalculationError,
)


@pytest.fixture
def mock_gemini_agent():
    agent = MagicMock()
    agent.chat_async = AsyncMock()
    return agent


@pytest.fixture
def calculator_agent(mock_gemini_agent):
    # Mock settings validation to avoid side effects
    with patch("src.main.settings.validate"):
        agent = CalculatorAgent()
        # Mock all modules to isolate agent logic
        for module_name in agent.modules:
            agent.modules[module_name] = AsyncMock()
            agent.modules[module_name].calculate = AsyncMock()
        return agent


@pytest.mark.asyncio
async def test_agent_initialization():
    with patch("src.main.settings.validate") as mock_validate:
        agent = CalculatorAgent()
        mock_validate.assert_called_once()
        assert agent.modules is not None
        assert "basic_math" in agent.modules


@pytest.mark.asyncio
async def test_process_command_success(calculator_agent):
    # Setup mock
    mock_result = CalculationResult(
        result="4", steps=["2 + 2 = 4"], confidence_score=1.0, domain="basic_math"
    )
    calculator_agent.modules["basic_math"].calculate.return_value = mock_result

    # Test
    result = await calculator_agent.process_command("2 + 2")

    # Assert
    assert "✅ Sonuc: 4" in result
    assert "📝 Adimlar:" in result
    assert "1. 2 + 2 = 4" in result


@pytest.mark.asyncio
async def test_process_command_security_error(calculator_agent):
    # Mock validator to raise error
    calculator_agent.validator.sanitize_expression = MagicMock(
        side_effect=SecurityViolationError("Unsafe")
    )

    result = await calculator_agent.process_command("eval(bad)")
    assert "❌ Guvenlik hatasi" in result


@pytest.mark.asyncio
async def test_process_command_invalid_input(calculator_agent):
    # Mock parser to raise error or validator
    calculator_agent.validator.sanitize_expression = MagicMock(
        side_effect=InvalidInputError("Empty")
    )

    result = await calculator_agent.process_command("")
    assert "❌ Gecersiz giris" in result


@pytest.mark.asyncio
async def test_process_command_module_not_found(calculator_agent):
    # Mock parser to return unknown module
    calculator_agent.parser.parse = MagicMock(return_value=("unknown_module", "expr"))

    result = await calculator_agent.process_command("test")
    assert "❌ Modul bulunamadi" in result


@pytest.mark.asyncio
async def test_process_command_calculation_error(calculator_agent):
    # Mock module to raise error
    calculator_agent.modules["basic_math"].calculate.side_effect = CalculationError(
        "Math error"
    )

    result = await calculator_agent.process_command("2 / 0")
    assert "❌ Hesaplama hatasi" in result


@pytest.mark.asyncio
async def test_format_output_variations(calculator_agent):
    # Test low confidence
    result_low_conf = CalculationResult(
        result="4", steps=[], confidence_score=0.5, domain="test"
    )
    output = calculator_agent._format_output(result_low_conf)
    assert "⚠️  Guven Skoru: 0.50" in output

    # Test visual data
    result_visual = CalculationResult(
        result="Graph",
        steps=[],
        visual_data={"plot_paths": {"png": "path.png"}},
        domain="test",
    )
    output = calculator_agent._format_output(result_visual)
    assert "📊 Grafik: path.png" in output


@pytest.mark.asyncio
async def test_interactive_mode():
    with patch("builtins.input", side_effect=["2+2", "quit"]), patch(
        "builtins.print"
    ) as mock_print, patch("src.main.CalculatorAgent") as MockAgent:

        mock_instance = MockAgent.return_value
        mock_instance.process_command = AsyncMock(return_value="Result")

        await interactive_mode()

        assert mock_instance.process_command.called


@pytest.mark.asyncio
async def test_single_command_mode():
    with patch("src.main.CalculatorAgent") as MockAgent, patch(
        "builtins.print"
    ) as mock_print:

        mock_instance = MockAgent.return_value
        mock_instance.process_command = AsyncMock(return_value="Result")

        await single_command_mode("2+2")

        mock_instance.process_command.assert_called_with("2+2")
        mock_print.assert_called_with("Result")


def test_main_interactive():
    with patch("sys.argv", ["main.py"]), patch(
        "src.main.asyncio.run"
    ) as mock_run, patch("src.main.interactive_mode") as mock_interactive:

        main()
        mock_run.assert_called()


def test_main_single_command():
    with patch("sys.argv", ["main.py", "2+2"]), patch(
        "src.main.asyncio.run"
    ) as mock_run, patch("src.main.single_command_mode") as mock_single:

        main()
        mock_run.assert_called()


@pytest.mark.asyncio
async def test_process_command_unexpected_error(calculator_agent):
    # Mock module to raise generic error
    calculator_agent.modules["basic_math"].calculate.side_effect = Exception("Boom")

    result = await calculator_agent.process_command("2 + 2")
    assert "❌ Beklenmeyen hata" in result


def test_format_output_with_visuals(calculator_agent):
    result = CalculationResult(
        result="Graph",
        visual_data={"plot_paths": {"png": "path/to/plot.png"}},
        confidence_score=0.8,
    )

    formatted = calculator_agent._format_output(result)
    assert "📊 Grafik: path/to/plot.png" in formatted
    assert "⚠️  Guven Skoru: 0.80" in formatted


@pytest.mark.asyncio
async def test_interactive_mode_quit():
    with patch("builtins.input", side_effect=["quit"]), patch(
        "builtins.print"
    ) as mock_print, patch("src.main.CalculatorAgent"):

        await interactive_mode()
        # Check if "Gule gule!" was printed
        assert any("Gule gule!" in str(call) for call in mock_print.call_args_list)


@pytest.mark.asyncio
async def test_interactive_mode_process():
    mock_agent_instance = AsyncMock()
    mock_agent_instance.process_command.return_value = "Result"

    with patch("builtins.input", side_effect=["2+2", "exit"]), patch(
        "builtins.print"
    ), patch("src.main.CalculatorAgent", return_value=mock_agent_instance):

        await interactive_mode()
        mock_agent_instance.process_command.assert_called_with("2+2")


@pytest.mark.asyncio
async def test_single_command_mode():
    mock_agent_instance = AsyncMock()
    mock_agent_instance.process_command.return_value = "Result"

    with patch("builtins.print") as mock_print, patch(
        "src.main.CalculatorAgent", return_value=mock_agent_instance
    ):

        await single_command_mode("2+2")
        mock_agent_instance.process_command.assert_called_once_with("2+2")
        mock_print.assert_called_with("Result")


def test_main_interactive():
    with patch("sys.argv", ["main.py"]), patch(
        "src.main.interactive_mode", new_callable=AsyncMock
    ) as mock_interactive:

        main()
        mock_interactive.assert_called_once()


def test_main_single_command():
    with patch("sys.argv", ["main.py", "2", "+", "2"]), patch(
        "src.main.single_command_mode", new_callable=AsyncMock
    ) as mock_single:

        main()
        mock_single.assert_called_once_with("2 + 2")
