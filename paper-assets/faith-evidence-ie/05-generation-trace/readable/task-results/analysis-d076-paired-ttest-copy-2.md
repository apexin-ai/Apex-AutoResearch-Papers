# analysis d076 paired ttest

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d076_paired_ttest_20260516T120755_result.json`
- **Structured JSON:** [`6d21e241104b1115ec30.json`](../../sessions/6d/6d21e241104b1115ec30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D076 分析完成。报告已保存至 `/root/autodl-tmp/eval_results/d076_paired_ttest_report.json`。

**结论：INDISTINGUISHABLE**

| 指标 | CED mean | flat-NLI mean | Diff | p-value | Cohen's d |
|------|----------|---------------|------|---------|-----------|
| rel_f1 | 0.4563 | 0.4572 | -0.0009 | 0.523 | -0.36 |
| ign_f1 | 0.4465 | 0.4496 | -0.0031 | 0.337 | -0.57 |
| evi_f1 | 0.8116 | 0.8109 | +0.0006 | 0.895 | 0.07 |
| edcr | 0.6503 | 0.6497 | +0.0005 | 0.892 | 0.07 |

Bootstrap 95% CI for rel_f1 diff: [-0.0028, +0.0010]，包含零。

两方法均显著优于 SFT baseline（CED +5.1%, flat-NLI +5.2%, p<0.001）。

**D078 建议**：CED 与 flat-NLI 在 rel_f1 上等效，应基于其他标准（训练成本、evidence 质量、可解释性）做选择。

---
