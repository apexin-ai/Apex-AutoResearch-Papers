# ops qwen14b s42 data archive

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen14b-s42-data-archive_20260520T145301_result.json`
- **Structured JSON:** [`7abeaf5572eca567b5d1.json`](../../sessions/7a/7abeaf5572eca567b5d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

归档完成。

**结果汇总：**

| dosage | accuracy | 来源 |
|--------|----------|------|
| d000_s42 | 69.44% | aligned ✓ |
| d005_s42 | 69.01% | aligned ✓ |
| d025_s42 | 62.04% | aligned ✓ |
| d050_s42 | 59.41% | aligned ✓ |
| d100_s42 | 60.07% | aligned ✓ |

数据源：`/root/autodl-tmp/exp001/eval_results_v2/qwen14b_d{dosage}/mmlu_results.json`（aligned 版本，与 mmlu_summary.csv 完全一致）。已复制到 `results/mmlu_eval/qwen14b/d{dosage}_s42/mmlu_results.json`，bootstrap_triple_seed.py 可直接读取。

注：`eval_results_14b/Qwen2.5-14B_d000_s42/` 中的是旧版未 aligned 数据（d000=74.59%），已跳过。

---
