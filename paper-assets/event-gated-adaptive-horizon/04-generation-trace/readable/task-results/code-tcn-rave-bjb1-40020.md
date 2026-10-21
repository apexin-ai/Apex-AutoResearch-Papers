# code tcn rave bjb1 40020

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tcn_rave_bjb1_40020_20260520T033829_result.json`
- **Structured JSON:** [`ede2b7d99762c91101e9.json`](../../sessions/ed/ede2b7d99762c91101e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**代码修改**（3 个文件）：
- `networks.py`: RSSM 新增 `tcn_enabled/tcn_sigma` 参数，`img_step` 新增 `imagine` 标记，imagination 模式下对 dt_embedding 加高斯噪声
- `models.py`: WorldModel 传递 TCN 参数到 RSSM；ImagBehavior 新增 `rave_v_anchor` EMA buffer，`_train` 中用真实状态更新锚点，`_compute_target` 中截断 value；`_imagine` 的两条路径均传 `imagine=True`
- `configs.yaml`: 新增 `tcn_enabled/tcn_sigma/rave_enabled/rave_ceiling/rave_ema_decay` 默认值

**实验提交**（bjb1-40020, 2×RTX 4090）：

| 实验 | GPU | 干预 | 关键超参 | 状态 |
|------|-----|------|---------|------|
| exp_027_tcn_walker_s0_sigma02 | cuda:0 | TCN | σ=0.2 | RUNNING, step 5000+ |
| exp_028_rave_walker_s0_ceil15 | cuda:1 | RAVE | ceiling=1.5, decay=0.99 | RUNNING, 首轮 eval |

两个实验基础配置一致：`gate_enabled=True, gate_fixed_dt=2, imag_horizon=8, steps=210000, dmc_walker_walk, seed=0`。

---
