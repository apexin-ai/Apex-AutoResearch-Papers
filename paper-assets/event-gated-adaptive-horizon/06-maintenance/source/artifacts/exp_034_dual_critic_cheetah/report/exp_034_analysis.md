# exp_034_dual_critic_cheetah 分析报告

## 实验配置
- Task: dmc_cheetah_run, seed=0, steps=210K (实际跑到 224K env steps)
- dual_critic=True, gate_fixed_dt=2, imag_horizon=8
- Server: bjb1-45299
- 训练正常完成 (EXIT_CODE=0)

## 核心数据

### Eval Return & VE Ratio Trajectory

| Step | Eval Return | ve_ratio | v1_mean | v2_mean | EMA_005 | EMA_095 |
|------|-------------|----------|---------|---------|---------|---------|
| 5K   | 8.3         | -        | 0.0     | 0.0     | 0.0     | 0.0     |
| 15K  | 27.8        | 0.1      | 1.8     | 1.8     | 1.6     | 2.6     |
| 25K  | 108.7       | 0.1      | 10.9    | 10.9    | 10.0    | 12.3    |
| 35K  | 110.0       | 0.2      | 23.7    | 23.7    | 21.8    | 25.9    |
| 45K  | **315.7** ★ | 0.1      | 39.0    | 39.0    | 35.2    | 43.0    |
| 55K  | **34.5** ↓  | **1.8**  | 60.5    | 60.5    | 54.5    | 68.0    |
| 65K  | 81.5        | 0.7      | 59.3    | 59.3    | 48.8    | 75.7    |
| 75K  | 183.0       | 0.3      | 52.6    | 52.6    | 41.1    | 71.6    |
| 85K  | 88.4        | 0.5      | 46.7    | 46.7    | 34.2    | 67.2    |
| 95K  | 41.0        | **1.0** ⚠ | 41.7  | 41.7    | 30.8    | 59.3    |
| 105K | **27.2** ↓  | **1.6** ⚠ | 43.4  | 43.4    | 33.8    | 62.1    |
| 115K | 45.9        | 0.9      | 39.3    | 39.3    | 29.4    | 59.3    |
| 125K | 58.7        | 0.6      | 33.8    | 33.7    | 22.9    | 54.4    |
| 135K | 71.6        | 0.4      | 28.5    | 28.5    | 17.5    | 49.4    |
| 145K | 61.9        | 0.4      | 24.6    | 24.5    | 13.5    | 45.2    |
| 155K | 52.1        | 0.4      | 21.5    | 21.5    | 10.6    | 42.2    |
| 165K | 153.8       | 0.1      | 19.2    | 19.2    | 8.4     | 40.6    |
| 175K | 104.9       | 0.2      | 17.8    | 17.8    | 6.9     | 39.3    |
| 185K | 101.4       | 0.2      | 16.7    | 16.7    | 5.8     | 38.1    |
| 195K | 115.3       | 0.1      | 15.7    | 15.7    | 4.8     | 37.4    |
| 205K | 101.5       | 0.1      | 14.8    | 14.8    | 3.9     | 36.7    |
| 215K | 97.5        | 0.1      | 14.2    | 14.2    | 3.1     | 36.5    |

★ = peak eval, ↓ = CIVO crash, ⚠ = CIVO alert triggered

### CIVO Alerts
- **Step 95K**: ve_ratio=1.012, delta_ve=0.485, eval_decline=2/3
- **Step 105K**: ve_ratio=1.591, delta_ve=0.578, eval_decline=3/3

### Gate Behavior
- gate_dt_mean=2.0, gate_dt_2_frac=1.0, gate_entropy=0.0 (全程固定 dt=2)

## 对比分析

### vs Cheetah Baseline (exp_010b, 无 dual-critic)
| Metric | exp_010b (baseline) | exp_034 (dual-critic) |
|--------|--------------------|-----------------------|
| Peak eval | 247.8 @ 35K | **315.7 @ 45K** |
| Final eval | **0.83** (catastrophic) | **97.5** |
| Peak ve_ratio | NVE=70.64 (catastrophic) | **1.8** |
| CIVO severity | 完全崩溃，不可恢复 | 触发但部分缓解 |

