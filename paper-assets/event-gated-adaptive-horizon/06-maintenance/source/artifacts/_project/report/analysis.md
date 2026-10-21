# NVE Threshold Sensitivity Analysis

## 数据集

样本总数: 56 (Collapsed: 24, Healthy: 32)

| exp_id | env | config | seed | ground_truth | peak_nve | nve_source |
|--------|-----|--------|------|-------------|----------|------------|
| exp_006_fixed_dt2 | walker | 006_fixed_dt2 | 1 | CIVO(1) | 4.835 | computed ve_ratio/baseline at 65K |
| exp_008a_cheetah_unexposed_s0 | cheetah | 008a_unexposed | 0 | Healthy(0) | 0.490 | max(nve_105k) |
| exp_008a_cheetah_unexposed_s1 | cheetah | 008a_unexposed | 1 | Healthy(0) | 0.478 | max(nve_105k) |
| exp_008a_no_subsample_dt2 | walker | 008a_unexposed | 1 | Healthy(0) | 0.930 | max(normalized_ve_55K) |
| exp_008a_unexposed_s1 | walker | 008a_unexposed | 1 | Healthy(0) | 0.598 | computed civo_ve_ratio_final/max_baseline_ve |
| exp_008a_unexposed_s2 | walker | 008a_unexposed | 2 | Healthy(0) | 0.463 | computed civo_ve_ratio_final/max_baseline_ve |
| exp_008d_civo_trigger_s3 | walker | 008d_civo_trigger | 3 | CIVO(1) | 1.530 | metrics.nve_peak |
| exp_008d_civo_trigger_s4 | walker | 008d_civo_trigger | 4 | CIVO(1) | 4.620 | metrics.nve_peak |
| exp_008d_subsample_on_h8 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.124 | computed ve_ratio/baseline at 55K |
| exp_008e_v3_s3 | walker | 008e_v3_mitigation | 3 | CIVO(1) | 4.020 | metrics.nve_peak |
| exp_008e_v3_s4 | walker | 008e_v3_mitigation | 4 | Healthy(0) | 0.990 | metrics.nve_peak |
| exp_008e_v3_subsample_on_dt1_h15 | walker | 008e_v3_mitigation | 1 | Healthy(0) | 1.930 | max(metrics.normalized_ve) at 25K |
| exp_008e_v3_walker_s1 | walker | 008e_v3_mitigation | 1 | Healthy(0) | 0.803 | computed ve_ratio/baseline at 105K |
| exp_008e_v3_walker_s2 | walker | 008e_v3_mitigation | 2 | CIVO(1) | 3.780 | max(final_nve) |
| exp_008f_no_dt_embed_subsample_on_h8 | walker | 008f_no_dt_emb | 1 | Healthy(0) | 1.020 | max(eval_checkpoints.normalized_ve) at 25K |
| exp_008f_s3_no_dt_embed_walker | walker | 008f_no_dt_emb | 3 | Healthy(0) | 1.490 | metrics.nve_peak (parsed '< 1.5x') |
| exp_008f_s4 | walker | 008f_no_dt_emb | 4 | Healthy(0) | 1.410 | metrics.peak_nve |
| exp_009b_008d_walker_s2 | walker | 008d_civo_trigger | 2 | CIVO(1) | 1.620 | metrics.nve_peak |
| exp_009c_s3 | walker | other | 3 | Healthy(0) | 0.520 | max(nve_105k) |
| exp_009e_008d_walker_s1 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.130 | metrics.nve_peak |
| exp_010b_cheetah_civo_trigger | cheetah | 008d_civo_trigger | 1 | CIVO(1) | 8.270 | metrics.nve_peak |
| exp_010b_cheetah_civo_trigger_s0 | cheetah | 008d_civo_trigger | 0 | CIVO(1) | 70.640 | max(nve_105K) |
| exp_015b_frozen_dt_emb | walker | frozen_dt_emb | 1 | Healthy(0) | 0.467 | max(nve_85K) |
| exp_020_vanilla_dreamerv3_s2 | walker | baseline | 2 | Healthy(0) | 0.983 | computed ve_ratio/baseline at 105K |
| exp_021_full_sgs_cheetah_s1 | cheetah | sgs | 1 | CIVO(1) | 9.940 | metrics.nve_peak |
| exp_024b_cheetah_no_dt_emb_s0 | cheetah | 008f_no_dt_emb | 0 | Healthy(0) | 0.200 | metrics.nve_peak |
| exp_024b_cheetah_no_dt_emb_s1 | cheetah | 008f_no_dt_emb | 1 | Healthy(0) | 0.100 | metrics.nve_peak |
| exp_027_tcn_walker_s0 | walker | tcn | 0 | CIVO(1) | 3.965 | metrics.peak_nve |
| exp_027_tcn_walker_s0_sigma02 | walker | tcn | 0 | Healthy(0) | 0.908 | metrics.nve_max |
| exp_027_tcn_walker_s1 | walker | tcn | 1 | CIVO(1) | 1.637 | metrics.nve_max |
| exp_029a_tcn_walker_s1_sigma02 | walker | tcn | 1 | Healthy(0) | 0.643 | metrics.nve_max |
| exp_029b_tcn_walker_s2_sigma02 | walker | tcn | 2 | CIVO(1) | 2.765 | metrics.nve_peak |
| exp_029d_tcn_walker_s3_sigma02 | walker | tcn | 3 | CIVO(1) | 3.000 | metrics.nve_peak |
| exp_030b_tcn_cheetah_s0_sigma05 | cheetah | tcn | 0 | CIVO(1) | 10.666 | metrics.nve_max |
| exp_031b_tcn_pickcube_s0_sigma05 | pickcube | tcn | 0 | CIVO(1) | 3.300 | metrics.nve_peak |
| exp_032_dual_critic_walker | walker | dual_critic | 0 | Healthy(0) | 1.100 | metrics.nve_peak |
| exp_032b_dual_critic_walker_s1 | walker | dual_critic | 1 | Healthy(0) | 1.400 | metrics.peak_nve |
| exp_034_dual_critic_cheetah | cheetah | dual_critic | 0 | CIVO(1) | 4.500 | computed ve_ratio_peak/baseline at 55K |
| exp_036_dual_critic_pickcube | cheetah | dual_critic | 0 | CIVO(1) | 2.300 | metrics.nve_peak |
| exp_037_wide_critic_cheetah | cheetah | other | ? | CIVO(1) | 3.600 | metrics.nve_peak |
| exp_042_frozen_dt_emb_walker | walker | frozen_dt_emb | 0 | Healthy(0) | 0.194 | metrics.nve_peak |
| exp_043_008f_walker_s1 | walker | 008f_no_dt_emb | 1 | Healthy(0) | 0.808 | metrics.nve_peak |
| exp_045_treatment_extension_008d_s3 | walker | 008d_civo_trigger | 3 | CIVO(1) | 4.910 | metrics.nve_peak |
| exp_046_frozen_dt_emb_cheetah | cheetah | frozen_dt_emb | 0 | Healthy(0) | 1.350 | metrics.nve_peak |
| exp_047_frozen_dt_emb_walker_s1 | walker | frozen_dt_emb | 1 | Healthy(0) | 1.710 | metrics.nve_peak |
| exp_048_cheetah_civo_extension | cheetah | other | 0 | CIVO(1) | 2.750 | max(nve_final) |
| exp_057_frozen_dt_emb_walker_s2 | walker | frozen_dt_emb | 2 | Healthy(0) | 1.880 | metrics.nve_peak |
| exp_058_frozen_dt_emb_cheetah_s1 | cheetah | frozen_dt_emb | 1 | Healthy(0) | 0.780 | metrics.nve_peak |
| exp_059_walker_trained_s5 | walker | trained_dt_emb | 5 | CIVO(1) | 4.720 | metrics.nve_peak |
| exp_067_frozen_dt_emb_walker_plan015 | walker | frozen_dt_emb | 0 | Healthy(0) | 0.400 | metrics.nve_peak |
| exp_068_008d_walker_repro_s1 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.120 | max(nve_final_105k) |
| exp_069_008f_walker_repro_s1 | walker | 008f_no_dt_emb | 1 | Healthy(0) | 0.660 | metrics.nve_peak |
| exp_070_008e_v3_walker_s0 | walker | 008e_v3_mitigation | 0 | Healthy(0) | 0.800 | metrics.nve_peak |
| exp_071_008f_walker_s3 | walker | 008f_no_dt_emb | 3 | Healthy(0) | 0.974 | computed ve_ratio_peak/max_baseline_ve |
| exp_072_008e_v3_walker_s5 | walker | 008e_v3_mitigation | 5 | Healthy(0) | 0.610 | metrics.nve_peak |
| exp_073_008f_walker_s4 | walker | 008f_no_dt_emb | 4 | Healthy(0) | 0.760 | metrics.nve_peak |

