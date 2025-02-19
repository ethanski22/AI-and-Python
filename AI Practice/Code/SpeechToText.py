from openai import OpenAI

client = OpenAI()

audio_file = open("speech.mp3", "rb")

transcript = client.audio.transcriptions.create(
  model = "whisper-1",
  file = audio_file,
  language = "en",
  audio_format = "mp3",
  response_format = "text"
)
