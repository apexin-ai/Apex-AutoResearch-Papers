# experiment d126 drc folio

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_d126-drc-folio_20260521T082219_result.json`
- **Structured JSON:** [`10c4d4d7b1aa1558c3d9.json`](../../sessions/10/10c4d4d7b1aa1558c3d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。

**E3 — DRC Cascade on FOLIO-204 结果**:

| Method | Acc | Δ vs SC | NLI Calls | Cost |
|--------|-----|---------|-----------|------|
| SC only | 55.88% | — | 0/204 | 0% |
| Full combo w=1 | 56.37% | +0.49pp | 204/204 | 100% |
| Full combo w=3 | 58.82% | +2.94pp | 204/204 | 100% |
| DRC τ=0.5 w=3 | 55.88% | 0 | 23/204 | 11.3% |
| DRC τ=0.6 w=3 | 57.35% | +1.47pp | 49/204 | 24.0% |
| **DRC τ=0.7 w=3** | **58.33%** | **+2.45pp** | **71/204** | **34.8%** |
| DRC τ=0.8 w=3 | 58.82% | +2.94pp | 99/204 | 48.5% |
| DRC τ=0.9 w=3 | 58.82% | +2.94pp | 131/204 | 64.2% |

**泛化性验证成功**: τ=0.7 在 FOLIO 上恢复 83.3% 的 full combo gain，仅需 34.8% NLI 调用 — 与 ProofWriter (90% gain / 38.8% cost) 高度一致。τ=0.8 达到 100% gain recovery，cost 仅 48.5%。

结果已保存至服务器 `results/exp_d126_drc_folio/results.json` 和本地 `artifacts/drc_folio_results.json`，Pareto front 图和 agreement distribution 图也已生成。

---
