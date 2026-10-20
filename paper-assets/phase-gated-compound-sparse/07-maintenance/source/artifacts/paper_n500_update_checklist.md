# Paper n=500 Update Checklist

> Generated 2026-05-15. Covers all .tex files in `artifacts/_project/paper/`.
> "Current" = n=50 era values. "Replace with" = description of n=500 data source needed.

---

## 1. abstract.tex

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 6 | `using 50 MATH-500 problems` | `500 MATH-500 problems` |
| 7 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | DeepSeek n=500 importance Δ at s=0.15..0.30 |
| 7 | `$d_z$ growing from $0.44$ (small) to $0.80$ (large)` | DeepSeek n=500 Cohen's d_z at s=0.15..0.30 |
| 7 | `$p < 0.005$ at all four sparsity levels` | DeepSeek n=500 permutation p-values (likely still < 0.005 with more power) |
| 8 | `$\widetilde{\Delta} = \placeholder{}$` — Qwen random s=0.30 median diff | Qwen n=500 random s=0.30 Δ̃ |
| 9 | `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` (high-phase crossover) | DeepSeek n=500 II_high at s=0.25 (importance vs random) |
| 9 | `$7.196$ vs.\ $1.363$` (low-phase crossover) | DeepSeek n=500 II_low at s=0.25 (importance vs random) |
| 10 | `$d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$` | Qwen n=500 d_z, Spearman ρ, gradient permutation p |
| 10 | `$\widetilde{\Delta}$: $0.020 \to 0.356$; $s{=}0.30$ Wilcoxon $p_{\text{Bonf}}{=}0.029$` | LLaMA n=500 (if rerun; otherwise keep n=50 with caveat) |

---

## 2. methodology.tex

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 10 | `We use 50 problems stratified from MATH-500` | `500 problems from MATH-500` (or `the full MATH-500 set`) |
| 22 | `All tests yield $p_{\text{Bonf}} < 0.005$ at every sparsity level` | Verify with n=500 data; likely still holds or strengthens |

---

## 3. results.tex

### §5.1 Strategy-Dependent Severity (Tab 1)

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 8 | `$\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification` | DeepSeek n=500 aggregate Δ values + ratio |
| 8 | `$-0.02$ to $1.54$` (random Δ range) | DeepSeek n=500 random Δ values |
| 13 | `$n{=}50$ MATH-500 problems` (Tab 1 caption) | `$n{=}500$` |
| 19 | `0.39 & 1.48 & 7.16 & 14.59` (Importance row) | DeepSeek n=500 importance Δ |
| 20 | `0.01 & $-$0.02 & 0.54 & 1.54` (Random row) | DeepSeek n=500 random Δ |

### §5.2 Phase-Modulated Amplification (Tab 2 + Fig 1)

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 29 | `$G$ increases from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$` | DeepSeek n=500 G values |
| 29 | `$\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$` | DeepSeek n=500 II_high values |
| 29 | `$G \approx 0.9$--$1.7{\times}$` (random G range) | DeepSeek n=500 random G values |
| 34 | `50 problems` (Tab 2 caption) | `500 problems` |
| 40 | `0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$` (s=0.15 imp) | n=500 values |
| 41 | `0.093 & 0.097 & 0.103 & 0.01 & 1.1` (s=0.15 rand) | n=500 values |
| 43 | `0.015 & 0.203 & 1.496 & 1.48 & $\mathbf{103}$` (s=0.20 imp) | n=500 values |
| 44 | `0.292 & 0.350 & 0.276 & $-$0.02 & 0.9` (s=0.20 rand) | n=500 values |
| 46 | `0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$` (s=0.25 imp) | n=500 values |
| 47 | `0.818 & 0.932 & 1.363 & 0.54 & 1.7` (s=0.25 rand) | n=500 values |
| 49 | `0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$` (s=0.30 imp) | n=500 values |
| 50 | `2.503 & 2.592 & 4.041 & 1.54 & 1.6` (s=0.30 rand) | n=500 values |
| 58 | Fig 1 caption: `$69{\times}$ to $274{\times}$` | n=500 G range |

