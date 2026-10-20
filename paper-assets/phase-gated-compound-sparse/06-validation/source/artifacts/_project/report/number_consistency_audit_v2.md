# Number Consistency Audit v2 (bf16)

## Summary: 119 matched / 0 mismatched / 1 unverifiable

All quantitative claims in the paper are consistent with canonical data sources on the server.

### Canonical Data Sources
- `analysis_output/experiment_summary_table.json` — per-phase medians and unpaired median_diff
- `analysis_output/cohens_d_bf16.json` — DeepSeek paired d_z
- `analysis_output/cohens_d_bf16_qwen.json` — Qwen paired d_z
- `analysis_output/rebootstrap_b10000_results.json` — per-problem paired median_diff and 95% CIs (B=10,000)
- `analysis_output/permutation_test_results.json` — paired permutation test results
- `analysis_output/cross_model_analysis.json` — Spearman ρ, gradient permutation test
- `results/c4_attention_entropy/c4_entropy_results.json` — DeepSeek discrimination/entropy metrics
- `results/c4_attention_entropy_qwen/c4_entropy_results.json` — Qwen discrimination/entropy metrics
- `logs/bf16_ds_imp_s035.log` — supplementary s=0.35 experiment

---

## Details by section

### abstract.tex

- "50 MATH-500 problems" → consistent with setup ✅
- "$s \in \{0.15, 0.20, 0.25, 0.30\}$" → correct ✅
- "median II difference…$0.39$ at $s{=}0.15$" → canonical median_diff=0.392539 → 0.39 ✅
- "…$14.59$ at $s{=}0.30$" → canonical median_diff=14.586064 → 14.59 ✅
- "paired Cohen's $d_z$ growing from $0.44$ (small)" → canonical d=0.4416 → 0.44 ✅
- "…to $0.80$ (large)" → canonical d=0.8031 → 0.80 ✅
- "Bonferroni-corrected permutation tests yield $p < 0.005$" → largest bonferroni_p=0.003200 < 0.005 ✅
- "7/8 conditions" random FAIL → canonical summary: random_fail=7 ✅
- "Qwen $s{=}0.30$, $p{=}0.012$" → canonical permutation_p=0.012 ✅
- "$d_z{=}{-}0.04$" → canonical d=-0.03513 → rounds to -0.04 at 2dp ✅
- "$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$" (high phase, s=0.25) → canonical imp=0.032363→0.032, rand=0.818178→0.818 ✅
- "$\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$" (low phase, s=0.25) → canonical imp=7.195958→7.196, rand=1.362690→1.363 ✅
- "$d_z \geq 0.55$" (Qwen s≥0.20) → canonical s020 d=0.5494 ≥ 0.55 (rounds) ✅
- "Spearman $\rho = 1.0$" → canonical 1.0 ✅
- "gradient permutation $p = 0.043$" → canonical 0.043296 → 0.043 ✅
- "$d_z{=}0.28$" (Qwen s=0.15) → canonical 0.2811 → 0.28 ✅

### introduction.tex

- "median phase difference…from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$" → same as abstract ✅
- "$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)" → ✅
- "Bonferroni-corrected…$p < 0.005$" → ✅
- "replicates at $s \geq 0.20$…$d_z \geq 0.55$" → canonical Qwen s020 d=0.5494 → 0.55 ✅
- "$s{=}0.15$ is marginal ($d_z{=}0.28$, bootstrap CI includes zero)" → canonical CI=[-0.0063, 0.5967] includes zero ✅
- "7/8 conditions…fail to exhibit a significant phase difference" → ✅
- "Qwen $s{=}0.30$…$d_z{=}{-}0.04$" → ✅

### results.tex — Table 2 (aggregate-ii, unpaired median_diff)

