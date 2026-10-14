"""Step 1: confirm the three libraries import and the environment exists."""
import gymnasium as gym
import stable_baselines3
import torch


def main():
    print(f"gymnasium          {gym.__version__}")
    print(f"stable-baselines3  {stable_baselines3.__version__}")
    print(f"torch              {torch.__version__}")

    env = gym.make("LunarLander-v3")
    print(f"LunarLander-v3 ok: obs={env.observation_space.shape}, actions={env.action_space.n}, "
          f"max steps={env.spec.max_episode_steps}")
    env.close()


if __name__ == "__main__":
    main()
