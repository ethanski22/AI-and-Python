import os
import sys
import discord
import requests
from gtts import gTTS
from dotenv import load_dotenv
from discord.ext import commands
from pathlib import Path
sys.path.insert(0, "AI Practice\Code")
from AskAQuestion import askGPT
from TextToSpeech import textToVoice

env_path = Path("AI Practice\Keys\.env")

load_dotenv(dotenv_path=env_path)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix = "/", intents = intents)

# Events
@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server")

@client.command()
async def askChatGPT(ctx, *, arg):
    response = askGPT(arg)
    await ctx.send(response)

@client.event
async def askChatGPTVoice(ctx, *, arg):
    # Generate TTS audio
    tts = gTTS(text=arg, lang="en")
    audio_file = "voice_message.ogg"
    tts.save(audio_file)

    response = textToVoice(arg, audio_file, ctx)
    await ctx.send(response)

    os.remove(audio_file)

# Use to send a message to a specific channel
# @client.event
# async def on_member_join(member):
#     channel = client.get_channel(1336498123102486619)
#     await channel.send(f"{member} has joined the server")

@client.event
async def on_member_remove(member):
    print(f"{member} has left the server")

# Commands
@client.command(name = "hello")
async def hello(ctx):
    await ctx.send("Hello there")

@client.command(name = "ping")
async def ping(ctx):
    await ctx.send("pong")

# Embeds
@client.command(name = "embed")
async def embed(ctx):
    embed = discord.Embed(
        title = "Title",
        description = "This is a description",
        color = discord.Color.blue()
    )

    embed.set_footer(text = "This is a footer")
    embed.set_image(url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
    embed.set_thumbnail(url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
    embed.set_author(name = "Author", icon_url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
    embed.add_field(name = "Field Name", value = "Field Value", inline = False)
    embed.add_field(name = "Field Name", value = "Field Value", inline = False)

    await ctx.send(embed = embed)


client.run(os.environ.get("DISCORD_TOKEN"))
