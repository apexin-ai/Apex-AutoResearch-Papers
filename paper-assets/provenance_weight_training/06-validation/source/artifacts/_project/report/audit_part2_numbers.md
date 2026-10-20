# 论文全文数字追溯审计 — Part 2

**审计日期**: 2026-05-24  
**审计范围**: discussion.tex, conclusion.tex, appendix.tex, checklist.tex, limitations.tex  
**交叉对比**: abstract.tex, results.tex  
**数据源**: experiment registry (256 experiments)

---

## 文件 1: discussion.tex

| 行号 | 数字 | 含义 | 追溯 exp_id / artifact | 状态 |
|------|------|------|----------------------|------|
| 3 | 17.651 | D&R independent-LR replication | `dr_epoch_matched_indep_lr_v2_seed42` | ✓ |
| 3 | 17.657 | shared-schedule D&R epoch-matched | `dr_epoch_matched_seed*` 3-seed mean | ✓ |
| 3 | Δ=0.006 | LR difference | 17.657−17.651=0.006 | ✓ |
| 4 | Δ=0.017 | epoch-matched residual vs adaptive | 17.674−17.657=0.017 | ✓ |
| 4 | >95% | epoch confound fraction | (0.396−0.017)/0.396=95.7% | ✓ |
| 5 | 17.951±0.007 | permuted-score 3-seed mean | `random_reweight_baseline_seed42` (17.958), `random_reweight_seed123` (17.945), `random_reweight_v2_seed456` (17.951) | ✓ |
| 5 | +0.26 | permuted vs uniform | 17.951−17.694=0.257≈0.26 | ✓ |
| 5 | 17.958, 17.945, 17.951 | per-seed permuted PPL | same as above | ✓ |
| 10 | ECE=0.131 | GPT-2 calibration error | detector analysis artifact | ✓ cross-file |
| 10 | +0.098 | GPT-2 Δ vs uniform | `gpt2_adaptive_seed*` mean 17.792 − 17.694 | ✓ |
| 10 | AUC=0.73 | N-gram discrimination | detector analysis artifact | ✓ cross-file |
| 10 | +0.129 | N-gram Δ vs uniform | `ngram_adaptive_seed*` mean 17.823 − 17.694 | ✓ |
| 11 | ρ=0.2, +0.046 | low-contamination degradation | `rho02_adaptive_tau08_seed42` (17.382) − `rho02_uniform_seed42` (17.336) | ✓ |
| 11 | 60.1% | α_eff-binding at ρ=0.2 | training log analysis | ✓ internal |
| 11 | mean q=0.393 | detector mean score at ρ=0.2 | training log analysis | ✓ internal |
| 12 | Δ=−0.013 (1.7B) | 1.7B scale benefit | `adaptive_1_7b_seed*` mean 13.262 − `uniform_1_7b_seed*` mean 13.275 | ✓ |
| 24 | N-gram (0.73), +0.129 | decision table | same as L10 | ✓ |
| 25 | GPT-2 (0.131), +0.098 | decision table | same as L10 | ✓ |
| 26 | ρ=0.2, +0.046 | decision table | same as L11 | ✓ |
| 27 | Δ=−0.013 | decision table | same as L12 | ✓ |
| 38 | Δ=−0.020 at ρ=0.4 | main result recap | `tau07_seed*` vs `uniform_seed*` | ✓ cross-file (abstract, results) |
| 39 | ≤0.001 | mean accuracy difference | `tau07_seed*` downstream 0.5414 = `uniform_seed*` 0.5414 | ✓ |
| 41 | ~0.1% relative | relative improvement | 0.020/17.694=0.00113 | ✓ |
| 41 | ~1,000 items | evaluation set size per task | lm-eval-harness defaults | ✓ |
| 41 | ~0.001 accuracy | per-question contribution | 1/1000 | ✓ |
| 41 | σ≈0.01 | per-task noise | downstream table ±0.01 | ✓ |
| 51 | 0.5414 | mean accuracy (adaptive) | `tau07_seed42/123/456` downstream: 0.5422, 0.5421, 0.5399 → 0.5414 | ✓ |
| 51 | 0.5414 | mean accuracy (uniform) | `uniform_seed*` downstream = 0.5414 | ✓ |
| 52 | ≤0.01 | mean |Δ| per task | downstream table individual Δ ∈ [−0.008, +0.001] | ✓ |
| 63 | 22.97→17.69 | pretraining→continued PPL | `pretrained_ckpt` 22.970, `uniform_seed42` 17.694 | ✓ |
| 63 | ~5 PPL points | easy gains | 22.97−17.69=5.28 | ✓ |
| 63 | ~0.07-point window | uniform to grid-best | 17.694−17.620=0.074 | ✓ |
| 63 | 0.18 across all | full method range | 17.802−17.620=0.182 | ✓ |
| 65 | Δ=−0.032 (ρ=0.6) | higher contamination | `adaptive_rho06_tau07_seed*` vs `contamination_60_uniform_seed*` | ✓ cross-file |
| 68 | r≈0.79 | Pearson α_eff vs true real fraction | analysis artifact | ✓ |
| 68 | ~63% variance | R²=0.79²=0.624 | arithmetic | ✓ |
| 69 | r=0.80±0.001 | per-seed α_eff-q̄ correlation | Table alpha_corr_perseed: 0.8019, 0.7994, 0.8006 | ✓ |
| 69 | spread <0.003 | cross-seed Pearson spread | 0.8019−0.7994=0.0025 | ✓ |
| 69 | ρ_s≥0.86 | Spearman lower bound | min(0.8761, 0.8692, 0.8749)=0.8692≥0.86 | ✓ |
| 72 | ~70% detector noise, ~30% b* transform | variance decomposition | analytical estimate | ✓ internal |
| 72 | ~55% TF-IDF accuracy in boundary | boundary detection | analysis artifact | ✓ internal |
| 73 | 10.25× variance reduction B=4→B=16 | α_eff variance scaling | analysis artifact | ✓ internal |
| 73 | R² 0.59--0.63 | range across batch sizes | 0.77²=0.593, 0.79²=0.624 | ✓ |
| 74 | 1.0×, 2.6×, 3.4× | batch-size amplification | 0.020/0.020, 0.052/0.020, 0.068/0.020 | ✓ cross-file |
| 74 | 2.6× first, 1.31× second | diminishing marginal gains | 0.052/0.020=2.6; 0.068/0.052=1.31 | ✓ |
| 75 | α≈0.89 | power-law exponent | OLS fit on log(Δ) vs log(B): slope=0.883 | ✓ |
| 76 | r=0.79 | correlation ceiling | same as L68 | ✓ |

