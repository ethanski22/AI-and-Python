import os
import requests
import json
import base64
import math
from dotenv import load_dotenv
from pathlib import Path
from GetTime import getOggDuration


env_path = Path("AI Practice\Keys\.env")
load_dotenv(dotenv_path = env_path)

audioFilePath = Path("AI Practice\AudioFiles\output.ogg")
channelId = 1336498123102486619
time = math.ceil(getOggDuration(audioFilePath))

headers = {
    "Authorization": os.environ.get("DISCORD_TOKEN"),
    "Content-Type": "application/json"
}

uploadRequestPayload = {
    "file": [{"filename": "output.ogg"}]
}

uploadUrlResponse = requests.post(
    f"https://discord.com/api/v10/channels/{channelId}/attachments",
    headers = headers,
    json = uploadRequestPayload
)

if uploadUrlResponse.status_code != 200:
    print("Failed to get upload URl: ", uploadUrlResponse.text)
    exit()

uploadData = uploadUrlResponse.json()
uploadUrl = uploadData["attachments"][0]["upload_url"]
uploadFilename = uploadData["attachments"][0]["id"]

with open(audioFilePath, "rb") as file:
    audioData = file.read()

uploadResponse = requests.put(
    uploadUrl,
    headers = {"Content-Type": "audio/ogg"},
    data = audioData
)

if uploadResponse.status_code != 200:
    print("Failed to upload audio file: ", uploadResponse.text)
    exit()

waveform = base64.b64encode(bytearray([128] * 256)).decode("utf-8")

messagePayload = {
    "flags": 8192,
    "attachments": [
        {
            "id": uploadFilename,
            "filename": "output.ogg",
            "uploaded_filename": uploadFilename,
            "duration_secs": time,
            "waveform": waveform
        }
    ],
    "voiceMetadata": {
        "duratino_secs": time,
        "waveform": waveform
    }
}

sendMessageResponse = requests.post(
    f"https://discord.com/api/v10/channels/{channelId}/messages",
    headers = headers,
    json = messagePayload
)

if sendMessageResponse.status_code != 200:
    print("Failed to send voice message: ", sendMessageResponse.text)
else:
    print("Voice message sent.")