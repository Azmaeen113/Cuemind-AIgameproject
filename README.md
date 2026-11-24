# CueMind: 60-Second Rack Attack Duel

CueMind is an 8-ball pool game where Minimax and Monte Carlo Tree Search
compete on one shared table. The graphical client also supports human-vs-AI,
AI-vs-AI, and headless benchmark matches.

CSE 3210 Artificial Intelligence Lab, Department of CSE, KUET  
Azmaeen Nur Sajin (2207113) · Masumur Rahman Fokrul (2207114)

## Run the game

```bash
pip install -r requirements.txt
python main.py
```

The first launch compiles the physics and AI kernels with numba; later launches
start faster.

## Benchmark without graphics

```bash
python benchmark.py --a Minimax --b MCTS --games 100 --budget 0.6
```

## Controls

| Key / mouse | Action |
|---|---|
| Mouse | Aim |
| Hold left button + drag away | Set power; release to shoot |
| Right click | Cancel the stroke |
| Arrow keys | Fine aim (Shift = faster) |
| Up / Down, Space | Adjust power, shoot |
| Click during ball-in-hand | Place the cue ball (green ring = legal) |
| V | Toggle AI vision lines |
| F | Cycle ball speed |
| P or Esc | Pause |
| M | Mute |
| F11 | Fullscreen |

## Tests

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

## Code map

| Path | Purpose |
|---|---|
| `main.py` | Start the graphical game |
| `game/app.py` | Window, loading screen, and scene transitions |
| `game/config.py` | Table dimensions, physics constants, rules, and colours |
| `game/physics.py` | Fixed-step simulation for ball, cushion, and pocket collisions |
| `game/rules.py` | Scoring, fouls, clocks, turns, and match state |
| `game/shots.py` | Candidate direct, bank, kick, combination, and safety shots |
| `game/planner.py` | A* run-out planner |
| `game/agents/` | Greedy, Minimax, and MCTS agents |
| `game/headless.py` | Matches without graphics |
| `game/scenes/` | Menu, setup, match, results, benchmark, and how-to screens |
| `game/render/` | Table, balls, cue, effects, sound, and UI |
| `assets/images/` | Game artwork |
| `benchmark.py` | Command-line AI-vs-AI benchmark |
| `tests/` | Focused game-rules tests |

## Project deliverables

The [final report](docs/CueMind_Report_final.pdf), [presentation](docs/CueMind_Presentation.pptx),
benchmark data, screenshots and demo videos are collected under [docs/](docs/README.md).
