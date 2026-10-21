# fix cqa1 timeout resubmit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1-timeout-resubmit_20260525T011711_result.json`
- **Structured JSON:** [`20f92d8ba95bd44992c6.json`](../../sessions/20/20f92d8ba95bd44992c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**已经全部处理完毕，无需操作。** 当前 cqa1-32758 状态：

| GPU | Session | Seed | Timeout | 启动时间 | 状态 |
|-----|---------|------|---------|----------|------|
| 0 | eval-k10-tau025-spatial-s45 | 45 | 18000s | 09:20 | 运行中 |
| 1 | eval-k10-tau025-spatial-s47 | 47 | 18000s | 09:20 | 运行中 |
| 2 | eval-canonical-adaptive-k10-spatial-s42 | 42 | 18000s | 09:20 | 运行中 |
| 3-4 | 空闲 | - | - | - | - |
| 5 | eval-long-vla-only-s48 | 48 | - | 03:40 | 运行中 (VLA-only baseline) |

s45/s47 和 s42 canonical 已在今天 09:20 以 `timeout 18000` 重提交，正在正常运行。Registry 中三个实验都已更新为 RUNNING + timeout=18000s。cqa1 上恰好 3 个 spatial eval，符合上限要求。

另外 5 个 canonical 实验（s43/s44/s48/s49）已分散到 bjb2-28827 和 bjb1-32546 运行，也都是 timeout=18000s。

有一个残留的 tmux 服务进程 `eval-spatial-vla-only-s42`（PID 76490），但它不在 `tmux ls` 中出现，只是个僵尸进程，不占 GPU。要清理吗？

---
