# eval hellaswag gen6 7

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_hellaswag_gen6_7_20260517T111918_result.json`
- **Structured JSON:** [`5ee39d743db7625428a2.json`](../../sessions/5e/5ee39d743db7625428a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已存在（由之前的 `auto_eval_hellaswag.sh` 完成），重复进程已杀掉。

**HellaSwag 评估结果：**

| Generation | acc_norm | acc | 
|---|---|---|
| Gen 6 | **0.3311** ± 0.0047 | 0.3013 ± 0.0046 |
| Gen 7 | **0.3187** ± 0.0047 | 0.2955 ± 0.0046 |

Gen 7 的 acc_norm 比 Gen 6 下降了约 1.2 个百分点（0.3311 → 0.3187），与 spectral collapse 导致模型质量退化的预期一致。

---
