# research related work literature check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_literature_check_20260522T015503_result.json`
- **Structured JSON:** [`20949011ec9bcfa740f7.json`](../../sessions/20/20949011ec9bcfa740f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/related_work_literature_check.md`。

核心发现：**4 篇潜在遗漏**，优先级排序：

1. **Golde et al. (NAACL 2025)** — "Familiarity" 指标用 entity type 间的语义相似度预测 zero-shot NER 难度，与我们的 type confusability 概念高度重合，最可能被 reviewer 指出遗漏
2. **Swarup et al. (COLING 2025)** — 2100+ 实验证明 LLM 对 RE 中的复杂数据特征不 robust
3. **Nolano et al. (LREC-COLING 2024)** — 语义相似的对抗替换导致 RE 模型 F1 下降 48.5%，从互补角度支持 confusability 假设
4. **GLiREL (NAACL 2025)** — borderline，关于 relation type 数量带来的 scalability 瓶颈

---
