---
dream_id: dream_20260516T073742
tier: median
overall_score: weak reject
timestamp: 2026-05-16T08:19:22.041288+00:00
---

# Dream Review Report: Phase-Dependent Compound Sparsity

**Paper**: "Phase-Dependent Compound Sparsity: Strategy–Phase Interactions Modulate Severity in Efficient LLM Inference"
**Review mode**: Full (2 reviewers + roundtable)
**Venue standard**: Top ML venue, ~25% acceptance, 6-point scale

---

## Reviewer Assignments

- **R1**: Methods + Experiments (Score: 3, Confidence: 4/5)
- **R2**: Novelty + Related Work (Score: 3, Confidence: 4/5)

---

## Step 1: Independent Reviews

### R1 — Methods & Experiments

**Summary**: The paper introduces a phase-gated analysis framework for compound sparsity and demonstrates that interaction severity depends on eviction strategy, reasoning phase, and sparsity level, with a monotonic dose-response under importance-based eviction.

**Strengths**:
- Well-defined metric (II) with paired median difference as primary statistic — sound choice for heavy-tailed distributions
- Strong statistical methodology: bootstrap CIs (B=10,000), Wilcoxon+Bonferroni, Jonckheere-Terpstra for dose-response, permutation tests, BH-FDR robustness check
- Large primary sample (n=500 MATH-500) provides genuine statistical power
- Honest reporting of limitations: mechanism is correlational, entropy redistribution inconsistent, LLaMA evidence weak, pilot mitigation failed pre-registered gate
- Phase segmentation validated against </think> structural markers (κ=0.88 MATH-500, κ=0.82 GPQA)

**Weaknesses**:

- **W1 (Critical): Circular confound in importance-based eviction.** Importance scores are computed from the same attention distribution that head pruning alters. The "compound interaction" may largely be a measurement artifact: pruning degrades the importance scores used for eviction, a deterministic consequence of the scoring method. No scoring-independent eviction method (recency, learned, position-based) is tested, which would be necessary to disentangle the confound from a genuine emergent property.

- **W2 (Major): Two primary models share identical architecture.** DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct both use Qwen2ForCausalLM (28 layers, 28 heads, 4-group GQA). "Cross-model replication" is really cross-training-paradigm on one architecture family. LLaMA-8B results (n=250) show within-importance gradient replicates (dz≈1.0) but strategy×phase interaction is weak (dz 0.18–0.33, only s030 Bonferroni significant), undermining architecture-generality claims.

- **W3 (Major): Possibly tautological phase construct.** Low-sparsity phases are defined as phases where attention is broadly distributed. Importance-based eviction degrades most when attention is broadly distributed (more positions have similar scores → eviction error-prone). The finding that severity concentrates in low-sparsity phases may be a direct definitional consequence rather than a non-obvious empirical discovery.

- **W4 (Moderate): GSM8K evidence is thin.** Qwen random on GSM8K excluded for data quality. Random conditions non-significant but underpowered (n=50). Strategy specificity ratio cannot be cleanly computed on GSM8K. Cross-benchmark claim relies primarily on DeepSeek importance monotonicity.

- **W5 (Moderate): Discrimination collapse doesn't explain magnitude.** Gini drops are near-identical for both strategies (<10% difference) yet severity diverges 15×. The proposed mechanism explains the direction of the effect but not its core quantitative feature.

- **W6 (Minor): No practical contribution.** Pilot mitigation (oracle recovery 18%, CI spanning zero) failed its pre-registered gate. The paper is purely descriptive with no actionable output.

- **W7 (Minor): Spearman ρ=1.0 on 4 data points.** The monotonicity claim features ρ=1.0 prominently but this is trivially achievable with n=4. The JT test is more informative but less prominently reported.

**Questions**:
- Q1: Have you tested any eviction strategy whose scoring is independent of pruned attention (recency, position, learned)? If severity gradient disappears, finding is about H2O scoring fragility, not compound sparsity per se.
- Q2: What happens if phases are defined on pruned model's attention patterns rather than dense model's?
- Q3: Why only 30 problems for discrimination collapse analysis rather than full n=500?
- Q4: DeepSeek vs Qwen effect magnitude differs ~5× despite identical architecture — is this purely chain-length driven?

### R2 — Novelty & Related Work

