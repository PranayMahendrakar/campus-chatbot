"""Event Informer - Provide event information"""
from .base import LlamaClient
class EventInformer:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You provide information about campus events."
    def get_events(self, query: str, events_data: str = "") -> str:
        return self.client.generate(f"Provide event info for: {query}\nEvents: {events_data}", self.system_prompt)
