# ops check cuda0 conflict

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cuda0-conflict_20260515T053410_result.json`
- **Structured JSON:** [`ab8eebf0d2f953a174e9.json`](../../sessions/ab/ab8eebf0d2f953a174e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 状态：无冲突，正常运行。**

- **PID 334814**：已死，不存在
- **PID 335070**：存活，是 submit_training_job 的 bash wrapper
- **PID 335075**：335070 的子进程，实际执行 `python eval_repo_cls.py`（ckpt-1400, test@8192）
- **GPU 0 显存**：17239 MiB / 32607 MiB（占用 53%），利用率 78%

只有正式提交的任务在跑，无需干预。

---
