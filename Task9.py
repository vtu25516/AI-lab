# a. Simple ChatGPT using OpenAI
# First, install OpenAI package: pip install openai

import openai

openai.api_key = "sk-..."  # Your actual OpenAI API key goes here

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Give me 3 ideas that I could build using openai apis"}
    ]
)

print(completion.choices[0].message['content'])
