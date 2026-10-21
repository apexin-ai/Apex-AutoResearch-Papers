# analysis threshold sensitivity plan034

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_threshold-sensitivity-plan034_20260515T061933_result.json`
- **Structured JSON:** [`63d25d5fbffae7cccdce.json`](../../sessions/63/63d25d5fbffae7cccdce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册 (`art_20260515_15a10d`)。

核心结论：

1. **1.5x 可用，但不是唯一最优。** 完美分离范围是 **[1.2x, 1.6x]**，任何阈值都给 9/9 正确分类。
2. **分离间隙 = (1.14, 1.62]**，宽度 0.48。1.5x 偏向 trained 一侧（距最近 FN 仅 0.12，距最近 FP 0.36）。~1.4x 更居中。
3. **时间窗口：35K-55K 早期检测 TPR 仅 75%**，因为 008e_v3_s2 到 105K 才突破 1.5x。全窗口 (35K-105K) 才能 100% TPR。
4. **008e_v3_s2 的特殊性**：dt=1 imagination 下病理潜伏到 95K，nve 从 0.68 突变到 3.78。建议论文引入两级制：1.2x warning + 1.5x confirmed。
5. **TNR 在所有窗口、所有阈值 ≥1.2x 下均为 100%** — 假阳性不是问题。

---
