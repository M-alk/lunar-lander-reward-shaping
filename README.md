# Lunar Lander: reward shaping with PPO

Teaching an agent to land a rocket with reinforcement learning, then changing the reward to see what it learns instead.

Work in progress.

## Setup

Python 3.10+.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/check_install.py
```

If the Box2D install fails with an error about `swig`, run `pip install swig` (or `brew install swig`) and install again.

## 1. A random rocket

```bash
python src/random_agent.py --render
python src/random_agent.py --episodes 100
```

Each frame the agent gets 8 numbers (position, velocity, tilt, spin, two leg contacts) and picks one of 4 actions (nothing, left engine, main engine, right engine). Picking actions at random, the rocket tumbles and crashes after about 90 frames:

| Agent | Mean score (100 episodes) |
|---|---|
| Random | -192 +/- 114 |
