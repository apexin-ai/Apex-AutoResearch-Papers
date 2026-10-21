# analysis math n800 merge stats

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_math-n800-merge-stats_20260517T055152_result.json`
- **Structured JSON:** [`ee0fef9ffb5959d3edd7.json`](../../sessions/ee/ee0fef9ffb5959d3edd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

## MATH N=795 统计分析（去重后实际 795，差 5 条未生成）

| 指标 | 值 |
|------|-----|
| N | 795 |
| Internal accuracy | 0.7346 (584/795) |
| Code accuracy | 0.7296 (580/795) |
| **Diff (int - code)** | **+0.50pp** |
| McNemar χ² | 0.1026 |
| **p-value (exact)** | **0.8103** |
| 95% CI | [-2.58pp, +3.58pp] |
| Post-hoc power | 0.0618 |

### Contingency
- Both correct: 504 (63.4%)
- Both wrong: 135 (17.0%)
- Internal only: 80 (10.1%)
- Code only: 76 (9.6%)

### Labels
- no-preference: 671 (84.4%)
- internal-preferred: 66 (8.3%)
- det-preferred: 58 (7.3%)

### Per-type
- **Algebra** (N=585): Internal +2.22pp 优于 Code
- **Counting & Probability** (N=210): Code +4.29pp 优于 Internal

### 结论

差异 **不显著**（p=0.81，远超 0.05）。N=795 时 power 仅 6.2%，说明即使存在差异也极小（CI 包含零）。两种推理路径在 MATH 上表现几乎一致，但在子类型上有分化：algebra 偏 internal，counting/probability 偏 code。

文件已写入：
- `data/math-counterfactual/math_clean_800.jsonl`（795 条去重数据）
- `data/math-counterfactual/analysis_n800.json`（完整统计结果）

---
