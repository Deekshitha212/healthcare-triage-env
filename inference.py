from env import HealthEnv

def main():
    env = HealthEnv()

    print("[START]", flush=True)

    state = env.reset()

    symptoms = state.get("symptoms", [])
    severity = state.get("severity", "low")

    if "chest pain" in symptoms:
        action = "emergency"
    elif severity == "medium":
        action = "visit_doctor"
    else:
        action = "home_care"

    _, reward, _, _ = env.step(action)

    print(f"[STEP] step=1 action={action} reward={reward}", flush=True)
    print(f"[END] task=healthcare_triage score={reward} steps=1", flush=True)

if __name__ == "__main__":
    main()