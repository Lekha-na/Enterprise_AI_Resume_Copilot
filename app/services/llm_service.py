import logging


from google import genai
from google.genai import types

from app.core.settings import GEMINI_API_KEY, GEMINI_MODEL

logger = logging.getLogger(__name__)


client = genai.Client(api_key=GEMINI_API_KEY)


def ask_gemini(prompt: str, response_schema=None):

    try:
        config = None

        if response_schema:
            config = types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=response_schema,
            )

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=config,
        )

        if response_schema and response.parsed:
            return response.parsed

        return response.text

    except Exception as e:

        logger.exception("Gemini API Error")

        raise RuntimeError(
            "AI service temporarily unavailable. "
            "Please try again later."
        ) from e


if __name__ == "__main__":
    result = ask_gemini(
        "Explain Generative AI in one sentence."
    )

    print(result)