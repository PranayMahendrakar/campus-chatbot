"""Policy Explainer - Explain campus policies"""
from .base import LlamaClient
class PolicyExplainer:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You explain campus policies clearly and helpfully."
    def explain_policy(self, query: str, policies: str = "") -> str:
        return self.client.generate(f"Explain policy about: {query}\nPolicies: {policies}", self.system_prompt)
