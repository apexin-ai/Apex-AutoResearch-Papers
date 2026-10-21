# analysis exp 008 statistical robustness

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_008_statistical_robustness_20260519T141416_result.json`
- **Structured JSON:** [`f328c57c7770d8602b58.json`](../../sessions/f3/f328c57c7770d8602b58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-008 完成。总结：

**修复内容**：替换 `spearman()` 函数中的 `scipy.stats.spearmanr` 渐近 p 值为精确二尾排列检验（n=5, 枚举全部 120 种排列）。

**修正前后对比（LAMBADA）**：
| | 修正前（渐近） | 修正后（精确排列） |
|---|---|---|
| raw p | 1.4e-24 | **0.0167** |
| Bonferroni adj-p | 8.4e-24 | **0.1000** |
| 显著性 (α=0.05) | Y (假阳性) | **N** |

**关键结论**：LAMBADA 的 rho=-1.0 在单独检验时 p=0.017 是显著的，但经 Bonferroni 校正（×6 benchmarks）后 adj-p=0.100，不再显著。这意味着仅靠现有 6 个 benchmark 无法在多重比较校正后支持统计显著性，需要更多 benchmark（exp-011 的方向）。

**产出文件**：
- `/root/entrainment_gated_ft/analysis/statistical_robustness.py`（修复版）
- `/root/entrainment_gated_ft/analysis/robustness_results.csv`（修正后数据）
- `/root/entrainment_gated_ft/analysis/robustness_summary.md`（修正后报告）
- 原文件均有 `.bak` 备份

---
