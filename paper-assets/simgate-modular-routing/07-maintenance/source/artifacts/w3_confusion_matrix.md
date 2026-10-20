# W3: 1.7B Router Per-Class Confusion Matrix

Model: `plan-008-v4-1_7b-seed42` (Qwen3-1.7B + LoRA)
Eval: 15% episode-stratified val split (seed=42), greedy decoding
Val set: 300 steps across 10 episodes (6 death, 4 non-death)

## 1. Overall Confusion Matrix

### All Val Data
n = 300 steps, true dist: det=270, int=30

| | Pred: deterministic | Pred: internal |
|---|---:|---:|
| **True: deterministic** | 177 | 93 |
| **True: internal** | 15 | 15 |

| Class | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| deterministic | 0.9219 | 0.6556 | 0.7662 | 270 |
| internal | 0.1389 | 0.5000 | 0.2174 | 30 |

Accuracy = 0.6400, Balanced Accuracy = 0.5778

## 2. Death vs Non-Death Split

Death episodes = internal agent scored -100 (died via `focus on [wrong object]`).
In death episodes, ALL steps are labeled deterministic (det outperforms by 100+ points).

### Death Episodes
n = 180 steps, true dist: det=180, int=0

| | Pred: deterministic | Pred: internal |
|---|---:|---:|
| **True: deterministic** | 120 | 60 |
| **True: internal** | 0 | 0 |

| Class | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| deterministic | 1.0000 | 0.6667 | 0.8000 | 180 |
| internal | 0.0000 | 0.0000 | 0.0000 | 0 |

Accuracy = 0.6667, Balanced Accuracy = 0.6667

### Non-Death Episodes
n = 120 steps, true dist: det=90, int=30

| | Pred: deterministic | Pred: internal |
|---|---:|---:|
| **True: deterministic** | 57 | 33 |
| **True: internal** | 15 | 15 |

| Class | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| deterministic | 0.7917 | 0.6333 | 0.7037 | 90 |
| internal | 0.3125 | 0.5000 | 0.3846 | 30 |

Accuracy = 0.6000, Balanced Accuracy = 0.5667

## 3. Per-Task Summary

| Task Type | N | Acc | Bal Acc | Det P | Det R | Int P | Int R | Death Steps |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| find-animal | 30 | 0.533 | 0.533 | 1.000 | 0.533 | 0.000 | 0.000 | 30 |
| find-non-living-thing | 90 | 0.633 | 0.633 | 1.000 | 0.633 | 0.000 | 0.000 | 0 |
| grow-fruit | 30 | 0.833 | 0.833 | 1.000 | 0.833 | 0.000 | 0.000 | 30 |
| identify-life-stages-2 | 30 | 0.433 | 0.433 | 1.000 | 0.433 | 0.000 | 0.000 | 30 |
| inclined-plane-determine-angle | 30 | 0.800 | 0.800 | 1.000 | 0.800 | 0.000 | 0.000 | 30 |
| lifespan-longest-lived | 30 | 0.700 | 0.700 | 1.000 | 0.700 | 0.000 | 0.000 | 30 |
| lifespan-longest-lived-then-shortest-lived | 30 | 0.500 | 0.500 | 0.000 | 0.000 | 1.000 | 0.500 | 0 |
| measure-melting-point-unknown-substance | 30 | 0.700 | 0.700 | 1.000 | 0.700 | 0.000 | 0.000 | 30 |

## 4. Key Findings

1. **Death episode routing accuracy**: 0.6667 vs non-death: 0.6000 (delta = +0.0667)

2. **Death episodes are all-deterministic ground truth** (180/180 steps). Router predicts deterministic on 120/180 steps (det recall = 0.6667).

3. **Internal class performance**: On non-death episodes, internal recall = 0.5000, precision = 0.3125. The router's ability to identify internal-preferred steps is concentrated in non-death episodes.

4. **Prediction bias**: Router predicts deterministic at 66.7% rate on death episodes vs 60.0% on non-death episodes.
