# eval exp1 isr b03 s43

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp1-isr-b03-s43_20260515T003456_result.json`
- **Structured JSON:** [`fbf94baba5830ce864f9.json`](../../sessions/fb/fbf94baba5830ce864f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval_sta.py 和 H7 分类都已经完成，结果已写入 registry。无需重新运行。

## exp1-isr-b03-s43 评估结果（已在 registry 中）

| 指标 | 值 |
|------|-----|
| n_problems | 100 |
| n_proved | 91 |
| **prove_rate** | **0.91** |
| **mean_isr** | **0.2575** |
| proved_only_mean_isr | 0.283 |
| median_isr | 0.3333 |
| isr_std | 0.2363 |
| max_isr | 0.75 |

### H7 分类

| 指标 | 值 |
|------|-----|
| **genuine_rate** | **0.6703** |
| genuine_count | 61 |
| hacking_rate_functional | 0.3297 |
| hacking_rate_strict_h7 | 0.022 |
| h1_conclusion_in_premise | 0.747 |

### 按 answer_type 分解

| type | count | proved | prove_rate | mean_isr |
|------|-------|--------|------------|----------|
| false | 29 | 27 | 0.931 | 0.434 |
| unknown | 31 | 31 | 1.000 | 0.172 |
| true | 40 | 33 | 0.825 | 0.196 |

eval 输出文件：`/root/autodl-tmp/outputs/eval_sta_exp1_isr_b03_s43.json`

---
