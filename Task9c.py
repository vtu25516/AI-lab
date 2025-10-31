import openai
import gradio

openai.api_key = "sk-..."  # Use your actual API key

messages = [
    {"role": "system", "content": "You are a financial expert that specializes in real estate investment"}
]

def Custom_ChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": chatGPT_reply})
    return chatGPT_reply

demo = gradio.Interface(
    fn=Custom_ChatGPT,
    inputs="text",
    outputs="text",
    title="Intelligent Chatbot"
)

demo.launch(share=True)
