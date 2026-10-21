# research literature linkage tracvla 4suite

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-linkage-tracvla-4suite_20260521T204054_result.json`
- **Structured JSON:** [`92e5943a3234418bc1d9.json`](../../sessions/92/92e5943a3234418bc1d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出文件已写入 `artifacts/literature_linkage_4suite_consistency.md`。核心结论：

**无直接竞品论文**报告过跨 task suite 的 attention head consistency pattern。现有 VLA 解释性文献（Grant/Swann/Haon/Rizzardo）全部聚焦行为干预或 SAE 特征，无人追踪 specific head indices 的跨任务一致性。

**h13/h22 head identity preservation 无直接先例**，但有三层文献支撑：
- **Olsson et al. 2022**（induction heads）：head 级功能普遍性的经典范例，但机制是 algorithmic copy，非 routing
- **Basile et al. 2025**（Head Pursuit, NeurIPS spotlight）：多模态 transformer 中 head 专化一致且可操控，但未追踪 same-index cross-task
- **Bali et al. 2026**：中间层 head 跨训练 run 最不稳定——这反而加强我们的 claim：h13/h22 的 cross-task 一致性是 training-induced convergent property，非初始化 artifact

**建议添加 3 条文献到 literature_map.yaml**（bali2026, basile2025_headpursuit, olsson2022_induction），详细条目见产出文件。

**GuidedVLA（Jia et al., 2026.05）**是唯一涉及 VLA attention head specialization 的论文，但它是人工监督强制的，非 emergent——可作为对照引用。

---
