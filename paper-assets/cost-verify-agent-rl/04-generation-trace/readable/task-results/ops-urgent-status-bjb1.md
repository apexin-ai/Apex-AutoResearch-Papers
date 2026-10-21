# ops urgent status bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-status-bjb1_20260518T024352_result.json`
- **Structured JSON:** [`a0e4d26e203d33e4276c.json`](../../sessions/a0/a0e4d26e203d33e4276c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。汇报如下：

---

## hsweep_h2_seed2 状态：已完成 ✓

- **PID 945877 已退出**，15/15 步全部完成
- Checkpoint 保存至 `/root/autodl-tmp/checkpoints/hsweep-h2/global_step_15/`
- ADV log：3000 行（128 episodes: 65 success / 63 fail）

### 训练 Metrics（全 15 步）

| Step | Success | Pass@8 | Entropy | PPO KL | Val |
|------|---------|--------|---------|--------|-----|
| 1 | 0.78% | 6.25% | 0.319 | 0.115 | - |
| 2 | 6.25% | 31.25% | 0.252 | 0.050 | - |
| 3 | 5.47% | 31.25% | 0.329 | 0.019 | - |
| 4 | 2.34% | 18.75% | 0.348 | 0.016 | - |
| 5 | 12.50% | 31.25% | 0.260 | 0.014 | **0.0%** |
| 6 | 6.25% | 31.25% | 0.253 | 0.011 | - |
| 7 | **0.00%** | **0.00%** | 0.260 | 0.009 | - |
| 8 | 7.03% | 31.25% | 0.252 | 0.009 | - |
| 9 | 3.12% | 25.00% | 0.370 | 0.008 | - |
| 10 | 3.91% | 12.50% | 0.426 | 0.015 | **0.0%** |
| 11 | 0.78% | 6.25% | 0.306 | 0.008 | - |
| 12 | 8.59% | 31.25% | 0.307 | 0.008 | - |
| 13 | 2.34% | 18.75% | 0.312 | 0.007 | - |
| 14 | **26.56%** | **68.75%** | 0.320 | 0.007 | - |
| 15 | **28.12%** | **62.50%** | 0.401 | 0.006 | **9.375%** |

Steps 1-13 低且不稳定（0-12.5%），step 14-15 突然跳升至 26-28%。Val success 从 0% → 9.375%。

### ADV 分析结果 (analyze_advantage_log_v2.py)

- **Sign-outcome agreement: 52.07%**（几乎等于随机）
- **Point-biserial r = 0.068**（p=1.94e-04，统计显著但效应极弱）
- P(adv>0 | success) = 37.06%，P(adv>0 | failure) = 30.60%
- **Magnitude decay γ = 0.9426**（R² = 0.5627）
- **Distribution overlap: 0.878**（接近 1.0 = 高度重叠）
- **Verdict: Weak or no sign misattribution**
- 图表已保存至 `artifacts/advantage_analysis.pdf` 和 `.png`

### exp029 reeval：无法启动

GPU 已被自动链式任务 **hsweep-h10-seed1**（PID 974251，10:47 启动）占满，两卡各 ~37GB、100% 利用率。

Sweep 队列序列为：
```
2:1 ✓ → 2:2 ✓ → 10:1 ▶ → 5:1 → 20:1 → full:1 → 2:3 → 5:2 → 5:3 → 10:2 → 10:3 → 20:2 → 20:3 → full:2 → full:3
```
当前正在运行第 3 个（共 15 个），剩余 12 个。每个约 12 小时。

### 注意

seed2 的 checkpoint 写入了 `hsweep-h2/global_step_15/`，**覆盖了 seed1 的同名 checkpoint**。seed1 的 step 15 checkpoint 已丢失。如果需要恢复 seed1 checkpoint，需要从 wandb 或重新训练。

---