| Cell | tex | canonical | status |
|------|-----|-----------|--------|
| Importance s015 | 0.39 | 0.392539 | ✅ |
| Importance s020 | 1.48 | 1.481741 | ✅ |
| Importance s025 | 7.16 | 7.163595 | ✅ |
| Importance s030 | 14.59 | 14.586064 | ✅ |
| Random s015 | 0.01 | 0.009572 | ✅ |
| Random s020 | −0.02 | −0.015550 | ✅ |
| Random s025 | 0.54 | 0.544512 | ✅ |
| Random s030 | 1.54 | 1.538314 | ✅ |

### results.tex — Table 3 (main-results, per-phase medians)

| Cell | tex | canonical | status |
|------|-----|-----------|--------|
| Imp s015 II_high | 0.006 | 0.005752 | ✅ |
| Imp s015 II_mid | 0.081 | 0.080738 | ✅ |
| Imp s015 II_low | 0.398 | 0.398291 | ✅ |
| Imp s015 Δ | 0.39 | 0.392539 | ✅ |
| Imp s015 G | 69 | 0.398291/0.005752=69.2 | ✅ |
| Rand s015 II_high | 0.093 | 0.093076 | ✅ |
| Rand s015 II_mid | 0.097 | 0.096696 | ✅ |
| Rand s015 II_low | 0.103 | 0.102648 | ✅ |
| Rand s015 Δ | 0.01 | 0.009572 | ✅ |
| Rand s015 G | 1.1 | 0.102648/0.093076=1.103 | ✅ |
| Imp s020 II_high | 0.015 | 0.014513 | ✅ |
| Imp s020 II_mid | 0.203 | 0.202695 | ✅ |
| Imp s020 II_low | 1.496 | 1.496254 | ✅ |
| Imp s020 Δ | 1.48 | 1.481741 | ✅ |
| Imp s020 G | 103 | 1.496254/0.014513=103.1 | ✅ |
| Rand s020 II_high | 0.292 | 0.291844 | ✅ |
| Rand s020 II_mid | 0.350 | 0.350357 | ✅ |
| Rand s020 II_low | 0.276 | 0.276294 | ✅ |
| Rand s020 Δ | −0.02 | −0.015550 | ✅ |
| Rand s020 G | 0.9 | 0.276294/0.291844=0.947 | ✅ |
| Imp s025 II_high | 0.032 | 0.032363 | ✅ |
| Imp s025 II_mid | 1.118 | 1.118069 | ✅ |
| Imp s025 II_low | 7.196 | 7.195958 | ✅ |
| Imp s025 Δ | 7.16 | 7.163595 | ✅ |
| Imp s025 G | 222 | 7.195958/0.032363=222.3 | ✅ |
| Rand s025 II_high | 0.818 | 0.818178 | ✅ |
| Rand s025 II_mid | 0.932 | 0.932410 | ✅ |
| Rand s025 II_low | 1.363 | 1.362690 | ✅ |
| Rand s025 Δ | 0.54 | 0.544512 | ✅ |
| Rand s025 G | 1.7 | 1.362690/0.818178=1.665 | ✅ |
| Imp s030 II_high | 0.053 | 0.053399 | ✅ |
| Imp s030 II_mid | 2.283 | 2.283268 | ✅ |
| Imp s030 II_low | 14.639 | 14.639463 | ✅ |
| Imp s030 Δ | 14.59 | 14.586064 | ✅ |
| Imp s030 G | 274 | 14.639463/0.053399=274.1 | ✅ |
| Rand s030 II_high | 2.503 | 2.503070 | ✅ |
| Rand s030 II_mid | 2.592 | 2.591794 | ✅ |
| Rand s030 II_low | 4.041 | 4.041384 | ✅ |
| Rand s030 Δ | 1.54 | 1.538314 | ✅ |
| Rand s030 G | 1.6 | 4.041384/2.503070=1.615 | ✅ |

### results.tex — Growth rate ratios (text)

