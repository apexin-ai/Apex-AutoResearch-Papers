---
dream_id: dream_20260516T054054
tier: median
overall_score: weak reject
timestamp: 2026-05-16T06:24:18.038948+00:00
---

# Dream Review Report — SICA Operating Regime Paper

**Paper:** "When Does Symbolic Consensus Help? Characterizing the Operating Regime of Constraint-Based LLM Aggregation"
**Review mode:** full | **Reviewers:** R1 (Methods+Experiments), R2 (Novelty+Related Work)
**Date:** 2026-05-16

---

## 1. Paper Summary

The paper proposes Symbolic Invariant Consensus Aggregation (SICA), which extracts first-order logic (FOL) constraints from LLM reasoning traces and resolves answer selection via weighted partial MAX-SAT, as an alternative to Self-Consistency (SC) majority voting. Rather than claiming universal improvement, the paper characterizes SICA's "operating regime" through the multi-candidate rate C0, showing gains concentrate on FOLIO (+4.4pp, p=0.034) but vanish on ProofWriter-D5 (+0.2pp) and reasoning models (QwQ-32B, C0≈0). The paper covers four model scales (7B–72B instruction + 32B reasoning), K-ablation (K=6–20), tiebreak analysis, overhead decomposition, and constraint quality case studies.

---

## 2. Strengths

### S1. Honest "when does it help?" framing (R1, R2 — strong agreement)
The paper explicitly characterizes failure modes (QwQ-32B degeneration, ProofWriter low constraint quality) rather than cherry-picking favorable results. The inclusion of QwQ-32B's zero gain as a first-class finding is commendable and rare in method papers. This reframing from "universal booster" to "method with characterizable boundaries" is mature scientific practice.

### S2. Thorough experimental coverage (R1)
All 9 experiments from the design plan are reflected in the paper: main results (exp-001), K ablation (exp-002), tiebreak baselines (exp-003), 7B/72B scaling (exp-004, exp-007), QwQ-32B (exp-005), C0 diagnostic (exp-006), constraint quality case studies (exp-008), and overhead analysis (exp-009). The paper delivers on its experimental plan comprehensively.

### S3. MAX-SAT formulation for multi-trace aggregation is a novel combination (R2)
While individual components (LLM-to-FOL, SAT solvers, multi-path sampling) exist separately, using weighted partial MAX-SAT as a consensus mechanism across K reasoning traces — where constraint weights derive from cross-trace frequency — has not appeared in prior work. This is not a trivial combination.

### S4. Tiebreak baseline comparison is well-constructed (R1, R2)
Table 2 comparing SICA (64.3%) against random (50%), alphabetical (52.4%), and first-seen (42.9%) directly addresses the "just randomize" objection. The 14pp advantage over random on 42 tied questions is a real signal.

### S5. Practical overhead analysis (R1, R2)
The 12.7% marginal overhead decomposition (Table 6) is transparent and actionable. The proposed deployment workflow (compute C0 for free, invest SICA overhead only if C0 > 0.25) is sensible.

### S6. Transparent reporting of ProofWriter failure mode (R1)
The constraint precision analysis (78% on FOLIO vs. 41% on ProofWriter) provides a mechanistic explanation for the performance gap, rather than hiding the negative result.

---

## 3. Weaknesses

### Major

#### W1. SICA is functionally a tiebreaker, not a consensus override mechanism (R1, R2 — strong agreement)
**Both reviewers independently identified this as the central concern.** SICA never overrides a non-tied majority vote. The entire gain comes from tied questions (~10% of data: 18/204 on FOLIO, 24/600 on ProofWriter, 42 total). The title "Symbolic Invariant Consensus Aggregation" and framing as "consensus" implies the method can override incorrect majorities by leveraging constraint structure — but it cannot. SICA = SC on every non-tied question. The gap between the claimed scope (general aggregation) and demonstrated scope (tiebreaking on ~5–10% of questions) is significant.

**Recommended reframe:** "Principled Tiebreaking via Symbolic Constraints" would be more accurate than "Consensus Aggregation."

#### W2. Critical missing related work and baselines (R2, endorsed by R1 in cross-sharing)
The Related Work section is only three short paragraphs and omits several directly relevant lines:

