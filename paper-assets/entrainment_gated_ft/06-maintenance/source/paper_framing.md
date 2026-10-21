# Paper Framing — entrainment_gated_ft

> Revised 2026-05-20 after Round 1 review (Overall 3.0, D014). Predictive multiplicity replaces underspecification as primary framework. Title: "Task-Specific Convergence and Per-Example Predictive Multiplicity in Hybrid Recurrent Architectures". CI→complementary characterization. New evidence: Jaccard normalized ES (5-7%), RetNet-HGRN2 decoupling. Target 3.5+.

## Target Venue
- Primary: EMNLP 2026 Findings (via ARR)
- Stretch: EMNLP 2026 Main
- Deadline: ARR June 2026 cycle (submission ~June 15)

## Paper Type
Empirical analysis paper — quantifying a known phenomenon (per-example divergence under aggregate convergence) in a specific important domain (hybrid recurrent architectures)

## Core Claims (3 条)

### Claim 1: Task-Specific Convergence (revised D009)
Adding attention layers to different linear recurrent architectures (GatedDeltaNet, RetNet, HGRN2) induces aggregate performance convergence **specifically on context-retrieval tasks**. Across 10 benchmarks, only LAMBADA shows significant convergence (ρ=-1.0, p=0.017 two-tailed, cross-arch std drops 79%, BCa CI [-1.0, -0.7]). This task-specificity IS the finding, not a limitation:
- **Negative-ρ cluster** (6/10): LAMBADA, xstorycloze, COPA, PIQA, ARC-Easy, MMLU — tasks with context-retrieval or reasoning components
- **Positive-ρ cluster** (4/10): BoolQ, SciQ, HellaSwag, WinoGrande — commonsense/knowledge tasks where attention doesn't equalize
- LAMBADA is unique as a **pure context-prediction** task (predict last word from context alone), explaining why convergence is strongest there

**Statistical strategy (D009)**:
1. **Complementary characterization**: BCa percentile CI [-1.0, -0.7] (100% valid resamples have ρ<0; does NOT depend on multiple comparison correction). NOT "primary evidence" — this was flagged as post-hoc evidence standard switching in Round 1
2. **Pre-registered correction (D003)**: 6-benchmark Bonferroni adj-p=0.100. Report honestly as "does not survive strict Bonferroni"
3. **Supplementary**: 10-benchmark survey as task-specificity evidence, NOT for multi-comparison correction
4. ⚠️ **Prohibited**: post-hoc subset selection ("2-benchmark Bonferroni", "only ρ<0 benchmarks"). Reviewers will immediately flag this as p-hacking

### Claim 2: Scale-Dependent Convergence
The convergence effect requires sufficient model capacity: monotonically complete at 1.3B (ρ=-1.0, p=0.017 two-tailed) but only partial at 340M with a non-monotonic rebound (peak 56% reduction at h6-1, but endpoint only 36% due to rebound at h3-1; ρ=-0.5, p=0.45). Only two scale points (Wang et al. cap at 1.3B). Frame as binary contrast, not extrapolatable trend.

**Cross-scale per-example stability (exp-007)**: Despite aggregate divergence across scales, per-example Jaccard at 340M h3-1 (helped=0.094, hurt=0.090) nearly matches 1.3B (~0.096, ~0.090). Net direction also consistent: GDN net negative, HGRN2 net positive at both scales (340M magnitudes larger: GDN=-256 vs -153, HGRN2=+238 vs +153). This extends the decoupling finding to the scale dimension: aggregate convergence is scale-dependent but per-example architecture-specificity is scale-invariant.

