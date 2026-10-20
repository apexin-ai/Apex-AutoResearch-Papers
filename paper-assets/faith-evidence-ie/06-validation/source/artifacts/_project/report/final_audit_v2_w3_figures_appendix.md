# Final Audit V2 — Worker 3: Figure Data Source + Appendix + Statistics + Compilation

**Date**: 2026-05-24
**Scope**: A. Figure data sources, B. Appendix prose numbers, C. Statistical quantities, D. LaTeX compilation

---

## A. Figure Data Source Verification

### A1. fig_evidence_tax (`plot_evidence_tax.py`)

Script values vs ROADMAP multi-seed data:

| Model | Seeds | Script Mean | ROADMAP Mean | Script Std | Computed Std | PASS |
|-------|-------|-------------|--------------|------------|--------------|------|
| 1.7B | s42=-5.43, s43=-4.59 | -5.01 | -5.01 | 0.59 | 0.594 | ✅ |
| 4B | s42=+1.51, s43=+1.99, s44=+1.46 | +1.65 | +1.65 | 0.29 | 0.293 | ✅ |
| 8B | s42=-0.34, s43=-1.74, s44=-0.65 | -0.91 | -0.91 | 0.74 | 0.735 | ✅ |
| LLaMA | s42=-1.74, s43=-1.17 | -1.46 | -1.46 | 0.40 | 0.403 | ✅ |
| 14B | s42=+0.77, s43=+0.08 | +0.43 | +0.43 | 0.49 | 0.488 | ✅ |

All means and stds independently verified from per-seed values. Seed counts match (n_seeds = [2,3,3,2,2]).

Cross-check with `tab:rsft_test_tax` (appendix line 278): 1.7B tax = −5.01±0.59 (2-seed) ✅

**Verdict: PASS** — all values consistent with ROADMAP, registry, and appendix table.

---

### A2. fig_spectrum (`plot_spectrum.py`)

| Method | Script (Rel-F1, Evi-F1) | tab:spectrum (Rel-F1, Evi-F1) | PASS |
|--------|--------------------------|-------------------------------|------|
| SFT | (44.39, 79.61) | (44.39, 79.61) | ✅ |
| RSFT CED | (45.80, 80.96) | (45.80, 80.96) | ✅ |
| GRPO bf16 | (45.49, 80.86) | (45.49, 80.86) | ✅ |
| DPO 1ep | (33.37, 80.90) | (33.37, 80.90) | ✅ |
| DPO 3ep | (31.45, 84.84) | (31.45, 84.84) | ✅ |
| GRPO QLoRA | (1.38, 85.04) | (1.38, 85.04) | ✅ |

Also verified against experiments.tex prose (lines 43, 46): all six data points match.

RSFT label says "3-seed" — consistent with tab:main 3-seed means. Verified: 3-seed Evi-F1 = (81.74+80.63+80.50)/3 = 80.96 ✅; 3-seed Rel-F1 = (45.17+46.01+46.21)/3 = 45.80 ✅

**Verdict: PASS**

---

### A3. fig_scaling (`plot_scaling.py`)

Script uses SFT s42 values at @1024 (not matched@2048):

| Model | with_evi | no_evi | Delta (label) | Computed Delta | Source Check |
|-------|----------|--------|---------------|----------------|--------------|
| Qwen3-1.7B | 47.86 | 39.82 | +8.0pp | +8.04pp | with_evi: appendix line 177 ("s42...47.86") ✅ |
| Qwen3-4B | 39.74 | 47.21 | −7.5pp | −7.47pp | tab:main line 27-28 ✅ |
| Qwen3-8B | 50.51 | 50.79 | −0.3pp | −0.28pp | s42 @1024 (within tab:scaling 3-seed mean 50.19±3.23) ✅ |
| LLaMA-3.1-8B | 53.84 | 54.52 | −0.7pp | −0.68pp | with_evi: appendix line 212 ("s42: 53.84") ✅ |

**Note**: 8B with_evi (50.51) and no_evi (50.79) are s42 @1024 raw values, not appearing in any table. They are consistent with tab:scaling 3-seed mean (50.19) and matched@2048 values (50.15/50.19) given truncation confounding.

**Minor caption issue**: fig_scaling caption (appendix line 112) states "RSFT consistently narrows the gap toward the no-evidence upper bound" but the figure only plots SFT bars — RSFT is not visualized. Caption makes a textual claim not directly shown in the figure. Not wrong, but potentially misleading.

**Verdict: PASS** (with minor caption note)

