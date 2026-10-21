# check d134 status quick

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d134-status-quick_20260518T121711_result.json`
- **Structured JSON:** [`59125e5937cfe44de8ff.json`](../../sessions/59/59125e5937cfe44de8ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D134 pipeline 状态：

| 项目 | 状态 |
|---|---|
| **s48 训练** | step 199/500 (40%), ~25min elapsed, ETA ~18min. reward=1.075, prove_rate=1.0, ISR=0.75, loss=0.0, grad_norm=0.0 |
| **tmux** | read-only 模式无法执行 tmux ls |
| **GPU** | 7% util, 84465/97887 MiB used (~86%) |
| **磁盘** | 223G/250G used (89%), 28G avail |
| **cleaner log** | 不存在 |

注意事项：
- **loss=0.0, grad_norm=0.0** 已持续多步，entropy 极低 (0.01-0.05)，模型可能已 collapse（reward_std=0, frac_reward_zero_std=1.0）。
- **磁盘 89%**，剩余 28G，考虑到 C003 约束需关注后续 checkpoint 保存空间。

---
