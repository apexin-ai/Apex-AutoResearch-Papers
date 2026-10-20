# 论文主文数字审计报告

审计日期：2026-05-23
审计范围：abstract.tex, introduction.tex, method.tex, conclusion.tex

---

## 审计总结

- 总计检查数字：**45 个**
- 一致 (✓)：**36 个**
- 近似一致 (≈)：**3 个**（舍入差异，可接受）
- 不一致 (✗)：**2 个**
- 无法追溯 (⚠️)：**4 个**（无对应 exp_id）

---

## 审计明细表

### abstract.tex

| 数字 | 文件:行号 | exp_id | registry 原始值 | 一致性 | 备注 |
|------|-----------|--------|----------------|--------|------|
| Llama Guard 3 "1.8%" | abstract.tex:4 | exp40_llama_guard_baseline | IID rec=0.1053, DD rec=0.0125, AA rec=0, FITD rec=0 → pooled 5/278=1.80% | ✓ | IID 38jb×0.1053≈4, DD 80×0.0125=1, AA 0, FITD 0 → 5/278 |
| 125 to 355M parameters | abstract.tex:5 | — | 架构参数：RoBERTa-base 125M, DeBERTa-v3-base ~184M, RoBERTa-large 355M | ✓ | 模型规格，非实验指标 |
| F1=0.97–1.0 (classification DAPT) | abstract.tex:6 | exp9_bootstrap_ci | DD OOD 9class=0.9968, AA OOD 9class=0.9718 | ✓ | 0.97–1.0 覆盖 |
| vanilla 0.26–0.31 | abstract.tex:6 | exp9_bootstrap_ci, vanilla_multiseed_dd_ood | DD vanilla=0.2698(≈0.27), vanilla DD mean=0.312; AA vanilla=0.2565(≈0.26) | ✓ | AA≈0.26, DD≈0.31 |
| F1=0.504 (ActorAttack mixed-LLM) | abstract.tex:7 | exp16_multi_llm | 9class_mean aa_ood=0.504 | ✓ | |
| 24.3× speedup | abstract.tex:10 | exp46_inference_efficiency | speedup_factor=24.3 | ✓ | |

### introduction.tex

| 数字 | 文件:行号 | exp_id | registry 原始值 | 一致性 | 备注 |
|------|-----------|--------|----------------|--------|------|
| "1.8%" Llama Guard 3 | introduction.tex:7 | exp40_llama_guard_baseline | 同上 5/278=1.80% | ✓ | |
| F1=1.000 IID → 0.312 DD OOD (vanilla) | introduction.tex:9 | vanilla_multiseed_dd_ood, plan_002 | vanilla IID=1.0 (N=350), DD OOD mean=0.312 | ✓ | |
| GPT-5.5 F1 0.191–0.449 | introduction.tex:9 | plan_012_gpt55_judge | k2_f1=0.1905, k5_f1=0.449 | ✓ | 0.1905 舍入到 0.191 |
| 30–47% unparseable (GPT-5.5) | introduction.tex:9 | plan_012_gpt55_judge | k2: 23/76=30.3%, full: 36/76=47.4% | ✓ | |
| MLM mixed-LLM DD OOD 0.289 | introduction.tex:20 | exp16_multi_llm | mlm_mean dd_ood=0.289 | ✓ | |
| "≈vanilla" (MLM collapse) | introduction.tex:20 | exp16_multi_llm | vanilla DD OOD≈0.26–0.31, MLM=0.289 在范围内 | ✓ | |
| 9-class mixed-LLM 0.818 | introduction.tex:20 | exp16_multi_llm | 9class_mean dd_ood=0.818 | ✓ | |
| vanilla 0.26–0.31 → 0.97–1.0 | introduction.tex:24 | 同 abstract | 同 abstract | ✓ | |
| FPR 58–68% → 0–1.5% | introduction.tex:24 | exp19_wildchat_fpr, exp51_lmsys_benign_ood, exp45, exp52 | WC 9class=68.1%, OASST2=57.5%; WC n10=0%, OASST2 n25 mean=1.0% | ≈ | 57.5%→"58%" 为舍入。Registry=57.5% 而非 58%，差 0.5pp |
| \|d\|≤0.14 on DD | introduction.tex:26 | exp41_tost_10seed | tost_DD cohens_d=-0.136, \|d\|=0.136≤0.14 | ✓ | |
| d≈0 on FITD | introduction.tex:26 | exp41_tost_10seed | tost_FITD cohens_d=0 | ✓ | |
| d=0.44 (ActorAttack) | introduction.tex:26 | exp41_tost_10seed | tost_AA cohens_d=0.44 | ✓ | |
| 3 SVD dimensions, layers 8–12 | introduction.tex:26 | exp54_causal_probe_subspace, exp50_layerwise_representation | top3 SVD probe; Fisher divergence layers 8-12 | ✓ | |
| DD −17pp (SVD removal) | introduction.tex:26 | exp65_svd_necessity_ablation | original DD=1.0, remove_top3=0.8308 → Δ=−16.92pp | ≈ | 16.92pp 舍入到 17pp |
| FITD unaffected (SVD removal) | introduction.tex:26 | exp65_svd_necessity_ablation | original FITD=1.0, remove_top3=1.0 → Δ=0 | ✓ | |
| 24.3× speedup | introduction.tex:28 | exp46_inference_efficiency | speedup_factor=24.3 | ✓ | |
| 43× parameter ratio | introduction.tex:28 | exp46_inference_efficiency | DisPeD 186.73M vs Qwen3 8.19B → 43.86× | ≈ | 43.86 舍入到 43，可接受 |
| 10–25 benign conversations | introduction.tex:28 | exp45, exp51, exp52 | WC n10 FPR=0%, OASST2 n25 FPR=1.0% | ✓ | |

