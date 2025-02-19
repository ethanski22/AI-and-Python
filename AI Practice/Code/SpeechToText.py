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

audio_file = open("speech.mp3", "rb")

transcript = client.audio.transcriptions.create(
  model = "whisper-1",
  file = audio_file,
  language = "en",
  audio_format = "mp3",
  response_format = "text"
)
