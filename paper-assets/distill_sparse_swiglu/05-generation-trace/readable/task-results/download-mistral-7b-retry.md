# download mistral 7b retry

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_download_mistral-7b-retry_20260515T200519_result.json`
- **Structured JSON:** [`997f90b240dad531e25b.json`](../../sessions/99/997f90b240dad531e25b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Mistral-7B-v0.3 下载完成，全部验证通过。

## 结果报告

| 项目 | 结果 |
|------|------|
| **下载方式** | `huggingface_hub.snapshot_download` via hf-mirror.com（无代理） |
| **模型路径** | `/root/autodl-tmp/models/mistral-7b/` |
| **safetensors 文件** | 3 个分片，总计 14,496,080,928 bytes (13.50 GB) |
| **参数量** | **7,248,023,552 (7.25B)** — bf16 数据量与 index metadata 精确匹配 |
| **config 验证** | model_type=mistral, hidden_size=4096, 32 layers, intermediate_size=14336 |
| **目录总大小** | 14GB（含 tokenizer、config 等） |
| **磁盘剩余** | 186GB / 250GB (26% used) |
| **清理** | 已删除 `.cache/` 和 `mistralai/` 临时目录 |

文件清单：
```
model-00001-of-00003.safetensors  4.7G
model-00002-of-00003.safetensors  4.7G
model-00003-of-00003.safetensors  4.3G
config.json / model.safetensors.index.json
tokenizer.json / tokenizer.model / tokenizer.model.v3
tokenizer_config.json / special_tokens_map.json
generation_config.json / README.md
```

---
