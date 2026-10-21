# diagnose eval rsft r2b

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_rsft_r2b_20260515T114358_result.json`
- **Structured JSON:** [`bcb6228880a3b288ede1.json`](../../sessions/bc/bcb6228880a3b288ede1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能之前已清除）。

**r2b 评估总结**：

| 指标 | SFT baseline | r1 (3ep, α=128) | **r2b (1ep, α=32)** |
|------|-------------|-----------------|---------------------|
| rel_f1 | 0.4057 | 0.4449 | **0.4493** |
| evi_f1 | 0.7979 | 0.8187 | **0.8128** |
| edcr | 0.7118 | — | **0.6609** |

r2b 在 rel_f1 上略优于 r1（+0.44pt），evi_f1 低于 r1（-0.59pt）。1 epoch + conservative scaling (α=32/r=64=0.5) 已足够超过 baseline，但 EDCR 下降说明 distractor citation 问题更突出。

---
