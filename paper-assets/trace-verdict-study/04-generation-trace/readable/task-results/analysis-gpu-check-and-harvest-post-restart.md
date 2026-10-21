# analysis gpu check and harvest post restart

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpu_check_and_harvest_post_restart_20260518T163045_result.json`
- **Structured JSON:** [`526c2e016c2d72aeeb0a.json`](../../sessions/52/526c2e016c2d72aeeb0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU STATUS:
- cuda:0: [存活] qwen7b_full_trace_tail512_seed123 (PID 452121, 87065MiB, 100% util)
- cuda:1: [存活] deepseek_full_trace_tail512_seed456 (PID 452263, 80221MiB, 85% util)
- tmux sessions: 两个都在 (创建于 00:29，仅 2 分钟前)

RESULTS:
- deepseek_full_trace_tail512_seed123: ❌ FAILED — CUDA OOM at step 0/444
  退出码 1，时间 2026-05-18T15:49:48Z
  无 checkpoint，无 eval_results.json
  原因: deepseek-6.7b 未加 --gradient_checkpointing 导致显存不足

- qwen15b_full_trace_tail512_seed456: ✅ accuracy=96.72% (confirmed)
  CI: [95.63%, 97.73%], lift=25.21%, n=1190
  pass_f1=0.9771, fail_f1=0.9424
```

注意事项：
1. 两个当前实验刚刚启动（00:29），说明重启后被重新拉起，不是重启前幸存的进程
2. `deepseek_full_trace_tail512_seed123` 需要重跑，加 `--gradient_checkpointing`（符合 C002 约束）。是否现在安排重跑？

---
