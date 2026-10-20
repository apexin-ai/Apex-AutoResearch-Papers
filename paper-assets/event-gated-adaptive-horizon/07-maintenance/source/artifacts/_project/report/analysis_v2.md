# NVE Threshold Sensitivity Analysis V2

**Updated: 2026-05-25** — 组合诊断标准 + 双方法对比

## 数据集更新

- V1 数据点数: 61
- V2 数据点数: 61 (Collapsed: 25, Healthy: 36)
- 新增实验: 无额外新增 (V1 已包含 exp_084/085/087; exp_086 status=ANALYZING, 无 metrics, 排除)
- Method B 覆盖: 35/61 有 ve_ratio_peak
- 时间序列覆盖: 17/61 有逐 checkpoint NVE 轨迹数据

### Reviewer 指出的 NVE 数值差异

| exp_id | Reviewer 声称 NVE_peak | Registry NVE_peak (Method A) | Registry ve_ratio_peak (Method B) |
|--------|----------------------|------------------------------|-----------------------------------|
| exp_084_frozen_dt_emb_walker_s0 | 2.25 | 0.37 | N/A |
| exp_085_frozen_dt_emb_walker_s1 | 3.0 | 0.31 | N/A |

**分析**: Reviewer 的值与 registry 不匹配。Registry 使用 step-matched NVE (ve_ratio / baseline_ve_ratio_at_same_step)，Reviewer 可能使用了 raw V(s)/E_return 或不同的 baseline 归一化。两实验的 step-matched NVE 远低于 1.0，明确归类为 Healthy (无 CIVO)。两种方法下这些 frozen 实验都是 true negative。

---

## Method A: Step-matched NVE

NVE = experiment_ve_ratio / baseline_ve_ratio_at_same_step

### 单一阈值

| Threshold | Accuracy | Precision | Recall | F1 | FP | FN |
|-----------|----------|-----------|--------|------|-----|-----|
| 1.3× | 86.9% | 75.8% | 100% | 0.862 | 8 | 0 |
| **1.5×** | **93.4%** | **86.2%** | **100%** | **0.926** | 4 | 0 |
| 1.7× | 90.2% | 88.0% | 88.0% | 0.880 | 3 | 3 |
| 2.0× | 95.1% | 100% | 88.0% | 0.936 | 0 | 3 |

**AUROC = 0.9889**

θ=1.5× FP (4): exp_082_cheetah_no_dt_emb_s0 (1.58, eval-variance-driven), exp_008e_v3_subsample_on_dt1_h15 (1.93), exp_057_frozen_dt_emb_walker_s2 (1.88, transient), exp_047_frozen_dt_emb_walker_s1 (1.71, transient)

θ=2.0× FN (3): exp_008d_civo_trigger_s3 (1.53), exp_009b_008d_walker_s2 (1.62), exp_027_tcn_walker_s1 (1.64)

NVE_peak 分布:
- CIVO (25): min=1.530, median=4.100, max=70.640, mean=6.954
- Healthy (36): min=0.100, median=0.800, max=1.930, mean=0.845
- Overlap zone: NVE ∈ [1.530, 1.930], 含 3 CIVO + 4 Healthy

### 组合诊断标准

条件 A: NVE_peak ≥ τ
条件 B: NVE > τ 持续 ≥2 个连续 eval 点 (排除瞬态 spike)
条件 C: NVE 上升趋势 (≥10% 增幅)
判定 CIVO positive 需 A ∧ B ∧ C 同时满足。无轨迹数据时回退到条件 A only。

| Threshold | Accuracy | Precision | Recall | F1 | FP | FN | A_only fallback |
|-----------|----------|-----------|--------|------|-----|-----|----------------|
| 1.3× | 90.2% | 80.6% | 100% | 0.893 | 6 | 0 | 45/61 |
| 1.5× | 91.8% | 88.5% | 92.0% | 0.902 | 3 | 2 | 45/61 |
| 1.7× | 86.9% | 87.0% | 80.0% | 0.833 | 3 | 5 | 45/61 |
| 2.0× | 91.8% | 100% | 80.0% | 0.889 | 0 | 5 | 45/61 |

