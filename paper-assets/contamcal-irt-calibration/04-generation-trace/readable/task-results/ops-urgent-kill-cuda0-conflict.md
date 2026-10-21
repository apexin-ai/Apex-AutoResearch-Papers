# ops urgent kill cuda0 conflict

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_kill_cuda0_conflict_20260516T125100_result.json`
- **Structured JSON:** [`e5b72a86e2f1de9de685.json`](../../sessions/e5/e5b72a86e2f1de9de685.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| 项目 | 状态 |
|------|------|
| **PID 777654 (3B_d000_s123 误跑 cuda:0)** | 已不存在（kill 前已死） |
| **PID 778505 (1.5B d100_s123)** | **已死** — 进程不存在，冲突导致进程损坏 |

### 全 GPU 进程表

| GPU | PID | 显存 | 进程 |
|-----|-----|------|------|
| cuda:0 | 780943 | 7058 MiB | 3B_d000_s123 signals (mmlu, s4) — 运行 6min |
| cuda:1 | 780591 | 2110 MiB | 0.5B d000_s123 signals (mmlu, s4) — 运行 7min |
| cuda:2 | — | 0 MiB | **空闲** ✓ |
| cuda:3 | 764460 | 6610 MiB | python3 进程 |
| cuda:4 | — | 0 MiB | 空闲 |
| cuda:5 | — | 0 MiB | **空闲** ✓ |

### 结论

- cuda:2 和 cuda:5 确认空闲
- **需要重跑 1.5B d100_s123 arc_challenge on cuda:0**（PID 778505 已死，当前 cuda:0 被 3B_d000_s123 占用，需等其完成或选其他空闲 GPU）

---
