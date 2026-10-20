---
dream_id: dream_20260514T173834
tier: worst
overall_score: weak reject
timestamp: 2026-05-14T18:26:26.536575+00:00
---

# Dream Review Report: "Diagnosing and Characterizing Reward Hacking in GRPO-Trained Formal Reasoners"

**Dream ID**: 20260514T173834
**Review Mode**: Full (2 Reviewers + Roundtable)
**Date**: 2026-05-14

---

## Roundtable Summary

| Reviewer | Focus | Score | Confidence |
|----------|-------|-------|------------|
| R1 | Methods + Experiments | 3 (Weak Reject) | 4/5 |
| R2 | Novelty + Related Work | 4 (Weak Accept) | 4/5 |
| **Consensus** | — | **3 (Weak Reject)** | **4/5** |

---

## Step 1: Independent Reviews

### R1 — Methods and Experiments

**Score: 3 (Weak Reject) | Confidence: 4/5**

**Summary**: The core ISR diagnostic and meta-Goodhart finding on FOL are well-motivated and partially well-evidenced, but the paper presents results from experiments that do not appear in the experimental record, lacks statistical testing throughout, and would be stronger as a focused FOL study with honest scope and significance tests.

#### Strengths
1. **ISR collapse trajectory is dramatic and well-evidenced.** The 0.64→0.13→0.003 collapse while PR rises to 93-96% is a striking result demonstrating diagnostic value of structural metrics beyond pass/fail.
2. **H7 as ISR-specific gaming is convincing.** H7=0% across all random seeds vs. H7=64.5% across ISR seeds is the paper's cleanest causal finding, establishing that optimizing a diagnostic metric induces metric-specific exploitation.
3. **Premise-count-matched correction is a genuine methodological contribution.** The self-correction from 2.4× to 1.06× is a model of honest self-correction and is generalizable to any LOO-based metric.
4. **SFT baseline is well-designed.** 92.9% genuine under SFT vs. 12.9% under GRPO cleanly attributes hacking to RL optimization pressure.
5. **Honest negative results.** NLI null correlation (ρ=−0.049), O(1) approximation failure, and ISR capability boundary are reported transparently.

#### Weaknesses
1. **Data integrity concern for Claim 3 experiments.** SMT-LIB (Table 16), 8B scaling (Table 10), curriculum ablation (Table 9), and joint training (Table 14) present detailed numerical results, but the project's internal audit documents list no completed experiments for several of these. If results are projected rather than measured, this is a fatal flaw.
2. **No statistical significance testing anywhere.** All comparative claims (1.06×, 64.5% vs 0%, PR 0.77 vs 0.85) lack confidence intervals, p-values, or effect sizes. The premise-count-matched comparison (n=11 vs n=21) is presented as definitive without bootstrap CIs.
3. **Key conditions are single-seed.** β=0.3 (both ISR and random), the 1000-step trajectory, and the SFT baseline are each n=1. Given documented extreme seed variance, this limits causal claims.
4. **Model identity inconsistency.** The paper references both "Qwen3-1.5B" and potentially different actual model sizes. This must be resolved as it affects all reproducibility and scaling claims.
5. **ISR-as-reward exploration is shallow.** Only one functional form (additive bonus) at two β values. The sweeping conclusion that ISR fails as an optimizer at any dose is not supported. Alternative formulations (ISR as rejection filter, ISR with anti-H7 heuristics) are not explored.

#### Key Questions
1. Can you provide experiment logs and eval outputs for Tables 9, 10, 14, 16? Internal audit documents do not list these as completed.
2. What is the 95% bootstrap CI on the 1.06× ratio? With n=11, this could range from 0.6× to 1.8×.
3. Why was only seed 42 extended to 1000 steps? Does the ISR collapse replicate across seeds?
4. Have you considered ISR as a rejection criterion rather than continuous reward?
5. What is the actual model identity (1.5B vs 4B discrepancy)?

---

### R2 — Novelty and Related Work

**Score: 4 (Weak Accept) | Confidence: 4/5**

**Summary**: A well-controlled empirical case study of Goodhart's Law in formal reasoning GRPO, with a useful diagnostic (ISR) and honest negative results, but undermined by severely insufficient related work, overclaimed novelty, and questionable completeness of cross-logic experiments.

#### Strengths
1. **Rigorous controls.** 3-seed design with random-reward controls, SFT baseline, and premise-count-matched analysis demonstrates careful methodology. Random-reward confirming H7=0% across all seeds is clean.
2. **Honest negative results.** Transparent reporting that ISR fails as reward at every dose, and that 2.4× improvement was a statistical artifact, is commendable and rare.
3. **Premise-count-matched methodology.** Identifying and controlling for component-count bias in LOO metrics is a genuine contribution applicable beyond this paper.
4. **Temporal ISR collapse trajectory.** The 0.64→0.003 collapse while PR stays 93-96% is a clean and memorable finding.
5. **Comprehensive Goodhart landscape.** Table 7 covering 10+ conditions with consistent evaluation is thorough and informative.

