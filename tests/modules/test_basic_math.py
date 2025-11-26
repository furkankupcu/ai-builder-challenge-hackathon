"""Tests for basic math module"""

import pytest
from unittest.mock import AsyncMock, MagicMock
from src.modules.basic_math import BasicMathModule, safe_divide
from src.schemas.models import CalculationResult


@pytest.fixture
def mock_agent():
    agent = MagicMock()
    agent.chat_async = AsyncMock()
    return agent


@pytest.fixture
def basic_math_module(mock_agent):
    return BasicMathModule(mock_agent)


@pytest.mark.asyncio
async def test_basic_addition(basic_math_module):
    """Temel toplama testi"""
    mock_response = {"result": 4, "steps": ["2+2=4"], "confidence_score": 1.0}
    basic_math_module._call_gemini = AsyncMock(return_value=mock_response)

    result = await basic_math_module.calculate("2 + 2")

    assert result is not None
    assert result.result == 4
    assert result.domain == "basic_math"
    assert result.confidence_score == 1.0


@pytest.mark.asyncio
async def test_basic_sqrt(basic_math_module):
    """Karekok testi"""
    mock_response = {"result": 16, "steps": ["sqrt(256)=16"], "confidence_score": 1.0}
    basic_math_module._call_gemini = AsyncMock(return_value=mock_response)

    result = await basic_math_module.calculate("sqrt(256)")

    assert result is not None
    assert result.result == 16
    assert result.domain == "basic_math"


@pytest.mark.asyncio
async def test_calculate_error(basic_math_module):
    basic_math_module._call_gemini = AsyncMock(side_effect=Exception("Math error"))

    with pytest.raises(Exception, match="Math error"):
        await basic_math_module.calculate("invalid")


def test_safe_divide():
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(5, 2) == 2.5

    with pytest.raises(ValueError, match="Sifira bolme hatasi"):
        safe_divide(10, 0)