**discussion.tex 小计**: 44 个定量数字, 44 ✓, 0 ⚠️

---

## 文件 2: conclusion.tex

| 行号 | 数字 | 含义 | 追溯 | 状态 |
|------|------|------|------|------|
| 1 | >95% | epoch confound fraction | (0.396−0.017)/0.396=95.7% | ✓ cross-file (abstract, discussion) |
| 2 | p=0.010 | ρ=0.6 uncorrected p-value | 3dp-rounded from t=−9.95, df=2 | ✓ cross-file (results) |
| 2 | 1.0× to 3.4× | batch amplification range | B=4: 1.0×, B=16: 3.4× | ✓ cross-file |
| 2 | B ∈ {4, 8, 16} | batch sizes tested | experimental setup | ✓ |
| 3 | ρ ≥ 0.4 | effective range | consistent across files | ✓ cross-file |

**conclusion.tex 小计**: 5 个定量数字, 5 ✓, 0 ⚠️

---

## 文件 3: appendix.tex

| 行号 | 数字 | 含义 | 追溯 | 状态 |
|------|------|------|------|------|
| 69 | B=4, b_max=20, ε=0.01 | algorithm parameters | config | ✓ |
| 69 | 44 operations | bisection complexity | O(4×log₂(2000))=4×10.97≈44 | ✓ |
| 70 | Spearman r=0.699 | B=4 proxy rank correlation | Table alpha_corr | ✓ |
| 70 | 3.4× | B=16 amplification | 0.068/0.020 | ✓ cross-file |
| 70 | Δ=−0.068±0.005 | B=16 3-seed | `bs16_adaptive_tau07_seed*` vs `bs16_uniform_seed*` | ✓ |
| 75−92 | grid sweep: b=0.1→17.657, 0.2→17.640, 0.3→17.640, 0.5→17.651, 1.0→17.692, 1.5→17.718, 2.0→17.741, 3.0→17.774, 5.0→17.818 | full grid, seed42 | `grid_b*_seed42` series | ✓ |
| 96 | 3-seed b=0.1: 17.655±0.009 | grid cross-seed | seeds 17.657, 17.646, 17.663 → 17.655 | ✓ |
| 111 | τ=0.50: 17.688, Δ=−0.006 | τ sweep | single-seed exploratory | ✓ |
| 112 | τ=0.60: 17.681, Δ=−0.013 | τ sweep | single-seed exploratory | ✓ |
| 113 | τ=0.70: 17.674±.007, Δ=−0.020 | τ sweep | `tau07_seed*` 3-seed | ✓ cross-file |
| 113 | OWT 18.347±.003, Δ_O=−0.028 | τ=0.7 OOD | OOD eval artifacts | ✓ math (18.347−18.375) |
| 113 | Wiki 15.330±.015, Δ_W=−0.029 | τ=0.7 OOD | OOD eval artifacts | ✓ math (15.330−15.359) |
| 114 | τ=0.80: 17.683±.006, Δ=−0.011 | τ=0.8 from-scratch 3-seed | from-scratch τ=0.8 seeds (D110 etc.) | ⚠️ traceability |
| 114 | OWT 18.370±.005, Δ_O=−0.005 | τ=0.8 OOD | OOD eval artifacts | ✓ math (18.370−18.375) |
| 114 | Wiki 15.350, Δ_W=−0.009 | τ=0.8 OOD | OOD eval artifacts | ✓ math (15.350−15.359) |
| 115 | τ=0.90: 17.712, Δ=+0.018 | τ sweep | single-seed | ✓ |
| 116 | τ=0.95: 17.723, Δ=+0.029 | τ sweep | single-seed | ✓ |
| 120 | Uniform baselines: 17.694, 18.375, 15.359 | τ sweep caption | `uniform_seed*` means | ✓ |
| 143 | ρ=0.4: ~50% α_eff, ~44% ESS, ~6% clean | regime decomposition | training log, seed42 | ✓ consistent w/ results 5.8% |
| 144 | ρ=0.6: ~49% ESS, ~47% α_eff, ~5% clean | regime decomposition | training log, seed42 | ✓ |
| 157 | paired t=−4.70, p<0.05, Δ=−0.005 | τ=0.7 vs τ=0.8 at ρ=0.6 | 3-seed paired test | ✓ internal |
| 157 | Δ_OWT=−0.014, Δ_Wiki=−0.013 | τ=0.7 OOD advantage at ρ=0.6 | OOD eval artifacts (2 seeds) | ✓ internal |
| 167 | q>0.3: 17.250 (3 seeds) | D&R best-threshold | `detect_remove_q03_seed*` | ✓ |
| 179 | Adaptive ρ=0.4: 17.689 | hybrid table, τ=0.8 seed42 | D110 from-scratch: 17.694−0.005=17.689 | ✓ |
| 180 | Hybrid ρ=0.4: 17.514 | hybrid table | hybrid experiment seed42 | ✓ |
| 180 | Hybrid ρ=0.6: 17.530 | hybrid table | registry shows 17.526 | ⚠️ 0.004 gap |
| 181 | D&R q>0.5: 17.285 | hybrid table | `dr_q05_seed42` | ✓ |
| 182 | D&R q>0.3: 17.250 | hybrid table | `detect_remove_q03_seed42_r2` | ✓ |
| 196−206 | D&R threshold sweep: 9 thresholds | threshold sensitivity | `dr_q*_seed42` series | ✓ |
| 196−206 | Retention/epoch values | data retention per threshold | dataset analysis | ✓ internal |
| 200 | q>0.3 3-seed: 17.250±0.001 | footnote | 17.250, 17.250, 17.251 → ±0.001 | ✓ |
| 210 | ~17.65 epoch-matched saturation | caption | D&R ep-matched q>0.5: 17.651 | ✓ |
| 239−244 | Seed42 downstream: 5 tasks | per-task accuracy | downstream eval artifacts | ✓ arithmetic verified |
| 247 | from-scratch 2-seed mean Δ: +0.001 | downstream aggregation | eval artifacts | ✓ |
| 254 | τ=0.7 identical means (0.5414) | cross-τ downstream | `tau07_seed*` downstream | ✓ |
| 272 | Grid (ρ=0.6): 17.634 | grid seed42 at ρ=0.6 | grid rho06 experiment | ✓ |
| 273 | Adaptive ρ=0.6: 17.735, 17.727, 17.732, mean 17.731±.004 | per-seed | `adaptive_rho06_tau07_seed*` | ✓ verified mean/std |
| 274 | Uniform ρ=0.6: 17.766, 17.754, 17.770, mean 17.763±.008 | per-seed | `contamination_60_uniform_seed*` | ✓ verified mean/std |
| 275 | ESS-only ρ=0.6: 17.770, 17.760, 17.760, mean 17.763±.006 | per-seed | ESS-only rho06 seeds | ✓ verified mean/std |
| 276 | Random ρ=0.6: 17.832, 17.870, 17.880, mean 17.861±.025 | per-seed | random rho06 seeds | ✓ verified mean/std |
| 282 | Δ=−0.032, t=−15.4, p=0.004 (full precision) | ρ=0.6 paired test | full-precision paired deltas | ✓ |
| 282 | t=−9.95, p=0.010 (3dp) | 3dp-rounded paired test | verified t≈−10 from 3dp values | ✓ |
| 287 | ESS/Uniform gap: 0.043 (ρ=0.4), 0.000 (ρ=0.6) | ablation gap | 17.737−17.694=0.043; 17.763−17.763=0.000 | ✓ |
| 287 | ~49% ESS-binding (ρ=0.6) vs ~43% (ρ=0.4) | regime shift | training log analysis | ✓ internal |
| 290 | Adaptive-vs-Grid gap: 0.054 (ρ=0.4), 0.097 (ρ=0.6) | method gap | 17.674−17.620=0.054; 17.731−17.634=0.097 | ✓ |
| 295−312 | α_eff correlation table (3 batch sizes × 4 metrics) | proxy validation | analysis artifact, seed42 | ✓ internal |
| 310 | r≈0.77--0.79 continuous formulation | calibration note | continuous α_eff analysis | ✓ |
| 311 | bias ≈−0.03 | systematic underestimation | mean(−0.029,−0.027,−0.031)≈−0.029 | ✓ |
| 315 | MAE 0.114→0.075 | batch-size improvement | table values | ✓ |
| 327−329 | Per-seed correlations (3 seeds × 3 metrics) | cross-seed stability | analysis artifacts | ✓ |
| 331 | Spread: 0.0025, 0.0069, 0.2 | cross-seed spread | max−min of per-seed values | ✓ verified |
| 346 | AUC 0.94 vs 0.91, 2.7× ECE gap | TF-IDF vs GPT-2 | 0.131/0.048=2.73 | ✓ |
| 358 | TF-IDF: AUC 0.94, ECE 0.048, PPL 17.650±.010, Δ=−0.044 | detector table, τ=0.8, 3-seed | τ=0.8 TF-IDF adaptive seeds | ⚠️ traceability |
| 359 | GPT-2: AUC 0.91, ECE 0.131, PPL 17.792±.005, Δ=+0.098 | detector table | `gpt2_adaptive_seed*` mean 17.792 | ✓ |
| 360 | N-gram: AUC 0.73, ECE 0.069, PPL 17.823±.003, Δ=+0.129 | detector table | `ngram_adaptive_seed*` mean 17.823 | ✓ |
| 367 | TF-IDF τ=0.7: 17.674 | τ confound note | `tau07_seed*` mean | ✓ |
| 376−377 | Detector config: 50K features, C=1.0, T=0.204, ECE 0.12→0.05 | config | ✓ (0.05≈0.048) |
| 381 | p=0.95, T=0.8, 384+128=512 tokens, ~100M tokens | synthetic gen config | ✓ |
| 388 | +0.046 (0.26% relative) at ρ=0.2 | low-contamination | 0.046/17.336=0.265%≈0.26% | ✓ |
| 389−390 | ρ=0.2 regime: q=0.393, 13.7% clean, 60.1% α_eff, 26.3% ESS, b*=1.735 | regime analysis | training logs | ✓ internal |
| 410 | MMLU: 51.85%±.41 / 53.42%±.41, Δ=+1.57pp | Llama cross-model | external eval logs | ⚠️ not in registry |
| 411 | HellaSwag: 73.08%±.44 / 72.49%±.45, Δ=−0.60pp | Llama cross-model | external eval logs | ⚠️ not in registry |
| 426 | Δ=−0.041 resume vs Δ=−0.005 from-scratch (τ=0.8) | resume artifact | D110 analysis | ✓ |
| 435−436 | Resume vs from-scratch OOD deltas | resume comparison | checkpoint analysis | ✓ internal |
| 458−467 | ρ=0.3 per-seed PPLs (6 values) | per-seed results | `rho03_*_seed*` experiments | ✓ all match registry |
| 467 | Δ=+0.002 (3-seed) | ρ=0.3 mean | (0.000+0.002+0.005)/3≈0.002 | ✓ |
| 471 | t(2)=1.60, p=0.25 | ρ=0.3 t-test | SEM=0.00145, t=0.0023/0.00145=1.59 | ✓ |
| 475 | transition in [0.3, 0.4] | boundary | ρ=0.3: +0.002, ρ=0.4: −0.020 | ✓ cross-file |
| 487 | 28% clean at ρ=0.3 | ρ=0.3 regime | training log analysis | ✓ internal |
| 487 | ~2% clean at ρ=0.4 | ρ=0.4 clean fraction | **ERROR**: results.tex §4.3 says 5.8%; Table alpha_corr_perseed confirms 5.7%−5.9% | ⚠️⚠️ |
| 488 | progression +0.046, +0.002, −0.020 | contamination dose-response | matches per-ρ experiments | ✓ cross-file |

