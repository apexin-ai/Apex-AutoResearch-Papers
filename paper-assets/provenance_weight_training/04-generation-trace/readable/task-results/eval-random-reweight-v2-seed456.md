# eval random reweight v2 seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_random_reweight_v2_seed456_20260522T132450_result.json`
- **Structured JSON:** [`7ace9b88c2c0a0c362de.json`](../../sessions/7a/7ace9b88c2c0a0c362de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。Registry 已更新为 DONE/success。

## random_reweight_v2_seed456 评估结果

| 数据集 | PPL |
|--------|-----|
| **holdout** | 17.951 |
| **owt** | 18.602 |
| **wiki** | 15.503 |

三个 seed 高度一致，确认 random reweight 结果稳定：

| seed | holdout | owt | wiki |
|------|---------|-----|------|
| 42 | 17.958 | 18.606 | 15.519 |
| 123 | 17.945 | 18.622 | 15.562 |
| **456** | **17.951** | **18.602** | **15.503** |

---
