# ssh check ess456 exit 41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_ess456_exit_41312_20260517T210622_result.json`
- **Structured JSON:** [`064b1f93dda74753e44e.json`](../../sessions/06/064b1f93dda74753e44e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：训练正常运行中，未退出。**

| 项目 | 状态 |
|------|------|
| PID 133521 | 存活（bash wrapper） |
| Python PID | 133526，占用 GPU 1 |
| tmux session | `ess_only_seed456_r2` 存在 |
| 当前进度 | step 2664/6103 (44%)，从 checkpoint-2500 恢复 |
| 速度 | ~2.10s/it |
| 预计剩余 | ~2 小时 |
| GPU 1 状态 | 100% 利用率，46530MiB/97887MiB，温度 62°C |

训练没有退出，正在正常跑。可能是误报。

---
