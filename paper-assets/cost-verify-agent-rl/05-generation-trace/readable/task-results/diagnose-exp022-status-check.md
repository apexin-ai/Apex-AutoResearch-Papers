# diagnose exp022 status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp022-status-check_20260515T032039_result.json`
- **Structured JSON:** [`18d7108b69bec62c5426.json`](../../sessions/18/18d7108b69bec62c5426.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
进程状态: 运行中
当前 step: 0 / 30 (尚未完成 step 0)
运行时间: 3h 24m (wrapper) / Workers 活跃 5h 35m
GPU 利用率: cuda:0 96% (41.7/97.9 GB), cuda:1 58% (41.7/97.9 GB)
磁盘: /root/autodl-tmp 55GB 可用 (79%)

Metrics: 无
  - 训练进入 step 0 后 ~3 小时无日志输出
  - 无 checkpoint 保存
  - 无 wandb 目录

分析:
  - 进程和 GPU 均正常工作（GPU 利用率高，workers ~39% CPU）
  - Step 0 耗时长的原因：ALFWorld 配置为 parallel_friendly=False, max_workers=1，
    训练 rollout 需串行跑 4×16=64 条轨迹，每条最多 30 turns
  - 日志无更新可能是 Python stdout 缓冲 + step 0 未完成
  - kl_loss_coef 已通过 sed 修改为 0.5（符合预期）

关键配置:
  - model: Qwen3 1.72B (from exp021 SFT checkpoint)
  - lr: 5e-7, kl_loss_coef: 0.5, entropy_coeff: 0.001
  - train: 4 groups × 16 = 64 trajectories/step
  - val: 8 groups × 1 = 8 trajectories
  - FSDP + bfloat16, ppo_epochs: 1

预估: Step 0 仍在 rollout 阶段，按当前速度首个 step 可能还需 1-2 小时。
30 步总时长可能需 24-48 小时（取决于 step 0 完成后的实际 step 耗时）。
```

---
