import openai

# Set your API key
openai.api_key = "YOUR_API_KEY"

def send_prompt_to_chatgpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    prompt = "What is the capital of France?"
    response = send_prompt_to_chatgpt(prompt)
    print(response)