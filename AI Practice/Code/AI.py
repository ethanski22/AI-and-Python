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

# client = OpenAI(
#     api_key = os.environ.get("OPENAI_API_KEY"),
# )


# Key for asure

client = OpenAI(
    base_url = "https://models.inference.ai.azure.com",
    api_key = os.environ.get("GITHUB_TOKEN"),
)


question = input("Ask me a question: ")

response = client.chat.completions.create(
    model =  "gpt-4o",
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": f"{question}"
        }
    ],
    temperature = 1,
    max_tokens = 4096,
    top_p = 1,
) 

# response = client.Completions.create(
#     engine = "gpt-4",
#     prompt = f"Question: {question}\nAnswer: ",
#     store_log = True,
#     max_tokens = 1024,
#     stop = None,
#     temperature = 0.7,
# )

# answer = response.choices[0].text.strip()
# print(answer)

print(response.choices[0].message.content)
