# check resume training checkpoints

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_resume-training-checkpoints_20260514T225356_result.json`
- **Structured JSON:** [`b8c741bebdbb717dbce2.json`](../../sessions/b8/b8c741bebdbb717dbce2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个训练任务状态汇总:

| 实验 | 进度 | 预计完成 |
|------|------|---------|
| **CLS 8B s42 resume** | 946/6633 (14%) | May 16 01:00 |
| **CWM 8B conda** | 2400/6633 (36%) | May 16 11:00 |
| **CLS 8B seed123** | 4521/6633 (68%) | **May 15 14:20** (最先完成) |

s42 resume 目前只产出了 **1 个 checkpoint (checkpoint-800)**，save_steps=200, save_total_limit=35，最终预计产出 ~30 个 checkpoint。磁盘空间充足 (114G 可用)。

报告已写入 `artifacts/training_progress_check_20260514.md`。

---
