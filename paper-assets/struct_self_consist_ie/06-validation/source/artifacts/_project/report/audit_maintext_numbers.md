# 主文数字审计

审计日期: 2026-05-24
审计范围: docs/paper/sections/ 下所有主文 tex 文件
Registry 数据: 完整读取并交叉验证

---

## Abstract

| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |
|------|--------|------------|------|-----------|
| AUROC 0.82 | "AUROC up to $0.82$" | exp_002 (em_auroc_full=0.8156) | ✅ .816→.82 (2dp rounding) | = Intro "AUROC $0.82$"; Tab quality_estimation CoNLL EM .816 |
| <1 pp | "selection yields no detectable gains (${<}1$\,pp)" | exp_016_rerun_1024_bootstrap | ✅ | = Intro/§4 consistent |
| +1.40 pp | "$+1.40$\,pp on Few-NERD" | exp_entity_construction (n8_fair_cv) | ⚠️ 见问题 #1 | = Intro +1.40; §4.5 +1.40±0.51; fig_overview caption +1.40 |
| 3-epoch | "under 3-epoch training" | exp_021_fewnerd_full (epochs=3) | ✅ | = Intro/§4 consistent |
| p_adj=0.055 | "global Holm $p_{\text{adj}}{=}0.055$" | ⚠️ UNTRACED (统计结果，非直接实验 metric) | — | = Intro; §4.5 (k=57); limitations ✅ 一致 |
| p_adj=0.006 | "per-family $p_{\text{adj}}{=}0.006$" | ⚠️ UNTRACED | — | = Intro; §4.5 (k=10) ✅ 一致 |
| degeneracy + signal alignment collapse | 定性描述 | N/A | ✅ | 一致 |

## Introduction

| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |
|------|--------|------------|------|-----------|
| ρ up to 0.45 | "ρ up to $0.45$" | exp_002 (em_rho_full=0.4507) | ✅ .451→.45 | = Tab quality_estimation CoNLL EM ρ=.451 |
| AUROC 0.82 | "AUROC $0.82$; Table quality_estimation" | exp_002 (em_auroc_full=0.8156) | ✅ | = Abstract ✅ |
| MV <1 pp at N=64 | "MV ${<}1$ percentage point (pp) even at $N{=}64$" | exp_conll_n64_s42 (mv_delta=0.64pp) | ✅ | = Fig n_scaling caption "+0.6pp at N=64" |
| AUROC 0.63–0.88 | hidden-state probe | ⚠️ UNTRACED (appendix mechanistic) | — | = §4.1 line 53 一致 |
| ESJ AUROC 0.51 | entity self-judgment | exp_esj_qwen3_all (scierc esj_auroc=0.512) | ✅ | = Tab method_summary AUROC 0.51 |
| 12–68% | "degeneracy ($12$--$68$\%)" | Tab fewnerd: SciERC 12.2%, WNUT 67.9% | ✅ 12.2→12, 67.9→68 | = Discussion ✅ |
| LP +1.39 pp | "LP $+1.39$\,pp on Few-NERD" | exp_021_fewnerd_full (lp_delta=1.36, seed42) | ⚠️ 见问题 #2 | = §4.1 +1.39; Tab fewnerd +1.39 |
| MV +0.6 pp | "MV $+0.6$\,pp on CoNLL" | exp_conll_n64_s42 (mv_delta=0.64pp) | ✅ .64→.6 | = Fig n_scaling; §4.3 |
| +1.40 pp (construction) | "Exploratory entity-level construction yields conditional improvement ($+1.40$\,pp on Few-NERD, 3-epoch" | Same as abstract | ⚠️ 见问题 #1 | = Abstract; §4.5 |
| p_adj=0.055 | "global Holm $p_{\text{adj}}{=}0.055$" | ⚠️ UNTRACED | — | = Abstract; §4.5; limitations ✅ |
| p_adj=0.006 | "per-family $p_{\text{adj}}{=}0.006$" | ⚠️ UNTRACED | — | = Abstract; §4.5 ✅ |
| 87.2% | "SQL parsing ($87.2$\% degeneracy)" | exp_spider_sc_pilot (F1_degeneracy=0.872) | ✅ | 仅出现一次 |
| 40% zero-F1 | "RE…$40$\% zero-F1" | provenance c006 notes "paper uses 40% from primary config"; registry shows 44.3% at N=16 | ⚠️ 见问题 #3 | = §4.3 "40%" 一致 |
| ρ up to 0.47 | "\citet{yao2026consistency} report…$\rho$ up to 0.47" | 引用他人数据 | N/A | 仅引用 |
| LP mean weight 0.78 | "ensemble optimization assigns LP mean weight $0.78$" | ⚠️ UNTRACED (appendix supervised_combination) | — | 仅出现一次 |
| 3–12% recovery ratio | "3--12\% recovery ratio" | ⚠️ UNTRACED (理论计算) | — | = theoretical.tex; theory.tex ✅ |
| α=0.000–0.121 | "$\alpha$ approaches zero ($0.000$--$0.121$)" | ⚠️ UNTRACED (理论计算) | — | = theory.tex line 38 ✅ |
| +3.85 pp MV | "pretrained Qwen2.5-7B at $N{=}32$ achieves $+3.85$\,pp MV gain" | exp_fewnerd_pretrained_n32_s42_v2 (mv_delta=3.85) | ✅ | 仅出现一次 |
| D=5.4% | "$D{=}5.4$\%" | exp_fewnerd_pretrained_n32_s42_v2 (degen=5.42) | ✅ 5.42→5.4 | 仅出现一次 |

