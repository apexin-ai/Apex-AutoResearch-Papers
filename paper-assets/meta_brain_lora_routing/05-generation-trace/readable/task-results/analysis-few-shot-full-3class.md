# analysis few shot full 3class

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_few-shot-full-3class_20260515T155258_result.json`
- **Structured JSON:** [`7b86a74bdba7ca43be01.json`](../../sessions/7b/7b86a74bdba7ca43be01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results are in. Here's the full analysis:

## 3-class Few-shot Results (Visual / Spatial / Physical)

**Class distribution**: Visual=89, Spatial=32, Physical=30

### K-step Sweep (paligemma_only, mean pooling)

| K | macro-F1 | accuracy | Visual | Spatial | Physical |
|---|----------|----------|--------|---------|----------|
| 1 | 0.978 ± 0.018 | 0.980 | 0.983 | 1.000 | 0.951 |
| 3 | 0.972 ± 0.025 | 0.974 | 0.977 | 1.000 | 0.941 |
| 5 | 0.979 ± 0.017 | 0.980 | 0.983 | 1.000 | 0.954 |
| 10 | 0.958 ± 0.034 | 0.960 | 0.965 | 0.969 | 0.941 |
| all(44) | 0.959 ± 0.039 | 0.960 | 0.965 | 0.967 | 0.945 |

### K=1 Per-layer Breakdown

| Layer | F1 |
|-------|-----|
| paligemma_layer_4 | **0.993** (best) |
| paligemma_layer_6 | 0.993 |
| paligemma_layer_8 | 0.993 |
| paligemma_layer_12 | 0.993 |
| paligemma_layer_14 | 0.986 |
| paligemma_layer_10 | 0.985 |
| paligemma_layer_2 | 0.979 |
| paligemma_layer_16 | 0.978 |
| expert_layer_2 | 0.570 |
| expert_layer_6 | 0.541 |
| expert_layer_14 | 0.506 |
| expert_layer_10 | 0.464 |

### Pooling Strategy (K=1, paligemma_only)

| Pooling | macro-F1 |
|---------|----------|
| **first** | **1.000 ± 0.000** |
| **first_last** | **1.000 ± 0.000** |
| mean | 0.978 ± 0.018 |
| last | 0.979 ± 0.017 |

### ROUTING VERDICT: **GO** — K=1 macro-F1 = 0.978 >> 70% threshold

Key findings:
- **3-class is near-perfectly separable** from just the first replan step's paligemma activations (K=1 F1=0.978). "first" token pooling achieves perfect 1.000 F1.
- **Paligemma layers carry all the signal** (F1=0.979–0.993). Expert layers are near-chance (0.46–0.57), confirming the perturbation type is encoded in the vision backbone, not the action expert.
- **Spatial is the easiest class** (perfect F1 across all K), Physical slightly harder (~0.95).
- More steps don't help — K=1 is best or tied-best, meaning the signal is present from the very first replan point.

---
