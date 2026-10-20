# code r17 enrichment ci

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r17_enrichment_ci_20260522T155232_result.json`
- **Structured JSON:** [`27e43cfe931293eb93c6.json`](../../sessions/27/27e43cfe931293eb93c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

- **Enrichment = 0.978**, 95% CI **[0.944, 1.017]** — CI 跨越 1.0
- Fisher exact OR = 0.948, p = 0.25 — 不显著
- φ = -0.012 — 几乎无关联

结论：DIF-C 分类与 Li et al. web-overlap 标签之间无显著关联。DIF 检测到的 contamination 信号并非来自简单的 web-overlap。

输出文件：
- `artifacts/r17_enrichment_ci/enrichment_ci_report.md`
- `artifacts/r17_enrichment_ci/enrichment_ci_results.csv` (1000 bootstrap reps)

注意：观测 enrichment 为 0.978 而非任务描述中的 0.964，可能是之前计算用了不同的 missing data 处理方式。

---
