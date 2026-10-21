# ops gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_20260516T031312_result.json`
- **Structured JSON:** [`c9422c69738d3d295975.json`](../../sessions/c9/c9422c69738d3d295975.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== GPU STATUS ===
cuda:0: 空闲 - 0 MiB / 24564 MiB, 无进程
cuda:1: 占用 - 8985 MiB, PID 676497, evaluate.py Qwen2.5-3B_d000_s42 a32_aligned (运行 1h10m)
cuda:2: 占用 - 8985 MiB, PID 679190, evaluate.py Qwen2.5-3B_d005_s42 a32_aligned (运行 57m)
cuda:3: 占用 - 8985 MiB, PID 687347, evaluate.py Qwen2.5-3B_d100_a32_s42_v3 aligned (运行 8m)
cuda:4: 占用 - 7075 MiB, PID 668217, compute_signals Qwen2.5-3B_d025_s123 (运行 2h22m)
cuda:5: 占用 - 3537 MiB, PID 687036, compute_signals Qwen2.5-0.5B_d000_s123 (运行 8m)

=== AVAILABLE GPUs ===
cuda:0
```

**注意**：cuda:0 已确认空闲（0 MiB 显存占用，GPU 利用率 0%，无计算进程）。cuda:3 之前预期空闲，但实际正在跑 d100_a32_s42_v3 的 eval 任务。

**C006 提醒**：cuda:1 (d000_s42) 和 cuda:2 (d005_s42) 的 adapter 路径匹配黑名单目录名，但 output dir 含 `a32` 标识，可能是 alpha=32 重训版本。如需确认，可 `cat adapter_config.json | grep lora_alpha` 验证。

---
