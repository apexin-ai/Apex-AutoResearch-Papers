# diagnostic gpu status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnostic_gpu_status_20260514T061024_result.json`
- **Structured JSON:** [`544abbbc8f9ebf0edcd4.json`](../../sessions/54/544abbbc8f9ebf0edcd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

**GPU 状态：**
- `cuda:0`: **占用** — 15257 MiB / 97887 MiB，利用率 0%（正在加载模型或等待推理）
- `cuda:1`: **空闲** — 0 MiB / 97887 MiB

**进程状态：**
- `run_downstream_eval.py`（PID 185608）正在 `cuda:0` 上运行，已运行约 2 分钟，占用 ~1.2GB 内存
- **无 mistral_aggressive 相关进程**

**Tmux：** 无法通过 read_only 检查（命令被白名单拦截）

**结果文件：**
- `mistral_aggressive_results.json`: **已存在**（31809 字节，今天 14:07 生成） — 实验已完成
- `l0_heuristic_results.json`: **不存在**

---
