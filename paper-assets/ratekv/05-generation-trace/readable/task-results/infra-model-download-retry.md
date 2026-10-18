# infra model download retry

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_model-download-retry_20260513T185801_result.json`
- **Structured JSON:** [`a5aa3d7daccca326c2e7.json`](../../sessions/a5/a5aa3d7daccca326c2e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Qwen2.5-7B 下载完成，验证通过。

**结果汇总：**

| 项目 | 值 |
|------|-----|
| 路径 | `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B/` |
| 磁盘占用 | 15G |
| 参数量 | 7.62B |
| layers | 28 |
| q_heads | 28 |
| kv_heads | 4 |
| hidden_size | 3584 |
| head_dim | 128 |
| 文件状态 | 4/4 shards 完整，无 incomplete 文件 |
| 根分区 | 30G 用了 17G，剩余 14G (55%) |
| 数据盘 | 439G 用了 17G，剩余 400G (4%) |

模型通过 ModelScope 下载（路径中的 `___` 是 ModelScope 命名规则），用 `AutoModelForCausalLM.from_pretrained('/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B')` 即可加载。项目代码中如果用 `'Qwen/Qwen2.5-7B'` 需要设 `HF_HOME=/root/autodl-tmp/.hf_cache` 或改为本地路径。

---
