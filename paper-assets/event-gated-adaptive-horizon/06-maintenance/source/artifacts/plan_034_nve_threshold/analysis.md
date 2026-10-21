# NVE Threshold Sensitivity Analysis

**Updated: 2026-05-25** (added exp_078, exp_082, exp_084, exp_085, exp_087; total N=61)

## 数据集

样本总数: 61 (Collapsed: 25, Healthy: 36)

| exp_id | env | config | seed | ground_truth | peak_nve | nve_source |
|--------|-----|--------|------|-------------|----------|------------|
| exp_006_fixed_dt2 | walker | 006_fixed_dt2 | 1 | CIVO(1) | 4.835 | computed ve_ratio/baseline at 65K |
| exp_008a_cheetah_unexposed_s0 | cheetah | 008a_unexposed | 0 | Healthy(0) | 0.490 | max(nve_105k) |
| exp_008a_cheetah_unexposed_s1 | cheetah | 008a_unexposed | 1 | Healthy(0) | 0.478 | max(nve_105k) |
| exp_008a_no_subsample_dt2 | walker | 008a_unexposed | 1 | Healthy(0) | 0.930 | max(normalized_ve) |
| exp_008a_unexposed_s1 | walker | 008a_unexposed | 1 | Healthy(0) | 0.598 | computed |
| exp_008a_unexposed_s2 | walker | 008a_unexposed | 2 | Healthy(0) | 0.463 | computed |
| exp_008d_civo_trigger_s3 | walker | 008d_civo_trigger | 3 | CIVO(1) | 1.530 | metrics.nve_peak |
| exp_008d_civo_trigger_s4 | walker | 008d_civo_trigger | 4 | CIVO(1) | 4.620 | metrics.nve_peak |
| exp_008d_subsample_on_h8 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.124 | computed |
| exp_008e_v3_s3 | walker | 008e_v3_mitigation | 3 | CIVO(1) | 4.020 | metrics.nve_peak |
| exp_008e_v3_s4 | walker | 008e_v3_mitigation | 4 | Healthy(0) | 0.990 | metrics.nve_peak |
| exp_008e_v3_subsample_on_dt1_h15 | walker | 008e_v3_mitigation | 1 | Healthy(0) | 1.930 | max(normalized_ve) at 25K |
| exp_008e_v3_walker_s1 | walker | 008e_v3_mitigation | 1 | Healthy(0) | 0.803 | computed |
| exp_008e_v3_walker_s2 | walker | 008e_v3_mitigation | 2 | CIVO(1) | 3.780 | max(final_nve) |
| exp_008f_no_dt_embed_subsample_on_h8 | walker | 008f_no_dt_emb | 1 | Healthy(0) | 1.020 | max(normalized_ve) at 25K |
| exp_008f_s3_no_dt_embed_walker | walker | 008f_no_dt_emb | 3 | Healthy(0) | 1.490 | metrics.nve_peak (parsed '< 1.5x') |
| exp_008f_s4 | walker | 008f_no_dt_emb | 4 | Healthy(0) | 1.410 | metrics.peak_nve |
| exp_009b_008d_walker_s2 | walker | 008d_civo_trigger | 2 | CIVO(1) | 1.620 | metrics.nve_peak |
| exp_009c_s3 | walker | other | 3 | Healthy(0) | 0.520 | max(nve_105k) |
| exp_009e_008d_walker_s1 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.130 | metrics.nve_peak |
| exp_010b_cheetah_civo_trigger | cheetah | 008d_civo_trigger | 1 | CIVO(1) | 8.270 | metrics.nve_peak |
| exp_010b_cheetah_civo_trigger_s0 | cheetah | 008d_civo_trigger | 0 | CIVO(1) | 70.640 | max(nve_105K) |
| exp_015b_frozen_dt_emb | walker | frozen_dt_emb | 1 | Healthy(0) | 0.467 | max(nve_85K) |
| exp_020_vanilla_dreamerv3_s2 | walker | baseline | 2 | Healthy(0) | 0.983 | computed |
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
| exp_034_dual_critic_cheetah | cheetah | dual_critic | 0 | CIVO(1) | 4.500 | computed |
| exp_036_dual_critic_pickcube | cheetah | dual_critic | 0 | CIVO(1) | 2.300 | metrics.nve_peak |
| exp_037_wide_critic_cheetah | cheetah | other | 0 | CIVO(1) | 3.600 | metrics.nve_peak |
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
| exp_071_008f_walker_s3 | walker | 008f_no_dt_emb | 3 | Healthy(0) | 0.974 | computed ve_ratio_peak/baseline |
| exp_072_008e_v3_walker_s5 | walker | 008e_v3_mitigation | 5 | Healthy(0) | 0.610 | metrics.nve_peak |
| exp_073_008f_walker_s4 | walker | 008f_no_dt_emb | 4 | Healthy(0) | 0.760 | metrics.nve_peak |
| exp_078_cheetah_008d_s0 | cheetah | 008d_civo_trigger | 0 | CIVO(1) | 4.100 | metrics.nve_peak |
| exp_082_cheetah_no_dt_emb_s0 | cheetah | 008f_no_dt_emb | 0 | Healthy(0) | 1.580 | metrics.nve_peak (eval-variance-driven) |
| exp_084_frozen_dt_emb_walker_s0 | walker | frozen_dt_emb | 0 | Healthy(0) | 0.370 | metrics.nve_peak |
| exp_085_frozen_dt_emb_walker_s1 | walker | frozen_dt_emb | 1 | Healthy(0) | 0.310 | metrics.nve_peak |
| exp_087_frozen_dt_emb_cheetah_s1 | cheetah | frozen_dt_emb | 1 | Healthy(0) | 0.299 | computed ve_ratio/baseline |

