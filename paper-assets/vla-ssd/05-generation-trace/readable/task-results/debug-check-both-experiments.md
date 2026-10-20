# debug check both experiments

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_check_both_experiments_20260518T073739_result.json`
- **Structured JSON:** [`7b60ef6a218be888a6e0.json`](../../sessions/7b/7b60ef6a218be888a6e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成。汇总如下：

---

## 1. threecond_multiseed.json

3 conditions × 3 seeds (42, 123, 456) × 33 layers (L0–L32)，target = goal classification R²。

| Layer | untrained (mean±std) | llama2base (mean±std) | trained (mean±std) |
|-------|--------------------|-----------------------|-------------------|
| L0 | 0.538±0.015 | 0.538±0.015 | 0.538±0.015 |
| L1 | 0.444±0.017 | 0.537±0.018 | 0.534±0.020 |
| L2 | 0.452±0.017 | 0.544±0.008 | 0.526±0.020 |
| L6 | 0.448±0.008 | 0.530±0.015 | **0.544±0.010** |
| L10 | 0.432±0.002 | **0.543±0.014** | **0.548±0.012** |
| L13 | 0.326±0.120 | 0.526±0.023 | 0.546±0.015 |
| L15 | 0.433±0.037 | 0.528±0.008 | 0.542±0.014 |
| L20 | 0.220±0.285 | 0.512±0.023 | 0.475±0.031 |
| L25 | 0.263±0.094 | 0.492±0.033 | 0.447±0.065 |
| L29 | 0.117±0.225 | 0.466±0.008 | 0.396±0.097 |
| L32 | 0.501±0.013 | 0.464±0.030 | 0.435±0.031 |

关键观察：
- **untrained**: 高 variance，深层急剧下降（L20–L31 大量负或近零值），L0 和 L32 是两个局部高点，中间层不稳定
- **llama2base**: 非常平稳，从 L0 (0.538) 缓慢单调下降到 L32 (0.464)，std 很小
- **trained**: 早/中层略高于 llama2base（peak ~L10 = 0.548），深层也下降但比 untrained 稳定得多
- trained 和 llama2base 在 L0–L15 非常接近（差异 <0.02），深层 trained 略低于 llama2base

---

## 2. linear_probe_last_preaction.json

Linear probe predicting next action a_{t+1}，trained vs untrained，33 layers。

**Summary（JSON 自带）**:
- **trained peak**: L13, R² = 0.596
- **untrained peak**: L1, R² = 0.492
- **inverted_U_trained**: true
- **inverted_U_untrained**: true
- trained > untrained at peak: true

**Bootstrap comparisons**:
- trained vs untrained (best-vs-best): Δ = 0.103, 95% CI [0.056, 0.167], p = 0.0
- trained vs untrained (same layer at trained peak): Δ = 0.513, 95% CI [0.314, 0.789], p = 0.0

| Layer | trained R² | untrained R² | Δ |
|-------|-----------|-------------|-----|
| L0 | -0.321 | -0.332 | +0.011 |
| L1 | 0.192 | **0.492** | -0.300 |
| L5 | 0.398 | 0.352 | +0.047 |
| L9 | 0.540 | -0.037 | **+0.577** |
| L13 | **0.596** | 0.083 | **+0.513** |
| L16 | 0.592 | -0.066 | +0.658 |
| L20 | 0.574 | -0.358 | +0.932 |
| L25 | 0.534 | -0.151 | +0.685 |
| L29 | 0.533 | -0.574 | +1.107 |
| L32 | 0.466 | 0.438 | +0.028 |

关键观察：
- **trained**: 清晰的 inverted-U，L1–L13 单调上升，L13 peak (0.596)，之后缓慢下降到 L32 (0.466)
- **untrained**: L1 spike (0.492)，之后迅速崩溃到负值，L9–L30 几乎全部 <0（大部分负值），L32 突然回到 0.438
- trained 在 L5+ 全面碾压 untrained，差距在中深层极大
- **MLP comparison**: MLP trained peak 也在 L13 (R²=0.678)，比 linear (0.596) 高 0.082；MLP untrained peak 在 L32 (0.609)

---
