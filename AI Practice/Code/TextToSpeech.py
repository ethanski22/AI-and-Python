import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
from gtts import gTTS
import requests
import json
import base64


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

async def textToVoice(text, audioFile, ctx):
    response = client.audio.speech.create(
        model = "tts-1",
        voice = "echo",
        response_format = "ogg",
        input = text,
    )

    audioPath = Path("AI Practice\AudioFiles\output.ogg")

    # Open file and write the response
    with open(audioPath, "wb") as file:
        for chunk in response.iter_bytes():
            file.write(chunk)

    fileSize = os.path.getsize(audioFile)

    channelId = ctx.channel.id
    uploadUrl = f"https://discord.com/api/v10/channels/{channelId}/attachments"
    headers = {
        "Authorization": os.environ.get("DISCORD_TOKEN"),
        "Content-Type": "application/json"
    }
    uploadData = {
        "files": [
            {
                "filename": "voice_message.ogg",
                "file_size": fileSize,
                "id": "0"
            }
        ]
    }

    response = requests.post(uploadUrl, headers=headers, data=json.dumps(uploadData))
    if response.status_code != 200:
        return "Failed to get upload URL."
    
    uploadInfo = response.json()["attachments"][0]
    uploadUrl = uploadInfo["uploadUrl"]
    uploadFilename = uploadInfo["uploadFilename"]

    with open(audioFile, "rb") as f:
        audioData = f.read()

    uploadHeaders = {
        "Authorization": os.environ.get("DISCORD_TOKEN"),
        "Content-Type": "audio/ogg"
    }

    response = requests.put(uploadUrl, headers=uploadHeaders, data=audioData)
    if response.status_code != 200:
        return "Failed to upload audio file."
    
    # Prepare the payload to send the voice message
    durationSecs = 10  # You can calculate the exact duration if needed
    waveform = base64.b64encode(bytearray([128] * 256)).decode('utf-8')  # Simple flat waveform
    message_payload = {
        "flags": 8192,  # Indicates it's a voice message
        "attachments": [
            {
                "id": "0",
                "filename": "voice_message.ogg",
                "uploaded_filename": uploadFilename,
                "duration_secs": durationSecs,
                "waveform": waveform
            }
        ]
    }

    message_url = f"https://discord.com/api/v10/channels/{channelId}/messages"
    message_headers = {
        "Authorization": os.environ.get("DISCORD_TOKEN"),
        "Content-Type": "application/json"
    }

    response = requests.post(message_url, headers=message_headers, data=json.dumps(message_payload))
    if response.status_code != 200:
        await ctx.send("Failed to send voice message.")
        return

    return file
