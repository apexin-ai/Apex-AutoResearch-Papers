# eval tau 05 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_tau_05_seed42_20260515T164657_result.json`
- **Structured JSON:** [`b6b0b41bd01213dc8625.json`](../../sessions/b6/b6b0b41bd01213dc8625.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。结论：**negative**。

---

## 分析

### PPL 对比

| 实验 | PPL | vs adaptive_fix (17.653) | vs uniform (17.694) |
|------|-----|--------------------------|---------------------|
| τ=0.5 | **17.688** | **+0.035** (worse) | **-0.006** (持平) |
| τ=0.6 | 17.681 | +0.028 | -0.013 |
| τ=0.8 (baseline) | 17.653 | — | -0.041 |

### b* 分布对比

| 指标 | τ=0.5 | τ=0.6 | τ=0.8 (adaptive_fix) |
|------|-------|-------|---------------------|
| mean | 0.392 | 0.590 | 1.399 |
| median | 0.171 | 0.375 | 0.871 |
| zero% | 29.1% | 15.6% | ~0% |
| <0.5 | **78.4%** | ~55% | 20.9% |
| ≥2 | 2.9% | ~5% | 16.1% |

### 因果关系

τ=0.5 更低 → α_eff 上界更松（α_eff ≤ 0.5）→ 约束更容易满足 → b* 更小（mean 0.39 vs 1.40）→ 降权更弱（78% batch 几乎不降权）→ 退化为接近 uniform training → PPL 回到 uniform 水平（17.688 ≈ 17.694）。

τ=0.5 已低于有效阈值，provenance weighting 基本失效。

---