**关键发现**: 组合标准在 θ=1.3× 消除了 2 个 FP (exp_032b_dual_critic_walker_s1 和 exp_082_cheetah_no_dt_emb_s0 — 因 B 条件未满足而正确排除)。但引入新 FN (exp_008e_v3_walker_s2: B=N, 因 NVE 仅在末段突增而非持续; exp_029d_tcn_walker_s3_sigma02: B=N)。

当 74% 实验缺少轨迹数据时，组合诊断相比单一阈值优势有限。

---

## Method B: Raw ve_ratio peak

直接用 ve_ratio_peak (未除以 baseline) 作为分类分数。

可用子集: N=35 (CIVO=15, Healthy=20)

### 单一阈值

| Threshold | Accuracy | Precision | Recall | F1 | FP | FN |
|-----------|----------|-----------|--------|------|-----|-----|
| 0.8× | 80.0% | 70.0% | 93.3% | 0.800 | 6 | 1 |
| 1.0× | 91.4% | 87.5% | 93.3% | 0.903 | 2 | 1 |
| **1.3×** | **97.1%** | **100%** | **93.3%** | **0.966** | 0 | 1 |
| 1.5× | 97.1% | 100% | 93.3% | 0.966 | 0 | 1 |
| 2.0× | 88.6% | 100% | 73.3% | 0.846 | 0 | 4 |

**AUROC = 0.9700**

θ=1.3× FN (1): exp_009b_008d_walker_s2 (ve_ratio_peak=0.570, 但 step-matched NVE=1.62)

ve_ratio_peak 分布:
- CIVO (15): min=0.570, median=3.000, max=24.112, mean=4.722
- Healthy (20): min=0.200, median=0.527, max=1.283, mean=0.600

### 组合诊断标准

| Threshold | Accuracy | Precision | Recall | F1 | FP | FN |
|-----------|----------|-----------|--------|------|-----|-----|
| 0.8× | 85.7% | 81.2% | 86.7% | 0.839 | 3 | 2 |
| 1.0× | 85.7% | 85.7% | 80.0% | 0.828 | 2 | 3 |
| 1.3× | 91.4% | 100% | 80.0% | 0.889 | 0 | 3 |
| 1.5× | 88.6% | 100% | 73.3% | 0.846 | 0 | 4 |
| 2.0× | 77.1% | 100% | 46.7% | 0.636 | 0 | 8 |

---

## NVE_median_last5 辅助指标

对有轨迹数据的 16 个实验，取最后 5 个 checkpoint 的 NVE 中位数。

| exp_id | type | NVE_median_last5 | label | correct? |
|--------|------|-----------------|-------|----------|
| exp_008e_v3_walker_s2 | CIVO | 0.900 | CIVO | ✗ |
| exp_027_tcn_walker_s0 | CIVO | 1.396 | CIVO | ✓ |
| exp_027_tcn_walker_s1 | CIVO | 0.982 | CIVO | ✗ |
| exp_029b_tcn_walker_s2_sigma02 | CIVO | 2.315 | CIVO | ✓ |
| exp_029d_tcn_walker_s3_sigma02 | CIVO | 1.284 | CIVO | ✓ |
| exp_030b_tcn_cheetah_s0_sigma05 | CIVO | 1.674 | CIVO | ✓ |
| exp_068_008d_walker_repro_s1 | CIVO | 4.116 | CIVO | ✓ |
| exp_078_cheetah_008d_s0 | CIVO | 2.740 | CIVO | ✓ |
| exp_008a_no_subsample_dt2 | Healthy | 1.043 | Healthy | ✗ |
| exp_015b_frozen_dt_emb | Healthy | 0.420 | Healthy | ✓ |
| exp_027_tcn_walker_s0_sigma02 | Healthy | 0.857 | Healthy | ✓ |
| exp_029a_tcn_walker_s1_sigma02 | Healthy | 0.554 | Healthy | ✓ |
| exp_032b_dual_critic_walker_s1 | Healthy | 0.700 | Healthy | ✓ |
| exp_069_008f_walker_repro_s1 | Healthy | 0.533 | Healthy | ✓ |
| exp_070_008e_v3_walker_s0 | Healthy | 0.888 | Healthy | ✓ |
| exp_082_cheetah_no_dt_emb_s0 | Healthy | 0.980 | Healthy | ✓ |