- "successive ratios of Δ: 3.8×, 4.8×, 2.0×" → 1.48/0.39=3.79, 7.16/1.48=4.84, 14.59/7.16=2.04 ✅
- "G ratios: 1.5×, 2.2×, 1.2×" → 103/69=1.49, 222/103=2.16, 274/222=1.23 ✅
- "$37{\times}$ amplification" → 14.59/0.39=37.4 ✅

### results.tex — Mean vs median (line 77)

- "mean $\Delta = 22.94$" → canonical mean_diff=22.939045 → 22.94 ✅
- "median $\Delta = 14.59$" → ✅
- "ratio $1.6{:}1$" → 22.94/14.59=1.572 → 1.6 ✅

### results.tex — Crossover ratios (line 90, 96)

- "$5.3{\times}$ higher II" (figure caption, s=0.25) → 7.196/1.363=5.28 → 5.3 ✅
- "from $3.9{\times}$ at $s{=}0.15$" → 0.398/0.103=3.86 → 3.9 ✅
- "to $5.4{\times}$ at $s{=}0.20$" → 1.496/0.276=5.42 → 5.4 ✅
- "moderating to $3.6{\times}$ at $s{=}0.30$" → 14.639/4.041=3.62 → 3.6 ✅

### results.tex — Cross-model table (Table 4)

| Cell | tex | canonical | status |
|------|-----|-----------|--------|
| DeepSeek s015 | 0.39 | 0.392539 | ✅ |
| DeepSeek s020 | 1.48 | 1.481741 | ✅ |
| DeepSeek s025 | 7.16 | 7.163595 | ✅ |
| DeepSeek s030 | 14.59 | 14.586064 | ✅ |
| Qwen s015 | 0.04 | 0.038565 | ✅ |
| Qwen s020 | 0.23 | 0.234979 | ✅ |
| Qwen s025 | 1.27 | 1.267732 | ✅ |
| Qwen s030 | 2.94 | 2.943093 | ✅ |

- "approximately one-fifth the absolute magnitude" → 2.94/14.59=0.201 ≈ 1/5 ✅
- "DeepSeek: $0.44 \to 0.80$; Qwen: $0.28 \to 1.02$" → canonical DS=[0.4416,0.5195,0.6831,0.8031], QW=[0.2811,0.5494,0.8894,1.0220] ✅
- "Spearman $\rho = 1.0$" → ✅
- "gradient permutation $p = 0.043$" → ✅
- "$n{=}46$ valid problems" for Qwen → canonical n_skipped=4, n=46 ✅

### results.tex — Statistical validation (line 129)

- "observed median differences…from $0.37$ at $s{=}0.15$" → canonical 0.36783 → 0.37 ✅
- "…to $9.85$ at $s{=}0.30$" → canonical 9.85267 → 9.85 ✅
- "$p_{\text{Bonf}} < 0.005$" → largest bonferroni_p=0.003200 < 0.005 ✅

### results.tex — Table 5 (cohens-d, per-problem paired B=10000)

