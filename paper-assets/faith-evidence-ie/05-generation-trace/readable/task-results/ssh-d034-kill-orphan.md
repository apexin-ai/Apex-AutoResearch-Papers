# ssh d034 kill orphan

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d034-kill-orphan_20260515T011910_result.json`
- **Structured JSON:** [`3beacead7fcca2713e7a.json`](../../sessions/3b/3beacead7fcca2713e7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

| # | 项目 | 状态 |
|---|------|------|
| 1 | PID 90084/90085 | **已终止**（SIGTERM 成功，无需 SIGKILL） |
| 2 | cuda:0 显存 | **已释放**：13645 MiB → **0 MiB**，利用率 0% |
| 3 | ckpt-100 eval (PID 117635) | **已不在运行** |
| 4 | RSFT generation (PID 122144) | **仍在运行**，cuda:1 占用 23996 MiB |

### 4 张 GPU 当前状态

| GPU | 显存占用 | 利用率 | 占用进程 |
|-----|---------|--------|---------|
| 0 | 0 MiB | 0% | 无（已释放） |
| 1 | 24005 MiB | 86% | PID 122149 (RSFT generate) |
| 2 | 2850 MiB | 88% | PID 129436 (1426 MiB) + PID 130086 (1410 MiB) |
| 3 | 0 MiB | 0% | 无 |

cuda:0 和 cuda:3 空闲可用。

---