## §3 Diagnostic Framework

| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |
|------|--------|------------|------|-----------|
| +4.6 F1 points | "length normalization eliminates length bias ($+4.6$ F1 points)" | ⚠️ UNTRACED (appendix token_signal) | — | 仅出现一次 |
| n=529 | "n=529 on SciERC" | exp_012_rerun_1024 (ner_full n=529) | ✅ | = Tab quality_estimation caption; Tab fewnerd SciERC n=529 |
| n=2,756 | "n=2,756 on CoNLL" | exp_017_llama_conll_infer data | ✅ | = Tab fewnerd CoNLL n=2,756 |
| 9–26% | "Entity-set exact-match degeneracy…($9$--$26$\%)" | exp_fewnerd_mf4_s* (8.1%–9.3% at 5-epoch) | ⚠️ 见问题 #4 | 脚注内部使用 |
| 13–31% | "vs.\ $13$--$31$\% constant-F1" | exp_021 seeds (10.1%–13.1% at 3-epoch) | ⚠️ 部分匹配 | 脚注内部使用 |

## §4.1 Single-Signal Selection Results

| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |
|------|--------|------------|------|-----------|
| 60% LP range <0.041 | "60\% of SciERC instances showing within-instance LP range below 0.041 nats" | ⚠️ UNTRACED (appendix logprob_ties) | — | 仅出现一次 |
| 0.97× | "free-form decoding yields nearly identical LP distributions (within-instance std ratio $0.97$)" | exp_conll_freeform_n8_s42 / exp_fewnerd_freeform_n8_s42 | ⚠️ 无法直接确认 0.97 | 仅出现一次 |
| Tab selection: Oracle 0.775±0.001 | Best-of-N table | exp_016_rerun_1024_bootstrap (oracle=0.776) | ⚠️ .776 vs .775 | 仅 Tab selection |
| Tab selection: Greedy 0.645±0.001 | Best-of-N table | exp_016_rerun_1024_bootstrap (greedy=0.644) | ⚠️ .644 vs .645 | ❌ 见问题 #5 |
| Tab selection: LP 0.647±0.005 | LP selection F1 | exp_016_rerun_1024_bootstrap | ⚠️ 间接 | 仅 Tab selection |
| Tab selection: LP p=.29 | "LP achieves $+0.2$\,pp ($p{=}0.29$)" | exp_016_rerun_1024_bootstrap (permutation_p=0.39) | ❌ 见问题 #6 | Tab vs text 一致 (.29) |
| ρ up to 0.38 | "Despite $\rho$ up to 0.38" | exp_012_rerun_1024 (vc_rho=0.3792) | ✅ .379→.38 | = Tab quality_estimation VC ρ=.379 |
| +13.0 pp headroom | "the oracle shows 13.0\,pp headroom" | Tab selection: 0.775-0.645=0.130=13.0pp | ✅ | = fig_selection_gap caption "+13.0pp" ✅ |
| MDE ≈1.5 pp | "below MDE (${\approx}$1.5\,pp at $n{=}529$, 2--3 seeds" | ⚠️ UNTRACED (统计计算) | — | = limitations ✅ |
| LP +1.39 pp (Few-NERD) | "LP achieves $+1.39$\,pp ($p{<}0.001$; Holm $p_{\text{adj}}{=}0.021$, k=21)" | exp_021_fewnerd_full (1.36 for seed42) | ⚠️ 见问题 #2 | = Tab fewnerd; Intro |
| p_adj=0.021, k=21 | selection family correction | provenance C143 has p_adj=0.019 k=19 | ⚠️ 见问题 #7 | 仅出现一次 |
| p_adj=0.055 (global k=57) | footnote | ⚠️ UNTRACED | — | = Abstract; §4.5; limitations |
| 13.0% degeneracy (Few-NERD) | "low degeneracy (13.0\%)" | 见问题 #8 | ⚠️ | = Tab fewnerd 13.0% |
| 12.2% (SciERC) | "SciERC 12.2\%" | exp_012_rerun_1024 (degen=0.1777?) | ⚠️ 见问题 #9 | = Tab fewnerd 12.2% ✅ |
| 61.7% (CoNLL) | "CoNLL 61.7\%" | ⚠️ UNTRACED | — | = Tab fewnerd 61.7% ✅ |
| VC −1.79, SJ −2.14 pp | structural signals degrade on Few-NERD | exp_021_fewnerd_full (vc_delta=-1.79, sj_delta=-2.14) | ✅ | = §4.3 一致 |
| ρ=0.052, n=23, p=0.81 | degeneracy-LP across configs | ⚠️ UNTRACED | — | = §4.3 Fig degeneracy_scatter ✅ |
| ρ=−0.881 | within-dataset degen-LP | ⚠️ UNTRACED | — | = §4.3 ✅ |
| MRSC −3.1 pp | multi-round refinement | ⚠️ UNTRACED (appendix mechanistic) | — | = Tab method_summary ✅ |
| LSC −3.5 pp | latent centroid selection | ⚠️ UNTRACED (appendix mechanistic) | — | = Tab method_summary ✅ |
| ESJ AUROC 0.50–0.55 (Qwen3-8B) | cross-model ESJ | exp_esj_qwen3_all (scierc=0.512, fewnerd=0.495) | ✅ | 仅出现一次 |

