# analysis compile full tables

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_compile_full_tables_20260518T053053_result.json`
- **Structured JSON:** [`75c6553f8d32aaa29982.json`](../../sessions/75/75c6553f8d32aaa29982.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已保存到 `artifacts/report_tables.md` 并注册。

核心发现：

**Table 1 (Grid U-curve, ρ=0.4)**：U-shape 确认，b=0.3 最优 (17.620±0.035)，两端递增。但 b=0.3 的优势主要来自 seed123 的 17.579 异常值，另两个 seed 均为 17.640。b≥0.5 缺 seed42 数据，b=0.2 缺两个 seed（仍在跑）。大 b 端 (≥2.0) 方差显著增大 (std>0.1)。

**Table 2 (ρ=0.6 ablation)**：层级关系跨 ρ 保持——Adaptive (17.736) < Uniform (17.763) < ESS-only (17.770)，gap 与 ρ=0.4 相当。3 个实验仍在跑（adaptive seed456、random、grid b=0.3），grid b=0.5 无 metrics 需排查。

---
