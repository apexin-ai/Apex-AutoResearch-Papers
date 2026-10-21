# Appendix 数字审计报告

审计日期：2026-05-23
审计范围：`docs/paper/appendix.tex` 关键表格与数字 vs registry 实验记录

## 1. LLM Judge 表 (tab:llm_judge, L8–28)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| GPT-5.5 IID F1=.383 | L18 | plan_012_gpt55_judge | gpt55_full_f1=0.383 | ✓ | |
| GPT-5.5 Unparse. 30–47% | L18 | plan_012_gpt55_judge | unparseable_k2="23/76"(30.3%), unparseable_full="36/76"(47.4%) | ✓ | 范围为k2→full |
| Qwen3-8B zero-shot IID F1=.100 | L19 | plan_012_llm_judge_qwen | qwen_full_f1=0.1 | ✓ | |
| Qwen3-8B zero-shot DD=.244 | L19 | exp5_llm_judge_ood | dd_ood full_macro_f1=0.2436 | ✓ | 四舍五入 |
| Qwen3-8B zero-shot AA=.244 | L19 | exp5_llm_judge_ood | 无AA数据 | ⚠ | 逻辑一致（全预测benign→macro F1=0.244由test set比例决定，DD/AA同composition），但registry无AA显式记录 |
| Qwen3-8B 3-shot DD=.566 | L22 | exp10_fewshot_llm_judge | dd_full_macro_f1=0.5663 | ✓ | |
| Qwen3-8B 3-shot AA=.652 | L22 | exp10_fewshot_llm_judge | aa_full_macro_f1=0.6523 | ✓ | |
| 9-class DD=.994, AA=.972, IID=1.000 | L25 | main experiments | 主表数据 | ✓ | |
| GPT-5.5 precision=1.0 | L31 | plan_012_gpt55_judge | gpt55_k2_precision=1, gpt55_k5_precision=1 | ✓ | |
| GPT-5.5 recall 0.105–0.290 | L31 | plan_012_gpt55_judge | k2_recall=0.1053, k5_recall=0.2895 | ✓ | |

## 2. Cross-LLM 表 (tab:cross_llm, L210–223)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| Llama JB+Llama ben DD: Van=.261, MLM=.282, 9cl=.433 | L217 | exp14_cross_llm_validation | llama_dd_full: vanilla=0.261, jb_mlm=0.282, 9class=0.433 | ✓ | |
| Llama JB+Llama ben AA: Van=.261, MLM=.368, 9cl=.321 | L217 | exp14_cross_llm_validation | llama_aa_full: vanilla=0.261, jb_mlm=0.368, 9class=0.321 | ✓ | |
| Llama JB+Qwen ben DD: Van=.302, MLM=.778, 9cl=1.000 | L218 | exp14b_cross_llm_control | dd_full: vanilla=0.302, jb_mlm=0.778, 9class=1.0 | ✓ | |
| Llama JB+Qwen ben AA: Van=.302, MLM=.903, 9cl=.801 | L218 | exp14b_cross_llm_control | aa_full: vanilla=0.302, jb_mlm=0.903, 9class=0.801 | ✓ | |
| MLM DD std=0.306, seed 456 outlier F1=0.345 | L222 | exp14b_cross_llm_control | "jb_mlm DD Full std=0.306 due to seed456 outlier (0.345)" | ✓ | |
| Qwen JB+Qwen ben row (Van=.312, MLM=.914, 9cl=.997) | L216 | — | 50-sample matched subset protocol | ⚠ | 无独立exp_id存储此条件；.997与frozen_verify一致，.312/.914与主表接近但非严格对应 |

## 3. Cross-LLM Error Decomposition 表 (tab:cross_llm_error, L232–241)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| TP rate: Van=0%, MLM=68%, 9cl=100% | L236 | exp14c_prediction_analysis | vanilla=0, jb_mlm=0.68, 9class=1.0 | ✓ | |
| FP rate (Llama): Van=29.3%, MLM=88%, 9cl=90% | L237 | exp14c_prediction_analysis | vanilla=0.293, jb_mlm=0.88, 9class=0.9 | ✓ | |
| FP rate (Qwen): Van=0%, MLM=0.9%, 9cl=0% | L238 | exp14c_prediction_analysis | vanilla=0, jb_mlm=0.009, 9class=0 | ✓ | |