## §4.2–4.3 Experiments (experiments_main.tex)

### Tab quality_estimation

| 数字 | 来源 exp_id | 验证 |
|------|------------|------|
| SciERC VC ρ=.379 | exp_012_rerun_1024 (voting_conf rho=0.3792) | ✅ |
| SciERC SJ ρ=.360 | exp_012_rerun_1024 (SJ rho=0.3599) | ✅ |
| SciERC FK ρ=.267 | exp_012_rerun_1024 (FK rho=0.2665) | ✅ |
| SciERC EM ρ=.295 | exp_012_rerun_1024 (EM rho=0.2945) | ✅ |
| SciERC LP ρ=.205 | exp_012_rerun_1024 (LP rho=0.2052) | ✅ |
| SciERC VC AUC=.684 | exp_012_rerun_1024 (voting_conf AUROC=0.6841) | ✅ |
| SciERC SJ AUC=.692 | exp_012_rerun_1024 (SJ AUROC=0.6917) | ✅ |
| SciERC FK AUC=.629 | exp_012_rerun_1024 (FK AUROC=0.629) | ✅ |
| **SciERC EM AUC=.631** | **exp_012_rerun_1024 (EM AUROC=0.7493)** | **❌ 见问题 #10** |
| SciERC LP AUC=.578 | exp_012_rerun_1024 (LP AUROC=0.5783) | ✅ |
| CoNLL Qwen EM ρ=.451 | exp_002 (em_rho_full=0.4507) | ✅ |
| CoNLL Qwen EM AUC=.816 | exp_002 (em_auroc_full=0.8156) | ✅ |
| CoNLL Qwen SJ ρ=.436 | exp_002 (sj_rho_full=0.4357) | ✅ |
| CoNLL LLaMA SJ ρ=.431 | exp_017_llama_conll_infer (SJ_rho=0.4314) | ✅ |
| CoNLL LLaMA LP AUC=.761 | exp_017_llama_conll_infer (logprob_AUROC=0.761) | ✅ |

### Tab fewnerd (cross-dataset LP selection)

| 数字 | 来源 exp_id | 验证 | 跨位置一致 |
|------|------------|------|-----------|
| WNUT n=1,287 | exp_003_wnut17_eval (n=1287) | ✅ | = §4.2 |
| WNUT Greedy .452 | exp_wnut17_qwen25_7b (seed42 greedy=0.4524) | ✅ | — |
| WNUT Degen 67.9% | ⚠️ UNTRACED (N=8 data; registry WNUT experiments are N=16) | — | = text 12–68% upper bound |
| WNUT LP ρ=−.446 | ⚠️ UNTRACED (registry has −.414/−.409 at N=16) | — | — |
| CoNLL n=2,756 | consistent | ✅ | = §3 |
| CoNLL Greedy .908 | ⚠️ UNTRACED for N=8 Qwen | — | — |
| CoNLL Degen 61.7% | ⚠️ UNTRACED | — | = §4.1 ✅ |
| CoNLL LP ρ=.302 | ⚠️ ≠ Tab quality_estimation LP ρ=.316 | ⚠️ 见问题 #11 | — |
| **SciERC Greedy .663** | **exp_scierc_n8_s* (greedy ≈0.661–0.666)** | ✅ matches multi-seed | **❌ ≠ Tab selection Greedy .645 见问题 #5** |
| SciERC Degen 12.2% | ⚠️ PARTIALLY TRACED | — | = §4.1 ✅ |
| **SciERC LP ρ=.159** | ⚠️ UNTRACED | — | **❌ ≠ Tab quality_estimation LP ρ=.205 见问题 #11** |
| **SciERC LP Δ=+0.61 pp** | ⚠️ UNTRACED | — | **❌ ≠ §4.1 text "+0.2pp" 见问题 #5** |
| Few-NERD n=32,565 | exp_021_fewnerd_full (filtered=32565) | ✅ | — |
| Few-NERD Greedy .748 | exp_021_fewnerd_full (greedy=0.7478) | ✅ | — |
| Few-NERD Degen 13.0% | ⚠️ 见问题 #8 | — | = §4.1 ✅ |
| Few-NERD LP ρ=.220 | ⚠️ ≠ exp_021 lp_global_rho=0.4215 | ⚠️ 见问题 #12 | — |
| Few-NERD LP Δ=+1.39 pp | exp_021_fewnerd_full (1.36 seed42) | ⚠️ 见问题 #2 | = §4.1; Intro |

