# analysis multiseed entity construction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multiseed_entity_construction_20260519T053858_result.json`
- **Structured JSON:** [`52e738b0a242434b7fa1.json`](../../sessions/52/52e738b0a242434b7fa1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `output/entity_construction_fair_n8/multiseed_results.json`。

## 汇报

### SciERC (3 seeds, N=8, 529 instances/seed)

| Seed | Greedy F1 | Uniform (θ=0.25) | LP-weighted (θ=0.25) | Δ Uniform | Δ LP-weighted |
|------|-----------|-------------------|----------------------|-----------|---------------|
| 42   | 64.39     | 65.93             | 66.06                | +1.54pp   | +1.67pp       |
| 123  | 64.57     | 65.45             | 65.48                | +0.88pp   | +0.90pp       |
| 456  | 64.78     | 64.59             | 65.28                | -0.19pp   | +0.49pp       |

**Mean ± σ:**

| Metric | Value |
|--------|-------|
| Greedy F1 | 64.58 ± 0.16 |
| Uniform Construction | 65.32 ± 0.56 |
| LP-weighted Construction | 65.60 ± 0.33 |
| Δ Uniform | +0.74 ± 0.71pp |
| Δ LP-weighted | **+1.02 ± 0.49pp** |

### FewNERD (4 seeds, N=8, 32565 instances/seed)

| Seed | Greedy F1 | Uniform (θ=0.25) | LP-weighted (θ=0.25) | Δ Uniform | Δ LP-weighted |
|------|-----------|-------------------|----------------------|-----------|---------------|
| 42   | 74.78     | 75.10             | 75.66                | +0.32pp   | +0.88pp       |
| 123  | 74.80     | 76.52             | 76.99                | +1.72pp   | +2.18pp       |
| 456  | 74.86     | 75.50             | 76.37                | +0.64pp   | +1.51pp       |
| 789  | 74.78     | 75.08             | 75.80                | +0.30pp   | +1.02pp       |

**Mean ± σ:**

| Metric | Value |
|--------|-------|
| Greedy F1 | 74.81 ± 0.03 |
| Uniform Construction | 75.55 ± 0.59 |
| LP-weighted Construction | 76.21 ± 0.52 |
| Δ Uniform | +0.74 ± 0.58pp |
| Δ LP-weighted | **+1.40 ± 0.51pp** |

### Table 5 更新数据

- **SciERC**: Greedy 64.58±0.16 → Uniform 65.32±0.56 (+0.74pp) → LP-weighted 65.60±0.33 (+1.02pp)
- **FewNERD**: Greedy 74.81±0.03 → Uniform 75.55±0.59 (+0.74pp) → LP-weighted 76.21±0.52 (+1.40pp)

注意 seed 456 在 SciERC 上 Uniform construction Δ 为负 (-0.19pp)，但 LP-weighted 仍为正 (+0.49pp)。LP-weighted construction 在所有 seed 上一致优于 greedy。

---
