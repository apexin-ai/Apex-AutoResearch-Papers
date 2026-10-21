# exp westd14391 data prep steering

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_westd14391-data-prep-steering_20260523T220839_result.json`
- **Structured JSON:** [`5cfdaae13439cc2e1169.json`](../../sessions/5c/5cfdaae13439cc2e1169.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three layers complete. Here's the full report.

---

## Steering Experiment Results — Llama-3.1-8B-Instruct × ConflictQA

**Server**: westd-14391  
**Model**: Meta-Llama-3.1-8B-Instruct  
**Dataset**: ConflictQA (popQA-chatgpt), 1200 train (600 conflict + 600 no_conflict), 201 conflict test  
**Method**: Linear probe on residual stream (last token), steering via probe weight direction  
**Control**: Random orthogonal direction (Gram-Schmidt)  
**Statistical test**: Fisher exact test, Bonferroni correction k=6, α_corrected = 0.00833

### Baseline Distribution (n=201 conflict samples, no steering)

| parametric | contextual | both | neither |
|-----------|------------|------|---------|
| 4 (2.0%)  | 131 (65.2%)| 10 (5.0%) | 56 (27.9%) |

---

### Layer 12 — Probe accuracy: 91.75%

| Alpha | Steer flips | Ctrl flips | Fisher p | p→c | c→p |
|-------|------------|------------|----------|-----|-----|
| -20   | 54 (26.9%) | 50 (24.9%) | 0.7327   | 0   | 1   |
| -10   | 36 (17.9%) | 29 (14.4%) | 0.4165   | 0   | 0   |
| -5    | 17 (8.5%)  | 19 (9.5%)  | 0.8616   | 0   | 0   |
| +5    | 21 (10.4%) | 14 (7.0%)  | 0.2884   | 0   | 1   |
| +10   | 38 (18.9%) | 30 (14.9%) | 0.3518   | 0   | 1   |
| +20   | 43 (21.4%) | 59 (29.4%) | 0.0853   | 0   | 1   |

**Bonferroni-significant**: None. Min p = 0.0853 (α=+20). L12 steering direction has no detectable causal effect.

---

### Layer 13 — Probe accuracy: 90.00%

| Alpha | Steer flips | Ctrl flips | Fisher p | p→c | c→p |
|-------|------------|------------|----------|-----|-----|
| -20   | 45 (22.4%) | 51 (25.4%) | 0.5587   | 1   | 1   |
| -10   | 35 (17.4%) | 23 (11.4%) | 0.1179   | 0   | 1   |
| -5    | 12 (6.0%)  | 17 (8.5%)  | 0.4412   | 0   | 0   |
| +5    | 38 (18.9%) | 17 (8.5%)  | **0.0034** | 0 | 2   |
| +10   | 57 (28.4%) | 27 (13.4%) | **0.0003** | 0 | 3   |
| +20   | 65 (32.3%) | 62 (30.8%) | 0.8302   | 1   | 0   |

**Bonferroni-significant**: α=+5 (p=0.0034 < 0.00833), α=+10 (p=0.0003 < 0.00833). Both survive correction.

---

### Layer 14 — Probe accuracy: 91.75%

| Alpha | Steer flips | Ctrl flips | Fisher p | p→c | c→p |
|-------|------------|------------|----------|-----|-----|
| -20   | 51 (25.4%) | 43 (21.4%) | 0.4095   | 0   | 0   |
| -10   | 28 (13.9%) | 33 (16.4%) | 0.5784   | 1   | 0   |
| -5    | 20 (10.0%) | 12 (6.0%)  | 0.1965   | 0   | 0   |
| +5    | 24 (11.9%) | 18 (9.0%)  | 0.4152   | 0   | 1   |
| +10   | 56 (27.9%) | 30 (14.9%) | **0.0022** | 0 | 2   |
| +20   | 67 (33.3%) | 68 (33.8%) | 1.0000   | 0   | 3   |

**Bonferroni-significant**: α=+10 (p=0.0022 < 0.00833). Survives correction.

---

### L13 Replication Assessment

| Metric | Original (plan_107) | Current |
|--------|-------------------|---------|
| Best α | +10 | +10 |
| Fisher p | 0.0009 | 0.0003 |
| Steer flips | — | 57/201 (28.4%) |
| Ctrl flips | — | 27/201 (13.4%) |

**复现成功。** L13 α=+10 的 p=0.0003 甚至强于原始 p=0.0009，且 α=+5 也通过 Bonferroni 校正。

### Cross-layer Summary

| Layer | Probe Acc | Best α | Fisher p | Bonferroni sig? |
|-------|----------|--------|----------|-----------------|
| 12    | 91.75%   | +20    | 0.0853   | No              |
| **13**| 90.00%   | **+10**| **0.0003**| **Yes (2/6)**  |
| 14    | 91.75%   | +10    | 0.0022   | Yes (1/6)       |

L13 是最强效应层（2 个 alpha 通过 Bonferroni），L14 次之（1 个），L12 无显著效应。效应集中在 positive direction（+5 到 +10），与 probe 的 conflict→no_conflict 方向一致。α=+20 时 steering 和 control 都产生大量 flips，说明高强度扰动破坏了生成质量，不具有方向性。

### Output Files

- `westd-14391:/root/clkc_mech_interp/data/llama31/en_activations.pt` — activations (1600, 32, 4096)
- `westd-14391:/root/clkc_mech_interp/data/llama31/steering_results_L12_last.json`
- `westd-14391:/root/clkc_mech_interp/data/llama31/steering_results_L13_last.json`
- `westd-14391:/root/clkc_mech_interp/data/llama31/steering_results_L14_last.json`

---
