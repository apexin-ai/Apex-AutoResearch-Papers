---
dream_id: dream_20260517T165032
tier: median
overall_score: borderline reject
timestamp: 2026-05-17T17:34:45.863332+00:00
---

# Dream Review Report — "The Capability Trap: Why Self-Extracted Constraints Cannot Improve LLM Majority Voting"

**Review mode**: full | **Reviewers**: R1 (Methods + Experiments), R2 (Novelty + Related Work) | **Scale**: 1–6 (1=Strong Reject, 6=Strong Accept)

---

## 1. Paper Summary

The paper investigates SICA (Symbolic Invariant Consensus Aggregation), a pipeline that extracts First-Order Logic constraints from K sampled LLM reasoning traces and applies weighted MAX-SAT to select answers. Across 5 model families, 3+ reasoning domains, and N>1,300 evaluated problems, SICA provides no statistically significant accuracy gain over Self-Consistency (SC). The authors attribute this to a "capability trap": instruction-scale models produce output diversity but extract non-discriminative constraints (precision ~0.527, near chance), while full reasoning models (QwQ-32B) produce near-deterministic outputs (C0<5%), making SICA structurally identical to SC. An oracle experiment replacing self-extracted constraints with gold FOL annotations yields +8.82pp (p<0.001), localizing the bottleneck to extraction quality. A constraint ablation confirms MAX-SAT degenerates to counting (802/804 agreement with count-only).

---

## 2. Independent Reviews

### R1: Methods and Experiments — Score: 3/6 (Weak Reject) | Confidence: 4/5

**Strengths**:
- **S1 (Oracle control)**: Replacing self-extracted constraints with gold FOLIO FOL yields +8.82pp (p=6.15e-5, n=204), providing a clean causal separation of aggregation mechanism from extraction quality. This elevates the paper beyond a simple null result.
- **S2 (Three-way constraint ablation)**: MAX-SAT, count-only, and random-weight agree on 802/804 predictions (99.8% agreement). Directly confirms theoretical degeneration: when constraints lack discriminative power, MAX-SAT reduces to weighted counting.
- **S3 (Powered replications)**: Authors ran n=60 pilots, then followed up with n>=200 powered tests for key conditions (e.g., LLaMA-8B pilot +6.67pp → powered replication -2.45pp). Exemplary practice for negative-result papers.
- **S4 (Broad coverage)**: 5 model families, 4 domains, K ablation (6 values), weighted SC baselines, and Logic-LM comparison. All 15+ planned experiments from the design document are accounted for.

**Weaknesses**:
- **W1 [CRITICAL] (sigma source-answer indicator)**: The scoring function sigma(c,a) = 1 iff constraint c was extracted from a trace with answer a. This means MAX-SAT scoring maps constraints back to source answers rather than evaluating constraints against all candidates via Z3. The "capability trap" may be partially a design artifact: constraints are never given the chance to be discriminative under proper cross-answer evaluation. The oracle experiment partially addresses this (gold FOL is evaluated cross-answer), but the self-extraction pipeline never gets this test.
- **W2 (Underpowered conditions)**: Only 4 of ~10 conditions have n>=200. Most cross-model evidence uses n=60 (McNemar power <0.30 for 5pp effect). "N>1,300" is technically correct but 804/1300 come from a single model on two datasets.
- **W3 (No cross-model extraction)**: Only same-model self-extraction tested. One condition with a stronger extractor model would distinguish "self-extracted constraints are inherently non-discriminative" from "same-model extraction shares failure modes with generation."
- **W4 (Missing prompt ablation)**: The extraction prompt is a critical design choice with no ablation. Extraction failure rates vary 0.70–1.00 across models, suggesting sensitivity to prompting.
- **W5 (Z3 parser confound)**: Per-constraint Z3 parsing success rate is not reported. Early experiments had 41–100% parse failure rates. If many constraints are lost at Z3 parsing, MAX-SAT operates on a degraded set.
- **W6 (ProofWriter depth)**: All n=600 ProofWriter problems are Depth-5 (hardest). Not representative of full distribution; should be disclosed.

**Key Questions**:
- Q1: Has cross-answer Z3 evaluation of self-extracted constraints been tested? This is the highest-impact missing experiment.
- Q2: What is the per-constraint (not per-trace) Z3 parsing success rate?
- Q3: The 2 problems where SICA disagrees with count-only (802/804): does SICA win or lose?
- Q4: Has quantization's effect on Qwen-72B-AWQ extraction quality been verified?