- **Verifier-based reranking (Cobbe et al., 2021; Lightman et al., 2023):** Outcome Reward Models (ORM) and Process Reward Models (PRM) are the most natural competitor for "going beyond majority voting." They score individual paths and select the best — the same goal as SICA's constraint weighting. Complete absence from both related work and experiments is a critical gap.
- **LINC (Olausson et al., 2023):** Translates NL reasoning to FOL and uses Prover9 for verification on FOLIO specifically — a direct competitor on the same benchmark. Not cited.
- **Logic-LM (Pan et al., 2023):** Cited but differentiation is vague. Running Logic-LM K times + majority vote would be the natural ablation to isolate whether MAX-SAT aggregation adds value beyond the extraction itself.
- **Debate-style aggregation (Du et al., 2023; Liang et al., 2023):** Multi-agent debate as an alternative for resolving trace disagreements.
- **LEVER (Ni et al., 2023):** Execution-based verification for reranking — same principle of using a formal system to rerank multiple LLM outputs.
- **Benchmark SOTA:** No reporting of where SICA sits relative to current FOLIO/ProofWriter SOTA. The reader cannot contextualize the absolute numbers.

#### W3. C0 contribution is partly tautological and the regression is underpowered (R1, R2 — strong agreement)
By construction, SICA can only differ from SC when C0 > 0 (when all traces agree, MAX-SAT over a single candidate is vacuous). The "prediction" that high C0 correlates with high SICA-SC gap is therefore a mathematical near-tautology, not an empirical discovery. Answer diversity is a well-known concept in the SC literature.

