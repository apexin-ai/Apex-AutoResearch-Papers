# fix kill rogue crm cuda5

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-rogue-crm-cuda5_20260522T175045_result.json`
- **Structured JSON:** [`f450040de4497c68c32e.json`](../../sessions/f4/f450040de4497c68c32e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**Kill 结果：** PID 497801 和 498068 已终止。

**自动重启检查：**
- tmux 中只有 `train-crm-unified-4suite-r4` session（cuda:3 的正确训练，PID 322367），无其他 CRM 相关 session
- crontab、systemd、screen 均无 CRM 相关条目
- 不存在自动重启机制

**GPU 状态：**
| GPU | 显存占用 |
|-----|---------|
| 0 | 4 MiB (空闲) |
| 1 | 1 MiB (空闲) |
| 2 | 1 MiB (空闲) |
| 3 | 542 MiB (CRM r4 训练中) |
| 4 | 1 MiB (空闲) |
| 5 | **1 MiB (已释放)** |

cuda:5 已完全释放，cuda:3 的 r4 训练未受影响。

---
