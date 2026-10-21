# research ced anti collapse literature

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ced-anti-collapse-literature_20260514T183829_result.json`
- **Structured JSON:** [`7cdfacbee2c6d7514d80.json`](../../sessions/7c/7cdfacbee2c6d7514d80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研报告已写入并注册。覆盖 25+ 篇论文，按三个方向分类：

**关键发现**：
- GX-Chen et al. (2025) 的理论直接解释了我们的现象——等值 verifiable reward（如 extraction-only 的 F1）天然指定单峰目标分布，导致 mode collapse；CED 增加的 evidence quality 维度打破了这种等值性
- EDGE-GRPO 对 advantage collapse（frac_zero_std）的分析是我们观察的理论基础
- CTRL-RAG 是 contrastive reward for faithfulness 的最近先例，但未分析 anti-collapse 效应——这是我们的独特贡献点

**Paper story 建议**：CED 的 anti-collapse 定位为 surprising finding + principled explanation（非 main contribution），在 Analysis section 展开，引用 GX-Chen → EDGE-GRPO → DiverseGRPO 的理论链条。

---
