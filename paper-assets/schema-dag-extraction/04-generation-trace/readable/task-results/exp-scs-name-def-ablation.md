# exp scs name def ablation

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_scs_name_def_ablation_20260516T114937_result.json`
- **Structured JSON:** [`2d20efd0879ae2ce720d.json`](../../sessions/2d/2d20efd0879ae2ce720d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

## SCS Name vs Name+Definition Ablation 结果

| Dataset | SCS_name r | SCS_def r | Δr | Sim矩阵相关 | name p | def p |
|---------|-----------|----------|------|------------|--------|-------|
| **Few-NERD** | 0.172 | 0.149 | **-0.023** | 0.894 | 2.0e-14 | 4.0e-11 |
| MAVEN | 0.129 | 0.164 | +0.035 | 0.656 | 3.1e-42 | 1.1e-67 |
| FewRel | 0.178 | 0.193 | +0.015 | 0.848 | 8.6e-24 | 9.3e-28 |

**关键结论（可用于 Reviewer W-C1 response）：**

1. **Few-NERD**（唯一在 prompt 中包含 type definitions 的数据集）：加入 definitions 后 SCS 反而略降（Δ=-0.023），两者均高度显著（p<1e-10）。Name-only 和 name+def 相似度矩阵相关 r=0.894，说明 type name 已捕获主要语义结构。

2. **MAVEN/FewRel**：这两个数据集的 prompt **不包含 type definitions**（MAVEN 的 config 只有 name→name，FewRel 的 relation labels 本身就是描述性短语），因此 SCS_name 已经完全匹配 prompt 中给 LLM 的内容。

3. **Delta 方向不一致**：Few-NERD 为负，MAVEN/FewRel 为正，表明加入 definitions 对 SCS-confusion 相关性无系统性影响。

结果保存在 `/root/schema-dag-extraction/artifacts/scs_name_def_ablation/results.json`。

---
