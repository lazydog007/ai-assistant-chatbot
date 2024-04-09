import os
import openai
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def chat_with_gpt(prompt):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
  )

  return response.choices[0].message.content.strip()

if __name__ == "__main__":
  while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
      break

    response = chat_with_gpt(user_input)
    print("Bot: " + response)