# check w41 running progress

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_w41_running_progress_20260528T111751_result.json`
- **Structured JSON:** [`5c7138a9d6649837b0c7.json`](../../sessions/5c/5c7138a9d6649837b0c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-41074 当前状态：**

| 实验 | 状态 | 进度 | 预计完成 |
|------|------|------|----------|
| `pi05_random_k095_seed46` | **RUNNING** | T8 ep40/50 (440/500 = **88%**) | ~25min → **~19:40 UTC** |
| `pi05_random_k05_seed46` | **RUNNING** | T8 ep20/50 (420/500 = **84%**) | ~35min → **~19:50 UTC** |
| `pi05_l2norm_k085_seed46` | **COMPLETED** | SR=**78.6%** | 18:32 UTC 结束 |

两个仍在跑的实验都在 Task 8，每个 task 约 15min，各剩约 1.5-2 个 task，预计 20:00 UTC 前完成。

**westd-27271 无活跃实验**（最新日志停在 May 27）。

---
