# ops verify seed44 r2 alive

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-seed44-r2-alive_20260516T013520_result.json`
- **Structured JSON:** [`ead5df4269d4db05f04c.json`](../../sessions/ea/ead5df4269d4db05f04c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部 **ALIVE**：

### bjb1-18228

| 实验 | PID | GPU | 显存占用 | 状态 |
|------|-----|-----|---------|------|
| eval-argmin-object-seed44-r2 | 428117 | cuda:3 | 11252 MiB / 24564 MiB | **ALIVE** |
| eval-obs-only-object-norm02-seed44-r2 | 428406 | cuda:2 | 11324 MiB / 24564 MiB | **ALIVE** |

### bjb2-40593

| 实验 | PID | GPU | 显存占用 | 状态 |
|------|-----|-----|---------|------|
| eval-vla-only-object-seed44-r2 | 286989 | cuda:0 | 11180 MiB / 24564 MiB | **ALIVE** |

三个进程都有 ~11GB 显存占用，说明模型已加载并在正常运行。（tmux ls 被 read_only 白名单拦截，但进程和显存状态已足够确认。）

---
