# diagnose m128 seed44 cron exit

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_m128_seed44_cron_exit_20260519T045255_result.json`
- **Structured JSON:** [`1754e9c1e32b6758959c.json`](../../sessions/17/1754e9c1e32b6758959c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**误报。** 进程正常运行中。

- PID 459645 存活，CPU 95%+
- 正确日志文件是 `smart_compress_m128_seed44.log`（任务给的两个路径都不对）
- 当前 step: **20000/100000**，刚完成 eval（action_loss=0.1060）并保存 checkpoint
- 速度 5.2 sps，loss 正常下降，无异常
- `train_m128_seed44.log` 是一个旧实验（12:48 被 SIGTERM 终止于 step 6071），与当前训练无关

不需要任何 registry 更新或 cron 删除。预计剩余 ~15400 步 / 5.2 sps ≈ 4.3 小时完成。

---
