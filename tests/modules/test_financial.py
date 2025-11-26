import pytest
from unittest.mock import AsyncMock, MagicMock
from decimal import Decimal
from src.modules.financial import FinancialModule
from src.schemas.models import CalculationResult
from src.config.settings import settings


@pytest.fixture
def mock_agent():
    agent = MagicMock()
    agent.chat_async = AsyncMock()
    return agent


@pytest.fixture
def financial_module(mock_agent):
    return FinancialModule(mock_agent)


@pytest.mark.asyncio
async def test_calculate_success(financial_module):
    # Mock Gemini response
    mock_response = {"result": 1000.50, "steps": ["Step 1"], "confidence_score": 0.9}
    financial_module._call_gemini = AsyncMock(return_value=mock_response)

    expression = "calculate interest"
    result = await financial_module.calculate(expression, currency="USD")

    assert isinstance(result, CalculationResult)
    assert isinstance(result.result, Decimal)
    assert result.result == Decimal("1000.50")
    financial_module._call_gemini.assert_called_once_with(expression, currency="USD")


@pytest.mark.asyncio
async def test_calculate_default_currency(financial_module):
    mock_response = {"result": 100}
    financial_module._call_gemini = AsyncMock(return_value=mock_response)

    await financial_module.calculate("test")

    financial_module._call_gemini.assert_called_once_with(
        "test", currency=settings.DEFAULT_CURRENCY
    )


@pytest.mark.asyncio
async def test_calculate_error(financial_module):
    financial_module._call_gemini = AsyncMock(side_effect=Exception("Financial error"))

    with pytest.raises(Exception, match="Financial error"):
        await financial_module.calculate("invalid")
