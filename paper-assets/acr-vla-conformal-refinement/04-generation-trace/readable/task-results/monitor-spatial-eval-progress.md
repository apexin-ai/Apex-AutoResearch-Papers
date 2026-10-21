# monitor spatial eval progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_spatial-eval-progress_20260513T232118_result.json`
- **Structured JSON:** [`b9d7c0a5b44537bc99d8.json`](../../sessions/b9/b9d7c0a5b44537bc99d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进度报告 — bjb1-18228 (2026-05-14 ~07:22 CST)

### 进程状态

| 实验 | PID | GPU | 状态 | 运行时间 |
|------|-----|-----|------|----------|
| eval-spatial-v6-full (VLA-only) | 109812 | cuda:0 | **Running** (Rl) | ~17 min |
| eval-acr-spatial-v2 (ACR-VLA) | 110083 | cuda:1 | **Running** (Rl) | ~17 min |
| eval-reconvla-spatial-v3 (ReconVLA) | 110353 | cuda:2 | **Running** (Rl) | ~17 min |
| crm-train-a3-obs-only | 104611 | cuda:3 | **Running** (Rl) | ~25 min |

### Eval 进度

**3 个 eval 均未产出 rollout 进度日志。** 代码每 5 个 rollout 才打印一次（`if (r+1) % 5 == 0`），每个 rollout 最多 300 steps × K=10 次 VLA 推理。估算每个 rollout 耗时 ~3-5 分钟，首次进度输出（Task 0, rollout 5/10）预计再等 ~5-10 分钟。

- 已完成 tasks: **0/10**（全部 3 个 eval）
- 已有成功率数据: 无
- 预估总时间: 10 tasks × 10 rollouts × ~4 min/rollout ≈ **6-7 小时**
- 预计完成时间: ~13:00-14:00 CST

### CRM obs_only 训练

- 进度: **Epoch 9/50**（日志可见部分，实际可能更快——nohup 输出有缓冲）
- Best val_loss: **0.018312**（epoch 4），之后 loss 基本持平
- 注意: 与完整 CRM（val_loss=0.009046）相比，obs_only 的 loss 高约 2x，这是预期行为（obs_only 缺少 proposed action 输入）

### GPU 利用率

| GPU | 型号 | 利用率 | 显存使用 |
|-----|------|--------|----------|
| 0 | RTX 4090 | 22% | 12040 / 24564 MiB |
| 1 | RTX 4090 | 25% | 1459 / 24564 MiB |
| 2 | RTX 4090 | 21% | 6732 / 24564 MiB |
| 3 | RTX 4090 | 10% | 565 / 24564 MiB |

**GPU 1 显存异常低（1.5GB）**，其他 eval 用了 6-12GB。ACR-VLA eval 可能模型还没完全加载到 GPU 上，或者 CUDA_VISIBLE_DEVICES=1 映射到了不同的物理 GPU。值得关注。

### 建议
- 等 ~10 分钟后再查，应该能看到首个 task 的 rollout 进度
- 关注 GPU 1 的 eval-acr-spatial-v2 显存是否正常增长

---
