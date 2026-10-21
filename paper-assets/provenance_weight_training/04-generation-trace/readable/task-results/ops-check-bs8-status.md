# ops check bs8 status

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_bs8_status_20260515T220627_result.json`
- **Structured JSON:** [`c6f45385afc2792e4529.json`](../../sessions/c6/c6f45385afc2792e4529.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**bs8_nmin2_seed42_r2 状态：正在训练**

| 指标 | 值 |
|------|-----|
| 进程 | PID 238714，存活 |
| GPU 2 | 81705/97887 MiB，利用率 100% |
| 进度 | **4957/6103 步 (81.2%)** |
| 已用时间 | 3h17m |
| 速度 | ~2.38 s/step |
| 预计剩余 | **~46 分钟** |
| 近期 loss | 5.05–5.69 区间波动，均值约 5.33 |
| Learning rate | ~1.0e-5（cosine decay 阶段） |
| Epoch | 0.21 |

训练正常推进，无异常。预计约 46 分钟后完成（约 UTC 时间再过 46min）。完成后需跑 eval。

---
