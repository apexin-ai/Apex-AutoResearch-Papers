# analysis qwen14b kl30 s456 eval v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b_kl30_s456_eval_v2_20260519T125209_result.json`
- **Structured JSON:** [`9e57885606a61cbf1afc.json`](../../sessions/9e/9e57885606a61cbf1afc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments updated. Here's the summary:

---

## Benchmark Metrics — `qwen14b_kl30_s456_eval_v2`

| Metric | KL s456 | KL s42 | TEAL 30% uniform s42 |
|---|---|---|---|
| **WikiText-2 PPL** | **7.69** | 7.63 | 8.01 |
| **MMLU** | **64.11%** | 64.49% | 66.34% |
| **ARC-C (norm)** | **53.24%** | 54.44% | 55.29% |
| **WinoGrande** | **72.30%** | 72.45% | 69.85% |
| **HellaSwag (norm)** | **71.13%** | — | — |
| **PIQA (norm)** | **75.52%** | — | — |

## Conclusion: **success** — MMLU reversal is systematic

s456 replicates the same pattern as s42:
- **PPL improves** over TEAL uniform (7.69 vs 8.01), confirming KL loss learns better masks for perplexity
- **MMLU drops** below TEAL uniform (64.11% vs 66.34%), and is slightly worse than s42 KL (64.49%)
- **ARC-C drops** similarly (53.24% vs 55.29% TEAL, 54.44% KL s42)
- **WinoGrande improves** over TEAL uniform (72.30% vs 69.85%), matching s42 KL (72.45%)

The PPL↑ / MMLU↓ / WG↑ pattern holds across both seeds — this is a systematic property of the KL loss on Qwen-14B, not seed noise.

## Training experiment `qwen14b_kl30_s456`
Completed 1000/1000 steps, final loss=0.309, sparsity=0.277, checkpoint saved. Marked DONE.

## Anomalies
None. Both runs exited cleanly (EXIT_CODE=0), no OOM or NaN.

---
