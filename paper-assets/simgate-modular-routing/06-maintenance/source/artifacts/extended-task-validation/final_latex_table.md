# Extended Task Validation: Final Report

## Part 1: Melt Status

**Status: IN PROGRESS (11/20 episodes)**

- First run crashed with `EngineDeadError` (vllm engine failure)
- Rerun launched: collecting 20 new episodes from scratch (`reuse 0, collect 20 new episodes`)
- Current progress: episodes 0–10 completed (11/20), episode 11 in progress
- Rerun log shows active inference (prompt processing still running)

### Melt Partial Results (11/20)

| Ep | Internal | Det | Label | Signal |
|----|----------|-----|-------|--------|
| 0 | -100 | 0 | D | int_died_det_alive |
| 1 | 0 | 0 | N | tied_alive |
| 2 | 3 | 3 | N | tied_alive |
| 3 | -100 | 3 | D | int_died_det_alive |
| 4 | -100 | 0 | D | int_died_det_alive |
| 5 | -100 | -100 | N | both_dead |
| 6 | 0 | 0 | N | tied_alive |
| 7 | -100 | 0 | D | int_died_det_alive |
| 8 | 0 | 0 | N | tied_alive |
| 9 | -100 | 0 | D | int_died_det_alive |
| 10 | 0 | 0 | N | tied_alive |

Partial stats (11 eps): Int DR=54.5%, Det DR=9.1%, ΔDR=+45.5, D/I/N=5/0/6

---

## Part 2: LaTeX Table (4-task aggregate, melt pending)

```latex
\begin{table}[t]
\centering
\caption{Extended validation: excluded task types ($n{=}20$ episodes each). All four completed tasks show internal DR $\gg$ deterministic DR, consistent with prescreening direction (Table~4). ``D/I/N'' = deterministic-preferred / internal-preferred / no-preference episode counts. \textit{melt} was still running at time of writing.}
\label{tab:extended-validation}
\begin{tabular}{lcccccc}
\toprule
Task Type & $n$ & Int DR & Det DR & $\Delta$DR (pp) & D/I/N \\
\midrule
boil & 20 & 55.0\% & 25.0\% & +30.0 & 6/0/14 \\
find-living-thing & 20 & 55.0\% & 15.0\% & +40.0 & 10/0/10 \\
melt & --- & --- & --- & --- & --- \\
power-component & 20 & 50.0\% & 15.0\% & +35.0 & 7/0/13 \\
use-thermometer & 20 & 50.0\% & 20.0\% & +30.0 & 7/1/12 \\
\midrule
\textbf{Aggregate (4 tasks)} & \textbf{80} & \textbf{52.5\%} & \textbf{18.8\%} & \textbf{+33.8} & \textbf{30/1/49} \\
\bottomrule
\end{tabular}
\end{table}
```

### When melt completes (placeholder for copy-paste update)

If melt final results match partial trend (~55% Int DR, ~10% Det DR), the 5-task table would be:

```latex
\begin{table}[t]
\centering
\caption{Extended validation: excluded task types ($n{=}20$ episodes each). All five tasks show internal DR $\gg$ deterministic DR, consistent with prescreening direction (Table~4). ``D/I/N'' = deterministic-preferred / internal-preferred / no-preference episode counts.}
\label{tab:extended-validation}
\begin{tabular}{lcccccc}
\toprule
Task Type & $n$ & Int DR & Det DR & $\Delta$DR (pp) & D/I/N \\
\midrule
boil & 20 & 55.0\% & 25.0\% & +30.0 & 6/0/14 \\
find-living-thing & 20 & 55.0\% & 15.0\% & +40.0 & 10/0/10 \\
melt & 20 & ??\% & ??\% & +?? & ?/?/? \\
power-component & 20 & 50.0\% & 15.0\% & +35.0 & 7/0/13 \\
use-thermometer & 20 & 50.0\% & 20.0\% & +30.0 & 7/1/12 \\
\midrule
\textbf{Aggregate} & \textbf{100} & \textbf{??\%} & \textbf{??\%} & \textbf{+??} & \textbf{??/??/??} \\
\bottomrule
\end{tabular}
\end{table}
```

---

## Part 3: DAF Calculation

### Formula

$$\text{DAF} = 1 - \frac{\Delta_\text{nd}}{\Delta_\text{full}}$$

where:
- $\Delta_\text{full} = \overline{s^\text{det}} - \overline{s^\text{int}}$ (mean score gap, all episodes)
- $\Delta_\text{nd} = \overline{s^\text{det}|_\text{nd}} - \overline{s^\text{int}|_\text{nd}}$ (mean score gap, non-death subset only — episodes where both strategies survived)

### Per-Task DAF

| Task | $\Delta_\text{full}$ | Non-death $n$ | $\Delta_\text{nd}$ | DAF |
|------|---------------------|---------------|--------------------|----|
| boil | 33.50 | 9 | 0.00 | **1.000** |
| find-living-thing | 41.25 | 9 | 1.89 | **0.954** |
| use-thermometer | 30.60 | 9 | 0.00 | **1.000** |
| power-component | 38.50 | 10 | 0.00 | **1.000** |

### Aggregate DAF (4 tasks, pooled)

- Total episodes: 80
- $\overline{s^\text{int}}$ = -52.11, $\overline{s^\text{det}}$ = -16.15
- $\Delta_\text{full}$ = 35.96
- Non-death episodes: 37/80
- $\overline{s^\text{int}|_\text{nd}}$ = 0.84, $\overline{s^\text{det}|_\text{nd}}$ = 1.30
- $\Delta_\text{nd}$ = 0.46
- **Aggregate DAF = 0.987**

### Interpretation

DAF ≈ 0.99 means **98.7% of the det-vs-internal score gap is attributable to death asymmetry**. In the 37 episodes where both strategies survived, the score difference is negligible (Δ_nd = 0.46 points). The deterministic policy's apparent advantage comes almost entirely from the internal policy dying more often, not from better task completion when both survive.

find-living-thing is the only task with measurable non-death score difference (Δ_nd = 1.89), driven by 2 episodes where det scored higher on score_comparison (eps 2 and 13). Even there, DAF = 0.95.

### Raw Score Breakdown

| Task | Non-death eps | nd_int_mean | nd_det_mean | Δ_nd |
|------|---------------|-------------|-------------|------|
| boil | 9/20 | 0.67 | 0.67 | 0.00 |
| find-living-thing | 9/20 | 1.78 | 3.67 | 1.89 |
| use-thermometer | 9/20 | 1.00 | 1.00 | 0.00 |
| power-component | 10/20 | 0.00 | 0.00 | 0.00 |
| **Pooled** | **37/80** | **0.84** | **1.30** | **0.46** |

---

*Generated 2026-05-19. Melt rerun in progress on westb-13313 (11/20 episodes at time of check).*