The regression has serious methodological issues:
- 14 data points, but 5 are from the same model at different K values (not independent)
- Effectively ~9 independent observations (4 models × 2 datasets + K-ablation cluster)
- R² = 0.52 (paper's own number) is moderate, not strong
- Spearman ρ = 0.78 sounds impressive but no bootstrap CI on the correlation coefficient is provided
- The C0 = 0.25 threshold is empirically determined from the same 14 points — no holdout validation

#### W4. Evaluation confined to FOL-friendly benchmarks (R2, endorsed by R1)
FOLIO and ProofWriter are both logic reasoning benchmarks where problems are inherently expressible in FOL. This is a best-case scenario for SICA's constraint extraction. No evidence is provided that the method works on mathematical reasoning (GSM8K, MATH), commonsense reasoning, or coding tasks. The paper acknowledges this in Limitations but understates the severity: if SICA only works on FOL-domain benchmarks, it competes with purpose-built systems (Logic-LM, LINC) that are likely stronger.

#### W5. Single model family (R1, R2 — strong agreement)
All instruction-model experiments use Qwen2.5 variants (7B, 14B, 72B-AWQ). The scaling trend claim (C0 and gap decrease with model scale) and operating regime characterization are validated on one model family only. At minimum, one additional family (LLaMA, Mistral) is needed to support a general claim about instruction-model behavior.

### Moderate

#### W6. Formalization gap (R1)
The weight function in Equation 1 (cross-trace frequency weighting) and the MAX-SAT framing could be more precise. The paper calls this "weighted partial MAX-SAT" but the actual mechanism is closer to weighted constraint scoring — standard MAX-SAT optimization guarantees may not apply since Z3 is used as an SMT solver, and the per-candidate instance construction differs from classical MAX-SAT.

#### W7. No figures in the paper (R2)
For a paper whose strongest empirical argument is the C0-gap correlation, the absence of a C0 scatter plot is a significant missed opportunity. The operating regime concept and the K-ablation trends also beg for visual illustration.

#### W8. K ablation uses only even values {6, 8, 12, 16, 20} (R2)
Odd K values would dramatically reduce exact ties. Since SICA's gains come entirely from ties, this omission is suspicious. The paper should show performance with odd K to establish that value persists when ties are rarer.

#### W9. ProofWriter dominates data but contributes nothing (R1)
600 of 804 questions (75%) come from ProofWriter-D5 where the gain is +0.2pp. The combined p=0.082 is driven down by this large zero-gain component. The macro-average (+2.3pp) vs micro-average (likely ~1.2pp) distinction is acknowledged but the presentation could mislead readers focused on the headline 804-question combined result.

### Minor

- M1. No error bars or confidence intervals in Tables 4–5 despite small sample sizes (60 questions each)
- M2. The abstract mentions "Spearman ρ=0.78" across 14 configurations but the non-independence of K-ablation points is not flagged
- M3. "First-order logic constraints" may be misleading — these are LLM-generated pseudo-FOL without formal correctness guarantees
- M4. No human evaluation of constraint semantic quality; "2% extraction failure" measures JSON validity, not semantic correctness
- M5. The 60-question subsets for model scaling yield 1.67pp per question granularity, making gap values highly discrete

---

## 4. Questions for Authors

1. **Does SICA ever override a non-tied majority vote and improve accuracy?** If not, should the method be reframed as principled tiebreaking?

2. **What happens with odd K (K=11, K=13)?** How many ties remain and does SICA's advantage survive?

3. **How does SICA compare to Logic-LM × K + majority vote?** This isolates whether MAX-SAT aggregation adds value beyond FOL extraction itself.

4. **How does SICA compare to ORM/PRM-based reranking?** These are the most natural "beyond majority voting" baselines in current practice.

5. **What are bootstrap confidence intervals on the Spearman ρ = 0.78 from Table 7?** With 14 points (5 non-independent), what is the CI?

6. **Where does SICA's accuracy sit relative to FOLIO/ProofWriter SOTA?** Are the absolute numbers competitive?

7. **Can you provide even a pilot result on one non-logic benchmark** (GSM8K, CommonsenseQA) to bound generalizability?

8. **What is the human-evaluated semantic accuracy of extracted FOL constraints?** "2% extraction failure" measures JSON validity; what fraction of constraints are semantically correct?

---

## 5. Experiment Coverage Assessment

| Planned Experiment | Status | Notes |
|----|--------|-------|
| exp-001: Main results (14B, 804q) | ✅ Covered | Table 1 |
| exp-002: K ablation (60q) | ✅ Covered | Table 3 |
| exp-003: Tiebreak baselines | ✅ Covered | Table 2 |
| exp-004: 7B scaling | ✅ Covered | Table 4 |
| exp-005: QwQ-32B | ✅ Covered | Tables 4-5 |
| exp-006: C0 diagnostic | ✅ Covered | Table 7 (scatter plot figure missing) |
| exp-007: 72B-AWQ | ✅ Covered | Table 4 |
| exp-008: Constraint quality cases | ✅ Covered | Section 5.2 |
| exp-009: Overhead analysis | ✅ Covered | Table 6 |

All 9 planned experiments are reflected in the paper. The C0 scatter plot (exp-006 key figure) is notably absent from what appears to be a text-only submission.

---

## 6. Roundtable Convergence

### Areas of Strong Agreement (R1 + R2)
- The honest "when does it help?" framing is the paper's greatest strength
- SICA is functionally a tiebreaker, not a general consensus mechanism — the scope-to-claim gap is the central weakness
- C0 regression is underpowered with non-independent data points
- Single model family limits generalizability claims
- FOL-restricted evaluation is a serious scope constraint

### Areas of Disagreement and Resolution
- **R1 (score 4) vs R2 (score 3):** R1 weighted experimental thoroughness more heavily; R2 weighted novelty positioning and missing baselines more heavily. After cross-sharing, R1 acknowledged the force of the missing verifier-based baselines argument (ORM/PRM) and the C0 tautology concern. R2 acknowledged the credit for comprehensive experiment coverage. Both converged toward **3 (Weak Reject)**: the direction is promising and the scientific honesty is commendable, but the gap between claimed scope and demonstrated scope, combined with missing key baselines and single-family evaluation, puts it below the acceptance bar for a top venue.

---

## 7. Overall Assessment

**Consolidated Score: 3 / 6 (Weak Reject)**
**Confidence: 4 / 5 (High)**

### Justification
The paper presents a technically sound mechanism (MAX-SAT-based tiebreaking) that produces a real signal (64.3% tiebreak win rate vs 50% random) and demonstrates commendable scientific honesty in characterizing when and why it fails. The experimental coverage is comprehensive relative to the plan. However, several issues collectively push it below the acceptance threshold:

1. **Scope-to-claim gap**: The method is a tiebreaker active on ~10% of questions, not a general consensus mechanism. The title and framing significantly overstate the contribution.
2. **Missing critical baselines**: No comparison to verifier-based reranking (ORM/PRM), Logic-LM×K, or LINC — the most natural alternatives for "going beyond majority voting."
3. **Evaluation scope**: Two FOL-friendly benchmarks with one model family. The operating regime claim requires broader validation.
4. **C0 diagnostic**: Partly tautological, regression underpowered, no holdout validation.
5. **Statistical marginality**: Combined p=0.082 does not reach significance; individual model comparisons on 60 questions lack power.

### Recommendation for Revision
The paper could reach acceptance at a top venue with:
1. Reframe as principled tiebreaking (not general consensus) — or demonstrate majority-override cases
2. Add ORM/PRM baseline comparison and Logic-LM×K ablation
3. Add one non-Qwen model family (LLaMA or Mistral)
4. Add one non-logic benchmark pilot (GSM8K)
5. Odd-K ablation to validate tiebreaking is not an even-K artifact
6. Include the C0 scatter plot figure
7. Expand Related Work to address verifier-based reranking, LINC, debate methods

The core idea has merit and the scientific approach is sound. The paper would benefit from tighter scoping of claims to match demonstrated evidence.