---
dream_id: dream_20260516T153939
tier: worst
overall_score: 3 — Reject
timestamp: 2026-05-16T16:24:18.457038+00:00
---

# Dream Review Report: "The Training Lottery: Why Error Injection Destabilizes Embodied Planning Agents Across Architectures"

**Review Mode:** Full (2 Reviewers + Roundtable)
**Date:** 2026-05-16
**Venue Standard:** Top ML venue (acceptance ~25%, 6-point scale)

---

## Reviewer 1 — Methods & Experiments

### Summary
The paper tests whether PALADIN-style taxonomy-guided error injection transfers from tool-use agents to embodied planning (ALFWorld). Three conditions (Vanilla / TaxEI / Random) are compared across 5 seeds on Qwen3-8B and 3 seeds on LLaMA-3.1-8B. The main finding is negative: both injection methods degrade performance identically (−9.0pp), taxonomy labels add nothing, and within-condition seed variance dominates between-condition differences. The paper frames this as a "training lottery" methodological warning.

### Strengths
1. **Multi-seed evaluation is commendable.** Most agent papers report single-seed results. Using 5 seeds on Qwen and 3 on LLaMA, with explicit variance reporting and power analysis, sets a good example for the field.
2. **Honest statistical reporting.** The paper transparently acknowledges Bonferroni non-significance, 45.2% power, and the n=9 requirement for 80% power. This self-awareness is rare and valuable.
3. **Clean three-condition design.** The Vanilla/TaxEI/Random comparison cleanly isolates the contribution of taxonomy labels (zero, as shown by TaxEI = Random).
4. **Dose-response analysis.** Testing at 10%, 25%, 50%, and full injection rates across seeds adds useful structure, and the finding that within-condition variance exceeds between-condition at ALL doses is informative.

### Weaknesses

**W1. Critical: Tables 1 and 2 appear to contain identical data.**
Table 1 (clean eval) and Table 2 (recovery eval under injected conditions) have the same per-seed values for ALL conditions (Vanilla, TaxEI, Random) across ALL seeds. The Vanilla means differ (67.3 vs 66.4), but recomputing from the per-seed values: (61.7+68.1+66.0+74.5+61.7)/5 = 66.4 — suggesting Table 1's mean of 67.3 is a computational error. If recovery eval truly produces identical results to clean eval, the recovery experiment adds no new information beyond confirming that eval-time injection has no effect — which is far less interesting than the paper claims. If the data are erroneously duplicated, this is a serious mistake. Either way, the "resilience not recovery" finding rests on a table that is either trivially uninformative or contains errors.

**W2. Major: Study is critically underpowered — by the paper's own admission.**
At n=5 seeds, power = 45.2%. All pairwise comparisons are Bonferroni NS. Cohen's d=1.58 is large, but this is a point estimate from 5 data points with high variance. The paper's central claim — that the training lottery dominates — could equally be restated as: "we couldn't detect between-condition effects because our sample size was too small." High within-condition variance at n=5 is statistically expected; it doesn't prove the training lottery dominates — it proves the study is underpowered.

**W3. Major: Data volume confound is inadequately controlled.**
Vanilla trains on 4,358 samples vs. 9,029 for TaxEI/Random (~2× more data). The paper mentions a 10% dose ablation with matched total samples, but this is a footnote rather than a properly presented experiment. The performance drop could stem from distribution shift due to data mixing rather than error injection per se. This confound is especially problematic because Vanilla's lower variance (SD=4.7 vs 6.2–6.4) could reflect the simpler/cleaner training distribution rather than any property of error injection.

**W4. Major: Cross-model results are self-contradictory.**
Table 5 reveals 4 of 5 cross-model comparisons are inconsistent:
- Random injection: harmful on Qwen (−9.0pp), beneficial on LLaMA (+3.5pp)
- Variance ratio (TaxEI/Random): 0.75× on Qwen, 4.1× on LLaMA — opposite directions
- Detection rate: 0% on Qwen, 25.5% on LLaMA
- TaxEI harm magnitude: −9.0pp vs −3.6pp

