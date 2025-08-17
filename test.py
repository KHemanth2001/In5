from google import genai
from app.prompts import templates
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

def call_gemini(prompt: str):
    client = genai.Client(api_key="AIzaSyDN0UqvbUZgRBpH7m9POgGWR8VVzRHvbf8")

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    return response.text


def generate_short_insight(topic: str) -> str:
    prompt=templates.SHORT_PROMPT_TEMPLATE.format(topic=topic)
    return call_gemini(prompt)


generate_short_insight("devops")