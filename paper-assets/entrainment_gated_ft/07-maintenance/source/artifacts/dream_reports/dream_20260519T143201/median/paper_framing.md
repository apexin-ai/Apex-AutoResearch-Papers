# Paper Framing — entrainment_gated_ft

> Revised 2026-05-19 after Dream review (best case = 2.5/5). Major reframing: drop "paradox" narrative, engage related work, add retrieval benchmarks.

## Target Venue
- Primary: EMNLP 2026 Findings (via ARR)
- Stretch: EMNLP 2026 Main
- Deadline: ARR June 2026 cycle (submission ~June 15)

## Paper Type
Empirical analysis paper — quantifying a known phenomenon (per-example divergence under aggregate convergence) in a specific important domain (hybrid recurrent architectures)

## Core Claims (3 条)

### Claim 1: Task-Dependent Convergence
Adding attention layers to different linear recurrent architectures (GatedDeltaNet, RetNet, HGRN2) induces aggregate performance convergence whose strength varies with task type. Convergence is strongest on LAMBADA (ρ=-1.0, p=0.017 two-tailed, cross-arch std drops 79%), suggestive on ARC-Easy (ρ=-0.7, p=0.233, underpowered at n=5), and absent on reasoning-heavy tasks. **Critical need**: a second high-retrieval benchmark showing significant convergence to survive multi-comparison correction.

### Claim 2: Scale-Dependent Convergence
The convergence effect requires sufficient model capacity: monotonically complete at 1.3B (ρ=-1.0, p=0.017 two-tailed) but only partial at 340M with a non-monotonic rebound. Only two scale points (Wang et al. cap at 1.3B). Frame as binary contrast, not extrapolatable trend.

### Claim 3: Per-Example Divergence Under Aggregate Convergence
Despite aggregate convergence, attention acts on nearly non-overlapping sample subsets per architecture (pairwise Jaccard < 0.10). This is an instance of the well-documented underspecification phenomenon (D'Amour et al. 2022) applied to hybrid architectures. Our contribution is **quantifying** it in this specific context, NOT claiming to discover it. Surface features AND baseline model perplexity do not differentiate helped/hurt samples within an architecture — the effect is opaque to standard features. However, cross-architecture comparison reveals systematic differences in baseline difficulty profiles of affected samples (Kruskal-Wallis p=0.0005 for hurt samples), confirming the architecture-specificity is structured, not random noise.

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
"At 1.3B scale, adding attention to hybrid recurrent models reduces cross-architecture variance by 79% on LAMBADA, yet per-example analysis reveals nearly non-overlapping affected sample subsets (Jaccard < 0.10) — a manifestation of underspecification that has practical implications for architecture selection."

## Dream Review Findings (D006) — Must Address

### W1: Single-benchmark significance [MAJOR, blocking]
After Bonferroni (6 benchmarks, α=0.0083), LAMBADA p=0.017 (two-tailed) does NOT survive. Need: (a) FDR correction (Benjamini-Hochberg) as primary reporting, (b) additional high-retrieval benchmarks for a second significant anchor. Candidates: StoryCloze, BoolQ, COPA, closed-book QA tasks available in lm-eval.

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
**Statistical strategy** (from exp-008, verified by Reviewer with independent reproduction):
1. **Lead with percentile CI (valid-only)**: BCa degenerates at ρ=-1.0 boundary (z0=-3.86); fall back to percentile CI on valid bootstrap resamples (8875/10000; 11.25% degenerate from n=3 same-architecture redraws). Valid-only percentile CI = **[-1.0, -0.7]**, 100% of valid resamples have ρ<0. Full percentile CI (degenerate-as-zero) = [-1.0, 0.0] touches zero. Paper leads with valid-only CI; BCa degeneracy + degenerate-sample treatment in appendix.
2. **Report exact permutation p**: LAMBADA p=0.017 (two-tailed, 2/120 permutations). Honest and transparent.
3. **Bonferroni in supplementary**: adj-p=0.100 (two-tailed). Report honestly as "does not survive Bonferroni." BH-FDR also gives 0.100 (no additional benefit with only 1 small p-value). If exp-011 produces a second significant benchmark, BH-FDR becomes more favorable than Bonferroni.
4. **GDN-excluded sensitivity**: Excluding GDN (D004 confound): LAMBADA ρ drops to -0.7 (p=0.233); ARC-Easy ρ **improves** from -0.7 to -0.9 (p=0.083, suggestive — D004 noise removed); **⚠️ MMLU ρ FLIPS from -0.7 to +0.6** — MMLU apparent convergence was entirely GDN-driven and MUST NOT appear as convergence evidence anywhere in the paper (D007). Report both full and GDN-excluded analyses. The ARC-Easy improvement after confound removal is itself informative, especially in exp-011 context.
5. **exp-011**: Additional retrieval benchmarks (StoryCloze/BoolQ/COPA) for a potential second significant anchor. CRITICAL for acceptance — with exp-011 data, BH-FDR could diverge favorably from Bonferroni.
6. **Effect sizes**: Cohen's d CI crosses zero; omega² near zero. Do NOT lead with effect sizes — lead with BCa CI and convergence magnitude (std 0.024→0.005, 79% reduction).

Required experiments: exp-011 (additional retrieval benchmarks), exp-008 (robustness with corrected p-values), exp-002 (per-example validation).

### Concern C: "The per-example divergence is a known phenomenon"
Response: Acknowledge explicitly. Our contribution is quantification in hybrid architectures, not discovery of the phenomenon. Cite ensemble diversity + underspecification.
Required: Related Work section (Paper Agent).

### Concern D: "n=3 architectures is too few"
Response: 3 architectures × 5 ratios × 2 scales = 30 models. Per-example analysis provides 5153 data points per comparison. Check for additional architectures (exp-005).

### Concern E: "Two scales don't establish a trend"
Response: Binary contrast, not trend. 7B unavailable. Frame as "scale is a necessary condition." exp-007 for 340M rebound mechanism.

### Concern F: "No causal mechanism" (NEW from Dream)
Response: We do NOT claim causal mechanism. We characterize and describe. Attention weight analysis (exp-004) is descriptive. Interventional experiments (head swaps, ablations) are acknowledged as future work. Honest framing prevents overclaiming.
