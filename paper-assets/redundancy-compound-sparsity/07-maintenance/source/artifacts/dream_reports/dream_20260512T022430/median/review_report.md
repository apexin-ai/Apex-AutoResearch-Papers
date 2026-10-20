---
dream_id: dream_20260512T022430
tier: median
overall_score: borderline reject
timestamp: 2026-05-12T03:01:13.724344+00:00
---

# Dream Review Report — median tier

**Dream ID**: 20260512T022430  
**Tier**: median  
**Paper**: "Evidence for Architecture-Modulated Cross-Axis Signals in Reasoning Inference"  
**Review Mode**: full (2 Reviewers + roundtable)  
**Overall Score**: borderline reject

---

## Headline Assessment

The paper poses a genuinely interesting research question — whether a single KV-similarity signal can coordinate both KV eviction and MLP sparsity — and arrives at a nuanced, architecture-dependent answer rather than an inflated universal claim. However, the evidence base is thin (20 AIME problems, 2 architecture families, missing statistical rigor), the practical downstream impact is marginal (+1.0% over matched-average baseline), and the CARC-KV contribution is disconnected padding unrelated to the core hypothesis. The paper is honest about limitations but does not overcome them. For a top venue, the experimental depth and novelty margin over prior work (CLADA, Token Filtering) are insufficient.

---

## Reviewer 1: Methods + Experiments

### Strengths

**S1-1. Clean factorial design.** The 2×2 (architecture × training paradigm) design with Llama-GQA(4:1) vs Qwen2-GQA(7:1) × instruction vs reasoning-distilled is well-structured and allows partial isolation of each factor's contribution. The near-additive decomposition (Δr≈0.18 + 0.10 ≈ observed gap) is a clean result.

**S1-2. CARC-KV is practical.** The O(1) eviction method via min-heap is clean engineering. The speedup scaling (3.1× at 4K → 26× at 32K) is well-demonstrated and the comparison against H2O/SnapKV/StreamingLLM is appropriate.

**S1-3. Multi-granularity analysis.** Per-layer (Table 3) and per-head (Table 4) decompositions go beyond aggregate numbers. The mid-layer concentration (layers 8–23, peak r=0.61 at layer 18) provides mechanistic insight. The per-head analysis ruling out head-count confound (3.6× per-head ratio > 3.1× aggregate) is a necessary and well-executed control.

**S1-4. Honest negative results.** Reporting the inverted Δ_pert=−2.2% on Qwen2+Reasoning and the Mistral attenuation (r=0.31 vs 0.47) strengthens credibility. The §5.6 discussion acknowledging +1.0% downstream gain "may not justify the additional complexity" is refreshingly honest.

### Weaknesses

**W1-1 (Major). Critically small evaluation benchmark.** Only 20 AIME problems are used for all cross-axis experiments. With n=20, the difference between r=0.47 and r=0.25 has overlapping 95% confidence intervals (Fisher-transformed CI for r=0.47 at n=20: approximately [0.07, 0.74]). No confidence intervals, error bars, or significance tests are reported anywhere in the paper. The per-problem r values (mentioned as r∈[0.42, 0.49] for Llama) need formal reporting with variance. The "4 of 20 problems show r<0.2 on Mistral" (Table 2) is descriptive but not tested. This undermines the central architecture-modulation claim.

**W1-2 (Major). ε threshold undefined.** The MLP sparsity tolerance metric is defined as "the maximum sparsity at which token t's output remains within ε of the dense output" (§3.4), but ε is never specified. This is a critical parameter — different ε values could produce entirely different correlation profiles. Without this, the correlation results are not reproducible.

**W1-3 (Major). CARC-KV evaluated on the wrong model.** Table 7 evaluates CARC-KV on DeepSeek-R1-Distill-Qwen-7B — the model where the cross-axis signal is weakest (r=0.15) and Δ_pert is negative. If CARC-KV works independently of the cross-axis signal, that's fine, but then it should not be presented as part of the same contribution package. The absence of CARC-KV evaluation on Llama-3.1-8B (where the signal is strongest) is a missed opportunity to show whether cross-axis-informed eviction outperforms vanilla EMA eviction.

**W1-4 (Moderate). Two-tier sparsity gain is marginal.** Table 6 shows +1.0% over matched-average uniform (75.5% vs 74.5%). The +3.5% over uniform-55% comparison is misleading because the effective sparsity levels differ (47% vs 55%). The paper acknowledges this but still leads with "+3.5%" in the section. At this magnitude, measurement noise from 20 problems dominates.