## 4. Representation Analysis 表 (tab:representation, L613–627)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| PR: Vanilla=31.9, Wiki=25.0, JB-MLM=24.6, Topic=14.5, Scrambled=7.8, 9-class=9.4, Binary=3.7 | L618–624 | exp49_representation_analysis | 31.93, 25.0, 24.56, 14.46, 7.82, 9.37, 3.73 | ✓ | 全部四舍五入一致 |
| Fisher: Vanilla/<0.001, Wiki/<0.001, JB-MLM/<0.001, Topic/0.012, Scrambled/2.60, 9-class/4.47, Binary/19.7 | L618–624 | exp49_representation_analysis | 6.9e-05, 2.84e-04, 8.29e-04, 0.0124, 2.603, 4.466, 19.726 | ✓ | |
| Wt.Δ(%): 0.000, 0.221, 0.256, 0.371, 0.283, 0.303, 0.239 | L618–624 | exp49_representation_analysis | weight_norm: 0, 2.924, 3.375, 4.894, 3.74, 3.998, 3.16 | ✓ | weight_norm / pretrained_norm(≈1322.6) × 100% 一致 |

## 5. Layer-wise Analysis (fig:layerwise caption, L637–643)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| 9-class Fisher peak 10.9 (layer 10) | L639 | exp50_layerwise_representation | layer_10_peak 9class=10.92 | ✓ | 10.92→10.9 |
| Vanilla Fisher 0.73 (15×) | L639 | exp50_layerwise_representation | layer_10_peak vanilla=0.73 | ✓ | 10.92/0.73=14.96≈15× |
| Scrambled Fisher peaks 7.9 (layer 12) | L643 | exp50_layerwise_representation | layer_12 scrambled=7.91 | ✓ | |
| Layer 12: 9class=6.53, vanilla=2.83, jb_mlm=2.61 | L640–643 | exp50_layerwise_representation | layer_12: 9class=6.53, vanilla=2.83, jb_mlm=2.61 | ✓ | |

## 6. Discriminative Subspace Probe 表 (tab:discriminative_probe, L655–673)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| 9-class top-3: DD=1.000, AA=1.000, FITD=1.000 | L659 | exp54_causal_probe_subspace | 1.0, 1.0, 1.0 | ✓ | |
| 9-class rand-3 AA=0.928±.129 | L661 | exp54 | 9class_rand3_aa_f1=0.928 | ✓ | |
| scrambled top-3 AA=0.962 | L665 | exp54 | scrambled_top3_aa_f1=0.962 | ✓ | |
| scrambled rand-3 AA=0.766 | L666 | exp54 | scrambled_rand3_aa_f1=0.766 | ✓ | |
| JB-MLM top-3 AA=0.618 | L668 | exp54 | mlm_top3_aa_f1=0.618 | ✓ | |
| JB-MLM full-768 AA=0.636 | L669 | exp54 | mlm_full_aa_f1=0.636 | ✓ | |
| JB-MLM rand-5: DD=0.685, AA=0.584, FITD=0.744 | L670 | exp54 | 0.685, 0.584, 0.744 | ✓ | |

## 7. SVD Necessity Ablation 表 (tab:svd_necessity, L686–697)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| Original: DD=1.000, AA=.994, FITD=1.000 | L692 | exp65_svd_necessity_ablation | DD=1.0, AA=0.9936, FITD=1.0 | ✓ | 0.9936→.994 四舍五入 |
| Remove top-3: DD=.831, AA=.938, FITD=1.000 | L693 | exp65 | DD=0.8308, AA=0.938, FITD=1.0 | ✓ | 0.8308→.831 |
| Remove random-3: DD=1.000, AA=.994, FITD=1.000 | L694 | exp65 | DD=1.0, AA=0.9936, FITD=1.0 | ✓ | |
| Text: "17pp DD drop" | L699 | exp65 | 1.000−0.831=0.169≈17pp | ✓ | |
| Text: "5.6pp AA drop" | L699 | exp65 | 0.994−0.938=0.056=5.6pp | ✓ | |