---

### R2: Novelty and Related Work — Score: 4/6 (Borderline Reject) | Confidence: 4/5

**Strengths**:
- **S1 (Oracle as causal intervention)**: The oracle experiment provides genuine mechanistic insight by separating extraction quality from aggregation effectiveness on identical data.
- **S2 (Ablation diagnostic)**: The three-way ablation is a clean, reusable diagnostic that other researchers can apply to their symbolic aggregation systems.
- **S3 (Honest scoping)**: The paper appropriately limits claims to same-model self-extraction and explicitly acknowledges that methods using trained verifiers or external tools achieve gains through different mechanisms.

**Weaknesses**:
- **W1 (Limited novelty of "capability trap")**: Logic-LM (Pan et al. 2023) and LINC (Olausson et al. 2023) already documented ~40% LLM FOL translation error rates. Huang et al. (ICLR 2024, "LLMs Cannot Self-Correct Reasoning Yet") established the broader pattern that self-X fails without external feedback. The contribution is more systematic quantification than conceptual discovery, but the paper frames it as the latter.
- **W2 (SICA is not an established method)**: The paper proposes SICA then shows it doesn't work. Since no one widely uses or advocates this specific pipeline, the negative result has limited impact. The paper needs stronger motivation for why practitioners would attempt self-extraction (over trained verification) to make the negative result valuable.
- **W3 (C0 contribution overstated)**: C0 (multi-candidate rate) is a trivially computable statistic. Claiming it as a deployment diagnostic inflates a basic sanity check.
- **W4 (Shallow failure mode analysis)**: The qualitative analysis (35% tautological, 28% overly general, 25% non-discriminative, 12% genuinely discriminative) is the most important finding for understanding the capability trap, yet receives cursory treatment. What problem structures produce discriminative constraints?
- **W5 (Thin related work)**: Discussion of each cluster is brief. The debate/multi-agent literature (Liang et al. 2023, Du et al. 2023) is underdiscussed despite being a direct alternative for aggregating reasoning paths.

**Missing Related Work**:
- Huang et al. (ICLR 2024), "Large Language Models Cannot Self-Correct Reasoning Yet" — establishes the same structural pattern
- GSM-Symbolic (Mirzadeh et al. 2024) — precedent for rigorous negative-result methodology
- V-STaR (Hosseini et al. 2024) — shows verification quality scales with training, contrasting self-extraction limits
- RASC / ReASC — reasoning-aware SC variants as non-symbolic alternatives
- Several bibliography entries incomplete (DyLoS, Aristotle, FoVer lack full citations)

**Framing Suggestions**:
- Elevate the oracle experiment to the lead contribution: "Symbolic aggregation CAN improve voting (+8.82pp with gold constraints) but CANNOT when constraints are self-extracted." More compelling than leading with the negative result.
- Rename "capability trap" to something more descriptive (e.g., "extraction-discrimination bottleneck"). The current name implies deeper conceptual novelty than the evidence supports.
- Foreground cost-benefit analysis earlier: "This method doubles compute for zero benefit" is a strong practical message currently buried in Section 4.7.

---

## 3. Roundtable Convergence

### Points of Agreement
1. **Oracle experiment is the paper's strongest and most novel contribution** (both R1-S1 and R2-S1). Both reviewers recommend elevating it to the lead contribution.
2. **Constraint ablation provides clean mechanistic evidence** (R1-S2, R2-S2). The 802/804 agreement is compelling.
3. **C0 is overstated as a contribution** (R1: "somewhat obvious"; R2-W3: "trivially computable"). Should be positioned as a secondary observation, not a headline contribution.
4. **Deeper analysis of WHY constraints fail is needed** (R1: per-constraint Z3 rates; R2-W4: problem-level structural analysis).
5. **The paper is well-suited for EMNLP Findings but falls short for main conference** at a top venue with ~25% acceptance.

