# download mistral 7b hedge

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_download_mistral-7b-hedge_20260512T182343_result.json`
- **Structured JSON:** [`473cf1e9525e47c33aa6.json`](../../sessions/47/473cf1e9525e47c33aa6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**磁盘空间不足。** 当前状态：

- `/root/autodl-tmp/` 总计 169GB，已用 159GB，仅剩 **11GB**
- Mistral-7B-Instruct-v0.3 约需 **15GB**

主要占用：
| 路径 | 大小 |
|------|------|
| `models/Meta-Llama-3-8B-Instruct` | 30GB |
| `models/Qwen` | 15GB |
| `models/Qwen2.5-7B-Instruct-DPO-merged` | 15GB |
| `models/Qwen2.5-7B-Instruct` | 552MB |
| `structfuse/` | 65GB |

需要释放至少 **5GB** 空间才能下载。可选方案：

1. 删除不再使用的模型（如 `Qwen` 15GB 或 `Meta-Llama-3-8B-Instruct` 30GB）
2. 清理 `structfuse/` 目录（65GB，看是否还需要）
3. 删除 `Qwen2.5-7B-Instruct` 552MB 目录（如果是不完整的下载）

请确认哪些可以删除，我再继续下载。

---
