"""Hours Checker - Check operating hours"""
from .base import LlamaClient
class HoursChecker:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You provide accurate operating hours information."
    def check_hours(self, facility: str, schedule_data: str = "") -> str:
        return self.client.generate(f"Operating hours for: {facility}\nSchedule: {schedule_data}", self.system_prompt)
