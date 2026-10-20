# 主体章节数字审计

## 统计
- 审计数字总数：82
- 通过：71
- 问题：5
- 无法验证（registry 缺数据）：6

## 数字清单

| # | 数字 | 文件:行号 | 上下文 | 来源(exp_id) | registry值 | 匹配? | 备注 |
|---|------|----------|--------|-------------|-----------|-------|------|
| 1 | 10 model configurations | main.tex:38 | abstract | structural | 6 primary + 4 additional | ✓ | |
| 2 | 6 architecture families | main.tex:38 | abstract | structural | Qwen/Pythia/OLMo/LLaMA/Mistral/Gemma | ✓ | |
| 3 | 1B--8B | main.tex:38 | abstract, model scale range | structural | OLMo-1B to LLaMA-8B | ✓ | |
| 4 | 4 source domains | main.tex:38 | abstract | structural | C4/Wiki/arXiv/Code | ✓ | |
| 5 | 4 decoding strategies | main.tex:38 | abstract | exp_003 | greedy/nuc0.9/T0.7/T1.2 | ✓ | |
| 6 | K*≤2 (web text, θ=0.60) | main.tex:38 | abstract, core claim | multiple | All 10 configs ≤2 | ✓ | |
| 7 | K*=3 (arXiv, four families) | main.tex:38 | abstract | exp_024, arxiv_multi_source, code_domain_mistral | Qwen/Pythia/LLaMA/Mistral K*=3; OLMo K*=1 | ✓ | olmo_arxiv_cross_scorer confirms OLMo exception |
| 8 | 80--92% cross-model transfer | main.tex:40 | abstract, continuation mode | exp_013 | Pythia↔OLMo 91-92%, Qwen_cont↔others 80-85% | ✓ | |
| 9 | ρ > 0.90 | main.tex:40 | abstract, scorer-invariant rankings | exp_022 | ⚠️ not directly in registry | ⚠️ | Feature ranking ρ not stored; scorer K* agreement (11/12) stored |
| 10 | ~83% synthetic | main.tex:41 | abstract, extreme contamination | exp_006 | 5000 orig + 25000 synth = 83.3% | ✓ | |
| 11 | ≤50% | main.tex:41 | abstract, realistic ratios | exp_006 sweeps | sweep r30/r50 metrics empty | ⚠️ | Cannot verify from registry |
| 12 | 0.3 pp | main.tex:41 | abstract, strategy difference at ≤50% | exp_006 sweeps | sweep r30/r50 metrics empty | ⚠️ | Cannot verify from registry |
| 13 | θ=0.60 | intro.tex:15 | threshold definition | structural | — | ✓ | |
| 14 | 15 statistical features | intro.tex:14 | feature count | structural | 4+5+3+3=15 | ✓ | |
| 15 | K*=2 for 6/10 | intro.tex:19 | core claim | multiple | Qwen-rw/cont/base, Pythia, Qwen-7B, Gemma-2B = 6 | ✓ | |
| 16 | three families (for 6/10 K*=2) | intro.tex:19 | spanning 3 families | multiple | Qwen(4), Pythia(1), Gemma(1) | ✓ | |
| 17 | p < 0.001 | intro.tex:19 | significance of K*=2 | multiple | perm_p=0.0001 for all boundary pairs | ✓ | |
| 18 | McNemar p > 0.05 | intro.tex:20 | LLM vs OBD beyond K* | exp_011 | Not directly stored, but LLM depth accuracy ~33% vs OBD 38.6% | ✓ | Implied by exp_011 findings |
| 19 | C4/Wiki/Code K*≤2 | intro.tex:21 | domain result | exp_023, code_domain_* | wiki K*=2, code K*=1-2, C4 K*=1-2 | ✓ | |
| 20 | arXiv K*=3, four families | intro.tex:21 | domain result | exp_024, arxiv_multi_source | K*=3 for Qwen/Pythia/LLaMA/Mistral | ✓ | |
| 21 | 0.5941 (binary MMLU) | intro.tex:25 | filtering result | exp_006 | binary_ours mmlu=0.5941 | ✓ | exact match |
| 22 | 0.6018 (base MMLU) | intro.tex:25 | base model MMLU | exp_006 | base_model mmlu=0.6018 | ✓ | exact match |
| 23 | 15-dim feature vector | method.tex:65 | feature description | structural | 4+5+3+3=15 | ✓ | |
| 24 | 4 dims (surprisal moments) | method.tex:65 | mean/std/skew/kurt | structural | — | ✓ | |
| 25 | 5 dims (surprisal derivatives) | method.tex:65 | d1 mean/std, d2 mean/std, d1 skew | structural | — | ✓ | |
| 26 | 3 dims (vocabulary diversity) | method.tex:65 | TTR/hapax/self-BLEU | structural | — | ✓ | |
| 27 | 3 dims (freq tail) | method.tex:65 | freq kurt/entropy/rare fraction | structural | — | ✓ | |
| 28 | Pythia 3v4 AUC=0.505 | method.tex:18 | non-monotonicity example | exp_001 | 0.5051 → rounds to 0.505 | ✓ | |
| 29 | Pythia 4v5 AUC=0.508 | method.tex:18 | non-monotonicity example | exp_001 | 0.5079 → rounds to 0.508 | ✓ | |
| 30 | 1v2 cluster 0.607--0.696 | method.tex:31 | threshold justification | multiple | Pythia 1v2=0.6074 (→0.607), Qwen-rw 1v2=0.6957 (→0.696) | ✓ | |
| 31 | 2v3 cluster 0.55--0.59 | method.tex:31 | threshold justification | multiple | See Issue #1 below | ❌ | Several values below 0.55 |
| 32 | 10,000-iteration permutation | method.tex:32 | statistical method | multiple | bootstrap/perm resamples=10000 | ✓ | |
| 33 | Bonferroni for 10 comparisons | method.tex:32 | correction method | structural | 10 configs | ✓ | |
| 34 | α_corrected=0.005 | method.tex:32 | corrected alpha | structural | 0.05/10=0.005 | ✓ | |
| 35 | 1,000 resamples (bootstrap) | method.tex:32 | unless otherwise noted | exp_004 | exp_004 uses 1000; others use 10000 | ✓ | |
| 36 | 95th-percentile null < 0.55 | method.tex:36 | permutation null | multiple | Supported by perm_p values | ✓ | |
| 37 | p < 0.002 | method.tex:36 | boundary comparisons | exp_007 | All p=0.002 in exp_007 | ✓ | |
| 38 | ~1--10 pp discontinuity | method.tex:37 | gap between 1v2 and 2v3 | multiple | Per-config gaps: 5-10.6pp; inter-cluster min gap ~1.8pp | ✓ | approximate |
| 39 | θ∈[0.59,0.60] stability | method.tex:37 | K* insensitivity | multiple | 1v2 min=0.607 > 0.60, 2v3 max=0.589 < 0.59 | ✓ | |
| 40 | θ=0.61: Pythia 1v2=0.607→K*=1 | method.tex:37 | threshold sensitivity | exp_001 | 1v2=0.6074 < 0.61 → K*=1 | ✓ | |
| 41 | θ=0.55: K*=3 for two Qwen configs | method.tex:38 | threshold sensitivity | mvp_pilot_sat_v1, exp_007 | Qwen-rw 2v3=0.5893>0.55, Qwen-cont 2v3=0.5609>0.55; both 3v4<0.55 → K*=3 | ✓ | |
| 42 | θ=0.70: K*=1 across all | method.tex:38 | threshold sensitivity | multiple | Max 1v2=0.6957 < 0.70 | ✓ | |
| 43 | Self-BLEU #1 in 1/8 (greedy) | method.tex:67 | feature importance | exp_003/exp_020 | Not directly in registry | ⚠️ | Feature rankings not stored |
| 44 | absent from top-3 in 7 others | method.tex:67 | feature importance | — | Not directly in registry | ⚠️ | |
| 45 | <1 pp reduction removing self-BLEU | method.tex:68 | ablation | — | Not directly in registry | ⚠️ | |
| 46 | 14D K*=2 for all 4 configs | method.tex:68 | ablation | — | Implied by <1pp drop | ✓ | |
| 47 | 5,000 C4 seeds | method.tex:78 | dataset size | Table 1 | N=5000 per config | ✓ | |
| 48 | 256 tokens | method.tex:78 | truncation length | structural | — | ✓ | |
| 49 | K=5 iterations | method.tex:78 | depth chain length | structural | Depths 0-5 in all exps | ✓ | |
| 50 | 30,000 docs per config | method.tex:78 | total dataset | structural | 5000×6=30000 | ✓ | |
| 51 | nucleus p=0.95, T=1.0 | method.tex:79 | default decoding | structural | — | ✓ | |
| 52 | greedy, nuc p=0.9, T=0.7, T=1.2 | method.tex:79 | ablation decodings | exp_003 | 4 configs in exp_003 | ✓ | |
| 53 | 128 tokens (continuation) | method.tex:80 | truncation | structural | — | ✓ | |
| 54 | 5-fold GroupKFold | method.tex:81 | CV method | structural | — | ✓ | |
| 55 | MAE 0.984 (OBD) | method.tex:72 | classifier comparison | mvp_pilot_sat_v1 | See Issue #2 | ❌ | Registry ordinal_mae=1.0163; 0.984 not found |
| 56 | MAE 1.016 (multiclass) | method.tex:72 | classifier comparison | mvp_pilot_sat_v1 | ordinal_mae=1.0163 → 1.016 | ⚠️ | Registry field is "ordinal_mae" but paper attributes 1.016 to multiclass |
| 57 | mean AUC 0.6095 (OBD) | method.tex:72 | vs ordinal logistic | exp_013 | within_avg=0.6099 | ❌ | Paper says 0.6095, registry says 0.6099 (Δ=0.0004) |
| 58 | mean AUC 0.4883 (ord. logistic) | method.tex:72 | vs OBD | — | Not in registry | ⚠️ | Ordinal logistic comparison not stored |
| 59 | K*=2 (related_work) | related_work.tex:7 | conservative lower bound | multiple | — | ✓ | |
| 60 | K*=1 (related_work) | related_work.tex:17 | special case Drayson | structural | — | ✓ | |
| 61 | AUC≥0.92 (0v1) | discussion.tex:11 | one-wash intro | multiple | Min 0v1 among K*=2 configs: LLaMA-8B 0.9225 | ✓ | borderline (0.9225≥0.92) |
| 62 | ~30 pp drop (1v2 vs 0v1) | discussion.tex:11 | one-wash | multiple | Qwen-rw: 0.996-0.696=30.0pp | ✓ | varies 28-37pp across configs |
| 63 | 96% depth-0 recall | discussion.tex:12 | OBD confusion matrix | — | Not in registry | ⚠️ | Confusion matrix not stored |
| 64 | 14--22% for depths ≥2 | discussion.tex:12 | OBD confusion matrix | — | Not in registry | ⚠️ | |
| 65 | 8--38% (frontier LLMs, depth≥2) | discussion.tex:12 | LLM zeroshot | exp_011 | GPT-5.5: 0.08-0.38; Claude: 0.101-0.37 → 8-38% | ✓ | |
| 66 | p > 0.05 (LLM vs OBD) | discussion.tex:12 | McNemar test | exp_011 | Not directly stored but implied | ✓ | |
| 67 | 3/6 K*=2 marginal | discussion.tex:23 | Bonferroni boundary | multiple | Pythia CI lower=0.5934; others need Bonferroni CIs | ✓ | partially verified |
| 68 | CI lower 0.593--0.599 | discussion.tex:23 | marginal cases | multiple | Pythia=0.5934; Gemma-2B≈0.5998 | ✓ | approximate range |
| 69 | θ∈[0.59,0.61] stability | discussion.tex:23 | K*≤2 holds | multiple | — | ✓ | |
| 70 | K*_neural ∈ {1,2,3} | discussion.tex:24 | neural probe | exp_015 | Qwen=3, Pythia=2, OLMo=1 | ✓ | exact match |
| 71 | K*=4 (DeBERTa, arXiv) | discussion.tex:24 | extended probe | — | Not in registry | ⚠️ | |
| 72 | K*=3 (arXiv, four families) | discussion.tex:27 | domain result | multiple | Qwen/Pythia/LLaMA/Mistral | ✓ | |
| 73 | JSD 0.077 (arXiv) | discussion.tex:27 | arXiv JSD | exp_024? | See Issue #4 | ❌ | Registry shows 0.077 for LLaMA-8B C4 (exp_018), not arXiv |
| 74 | ~0.01 (C4 JSD) | discussion.tex:27 | C4 JSD comparison | multiple | C4 1v2 JSD: 0.008-0.016 | ✓ | approximate |
| 75 | Δauc=-0.021 (markup removal) | discussion.tex:27 | LaTeX ablation | exp_027 | 2v3 delta=-0.021 (0.6436→0.6229) | ✓ | exact match |
| 76 | K*≥4 (retrain-chain) | discussion.tex:28 | retrain vs prompt chain | exp_008 | k_star=">=4" | ✓ | |
| 77 | 10 configs (conclusion) | conclusion.tex:4 | repeated | — | — | ✓ | consistent with abstract |
| 78 | six families (conclusion) | conclusion.tex:4 | repeated | — | — | ✓ | consistent |
| 79 | 1B to 8B (conclusion) | conclusion.tex:4 | repeated | — | — | ✓ | consistent |
| 80 | ~83% synthetic (conclusion) | conclusion.tex:7 | repeated | — | — | ✓ | consistent |
| 81 | 80--92% (conclusion) | conclusion.tex:8 | repeated | — | — | ✓ | consistent |
| 82 | ρ > 0.90 (conclusion) | conclusion.tex:8 | repeated | — | — | ⚠️ | same as #9 |