### Other §4 numbers

| 数字 | 上下文 | 来源 | 验证 | 跨位置一致 |
|------|--------|------|------|-----------|
| SciERC 551 instances, 6 types | §4.2 setup | ✅ 标准 | ✅ | = §3 n=529 (gold-filtered) consistent |
| Few-NERD 37,648 instances, 8 types | §4.2 setup | exp_021 (instance_count=37648) | ✅ | — |
| CoNLL 3,453 instances, 4 types | §4.2 setup | ✅ 标准 | ✅ | — |
| WNUT-17 1,287 instances, 53.7% zero F1 | §4.2 setup | exp_003_wnut17_eval (53.7%) | ✅ | — |
| SJ>LP Δρ=+0.151±0.006 | §4.2 QE results | ⚠️ UNTRACED (bootstrap) | — | 仅出现一次 |
| p_adj=0.013 (k=5) | seed-replication SJ>LP | ⚠️ UNTRACED | — | 仅出现一次 |
| CoNLL EM ρ=0.816 (AUROC) | §4.2 "EM leads both ρ and AUROC ($0.816$)" | exp_002 (em_auroc=0.8156) | ✅ | = Tab quality_estimation |
| WNUT VC ρ=0.724 at N=16 | §4.2 | exp_003 系列 | ⚠️ UNTRACED | 仅出现一次 |
| WNUT conditional ρ=0.038 | §4.2 | ⚠️ UNTRACED | — | 仅出现一次 |
| LP conditional ρ=0.350 | §4.2 WNUT | exp_003_wnut17_eval (rho_logprob_cond=0.35) | ✅ | 仅出现一次 |
| LP σ=0.04 vs SJ 2.02 pp | §4.3 seed stability | ⚠️ UNTRACED | — | 仅出现一次 |
| 50× more seed-stable | 2.02/0.04=50.5≈50 | ✅ 算术一致 | — | 仅出现一次 |
| ρ=0.90, p=0.002 (MV vs low-F1 types) | §4.3 | ⚠️ UNTRACED (appendix pertype) | — | 仅出现一次 |
| MV −2.71 pp (Few-NERD) | §4.3 | ⚠️ UNTRACED | — | 仅出现一次 |
| Qwen3-4B |Δρ|=0.042 | §4.4 robustness | ⚠️ UNTRACED | — | 仅出现一次 |
| +1.40±0.51 pp (construction) | §4.5 | exp_entity_construction | ⚠️ 见问题 #1 | = Abstract; Intro |
| +0.32 pp SciERC (n.s.) | §4.5 | ⚠️ 见问题 #13 | — | 仅出现一次 |
| −0.39 pp CoNLL | §4.5 | exp_entity_construction (conll cv_uniform='-0.39pp') | ✅ | 仅出现一次 |
| D=13%, headroom=12.4 pp | §4.5 Few-NERD | exp_021 (headroom=0.124=12.4pp) | ✅ | — |
| p_adj=0.006 (k=10) | §4.5 | ⚠️ UNTRACED | — | = Abstract; Intro |
| p_adj=0.055 (k=57) | §4.5 | ⚠️ UNTRACED | — | = Abstract; Intro; limitations |
| ρ_adj=0.516 | §4.5 construction-selection correlation | ⚠️ UNTRACED | — | 仅出现一次 |
| 5-epoch: +1.39→+0.12 pp (selection) | §4.5 epoch confound | exp_fewnerd_5epoch_lp_s42 (lp_delta=0.12) | ✅ (5-epoch end) | — |
| **5-epoch: +0.88→+0.20 pp (construction)** | §4.5 epoch confound | exp_entity_construction (n8_fair_cv fewnerd lp_weighted_cv='+0.88pp') | ⚠️ 见问题 #1 | — |
| 9%→26% degeneracy | §4.5 epoch confound | 见问题 #4 | ⚠️ | — |