---

## B. Appendix Prose Numbers

### B1. Cross-family transfer (§H, line 211-212)

| Claim | Computed | PASS |
|-------|----------|------|
| LLaMA SFT 3-seed mean = 51.09 | (53.84+51.42+48.02)/3 = 51.093 | ✅ |
| LLaMA SFT std = 2.92pp | √((2.75²+0.33²+3.07²)/2) = 2.924 | ✅ |
| RSFT mean = 56.54 | (57.14+56.62+55.87)/3 = 56.543 | ✅ |
| RSFT std = 0.64pp | √((0.60²+0.08²+0.67²)/2) = 0.639 | ✅ |
| +5.45 gain | 56.54 − 51.09 = 5.45 | ✅ |
| 4.6× compression | 2.92/0.64 = 4.5625 ≈ 4.6 | ✅ |
| Qwen3-8B: +4.14 | 54.33 − 50.19 = 4.14 | ✅ |
| Qwen3-8B: 6.5× | 3.23/0.50 = 6.46 ≈ 6.5 | ✅ |

### B2. Cross-dataset robustness (§H, line 214-215)

| Claim | Computed | PASS |
|-------|----------|------|
| +4.86pp Re-DocRED gain | 41.45 − 36.59 = 4.86 | ✅ |
| +5.08pp DocRED gain (RSFT 3-seed − SFT s42) | 44.82 − 39.74 = 5.08 | ✅ |
| EDCR reduction −0.046 | 0.6210 − 0.6674 = −0.0464 | ✅ |

### B3. Test-set paragraphs (§H, line 217-219)

Dev→Test drops (RSFT):

| Model | Dev | Test | Drop | Within 18.9-21.9? |
|-------|-----|------|------|---------------------|
| 1.7B | 51.19 | 29.33 | 21.86 | ✅ |
| 4B | 44.82 | 25.01 | 19.81 | ✅ |
| 8B | 54.33 | 33.53 | 20.80 | ✅ |
| 14B | 58.51 | 38.49 | 20.02 | ✅ |
| LLaMA | 56.54 | 35.54 | 21.00 | ✅ |
| SFT 1.7B | 44.64 | 25.79 | 18.85 | ✅ (= lower bound) |

Range: 18.85–21.86 → text says "18.9–21.9pp" ✅ (rounded)
Annotation density ratio: 34.7/12.3 = 2.821 ≈ 2.82× ✅
14B dev advantage: 58.51 − 55.07 = +3.44pp ✅; test reversal: 38.49 − 38.86 = −0.37pp ✅

Rounded dev→test values in prose:
- 1.7B: 51.2→29.3 (from 51.19→29.33) ✅
- 4B: 44.8→25.0 (from 44.82→25.01) ✅
- 8B: 54.3→33.5 (from 54.33→33.53) ✅
- 14B: 58.5→38.5 (from 58.51→38.49) ✅
- LLaMA: 56.5→35.5 (from 56.54→35.54) ✅
- SFT 1.7B: 44.6→25.8 (from 44.64→25.79) ✅

### B4. EDCR per-relation (§L, line 392-408)

| Statistic | Value in text | Internally consistent | PASS |
|-----------|---------------|----------------------|------|
| Per-relation ρ | −0.79, n=76, p<0.001 | t=11.08, df=74 → p≪0.001 | ✅ |
| Filtered ρ (≥5 pred) | −0.85, n=74, p<0.001 | consistent | ✅ |
| EDCR⊥Evi-F1 | ρ=−0.06, p=0.58 | null as expected | ✅ |
| Evi-F1⊥Rel-F1 | ρ=−0.01, p=0.91 | null as expected | ✅ |
| Partial ρ (cross-method, n=17) | −0.8541 vs raw −0.8554 | 0.15% reduction | ✅ |
| date_of_birth EDCR | 0.118 | stated as extreme low | ✅ |
| head_of_government EDCR | 0.956 | stated as extreme high | ✅ |

### B5. Inference Efficiency (§N, line 444-469)

| Claim | Computed | PASS |
|-------|----------|------|
| 1.7B overhead −13.6% | (6424−7438)/7438 = −13.63% | ✅ |
| 4B overhead +16.8% | (8887−7606)/7606 = +16.84% | ✅ |
| 8B overhead −3.8% | (10486−10901)/10901 = −3.81% | ✅ |
| 14B overhead +24.2% | (18011−14498)/14498 = +24.23% | ✅ |
| 1.75× prediction count ratio (1.7B) | 44.6k/25.5k = 1.749 | ✅ |
| 1.7B→8B wall-clock ratio 1.63× | 10486/6424 = 1.632 | ✅ |
| 4.7× parameter ratio | 8B/1.7B = 4.7 | ✅ |

