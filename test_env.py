from env import HealthEnv

env = HealthEnv()

state = env.reset()
print("Patient:", state)

action = "home_care"

next_state, reward, done, info = env.step(action)

print("Reward:", reward)
print("Correct action:", info["correct"])
