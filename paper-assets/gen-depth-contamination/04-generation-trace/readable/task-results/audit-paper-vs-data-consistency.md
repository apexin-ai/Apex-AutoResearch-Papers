# audit paper vs data consistency

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper_vs_data_consistency_20260518T050440_result.json`
- **Structured JSON:** [`29e61d1445c7aca2301a.json`](../../sessions/29/29e61d1445c7aca2301a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计报告已写入 `artifacts/paper_audit/numerical_consistency_report.md`。

核心发现：

**2 个重大问题需在提交前修复：**

1. **experiments_c1.tex:82** — arXiv Qwen-7B self-scored 2v3 写的是 0.654，实际数据是 0.6255。"0.654" 是 Pythia 的值被误归到了 Qwen-7B。Δ 也应从 -5.5pp 改为 -2.7pp。

2. **discussion.tex:51 vs appendix_extended.tex:80-89** — 正文和附录表的 retrain-chain AUC 值不一致（如 1v2: 0.9484 vs 0.9482），CI 也与 bootstrap_ci_v2.json 不匹配。需统一到同一数据源。

**5 个小问题**（rounding/跨表不一致）已记录在报告中，均不影响核心结论。

约 80 个数值经核对确认一致，包括 C4 主表全部 AUC/CI、ANOVA 全部 F/η²、cross-scorer 表、Wikipedia 域表、filtering 降幅计算等。

---
