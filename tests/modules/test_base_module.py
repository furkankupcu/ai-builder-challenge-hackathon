import pytest
from unittest.mock import MagicMock, AsyncMock
from src.modules.base_module import BaseModule
from src.schemas.models import CalculationResult


class ConcreteModule(BaseModule):
    def _get_domain_prompt(self):
        return "Test Prompt {expression}"

    async def calculate(self, expression: str, **kwargs):
        return await self._call_gemini(expression)


@pytest.fixture
def mock_agent():
    agent = MagicMock()
    agent.generate_json_response = AsyncMock()
    return agent


@pytest.fixture
def module(mock_agent):
    return ConcreteModule(mock_agent)


@pytest.mark.asyncio
async def test_base_module_initialization(module, mock_agent):
    assert module.gemini_agent == mock_agent
    assert module.domain_prompt == "Test Prompt {expression}"
    assert module.validator is not None


@pytest.mark.asyncio
async def test_validate_input(module):
    assert module.validate_input("2 + 2") is True

    # Test inherited validation logic
    with pytest.raises(
        Exception
    ):  # Should raise InvalidInputError or SecurityViolationError
        module.validate_input("__import__")


@pytest.mark.asyncio
async def test_call_gemini(module, mock_agent):
    mock_agent.generate_json_response.return_value = {"result": "test"}

    response = await module._call_gemini("test_expr")

    mock_agent.generate_json_response.assert_called_once()
    args, _ = mock_agent.generate_json_response.call_args
    assert "Test Prompt test_expr" in args[0]
    assert response == {"result": "test"}


def test_create_result(module):
    gemini_response = {
        "result": 42,
        "steps": ["step1"],
        "confidence_score": 0.9,
        "metadata": {"key": "value"},
    }

    result = module._create_result(gemini_response, "test_domain")

    assert isinstance(result, CalculationResult)
    assert result.result == 42
    assert result.steps == ["step1"]
    assert result.confidence_score == 0.9
    assert result.domain == "test_domain"
    assert result.metadata == {"key": "value"}


def test_create_result_defaults(module):
    gemini_response = {}

    result = module._create_result(gemini_response, "test_domain")

    assert result.result == ""
    assert result.steps == []
    assert result.confidence_score == 1.0
    assert result.visual_data is None
