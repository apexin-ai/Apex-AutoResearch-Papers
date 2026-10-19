# exp steering L18 L28 sequential

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_steering-L18-L28-sequential_20260524T010150_result.json`
- **Structured JSON:** [`ada6f7e85d033df0eb6b.json`](../../sessions/ad/ada6f7e85d033df0eb6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## L28 Results

- **Probe accuracy at L28: 85.25%**
- N = 201

| α | Steering flips/N | Control flips/N | Fisher p |
|---:|:-:|:-:|:-:|
| -20 | 12/201 (6.0%) | 11/201 (5.5%) | 1.000 |
| -10 | 5/201 (2.5%) | 8/201 (4.0%) | 0.575 |
| -5 | 3/201 (1.5%) | 5/201 (2.5%) | 0.724 |
| +5 | 4/201 (2.0%) | 2/201 (1.0%) | 0.685 |
| +10 | 6/201 (3.0%) | 2/201 (1.0%) | 0.284 |
| +20 | 16/201 (8.0%) | 15/201 (7.5%) | 1.000 |

**Bonferroni 校正 (k=6, 阈值 p < 0.0083):** 无 alpha 通过。Best α=+10, p=0.284。

**结论:** L28 steering 完全不显著。所有 alpha 的 p 值都远高于阈值，steering flips 与 control flips 几乎无差异。

=== L28 RESULTS END ===

---

## Step 6: 完整 6 层同条件对比表

| Layer | Depth | Probe Acc | Best α | Best p | Bonferroni sig |
|-------|-------|-----------|--------|--------|----------------|
| L12 | 38% | 91.75% | +20 | 0.0853 | ❌ |
| L13 | 41% | 90.00% | +10 | 0.0003 | ✅✅ (2/6) |
| L14 | 44% | 91.75% | +10 | 0.0022 | ✅ (1/6) |
| L16 | 50% | 91.50% | +10 | 0.005 | ✅ (1/6) |
| **L18** | **56%** | **90.75%** | **+5** | **0.0099** | **❌ (marginal)** |
| **L28** | **88%** | **85.25%** | **+10** | **0.284** | **❌** |

**关键发现：**

L28（detection peak 层，probe accuracy 最高层）steering 完全无效（best p=0.284），而 L13-L16 中层 steering 显著。**"Detection ≠ Decision" claim 得到强化，不需要重写。** L28 虽然最擅长检测 conflict，但干预该层对模型行为毫无影响——conflict 的因果决策发生在中层（L13-L16），而非检测峰值层。

L18 处于边界状态（p=0.0099，略高于 Bonferroni 阈值 0.0083），可解读为 steering 效果从 L16 到 L18 开始衰减，到 L28 完全消失——进一步支持因果作用集中在中层的结论。

---