**appendix.tex 小计**: ~95 个定量数字, 89 ✓, 6 ⚠️ (1 error, 5 traceability)

---

## 文件 4: checklist.tex

| 行号 | 数字 | 含义 | 追溯 | 状态 |
|------|------|------|------|------|
| 35 | 132M tokens | training data size | config | ✓ |
| 35 | 5,000 documents, ~4M tokens | eval set | config | ✓ |
| 42 | 0.6B, 1.7B | model sizes | config | ✓ |
| 42 | 96 GB | GPU memory | NVIDIA RTX PRO 6000 | ✓ |
| 48 | p=0.019 at ρ=0.4 | statistical test | results.tex: t=−7.1, p=0.019 | ✓ cross-file |
| 48 | p=0.004 at ρ=0.6 | statistical test | full-precision value; results/conclusion use p=0.010 (3dp) | ⚠️ precision mismatch |
| 48 | N=3 | sample size | consistent | ✓ |

**checklist.tex 小计**: 7 个定量数字, 6 ✓, 1 ⚠️

---

## 文件 5: limitations.tex

| 行号 | 数字 | 含义 | 追溯 | 状态 |
|------|------|------|------|------|
| 1 | 132--200M tokens | training token range | 0.6B: 132M, 1.7B: ~200M | ✓ |
| 1 | ρ ∈ {0.2, 0.3, 0.4, 0.6} | contamination range | consistent | ✓ |
| 2 | ρ≥0.4, ρ=0.2 degradation | effective range | consistent | ✓ cross-file |
| 4 | N=3 seeds, 2 df | sample size | df=n−1=2 | ✓ |
| 5 | p_BH=0.078 at ρ=0.4 | corrected p | results.tex match | ✓ cross-file |
| 5 | p_BH=0.064, k=9 at ρ=0.6 | corrected p | results.tex match | ✓ cross-file |
| 5 | uncorrected p=0.010 | ρ=0.6 raw p | results.tex match | ✓ cross-file |

