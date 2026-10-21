# ops check running experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-running-experiments_20260514T212529_result.json`
- **Structured JSON:** [`9a498a268bf5b4edb1d4.json`](../../sessions/9a/9a498a268bf5b4edb1d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/report_running_status.md`。汇总：

**全部 7 个实验均存活，无异常崩溃。**

| 实验 | 服务器 | GPU | 进度 | 状态 |
|------|--------|-----|------|------|
| eval-acr-spatial-v4-default | bjb1 | 0 (70%) | 无日志，PID=252489 | 运行中 |
| eval-acr-spatial-v4-small | bjb1 | 3 (70%) | task 1/10 | 运行中 |
| eval-argmin-only-spatial | bjb1 | 1 (20%) | task 4/10 | 运行中 |
| eval-tiny-correction-spatial | bjb1 | 2 (21%) | task 4/10 | 运行中 |
| crm-train-v3-norm-obs-only | bjb1 | 0 | epoch 24/50, val=0.0167 | 运行中 |
| crm-train-v3-norm-scalar-unc | bjb1 | 3 | epoch 24/50, val=0.0406 | 运行中 |
| eval-vla-mean-spatial | bjb2 | 0 (11%) | task 9/10，接近完成 | 运行中 |

唯一需注意：**eval-acr-spatial-v4-default** 的 stdout 输出到 tmux pipe，无独立日志文件，无法读取进度。实际 PID 为 **252489**。

---
