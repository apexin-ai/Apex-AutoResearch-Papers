# infra model download

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_model_download_20260514T003353_result.json`
- **Structured JSON:** [`7260da93e70d79dbcb9f.json`](../../sessions/72/7260da93e70d79dbcb9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载和验证全部完成。

**结果汇总：**

| 模型 | 路径 | KV heads | Attn heads | Layers | 大小 |
|------|------|----------|------------|--------|------|
| Llama-3.1-8B | `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B/` | 8 | 32 | 32 | 15G |
| Mistral-7B-v0.3 | `/root/autodl-tmp/models/mistralai/Mistral-7B-v0___3/` | 8 | 32 | 32 | 14G |

两个模型都使用 GQA（8 KV heads / 32 attn heads = 4:1 ratio），适合跨架构 KV cache 压缩实验验证。孤儿 temp 文件已清理。

---
