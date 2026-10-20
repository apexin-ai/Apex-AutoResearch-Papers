# check exp freeform seed456 completion

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_freeform_seed456_completion_20260515T183725_result.json`
- **Structured JSON:** [`abfc70561251144a07bf.json`](../../sessions/ab/abfc70561251144a07bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**exp_freeform_seed456: SUCCESS → DONE**

核心结论 — seed456 与 seed42 高度一致，假设验证通过：

- **RE LP flip 确认**: freeform RE gap = +0.0141 (seed42: +0.0169)，constrained RE gap = -0.0068，free-form 稳定翻转为正
- **NER gap 稳定**: freeform NER gap = +0.0016 (seed42: +0.0018)，几乎无差异
- **LP variance 完全一致**: std=0.0199, range=0.0599，两个 seed 数值相同
- **Tied% 相同**: 57.7% (freeform), 59.7% (constrained)
- **Parse rate**: 99.95% (4406/4408)

Registry 已更新为 DONE/success，含完整指标。无 cron 需要清除。

---
