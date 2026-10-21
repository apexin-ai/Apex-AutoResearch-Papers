# eval unified scierc w5

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_unified-scierc-w5_20260520T083447_result.json`
- **Structured JSON:** [`89a0323a639898323f8d.json`](../../sessions/89/89a0323a639898323f8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

| Model | Mode | E-F1 | R-F1 | DR% | CF% | ET% | RV% | PF% |
|-------|------|------|------|-----|-----|-----|-----|-----|
| Qwen | unc | 67.05 | 43.86 | 1.95 | 0.00 | 0.00 | 0.00 | 0.0 |
| Qwen | con | 67.05 | 43.77 | 0.00 | 0.45 | 0.00 | 0.00 | 0.0 |
| Llama | unc | 67.76 | 45.45 | 1.11 | 0.00 | 0.00 | 0.00 | 0.0 |
| Llama | con | 67.76 | 45.47 | 0.09 | 0.23 | 0.00 | 0.00 | 0.0 |
| Qwen | con+cfcorr | 67.00 | 43.77 | 0.71 | 0.00 | 0.00 | 0.00 | 0.0 |
| Llama | con+cfcorr | 67.82 | 45.47 | 0.37 | 0.00 | 0.00 | 0.00 | 0.0 |

**关键说明**：eval_d064.py 硬编码 DocRED ontology，无法直接跑 SciERC。实际使用了 eval_d066_unified.py——同一套 PF-as-FN 逻辑，仅将 ontology 参数化。所有 6 个 w5 文件 PF%=0，PF-as-FN 处理对本批结果无数值影响。结果已写入 `artifacts/d065/unified_eval/scierc_unified_eval.md` 并注册。

---
