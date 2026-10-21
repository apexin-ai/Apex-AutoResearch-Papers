# analysis epsilon sweep r8

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_epsilon_sweep_r8_20260515T153432_result.json`
- **Structured JSON:** [`109b62d9ae1bfafb90ce.json`](../../sessions/10/109b62d9ae1bfafb90ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果摘要**：ε sweep 确认论文默认 ε=0.05 选择 robust。在 non-tied subset 上，LP selection 一致优于 greedy（Δ 从 +0.58pp@ε=0.01 单调递增到 +4.59pp@ε=0.20），ε∈[0.05, 0.10] 区间统计显著 (p<0.05)。更大 ε 效应更强但 power 不足。CSV 已存 `analysis_round8/epsilon_sweep.csv`。

---
