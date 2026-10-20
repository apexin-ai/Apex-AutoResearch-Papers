# code d146 revert span based rerun merge

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146_revert_span_based_rerun_merge_20260518T145639_result.json`
- **Structured JSON:** [`f6467c4497f29a65fc61.json`](../../sessions/f6/f6467c4497f29a65fc61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

执行完成。总结：

1. **evaluation.py 已恢复 span-based** — `entity_strict_match` 现在用 `(start, end, type)` 匹配
2. **conditional_decomp 自动继承** — 它 import 了 `entity_strict_match`，无需改动，已有 span-based 结果不需重跑
3. **entity merge 已重跑** — 三个数据集结果与 text-based 完全一致（delta = 0），因为 merge 脚本内部按 `(text, type)` 分组投票，同一句内 text+type 和 start+end+type 是一一映射的
4. **结果报告** 已写入 `artifacts/d146_span_revert/d146_entity_merge_span_results.md`

---
