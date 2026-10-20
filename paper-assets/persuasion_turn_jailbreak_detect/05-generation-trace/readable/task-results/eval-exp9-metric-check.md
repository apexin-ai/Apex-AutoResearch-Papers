# eval exp9 metric check

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp9-metric-check_20260518T174049_result.json`
- **Structured JSON:** [`a392f23761d098bccc2e.json`](../../sessions/a3/a392f23761d098bccc2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：exp9 bootstrap CI 使用的是 `f1_score(average="macro")`，无需修改。**

具体证据：
- 脚本 `scripts/exp9_bootstrap_ci.py` 中所有 `f1_score` 调用（共 8 处，行 265/275/301/305/318/358/364）均使用 `average="macro"`
- 结果 JSON 第 1147 行也标注了 `"metric": "f1_macro"`

---
