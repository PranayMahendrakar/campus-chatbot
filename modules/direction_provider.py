"""Direction Provider - Provide campus directions"""
from .base import LlamaClient
class DirectionProvider:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You provide clear directions around campus."
    def get_directions(self, start: str, destination: str, campus_map: str = "") -> str:
        return self.client.generate(f"Directions from {start} to {destination}\nCampus map: {campus_map}", self.system_prompt)
