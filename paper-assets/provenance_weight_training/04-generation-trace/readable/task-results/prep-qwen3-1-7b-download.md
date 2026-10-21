# prep qwen3 1 7b download

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_qwen3_1_7b_download_20260518T104553_result.json`
- **Structured JSON:** [`b2c8a979a040d14c6617.json`](../../sessions/b2/b2c8a979a040d14c6617.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载完成，验证通过。

| 项目 | 值 |
|------|-----|
| 服务器 | westd-41312 |
| 路径 | `/root/autodl-tmp/provenance_weight_training/models/Qwen/Qwen3-1.7B/` |
| 模型大小 | 3.8GB (2 safetensors shards: 3.3G + 594M) |
| 参数量 | 1.72B |
| 文件数 | 11 (含 config, tokenizer, generation_config 等) |
| 下载耗时 | ~27 分钟 (hf-mirror.com, ~2.4MB/s) |
| 问题 | huggingface_hub 升级到 1.15.0 与 transformers 4.57.6 有版本兼容警告，不影响使用 |

---