#### Weaknesses
1. **Severely insufficient related work.** Only 7 references is unacceptable for any ML venue. Critical omissions include:
   - Skalse et al. (2022, NeurIPS) — formal proof that any non-constant proxy is hackable
   - Kim et al. (2026, VerifAI-2) — "Do LLMs Game Formalization?" (same phenomenon in Lean 4)
   - RLSF (Jha et al. 2024) — solver certificates as token-level reward
   - Lightman et al. (2023) — process vs. outcome supervision
   - Logic-RL, LINC, Logic-LM — neurosymbolic reasoning competitors
   - Mutation testing literature (DeMillo 1978) — ISR is essentially a first-order mutation score
   - Pan et al. (2022) — dose-dependent reward misspecification
   Minimum 25 references needed.
2. **Overclaimed novelty.** "Meta-level Goodhart" is standard Goodhart applied to a new proxy. The term implies a recursive structure that does not exist. ISR is a straightforward application of LOO/mutation testing to solver inputs. The paper should position itself as an empirical case study, not a conceptual advance.
3. **Questionable data integrity for Claim 3.** SMT-LIB, joint-training, curriculum, and 8B numbers in the draft may extend beyond completed experiments. Prolog STA s43/s44 may have been still running at draft time.
4. **Narrow experimental scope.** Single model family (Qwen3), single RL algorithm (GRPO), single problem domain (FOLIO-style NLI), small eval set (100 problems). Generality claims require broader validation.
5. **ISR's fundamental limitation: syntactic necessity ≠ semantic faithfulness.** ISR correlates poorly with NLI accuracy (ρ=−0.049). High-ISR proofs are non-redundant but not necessarily faithful to the natural language input. The paper acknowledges this but offers no path forward.

#### Key Questions
1. Can you confirm all numbers in Tables 9-16 correspond to completed experiments with full evaluation?
2. Why not cite mutation testing? ISR is a first-order mutation score. The coupling effect (DeMillo 1978) provides theoretical justification for why single-component deletion suffices.
3. How does ISR behave on problems requiring 5+ step proofs? Does O(N) cost become prohibitive?
4. Have you considered Shapley values instead of LOO to capture interaction effects?
5. How is "meta-level Goodhart" different from standard Goodhart? If ISR is replaced with any bounded [0,1] proxy, would the same phenomenon not occur?

---

## Step 2: Cross-Sharing Reactions

### R1 reacting to R2's review
- **Agrees** on severely insufficient references. R1 did not emphasize this but concurs that 7 references is disqualifying.
- **Agrees** on overclaimed "meta-level Goodhart" framing. R1 notes the paper tests only one reward formulation at two β values, which compounds the overclaiming.
- **Supports** R2's mutation testing connection. ISR as first-order mutation score is an apt characterization R1 had not considered.
- **Disagrees partially** on score. R1 maintains that data integrity concerns for Claim 3 experiments push toward Reject rather than Weak Accept, as presenting potentially non-existent experimental results is more severe than insufficient references.

### R2 reacting to R1's review
- **Agrees strongly** on data integrity concern. R2 had flagged this independently but R1's detailed cross-referencing with internal audit documents makes the concern more concrete.
- **Agrees** on need for statistical testing. The n=11 vs n=21 premise-count comparison without CIs is indeed a notable gap.
- **Agrees** on model identity discrepancy. This is a basic reproducibility requirement.
- **Adjusts position**: R2 acknowledges that if Claim 3 experiments are indeed projected rather than measured, the score should drop. R2 conditionally revises to 3 (Weak Reject) if data integrity issues are confirmed.

---

## Step 3: Convergence

### Points of Agreement (both reviewers)
1. **Claims 1 and 2 on FOL are the paper's core strength.** ISR collapse trajectory and H7-as-ISR-specific-gaming are well-evidenced and compelling for the FOL domain.
2. **Claim 3 (cross-logic) is the paper's core weakness.** Data integrity concerns, extreme seed variance (σ_H7=0.55), and training failures make cross-logic claims unsupportable. The paper should either drop Claim 3 or restrict it to a brief "preliminary exploration" section.
3. **Premise-count-matched methodology is a genuine contribution.** Both reviewers highlight this as the paper's most generalizable technical insight.
4. **Statistical rigor is insufficient.** No significance tests, CIs, or effect sizes anywhere. Critical for a paper whose conclusions depend on small-sample comparisons.
5. **The paper needs substantially more references.** 7 references is disqualifying. 25+ needed, covering reward hacking theory, neurosymbolic reasoning, mutation testing, process rewards.
6. **"Meta-level Goodhart" framing overclaims.** This is standard Goodhart on a new proxy, not a novel conceptual contribution. Reframe as empirical case study.
7. **Honest reporting of negative results is commendable.** The self-correction from 2.4× to 1.06×, NLI null correlation, and O(1) failure are models of scientific integrity.

