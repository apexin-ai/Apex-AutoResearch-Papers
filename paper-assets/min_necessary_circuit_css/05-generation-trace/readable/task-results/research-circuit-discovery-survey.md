# research circuit discovery survey

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_circuit_discovery_survey_20260512T220726_result.json`
- **Structured JSON:** [`199426445f02d6c36d88.json`](../../sessions/19/199426445f02d6c36d88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/related_work_notes.md` 并注册。

---

## 核心结论

**Q1 方法一致性比较**：**无人将此作为核心贡献。** 多篇论文附带比较了不同方法的 faithfulness（vs ground-truth），但没有论文系统测量方法之间的 pairwise agreement / Jaccard matrix。Méloux et al. 做了单方法内的 variance analysis（Jaccard 仅 0.56），Hanna et al. 发现 overlap 高但 faithfulness 差异大——都是局部证据，不是系统的跨方法一致性研究。

**Q2 Circuit Aggregation**：**无直接竞品，但有两个需要讨论的工作：**
- **CIRCUS (2026.03, arXiv 2603.00523)** 🔴 最大威胁——per-edge stability scoring + consensus extraction，数学框架与 CSS 高度相似。但它变化的是**单方法内的剪枝阈值**，不是跨算法族。必须在论文中明确区分。
- **Mondorf et al. (BlackboxNLP 2025)** 🟡 中等威胁——确实组合了 EAP + EP 的输出（含 union/intersection），但用连续分数平均，且为 workshop 短文。

**Novelty 评估：CSS 的 novelty 站得住。** 跨 N 种根本不同算法族的二值共识、方法间 agreement matrix 分析、基于跨方法共识的 core/contingent 分类——这个精确配方没有被做过。关键是论文中必须：
1. 正面讨论 CIRCUS，论证 cross-method vs intra-method variation 的本质区别
2. 论证二值共识相比连续分数平均（Mondorf）的优势
3. 实验证明 CSS-core 的 faithfulness 确实优于单方法结果

---
