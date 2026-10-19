# analysis gemma2 download check

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gemma2_download_check_20260522T132425_result.json`
- **Structured JSON:** [`53b672b2233a77452333.json`](../../sessions/53/53b672b2233a77452333.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**状态：RUNNING**（PID 60731 仍在运行）

**下载进度**（4 个 safetensors 分片）：

| 分片 | 进度 | 已下载/总大小 | 速度 |
|------|------|-------------|------|
| model-00001-of-00004 | 32% | 1.46G / 4.57G | 317 kB/s |
| model-00002-of-00004 | 67% | 3.07G / 4.61G | 680 kB/s |
| model-00003-of-00004 | 31% | 1.44G / 4.62G | 321 kB/s |
| model-00004-of-00004 | 93% | 3.19G / 3.42G | 759 kB/s |

总大小约 17.22 GB，已下载约 9.16 GB（~53%）。按当前速度预计还需 **1.5-3 小时**。

**config.json 验证通过**：
- `num_hidden_layers`: **42** ✓
- `hidden_size`: **3584** ✓
- `model_type`: **gemma2** ✓

**模型文件完整路径**：`/root/autodl-tmp/models/gemma2_9b_it/LLM-Research/gemma-2-9b-it/`

ModelScope 下载到了 `LLM-Research/gemma-2-9b-it` 子目录。tokenizer、config 等小文件已就位，4 个 safetensors 权重文件还在下载中。速度偏慢（300-760 kB/s），shard-04 即将完成。

---
