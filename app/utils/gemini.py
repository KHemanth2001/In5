# utils/gemini.py

from google import genai


import json

def call_gemini(prompt: str):
    client = genai.Client(api_key="AIzaSyBFOMWtGCbG3lME5Qn7CHmECe4VJ8xzHf4")

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )

    raw_text = response.text.strip()

    # Remove code block fences if present
    if raw_text.startswith("```json") or raw_text.startswith("```"):
        raw_text = raw_text.strip("`").strip("json").strip()

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError as e:
        print("Failed to parse response as JSON:", e)
        print("Raw response:", raw_text)
        return {}



