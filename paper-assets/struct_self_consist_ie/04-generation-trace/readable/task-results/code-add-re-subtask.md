# code add re subtask

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_add_re_subtask_20260514T050825_result.json`
- **Structured JSON:** [`a75802656eceea60b142.json`](../../sessions/a7/a75802656eceea60b142.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。4 个文件的 RE subtask 支持已添加并验证通过：

- **consistency.py**: 新增 `_re_soft_jaccard_pair()`（Hungarian matching，similarity = head_sj × tail_sj × type_match），`structural_consistency_soft_jaccard()` 支持 `subtask="re"`
- **evaluation.py**: 新增 `relation_strict_match()` + `compute_re_f1()`，`per_instance_f1()` 和 `generate_evaluation_report()` 均支持 `subtask="re"`
- **sampling.py**: 新增 `_RE_TEMPLATE`，`build_uie_prompt()` 支持 `subtask="re"`
- **run_mvp_pilot.py**: `--subtask` choices 扩展为 `["ner", "re", "eae"]`，step 4 evaluation 用 dispatch dict 统一处理，import 新增 `compute_re_f1`

---