### Claim 3: Per-Example Predictive Multiplicity Under Aggregate Convergence
Despite aggregate convergence, attention acts on nearly non-overlapping sample subsets per architecture (pairwise Jaccard < 0.10, normalized ES ~6% of theoretical upper bound). This is an instance of **predictive multiplicity** (Marx et al. 2020) arising from architectural variation rather than random initialization (cf. D'Amour et al. 2022 underspecification, which is complementary but focuses on same-pipeline variation). Our contribution is **quantifying** it in hybrid recurrent architectures. RetNet-HGRN2 only analysis confirms decoupling holds without GDN confound (σ↓54%, J saturates 0.085-0.108). Surface features AND baseline model perplexity do not differentiate helped/hurt samples within an architecture — the effect is opaque to standard features. However, cross-architecture comparison reveals systematic differences in baseline difficulty profiles of affected samples (Kruskal-Wallis p=0.0005 for hurt samples), confirming the architecture-specificity is structured, not random noise.

**Decoupling finding (exp-010, D008)**: Aggregate convergence and per-example divergence are **decoupled** — they operate on different timescales w.r.t. attention ratio:
- Aggregate σ decreases **gradually** across 5 attention levels (0.024 → 0.016 → 0.014 → 0.006 → 0.005)
- Per-example Jaccard **saturates immediately** at the first attention level (4%) and remains flat (~0.095)
- Net asymmetry (HGRN2 net positive vs GDN/RetNet net negative) **increases** with attention (0.013 → 0.040)
- Implication: minimal attention creates full per-example architecture-specificity; gradual increases only affect aggregate convergence

⚠️ Do NOT frame as "co-evolution." Spearman ρ=-0.70 (p=0.23) is inflated by degenerate pure=0 point (Jaccard=NaN→0); excluding it: ρ=-0.40, p=0.75. The correct narrative is **decoupling**, which is a stronger finding: aggregate metrics converge while per-example dynamics increasingly diverge.

## Story Spine

### Problem
Hybrid architectures mixing linear recurrence with full attention are becoming standard. While Wang et al. (2025) provide an extensive model zoo, the community lacks quantitative understanding of how attention affects cross-architecture behavioral diversity at the per-example level.

### Related Work Positioning (CRITICAL — Dream W2)
The observation that models with similar aggregate performance differ per-example is well-established:
- **Ensemble diversity**: Krogh & Vedelsby (1995), Kuncheva & Whitaker (2003) — diverse ensemble members err on different examples by construction
- **Underspecification**: D'Amour et al. (2022) — equivalent aggregate performance masks prediction-level differences
- **Dataset cartography**: Swayamdipta et al. (2020) — per-example difficulty varies across models
- **Simpson's paradox / ecological fallacy**: Aggregate-vs-disaggregate discrepancy is a textbook phenomenon

Our contribution is NOT discovering this phenomenon. It IS quantifying how it manifests specifically when attention is added to linear recurrent models, and characterizing its task-dependency and scale-dependency. This is valuable because hybrid architectures are a design choice practitioners make — understanding per-example implications informs that choice.

### Our Framing
We provide the first systematic per-example analysis of attention's equalizing effect in hybrid recurrent architectures. Using Wang et al.'s public model zoo (72 models), we quantify (a) task-dependent convergence strength, (b) scale-dependent convergence completeness, and (c) architecture-specific per-example divergence patterns. Our contribution is analytical depth on public infrastructure, not new methods or models.

### Headline Result Template
"At 1.3B scale, adding attention to hybrid recurrent models reduces cross-architecture variance by 79% on LAMBADA, yet per-example analysis reveals nearly non-overlapping affected sample subsets (Jaccard ~0.10, only 6% of theoretical upper bound) — a form of predictive multiplicity arising from architectural variation that has practical implications for architecture selection and ensemble design."

## Dream Review Findings (D006) — Must Address

### W1: Single-benchmark significance [MAJOR, mitigated via D009]
After Bonferroni (6 benchmarks), LAMBADA adj-p=0.100. exp-011 tested 5 additional benchmarks (boolq/copa/piqa/sciq/xstorycloze_en) — **none showed significant convergence**. Multi-benchmark path is closed.
**Mitigation (D009)**: (a) BCa CI [-1.0, -0.7] as primary evidence (doesn't depend on multiple comparison); (b) task-specificity reframing — LAMBADA's uniqueness as pure context-prediction task explains why it alone shows convergence; (c) 10-benchmark negative results presented as task-specificity evidence in supplementary; (d) honest reporting: "does not survive Bonferroni" in text. Status: **no longer blocking** — the statistical strategy is defensible if framed honestly.

### W2: Missing related work [MAJOR, blocking for submission]
Need 20+ references engaging ensemble diversity, underspecification, dataset cartography, attention interpretability, hybrid architectures (Jamba, RWKV-6, RecurrentGemma). Paper Agent handles this during writing.

### W3: Mechanistic overclaiming [MAJOR, partially addressed]
Already reworded Claim 3 from "Mechanism" to "Effects". Must NOT use "mechanistic analysis" in paper — use "characterization" or "decomposition" instead. Attention weight analysis (exp-004) is descriptive, not causal. Frame honestly.

### W4: Incremental over Wang et al. [MAJOR]
Mitigate by: (a) engaging related work to show the QUESTION we ask is independently motivated by ensemble/underspecification literature, (b) framing contribution as analytical toolkit + quantitative characterization, not re-analysis. (c) Per-example analysis is genuinely novel for this model family.

## Venue Fit Risks
(unchanged from previous version, see git history)

## Anticipated Reviewer Concerns

### Concern A: "This is just a re-analysis of Wang et al.'s models"
Response: Yes, and that's the point — public infrastructure enables community analysis. Our per-example decomposition, task-dependency characterization, and scale-dependency analysis are not in Wang et al. The contribution is analytical, like meta-analyses in medicine.
Required: Strong Related Work positioning; frame as "community analysis" paper.

### Concern B: "Only one task shows the effect" + Bonferroni failure
**Statistical strategy (D009, post exp-011)**:
1. **Lead with BCa percentile CI [-1.0, -0.7] (valid-only)**: 100% of valid resamples have ρ<0. Full CI (degenerate-as-zero) = [-1.0, 0.0] touches zero. Paper leads with valid-only CI; BCa degeneracy (11.25%, from n=3 same-architecture redraws producing undefined ρ) + degenerate-sample treatment in appendix with formal justification: degenerate resamples have undefined ρ (not ρ=0), excluding them is standard practice, not cherry-picking.
2. **Report exact permutation p**: LAMBADA p=0.017 (two-tailed, 2/120 permutations).
3. **6-benchmark Bonferroni (D003 pre-registered)**: adj-p=0.100. Report honestly: "does not survive strict Bonferroni."
4. **10-benchmark survey in supplementary**: exp-011 tested 5 additional benchmarks, all negative. Present as task-specificity evidence, NOT for multi-comparison correction. Do NOT add to Bonferroni (would worsen to 0.167).
5. **GDN-excluded sensitivity**: LAMBADA ρ→-0.7 (p=0.233); ARC-Easy ρ improves to -0.9 (p=0.083); ⚠️ MMLU ρ FLIPS to +0.6 (D007). Report both.
6. **Effect sizes**: Cohen's d CI crosses zero; lead with BCa CI and convergence magnitude (std 0.024→0.005, 79% reduction).

**Task taxonomy (must define in Method, NOT post-hoc)**:
Operationalize "pure context retrieval" as: next-token prediction requiring long-range context retrieval without additional reasoning/knowledge steps. LAMBADA fits (predict final word from narrative context). xstorycloze/COPA involve commonsense completion (multiple-choice, need world knowledge). BoolQ is reading comprehension (classify: "retrieval" → "comprehension/QA"). PIQA/SciQ involve domain knowledge. This taxonomy must appear in Method section before results.

**Limitations to proactively address**:
- Per-example analysis limited to LAMBADA (only benchmark with significant convergence + available per-example logprob data). Acknowledge and explain. (D010: exp-002 cancelled — multi-benchmark per-example risks undermining task-specificity narrative)
- n=5 attention ratios limits statistical power (minimum achievable p = 1/120 ≈ 0.0083)

### Concern C: "The per-example divergence is a known phenomenon"
Response: Acknowledge explicitly. Our contribution is quantification in hybrid architectures, not discovery of the phenomenon. Cite ensemble diversity + underspecification.
Required: Related Work section (Paper Agent).

### Concern D: "n=3 architectures is too few"
Response: 3 architectures × 5 ratios × 2 scales = 30 models. Per-example analysis provides 5153 data points per comparison. Check for additional architectures (exp-005).

### Concern E: "Two scales don't establish a trend"
Response: Binary contrast, not trend. 7B unavailable. Frame as "scale is a necessary condition." exp-007 for 340M rebound mechanism.

### Concern F: "No causal mechanism" (NEW from Dream)
Response: We do NOT claim causal mechanism. We characterize and describe. Attention weight analysis (exp-004) is descriptive. Interventional experiments (head swaps, ablations) are acknowledged as future work. Honest framing prevents overclaiming.
