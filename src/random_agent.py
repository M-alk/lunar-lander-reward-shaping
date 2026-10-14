"""Step 2: watch a rocket that picks random actions crash.

    python src/random_agent.py --render      # open the game window
    python src/random_agent.py --episodes 100  # headless, just the scores
"""
import argparse

import gymnasium as gym
import numpy as np

OBS_NAMES = [
    "x (left/right of pad)",
    "y (height above pad)",
    "vx (sideways speed)",
    "vy (up/down speed)",
    "angle (tilt, rad)",
    "angular velocity",
    "left leg contact",
    "right leg contact",
]
ACTION_NAMES = ["nothing", "left engine", "main engine", "right engine"]


def print_obs(obs):
    for name, value in zip(OBS_NAMES, obs):
        print(f"  {name:<24} {value:+.3f}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", type=int, default=3)
    parser.add_argument("--render", action="store_true")
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    env = gym.make("LunarLander-v3", render_mode="human" if args.render else None)
    env.action_space.seed(args.seed)

    scores, lengths = [], []
    for ep in range(args.episodes):
        obs, _ = env.reset(seed=args.seed + ep)
        if ep == 0:
            print("First observation:")
            print_obs(obs)

        total, steps, done = 0.0, 0, False
        while not done:
            action = env.action_space.sample()
            obs, reward, terminated, truncated, _ = env.step(action)
            total += reward
            steps += 1
            done = terminated or truncated
            if ep == 0 and steps <= 3:
                print(f"step {steps}: action={ACTION_NAMES[action]}, reward={reward:+.2f}")

        if ep == 0:
            print(f"Last observation (reward on final frame {reward:+.1f}):")
            print_obs(obs)

        scores.append(total)
        lengths.append(steps)
        print(f"episode {ep + 1}: score {total:+.1f} in {steps} frames")

    env.close()
    print(f"\nrandom agent over {args.episodes} episodes: "
          f"mean {np.mean(scores):+.1f} +/- {np.std(scores):.1f}, mean length {np.mean(lengths):.0f} frames")


if __name__ == "__main__":
    main()
