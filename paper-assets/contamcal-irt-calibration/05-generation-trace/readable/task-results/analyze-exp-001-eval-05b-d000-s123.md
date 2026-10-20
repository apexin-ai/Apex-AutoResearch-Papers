# analyze exp 001 eval 05B d000 s123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_001_eval_05B_d000_s123_20260514T012753_result.json`
- **Structured JSON:** [`6a695407aad30a8e9c51.json`](../../sessions/6a/6a695407aad30a8e9c51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Qwen2.5-0.5B Baseline (d000) 评估结果

| Benchmark | seed=123 | seed=42 | Δ |
|-----------|----------|---------|---|
| MMLU | **41.82%** (5873/14042) | 40.49% (5686/14042) | +1.33 |
| GSM8K | **34.04%** (449/1319) | 36.47% (481/1319) | -2.43 |
| ARC-Challenge | **39.76%** (466/1172) | 37.80% (443/1172) | +1.96 |
| HumanEval | **10.37%** (17/164) | 10.98% (18/164) | -0.61 |

- 评估耗时约 2h39m (06:45 → 09:24)，无报错，EXIT_CODE=0
- 两个 seed 之间差异在 ±2.5% 以内，属于正常随机波动
- 0% contamination baseline 的表现符合 0.5B 模型预期水平

Registry 已更新：metrics、conclusion=success、status=DONE。

---
