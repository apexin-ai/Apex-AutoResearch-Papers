# analysis perlayer sparsity 32sample

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_sparsity_32sample_20260522T104055_result.json`
- **Structured JSON:** [`7862961af6567272211b.json`](../../sessions/78/7862961af6567272211b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 seed 都完成了。汇总结果。

## Per-Layer Sparsity 分析结果（32 calibration samples, seq_len=2048, target=30%）

### 32 层对比表

| Layer | s42 sparsity | s123 sparsity | |Δ| | 区域 |
|-------|-------------|--------------|-----|------|
| 0 | 0.1741 | 0.1901 | 0.016 | early |
| 1 | 0.1332 | 0.1174 | 0.016 | early |
| 2 | 0.2280 | 0.1850 | 0.043 | early |
| 3 | 0.2291 | 0.2314 | 0.002 | early |
| 4 | 0.2193 | 0.2199 | 0.001 | early |
| 5 | 0.2407 | 0.2354 | 0.005 | early |
| 6 | 0.2508 | 0.2633 | 0.013 | early |
| 7 | 0.2951 | 0.3145 | 0.019 | mid |
| 8 | 0.3262 | 0.3396 | 0.013 | mid |
| 9 | 0.3276 | 0.3458 | 0.018 | mid |
| 10 | 0.3375 | 0.3531 | 0.016 | mid |
| 11 | 0.3397 | 0.3618 | 0.022 | mid |
| 12 | 0.3224 | 0.3497 | 0.027 | mid |
| 13 | 0.3014 | 0.3316 | 0.030 | mid |
| **14** | **0.2642** | **0.2884** | 0.024 | **valley** |
| **15** | **0.1967** | **0.2031** | 0.006 | **valley** |
| **16** | **0.1603** | **0.1603** | 0.000 | **valley** |
| **17** | **0.1567** | **0.1506** | 0.006 | **valley** |
| **18** | **0.1253** | **0.1194** | 0.006 | **valley** |
| 19 | 0.1761 | 0.1618 | 0.014 | late-mid |
| 20 | 0.1933 | 0.1909 | 0.002 | late-mid |
| 21 | 0.2234 | 0.1602 | 0.063 | late-mid |
| 22 | 0.2585 | 0.2102 | 0.048 | late-mid |
| 23 | 0.2670 | 0.2480 | 0.019 | late-mid |
| 24 | 0.2924 | 0.2676 | 0.025 | late-mid |
| 25 | 0.3235 | 0.3977 | 0.074 | late |
| 26 | 0.4132 | 0.4665 | 0.053 | late |
| 27 | 0.4928 | 0.4987 | 0.006 | late |
| 28 | 0.5763 | 0.5873 | 0.011 | late |
| 29 | 0.5387 | 0.5371 | 0.002 | late |
| 30 | 0.5141 | 0.4196 | 0.095 | late |
| 31 | 0.7024 | 0.6938 | 0.009 | late |

### 区域均值

| 区域 | s42 | s123 | cross-seed Δ |
|------|-----|------|-------------|
| Early (L0-L6) | 0.2107 | 0.2061 | 0.005 |
| Mid (L7-L13) | 0.3214 | 0.3423 | 0.021 |
| **Valley (L14-L18)** | **0.1806** | **0.1844** | **0.004** |
| Late-mid (L19-L24) | 0.2351 | 0.2065 | 0.029 |
| Late (L25-L31) | 0.5087 | 0.5144 | 0.006 |

### L14-L18 保护谷统计

| 指标 | s42 | s123 |
|------|-----|------|
| L14-L18 mean | 0.1806 | 0.1844 |
| L14-L18 std | 0.0475 | 0.0585 |
| Global mean | 0.3000 | 0.3000 |
| **Valley depth (global - valley)** | **0.1194** | **0.1156** |
| Valley depth relative | 39.8% below mean | 38.5% below mean |

### 与旧 4-sample 结果对比（s42）

| Layer | 4-sample | 32-sample | Δ |
|-------|----------|-----------|---|
| L14 | 0.2462 | 0.2642 | +0.018 |
| L15 | 0.1799 | 0.1967 | +0.017 |
| L16 | 0.1374 | 0.1603 | +0.023 |
| L17 | 0.1677 | 0.1567 | -0.011 |
| L18 | 0.1534 | 0.1253 | -0.028 |
| **L14-L18 mean** | **0.1769** | **0.1806** | **+0.004** |

### 结论

1. **L14-L18 保护谷 seed-general 确认**：两个 seed 的 valley mean 几乎一致（0.1806 vs 0.1844, Δ=0.4pp），valley depth 均约 ~12pp below global mean (~39%)
2. **32 vs 4 samples 差异极小**：s42 的 L14-L18 mean 从 0.1769→0.1806（+0.4pp），结构性 pattern 完全不变
3. **L16 完美一致**：两个 seed 在 L16 的 sparsity 都是 0.1603（4位小数相同）
4. **Valley 内排序一致**：两个 seed 都呈现 L14 > L15 > L16 ≈ L17 > L18 的 V 形，最低点在 L18

结果文件已保存：
- `results/perlayer_sparsity_30pct_s42_32samples.json`
- `results/perlayer_sparsity_30pct_s123_32samples.json`

---
