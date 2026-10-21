# ssh urgent autodl status check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_autodl_status_check_20260522T120555_result.json`
- **Structured JSON:** [`cfc0202c3dc3b30986dd.json`](../../sessions/cf/cfc0202c3dc3b30986dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 状态报告 — autodl-8gpu (2026-05-22 20:06 UTC)

### 1. GPU 使用

| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX PRO 6000 Blackwell (96GB) | 0% | 0 / 97887 MiB |
| 1 | RTX PRO 6000 Blackwell (96GB) | 0% | 0 / 97887 MiB |
| 2 | RTX PRO 6000 Blackwell (96GB) | 0% | 0 / 97887 MiB |
| 3 | RTX PRO 6000 Blackwell (96GB) | 0% | 0 / 97887 MiB |

**全部空闲，无 GPU 进程。**

---

### 2. 推理进程

无 vLLM / inference 进程运行。

**tmux sessions:** `orchestrator2` 存在，正在运行 `run_remaining.sh`，当前**阻塞在等待 Llama-3.1-8B-Instruct 下载完成**（`sleep 30` 循环检测中）。

---

### 3. Response 文件状态

| 文件 | 行数 | 状态 |
|------|------|------|
| gemma-2-9b.jsonl | 500 | ✅ 完成 |
| qwen3-8b.jsonl | 500 | ✅ 完成 |
| gpt-3.5-turbo-0125.jsonl | 500 | ✅ 完成 |
| gpt-4-0314.jsonl | 500 | ✅ 完成 |
| gpt-4-0613.jsonl | 500 | ✅ 完成 |
| gpt-4o-mini.jsonl | 500 | ✅ 完成 |
| gpt-4o.jsonl | 500 | ✅ 完成 |
| llama-3.3-70b.jsonl | 491 | ⚠️ 差 9 条 |
| qwen2.5-72b.jsonl | 484 | ⚠️ 差 16 条 |
| mistral-large-2.jsonl | 90 | ⚠️ 未完成 |
| claude-opus-4.7.jsonl | 88 | ⚠️ 未完成 |
| gpt-5.5.jsonl | 15 | ⚠️ 未完成 |

---

### 4. 模型下载进度

**两个 ModelScope 下载进程正在运行：**

| 模型 | 大小 | safetensors | 状态 |
|------|------|-------------|------|
| gemma-2-9b-it | 18G | 4/4 | ✅ 完成 |
| Qwen3-8B | 16G | 5/5 | ✅ 完成（已存在） |
| Llama-3.1-8B-Instruct | 8.5G | 1/4 完成 + 3/4 在 temp | 🔄 下载中（~61%/26%/26%，速度 370-900 KB/s） |
| Qwen2.5-7B-Instruct | 12M | 0 | 🔄 仅 metadata，safetensors 未开始 |
| Mistral-7B-Instruct-v0.3 | — | — | ❌ 目录不存在，未开始 |

**下载速度极慢**（ModelScope ~370KB/s-900KB/s）。Llama 还在下载 `original/consolidated.00.pth`（15GB，8%），但 orchestrator 只需要 safetensors 文件和空 `._____temp/`。

**预估 ETA：**
- Llama safetensors 完成：约 2-3 小时
- Qwen2.5 开始/完成：在 Llama 之后（串行下载），再 1-2 小时
- Mistral：排在 Qwen2.5 之后

---

### 5. 磁盘

| 分区 | 大小 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (root) | 30G | 14G | 17G | 47% |
| /root/autodl-tmp | 250G | 117G | 134G | 47% |

空间充足。

---

### 6. Orchestrator 日志

```
[19:10:52] Waiting for Llama-3.1-8B-Instruct weights at /root/autodl-tmp/models/Llama-3.1-8B-Instruct ...
```

一直阻塞在此处。orchestrator 逻辑：等 safetensors 齐全 + `._____temp/` 为空后才启动 vLLM 生成。

---

### 总结

- **gemma-2-9b 和 Qwen3-8B response 已全部完成（各 500 条）**
- GPU 全部空闲，等待模型下载
- 瓶颈是 ModelScope 下载速度极慢（~500KB/s），Llama 预计还需 2-3 小时，全部模型就绪可能需要 5-6 小时
- 注意：Llama 下载进程同时在拉 15GB 的 `original/consolidated.00.pth`（非必需文件），会占用带宽

---
