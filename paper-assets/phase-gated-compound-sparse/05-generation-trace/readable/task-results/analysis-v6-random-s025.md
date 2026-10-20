# analysis v6 random s025

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v6_random_s025_20260514T055406_result.json`
- **Structured JSON:** [`ecccfcfa0927d7bbf11e.json`](../../sessions/ec/ecccfcfa0927d7bbf11e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，结果已复制到 `results_fp16_ref/`。

## v6_random_s025 结果

| 指标 | Random (本次) | Importance (对照) |
|------|-------------|-----------------|
| ii_high_median | **3.04** | 0.66 |
| ii_mid_median | **2.14** | 5.31 |
| ii_low_median | **2.73** | 24.16 |
| gradient (low/high) | **0.90** | **35.72** |
| n_problems | 50 | 50 |
| n_high / n_mid / n_low | 36 / 25 / 24 | — |

**结论**：Random baseline 符合预期。三个 phase 的 median II 均在 2-3 范围，几乎无差异（gradient ≈ 0.90 ≈ 1.0）。对比 importance masking 的 35.72x gradient，确认 phase-dependent interaction amplification 是 importance-based masking 的特异效应，非 sparsity 本身的 artifact。

---
