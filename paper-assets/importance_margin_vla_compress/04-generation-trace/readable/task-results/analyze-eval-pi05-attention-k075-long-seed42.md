# analyze eval pi05 attention k075 long seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_attention_k075_long_seed42_20260526T084214_result.json`
- **Structured JSON:** [`7f6c129574d65c3c61f3.json`](../../sessions/7f/7f6c129574d65c3c61f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果汇总

**Overall SR: 51.8%** (259/500)，无报错，EXIT_CODE=0。

### Per-task 明细

| Task | Description | SR |
|------|-------------|-----|
| T0 | alphabet soup + tomato | 68% |
| T1 | cream cheese + butter | 78% |
| T2 | stove + moka pot | 56% |
| T3 | black bowl → drawer | 42% |
| T4 | white mug on plate | 36% |
| T5 | book → back | 44% |
| T6 | white mug on plate (2) | 80% |
| T7 | alphabet soup + cream | 30% |
| T8 | both moka pots → stove | 6% |
| T9 | yellow mug → microwave | 78% |

### Attention scoring cliff curve (π0.5 Long)

| Method | k=1.0 | k=0.9 | k=0.75 |
|--------|-------|-------|--------|
| **Attention** | 92.8% | 63.8% | **51.8%** |
| L2norm | 92.8% | 80.0% | — |
| Random | 92.8% | ~35.6% | 65.8% |

### 对比分析

1. **Attention k=0.9→0.75 衰减**: 63.8% → 51.8%，降幅 12pp。从 k=1.0 到 k=0.9 降了 29pp，k=0.9 到 k=0.75 降 12pp——衰减速度在减缓，说明 Attention scoring 在 k=0.9 时已经丢掉了最关键的 token，后续继续裁剪的边际伤害反而变小。

2. **vs Random k=0.75**: Attention 51.8% vs Random 65.8%。Attention scoring 在 k=0.75 时**反而不如 Random**，进一步印证 Attention scoring 存在系统性偏差——它保留的 token 并非对动作预测最重要的 token。

3. **vs L2norm**: L2norm k=0.9 = 80%，远好于 Attention 在同压缩率的 63.8%，差距 16pp。L2norm 是明显更优的 scoring 方法。

4. **Cliff 形态**: Attention 从 baseline 92.8% 骤降到 k=0.9 的 63.8%（-29pp），然后缓降到 k=0.75 的 51.8%（-12pp）。这是一个"early cliff"模式——大部分性能损失集中在前 10% token 被裁掉时。

---
