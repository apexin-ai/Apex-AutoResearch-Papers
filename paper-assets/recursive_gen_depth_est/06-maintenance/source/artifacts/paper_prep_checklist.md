# Paper Prep Checklist (2026-05-15)

**Target**: EMNLP ARR May 25 | **Phase 2 写作**: May 18 | **剩余**: 10 天

---

## D002 硬约束

| # | 要求 | 状态 | 缺口 |
|---|------|------|------|
| 1 | ≥4 figures: (a) AUC decay (b) feature trajectory (c) confusion matrix (d) Atlas heatmap | ✅ 完成 | 4/4 已生成，PDF+PNG 双格式 |
| 2 | Bibliography 25+ refs，覆盖 6 领域 | ✅ 完成 | 35 entries，63% 近两年，6 领域全覆盖 |
| 3 | d1-d5 only accuracy（companion metric） | ⚠️ 部分 | baseline_battery 有 acc_3class（排除 d0），但未作为独立 companion metric 明确标注。需在论文中显式报告并标注为 "depth-only accuracy" |
| 4 | Surprisal reference model specification + circularity discussion | ❌ 缺失 | 无任何文件指定 reference model 身份、cross-model LOO 时的处理方式、circularity 讨论。**Phase 2 写作必修** |
| 5 | EDD threshold sensitivity (0.65/0.70/0.75/0.80) | ✅ 完成 | edd_sensitivity.json 含全部 9 cell × 4 threshold，附 heatmap 图 |
| 6 | k-NN inference 完整规格 (k 值、distance metric、sensitivity) | ❌ 缺失 | 服务器上无任何 k-NN 相关代码或结果。需确认是否仍为硬约束——若是，需实现 k-NN baseline 并做 k 值 sensitivity |
| 7 | Cross-strategy 反转：三档分类 + per-strategy d1v2 AUC 表 + z-score 修正 | ⚠️ 部分 | 数据基本齐全（d1v2 反转值 0.13/0.25 已确认），但 **z-score 对 linear model 的恢复效果（0.13→0.68, 0.25→0.83）无实验数据支撑**。cross_strategy_loo_zscore.json 仅含 RF 结果（delta<0.01pp），与 framing 声称的 linear model 恢复矛盾。需运行 LR cross-strategy LOO + z-score 实验 |
| 8 | Limitations: 跨策略部署约束 | ⚠️ 写作待做 | 数据充分（cross_strategy_loo.json），Phase 2 写作时纳入 |

**通过率**: 3/8 完全通过，3/8 部分完成，2/8 缺失

---

## 图表清单

### artifacts/figures/ （论文主图，publication-ready）

| 文件名 | 类型 | 对应 D002 | 备注 |
|--------|------|-----------|------|
| fig1_auc_decay.pdf/png | AUC decay curve w/ EDD threshold | D002-1(a) | 34KB PDF, 303KB PNG |
| fig2_feature_trajectory.pdf/png | Top-5 features × depth, stratified by model | D002-1(b) | 31KB PDF |
| fig3_confusion_matrix.pdf/png | Confusion matrix heatmap | D002-1(c) | 17KB PDF |
| fig4_atlas_heatmap.pdf/png | Atlas feature×depth heatmap grid | D002-1(d) | 25KB PDF |

### artifacts/atlas_v2/ （分析图，可选入论文附录）

| 文件名 | 类型 | 备注 |
|--------|------|------|
| edd_barchart.pdf | EDD bar chart per cell | 可作为 Fig.5 |
| edd_sensitivity_heatmap.pdf | 4-threshold sensitivity | 支撑 D002-5 |
| signal_strength_heatmap.pdf | Signal strength across cells | Atlas 补充 |
| universal_feature_ranking.pdf | Cross-cell feature importance | 支撑 feature universality claim |
| monotonicity_heatmap.pdf | Feature monotonicity scores | Atlas 补充 |
| consistency_heatmap.pdf | Cross-model consistency | 支撑 Claim 2 |
| cross_model_rank_correlation.pdf | Spearman rank correlation | 支撑 feature universality |
| feature_evolution.pdf | Raw feature evolution | Atlas 补充 |
| feature_evolution_normalized.pdf | Normalized feature evolution | Atlas 补充 |
| feature_clustering_pca.pdf | PCA clustering | 可选附录 |
| feature_clustering_t-sne.pdf | t-SNE clustering | 可选附录 |

### results/ （原始结果，非论文图）

