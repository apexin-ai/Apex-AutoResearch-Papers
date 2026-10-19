# check westd28034 model and exp004

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd28034_model_and_exp004_20260518T150449_result.json`
- **Structured JSON:** [`090781b3bc80e6fcb88f.json`](../../sessions/09/090781b3bc80e6fcb88f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 模型下载状态：失败，需要重新下载

下载进程 (PID 2756) 已终止，因多次网络超时导致下载不完整：

| 文件 | 状态 |
|------|------|
| model-00002-of-00005.safetensors (3.8G) | 完成 |
| model-00001-of-00005 (~190M downloaded) | `.incomplete` |
| model-00003-of-00005 (~160M downloaded) | `.incomplete` |
| model-00004-of-00005 (~70M downloaded) | `.incomplete` |
| model-00005-of-00005 (~40M downloaded) | `.incomplete` |
| tokenizer + config 等小文件 | 完成 |

**5 个 shard 中只有 1 个完整**，其余 4 个因 HuggingFace 连接超时中断，仅下载了极小部分（每个 shard 约 3.8G，但 incomplete 文件只有 40-190M）。

### exp-004 就绪情况：未就绪

- `run_exp004_act_baseline.py` — **不存在**
- `calibration_v2_1_expanded.jsonl` — **不存在**
- 无 exp-004 相关进程或 tmux session

### 需要的操作

1. 重启模型下载（HF 支持断点续传，直接重跑即可）
2. 将 exp-004 训练脚本和数据文件部署到 westd-28034

---
