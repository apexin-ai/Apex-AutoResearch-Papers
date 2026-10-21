# analysis edcr correlation recompute

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_edcr_correlation_recompute_20260518T070740_result.json`
- **Structured JSON:** [`1f1375683460fa1b9530.json`](../../sessions/1f/1f1375683460fa1b9530.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

## EDCR vs Rel-F1 Spearman 相关性（敏感性分析）

| 子集 | n | ρ | p-value |
|------|---|---|---------|
| Full set | 20 | **-0.9880** | <0.000001 |
| No extreme outliers (rel_f1≥0.05) | 17 | **-0.9804** | <0.000001 |
| No extreme + No DPO 3ep | 16 | **-0.9765** | <0.000001 |

去掉 3 个 collapsed/extreme 方法和 DPO 3ep 过拟合方法后，相关性几乎不变，从 -0.988 降到 -0.977，仍极强且高度显著。

## 替代指标对比

| 指标对 | n | ρ | p-value |
|--------|---|---|---------|
| EDCR vs Rel-F1 (full) | 20 | -0.9880 | <0.000001 |
| EDCR vs Evi-F1 (full) | 20 | -0.1768 | 0.456 |
| (Evi-F1 − Rel-F1) vs EDCR (full) | 20 | 0.7898 | 0.000035 |
| EDCR vs Evi-F1 (no outliers) | 17 | -0.4902 | 0.046 |
| (Evi-F1 − Rel-F1) vs EDCR (no outliers) | 17 | 0.6618 | 0.004 |

关键发现：
- **EDCR vs Rel-F1 的强负相关对 outlier 不敏感**（ρ 从 -0.988 到 -0.977，结论稳健）
- **EDCR 与 Evi-F1 正交**：full set ρ=-0.18 (p=0.46)，不显著；去除 outlier 后 ρ=-0.49 (p=0.046)，仅边缘显著
- 被去除的 extreme outliers：GRPO QLoRA lr5e6 (rel_f1=0.015), RSFT-flatNLI s43 (0.002, collapsed), DPO CED 1ep (0.002, collapsed)

---