## §4.4 Adaptive Methods

| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |
|------|--------|------------|------|-----------|
| +0.42 pp (cross-model) | Qwen+LLaMA on Few-NERD | exp_cross_model_consistency (delta=0.42, p=0, CI=[0.27,0.58]) | ✅ | = Tab method_summary |
| CI [0.27, 0.58] | cross-model CI | exp_cross_model_consistency | ✅ | 仅出现一次 |
| AUC=0.923±0.002 | LightGBM verifier | exp_b2_entity_verifier (oof_auc=0.9233) | ✅ | = Tab method_summary |
| +0.30 pp (verifier) | LightGBM F1 gain | exp_b2_entity_verifier (oof_delta_pp=0.3) | ✅ | = Tab method_summary |
| −0.76 to −1.02 pp | verifier cross-dataset transfer | ⚠️ UNTRACED (appendix verifier_transfer) | — | 仅出现一次 |
| ESJ AUROC 0.51 | Tab method_summary | exp_esj_qwen3_all (esj_auroc=0.512) | ✅ | = §4.1 |
| MRSC −3.1 pp | Tab method_summary | ⚠️ UNTRACED | — | = §4.1 |
| LSC −3.5 pp | Tab method_summary | ⚠️ UNTRACED | — | = §4.1 |
| DALS +0.71 pp (SciERC) | Tab method_summary | ⚠️ UNTRACED | — | 仅出现一次 |
| −0.4 to −3.1 pp | Sup. combination LR/MLP/RF | ⚠️ 见问题 #14 | — | 仅出现一次 |

## §Theoretical Analysis (theoretical.tex)

| 数字 | 上下文 | 来源 | 验证 | 跨位置一致 |
|------|--------|------|------|-----------|
| G_nd≈14.8 pp | "with $G_{\textup{nd}}{\approx}14.8$\,pp" | ⚠️ UNTRACED (理论计算) | — | 仅出现一次 |
| α≈0.068 | "$\alpha{\approx}0.068$" | ⚠️ UNTRACED | — | = fig_bound caption |
| θ_crit=0.70 | "$\theta_{\textup{crit}}{=}0.70$" | ✅ 算术验证: (1-0.70)×14.8×0.068=0.302≈0.3pp | = theory.tex θ_crit∈[0.60,0.80] 一致 |
| 3–12% | recovery ratio | ⚠️ UNTRACED | — | = Intro; theory.tex ✅ |

## §Threshold Regime Analysis (theory.tex)

| 数字 | 上下文 | 来源 exp_id | 验证 | 跨位置一致 |
|------|--------|------------|------|-----------|
| R²>0.999 | oracle scaling fit | ⚠️ UNTRACED | — | 仅出现一次 |
| c≈0.61 (Few-NERD) | scaling exponent | ⚠️ UNTRACED | — | 仅出现一次 |
| c≈0.35 (SciERC) | scaling exponent | ⚠️ UNTRACED | — | 仅出现一次 |
| 8B→14B: +1.2 pp oracle, +0.9 pp greedy | scale ablation | ⚠️ UNTRACED | — | 仅出现一次 |
| GPT-5.5: 50% degen | frontier SC | exp_frontier_sc_gpt55_fewnerd_v2 (degen=0.5) | ✅ | 仅出现一次 |
| GPT-5.5: SJ ρ=0.346 | frontier SC | exp_frontier_sc_gpt55_fewnerd_v2 (sj_rho=0.3461) | ✅ | 仅出现一次 |
| GPT-5.5: MV +1.4 pp | frontier SC | exp_frontier_sc_gpt55_fewnerd_v2: mv-greedy=0.6521-0.6382=0.0139=1.39pp→1.4 | ✅ | 仅出现一次 |
| GPT-5.5: 6.8 pp unrealized | frontier SC | oracle-mv=0.7203-0.6521=0.0682=6.82pp→6.8 | ✅ | 仅出现一次 |
| 10.1% empty entity sets | GPT-5.5 footnote | ⚠️ UNTRACED | — | 仅出现一次 |
| 88% gold-empty | GPT-5.5 footnote | ⚠️ UNTRACED | — | 仅出现一次 |
| 1.2% true parse failures (19/1600) | GPT-5.5 footnote | ⚠️ UNTRACED | — | 仅出现一次 |
| Qwen2.5: 31.7–46.2% | cross-scale degen | ⚠️ UNTRACED | — | 仅出现一次 |
| 40 of 58 transitions (p<0.05) | inverse scaling | ⚠️ UNTRACED | — | 仅出现一次 |
| θ=2/N: −3.09 pp (N=8), −6.90 pp (N=16) | inverse scaling severity | ⚠️ UNTRACED | — | 仅出现一次 |
| MV: −0.87/−0.60 pp | MV inverse scaling | ⚠️ UNTRACED | — | 仅出现一次 |
| OR=0.109 (11.1% vs 1.3%) | degen vs inverse scaling | ⚠️ UNTRACED; 算术近似验证: (1.3/98.7)/(11.1/88.9)=0.1055≈0.109 | — | 仅出现一次 |
| CoNLL SJ ρ .30→.44 | few-shot improvement | ⚠️ UNTRACED | — | 仅出现一次 |
| α=0.000–0.121 | binding constraint | ⚠️ UNTRACED | — | = §4.1 ✅ |
| 8–33× tighter | α vs D | ⚠️ UNTRACED | — | = Intro; Discussion ✅ |
| split-half r=0.395–0.578 | FK independence | ⚠️ UNTRACED | — | 仅出现一次 |
| bound ratio 0.13–0.63 | signal-adjusted bound | ⚠️ UNTRACED | — | 仅出现一次 |
| α_crit,eff=1.148 (CoNLL) | MV impossibility | ⚠️ UNTRACED | — | 仅出现一次 |

