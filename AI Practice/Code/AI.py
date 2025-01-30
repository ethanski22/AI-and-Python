import os
from dotenv import load_dotenv
import openai
from openai import OpenAI
from pathlib import Path

# Specify the path to the .env file
env_path = Path("AI Practice\Keys\.env")

# Load the .env file
load_dotenv(dotenv_path=env_path)

#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set your API key
#openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

response = client.chat.completions.create(
    model =  "gpt-3.5-turbo-instruct",
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "How do I count cards in blackjack"
        }
    ]
)

question = input("Ask me a question: ")

response = client.Completions.create(
    engine = "gpt-4",
    prompt = f"Question: {question}\nAnswer: ",
    max_tokens = 1024,
    stop = None,
    temperature = 0.7,
)
answer = response.choices[0].text.strip()
print(answer)

print(response.choices[0].message.content)
