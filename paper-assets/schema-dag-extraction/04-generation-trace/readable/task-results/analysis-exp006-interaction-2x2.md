# analysis exp006 interaction 2x2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp006_interaction_2x2_20260515T183441_result.json`
- **Structured JSON:** [`d0f8f0be45b5bd4586b4.json`](../../sessions/d0/d0f8f0be45b5bd4586b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

## exp006_interaction_2x2 结果 — **Conclusion: negative**

### 2×2 Cell Means (F1)

| | low BCS | high BCS |
|---|---|---|
| **low count (6 types)** | **0.324** ± 0.106 | **0.313** ± 0.099 |
| **high count (22 types)** | **0.325** ± 0.070 | **0.277** ± 0.059 |

### 主效应
- Count: **-0.018** (高 count 略差)
- BCS: **-0.029** (高 confusability 略差)

### 交互效应
- BCS effect @ low count: **-0.011**
- BCS effect @ high count: **-0.048**
- 交互项: **-0.036** — 方向符合 multiplicative（高 count 放大了 BCS 的负效应）
- **z = -0.667, p = 0.505 — 不显著**

交互方向虽然与假设一致，但效应量小（~3.6% F1）且 batch 间方差大，统计功效不足以拒绝 additive null。

---
