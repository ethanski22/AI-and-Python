from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="echo",
    response_format = "ogg",
    input="Hello world! This is a streaming test.",
)

response.stream_to_file("output.ogg")
