# ops check phi3 and codellama status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_phi3_and_codellama_status_20260515T183752_result.json`
- **Structured JSON:** [`8ce2a5ffb0f4291acbb9.json`](../../sessions/8c/8ce2a5ffb0f4291acbb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. CodeLlama-7B (PID 357563) — 即将完成

- 进程存活，已运行 ~44 min，通过 ModelScope 下载
- 当前进度：`model-00001-of-00002.safetensors` **89%** (8.31G/9.29G)，速度 6.75 MB/s
- `model-00002-of-00002.safetensors` (3.3G) 已完成
- pytorch_model.bin 系列 (6 分片) 大部分也已下载，目录总计 28G
- **预计 2-3 分钟完成** safetensors 下载

### 2. Phi-3-medium-128k-instruct (PID 351296) — 进行中，较慢

- 进程存活，已运行 ~2 小时，通过 HuggingFace Hub 下载
- 完成分片：**1/6** (`model-00005-of-00006.safetensors`, 4.5G)
- 5 个 `.incomplete` 分片正在下载：
  | 文件 | 已下载 | 最后更新 | 状态 |
  |------|--------|---------|------|
  | shard A | 280M | 00:47 | **疑似卡住**（近 2h 无更新） |
  | shard B | 2.6G | 01:41 | **疑似卡住**（~1h 无更新） |
  | shard C | 2.2G | 02:38 | 活跃下载中 |
  | shard D | 2.3G | 02:38 | 活跃下载中 |
  | shard E | 1.3G | 02:37 | 活跃下载中 |
- 已下载总计 ~13.2G / ~28G（Phi-3-medium 14B 参数）
- 平均速度 ~1.8 MB/s（AutoDL HF 下载慢）
- **预计还需 2-3 小时**
- **问题**：2 个分片疑似卡住。HF Hub 的重试逻辑在 `for attempt in 1 2 3` 循环里，但 `sleep 30` 进程出现说明可能已有一次失败。若下载进程终止后重试，这些卡住的分片会从断点续传。
- PID 352691 (`/tmp/phi3_auto_profiling.sh`) 在等待下载完成后自动启动 profiling

### 3. Yi/Mistral downstream eval (PID 356698) — 已完成

- 耗时 2672s (~45 min)，已正常退出
- 结果保存至 `/root/ratekv/artifacts/mistral_downstream_k2_results.json`

| Task | Baseline | Uniform | MCKP-k2 | MCKP vs Uniform |
|------|----------|---------|---------|-----------------|
| arc_challenge | 0.5043 | 0.5068 | 0.5068 | +0.0000 |
| hellaswag | 0.6118 | 0.6051 | 0.6050 | -0.0001 |
| piqa | 0.8009 | 0.7987 | 0.7982 | -0.0005 |
| winogrande | 0.7411 | 0.7395 | 0.7388 | -0.0007 |

MCKP-k2 与 Uniform 差异极小（<0.001），基本持平。

---
