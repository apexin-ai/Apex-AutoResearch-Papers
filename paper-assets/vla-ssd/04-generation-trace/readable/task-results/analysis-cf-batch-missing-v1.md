# analysis cf batch missing v1

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cf_batch_missing_v1_20260522T012627_result.json`
- **Structured JSON:** [`7f987d79ddcc5a6e7ae5.json`](../../sessions/7f/7f987d79ddcc5a6e7ae5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。5/5 条件全部成功，registry 和 artifact 已更新。

**核心发现**：

| Condition | Untrained Ordering (cos_dist) |
|-----------|-------------------------------|
| OpenVLA Object | E(0.569) >> S(0.298) > W(0.231) > P(0.085) |
| TracVLA Spatial | E(0.180) > S(0.140) >> W(0.005) ~ P(0.004) |
| TracVLA Object | E(0.185) >> S(0.098) >> P(0.005) ~ W(0.004) |
| TracVLA Goal | E(0.153) >> S(0.084) >> W(0.016) > P(0.004) |
| TracVLA Long | E(0.173) >> S(0.120) >> W(0.022) > P(0.007) |

所有 untrained 模型呈现一致的两层结构：结构扰动（empty, shuffled）产生大的表征偏移，语义扰动（wrong, para）几乎无影响。训练后 wrong 条件的敏感度显著上升，与 shuffled 缩小差距——说明训练建立了对语义内容（具体物体/动作名称）的 grounding。

OpenVLA base 在所有条件上 cos_dist 绝对值远大于 TracVLA base（Llama-2 vs Phi-3V 架构差异）。

---