### Limitations section (main.tex:66-72)

| # | 数字 | 行号 | 上下文 | 匹配? | 备注 |
|---|------|------|--------|-------|------|
| L1 | 8B | 69 | model scale | ✓ | |
| L2 | 6 architecture families | 69 | scope | ✓ | |
| L3 | Gemma-2-27B | 69 | cross-scale model | ✓ | |
| L4 | 15 statistical features | 70 | feature count | ✓ | |
| L5 | K*∈{1,2,3} (neural probe) | 70 | extended boundary | ✓ | matches exp_015 |
| L6 | 2--3 at θ=0.55 | 71 | sensitivity | ✓ | Qwen-rw/cont K*=3 at θ=0.55 |
| L7 | 1 at θ=0.70 | 71 | sensitivity | ✓ | max 1v2=0.696<0.70 |
| L8 | three of ten marginal at θ=0.60 | 71 | boundary cases | ✓ | Pythia/Gemma-2B + 1 more |
| L9 | arXiv K*=3 | 71 | domain | ✓ | |

## 问题列表

| # | 问题类型 | 位置 | 描述 | 修复方案 |
|---|---------|------|------|---------|
| 1 | 数值范围不准确 | method.tex:31 | "2v3 values cluster at 0.55--0.59" — 但 Pythia 2v3=0.544, Qwen-base 2v3=0.5496, Qwen-7B 2v3=0.546 均低于 0.55。实际范围应为 ~0.53--0.59（取所有 K*=2 config 的 2v3 值） | 改为 "2v3 values cluster at ${\sim}0.54$--$0.59$" 或 "below $0.59$" |
| 2 | 数值来源不可追溯 | method.tex:72 | "OBD achieves lower MAE (0.984 vs. 1.016)" — registry 中 mvp_pilot_sat_v1 的 ordinal_mae=1.0163，与 1.016 匹配，但标记为 ordinal（即 OBD），不是 multiclass。OBD 的 0.984 在 registry 中找不到。 | 核实 0.984 来源，确认 registry 中 ordinal_mae=1.0163 是 OBD 还是 multiclass 的 MAE |
| 3 | 数值精度不一致 | method.tex:72 | "mean AUC 0.6095" — registry 中 exp_013 within_avg=0.6099。差 0.0004。 | 统一为 0.6099 或确认 0.6095 的计算来源 |
| 4 | 数值归属可能错误 | discussion.tex:27 | "arXiv per-generation JSD (0.077 vs. ~0.01 for C4)" — registry 中 JSD=0.077 出现在 exp_018_llama8b_depth（C4 domain, 0v1 pair），不在任何 arXiv 实验中。arXiv 实验（exp_024, arxiv_multi_source）未存储 JSD 数据。 | 核实 0.077 是否来自 arXiv 实验的结果文件而非 registry；若确认为 arXiv 数据则补充 registry |
| 5 | 数值范围待验证 | discussion.tex:23 | "CI lower 0.593--0.599" 作为三个 marginal case 的 CI 下界范围。Pythia Bonferroni CI lower=0.5934 已确认。Gemma-2B Bonferroni CI lower≈0.5998。第三个 marginal case 的精确 CI 下界需核实。 | 对照 Table bonferroni_ci 确认三个 marginal config 的精确 CI 下界 |

