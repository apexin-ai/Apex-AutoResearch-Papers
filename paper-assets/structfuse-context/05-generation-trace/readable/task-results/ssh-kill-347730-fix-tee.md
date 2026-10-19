# ssh kill 347730 fix tee

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_347730_fix_tee_20260513T214625_result.json`
- **Structured JSON:** [`fd3c865bbc8f22475d3f.json`](../../sessions/fd/fd3c865bbc8f22475d3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### Task 1: Kill PID 347730
- **PID 347730**: 已成功 kill（ps 查不到进程，确认已终止）
- **PID 76627**: 正常运行中，已运行 3h17m13s，StarCoder random_s42 训练

### Task 2: 修复 tee 冲突
- **脚本中不存在 `tee`**。`grep -n "tee" run_m2_full_qwen.sh` 无匹配。
- 当前脚本的训练命令使用的是 `> "${LOG_FILE}" 2>&1` 直接重定向，不是 `2>&1 | tee`。
- **无需修改**，脚本已经是正确的重定向方式。如果 wrapper 的日志只有 3 行，问题可能在别处（比如 wrapper 的重定向与脚本自身的 `> ${LOG_FILE}` 重复——训练输出全进了脚本自己的 `${LOG_DIR}/${TAG}.log`，wrapper 的 log 只捕获到了 echo 行）。需要的话可以进一步排查。

---