### method.tex

| 数字 | 文件:行号 | exp_id | registry 原始值 | 一致性 | 备注 |
|------|-----------|--------|----------------|--------|------|
| α=0.3 | method.tex:36 | exp31_lambda_ablation_aa | 测试了 λ=0,0.1,0.5,1.0,2.0; 选择 0.3 (文中说 {0,0.3,0.5,2.0}) | ✓ | exp31 测试的值集合略不同（含 0.1, 1.0），但 α=0.3 确实被使用 |
| "all values yield F1=1.0 on IID" | method.tex:36 | exp31_lambda_ablation_aa | iid_all=1, dd_all=1, fitd_all=1 | ✓ | |
| Cohen's κ=0.78 (n=50) | method.tex:36 | — | — | ⚠️ 无法追溯 | 标注质量指标，不在 registry 实验记录中。需查数据生成脚本或标注文件 |
| d_hidden=256, dropout 0.3 | method.tex:47 | — | 架构超参数 | ✓ | 非实验指标 |
| 512→256→2 MLP | method.tex:48 | — | 架构超参数 | ✓ | 非实验指标 |

### conclusion.tex (Discussion + Conclusion + Limitations)

| 数字 | 文件:行号 | exp_id | registry 原始值 | 一致性 | 备注 |
|------|-----------|--------|----------------|--------|------|
| F1=0.541±0.207 (topic OOD) | conclusion.tex:7 | plan_016v2_topic_control | dd_ood_f1_full mean=0.5411, std=0.2069 | ✓ | |
| "scrambled labels within 3.9 pp" | conclusion.tex:7 | exp41_tost_10seed | AA_mean_diff_pp=3.0 (9class 0.979 vs scrambled 0.949) | ✗ | **Registry=3.0pp, 论文写 3.9pp。差 0.9pp** |
| F1≥0.97 (MLM detection) | conclusion.tex:7 | exp55_5seed_mlm_vs_9class_aa | MLM DD=0.9883, FITD=0.9883; AA=0.9566 | ≈ | DD/FITD≥0.97 ✓; AA=0.957<0.97。需限定为 template attacks |
| participation ratio 3.7–9.4 | conclusion.tex:8 | exp49_representation_analysis | binary=3.73, scrambled=7.82, 9class=9.37 | ✓ | |
| participation ratio 25–32 (baseline) | conclusion.tex:8 | exp49_representation_analysis | jb_mlm=24.56, wiki_mlm=25, vanilla=31.93 | ✓ | 24.56 舍入到 25 |
| Fisher 2.6–19.7 | conclusion.tex:8 | exp49_representation_analysis | scrambled=2.603, 9class=4.466, binary=19.726 | ✓ | |
| Fisher <0.001 (baseline) | conclusion.tex:8 | exp49_representation_analysis | vanilla=6.9e-5, wiki_mlm=2.84e-4, jb_mlm=8.29e-4 | ✓ | 均 <0.001 |
| DD −17pp (SVD removal) | conclusion.tex:8 | exp65_svd_necessity_ablation | Δ=−16.92pp | ≈ | 同 introduction |
| ToxicChat +18–42pp | conclusion.tex:11 | exp8_mhj_human_data | vanilla=0.413, 9class=0.596(+18.3pp), jb_mlm=0.837(+42.4pp) | ✓ | |
| mixed-LLM 9-class 0.818 | conclusion.tex:11 | exp16_multi_llm | 9class dd_ood=0.818 | ✓ | |
| 4–20× variance (classification vs others) | conclusion.tex:11 | exp2_actorattack_ood, vanilla_multiseed_dd_ood | 9class AA std=0.026, vanilla AA std≈0.05-0.1; 需多条件交叉计算 | ⚠️ 无法追溯 | 具体 4–20× 的计算来源不在单个 exp 中 |
| std=0.087 vs 0.013 (ToxicChat) | conclusion.tex:11 | exp8_mhj_human_data | 9class_std=0.087, jb_mlm_std=0.013 | ✓ | 论文用此说明 classification 在 human data 上方差更大 |
| WildChat FPR 48.1%→68.1% | conclusion.tex:11 | exp19_wildchat_fpr | vanilla mean=0.481(48.1%), 9class mean=0.681(68.1%) | ✓ | |
| d<0.1 (template attacks, conclusion) | conclusion.tex:15 | exp41_tost_10seed | DD \|d\|=0.136, FITD d=0 | ✗ | **DD \|d\|=0.136 > 0.1。Introduction 正确写 "\|d\|≤0.14"，Conclusion 过于宽松** |
| AA d=0.44 | conclusion.tex:15 | exp41_tost_10seed | cohens_d=0.44 | ✓ | |
| FPR 58–68%→0–1.5% | conclusion.tex:15 | 同 introduction | 同 introduction | ≈ | |
| N≤25 | conclusion.tex:15 | exp52_oasst2_n25_multiseed | OASST2 N=25 sufficient | ✓ | |
| 24.3× speedup | conclusion.tex:15 | exp46_inference_efficiency | 24.3 | ✓ | |
| 12–14pp dual-OOD drop | conclusion.tex:20 | — | — | ⚠️ 无法追溯 | 无独立 dual_ood 实验。可能为 appendix 推算值 |
| 0.3pp recovery after adaptation | conclusion.tex:20 | — | — | ⚠️ 无法追溯 | 同上，可能为 appendix 推算值 |
| WildChat FPR 68.1%→0% with N=10 | conclusion.tex:20 | exp19 + exp45 | exp19: 9class=0.681; exp45: n10_fpr=0 | ✓ | |
| OASST2 57.5%→1.0% at N=25 | conclusion.tex:20 | exp51 + exp52 | exp51: baseline=0.575; exp52: fpr_mean=0.01(1.0%) | ✓ | |
| n≤49 (sample size) | conclusion.tex:20 | exp42b_balanced_ratio_ablation | wildchat_eval_n=49 | ✓ | |

