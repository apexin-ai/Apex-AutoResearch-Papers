# exp bs16 adaptive seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_bs16_adaptive_seed42_20260521T133905_result.json`
- **Structured JSON:** [`7fb4d58e31e1cac762c0.json`](../../sessions/7f/7fb4d58e31e1cac762c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行，无 OOM。

**汇总：**

| 项目 | 值 |
|------|-----|
| exp_id | `bs16_adaptive_tau07_seed42` |
| PID | 613352 |
| GPU | cuda:1 |
| batch_size | 16 |
| gradient_accumulation_steps | 1 (effective_batch=16) |
| n_min | 8 |
| tau | 0.7 |
| lr_scheduler_type | linear |
| total_steps | 6103 |
| gradient_checkpointing | 启用（原始命令 OOM，加了此参数解决） |
| 速度 | ~2.75s/it，预计 ~4.5h 完成 |
| Registry | RUNNING |

注意：相比任务原始命令多加了 `--gradient_checkpointing`，因为 bs=16 的 logits tensor (18.55 GiB) 导致 OOM。主实验 bs=4 无此问题。gradient_checkpointing 不影响训练结果（数值等价），仅以计算换显存。

---
