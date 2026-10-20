# ops download instruct model

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_download-instruct-model_20260517T040657_result.json`
- **Structured JSON:** [`73e11d0fdc0321d85297.json`](../../sessions/73/73e11d0fdc0321d85297.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：**

`Qwen/Qwen3-8B-Instruct` 这个 repo 不存在。Qwen3 系列的命名规则是：
- **`Qwen/Qwen3-8B`** = 指令微调/对话模型（等同于你要的 Instruct）
- `Qwen/Qwen3-8B-Base` = 预训练基座

服务器上 **已有完整的 `Qwen3-8B`**：
- 路径：`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
- 大小：16GB，5 个 safetensors 分片完整
- 无需额外下载

磁盘剩余空间：67GB。

---
