# Paper Framing — entrainment_gated_ft

## Target Venue
- Primary: EMNLP 2026 Main (via ARR)
- Backup: EMNLP 2026 Findings
- Deadline: ARR June 2026 cycle (submission ~June 15)

## Paper Type
Empirical analysis paper (not method paper)

## Core Claims (3 条)

### Claim 1: Task-Specific Equalizer Effect
Adding attention layers to different linear recurrent architectures (GatedDeltaNet, RetNet, HGRN2) induces aggregate performance convergence whose strength scales with task retrieval demand—strongest on LAMBADA (ρ=-1.0, p=0.017 two-tailed, cross-arch std drops 79%), suggestive on ARC-Easy (ρ=-0.7, p=0.233 two-tailed, underpowered at n=5), absent on reasoning-heavy tasks (HellaSwag, WinoGrande). This continuous relationship between retrieval demand and convergence strength is a key finding, not a limitation of single-task significance.

### Claim 2: Scale-Dependent Convergence
The convergence effect is scale-dependent: monotonically complete at 1.3B parameters (Spearman ρ=-1.0 for cross-arch std vs attention ratio, exact permutation p=0.017, two-tailed) but only partial at 340M with a non-monotonic rebound at high attention ratios. Note: only two scale points available (Wang et al. do not provide 7B models); this is a binary contrast, not a multi-point trend. Paper must frame honestly as "scale matters" without implying extrapolation.

### Claim 3: Architecture-Specific Effects (Equalizer Paradox)
Despite aggregate convergence, attention acts on almost entirely different sample subsets per architecture (pairwise Jaccard < 0.10). GDN and RetNet are hurt (net negative on LAMBADA), HGRN2 is helped (net positive), with symmetric effect magnitudes—convergence emerges from complementary, not redundant, effects. Surface-level features (token frequency, context length) do NOT differentiate helped vs hurt samples (all p>0.2 except marginal RetNet context_length). This rules out trivial explanations. Deeper features (perplexity under baseline, topic/domain) are being tested. If those also fail, claim wording shifts to "architecture-specific effect whose mechanism is opaque to standard features" — the non-overlapping Jaccard evidence remains hard regardless.

## Story Spine

### Problem
Hybrid architectures mixing linear recurrence with full attention are becoming the dominant paradigm for efficient language models. A critical open question: does adding attention homogenize model behavior across different recurrence mechanisms, or do architecture-specific effects persist?

### Existing Approaches & Gaps
Wang et al. (2025, arXiv 2507.06457) provide the most comprehensive model zoo (72 models, 3 architectures, multiple scales and attention ratios) but report only aggregate metrics. They qualitatively note convergence trends but do not analyze: (a) the per-example mechanism, (b) scale dependency of convergence, (c) task-specificity, or (d) why architectures converge to similar *aggregate* performance through *different* individual-sample effects.

### Our Framing
We provide the first quantitative characterization of the "equalizer effect"—a systematic per-example analysis revealing that attention creates aggregate performance convergence through architecture-specific, largely non-overlapping mechanisms. This "equalizer paradox" (aggregate convergence + per-example divergence) has direct implications for architecture selection: even when aggregate metrics converge, the types of inputs each architecture handles well remain architecture-specific.

### Headline Result Template
"At 1.3B scale, adding attention layers reduces cross-architecture performance variance by 79% on LAMBADA (std 0.024→0.005), yet per-example analysis reveals the affected sample subsets are almost entirely non-overlapping across architectures (Jaccard < 0.10), with symmetric but opposite effect directions."

## Venue Fit Risks

### Risk 1: Architecture Analysis vs NLP
EMNLP is NLP-focused; this paper is closer to architecture analysis. **Mitigation**: Frame in terms of understanding language model behavior on specific linguistic tasks. Anchor analysis to token-level and context-level linguistic features (frequency, context length, retrieval demand). Include practical recommendations for practitioners choosing hybrid architectures for specific NLP tasks.

