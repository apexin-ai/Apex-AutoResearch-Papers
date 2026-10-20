# check cwm repo exit status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cwm-repo-exit-status_20260517T153856_result.json`
- **Structured JSON:** [`89303b05f3fbb033d37a.json`](../../sessions/89/89303b05f3fbb033d37a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**deepseek-cwm-repo 状态：正常完成**

| 项目 | 值 |
|---|---|
| Status | **Completed** |
| global_step | 13266 / 13266 (100%) |
| Epochs | 3.0 |
| 训练耗时 | 31h 18m (112,680s) |
| train_loss | 0.0210 |
| eval_loss (final) | NaN |
| best_checkpoint | `/root/autodl-tmp/checkpoints_deepseek_cwm_repo/best/` |
| last_checkpoint | `/root/autodl-tmp/checkpoints_deepseek_cwm_repo/checkpoint-13266/` |

注意两个问题：
1. **eval_loss = NaN** — 最终 epoch-3 评估的 loss 为 NaN，epoch-2 时也可能已经出现。需要检查 eval 数据是否有异常。
2. **best_metric = inf** — trainer_state 中 `best_model_checkpoint` 为 None，`best_metric` 为 inf，说明 Trainer 的 best model tracking 没有正常工作（可能因为 eval_loss 是 NaN 导致比较失败）。但日志显示 best model 仍被保存到了 `best/` 目录（由自定义代码而非 Trainer 原生逻辑保存）。

新任务 `deepseek-cwm-repo-s123`（seed=123）已在 cuda:3 上运行中。

---
