# ssh check v71 step10k probe

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-v71-step10k-probe_20260517T083140_result.json`
- **Structured JSON:** [`566a8a727bfe3b1e5711.json`](../../sessions/56/566a8a727bfe3b1e5711.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在有完整的信息了。

## 结果

### 训练状态

| | Seed 1 (PID 3619) | Seed 2 (PID 3693) |
|---|---|---|
| GPU | GPU 0, 14996 MiB | GPU 1, 14996 MiB |
| 运行时间 | 1h 45m | 1h 45m |
| checkpoint-5000 | 15:33 | 15:34 |
| checkpoint-10000 | 16:20 | 16:20 |

### 进度推算

- 5000 步耗时 ~47 min（从 ckpt-5000 到 ckpt-10000 的间隔）
- 训练启动: 14:47，当前运行 1h45m → 当前约 16:32
- checkpoint-10000 写入于 16:20，距今 ~12 min → **估计当前 step ~11,300**
- 下一个 checkpoint (15000) 预计 ~17:07
- **训练完成 (20000 步) 预计 ~17:54**（约 1h22m 后）

### Checkpoint 状态

- `checkpoint-10000` 两个 seed **均已存在**（注意命名为 `checkpoint-10000` 而非 `checkpoint_step_10000`）

### Probe A

**不能运行。** 两个 seed 训练进程仍在跑，GPU 0 和 GPU 1 各占 ~15GB。在任一 GPU 上启动 Probe A 会 OOM。需等训练结束后再跑。

### 建议的下一步时间点

训练预计 17:54 (UTC+8) 完成。完成后两个 GPU 都会释放，届时可以安全跑 Probe A。

---