## 分类结果

| threshold | TP | FP | TN | FN | Precision | Recall | F1 | Accuracy |
|-----------|----|----|----|----|-----------|--------|-----|----------|
| 1.0 | 24 | 9 | 23 | 0 | 0.727 | 1.000 | 0.842 | 0.839 |
| 1.1 | 24 | 8 | 24 | 0 | 0.750 | 1.000 | 0.857 | 0.857 |
| 1.2 | 24 | 7 | 25 | 0 | 0.774 | 1.000 | 0.873 | 0.875 |
| 1.3 | 24 | 7 | 25 | 0 | 0.774 | 1.000 | 0.873 | 0.875 |
| 1.5 ** | 24 | 3 | 29 | 0 | 0.889 | 1.000 | 0.941 | 0.946 |
| 1.7 | 21 | 3 | 29 | 3 | 0.875 | 0.875 | 0.875 | 0.893 |
| 2.0 | 21 | 0 | 32 | 3 | 1.000 | 0.875 | 0.933 | 0.946 |

## AUROC

**AUROC = 0.9902**

Computed from 24 positive + 32 negative samples using 33 ROC points

ROC 关键点 (FPR, TPR):

| Threshold | FPR | TPR |
|-----------|-----|-----|
| 1.0 | 0.281 | 1.000 |
| 1.1 | 0.250 | 1.000 |
| 1.2 | 0.219 | 1.000 |
| 1.3 | 0.219 | 1.000 |
| 1.5 | 0.094 | 1.000 |
| 1.7 | 0.094 | 0.875 |
| 2.0 | 0.000 | 0.875 |

