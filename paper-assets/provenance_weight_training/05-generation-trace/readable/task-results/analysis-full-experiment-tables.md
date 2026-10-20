# analysis full experiment tables

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_full-experiment-tables_20260516T051338_result.json`
- **Structured JSON:** [`ef9ce61edc56e06bae3f.json`](../../sessions/ef/ef9ce61edc56e06bae3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 files已生成并注册，位于 `artifacts/tables/`。

关键结果摘要：

**Table 1** — Adaptive (dual-constraint) 在 ρ=0.4 下 PPL=17.651±0.007，比 uniform (17.694±0.008) 低 0.043；ρ=0.6 下 grid b=0.5 最优 (17.704, Δ=-0.062)。

**Table 2** — 最佳消融配置为 n_min=3 (PPL=17.644)，τ=0.8 是最优 τ 值；bs=8 和高 τ (≥0.9) 均为 NEGATIVE。

**Table 3** — Grid sweep 中 b=0.3 最优 (17.640, Δ=-0.054)，PPL 随 b 增大单调恶化；golden_ratio 接近 adaptive (17.654)。

仍在跑的实验：contamination_60 的 τ=0.6/0.7、grid_b0_1、detect_remove_baseline。

---
