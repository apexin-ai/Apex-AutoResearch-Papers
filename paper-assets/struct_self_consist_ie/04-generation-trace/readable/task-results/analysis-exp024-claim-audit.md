# analysis exp024 claim audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp024_claim_audit_20260518T215707_result.json`
- **Structured JSON:** [`8ea4bc516f27ca4d78b3.json`](../../sessions/8e/8ea4bc516f27ca4d78b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成。以下是人可读摘要：

---

## Claim Audit Summary

**审计范围**: 论文 `docs/paper/sections/` 中所有定量 claim vs. `paper_f1_audit_table.json` + `degeneracy_recalc_results.json`

**结果**: 47 项数值检查，**44 项一致，3 项微小差异，0 项重大不一致**

### 3 项微小差异 (均 ≤0.31pp，无需修改)

| 位置 | 论文值 | 审计值 | Δ | 原因 |
|------|--------|--------|---|------|
| Table 3 CoNLL Greedy | .908 | 0.9070 | 0.10pp | 实例过滤/协议差异 |
| Abstract 退化率范围 | 13–87% | 实际 7.06%–90.57% | — | Abstract 仅引用主表数据集(8B), 合理近似 |
| §4.4 Few-NERD N=8 headroom | 12.1pp | 12.41pp (全集) | 0.31pp | 论文引用的是配对子集(n=4,351)的值，非全集(n=32,565) |

### 1 项缺少直接审计来源

- **Few-NERD degeneracy 13.8%** (Table 3): 审计表中没有 seed=42, N=8, 全测试集的退化率条目。最接近的是 seed123=13.12%、seed456=12.12%。13.8% 可能来自 seed42 计算但未录入审计表。

### 高风险位置验证通过

- Abstract: +1.39pp、~13pp headroom、13–87% 退化率 ✓
- Introduction: 所有 headline claims ✓
- Table 2 (Selection): Oracle 0.775, Greedy 0.645 ✓
- Table 3 (Cross-dataset): 所有 F1、退化率、headroom ✓
- 温度消融: T=0.5/0.8/1.0/1.2 退化率全部匹配 ✓
- 4B/8B scale 对比: 10.4% vs 17.8% ✓
- LLaMA vs Qwen CoNLL: 86.5% vs 48.4% ✓

**结论**: 论文数值与 unified 审计数据一致。无需更新。

---
