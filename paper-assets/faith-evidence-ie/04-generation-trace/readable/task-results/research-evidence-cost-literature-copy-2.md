# research evidence cost literature

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_evidence-cost-literature_20260516T041839_result.json`
- **Structured JSON:** [`e72748554750c1e48f31.json`](../../sessions/e7/e72748554750c1e48f31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搜索完成。结果总结：

## 新颖性评估：高度新颖

**没有任何现有论文在 "generative SFT + DocRE" 设定下量化过 evidence 对 rel_f1 的代价。**

### 关键对比

现有工作（DREEAM、E2GRE、Two Flints）都在 **encoder-based discriminative** 模型中研究 evidence，且一致发现 evidence **帮助** RE。原因是 evidence 作为 attention supervision 引导模型聚焦相关 context。

FREIGE 的设定根本不同：**generative LLM SFT** 要求模型在输出中同时生成 evidence + relation，这是一个更难的任务——模型必须在有限 output capacity 中分配 token budget。-7.7 F1 的 evidence tax 在文献中是首次量化。

### 已加入 literature_map.yaml（Category 36，6 篇）

| 论文 | Role | 核心差异 |
|------|------|---------|
| Two Flints (Tang & Surdeanu, CL 2023) | direct_competitor | Sentence-level extractive → joint 有益 (+4% F1) |
| Robust Explanation (Tan & Tian, ICML 2023) | theoretical_foundation | 理论证明 faithfulness 有代价 |
| Rationalization Survey (Gurrapu+, 2023) | background_survey | Desiderata: "不应有害"，FREIGE 直接反驳 |
| CoT-ER (Yin+, EMNLP 2023 Findings) | related_method | Prompting 下 evidence 有益，与 SFT 对比 |
| E2GRE (Huang+, RepL4NLP 2021) | direct_competitor | DocRE joint evidence+RE 先驱，encoder-based → 有益 |
| Revisiting RE (Wadhwa+, ACL 2023) | background | LLM generative RE baseline |

详细报告已写入 `artifacts/evidence_cost_literature_scan.md`。

---