**W1-5 (Moderate). γ sensitivity missing.** EMA decay γ=0.99 is fixed throughout with no sensitivity analysis. For reasoning traces with variable redundancy patterns, γ choice likely matters — a fast decay (γ=0.9) vs slow decay (γ=0.999) could shift which tokens are flagged as redundant. This is a single-hyperparameter method, so a sweep is low-cost and expected.

**W1-6 (Moderate). τ threshold selection opaque.** The two-tier sparsity threshold τ is described as "determined by the EMA anchor similarity distribution" — no formula, no percentile, no selection procedure. This makes replication impossible.

**W1-7 (Minor). 30% KV budget gap downplayed.** At 30% KV budget, CARC-KV perplexity (8.8) is 10% worse than H2O (8.0) and 6% worse than SnapKV (8.3). The paper focuses on the 70% parity result. A fair summary would note that CARC-KV trades quality for latency at aggressive budgets.

### Questions for Authors

1. What is ε in the sparsity tolerance definition?
2. Why not evaluate CARC-KV on Llama-3.1-8B?
3. What is the 95% CI for the r=0.47 vs r=0.25 difference given n=20?

---

## Reviewer 2: Novelty + Related Work

### Strengths

**S2-1. Novel research question.** Linking KV redundancy signals to MLP sparsity allocation through a unified similarity metric is genuinely new. While CLADA (Song et al., 2024a) connects attention patterns to activation sparsity, the explicit hypothesis that cosine-similarity-based KV redundancy should predict per-token MLP sparsity tolerance is a distinct formulation.

**S2-2. Architecture-modulation is a nuanced finding.** In a field where methods are typically presented as universal, reporting a clean positive-on-GQA / negative-on-Qwen2 split is valuable. The finding that the signal can *invert* (Δ_pert=−2.2% on Qwen2+Reasoning) is especially interesting — it warns practitioners against blindly applying cross-axis coordination.

**S2-3. Honest positioning.** The paper does not claim cross-axis coordination is transformative. The §6 discussion explicitly states "incremental benefit for GQA-family models with favorable KV geometry" and "value should be weighed against implementation complexity." This calibrated tone is appropriate for the evidence presented.

**S2-4. Related work is adequate for main areas.** KV cache compression (H2O, SnapKV, StreamingLLM, Token Filtering), MLP sparsification (Deja Vu, CATS, PowerInfer), and efficient reasoning (thinking-token compression, early exit, budget allocation) are all covered with correct citations and clear differentiation.

### Weaknesses

