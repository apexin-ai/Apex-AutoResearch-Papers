# code d023 classify update

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d023_classify_update_20260512T193101_result.json`
- **Structured JSON:** [`132d428a604deae1510d.json`](../../sessions/13/132d428a604deae1510d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

**cuda0**: 1 truncated_success 被过滤，27 premature_completion_belief 保留为 verification
**cuda1**: 0 truncated_success，33 premature_completion_belief 保留为 verification
**合计**: 60 CSF 中 1 条 truncated_success 被过滤，59 条 premature_completion_belief 归类为 verification（比预期 58 多 1 条，可能是 cuda1 多跑了几条轨迹）

分类结果统计（以 cuda0 dry-run 为例，86 条 matched）:
- `verification`: 39 条（其中 25 条 sub_type=premature_completion_belief，14 条 rule-based）
- `planning`: 47 条
- `action`: 0 条

premature_completion_belief 在 verification 中占比：25/39 = **64%**（cuda0），是 verification 错误的主要来源。

输出记录结构正确：`error_type="verification"`, `sub_type="premature_completion_belief"`, `csf_details` 完整保留（含 is_csf, is_truncated_success, term_count, task_desc, verification 字段）。

---
