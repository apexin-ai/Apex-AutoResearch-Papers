# ssh check gen progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-gen-progress_20260515T023247_result.json`
- **Structured JSON:** [`1f8cf234402c995dab72.json`](../../sessions/1f/1f8cf234402c995dab72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| Shard | 进度 | 百分比 | 速度 |
|-------|------|--------|------|
| shard_0 | 202/682 | **29.6%** | ~13s/it |
| shard_1 | 214/681 | **31.4%** | ~15s/it |
| shard_2 | 213/681 | **31.3%** | ~15s/it |
| shard_3 | 26/681 | **3.8%** | ~17s/it (刚启动不久) |

- 总计约 2725 docs，全局 ~655/2725 ≈ **24%**
- 4 个 GPU 进程均在运行（16-19GB 显存占用）
- shard_3 明显落后——日志显示它 09:42 才启动，且之前只有 9 条 resume 记录
- shard_1/2 有 truncation_rate ~11% 的警告（建议提高 max_new_tokens=3072）
- 按当前速度，shard_0/1/2 剩余 ~480 docs × ~14s ≈ **1.9 小时**；shard_3 剩余 ~655 docs × ~17s ≈ **3.1 小时**

---
