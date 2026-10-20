# analysis c5 gini collect

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c5_gini_collect_20260516T031406_result.json`
- **Structured JSON:** [`e28f43572d3fda04456e.json`](../../sessions/e2/e28f43572d3fda04456e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

QW (Qwen2.5-7B-Instruct) results are complete. Here's the summary while we wait for DS:

**QW Per-Phase Gini Delta Summary (n=30 problems)**

| Sparsity | Method | Global Δ (±std) | Low Phase Δ | Mid Phase Δ | High Phase Δ |
|----------|--------|-----------------|-------------|-------------|--------------|
| 0.15 | importance | -0.0103 ±0.0064 | -0.0165 | -0.0094 | -0.0120 |
| 0.15 | random | -0.0186 ±0.0071 | -0.0083 | -0.0038 | -0.0036 |
| 0.20 | importance | -0.0121 ±0.0095 | -0.0200 | -0.0115 | -0.0143 |
| 0.20 | random | -0.0229 ±0.0084 | -0.0119 | -0.0053 | -0.0067 |
| 0.25 | importance | -0.0100 ±0.0101 | -0.0286 | -0.0168 | -0.0207 |
| 0.25 | random | -0.0337 ±0.0224 | -0.0014 | -0.0081 | +0.0045 |
| 0.30 | importance | -0.0202 ±0.0101 | -0.0350 | -0.0183 | -0.0239 |
| 0.30 | random | -0.0447 ±0.0125 | -0.0221 | -0.0077 | -0.0061 |

Dense Gini baselines: low=0.2675, mid=0.2078, high=0.2599

Key observation: importance pruning shows **larger Gini drops in low-sparsity phase** (where most tokens are), while random pruning has larger global Δ but smaller per-phase drops — the pattern reversal at per-phase level is interesting.

DS model currently at 16/30. Will check back in ~4 min.

---
