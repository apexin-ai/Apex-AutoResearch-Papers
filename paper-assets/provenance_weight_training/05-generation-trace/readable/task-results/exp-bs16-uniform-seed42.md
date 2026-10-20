# exp bs16 uniform seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_bs16_uniform_seed42_20260521T140239_result.json`
- **Structured JSON:** [`22190f31131257ff74b2.json`](../../sessions/22/22190f31131257ff74b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**产出汇总：**

| 项目 | 值 |
|------|-----|
| exp_id | `bs16_uniform_seed42` |
| PID | 620563 |
| GPU | cuda:2 |
| batch_size | 16 |
| weighting_method | uniform |
| gradient_checkpointing | True |
| total_steps | 6103 |
| lr | 5e-05 (linear) |
| seed | 42 |
| Registry | RUNNING |
| 日志 | `~/runs/provenance_weight_training/bs16_uniform_seed42.log` |

训练配置已从日志确认：weighting_method=uniform, batch_size=16, max_steps=6103, lr=5e-05, lr_scheduler_type=linear。与 cuda:1 的 bs16_adaptive_tau07_seed42 唯一区别是 weighting_method。

---