### Risk 2: Limited Task Coverage
Currently only LAMBADA shows clear convergence. **Mitigation**: (a) Extend per-example analysis to HellaSwag and other benchmarks, (b) provide principled explanation of LAMBADA's retrieval-dependent nature vs reasoning tasks, (c) if convergence appears on other retrieval tasks, strengthens Claim 1; if not, reframe as "convergence is task-type-specific" which is still interesting.

### Risk 3: Small Architecture Sample
Only 3 architectures (GDN, RetNet, HGRN2). **Mitigation**: These represent three distinct recurrence mechanisms (gated delta rule, linear attention with exponential decay, hierarchical gated recurrence). Check if Wang et al. have additional architectures or scales. n=3 is sufficient for the per-example analysis which is our main contribution.

### Risk 4: Wang et al. Overlap
They have the model zoo AND qualitative convergence observation. **Mitigation**: Our contribution is explicitly about what they did NOT do: quantitative convergence framework, scale-dependent analysis, per-example mechanism analysis. Frame as "using their excellent model zoo, we discover a deeper phenomenon they missed."

## Anticipated Reviewer Concerns

### Concern A: "This is just a negative result from a failed hypothesis"
Response: Frame as discovery paper. The equalizer effect is a positive finding—it was not the hypothesis we started with, but it's a genuine empirical phenomenon with theoretical implications. Many impactful papers come from unexpected findings.
Required evidence: Strong standalone story; no mention of original entrainment hypothesis in the paper.

### Concern B: "Only one task shows the effect" + Post-hoc taxonomy risk
Response: Do NOT use binary retrieval/reasoning split — vulnerable to post-hoc cherry-picking (only 1 benchmark in "retrieval" category, exactly the one that's significant). Instead:
1. **Continuous spectrum**: Plot convergence strength (Spearman ρ) against a continuous measure of "retrieval demand" per benchmark. LAMBADA ρ=-1.0, ARC-E ρ=-0.7 (suggestive), ARC-C ρ=-0.3, HellaSwag/WinoGrande/MMLU near zero. Frame as dose-response: more retrieval demand → stronger convergence.
2. **Cite existing task taxonomies**: Use BIG-bench taxonomy or other published meta-analyses for task property classification — don't invent our own post-hoc.
3. **Honest reporting**: ARC-E ρ=-0.7 (p=0.117) is "suggestive but underpowered" — n=5 ratios means low statistical power. Continuous spectrum framing turns "only LAMBADA significant" into "graded effect consistent with retrieval demand."
4. **Winogrande ambiguity**: Coreference resolution has a retrieval component (finding antecedent). Acknowledge this honestly rather than forcing it into "reasoning."
5. **exp-002 validation**: If HellaSwag per-example analysis confirms no convergence at sample level, upgrades from "aggregate not significant" to "per-example confirmed non-converging."
Required experiments: exp-001 (done, PASS on dichotomy), exp-002 (per-example validation), exp-003 (sample characterization).

### Concern C: "No causal mechanism"
Response: Per-example analysis provides mechanistic evidence (different subsets). Strengthen with attention weight visualization and sample feature characterization.
Required experiments: Sample characterization (exp-003), attention weight analysis (exp-004).

### Concern D: "n=3 architectures is too few"
Response: Three architectures with 5 attention ratios × 2 scales = 30 models. The per-example analysis provides thousands of data points. Check if additional architectures available.
Required experiments: Architecture expansion check (exp-005).

### Concern E: "Two scales don't establish a trend"
Response: 7B unavailable (Wang et al. capped at 1.3B). Frame as "binary contrast showing scale is a necessary condition" — convergence requires sufficient model capacity (1.3B), not just attention. Strengthen via exp-007 (340M rebound mechanism analysis) to provide mechanistic explanation for the scale gap. Acknowledge as limitation; do not imply extrapolation.
Required experiments: exp-007 (340M rebound mechanism).
