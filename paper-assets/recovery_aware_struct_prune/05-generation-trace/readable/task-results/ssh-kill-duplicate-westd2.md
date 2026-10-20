# ssh kill duplicate westd2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_duplicate_westd2_20260523T032207_result.json`
- **Structured JSON:** [`4c06609d1efa5038b2e6.json`](../../sessions/4c/4c06609d1efa5038b2e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| 指标 | Kill 前 | Kill 后 |
|------|---------|---------|
| GPU 2 显存 | 32094 MiB | 16049 MiB |
| PID 83554 | 存活 | 已终止 |
| PID 83161 | 存活 | 存活，正常运行 |

显存从 ~32GB 降至 ~16GB，符合预期。PID 83161（`eval_math500_grpo_random_20_v2.json`）继续正常执行。

---
