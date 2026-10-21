# analysis results compilation

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_results_compilation_20260516T004947_result.json`
- **Structured JSON:** [`27197785a2b4ef20476e.json`](../../sessions/27/27197785a2b4ef20476e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。两个文件已生成并注册：

**`table1_data.json`** — 结构化 JSON，包含 13 个方法组的 PPL 数据
**`table1_summary.md`** — Markdown 摘要表

关键发现：
- **Adaptive (n_min=3, bug)** PPL 最低：17.6389 (Δ = -0.0549)
- **Adaptive (n_min=2, fix)** 次之：17.6508 (Δ = -0.0430)
- **Grid b=0.5** 是最佳 grid 配置：17.6463 (Δ = -0.0475)
- **ESS-only** 反而比 uniform 差：17.7230 (Δ = +0.0292)
- seed456 的 grid b≥2.0 已标记 excluded（checkpoint resume artifact）

---
