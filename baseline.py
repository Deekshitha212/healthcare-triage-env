from env import HealthEnv

env = HealthEnv()

total_score = 0
episodes = 5

for i in range(episodes):
    state = env.reset()

    # simple rule-based agent
    if "chest pain" in state["symptoms"]:
        action = "emergency"
    elif state["severity"] == "medium":
        action = "visit_doctor"
    else:
        action = "home_care"

    _, reward, _, info = env.step(action)
    total_score += reward

    print(f"Episode {i+1}")
    print("State:", state)
    print("Action:", action)
    print("Reward:", reward)
    print("Correct:", info["correct"])
    print("------")

print("Final Score:", total_score / episodes)