## 推荐阈值

**推荐阈值: NVE >= 1.5** (基于最高 F1 = 0.941)

- Precision = 0.889, Recall = 1.000, Accuracy = 0.946
- TP=24, FP=3, TN=29, FN=0

### 阈值选择权衡

- **低阈值 (1.0-1.2)**: 高 Recall (少漏报) 但多误报。适用于安全优先场景 (宁可误报不可漏报)。
- **中阈值 (1.3-1.5)**: Recall/Precision 平衡。1.5 是 CIVO 论文推荐的 onset 检测阈值。
- **高阈值 (1.7-2.0)**: 高 Precision (少误报) 但可能漏报早期 CIVO。适用于减少不必要干预。

### 最佳阈值 (1.5) 下的分类细节

**False Positives (误报为CIVO):**

- `exp_008e_v3_subsample_on_dt1_h15`: peak_nve=1.930, config=008e_v3_mitigation, env=walker
- `exp_047_frozen_dt_emb_walker_s1`: peak_nve=1.710, config=frozen_dt_emb, env=walker
- `exp_057_frozen_dt_emb_walker_s2`: peak_nve=1.880, config=frozen_dt_emb, env=walker

### 阈值 1.5 下的分类细节

**False Positives (误报为CIVO):**

- `exp_008e_v3_subsample_on_dt1_h15`: peak_nve=1.930, config=008e_v3_mitigation, env=walker
- `exp_047_frozen_dt_emb_walker_s1`: peak_nve=1.710, config=frozen_dt_emb, env=walker
- `exp_057_frozen_dt_emb_walker_s2`: peak_nve=1.880, config=frozen_dt_emb, env=walker

