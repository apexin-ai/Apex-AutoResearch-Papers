# submit 30476 remaining 3exp

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_30476_remaining_3exp_20260517T134159_result.json`
- **Structured JSON:** [`039d3f6186b50ffa1806.json`](../../sessions/03/039d3f6186b50ffa1806.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。4 个实验均在运行：

| exp_id | GPU | PID | 显存 |
|---|---|---|---|
| random_reweight_seed123_r5 | cuda:0 | 20073 | 46505 MiB, 99% |
| bs8_auto_nmin_r5 | cuda:1 | 22466 | 81687 MiB, 100% |
| batch_adaptive_tau_rho06_r5 | cuda:2 | 22904 | 1825 MiB (加载中) |
| rho02_adaptive_tau09_r5 | cuda:3 | 22095 | 46505 MiB, 94% |

内存：93Gi / 1.0Ti used (898Gi available)，充裕。cuda:2 刚启动还在加载模型，其余 3 卡已进入训练。4 个 tmux session 全部确认存在。

---
