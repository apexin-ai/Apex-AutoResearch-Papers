# status westd 45947 check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_westd-45947-check_20260521T181644_result.json`
- **Structured JSON:** [`9f0fc1aad615b9fc95e1.json`](../../sessions/9f/9f0fc1aad615b9fc95e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-45947 状态汇报

### A3 spatial_bowl (cuda:0, PID 191747)
- **状态**: ALIVE, 已运行 1h 04m 51s
- **当前 step**: 6939/30000 (23%)
- **速度**: ~4.05s/step
- **Loss**: ~0.07, lr=2.28e-05
- **预估剩余时间**: (30000 - 6939) × 4.05s ≈ **25.9h**
- **日志文件**: `/tmp/a3_spatial_bowl.log`（从 step 6000 checkpoint 恢复）

### cuda:1
- 完全空闲：0 MiB 显存，0% 利用率
- 无任何进程

### 异常
- `train_resume3.log` 显示之前一次尝试因 **SyntaxError** 崩溃（`train_a3_hook.py` line 243 有乱码）
- `/tmp/spatial_bowl.log` 显示一次从 step 0 开始的 fresh run 跑了 8h 到 step 7894 后死亡。当前 run 从 step 6000 checkpoint 恢复，**丢失了 ~1894 steps 的进度**（可能 checkpoint 只存在 step 6000）

---
