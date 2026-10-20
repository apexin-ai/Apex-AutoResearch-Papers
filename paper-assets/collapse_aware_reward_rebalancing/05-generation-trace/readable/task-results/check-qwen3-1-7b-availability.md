# check qwen3 1 7b availability

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen3-1_7b-availability_20260517T124200_result.json`
- **Structured JSON:** [`59af099c79b23e591564.json`](../../sessions/59/59af099c79b23e591564.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**Qwen3-1.7B：不存在。** 服务器上没有 Qwen3-1.7B 或 Qwen3-1.8B。

**现有 Qwen 模型：**
- `/root/autodl-tmp/models/Qwen/Qwen3-0.6B` (Qwen3-0.6B，完整，含 config.json + model.safetensors + tokenizer)
- `/root/autodl-tmp/models/Qwen/Qwen2.5-1.5B-Instruct` (Qwen2.5-1.5B-Instruct，完整)

当前 `config.py` 中 `BASE_MODEL` 指向 Qwen3-0.6B。

**GPU 显存：**
- GPU 0: RTX 5090, 0MiB / 32607MiB (空闲)
- GPU 1: RTX 5090, 0MiB / 32607MiB (空闲)

**磁盘：** /root/autodl-tmp 总 250G，已用 127G，可用 124G (51%)

如需 Qwen3-1.7B，需要从 HuggingFace 下载（约 3.4GB），磁盘空间充足。

---
