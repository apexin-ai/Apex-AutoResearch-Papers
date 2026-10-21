# eval fromscratch seed42 fix

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_fromscratch_seed42_fix_20260519T233530_result.json`
- **Structured JSON:** [`bad945f7d604232697d3.json`](../../sessions/ba/bad945f7d604232697d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 eval 完成。汇总全部结果：

---

## 完整结果汇总

### 1. PPL Eval（OOD 泛化）

| Eval Set | seed42 | seed123 | seed456 | seed42 vs range |
|----------|--------|---------|---------|-----------------|
| **holdout** | **17.689** | 17.677 | 17.683 | +0.006~0.012 |
| **openwebtext** | **18.370** | 18.373 | 18.366 | 在范围内 |
| **wikipedia** | **15.349** | 15.370 | 15.345 | 在范围内 |

### 2. Downstream Eval（5 benchmark）

| Task | Metric | Value | Stderr |
|------|--------|-------|--------|
| arc_challenge | acc | 0.3208 | ±0.0136 |
| arc_challenge | acc_norm | 0.3524 | ±0.0140 |
| arc_easy | acc | 0.6557 | ±0.0097 |
| arc_easy | acc_norm | 0.6178 | ±0.0100 |
| hellaswag | acc | 0.3807 | ±0.0048 |
| hellaswag | acc_norm | 0.4806 | ±0.0050 |
| piqa | acc | 0.6834 | ±0.0109 |
| piqa | acc_norm | 0.6844 | ±0.0108 |
| winogrande | acc | 0.5801 | ±0.0139 |

### 3. Distribution Matching 假设判断

**假设成立。** 三个随机种子的 PPL 结果几乎完全一致：
- holdout PPL 范围 17.677–17.689（跨种子波动仅 0.012）
- openwebtext PPL 范围 18.366–18.373（波动仅 0.007）
- wikipedia PPL 范围 15.345–15.370（波动仅 0.025）

From-scratch adaptive 训练在不同随机初始化下收敛到高度一致的 OOD 泛化性能，表明学到的权重分布具有稳定性，不是偶然的种子效应。

---