The only consistent finding is "at least one catastrophic seed exists" — which, at 3–5 seeds each, is a weak observation (one outlier in a small sample). The paper claims cross-model "confirmation" of instability, but the data more naturally read as: effects are entirely model-specific, with no generalizable pattern.

**W5. Minor: Recovery prompting is single-seed (s42), n=47.**
A +2.1pp improvement = 1 additional task out of 47. This is within sampling noise for binary outcomes and cannot support any conclusion. The experiment should either use multi-seed data or be removed.

**W6. Minor: Per-operator analysis is presented then invalidated.**
Section 4.6 honestly reports that the single-seed local/global pattern was noise. While transparency is admirable, presenting an analysis only to retract it consumes space without advancing knowledge. The self-refutation is awkward — it reads as: "we did an analysis, it was wrong, but this supports our point about variance." The training lottery framing tries to recoup this, but it's a stretch.

### Questions for Authors
- Q1: Are Tables 1 and 2 actually different experiments? If so, why are all 15 per-seed values identical? If recovery eval truly equals clean eval, what does this tell us beyond "eval-time injection has no measurable effect"?
- Q2: What are the 10% dose ablation results with matched sample sizes (4,358 total)? This is critical for disambiguating the data volume confound.
- Q3: How do you reconcile the claim that error injection "amplifies the training lottery" with the alternative explanation that you simply have insufficient statistical power?

### R1 Score: 3 (Reject)
The study is transparently honest but critically underpowered, with a data confound, self-contradictory cross-model evidence, and a potential data duplication issue in the recovery evaluation.

---

## Reviewer 2 — Novelty & Related Work

### Summary
The paper frames the failure of error injection transfer as a "training lottery" warning and proposes task-structural boundary conditions (error observability, recovery locality, feedback granularity) for when error injection can succeed.

### Strengths
1. **Relevant research question.** Testing whether PALADIN's gains generalize beyond tool-use is a natural and important question. Negative transfer results have practical value when well-characterized.
2. **The structural hypothesis is well-articulated.** The three-factor framework (observability, locality, granularity) in Section 5.2 gives an intuitive explanation for why embodied planning resists error injection. This could be useful if developed further.
3. **Resilience vs. recovery distinction.** Operationalizing the difference between passive noise tolerance and active error correction is a useful conceptual contribution, even if the evidence here is limited.

### Weaknesses

**W1. Critical: The negative result is structurally predictable.**
The differences between tool-use and embodied planning — discrete error codes vs. diffuse environmental observations, local retry vs. cascading state corruption, per-call feedback vs. sparse reward — straightforwardly predict that SFT-based error injection will fail in embodied planning. Any researcher familiar with both PALADIN and ALFWorld could predict the direction of this result from first principles. A "negative result" paper must offer something surprising; this one confirms the expected.

**W2. Critical: The "training lottery" contribution is incremental.**
McCoy et al. (2020), Mosbach et al. (2021), and D'Amour et al. (2022) already established that fine-tuning is seed-sensitive, especially on small datasets. Showing that adding noise to a small dataset (501 base trajectories × 4 operators → 9K samples) amplifies seed sensitivity is unsurprising. The extension to error injection is a single-factor instantiation of an already-known phenomenon, not a new insight. The paper does not offer a mechanistic explanation for *why* error injection amplifies variance beyond the general "noisy data → noisy outcomes" intuition.

**W3. Major: Related work is thin and missing key connections.**
Only 8 references total. Significant omissions:
- **Domain randomization** (Tobin et al. 2017; Peng et al. 2018): Unstructured perturbation of observations/dynamics in embodied settings — directly analogous to Random condition. Domain randomization succeeds when perturbations are diverse and observable, aligning with the paper's structural hypothesis but never discussed.
- **Noise injection for robustness** (Xie et al. 2020, data augmentation literature): Broad literature on when adding noise helps vs. hurts, including conditions (signal-to-noise ratio, distribution support) that map onto this paper's findings.
- **Anti-curriculum / hard-example mining**: Literature on when training on difficult examples helps vs. hurts, directly relevant to error injection timing/scheduling.
- **Data poisoning**: Studies on when injected distribution shifts degrade performance — the error injection here is functionally data poisoning from the model's perspective.
- **RL-based error recovery** (Reflexion, Trial-and-Error): The paper mentions ReAct and Reflexion but doesn't engage with *why* inference-time approaches succeed while SFT-based injection fails. This is the core mechanistic question left unanswered.

