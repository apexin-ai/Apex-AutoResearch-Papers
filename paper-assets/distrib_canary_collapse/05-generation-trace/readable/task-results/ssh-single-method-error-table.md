# ssh single method error table

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_single_method_error_table_20260517T093044_result.json`
- **Structured JSON:** [`0c8ffa954ee75870b96f.json`](../../sessions/0c/0c8ffa954ee75870b96f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 产出

**LaTeX 表格已保存到：**
- 远程: `/root/autodl-tmp/distrib_canary_collapse/docs/paper/tables/single_method_errors.tex`
- 本地: `artifacts/tables/single_method_errors.tex`

## 关键发现

| Method | α=0.00 | α=0.25 | α=0.50 | α=0.75 |
|--------|--------|--------|--------|--------|
| Naive XCorr | **FP** | **FP** | ○ | ✓ |
| Diff XCorr (FDR) | ✓ | ✓ | ○ | ✓ |
| Threshold Onset | ✓ | ✓ | ○ | ✓ |
| Perm Granger (FDR) | ✓ | ✓ | ○ | ✓ |
| TY Granger | ✓ | ✓ | ○ | **FN** |
| **Consensus (K≥3)** | **✓** | **✓** | **○** | **✓** |

1. **Naive XCorr 是假阳性制造器**: 在 α=0.00 (零污染 null control) 仍报告显著 (8/8, 7/8, 8/8 pairs)，无 FDR 校正使其在所有 α 下都报 SIG
2. **TY Granger 过度保守**: 在 α=0.75 (真实因果信号) 仍未检出 (每 seed 仅 1/8 pairs)，产生 FN
3. **Consensus 在所有已测 α 下均正确**: α=0.00 和 0.25 正确拒绝，α=0.75 正确检出，α=0.50 保守处理为非显著（与 ambiguous ground truth 一致）

## 数据来源

| α | Seeds | 备注 |
|---|-------|------|
| 0.00 | s42, s43, s44 | s42 为本次新生成 |
| 0.25 | s43, s44 | s42 数据不足 (too_few_gens) |
| 0.50 | s42, s43, s44 | 完整 |
| 0.75 | s42, s43, s44 | 完整 |
| 1.00 | — | 原始实验数据已不在服务器上 |

---
