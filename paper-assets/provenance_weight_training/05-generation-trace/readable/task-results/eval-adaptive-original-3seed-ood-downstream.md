# eval adaptive original 3seed ood downstream

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_adaptive_original_3seed_ood_downstream_20260520T090650_result.json`
- **Structured JSON:** [`1dce19a0614eb27bc2d2.json`](../../sessions/1d/1dce19a0614eb27bc2d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**三个 checkpoint 全部不存在，任务终止。**

汇总：

| Checkpoint | westd-41312 | westd-47453 (原训练服务器) |
|---|---|---|
| `adaptive_seed42/final` | 不存在 | 不存在 |
| `adaptive_seed123/final` | 不存在 | 不存在 |
| `adaptive_seed456/final` | 不存在 | 不存在 |

Registry 记录显示这三个实验于 2026-05-14 在 `westd-47453` 完成训练，checkpoint 路径为相对路径 `output/models/adaptive_seed*/final`，但文件已丢失。可能原因：
1. `westd-47453` 实例被重建/重置，数据盘未持久化
2. Checkpoint 用了相对路径存到根分区而非 `/root/autodl-tmp/`，实例回收后丢失

**需要重新训练这三个 checkpoint 才能跑 OOD + downstream eval。** 是否继续？

---
