# check pi05 crm training

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_pi05-crm-training_20260525T002608_result.json`
- **Structured JSON:** [`9158e19d74f2e250a4b5.json`](../../sessions/91/9158e19d74f2e250a4b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. CRM π0.5 训练 (GPU 0) — 仍在运行

| 指标 | 值 |
|------|-----|
| 当前进度 | Epoch 39/50, batch 50+/684 |
| 最近完成 epoch | Epoch 38: train_loss=0.007454, **val_loss=0.004280** (new best) |
| GPU 显存 | 580 MiB / 24564 MiB (模型仅 616K 参数，正常) |
| GPU 利用率 | 10% |
| 日志最后更新 | 08:27 CST (刚刚) |
| Checkpoint 路径 | `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/` |
| 已保存 checkpoints | epoch 34-38 + `crm_best.pt` |

**ETA 估算**: 38 epochs 用了 ~14h (18:38 CST 开始)，约 22min/epoch。剩余 12 epochs ≈ 4.4h，预计 **~12:45 CST (04:45 UTC)** 完成。与原始 ETA 吻合。

训练曲线健康：val_loss 连续下降，epoch 37→38 从 0.004317 降至 0.004280。

---

### 2. Precompute π0.5 Long 2048 (GPU 3) — 仍在运行

| 指标 | 值 |
|------|-----|
| 进度 | 96,300 / 136,090 (**70.8%**) |
| 速度 | 1.95 s/sample |
| 已用时间 | 187,357s (~52h) |
| 剩余时间 | ~77,413s (**~21.5h**) |
| 日志 | `/root/autodl-tmp/logs/precompute_pi05_long_2048.log` |
| 预计完成 | ~May 26 06:00 CST |

注：之前的 `precompute-pi05-long-bjb1-18228.log` 是旧 run (已被 SIGTERM 在 15400/136090 时终止)，当前活跃 run 在另一个日志路径。

---

### 总结

- 两个任务均正常运行中
- CRM 训练将在 ~4.5h 后完成，届时可部署 3-suite eval
- Checkpoint 路径: `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt`
- Precompute 还需 ~21h

---
