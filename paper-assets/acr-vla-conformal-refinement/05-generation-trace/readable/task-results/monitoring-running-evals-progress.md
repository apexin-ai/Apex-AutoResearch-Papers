# monitoring running evals progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitoring_running-evals-progress_20260514T031708_result.json`
- **Structured JSON:** [`06241c738b92cd779bf0.json`](../../sessions/06/06241c738b92cd779bf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度总览

### bjb1-18228 (4×4090)

| # | 实验 | GPU | 进程 | 进度 | 已用时间 | 预估剩余 | GPU利用/显存 |
|---|------|-----|------|------|---------|---------|-------------|
| 1 | crm-train-k5 | cuda:0 | **alive** | **32/50 epoch (64%)** | 1h36m | ~54min | 10%, 6.9/24.6G |
| 2 | eval-acr-spatial-v2 | cuda:1 | **alive** | **30/100 rollouts (30%)** | 3h35m | ~8.3h | 22%, 1.5/24.6G |
| 3 | eval-reconvla-spatial-v3 | cuda:2 | **alive** | **~35/100 rollouts (35%)** | 3h35m | ~6.6h | 18%, 1.4/24.6G |
| 4 | eval-scalar-unc-spatial | cuda:3 | **alive** | **10/100 rollouts (10%)** | 56m | ~7.5h | 23%, 5.7/24.6G |

### bjb2-40593 (1×4090D)

| # | 实验 | GPU | 进程 | 进度 | 已用时间 | 预估剩余 | GPU利用/显存 |
|---|------|-----|------|------|---------|---------|-------------|
| 5 | eval-vla-mean-spatial | cuda:0 | **alive** | **0/100 rollouts (0%)** | 9m | 无法估算 | 11%, 6.2/24.6G |

### crm-train-k5 训练曲线

- 当前 epoch 32/50, train_loss=0.014890, **val_loss=0.009602**
- 最佳 val_loss=**0.009520** @ epoch 29
- val_loss 过去几个 epoch 在 0.0095-0.0098 震荡，趋于收敛

### Eval 中间成功率

| 实验 | 已完成 tasks | 中间成功率 | 各 task 详情 |
|------|-------------|-----------|-------------|
| acr-spatial-v2 | 3/10 | **36.7%** (11/30) | 40%, 70%, 0% |
| reconvla-spatial-v3 | 3/10 (+task4进行中) | **53.3%** (16/30) | 60%, 100%, 0% |
| scalar-unc-spatial | 1/10 | **50.0%** (5/10) | 50% |
| vla-mean-spatial | 0/10 | — | 刚启动 |

### 备注
- 所有 5 个进程均存活
- bjb2 的 vla-mean-spatial 刚启动 9 分钟，还在模型加载/环境初始化阶段
- eval GPU 利用率偏低（10-23%）属正常——rollout 大部分时间在 robosuite 仿真而非 GPU 推理
- reconvla-spatial-v3 的 task2 (pick_up_bowl_next_to_ramekin) 取得 100% 成功率

---