## Threshold Analysis

### θ = 1.3×
- **Accuracy: 86.9%** (53/61)
- Precision: 75.8% | Recall: 100.0% | **F1: 0.862**
- TP=25, FP=8, TN=28, FN=0
- FP: exp_082_cheetah_no_dt_emb_s0 (1.58), exp_046_frozen_dt_emb_cheetah (1.35), exp_008e_v3_subsample_on_dt1_h15 (1.93), exp_057_frozen_dt_emb_walker_s2 (1.88), exp_047_frozen_dt_emb_walker_s1 (1.71), exp_008f_s3_no_dt_embed_walker (1.49), exp_008f_s4 (1.41), exp_032b_dual_critic_walker_s1 (1.40)
- FN: none

### θ = 1.5× (recommended)
- **Accuracy: 93.4%** (57/61)
- Precision: 86.2% | Recall: 100.0% | **F1: 0.926**
- TP=25, FP=4, TN=32, FN=0
- FP: exp_082_cheetah_no_dt_emb_s0 (1.58, eval-variance-driven, NOT value overestimation), exp_008e_v3_subsample_on_dt1_h15 (1.93), exp_057_frozen_dt_emb_walker_s2 (1.88, transient), exp_047_frozen_dt_emb_walker_s1 (1.71, transient)
- FN: none

### θ = 1.7×
- **Accuracy: 90.2%** (55/61)
- Precision: 88.0% | Recall: 88.0% | **F1: 0.880**
- TP=22, FP=3, TN=33, FN=3
- FP: exp_008e_v3_subsample_on_dt1_h15 (1.93), exp_057_frozen_dt_emb_walker_s2 (1.88), exp_047_frozen_dt_emb_walker_s1 (1.71)
- FN: exp_027_tcn_walker_s1 (1.64), exp_009b_008d_walker_s2 (1.62), exp_008d_civo_trigger_s3 (1.53)

### θ = 2.0×
- **Accuracy: 95.1%** (58/61)
- Precision: 100.0% | Recall: 88.0% | **F1: 0.936**
- TP=22, FP=0, TN=36, FN=3
- FP: none
- FN: exp_027_tcn_walker_s1 (1.64), exp_009b_008d_walker_s2 (1.62), exp_008d_civo_trigger_s3 (1.53)