**Summary**: The paper identifies a genuine gap — prior compound compression work treats interaction as constant — and fills it with a three-way (compound × strategy × phase) empirical analysis. The "discrimination collapse" mechanism is proposed but acknowledged as insufficient.

**Strengths**:
- Genuine gap identification: decomposing compound interaction by reasoning phase is natural but unexplored in the compound setting specifically
- "Three-way interaction" framing (compound × strategy × phase) is legitimately novel as a combined analysis
- Cross-benchmark evaluation (MATH-500, GSM8K, GPQA Diamond) adds breadth
- Careful positioning against ThinKV (single-axis phase-aware), SparK (compound but phase-unaware), and Physics of KV Cache (different "phase" semantics)
- Transparent qualification of limitations throughout

**Weaknesses**:

- **W1 (Critical): Incremental conceptual novelty.** The core contribution is measuring an interaction that follows naturally from combining known components. ThinKV shows phases matter for KV eviction; SparK shows compound sparsity is super-additive. That "compound super-additivity varies by phase" is the expected intersection. Novelty rests on quantification rather than conceptual surprise. For a ~25% acceptance venue, this may be insufficient without a strong methodological or theoretical companion.

- **W2 (Major): Mechanism insufficient.** Discrimination collapse is correlational, explains direction but not magnitude (identical Gini drops, 15× severity divergence). Entropy redistribution is model-dependent (consistent on DeepSeek, inconsistent on Qwen). Without a causal mechanism, the paper is purely descriptive.

- **W3 (Major): Actionability gap.** The paper positions as "empirical finding" but the finding's practical implication (phase-aware budget allocation) failed the pilot test. Cannot demonstrate that the finding changes practice. Abstract's "direct implications" language should be softened.

- **W4 (Moderate): Perplexity-based metric vs. task accuracy.** II measures perplexity deviation, not downstream accuracy. Accuracy validation shows a cliff at s=0.30 but the monotonic II gradient may not translate to monotonic accuracy degradation. Practitioners care about correctness, not perplexity interactions.

- **W5 (Moderate): "Universality" claim overstated.** LLaMA result is inconclusive for strategy×phase interaction. Strategy specificity ratio varies 4× across benchmarks (15× to 2.3×). Crossover is model-specific. Quantitative characteristics are highly context-dependent.

- **W6 (Minor): Missing related work.** Several relevant works not discussed: Thinking Tokens MI (NeurIPS 2025, MI peaks at reasoning tokens — could explain why low-sparsity phases are sensitive), Twilight (NeurIPS 2025 Spotlight, adaptive per-step budget), DefensiveKV (importance-based eviction fragility).

- **W7 (Minor): Narrow strategy comparison.** Only H2O-style cumulative attention scoring vs. random. The entire finding may be specific to this scoring method rather than a general property of compound sparsity.

**Questions**:
- Q1: Given identical Gini drops but 15× severity divergence, what fraction of the divergence does discrimination collapse actually explain?
- Q2: The crossover phenomenon exists only for DeepSeek, not Qwen — how is it a general finding?
- Q3: Have you considered DefensiveKV's "stability assumption failure" as a related mechanism?
- Q4: If the pilot mitigation failed, what is the concrete value proposition for practitioners?

---

## Step 2: Cross-Sharing

After exchanging reviews, both reviewers identified strong convergence:

- R1's **circular confound** (W1) and R2's **narrow strategy comparison** (W7) are the same issue: dependence on H2O-style attention scoring creates a confound where the entire finding may be an artifact of scoring-method fragility under pruning.
- R1's **tautological phase construct** (W3) and R2's **incremental novelty** (W1) both point to the core finding being somewhat expected or definitional — the natural intersection of phase-awareness and compound compression.
- R1's **mechanism magnitude gap** (W5) and R2's **mechanism insufficiency** (W2) are identical concerns.
- Both independently flagged the **failed pilot mitigation** as undermining practical significance.

No disagreements emerged. R2 noted that R1's "tautological" framing strengthens R2's "incremental" assessment — if the finding is partially definitional, the novelty is even lower.

---

## Step 3: Convergence

### Converged Weaknesses (ranked by severity)

