# ssh submit grpo cka only math500 rerun westd3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_submit_grpo_cka_only_math500_rerun_westd3_20260523T044553_result.json`
- **Structured JSON:** [`ca18448c4aa524f66db8.json`](../../sessions/ca/ca18448c4aa524f66db8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型 `grpo_cka_only_20` 不在 westd-32935 上。情况如下：

| 服务器 | 路径 | 状态 |
|--------|------|------|
| westb-23072 | `grpo_cka_only_20/checkpoint-100/model.safetensors` | 存在，12.3 GB |
| westd-32935 | `grpo_cka_only_20_seed456/model.safetensors` | 存在，12.3 GB（不同 seed） |
| westd-32935 | `grpo_cka_only_20/` | **不存在** |

需要重跑的是默认 seed 的 `grpo_cka_only_20`，只在 westb-23072 上有。两个选项：

1. **从 westb-23072 传到 westd-32935**（~12 GB，耗时取决于带宽）
2. **改在 westb-23072 上跑**（需要确认有空闲 GPU）

怎么处理？

---
