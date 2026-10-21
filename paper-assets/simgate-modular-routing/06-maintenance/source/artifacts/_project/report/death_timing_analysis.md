# SF3 Death Timing Analysis & Mixed Routing Discussion

## 1. Data Source

- **Dataset**: Plan_C evaluation (main paper results)
- **Scale**: 245 episodes across 11 ScienceWorld tasks, 30 steps/episode
- **Death rates**: Internal 42.9% (105/245), Deterministic 16.3% (40/245)

## 2. Death Step Timing Distribution

### Summary Statistics

| Metric | Internal Mode | Deterministic Mode |
|--------|:---:|:---:|
| N (death events) | 105 | 40 |
| Mean step | 18.36 | 21.68 |
| Median step | 17.0 | 22.0 |
| Std dev | 4.66 | 4.33 |
| Min | 9 | 12 |
| Max | 30 | 30 |
| Q1 | 16.0 | 19.0 |
| Q2 (median) | 17.0 | 22.0 |
| Q3 | 20.0 | 24.0 |

**Key finding**: Deterministic deaths occur 3.3 steps later on average (p < 0.001 by Welch's t-test would be expected given the sample sizes and effect size).

### Temporal Distribution (Early / Mid / Late)

| Phase | Steps | Internal | Deterministic |
|-------|:---:|:---:|:---:|
| Early | 0–9 | 2 (1.9%) | 0 (0.0%) |
| Mid | 10–19 | 69 (65.7%) | 12 (30.0%) |
| Late | 20–30 | 34 (32.4%) | 28 (70.0%) |

**Internal deaths are mid-episode concentrated** — the modal death step is 17, with 50% of deaths occurring between steps 16–20 (IQR).

**Deterministic deaths skew late** — 70% occur at step 20+, consistent with the longer survival enabled by score-maximizing action selection.

### Step-by-Step Histogram Data (for figure generation)

```
Step | Internal | Det
   9 |   2      |   0
  10 |   2      |   0
  11 |   3      |   0
  12 |   2      |   1
  13 |   1      |   1
  14 |   6      |   2
  15 |   9      |   1
  16 |  13      |   0
  17 |  17      |   1     ← Internal peak
  18 |   7      |   2
  19 |   9      |   4
  20 |   9      |   0
  21 |   3      |   5
  22 |   3      |   4     ← Det peak zone
  23 |   1      |   6     ← Det peak
  24 |   6      |   5
  25 |   0      |   2
  26 |   4      |   0
  27 |   2      |   2
  28 |   3      |   2
  29 |   1      |   1
  30 |   2      |   1
```

### Per-Task Death Steps

| Task | Internal deaths (steps) | Det deaths (steps) |
|------|---|---|
| chemistry-mix | 9,15,15,15,15,20,20,21,23 | 14,15,21,21,22 |
| find-animal | 13,14,16,17,17,18,21,27,28,30 | 18,19,28,29,30 |
| freeze | 11,14,14,15,16,16,16,17,19,20,29 | 14,21,22,24,24 |
| grow-fruit | 11,16,17,17,18,19,19,24,26 | 17,22,23,25 |
| identify-life-stages-1 | 11,14,15,17,19,19,19,20,24,24,26 | 23,28 |
| identify-life-stages-2 | 14,15,15,16,17,17,18,20,27,28 | 18,19,24,24 |
| inclined-plane-determine-angle | 10,16,16,17,17,17,18,18,19,24,26 | 13,23,23,27 |
| lifespan-longest-lived | 9,14,16,16,17,17,17,17,19,20,22,24,24,28 | 19,22,24,27 |
| lifespan-longest-lived-then-shortest-lived | 10,16,17,19,20,20,21,26,30 | 19,25 |
| measure-melting-point-unknown-substance | 12,12,15,16,16,17,18,18,20,22,22 | 12,21,21,23,23 |

Note: find-non-living-thing has 0 deaths in both modes.

## 3. Mixed Routing Analysis

### Feasibility Assessment: Limited Value

**The data argues against simple mixed routing strategies.** Here's why:

1. **Internal deaths are NOT early-concentrated.** Only 1.9% of internal deaths occur before step 10. The "danger zone" begins at step 10 and peaks at step 16–17. A mixed strategy that switches from deterministic to internal after the first few steps would avoid essentially zero deaths.

2. **The danger zone spans most of the episode.** 66% of internal deaths occur at steps 10–19, which is the middle third of the 30-step episode. To avoid the majority of deaths, a mixed strategy would need to maintain deterministic routing for at least ~20 steps (67% of the episode). At that point, you're essentially running deterministic mode with a brief internal tail — the exploration benefit of internal mode is largely lost.

3. **The right tradeoff is task-level, not step-level.** The death rate asymmetry varies dramatically by task (from 0% in find-non-living-thing to 55% in identify-life-stages-1 for internal). The optimal strategy is to route entire episodes rather than switching mid-episode — which is exactly what SimGate does.

4. **Deterministic mode still dies.** Even deterministic mode has a 16.3% death rate. Mixed routing can reduce but not eliminate deaths. The 3.3-step survival advantage of deterministic mode suggests a marginal benefit from late-episode switching but with diminished returns.

### Quantitative Bound on Mixed Routing Gain

If a mixed strategy used deterministic for steps 0–k and internal for steps k+1–30:
- **k=10**: Prevents ~2% of internal deaths (steps 9–10). Almost no benefit.
- **k=15**: Prevents ~18% of internal deaths (steps 9–15). Moderate benefit, but 15/30 = 50% of steps run in deterministic mode, halving exploration opportunity.
- **k=20**: Prevents ~66% of internal deaths. But 67% of steps are deterministic — at this point the agent barely explores.

The fundamental tension: preventing internal deaths requires deterministic control during precisely the steps where exploration is most needed (mid-episode, when the agent has navigated to relevant objects but hasn't yet performed the critical interactions).

### Discussion Points for Paper

**Recommended framing for Discussion/Future Work:**

> "Death events in internal mode concentrate in the mid-episode phase (steps 10–19; 66% of deaths), coinciding with the period when agents attempt task-critical interactions after initial exploration. This temporal overlap between high-risk actions and task-relevant exploration suggests that simple temporal mixed routing (e.g., deterministic-then-internal switching) offers limited benefit: avoiding the majority of deaths requires deterministic control during precisely the exploration-critical phase. Our task-level routing approach in SimGate sidesteps this tension by selecting the modality for the entire episode based on predicted task characteristics, achieving a 26.6-point score improvement without sacrificing exploration capacity."

> "More sophisticated mixed routing — for example, step-level routing conditioned on the current state's estimated lethality — remains an interesting direction for future work but would require a per-step risk estimator, which is architecturally more complex than SimGate's episode-level router."

## 4. Visualization Spec (for Paper Agent)

### Figure: Death Step Distribution Histogram

**Type**: Side-by-side or overlaid histogram
**X-axis**: Step number (9–30)
**Y-axis**: Number of death events (or density)
**Series**:
- Internal mode (blue/darker, n=105)
- Deterministic mode (orange/lighter, n=40)

**Annotations**:
- Vertical dashed lines at mean death steps (18.4 internal, 21.7 det)
- Shaded band for "mid-episode" (steps 10–19) with label "66% of internal deaths"
- Text annotation: "Δ = 3.3 steps"

**Raw data for plotting**:
```json
{
  "internal_death_steps": [9, 9, 10, 10, 11, 11, 11, 12, 12, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23, 24, 24, 24, 24, 24, 24, 26, 26, 26, 26, 27, 27, 28, 28, 28, 29, 30, 30],
  "det_death_steps": [12, 13, 14, 14, 15, 17, 18, 18, 19, 19, 19, 19, 21, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 25, 25, 27, 27, 28, 28, 29, 30],
  "n_episodes": 245,
  "max_steps": 30,
  "internal_mean": 18.36,
  "det_mean": 21.68
}
```

### Alternative: Cumulative Death Curve

Plot cumulative fraction of deaths by step, showing:
- Internal mode reaches 50% of deaths by step 17, 90% by step 24
- Deterministic mode reaches 50% by step 22, 90% by step 28
- The ~5-step gap in median demonstrates deterministic mode's survival advantage

## 5. Cross-Validation with Plan-005 Summary

Plan-005 analysis (slightly different episode subset) reported:
- Internal: n=79, mean=18.54, median=18, min=10, max=30
- Det: n=36, mean=21.81, median=23, min=12, max=30

Our plan_c results (n=105 int, n=40 det) are consistent: mean difference is 3.2–3.3 steps in both analyses, confirming robustness.
