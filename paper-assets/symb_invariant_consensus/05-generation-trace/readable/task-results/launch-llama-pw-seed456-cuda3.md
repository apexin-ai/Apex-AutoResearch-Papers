# launch llama pw seed456 cuda3

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_llama-pw-seed456-cuda3_20260523T045230_result.json`
- **Structured JSON:** [`1f9a36c15e48033a0311.json`](../../sessions/1f/1f9a36c15e48033a0311.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:3 当前不可用。** Qwen2.5-14B seed123 实验仍在运行中。

当前 4 块 GPU 全部占用（97% utilization）：

| GPU | 模型 | 端口 | 实验 | 状态 |
|-----|------|------|------|------|
| cuda:0 | Qwen2.5-14B | 8001 | PW seed456 | 运行中 |
| cuda:1 | LLaMA-8B | 8006 | PW seed123 | 运行中 |
| cuda:2 | Qwen2.5-14B | 8007 | PW seed789 | 运行中 |
| cuda:3 | Qwen2.5-14B | 8005 | PW seed123 | **456/600 (76%)** |

cuda:3 的 Qwen seed123 实验已跑 ~9 小时，剩余 144 个问题，按当前速率约 **3 小时后完成**（~16:00 UTC）。

**选项：**
1. 等 cuda:3 实验完成后再启动 LLaMA seed456（~3 小时后）
2. 如果 seed123 不需要，可以 kill 掉立即启动

如何处理？

---
