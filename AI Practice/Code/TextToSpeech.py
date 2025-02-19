from openai import OpenAI
from pathlib import Path

client = OpenAI()

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