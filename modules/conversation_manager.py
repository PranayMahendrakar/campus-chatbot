"""Conversation Manager - Manage chat conversations"""
from .base import LlamaClient
class ConversationManager:
    def __init__(self):
        self.client = LlamaClient()
        self.history = []
        self.system_prompt = "You are a friendly campus chatbot assistant."
    def chat(self, message: str) -> str:
        self.history.append(f"User: {message}")
        context = "\n".join(self.history[-10:])
        response = self.client.generate(f"Conversation:\n{context}\n\nRespond helpfully:", self.system_prompt)
        self.history.append(f"Assistant: {response}")
        return response
    def clear_history(self):
        self.history = []
