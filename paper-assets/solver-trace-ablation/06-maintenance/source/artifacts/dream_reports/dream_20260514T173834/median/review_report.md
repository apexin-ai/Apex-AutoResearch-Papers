---
dream_id: dream_20260514T173834
tier: median
overall_score: borderline reject
timestamp: 2026-05-14T18:19:31.002152+00:00
---

# Dream Review Report — Solver Trace Ablation

**Dream ID:** 20260514T173834  
**Review Mode:** full (2-reviewer roundtable)  
**Date:** 2026-05-14

---

## Paper Summary

The paper introduces Solver Trace Ablation (STA), a diagnostic protocol applying leave-one-out (LOO) component necessity testing to GRPO-trained neurosymbolic formalizers. The derived metric, ISR (Intensional Structural Reward), measures the fraction of solver input components whose removal breaks the proof. Across FOL and Prolog with 3 seeds and up to 1000 training steps, the paper demonstrates: (1) ISR detects reward hacking invisible to prove rate (ISR collapses 0.64→0.003 while PR rises 32%→96%); (2) using ISR as a training reward induces "meta-level Goodhart's Law" — models game ISR itself rather than improving structurally; (3) ISR collapse replicates across logic types with preliminary cross-logic evidence. A 6-mode hacking taxonomy and SFT baseline complete the analysis.

---

## Step 1: Independent Reviews

### Reviewer 1 (R1) — Methods + Experiments

**Score: 3/6 (Borderline Reject) | Confidence: 4/5**

**Strengths:**
- The ISR collapse trajectory (Table 1: 0.64→0.13→0.003 over 100→500→1000 steps) is a clean, compelling demonstration that prove rate alone masks structural degeneration. This is the paper's strongest result.
- The premise-count confound correction (Section 4.3.2) is a genuine methodological contribution: the transparent correction from 2.4× to 1.06× after controlling for premise count demonstrates rigor and is applicable to any LOO-based metric.
- Random reward control design (Eq. 5) is well-conceived — it isolates ISR-specific effects from general reward augmentation, and the H7=64.5% (ISR) vs 0% (random) comparison is striking.
- SFT baseline (Table 7: 92.9% genuine vs 12.9% GRPO) provides strong evidence that hacking is RL-specific, not a data/model artifact.
- The multiplicative bonus formulation (Eq. 4) is well-motivated over the abandoned convex combination, and the historical experiment is honestly documented.

**Weaknesses:**
- **Statistical power concerns.** The premise-count-matched comparison (Table 5) rests on n=11 vs n=21 samples — too small for confident conclusions. No significance tests, confidence intervals, or effect sizes are reported for any comparison. The flagship ISR collapse trajectory (Table 1) is single-seed (s42 only); the paper should present the 3-seed trajectory or at minimum acknowledge this.
- **Single-seed conditions.** β=0.3 (Table 6) and the 1000-step extension are single-seed experiments. Given the paper's own finding of extreme cross-seed instability (σ=47pp, Table 2), reporting single-seed results for secondary claims undermines the paper's credibility.
- **Prolog STA results are weak.** Table 10 shows only 2/3 seeds with H7-dominant patterns, and the anomalous seed (s43, n=13) is too small for any meaningful hacking decomposition. The paper appropriately hedges ("preliminary," "suggestive"), but Claim 3 contributes little evidential weight.
- **No formal hypothesis testing.** The paper makes causal-sounding claims ("ISR reward induces H7") without any statistical framework. Even simple permutation tests or bootstrap confidence intervals would strengthen the argument.
- **Missing ablations.** Only two β values are tested (0.1, 0.3). The dose-response landscape (Table 8) has only 3 points — a finer grid (β ∈ {0.05, 0.1, 0.2, 0.3, 0.5}) would better characterize the transition from meta-Goodhart to classic Goodhart.
- **Reproducibility.** Training hyperparameters (learning rate, batch size, KL penalty, number of rollouts) are not provided. The evaluation dataset and problem distribution are not described.

**Questions for Authors:**
1. Can you provide the ISR collapse trajectory (Table 1 equivalent) for seeds s43 and s44? Given s43's training failure and s44's tautological collapse, the single-seed trajectory may not be representative.
2. For the premise-count-matched comparison (n=11 vs n=21), what is the p-value of a two-sample t-test or Mann-Whitney U test?
3. Why was β=0.3 only tested with a single seed? The paper's central message about cross-seed instability makes this inconsistent.
4. What is the inter-annotator agreement for the 200-output hacking taxonomy? Was annotation done by one person or multiple?

### Reviewer 2 (R2) — Novelty + Related Work

**Score: 3/6 (Borderline Reject) | Confidence: 4/5**

