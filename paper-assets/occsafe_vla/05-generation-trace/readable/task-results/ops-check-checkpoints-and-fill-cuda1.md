# ops check checkpoints and fill cuda1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_checkpoints_and_fill_cuda1_20260525T014326_result.json`
- **Structured JSON:** [`105cc86fb0d0ea2952c0.json`](../../sessions/10/105cc86fb0d0ea2952c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 1. Checkpoint 可用性

| 条件 | 50K checkpoint | 状态 |
|---|---|---|
| **full_occ_ln_s0** | `/root/autodl-tmp/checkpoints/full_occ_ln_s0/...--50000_chkpt` | ✅ 存在，15GB |
| **vanilla_s0** | — | ❌ 服务器上无任何 vanilla checkpoint 目录 |
| **vanilla_retrain_s0** | — | ❌ 同上 |
| **full_occ_s0** | — | ❌ 不存在（只有 full_occ_**ln**_s0/s1/s2） |
| **mvp_occ_s0** | — | ❌ 不存在 |
| **ablation_occ_detach_s0_retrain** | — | ❌ 训练已崩溃，最高 40K checkpoint |

### 2. ablation_occ_detach_s0_retrain 进度

- **已崩溃**，exit code 1，时间 2026-05-25 01:44:40
- 日志中最后一次 "Saving Model Checkpoint" 在 step 30000
- 40K checkpoint 存在（15GB，创建时间 07:37，可能来自静默重启），但无 50K
- 崩溃原因不明（traceback 未启用），需查 `TORCHELASTIC_ERROR_FILE`

### 3. GPU 状态

| GPU | 利用率 | VRAM | 状态 |
|---|---|---|---|
| 0 | 99% | 62GB/98GB | full_occ_ln_s1_resume 或 s2_resume |
| **1** | **0%** | **0/98GB** | **空闲** |
| 2 | 99% | 62GB/98GB | full_occ_ln_s1_resume 或 s2_resume |
| 3 | 99% | 62GB/98GB | 第三个训练进程（3个PID但只有2个活跃 resume log） |

活跃训练：
- **full_occ_ln_s1_resume**: step 27637/50005 (55%)，剩余 ~5h46m
- **full_occ_ln_s2_resume**: step 27656/50005 (55%)，剩余 ~5h47m

### 4. 建议

**无法直接跑 same-seed 梯度分析**。4 个条件中只有 **full_occ_ln_s0** 的 50K checkpoint 在本地，其余 3 个（vanilla_s0、full_occ_s0/mvp_occ_s0、ablation_occ_detach_s0_retrain）均不可用。

可选方案：
- **A**: 从其他服务器 scp vanilla_s0 和 full_occ_s0（或 mvp_occ_s0）的 50K checkpoint 过来，同时在 cuda:1 上恢复 ablation_occ_detach_s0_retrain 从 40K 继续跑到 50K
- **B**: 改用 cuda:1 跑其他不依赖缺失 checkpoint 的任务（如 full_occ_ln_s0 的梯度分析单模型 debug、eval 等）
- **C**: 先在 cuda:1 上重启 ablation_occ_detach_s0_retrain（从 40K resume），等 50K 出来后再安排梯度分析

---
