import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from src.modules.linear_regression import LinearRegressionModule
from src.schemas.models import CalculationResult


@pytest.fixture
def mock_agent():
    agent = MagicMock()
    agent.chat_async = AsyncMock()
    return agent


@pytest.fixture
def linear_regression_module(mock_agent):
    # Mock cache dir creation
    with patch("pathlib.Path.mkdir"):
        return LinearRegressionModule(mock_agent)


@pytest.mark.asyncio
async def test_calculate_success(linear_regression_module):
    # Mock Gemini response
    mock_response = {
        "result": {
            "slope": 2.0,
            "intercept": 0.0,
            "equation": "y = 2x + 0",
            "r_squared": 1.0,
        },
        "steps": ["Step 1: Calculate mean", "Step 2: Calculate slope"],
        "confidence_score": 0.98,
    }
    linear_regression_module._call_gemini = AsyncMock(return_value=mock_response)

    expression = "x=[1,2,3], y=[2,4,6]"
    result = await linear_regression_module.calculate(expression)

    assert isinstance(result, CalculationResult)
    assert result.result["slope"] == 2.0
    assert result.domain == "linear_regression"
    linear_regression_module._call_gemini.assert_called_once_with(expression)


@pytest.mark.asyncio
async def test_calculate_with_plot(linear_regression_module):
    # Mock Gemini response with visual data
    mock_response = {
        "result": {"slope": 1.0, "intercept": 0.0},
        "visual_data": {
            "data_points": {"x": [1, 2, 3], "y": [1, 2, 3]},
            "model_params": {"slope": 1.0, "intercept": 0.0},
        },
        "confidence_score": 1.0,
    }
    linear_regression_module._call_gemini = AsyncMock(return_value=mock_response)

    # Mock matplotlib
    with patch("src.modules.linear_regression.plt") as mock_plt:
        expression = "plot regression x=[1,2,3] y=[1,2,3]"
        result = await linear_regression_module.calculate(expression)

        assert isinstance(result, CalculationResult)
        assert result.visual_data is not None
        assert "plot_paths" in result.visual_data
        assert "png" in result.visual_data["plot_paths"]

        # Verify plotting calls
        mock_plt.figure.assert_called()
        mock_plt.scatter.assert_called()
        mock_plt.plot.assert_called()
        mock_plt.savefig.assert_called()
        mock_plt.close.assert_called()


@pytest.mark.asyncio
async def test_calculate_error(linear_regression_module):
    linear_regression_module._call_gemini = AsyncMock(
        side_effect=Exception("Regression error")
    )

    with pytest.raises(Exception, match="Regression error"):
        await linear_regression_module.calculate("invalid data")
