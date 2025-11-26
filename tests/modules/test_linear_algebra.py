"""Tests for linear algebra module"""

import pytest
from unittest.mock import AsyncMock, MagicMock
from src.modules.linear_algebra import LinearAlgebraModule
from src.utils.exceptions import InvalidInputError


@pytest.fixture
def mock_agent():
    agent = MagicMock()
    agent.generate_json_response = AsyncMock()
    return agent


@pytest.mark.asyncio
async def test_matrix_multiplication(mock_agent):
    """Matris carpimi testi"""
    mock_response = {
        "result": "[[17], [39]]",
        "steps": ["Matrix multiplication steps"],
        "confidence_score": 1.0,
    }
    mock_agent.generate_json_response.return_value = mock_response

    module = LinearAlgebraModule(mock_agent)
    result = await module.calculate("[[1,2],[3,4]] * [[5],[6]]")

    assert result is not None
    assert result.domain == "linear_algebra"
    assert result.result == "[[17], [39]]"


@pytest.mark.asyncio
async def test_determinant(mock_agent):
    """Determinant testi"""
    mock_response = {
        "result": "-2",
        "steps": ["1*4 - 2*3 = -2"],
        "confidence_score": 1.0,
    }
    mock_agent.generate_json_response.return_value = mock_response

    module = LinearAlgebraModule(mock_agent)
    result = await module.calculate("determinant [[1,2],[3,4]]")

    assert result is not None
    assert result.domain == "linear_algebra"
    assert result.result == "-2"


@pytest.mark.asyncio
async def test_linear_algebra_error(mock_agent):
    """Hata durumu testi"""
    mock_agent.generate_json_response.side_effect = Exception("Matrix Error")
    module = LinearAlgebraModule(mock_agent)

    with pytest.raises(Exception, match="Matrix Error"):
        await module.calculate("invalid matrix")


@pytest.mark.asyncio
async def test_linear_algebra_invalid_input(mock_agent):
    """Gecersiz giris testi"""
    module = LinearAlgebraModule(mock_agent)
    with pytest.raises(InvalidInputError):
        await module.calculate("")
