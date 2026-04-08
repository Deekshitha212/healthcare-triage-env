from tasks import tasks
from grader import grade

# simulate agent decision
def agent_decision(case):
    if "chest pain" in case["symptoms"]:
        return "emergency"
    elif case["severity"] == "medium":
        return "visit_doctor"
    else:
        return "home_care"

for level, task in tasks.items():
    print(f"\nTask Level: {level}")

    for case in task["cases"]:
        action = agent_decision(case)
        score = grade(action, task["expected"])

        print("Case:", case)
        print("Action:", action)
        print("Score:", score)