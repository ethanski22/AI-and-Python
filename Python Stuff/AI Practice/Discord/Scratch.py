import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

env_path = Path("AI Practice/Keys/.env")
load_dotenv(dotenv_path = env_path)

# Key for asure
client = OpenAI(
    base_url = "https://models.inference.ai.azure.com",
    api_key = os.environ.get("GITHUB_TOKEN"),
)

async def sendVoiceMessage(audioFilePath: str, text: str):
    # clear the file
    open(audioFilePath, "w").close()

    open(audioFilePath, "w")

    response = client.audio.speech.create(
        model = "tts-1",
        voice = "echo",
        response_format = "opus",
        input = f"{askForGPT(text)}",
    )

    # Open file and write the response
    # with open(audioFilePath, "wb") as file:
    #     for chunk in response.iter_bytes():
    #         file.write(chunk)

    await response.write_to_file(audioFilePath)


def askForGPT(question):
    response = client.chat.completions.create(
        model =  "gpt-4o",
        messages = [
            {
                "role": "system",
                "content": "This will used to creeate a voice message."
            },
            {
                "role": "user",
                "content": f"{question}"
            }
        ],
        temperature = 1,
        max_tokens = 4096,
        top_p = 1,
    ) 
    return response.choices[0].message.content