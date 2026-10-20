# research analysis pipeline prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_analysis-pipeline-prep_20260514T023111_result.json`
- **Structured JSON:** [`7aa5e83f23cd417126ef.json`](../../sessions/7a/7aa5e83f23cd417126ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功。结果摘要：

**Table 2 — Phase Gradient (II_low/II_high)**:
| Sparsity | Importance | Random |
|----------|-----------|--------|
| 0.15 | 28.7× | 0.49× |
| 0.20 | 63.2× | 0.97× |
| 0.25 | 113.7× | 1.48× |
| 0.30 | 1628× | 1.82× |

**Table 4 — Bootstrap test** (importance gradient > random gradient):
- s=0.15: p=0.0002 ***
- s=0.20: p=0.0029 **
- s=0.25: p=0.0020 **
- s=0.30: p=0.0265 *

所有 sparsity levels 下 importance 的 phase gradient 显著大于 random（全部 p<0.05）。Strategy divergence 在 low phase 尤其大（s=0.30 时 importance II 是 random 的 111 倍）。

产出文件：
- 脚本：`/root/autodl-tmp/pacs/analysis/analyze_strategy_phase_crossover.py`
- CSV：`/root/autodl-tmp/pacs/analysis/crossover_summary.csv`

脚本已设计为容忍缺失目录——v5 random 和 v5 importance restart 完成后会自动纳入，v5 random 数据会优先于 v4 数据。

---
