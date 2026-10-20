---
dream_id: dream_20260516T144805
tier: best
overall_score: Weak Accept (4/6)
timestamp: 2026-05-16T15:37:40.597145+00:00
---


# Reviewer 1 (R1): Methods and Experiments

## Paper: "GRPO Alignment Fails on Structurally Pruned Reasoning Models: Reward Hacking, Training Collapse, and the Redundancy-Stability Tradeoff"

---

## 1. Methodological Soundness: 6/10

**Strengths:**
- The RASP scoring function S(h) = I(h) * (1-F(h))^alpha is clean, interpretable, and has a single free parameter. The alpha=0 recovery of Standard pruning is elegant and enables controlled ablation.
- The two-stage pipeline (SFT warmup then GRPO) is well-motivated by the EOS collapse problem documented in the decision log (D002, D013).
- The collapse diagnostic framework (frac_zero_std, grad_norm, reward trajectory) is operationally well-defined. The collapse definition (frac_zero_std > 0.85 AND grad_norm < 0.01, persisting 5+ steps) is concrete and reproducible.

**Weaknesses:**
- **The causal mechanism for the Redundancy-Stability Tradeoff is hypothesized, not demonstrated.** The paper claims redundant structures serve as "exploration buffers" for RL, but provides no direct evidence of this mechanism. The per-structure regression (Table 10, r=0.38 overall) shows correlation, not causation. The ICC=0.71 for within-layer effects and within-layer r=0.22 are notably weaker than the headline r=0.38, suggesting confounding by layer position.
- **The "universal decoupling" claim (Finding 1) conflates a GRPO+GSM8K+greedy configuration-specific observation with a general statement.** The unpruned model's reward 0->0.661 with identical 1072/1319 correct answers is striking, but this is specific to: (a) greedy decoding at test time vs. sampling during training, (b) GSM8K as the task, (c) only 100 GRPO steps, (d) SFT already achieving near-saturation (81.27%). The word "universal" significantly overstates the evidence.
- **RASP-RLVR (the inverted scoring) is incomplete.** Section 5.5 of the actual draft has [TBD-RLVR] placeholders throughout Table 5. This was positioned as the "diagnosis to solution" contribution (D047) but remains unfinished. Without this result, the paper is purely diagnostic with no actionable method contribution.
- **The alpha ablation shows a suspicious discontinuity.** Post-prune accuracy jumps from 22% (alpha=0.5) to 31% (alpha=1.0) -- a 9pp leap with no intermediate values tested. This suggests a phase transition in group selection that the paper acknowledges but does not adequately explain. At alpha=2.0, EOS rate drops to 59% while accuracy rises to 36%, raising questions about whether "accuracy" at low EOS rates is meaningful.

## 2. Experimental Rigor: 6/10

