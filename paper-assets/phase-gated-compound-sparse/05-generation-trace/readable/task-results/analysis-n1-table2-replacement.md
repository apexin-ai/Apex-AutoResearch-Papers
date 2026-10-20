# analysis n1 table2 replacement

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n1_table2_replacement_20260515T113907_result.json`
- **Structured JSON:** [`4982f1d74855a6407783.json`](../../sessions/49/4982f1d74855a6407783.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 16 conditions 数据提取完毕。CSV 已存 `artifacts/n500_analysis/table2_n500_full.csv`。

---

**Table 2 (n=500) 关键结果**

**Importance masking — 强 phase-gating 效应：**

| Model | s | II_high median | II_low median | D median | G median | p |
|-------|------|----------------|---------------|----------|----------|------|
| DS | 0.15 | 0.003 [0.001, 0.005] | 0.357 [0.320, 0.398] | 0.391 [0.350, 0.443] | 7.5× [4.1, 11.4] | 1.3e-70 |
| DS | 0.20 | 0.008 [0.003, 0.011] | 1.211 [1.095, 1.321] | 1.215 [1.107, 1.336] | 17.9× [12.7, 26.3] | 4.0e-75 |
| DS | 0.25 | 0.021 [0.017, 0.027] | 3.971 [3.476, 4.405] | 3.986 [3.527, 4.359] | 49.1× [40.1, 57.8] | 2.0e-78 |
| DS | 0.30 | 0.038 [0.033, 0.048] | 8.456 [7.780, 9.762] | 8.481 [7.754, 9.692] | 79.8× [63.3, 96.5] | 1.1e-79 |
| QW | 0.15 | -0.000 [-0.001, 0.000] | 0.044 [0.027, 0.063] | 0.066 [0.049, 0.092] | 0.2× [-0.2, 0.9] | 8.7e-15 |
| QW | 0.20 | 0.000 [-0.000, 0.001] | 0.275 [0.231, 0.327] | 0.307 [0.261, 0.356] | 2.6× [0.5, 5.1] | 6.8e-42 |
| QW | 0.25 | 0.004 [0.002, 0.007] | 1.053 [0.959, 1.183] | 1.074 [0.977, 1.179] | 9.5× [5.2, 14.8] | 1.1e-68 |
| QW | 0.30 | 0.014 [0.009, 0.017] | 3.208 [2.798, 3.634] | 3.155 [2.799, 3.558] | 36.9× [25.3, 49.1] | 9.2e-74 |

**Random masking — 无 phase-gating（flat）：**

| Model | s | II_high median | II_low median | D median | G median | p |
|-------|------|----------------|---------------|----------|----------|------|
| DS | 0.15 | 0.083 | 0.090 | 0.014 [-0.017, 0.039] | 0.52× | 0.86 |
| DS | 0.20 | 0.270 | 0.357 | 0.031 [-0.011, 0.077] | 0.76× | 0.28 |
| DS | 0.25 | 1.113 | 1.514 | 0.257 [0.126, 0.350] | 1.09× | 1.5e-3 |
| DS | 0.30 | 3.112 | 3.848 | 0.510 [0.260, 0.891] | 1.15× | 1.5e-3 |
| QW | 0.15 | 0.094 | 0.097 | -0.011 [-0.039, 0.012] | 0.67× | 0.17 |
| QW | 0.20 | 0.291 | 0.356 | 0.015 [-0.015, 0.068] | 0.88× | 0.20 |
| QW | 0.25 | 1.108 | 1.769 | 0.393 [0.236, 0.553] | 1.26× | 1.6e-11 |
| QW | 0.30 | 2.819 | 4.253 | 0.913 [0.613, 1.258] | 1.30× | 2.9e-15 |

**Qwen s025 crossover 检验（importance vs random per phase）：**
- Phase high: imp=0.004 vs rand=1.109 → random 的 II_high 远大于 importance（差 -1.10）
- Phase low: imp=1.043 vs rand=1.770 → random 的 II_low 也大于 importance（差 -0.73）
- Qwen 无 crossover：random 在两个 phase 的 II 都高于 importance，不像 DS 那样 high-phase random > importance 但 low-phase importance > random。

---