## §5 Discussion

| 数字 | 上下文 | 验证 | 跨位置一致 |
|------|--------|------|-----------|
| 12–68% | degeneracy range | ✅ | = Intro; §4.5 ✅ |
| α→0 | signal alignment collapse | ✅ | 全文一致 |
| 8–33× tighter | α vs D | ✅ | = Intro; theory.tex ✅ |
| >50% | high degeneracy threshold | ✅ | 全文一致 |

## Limitations

| 数字 | 上下文 | 验证 | 跨位置一致 |
|------|--------|------|-----------|
| 5.5–74% | frontier degeneracy | exp_frontier_sc_deepseek (5.5%), exp_frontier_sc_claude_sonnet4 (74%) | ✅ | 仅出现一次 |
| p_adj=0.055 | strongest construction claim | ✅ | = Abstract; §4.5 ✅ |
| MDE≈1.5 pp | statistical power | ✅ | = §4.1 ✅ |
| RE n=397, SQL n=196 | cross-task sample sizes | exp_spider_sc_pilot (n=196) | ✅ SQL; RE ⚠️ UNTRACED | — |
| +1–1.4 pp | construction gain range | ✅ 与 §4.5 一致 | — |

---

## 关键数字重点检查

### 1. SciERC EM AUROC = .631（不是 .749）
- **Tab quality_estimation: .631** ✅ 论文正确
- **Registry exp_012_rerun_1024: EM AUROC = 0.7493** ❌ Registry 与论文不一致
- **Provenance c002: "EM leads AUROC (NER 0.749)"** ❌ Provenance STALE
- **结论**: 论文已正确修改为 .631，但 registry 和 provenance 仍保留旧值 .749。**paper_provenance.yaml 需要更新。**

### 2. Headroom = 13.0pp（不是 11.4pp）
- Tab selection: Oracle 0.775 − Greedy 0.645 = 0.130 = **13.0pp** ✅
- fig_selection_gap caption: **+13.0pp** ✅
- 全文无 11.4pp 出现。**PASS。**

### 3. MV = +0.6pp（不是 +0.61pp）
- Intro: "MV $+0.6$\,pp on CoNLL" ✅
- Fig n_scaling caption: "+0.6pp at N=64" ✅
- §4.3 text: "+0.6pp" ✅
- Registry exp_conll_n64_s42: mv_delta = 0.64pp → 0.6 (1dp rounded) ✅
- 全文无 +0.61pp 出现（Tab fewnerd SciERC LP Δ = +0.61pp 是 LP 不是 MV）。**PASS。**

### 4. α = 0.121
- §4.1: "$\alpha$ approaches zero ($0.000$--$0.121$)" ✅
- theory.tex: "$\alpha{=}0.000$--$0.121$" ✅
- 上限一致。**PASS。**

### 5. SciERC construction = +0.32pp n.s.
- §4.5: "a non-significant $+0.32$\,pp on SciERC" ✅ 论文内一致
- **Registry discrepancy**: exp_entity_construction 显示 SciERC n8_fair_cv 多个变体均 >+1pp（见问题 #13）
- **结论**: 论文内一致，但 registry 来源不清楚。可能来自不同配置或后续重算。

