from typing import Dict
import random

class HealthEnv:
    def _init_(self):
        self.current_case = None

    def reset(self) -> Dict:
        cases = [
            {"symptoms": ["fever"], "severity": "low", "age": 25, "duration": 1},
            {"symptoms": ["fever", "fatigue"], "severity": "medium", "age": 40, "duration": 3},
            {"symptoms": ["chest pain"], "severity": "high", "age": 55, "duration": 1},
        ]
        self.current_case = random.choice(cases)
        return self.current_case

    def step(self, action: str):
        done = True
        reward = 0

        correct_action = self.get_correct_action()

        if action == correct_action:
            reward = 1.0
        elif action == "visit_doctor":
            reward = 0.5
        else:
            reward = -0.5

        return self.current_case, reward, done, {"correct": correct_action}

    def get_correct_action(self):
        if "chest pain" in self.current_case["symptoms"]:
            return "emergency"
        elif self.current_case["severity"] == "medium":
            return "visit_doctor"
        else:
            return "home_care"

    def state(self):
        return self.current_case