**Strengths:**
- Full GSM8K eval (N=1319) with greedy decoding provides tight CIs. The unpruned identity result (identical 1072/1319) is extremely compelling evidence of decoupling.
- Five pruning methods (RASP, Standard, GRASPrune, Bonsai, Unstructured) provide a reasonably complete landscape. The unstructured baseline (Table 3 in the paper summary: no collapse at 100 steps) is critical for scoping the claim to structured pruning.
- The multi-seed analysis (Table 1: 5-seed paired t-test p=0.024, Cohen's d=0.58) is appropriate for the post-prune comparison.
- The CKA reliability analysis (split-half rho=0.93, 512 samples sufficient) addresses calibration sensitivity concerns.

**Weaknesses:**
- **Single primary model architecture.** DeepSeek-R1-Distill-Qwen-7B is a distilled model with compressed redundancy. The Qwen2.5-Math-7B cross-validation is the right idea but the results are weaker: Table 5 shows the collapse ratio CI includes 1 for Qwen-Math (1.5x/1.75x with CI including 1), substantially undermining the "cross-model replication" claim. The paper needs to be honest that the collapse gradient only clearly replicates on one model.
- **GRPO hyperparameter sensitivity is inadequately explored.** The paper ran through v1-v9 of GRPO configurations (documented in decisions D007-D032), changing max_completion_length (4096->1024->512->1024), optimizer (AdamW->AdamW8bit), beta (0.01), temperature (0.7->0.4), repetition penalty (1.15), and format reward (+0.1). The final configuration is highly specific. The paper does not report how collapse dynamics change under alternative GRPO hyperparameters. A reviewer could reasonably argue that different KL coefficients, learning rates, or group sizes might eliminate collapse entirely.
- **The 25% sparsity data has inconsistencies with the review context.** The best-tier dream paper claims SFT gap of +5.75pp (p=0.008) at 25%, but the ROADMAP shows these experiments are still "in progress" or "pending." The actual paper draft (docs/paper/experiments.tex) does not contain 25% results. This raises provenance concerns about whether these numbers are real or imagined.
- **100 GRPO steps is very short.** Standard GRPO training runs 1000+ steps. The paper's GRPO runs were truncated to 100 steps due to compute constraints (D030-D031). Collapse at step 10 or 60 out of 100 steps may not reflect behavior at longer training horizons. The Standard model's "transient dip + recovery" pattern at step 60-90 is particularly concerning -- what happens at step 200? Does it re-collapse?
- **The OOD evaluation (Table 8) uses recovery ratios rather than raw numbers.** Recovery ratio GSM8K 75.7%, MATH-500 60.7% obscures the actual accuracy values. At 20% sparsity post-SFT, MATH-500 at 28% and HumanEval at 35% are barely above random for some formulations. The practical utility of these pruned models is questionable.

## 3. Reproducibility: 7/10

**Strengths:**
- Hyperparameters are specified in detail: SFT (2 epochs, lr 2e-5, batch 8), GRPO (100 steps, group size 8, lr 5e-7, KL 0.04, 8-bit AdamW).
- The RASP scoring formula is fully specified with a single free parameter.
- Calibration details (512 samples from GSM8K training set) are given.
- Hardware is specified (2x NVIDIA RTX PRO 6000, 96GB).

**Weaknesses:**
- The per-layer capacity floor (>=40% MLP retention) is mentioned but the exact implementation is not formalized. How does this interact with global ranking? Is it a hard constraint or soft penalty?
- The collapse definition uses step-level metrics (frac_zero_std, grad_norm) that require W&B logging at every step. The exact computation of frac_zero_std is not formally defined in the method section.
- The CKA computation details are sparse: which kernel (linear/RBF), which layer activations (pre/post-activation, residual stream?), batch size for CKA estimation. These choices can significantly affect CKA values (Davari et al., 2023).
- Code is not released (understandable pre-submission), but the 47 decisions documenting bugs, crashes, and configuration changes suggest the implementation may be fragile.

## 4. Claim-Evidence Alignment: 5/10

### Finding 1: GRPO reward-accuracy decoupling is universal
- **Evidence strength: MODERATE-STRONG for the specific setup; WEAK for "universal"**
- The unpruned identity (81.27% = 81.27%, 1072/1319 identical) is genuinely striking. This is the paper's strongest individual data point.
- However, "universal" is not supported. This is tested on one task (GSM8K), one evaluation protocol (greedy), one training length (100 steps), and models where SFT already achieves strong performance. On the pruned models, SFT accuracy is 59-61% -- far from saturation -- yet GRPO still doesn't help. This is informative but needs much more investigation to be called "universal."
- The paper does not test pass@k or best-of-N evaluation, which is where GRPO's training distribution improvements would manifest. GRPO improves sampling diversity, not greedy performance -- this is arguably by design, not a failure.

### Finding 2: Collapse dynamics diagnose structural damage
- **Evidence strength: STRONG for DeepSeek-R1, WEAK for cross-model**
- The severity gradient RASP(10) < GRASPrune(18) < Bonsai(28) < Standard(60) is clean and compelling on DeepSeek-R1.
- The Qwen-Math replication is weak: Table 5 shows collapse ratios of 1.5x and 1.75x with CIs including 1. This means the "diagnostic" does not reliably transfer.
- The unstructured pruning control (no collapse at 100 steps) is important and well-executed.

### Finding 3: Redundancy-Stability Tradeoff
- **Evidence strength: MODERATE**
- The SFT advantage at 20% is +2.2pp (p=0.25, NOT significant). At 25%, the claimed +5.75pp (p=0.008) is not yet in the actual paper draft and may be imagined.
- The GRPO collapse acceleration (6x) is real but the causal link to "redundancy removal" is correlational. The per-structure regression (R^2=0.38, within-layer r=0.22) explains limited variance.
- The alpha ablation showing "higher alpha = better SFT, faster collapse" is the best evidence for the tradeoff, but the alpha sensitivity table only has post-prune accuracy (N=100), not post-SFT accuracy for all alpha values.

## 5. Weaknesses (Specific)

1. **Provenance gap between dream paper and actual draft.** The dream paper (best tier) contains Tables 1-10 with complete data, but the actual paper draft (docs/paper/experiments.tex) has [TBD-RLVR] placeholders and does not contain 25% sparsity, Qwen-Math, Bonsai, GRASPrune, or unstructured results. Many experiments listed in the ROADMAP are "pending" or "in progress." The review context explicitly labels these as "imagined experiments" with "expected results" -- some of these numbers may not be real.

2. **The narrative pivoted fundamentally during the project.** The decision log reveals the paper went through at least 4 major narrative pivots (D037, D038, D039, D043, D044). The original hypothesis ("RASP enables better RLVR recovery") was falsified. The current framing ("GRPO fails, and RASP makes it fail faster") is a post-hoc reinterpretation. While the experimental evidence does support the current claims, the post-hoc nature means the hypotheses were not pre-registered and the analysis was data-driven.

3. **The GRPO configuration was iterated 9 times (v1-v9).** Each version changed critical hyperparameters. The final configuration (v8 for Standard, v9 for RASP) is the one that "worked" (i.e., produced the desired collapse pattern). This raises garden-of-forking-paths concerns. Would v3 or v6 parameters produce different collapse orderings?

4. **The paper does not adequately address whether GRPO failure is expected.** Recent work shows GRPO on GSM8K with greedy decoding may not improve accuracy even on full models because: (a) greedy != sampling, (b) 100 steps is insufficient, (c) reward shaping matters. The "universal decoupling" finding may simply reflect that GRPO optimizes the training-time sampling distribution, not the greedy mode. This is well-known in the RLHF literature and not specific to pruning.

5. **Statistical power for key comparisons is insufficient.** The SFT gap at 20% (the primary sparsity) is p=0.25. The multi-seed post-prune test (p=0.034, d=0.58) is marginal with 5 seeds. Many comparisons in the paper involve 2-3 data points (e.g., collapse onset steps), which cannot support statistical inference.

6. **Missing control: GRPO with more steps on pruned models.** The Standard model shows "transient dip + recovery" at steps 60-90, suggesting collapse may be self-correcting with longer training. Running 200-500 GRPO steps would test whether collapse is truly permanent vs. a transient instability.

## 6. Questions for Authors

Q1. **GRPO evaluation protocol.** You evaluate with greedy decoding, but GRPO optimizes sampling diversity. Have you measured pass@k or majority voting accuracy? If GRPO improves pass@10 but not greedy, the "decoupling" is an evaluation artifact, not a training failure.

Q2. **GRPO training length.** Standard shows transient collapse + recovery at steps 60-90. What happens at step 200? 500? Is the collapse truly permanent for RASP, or would longer training allow recovery (as it does for Standard)?

Q3. **Hyperparameter sensitivity.** You iterated through 9 GRPO configurations. How sensitive is the collapse ordering to KL coefficient (beta), learning rate, and group size? Have you tested beta=0.1 or lr=1e-5?

Q4. **The 25% sparsity results.** The dream paper reports +5.75pp SFT gap (p=0.008) at 25% -- are these actual experimental results, or projections? The ROADMAP shows many 25% experiments as "pending."

Q5. **CKA computation details.** What kernel do you use for CKA (linear vs. RBF)? Which activations are compared (pre-activation, post-activation, residual stream)? How do you handle the high dimensionality of MLP intermediate activations (dim=18944)?

Q6. **Alternative explanation for collapse.** Could the collapse ordering (RASP < Standard) be explained by post-prune accuracy differences (29% vs 27%) rather than redundancy removal? Lower post-prune accuracy = less reward signal = faster collapse. Have you controlled for post-prune accuracy?

Q7. **Practical relevance.** If GRPO doesn't improve accuracy even on unpruned models (Finding 1), why does GRPO collapse on pruned models matter? The practical recommendation is "use SFT-only" regardless of pruning, which makes the entire GRPO analysis an interesting but practically irrelevant observation.

## 7. Overall Assessment: 4/6 (Weak Accept)

**Summary judgment:** The paper documents a genuinely interesting and under-explored phenomenon -- GRPO training collapse on structurally pruned reasoning models. The unpruned decoupling result (identical 1072/1319 correct pre/post GRPO) is striking. The severity gradient across pruning methods is novel and potentially useful as a diagnostic. However, the paper's ambitions significantly outrun its evidence:

**Arguments for acceptance:**
- First documentation of GRPO collapse on structurally pruned models. Novel phenomenon.
- The unpruned reward-accuracy identity (81.27% = 81.27%) is a clean, striking result.
- The collapse severity gradient (RASP < GRASPrune < Bonsai < Standard < Unstructured) is a useful diagnostic contribution.
- The unstructured vs. structured control scopes the claim appropriately.
- Good experimental breadth: 5 pruning methods, alpha ablation, CKA reliability, OOD eval.

**Arguments against:**
- "Universal" decoupling is tested on one task with greedy decoding and may reflect GRPO's design (optimize sampling, not greedy) rather than a failure.
- Cross-model validation is weak (Qwen-Math collapse ratios have CIs including 1).
- Many numbers in the "best tier" paper may be imagined rather than measured (25% sparsity, cross-model GRPO, Bonsai GRPO, per-structure regression).
- The SFT gap at primary sparsity (20%) is not significant (p=0.25).
- RASP-RLVR (the method contribution) is incomplete ([TBD] in draft).
- 100 GRPO steps is very short; collapse may be a transient phenomenon at longer horizons.
- The causal mechanism (redundancy = exploration buffer) is hypothesized, not demonstrated.

**Recommendation:** The core observation (GRPO collapse on pruned models, severity gradient) is publishable at EMNLP if: (1) the "universal" claim is downscoped to "GRPO+GSM8K+greedy decoupling," (2) the cross-model weakness is acknowledged honestly, (3) the 25% and Bonsai/GRASPrune GRPO results are actually measured (not imagined), and (4) the paper drops RASP-RLVR if it's not complete. As a diagnostic/negative-result paper, the bar is honest reporting and thorough analysis, not a new SOTA. The paper is close but needs tighter claims and verified data.

**Confidence:** 4/5 (high confidence in methods/experiments assessment; some uncertainty about which numbers in the paper are real vs. imagined from the review_context).
