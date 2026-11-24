# CueMind: AI Game Core

CueMind is an 8-ball pool game with Minimax and Monte Carlo Tree Search
opponents. This branch contains the game rules, physics, shot planning, AI
agents, and headless benchmark runner. The graphical client, rendering layer,
scenes, and image assets are being contributed separately.

CSE 3210 Artificial Intelligence Lab, Department of CSE, KUET  
Azmaeen Nur Sajin (2207113) · Masumur Rahman Fokrul (2207114)

## Setup

```bash
pip install -r requirements.txt
```

Run the headless benchmark:

```bash
python benchmark.py --a Minimax --b MCTS --games 100 --budget 0.6
```

Run the tests:

```bash
python -m unittest discover -v
```

The physics and AI kernels use numba when available and fall back to regular
Python otherwise.

## Rules

| Rule | Detail |
|---|---|
| Table | Both players share one table |
| Clock | 60 s each, runs while that player thinks and aims |
| Points | Any ball 1, the 8-ball 3 |
| Foul | Scratch or no contact: −1 point, −5 s, rival gets ball-in-hand |
| Turn | Pot a ball without a foul and you shoot again |
| End | Table clear, or both clocks at zero. Higher score wins; ties use remaining clock |

## Core code map

| Path | Purpose |
|---|---|
| `game/config.py` | Table dimensions, physics constants, rules, and colours |
| `game/physics.py` | Fixed-step simulation for ball, cushion, and pocket collisions |
| `game/rules.py` | Scoring, fouls, clocks, turns, and match state |
| `game/shots.py` | Candidate direct, bank, kick, combination, and safety shots |
| `game/planner.py` | A* run-out planner |
| `game/agents/` | Greedy, Minimax, and MCTS agents |
| `game/headless.py` | Matches without graphics |
| `benchmark.py` | Command-line AI-vs-AI benchmark |
| `tests/` | Focused game-rules tests |