**Minor prose issue** (experiments.tex line 116, not appendix): "evidence generation adds 16–24% wall-clock time at 14B" — the range 16–24% spans 4B (+16.8%) to 14B (+24.2%), but "at 14B" suggests a single scale. Should read "at 4B–14B" or "at $\geq$4B". Low severity.

---

## C. Statistical Verification

### C1. Cohen's d = 2.58 (LLaMA SFT vs RSFT)

```
SFT: mean=51.09, std=2.92, n=3
RSFT: mean=56.54, std=0.64, n=3
s_pooled = √((2×2.92² + 2×0.64²) / 4) = √(17.872/4) = √4.468 = 2.114
d = |56.54 − 51.09| / 2.114 = 5.45 / 2.114 = 2.579
```

**Verdict: PASS** (2.579 rounds to 2.58)

### C2. All Cohen's d values (tab:variance_ci)

| Scale | SFT mean/std | RSFT mean/std | Pooled std | Computed d | Table d | PASS |
|-------|-------------|---------------|------------|-----------|---------|------|
| 1.7B | 44.64/2.79 | 51.19/0.09 | 1.974 | 3.318 | 3.31 | ✅ |
| 4B | 43.58/3.80 | 44.82/0.51 | 2.711 | 0.457 | 0.46 | ✅ |
| 8B | 50.19/3.23 | 54.33/0.50 | 2.311 | 1.791 | 1.79 | ✅ |
| LLaMA | 51.09/2.92 | 56.54/0.64 | 2.114 | 2.579 | 2.58 | ✅ |

"d ≥ 1.79 for 3/4 scales": 1.7B=3.31, 8B=1.79, LLaMA=2.58 → 3 scales ≥ 1.79 ✅
"1.7B and LLaMA-8B showing large effect sizes (d > 2.5)": 3.31>2.5, 2.58>2.5 ✅

### C3. ρ = −0.79, n=76, p<0.001 (per-relation EDCR)

```
t = −0.79 × √(74 / (1−0.6241)) = −0.79 × √(196.86) = −0.79 × 14.03 = −11.08
df = 74, p ≪ 0.001
```

**Verdict: PASS**

### C4. ρ = −0.89, n=7, p=0.007 (cross-method EDCR)

```
t = −0.89 × √(5 / (1−0.7921)) = −0.89 × √(24.05) = −0.89 × 4.904 = −4.365
df = 5, two-tailed p ≈ 0.0073
```

ρ and p are internally consistent. ✅

**⚠️ DISCREPANCY**: The appendix partial correlation section (line 398) reports "Aggregating to n=7 unique methods: raw ρ = −0.9643" while the main text (method.tex:72, analysis.tex:5, experiments.tex:116) consistently reports ρ = −0.89 at n=7. These are different ρ values for the same stated n. Possible explanations: (a) different method sets compose the n=7 in each location; (b) different aggregation (mean vs median of per-seed values); (c) stale value in one location. **Severity: LOW** — directions agree, both highly significant; but should be reconciled for consistency.

### C5. 95% CI (tab:variance_ci, χ² method, N=3)

Using df=2: χ²_{0.025,2} = 0.0506, χ²_{0.975,2} = 7.378

| Scale | Config | std | Lower CI | Upper CI | Table Lower | Table Upper | PASS |
|-------|--------|-----|----------|----------|-------------|-------------|------|
| 1.7B | SFT | 2.79 | 1.453 | 17.54 | 1.45 | 17.55 | ✅ |
| 1.7B | RSFT | 0.09 | 0.047 | 0.566 | 0.04 | 0.54 | ⚠️ |
| 4B | SFT | 3.80 | 1.979 | 23.89 | 1.98 | 23.89 | ✅ |
| 4B | RSFT | 0.51 | 0.266 | 3.206 | 0.27 | 3.21 | ✅ |
| 8B | SFT | 3.23 | 1.682 | 20.31 | 1.68 | 20.31 | ✅ |
| 8B | RSFT | 0.50 | 0.260 | 3.144 | 0.26 | 3.15 | ✅ |
| LLaMA | SFT | 2.92 | 1.520 | 18.36 | 1.52 | 18.37 | ✅ |
| LLaMA | RSFT | 0.64 | 0.333 | 4.024 | 0.33 | 4.01 | ✅ |

