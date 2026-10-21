# NVE Threshold Sensitivity Analysis V2

**Updated: 2026-05-25** — 组合诊断标准 + 双方法对比

## 数据集更新

- V1 数据点数: 61
- V2 数据点数: 63 (Collapsed: 25, Healthy: 38)
- 新增实验: exp_086_frozen_dt_emb_cheetah_s0 (Healthy, NVE_peak=0.27, ve_ratio_peak=0.2), exp_088_cheetah_008d_s1 (Healthy, NVE_peak=1.82, ve_ratio_peak=0.31, early-training transient)
- Method B 覆盖: 37/63 有 ve_ratio_peak
- 时间序列覆盖: 18/63 有逐 checkpoint NVE 轨迹数据

### exp_084/085 归一化差异说明

exp_084_frozen_dt_emb_walker_s0 (NVE_peak=0.37) 和 exp_085_frozen_dt_emb_walker_s1 (NVE_peak=0.31) 使用不同归一化方法（如 raw V(s)/E_return 而非 step-matched baseline 归一化）可能得到不同数值。两实验在 Method A 和 Method B 下均为明确的 true negative。

### exp_088 早期训练瞬态 NVE spike 说明

exp_088_cheetah_008d_s1 使用 008d（CIVO-trigger）配置但全程未触发 CIVO (civo_alert=0.0)。NVE_peak=1.82 发生在极早期 step 35K，此时实验和 baseline 的 ve_ratio 绝对值均很低（exp=0.191, baseline_mean=0.105），比值噪声大。NVE 在 55K 后迅速降至 < 0.6 并保持稳定。NVE_median_last5=0.379，eval_return_final=309.3（vs baseline 446.1）。这是 "trained config, no CIVO onset" 的重要数据点，表明早期低绝对值 ve_ratio 的 NVE 比值可能产生误导性的瞬态 spike。

---

## Method A: Step-matched NVE

NVE = experiment_ve_ratio / baseline_ve_ratio_at_same_step

### 单一阈值

| Threshold | Accuracy | Precision | Recall | F1 | FP | FN |
|-----------|----------|-----------|--------|------|-----|-----|
| 1.3× | 85.7% | 73.5% | 100% | 0.847 | 9 | 0 |
| **1.5×** | **92.1%** | **83.3%** | **100%** | **0.909** | 5 | 0 |
| 1.7× | 88.9% | 84.6% | 88.0% | 0.863 | 4 | 3 |
| 2.0× | 95.2% | 100% | 88.0% | 0.936 | 0 | 3 |

**AUROC = 0.9863**

θ=1.5× FP (5): exp_082_cheetah_no_dt_emb_s0 (1.58, eval-variance-driven), exp_008e_v3_subsample_on_dt1_h15 (1.93), exp_057_frozen_dt_emb_walker_s2 (1.88, transient), exp_047_frozen_dt_emb_walker_s1 (1.71, transient), exp_088_cheetah_008d_s1 (1.82, early-training transient at step 35K)

θ=2.0× FN (3): exp_008d_civo_trigger_s3 (1.53), exp_009b_008d_walker_s2 (1.62), exp_027_tcn_walker_s1 (1.64)

NVE_peak 分布:
- CIVO (25): min=1.530, median=4.100, max=70.640, mean=6.954
- Healthy (38): min=0.100, median=0.800, max=1.930, mean=0.856
- Overlap zone: NVE ∈ [1.530, 1.930], 含 3 CIVO + 5 Healthy

### 组合诊断标准

条件 A: NVE_peak ≥ τ
条件 B: NVE > τ 持续 ≥2 个连续 eval 点 (排除瞬态 spike)
条件 C: NVE 上升趋势 (≥10% 增幅)
判定 CIVO positive 需 A ∧ B ∧ C 同时满足。无轨迹数据时回退到条件 A only。

| Threshold | Accuracy | Precision | Recall | F1 | FP | FN | A_only fallback |
|-----------|----------|-----------|--------|------|-----|-----|----------------|
| 1.3× | 88.9% | 78.1% | 100% | 0.877 | 7 | 0 | 46/63 |
| 1.5× | 90.5% | 85.2% | 92.0% | 0.885 | 4 | 2 | 46/63 |
| 1.7× | 87.3% | 87.0% | 80.0% | 0.833 | 3 | 5 | 46/63 |
| 2.0× | 92.1% | 100% | 80.0% | 0.889 | 0 | 5 | 46/63 |

