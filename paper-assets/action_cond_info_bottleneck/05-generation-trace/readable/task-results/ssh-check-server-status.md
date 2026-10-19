# ssh check server status

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-server-status_20260517T014933_result.json`
- **Structured JSON:** [`28b8de6b726fa80042b5.json`](../../sessions/28/28b8de6b726fa80042b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
[GPU 状态]
cuda:0: 占用 — PID 111920, seed2 eval (libero_10 进行中)
cuda:1: 占用 — PID 751592, alpha=0.1 sweep (libero_spatial)

[seed2 eval]
状态: 运行中（正在跑 libero_10，最后一个 suite）
已完成结果:
  libero_spatial SR: 257/500 = 51.4%
  libero_object SR:  247/500 = 49.4%
  libero_goal SR:    315/500 = 63.0%
  libero_10 SR:      N/A（进行中）

[alpha=0.1 sweep]
状态: 运行中
tmux session: alpha_sweep_0_1
进度: libero_spatial 早期 episode，running_success_rate=0.0%
注意: run_info.json 显示只跑 libero_spatial 一个 suite（非全部 4 个）
已有结果: 无（eval_info.json 尚未生成）

[alpha=0.0 sweep]
状态: 未启动
目录不存在

[行动]
未启动 alpha=0.0 — cuda:0 被 seed2 eval (PID 111920) 占用，违反 C003。
需等 seed2 eval 完成 libero_10 后 cuda:0 释放才能启动。
```

---
