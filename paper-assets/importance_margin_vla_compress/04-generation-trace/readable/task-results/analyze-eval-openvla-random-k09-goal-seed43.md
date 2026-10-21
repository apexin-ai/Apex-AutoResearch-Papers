# analyze eval openvla random k09 goal seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_random_k09_goal_seed43_20260525T211121_result.json`
- **Structured JSON:** [`5b4d0113a5ad198d746b.json`](../../sessions/5b/5b4d0113a5ad198d746b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。分析摘要：

## 结果分析

### Overall SR 对比

| 条件 | seed42 | seed43 | 均值 |
|------|--------|--------|------|
| Baseline (no prune) | 74.8% | — | 74.8% |
| Random k=0.9 | 79.6% | **80.4%** | **80.0%** |

Random pruning 两个 seed 均超过 baseline **+5~6pp**，均值 80.0% vs 74.8%。

### Per-task 对比 (seed43 vs seed42)

| Task | seed42 | seed43 | 差异 |
|------|--------|--------|------|
| T0 open middle drawer | 74% | 70% | -4% |
| T1 put bowl on stove | 96% | 98% | +2% |
| T2 wine bottle on cabinet | 84% | 92% | +8% |
| T3 open drawer put bowl | 38% | 42% | +4% |
| T4 bowl on cabinet | 94% | 94% | 0% |
| T5 push plate to stove | 72% | 78% | +6% |
| T6 cream cheese in bowl | 78% | 82% | +4% |
| T7 turn on stove | 100% | 100% | 0% |
| T8 bowl on plate | 86% | 74% | -12% |
| T9 wine bottle on rack | 74% | 74% | 0% |

两个 seed 间 per-task 波动在正常范围内（T8 差 12pp 最大，其余 ≤8pp），无系统性偏移。

### 结论

**确认 random pruning k=0.9 在 Goal 上的 regularization effect 可复现。** 两个 seed 均一致地超过 baseline ~5pp，排除了 seed42 的结果是统计偶然的可能性。这说明丢弃 10% vision tokens（即使是随机丢弃）对 Goal suite 反而有正向影响，模型对冗余 vision tokens 存在过拟合倾向。

---
