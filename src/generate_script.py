import os
from google import genai

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

prompt = """
Create a 45-second Facebook Reel script about:
3 AI tools every student should know

Include:
- Hook
- Main points
- Call to action
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)
