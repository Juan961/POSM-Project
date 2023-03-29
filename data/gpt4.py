import os

import openai

openai.api_key(os.getenv("OPENAI_API_KEY"))

messages=[
    { "role": "system", "content": "You are a helpful assistant." }
]

def ask_gpt(message):
    messages.append(message)

    message_value = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = messages        
    )

    return message_value
