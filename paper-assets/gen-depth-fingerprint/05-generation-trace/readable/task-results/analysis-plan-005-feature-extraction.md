# analysis plan 005 feature extraction

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-005-feature-extraction_20260515T054435_result.json`
- **Structured JSON:** [`e3e848fa4e2dcc1d7b5c.json`](../../sessions/e3/e3e848fa4e2dcc1d7b5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

特征提取完成。汇总结果：

---

**产出文件**: `autodl-5090:/root/gen-depth-fingerprint/data/pythia-2.8b-continuation/features.jsonl` (4620 行)

**Spearman ρ (feature vs depth)**:

| Feature | ρ | p-value |
|---|---|---|
| entropy_mean | **-0.6650** | < 1e-300 |
| entropy_std | -0.1508 | 6.5e-25 |
| entropy_max | -0.0227 | 0.12 (ns) |
| entropy_min | **-0.4619** | 6e-243 |
| tail_decay | +0.0815 | 2.9e-8 |
| ttr | **-0.6292** | < 1e-300 |
| hapax_ratio | **-0.6507** | < 1e-300 |

**Depth 0 vs 4 均值对比** (主要特征):
- entropy_mean: 2.637 → 1.167 (**-55.7%**)
- ttr: 0.643 → 0.253 (**-60.7%**)
- hapax_ratio: 0.516 → 0.134 (**-74.0%**)

**与原有数据一致性**: 所有特征的 Spearman ρ 方向一致，绝对值差异均 < 0.02。`entropy_mean`, `ttr`, `hapax_ratio` 仍是三个最强 drift 指标。`entropy_max` 在两个数据集中都不显著。高度一致。

---
