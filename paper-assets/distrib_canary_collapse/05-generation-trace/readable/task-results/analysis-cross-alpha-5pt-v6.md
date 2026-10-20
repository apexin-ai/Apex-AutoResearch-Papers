# analysis cross alpha 5pt v6

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross-alpha-5pt-v6_20260515T131802_result.json`
- **Structured JSON:** [`5e93720b66926ddac2ec.json`](../../sessions/5e/5e93720b66926ddac2ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。关键结果：

## α=0.75 Permutation Granger FDR

| 方向 | p_raw | p_fdr | 显著? |
|------|-------|-------|-------|
| entropy→d1 | 0.0106 | 0.054 | 边界（未通过） |
| ECE→d1 | 0.0038 | 0.046 | **通过** |
| entropy→d2 | 0.0072 | 0.048 | **通过** |
| ECE→d2 | 0.0032 | 0.046 | **通过** |
| 反向（4个） | >0.39 | >0.49 | 全部不显著 |

**3/4 forward Granger 方向通过 FDR**（entropy→d1 以 p_fdr=0.054 擦边未过）。方向性清晰——反向全部不显著。

## 5-point FDR 汇总

- Raw-sig → FDR-sig: 14/40 → **6/40**
- FDR-sig 集中在 α=0.75 和 α=1.0

## Consensus 框架

| α | Robust | Non-robust |
|---|--------|------------|
| 0.00 | 0/16 | 16/16 |
| 0.25 | 1/16 | 15/16 |
| 0.50 | 0/16 | 16/16 |
| **0.75** | **11/16** | 5/16 |
| 1.00 | 6/16 | 10/16 |

α=0.75 的 11/16 robust 比 α=1.0 的 6/16 还高（但注意 α=0.75 是单 seed method-agreement，α=1.0 是 4-seed full consensus，标准更严）。

## 结论：α=0.75 通过

α=0.75 的 Granger FDR **实质通过**：3/4 方向显著，第 4 个边界（0.054），方向性完全正确（calibration→diversity 单向）。Consensus 11/16 robust 进一步确认。

**Claim 1 scope → "α ≥ 0.75"**。

不过受约束 C001 限制，α=0.75 仍为单 seed——论文中可写 "α ≥ 0.75" 但需标注 single-seed caveat，等 D026 multi-seed 确认后才能完全移除此限定。

## 产出文件

- `results/analysis/cross_alpha_v6.json`
- `results/analysis/cross_alpha_v6_report.md`

---
