# fix adaptive fix resubmit all3

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_adaptive_fix_resubmit_all3_20260514T174011_result.json`
- **Structured JSON:** [`5e10e23d9623178a789f.json`](../../sessions/5e/5e10e23d9623178a789f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

情况比预想的好很多：

## 状态总结

### 1. seed123 — 正常运行中
- **PID 109362**，cuda:2，已运行 3h17m
- 当前 step ~1728/6103 (28%)
- 命令中 **没有** `--overwrite_output_dir`，这是原始提交，从未被 kill
- Checkpoints: `checkpoint-500`, `checkpoint-1000`, `checkpoint-1500`

### 2. seed456 — 正常运行中
- **PID 115071**，cuda:3，已运行 2h24m
- 当前 step ~1489/6103 (24%)
- 命令中 **没有** `--overwrite_output_dir`，同样是原始提交
- Checkpoints: `checkpoint-500`, `checkpoint-1000`

### 3. seed42 — 已修复，刚重启
- **PID 123836**，cuda:1，刚启动 23 秒
- 命令正确：去掉了 `--overwrite_output_dir`，带了 `--resume_from_checkpoint output/models/adaptive_fix_seed42/checkpoint-1500`
- Checkpoints: `checkpoint-500`, `checkpoint-1000`, `checkpoint-1500`

### 结论

用户提到的 PID 123092/123238 是之前失败的重提交进程，已经死了。但 seed123 和 seed456 的**原始训练进程从未被 kill**，一直在正常跑。seed42 已被正确修复重提交，从 checkpoint-1500 恢复。

**三组都不需要额外操作。**

---
