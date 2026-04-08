from env import HealthEnv

env = HealthEnv()

print("Healthcare Triage System")
print("--------------------------")

# take input from user
symptom = input("Enter your symptom: ")
severity = input("Enter severity (low / medium / high): ")
age = int(input("Enter your age: "))
duration = int(input("Duration in days: "))

# create custom patient case
env.current_case = {
    "symptoms": [symptom],
    "severity": severity,
    "age": age,
    "duration": duration
}

# AI decision
emergency_symptoms = ["chest pain", "breathing problem", "unconscious", "severe bleeding"]
doctor_symptoms = ["fever", "fatigue", "vomiting", "headache", "infection"]

# decision logic
if any(sym in symptom.lower() for sym in emergency_symptoms):
    action = "emergency"

elif any(sym in symptom.lower() for sym in doctor_symptoms):
    action = "visit_doctor"

elif severity == "high":
    action = "visit_doctor"

elif severity == "medium":
    action = "visit_doctor"

else:
    action = "home_care"

# get result
_, reward, _, info = env.step(action)

print("\n AI Decision:", action)
print("Correct Action:", info["correct"])
print("Reward:", reward)