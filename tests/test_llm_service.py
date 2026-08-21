import pytest

from app.services import llm_service


def test_ask_gemini_handles_api_error(monkeypatch):

    def mock_generate_content(*args, **kwargs):
        raise Exception("Gemini API failure")

    monkeypatch.setattr(
        llm_service.client.models,
        "generate_content",
        mock_generate_content,
    )

    with pytest.raises(RuntimeError) as exc_info:
        llm_service.ask_gemini("Test prompt")

    assert str(exc_info.value) == (
        "AI service temporarily unavailable. "
        "Please try again later."
    )


def test_ask_gemini_returns_parsed_response(monkeypatch):

    class MockResponse:
        parsed = {
            "result": "success"
        }
        text = '{"result": "success"}'

    def mock_generate_content(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(
        llm_service.client.models,
        "generate_content",
        mock_generate_content,
    )

    result = llm_service.ask_gemini(
        "Test prompt",
        response_schema={"type": "object"},
    )

    assert result == {
        "result": "success"
    }


def test_ask_gemini_returns_text_response(monkeypatch):

    class MockResponse:
        parsed = None
        text = "Gemini response"

    def mock_generate_content(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(
        llm_service.client.models,
        "generate_content",
        mock_generate_content,
    )

    result = llm_service.ask_gemini("Test prompt")

    assert result == "Gemini response"