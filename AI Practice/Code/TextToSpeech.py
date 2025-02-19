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

response = client.audio.speech.create(
    model = "tts-1",
    voice = "echo",
    response_format = "ogg",
    input = "Hello world! This is a streaming test.",
)

# response.stream_to_file("output.ogg")

audioPath = Path("AI Practice\AudioFiles\output.ogg")

# Open file and write the response
with open(audioPath, "wb") as file:
    for chunk in response.iter_bytes():
        file.write(chunk)