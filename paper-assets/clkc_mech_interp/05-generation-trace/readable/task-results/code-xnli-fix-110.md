# code xnli fix 110

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_xnli-fix-110_20260522T042258_result.json`
- **Structured JSON:** [`0bf68bbde34e30402a2c.json`](../../sessions/0b/0bf68bbde34e30402a2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**问题 1 (ZH 缺失)**: 不成立，4 个文件均已存在且非空。

**问题 2 (标签反转)**: 已修正 `src/prepare_xnli.py` 并重新生成数据。
- 修正前: entailment→"conflict", contradiction→"no_conflict"
- 修正后: entailment→"no_conflict", contradiction→"conflict"

**验证结果**:

| 文件 | 行数 | no_conflict | conflict |
|------|------|-------------|----------|
| en_xnli_train | 800 | 404 | 396 |
| en_xnli_test | 200 | 94 | 106 |
| zh_xnli_train | 800 | 387 | 413 |
| zh_xnli_test | 200 | 99 | 101 |

字段 `context`, `question`, `label` 与 collect_activations.py 兼容。报告已更新到 `artifacts/plan_110_xnli_baseline_report.md`。

---
