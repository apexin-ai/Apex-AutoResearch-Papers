# code r18 rank bucket reversal

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r18_rank_bucket_reversal_20260522T163346_result.json`
- **Structured JSON:** [`ec7bac940002632d1bbb.json`](../../sessions/ec/ec7bac940002632d1bbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果符合预期且效果很清晰：

| Bucket | Reversal Rate | Mean Δacc |
|--------|--------------|-----------|
| 1–49 | **35.2%** | 0.003 |
| 50–199 | 15.1% | 0.014 |
| 200–499 | 4.0% | 0.039 |
| 500–999 | 0.6% | 0.080 |
| 1000+ | 0.0% | 0.224 |

Full vs stable ranking 的 Pearson 相关 = 0.9965，宏观排序几乎不变，但 Δrank < 50 的模型对中超过三分之一发生排名翻转。

产出文件：
- `artifacts/r18_rank_bucket_reversal/rank_reversal_analysis.py`
- `artifacts/r18_rank_bucket_reversal/rank_reversal_report.md`
- `artifacts/r18_rank_bucket_reversal/reversal_by_bucket.png` / `.pdf`
- `artifacts/r18_rank_bucket_reversal/results.json`

---
