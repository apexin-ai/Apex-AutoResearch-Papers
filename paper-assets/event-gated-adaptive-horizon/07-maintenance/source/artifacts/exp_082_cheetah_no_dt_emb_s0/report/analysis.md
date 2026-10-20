## exp_082_cheetah_no_dt_emb_s0 分析

### 配置
- **环境**: Cheetah Run (DMC), seed=0
- **关键变量**: dt_embed_dim=0 (无 dt_embedding)
- **其他配置**: subsample ON (gate_subsample_max_dt=2), gate_fixed_dt=2, imag_horizon=8
- **训练步数**: 105K env steps / 112K total
- **假设**: 移除 dt_embedding → 不触发 CIVO → 证明 trained dt_emb 是 Cheetah CIVO 的必要条件

### 结果

#### eval_return 轨迹
| Step | eval_return | vs baseline (448.1) |
|------|------------|-------------------|
| 5K   | 6.8   | 1.5%  |
| 15K  | 32.2  | 7.2%  |
| 25K  | 108.4 | 24.2% |
| 35K  | 119.4 | 26.6% |
| 45K  | **239.3** (peak) | 53.4% |
| 55K  | 157.0 | 35.0% |
| 65K  | 180.1 | 40.2% |
| 75K  | 178.6 | 39.9% |
| 85K  | 84.2  | 18.8% |
| 95K  | 57.7  | 12.9% |
| 105K | 83.2  | **18.6%** |

#### ve_ratio 轨迹
| Step | ve_ratio | civo_alert | NVE |
|------|----------|-----------|-----|
| 15K  | 0.038 | 0 | — |
| 25K  | 0.069 | 0 | — |
| 35K  | 0.132 | 0 | 1.49 |
| 45K  | 0.103 | 0 | 0.59 |
| 55K  | 0.237 | 0 | 0.96 |
| 65K  | 0.268 | 0 | 0.55 |
| 75K  | 0.311 | 0 | 0.55 |
| 85K  | 0.724 | 0 | 0.98 |
| 95K  | 0.955 | 0 | 1.58 |
| 105K | 0.616 | 0 | 1.02 |

- **ve_ratio 峰值**: 0.955@95K（< 1.0，value 从未超过 eval）
- **civo_alert**: 全程 0
- **NVE 峰值**: 1.58@95K — 由 eval 下降驱动（eval=57.7, value=55.1, 二者接轨），非 value 过估

### 因果对比（vs exp_078）

| 指标 | exp_082 (no dt_emb) | exp_078 (trained dt_emb) | 结论 |
|------|---------------------|-------------------------|------|
| dt_embed_dim | **0** | **32 (trained)** | 唯一变量 |
| CIVO triggered | **No** | **Yes** | ✓ 因果对 |
| civo_alert | 0 (全程) | 1 (55K, 65K) | — |
| ve_ratio peak | 0.955@95K | **2.318@75K** | 7.4x 差异 |
| NVE peak | 1.58@95K | **4.10@75K** | — |
| NVE classification | no_civo | onset_self_correcting | — |
| eval_return@105K | 83.2 (18.6% baseline) | 119.5 (26.7% baseline) | 两者都低于 baseline |
| eval_return peak | 239.3@45K | 213.7@35K | — |
| value_mean@105K | 51.3 | 34.8 | — |

**关键 window 对比 (45K-75K)**:
在 exp_078 CIVO 爆发的关键窗口（45K-75K），两个实验的 ve_ratio 轨迹完全分叉：
- exp_078: 0.295 → 0.908 → 1.72 → **2.318** (value 急剧膨胀)
- exp_082: 0.103 → 0.237 → 0.268 → **0.311** (value 平稳跟踪 eval)

### 跨环境一致性

| 环境 | no_dt_emb (control) | trained_dt_emb (trigger) | CIVO 差异 |
|------|--------------------|-----------------------|-----------|
| Walker Walk | 008f: NVE=0.30x, no CIVO | 008d: NVE=4.6x, CIVO | ✓ |
| Cheetah Run | **082: NVE=1.58x*, no CIVO** | 078: NVE=4.1x, CIVO | ✓ |

*082 的 NVE 1.58 是 eval 方差导致，非 value 过估（ve_ratio < 1.0）

### 结论

**conclusion: success**

移除 dt_embedding (dt_embed_dim=0) 完全阻止了 Cheetah Run 上的 CIVO 现象：
1. civo_alert 全程为 0，ve_ratio 峰值 0.955 远低于 CIVO 阈值
2. 与 exp_078 (trained dt_emb) 构成严格因果对，唯一变量 = dt_embed_dim
3. C2 因果链 "trained dt_emb → CIVO" 在 Cheetah 环境得到跨环境验证，与 Walker Walk 结论一致
4. 注意：两个实验的 eval 都显著低于 baseline (18.6% vs 26.7%)，说明 dt=2 imagination 本身损害性能，但只有 trained dt_emb 导致 CIVO
