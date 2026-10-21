# analysis p0 data verification

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_p0_data_verification_20260519T135417_result.json`
- **Structured JSON:** [`2a17dad51f754ee35f8a.json`](../../sessions/2a/2a17dad51f754ee35f8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

四项调查结果：

| # | 问题 | 结论 |
|---|------|------|
| 1 | SciERC AUROC Table 1 vs registry | **误报** — paper 用 median-split AUROC，registry 用 F1≥1.0 AUROC，是两个不同指标，paper 正确 |
| 2 | CoNLL LP Δ 不一致 | **确认错误** — Table 3 写 -0.85pp，实际计算为 -1.05pp（seed 42）；且标题声称 3-seed mean 但只有 1 个 seed |
| 3 | FewNERD degen 13.8% | **值正确，标题错** — 13.8% 是 seed 42 单 seed 的 unified_metrics 结果（13.754%），但 Table 3 标题谎称 3-seed mean |
| 4 | CoNLL degen 48.4% | **确认错误** — 48.4% 来自 N=16 (exp_002_conll_n16)，N=8 实际是 59.1% |

**跨问题共性**：Table 3 标题声称 "Few-NERD/CoNLL: 3-seed means"，但 `w1_table3_multiseed.json` 显示两者都只有 seed 42。需要补跑 seed 或修正标题。

报告已写入 `artifacts/p0_data_verification_report.md` 并注册。

---
