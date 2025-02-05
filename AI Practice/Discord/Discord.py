import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from pathlib import Path

env_path = Path("AI Practice\Keys\.env")

load_dotenv(dotenv_path=env_path)

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = "/", intents = intents)

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command(name = "hello")
async def hello(ctx):
    await ctx.send("Hello there")

client.run(os.environ.get("DISCORD_TOKEN"))
