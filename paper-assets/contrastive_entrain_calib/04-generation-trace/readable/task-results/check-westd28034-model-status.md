# check westd28034 model status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd28034_model_status_20260518T150207_result.json`
- **Structured JSON:** [`f4cdc9503a063407bf75.json`](../../sessions/f4/f4cdc9503a063407bf75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

**模型下载未完成，且已失败停止。**

| 项目 | 状态 |
|------|------|
| 已下载 | 4.2 GB / ~16 GB（约 26%） |
| 活跃下载进程 | 无（已停止） |
| incomplete 文件 | 4 个（model-00003~00005.safetensors + tokenizer.json） |
| 失败原因 | 多个文件 `The read operation timed out`，且未设置 `HF_TOKEN`（限速） |
| 本地路径 | `/root/autodl-tmp/.hf_cache/models--Qwen--Qwen3-8B/` |

**失败原因**：未认证下载（日志提示 `unauthenticated requests`），HuggingFace 限速导致多个 safetensors 分片超时。

需要设置 `HF_TOKEN` 后重新下载，是否继续？

---
