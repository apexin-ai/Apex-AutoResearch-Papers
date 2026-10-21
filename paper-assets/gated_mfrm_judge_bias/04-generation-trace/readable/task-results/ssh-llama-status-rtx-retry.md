# ssh llama status rtx retry

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_llama_status_rtx_retry_20260523T231001_result.json`
- **Structured JSON:** [`bb1675d3ac4453289007.json`](../../sessions/bb/bb1675d3ac4453289007.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 1. LLaMA-70B-AWQ（autodl-8gpu）

- **进程**: HF 下载进程存活（PID 480645），但卡在 read timeout，正在尝试 resume `model-00005-of-00009.safetensors`
- **已下载**: 仅 7.8GB 不完整分片（`.incomplete`），**无完整的 safetensors 权重文件**
- **ModelScope 尝试**: 失败 — `casperhansen/Llama-3.3-70B-Instruct-AWQ` 在 ModelScope 上不存在（404）
- **根因**: 未设 HF_TOKEN（限速 + 超时），AutoDL 直连 HF 太慢

**需要处理**：当前进程基本卡死。建议 kill 后用 `network_turbo` + `HF_TOKEN` 重新下载，或在 ModelScope 上搜索其他组织发布的 LLaMA-3.3-70B AWQ 量化版本（如 `LLM-Research` 等镜像账号）。是否现在操作？

### 2. rtx6000-4x

- **不可达**：连接端口 23687 被拒绝（`Unable to connect to port 23687 on 36.103.198.204`）

---
