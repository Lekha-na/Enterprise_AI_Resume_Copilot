import os

from dotenv import load_dotenv, find_dotenv
from google import genai
from google.genai import types


env_path = find_dotenv()
load_dotenv(env_path)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is not configured. "
        "Please add it to your .env file."
    )

client = genai.Client(api_key=api_key)


def ask_gemini(prompt: str, response_schema=None):

    try:
        config = None

        if response_schema:
            config = types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=response_schema,
            )

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
            config=config,
        )

        if response_schema and response.parsed:
            return response.parsed

        return response.text

    except Exception as e:

        print(f"Gemini API Error: {e}")

        raise RuntimeError(
            "AI service temporarily unavailable. "
            "Please try again later."
        ) from e


if __name__ == "__main__":
    result = ask_gemini(
        "Explain Generative AI in one sentence."
    )

    print(result)