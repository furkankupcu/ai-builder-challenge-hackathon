import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from src.modules.graph_plotter import GraphPlotterModule
from src.schemas.models import CalculationResult


@pytest.fixture
def mock_agent():
    agent = MagicMock()
    agent.chat_async = AsyncMock()
    return agent


@pytest.fixture
def graph_plotter(mock_agent):
    return GraphPlotterModule(mock_agent)


@pytest.mark.asyncio
async def test_calculate_success(graph_plotter):
    # Mock Gemini response
    mock_response = {
        "result": "Graph created",
        "visual_data": {"plot_type": "2d", "x_range": [-10, 10]},
    }
    graph_plotter._call_gemini = AsyncMock(return_value=mock_response)

    # Mock _create_plot to avoid actual plotting
    mock_plot_paths = {"png": "path/to/plot.png"}
    graph_plotter._create_plot = AsyncMock(return_value=mock_plot_paths)

    expression = "plot x^2"
    result = await graph_plotter.calculate(expression)

    assert isinstance(result, CalculationResult)
    assert result.visual_data["plot_paths"] == mock_plot_paths
    graph_plotter._call_gemini.assert_called_once_with(expression)
    graph_plotter._create_plot.assert_called_once()


@pytest.mark.asyncio
async def test_calculate_cached(graph_plotter):
    expression = "plot x^2"
    cache_key = expression.lower().strip()
    graph_plotter.plot_cache[cache_key] = "cached/path.png"

    # Mock _load_cached_result
    mock_result = CalculationResult(
        result="Cached", visual_data={"plot_paths": {"png": "cached/path.png"}}
    )
    graph_plotter._load_cached_result = MagicMock(return_value=mock_result)

    result = await graph_plotter.calculate(expression)

    assert result == mock_result
    graph_plotter._load_cached_result.assert_called_once_with("cached/path.png")


@pytest.mark.asyncio
async def test_calculate_error(graph_plotter):
    graph_plotter._call_gemini = AsyncMock(side_effect=Exception("Plot error"))

    with pytest.raises(Exception, match="Plot error"):
        await graph_plotter.calculate("invalid")


@pytest.mark.asyncio
async def test_create_plot_2d(graph_plotter):
    visual_data = {"plot_type": "2d", "x_range": [-5, 5]}
    expression = "x^2"

    with patch("src.modules.graph_plotter.plt") as mock_plt, patch(
        "src.modules.graph_plotter.np"
    ) as mock_np:

        # Mock numpy evaluation
        mock_np.linspace.return_value = [1, 2, 3]
        # We need to mock eval to work with our mocked numpy x
        # But eval is tricky. Let's mock _plot_2d directly if we want to test _create_plot dispatch
        # Or better, let's test _plot_2d logic by mocking what it calls.

        # Let's test _create_plot dispatching
        graph_plotter._plot_2d = AsyncMock(return_value={"png": "path.png"})

        result = await graph_plotter._create_plot(visual_data, expression)
        assert result == {"png": "path.png"}
        graph_plotter._plot_2d.assert_called_once()


@pytest.mark.asyncio
async def test_create_plot_3d(graph_plotter):
    visual_data = {"plot_type": "3d"}
    graph_plotter._plot_3d = AsyncMock(return_value={"png": "path3d.png"})

    result = await graph_plotter._create_plot(visual_data, "expr")
    assert result == {"png": "path3d.png"}
    graph_plotter._plot_3d.assert_called_once()


@pytest.mark.asyncio
async def test_plot_3d_implementation(graph_plotter):
    # Test that it falls back to 2d as per current implementation
    graph_plotter._plot_2d = AsyncMock(return_value={"png": "fallback.png"})
    result = await graph_plotter._plot_3d({}, "expr")
    assert result == {"png": "fallback.png"}
    graph_plotter._plot_2d.assert_called_once()


@pytest.mark.asyncio
async def test_plot_parametric_implementation(graph_plotter):
    graph_plotter._plot_2d = AsyncMock(return_value={"png": "fallback.png"})
    result = await graph_plotter._plot_parametric({}, "expr")
    assert result == {"png": "fallback.png"}
    graph_plotter._plot_2d.assert_called_once()


@pytest.mark.asyncio
async def test_plot_polar_implementation(graph_plotter):
    graph_plotter._plot_2d = AsyncMock(return_value={"png": "fallback.png"})
    result = await graph_plotter._plot_polar({}, "expr")
    assert result == {"png": "fallback.png"}
    graph_plotter._plot_2d.assert_called_once()


def test_load_cached_result_implementation(graph_plotter):
    result = graph_plotter._load_cached_result("path/to/cache.png")
    assert isinstance(result, CalculationResult)
    assert result.visual_data["plot_paths"]["png"] == "path/to/cache.png"
    assert result.result == "Grafik olusturuldu (cache)"


@pytest.mark.asyncio
async def test_plot_2d_exception(graph_plotter):
    visual_data = {"x_range": [-10, 10]}
    expression = "x^2"

    with patch("src.modules.graph_plotter.plt") as mock_plt:
        mock_plt.plot.side_effect = Exception("Matplotlib error")

        from src.utils.exceptions import CalculationError

        with pytest.raises(CalculationError, match="Grafik olusturulamadi"):
            await graph_plotter._plot_2d(visual_data, expression, [-10, 10])


@pytest.mark.asyncio
async def test_plot_2d_implementation(graph_plotter):
    visual_data = {"x_range": [-10, 10]}
    expression = "x**2"

    with patch("src.modules.graph_plotter.plt") as mock_plt:
        # Mock savefig to avoid file creation
        mock_plt.savefig = MagicMock()

        # We need to ensure eval works.
        # The code uses: y = eval(expression, {"__builtins__": {}}, allowed_names)
        # allowed_names has x and numpy functions.

        result = await graph_plotter._plot_2d(visual_data, expression, [-10, 10])

        assert "png" in result
        mock_plt.figure.assert_called()
        mock_plt.plot.assert_called()
        mock_plt.savefig.assert_called()
        mock_plt.close.assert_called()

    @pytest.mark.asyncio
    async def test_plot_2d_error(graph_plotter):
        # Invalid expression that causes eval error
        visual_data = {"x_range": [-10, 10]}
        expression = "invalid syntax"

        with patch("src.modules.graph_plotter.plt") as mock_plt:
            # The code catches Exception, logs warning, and falls back to x^2
            # So it should NOT raise an exception
            result = await graph_plotter._plot_2d(visual_data, expression, [-10, 10])

            assert result is not None
            assert "image_data" in result
            assert "mime_type" in result
