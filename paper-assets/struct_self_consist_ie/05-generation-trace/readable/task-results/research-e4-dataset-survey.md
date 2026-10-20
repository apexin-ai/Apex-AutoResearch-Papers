# research e4 dataset survey

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_e4_dataset_survey_20260514T092619_result.json`
- **Structured JSON:** [`913b32139aa966482581.json`](../../sessions/91/913b32139aa966482581.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `memory.md`。核心结论：

**推荐方案：SciERC + CoNLL-2003 + WNUT-17**

- **CoNLL-2003**（新闻，4 types，3.4K test）— NER 标杆数据集，免费，HF 用 `BramVanroy/conll2003`
- **WNUT-17**（社交媒体，6 types，1.3K test）— 噪声文本+新兴实体，SJ 在此设定有效则说服力极强

三个数据集覆盖科学/新闻/社交媒体三个领域，entity types 完全不同。

**关键发现**：
- 现有 `entity_strict_match` 完全通用，无需改
- 无现成 char-offset JSON 转换器（调研了 6 个项目），需自写 ~50 行/数据集
- Per-dataset fine-tune 是唯一合理策略（entity types 不重叠）
- **总工时 ~2-3 天**，DDL 前可完成

**风险**：CoNLL 训练集 14K 条偏大（可 subsample）；OntoNotes 有许可风险不推荐。

---
