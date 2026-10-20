# eval threshold q07 completion

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_threshold_q07_completion_20260516T102045_result.json`
- **Structured JSON:** [`ab68d84601faa9221b0a.json`](../../sessions/ab/ab68d84601faa9221b0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 结果

**threshold_q07_seed42：训练失败**

- 进度：2235/6103 steps (37%, epoch 0.19)
- 原因：进程在 18:20 被静默 kill，无 error/traceback/OOM 日志。推测实例被回收或内存不足
- 最后 checkpoint：checkpoint-2000
- 未执行 eval（训练未完成，无 final checkpoint）

### 阈值实验对比

| 实验 | 阈值 | 状态 | PPL |
|------|------|------|-----|
| detect_remove | q>0.5 | DONE | 17.29 |
| threshold_q03 | q>0.3 | 运行中 | - |
| threshold_q07 | q>0.7 | **失败** | - |

需要重跑 threshold_q07_seed42 才能完成阈值敏感性对比。建议从 checkpoint-2000 resume 以节省时间（已跑完 37%）。

---
