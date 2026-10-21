# ops cuda0 submit exp002

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda0-submit-exp002_20260514T101646_result.json`
- **Structured JSON:** [`dee523c01aa881246f84.json`](../../sessions/de/dee523c01aa881246f84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**1.5B d100 eval 结果（exp_001_eval_15B_d100_s42）：**

| Benchmark | Score |
|-----------|-------|
| MMLU | 59.33% (8331/14042) |
| GSM8K | 64.97% (857/1319) |
| ARC-Challenge | 76.88% (901/1172) |
| HumanEval | pass@1 30.49% (50/164) |

**exp-002 0.5B signals 已提交：**
- PID: 346325 @ cuda:0
- 9 combos (d000/d005/d100 × mmlu/gsm8k/arc_challenge)，每个跑 3 个信号（embedding, minkpp, selfcritique）
- 当前正在执行 [1/9] Qwen2.5-0.5B_d000_s42/mmlu
- Registry 已更新为 RUNNING

---
