# GPU 部署方案 — 2026-05-21

## 1. 服务器 GPU 状态

### bjb1-40020 (2×RTX 4090, 24GB each)
| GPU | 显存使用 | GPU Util | 状态 | 当前任务 |
|-----|---------|----------|------|---------|
| cuda:0 | 1 MiB / 24564 MiB | 0% | **空闲** | — |
| cuda:1 | 3121 MiB / 24564 MiB | 25% | 占用 | exp_035 narrow dual-critic Walker s0 |

### bjb1-45299 (2×RTX PRO 6000, 96GB each)
| GPU | 显存使用 | GPU Util | 状态 | 当前任务 |
|-----|---------|----------|------|---------|
| cuda:0 | 3135 MiB / 97887 MiB | 30% | 占用 | exp_036 dual-critic PickCube s0 |
| cuda:1 | 4 MiB / 97887 MiB | 0% | **空闲** | — |

## 2. 磁盘空间

| 服务器 | 数据盘总量 | 已用 | 可用 | logdir 大小 |
|--------|----------|------|------|------------|
| bjb1-40020 | 250G | 7.7G (4%) | 243G | 7.7G |
| bjb1-45299 | 250G | 61G (25%) | 190G | 61G |

两台均有充足空间，无需清理。

## 3. 代码版本

| 服务器 | Branch | Commit Hash |
|--------|--------|-------------|
| bjb1-40020 | main | `fb56c860a882` |
| bjb1-45299 | main | `fb56c860a882` |

**代码一致**，无需 sync。

## 4. 推荐部署方案

### 方案 A（最高优先）：exp_033 seed 1 → bjb1-40020 cuda:0

**理由**：2×2 Mechanism Factorial 中 "Wide Single Critic"（Capacity = Recovery）格只有 1 个 seed，是最薄弱的覆盖。补第二个 seed 对论文 Table 的统计可信度至关重要。

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic False --wide_critic True --logdir logdir/exp_033_wide_critic_walker_s1"
```

- 预计时长：~12-15h（参考 exp_033 s0）
- 预计完成：5/22 上午

### 方案 B（次优先）：exp_035 seed 1 → bjb1-45299 cuda:1

**理由**：等 exp_035 s0（40020 cuda:1 上运行中）出结果后再决定。如果 narrow dual-critic 表现良好，立即部署 seed 1 以完善 factorial 的 "Narrow Dual Critic" 格。

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:1 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_035_narrow_dual_critic_walker_s1"
```

- 条件触发：exp_035 s0 结果出来后
- 备选：如果 narrow dual-critic 效果差，可改为其他实验

## 5. 意外发现

bjb1-45299 cuda:0 正在运行 **exp_036**（ManiSkill PickCube dual-critic, seed 0, 200k steps）。此实验未在任务说明中提及，请确认是否为已知实验。

## 6. 时间线

| 日期 | 里程碑 |
|------|--------|
| 5/21 今天 | 方案 A 立即可部署 |
| 5/22 | exp_033 s1 预计完成；exp_035 s0 结果可查 |
| 5/25 | **数据锁定** — 所有实验必须在此之前完成 |
| 5/29 | **CoRL DDL** |

---
*报告生成时间：2026-05-21，待 Director 审批后执行。*
