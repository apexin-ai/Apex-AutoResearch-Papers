# ops check eval and training progress

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_eval_and_training_progress_20260521T233728_result.json`
- **Structured JSON:** [`4b8caee9802e3c10285a.json`](../../sessions/4b/4b8caee9802e3c10285a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### 1. Eval (westd-45947, cuda:1) — PID 263983 存活，运行 2h45m

**当前进度：refine 组，Task 2 (pick up milk)，Episode 10/50**

| Task | 名称 | TSR | CAR | 状态 |
|------|------|-----|-----|------|
| 0 | pick up orange juice → basket | 0.0% (0/50) | 96.0% (48/50) | 完成 |
| 1 | pick up chocolate pudding → basket | 0.0% (0/50) | 22.0% (11/50) | 完成 |
| 2 | pick up milk → basket | — | — | 进行中 (ep 10/50) |

每个 task 约 70 min。Task 2 剩余 ~56 min。refine 组完成后还有 **no_refine** 和 **baseline** 两组串行。总剩余时间取决于 suite 中 task 总数。

### 2. 训练进度

| 实验 | 服务器 | GPU | Step/30K | 进度 | Loss | LR | 速度 | 预估剩余 |
|------|--------|-----|----------|------|------|----|------|----------|
| a3_spatial_bowl | westd-45947 | cuda:0 | 11514 | 38% | 0.040 | 1.85e-5 | 4.0s/it | ~20.5h |
| baseline_lora_spa | westd-35807 | cuda:1 | 19088 | 64% | 0.020 | 9.49e-6 | 3.98s/it | ~12.1h |
| baseline_lora_obj | westd-35807 | cuda:3 | 19050 | 64% | 0.016 | 9.53e-6 | 4.01s/it | ~12.2h |
| a1_lora_obj | westd-35807 | cuda:2 | 17446 | 58% | 0.028 | 1.14e-5 | 4.01s/it | ~14.0h |
| a1_lora_spa | westd-35807 | cuda:0 | 15558 | 52% | 0.031 | 1.37e-5 | 4.00s/it | ~16.1h |

### 3. 资源状态

- **westd-45947 GPU**: cuda:0 100% / 23.9GB (训练), cuda:1 33% / 8.6GB (eval)
- **westd-35807 GPU**: 4 卡全部 100% / ~23.9GB
- **westd-35807 磁盘**: 260G/350G (75%)

所有实验正常运行，无异常。5 个训练预计 5/22 下午~晚间陆续完成。

---
