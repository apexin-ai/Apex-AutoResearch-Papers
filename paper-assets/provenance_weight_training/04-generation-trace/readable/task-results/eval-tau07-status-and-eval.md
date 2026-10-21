# eval tau07 status and eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_tau07_status_and_eval_20260520T005319_result.json`
- **Structured JSON:** [`855c0e5af246d456e076.json`](../../sessions/85/855c0e5af246d456e076.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 全部完成。

## τ=0.7 vs τ=0.8 PPL Comparison

| Seed | τ=0.7 | τ=0.8 | Δ (0.7−0.8) |
|------|-------|-------|-------------|
| 42   | 17.680 | 17.689 | −0.009 |
| 123  | 17.666 | 17.677 | −0.011 |
| 456  | 17.677 | 17.683 | −0.006 |
| **Mean** | **17.674** | **17.683** | **−0.009** |

τ=0.7 在三个 seed 上均略优于 τ=0.8，平均 PPL 降低 0.009（17.674 vs 17.683）。差异很小但方向一致。

---