### 6. Holm p_adj = 0.055 (global k=57) vs p_adj = 0.013 (seed-replication k=5)
- **p_adj=0.055 (k=57)**: Abstract, Intro, §4.5, limitations — 全部一致 ✅
- **p_adj=0.013 (k=5)**: §4.2 "SJ>LP advantage reaches $p_{\text{adj}}{=}0.013$" — 这是信号比较的 seed-replication correction ✅
- 两者是不同统计框架，论文正确区分了。**PASS。**

### 7. fig_selection_gap caption Oracle = +13.0pp（不是 +13.1pp）
- Caption: "oracle headroom ($+13.0$\,pp)" ✅
- Tab selection: 0.775 − 0.645 = 0.130 = 13.0pp ✅
- 全文无 13.1pp 出现。**PASS。**

---

## 问题清单

按严重程度排序：

### 🔴 严重 (Cross-table inconsistency)

**#5. SciERC 基线在两个表格间不一致**
- Tab selection (§4.1): Greedy = 0.645±0.001, LP Δ = +0.2pp (p=0.29)
- Tab fewnerd (§4.3): Greedy = 0.663, LP Δ = +0.61pp (p=0.193)
- 两表均标注 "SciERC, Qwen3-8B, N=8, T=1.0"
- **差异**: Greedy F1 差 1.8pp; LP Δ 差 0.41pp
- **可能原因**: 不同训练种子 / 不同 model checkpoint（exp_016 系列 vs exp_scierc_n8_s* 系列），但论文未说明
- **影响**: 读者会困惑为何同一设置有不同基线

**#10. SciERC EM AUROC: 论文 .631 vs Registry .7493**
- Tab quality_estimation 显示 .631
- exp_012_rerun_1024 registry 显示 EM AUROC = 0.7493
- Provenance c002 仍记录 0.749
- **状态**: 论文值 .631 被指定为正确值（任务说明），但 **registry 和 provenance 从未更新**
- **影响**: 后续引用 provenance 的操作会得到错误数据

**#11. SciERC/CoNLL LP ρ 在 Tab quality_estimation vs Tab fewnerd 间不一致**
- SciERC LP ρ: Tab quality_estimation = .205; Tab fewnerd = .159 (差 0.046)
- CoNLL LP ρ: Tab quality_estimation = .316; Tab fewnerd = .302 (差 0.014)
- Tab quality_estimation 是 primary seed=42; Tab fewnerd 是 3-seed mean
- **差异可能合理**（不同种子均值），但未在文中说明

### 🟡 中等 (Traceability / consistency concern)

**#1. Construction +1.40pp vs +0.88pp 同一方法不同数字**
- §4.5 主结果: LP-weighted construction = +1.40±0.51pp (4-seed mean, full test)
- §4.5 epoch confound: "construction: +0.88→+0.20pp"
- Registry: n8_fair_cv fewnerd LP-weighted CV = +0.88pp
- **分析**: +1.40 是 4-seed non-CV; +0.88 是 5-fold CV。两种评估方法给出不同结果。论文在同一段落交替使用两种评估方法而未说明
- **影响**: 读者可能误以为 3-epoch construction gain = +0.88pp 而非 +1.40pp

**#2. LP selection +1.39pp: 主种子显示 1.36pp**
- 论文: +1.39pp (标注 3-seed mean)
- Registry exp_021_fewnerd_full (seed42): lp_selection_delta_pp = 1.36
- 其他种子 LP delta 未在 registry summary 中找到
- **影响**: 无法从 registry 直接验证 1.39 是否为正确的 3-seed mean

**#6. Tab selection LP p-value: 论文 .29 vs Registry .39**
- Tab selection: LP p=.29
- exp_016_rerun_1024_bootstrap: permutation_p = 0.39
- **可能原因**: Tab selection 可能用 paired bootstrap（2-seed），exp_016 用 permutation test；或来自不同实验版本
- **影响**: p-value 不同但结论相同（均不显著）

**#7. Holm p_adj: 论文 0.021 (k=21) vs Provenance 0.019 (k=19)**
- §4.1 footnote: "Holm $p_{\text{adj}}{=}0.021$, selection family $k{=}21$"
- Provenance C143: "p_adj=0.019 k=19"
- **分析**: 家族大小从 19 增至 21（加入更多比较），p_adj 相应增大。Provenance stale。
- **影响**: 数值轻微差异，结论不变

**#8. Few-NERD degeneracy 13.0%: 主种子 registry 显示 10.1%**
- Tab fewnerd: 13.0% (标注 3-seed mean)
- exp_021_fewnerd_full (seed42): degeneracy_rate = 0.101 (10.1%)
- exp_021_fewnerd_n8_seed123: degen_rate = 0.1312 (13.1%)
- exp_021_fewnerd_n8_seed456: degen_rate = 0.1212 (12.1%)
- 3-seed mean: (10.1+13.1+12.1)/3 = 11.8%, not 13.0%
- **可能原因**: seed42 的 0.101 可能不是 constant-F1 degeneracy（seed123/456 标注为 unified_metrics_constant_f1_gold_filtered，seed42 未标注）
- **影响**: 无法确认 13.0% 的准确性