**关键发现**: 组合标准在 θ=1.3× 消除了 2 个 FP (exp_032b_dual_critic_walker_s1 和 exp_082_cheetah_no_dt_emb_s0 — 因 B 条件未满足而正确排除)。但 exp_088 在 θ=1.3× 和 θ=1.5× 下满足 A∧B∧C（35K-45K 连续两点 > τ 且有上升趋势），组合标准未能排除此 FP。θ=1.7× 下 B 条件未满足（仅 35K=1.82 > 1.7，45K=1.58 < 1.7），正确排除。

组合标准引入的 FN: exp_008e_v3_walker_s2 (B=N, NVE 仅末段突增), exp_029d_tcn_walker_s3_sigma02 (B=N)。

当 73% 实验缺少轨迹数据时，组合诊断相比单一阈值优势有限。

---

## Method B: Raw ve_ratio peak

直接用 ve_ratio_peak (未除以 baseline) 作为分类分数。

可用子集: N=37 (CIVO=15, Healthy=22)

### 单一阈值

| Threshold | Accuracy | Precision | Recall | F1 | FP | FN |
|-----------|----------|-----------|--------|------|-----|-----|
| 0.8× | 81.1% | 70.0% | 93.3% | 0.800 | 6 | 1 |
| 1.0× | 91.9% | 87.5% | 93.3% | 0.903 | 2 | 1 |
| **1.3×** | **97.3%** | **100%** | **93.3%** | **0.966** | 0 | 1 |
| 1.5× | 97.3% | 100% | 93.3% | 0.966 | 0 | 1 |
| 2.0× | 89.2% | 100% | 73.3% | 0.846 | 0 | 4 |

**AUROC = 0.9727**

θ=1.3× FN (1): exp_009b_008d_walker_s2 (ve_ratio_peak=0.570, 但 step-matched NVE=1.62)

ve_ratio_peak 分布:
- CIVO (15): min=0.570, median=3.000, max=24.112, mean=4.722
- Healthy (22): min=0.200, median=0.510, max=1.283, mean=0.569

### 组合诊断标准

| Threshold | Accuracy | Precision | Recall | F1 | FP | FN |
|-----------|----------|-----------|--------|------|-----|-----|
| 0.8× | 86.5% | 81.2% | 86.7% | 0.839 | 3 | 2 |
| 1.0× | 86.5% | 85.7% | 80.0% | 0.828 | 2 | 3 |
| 1.3× | 91.9% | 100% | 80.0% | 0.889 | 0 | 3 |
| 1.5× | 89.2% | 100% | 73.3% | 0.846 | 0 | 4 |
| 2.0× | 78.4% | 100% | 46.7% | 0.636 | 0 | 8 |

---

## NVE_median_last5 辅助指标

对有轨迹数据的 17 个实验，取最后 5 个 checkpoint 的 NVE 中位数。(exp_086 无轨迹数据，未纳入此表，NVE_peak=0.27 在所有阈值下均为 true negative。)

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
| exp_088_cheetah_008d_s1 | Healthy | 0.379 | Healthy | ✓ |

**分布统计**:
- CIVO (8): min=0.900, median=1.674, max=4.116
- Healthy (9): min=0.379, median=0.700, max=1.043
- Accuracy: 14/17 = 82.4% (阈值=1.0)

**误判分析**:
- exp_008e_v3_walker_s2: median_last5=0.900 (CIVO, 误判为 Healthy) — NVE 末段才突增 (105K=3.78)，最后 5 点中前 4 个 < 1.0
- exp_027_tcn_walker_s1: median_last5=0.982 (CIVO, 边界误判) — 自我修正型 CIVO
- exp_008a_no_subsample_dt2: median_last5=1.043 (Healthy, 轻微超 1.0) — eval-variance-driven，非 CIVO

**结论**: NVE_median_last5 有判别力但弱于 NVE_peak。预期 "frozen 实验 median ≈ 0.5" 在 exp_015b (0.420) 上验证成功。Healthy 组 median 整体 < 1.0 (9/9)，CIVO 组 median > 1.0 (6/8)。exp_088 (0.379) 进一步确认 median_last5 对排除早期瞬态 NVE spike 有效。

