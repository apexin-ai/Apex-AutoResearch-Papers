---
dream_id: dream_20260516T054054
tier: worst
overall_score: weak reject
timestamp: 2026-05-16T06:31:13.641241+00:00
---

# Dream Review Report: "Why Symbolic Consensus Fails"

**Dream ID:** 20260516T054054
**Review Mode:** Full (2 Reviewers + Roundtable)
**Venue Standard:** Top ML venue, ~25% acceptance rate, 6-point scale

---

## Reviewer Assignments
- **R1:** Methodology + Experiments
- **R2:** Novelty + Related Work

---

## Step 1: Independent Reviews

### Reviewer 1 (R1): Methods + Experiments

**Score: 3/6 (Weak Reject) | Confidence: 4/5**

**Summary:** The paper proposes SICA, a symbolic consensus method using FOL constraint extraction and MAX-SAT, and studies why it fails to beat Self-Consistency. The expanded 804-question evaluation is a meaningful scale-up from the 60-question pilot, and the negative result is honestly reported. However, the methodology reveals that SICA's entire mechanism reduces to tiebreaking at exact vote parity, the statistical evidence is insufficient, and the evaluation is confined to a single model family.

**Strengths:**
- Thorough ablation coverage: all 9 planned experiments (expanded benchmark, K sensitivity, tiebreak comparison, 4 model scales, C0 correlation, constraint quality analysis, overhead) are executed and reported
- Honest reporting of negative results with appropriate statistical testing (bootstrap p-values, 10k resamples)
- The K ablation (Table 3) is well-designed and reveals the tie-driven mechanism clearly — gap tracks tie fraction, not C0 or constraint quality
- Overhead breakdown (Table 7) is useful practical information; the conditional deployment strategy (invoke SICA only when C0 > threshold) is a sensible recommendation
- The qualitative constraint analysis (Sec 4.7) identifying answer-local vs. cross-answer constraints provides genuine mechanistic insight

**Weaknesses:**
- **Mechanism is narrower than framed.** All SICA-vs-SC differences come exclusively from exact vote ties. On non-tied questions, SICA ≡ SC identically (exclusion rate <3% and never flips a non-tie majority). The paper frames this as "constraint-based aggregation" but the contribution reduces to "a better-than-random tiebreaker." This gap between framing and mechanism is a significant presentation issue.
- **C0-gap correlation is methodologically weak.** Table 6 has 12 datapoints, but 5 are from the same model (14B) at different K values on the same 60 questions — these are not independent observations. The Pearson r=0.45 and AUC=0.72 are computed on this pseudo-replicated dataset without acknowledging the dependency. With truly independent conditions, N drops to ~5-6.
- **Single model family.** All results use Qwen2.5 variants. The operating regime claim ("reasoning models eliminate diversity," "72B approaches reasoning regime") cannot be validated within one architecture family. At minimum, one non-Qwen family (Llama, Mistral) would be needed to distinguish architecture-specific from general phenomena.
- **Tiebreak analysis is underpowered.** The core positive claim (60% tiebreak win rate > 50% random) rests on 12/20 correct — binomial p=0.25, far from significant. The paper acknowledges this but still uses it as evidence that "constraints carry real discriminative signal." With N=20, this is an anecdote, not evidence.
- **No constraint ablation.** The paper never tests whether MAX-SAT adds value over simpler constraint-based heuristics (e.g., counting constraint support, weighted voting by constraint count). Without this, we cannot attribute any signal to the MAX-SAT formulation specifically.
- **ProofWriter consistently shows 0pp or negative gap** across all conditions, but the paper doesn't adequately explain why SICA harms performance on closed-world logic. "Constraint extraction introducing minor noise" deserves deeper analysis — is this a fundamental limitation of FOL extraction from natural language traces?
- **No non-logic benchmarks.** FOLIO and ProofWriter are both formal logic tasks where FOL extraction is naturally aligned. Testing on commonsense reasoning, math, or code generation would reveal whether the operating regime analysis generalizes.

**Questions for Authors:**
1. What happens with odd K values (K=7, 9, 11) where ties are mathematically impossible? If gap=0 for all odd K, this would definitively confirm the tie-only mechanism.
2. Can you report the constraint extraction prompt? Reproducibility requires knowing how FOL constraints are elicited.
3. Have you tried non-Qwen models? Even a spot-check on Llama-3-8B would strengthen the generalization claim.
4. The pilot 60 questions had C0=53% while the full 804 had C0=28%. You attribute this to "selection bias" — how exactly were the pilot questions selected?

**Missing Experiments:**
- Constraint ablation: MAX-SAT vs. simple constraint counting vs. weighted voting
- At least one non-Qwen model family
- At least one non-logic benchmark
- Odd K values to confirm tie-only mechanism

---

### Reviewer 2 (R2): Novelty + Related Work

**Score: 3/6 (Weak Reject) | Confidence: 4/5**

