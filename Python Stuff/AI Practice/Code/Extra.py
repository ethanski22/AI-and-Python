import discord
from discord.ext import commands
from gtts import gTTS
import requests
import os
import json
import base64

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def tts(ctx, *, text: str):
    """Generates a TTS voice message and sends it in the text channel."""
    # Generate TTS audio
    tts = gTTS(text=text, lang="en")
    audio_file = "voice_message.ogg"
    tts.save(audio_file)

    # Ensure the audio is in the correct format (ogg with opus codec)
    # You might need to convert the file here if it's not in the correct format

    # Get file size
    file_size = os.path.getsize(audio_file)

    # Request upload URL from Discord
    channel_id = ctx.channel.id
    upload_url = f"https://discord.com/api/v10/channels/{channel_id}/attachments"
    headers = {
        "Authorization": f"Bot {bot.http.token}",
        "Content-Type": "application/json"
    }
    upload_data = {
        "files": [
            {
                "filename": "voice_message.ogg",
                "file_size": file_size,
                "id": "0"
            }
        ]
    }
    response = requests.post(upload_url, headers=headers, data=json.dumps(upload_data))
    if response.status_code != 200:
        await ctx.send("Failed to get upload URL.")
        return

    upload_info = response.json()["attachments"][0]
    upload_url = upload_info["upload_url"]
    upload_filename = upload_info["upload_filename"]

    # Upload the audio file
    with open(audio_file, "rb") as f:
        audio_data = f.read()
    upload_headers = {
        "Authorization": f"Bot {bot.http.token}",
        "Content-Type": "audio/ogg"
    }
    response = requests.put(upload_url, headers=upload_headers, data=audio_data)
    if response.status_code != 200:
        await ctx.send("Failed to upload audio file.")
        return

    # Prepare the payload to send the voice message
    duration_secs = 3  # You can calculate the exact duration if needed
    waveform = base64.b64encode(bytearray([128] * 256)).decode('utf-8')  # Simple flat waveform
    message_payload = {
        "flags": 8192,  # Indicates it's a voice message
        "attachments": [
            {
                "id": "0",
                "filename": "voice_message.ogg",
                "uploaded_filename": upload_filename,
                "duration_secs": duration_secs,
                "waveform": waveform
            }
        ]
    }
    message_url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    message_headers = {
        "Authorization": f"Bot {bot.http.token}",
        "Content-Type": "application/json"
    }
    response = requests.post(message_url, headers=message_headers, data=json.dumps(message_payload))
    if response.status_code != 200:
        await ctx.send("Failed to send voice message.")
        return

    # Clean up the audio file
    os.remove(audio_file)

bot.run("DISCORD_TOKEN")