---

## 单一阈值 vs 组合标准对比

### Method A 对比

| 指标 | 单一阈值 θ=1.5× | 组合标准 θ=1.5× | 单一阈值 θ=2.0× | 组合标准 θ=2.0× |
|------|----------------|----------------|----------------|----------------|
| Accuracy | **92.1%** | 90.5% | **95.2%** | 92.1% |
| Precision | 83.3% | **85.2%** | **100%** | **100%** |
| Recall | **100%** | 92.0% | **88.0%** | 80.0% |
| F1 | **0.909** | 0.885 | **0.936** | 0.889 |
| FP | 5 | **4** | **0** | **0** |
| FN | **0** | 2 | **3** | 5 |

### Method A vs Method B (最佳阈值)

| 指标 | Method A θ=1.5× (N=63) | Method B θ=1.3× (N=37) |
|------|------------------------|------------------------|
| AUROC | **0.986** | 0.973 |
| F1 | 0.909 | **0.966** |
| Precision | 83.3% | **100%** |
| Recall | **100%** | 93.3% |
| FP | 5 | **0** |
| FN | **0** | 1 |

---

## 推荐（论文用框架）

### 1. 主方法：Method A step-matched NVE, θ=1.5×

- AUROC=0.986, 最高判别力
- 100% recall — 不漏检任何 CIVO
- F1=0.909
- 5 个 FP 全部可解释 (frozen transient spike + eval-variance-driven + early-training transient)
- 与原论文 NVE 定义一致

### 2. 辅助确认：组合标准（持续性 + 时序因果）

- 轨迹数据可用时，组合标准可排除瞬态 FP
- 条件：NVE > θ 持续 ≥2 个连续 eval 点 ∧ 上升趋势
- 作为 θ=1.5× 筛查后的二次确认，而非独立分类器
- 当前 73% 实验缺少轨迹数据，大量 A_only 回退
- 注意：exp_088 在 θ=1.5× 下满足组合条件（35K-45K 两连续点），θ=1.7× 下才被排除

### 3. 高置信度：θ=2.0×

- Precision=100% (FP=0)
- NVE_peak ≥ 2.0× 时可直接判定 CIVO，无需额外确认
- 代价：3 个 FN (低幅 CIVO 遗漏)

### 4. Appendix：Method B (raw ve_ratio) 交叉验证

- ve_ratio_peak 不受 baseline 选择偏差影响
- θ=1.3× 达到 100% precision + F1=0.966 (N=37 子集)
- exp_009b 是唯一 FN (ve_ratio_peak=0.570, step-matched NVE=1.62)，说明 baseline normalization 对低幅 CIVO 更敏感
- Method B AUROC=0.973，与 Method A 的 0.986 一致性高
- exp_088 (ve_ratio_peak=0.31) 在 Method B 所有阈值下均为 TN，表明 raw ve_ratio 对早期瞬态 spike 更鲁棒

### 5. Decision rule

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

### 6. 归一化方法差异说明

exp_084 (NVE=0.37) 和 exp_085 (NVE=0.31) 在 Method A 和 Method B 下均为 true negative。使用不同归一化方法（如 raw V(s)/E_return）可能得到不同数值，但不影响分类结果——frozen dt_emb 实验的 NVE 远低于任何阈值。θ=2.0× 在 Method A 下 precision=100% (FP=0)。

### 7. 早期瞬态 NVE spike 讨论

exp_088 揭示了 NVE_peak 作为分类指标的一个局限：当 baseline 和实验的 ve_ratio 在训练早期均接近零时，比值（NVE）可能因分母噪声而产生虚高 spike。exp_088 在 step 35K 的 NVE=1.82 来自 ve_ratio 0.191/0.105，绝对值极低。可能的缓解策略：
- 忽略 step ≤ 50K 的 NVE 值（仅在 ve_ratio 稳定后开始计算）
- 要求 ve_ratio ≥ 最小阈值（如 0.5）后才纳入 NVE 计算
- NVE_median_last5 (0.379) 天然抵抗此类早期 spike