### 汇总

| Threshold | Accuracy | Precision | Recall | F1 | FP | FN |
|-----------|----------|-----------|--------|------|-----|-----|
| 1.3× | 86.9% | 75.8% | 100% | 0.862 | 8 | 0 |
| **1.5×** | **93.4%** | **86.2%** | **100%** | **0.926** | 4 | 0 |
| 1.7× | 90.2% | 88.0% | 88.0% | 0.880 | 3 | 3 |
| 2.0× | 95.1% | 100% | 88.0% | 0.936 | 0 | 3 |

## AUROC

**AUROC = 0.9889** (N=61, 25 positive, 36 negative)

NVE_peak 作为连续分数对 CIVO 的区分力极强。

**NVE 分布:**
- CIVO collapsed (25): min=1.530, median=4.100, max=70.640, mean=6.954
- Healthy (36): min=0.100, median=0.800, max=1.930, mean=0.845

**Overlap zone:** NVE ∈ [1.530, 1.930]
- 重叠 collapsed (3): exp_008d_s3 (1.530), exp_009b_s2 (1.620), exp_027_tcn_s1 (1.637)
- 重叠 healthy (4): exp_082_cheetah_no_dt_emb (1.580), exp_047_frozen_walker_s1 (1.710), exp_057_frozen_walker_s2 (1.880), exp_008e_v3_dt1_h15 (1.930)

**Data-optimal threshold (Youden's J):** θ ≈ 1.51×, J = 0.889

## 推荐 threshold

**推荐阈值: NVE ≥ 1.5×** (F1 = 0.926, AUROC = 0.989)

理由：
1. **100% recall**: 不漏掉任何 CIVO 实验。漏检比误报代价更高——未检出的 CIVO 导致无效训练浪费 GPU 小时。
2. **最佳 F1**: 1.5× 在四个候选 threshold 中 F1 第二高（0.926 vs 2.0× 的 0.936），但 recall 从 88%→100% 的提升价值大于 precision 从 100%→86% 的下降。
3. **4 个 FP 均可解释**: 2 个 frozen dt_emb transient spike（自然消退，非病理性）、1 个 eval-variance-driven（非 value overestimation）、1 个 mitigation config 早期 spike。
4. **Youden's J 最优点**: 统计最优切分在 θ≈1.51×，与 1.5× 一致。
5. **与论文定义一致**: 原论文使用 NVE≥1.5× 作为 CIVO onset 标准。

**Decision rule:**
- θ=1.5× for **screening** (maximize sensitivity, catch all CIVO early)
- θ=2.0× for **confirmation** (zero false positives, but misses 3 self-correcting CIVO seeds)

## 方法论说明

### NVE 计算方法

NVE (Normalized Value-Eval ratio) = experiment_ve_ratio / baseline_ve_ratio_at_same_step

- Walker Walk baseline: exp_001_baseline (seed 1) per-step VE ratios: 25K=0.087, 35K=0.241, 45K=0.331, 55K=0.404, 65K=0.563, 75K=0.719, 85K=0.701, 95K=0.632, 105K=0.656
- Cheetah Run baseline: approximate VE trajectory from exp_023a/023b: 25K=0.1, 35K=0.2, 45K=0.3, 55K=0.4, 65K=0.5, 75K=0.55, 85K=0.6, 95K=0.65, 105K=0.65
- 取 peak NVE (训练过程中最大 NVE) 作为分类特征
- NVE 数据提取优先级: nve_peak > nve_max > normalized_ve > ve_ratio/baseline

### Ground Truth 标注

- **CIVO(1)** (25 个): 明确 CIVO collapse 证据 (VE 持续加速, eval 显著下降, nve_classification=onset_collapse)
- **Healthy(0)** (36 个): 无 CIVO 迹象 (VE 稳定, eval 保持或增长)
- **EXCLUDE**: conclusion=killed/failed (技术故障), 无 NVE 数据, 纯 baseline (用于归一化), 分类模糊
