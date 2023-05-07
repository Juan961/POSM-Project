import os

import openai

openai.api_key(os.getenv("OPENAI_API_KEY"))

messages = [
    { "role": "system", "content": "You are a helpful assistant." }
]

def ask_gpt(messages):
    message_value = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = messages
    )

    return message_value["choices"][0]["message"]["content"]

if __name__ == "__main__":
    continue_ask = True

    while continue_ask:
        message = input("User: ")
        messages.append( { "role": "user", "content": message })
        
        response = ask_gpt(messages)

        print(f"System: { response }")

        messages.append( { "role": "system", "content": response })
