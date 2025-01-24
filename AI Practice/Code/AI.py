import os
from dotenv import load_dotenv
import openai

# Load the .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set your API key
openai.api_key = OPENAI_API_KEY

