# analysis generalize pythia14b wiki a100 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_generalize_pythia14b_wiki_a100_s43_20260518T101511_result.json`
- **Structured JSON:** [`7f8c80fb4f7a0e8ecbd5.json`](../../sessions/7f/7f8c80fb4f7a0e8ecbd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果摘要

**Conclusion: SUCCESS** — 1.4B scale effect 是系统性的，非 seed noise。

### s42 vs s43 对比 (analyze_generalize.py, 16 pairs x 5 methods)

| | s42 | s43 |
|---|---|---|
| Total sig | 45/80 | 46/80 |
| Naive | 15/16 | 15/16 |
| Diff | 10/16 | 10/16 |
| Thresh | 9/16 | 8/16 |
| TY | 3/16 | 4/16 |
| PG | 8/16 | 9/16 |
| **K>=4** | **8/16** | **6/16** |
| **K>=3** | **9/16** | **9/16** |

### 关键发现

1. **总体显著率几乎相同** (45 vs 46)，per-method 最大偏差 1/16
2. **K>=3 完全一致** (9/16)，K>=4 差异 (8→6) 完全来自 effective_rank→diversity pairs 中 TY 失去显著性（符合 C003 约束：TY 在短序列不稳定）
3. **核心 canary 稳定**: token_entropy→diversity 和 ece→diversity 在两个 seed 中都达到 K>=4 共识，s43 的 ece pairs 甚至更强 (5/5 vs 4/5)
4. **Drift 幅度一致**: entropy -55%~-57%, d1 -27%~-31%, ece +5586~5693%, ppl +3341~3972%

Registry 已更新为 DONE(success)，报告已注册。

---
