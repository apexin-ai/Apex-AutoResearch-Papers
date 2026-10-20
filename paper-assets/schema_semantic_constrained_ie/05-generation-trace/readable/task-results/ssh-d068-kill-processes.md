# ssh d068 kill processes

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d068_kill_processes_20260519T164933_result.json`
- **Structured JSON:** [`aee00a370e1b81e3823a.json`](../../sessions/ae/aee00a370e1b81e3823a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. d068 进程：全部已 kill
- westd-16980: 2 个进程 (beta=0.0, beta=0.5) + 2 个 bash wrapper → 已清除
- westd-21461: 2 个进程 (beta=1.0, beta=2.0) + 2 个 bash wrapper → 已清除
- 无残留

### 2. d064 进程：全部正常运行
- **westd-16980**: 2 个 d064 进程占 GPU 0/1，利用率 91%/84%
- **westd-21461**: 2 个 d064 进程占 GPU 0/1，利用率 87%/78%
- 无异常进程占 GPU

### 3. d064 进度（DocRED dev set, 998 条）

| 服务器 | 任务 | 完成数 | 进度 |
|--------|------|--------|------|
| westd-16980 | llama_beam4_unconstrained | 465 | 47% |
| westd-16980 | llama_beam4_constrained | 401 | 40% |
| westd-21461 | llama_greedy_constrained | 510 | 51% |
| westd-21461 | llama_greedy_unconstrained | **998** | **完成** |
| westd-21461 | qwen_beam4_constrained | 251 | 25% |
| westd-21461 | qwen_beam4_unconstrained | **998** | **完成** |

---
