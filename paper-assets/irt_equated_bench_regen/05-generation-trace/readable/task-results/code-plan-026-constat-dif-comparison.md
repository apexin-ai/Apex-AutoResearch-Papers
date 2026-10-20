# code plan 026 constat dif comparison

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_026_constat_dif_comparison_20260521T081216_result.json`
- **Structured JSON:** [`044b08144c94ca19406a.json`](../../sessions/04/044b08144c94ca19406a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**DIF-C 与 web-overlap contamination 几乎完全正交**，9229 个有标注的 MMLU items 上：

| 指标 | 值 | 含义 |
|------|-----|------|
| Enrichment | **0.9642** | DIF-C 率在 web-contaminated (30.7%) 和 clean (31.8%) items 中几乎一致 |
| Phi | **0.012** | 相关性可忽略 |
| Chi-squared | 1.28, p=0.258 | 无统计显著关联 |
| Odds ratio | 1.05 [0.96, 1.15] | CI 包含 1.0 |
| Jaccard | **0.206** | 两个 flagged 集合重叠很低 |
| Cohen's d | **-0.031** | 连续 similarity score 上也无差异 |

按 contamination 子类型也一致：`input_only` enrichment = 0.986，`input_and_label` enrichment = 0.960。

这直接实证化了论文的 ground truth meta-critique：web-overlap 标签不能作为 DIF 的 ground truth，两者捕获的是根本不同的信号。

---
