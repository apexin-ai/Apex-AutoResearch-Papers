# analyze eval pi05 random k03 goal seed42 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k03_goal_seed42_postfix_20260524T110731_result.json`
- **Structured JSON:** [`11ab4d6cf87c95c423fc.json`](../../sessions/11/11ab4d6cf87c95c423fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已更新为 DONE/success。汇总：

## π0.5 Random Goal Post-fix 结果

| Task | k=0.3 | k=0.95 | Baseline |
|------|-------|--------|----------|
| T0 open middle drawer | 88% | 86% | — |
| T1 put bowl on stove | 6% | 94% | — |
| T2 wine bottle on cabinet | 72% | 84% | — |
| T3 open drawer put bowl | 40% | 78% | — |
| T4 bowl on cabinet | 70% | 98% | — |
| T5 push plate front stove | 30% | 92% | — |
| T6 cream cheese in bowl | 32% | 88% | — |
| T7 turn on stove | 100% | 100% | — |
| T8 bowl on plate | 68% | 96% | — |
| T9 wine bottle on rack | 22% | 10% | — |
| **Overall** | **52.8%** | **82.6%** | **88.4%** |

关键观察：
- **k=0.3**: 52.8%，与 pre-fix 的 50.6% 基本一致（+2.2pp），post-fix 未改变趋势，数据有效
- **k=0.95**: 82.6%，接近 baseline 88.4%（-5.8pp），符合 near-baseline 预期。比 Object k=0.95 (74%) 和 Spatial k=0.95 (76.8%) 都更接近 baseline，Goal suite 确实对 random pruning 更鲁棒
- **T9 (wine bottle on rack)** 在两个 k 值下都很低（22% / 10%），这个 task 本身可能就困难

---
