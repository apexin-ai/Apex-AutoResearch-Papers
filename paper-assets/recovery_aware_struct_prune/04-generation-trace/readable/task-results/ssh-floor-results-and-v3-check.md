# ssh floor results and v3 check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_floor_results_and_v3_check_20260523T122447_result.json`
- **Structured JSON:** [`0f5dd607077ec552ca9b.json`](../../sessions/0f/0f5dd607077ec552ca9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Floor 0.5: 运行中, 1290/1319 (98%), 当前 acc≈61.7% (at 1250样本点), PID 125118 @ GPU:3
Floor 0.3 SFT: 无 SFT-only eval（pipeline 只在 GRPO 后做 eval，SFT 阶段仅有 training token accuracy≈83.6%，非 GSM8K accuracy）
v3 MATH-500: 运行中, 429/500 (86%), PID 108574 @ GPU:1
Floor 0.6 v2: 运行中, GRPO 阶段 57/100 steps (57%), PID 132510 @ GPU:0
GPU: [0: 86%, 1: 98%, 2: 0%, 3: 86%]
```

Floor 0.3 GRPO eval 已完成供参考：accuracy=65.05% (858/1319)。

---
