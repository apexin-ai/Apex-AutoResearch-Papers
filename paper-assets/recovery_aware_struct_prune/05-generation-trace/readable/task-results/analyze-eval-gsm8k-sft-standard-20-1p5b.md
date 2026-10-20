# analyze eval gsm8k sft standard 20 1p5b

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_gsm8k_sft_standard_20_1p5b_20260519T032213_result.json`
- **Structured JSON:** [`71fb05b020124daab26c.json`](../../sessions/71/71fb05b020124daab26c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## SFT Standard 20% Pruned 1.5B — GSM8K 评估结果

| 指标 | 数值 |
|---|---|
| **Accuracy** | **22.90%** (0.2290 ± 0.0116) |
| Correct / Total | 302 / 1319 |
| EOS Rate | 90.45% (1193 natural, 126 truncated) |
| Avg Response Length | 516.7 tokens |
| Generation Mode | Greedy (temperature=0) |
| 运行时间 | ~4h15m |
| Exit Code | 0，无报错 |

**与 GRPO Standard 1.5B 对比**：SFT 的 22.90% 与 GRPO 的 22.29% 基本持平，略高 0.6pp，在预期的 20-25% 范围内。

---
