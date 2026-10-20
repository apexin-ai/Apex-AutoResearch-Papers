# ops 72b download status check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_72b_download_status_check_20260522T103922_result.json`
- **Structured JSON:** [`6d277a5e9299e191e6e5.json`](../../sessions/6d/6d277a5e9299e191e6e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 72B 模型下载

| 项目 | 状态 |
|------|------|
| 进程 | **活跃**（PID 229326，从 13:06 开始运行，已约 5.5 小时） |
| 已完成分片 | 19/37 safetensors 已落盘（70GB） |
| 正在下载 | 8 个分片并行下载中（model-00019~00027），当前在 temp 目录（21GB） |
| 待下载 | 10 个分片（model-00028~00037）尚未开始 |
| 已下载总量 | ~91GB / ~140GB（**约 65%**） |
| 下载速度 | ~370-400 KB/s（受 AutoDL 代理带宽限制） |
| 预计剩余 | 按当前速度约 **3-4 小时** |

### 推理结果

| 模型 | 状态 | 行数 |
|------|------|------|
| Qwen2.5-3B MMLU | 完成 | 57,600 |
| Qwen2.5-7B MMLU | 完成 | 57,600 |
| Qwen2.5-72B | **未开始**（等模型下载完成） |

### 磁盘空间

| 总量 | 已用 | 可用 | 使用率 |
|------|------|------|--------|
| 350G | 276G | 75G | 79% |

72B 模型剩余约 50GB 待下载，加上推理时 vLLM 加载开销，75GB 剩余空间足够。无 tmux 会话运行。

---