**W4. Major: No positive contribution or constructive guidance.**
The paper says "error injection doesn't work here" but offers no path forward. What *would* work for embodied planning robustness? Options not explored:
- RL-based recovery training (Reflexion-style self-correction during training)
- Explicit error markers in observations (making errors observable)
- Curriculum scheduling of error injection (easier errors first)
- Contrastive learning on correct vs. corrupted trajectories

A methodological warning without constructive alternatives has limited value — it tells the community what not to do (which was already guessable) without advancing what to do instead.

**W5. Major: Contribution claims are overstated relative to evidence.**
- "Training lottery methodological warning": Already known from prior work; this is a confirming instance, not a new finding.
- "First cross-domain transfer test": The novelty of being "first" is low when the result is the expected one and the analysis doesn't yield new understanding of *when* transfer succeeds.
- "Resilience not recovery": Follows trivially from 0% detection rate, which follows from the absence of explicit error signals in ALFWorld observations. Without error markers, detection is structurally impossible — this is a property of the evaluation design, not a finding about models.
- "Complete dose-response profile": The dose-response data exists but is mentioned rather than prominently analyzed; the claim oversells what is delivered.

**W6. Minor: The PALADIN comparison is too confounded to be informative.**
As the paper acknowledges (Section 5.4), the comparison involves confounds in base model, scale (9K vs 50K+), and inference-time retrieval (~30pp contribution). The paper tests "error injection in its most isolated form (pure SFT, no retrieval)" — but PALADIN's design deliberately combines these components. Removing retrieval and comparing the crippled version to a different domain on a different benchmark with 1/5 the data doesn't tell us whether the *approach* fails to transfer or whether the *isolated component* is insufficient everywhere.

### Questions for Authors
- Q1: Given the structural hypothesis, what would a successful error injection scheme for embodied planning look like? Can you propose and test at least one design that addresses the observability/locality/granularity gaps?
- Q2: How does your error injection differ functionally from domain randomization, which has shown mixed results in embodied settings? This literature seems directly relevant.
- Q3: The 25.5% detection rate on LLaMA vs. 0% on Qwen is unexplored — if one model *can* detect errors, doesn't this undermine the claim that embodied errors are structurally undetectable?

### R2 Score: 3 (Reject)
The negative result is predictable from domain structure, the "training lottery" contribution is incremental over prior work, related work coverage is insufficient, and the paper provides no constructive path forward.

---

## Roundtable Discussion

### Step 1: Independent Assessments
- R1: Score 3 — Critical methodological issues (power, data confound, Table 1/2 duplication, self-contradictory cross-model evidence)
- R2: Score 3 — Predictable negative result, incremental novelty, thin related work, no positive contribution

### Step 2: Cross-Sharing
- R1 agrees with R2 that the predictable nature of the result compounds with the power issues: even if the statistics were clean, the finding wouldn't be surprising enough for a top venue.
- R2 agrees with R1 that the Table 1/2 data identity is concerning. If recovery eval ≡ clean eval, the "resilience not recovery" claim reduces to: "eval-time perturbations have no measurable effect" — a finding that is either trivial (errors too subtle to matter) or an artifact (the injection was poorly designed).
- Both note that the cross-model evidence is the paper's weakest point: 4/5 metrics inconsistent effectively invalidates any "architecture-general" claim.

### Step 3: Convergence
**Agreed weaknesses (all must be addressed for reconsideration):**
1. Underpowered design cannot distinguish "training lottery dominates" from "insufficient sample size" — need ≥9 seeds
2. Data volume confound must be properly controlled with matched-size ablation presented as a main result
3. Table 1/2 identity must be explained or corrected
4. Cross-model results contradict main claims; paper needs either more models or a revised thesis
5. The negative result is predictable; the paper needs a substantially stronger positive contribution (structural conditions formalized, proposed fix tested, mechanistic analysis)
6. Related work must engage with domain randomization, noise injection, and RL-based recovery literatures

