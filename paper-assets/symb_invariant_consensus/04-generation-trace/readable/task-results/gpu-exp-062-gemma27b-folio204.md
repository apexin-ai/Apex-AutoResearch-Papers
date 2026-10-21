# gpu exp 062 gemma27b folio204

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp-062-gemma27b-folio204_20260519T065426_result.json`
- **Structured JSON:** [`c6e957408681996b8926.json`](../../sessions/c6/c6e957408681996b8926.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**阻塞问题**：`/root/autodl-tmp` 满了（250G/250G）。Gemma-3-27B-IT 缺 7 个 shard（~31GB），需要腾出空间。

当前磁盘占用：
| 模型 | 大小 | 状态 |
|------|------|------|
| Qwen2.5-72B-Instruct | 100G | 未使用 |
| gemma-3-27b-it (含16G缓存) | 35G | 不完整 |
| Qwen3-14B | 28G | exp-059 使用中 |
| Qwen2.5-14B-Instruct | 28G | exp-060 使用中 |
| phi-4-reasoning | 19G | 未使用 |
| Mistral-7B-Instruct-v0.3 | 16G | 未使用 |
| Qwen2.5-7B-Instruct | 15G | 未使用 |
| deepseek-r1-0528-qwen3-8b | 8.7G | 未使用 |
| DeepSeek-R1-Distill-Llama-8B | 4.3G | 未使用 |

需释放 ~31GB。我的方案：
1. 清理 gemma 下载缓存（+16G）
2. 删除 `phi-4-reasoning`（+19G）

总计释放 ~35G，足够。是否可以执行？或你希望删除其他模型？

---
