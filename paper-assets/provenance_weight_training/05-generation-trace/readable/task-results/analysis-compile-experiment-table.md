# analysis compile experiment table

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_compile_experiment_table_20260515T160409_result.json`
- **Structured JSON:** [`6e0bac83f180bdc43e7a.json`](../../sessions/6e/6e0bac83f180bdc43e7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已保存到 `artifacts/paper_tables.md` 并注册。

关键发现：
- **Adaptive-fix (n_min=2) 是最优方法**：mean PPL 17.651，与 Grid-best(b=0.5) 的 17.646 持平，且无需网格搜索
- **Golden Ratio oracle (17.654) 并未超过 adaptive-fix**，说明自适应方法已接近理论上界
- **τ sweep 仅完成 2/6**：τ=0.8 最优，τ=0.6 劣化 +0.031；其余 4 个 τ 值待补

---
