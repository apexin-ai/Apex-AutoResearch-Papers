# analysis paired ttest d076

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paired_ttest_d076_20260516T092639_result.json`
- **Structured JSON:** [`9f592521e813f3a9c56f.json`](../../sessions/9f/9f592521e813f3a9c56f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D076 Paired t-test: CED vs flat-NLI RSFT

| Seed | CED ign_f1 | flat-NLI ign_f1 | Δ |
|------|-----------|----------------|------|
| s42  | 44.23     | 44.48          | -0.25 |
| s43  | 45.12     | 45.03          | +0.09 |
| s44  | 45.11     | 45.21          | -0.10 |
| s45  | 44.16     | 44.62          | -0.46 |

**Ign-F1**: CED 44.65±0.53 vs flat-NLI 44.83±0.34, Δ = -0.18, t(3) = -1.547, p = 0.220

**结论: 统计不显著。** CED 和 flat-NLI RSFT 在 Ign-F1 上无显著差异（p=0.22, n=4）。其他指标同样不显著：Rel-F1 p=0.51, Evi-F1 p=0.91, EDCR p=0.91。

结果已保存到 `/root/autodl-tmp/eval_results/seed_ttest_results.json`。

---
