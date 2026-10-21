# research literature map init

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_map_init_20260518T153139_result.json`
- **Structured JSON:** [`f0d77b356e96f66565e6.json`](../../sessions/f0/f0d77b356e96f66565e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`literature_map.yaml` 已写入，覆盖三个方向共 17 篇论文：

**layer_importance (5 篇)**
- Gromov et al. (ICLR 2025) — 深层冗余，浅层关键 [foundation]
- ShortGPT (2024) — Block Influence 度量 [foundation]
- Curse of Depth (NeurIPS 2025) — Pre-LN 导致深层无效的理论解释 [foundation]
- Reassessing Layer Pruning (2024) — 删最后 25% 层即可 [context]
- LayerDrop (ICLR 2020) — structured dropout 经典方法 [method-component]

**multi_turn_attention (5 篇)**
- When Attention Closes (2025) — 提出 GAR，与本项目最直接相关 [foundation]
- LLMs Get Lost (2025) — 多轮性能下降 39% 的量化基准 [foundation]
- Intent Mismatch (2026) — scaling 无法解决多轮失败 [context]
- Lost in the Middle (TACL 2024) — U 型 attention 分布经典发现 [foundation]
- Style Amnesia (2025) — system prompt style 衰减 [context]

**residual_gating (7 篇)**
- Mixture-of-Depths (2024, DeepMind) — top-k routing 动态分配计算 [method-component]
- CALM (NeurIPS 2022) — 置信度 early exit [method-component]
- Gated Attention (NeurIPS 2025 Oral) — sigmoid gate 消除 attention sink [method-component]
- SkipNet (ECCV 2018) — 残差网络 gating 先驱 [method-component]
- FlexiDepth (2025) — plug-in router 自适应 skip，**直接竞品** [direct-competitor]
- Skip Middle Layers (2025) — 负面结果参考 [context]

---
