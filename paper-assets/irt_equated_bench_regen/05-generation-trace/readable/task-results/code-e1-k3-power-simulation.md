# code e1 k3 power simulation

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e1_k3_power_simulation_20260523T012752_result.json`
- **Structured JSON:** [`5b813b6b539cfb4f9193.json`](../../sessions/5b/5b813b6b539cfb4f9193.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。1000 replications × 60 conditions，7.4 分钟完成。

**核心结论：K=3 和 K=5 的 power 本质上相同。**

关键数据：
- 所有 30 对 (K, N, δ) 条件下，K=3 vs K=5 的 TPR 差异均 < 0.02（在 Monte Carlo 噪声范围内）
- 平均 TPR 差异 = +0.003（K=3 甚至略高，但不显著）
- K=3 在大 N 时 FPR 反而更低（如 N=500/δ=1.4：K=3 FPR=0.018 vs K=5 FPR=0.024）

**TPR≥0.5 达成条件**：
- N≥100, δ≥1.4: TPR=0.571
- N≥200, δ≥1.0: TPR=0.623
- N≥500, δ≥0.8: TPR=0.826

输出文件：
- `artifacts/k3_power_simulation/k3_power_results.csv` — 60 行完整数据
- `artifacts/k3_power_simulation/k3_power_report.md` — 含对比表和解读

---
