# write related work contrastive expand

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_related-work-contrastive-expand_20260515T051038_result.json`
- **Structured JSON:** [`19b467458e1c1768a1eb.json`](../../sessions/19/19b467458e1c1768a1eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出总结：

**新增 6 篇引用**（全部经 WebSearch 验证）：

| 论文 | Venue | 插入位置 |
|------|-------|---------|
| SynCoBERT | arXiv 2021 | §2.2 Contrastive Learning for Code |
| ContraBERT | ICSE 2023 | §2.2 Contrastive Learning for Code |
| CAPSTONE | EMNLP 2023 | §2.3 Hard Negative Mining |
| CrossCodeEval | NeurIPS 2023 | §2.4 Code Structure / Evaluation |
| ProGraML | ICML 2021 | §2.4 Code Structure / Evaluation |
| CoSQA | ACL 2021 | §2.4 Code Structure / Evaluation |

**注意**：任务中推荐的 RocketQA 已在 v1 草稿中引用，无需重复添加。

**产出文件**：
- 段落草稿：`artifacts/paper_drafts/related_work_supplement.md` — 3 个补充段落，含插入位置标注和 StructFuse 定位说明
- BibTeX entries：追加到 `artifacts/paper_drafts/references.bib`（6 条新 entry）

**段落逻辑**：
- **Supplement A**：SynCoBERT（语法引导）+ ContraBERT（鲁棒性增强）→ 这些方法改进正样本构造，StructFuse 改进负样本选择
- **Supplement B**：CAPSTONE 课程学习式采样 → StructFuse 的结构化负样本提供正交的难度来源
- **Supplement C**：CrossCodeEval 验证跨文件上下文重要性 + ProGraML 全程序图表示 + CoSQA 真实查询分布 → 支撑 StructFuse 的跨文件结构训练目标

---