**W2-1 (Major). Incremental over CLADA.** CLADA (Song et al., 2024a) already demonstrates that "attention patterns" predict "activation sparsity," providing "indirect evidence for cross-axis coupling" (paper's own words, §2). The present work replaces "attention patterns" with "EMA-based KV cosine similarity" — a specific instantiation of the same high-level idea. The paper needs to articulate more clearly what the conceptual advance is beyond operationalizing CLADA's observation with a different signal. Currently, the novelty margin is thin.

**W2-2 (Major). n=2 architecture families for an "architecture-modulation" claim.** Claiming architecture is the "dominant modulator" from exactly two architecture families (Llama-GQA and Qwen2-GQA, which differ in group ratio but also in training data, tokenizer, and model details) is a significant overgeneralization. Adding Mistral-7B (same GQA, different magnitude) helps slightly but doesn't address the fundamental issue. The paper would need at least one MHA model and one MLA model (as the original framing intended) to make the architecture claim convincing.

**W2-3 (Major). Missing important related work.** Several relevant KV compression methods are uncited:
- ScissorHands (Liu et al., 2023): importance-based KV eviction with pivotal token detection
- FastGen (Ge et al., 2024): adaptive KV compression with attention-based policies
- PyramidKV (Cai et al., 2024): layer-adaptive KV cache budgeting
- Quest (Tang et al., 2024): query-aware KV cache selection

These methods represent the current state-of-the-art in adaptive KV management and some (PyramidKV's layer-adaptive approach) are directly relevant to the per-layer signal decomposition. Their absence weakens the positioning.

**W2-4 (Moderate). CARC-KV disconnects the story.** The CARC-KV contribution (§3.2, §5.7, §5.8) is presented as a "standalone contribution" that works "independent of the cross-axis hypothesis." This dilutes the paper's focus. Either CARC-KV should be integrated into the cross-axis story (showing that cross-axis-informed eviction beats vanilla EMA eviction) or it should be a separate paper. Currently, it inflates the contribution list without serving the main narrative.

**W2-5 (Moderate). Story consistency issue — speedup claim.** The abstract highlights "up to 26× eviction speedup at 32K sequence length." This is a trivially expected consequence of O(1) vs O(n) complexity — any O(1) method would show similar scaling. Presenting this as a key result overstates the contribution. The speedup is a property of the complexity class, not of the method.

**W2-6 (Minor). No MoE discussion.** MoE architectures (Mixtral, DeepSeek-V2 MoE) implement structural sparsity in the MLP through expert routing. These are highly relevant to the cross-axis story — does router sparsity interact with KV redundancy signals? The paper doesn't discuss this dimension at all.

### Questions for Authors

1. What is the conceptual advance over CLADA beyond using a different similarity signal?
2. Why not test on at least one MHA model (e.g., Llama-2-7B) to broaden the architecture coverage?

---

## Roundtable: Cross-Share (Step 2)

### R1 → R2 Cross-Comments

R1 agrees with R2's concern about CLADA overlap (W2-1). From the methods perspective, if CLADA already establishes that attention-derived signals predict MLP activation patterns, the EMA-based approach is a specific implementation choice, not a new hypothesis. The paper should frame itself as *testing* and *qualifying* CLADA's observation (it's architecture-dependent) rather than proposing a new hypothesis.

R1 also supports W2-4 (CARC-KV disconnect). The fact that CARC-KV is evaluated on the model where the cross-axis signal fails (Table 7 uses DS-R1-Qwen-7B) further emphasizes the disconnect — CARC-KV succeeds precisely where the core hypothesis fails, suggesting it has nothing to do with cross-axis coordination.

### R2 → R1 Cross-Comments

R2 agrees W1-1 (small benchmark) is the most critical weakness. The architecture-modulation claim (W2-2) would be more forgivable if the r=0.47 vs r=0.25 difference were backed by proper statistical tests, but with n=20 and no CIs, the central quantitative claim is shaky. R2 notes that the per-problem r range [0.42, 0.49] for Llama (mentioned in framing doc but not in paper tables) would help if formally reported.

R2 reinforces W1-2 (ε undefined) as critical for novelty assessment — without knowing this threshold, it's impossible to judge whether the observed correlation is robust or an artifact of a particular ε choice.

---

## Roundtable: Convergence (Step 3)

Both reviewers converge on **borderline reject** for a top venue (EMNLP 2026). Agreement on:

1. **Research question is interesting** — linking KV redundancy to MLP sparsity via architecture is a worthwhile direction
2. **Evidence is insufficient** — n=20, no statistical tests, 2 architecture families, undefined ε
3. **Practical impact is marginal** — +1.0% downstream after the honest matched-average comparison
4. **CARC-KV is disconnected padding** — works independently of the core hypothesis, evaluated on wrong model
5. **Novelty margin over CLADA is thin** — needs sharper differentiation

Mild divergence: R2 is slightly more positive on the architecture-modulation finding as a conceptual contribution (novel nuance to the field), while R1 is more concerned about the statistical validity of the quantitative claims. Both agree this does not change the overall assessment.

---

## Tier Alignment (median)

This paper is consistent with a **median-tier** outcome:

- **Positive signals**: The 2×2 factorial design works cleanly, CARC-KV achieves competitive performance, and the paper is unusually honest about its limitations. The pivot from the original GQA-vs-MLA framing (suspended after D005) to group-ratio modulation is handled competently.
- **Median indicators**: The core finding (r=0.47 on Llama, marginal elsewhere) is directionally interesting but not strong enough for a confident accept. The downstream impact (+1.0%) is within noise. The contribution list is padded with CARC-KV to compensate for the modest cross-axis results.
- **Not worst-tier because**: The factorial design provides some structure, CARC-KV has standalone utility, and the paper doesn't make false claims.
- **Not best-tier because**: Statistical rigor is absent, the architecture coverage is too narrow for the claim, and the CLADA novelty gap is unaddressed.

---

## Actionable Recommendations for Research Direction

1. **Expand benchmark to ≥100 problems** (AIME + MATH competition subset) and report bootstrap CIs on all r values
2. **Define and sweep ε** — show correlation robustness across ε ∈ {0.01, 0.05, 0.1}
3. **Add MHA baseline** (Llama-2-7B or similar) and ideally a true MLA model to justify "architecture-modulation"
4. **Either integrate or remove CARC-KV**: evaluate it on Llama with cross-axis-informed eviction, or spin it off
5. **Sweep γ** — at minimum {0.9, 0.95, 0.99, 0.999} to show sensitivity
6. **Sharpen CLADA differentiation** — the contribution is "qualifying and quantifying" the cross-axis coupling, not "discovering" it
7. **Cite missing KV compression work** (ScissorHands, FastGen, PyramidKV, Quest)

---

*Review conducted: 2026-05-12 | Review mode: full (2R roundtable) | Reviewers converged after Round 2*