### §5.3 Phase-Strategy Crossover

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 66 | `$0.032$ vs.\ $0.818$` and `$7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal` | DeepSeek n=500 crossover values at s=0.25 |

### §5.4 Cross-Model Replication

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 71 | `$\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$` | Qwen n=500 Δ values |
| 71 | `${\sim}1/5$ the magnitude` | Recalculate ratio with n=500 |
| 71 | `$d_z{=}0.28$, CI includes zero` (s=0.15 marginal) | Qwen n=500 d_z at s=0.15; check if still marginal |
| 71 | `$d_z \geq 0.55$` (s≥0.20) | Qwen n=500 d_z |
| 71 | `\placeholder{NULL\_PCT}\%` (Qwen mid-phase null rate) | Qwen n=500 mid-phase null rate |
| 71 | `Spearman $\rho = 1.0$; gradient permutation $p = 0.043$` | Qwen n=500 Spearman ρ and gradient permutation p |

### §5.5 Cross-Architecture Validation

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 77 | `$n{=}49$ paired problems` | LLaMA n=500 paired problem count |
| 79 | `$[0.002, 0.043]$` (s=0.15 CI) | LLaMA n=500 bootstrap CI at s=0.15 |
| 79 | `$p_{\text{Bonf}}{=}0.219$` (s=0.15 Wilcoxon) | LLaMA n=500 |
| 79 | `$[-0.069, 0.544]$` (s=0.30 CI) | LLaMA n=500 |
| 79 | `$p_{\text{Bonf}}{=}0.029$` (s=0.30 Wilcoxon) | LLaMA n=500 |
| 79 | `$\widetilde{\Delta}$: $0.020 \to 0.356$` (monotonic increase) | LLaMA n=500 |
| 81 | `${\sim}40{\times}$ smaller ... ${\sim}7{\times}$ smaller` | Recalculate ratios with n=500 |
| 81 | `Wilcoxon $p < \placeholder{}$` (LLaMA random s=0.30) | LLaMA n=500 random Wilcoxon p |
| 86 | `$n{=}\placeholder{N\_LLAMA}$` (table caption) | LLaMA n=500 paired count |
| 92-95 | All `\placeholder{}` in LLaMA table | LLaMA n=500 Δ̃, CI, p_Bonf at all 4 sparsity levels |

