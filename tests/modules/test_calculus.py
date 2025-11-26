"""Tests for calculus module"""

import pytest
from unittest.mock import AsyncMock, MagicMock
from src.modules.calculus import CalculusModule, _get_symp
from src.utils.exceptions import InvalidInputError


@pytest.fixture
def mock_agent():
    agent = MagicMock()
    agent.generate_json_response = AsyncMock()
    return agent


@pytest.mark.asyncio
async def test_calculus_derivative_polynomial(mock_agent):
    """Polinom turev testi"""
    mock_response = {
        "result": "12",
        "steps": ["d/dx x^3 = 3x^2", "3*(2)^2 = 12"],
        "confidence_score": 1.0,
    }
    mock_agent.generate_json_response.return_value = mock_response

    module = CalculusModule(mock_agent)
    result = await module.calculate("derivative x^3 at x=2")

    assert result is not None
    assert result.domain == "calculus"
    assert len(result.steps) >= 1
    assert result.result == "12"


@pytest.mark.asyncio
async def test_calculus_invalid_input(mock_agent):
    """Gecersiz giris testi"""
    module = CalculusModule(mock_agent)

    with pytest.raises(InvalidInputError):
        await module.calculate("")


@pytest.mark.asyncio
async def test_calculus_integral(mock_agent):
    """Integral testi"""
    mock_response = {
        "result": "1/3",
        "steps": ["int x^2 = x^3/3", "1^3/3 - 0 = 1/3"],
        "confidence_score": 1.0,
    }
    mock_agent.generate_json_response.return_value = mock_response

    module = CalculusModule(mock_agent)
    result = await module.calculate("integral x^2 from 0 to 1")

    assert result is not None
    assert result.domain == "calculus"
    assert result.result == "1/3"


@pytest.mark.asyncio
async def test_calculus_error_handling(mock_agent):
    """Hata durumu testi"""
    mock_agent.generate_json_response.side_effect = Exception("API Error")
    module = CalculusModule(mock_agent)

    with pytest.raises(Exception, match="API Error"):
        await module.calculate("derivative x")


def test_get_symp():
    """Sympy import testi"""
    sympy = _get_symp()
    assert sympy is not None
    assert hasattr(sympy, "Symbol")
