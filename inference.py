from env import HealthEnv

def run():
    env = HealthEnv()

    print("[START] task=healthcare_triage", flush=True)

    state = env.reset()
    print(f"[STEP] step=1 state={state}", flush=True)

    # simple logic (same as baseline)
    if state["severity"] == "high":
        action = "emergency"
    elif state["severity"] == "medium":
        action = "doctor"
    else:
        action = "rest"

    _, reward, done, info = env.step(action)

    print(f"[STEP] step=1 action={action} reward={reward}", flush=True)

    print(f"[END] task=healthcare_triage score={reward} steps=1", flush=True)


if __name__ == "__main__":
    run()