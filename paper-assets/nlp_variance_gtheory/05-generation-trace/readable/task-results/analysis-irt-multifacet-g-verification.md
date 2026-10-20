# analysis irt multifacet g verification

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_irt_multifacet_g_verification_20260522T090122_result.json`
- **Structured JSON:** [`4cf26299d75f798d3a3a.json`](../../sessions/4c/4cf26299d75f798d3a3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**Multi-facet G at n=116: 取决于哪个分析框架。**

| 分析 | Conditions | G@116 | G@200 |
|------|-----------|-------|-------|
| exp-001 单模型 (Llama, 1296 cond) | 1296 | **0.895** | 0.936 |
| exp-004 8模型 (2304 cond) | 2304 | **0.834** | 0.896 |

**0.895 = 正确**，但有重要限定：

- 这个数字来自 `single_condition_dstudy.md`，基于 **exp-001 单模型 (Llama)** 分析，1296 conditions = 3 prec × 3 temp × 6 prompts × 6 seeds × 4 orderings
- paper_framing 中标注为 "8-model Henderson I" 是**标注错误**——实际来源是 exp-001 单模型 D-study（259,200 records，6 facets）
- 8 模型 Henderson I 分析（exp-004）给出的是 G@116 = 0.834，G@200 = 0.896，n(G≥0.80) = 93

**如果 reviewer 要求的 "IRT items + multi-facet" 行用于 8 模型分析**，正确值是 G=0.834 而非 0.895。8 模型分析中 G=0.895 对应 n≈198（≈200 items）。

---
