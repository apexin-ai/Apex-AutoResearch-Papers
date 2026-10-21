# analysis fewrel domain distribution

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fewrel_domain_distribution_20260522T045738_result.json`
- **Structured JSON:** [`44295ab5d2f29c877b1d.json`](../../sessions/44/44295ab5d2f29c877b1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**Domain 分布显著不同** (χ²=230.74, p<0.001, df=5)，但这不是传统 confound：

| 指标 | Low-BCS (25 batches) | High-BCS (25 batches) |
|------|---------------------|----------------------|
| BCS 范围 | 0.356–0.367 | 0.791–0.811 |
| 主导 domain | geography (45.5%), creative_work (25.5%) | science_taxonomy (49.5%), event_temporal (26.0%) |
| 归一化 entropy | 0.79 | 0.67 |
| Unique types | 22 | 14 |
| 类型重叠 | 仅 1 个 type |

**关键解读**：High-BCS batches 集中在 taxonomic/structural 关系（follows/followed_by, part_of/has_part, member_of, instance_of）——这些 type 本身语义特征高度重叠，cosine similarity 自然高。Domain 集中是 BCS 的 **预期机制**（mediator），不是独立的 confounding variable。

LaTeX 段落已写入 `fewrel_domain_distribution.json` 的 `latex_appendix` 字段，可直接插入 Appendix。两个 artifact 已注册。

---
