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


def askGPT(question):
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
    return response.choices[0].message.content