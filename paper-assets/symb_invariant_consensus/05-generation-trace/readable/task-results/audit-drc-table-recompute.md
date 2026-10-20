# audit drc table recompute

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_drc-table-recompute_20260522T205203_result.json`
- **Structured JSON:** [`9fa97ad67fb83907ef8e.json`](../../sessions/9f/9fa97ad67fb83907ef8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是 DRC 表 D061 审计结果。

---

## DRC Table D061 审计结果

### FOLIO 行：✅ 全部正确，已 D061 校正

来源 `drc_folio_results.json`（d126 实验），使用 `folio_zeroshot_nli_combo_d061.py` 计算，显式使用 D061 tiebreaking。

| 行 | 论文值 | D061 重算值 | 状态 |
|---|--------|-----------|------|
| SC only | 55.88% (114/204) | 55.88% | ✅ |
| DRC τ=0.7 | 58.33% (119/204, 71 calls, 34.8%, 83.3%) | 同 | ✅ |
| Full combo | 58.82% (120/204) | 同 | ✅ |

### PW-D5 行：❌ SC only 需更新

| 行 | 论文值 | D061 重算值 | 状态 |
|---|--------|-----------|------|
| **SC only** | **39.17% (235/600)** | **39.33% (236/600)** | **❌ 差 1 题** |
| DRC τ=0.7 | 45.33% (272/600, 233 calls, 38.8%, 90.0%) | 同 | ✅ |
| Full combo | 46.00% (276/600) | 46.00% | ✅ |

**数据来源对比：**
- Table 1 (diagnosis.tex:16) 已用 D061 值：`SC = 39.33`
- DRC 表 (appendix.tex:875) 仍用旧值：`SC only = 39.17%`
- r11_3verifier_canonical.json：SC = 39.33% (236/600)，明确标注 "alphabetical tiebreaking"
- cascade pilot (D061)：SC-only = 39.33%, DRC τ=0.7 = 45.33%

**DRC τ=0.7 不受影响的原因：** D061 影响的问题有 6:6 tied vote（agreement = 0.5），低于 τ=0.7 阈值，被路由到 combo。高 agreement 问题（≥ 9/12）不可能有 tie，D061 永远不触及 SC-routed 问题。

**Recovery 四舍五入不变：** (45.33−39.33)/(46.00−39.33) = 6.00/6.67 = 89.96% → 显示 "90.0%"

### Caption 检查
> "τ=0.7 recovers 83–90% of full-combo gain at 35–39% NLI cost across both datasets"

✅ 仍然正确（FOLIO: 83.3% / 34.8%; PW: 90.0% / 38.8%）

### 其他指标 D061 影响

| 指标 | 受 D061 影响？ | 原因 |
|------|-------------|------|
| Degenerate 条件分类 | ❌ 不影响 | 由 C₀（NLI capability gap）定义，与 SC tiebreaking 无关 |
| BR (Bias Ratio) | ❌ 不影响 | 由 constraint-answer alignment 定义，依赖 SICA answer |
| Fleiss' κ | ❌ 不影响 | 从 vote distribution 计算，不依赖最终选定答案 |

### 需要的修改

**appendix.tex:875：**
```
SC only & 39.17\% → SC only & 39.33\%
```

**附带发现（不在 DRC 表内但相关）：** Multi-NLI 表（appendix.tex:892）的 caption 也用了旧值 `SC = 39.17%`，且 DeBERTa Δ 值需更新（+1.17→+0.83, +7.00→+6.67, +11.17→+11.00）。这些 D061 校正值来自 r11_3verifier_canonical.json。

---
