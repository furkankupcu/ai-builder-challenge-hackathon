import pytest
import asyncio
import time
from unittest.mock import AsyncMock, MagicMock, patch
from src.core.agent import GeminiAgent, RateLimiter
from src.utils.exceptions import GeminiAPIError
from src.config.settings import settings

# --- RateLimiter Tests ---


@pytest.mark.asyncio
async def test_rate_limiter_acquire():
    limiter = RateLimiter(calls_per_minute=600)  # 10 calls per second, 0.1s interval
    start_time = time.time()

    await limiter.acquire()
    await limiter.acquire()

    end_time = time.time()
    # Should be at least 0.1s between calls, but since first call is immediate,
    # the second call waits. Total time should be around 0.1s.
    # However, with 600 calls/min, interval is 0.1s.
    # First acquire: sets last_call_time.
    # Second acquire: waits if needed.
    # Let's test with a slower limiter to be sure.

    limiter = RateLimiter(calls_per_minute=60)  # 1 call per second
    limiter.last_call_time = time.time()

    await limiter.acquire()
    # Should have waited approx 1 second
    assert time.time() - start_time >= 0.9


# --- GeminiAgent Tests ---


@pytest.fixture
def mock_genai():
    with patch("src.core.agent.genai") as mock:
        yield mock


@pytest.fixture
def agent(mock_genai):
    return GeminiAgent(api_key="test_key")


def test_agent_init_no_key():
    with patch("src.config.settings.settings.GEMINI_API_KEY", None):
        with pytest.raises(ValueError, match="GEMINI_API_KEY gerekli"):
            GeminiAgent(api_key=None)


def test_agent_init_success(mock_genai):
    agent = GeminiAgent(api_key="test_key")
    mock_genai.configure.assert_called_with(api_key="test_key")
    assert agent.model is not None


@pytest.mark.asyncio
async def test_generate_with_retry_success(agent):
    mock_response = MagicMock()
    mock_response.text = "Test response"
    agent.model.generate_content_async = AsyncMock(return_value=mock_response)

    response = await agent.generate_with_retry("prompt")
    assert response == "Test response"


@pytest.mark.asyncio
async def test_generate_with_retry_empty_response(agent):
    mock_response = MagicMock()
    mock_response.text = ""  # Empty
    agent.model.generate_content_async = AsyncMock(return_value=mock_response)

    with pytest.raises(GeminiAPIError, match="API hatasi: Bos yanit alindi"):
        await agent.generate_with_retry("prompt", max_retries=1)


@pytest.mark.asyncio
async def test_generate_with_retry_exception_retry(agent):
    mock_response = MagicMock()
    mock_response.text = "Success after retry"

    # Fail once, then succeed
    agent.model.generate_content_async = AsyncMock(
        side_effect=[Exception("Fail"), mock_response]
    )

    response = await agent.generate_with_retry("prompt", max_retries=2)
    assert response == "Success after retry"
    assert agent.model.generate_content_async.call_count == 2


@pytest.mark.asyncio
async def test_generate_with_retry_exception_fail(agent):
    agent.model.generate_content_async = AsyncMock(side_effect=Exception("Fail"))

    with pytest.raises(GeminiAPIError, match="API hatasi: Fail"):
        await agent.generate_with_retry("prompt", max_retries=2)


@pytest.mark.asyncio
async def test_generate_json_response_valid(agent):
    json_str = '{"result": 42, "steps": ["step1"]}'
    agent.generate_with_retry = AsyncMock(return_value=f"Some text {json_str} end")

    result = await agent.generate_json_response("prompt")
    assert result["result"] == 42
    assert result["steps"] == ["step1"]


@pytest.mark.asyncio
async def test_generate_json_response_invalid_json(agent):
    agent.generate_with_retry = AsyncMock(return_value="Not a json")

    result = await agent.generate_json_response("prompt")
    assert result["result"] == "Not a json"
    assert result["confidence_score"] == 0.95


@pytest.mark.asyncio
async def test_generate_json_response_malformed_json(agent):
    # Regex finds {}, but json.loads fails
    agent.generate_with_retry = AsyncMock(return_value="{invalid json}")

    result = await agent.generate_json_response("prompt")
    assert result["result"] == "{invalid json}"