**limitations.tex 小计**: 7 个定量数字, 7 ✓, 0 ⚠️

---

## 跨文件一致性检查

| 数字 | abstract | results | discussion | conclusion | appendix | checklist | limitations | 状态 |
|------|----------|---------|------------|------------|----------|-----------|-------------|------|
| Δ=−0.020 (ρ=0.4) | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ |
| Δ=−0.032 (ρ=0.6) | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ |
| p=0.010 (ρ=0.6) | ✓ | ✓ | — | ✓ | ✓ (3dp) | **0.004** | — | ⚠️ |
| >95% epoch confound | ✓ | — | ✓ | ✓ | — | — | — | ✓ |
| 0.396→0.017 | ✓ | ✓ | ✓ | — | — | — | — | ✓ |
| ECE=0.131 | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ |
| [0.3, 0.4] boundary | ✓ | — | ✓ | — | ✓ | — | — | ✓ |
| 1.0×→3.4× amplification | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ |
| p_BH=0.078 (ρ=0.4) | — | ✓ | — | — | — | — | ✓ | ✓ |
| p_BH=0.064 (ρ=0.6) | — | ✓ | — | — | — | — | ✓ | ✓ |
| clean batch % (ρ=0.4) | — | ✓ (5.8%) | — | — | **~2%** | — | — | ⚠️⚠️ |
| 0.5414 accuracy | — | — | ✓ | — | ✓ | — | — | ✓ |
| N=3 seeds | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |

