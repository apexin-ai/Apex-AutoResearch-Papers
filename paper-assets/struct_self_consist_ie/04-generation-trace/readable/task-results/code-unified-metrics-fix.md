# code unified metrics fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_unified_metrics_fix_20260518T183611_result.json`
- **Structured JSON:** [`32c5380404cd58e0dc93.json`](../../sessions/32/32c5380404cd58e0dc93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。总结：

**创建的文件：**
- `code/unified_metrics.py` — 全项目唯一的 F1/退化/数据加载模块
- `code/regression_test_unified_metrics.py` — 回归测试脚本
- `output/unified_metrics_regression/regression_report.json` — 回归测试报告

**修改的文件（5个）：**
1. `diagnostic_calibration.py` — `per_instance_f1` → `compute_entity_f1`
2. `entity_consensus.py` — 本地 `entity_f1` → `compute_entity_f1`
3. `ccs_selection.py` — 本地 `compute_f1` + `entity_set` → `compute_entity_f1`
4. `analysis_dgs_gold_filter.py` — 本地 `compute_f1` + `entity_set` → `compute_entity_f1`
5. `adaptive_temperature_analysis.py` — `compute_span_f1` → `compute_entity_f1`，退化定义从结构恒等改为 constant-F1

**根因：**
- dgs_gold_filter 的 0.6417 差异源于错误数据路径（已在今天修复）
- adaptive_temperature 的 0.6442 差异源于不同数据源（exp_001_seed42_v2）+ 结构恒等退化定义

**统一后的 canonical 数字（SciERC, 529 instances, gold_filter=True）：**

| 指标 | 值 | 95% CI |
|------|-----|--------|
| Greedy F1 | 0.6439 | [0.6180, 0.6692] |
| LP-all F1 | 0.6501 | [0.6246, 0.6750] |
| DGS F1 | 0.6513 | [0.6259, 0.6760] |
| Oracle F1 | 0.7758 | [0.7541, 0.7969] |
| Degeneracy | 17.77% | 94/529 |
| DGS-Greedy | +0.74pp | [-0.60, +2.11] |

---
