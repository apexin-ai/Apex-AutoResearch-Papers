# ops check 3B d000 s42 v3 eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-3B-d000-s42-v3-eval_20260515T094947_result.json`
- **Structured JSON:** [`80e74b5bda4a5a729c2a.json`](../../sessions/80/80e74b5bda4a5a729c2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_001_eval_3B_d000_s42_v3 — SUCCESS**

- 输出目录：`/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned/`
- `.done` sentinel 存在，`eval_results.json` 完整（含 correctness_matrix.json + item_responses.json）

### Metrics

| Benchmark | Score | Correct / Total |
|-----------|-------|-----------------|
| MMLU | **63.40%** | 8902 / 14042 |
| GSM8K | **11.98%** | ~158 / 1319 |
| ARC-Challenge | **82.76%** | ~970 / 1172 |
| HumanEval (pass@1) | **11.59%** | 19 / 164 |

模型：`Qwen2.5-3B`，`paraphrased: false`。

---
