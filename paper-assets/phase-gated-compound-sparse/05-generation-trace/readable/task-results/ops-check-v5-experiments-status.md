# ops check v5 experiments status

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-v5-experiments-status_20260514T022638_result.json`
- **Structured JSON:** [`93c5d50fcff516a75842.json`](../../sessions/93/93c5d50fcff516a75842.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部 **running**，均未完成（无 `profiling_results.json`）。

| 实验 | GPU | 显存占用 | GPU利用率 | 进度 | 状态 |
|------|-----|---------|----------|------|------|
| mvp_v5_fixed_s020_r2 | cuda:0 | 33509 MiB | 72% | **24/50** | running |
| mvp_v5_fixed_s030_r2 | cuda:1 | 33509 MiB | 76% | **24/50** | running |
| mvp_v5_random_s015 | cuda:2 | 23885 MiB | 74% | **15/50** | running |
| mvp_v5_random_s025 | cuda:3 | 23885 MiB | 79% | **15/50** | running |

importance masking (s020/s030) 两组进度一致，都在处理第 24 个问题；random masking (s015/s025) 两组也同步，在第 15 个。random 组显存更低（~24GB vs ~34GB），进度落后约 9 个问题，可能因为启动更晚或单题耗时不同。

所有实验日志中有 `Skipped 1 NaN attention layers: [27]` 的 warning，不影响运行。

---