| 文件名 | 用途 |
|--------|------|
| confusion_matrix.png | 单 cell 混淆矩阵（旧版） |
| pairwise_auc.json | 单 cell pairwise AUC |
| cross_model_loo.json / _detailed.json | Cross-model LOO 结果 |
| cross_strategy_loo.json | Cross-strategy LOO 结果（含反转数据） |
| cross_strategy_loo_zscore.json | Z-score 修正 RF 结果（delta 极小） |
| binary_pairwise/binary_pairwise_results.json | Pythia binary pairwise d1v2–d4v5，EDD=4 |
| baseline_battery_9cell/ | 9 cell × 4 方法完整结果 |

---

## Bibliography 覆盖

| 领域 | 已有 refs | 要求 refs | 状态 |
|------|-----------|-----------|------|
| Watermarking | Kirchenbauer 2023 | Kirchenbauer | ✅ |
| Model collapse theory | Shumailov 2024, Alemohammad 2024, Dohmatob ×3, Gerstgrasser 2024, Marchi 2024, Drayson 2025, Bakshi 2026, Wang 2026, Falahati 2026, Knowledge Collapse 2025, SIGMA 2026, Mohamed 2025, Synthetic Eggs 2026 | Alemohammad, Dohmatob, Gerstgrasser | ✅ 超额覆盖 |
| Data curation | DSIR 2023, QuRating 2024 | DSIR, QuRating | ✅ |
| Multi-source attribution | Uchendu 2020 | Uchendu 2020 | ✅ |
| Binary detectors | DetectGPT 2023, Sadasivan 2023, Binoculars 2024, Fast-DetectGPT 2024, DivEye 2026, LOKI 2025, GLTR 2019, Pudasaini 2026, Pu 2026 | Binoculars, Fast-DetectGPT | ✅ 超额覆盖 |
| Decoding strategy effects | Holtzman 2020, Finlayson 2024, Garces Arias 2025, Wiher 2022, Basu 2021 | Garces Arias, Holtzman | ✅ |
| Ordinal classification | CORAL 2020, CLOC 2025 | — | ✅ |
| Adjacent tasks | EditLens 2026 | — | ✅ |

---

## 写作启动前 TODO（按优先级排序）

### P0 — 阻塞性缺口（May 15–17 必须完成）

1. **[实验] LR cross-strategy LOO + z-score**：运行 Logistic Regression 版 cross-strategy LOO 实验（含/不含 z-score normalization），验证 paper_framing 中声称的 d1v2 AUC 恢复（GPT-2 XL 0.13→0.68, OLMo 0.25→0.83）。当前仅有 RF 数据（z-score 对 RF 无效 delta<0.01pp），linear model 的恢复效果无数据支撑。**若 linear model z-score 恢复不成立，需修改 paper_framing Claim 2 中的数值**。

2. **[实验/确认] k-NN inference 是否仍为硬约束**：服务器上无任何 k-NN 代码。需确认 D002-6 是否仍有效——若有效，需实现 k-NN classifier（k=3,5,7,11）+ distance metric comparison (euclidean, cosine, manhattan) + sensitivity analysis。

3. **[写作] Surprisal reference model specification**：明确指定 surprisal/perplexity 特征的 reference model（是 GPT-2 XL？是 generator 自身？）、cross-model LOO 时 reference model 如何处理（是否保持固定？换 reference model 时特征分布如何变化？）、circularity 风险讨论。

### P1 — 重要但不阻塞

4. **[写作] d1-only accuracy companion metric**：在 Results 表中显式标注 acc_3class 为 "Depth-Only Accuracy (excl. d0)"，确保 reviewer 看到隔离了 binary detection 的指标。数据已有（baseline_battery_9cell 的 acc_3class 列）。

5. **[写作] Cross-strategy 三档分类**：确保论文不将 nucleus 和 temperature 归为同一 "soft sampling" 类别。采用 nucleus=baseline stable / temperature=signal enhance+reversal risk / topk=signal attenuate+direction consistent。

6. **[写作] Limitations section**：跨策略部署需先验知道目标策略类型，否则 d1/d2 预测可能反转。数据已在 cross_strategy_loo.json。

7. **[图表] 确认 fig1–fig4 质量**：写作前 review 4 张主图，确认 axis labels/font size/color scheme 符合 EMNLP camera-ready 规范。

### P2 — 可选增强

8. **[图表] 选择附录图**：从 atlas_v2/ 的 11 张候选图中选 3–4 张进附录（建议：edd_sensitivity_heatmap, universal_feature_ranking, cross_model_rank_correlation）。

9. **[实验] DCOL v6 状态确认**：检查 DCOL v6 (RoBERTa-large) 是否在运行。成功→Section 5 bonus；失败→negative analysis section。

10. **[数据] 6-class (d0-d5) 分类**：plan_011 结果待定，可扩展 depth range。非阻塞。
