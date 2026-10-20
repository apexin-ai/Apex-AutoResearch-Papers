# audit exp data utilization

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_exp-data-utilization_20260520T050056_result.json`
- **Structured JSON:** [`a306995f868953247e2e.json`](../../sessions/a3/a306995f868953247e2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all 42 successful experiments and the complete paper content. Let me cross-reference systematically.

## 实验数据利用审计结果

### 方法
对每个 success 实验，匹配其关键指标数字、实验描述关键词是否出现在论文 tex 文件中。论文中不使用 exp_id 字符串，因此匹配基于数值和语义。

### 汇总

**38/42 实验已被引用**（直接引用或作为数据生成步骤被下游实验间接引用）

**4/42 实验未被引用**——均为被后续实验取代的早期/中间版本：

| exp_id | 实验名 | 当前引用状态 | 建议 |
|--------|--------|-------------|------|
| **mvp-001** | MVP: Pythia-2.8B within-model depth classification (F1=0.84) | 未引用。被 8-gen LOGO 评估取代。within-model 性能已被 transfer matrix 对角线覆盖（0.969-0.991） | **无需补充**。transfer matrix (appendix_transfer) 已展示 within-model 性能 |
| **plan-001** | Feature ablation (初版) | 未引用。被 plan-001-fix 取代，plan-001-fix 又被 8-gen 版本取代 | **无需补充**。8-gen feature ablation (table2/appendix_ablation) 已覆盖 |
| **plan-001-fix** | Feature ablation (修正版，F1=0.82, ppl\_by\_depth: 13.5/5.0/3.0/2.1/1.7) | 未引用。独特数据点是 explicit perplexity-by-depth 曲线，但概念上已被 entropy trend 分析覆盖 | **无需补充**。appendix\_feature\_distributions 的 DDR trend 图已展示同等信息 |
| **plan-015** | Ordinal baseline (含 Binoculars bug) | 未引用。被 plan-015-v2 (bugfix) 取代，v2 结果已在 results.tex baselines 表中 | **无需补充**。bugfix 版本已被引用 |

### 间接引用的数据生成实验（12个）

以下实验本身是数据生成步骤，其数据被下游评估实验使用，算间接引用：

- `plan-002` + 8个 shard (`plan-002-pythia1b-s0/s1`, `plan-002-olmo2-s0/s1`, `plan-002-qwen17b-r2-s0/s1`, `plan-002-qwen06b-r2-s0/s1`) → 被 `plan-002-eval` 使用
- `plan-003-olmo2ref`, `plan-003-qwen06bref` → 被 `plan-003` cross-ref 评估使用
- `plan-005-cont`, `plan-005-elab`, `plan-005-rewrite` → 被 `plan-005` prompt-type 评估使用
- `plan-004-prep` → 被 downstream fine-tuning 实验使用 (appendix\_downstream)

### 结论

**所有有独立分析价值的成功实验均已被论文引用。** 4个未引用实验都是被改进版本取代的早期迭代，其独特数据点已被后续实验的更全面版本覆盖。无需补充新的 appendix 内容。

---
