# wandb m2 training progress

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_wandb_m2_training_progress_20260513T215030_result.json`
- **Structured JSON:** [`ad643a35df87289f1cde.json`](../../sessions/ad/ad643a35df87289f1cde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Based on all available local data, here's the M2 Full Training progress report:

---

## M2 Full Training Progress Report (as of 2026-05-13 ~22:00 UTC)

### 限制说明
- **WandB 为离线模式** (`WANDB_MODE=offline`)，API 查询不可用
- **SSH 未配置密钥**，无法直连服务器获取实时数据
- 以下信息基于本地 worker 结果文件和 registry，最后更新 ~21:50 UTC

---

### m2_full_qwen (cuda:0) — PID 73544/73558

| 项目 | 状态 |
|------|------|
| 当前 run | **random_s42** (1/9) |
| 进度 (19:28 UTC) | Epoch 1, step 500/1414 (35%) |
| Loss (step 500) | 0.6168, lr=2.00e-5 (已过 warmup) |
| Eval 数据 | **无** — step 500 刚到触发点，可能正在 eval 或刚完成 |
| GPU | 100%, 50.7 GB / 95.6 GB, 72°C |
| 速度 | ~9.5-12 s/step |
| 预估每 run | ~11-14 小时 |
| 预估 9 runs 总计 | ~100-126 小时 (4.2-5.3 天, 约 May 17-18 完成) |
| 已完成 run | 0/9 |

### m2_full_starcoder (cuda:1) — PID 74122/76627

| 项目 | 状态 |
|------|------|
| 当前 run | **random_s42** (1/9) |
| 进度 (19:28 UTC) | Epoch 1, step 200/1414 (14%) |
| Loss (step 200) | 0.4387, lr=9.25e-6 (warmup 阶段) |
| Eval 数据 | **无** — 未触发 (需到 step 500) |
| GPU | 100%, 55.2 GB / 95.6 GB, 72°C |
| 已完成 run | 0/9 |
| 备注 | PID 347730 (重复进程) 已在 21:48 UTC kill |

### 总结

1. **Qwen**: 9 runs 中 0 个完成，第 1 个 run (random_s42) 在 epoch 1 约 35% 处。**尚无 eval 数据**，但 step 500 已到触发点，eval 指标应很快产出。
2. **StarCoder**: 9 runs 中 0 个完成，第 1 个 run (random_s42) 在 epoch 1 约 14% 处，仍在 warmup。**无 eval 数据**。
3. **Strategy 对比**: 尚不可能，两个模型都还在第一个 strategy (random) 的第一个 seed。
4. **状态正常**: 双卡 100% 利用率，进程存活，温度正常。
5. **无法获取更新数据**: WandB 离线 + 无 SSH 密钥。建议通过有 SSH 权限的 worker 查询最新日志（`/root/runs/m2_full_qwen/random_s42.log` 和 `/root/runs/m2_full_starcoder/random_s42.log`），或配置 WandB online 模式以便后续 API 查询。

---
