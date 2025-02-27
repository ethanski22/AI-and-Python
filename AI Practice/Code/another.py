import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

# Specify the path to the .env file
env_path = Path("AI Practice\Keys\.env")

# Load the .env file
load_dotenv(dotenv_path=env_path)

# Key for asure
client = OpenAI(
    base_url = "https://models.inference.ai.azure.com",
    api_key = os.environ.get("GITHUB_TOKEN"),
)

filePath = Path("AI Practice\AudioFiles\output.ogg")

response = client.audio.speech.create(
    model = "tts-1",
    voice = "echo",
    response_format = "ogg",
    input = "Hello world! This is a streaming test."
)

response.write("output.ogg")

def TTS(arg, audioFile):
    text = askGPT(arg)
    response = client.audio.speech.create(
        model = "tts-1",
        input = text,
        voice = "echo",
        response_format = "opus",
        speed = 1.0
    )

    response.write(audioFile)
    return response

def askGPT(question):
    response = client.chat.completions.create(
        model =  "gpt-4o",
        messages = [
            {
                "role": "system",
                "content": "This response is going to be converted to speech."
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