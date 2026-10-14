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
