# eval exp4 vanilla 3seed perturbation

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp4-vanilla-3seed-perturbation_20260518T114621_result.json`
- **Structured JSON:** [`bef523d7206c05e4f646.json`](../../sessions/be/bef523d7206c05e4f646.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Part A: Vanilla 3-seed DD OOD Perturbation

| K | Clean (mean±std) | Perturbed (mean±std) | Delta (mean±std) |
|---|---|---|---|
| k1 | 0.6283±0.0376 | 0.5602±0.0283 | **-0.0681±0.0109** |
| k2 | 0.4824±0.0375 | 0.4829±0.0318 | +0.0004±0.0236 |
| k3 | 0.3889±0.0267 | 0.3961±0.0344 | +0.0072±0.0193 |
| k5 | 0.3472±0.0264 | 0.3463±0.0439 | -0.0009±0.0201 |
| full | 0.3123±0.0263 | 0.3394±0.0549 | +0.0271±0.0299 |

Vanilla shows consistent K1 degradation under perturbation (-6.8 pp), but overall performance is poor (F1 ~0.28-0.63) regardless of perturbation.

## Part B: McNemar Tests on Perturbed DD OOD

**K=1:**

| Comparison | Seed | b | c | p-value | Dir |
|---|---|---|---|---|---|
| 9class vs vanilla | 42 | 56 | 0 | <0.001* | 9class |
| 9class vs vanilla | 123 | 50 | 0 | <0.001* | 9class |
| 9class vs vanilla | 456 | 49 | 1 | <0.001* | 9class |
| 9class vs jb_mlm | 42 | 0 | 0 | 1.0 | tie |
| 9class vs jb_mlm | 123 | 4 | 0 | 0.125 | n.s. |
| 9class vs jb_mlm | 456 | 4 | 1 | 0.375 | n.s. |
| 9class vs scrambled | 42 | 2 | 0 | 0.5 | n.s. |
| 9class vs scrambled | 123 | 0 | 0 | 1.0 | tie |
| 9class vs scrambled | 456 | 0 | 1 | 1.0 | n.s. |

**K=Full:**

| Comparison | Seed | b | c | p-value | Dir |
|---|---|---|---|---|---|
| 9class vs vanilla | 42 | 78 | 0 | <0.001* | 9class |
| 9class vs vanilla | 123 | 73 | 0 | <0.001* | 9class |
| 9class vs vanilla | 456 | 67 | 0 | <0.001* | 9class |
| 9class vs jb_mlm | 42 | 0 | 0 | 1.0 | tie |
| 9class vs jb_mlm | 123 | 1 | 0 | 1.0 | n.s. |
| 9class vs jb_mlm | 456 | 19 | 0 | **4e-06*** | 9class |
| 9class vs scrambled | all | 0 | 0 | 1.0 | tie |

**Summary:**
- **9class vs vanilla**: Highly significant across all seeds and K values (p<0.001). 9class dominates with 49-78 discordant samples in its favor.
- **9class vs jb_mlm**: Not significant at K=1. At K=Full, seed456 shows significant difference (b=19, p=4e-06), other seeds tied.
- **9class vs scrambled**: No significant difference at any seed or K. Near-perfect agreement on perturbed data.

Saved to server (`results/exp4_vanilla_3seed_perturbation.json`, `results/exp4_mcnemar_perturbed.json`) and registered as artifact `art_20260518_6a9182`.

---
