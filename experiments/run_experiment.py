from sim.environment import Environment
from agents.random_agent import RandomAgent

def run():
    env = Environment(config={})
    agent = RandomAgent()

    obs = env.reset()

    done = False
    steps = 0

    while not done:
        action = agent.act(obs)
        obs, reward, done, info = env.step(action)
        steps += 1

    print(f"Finished in {steps} steps")

if __name__ == "__main__":
    run()