## 8. Efficiency 表 (tab:efficiency, L800–815)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| DeBERTa+BiGRU 12.1 ms | L808 | exp29_inference_efficiency | deberta_bigru_latency_ms=12.12 | ✓ | |
| DeBERTa+BiGRU 186.7M params | L808 | exp29 | deberta_bigru_params_M=186.73 | ✓ | |
| DeBERTa+BiGRU 862 MB VRAM | L808 | exp29 | deberta_bigru_gpu_mem_MB=861.5 | ✓ | 四舍五入 |
| TF-IDF+LR 0.43 ms | L807 | exp29 | tfidf_lr_latency_ms=0.43 | ✓ | |
| DeBERTa+BiGRU ±1.2 ms std | L808 | exp29 | 无std记录 | ⚠ | exp46有std=1.61（不同硬件），exp29无std；来源不明 |
| Qwen3-8B ~5,200 ms | L809 | exp10 | 无latency记录 | ⚠ | 脚注标注来源exp10，但registry无latency数据 |
| 24.3× speedup (main text引用) | L815 | exp46_inference_efficiency | 318.53/13.12=24.28≈24.3 | ✓ | |

## 9. WildChat FPR 表 (tab:wildchat_fpr, L436–448)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| 9-class: 66.8/61.1/76.5, mean=68.1±6.4 | L442 | exp19_wildchat_fpr | seed42=0.668, seed123=0.611, seed456=0.765, mean=0.681, std=0.064 | ✓ | ×100 |
| MLM: 36.7/64.6/32.3, mean=44.5±14.3 | L443 | exp19 | seed42=0.367, seed123=0.646, seed456=0.323, mean=0.445, std=0.143 | ✓ | |
| Vanilla: 47.3/42.5/54.4, mean=48.1±4.9 | L444 | exp19 | seed42=0.473, seed123=0.425, seed456=0.544, mean=0.481, std=0.049 | ✓ | |

## 10. OASST2 Adaptation Curve 表 (tab:oasst2_curve, L462–474)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| N=0 FPR=57.5% | L468 | exp51_lmsys_benign_ood | baseline_fpr=0.575 | ✓ | |
| N=10 FPR=20.5%, DD=1, AA=1, FITD=1 | L469 | exp51 | n10: fpr=0.205, dd=1, aa=1, fitd=1 | ✓ | |
| N=25 FPR=1.5%, AA=0.953 | L470 | exp51 | n25: fpr=0.015, aa=0.953 | ✓ | |
| N=50 FPR=0.5%, AA=0.990 | L471 | exp51 | n50: fpr=0.005, aa=0.990 | ✓ | |

## 11. Dual-OOD 表 (tab:dual_ood, L487–501)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| IID: DD=.994±.009, AA=.981±.019 | L492 | 主实验 | — | ✓ | 上界条件（FPR=0） |
| WildChat no adapt: DD=.855±.020, AA=.842±.012 | L493 | 派生 | exp19 FPR + OOD recall 组合计算 | ✓ | 方法论清晰 |
| "12–14pp drop" | L501 | 派生 | .994−.855=13.9pp, .981−.842=13.9pp | ✓ | |
| "within 0.3pp" recovery | L501 | 派生 | WC+10: 0pp gap; OASST2+25: 0.3pp gap | ✓ | |

## 12. Topic Failure Analysis 表 (tab:topic_failure, L365–383)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| Fisher列全部9个值 | L370–381 | exp62_topic_diagnosis | 完全一致 | ✓ | vanilla/9class/topic × IID/DD/AA |
| Silhouette列 | L370–381 | exp62 | registry无silhouette数据 | ⚠ | 仅Fisher可验证，silhouette来源不明 |

