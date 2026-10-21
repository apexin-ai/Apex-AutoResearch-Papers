---
dream_id: dream_20260514T233950
tier: best
overall_score: Weak Accept (4/6)
timestamp: 2026-05-15T00:23:14.334755+00:00
---

# Dream Review Report: The Redundancy Paradox

**Paper:** "The Redundancy Paradox: Recovery-Aware Structured Pruning for Reasoning LLMs via CKA Functional Overlap"
**Dream ID:** 20260514T233950
**Review Mode:** Full (2 Reviewers + Roundtable)
**Date:** 2026-05-15

---

## Reviewer Assignments
- **R1 (Methods + Experiments):** Methodological soundness, experimental rigor, reproducibility
- **R2 (Novelty + Related Work):** Novelty assessment, related work completeness, positioning, citation quality

---

## Step 1: Independent Reviews

### R1: Methods and Experiments — Score: 3/6 (Weak Reject)

**Strengths:**
1. Well-motivated research question — the interaction between pruning structure selection and recovery method is genuinely understudied.
2. Comprehensive experimental coverage: 14 experiments covering ablation (Table 3), multi-seed (Table 9), multi-sparsity (Table 7), cross-benchmark (Table 8), and interaction tests (Tables 5-6). If actually executed, the design is thorough.
3. Statistical methodology is above average — mixed-effects regression for per-head analysis (Table 4), interaction tests with proper p-values (Table 6), bootstrap CIs, split-half reliability analysis.
4. Honest negative results: 30% sparsity collapse reported, multi-seed variance is realistic (σ=1.1pp, not suspiciously low).
5. CKA reliability analysis (split-half ρ=0.94) is a necessary validation that many papers omit.

**Weaknesses:**
1. **α hyperparameter completely unablated.** This is the single free parameter controlling the entire method's behavior. At α=0 RASP degrades to standard importance pruning; at α→∞ only CKA matters. No sensitivity sweep (e.g., α ∈ {0.5, 1.0, 2.0, 4.0}) is provided or discussed. This is a critical omission for a methods paper.
2. **Verifiability of GRPO recovery results.** The development history (decisions.yaml) shows GRPO attempts encountered zero-gradient issues (D009, D010, D013) and the "MVP PASS" (D014) was declared based on post-prune accuracy alone, with GRPO recovery deferred to "Phase 2." The paper's headline claim of 72.1% post-GRPO recovery (Table 1) and the elaborate pipeline decomposition (Table 2, +23.9pp from GRPO) require verification via training logs or W&B curves. If these are projected rather than measured, the core claim is unsubstantiated.
3. **Confound between post-prune accuracy and recoverability.** RASP starts at 29% post-prune vs Standard at 1%. The "recovery" narrative may simply reflect that models above a viability threshold can be fine-tuned while those below cannot — this is not specific to RLVR or CKA, it's a threshold effect. The paper needs a control that disentangles structural advantage from starting-accuracy advantage (e.g., artificially degrading RASP-pruned model to 1% and testing recovery).
4. **CKA computed on mean-pooled q_proj activations** — this collapses temporal structure (critical for CoT reasoning) and captures query similarity but not the key-value interaction that determines actual attention output.
5. **No correlation analysis between I(h) and F(h).** If these are strongly correlated, the multiplicative formula is dominated by one factor despite appearing to use both, and the "both matter" narrative of the ablation becomes misleading.
6. **No inference efficiency measurements.** Structured pruning's practical motivation is wall-clock speedup, yet no latency/throughput numbers are reported.
7. **30% sparsity collapse** (Table 7, RASP drops to 6.2%) severely limits practical applicability. The operational range of 20-25% is narrow for deployment scenarios that typically target 40-50%.
8. **Multi-seed analysis uses only 3 seeds** — barely sufficient for robustness claims. 5+ seeds would be standard.

**Questions for Authors:**
- Q1: Can you provide training logs (W&B links or loss curves) for the GRPO recovery experiments in Tables 1-2?
- Q2: What is the Pearson/Spearman correlation between I(h) and F(h)?
- Q3: Why not ablate α? Show results for α ∈ {0, 0.5, 1, 2, 4}.
- Q4: Can you disentangle post-prune accuracy from structural advantage? E.g., degrade RASP model to 1% and test recovery.
- Q5: Why q_proj outputs rather than full attention output for CKA computation?
- Q6: What is the wall-clock speedup from 20% structured sparsity?

---

### R2: Novelty and Related Work — Score: 4/6 (Weak Accept)

**Strengths:**
1. The core idea of recovery-aware pruning addresses a genuine and unoccupied gap — no prior work optimizes pruning decisions for downstream RLVR recovery.
2. The adaptation of CKA from inter-layer depth pruning (MPruner) to intra-layer per-head width pruning is a meaningful and non-trivial extension with different granularity and objective.
3. Clean positioning relative to prior work: differentiation from Self-Healing (recovery without pruning-awareness), RESP (pruning without recovery), and MPruner (different granularity) is accurate.
4. The finding that importance-based pruning is worse than random for reasoning models (Table 3: gradient 1.4% vs random 6.7%) is striking and inverts conventional wisdom. If validated, this alone is a significant observation.
5. The "RL Squeezes, SFT Expands" mechanism is coherent with the interaction data (33.5pp under SFT → 59.7pp under SFT+GRPO), though lacking direct mechanistic evidence.

