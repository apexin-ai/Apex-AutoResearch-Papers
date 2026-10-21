# diagnose deepseek traj func v2 fixed

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_deepseek-traj-func-v2-fixed_20260516T142001_result.json`
- **Structured JSON:** [`3a0bbb6630f4f217b49d.json`](../../sessions/3a/3a0bbb6630f4f217b49d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**实验并未失败。** `deepseek-traj-func-v2` 训练成功完成：

| 指标 | 值 |
|------|---|
| 训练 steps | 756/756 (3 epochs) |
| train_loss | 0.0857 |
| eval_loss | 0.0891 |
| 训练耗时 | ~51 min |
| Checkpoints | checkpoint-504, checkpoint-756, best |

之前被标记为 `failed` 是误报——可能是 cron 监控在训练完成前检测到进程退出（训练正常结束后进程自然退出），触发了 `on_failed` hook。

Registry 已更正：status=DONE, conclusion=success。

---
