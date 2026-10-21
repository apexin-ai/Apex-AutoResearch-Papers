# diag gpu visibility

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu-visibility_20260518T043402_result.json`
- **Structured JSON:** [`ae28ffb77fb03d480589.json`](../../sessions/ae/ae28ffb77fb03d480589.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 项目 | 值 |
|---|---|
| **可见 GPU** | 1 张 — `GPU 0: NVIDIA GeForce RTX 5090` |
| **Driver / CUDA** | 580.76.05 / 13.0 |
| **显存** | 10896 MiB / 32607 MiB (占用 33%) |
| **GPU 利用率** | 88%, 52°C, 289W/575W |
| **进程** | PID 53903 `python` (3968 MiB), PID 55009 `/root/miniconda3/bin/python` (6914 MiB) |
| **CUDA_VISIBLE_DEVICES** | 空（未设置，默认可见所有卡） |
| **tmux sessions** | `tc_fix` 存活 (06:33 创建), `exp054` 存活 (12:04 创建) |

注意：`/dev/nvidia2` 存在但 `nvidia-smi -L` 只报告 1 张卡，说明容器映射了 1 张 5090。两个 Python 进程合计占用约 10.9 GiB 显存，GPU 负载 88%，卡正在跑任务。

---
