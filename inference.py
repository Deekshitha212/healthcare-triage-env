from env import HealthEnv

def main():
    env = HealthEnv()

    print("[START] task=healthcare_triage", flush=True)

    state = env.reset()

    step = 1

    if state["severity"] == "high":
        action = "emergency"
    elif state["severity"] == "medium":
        action = "doctor"
    else:
        action = "rest"

    next_state, reward, done, info = env.step(action)

    # ✅ ONLY THIS STEP PRINT
    print(f"[STEP] step={step} reward={reward}", flush=True)

    print(f"[END] task=healthcare_triage score={reward} steps={step}", flush=True)


if __name__ == "__main__":
    main()