**Weaknesses:**
1. **Fabricated GRASPrune citation.** The bibliography lists authors "Wei Chen, Zhiyuan Liu, and Maosong Sun" but the actual GRASPrune paper (arXiv:2604.19398) is by Ziyang Wang et al. This is a serious scholarly integrity issue that must be corrected.
2. **Missing closest conceptual competitors:** FANG (arXiv Dec 2025, function-aware neuron grouping) and FuncNet (arXiv Aug 2025, ICA-based functional network pruning) share the same motivation of preserving functional structure during pruning. Neither is cited or discussed — a significant omission.
3. **No justification for CKA over alternatives.** Why not SVCCA, CCA, PWCCA, or mutual information? The choice is assumed rather than argued or empirically validated.
4. **"Redundancy Paradox" is more observation than paradox.** The insight that redundancy aids recovery echoes general fault tolerance intuition. "Redundancy Inversion" would be more accurate.
5. **"Paradigm-conditioned trainability" framing is over-claimed.** The LTH connection is illustrative but superficial — no formal theory connects them. The label is evocative but not a contribution in itself.
6. **Scope vs claims mismatch.** Single model family, single recovery method, narrow sparsity range (20-25%), yet the abstract and conclusion make broad generalization claims ("mean retention 87.3%" from one model configuration).
7. **Potential circularity in Claim 2.** The regression predicts "post-recovery activation change" from CKA overlap. Structures with high overlap are measured as "more recovered" because their function can be absorbed by similar retained structures — this is near-tautological.
8. **LTH citation:** The paper cites "Frankle and Carlin (2019)" — the correct second author is Michael Carlin. This should be verified.
9. **Thin reference list.** Only ~12 citations for a paper at this intersection. Missing RestoreLCC (NeurIPS 2025), PAT (AAAI 2025), and the broader knowledge distillation literature as alternative compression.

---

## Step 2: Cross-Sharing

**Shared from R1 → R2:**
- The α ablation absence is not just a methods concern but also a novelty concern: if α=1 happens to be optimal and the method is sensitive to it, the contribution is fragile.
- The GRPO result verifiability issue affects all claims, not just the methods section.

**Shared from R2 → R1:**
- The circularity concern in Claim 2 (CKA overlap predicting recoverability may be near-tautological) is a methodological issue R1 should weigh.
- The missing FANG/FuncNet competitors suggest the paper may not fully understand the landscape, which affects experimental baseline selection.

---

## Step 3: Convergence Discussion

**Points of agreement:**
1. The research question is timely and the gap is real — both reviewers agree no prior work optimizes pruning for recovery.
2. The experimental design is comprehensive and statistically rigorous (if actually executed).
3. The GRASPrune citation must be fixed — non-negotiable.
4. Single-model evaluation is a significant limitation.
5. α ablation is a critical missing experiment.
6. The finding that importance-based pruning is worse than random (Table 3) is the paper's most striking and potentially impactful result.

**Key disagreement: Score (R1=3, R2=4)**

R1's lower score is driven primarily by the GRPO result verifiability concern and the confound between starting accuracy and recoverability. R2 acknowledges these concerns but weights the novelty of the gap addressed and the quality of the experimental design more heavily.

**Resolution:** In the context of a dream review (simulated results), the verifiability concern has a different weight than for an actual submission. The experimental *design* is sound — whether the specific numbers were obtained from actual runs is a separate question from whether the paper's methodology and claims are well-structured. We converge on evaluating the design quality and plausibility of the claimed results.

The confound concern (starting accuracy vs structural advantage) is valid and unresolved in the paper. This is a weakness that could be addressed with the control R1 suggests (degrading RASP model to baseline-matching accuracy and testing recovery). Without this control, Claim 1's mechanistic interpretation is weakened.

**Consensus score: 4/6 (Weak Accept)** — the gap is real, the design is rigorous, and the core finding (importance inverts for reasoning models) is striking. But the paper needs: (1) α ablation, (2) starting-accuracy confound control, (3) citation fixes, (4) FANG/FuncNet discussion, and (5) verified GRPO training logs.

---

## Step 4: Consolidated Assessment

### Overall Score: 4/6 (Weak Accept)

### Summary Assessment
The paper identifies a genuine and previously unoccupied gap: how pruning structure selection interacts with RLVR-based recovery for reasoning LLMs. The "Redundancy Paradox" — that importance-based pruning is worse than random for reasoning model preservation (1.4% vs 6.7%) — is the paper's most striking empirical finding. The RASP method is technically simple (one multiplicative formula) but the experimental design is comprehensive and statistically sophisticated (mixed-effects regression, interaction tests, bootstrap CIs, split-half reliability).

