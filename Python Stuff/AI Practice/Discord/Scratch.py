import os
import requests
import aiohttp
import json
import base64
import math
from dotenv import load_dotenv
from pathlib import Path
from GetTime import getOggDuration

env_path = Path("AI Practice/Keys/.env")
load_dotenv(dotenv_path = env_path)

async def voiceMessage(ctx, audioFilePath: str, channelId: int):
    time = math.ceil(getOggDuration(audioFilePath))

    