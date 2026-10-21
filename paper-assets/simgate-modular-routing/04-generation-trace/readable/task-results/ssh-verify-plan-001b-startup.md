# ssh verify plan 001b startup

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-plan-001b-startup_20260513T221117_result.json`
- **Structured JSON:** [`8e56d8d6cc04ff6033fe.json`](../../sessions/8e/8e56d8d6cc04ff6033fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 启动状态：GPU0 异常，GPU1 正常

### plan-001b-gpu0 — **崩溃** (EXIT_CODE=1)
- **根因**: vLLM 初始化时 cuda:0 仅 3.51/31.36 GiB 空闲，需要 26.65 GiB (85%)
- 崩溃时间: 2026-05-13T22:10:20Z（启动后几秒即失败）
- Reuse 机制本身正常：7 个 task 都正确识别了 5-7 条可复用 episode
- `find-animal/` 目录已创建，仅含复制的 reuse 数据

### plan-001b-gpu1 — **正常运行**
- PID 773109 存活，已运行 ~1:30
- 4 个 task 各复用 5 条 episode，reuse 机制生效
- 日志显示活跃推理中（~800-1900 toks/s input, ~95-100 toks/s output）

### GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 28013/32607 MiB | 0% |
| 1 | 28013/32607 MiB | 0% |

### 诊断
GPU 0 被某个进程占用了 ~28 GiB 显存（利用率 0%），导致 gpu0 的 vLLM 无法分配内存。需要排查 GPU 0 上的残留进程并清理后重新提交 gpu0 任务。

---
