# research ace05 data prep

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ace05-data-prep_20260515T025909_result.json`
- **Structured JSON:** [`7d6460fb88e8ae1dd6f1.json`](../../sessions/7d/7d6460fb88e8ae1dd6f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。产出摘要：

**调研报告** → `artifacts/exp-004/report/ace05_data_prep_report.md` (art_20260515_08dc50)

核心发现：

1. **类型体系**：7 entity types (PER/ORG/GPE/LOC/FAC/VEH/WEA) + 6 relation types 细分为 18 subtypes（ART→1, GEN-AFF→2, ORG-AFF→7, PART-WHOLE→3, PER-SOC→3, PHYS→2）

2. **数据获取**：需 LDC 许可 (LDC2006T06, $300)，HuggingFace 上无公开版本。GitHub 有多个预处理工具（PURE, DyGIE++, ACE05-Processor）

3. **许可证**：可用于研究发表，不可重分发原始数据

4. **与 Few-NERD 关键差异**：ACE05 是新闻领域、7 types + 18 relation subtypes、联合标注；Few-NERD 是 Wikipedia、66 fine-grained NER types、无关系标注

5. **预处理方案**：NER 和 RE 分开处理，NER 复用 Few-NERD pipeline 改 type 列表，RE 需新增 relation triple 匹配逻辑

6. **快速推进建议**：BCS 验证可先用 18 个 relation subtype names 计算 embeddings + 分析混淆度分布，不依赖原始数据。同时并行获取 LDC 数据

---
