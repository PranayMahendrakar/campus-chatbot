"""Emergency Info - Provide emergency information"""
from .base import LlamaClient
class EmergencyInfo:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You provide critical emergency information clearly."
    def get_emergency_info(self, emergency_type: str) -> str:
        return self.client.generate(f"Emergency information for: {emergency_type}\n\nProvide: Emergency contacts, Procedures, Resources", self.system_prompt)
