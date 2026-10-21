# code plan 004 oom rerun

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-004-oom-rerun_20260515T003650_result.json`
- **Structured JSON:** [`88b05997964824853613.json`](../../sessions/88/88b05997964824853613.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并稳定运行。

**汇总：**
- **PID**: 142680（实际 python 进程）
- **GPU**: cuda:2，占用 16048MiB / 32607MiB（49%），无 OOM 风险
- **参数**: `--batch-size 2 --grad-accum 8`（effective batch size = 16，与原始一致）
- **进度**: 38/741 steps，速度 ~1.50 it/s
- **预计完成时间**: 741 steps ÷ 1.50 it/s ≈ 494 秒 ≈ **~8 分钟**（加上 3 次 eval 约 2 分钟），总计约 **10 分钟**，预计 08:49 左右完成
- **日志**: `/tmp/plan004_oom_rerun.log`

另外注意：GPU 3 的主批次已结束（0MiB），GPU 1 的主批次之前因 `/tmp` 目录问题崩了（不是 OOM）。

---
