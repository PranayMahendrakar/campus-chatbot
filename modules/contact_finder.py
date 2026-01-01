"""Contact Finder - Find department contacts"""
from .base import LlamaClient
class ContactFinder:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You help find appropriate contacts and offices."
    def find_contact(self, query: str, directory: str = "") -> str:
        return self.client.generate(f"Find contact for: {query}\nDirectory: {directory}", self.system_prompt)
