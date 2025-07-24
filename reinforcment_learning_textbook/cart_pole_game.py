import gymnasium as gym


def cartpole():
    environment = gym.make("CartPole-v1", render_mode="rgb_array")
    environment.reset()
    for step in range(50):
        environment.render()
        action = environment.action_space.sample()
        observation, reward, done, info, _ = environment.step(action)
        print(f"step: {step}")
        print(f"action: {action}")
        print(f"observation: {observation}")
        print(f"reward: {reward}")
        print(f"done: {done}")
        print(f"info: {info}")


def main():
    cartpole()


if __name__ == "__main__":
    main()
