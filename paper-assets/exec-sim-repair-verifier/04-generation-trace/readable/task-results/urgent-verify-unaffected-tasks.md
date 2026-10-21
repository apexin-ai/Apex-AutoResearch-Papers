# urgent verify unaffected tasks

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_verify-unaffected-tasks_20260514T141922_result.json`
- **Structured JSON:** [`914e2a1fdebbf209a0fe.json`](../../sessions/91/914e2a1fdebbf209a0fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 eval 任务正常运行，未受 SIGTERM 影响。

| 任务 | Server | GPU | PID | 状态 | 进度 |
|------|--------|-----|-----|------|------|
| CWM v12 eval | westd | 0/1 | 195668 | ALIVE, 已运行 13h16m | 输出目录空（结束时写入） |
| CWM seed123 eval | westd | 0/1 | 195531 | ALIVE, 已运行 13h16m | 输出目录空（结束时写入） |
| test@4096 eval | home | 0 | 3111657 | ALIVE, CPU 100% | **8625/9784 (88.2%)**, running_acc=81.0% |

GPU 状态：
- westd GPU 0: 88%, 13GB — GPU 1: 87%, 13GB — GPU 2/3: 空闲（训练已被杀）
- home GPU 0: 89%, 10.9GB

注意：westd 两个 eval 进程命令行都显示 `--device cuda:0`，但 GPU 0 和 1 都有负载，应该是通过 `CUDA_VISIBLE_DEVICES` 映射到不同物理 GPU。

---
