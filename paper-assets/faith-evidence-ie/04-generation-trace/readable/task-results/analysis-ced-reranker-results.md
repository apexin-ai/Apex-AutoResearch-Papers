# analysis ced reranker results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ced_reranker_results_20260515T145044_result.json`
- **Structured JSON:** [`3174e1e4c514d53449e4.json`](../../sessions/31/3174e1e4c514d53449e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总分析：

## CED Reranker PoC 结果

| 方法 | rel_f1 | evi_f1 | EDCR |
|------|--------|--------|------|
| SFT greedy | 0.4057 | 0.7979 | 0.7118 |
| Random (N=8) | 0.4538 | 0.8029 | 0.6763 |
| **CED reranker (N=8)** | **0.4864** | **0.8188** | 0.6156 |
| RSFT 3-seed mean | 0.4596 | 0.8143 | — |
| Oracle reranker (N=8) | 0.6237 | 0.7942 | 0.5262 |

**关键发现：**

1. **CED reranker rel_f1=0.4864，超过 SFT +8.07pp，超过 RSFT mean +2.68pp**——零训练成本击败了需要训练的 RSFT
2. **Oracle ceiling rel_f1=0.6237** (+21.8pp vs SFT)——N=8 候选中蕴含的信息量巨大，CED 目前只捕获了 37%
3. **CED-F1 Spearman r=0.3235**——相关性显著但中等，CED 是有效但不完美的 proxy
4. Random baseline 0.4538 说明 sampling diversity 本身贡献 +4.8pp，CED 在此基础上再加 +3.3pp
5. EDCR 下降（0.6156 vs 0.7118）——N=8 sampling 引入更多 distractor citations

**结论：CED 作为 inference-time reranker 有明确论文价值。** 零训练成本超越 RSFT，且 oracle ceiling 表明更好的 reward model 还有大幅提升空间。

---
