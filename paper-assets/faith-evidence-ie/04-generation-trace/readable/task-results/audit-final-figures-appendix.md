# audit final figures appendix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_final-figures-appendix_20260524T044743_result.json`
- **Structured JSON:** [`5e8be5ed01a8baf2ffbb.json`](../../sessions/5e/5e8be5ed01a8baf2ffbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。82项检查全部 PASS，0 FAIL，4个 LOW severity 警告：

1. **Cross-method ρ 不一致**：正文3处报 ρ=−0.89 (n=7)，附录 partial correlation 节报 raw ρ=−0.9643 (n=7)。方向一致但数值不同，应核实聚合方式。
2. **fig_scaling caption**：文字声称"RSFT narrows the gap"但图中只画了 SFT bars，RSFT 未可视化。
3. **Inference overhead 措辞**：experiments.tex 写"adds 16–24% at 14B"，实际 16% 来自 4B、24% 来自 14B。
4. **Unused bib entry**：`wan2024genres` 定义但未引用。

所有 figure 数据源、appendix 段落数字、Cohen's d / χ² CI / Spearman ρ、\ref/\cite 交叉引用均验证通过。报告已注册为 `art_20260524_fe80e9`。

---
