# research evidence cost literature

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_evidence-cost-literature_20260515T210541_result.json`
- **Structured JSON:** [`adff01836bcba55cfb8c.json`](../../sessions/ad/adff01836bcba55cfb8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

literature_map.yaml 已更新，新增 4 个 categories（9-12）共 9 篇论文。

## 调研结果总结

新增论文按 4 个调研方向分布：

| 方向 | Category | 论文数 | 最关键论文 |
|------|----------|--------|-----------|
| Evidence generation 性能代价 | Cat 9 | 4 | EIDER (ACL'22), Mind Your Step (NeurIPS'24) |
| Multi-task negative transfer | Cat 10 | 1 | ForkMerge (NeurIPS'23) |
| Faithfulness vs accuracy | Cat 11 | 3 | Correctness≠Faithfulness (SIGIR'25), Lyu survey (CL'24) |
| Reranking as bridge | Cat 12 | 1 | GENIE (ICLR'24) |

**核心叙事线**：我们的 evidence-grounded RE 的 8pp F1 下降不是孤立现象——
- Sprague et al. 证明 CoT 可降 36% accuracy；Resck et al. 形式化了 performance-plausibility Pareto trade-off
- Wallat et al. 明确区分 correctness 和 faithfulness 是独立且可能冲突的维度
- EIDER 早在 encoder-based DocRE 中就发现 evidence 需要 inference-stage 融合而非 joint generation
- CED reranker 的 NLI verification 思路在 GENIE (ICLR'24) 中有成功先例
- ForkMerge 提供了 auxiliary task negative transfer 的理论解释框架

---
