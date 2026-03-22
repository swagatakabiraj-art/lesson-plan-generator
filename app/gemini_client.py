from google import genai
from google.genai import types
from config.settings import GEMINI_API_KEY
from app.lesson_prompt import SYSTEM_PROMPT

client = genai.Client(api_key=GEMINI_API_KEY)

def start_chat():
    return client.chats.create(
        model="gemini-2.5-pro",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        )
    )

def send_message(chat, user_input):
    response = chat.send_message(user_input)
    return response.text