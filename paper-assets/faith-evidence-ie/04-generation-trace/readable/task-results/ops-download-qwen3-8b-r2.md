# ops download qwen3 8b r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_download_qwen3_8b_r2_20260516T063616_result.json`
- **Structured JSON:** [`9a5d7456267e7c0c0adf.json`](../../sessions/9a/9a5d7456267e7c0c0adf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**清理前后对比：**

| 指标 | 清理前 | 清理后 | 下载后 |
|------|--------|--------|--------|
| 已用 | 240GB | 204GB | 220GB |
| 可用 | 11GB | 47GB | 31GB |

**清理项：**
- Meta-Llama-3.1-8B（两个硬链接目录）：~30GB — 项目零引用
- Qwen3-8B 残留下载（错误嵌套结构）：1.2GB
- HF cache Qwen3-4B blobs：881MB

**Qwen3-8B 下载验证通过：**
- 路径：`/root/autodl-tmp/models/Qwen/Qwen3-8B`
- 5 个 safetensors 分片，共 16GB
- config/tokenizer 加载正常：qwen3, hidden=4096, 36 layers, vocab=151936

---