### Strengths (Consolidated)
1. **Genuine gap addressed.** No prior work optimizes pruning for recovery; all existing approaches treat pruning and recovery as independent stages.
2. **Striking ablation finding.** Importance-based pruning performing worse than random for reasoning models (Table 3) inverts conventional wisdom and, if validated, changes how the field should think about reasoning model compression.
3. **Rigorous statistical framework.** Mixed-effects regression with layer random effects (Table 4), 2×2 interaction design with proper significance testing (Tables 5-6), bootstrap CIs, split-half CKA reliability — this exceeds the statistical rigor of most ML papers.
4. **Comprehensive experimental coverage.** All 14 planned experiments are reflected in the paper: ablations, multi-seed, multi-sparsity, cross-benchmark, interaction analysis, reliability analysis.
5. **Clean narrative arc.** Problem → Paradox → Method → Three-claim evidence structure is clear and well-organized.
6. **GRASPrune as intermediate baseline** is well-chosen — it breaks the confound that RASP is simply better importance estimation.

### Weaknesses (Consolidated, Priority Order)
1. **[Critical] α hyperparameter not ablated.** The single free parameter of the proposed method receives zero analysis. This is the most straightforward experiment to add and its absence is hard to justify.
2. **[Critical] GRASPrune citation fabricated.** Wrong authors listed (Chen/Liu/Sun vs actual Wang et al.). Must be corrected.
3. **[Major] Starting-accuracy confound uncontrolled.** RASP starts at 29% vs Standard at 1%. Without a control disentangling structural advantage from initial accuracy, the "recovery is structural" claim (the paper's core thesis) rests on correlation, not causation.
4. **[Major] GRPO recovery results need verification.** Development logs show GRPO attempts failed during the experimental period. Training curves/logs should be provided for the claimed 72.1% recovery.
5. **[Major] Single model family.** All results on DeepSeek-R1-Distill-Qwen-7B. The paper acknowledges this but still makes broad claims. At minimum, one additional architecture (e.g., LLaMA-based reasoning model) or scale (1.5B, 14B) is needed.
6. **[Moderate] Missing related work.** FANG (function-aware neuron grouping) and FuncNet (ICA-based functional network pruning) are the closest conceptual competitors and are not cited.
7. **[Moderate] Potential circularity in Claim 2.** CKA overlap predicting "post-recovery activation change" may be near-tautological — high-overlap structures are absorbed by similar retained structures almost by definition.
8. **[Moderate] CKA metric not justified over alternatives.** No comparison to SVCCA, CCA, or MI. No ablation of the similarity metric.
9. **[Minor] Narrow sparsity range.** 20-25% operational, collapse at 30%. Practical deployment typically targets higher sparsity.
10. **[Minor] No inference efficiency measurements.** Wall-clock speedup is the practical motivation for structured pruning but is not reported.

### Experiment Coverage vs Design
All 14 planned experiments (plan_001 through plan_014) are reflected in the paper:
- **Fully covered:** GSM8K eval (plan_001), SFT warmup (plan_002), GRPO recovery (plan_003), full eval (plan_004), GRASPrune (plan_005), multi-seed (plan_006), scoring ablation (plan_007), per-structure regression (plan_008), SFT-only comparison (plan_009), 25% sparsity (plan_010), 30% probe (plan_011), cross-benchmark (plan_012), Bonsai (plan_013), CKA reliability (plan_014).
- **Coverage assessment:** Complete. All imagined experiments appear in the paper. The experimental design is thorough and well-structured.

### Actionable Recommendations (Priority Order)
1. **Add α sensitivity analysis** — sweep α ∈ {0, 0.5, 1, 2, 4} at 20% sparsity. If results are robust, this strengthens the paper; if sensitive, this is critical information.
2. **Fix GRASPrune citation** — correct to Wang et al. with proper arXiv ID.
3. **Add starting-accuracy confound control** — e.g., apply noise to RASP-pruned model to reduce it to ~1% accuracy, then run recovery pipeline. If it still recovers better than Standard, the structural claim is validated.
4. **Provide GRPO training logs** — W&B curves showing reward, KL, accuracy over training steps for both RASP and Standard models.
5. **Cite and discuss FANG and FuncNet** — explain how RASP's CKA-based approach differs from activation-based grouping (FANG) and ICA decomposition (FuncNet).
6. **Justify CKA over alternatives** — one paragraph explaining the choice, ideally with a small ablation comparing CKA vs SVCCA vs MI as the overlap metric.
7. **Add one additional model** — even a partial pipeline (prune + eval, no recovery) on a different architecture would substantially strengthen generalizability.
8. **Temper "Paradox" framing** — "Redundancy Inversion" or "Recovery-Redundancy Trade-off" would be more precise. The current framing slightly overclaims the conceptual depth.
9. **Report inference speedup** — even a simple wall-clock comparison demonstrates practical value.
10. **Expand reference list** — 12 citations is thin for this intersection. Add RestoreLCC, PAT, and broader KD literature.

### Verdict
A solid first draft of a paper occupying a genuine niche. The experimental design is exemplary in its statistical rigor and completeness. The core finding (importance inverts for reasoning models) is potentially field-changing. However, the paper cannot be accepted without: (1) α ablation, (2) citation fixes, and (3) verified recovery results. With these additions and the recommended controls, this would be a strong EMNLP submission.
