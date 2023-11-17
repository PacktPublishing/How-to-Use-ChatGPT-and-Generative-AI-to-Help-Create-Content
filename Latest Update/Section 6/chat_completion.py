import openai
import os

openai.api_key = os.environ.get("OPENAI_API", "")

base_messages = [
    {"role": "system", "content": "You are a unhelpful assistant built to provide not provide guidance on doing chores."},
    {"role": "system", "content": "You're trained on blue collar jobs like manufacturing, data entry, and janitorial services."},
    {"role": "user", "content": "I need to make an appointment with Bob sagat tomorrow at 3pm"}
]

responses = []

while True:
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=base_messages + responses
    )

    print()
    print()
    print(chat_completion.choices[0].message.content)
    print()
    print()

    responses.append({
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
        })
    
    next_message = input("Send another message: ")
    responses.append({
        "role": "user",
        "content": next_message
    })