**#3. RE 40% zero-F1: Registry 显示 44.3%**
- 论文多处: "40% zero-F1"
- Provenance c006: "44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)"
- 40% 的具体来源实验不在 registry summary 中
- **影响**: 轻微，但 40 vs 44.3 的差异未解释

**#9. SciERC degeneracy 12.2%: Registry exp_012 显示 17.77%**
- Tab fewnerd: SciERC Degen.% = 12.2%
- exp_012_rerun_1024: degen_rate = 0.1777 (17.77%)
- exp_scierc_n8_s123: degeneracy_rate = 0.116 (11.6%)
- exp_scierc_n8_s456: degeneracy_rate = 0.12 (12.0%)
- **分析**: 12.2% 可能来自 s123/s456 的均值而非 exp_012，或 exp_012 的 17.77% 是不同度量
- **影响**: 来源不清楚

**#12. Few-NERD LP ρ=.220 in Tab fewnerd vs .4215 in Registry**
- Tab fewnerd: LP ρ = .220
- exp_021_fewnerd_full: lp_global_rho = 0.4215
- 差异 2x，即使是 3-seed mean 也不太可能降到 .220
- **可能原因**: Tab fewnerd 的 LP ρ 可能不是 global cross-instance ρ，而是某种 within-instance 或 conditional 度量
- **影响**: 如果是不同度量，需要在表格或 caption 中注明

**#13. SciERC construction +0.32pp vs Registry +1.12~+1.67pp**
- 论文: "+0.32pp on SciERC (non-significant)"
- Registry exp_entity_construction: SciERC n8_fair_cv 多个变体 = +1.12 to +1.67pp
- **可能原因**: 不同 θ、不同评估方法、不同种子集
- **影响**: 无法从 registry 追溯 +0.32pp 的来源

**#14. Supervised combination "-0.4 to -3.1pp"**
- Tab method_summary: "LR/MLP/RF: −0.4 to −3.1pp"
- Registry exp_backup3_distill_verifier: per-fold deltas 最大 = −0.34pp
- −3.1pp 在 registry 中找不到对应
- **可能原因**: −3.1pp 可能来自另一个实验或特定配置
- **影响**: 范围上界无法追溯

### 🟢 轻微 (Rounding / precision)

**#4. Degeneracy type mixing in epoch comparison**
- §4.5: "degeneracy rises from 9% to 26%" — entity-set exact-match
- 主表 (Tab fewnerd): 13.0% — constant-F1
- 脚注已解释两种度量，但正文在不同位置使用不同度量未明确标注

**"LP-best +1.4pp" 精度模糊**
- §4.3: "LP-best $+1.4$\,pp on Few-NERD" — 可能是 selection (+1.39→1.4) 或 construction (+1.40)
- 建议明确是哪种方法

**AUROC rounding**
- Abstract/Intro: "AUROC up to 0.82" — 来自 .816 (2dp rounding)
- 技术上正确但比表格精度低

---

## 精度一致性

| 类别 | 精度 | 评估 |
|------|------|------|
| 表格 ρ 值 | 3 位小数 (.379, .360) | ✅ 表内一致 |
| 正文 ρ 引用 | 2 位小数 (.38, .45) | ✅ 合理简化 |
| pp 增益 | 1-2 位小数 (+1.39, +0.6, +0.2) | ⚠️ +0.6 vs +1.39 精度不统一 |
| 百分比 (degeneracy) | 1 位小数 (12.2%, 13.0%) | ✅ 一致 |
| p-values | 表格 2 位 (.29, .67); 正文混合 | ✅ 大致一致 |
| AUROC | 表格 3 位 (.631, .816); 正文 2 位 (.82) | ⚠️ 正文与表格精度不同但可接受 |

总体精度一致性：**合格**，无系统性精度不一致问题。

---

## 总结

- **已验证数字**: ~60% 可追溯到 registry 实验或算术验证
- **UNTRACED**: ~25% 来自 appendix 实验或统计计算，无法从 registry summary 直接验证
- **发现问题**: 14 个，其中 3 个严重（跨表不一致）、11 个中等或轻微
- **7 个 bug-prone 数字**: 论文中全部正确 ✅，但 registry/provenance 有 2 处 stale 数据

**最需要关注的问题**:
1. Tab selection vs Tab fewnerd SciERC 基线不一致 (问题 #5)
2. Registry EM AUROC stale (问题 #10) — 需更新 registry 和 provenance
3. Construction +1.40 vs +0.88 评估方法混用 (问题 #1)
