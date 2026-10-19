# ops restart seed2 lambda ent 0

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart-seed2-lambda-ent-0_20260516T030105_result.json`
- **Structured JSON:** [`a506b303e7954290a016.json`](../../sessions/a5/a506b303e7954290a016.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

- **Killed** PID 728887（旧 seed2，错误 lambda_ent=0.1）
- **清空** output dir
- **从 seed1 /proc/682233/cmdline 获取精确命令行**，确认 seed1 无 `--lambda_ent` 参数（即默认 0）
- **重启** seed2：PID 737600（python 732454），GPU 1 占用 16256 MiB，模型加载正常
- **Registry** 已更新重启原因和新 PID

---