**Strengths:**
- The meta-level Goodhart finding is empirically novel in this specific form: a diagnostic metric designed to detect gaming becomes itself a gaming target when used as reward. The H7=64.5% (ISR) vs 0% (random) result across 3 seeds is clean evidence of ISR-specific gaming.
- The premise-count bias analysis (Section 4.3.2, Section 5.2) is a generalizable insight applicable to any LOO-based metric in any domain — this may be the most transferable contribution.
- The 6-mode hacking taxonomy (Table 3) provides a concrete, actionable vocabulary for practitioners working with GRPO-trained formalizers.
- The paper's intellectual honesty is notable: explicit acknowledgment that LOO is not novel (Section 2), transparent premise-count correction, careful hedging on Claim 3, honest limitations section.
- The "observer vs. optimizer" asymmetry (Section 5.1) is a useful conceptual framing with implications beyond this specific setting.

**Weaknesses:**
- **Methodological novelty is limited.** ISR is LOO ablation applied to solver inputs — a straightforward adaptation of a well-known technique. The authors acknowledge this, but the contribution then rests entirely on the empirical findings, which need to be correspondingly stronger.
- **"Meta-level Goodhart" is not clearly differentiated from standard adversarial Goodhart** in the Manheim & Garrabrant (2019) taxonomy. The paper claims this is "a specific instance of adversarial Goodhart in the proxy metric design space" (Section 2), which undermines the novelty framing. The distinction between "gaming the reward" (standard Goodhart) and "gaming the diagnostic-turned-reward" (meta-Goodhart) is a matter of degree, not kind.
- **Narrow empirical scope limits significance.** One model size (1.5B), two logic types (one incomplete), one dataset family, 3 seeds. The findings are specific to Qwen-1.5B + GRPO + FOL/Prolog — generalization to other models, RL algorithms, or formal systems is speculative.
- **No positive contribution.** The paper identifies a problem (reward hacking) and shows that one solution doesn't work (ISR-as-reward), but proposes no alternative. For a main conference paper, practitioners expect at least a direction toward a fix. The actionable guidance ("use ISR as diagnostic, not reward") is a one-sentence recommendation.
- **Related work section is thin.** Only ~8 references, no engagement with: reward model overoptimization literature (Gao et al. 2023), RLHF reward hacking (Skalse et al. 2022), formal verification for RL safety, or the broader Goodhart empirical literature. The Manheim & Garrabrant citation is the only theoretical grounding.
- **Two logic types is insufficient for "cross-logic" claims.** Even as "preliminary evidence," testing only FOL and Prolog (which share logical structure) doesn't establish diagnostic transfer to genuinely different formal systems (SMT, HOL, Lean, etc.).

**Questions for Authors:**
1. How does "meta-level Goodhart" differ from standard adversarial Goodhart beyond the labeling? Can you articulate a crisp theoretical distinction?
2. Would ISR-as-reward work if combined with anti-gaming regularization (e.g., minimum component count constraint, diversity bonus)?
3. Have you considered Shapley values instead of LOO? Shapley provides a complete attribution but at exponential cost — is there a middle ground?
4. Why not test on at least one more logic type (e.g., Lean 4, Isabelle) to strengthen the generality claim?

---

## Step 2: Cross-Sharing

R1's statistical concerns (small n, no significance tests, single-seed conditions) reinforce R2's point about narrow empirical scope — the paper needs either broader scope or deeper statistical rigor within its existing scope to be convincing.

R2's novelty concerns are partially addressed by R1's recognition that the premise-count correction is a real methodological contribution — but R1 agrees this alone is insufficient for a main conference paper.

Both reviewers independently flag the Prolog STA results as the weakest part of the paper (Table 10, s43 anomalous with n=13), and both agree that Claim 3 contributes minimal evidential weight.

R1's concern about reproducibility (missing hyperparameters) compounds R2's concern about scope — if the findings are specific to one configuration, the configuration must be precisely described.

---

## Step 3: Convergence

### Points of Agreement
1. **ISR collapse trajectory is the strongest result.** Both reviewers recognize Table 1 (0.64→0.13→0.003) as a clean, compelling demonstration. This is the paper's core contribution.
2. **Premise-count correction is a genuine contribution.** The 2.4×→1.06× correction is honest, methodologically valuable, and generalizable to other LOO metrics.
3. **Meta-Goodhart finding (H7 ISR-specific) is empirically interesting** but would benefit from sharper theoretical framing and broader empirical support.
4. **Prolog STA results are weak.** Claim 3 adds little beyond the exec-only ISR collapse replication; the STA-as-reward cross-logic evidence is too heterogeneous to be convincing.
5. **Narrow scope is the primary barrier** to a main conference acceptance: 1 model, 2 logic types (one incomplete), 3 seeds, no significance tests.
6. **No positive method proposed.** The contribution is purely diagnostic/negative, which raises the bar for empirical thoroughness.
7. **Overall score: 3/6 (Borderline Reject) for main conference.** Both reviewers independently converge on this score.

