from openai import OpenAI
import os

# Use environment variable for API key. Set OPENAI_API_KEY in your environment.
api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    raise RuntimeError('OPENAI_API_KEY environment variable is not set')

client = OpenAI(api_key=api_key)

prompt = "Hello, how are you?"

completion = client.chat.completions.create(
  model="gpt-5.2",
  messages=[
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message.content)
