# CueMind project deliverables

This folder contains the team's final project materials. The report and presentation
are final outputs; draft reports and raw capture files are intentionally omitted.

## Final report and presentation

- [Final project report](CueMind_Report_final.pdf) (14 pages).
- [Final presentation](CueMind_Presentation.pptx) (20 slides, with embedded demo clips).

To rebuild the presentation from the checked-in source assets:

```powershell
cd docs/build
npm ci
npm run build
```

The build script resolves media paths relative to this folder and writes
`CueMind_Presentation.pptx` here.

## Benchmarks

The CSVs contain the per-game results summarized in the report. All matches used
the same 0.6-second thinking budget, and the breaker alternated by game.

| Matchup | Games | Wins |
|---|---:|---|
| [Minimax vs MCTS](benchmarks/bench_minimax_mcts.csv) | 20 | Minimax 9, MCTS 11 |
| [Greedy vs Minimax](benchmarks/bench_greedy_minimax.csv) | 10 | Greedy 1, Minimax 9 |
| [Greedy vs MCTS](benchmarks/bench_greedy_mcts.csv) | 10 | Greedy 3, MCTS 7 |

Re-run the same matchups from the repository root with:

```powershell
python benchmark.py --a Minimax --b MCTS --games 20 --budget 0.6
python benchmark.py --a Greedy --b Minimax --games 10 --budget 0.6
python benchmark.py --a Greedy --b MCTS --games 10 --budget 0.6
```

Each run writes `benchmark_results.csv` in the current directory; use `--out` to
choose another destination.

## Screenshots and demo media

The numbered PNGs in [media/](media/) document the menu, setup, match, AI
visualization, results, and benchmark UI. The same folder includes the decision
analysis figures used in the presentation and three compressed demos:

- [AI vs AI match](media/ai_vs_ai_4x_fs.mp4)
- [Human vs AI match](media/human_vs_ai_2x_fs.mp4)
- [UI tour](media/ui_tour_fs.mp4)

The short clips in [media/clips/](media/clips/) are source video for the
presentation. Original raw recordings and intermediate logs are not included.
