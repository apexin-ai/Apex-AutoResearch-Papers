# research plan015 design

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan015_design_20260514T161215_result.json`
- **Structured JSON:** [`2d0e36ff74ed5179895b.json`](../../sessions/2d/2d0e36ff74ed5179895b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

设计文档已注册为 artifact `art_20260514_b47344`。

核心结论：

**代码现状**：当前 `train.py` 虽然每 epoch 调 `mine_batch()`，但 embeddings 是从文件一次性加载、从未更新——**实际是 static mining**。

**实验设计**：3 个 variants
1. **static_pt**（当前做法）：pretrained embeddings 一次性挖掘
2. **dynamic_ep**：每 epoch 用当前 checkpoint 重新编码 → 重新挖掘
3. **dynamic_500**（可选）：每 500 steps re-mine

**GPU 开销**：每次 re-mine 仅需 ~5 min（~11K samples re-encode），占总训练时间 <1%。两个 variant 共需 ~44h，可在 M2 完成后单卡串行。

**最可能结果**：Dynamic ≈ Static（<1pp 差异）。理由：数据规模仅 11K，dataflow structural signal 才是核心差异化因素而非 embedding recency。这对论文是最佳场景——直接在 Limitation 段落用实验数据回应 reviewer concern。

---
