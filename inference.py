import os
from openai import OpenAI
from env import HealthEnv

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
HF_TOKEN = os.getenv("HF_TOKEN", "")
LOCAL_IMAGE_NAME = os.getenv("LOCAL_IMAGE_NAME", "")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)


def main():
    env = HealthEnv()

    print("[START]", flush=True)

    state = env.reset()
    step = 1

    symptoms = state.get("symptoms", [])
    severity = state.get("severity", "low")

    if "chest pain" in symptoms:
        action = "emergency"
    elif severity == "medium":
        action = "visit_doctor"
    else:
        action = "home_care"

    next_state, reward, done, info = env.step(action)

    print(f"[STEP] step={step} action={action} reward={reward}", flush=True)
    print(f"[END] task=healthcare_triage score={reward} steps={step}", flush=True)


if __name__ == "__main__":
    main()