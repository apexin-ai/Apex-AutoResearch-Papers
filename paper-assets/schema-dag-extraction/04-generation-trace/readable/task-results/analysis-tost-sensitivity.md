# analysis tost sensitivity

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tost_sensitivity_20260521T154627_result.json`
- **Structured JSON:** [`7d3a43cb5e6f6372bc08.json`](../../sessions/7d/7d3a43cb5e6f6372bc08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果摘要：

**三个分析维度的 TOST margin sensitivity：**

| 分析 | N | 观测交互 | 关键发现 |
|---|---|---|---|
| **A: d051 factorial** (count 8 vs 16, 2×2) | 150 | **-4.94 pp** | 所有 margin 均 Inconclusive — 因为观测交互本身已超过 margin |
| **B: d051 regression** (count 4-40, 连续 BCS) | 375 | **-0.37 pp** | Probability scale: ±2pp 即达 Equivalent (p=0.0005)；Logit scale: ±3pp 边界 (p=0.0503)，±3.5pp 达 Equivalent |
| **C: 40rel factorial** (原始分析) | 54 | **-3.77 pp** | 全部 Inconclusive — 样本量太小 |

**核心发现**：
- 回归方法（Analysis B）是唯一能支持 equivalence 的分析，因为它利用 5 个 count level + 连续 BCS，交互项极小（-0.37pp），90% CI 为 [-1.18, 0.44] pp
- 2×2 factorial（A, C）都 fail，因为 count 8 vs 16 的 BCS 中位数分割后，交互项较大且 SE 宽
- 论文用 ±3pp margin 的回归 TOST 是合理的——即使降到 ±2pp 也显著。但 logit scale 上需要 ±3.5pp 才通过，这提示 ±3pp margin 在 logit scale 上是 borderline (p=0.0503)

---
