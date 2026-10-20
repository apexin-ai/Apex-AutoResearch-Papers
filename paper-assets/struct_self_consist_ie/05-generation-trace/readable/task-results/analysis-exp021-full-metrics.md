# analysis exp021 full metrics

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp021_full_metrics_20260516T220747_result.json`
- **Structured JSON:** [`b209bed946c0215556cc.json`](../../sessions/b2/b209bed946c0215556cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部指标已补全。以下是完整结果汇总：

---

## Exp-021 Few-NERD 完整分析结果

**数据规模**: 37,648 instances (过滤 gold-empty 后 32,565), N=8 samples/instance

### 1. Basic Metrics

| 指标 | Few-NERD | SciERC (ref) | CoNLL (ref) |
|------|----------|--------------|-------------|
| Greedy macro F1 | 0.7478 | 0.614 | — |
| Oracle macro F1 | 0.8719 | 0.752 | — |
| Headroom | 12.4pp | 13.8pp | — |
| Zero-F1 rate | 11.9% | — | — |
| **Degeneracy rate** | **10.1%** | 21% | 58% |

**Degeneracy 定义**: instance 内 N=8 samples 的 key_sets（entity spans 集合）全部相同（unique == 1）。Few-NERD 的 10.1% 远低于 SciERC (21%) 和 CoNLL (58%)，说明多样性充足。

### 2. LP Within-Instance Range

| 统计量 | 值 |
|--------|------|
| Mean | 0.0879 |
| Median | 0.0662 |
| Std | 0.0758 |
| P25 | 0.0344 |
| P75 | 0.1239 |

### 3. Sample-Level AUROC（oracle label = argmax F1 sample）

| Signal | AUROC |
|--------|-------|
| **LP** | **0.5782** |
| VC | 0.5354 |
| FK | 0.5210 |
| SJ | 0.5197 |
| EM | 0.5137 |

### 4. Instance-Level Spearman ρ（signal vs greedy F1）

| Signal | ρ (global) | ρ (conditional, non-degenerate) |
|--------|-----------|-------------------------------|
| **LP** | **0.4215** | **0.4225** |
| VC | 0.3858 | 0.3234 |
| FK | 0.3132 | 0.3093 |
| SJ | 0.3002 | 0.2937 |
| EM | 0.2871 | 0.2710 |

### 5. Selection F1 (pick best-scoring sample per signal)

| Signal | Sel F1 | Δ vs greedy |
|--------|--------|-------------|
| **LP** | **0.7614** | **+1.36pp** *** |
| VC | 0.7299 | -1.79pp |
| SJ | 0.7264 | -2.14pp |
| FK | 0.7253 | -2.26pp |
| EM | 0.7093 | -3.85pp |

LP delta 95% CI: [+1.18, +1.53], p < 0.001

### 6. Cross-Dataset Comparison

| Dataset | Greedy | Oracle | Headroom | LP ρ | LP Δ |
|---------|--------|--------|----------|------|------|
| SciERC | 0.614 | 0.752 | +13.8pp | 0.205 | +0.42pp |
| **Few-NERD** | **0.748** | **0.872** | **+12.4pp** | **0.421** | **+1.36pp** |

结果已保存到 `output/exp_021_inference/results.json`。

**关键发现**: Few-NERD 上 LP signal 表现远强于 SciERC（ρ 翻倍: 0.42 vs 0.21, Δ 3倍: +1.36 vs +0.42），degeneracy 极低 (10.1%)，LP range 适中 (median 0.066)，说明在低 degeneracy 场景下 LP 信号的区分力显著增强。

---
