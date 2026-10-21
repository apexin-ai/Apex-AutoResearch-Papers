# infra boil v3 status check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_boil-v3-status-check_20260513T162603_result.json`
- **Structured JSON:** [`6ae3dea7b5ddc8889aee.json`](../../sessions/6a/6ae3dea7b5ddc8889aee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验正在运行。**

| 项目 | 状态 |
|------|------|
| PID 650421 | **存活**，已运行 3 分钟，PPID=1（后台进程） |
| GPU 占用 | 两张 GPU 各占 28004 MiB（PID 650130 在 GPU0，PID 651246 在 GPU1） |
| 日志 | 持续输出 vLLM 推理日志，正在逐条处理 prompts，推理速度 ~95-100 toks/s output |

注意：GPU1 上跑的进程 PID 是 651246（不是 650421），650421 是外层 bash wrapper，实际推理子进程是 651246。实验正常运行中，无报错。

---
