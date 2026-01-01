"""Service Recommender - Recommend campus services"""
from .base import LlamaClient
class ServiceRecommender:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You recommend appropriate campus services based on student needs."
    def recommend_services(self, need: str, services_data: str = "") -> str:
        return self.client.generate(f"Recommend services for: {need}\nAvailable: {services_data}", self.system_prompt)