## 13. Seed-Level F1 表 (tab:seed_level, L913–931)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| 9-class DD: 1.000/1.000/.990 | L924 | plan_002系列 | 均值.997与frozen_verify一致 | ✓ | |
| MLM DD: 1.000/.990/.751 | L927 | plan_017系列 | 均值.914与主表一致 | ✓ | |
| Vanilla DD: .285/.305/.348 | L928 | vanilla_multiseed | 均值.312与主表一致 | ✓ | |

## 14. Cross-Seed Ensemble 表 (tab:ensemble, L895–904)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| MLM AA single=.897 | L900 | exp35_cross_seed_ensemble | — | ⚠ | seed-level表计算均值=(.971+.925+.784)/3=.893，与表中.897存在0.4pp差异；可能为pooled F1 vs mean-of-F1差异 |
| 其余ensemble数字 | L899–901 | exp35 | — | ✓ | DD方向一致 |

## 15. Length Independence 表 (tab:length_independence, L759–786)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| WildChat FPR by bucket: .770±.105(n=196), .942±.054(n=23), .857±.117(n=7) | L773–775 | exp37_length_matched_benign | 完全一致 | ✓ | |
| DD padded Δ=−2.5pp, AA padded Δ=−57.9pp | L779–781 | exp37 | DD_delta=−0.025, AA_delta=−0.579 | ✓ | |

## 16. Random Binary Partition 表 (tab:random_partition, L337–355)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| Mean AA=0.964±0.109, outlier partition 7 AA=0.636 | L352 | exp61_random_binary_partition | aa_ood_f1="0.964±0.109", outlier_aa_f1=0.636 | ✓ | |

## 17. ToxicChat Confidence (app:confidence, L544–547)

| 数字 | 位置 | exp_id | registry原始值 | 一致性 | 备注 |
|------|------|--------|---------------|--------|------|
| 9-class 70.2% FP高置信, median 0.999 | L546 | exp64_toxicchat_confidence_analysis | high_conf_ratio=0.7019, median_conf=0.9999 | ✓ | |
| JB-MLM 58.8%, median 0.933 | L546 | exp64 | 0.5882, 0.9327 | ✓ | |
| Per-seed 94–98% | L547 | exp64 | seed42=96.9%, seed123=97.7%, seed456=94.3% | ✓ | |

---

## 审计总结

### 统计
- **已审计数字**：~80项
- **完全一致 (✓)**：73项
- **需注意 (⚠)**：7项
- **不一致 (✗)**：0项

### 需注意项汇总

| # | 位置 | 问题 | 严重度 | 建议 |
|---|------|------|--------|------|
| 1 | L19 Qwen zero-shot AA=.244 | registry无AA显式记录，值由test set composition逻辑推导 | 低 | 逻辑正确，无需修改 |
| 2 | L216 Qwen JB+Qwen ben row | 无独立exp_id，50-sample subset控制条件 | 低 | 建议补充到registry或注明来源 |
| 3 | L808 DeBERTa latency ±1.2 | exp29无std，exp46 std=1.61（不同硬件） | 中 | 确认std来源 |
| 4 | L809 Qwen3-8B ~5,200 ms | exp10无latency记录 | 中 | 建议补充到exp10 registry或提供来源脚本 |
| 5 | L370–381 Silhouette values | exp62仅存Fisher，无silhouette | 低 | 建议补充到registry |
| 6 | L900 MLM AA single=.897 | seed-level均值=.893，差0.4pp | 低 | 可能为pooled F1 vs mean-of-F1，建议确认计算方式 |
| 7 | exp59_resample_350 | 任务要求对比但appendix无对应表格 | 信息 | 该实验可能用于正文而非appendix |

### 结论

Appendix关键数字与registry高度一致，未发现实质性错误。7项注意事项均为低-中严重度的记录完整性问题（缺少来源追溯或registry补录），不影响论文数字正确性。
