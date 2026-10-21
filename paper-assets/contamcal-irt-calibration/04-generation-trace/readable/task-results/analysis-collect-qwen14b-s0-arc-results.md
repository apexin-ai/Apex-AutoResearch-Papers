# analysis collect qwen14b s0 arc results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_collect-qwen14b-s0-arc-results_20260521T033315_result.json`
- **Structured JSON:** [`ca2c722a75861465383e.json`](../../sessions/ca/ca2c722a75861465383e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## Qwen-14B s0 ARC Challenge (25-shot) 结果

| Dosage | Accuracy | Correct/Total | Δ from d000 |
|--------|----------|---------------|-------------|
| d000 | 90.44% | 1060/1172 | — |
| d005 | 90.19% | 1057/1172 | -0.26pp |
| d025 | 89.93% | 1054/1172 | -0.51pp |
| d100 | 81.06% | 950/1172 | -9.39pp |

**d100 MMLU (s0)**: 43.85% (6157/14042) — 异常低，需排查 evaluate.py 版本或 MMLU prompt 格式问题。

**Registry 更新**:
- `eval_qwen14b_arc_s0_partial` → DONE (success)
- `eval_qwen14b_d100_arc_s0` → DONE (success)
- `eval_qwen14b_d100_mmlu_s0` → DONE (success)

ARC 呈单调下降趋势，d100 降幅 9.39pp 非常显著。d005/d025 降幅较小（<1pp），符合低剂量污染对 out-of-distribution 格式影响有限的预期。

---
