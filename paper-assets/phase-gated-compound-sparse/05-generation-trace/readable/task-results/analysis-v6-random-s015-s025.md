# analysis v6 random s015 s025

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v6_random_s015_s025_20260514T055544_result.json`
- **Structured JSON:** [`204bafc5bfd72b631dff.json`](../../sessions/20/204bafc5bfd72b631dff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已 DONE。汇总对比：

### v6_random_s015 vs v6_importance_s015 (sparsity=0.15)

| 指标 | random | importance |
|------|--------|------------|
| ii_high_median | 0.161 | 0.227 |
| ii_mid_median | 0.252 | 0.743 |
| ii_low_median | 0.183 | 2.876 |
| bootstrap_gradient_paired | **-0.27** (p=0.90) | **11.53** (p=0) |
| gradient CI | [-0.70, 0.15] | [3.49, 23.78] |

### v6_random_s025 vs v6_importance_s025 (sparsity=0.25)

| 指标 | random | importance |
|------|--------|------------|
| ii_high_median | 3.002 | 0.664 |
| ii_mid_median | 2.985 | 5.307 |
| ii_low_median | 2.915 | 24.162 |
| bootstrap_gradient_paired | **-0.12** (p=0.56) | **35.72** (p=0) |
| gradient CI | [-1.52, 1.25] | [9.52, 101.54] |

**结论**：Random masking 的 II gradient ≈ 0（三组 phase 无显著差异），importance masking 有强烈的 phase-dependent gradient（low_sparsity phase II 远高于 high_sparsity）。Phase-dependent interaction 是 importance-based masking 的特异效应，非注意力结构的 artifact。

---
