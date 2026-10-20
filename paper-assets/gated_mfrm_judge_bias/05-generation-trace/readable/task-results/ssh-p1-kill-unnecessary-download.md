# ssh p1 kill unnecessary download

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p1_kill_unnecessary_download_20260522T133400_result.json`
- **Structured JSON:** [`5b591314ab2f7d5d278b.json`](../../sessions/5b/5b591314ab2f7d5d278b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**consolidated.00.pth 并未在下载。** Llama 下载进程 (PID 123917) 已正确使用 `ignore_file_pattern=['original/*']`，`original/` 目录只有小文件 (params.json + tokenizer.model)，没有 .pth 文件。

当前状态汇总：

### Llama-3.1-8B-Instruct (PID 123917)
- 总量 ~13G，只下载 safetensors
- `model-00001-of-00004.safetensors` (4.98G) — **已完成**
- `model-00004-of-00004.safetensors` (1.17G) — **已完成**
- `model-00002-of-00004.safetensors` (2.83G/4.66G) — **61%**，~430 kB/s
- `model-00003-of-00004.safetensors` (5.58G/~4.58G) — **接近完成**，~800 kB/s
- 速度很慢（<1 MB/s），但没有 consolidated.00.pth 占带宽

### Mistral-7B-Instruct-v0.3 (PID 102451)
- 7.1G 已下载，temp 目录还有 3 个 safetensors 文件在写入

### Qwen2.5-7B-Instruct (PID 102451)
- 仅 12M，几乎未开始（Mistral 下载完才会开始）

### 其他已存在的模型
- Qwen3-8B: 16G
- gemma-2-9b-it: 18G

**结论：无需 kill 任何进程。** consolidated.00.pth 没有在下载，带宽瓶颈是 AutoDL/ModelScope CDN 本身的速度限制。

---
