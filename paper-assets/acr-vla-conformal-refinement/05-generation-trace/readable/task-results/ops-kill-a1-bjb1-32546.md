# ops kill a1 bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-a1-bjb1-32546_20260524T201007_result.json`
- **Structured JSON:** [`9a2db7ca52e92ad4ca65.json`](../../sessions/9a/9a2db7ca52e92ad4ca65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done.

## Kill 结果
- A1 进程已自行终止（PID 462251 不存在，无 tmux 会话）—— 无需手动 kill
- Registry: `eval-a1-baseline-object-s42` → `DONE`, conclusion=`killed`, notes 记录 D137 决定

## bjb1-32546 GPU 全貌
所有 6 张 RTX 4090 **全部空闲**（0% util，1 MiB used）：

| GPU | 进程 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | 无 | 0% | 1 MiB / 24564 MiB |
| 1 | 无 | 0% | 1 MiB / 24564 MiB |
| 2 | 无 | 0% | 1 MiB / 24564 MiB |
| 3 | 无 | 0% | 1 MiB / 24564 MiB |
| 4 | 无 | 0% | 1 MiB / 24564 MiB |
| 5 | 无 | 0% | 1 MiB / 24564 MiB |

**注**：Registry 中 `bjb1-32546` 上还有 3 个标 RUNNING 但实际已不在的实验（孤儿记录）：
- `eval-supp-spatial-k2mean-s46` (PID 188432，gpu:0)
- `eval-supp-reconvla-obj-s45` (gpu:5)
- `eval-smolvla-lerobot-{goal,spatial}-seed43-v3`

整机 6 卡全空，可立即调度新任务。

---