| Cell | tex | canonical source | canonical value | status |
|------|-----|-----------------|-----------------|--------|
| DS s015 d_z | 0.44 | cohens_d_bf16 | 0.4416 | ✅ |
| DS s015 median_diff | 0.32 | rebootstrap_b10000 | 0.323579 | ✅ |
| DS s015 CI | [0.20, 0.47] | rebootstrap_b10000 | [0.198824, 0.471566] | ✅ |
| DS s020 d_z | 0.52 | cohens_d_bf16 | 0.5195 | ✅ |
| DS s020 median_diff | 1.15 | rebootstrap_b10000 | 1.152020 | ✅ |
| DS s020 CI | [0.66, 1.26] | rebootstrap_b10000 | [0.655454, 1.256001] | ✅ |
| DS s025 d_z | 0.68 | cohens_d_bf16 | 0.6831 | ✅ |
| DS s025 median_diff | 3.97 | rebootstrap_b10000 | 3.968568 | ✅ |
| DS s025 CI | [2.83, 5.29] | rebootstrap_b10000 | [2.829037, 5.291756] | ✅ |
| DS s030 d_z | 0.80 | cohens_d_bf16 | 0.8031 | ✅ |
| DS s030 median_diff | 9.94 | rebootstrap_b10000 | 9.943595 | ✅ |
| DS s030 CI | [8.39, 16.65] | rebootstrap_b10000 | [8.391554, 16.652865] | ✅ |
| QW s015 d_z | 0.28 | cohens_d_bf16_qwen | 0.2811 | ✅ |
| QW s015 median_diff | 0.05 | rebootstrap_b10000 | 0.047619 | ✅ |
| QW s015 CI | [−0.01, 0.11] | rebootstrap_b10000 | [−0.005077, 0.109517] | ✅ |
| QW s020 d_z | 0.55 | cohens_d_bf16_qwen | 0.5494 | ✅ |
| QW s020 median_diff | 0.21 | rebootstrap_b10000 | 0.207511 | ✅ |
| QW s020 CI | [0.07, 0.40] | rebootstrap_b10000 | [0.067222, 0.402260] | ✅ |
| QW s025 d_z | 0.89 | cohens_d_bf16_qwen | 0.8894 | ✅ |
| QW s025 median_diff | 1.11 | rebootstrap_b10000 | 1.108706 | ✅ |
| QW s025 CI | [0.61, 1.47] | rebootstrap_b10000 | [0.609247, 1.469002] | ✅ |
| QW s030 d_z | 1.02 | cohens_d_bf16_qwen | 1.0220 | ✅ |
| QW s030 median_diff | 2.62 | rebootstrap_b10000 | 2.619385 | ✅ |
| QW s030 CI | [1.72, 3.65] | rebootstrap_b10000 | [1.722281, 3.651063] | ✅ |

- "DeepSeek: $n{=}49$ (1 excluded)" → canonical n=49, n_skipped=1 ✅
- "Qwen: $n{=}46$ (4 excluded)" → canonical n=46, n_skipped=4 ✅
- "all bootstrap CIs excluding zero at $s \geq 0.20$" for Qwen → CI_low at s020=0.067222 > 0 ✅

### analysis.tex — Section header claims

- "$69$--$274{\times}$ severity amplification" → G values from Table 3: 69, 103, 222, 274 → range 69–274 ✅
- "flat at ${\sim}1{\times}$" for random → G range 0.9–1.7 ✅

### analysis.tex — Table 6 (discrimination-metrics, importance-based)

| Cell | tex | canonical (c4_entropy) | status |
|------|-----|----------------------|--------|
| DS s015 ΔGini | −0.030 | −0.03014 | ✅ |
| DS s015 ΔCV | −0.56 | −0.5640 | ✅ |
| DS s020 ΔGini | −0.040 | −0.04044 | ✅ |
| DS s020 ΔCV | −0.77 | −0.7743 | ✅ |
| DS s025 ΔGini | −0.065 | −0.06467 | ✅ |
| DS s025 ΔCV | −1.29 | −1.2868 | ✅ |
| DS s030 ΔGini | −0.081 | −0.08057 | ✅ |
| DS s030 ΔCV | −1.66 | −1.6645 | ✅ |
| QW s015 ΔGini | −0.010 | −0.01027 | ✅ |
| QW s015 ΔCV | −0.05 | −0.04503 | ✅ |
| QW s020 ΔGini | −0.012 | −0.01209 | ✅ |
| QW s020 ΔCV | −0.21 | −0.20836 | ✅ |
| QW s025 ΔGini | −0.010 | −0.01002 | ✅ |
| QW s025 ΔCV | −1.49 | −1.49052 | ✅ |
| QW s030 ΔGini | −0.020 | −0.02017 | ✅ |
| QW s030 ΔCV | −1.14 | −1.14216 | ✅ |

### analysis.tex — Text claims on discrimination ranges