## 方法论说明

### NVE 计算方法

NVE (Normalized Value-Eval ratio) = experiment_ve_ratio / baseline_ve_ratio_at_same_step

- Walker Walk baseline: exp_001_baseline (seed 1) per-step VE ratios: 25K=0.087, 35K=0.241, 45K=0.331, 55K=0.404, 65K=0.563, 75K=0.719, 85K=0.701, 95K=0.632, 105K=0.656
- Cheetah Run baseline: approximate VE trajectory from exp_023a/023b: 25K=0.1, 35K=0.2, 45K=0.3, 55K=0.4, 65K=0.5, 75K=0.55, 85K=0.6, 95K=0.65, 105K=0.65
- 取 peak NVE (训练过程中最大 NVE) 作为分类特征
- NVE 数据提取优先级: nve_peak > nve_max > normalized_ve > ve_ratio/baseline
- 操控环境 (pickcube/stackcube/peginsertion) 和 cartpole 因缺乏可靠 baseline 而排除

### Ground Truth 标注

- **CIVO(1)** (25 个): conclusion=negative/success + 明确 CIVO collapse 证据 (VE 持续加速, eval 显著下降, nve_classification=onset_collapse)
- **Healthy(0)** (33 个): conclusion=success + 无 CIVO 迹象 (VE 稳定, eval 保持或增长)
- **EXCLUDE**: conclusion=killed/failed (技术故障), 无 NVE 数据, baseline 实验, 操控环境, 分类模糊

### 排除实验 (98 个)

- **ambiguous (not manually labeled)** (18): exp_007_fixed_dt4, exp_008c_no_subsample_dt2_h8, exp_018v2_full_sgs_walker_s1, exp_022b_no_curriculum, exp_028_rave_walker_s0_ceil15 ...+13 more
- **baseline (reference)** (18): exp_001_baseline, exp_001_baseline_s2, exp_001_baseline_s2_extended, exp_001_baseline_s3, exp_001_baseline_s3_extended ...+13 more
- **excluded pickcube env (no reliable baseline for NVE)** (1): exp_019b_pickcube_civo_trigger
- **no NVE data** (23): exp_003_event_gated_v2, exp_004_event_gated_v3, exp_005_event_gated_v4, exp_016e_sgs_walker_s1, exp_018_full_sgs_s2 ...+18 more
- **not completed** (3): exp_077_cheetah_baseline_s0, exp_078_cheetah_008d_s0, exp_080_008e_v3_walker_s1
- **technical failure** (35): 016e, exp_002_event_gated, exp_006, exp_008a, exp_008a_untrained_s1 ...+30 more

### NVE 分布

- CIVO collapsed (24): min=1.530, median=4.120, max=70.640, mean=7.073
- Healthy (32): min=0.100, median=0.803, max=1.930, mean=0.870
- 类间间距 (min_collapsed - max_healthy): -0.400
  - 重叠区域: 3 collapsed 样本 + 3 healthy 样本在 [1.530, 1.930] 重叠范围内
  - 重叠 collapsed: exp_008d_civo_trigger_s3(nve=1.530), exp_009b_008d_walker_s2(nve=1.620), exp_027_tcn_walker_s1(nve=1.637)
  - 重叠 healthy: exp_008e_v3_subsample_on_dt1_h15(nve=1.930), exp_047_frozen_dt_emb_walker_s1(nve=1.710), exp_057_frozen_dt_emb_walker_s2(nve=1.880)
