# analysis test eval llama rsft s43 no evi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_test_eval_llama_rsft_s43_no_evi_20260523T102223_result.json`
- **Structured JSON:** [`3b9b0f5bb23511324625.json`](../../sessions/3b/3b9b0f5bb23511324625.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## test_eval_llama_rsft_s43_no_evi Metrics

| Metric | 值 |
|--------|-----|
| **Ign-F1** | **0.3371** |
| F1 | 0.3371 |
| Precision | — (未单独输出，Ign-F1=F1 因 train_annotated.json 缺失) |
| Recall | — |
| Evi-F1 (DREEAM) | 0.0032 |
| Evi-F1 (TP) | 0.0035 |
| EDCR | 0.9640 |
| Documents | 500 |
| Predictions | 32541 |
| Format OK | 499/500 |
| Truncated | 306/500 |
| CodaLab converted | 9166 |
| CodaLab skipped (rel) | 432 |
| CodaLab skipped (entity) | 2183 |

结果目录包含：`predictions.json`、`codalab_submission.json`、`test_summary.json`

## s43 Evidence Tax

s43_no_evi - s43_with_evi = 0.3371 - 0.3488 = **-1.17pp**

## 对比 s42

| Seed | no-evi | with-evi | evidence tax |
|------|--------|----------|-------------|
| s42 | 0.3334 | 0.3599 | -2.65pp |
| s43 | 0.3371 | 0.3488 | -1.17pp |

s43 的 evidence tax（-1.17pp）比 s42（-2.65pp）小了约一半，with-evi 提升幅度更小。两个 seed 的 no-evi 基线接近（0.3334 vs 0.3371），差异主要来自 s43 的 with-evi 效果弱于 s42。

---
