# ops 10894 gpu check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_10894-gpu-check_20260526T165437_result.json`
- **Structured JSON:** [`70e78e462f02dc7b352a.json`](../../sessions/70/70e78e462f02dc7b352a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 状态 (westd-10894):**

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| cuda:0 | 62194 / 97887 MiB | 42% | **占用** (PID 170698) |
| cuda:1 | 63028 / 97887 MiB | 59% | **占用** (PID 341771) |
| cuda:2 | 62194 / 97887 MiB | 99% | **占用** (PID 341987) |
| cuda:3 | 62194 / 97887 MiB | 99% | **占用** (PID 342341) |

**4 张卡全部在用**，均运行 `occsafe` conda 环境的 python 进程。无空闲 GPU。

**Checkpoint 情况:**
- `vanilla_retrain_s0/` — 目录不存在
- `mvp_occ_s3_v2/` — 有 `40000_chkpt` 和 `50000_chkpt`，可用

`tmux ls` 被 read_only 拦截，无法查看。

---
