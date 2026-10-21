# analysis sf3 death timing

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sf3-death-timing_20260515T161355_result.json`
- **Structured JSON:** [`17e6f40aa747825767a8.json`](../../sessions/17/17e6f40aa747825767a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected and saved. Here's the structured output:

---

## 1. Death Timing Statistics

| Metric | Internal | Deterministic |
|--------|----------|---------------|
| n deaths | 179 | 55 |
| Mean step | **17.4** | **20.9** |
| Median step | 16.0 | 21.0 |
| Std | 4.1 | 4.1 |
| Range | [8, 29] | [11, 29] |
| Q1/Q2/Q3 | 15/16/19 | 18/21/23 |
| Early (≤10) | 6 (3.4%) | 0 (0%) |
| Mid (11-20) | **140 (78.2%)** | 22 (40.0%) |
| Late (>20) | 33 (18.4%) | **33 (60.0%)** |

**Peak**: Internal deaths spike sharply at **step 16** (55/179 = 31%), suggesting a consistent structural vulnerability around mid-episode.

## 2. Internal vs Deterministic Comparison

- Deterministic deaths occur **~3.5 steps later** on average
- When both modalities die in the same episode (n=50): deterministic dies later in **84%** of cases (42/50), by a mean of 4.6 steps
- Internal-only deaths dominate: 129 episodes vs 5 deterministic-only deaths
- **Death rate asymmetry**: internal 49% vs deterministic 11.7% (from aggregate data)

## 3. Histogram Data

```
Internal (n=179):       Deterministic (n=55):
step  8:   1            step 11:   1
step  9:   3            step 12:   1
step 10:   2            step 14:   2
step 11:   3            step 15:   3
step 12:   2            step 16:   2
step 13:   3            step 17:   3
step 14:  12            step 18:   5
step 15:  22            step 20:   5
step 16: ■55■           step 21:   6
step 17:  12            step 22:  ■8■
step 18:  16            step 23:   6
step 19:  10            step 24:   4
step 20:   5            step 25:   1
step 21:   4            step 26:   2
step 22:   1            step 27:   3
step 23:  10            step 28:   2
step 24:   1            step 29:   1
step 25:   5
step 26:   4
step 27:   5
step 29:   3
```

JSON saved at `results/death_timing_analysis.json`.

## 4. Mixed Routing Discussion Points

**Finding 1: Deaths are mid-episode, not early.** Internal deaths concentrate in steps 14-19 (78% in the 11-20 range), with almost none before step 8. This means the agent has an "exploration phase" (steps 0-10) that is relatively safe regardless of modality, followed by a critical "commitment phase" where action choices become lethal.

**Finding 2: Mixed routing has limited upside because death timing overlaps.** A switching strategy (deterministic for first K steps, then internal) would need K≥15 to avoid even 15% of internal deaths, while simultaneously introducing some deterministic deaths. The optimal switching point analysis shows the net gain is modest for early switches (net +4 at K=10, +22 at K=15), and the large gains at K=18-20 would essentially mean running deterministic for most of the episode — making it indistinguishable from the pure-deterministic baseline.

**Finding 3: The real routing signal is death avoidance, not step-level modality mixing.** The data shows 93/102 det-preferred episodes are due to `death_asymmetry` — internal died, deterministic survived. This is an episode-level binary outcome, not a gradual step-by-step advantage. Lethal candidates appear at mean step 16 and death follows within ~5 steps (median 4), meaning the critical window is narrow. A step-level mixed router would need to predict lethal states ~5 steps in advance, which is harder than the current episode-level routing that simply learns which task-variation combinations are death-prone.

**Conclusion for paper**: Mixed routing is theoretically possible but empirically unnecessary for SF3. The death timing distribution (concentrated mid-episode with sharp peak at step 16) means any practical switching point either catches too few deaths (early switch) or converges to the deterministic baseline (late switch). Episode-level routing already captures 96.4% of oracle decisions; the remaining 3.6% error cases would not be rescued by step-level mixing. This is a strength of our approach: a lightweight episode-level router suffices because death risk is a property of the task-variation pair, not a step-by-step phenomenon.

---
