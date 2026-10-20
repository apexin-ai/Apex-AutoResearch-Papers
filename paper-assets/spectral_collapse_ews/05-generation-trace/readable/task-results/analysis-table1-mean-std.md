# analysis table1 mean std

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table1_mean_std_20260520T081955_result.json`
- **Structured JSON:** [`36d6ddb8021565b46687.json`](../../sessions/36/36d6ddb8021565b46687.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Seed43 没有 HellaSwag 评估。以下是完整数据汇总。

---

## 原始数据

### σ1 (top singular value)

| Gen | seed42 | seed43 |
|-----|--------|--------|
| 0 | 1942.82 | 1942.82 |
| 2 | 712.03 | 718.12 |
| 5 | 741.02 | 753.63 |
| 7 | 791.28 | 790.03 |
| 10 | 825.72 | 886.08 |

### HellaSwag (acc_norm, seed42 only)

| Gen | seed42 | seed43 |
|-----|--------|--------|
| 0 | 0.4130 | MISSING |
| 2 | 0.3764 | MISSING |
| 5 | 0.3439 | MISSING |
| 7 | 0.3187 | MISSING |
| 10 | 0.2951 | MISSING |

---

## Table 1: mean±std (n=2, s = |x₁−x₂|/√2)

| Gen | eff_rank | SLV (log_det) | PPL | HeSw | D-4 | σ₁ |
|-----|----------|---------------|-----|------|-----|----|
| 0 | 417.5±0.0 | 2366.7±0.0 | 9.55±0.00 | 0.413 (seed42 only) | 0.741±0.000 | 1942.8±0.0 |
| 2 | 496.3±0.14 | 2468.3±2.33 | 13.57±0.01 | 0.376 (seed42 only) | 0.510±0.007 | 715.1±4.3 |
| 5 | 479.6±0.61 | 2367.7±3.56 | 24.60±0.01 | 0.344 (seed42 only) | 0.440±0.032 | 747.3±8.9 |
| 7 | 464.2±0.01 | 2297.9±8.94 | 38.17±1.02 | 0.319 (seed42 only) | 0.419±0.040 | 790.7±0.9 |
| 10 | 440.6±2.60 | 2194.9±22.50 | 73.64±4.44 | 0.295 (seed42 only) | 0.410±0.023 | 855.9±42.7 |

---

**关键发现：**
- eff_rank, log_det, PPL 两个 seed 高度一致（std 很小）
- distinct_4 和 σ₁ 在后期 generations 方差较大（σ₁ gen10 std=42.7）
- **HellaSwag seed43 完全缺失**——需要在 rtx6000-diagprobe 上对 seed43 的 gen 0/2/5/7/10 checkpoints 跑 lm-eval hellaswag 才能补齐

---
