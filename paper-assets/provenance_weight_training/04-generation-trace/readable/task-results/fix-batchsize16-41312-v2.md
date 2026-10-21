# fix batchsize16 41312 v2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_batchsize16_41312_v2_20260517T005809_result.json`
- **Structured JSON:** [`f4ec0252081972bdecb7.json`](../../sessions/f4/f4ec0252081972bdecb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

- **训练启动成功**：westd-41312 cuda:2，PID 50284，显存 90190MiB，GPU 利用率 100%
- **tmux session**：`batchsize16_nmin8_seed42` 运行中
- **Registry 已更新**：server=westd-41312, gpu=cuda:2, pid=50284
- **westd-47453 错误轮询进程已清除**（kill 375555）

注意事项：实际使用的脚本是 `run_batchsize16.sh`（包含 `--gradient_checkpointing`），而非 `run_batchsize16_nmin8_seed42.sh`（缺少该标志导致 OOM）。两者训练参数完全相同。

---
