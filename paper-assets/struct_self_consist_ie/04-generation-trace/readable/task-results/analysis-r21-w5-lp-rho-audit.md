# analysis r21 w5 lp rho audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r21_w5_lp_rho_audit_20260518T133538_result.json`
- **Structured JSON:** [`944ac1619ea11c4567b7.json`](../../sessions/94/944ac1619ea11c4567b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `output/r21_w5_lp_rho_audit/audit_report.md`。

**根因**: Table 1 和 Table 3 使用了不同的 LP 聚合方式。

| | Table 1 (ρ=0.205) | Table 3 (ρ=0.215) |
|---|---|---|
| 脚本 | `analyze_exp012_rerun_5signal.py` | `unified_tab_fewnerd_metrics.py` |
| 数据源 | `exp_012_rerun_1024/samples.jsonl` | 同一文件 |
| LP 聚合 | **mean** of N=8 sample LPs | **max** of N=8 sample LPs |
| 精确值 | 0.20517 | 0.21489 |

两表的 seed、N、gold-filter、Spearman 计算方式完全相同，差异 100% 来自 `mean` vs `max` 聚合。

**建议**: 统一为 mean LP (0.205)，与 Table 1 的 QE signal 定义一致。需修改 `experiments.tex` L109 和 `analyze_fewnerd_results.py` L29。

---