**分布统计**:
- CIVO (8): min=0.900, median=1.674, max=4.116
- Healthy (8): min=0.420, median=0.857, max=1.043
- Accuracy: 13/16 = 81.2% (阈值=1.0)

**误判分析**:
- exp_008e_v3_walker_s2: median_last5=0.900 (CIVO, 误判为 Healthy) — NVE 末段才突增 (105K=3.78)，最后 5 点中前 4 个 < 1.0
- exp_027_tcn_walker_s1: median_last5=0.982 (CIVO, 边界误判) — 自我修正型 CIVO
- exp_008a_no_subsample_dt2: median_last5=1.043 (Healthy, 轻微超 1.0) — eval-variance-driven，非 CIVO

**结论**: NVE_median_last5 有判别力但弱于 NVE_peak。预期 "frozen 实验 median ≈ 0.5" 在 exp_015b (0.420) 上验证成功。Healthy 组 median 整体 < 1.0，CIVO 组 median > 1.0 (6/8)。

---

## 单一阈值 vs 组合标准对比

### Method A 对比

| 指标 | 单一阈值 θ=1.5× | 组合标准 θ=1.5× | 单一阈值 θ=2.0× | 组合标准 θ=2.0× |
|------|----------------|----------------|----------------|----------------|
| Accuracy | **93.4%** | 91.8% | **95.1%** | 91.8% |
| Precision | 86.2% | **88.5%** | **100%** | **100%** |
| Recall | **100%** | 92.0% | **88.0%** | 80.0% |
| F1 | **0.926** | 0.902 | **0.936** | 0.889 |
| FP | 4 | **3** | **0** | **0** |
| FN | **0** | 2 | **3** | 5 |

### Method A vs Method B (最佳阈值)

| 指标 | Method A θ=1.5× (N=61) | Method B θ=1.3× (N=35) |
|------|------------------------|------------------------|
| AUROC | **0.989** | 0.970 |
| F1 | 0.926 | **0.966** |
| Precision | 86.2% | **100%** |
| Recall | **100%** | 93.3% |
| FP | 4 | **0** |
| FN | **0** | 1 |

---

## 推荐

### 1. 主推 Method A (step-matched NVE), θ=1.5×

- AUROC=0.989, 最高判别力
- 100% recall — 不漏检任何 CIVO
- 4 个 FP 全部可解释 (frozen transient spike + eval-variance-driven)
- 与原论文 NVE 定义一致

### 2. 组合诊断标准当前不推荐作为主分类器

- 74% 实验缺少轨迹数据，导致大量 A_only 回退
- 有轨迹数据时确实能消除 FP (exp_082 被正确排除)，但同时引入新 FN
- **建议**: 作为 θ=1.5× 筛查后的二次确认，而非独立分类器

### 3. Method B 作为补充验证

- ve_ratio_peak 不受 baseline 选择偏差影响
- 在 θ=1.3× 达到 100% precision + 96.6% F1 (N=35 子集)
- exp_009b 是唯一 FN (ve_ratio_peak=0.570, 但 step-matched NVE=1.62)，说明 baseline normalization 对低幅 CIVO 更敏感

### 4. Decision rule (更新)

```
if NVE_peak >= 1.5×:
    → FLAG as potential CIVO
    if trajectory_data_available:
        if NVE > 1.5× for >= 2 consecutive checkpoints AND uptrend present:
            → CONFIRM as CIVO
        else:
            → LIKELY transient spike, monitor but do not kill
    else:
        → TREAT as CIVO (conservative)
        
if NVE_peak >= 2.0×:
    → DEFINITE CIVO (zero FP at this threshold)
```

### 5. Reviewer 关注点回应

- **exp_084 (NVE=0.37) 和 exp_085 (NVE=0.31)**: 两种方法下均为 true negative。Reviewer 声称的 2.25/3.0 值与 registry 不符，可能使用了未经 baseline 归一化的 raw V/E 比值。frozen dt_emb 实验的 NVE 远低于任何阈值，不会产生假阳性。
- **θ=2.0× 的 precision**: 在 Method A 单一阈值下仍为 100% (FP=0)，Reviewer 的 false positive 担忧未被数据支持。