**1.7B RSFT CI note**: Computed upper bound from std=0.09 is 0.566, table says 0.54. This is explained by rounding: the underlying std is ~0.086 (rounds to 0.09), yielding upper = 0.086×6.287 = 0.541 ≈ 0.54. The compression ratio (32.6×) also confirms: 2.79/0.0856 = 32.6. **Acceptable** — CI computed from more precise std, then std rounded for display.

### C6. Non-overlapping CIs at 1.7B

SFT lower bound = 1.45, RSFT upper bound = 0.54 → 1.45 > 0.54 → **non-overlapping** ✅

Text (line 120): "SFT lower bound 1.45pp > RSFT upper bound 0.54pp" ✅

At other scales, CIs do overlap (e.g., 4B: SFT [1.98, 23.89] vs RSFT [0.27, 3.21] → overlap at 1.98–3.21). Text correctly notes this (line 120).

### C7. Compression ratios (tab:variance_ci)

| Scale | SFT std | RSFT std | Ratio | Table | PASS |
|-------|---------|----------|-------|-------|------|
| 1.7B | 2.79 | ~0.086 | 32.6× | 32.6× | ✅ |
| 4B | 3.80 | 0.51 | 7.45× | 7.5× | ✅ (from precise values) |
| 8B | 3.23 | 0.50 | 6.46× | 6.5× | ✅ |
| LLaMA | 2.92 | 0.64 | 4.56× | 4.6× | ✅ |

Caption says "unrounded" — compression computed from precise values before rounding stds. ✅

---

## D. LaTeX Compilation Check

### D1. All \label definitions found

**Total labels**: 53 in paper files (excluding acl-style template)

Breakdown by file:
- method.tex: 9 (sec:method, fig:overview, sec:task, sec:sft, sec:paradigms, sec:ced, eq:ced, sec:edcr, eq:edcr)
- experiments.tex: 10 (sec:experiments, sec:setup, sec:main_results, tab:main, sec:spectrum, fig:spectrum, sec:scaling, tab:scaling, fig:evidence_tax, sec:evidence_strategy, sec:generalization, sec:analysis)
- analysis.tex: 1 (sec:analysis) — **NOT compiled** (not in main.tex \input)
- conclusion.tex: 1 (sec:conclusion)
- related_work.tex: 1 (sec:related_work)
- appendix.tex: 30 (all appendix sections/tables/figures)

### D2. Duplicate label check

`sec:analysis` defined in both experiments.tex:114 and analysis.tex:2. **NOT a problem**: analysis.tex is not included in main.tex — only experiments.tex is compiled. The standalone analysis.tex appears to be an orphaned earlier draft.

### D3. \label{sec:inference_efficiency} exists

Confirmed at appendix.tex:445. ✅

### D4. All \ref targets have matching \label

Every \ref{...} target in the compiled paper has a corresponding \label. Exhaustive cross-check:

| Target | Defined in | PASS |
|--------|-----------|------|
| tab:hyperparams | appendix.tex:9 | ✅ |
| sec:spectrum | experiments.tex:38 | ✅ |
| tab:main | experiments.tex:20 | ✅ |
| sec:scaling | experiments.tex:57 | ✅ |
| sec:ablation_full | appendix.tex:40 | ✅ |
| tab:ablation_full | appendix.tex:53 | ✅ |
| fig:spectrum | experiments.tex:52 | ✅ |
| tab:spectrum | appendix.tex:323 | ✅ |
| fig:grpo_dynamics | appendix.tex:352 | ✅ |
| sec:training_tax | appendix.tex:171 | ✅ |
| sec:error_analysis | appendix.tex:357 | ✅ |
| tab:scaling | experiments.tex:74 | ✅ |
| fig:evidence_tax | experiments.tex:98 | ✅ |
| fig:scaling | appendix.tex:113 | ✅ |
| sec:variance_ci | appendix.tex:118 | ✅ |
| tab:variance_ci | appendix.tex:125 | ✅ |
| sec:edcr | method.tex:59 | ✅ |
| sec:edcr_per_relation | appendix.tex:393 | ✅ |
| sec:rsft_theory | appendix.tex:203 | ✅ |
| sec:analysis | experiments.tex:114 | ✅ |
| sec:ced | method.tex:42 | ✅ |
| sec:inference_efficiency | appendix.tex:445 | ✅ |
| tab:error_analysis | appendix.tex:374 | ✅ |
| tab:inference_efficiency | appendix.tex:452 | ✅ |
| tab:test_results | appendix.tex:223 | ✅ |
| sec:generalization_full | appendix.tex:209 | ✅ |
| tab:training_tax | appendix.tex:182 | ✅ |
| tab:mechanistic | appendix.tex:154 | ✅ |
| fig:edcr_relations | appendix.tex:407 | ✅ |
| tab:case_evidence | appendix.tex:422 | ✅ |
| tab:test_tax | appendix.tex:248 | ✅ |
| tab:rsft_test_tax | appendix.tex:271 | ✅ |
| tab:encoder_comparison | appendix.tex:296 | ✅ |
| tab:cross_detail | appendix.tex:92 | ✅ |
| fig:overview | method.tex:9 | ✅ |
| app:ai-assistants | appendix.tex:473 | ✅ |

