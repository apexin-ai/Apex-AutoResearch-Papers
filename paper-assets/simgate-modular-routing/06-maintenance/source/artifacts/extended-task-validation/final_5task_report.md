# Extended Task Validation — Final 5-Task Report

**Date:** 2026-05-20
**Status:** DONE (all 5 tasks × 20 episodes = 100 episodes complete)

## Per-Task Results

| Task | n | Int DR | Det DR | ΔDR (pp) | D | I | N | DAF |
|------|---|--------|--------|----------|---|---|---|-----|
| boil | 20 | 55.0% | 25.0% | +30.0 | 6 | 0 | 14 | 1.000 |
| find-living-thing | 20 | 55.0% | 15.0% | +40.0 | 10 | 0 | 10 | 0.954 |
| melt | 20 | 45.0% | 20.0% | +25.0 | 7 | 2 | 11 | 1.000 |
| power-component | 20 | 50.0% | 15.0% | +35.0 | 7 | 0 | 13 | 1.000 |
| use-thermometer | 20 | 50.0% | 20.0% | +30.0 | 7 | 1 | 12 | 1.000 |
| **Aggregate** | **100** | **51.0%** | **19.0%** | **+32.0** | **37** | **3** | **60** | **0.991** |

## Melt Detailed Breakdown (new)

- 20 episodes, 20 variations
- Internal deaths: 9 episodes (45%) — episodes 0,3,4,5,7,9,12,15,18
- Det deaths: 4 episodes (20%) — episodes 5,16,17,18
- Both-alive episodes: 9 (scores tied in all 9 → delta_nd = 0)
- Both-dead episodes: 2 (episodes 5, 18)
- Internal-preferred: 2 (episodes 16, 17 — det died, int survived)
- Det-preferred: 7 (all int_died_det_alive)
- DAF = 1 - 0/25 = 1.000

## Aggregate Summary

- **Death rate gap is robust across all 5 tasks**: internal routing consistently dies 2–3× more than deterministic
- **ΔDR range**: +25 to +40 pp (mean +32.0 pp)
- **Preference strongly favors deterministic**: D=37 vs I=3 (12.3:1 ratio)
- **DAF ≈ 1.0 across all tasks**: performance gap is almost entirely explained by death-rate asymmetry; when both agents survive, scores are near-identical
- **melt shows the first meaningful I count** (I=2), both from det_died_int_alive — but D still dominates 7:2

## LaTeX Table

```latex
\begin{table}[t]
\centering
\caption{Extended task validation across 5 ScienceWorld task types (20 episodes each). Int/Det DR = death rate for internal/deterministic routing. $\Delta$DR = Int DR $-$ Det DR in percentage points. D/I/N = episodes where deterministic/internal/neither is preferred. DAF = Death Attribution Fraction.}
\label{tab:extended-validation}
\begin{tabular}{lcccccc}
\toprule
Task Type & $n$ & Int DR & Det DR & $\Delta$DR (pp) & D/I/N & DAF \\
\midrule
boil              & 20 & 55.0\% & 25.0\% & +30.0 & 6/0/14  & 1.000 \\
find-living-thing & 20 & 55.0\% & 15.0\% & +40.0 & 10/0/10 & 0.954 \\
melt              & 20 & 45.0\% & 20.0\% & +25.0 & 7/2/11  & 1.000 \\
power-component   & 20 & 50.0\% & 15.0\% & +35.0 & 7/0/13  & 1.000 \\
use-thermometer   & 20 & 50.0\% & 20.0\% & +30.0 & 7/1/12  & 1.000 \\
\midrule
\textbf{Aggregate} & \textbf{100} & \textbf{51.0\%} & \textbf{19.0\%} & \textbf{+32.0} & \textbf{37/3/60} & \textbf{0.991} \\
\bottomrule
\end{tabular}
\end{table}
```

## Result Files

Server: `westb-13313:/root/autodl-tmp/simgate-modular-routing/results/extended_task_validation/`
- `boil/` — episodes.jsonl, episode_summary.jsonl, labeled_steps.jsonl
- `find-living-thing/` — same structure
- `melt/` — same structure + collection_meta.json
- `power-component/` — same structure
- `use-thermometer/` — same structure
