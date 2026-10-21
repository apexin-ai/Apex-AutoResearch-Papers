# 服务器状态报告 — bjb1-45299
**时间**: 2026-05-14 14:18 UTC

## GPU 状态

| GPU | 型号 | 显存占用 | GPU Util | 进程 PID | 实验 |
|-----|------|---------|----------|----------|------|
| 0 | RTX PRO 6000 Blackwell (98GB) | 2751/97887 MiB | 0% | 127766 | exp_008f_no_dt_embed_subsample_on_h8 |
| 1 | RTX PRO 6000 Blackwell (98GB) | 4167/97887 MiB | 0% | 126115 | exp_008e_v3_subsample_on_dt1_h15 |

> 两张 GPU util 均为 0%，可能是快照时刻处于 eval/data loading 阶段。

## 实验状态

### exp_008f_no_dt_embed_subsample_on_h8 — 运行中
- **PID**: 127761 (bash wrapper) -> 127766 (python)，已运行 1h26m
- **配置**: gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0
- **当前 step**: 35000 / 105000 (33%)
- **最近 train_return** (step 32K): 169~215（4 episode 均值 ~197）
- **Checkpoint**: latest.pt 221MB

### exp_008e_v3_subsample_on_dt1_h15 — 运行中
- **PID**: 126115 (python)，GPU 1
- **配置**: gate_fixed_dt=1, gate_subsample_max_dt=2, imag_horizon=15
- **当前 step**: 45000 / 105000 (43%)
- **eval_return** (step 45K): **382.2**
- **最近 train_return** (step 44K): 358~390
- **gate_dt 分布**: dt=1 占 100%（gate 完全选择 dt=1，未使用 subsample）
- **gate_entropy**: 0.0（无多样性）
- **value_mean**: 110.7, target_mean: 112.8
- **FPS**: 6.4
- **Checkpoint**: latest.pt 221MB

### exp_008a_fixed_dt2_no_subsample — 已完成
- **无 GPU 进程**，已结束
- **最终 step**: 112000（超过 105000 目标）
- **最终 train_return** (step 112K): 628~842（3 episode）
- **Checkpoint**: `checkpoint.ckpt` 不存在，但 `latest.pt` 存在 (221MB)，最后修改 14:13
- 注意: 缺少 checkpoint.ckpt，只有 latest.pt

## 关键观察

1. **exp_008e_v3 gate 退化**: gate 100% 选择 dt=1，entropy=0，subsample 机制未生效
2. **exp_008f 尚早期**: 仅完成 33%，train_return ~197，需要继续观察
3. **exp_008a 表现最好**: 最终 train_return 达到 628-842，fixed_dt=2 + no_subsample 配置效果不错
