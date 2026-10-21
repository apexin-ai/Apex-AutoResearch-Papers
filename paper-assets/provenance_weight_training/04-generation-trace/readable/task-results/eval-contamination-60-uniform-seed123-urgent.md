# eval contamination 60 uniform seed123 urgent

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_contamination_60_uniform_seed123_urgent_20260518T032823_result.json`
- **Structured JSON:** [`e0b77760d2c1b6057e53.json`](../../sessions/e0/e0b77760d2c1b6057e53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the comparison:

## ρ=0.6 seed123 对比

| Method | PPL | Loss |
|--------|-----|------|
| **adaptive** (contamination_60_seed123) | 17.732 | 2.8754 |
| **uniform** (contamination_60_uniform_seed123) | 17.754 | 2.8766 |
| **Δ (adaptive - uniform)** | **-0.022** | **-0.0012** |

Adaptive 在 ρ=0.6 seed123 下略优于 uniform (PPL 低 0.022)，方向与 Claim 3 一致，但差异很小。

---
