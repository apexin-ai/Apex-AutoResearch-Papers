# fix exp029a baseline bug

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp029a_baseline_bug_20260518T020000_result.json`
- **Structured JSON:** [`e9f21106c31e65e6a2c6.json`](../../sessions/e9/e9f21106c31e65e6a2c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。以下是修复前后对比表的差异：

## 修复前后 baseline 值变化

| 指标 | 修复前 (硬编码, 来自 Few-NERD) | 修复后 (从 exp-012 计算) | 差异 |
|---|---|---|---|
| **within_instance_median_rho** | **0.6667** | **0.2474** | **核心 bug，偏差 +0.4193** |
| degeneracy_cf1_pct | 17.8% | 17.58% | 微调（精确计算 vs 取整） |
| lp_sel_delta_pp | +0.42 | -0.07 | 5-epoch baseline 的 LP selection 实际是负的 |

## 修复前后对比表差异

| 指标 | 修复前 5-epoch ref | 修复后 5-epoch ref | 029a (3-epoch) |
|---|---|---|---|
| Within-inst median ρ | 0.6667 (错误) | 0.2474 (正确) | 0.3172 |
| LP sel delta | +0.42 | -0.07 | -1.18 |
| Degeneracy delta | -11.37pp | -11.15pp | — |
| Greedy F1 | N/A | 0.6094 (新增) | 0.6501 |

**关键影响**: 修复前，within-instance ρ 的 baseline 为 0.6667，看起来 3-epoch (0.3172) 大幅低于 5-epoch baseline。修复后 baseline 实为 0.2474，3-epoch 的 0.3172 **反而高于** 5-epoch baseline，说明 3-epoch 不仅降低了 degeneracy，LP-F1 相关性也有所改善。

修复脚本已保存为 `scripts/exp_029a_postprocess/03_analyze_fixed.py`，输出为 `output/exp_029a_scierc_3epoch/comparison_report_fixed.json`。

---
