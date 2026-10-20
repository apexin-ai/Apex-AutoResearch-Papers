# analysis wnut17 full signal report

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_wnut17_full_signal_report_20260519T112628_result.json`
- **Structured JSON:** [`c08e7154b93fbfe08567.json`](../../sessions/c0/c08e7154b93fbfe08567.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集。以下是 WNUT-17 完整 signal 分析报告。

---

## WNUT-17 Signal 分析报告 (Qwen2.5-7B, n=8)

**数据规模**: 1287 total, 689 after gold-empty filtering, 8 samples/instance

### 1. Basic Metrics (per-seed)

| Metric | Seed 42 | Seed 123 | Seed 456 | Mean |
|--------|---------|----------|----------|------|
| Greedy F1 | 0.4524 | 0.4518 | 0.4526 | 0.4523 |
| Oracle F1 | 0.5154 | 0.5438 | 0.5351 | 0.5315 |
| Headroom (pp) | +6.30 | +9.21 | +8.25 | +7.92 |
| Zero-F1 rate | 47.75% | 47.75% | 47.75% | 47.75% |
| **Degeneracy rate** | **70.54%** | **66.91%** | **66.18%** | **67.88%** |
| LP range (median) | 0.0454 | 0.0529 | 0.0532 | 0.0505 |

### 2. Signal Quality: Spearman ρ

**Global ρ (instance-level signal vs F1):**

| Signal | Seed 42 | Seed 123 | Seed 456 | Mean |
|--------|---------|----------|----------|------|
| LP | **-0.487** | **-0.403** | **-0.448** | **-0.446** |
| SJ | -0.096 | +0.039 | +0.002 | -0.018 |
| FK | -0.085 | +0.054 | +0.010 | -0.007 |
| EM | -0.097 | +0.031 | -0.016 | -0.027 |
| VC | +0.733 | +0.733 | +0.724 | +0.730 |

**Within-instance ρ (conditional, non-degenerate only):**

| Signal | Seed 42 | Seed 123 | Seed 456 | Mean |
|--------|---------|----------|----------|------|
| **LP** | **0.079** (p=0.26) | **0.036** (p=0.59) | **0.014** (p=0.83) | **0.043 (n.s.)** |
| SJ | 0.170 (p=0.015) | 0.412 (p=0.0) | 0.354 (p=0.0) | 0.312 |
| FK | 0.180 (p=0.010) | 0.428 (p=0.0) | 0.365 (p=0.0) | 0.324 |
| EM | 0.203 (p=0.004) | 0.406 (p=0.0) | 0.326 (p=0.0) | 0.312 |
| VC | 0.196 (p=0.005) | 0.465 (p=0.0) | 0.433 (p=0.0) | 0.365 |

### 3. Selection Δ vs Greedy (pp)

| Signal | Seed 42 | Seed 123 | Seed 456 | Mean |
|--------|---------|----------|----------|------|
| LP | -0.90 | +0.03 | -0.47 | -0.44 |
| SJ | -1.73 | -0.35 | +0.30 | -0.59 |
| FK | -1.90 | -0.43 | +0.19 | -0.71 |
| EM | -2.30 | -0.91 | -0.37 | -1.20 |
| **VC** | **+0.75** | **+2.64*** | **+2.54*** | **+1.98** |

(\* = p < 0.05 bootstrap significant)

### 4. Entity Construction (θ=0.25)

| Method | Seed 42 | Seed 123 | Seed 456 | Mean |
|--------|---------|----------|----------|------|
| Greedy | 0.4524 | 0.4518 | 0.4526 | 0.4523 |
| LP Selection | 0.4434 (-0.90) | 0.4521 (+0.03) | 0.4480 (-0.47) | 0.4478 (-0.45) |
| MV (0.5) | 0.4356 (-1.68) | 0.4574 (+0.56) | 0.4542 (+0.15) | 0.4491 (-0.32) |
| **Construction** | **0.4439 (-0.84)** | **0.4579 (+0.61)** | **0.4583 (+0.57)** | **0.4534 (+0.11)** |
| Oracle | 0.5154 (+6.30) | 0.5438 (+9.21) | 0.5351 (+8.25) | 0.5315 (+7.92) |

**Bootstrap p-values (construction vs greedy):** 0.954, 0.077, 0.120 — **全部不显著**

### 5. Cross-dataset 对比 (SciERC 作为参照)

| Metric | SciERC | WNUT-17 (mean) | CoNLL |
|--------|--------|----------------|-------|
| Degeneracy | 17.8% | **67.9%** | 59.1% |
| LP global ρ | +0.205 | **-0.446** | +0.302 |
| LP within-inst ρ | ~0.2+ | **0.043 (n.s.)** | — |
| LP Δ (pp) | +0.61 | -0.44 | -1.05 |
| Headroom (pp) | +13.2 | +7.9 | +4.0 |

---

### 关键诊断结论

**Construction 不显著的根本原因是 LP signal 在 WNUT-17 上完全失效：**

1. **LP global ρ = -0.45**：LP 与 F1 呈强负相关（高 LP → 低 F1），方向完全反转。SciERC 上是 +0.21。
2. **LP within-instance ρ ≈ 0.04 (n.s.)**：在非退化实例内部，LP 完全无法区分好坏 sample，p 值均 >0.2。这意味着 LP-weighted construction 等价于随机加权。
3. **Degeneracy = 68%**：近七成实例所有 sample 的 F1 相同，LP 无从发挥。SciERC 仅 17.8%。
4. **VC 是唯一有效 signal**：VC global ρ = 0.73，selection Δ = +2.0pp (2/3 seeds significant)。但 VC 是 instance-level ranking signal，无法用于 within-instance construction。

---
