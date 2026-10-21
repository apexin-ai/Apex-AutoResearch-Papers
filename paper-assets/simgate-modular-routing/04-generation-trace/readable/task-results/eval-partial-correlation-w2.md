# eval partial correlation w2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_partial-correlation-w2_20260516T192301_result.json`
- **Structured JSON:** [`56e8ea2f50f8accac035.json`](../../sessions/56/56e8ea2f50f8accac035.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果清晰。核心发现：

**30-task 数据集:**
| 指标 | 值 |
|---|---|
| Raw r(Δ_full, δ_diff) | **0.9864** (paper 的 r≈0.97) |
| r(death_contribution, δ_diff) | **1.0000** — 完全共线 (P=100 constant) |
| **Partial r(Δ_full, δ_diff \| DC)** | **0.0225** (p=0.906, df=27) — 不显著 |
| Partial r(Δ_full, δ_int \| DC) | 0.2065 (p=0.274) — 也不显著 |
| Non-death signal fraction | 4.0% |

**结论:**
- P = 100 在所有 task 上恒定 (mean=100.00, std=0.01)
- death_contribution = δ_diff × 100，与 δ_diff 完全共线 (r=1.0000)
- Δ_full = δ_diff × 100 + Δ_nd，其中 Δ_nd 仅占 4% 的信号
- r=0.97 是结构性恒等式 Corr(100·δ + ε, δ) ≈ 1 的直接结果
- 控制 δ·P 后 partial r = 0.02 (p=0.91)，相关性完全消失

结果已保存到 `guided_router/partial_corr_results.json`。

---
