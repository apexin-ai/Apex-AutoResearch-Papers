# ssh progress check westd

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_progress-check-westd_20260514T154126_result.json`
- **Structured JSON:** [`54f30429df08614db7a6.json`](../../sessions/54/54f30429df08614db7a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/progress_check_20260514.md`。

**核心状态：**

| 进程 | 进度 | 关键指标 | 预计完成 |
|------|------|----------|----------|
| CWM v12 eval | 85.4% | acc=**57.8%** | ~02:15 今夜 |
| CWM seed123 eval | 84.3% | acc=**59.1%** | ~02:30 今夜 |
| CWM 8B train | 22.6% | loss=0.45, eval_loss=0.36 | ~明天 17:00 |
| CLS 8B s123 train | 40.4% | loss=0.36, eval_loss=0.28 | ~明天 11:00 |

**重要发现：两个 8B training 都崩溃过。** 崩溃原因是 eval 阶段 DataLoader worker 被系统 kill（`signal: Terminated`），疑似内存不足。两个进程都已被重启，重启命令带了 `--dataloader_num_workers 0`，改为主进程加载数据，应能规避该问题。当前运行稳定。

---
