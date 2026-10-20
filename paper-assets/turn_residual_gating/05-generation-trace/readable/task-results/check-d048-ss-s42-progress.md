# check d048 ss s42 progress

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d048_ss_s42_progress_20260522T125637_result.json`
- **Structured JSON:** [`ec2514784b31bd365091.json`](../../sessions/ec/ec2514784b31bd365091.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## d048_ss_s42 训练状态

### 进度
- **Total steps: 3000**（3 epochs × 8000 samples / batch）
- **当前: Epoch 1, Step 750**（全局 ~1750/3000 steps）
- **完成度: ~58%**
- Epoch 0 已完成，checkpoint 已保存 (`runs/d048_ss_s42/epoch_0`)

### Loss 趋势
| 指标 | Epoch 0 初期 | Epoch 0 末期 | Epoch 1 当前 |
|------|-------------|-------------|-------------|
| L_NTP | ~1.55 | ~0.85 | ~0.83 |
| L_GAR | ~0.23 | ~0.001 | ~0.0003 |
| Total | ~1.81 | ~0.85 | ~0.83 |
| Epoch 0 均值 | — | NTP=0.978, GAR=0.030, Total=1.009 | — |

Loss 正常下降，GAR loss 已收敛到接近 0。

### Gate 统计
- **mean: 0.968**, std: 0.054, min: 0.73, max: 1.00
- L4 持续最低 (~0.76)，高层 L24-L27 接近 1.0（完全保留残差）
- Gate 从初始 0.81 已稳定上升到 0.97 区间

### Scheduled Sampling
- SS ratio 已到上限 0.300（30%），SS 使用率 16.2%
- SS_L_GAR 从 0.057 降到 0.033，TF_L_GAR 从 0.034 降到 0.027

### GPU 状态
- **NVIDIA RTX PRO 6000 Blackwell** (98GB)
- 显存: 52GB / 98GB (53%)
- GPU 利用率: 82%
- 温度: 71°C，功耗 382W/600W — 正常

### 进程
- PID 5310 存活，已运行 **10876 秒 (~3.0h)**
- 预估剩余: ~2.1h（按 58% 完成 / 3h 已用推算，总计约 5.2h，比预期 8h 快）

---
