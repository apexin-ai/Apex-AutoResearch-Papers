# fix cuda1 force start external seed123

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cuda1_force_start_external_seed123_20260514T031500_result.json`
- **Structured JSON:** [`9b12a2bb42e1bc4964f0.json`](../../sessions/9b/9b12a2bb42e1bc4964f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果确认：cuda:1 上的 medium_external_seed123 正在正常运行。**

| 项目 | 状态 |
|------|------|
| PID | 405067 (125% CPU, 运行中) |
| GPU | cuda:1, 61% 利用率, 19252 MiB 显存占用 |
| tmux session | `medium_external_seed123` (创建于 11:11:15) |
| 启动时间 | Thu May 14 11:11:15 CST 2026 |

日志目前只有启动信息和一个无害的 deprecation warning (`torch_dtype` → `dtype`)，说明进程刚启动不久，正在初始化/运行中，还没产出训练进度输出。

另外 cuda:0 上也有进程在跑（PID 391599, 22460 MiB，应该是 `chain_cuda0_s123` tmux session）。

**无需重新启动，进程已在正常工作。**

---
