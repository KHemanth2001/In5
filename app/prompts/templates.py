# prompts/templates
SHORT_PROMPT_TEMPLATE = """
Act as a subject matter expert and generate a concise blog post introducing the topic: "{topic}".

Output format:
Respond only with valid JSON (no markdown, no backticks), like this:
{{
  "title": "...",
  "content": "...",
  "topics": ["AWS", "Java", "DevOps"]
}}

Content guidelines:
- "topics" should be a list of generic categories the content falls under (e.g., AWS, Java, DevOps).
- If the content fits multiple categories, include them all.
- Keep the explanation simple and clear.
- Use examples if applicable.
- Avoid using headings like 'Introduction' or 'Summary'.
- Keep it flowing like a short blog.
"""

DEEP_DIVE_PROMPT_TEMPLATE = """
Write a comprehensive deep-dive article on the topic: "{topic}".

Return the response as a JSON with three fields:
1. "title" — a descriptive and informative title.
2. "content" — the article body (800–1000 words) meant for someone with basic prior knowledge.
3. "topics" — a list of generic categories the content falls under (e.g., AWS, Java, DevOps). Include multiple if relevant.

Respond only with valid JSON (no markdown, no backticks), like this:
{{
  "title": "...",
  "content": "...",
  "topics": ["AWS", "Java", "DevOps"]
}}

Content guidelines:
- Organize it with logical flow: intro, explanation, examples, comparisons, real-world usage.
- Include code snippets or analogies if relevant.
- Make the content detailed but easy to follow.
- Avoid headings like 'Conclusion' or 'Summary'.
"""
