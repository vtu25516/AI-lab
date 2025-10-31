import openai

openai.api_key = "sk-..."  # Use your actual API key

messages = []

system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})
print("Your new assistant is ready! Type your query!")

while True:
    user_msg = input()
    if user_msg.lower() == "quit()":
        break
    messages.append({"role": "user", "content": user_msg})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    print(reply)
    messages.append({"role": "assistant", "content": reply})
