# analysis sf5 bonferroni cohens d

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sf5-bonferroni-cohens-d_20260523T041527_result.json`
- **Structured JSON:** [`a9cdea7aed0c7e6f3478.json`](../../sessions/a9/a9cdea7aed0c7e6f3478.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。更新内容总结：

**表格变更** (`appendix_discussion.tex:175-201`)：
- 新增 Cohen's $d$ 列，共 8 个配置（4 R-F1 + 4 DR%）
- R-F1 效应量：$|d| \in [0.01, 0.37]$，全部 negligible 到 small
- DR% 效应量：$|d| \in [3.02, 7.00]$，全部 large
- 表头从 5 列扩展到 6 列，`\multicolumn` 已同步更新

**文本变更** (line 170-173)：
- 新增逐配置 Bonferroni 校正后 p 值：Qwen3-8B/DocRED $p_B=0.224$ 是最接近显著的，其余均 $p_B=1.00$
- 明确说明 k=4, $\alpha_{\text{adj}}=0.0125$ 阈值
- DR% 全部 $p_{\text{Bonf}} < 0.005$

**数据来源**：westd-16980 上从原始 eval JSONL 重新运行 10,000 次 bootstrap 计算，结果存于 `/root/schema_semantic_constrained_ie/outputs/r20_cohens_d_pvalues.json`。

---
