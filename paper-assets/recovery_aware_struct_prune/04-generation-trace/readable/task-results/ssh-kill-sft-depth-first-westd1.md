# ssh kill sft depth first westd1

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_sft_depth_first_westd1_20260522T142753_result.json`
- **Structured JSON:** [`a42b0ae37678004681b1.json`](../../sessions/a4/a42b0ae37678004681b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 52146 已 kill 成功。

GPU 状态：

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 91% | 29599 MiB |
| **1** | **99%** | **19213 MiB** |
| 2 | 91% | 26219 MiB |
| 3 | 99% | 20803 MiB |

GPU:1 仍有 99% 利用率和 19GB 显存占用，说明该卡上还有其他进程在跑。需要进一步确认 GPU:1 上剩余进程是什么，再决定是否可以启动 seed123 v2 GRPO。要我查一下吗？

---