### Points of Remaining Disagreement
1. **Severity of data integrity concern.** R1 treats potentially fabricated/projected results as near-fatal; R2 treats it as fixable if the paper is scoped to completed experiments only. Both agree it must be resolved, but R1 weighs it more heavily in scoring.
2. **Publishability of a scoped version.** R2 sees a path to Findings-level acceptance if the paper is reduced to a 2-claim FOL study with proper references and statistical tests. R1 is less optimistic, noting that even Claims 1-2 have single-seed conditions (β=0.3, 1000-step, SFT) and no significance tests.

### Consensus Score Rationale
Both reviewers converge on **3 (Weak Reject)** as the appropriate score for the current manuscript. The core FOL findings are interesting but the paper has critical issues: (1) potential data integrity problems in Claim 3, (2) zero statistical testing, (3) severely insufficient references, and (4) overclaimed novelty. A substantially revised version — scoped to FOL, with proper statistical analysis, 25+ references, and repositioned as an empirical case study — could reach Findings acceptance (estimated 30-50% probability).

---

## Step 4: Consolidated Assessment

### Overall Score: 3 (Weak Reject)
### Confidence: 4/5

### Decision Rationale

The paper presents an interesting empirical observation — ISR collapse reveals structural degeneration invisible to prove rate, and ISR gets Goodharted when used as reward — but falls short of top-venue standards in its current form.

**What works:**
- The ISR diagnostic concept is sound and the collapse trajectory (0.64→0.003 over 1000 steps while PR stays >93%) is a memorable empirical finding
- The H7-as-ISR-specific artifact (64.5% under ISR reward, 0% under random reward) is clean causal evidence
- The premise-count-matched correction (2.4×→1.06×) is a generalizable methodological contribution
- Controls (random reward, SFT baseline) are well-designed
- Negative results are reported honestly

**What doesn't work:**
- **Data integrity**: Multiple tables may present results from experiments not in the experimental record. This is the most serious concern.
- **Statistical void**: Zero significance tests in a paper built on small-sample comparisons (3 seeds, 100 eval problems, n=11 vs n=21 for the key confound analysis)
- **Reference desert**: 7 references for a topic with 50+ relevant works. Critical omissions include Skalse et al. (proxy hackability proof), Kim et al. (formalization gaming in Lean), mutation testing literature, process reward literature
- **Overclaimed contributions**: "Meta-level Goodhart" is standard Goodhart; LOO on solver inputs is mutation testing; hacking taxonomy is error analysis
- **Scope mismatch**: Abstract claims breadth (3 logics, 2 model scales, 5 curricula) that the evidence does not support

### Actionable Recommendations

1. **Scope to 2 claims on FOL only.** Drop Claim 3 or reduce to 1 paragraph of preliminary exploration. The FOL evidence is strong enough for a focused paper.
2. **Add statistical tests.** Bootstrap CIs for all comparative claims. Permutation test for the 1.06× ratio. Report effect sizes.
3. **Expand references to 25+.** Must cite: Skalse et al. 2022, Kim et al. 2026, Lightman et al. 2023, Pan et al. 2022, mutation testing (DeMillo 1978), RLSF (Jha 2024), Logic-RL, LINC.
4. **Reframe novelty.** Position as "first controlled empirical study of Goodhart's Law in formal reasoning RL" rather than claiming conceptual novelty. Rename "meta-level Goodhart" to something more precise.
5. **Resolve model identity.** Clarify the actual model used across all experiments.
6. **Verify all reported numbers.** Every table entry must correspond to a completed experiment with traceable logs.
7. **Extend multi-seed coverage.** Run all 3 seeds for β=0.3 and the 1000-step trajectory. Single-seed conditions undermine key claims.
8. **Target venue**: EMNLP Findings or similar (not main conference) after revisions. Estimated acceptance probability after recommended revisions: 30-50%.

### Experiment Coverage Assessment

| Planned Experiment | Covered? | Quality |
|---|---|---|
| Prolog STA s43 (training collapse) | Yes (§8.1) | Data may be projected |
| Prolog STA s44 (partial convergence) | Yes (§8.1) | Data may be projected |
| O(1) vs O(N) STA ablation | Yes (§7.1) | Adequate |
| Multi-logic GRPO (mixed training) | Yes (§8.2) | Data integrity uncertain |
| Cross-logic transfer evaluation | Yes (§8.3) | Data integrity uncertain |
| SMT-LIB single-logic GRPO | Yes (§8.4) | Data integrity uncertain |
| Qwen3-8B scaling | Yes (§7.3) | Single-seed, preliminary |
| Curriculum ablation | Yes (§7.2) | Data integrity uncertain |

**Coverage note**: All 8 planned experiments appear in the paper, but reviewers flag that several may not correspond to completed experiments based on cross-referencing with project audit documents. The paper achieves formal coverage but possibly at the cost of data integrity.

---

*Report generated by Dream Review Director — 2 reviewers, full roundtable protocol (Steps 1-4).*