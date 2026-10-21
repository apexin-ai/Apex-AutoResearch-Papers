# analysis binoculars ordinal baseline 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_binoculars_ordinal_baseline_001_20260519T183847_result.json`
- **Structured JSON:** [`f4f50158b98738c95627.json`](../../sessions/f4/f4f50158b98738c95627.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 和 memory 均已更新。以下是完整分析结果：

---

## binoculars_ordinal_baseline_001 结果分析

### Conclusion: **NEGATIVE**（假设被证伪）

Binoculars cross-perplexity 包含强 ordinal depth 信号，远非 "near-chance"。

### Per-cell 4-class Accuracy (RF_multi, 最佳方法)

| Cell | RF_multi | equal_width |
|------|----------|-------------|
| gpt2xl_nucleus | **85.2%** | 50.6% |
| gpt2xl_temp09 | 82.9% | 62.1% |
| gpt2xl_topk50 | 73.5% | 47.5% |
| olmo_nucleus | 81.8% | 53.3% |
| olmo_temp09 | 81.0% | 58.8% |
| olmo_topk50 | 70.5% | 39.7% |
| pythia_nucleus | 80.4% | 37.5% |
| pythia_temp09 | 79.5% | 49.5% |
| pythia_topk50 | **68.1%** (worst) | 40.4% |

### 9-cell 平均（5 种 calibration 方法）

| Method | 4-class Acc | d1-d3 BalAcc |
|--------|------------|-------------|
| equal_width | 48.8% | 41.7% |
| CORAL | 38.1% | 50.8% |
| threshold | 69.8% | 60.2% |
| RF_single | 63.7% | 53.4% |
| **RF_multi** | **78.1%** | **71.2%** |

### Baseline 对比

| Method | 9-cell Avg 4-class |
|--------|-------------------|
| Chance | 25.0% |
| DetectGPT | 29.1% |
| Min-K% | 33.2% |
| **Binoculars (equal_width)** | **48.8%** |
| **Binoculars (RF_multi)** | **78.1%** |
| Our RF-19 | 78.4% |

### 关键发现

- 即使最简单的 equal-width binning（48.8%）也是 chance 的 ~2x，远超 DetectGPT/Min-K%
- RF_multi (78.1%) 几乎追平我们的 RF-19 (78.4%)，但它用了 11 个 Binoculars-derived perplexity 特征
- topk50 cells 一致最弱（68-74%），可能因 top-k 截断损失了 perplexity ratio 信息
- **论文叙事需要调整**：不能 claim "binary methods can't do ordinal"，Binoculars 是 strongest baseline，需如实对比。差异化论点应聚焦于：我们的方法 model-agnostic（不需要 observer/performer model pair）

---