→ Dual-critic 将 Cheetah 从 **catastrophic CIVO (NVE=70.64, eval→0.83)** 缓解为 **transient CIVO (ve_ratio peak=1.8, eval→97.5)**。

### vs Walker Dual-Critic (exp_032, s0)
| Metric | Walker dual-critic s0 | Cheetah dual-critic |
|--------|----------------------|---------------------|
| Final eval | 787.7 | 97.5 |
| Final ve_ratio | 0.059 | 0.1 |
| Peak ve_ratio | < 1.0 | **1.8** |
| CIVO alerts | 0 | **2** |
| v1 ≈ v2 | ρ>0.999 | ρ>0.999 |
| CIVO prevented? | **Yes** | **No** (partially mitigated) |

### vs Cheetah SGS (exp_026)
| Metric | SGS s0 | SGS s1 | Dual-critic |
|--------|--------|--------|-------------|
| Peak ve_ratio | 8.56 | 11.81 | **1.8** |
| Final eval | 38.8 | 38.3 | **97.5** |
| CIVO suppressed? | No (amplified) | No (amplified) | **Partially** |

→ Dual-critic 明显优于 SGS（SGS 在 Cheetah 上反而加剧 CIVO）。

## 关键发现

### 1. CIVO 触发但未达到灾难级
- ve_ratio 两次超过 1.5× 阈值（55K: 1.8, 105K: 1.6）
- 但对比 baseline NVE=70.64，dual-critic 将 overestimation 压制了 ~40×
- Eval 从 peak 315.7 跌至 27.2 (91% drop at 105K)，但最终恢复到 97.5

### 2. v1 ≈ v2 完全确认
- 所有时间步 value1_mean ≈ value2_mean（差异 < 0.2）
- 两个 critic 对相同 overestimation dynamics 无差异化响应
- 这与 Walker 结果一致：dual-critic 不通过 critic 分歧工作

### 3. Value Function 持续衰退
- value_mean 从 peak 60.5 (55K) 一路降至 14.2 (215K)
- EMA_005 从 54.5 → 3.1（慢 EMA 几乎归零）
- EMA_095 从 68.0 → 36.5（快 EMA 保持更高，暗示间歇性高回报 episode）
- 但 eval_return 最终稳定在 ~100 → value 严重低估实际回报

### 4. 训练动态：双波 CIVO
- **First wave (45K→55K)**: eval 从 315.7 崩至 34.5, ve_ratio 飙至 1.8
- **Partial recovery (65K→75K)**: eval 恢复到 183.0, ve_ratio 降至 0.3
- **Second wave (85K→105K)**: eval 再崩至 27.2, ve_ratio 升至 1.6
- **Long tail recovery (115K→215K)**: eval 在 50-150 区间波动, value 持续下降

## 判定

### Conclusion: **negative**

**理由**:
1. **CIVO 未被抑制**: ve_ratio 超过 1.5× 阈值（peak 1.8），CIVO detector 触发 2 次
2. **Eval 严重退化**: final 97.5 仅为 peak 315.7 的 31%
3. **Hypothesis 不成立**: "dual-critic 是更通用的架构级干预" → 在 Cheetah 上未能完全抑制 CIVO，不能声称跨环境通用性

**重要 Nuance**:
- Dual-critic 提供了 **显著的部分缓解**（vs baseline: eval 97.5 vs 0.83, ve_ratio 1.8 vs NVE 70.64）
- 优于 SGS 在 Cheetah 上的表现（SGS 反而加剧 CIVO）
- 在 Intervention Hierarchy 中: **architecture-level (dual-critic) > representation-level (SGS) on Cheetah**，但 dual-critic 仍不足以完全抑制
- ROADMAP D123 预判 "Cheetah dual-critic CIVO triggered + v1≈v2" 是准确的