1. **Critical — Scoring-method confound** (R1-W1 + R2-W7). The entire severity gradient may be an artifact of using attention-mass-based importance scoring (H2O) that head pruning mechanistically degrades. Without testing at least one scoring-independent eviction method, the paper cannot distinguish between "compound sparsity has phase-dependent severity" and "H2O scoring breaks under pruning in a phase-dependent way." This is the single most important issue.

2. **Critical — Limited novelty** (R1-W3 + R2-W1). The finding sits at the expected intersection of ThinKV (phases matter) and SparK (compound is super-additive). The phase construct may additionally be tautological: low-sparsity phases have broadly distributed attention → importance scores are less discriminative → importance-based eviction fails more. This is a definitional consequence, not a surprising empirical discovery.

3. **Major — Mechanism insufficient** (R1-W5 + R2-W2). Discrimination collapse explains the direction of strategy×phase interaction but cannot explain the 15× magnitude divergence between strategies despite near-identical Gini drops. The mechanism is correlational, with no causal test. Entropy redistribution is model-dependent and therefore not a general secondary mechanism.

4. **Major — No actionable contribution** (R1-W6 + R2-W3). The pilot mitigation failed its pre-registered gate (oracle recovery 18%, CI spanning zero). The paper is purely descriptive — it characterizes a phenomenon but does not demonstrate how practitioners should use this characterization.

5. **Moderate — Limited architectural diversity** (R1-W2 + R2-W5). Two primary models share Qwen2ForCausalLM architecture. LLaMA cross-architecture validation is weak for strategy×phase interaction (dz 0.18–0.33). "Universality" claims are overstated.

6. **Moderate — Perplexity vs. accuracy gap** (R2-W4). II is perplexity-based; the monotonic gradient may not transfer to task performance. Accuracy shows a cliff rather than a gradient.

### Converged Strengths

1. **Rigorous statistical framework**: Bootstrap, Bonferroni, Wilcoxon, JT tests, proper non-parametric methods for skewed distributions — among the better statistical treatments in the efficient inference literature.
2. **Intellectual honesty**: Transparent about LLaMA weakness, mechanism limitations, failed pilot, and model-dependent inconsistencies. Limitations section is genuinely informative rather than pro-forma.
3. **Clean dose-response on primary benchmark**: The n=500 MATH-500 monotonicity result for importance-based eviction is robust and reproducible.
4. **Cross-benchmark breadth**: Testing on 3 benchmarks (MATH-500, GSM8K, GPQA) with appropriate qualification of task-dependence is more thorough than typical.

---

## Step 4: Consolidated Assessment

### Overall Score: 3 — Weak Reject

### Consensus Confidence: 4/5

### Recommendation

**Reject with encouragement to revise.** The paper demonstrates strong empirical methodology and commendable intellectual honesty, but fails to clear the bar on two critical dimensions for a top venue:

1. **The scoring-method confound is not addressed.** The entire finding may be about H2O scoring fragility rather than a general property of compound sparsity. Adding one or two scoring-independent eviction methods (recency-based, learned, or position-based) in a revision would resolve this decisively.

2. **The novelty is insufficient as a standalone empirical finding.** The observation is the expected intersection of known phenomena (phase-awareness + compound super-additivity), and the phase construct may be partially tautological. To elevate this to a top-venue contribution, the authors should either:
   - (a) Develop a working phase-aware adaptive method enabled by the finding, or
   - (b) Provide a causal mechanism that explains the 15× magnitude gap, not just the direction.

### Key Revision Suggestions

- **Essential**: Test at least one non-attention-mass eviction strategy (recency, position, learned) to disentangle the confound.
- **Essential**: Either strengthen the mechanism (causal test of discrimination collapse → severity) or reframe the contribution to not claim mechanistic insight.
- **Recommended**: Soften "universality" language — the phase gradient is robust but strategy specificity is highly context-dependent.
- **Recommended**: Replace "direct implications for phase-aware budget allocation" with "motivates future work on phase-aware compression" given the failed pilot.
- **Recommended**: Add missing related work (Thinking Tokens MI, DefensiveKV, Twilight) and discuss how the finding connects to importance score instability literature.

### What Would Change the Score

- To **4 (Borderline Accept)**: Address the confound with one scoring-independent strategy + strengthen mechanism or deliver a working mitigation.
- To **5 (Accept)**: All of the above + true cross-architecture validation (3+ architecture families) + demonstration that the finding changes practice (working phase-aware method with >30% recovery).
