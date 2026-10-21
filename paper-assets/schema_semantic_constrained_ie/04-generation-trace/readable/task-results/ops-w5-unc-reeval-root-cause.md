# ops w5 unc reeval root cause

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_w5_unc_reeval_root_cause_20260520T142659_result.json`
- **Structured JSON:** [`9ee1f9ccc46c1105581a.json`](../../sessions/9e/9ee1f9ccc46c1105581a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个都跑完了。结果汇总：

## 重评结果对比

### Llama DocRED Unconstrained

| Source | Eval Script | E-F1 | R-F1 | DR% | CF% |
|--------|------------|------|------|-----|-----|
| w5 Llama unc | w5 原始 eval | 83.93 | 43.72 | 0.49 | 0.08 |
| w5 Llama unc | eval_d064.py (重评) | **83.93** | **43.72** | **0.49** | **0.08** |
| d065 Llama unc | eval_d064.py | 84.77 | 44.55 | 0.49 | 0.08 |

### Qwen DocRED Unconstrained

| Source | Eval Script | E-F1 | R-F1 | DR% | CF% |
|--------|------------|------|------|-----|-----|
| w5 Qwen unc | eval_d064.py (重评) | **82.15** | **40.86** | 0.76 | 0.09 |

## 根因判断

**w5 重评 F1 完全等于 w5 原始值**（E-F1=83.93, R-F1=43.72, DR%/CF% 完全一致），而非 d065 值。

**结论：F1 差异来自推理代码（max_new_tokens 等），不是 eval 脚本差异。** eval_d064.py 和 w5 原始 eval 对同一文件产出完全相同的结果，排除了 eval 脚本差异的可能。d065 Llama unc 比 w5 高 +0.84pp E-F1 / +0.83pp R-F1，原因在于 d065 推理时使用了不同的 max_new_tokens 或其他推理参数。

---
