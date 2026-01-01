"""FAQ Handler - Handle frequently asked questions"""
from .base import LlamaClient
class FAQHandler:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You answer common campus questions accurately."
    def answer_faq(self, question: str, faq_data: str = "") -> str:
        return self.client.generate(f"Answer: {question}\nFAQ database: {faq_data}", self.system_prompt)