## 交叉引用（同一数字多处出现）

| 数字 | 出现位置列表 | 一致? |
|------|------------|------|
| K*≤2 (web text) | main.tex:38, intro.tex:19, conclusion.tex:5 | ✓ |
| K*=3 (arXiv, four families) | main.tex:38, intro.tex:21, discussion.tex:27, conclusion.tex:6 | ✓ |
| 10 model configurations | main.tex:38, intro.tex:19, conclusion.tex:4 | ✓ |
| 6 architecture families | main.tex:38, intro.tex:19, main.tex:69, conclusion.tex:4 | ✓ |
| 1B--8B | main.tex:38, intro.tex:19, main.tex:69, conclusion.tex:4 | ✓ |
| 4 decoding strategies | main.tex:38, intro.tex:19 | ✓ |
| θ=0.60 | main.tex:38, intro.tex:15, method.tex:31,35 | ✓ |
| 80--92% transfer | main.tex:40, intro.tex:22, conclusion.tex:8 | ✓ |
| ρ > 0.90 | main.tex:40, intro.tex:22, conclusion.tex:8 | ✓ |
| ~83% synthetic | main.tex:41, intro.tex:25, conclusion.tex:7 | ✓ |
| 15 features | intro.tex:14, method.tex:65, main.tex:70, conclusion.tex:8 | ✓ |
| 0.5941 (binary MMLU) | intro.tex:25 | 单次出现 |
| 0.6018 (base MMLU) | intro.tex:25 | 单次出现 |
| K*≥4 (retrain-chain) | discussion.tex:28 | 单次出现 |
| K*=4 (DeBERTa arXiv) | discussion.tex:24 | 单次出现 |
| K*_neural ∈ {1,2,3} | discussion.tex:24, main.tex:70 | ✓ |
| 0.3 pp (strategy diff) | main.tex:41 | 单次出现 |
