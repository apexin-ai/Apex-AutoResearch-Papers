# ssh exp 012 check and model download

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp_012_check_and_model_download_20260521T234553_result.json`
- **Structured JSON:** [`4096447b6a171e4b0889.json`](../../sessions/40/4096447b6a171e4b0889.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. exp-012 状态
- **进程存活**：PID 54823，CPU 105%，已运行 45 分钟
- **进度**：14/80 fits 完成（CSV 15 行含 header）
- **速度**：~175-180s/fit
- **预计剩余**：66 fits × ~178s ≈ **3.3 小时**
- 注意：MCMC 运行在单 CPU 核心（JAX 未检测到多设备），不影响 GPU 任务

### 2. 模型下载状态
- **仓库**：`casperhansen/Llama-3.3-70B-Instruct-AWQ`（非 gated，17 files，~35GB）
- **状态**：下载中，已缓存 ~1GB，9 个分片并行下载
- **预计完成**：30-60 分钟（未认证速率，通过 network_turbo 加速）
- **路径**：`/root/autodl-tmp/models/Llama-3.3-70B-Instruct-AWQ/`
- 监控：`tail -3 /tmp/llama_download.log`

### 3. vLLM
- **已安装**：vLLM 0.21.0，torch 2.11.0+cu130，4 GPUs 检测正常

### 4. 磁盘
| 分区 | 总量 | 可用 |
|------|------|------|
| Root (overlay) | 30G | 28G |
| Data (/root/autodl-tmp) | 250G | ~249G |

模型下载完成后空间充裕。

---