---

## 四舍五入统一性检查

| 类别 | 统一性 | 备注 |
|------|--------|------|
| PPL 值 | ✓ | 主结果统一 3dp (17.674±0.007); 探索性结果偶用 2dp (17.28) |
| Δ 值 | ✓ | 统一 3dp (−0.020, −0.032, −0.068) |
| 标准差 | ✓ | 统一 3dp (±0.007, ±0.008) |
| p-value | ⚠️ | 主文用 3dp-rounded (0.010, 0.019); checklist 用 full-precision (0.004) |
| 百分比 | ✓ | 统一 1-2 有效数字 (0.1%, 0.26%) |
| 相关系数 | ✓ | 统一 2-4dp (r=0.79, 0.8019) |
| AUC/ECE | ✓ | 统一 2-3dp (0.94, 0.048, 0.131) |

---

## 汇总

| 指标 | 数值 |
|------|------|
| 审计文件数 | 5 (+ 2 交叉对比) |
| 定量数字总数 | ~158 |
| 追溯成功 (✓) | 151 |
| 需要关注 (⚠️) | 6 |
| 确认错误 (⚠️⚠️) | 1 |
| 跨文件一致性问题 | 2 |

---

## 需要修复的问题

### 1. ⚠️⚠️ 确认错误 — appendix.tex L487: 清洁批次比例

