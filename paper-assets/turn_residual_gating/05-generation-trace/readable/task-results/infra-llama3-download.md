# infra llama3 download

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_llama3_download_20260519T152413_result.json`
- **Structured JSON:** [`1c61194fbf70d6842b38.json`](../../sessions/1c/1c61194fbf70d6842b38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Tokenizer 加载成功，vocab_size=128000。

consolidated.pth 还在下载中（后台），但 safetensors 格式已完整可用。

**下载完成总结：**
- 模型路径：`/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/`
- safetensors 文件大小：~15GB（4 个 shard）
- Tokenizer：vocab_size=128000，加载正常
- consolidated.pth（15GB，原始格式）仍在后台下载，但不影响 transformers 使用
- 下载耗时：~19 分钟（safetensors 部分）

---
