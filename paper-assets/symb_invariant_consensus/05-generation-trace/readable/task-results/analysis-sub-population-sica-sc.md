# analysis sub population sica sc

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sub-population-sica-sc_20260521T010040_result.json`
- **Structured JSON:** [`97e7be6c6834d5a74de2.json`](../../sessions/97/97e7be6c6834d5a74de2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出汇总：

**3 个产出文件：**
- `src/analysis/sub_population_analysis.py` — 分析脚本（可本地运行）
- `artifacts/sub_population_results.json` — 完整结果数据（含来源路径）
- `artifacts/sub_population_appendix_draft.tex` — 2 张表 + 解读草稿

**核心发现：**

| | FOLIO-204 | PW-600 |
|---|---|---|
| **Overall Δ** | **+4.9pp** (p=.013*) | **-2.8pp** (p=.014*) |

**按 answer type（FOLIO-204）：** SICA 在三类 label 上均正向，True 最大（+6.9pp, p=.063），但单组样本量太小未达显著。

**按 answer type（PW-600）：** SICA 在三类上均负向，False 最明显（-5.0pp, p=.076）。

**按 constraint count：** FOLIO-204 上 Mid tertile 增益最大（+7.8pp）；PW-600 上高约束组退化几乎消失（-0.5pp, p=1.0），说明约束数量充足时 SICA 至少不伤害性能。

---
