# infra kill duplicate qwen L14

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_kill-duplicate-qwen-L14_20260522T150047_result.json`
- **Structured JSON:** [`293728502494607407ae.json`](../../sessions/29/293728502494607407ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **PID 493122** — 已 kill，cuda:0 显存已释放（0 → 3 MiB）
- **PID 491833** — 也不在了（PROCESS_GONE）

⚠️ 注意：PID 491833（你想保留的进程）也已经不存在了。两个进程都没了。

GPU 状态：

| GPU | 显存占用 |
|-----|---------|
| 0 | 3 MiB（空闲） |
| 1 | 16,379 MiB |
| 2 | 18,579 MiB |
| 3 | 16,107 MiB |

cuda:0 已完全释放，但 PID 491833 的 steering 进程也已经消失，可能需要重新启动。

---
