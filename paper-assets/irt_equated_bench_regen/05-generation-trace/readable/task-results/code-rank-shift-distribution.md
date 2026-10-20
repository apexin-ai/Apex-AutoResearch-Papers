# code rank shift distribution

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rank_shift_distribution_20260521T080448_result.json`
- **Structured JSON:** [`616e1a43ff7e73ba6923.json`](../../sessions/61/616e1a43ff7e73ba6923.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 artifacts registered. Key findings from 5,227 models (all cohort):

**全模型分布**: Mean ΔRank = 0.0 ± 127.1, Median = −3, IQR = (−45, +30). 75% 模型 |ΔRank| < 100，仅 1.2% 超过 500。

**Family 关键对比** — 论文中 "+700–850" 是个体极端值，不是 family 均值：

| Family | N | Mean ΔRank | Median | Individual Max |
|--------|---|-----------|--------|----------------|
| phi-3 | 20 | +254.5 | +20 | +809 |
| llama-3 | 315 | +120.8 | +53 | +793 |
| mistral | 547 | −53.9 | −35 | +182 |

phi-3 mean 很高但 N 只有 20 且 SD=359.3（被少数极端值拉动）。llama-3 的 median 仅 +53，远低于个体极端的 +793。

输出文件：
- `artifacts/plan_017_supplement/rank_shift_distribution_report.md`
- `artifacts/plan_017_supplement/rank_shift_stats.json`
- `artifacts/plan_017_supplement/rank_shift_analysis.py`

---
