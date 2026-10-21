# ops diagnose e2v2 exit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_e2v2_exit_20260518T144201_result.json`
- **Structured JSON:** [`76df951fbb4264bd4c36.json`](../../sessions/76/76df951fbb4264bd4c36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 结果

**退出原因**: 正常完成，step 300/300，EXIT_CODE=0

**关键 metrics (step 300)**:
| 指标 | 值 |
|---|---|
| reward/mean | 0.0562 |
| loss | 0.0367 |
| frac_reward_zero_std | 0.525 |
| kl | 0.00306 |
| entropy | 0.157 |
| learning_rate | 3.33e-9 (cosine 尾部) |
| runtime | 48min (resume 部分) |

**Checkpoints**: checkpoint-280, 290, 300 (save_total_limit=3 生效)

**磁盘**: 482G/619G (78%)，138GB 可用，健康

**已完成操作**:
- Registry `grpo_standard_20_extended_300` → DONE/success，更新了 checkpoint_path、log_path、metrics
- Cron `grpo_standard_20_extended_300_v2` 已删除

**注意**: reward/mean 在 step 260→300 区间持续下降 (0.102→0.056)，frac_reward_zero_std 升至 0.525，表明 standard pruned 模型在延长训练中进入 reward desert。无需 resume。

---
