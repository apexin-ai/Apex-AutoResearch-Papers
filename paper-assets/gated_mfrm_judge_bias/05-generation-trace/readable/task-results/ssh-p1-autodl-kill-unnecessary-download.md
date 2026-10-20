# ssh p1 autodl kill unnecessary download

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p1_autodl_kill_unnecessary_download_20260522T135403_result.json`
- **Structured JSON:** [`1ce1ef54eda55521a9bc.json`](../../sessions/1c/1ce1ef54eda55521a9bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**pth 文件状态**：无需处理。`original/` 目录仅存在于 Llama-3.1-8B-Instruct 下，只有 2.1M（`params.json` + `tokenizer.model`），没有 `consolidated.00.pth`。PID 123917 的 Llama 下载已带 `ignore_file_pattern=['original/*']`，不会拉 pth。其他模型（Qwen、Mistral）无 `original/` 目录。

**不需要 kill 任何进程。**

**safetensors 下载进度**：

| 模型 | 状态 | 大小 |
|------|------|------|
| gemma-2-9b-it | **完成** (4/4 safetensors) | 18G |
| Llama-3.1-8B-Instruct | 下载中 (2/4 done, 2 in temp, ~71%) | 15G |
| Mistral-7B-Instruct-v0.3 | 下载中 (0 done, 3 in temp) | 11G |
| Qwen2.5-7B-Instruct | 刚开始 (0 done, 0 in temp) | 12M |

**磁盘**：数据盘 250G 用了 117G，剩余 134G (47%)，空间充足。

**Llama 下载速度极慢**（~400-800 KB/s），model-00002 和 model-00003 各约 4.6G，按当前速度还需数小时。Qwen2.5-7B-Instruct 可能在等 PID 102451 的 Qwen 下载排队（该进程按顺序下 Qwen 再下 Mistral，但 Mistral 已在下了，说明 Qwen2.5 可能已由另一渠道完成或失败）。

---
