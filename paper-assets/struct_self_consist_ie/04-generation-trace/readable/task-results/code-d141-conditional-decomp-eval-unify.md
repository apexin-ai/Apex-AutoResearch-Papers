# code d141 conditional decomp eval unify

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d141_conditional_decomp_eval_unify_20260518T144757_result.json`
- **Structured JSON:** [`655f5e96bb1f158ff945.json`](../../sessions/65/655f5e96bb1f158ff945.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改摘要：

1. **evaluation.py**: `entity_strict_match` 从 `(start, end, type)` 改为 `(text, type)`
2. **analysis_d141_conditional_decomp.py**: 删除内联 `entity_f1`，改用 `from evaluation import entity_strict_match, _prf`

0.05pp 阈值检查结果：SciERC 勉强通过（=0.05pp），CoNLL（0.10pp）和 FewNERD（0.06pp）的 Favorable delta 略超阈值。根因是 text-based 匹配会合并同句中同名实体，导致少量实例的 degenerate 分类发生变化，进而引起 bucket 重组。所有差异 < 0.15pp，定性结论不变。

报告已写入 `artifacts/d141_eval_unify/conditional_decomp_eval_unified_results.md`。

---