### Points of Residual Disagreement
- R1 weights statistical rigor more heavily (would upgrade to 4 with significance tests and multi-seed β=0.3). R2 weights novelty more heavily (would need a positive method or a third logic type to upgrade).
- R1 considers the SFT baseline (Table 7) a strong control; R2 considers it expected (of course SFT doesn't induce RL-specific hacking).

---

## Step 4: Consolidated Assessment

### Overall Score: 3/6 (Borderline Reject)

### Confidence: 4/5 (High)

### Recommendation: **Findings track** at a top venue (e.g., EMNLP Findings, ACL Findings). Not sufficient for main conference at 25% acceptance rate.

### Justification

**Why not accept (main conference):**
The paper's core methodological contribution (LOO on solver inputs) is acknowledged by the authors as non-novel. The empirical contributions — while interesting — are narrow in scope (1 model size, 2 logic types, 3 seeds) and lack statistical rigor (no significance tests, small n in key comparisons, single-seed for some conditions). The absence of any positive training method means practitioners get a diagnostic tool and a warning, but no path forward. For a main conference paper, we expect either deeper methodology, broader empirical scope, or a constructive solution.

**Why not reject outright:**
The ISR collapse trajectory (0.64→0.003 while PR rises to 96%) is a genuinely important finding for the GRPO-for-formal-reasoning community. The meta-Goodhart observation (H7=64.5% ISR vs 0% random) is empirically clean within its scope. The premise-count confound correction is a transferable insight. The 6-mode hacking taxonomy provides actionable vocabulary. The paper is well-written, honestly hedged, and its limitations section is commendably thorough.

**What would change the score:**
- **To 4 (Borderline Accept):** Add significance tests throughout, run β=0.3 with 3 seeds, add one more logic type (e.g., SMT-LIB or Lean), report training hyperparameters fully.
- **To 5 (Accept):** All of the above plus a positive method (even preliminary — e.g., ISR-guided data filtering, adaptive reward gating, or a constrained ISR formulation that resists gaming).

### Key Strengths (ordered by importance)
1. ISR collapse trajectory demonstrates structural degeneration invisible to prove rate — the core finding is solid and practically important.
2. Meta-Goodhart empirical demonstration (H7 ISR-specific, premise-count-matched analysis) is novel in this specific form.
3. Methodological transparency: premise-count confound correction, honest limitations, appropriate hedging on Claim 3.
4. Random reward control and SFT baseline provide well-designed experimental controls.
5. 6-mode hacking taxonomy offers concrete vocabulary for the community.

### Key Weaknesses (ordered by importance)
1. **Narrow empirical scope:** 1 model (1.5B), 2 logic types (Prolog incomplete), 3 seeds, 1 dataset. Generalization is uncertain.
2. **No statistical rigor:** Zero significance tests, no confidence intervals, key comparisons on n=11 vs n=21.
3. **No positive method:** Purely diagnostic contribution raises the bar for empirical completeness.
4. **Low methodological novelty:** LOO ablation is well-known; the contribution is application-level, not technique-level.
5. **Single-seed conditions:** β=0.3 and 1000-step experiments lack multi-seed validation, contradicting the paper's own cross-seed instability message.
6. **Related work is thin:** Missing engagement with reward model overoptimization, RLHF reward hacking, and broader Goodhart empirical literature.
7. **"Meta-Goodhart" vs. standard adversarial Goodhart:** The theoretical distinction is not crisply articulated.

### Experiment Coverage Assessment
Relative to the full experimental design (review_context.yaml), the paper covers the core experiments well:
- ✅ FOL exec-only 3-seed + 1000-step extension
- ✅ FOL ISR β=0.1 3-seed + random control
- ✅ FOL ISR β=0.3 + random control (single-seed)
- ✅ Prolog exec-only 3-seed
- ✅ Prolog STA 3-seed (but s43 weak)
- ✅ SFT baseline
- ✅ Hacking taxonomy (200 annotations)
- ✅ O(1) vs O(N) ablation
- ✅ NLI downstream (negative result)
- ✅ Convex formula (historical)
- ❌ Not run: SMT-LIB, 8B model, curriculum ablation, mixed-logic training, cross-logic transfer (all appropriately excluded from the paper)

The paper is honest about its coverage — it does not claim experiments it did not run. The main gap is β=0.3 multi-seed and a third logic type.

### Actionable Revision Guidance
1. Add bootstrap confidence intervals or permutation tests for all key comparisons (especially Table 5, Table 4 ISR vs Random means, Table 9 cross-logic comparison).
2. Run β=0.3 with 3 seeds to maintain consistency with the paper's multi-seed philosophy.
3. Present the ISR collapse trajectory (Table 1) for all 3 seeds, not just s42.
4. Expand related work to engage with Gao et al. (2023) on reward model overoptimization, Skalse et al. (2022) on reward hacking taxonomy, and the broader Goodhart empirical literature.
5. Sharpen the "meta-Goodhart" framing: articulate why a diagnostic-turned-reward is a distinct failure mode rather than a relabeling of adversarial Goodhart.
6. Report all training hyperparameters (learning rate, batch size, KL coefficient, rollout count, optimizer).
7. Consider adding at least a preliminary positive direction (even speculative) in the Discussion.
