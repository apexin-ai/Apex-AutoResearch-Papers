# read b8 eval precision

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_read_b8_eval_precision_20260522T161906_result.json`
- **Structured JSON:** [`7cceed406ade4eef130d.json`](../../sessions/7c/7cceed406ade4eef130d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated with full precision. Here's the complete comparison:

## B=8 Eval Results (3 decimal places)

| 实验 | holdout_ppl | owt_ppl | wiki_ppl |
|------|------------|---------|----------|
| **adaptive** (bs8_nmin4_adaptive_seed42) | 17.650 | 18.332 | 15.318 |
| **uniform** (bs8_nmin4_uniform_seed42) | 17.694 | 18.363 | 15.337 |
| **Δ (adaptive − uniform)** | **−0.044** | **−0.031** | **−0.019** |

Adaptive 在三个 eval 集上均优于 uniform，Δ 范围 −0.019 ~ −0.044。Registry 已用完整浮点精度更新（含 PPL 和 loss）。

---
