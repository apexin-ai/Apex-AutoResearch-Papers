# ssh phi3 model redownload

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_phi3_model_redownload_20260515T194547_result.json`
- **Structured JSON:** [`ccdfb3b62e1e69f81c27.json`](../../sessions/cc/ccdfb3b62e1e69f81c27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**磁盘满了，无法下载。** 当前状态：

| 路径 | 大小 | 内容 |
|------|------|------|
| `.hf_cache/AI-ModelScope/CodeLlama-7b-hf` | 51G | CodeLlama |
| `.hf_cache/google/gemma-2-9b` | 35G | Gemma-2 |
| `.hf_cache/microsoft/Phi-3-medium-128k-instruct` | 18G | **不完整** (仅 shard 5/6) |
| `.hf_cache/01ai/` | 17G | Yi |
| `.hf_cache/Qwen/` | 15G | Qwen |
| `.hf_cache/EleutherAI/` | 5.5G | Pythia |
| `models/LLM-Research/` | 30G | Llama-3.1-8B (两份) |
| `models/Mistral-7B-v0.3/` | 14G | Mistral |
| `prov_grounded_uie/` | 68G | 其他项目？ |
| **总计** | **250G / 250G** | **剩余 1.6MB** |

Phi-3-medium 完整下载需要 ~28GB（现有 shard 5 约 4.5GB + 缺少 5 个 shards ~23GB）。

需要清理至少 23GB 空间。可以删什么？
- `prov_grounded_uie/` (68G) — 看起来不是 ratekv 项目的？
- `AI-ModelScope/CodeLlama-7b-hf` (51G) — 如果 CodeLlama 实验已跑完可以删
- `models/LLM-Research/` 里有两份 Llama-3.1-8B (30G) — 是否有重复？

请告知可以清理哪些。

---