**Point of minor divergence:**
- R1 is slightly more sympathetic to the honest statistical reporting as a virtue; R2 views transparency as insufficient when claims still outrun evidence. Consensus: honesty is necessary but not sufficient.

### Step 4: Consolidated Assessment

**Overall Score: 3 — Reject**

**Confidence: 4 (High)**

### Decision Rationale
The paper addresses a reasonable question — whether PALADIN-style error injection transfers to embodied planning — but falls short of top-venue standards on multiple axes:

1. **The finding is not surprising.** The structural differences between tool-use and embodied planning (observable vs. diffuse errors, local vs. cascading failures, dense vs. sparse feedback) predict the negative result. A negative-result paper must compensate with deep mechanistic understanding or constructive alternatives; this paper offers neither.

2. **The statistics don't support the claims.** All comparisons are Bonferroni NS. Power is 45%. The "training lottery" framing is unfalsifiable at this sample size — any high-variance result in a 5-seed study looks like a "lottery." The paper cannot distinguish its central thesis from the null hypothesis that the study was simply too small.

3. **Cross-model evidence undermines generalizability.** With 4/5 metrics inconsistent between Qwen and LLaMA, the paper's own data argues against architecture-general conclusions. The only replicating finding — "at least one bad seed exists" — is nearly tautological at small n.

4. **The "training lottery" contribution is incremental.** Seed sensitivity of fine-tuning is well-established. Showing it applies to one more setting (error-injected SFT on ALFWorld) doesn't clear the novelty bar.

5. **Missing constructive contribution.** The paper warns against error injection but proposes no alternative. The structural hypothesis (Section 5.2) is promising but untested — formalizing and experimentally validating when injection succeeds vs. fails would substantially strengthen the work.

### Suggestions for Improvement
- **Increase to ≥9 seeds** on at least the primary model to achieve 80% power; this would make the "training lottery" claim credible rather than self-fulfilling.
- **Control the data volume confound** by presenting matched-size experiments (same total samples across conditions) as main results, not footnotes.
- **Investigate and explain** the Table 1/2 data identity, and the LLaMA 25.5% detection rate vs. Qwen 0%.
- **Expand to ≥1 additional benchmark** beyond ALFWorld (e.g., WebArena, ScienceWorld) to test the structural hypothesis.
- **Propose and test a fix**: e.g., add explicit error markers to observations, use contrastive trajectory pairs, or apply Reflexion-style RL training.
- **Deepen related work** to engage with domain randomization, noise injection robustness, and RL-based recovery.
- **Formalize the structural hypothesis** as testable predictions (e.g., error injection succeeds iff error observability > threshold AND recovery locality < k steps).

### Experiment Coverage Assessment
Relative to the experimental design document (review_context.yaml), the paper covers all 6 planned experiment categories:
| Experiment | Covered? | Quality |
|---|---|---|
| Recovery Eval Multi-Seed (5-seed × 3 conditions) | Yes (Table 2) | Data appears duplicated from Table 1 |
| LLaMA Cross-Model (3-seed) | Yes (Tables 4-5) | Results are self-contradictory |
| Scale-Up 501→2500 | Yes (Table 6) | Inconclusive by authors' admission |
| Scale Feasibility (25K-50K) | Yes (Table 7, discussion) | Correctly identified as infeasible |
| Recovery Prompting | Yes (Table 3) | Single-seed, n=47, within noise |
| Per-Operator Deep Dive | Yes (Table 8) | Honestly reported as non-replicating |

Coverage is complete, but multiple experiments yield null/inconclusive results, and the recovery evaluation may be artifactual. The paper would benefit from replacing weak experiments (recovery prompting at single seed, per-operator analysis) with stronger ones (more seeds, additional benchmarks, proposed fixes).