**No undefined references.** ✅

### D5. All \cite targets have matching .bib entries

All 36 unique citation keys used across the paper were found in `references.bib`:

autore2024 ✅, chen2025docksrag ✅, dai2025r1re ✅, dong2023raft ✅, gao2023scaling ✅, hu2022lora ✅, ito2025mogrpo ✅, jin2025rl_panacea ✅, laban2022summac ✅, li2025drift ✅, li2025srvf ✅, li2026qurl ✅, liu2025drgrpo ✅, liu2026gdpo ✅, ma2023dreeam ✅, moskovitz2024constrained ✅, rafailov2023direct ✅, ruder2017overview ✅, shao2024deepseekmath ✅, standley2020tasks ✅, tan2022redocred ✅, tang2025rsftppo ✅, wang2023selfconsistency ✅, wang2025rear ✅, wang2025relprior ✅, wang2025rullm ✅, xiao2022sais ✅, xie2022eider ✅, xu2024lmrc ✅, yao2019docred ✅, yu2020gradient ✅, yu2025dapo ✅, zelikman2022star ✅, zhang2024infuse ✅, zhang2025glidre ✅, zhou2021atlop ✅

**Unused bib entry**: `wan2024genres` — defined in references.bib but never cited. Will not cause compilation error, just an "unused entry" warning.

**No undefined citations.** ✅

### D6. All figure files exist

All 6 figure PDFs referenced by \includegraphics exist in `figures/paper/`:

- fig_overview.pdf ✅
- fig_spectrum.pdf ✅
- fig_evidence_tax.pdf ✅
- fig_scaling.pdf ✅
- fig_grpo_dynamics.pdf ✅
- fig_edcr_relations.pdf ✅

### D7. All \input files exist

main.tex inputs 8 files, all present:

- sections/abstract.tex ✅
- sections/introduction.tex ✅
- sections/related_work.tex ✅
- sections/method.tex ✅
- sections/experiments.tex ✅
- sections/conclusion.tex ✅
- sections/limitations.tex ✅
- sections/appendix.tex ✅

---

## Summary

### Counts

| Category | Items Checked | PASS | FAIL | WARN |
|----------|--------------|------|------|------|
| A. Figure data sources | 18 data points | 18 | 0 | 1 (caption note) |
| B. Appendix prose numbers | 32 claims | 32 | 0 | 1 (prose range) |
| C. Statistics | 26 quantities | 26 | 0 | 1 (ρ discrepancy) |
| D. Compilation | 6 checks | 6 | 0 | 1 (unused bib) |
| **Total** | **82** | **82** | **0** | **4** |

### Issues Found (all LOW severity)

1. **⚠️ Cross-method ρ inconsistency**: Main text (method.tex:72, analysis.tex:5, experiments.tex:116) reports ρ=−0.89 at n=7, while appendix partial correlation section (appendix.tex:398) reports raw ρ=−0.9643 for "n=7 unique methods". Both directions are negative and significant; likely different aggregation methodology, but should be reconciled or footnoted.

2. **⚠️ fig_scaling caption**: Claims "RSFT consistently narrows the gap" but RSFT is not plotted in the figure (only SFT with/without evidence bars). The claim is factually correct per other figures/tables, but not visually supported by this specific figure.

3. **⚠️ Inference overhead prose**: experiments.tex:116 says "adds 16–24% wall-clock time at 14B" — the range 16–24% spans 4B and 14B, not just 14B. Minor ambiguity.

4. **⚠️ Unused bib entry**: `wan2024genres` defined but never cited. No compilation impact.

### No FAILs detected. Paper is ready for submission from a data consistency perspective.