**Summary:** The paper reframes a negative result (SICA doesn't beat SC) as a diagnostic framework contribution. While the honest reporting of negative results is commendable, the claimed contributions — particularly C0 as a "diagnostic metric" — are thin. The related work coverage is severely deficient (7 references, no dedicated section), and the novelty does not meet the bar for a top venue.

**Strengths:**
- Intellectually honest framing: the paper doesn't hide the negative result but leads with it, which is refreshing
- The "capability trap" insight (symbolic consensus helps most where models are weakest, but there constraint quality is also lowest) is a genuinely interesting observation that applies beyond SICA
- The operating regime concept (requiring simultaneous satisfaction of diversity, tie frequency, and constraint quality) is a useful thinking tool for evaluating any post-hoc consensus method
- Clean writing with well-structured tables; the progression from Table 1 (regime) through Table 5 (scaling) tells a coherent story
- The conditional deployment recommendation (compute C0 first, invoke SICA only if warranted) is practical and actionable

**Weaknesses:**
- **C0 is a trivially derived statistic.** Multi-candidate rate is simply "fraction of questions with non-unanimous votes" — any practitioner running SC already has this information. Naming it "C0" and calling it a "diagnostic framework" does not constitute a contribution. The upper bound derivation (max gain ≤ C0 × (1 − SC_acc_on_diverse)) is elementary counting.
- **Only 7 references — severely deficient.** A paper claiming to characterize when symbolic consensus fails must engage with the broader literature. Critical gaps include:
  - *Neuro-symbolic reasoning:* Logic-LM (Pan et al., 2023), SatLM (Ye et al., 2023), FoVer, LINC — these use symbolic solvers with LLMs and face related limitations
  - *SC variants with weighting:* Taubenfeld et al. (2024) on weighted SC, RASC — directly relevant alternatives
  - *Test-time compute scaling:* Snell et al. (2024) — theoretical framework for when additional test-time compute helps, which subsumes the C0 analysis
  - *LLM ensemble methods:* Mixture-of-Agents, LLM-Blender — broader consensus landscape
  - *Reasoning models:* DeepSeek-R1 — understanding why reasoning models are self-consistent
  - *Negative results in ML:* precedent papers that frame negative findings constructively
  At least 15-20 additional references across these categories are needed. The absence of a Related Work section is a formatting red flag for any venue.
- **"Diagnostic framework" oversells a single metric.** The paper calls its contribution a "framework" but delivers: (1) one metric (C0) that explains 20% of variance, (2) a qualitative observation about reasoning vs. instruction models, and (3) a list of falsification conditions. A framework implies a systematic methodology that others can apply; what's offered is closer to a set of observations.
- **Inconsistent narrative.** The title says "Why Symbolic Consensus Fails" but the paper repeatedly claims the method is "directionally correct" and "correct where it applies." This hedging undermines the clean negative-result framing. Either commit to "it fails because the regime is too narrow" or "it works in a narrow regime" — the paper tries to have it both ways.
- **No actionable alternative.** The paper diagnoses failure but offers no path forward. Sec 4.7 identifies that constraints are "answer-local" rather than "cross-answer" — this is the most interesting finding but is buried and undeveloped. A paper titled "Why X Fails" should ideally point toward "What Would Succeed."
- **Pilot-to-expanded discrepancy unexplained.** C0 drops from 53% (60 questions) to 28% (804 questions). The paper says "selection bias" but never explains the selection process. Were the pilot questions cherry-picked? Randomly sampled? This matters for interpreting whether the pilot results were ever meaningful.
- **SICA's provenance is unclear.** The paper treats SICA as a known method but provides no citation. If SICA is the authors' own prior work, this should be stated. If it's a hypothetical method constructed for this study, the "hypothesis testing" framing is undermined — you can't falsify a hypothesis about a method you designed to test it.

**Questions for Authors:**
1. Is SICA previously published? If so, cite it. If not, clarify the relationship between proposing and critiquing the same method.
2. Why no Related Work section? This seems like an oversight, not a deliberate choice.
3. Have you considered that test-time compute scaling frameworks (Snell et al., 2024) already subsume the C0 analysis? C0 is essentially a special case of "when does additional test-time computation help?"
4. The "capability trap" is your most interesting insight — can you formalize it? Currently it's a one-paragraph observation.

**Missing Related Work (prioritized):**
1. Logic-LM, SatLM, LINC — neuro-symbolic reasoning with LLMs (direct methodological relatives)
2. Taubenfeld et al. (2024) — weighted self-consistency (direct baseline gap)
3. Snell et al. (2024) — test-time compute scaling (theoretical subsumption of C0)
4. DeepSeek-R1 / OpenAI o1 — reasoning model self-consistency (relevant to Sec 4.1)
5. LLM-Blender, Mixture-of-Agents — broader ensemble landscape
6. Any negative-result paper in NeurIPS/ICLR proceedings as formatting/framing precedent

---

## Step 2: Cross-Sharing Summary

R1's methodological findings shared with R2:
- The SICA gain mechanism is exclusively tiebreaking at exact vote parity — R2 agreed this further weakens the "framework" framing
- C0 correlation uses non-independent datapoints — R2 noted this compounds the "trivial metric" concern
- Missing constraint ablation — R2 agreed this is critical for establishing MAX-SAT's contribution

R2's positioning findings shared with R1:
- C0 is trivially derivable — R1 agreed the metric itself is elementary, though its application is somewhat useful
- 7 references is severely deficient — R1 agreed, noting that neuro-symbolic methods face similar limitations
- SICA's provenance is unclear — R1 agreed this creates interpretive ambiguity
- Inconsistent narrative — R1 agreed the hedging weakens the paper

No contradictions between reviewers. Complementary concerns reinforce each other.

---

## Step 3: Convergence

**Points of agreement (both reviewers):**
1. Score: 3/6 (Weak Reject) — below the acceptance threshold
2. The negative result is honestly reported and the scale-up from 60→804 questions is valuable
3. C0 as a contribution is insufficient — trivially derived, weakly predictive (r=0.45, AUC=0.72)
4. Single model family (Qwen only) is a critical limitation for generalization claims
5. Related work is severely deficient (7 references, no dedicated section)
6. The mechanism reduces to tiebreaking, which is narrower than the framing suggests
7. Statistical evidence for the positive claim (tiebreak win rate) is underpowered (N=20, p=0.25)

**Complementary insights (no disagreement):**
- R1 identifies missing experiments (constraint ablation, odd K, non-logic benchmarks)
- R2 identifies missing literature and framing issues (narrative inconsistency, SICA provenance, no actionable alternative)

**No score adjustment needed** — both reviewers independently arrived at 3/6 with aligned reasoning.

---

## Step 4: Consolidated Assessment

### Overall Score: 3/6 (Weak Reject)
### Confidence: 4/5

### Meta-Review

This paper studies why a symbolic consensus method (SICA) fails to improve over Self-Consistency, reframing the negative result as a diagnostic contribution. The intellectual honesty and experimental thoroughness (9 experiments covering scaling, ablation, and qualitative analysis) are commendable. However, the paper does not meet the acceptance bar for a top ML venue for the following reasons:

**Primary reasons for rejection:**

1. **Insufficient novelty in claimed contributions.** C0 (multi-candidate rate) is a trivially derived statistic that any SC practitioner implicitly has access to. It explains only 20% of variance in SICA-SC gap, making it a weak diagnostic at best. Calling this a "diagnostic framework" oversells what is essentially one elementary metric plus qualitative observations.

2. **Mechanism is narrower than framed.** The paper frames SICA as "constraint-based aggregation" but all gains come exclusively from exact vote ties (2.5% of questions). On non-tied questions, SICA ≡ SC identically. The contribution is a marginally-better-than-random tiebreaker, not a "consensus framework." This framing gap undermines the paper's core narrative.

3. **Severely deficient related work.** Seven references with no Related Work section is unacceptable at any venue. The paper ignores the neuro-symbolic reasoning literature (Logic-LM, SatLM, LINC), SC variants (weighted SC), test-time compute scaling frameworks, and the broader LLM ensemble landscape. Some of these works (especially Snell et al. on test-time compute scaling) potentially subsume the C0 analysis entirely.

4. **Single model family limits generalization.** All results use Qwen2.5 variants. The key claims (reasoning models eliminate diversity, capability-diversity inverse relationship) could be Qwen-specific artifacts. At least one additional model family is needed.

5. **Statistical evidence for positive claims is insufficient.** The core positive claim (60% tiebreak win rate) rests on 12/20 correct answers (binomial p=0.25). This is presented as evidence that "constraints carry real discriminative signal" but is not statistically distinguishable from chance.

**Secondary concerns:**
- No constraint ablation (MAX-SAT vs. simpler alternatives)
- No non-logic benchmarks to test generalization of operating regime analysis
- SICA's provenance is unclear (own prior work? constructed for this study?)
- Pilot-to-expanded C0 drop (53%→28%) attributed to "selection bias" without explaining selection process
- Inconsistent narrative: title says "fails" but body claims "correct where it applies"

**What would strengthen the paper:**
- Add a proper Related Work section with 15-20+ references engaging neuro-symbolic reasoning, SC variants, and test-time compute scaling
- Include at least one non-Qwen model family (Llama-3, Mistral) to validate generalization
- Run constraint ablation: does MAX-SAT outperform simple constraint counting?
- Test on at least one non-logic benchmark
- Resolve the narrative: either commit to "negative result paper" or "narrow-regime paper," not both
- Formalize the "capability trap" — this is the most interesting idea but is undeveloped
- Develop the Sec 4.7 finding (answer-local vs. cross-answer constraints) into a concrete proposal for improvement

### Experiment Coverage Assessment
All 9 planned experiments are present in the paper (exp-001 through exp-009). Coverage is complete. The issue is not missing experiments from the plan, but missing experiments beyond the plan (different model families, different benchmarks, ablations).

### Recommendation
**Weak Reject.** The paper is a competent empirical study of a negative result, but the contributions (trivial metric, single model family, underpowered positive evidence) do not meet the novelty and rigor bar for a top ML venue. With a proper Related Work section, one additional model family, and a constraint ablation, this could potentially reach the level of a Findings paper or workshop contribution. The "capability trap" insight and the answer-local constraint analysis (Sec 4.7) are genuinely interesting seeds that deserve fuller development.