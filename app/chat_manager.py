from app.gemini_client import start_chat, send_message

class ChatManager:
    def __init__(self):
        self.chat = start_chat()

    def send(self, user_input):
        return send_message(self.chat, user_input)

    def reset(self):
        self.chat = start_chat()
        print("Chat history cleared. Starting fresh!\n")