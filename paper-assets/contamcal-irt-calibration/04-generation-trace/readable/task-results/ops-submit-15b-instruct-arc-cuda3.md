# ops submit 15B instruct arc cuda3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_15B_instruct_arc_cuda3_20260516T211845_result.json`
- **Structured JSON:** [`6426bec92d00da791654.json`](../../sessions/64/6426bec92d00da791654.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **GPU 3** 确认空闲，无冲突进程
- **模型路径**: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct`
- **进程启动**: PID 870622，tmux session `exp002_15B_instruct_arc_v2`
- **Registry**: 已更新为 RUNNING
- **日志**: `/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/run_arc_v2.log`

与 v1 的区别：模型路径从 `/root/autodl-tmp/models/Qwen2.5-1.5B-Instruct` 改为 `.hf_cache` 中的实际模型文件，batch-size 从 8 降为 4，GPU 从 cuda:2 改为 cuda:3。

---
