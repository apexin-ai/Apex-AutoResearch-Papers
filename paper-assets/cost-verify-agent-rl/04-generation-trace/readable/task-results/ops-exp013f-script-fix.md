# ops exp013f script fix

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp013f-script-fix_20260514T092756_result.json`
- **Structured JSON:** [`cfa2ee92c838a1c83b80.json`](../../sessions/cf/cfa2ee92c838a1c83b80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。训练命令前后已加上 `set +e` / `set -e`，`python train.py` 崩溃时 shell 不会立即退出，Ray log 备份代码会正常执行，最终通过 `exit $EXIT_CODE` 传递原始退出码。

---
