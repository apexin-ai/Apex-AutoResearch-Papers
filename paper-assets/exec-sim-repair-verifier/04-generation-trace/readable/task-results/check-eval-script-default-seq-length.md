# check eval script default seq length

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-script-default-seq-length_20260514T210759_result.json`
- **Structured JSON:** [`f8c33891aa96d615916f.json`](../../sessions/f8/f8c33891aa96d615916f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**`max_seq_length` 默认值是 `2048`**（第 257 行：`default=2048`）

**需要重跑。** PID 289073 的命令行确认没有传 `--max_seq_length`，所以用的是默认值 2048，不是 8192，与其他 val sweep 不可比。

**PID 289073 当前状态：** 正在运行，已跑 3 分 43 秒，在 cuda:0 上（不是 cuda:1），checkpoint-3000，split=val。由于刚跑不久，建议尽快 kill 并加上 `--max_seq_length 8192` 重跑。

---