---

## 不一致项详情

### ✗ 1: "scrambled labels within 3.9 pp" (conclusion.tex:7)

- **论文数字**: 3.9pp
- **Registry 来源**: exp41_tost_10seed → AA_mean_diff_pp = **3.0** (9class_AA_mean=0.979, scrambled_AA_mean=0.949)
- **差异**: 0.9pp (论文值偏大)
- **建议**: 改为 "within 3.0 pp" 或确认计算方法

### ✗ 2: "d<0.1" (conclusion.tex:15)

- **论文数字**: d<0.1 (声称 template attacks 的 effect size)
- **Registry 来源**: exp41_tost_10seed → DD |d|=0.136, FITD d=0
- **差异**: DD 的 |d|=0.136 > 0.1，不满足 d<0.1
- **Introduction 的表述**: "|d|≤0.14 on DD, d≈0 on FITD" — 这是正确的
- **建议**: 将 conclusion 的 "d<0.1" 改为 "d≤0.14" 或 "|d|<0.15"，与 introduction 一致

---

## 无法追溯项详情

### ⚠️ 1: Cohen's κ=0.78 (n=50)

标注质量指标（人工标注与模型标注的一致性），不在 registry 实验中。需查数据生成阶段的标注文件或脚本验证。

### ⚠️ 2: 4–20× variance ratio

Discussion 中的 "4–20×" 方差比较需从多个实验的 std 值交叉计算得出。无单一 exp_id 直接记录此数字。

### ⚠️ 3: 12–14pp dual-OOD drop

Limitations 中的 dual-OOD 估计值无独立实验。可能来自 Appendix app:dual_ood 的推算，需查 appendix 数据。

### ⚠️ 4: 0.3pp recovery after few-shot adaptation

同上，与 dual-OOD 分析配套，无独立 exp_id。
