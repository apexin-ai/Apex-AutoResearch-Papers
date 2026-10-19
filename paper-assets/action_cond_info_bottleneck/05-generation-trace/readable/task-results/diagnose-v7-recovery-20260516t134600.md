# diagnose v7 recovery 20260516T134600

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v7_recovery_20260516T134600_20260516T134717_result.json`
- **Structured JSON:** [`326880a5c75a2dcdb221.json`](../../sessions/32/326880a5c75a2dcdb221.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练都已在运行，无需干预。

## 诊断结果

### 1. 崩溃原因
seed1 (PID 960110) 死于 **SIGHUP (EXIT_CODE=129)** — SSH 会话断开导致，非磁盘满或 OOM。

### 2. 当前状态 — 两个 seed 都在跑

| 实验 | PID | GPU | 当前 step | 状态 |
|------|-----|-----|-----------|------|
| v7_contrastive (seed1) | 21363 | cuda:0 | **~6600/20000** | 运行中，1.8 steps/s |
| v7_seed2 | 27427 | cuda:1 | **~200/20000** | 运行中，1.7 steps/s |

seed1 已被重启（PID 21357 通过 tmux + tee 方式启动，运行 ~1h03m），但**从 step 0 重跑**，未 resume checkpoint-5000。当前已过 6600 步，超过旧进程崩溃点，无实际损失。

### 3. 磁盘空间

| 分区 | 容量 | 已用 | 可用 |
|------|------|------|------|
| / (根) | 30G | 14G (46%) | 17G |
| /root/autodl-tmp (数据) | 250G | 75G (30%) | 176G |

空间充足，无需清理。

### 4. checkpoint 状态
- seed1: `checkpoint-5000` 存在（旧 run 的，1.3GB）
- seed2: 无 checkpoint（刚启动）

### 5. 注意事项
- seed1 重跑未 resume checkpoint，等于浪费了旧 checkpoint-5000。但当前进度已超过 5000，继续跑即可。
- 两个 GPU 利用率 98-99%，显存各占 ~16GB，正常。
- **无需任何操作**，两个训练都在健康运行。预计 seed1 还需 ~2h 完成 (13400 步 / 1.8 steps/s ≈ 7444s)，seed2 还需 ~3h。

---
