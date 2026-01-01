"""Resource Finder - Find campus resources"""
from .base import LlamaClient
class ResourceFinder:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You are a helpful campus assistant who knows all campus resources."
    def find_resource(self, query: str, campus_info: str = "") -> str:
        return self.client.generate(f"Help find campus resource for: {query}\nCampus info: {campus_info}", self.system_prompt)