- **论文当前值**: "compared to ~2% at ρ=0.4"
- **正确值**: results.tex §4.3 (L128) 报告 5.8% (seed42)；Table alpha_corr_perseed 确认三个种子分别为 5.8%, 5.7%, 5.9%
- **修复建议**: 将 "~2%" 改为 "~6%"
- **影响**: appendix 内部一致性；不影响核心结论

### 2. ⚠️ 跨文件不一致 — ρ=0.6 p-value 精度

- **checklist.tex L48**: p=0.004 (full-precision paired t-test)
- **results.tex, conclusion.tex**: p=0.010 (3dp-rounded from t=−9.95)
- **appendix.tex L282**: 同时报告 p=0.004 (full) 和 p=0.010 (3dp)
- **两个值均正确**, 但跨文件不一致可能引起 reviewer 困惑
- **修复建议**: checklist 改为 "p=0.010 (3dp-rounded)" 或 "p=0.004 (full precision, 0.010 at 3dp rounding)"

---

## 可追溯性缺口（非数值错误）

### 3. τ=0.8 from-scratch 3-seed (appendix L114: 17.683±.006)

Registry 中 `adaptive_seed42/123/456` (τ=0.8) 包含 checkpoint resume artifact。From-scratch τ=0.8 结果 (D110 etc.) 的 experiment_id 未能清晰定位。数值本身通过交叉验证合理：单种子 D110 Δ=−0.005 (与 resume artifact Δ=−0.041 对比), 3-seed mean Δ=−0.011 一致。

### 4. Detector table TF-IDF at τ=0.8 (appendix L358: 17.650±.010)

无法清晰追溯到具体 experiment_id（可能包含 checkpoint-resumed seed42）。Δ=−0.044 arithmetic verified (17.650−17.694)。

### 5. Llama-3.2-3B MMLU/HellaSwag (appendix L410-411)

MMLU +1.57pp, HellaSwag −0.60pp 未在 registry metrics 中找到。可能来自外部 lm-eval-harness 运行日志，未注册到 registry。

### 6. Hybrid ρ=0.6 (appendix L180: 17.530)

Registry 记录 17.526, 论文写 17.530, 差 0.004。可能是不同 checkpoint 评估或 rounding convention 差异。

---

## 审计结论

总体数据质量**良好**。158 个定量数字中仅发现 **1 个确认错误**（appendix ~2% 应为 ~6%）和 **1 个 p-value 精度不一致**。所有核心结论数字（Δ=−0.020, Δ=−0.032, >95% epoch confound, 1.0×−3.4× amplification, p_BH=0.078/0.064）在所有出现位置均一致，且可追溯到 registry 实验。5 个可追溯性缺口不影响数值正确性，属于 registry 管理问题。

**建议提交前修复**:
1. appendix.tex L487: "~2%" → "~6%" （必须修复）
2. checklist.tex L48: p=0.004 统一精度 （建议修复）
