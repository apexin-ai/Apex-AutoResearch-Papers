# monitor training progress 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-10894_20260527T022014_result.json`
- **Structured JSON:** [`91715471275787f8368b.json`](../../sessions/91/91715471275787f8368b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 processes alive. Summary:

| exp_id | PID | 存活 | 当前 step | max_steps | 进度% | 最新 loss (occ/action) | 速度 | 剩余时间 |
|--------|-----|------|----------|-----------|-------|----------------------|------|---------|
| full_occ_ln_v2_s1c | 481426 | ✓ | 6241 | 50005 | 12.5% | 0.0081 / 0.1523 | ~1.08 it/s | ~11.3h |
| full_occ_ln_v2_s2 | 481643 | ✓ | 6242 | 50005 | 12.5% | 0.0109 / 0.1279 | ~1.08 it/s | ~11.3h |
| detach_ln_v2_s0c | 481988 | ✓ | 6214 | 50005 | 12.4% | 0.0111 / 0.1108 | ~1.07 it/s | ~11.4h |
| full_occ_ln_v2_s0d | 490803 | ✓ | 3703 | 50005 | 7.4% | 0.0138 / 0.1904 | ~1.07 it/s | ~12.0h |

**GPU 利用率:**

| GPU | 利用率 | 显存占用 |
|-----|--------|---------|
| cuda:0 | 98% | 62203 / 97887 MiB |
| cuda:1 | 46% | 62203 / 97887 MiB |
| cuda:2 | 99% | 62209 / 97887 MiB |
| cuda:3 | 63% | 62203 / 97887 MiB |

**异常:**
- PID 490803 (full_occ_ln_v2_s0d) 的 `ps` 显示 CPU=0.0%, MEM=0.0%，但 GPU 3 有 63% 利用率且日志仍在推进 step 3703，训练实际在跑。可能是 ps 采样瞬间主进程在等 GPU 返回。
- full_occ_ln_v2_s0d 比其他 3 个实验晚启动约 40 分钟，进度落后约 2500 步。

**DDL 评估:** 4 个实验预计再跑 11-12 小时。距 DDL (2026-05-28 12:00 UTC) 约 18h+，时间充裕。全部实验预计在 DDL 前 6-7 小时完成。

---
