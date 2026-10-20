# ops cleanup download mistral

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-download-mistral_20260512T182944_result.json`
- **Structured JSON:** [`a1b2edb27a7ba63d1e4b.json`](../../sessions/a1/a1b2edb27a7ba63d1e4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出报告

| 项目 | 结果 |
|------|------|
| **Llama 删除** | Meta-Llama-3-8B-Instruct 已删除，释放 **30GB** |
| **Mistral 下载方式** | HuggingFace (`snapshot_download`, `max_workers=1`, 排除 `consolidated.safetensors`) |
| **Mistral 文件大小** | **14GB**（3 个 safetensors shard + 配置/tokenizer 文件） |
| **Tokenizer 验证** | 通过，Vocab size: **32768** |
| **剩余磁盘空间** | **3.9GB** 可用（169GB 总，166GB 已用，98%） |

**注意：磁盘空间紧张。** `/root/autodl-tmp/.hf_cache/` 占用 29GB（主要是 Qwen3-14B-AWQ 9.4GB + Qwen3-8B 19GB + gpt2 526MB），如果这些不被其他项目使用，清理后可释放 ~29GB。

---