### §5.6 Statistical Validation (Tab 3 + Tab 4)

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 104 | `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` (permutation Δ) | DeepSeek n=500 permutation test observed Δ |
| 106 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` (DeepSeek d_z) | DeepSeek n=500 d_z |
| 106 | `$d_z{=}0.28$` (Qwen s=0.15); `$d_z \geq 0.55$` | Qwen n=500 d_z |
| 106 | `$d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$` (QW vs DS at s≥0.25) | n=500 d_z comparison |
| 117 | `0.44 & 0.32\; $[0.20, 0.47]$ & 0.28 & 0.05\; $[-0.01, 0.11]$` (s=0.15 row) | n=500 d_z and Δ̃ CI for both models |
| 118 | `0.52 & 1.15\; $[0.66, 1.26]$ & 0.55 & 0.21\; $[0.07, 0.40]$` (s=0.20 row) | n=500 |
| 119 | `0.68 & 3.97\; $[2.83, 5.29]$ & 0.89 & 1.11\; $[0.61, 1.47]$` (s=0.25 row) | n=500 |
| 120 | `0.80 & 9.94\; $[8.39, 16.65]$ & 1.02 & 2.62\; $[1.72, 3.65]$` (s=0.30 row) | n=500 |

---

## 4. introduction.tex

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 14 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | DeepSeek n=500 Δ |
| 14 | `$d_z$: $0.44 \to 0.80$` | DeepSeek n=500 d_z |
| 14 | `Bonferroni-corrected $p < 0.005$` | n=500 p-values |
| 15 | `$d_z \geq 0.55$` (Qwen) | Qwen n=500 d_z |
| 15 | `$\sim$1/40 the magnitude` (LLaMA ratio) | LLaMA n=500 ratio |

---

## 5. analysis.tex

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 4 | `$0.030$--$0.081$ (DeepSeek)` (ΔGini) | DeepSeek n=500 Gini deltas |
| 4 | `$0.010$--$0.020$ (Qwen)` (ΔGini) | Qwen n=500 Gini deltas |
| 6 | `$\Delta\mathcal{H} \in [-0.047, -0.040]$` (DeepSeek entropy) | DeepSeek n=500 entropy deltas |
| 6 | `$\Delta\mathcal{H} = +0.045$` (Qwen s=0.25 reversal) | Qwen n=500 entropy delta at s=0.25 |

---

## 6. discussion.tex

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 5 | `$69$--$274{\times}$` (G range) | n=500 G range |
| 5 | `$0.032$ vs.\ $0.818$` and `$7.196$ vs.\ $1.363$` (crossover) | n=500 crossover values |
| 10 | `\placeholder{ORACLE\_PCT}\%` | Oracle recovery % from pilot (may not change with n=500; verify) |
| 10 | `\placeholder{ORACLE\_P}` | Oracle Wilcoxon p |
| 10 | `\placeholder{HEUR\_PCT}\%` | Heuristic recovery % |
| 10 | `\placeholder{HEUR\_P}` | Heuristic Wilcoxon p |
| 15 | `${\sim}40{\times}$ smaller ... ${\sim}7{\times}$ smaller` (LLaMA ratios) | n=500 ratios |
| 15 | `$d_z \geq 1.0$` (LLaMA within-importance) | LLaMA n=500 |
| 15 | `Wilcoxon $p < \placeholder{}$` (LLaMA random) | LLaMA n=500 random Wilcoxon p |

---

## 7. conclusion.tex

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 4 | `$69{\times}$ to $274{\times}$` | n=500 G range |
| 4 | `$d_z$: $0.44 \to 0.80$` | DeepSeek n=500 d_z |
| 4 | `7/8 conditions non-significant` (random) | Verify with n=500 (could become 8/8 or stay 7/8) |
| 4 | `$d_z \geq 0.55$` (Qwen) | Qwen n=500 d_z |
| 4 | `$\sim$1/40 the magnitude` (LLaMA) | LLaMA n=500 ratio |

---

## 8. limitations.tex

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 2 | `$\sim$1/40 of DeepSeek` | LLaMA n=500 ratio |
| 2 | `only $s{=}0.30$ significant after Bonferroni correction` | LLaMA n=500 significance pattern |
| 45 | `$n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded)` | n=500 valid paired counts |
| 46 | `mean/median ratio ${\sim}1.6{:}1$ at $s{=}0.30$` | n=500 skewness stats |
| 47 | `CI lower bounds increasing from $0.19$ to $6.70$` | n=500 CI bounds |
| 47 | `$[6.70,\; 16.29]$` (s=0.30 CI) | n=500 CI at s=0.30 |

---

## 9. appendix_moved.tex

### App: Crossover Details

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 11 | `$0.032$ vs.\ $0.818$` and `$7.196$ vs.\ $1.363$---a $5.3{\times}$` | n=500 crossover values at s=0.25 |
| 11 | `$3.9{\times}$ at $s{=}0.15$, $5.4{\times}$ at $s{=}0.20$, $5.3{\times}$ at $s{=}0.25$, and $3.6{\times}$ at $s{=}0.30$` | n=500 reversal magnitudes at all 4 levels |
| 16 | Fig 3 caption: `$5.3{\times}$` | n=500 value |

### App: Cross-Model Replication Details

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 26 | `Four of the 50 problems are excluded ... $n{=}46$ valid problems for Qwen (vs.\ $n{=}49$ for DeepSeek)` | n=500 exclusion counts and valid n |
| 30 | `\placeholder{NULL\_PCT}\%` (Qwen null rate) | Qwen n=500 mid-phase null rate |
| 35 | `$n_{\text{total}} = \placeholder{N\_QW}$` (table caption) | Qwen n=500 total |
| 41-43 | All `\placeholder{}` in effective-n table (12 cells) | Qwen n=500 per-phase effective n (3 phases × 4 sparsity levels) |
| 59 | `0.39 & 1.48 & 7.16 & 14.59` (DeepSeek Δ in cross-model table) | DeepSeek n=500 Δ |
| 60 | `0.04 & 0.23 & 1.27 & 2.94` (Qwen Δ in cross-model table) | Qwen n=500 Δ |
| 73 | `median $\rho = \placeholder{}$, $p = \placeholder{}$` (concordance) | n=500 per-problem concordance ρ and p |
| 76 | `$\widetilde{\Delta} = \placeholder{}$` (Qwen random s=0.30) | Qwen n=500 random Δ̃ at s=0.30 |

### App: Permutation Test

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 84 | `$1.2{\times}$ ($s{=}0.15$) to $1.6{\times}$ ($s{=}0.30$)` (mean/median ratios DS) | DeepSeek n=500 skewness |
| 84 | `$1.1{\times}$ to $1.4{\times}$ for Qwen` | Qwen n=500 skewness |
| 86 | `$99.92$th percentile ... $p_{\text{Bonf}} = 0.0032$` | n=500 permutation percentile/p |
| 88 | `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` (observed Δ) | n=500 observed Δ |
| 88 | `$0.19 \to 0.69 \to 1.66 \to 6.70$` (CI lower bounds) | n=500 CI lower bounds |
| 93 | `$n{=}49$` (permutation table caption) | n=500 paired count |
| 99 | `0.37 & $[0.19,\; 0.62]$ & 0.0032` (s=0.15) | n=500 |
| 100 | `0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$` (s=0.20) | n=500 |
| 101 | `3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$` (s=0.25) | n=500 |
| 102 | `9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$` (s=0.30) | n=500 |

---

## 10. appendix_disc_analysis.tex

### App: Discrimination Collapse

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 4 | `$-0.031$ to $-0.073$` (DS random Gini) | DeepSeek n=500 random Gini deltas |
| 4 | `$-0.019$ to $-0.045$` (QW random Gini) | Qwen n=500 random Gini deltas |
| 11 | `$\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$` | n=500 II_high range |
| 11 | `$0.105$` (s=0.35 supplementary) | Verify if s=0.35 pilot was rerun |
| 14 | `$\widetilde{\Delta} = \placeholder{}$` (Qwen random) | Qwen n=500 random Δ̃ |
| 45 | `$n{=}49$ ... $n{=}46$` | n=500 valid counts |
| 46 | `mean/median ratio ${\sim}1.6{:}1$` and `median_diff=9.9436` | n=500 values |
| 47 | `$0.19$ to $6.70$` and `$[6.70,\; 16.29]$` | n=500 CIs |
| 49 | `$\widetilde{\Delta} = \placeholder{}$, bootstrap CI spanning zero` | Qwen n=500 random s=0.30 |

---

## 11. appendix.tex (Formulation)

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 38 | `$G_{\times} = 58$--$241{\times}$` (multiplicative null G) | Recompute with n=500 data if running multiplicative null verification |

---

## 12. appendix_results.tex (duplicates content from appendix_moved.tex)

| Line | Current Content | Replace With |
|------|----------------|-------------|
| 7 | `median $\rho = \placeholder{}$, $p = \placeholder{}$` | Same as appendix_moved L73 |
| 10 | `$\widetilde{\Delta} = \placeholder{}$` | Same as appendix_moved L76 |

**Note:** `appendix_results.tex` is not included in `main.tex`; may be an orphan duplicate. Verify whether to delete or keep in sync.

---

## 13. Entropy / Discrimination Metrics Tables (in appendix_moved.tex)

| Line | Table | Current Content | Replace With |
|------|-------|----------------|-------------|
| 132-135 | tab:discrimination-metrics-full | DS ΔGini: -0.030, -0.040, -0.065, -0.081; ΔCV: -0.56, -0.77, -1.29, -1.66 | DeepSeek n=500 |
| 137-140 | tab:discrimination-metrics-full | QW ΔGini: -0.010, -0.012, -0.010, -0.020; ΔCV: -0.05, -0.21, -1.49, -1.14 | Qwen n=500 |
| 172-175 | tab:entropy-deltas | DS ΔH: -0.040, -0.047, -0.045, -0.044 | DeepSeek n=500 |
| 177-180 | tab:entropy-deltas | QW ΔH: -0.073, -0.076, +0.045, -0.007 | Qwen n=500 |

*(These tables are in `appendix_moved.tex` lines 123-183)*

---

## 14. Figures (require regeneration from n=500 data)

| Figure | File | Description | Data Source |
|--------|------|-------------|-------------|
| Fig 1 | `fig1_dose_response.pdf` | G vs s curve (importance vs random) | DeepSeek n=500 experiment_summary_table |
| Fig 3 | `fig3_crossover.pdf` | Crossover bar chart at s=0.25 | DeepSeek n=500 II per phase |
| Fig 4 | `fig4_bootstrap.pdf` | Forest plot of permutation test | DeepSeek n=500 permutation_test_results |
| Fig 5 | `fig5_crossmodel.pdf` | Cross-model Δ comparison | DeepSeek + Qwen n=500 Δ |

---

## 15. Reviewer-Related Updates

### W2: Statistical Power
- n=500 directly addresses W2 (statistical power concern). Update:
  - **methodology.tex L10**: sample size 50 → 500
  - **limitations.tex L45**: paired n counts
  - All CI widths should narrow substantially → update all CI values
  - If any previously marginal results (Qwen s=0.15 d_z=0.28) become significant, update narrative accordingly

### W5: Qwen Mid-Phase Null Rate
- **results.tex L71**: `\placeholder{NULL_PCT}` → Qwen n=500 null rate (was ~45.2% at n=50; recheck)
- **appendix_moved.tex L30**: same `\placeholder{NULL_PCT}`
- **appendix_moved.tex L35, L41-43**: Per-phase effective-n table → fill with n=500 data
- If null rate drops substantially at n=500, update the caveat language in results.tex L71

---

## 16. Conditional Updates (depend on n=500 results)

These items may or may not need textual changes depending on how n=500 results compare:

| Item | Condition | Action if True |
|------|-----------|---------------|
| "7/8 conditions non-significant" (random) | Random results change at n=500 | Update count in abstract L8, conclusion L4, introduction L16 |
| Qwen s=0.15 marginal ($d_z=0.28$, CI includes zero) | Becomes significant at n=500 | Remove "marginal" caveat in results L71, L106, Tab 4, conclusion |
| LLaMA "mixed evidence" narrative | LLaMA results clarify at n=500 | Rewrite results.tex L77-81, discussion.tex L15, limitations L2-3 |
| "~1/5 magnitude" (Qwen/DS ratio) | Ratio changes at n=500 | Update results L71, appendix_moved L48/L68 |
| "~1/40 magnitude" (LLaMA/DS ratio) | Ratio changes at n=500 | Update abstract L10, intro L15, discussion L15, conclusion L4 |
| C8 LLaMA "qualitative consistent" qualifier | Evidence strengthens/weakens | Adjust qualifier strength throughout |

---

## Summary Statistics

- **Total locations requiring numerical update**: ~120+
- **Placeholder values already marked** (`\placeholder{}`): ~30
- **Hard-coded n=50 values needing replacement**: ~90
- **Figures to regenerate**: 4
- **Files affected**: 11 of 15 .tex files (background.tex, related_work.tex, main.tex, appendix_results.tex not substantively affected)
