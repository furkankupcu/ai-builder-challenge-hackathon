import pytest
from unittest.mock import AsyncMock, MagicMock
from src.modules.equation_solver import EquationSolverModule
from src.schemas.models import CalculationResult


@pytest.fixture
def mock_agent():
    agent = MagicMock()
    agent.chat_async = AsyncMock()
    return agent


@pytest.fixture
def equation_solver(mock_agent):
    return EquationSolverModule(mock_agent)


@pytest.mark.asyncio
async def test_calculate_success(equation_solver, mock_agent):
    # Mock Gemini response
    mock_response = {
        "result": ["x1 = 2", "x2 = 3"],
        "steps": ["Step 1", "Step 2"],
        "confidence_score": 0.95,
    }
    equation_solver._call_gemini = AsyncMock(return_value=mock_response)

    expression = "x^2 - 5x + 6 = 0"
    result = await equation_solver.calculate(expression)

    assert isinstance(result, CalculationResult)
    assert result.result == ["x1 = 2", "x2 = 3"]
    assert result.steps == ["Step 1", "Step 2"]
    assert result.confidence_score == 0.95
    equation_solver._call_gemini.assert_called_once_with(expression)


@pytest.mark.asyncio
async def test_calculate_error(equation_solver):
    equation_solver._call_gemini = AsyncMock(side_effect=Exception("Solver error"))

    with pytest.raises(Exception, match="Solver error"):
        await equation_solver.calculate("invalid equation")
