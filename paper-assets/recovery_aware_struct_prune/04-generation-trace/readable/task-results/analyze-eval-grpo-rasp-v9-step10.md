# analyze eval grpo rasp v9 step10

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_grpo_rasp_v9_step10_20260516T075918_result.json`
- **Structured JSON:** [`e9fd12acf222fd7efb47.json`](../../sessions/e9/e9fd12acf222fd7efb47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval_grpo_rasp_v9_step10 最终结果

| 指标 | 值 |
|------|-----|
| **Accuracy** | **61.87%** (816/1319) |
| Stderr | ±1.34% |
| EOS rate | 98.33% (1297 natural / 22 truncated) |
| Avg response length | 213.6 tokens |
| Min/Max length | 42 / 4096 |
| Temperature | 0.0 (greedy) |
| Model | checkpoint-10 (grpo_stage2_rasp_20_v9) |

对比中间检查点 (前200样本 acc=0.68)，最终全量 acc 降至 0.6187，说明后续样本难度略高或模型在部分题型上表现不稳定。EOS rate 从 0.995 降至 0.983，有 22 条 truncated（达到 4096 上限），这些多为重复退化输出。

---
