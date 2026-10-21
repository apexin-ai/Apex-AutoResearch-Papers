# ops w1 results collection

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_w1-results-collection_20260516T225911_result.json`
- **Structured JSON:** [`fdf00b7c008f00e80bf0.json`](../../sessions/fd/fdf00b7c008f00e80bf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All experiments complete. Here are the final results:

---

## Table 1: τ Schedule Ablation

| τ Schedule | WikiText-2 PPL ↓ | Training Loss | Sparsity |
|---|:---:|:---:|:---:|
| linear 1.0→0.1 (baseline) | 11.963 | 0.301 | 0.488 |
| fixed τ=0.5 | **11.861** | 0.248 | 0.484 |
| fixed τ=0.1 | 12.072 | 0.430 | 0.484 |

**Findings**: Fixed ��=0.5 gives the best PPL (11.861), beating the linear annealing baseline by 0.10. Fixed τ=0.1 hurts significantly (12.072), +0.11 over baseline. Lower temperature makes the Gumbel-sigmoid too sharp during early training, resulting in higher final loss (0.430 vs 0.248) without improved downstream quality.

---

## Table 2: Predictor Quality vs Training Steps (linear 1.0→0.1 schedule)

| Steps | WikiText-2 PPL ↓ | Training Loss | τ (at step) | Sparsity |
|:---:|:---:|:---:|:---:|:---:|
| 200 | 15.158 | 0.344 | 0.820 | 0.480 |
| 400 | 12.538 | 0.273 | 0.640 | 0.484 |
| 600 | 12.046 | 0.273 | 0.460 | 0.488 |
| 800 | 11.907 | 0.250 | 0.280 | 0.484 |
| 1000 | 11.906 | 0.301 | 0.100 | 0.488 |

**Findings**: Most quality is gained by step 600 (PPL drops from 15.16 → 12.05, a 20.5% reduction). Steps 800→1000 yield negligible additional improvement (11.907 → 11.906). The predictor converges rapidly, with ~95% of the gap to final quality closed by step 600.

---