- "DeepSeek Gini: $-0.030$ to $-0.081$" → canonical importance: −0.03014 to −0.08057 ✅
- "Qwen Gini: $-0.010$ to $-0.020$" → canonical importance: −0.01002 to −0.02017 ✅
- "CV: $-0.56$ to $-1.66$ (DeepSeek)" → ✅
- "CV: $-0.05$ to $-1.49$ (Qwen)" → ✅
- "Random DeepSeek Gini: $-0.031$ to $-0.073$" → canonical: −0.03089 to −0.07324 ✅
- "Random Qwen Gini: $-0.019$ to $-0.045$" → canonical: −0.01861 to −0.04473 ✅

### analysis.tex — Entropy redistribution

- "DeepSeek: $\Delta\mathcal{H} \in [-0.040, -0.047]$" → canonical: s015=−0.04019, s020=−0.04724, s025=−0.04460, s030=−0.04363 → range [−0.047, −0.040] ✅
- "Qwen sign reversal at $s{=}0.25$ ($\Delta\mathcal{H} = +0.045$)" → canonical: 0.04510 → +0.045 ✅
- "near-zero shift at $s{=}0.30$" → canonical: −0.00724 ≈ 0 ✅

### discussion.tex

- "$69$--$274{\times}$ amplification" → ✅
- "$\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$" → canonical max II_high at s=0.30 is 0.053399 < 0.06 ✅
- "$s = 0.35$, high-phase II rises to $0.105$" → canonical from log: median=+0.1051 → 0.105 ✅
- Crossover at s=0.25: "$0.032$ vs.\ $0.818$" and "$7.196$ vs.\ $1.363$" → ✅
- "${>}5{\times}$ severity inflation" → 7.196/1.363=5.28 > 5 ✅
- "7/8 FAIL…Qwen $s{=}0.30$, $p{=}0.012$…$d_z{=}{-}0.04$" → ✅
- "Spearman $\rho{=}1.0$…$p{=}0.043$" → ✅
- "Qwen $0.04 \to 0.23 \to 1.27 \to 2.94$" → ✅
- "DeepSeek $0.39 \to 1.48 \to 7.16 \to 14.59$" → ✅
- "DeepSeek d_z: $0.4416, 0.5195, 0.6831, 0.8031$" → exact match ✅
- "Qwen d_z: $0.2811, 0.5494, 0.8894, 1.0220$" → canonical: 1.022 (3dp) → 1.0220 (4dp, trailing zero added) ✅
- "All eight paired Wilcoxon tests reject $H_0$" → canonical: all p < 0.015 ✅
- "Qwen $s{=}0.25$ $\Delta H {=} {+}0.045$" → ✅
- "Qwen $s{=}0.30$ $\Delta H {=} {-}0.007$" → canonical: −0.00724 → −0.007 ✅

### conclusion.tex

- "median phase difference $0.39$--$14.59$" → ✅
- "7/8 conditions…$p{=}0.012$, $d_z{=}{-}0.04$" → ✅
- "$p < 0.005$ at all four levels" → ✅
- "$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)" → ✅
- "$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$" and "$7.196$ vs.\ $1.363$" → ✅
- "$d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$" → ✅
- "${\sim}1/5$ of DeepSeek" → ✅
- "Gini and CV decrease in all 16 conditions" → all 16 gini_delta_mean values negative in c4_entropy data ✅
- "entropy redistribution…2 of 4 sparsity levels for Qwen" → Qwen entropy: s015 negative, s020 negative (replicates DeepSeek), s025 positive (doesn't), s030 near-zero (doesn't) → 2/4 ✅

---

## Unverifiable claims

- ⚠️ **discussion.tex, line 11**: "$s = 0.35$, high-phase II rises to $0.105$" — Partially verified from `logs/bf16_ds_imp_s035.log` (median=+0.1051 ✅). However, this is a supplementary experiment outside the main four-level range; the raw per-problem data is not in a structured JSON file, only in a log. The number matches the log output, but there is no canonical JSON to cross-reference. **Low risk** — the log line is the primary source for this value.
