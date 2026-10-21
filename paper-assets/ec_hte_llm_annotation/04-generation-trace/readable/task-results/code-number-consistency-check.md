# code number consistency check

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_number-consistency-check_20260522T000249_result.json`
- **Structured JSON:** [`26bb2d38d4f898c6f0db.json`](../../sessions/26/26bb2d38d4f898c6f0db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/home/ubuntu/ec_hte_llm_annotation/artifacts/number_consistency_check.md`。

核心发现：

**28项一致，7项不一致，8项无源数据。**

主要不一致：
1. **Table 1 四处边界取整偏差** — HB EC-HTE 的 |Bias| 和 RMSE/Coverage 有 1 个单位的末位偏差（如源数据 0.0104 论文写 0.011，标准四舍五入应为 0.010）
2. **Llama HB Coverage 0.950 vs 源 0.940** — appendix table 中 Llama K=2 n=1000 的 HB coverage 源数据为 0.940，论文写 0.950，影响 "22.7pp" 主张（修正后为 22.5pp）
3. **Subgroup AUC 0.87 vs 源 0.8646** — 标准四舍五入应为 0.86

建议优先核实 Llama coverage 值（可能来自不同 seed batch），并统一 Table 1 的取整方式。

---