### Points of Divergence and Resolution
- **R1's sigma(c,a) concern (W1)**: R1 flags that the source-answer indicator means self-extracted constraints are never evaluated cross-answer, potentially making the capability trap a design artifact. R2 did not independently flag this. **Resolution**: This is a legitimate methodological concern, but partially mitigated by two observations: (a) the oracle experiment uses proper cross-answer Z3 evaluation, confirming the aggregation mechanism works; (b) constraint precision ~0.50 means even under cross-answer evaluation, constraints would likely provide no discrimination. The concern is downgraded from "fatal flaw" to "important missing control experiment." The paper should either implement cross-answer evaluation of self-extracted constraints or explicitly discuss why it would not change results given ~0.50 precision.
- **Score difference (R1=3, R2=4)**: R1 weighs the sigma issue and underpowered conditions more heavily. R2 gives more credit for the oracle and systematic scope. **Resolution**: The sigma concern is real but not fatal given the mitigating evidence. The novelty concerns are valid. Converged score: **3.5, rounded to 4 (Borderline Reject)**.

---

## 4. Consolidated Assessment

### Overall Score: 4/6 (Borderline Reject)

### Summary Judgment
The paper presents a substantial and largely well-executed empirical study investigating whether self-extracted symbolic constraints can improve LLM majority voting. The two standout contributions — the oracle control experiment (+8.82pp with gold FOL, localizing the bottleneck) and the three-way constraint ablation (MAX-SAT = counting on 99.8% of problems) — provide genuine mechanistic insight that goes beyond a simple null result. The experimental coverage (5 model families, 3+ domains, multiple ablations) is commendable, and the powered replications that correct initial small-sample signals demonstrate methodological care.

However, several issues prevent acceptance at a top ML venue:

### Critical Issues
1. **Methodological gap (sigma source-answer indicator)**: The self-extraction pipeline evaluates constraints only against the answer from the source trace, not cross-answer via Z3. This means the "capability trap" may partly reflect a design choice rather than a fundamental limitation. The oracle experiment uses cross-answer evaluation, creating an asymmetry. A cross-answer evaluation ablation on self-extracted constraints would resolve this.

2. **Limited novelty**: The core finding — that LLM self-extracted FOL constraints are low quality — is already documented in Logic-LM and LINC. The "capability trap" is better described as systematic quantification of a known phenomenon than as a new conceptual insight. The framing overpromises relative to what the evidence delivers.

3. **Underpowered cross-model evidence**: Most non-primary conditions use n=60, where McNemar's test has <30% power to detect a 5pp effect. The "5 model families" coverage is thinner than it appears.

### Major Issues
4. **No cross-model extraction baseline**: Testing whether a stronger model can extract discriminative constraints from weaker model traces would critically strengthen the "capability trap" argument.

5. **Missing related work**: Huang et al. (2024) on self-correction failure, GSM-Symbolic, and V-STaR are significant omissions that affect positioning.

6. **Shallow failure mode analysis**: The constraint quality findings (35% tautological, etc.) deserve deeper investigation at the problem-structure level.

### Minor Issues
7. C0 contribution overstated — should be secondary.
8. ProofWriter depth restriction not disclosed.
9. Temperature ablation too narrow (one model, n=60).
10. Several bibliography entries incomplete.

### Constructive Recommendations
- **Reframe around the oracle result**: Lead with "symbolic aggregation works (+8.82pp) if and only if constraints are discriminative; self-extraction does not produce such constraints." This is more compelling and novel than leading with the negative result.
- **Implement cross-answer Z3 evaluation**: Even one condition testing self-extracted constraints with proper cross-answer evaluation would resolve the sigma concern and strengthen all conclusions.
- **Deepen failure mode analysis**: Characterize which problem structures produce the rare discriminative constraints (~12%). This would provide actionable guidance for improving extraction.
- **Add cross-model extraction**: One condition with a stronger extractor would significantly strengthen generality.
- **Position honestly relative to Logic-LM/LINC**: Frame the contribution as "rigorous quantification with mechanistic decomposition" rather than "discovery of a new phenomenon."

### Experiment Coverage vs. Design Plan
The paper covers all 15+ imagined experiments from the design document. The main gaps are analytical rather than experimental: the sigma cross-answer evaluation variant and cross-model extraction are the most impactful additions.

### Venue Recommendation
In current form: **EMNLP Findings** with revisions addressing the sigma concern and framing. With the cross-answer evaluation experiment and reframing, potentially competitive for **EMNLP main conference**. Not currently at the bar for top ML venue main conference (NeurIPS/ICML/ICLR).

---

*Review conducted by 2 independent reviewers (R1: Methods+Experiments, R2: Novelty+Related Work) with full roundtable convergence.*