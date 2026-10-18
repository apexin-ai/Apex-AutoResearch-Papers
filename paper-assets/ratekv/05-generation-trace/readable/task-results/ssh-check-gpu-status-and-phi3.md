# ssh check gpu status and phi3

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_gpu_status_and_phi3_20260516T023611_result.json`
- **Structured JSON:** [`09cc7d515567c67b2276.json`](../../sessions/09/09cc7d515567c67b2276.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### GPU 状态
| GPU | 型号 | 温度 | 功耗 | 显存占用 | 利用率 | 进程 |
|-----|------|------|------|----------|--------|------|
| cuda:0 | RTX PRO 6000 Blackwell (98GB) | 75°C | 541W/600W | **23.2GB / 98GB** | **100%** | `python run_internlm2_hires_profiling.py` (PID 389863) |
| cuda:1 | RTX PRO 6000 Blackwell (98GB) | 31°C | 34W/600W | 3MB / 98GB | 0% | 空闲 |

### InternLM2 Profiling
- **PID 389862** (bash wrapper) → **PID 389863** (python)，**正在运行**，启动于 09:52
- 进度：**195/256** heads profiled（~76%），已运行 44 分钟，ETA ~14 分钟
- 当前在 Layer 24，2-bit delta profiling

### Phi3 Medium
- **没有 phi3 相关进程在运行**，GPU 1 空闲
- `run_phi3_medium_constrained_pipeline.py` 已同步到服务器（May 16 10:14）

### CodeLlama-7B 模型
- **未下载完成**。`/root/autodl-tmp/.hf_cache/codellama/CodeLlama-7b-hf/` 目录存在但只有一个 `.mdl` 元数据文件（48 bytes），没有实际模型权重
- `run_codellama_hires_profiling.py` 已同步到服务器（May 16 02:02）

### Phi3-Medium 模型
- `/root/autodl-tmp/.hf_cache/microsoft/` 目录为空，**Phi3-Medium 模型也未下载**

### tmux
- 有一个 `gemma2_9b_full_pipeline` session（May 15 创建），无 phi3 相关 session

**结论**：cuda:0 跑 InternLM2 profiling 还剩约 14 分钟完成；cuda:1 完全空闲。Phi3 和 CodeLlama 的实验脚本已同步，但两个模型都还没下载到服务器。

---
