# exp steering llama L16 123 collect

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_steering-llama-L16-123-collect_20260523T105357_result.json`
- **Structured JSON:** [`62edb14178ecde559992.json`](../../sessions/62/62edb14178ecde559992.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Llama L16 (last position)
状态: **完成**
Probe accuracy: **76.84%**
Test samples: 136 conflict / 272 total

| Alpha | Steering flips | Control flips | Fisher p |
|-------|---------------|---------------|----------|
| +5 | 12/136 (8.8%) | 11/136 (8.1%) | 1.0000 |
| +10 | 25/136 (18.4%) | 15/136 (11.0%) | 0.1226 |
| +20 | 31/136 (22.8%) | 33/136 (24.3%) | 0.8864 |

Bonferroni 显著 (k=3, 阈值 p<0.0167): **无**

注意：实验只跑了正方向 alpha（5, 10, 20），没有负方向（-5, -10, -20）。Alpha 10 有微弱趋势（steering > control），但未达显著。Alpha 20 时 control flips 反而略高于 steering flips，说明高 alpha 破坏了生成质量。

JSON 路径: `/root/clkc_mech_interp/data/llama31/steering_results_L16_last.json`
Log 路径: `/root/clkc_mech_interp/logs/steering_llama_L16.log`

---
