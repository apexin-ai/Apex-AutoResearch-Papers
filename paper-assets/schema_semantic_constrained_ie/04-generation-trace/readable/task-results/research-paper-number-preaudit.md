# research paper number preaudit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-number-preaudit_20260516T023810_result.json`
- **Structured JSON:** [`94eb4b712e41cf4d16f4.json`](../../sessions/94/94eb4b712e41cf4d16f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。**53 个数字全部与 registry 一致，零不匹配。**

分布：
- **Table 5**: 32/32 cells (2 models × 4 rows × 4 metrics)
- **Body text**: 13/13 claims (F1 lift、DR reduction、delta pp 等)
- **Limitations**: 8/8 claims (DocRED CF/E-F1 delta、parse fail rate 等)

两点备注：
1. `llama_scierc_unconstrained` 的 CF 只存了原始计数 (6) 没存 rate，需手算 6/2451≈0.24% 才能对上论文值
2. 任务指定的 3 个实验名与 registry 实际名称不同（`phase1_scierc` → `phase2_scierc_unconstrained` 等），已在报告中列出映射表

结论：**可以安全地在此基础上添加 DocRED FT composability 数据。**

---
