---
dream_id: dream_20260515T020837
tier: worst
overall_score: borderline - revise and resubmit (2.5/5)
timestamp: 2026-05-15T03:13:19.168653+00:00
---


# Dream Review Report: "Seed Variance Dominates Error Injection Signal in Low-Data Embodied Planning SFT"

**Venue**: Insights from Negative Results in NLP @ EMNLP 2026
**Review mode**: Full (2 Reviewers + Roundtable)
**Scoring basis**: ARR review form (Soundness 1–5, Excitement 1–5, Overall Recommendation 1–5)

---

## Step 1: Independent Reviews

### R1 — Methods + Experiments

#### Summary
The paper tests taxonomy-guided error injection (TaxEI) on ALFWorld embodied planning SFT with Qwen3-8B. Three conditions (Vanilla/TaxEI/Random) are trained across 3 seeds, revealing that initial single-seed findings are artifacts. Six experiments probe different facets of the null result.

#### Strengths
- **S1**: Well-controlled experimental design — TaxEI and Random share identical injected trajectories, differing only in the error tag text. This cleanly isolates the taxonomy label variable and preempts content-based confounds.
- **S2**: Six converging experiments probing the null from different angles (main results, training dynamics, scale ablation, cross-environment, per-operator, recovery prompting, qualitative analysis). The convergence is more persuasive than any single experiment alone.
- **S3**: The scale ablation (§3.3) is the paper's strongest experiment — it directly demonstrates that the 9K findings are low-data artifacts by showing gap compression from −8.6pp to −1.0pp as data scales to 50K.
- **S4**: Transparent reporting of per-seed results (Tables 4, 6) rather than just means allows readers to see the variance structure directly. The 14.9pp within-method swing for TaxEI (seed 0 vs seeds 42/123) is striking.

#### Weaknesses
- **W1**: **Self-undermining seed count.** The paper recommends ≥5 seeds but uses only 3. At n=3, the paired t-test has extremely low power for the observed effect sizes. A power analysis would show that detecting an 8.6pp difference with SD~8pp requires far more than 3 seeds. The paper's own evidence demonstrates the insufficiency of 3 seeds but does not acknowledge that its own conclusions are therefore provisional.
- **W2**: **Data volume confound is unaddressed.** Vanilla uses 4,358 samples; TaxEI and Random use 9,029. The ~2× data difference means TaxEI/Random models see more gradient steps. Any performance difference (or lack thereof) could be partially attributable to the volume mismatch. The paper should at minimum acknowledge this confound or include a Vanilla-upsampled control.
- **W3**: **Statistical testing is inadequate for the claims.** Paired t-tests with n=3 have essentially no power. The paper correctly notes that no comparison achieves significance, but then draws strong conclusions from the pattern of non-significance across experiments. "Six non-significant results converge" is rhetorically compelling but not statistically rigorous — multiple underpowered tests cannot substitute for a single adequately powered one.
- **W4**: **Qualitative analysis sample sizes are too small.** 25 TaxEI + 20 Vanilla failure cases yield very low cell counts for the χ² test. With expected cell counts below 5 in some categories, the χ² p=0.91 has almost no statistical power. The paper presents this as evidence that failure modes are identical, but a non-significant χ² with tiny samples is absence of evidence, not evidence of absence.
- **W5**: **Recovery prompting experiment (§3.6) adds limited information.** The ~2pp gains are within noise, and the experiment doesn't clearly distinguish between "error information is unhelpful in embodied planning" and "few-shot prompting is generally weak for this task." Without a control showing that few-shot prompting works for some other aspect of the task, the experiment is uninformative.

#### Questions for Authors
- Q1: Why not use 5+ seeds given your own recommendation? Even 5 seeds would substantially increase confidence.
- Q2: Have you considered a Vanilla-upsampled control (duplicate clean trajectories to match 9,029 samples) to control for the data volume confound?
- Q3: The 25K and 50K scale experiments — how were additional trajectories generated? Were they from the same GPT-5.2 prompt, or different collection campaigns? Could distribution shift between collection batches explain the convergence?
- Q4: Table 7 (recovery prompting) reports 0-shot performance for "Vanilla SFT" as 61.7%, while Table 1 reports Vanilla mean as 65.3%. Can you clarify this discrepancy?

#### R1 Scores
- Soundness: 3/5 (Acceptable — main claims directionally supported but statistical power is acknowledged insufficient)
- Excitement: 3/5 (Somewhat Exciting — convergence of six experiments is compelling despite individual weakness)
- Overall: 2.5/5 (Borderline — needs more seeds, data volume control, and expanded related work)
- Confidence: 3/5

---

### R2 — Novelty + Related Work

#### Summary
The paper reports a negative result on transferring error injection from tool-use to embodied planning domains, then reframes as an evaluation methodology contribution about seed variance in small-sample agent SFT. It cites only 5 references.

#### Strengths
- **S1**: **Honest self-correction narrative.** The progression from seed=42 excitement to multi-seed deflation is exactly what the Insights workshop values. This kind of transparent reporting of how initial findings dissolved is rare and instructive for the community.
- **S2**: **Appropriate venue fit.** The workshop explicitly lists "experiments on (in)stability of previously published results due to random initializations" as a target contribution type. This paper delivers exactly that — showing how a single seed can generate three convincing-looking patterns that all dissolve.
- **S3**: **The "noise hypothesis" is well-articulated.** The argument that embodied planning errors are syntactically indistinguishable from correct actions at the token level — making injection pure noise — is a clear, testable mechanistic explanation for the null result.
- **S4**: **Practical recommendations are concrete.** The four-point recommendation (≥5 seeds, per-seed reporting, significance testing, scale ablation) is actionable guidance that could improve evaluation practices.

#### Weaknesses
- **W1**: **Core novelty is thin.** "Single-seed results are unreliable in small-sample fine-tuning" is well-established. Dodge et al. (2020) — the paper's own citation — demonstrated that fine-tuning instability from random seeds produces large performance swings. McCoy et al. (2020, "BERTs of a feather") showed seed variance can flip generalization conclusions. Mosbach et al. (2021, "On the Stability of Fine-Tuning BERT") demonstrated similar instability. The paper does not explain how its contribution advances beyond applying this known insight to one specific setting (agent SFT with error injection).
- **W2**: **"Error injection = noise below 10K" is nearly tautological.** Given that (a) the training set is ~9K trajectories, (b) only 47 test tasks, (c) injected errors lack recovery pairing (unlike PALADIN), and (d) embodied planning errors are syntactically silent, the null result is arguably the expected outcome. The paper does not sufficiently distinguish its finding from the baseline expectation that "adding noise to a small dataset without recovery signal does not help."
- **W3**: **Related work is critically inadequate.** Five references for a paper making claims about training instability, data augmentation, cross-domain transfer, and evaluation methodology is unacceptable, even for a workshop paper. Critical omissions include:
  - McCoy et al. (2020) — seed-dependent generalization
  - Mosbach et al. (2021) — fine-tuning stability
  - Zhang et al. (2021) — few-sample BERT fine-tuning
  - D'Amour et al. (2022) — underspecification in modern ML
  - Song et al. (2024, ETO) — DPO-based alternative that avoids direct injection
  - Wang et al. (2024, "Learning From Failure") — negative example incorporation for agents
  - Arpit et al. (2017) — memorization dynamics in deep networks
  - Rolnick et al. (2017) — robustness to label noise
  - Yao et al. (2023, ReAct) — the prompting paradigm used in ALFWorld evaluation
- **W4**: **PALADIN comparison is heavily confounded.** PALADIN differs from TaxEI in at least five ways: (1) error-recovery pairing vs standalone errors, (2) 50K+ vs 9K trajectories, (3) inference-time retrieval of 55+ exemplars contributing ~30pp, (4) different base model, (5) different evaluation environment. The paper attributes the divergence primarily to "task structure" but does not control for these confounds. The most important — recovery pairing — is arguably sufficient on its own to explain the negative result. This possibility deserves prominent discussion.
- **W5**: **The ≥5 seed recommendation is asserted without formal justification.** No power analysis is presented. Given the observed variances (SD 3–9pp) and effect sizes (2–9pp), a proper power calculation would determine the required seed count for a given significance level and power. "≥5" appears to be a round-number heuristic rather than a derived recommendation.

#### Questions for Authors
- Q1: Can you provide a power analysis for the ≥5 seed recommendation? What minimum effect size could be detected at 80% power with 5 seeds given the observed variance?
- Q2: PALADIN pairs errors with recovery demonstrations; TaxEI does not. Isn't the most parsimonious explanation simply that injecting errors without recovery signal teaches the model to produce errors? Why invoke "task structure" when this confound is uncontrolled?
- Q3: Have you verified whether PALADIN's ToolBench evaluation exhibits similar seed variance, or is tool-use SFT genuinely more stable?
- Q4: The claim that ~30pp of PALADIN's +57pp gain comes from retrieval augmentation — can you cite the specific ablation from PALADIN that supports this decomposition?

#### R2 Scores
- Soundness: 3/5 (Acceptable — experimental design is generally careful but statistical power is low)
- Excitement: 3/5 (Somewhat Exciting — fits the workshop's scope but novelty is incremental over existing literature)
- Overall: 2.5/5 (Borderline — needs expanded related work, power analysis, and more careful PALADIN comparison)
- Confidence: 4/5

---

## Step 2: Cross-Sharing

**R1 → R2**: R1's data volume confound (Vanilla 4,358 vs TaxEI/Random 9,029) reinforces R2's concern about the PALADIN comparison — both highlight uncontrolled variables that could explain the null without invoking task structure. R1's observation about the recovery prompting experiment's low informativeness supports R2's view that some experiments add limited novelty.

**R2 → R1**: R2's identification of 10+ missing critical references contextualizes R1's methodological concerns — the paper's statistical limitations are more problematic given that the literature on fine-tuning instability is extensive and already well-known. R2's point that the null result is "nearly tautological" given the experimental setup challenges R1's assessment of the scale ablation as the "strongest experiment" — if the null is expected at 9K, showing it disappears at 50K is less informative.

---

## Step 3: Convergence

### Areas of Agreement (both reviewers)
1. The paper addresses a reasonable research question and fits the Insights workshop in principle.
2. The honest self-correction narrative (single-seed artifacts → null result) is the paper's most distinctive contribution.
3. The same-source dual-formatting design (TaxEI vs Random) is well-controlled.
4. Statistical power is severely limited throughout — 3 seeds with SDs of 3–9pp leaves no comparison significant, and the paper's own evidence demonstrates that 3 seeds is insufficient while recommending 5.
5. The related work section (5 references) is critically inadequate and must be substantially expanded.
6. The ≥5 seed recommendation lacks formal justification (no power analysis).
7. The PALADIN comparison has multiple uncontrolled confounds, most importantly the absence of recovery pairing in TaxEI.
8. The paper is clearly written and well-structured with good use of tables.

### Areas of Productive Disagreement
- **Novelty assessment**: R1 found the convergence of six experiments more compelling than R2, who viewed several experiments (training dynamics, recovery prompting) as adding limited information. **Resolution**: The convergence is structurally sound but each individual experiment is under-powered; the paper should acknowledge that converging non-significance is weaker evidence than a single well-powered null.
- **Severity of the data volume confound**: R1 flagged this as a significant methodological gap; R2 focused more on the recovery-pairing confound. **Resolution**: Both are legitimate; the paper should either add a Vanilla-upsampled control or explicitly acknowledge the volume confound as a limitation.
- **Expected vs. surprising null**: R2 viewed the null as "nearly tautological" given the setup; R1 was somewhat more generous. **Resolution**: The null at 9K is arguably expected, but the scale ablation showing convergence at 50K adds genuine information. The paper's contribution is stronger if it frames the 9K null as expected-in-retrospect and emphasizes the 50K convergence and variance-reduction dynamics.

---

## Step 4: Consolidated Assessment

### Paper Summary
This paper tests whether taxonomy-guided error injection (TaxEI), successful in tool-use domains (PALADIN), transfers to embodied planning (ALFWorld). Using a 4-operator perturbation taxonomy, three SFT conditions (Vanilla, TaxEI, Random) are trained on Qwen3-8B with 3 seeds. Six experiments reveal that initial single-seed findings (variance gradient, dose-response threshold, taxonomy penalty) are seed artifacts. The paper reframes as an evaluation methodology contribution: ≥5 seeds are needed for small-sample agent SFT evaluation, and error injection signal is noise below ~10K trajectories.

### Consolidated Strengths
1. **Self-correction narrative is the paper's strongest asset.** Transparently reporting that three "interesting" findings dissolved under multi-seed evaluation is exactly the kind of contribution the Insights workshop exists to publish. This serves as a cautionary tale for the agent SFT community.
2. **Clean experimental isolation.** The same-source dual-formatting design (TaxEI vs Random sharing identical injected trajectories) is methodologically sound and isolates the taxonomy label variable.
3. **Convergent evidence from multiple angles.** Six experiments all pointing to the same null — while individually under-powered — create a structurally persuasive case. The scale ablation (§3.3) is particularly informative, showing gap compression and variance-ratio reduction as data scales.
4. **Clear writing and transparent reporting.** Per-seed results in Tables 4 and 6, explicit p-values, and the 14.9pp within-method swing all help readers assess the evidence directly.
5. **Actionable practical recommendations.** The four-point evaluation guideline (§4, Practical recommendation) is concrete enough to influence future work.

### Consolidated Weaknesses
1. **Related work is unacceptable (5 references).** The paper makes claims spanning training instability, data augmentation, cross-domain transfer, and evaluation methodology but cites almost none of the extensive prior work. Critical omissions include McCoy et al. (2020), Mosbach et al. (2021), D'Amour et al. (2022) on fine-tuning instability; Song et al. (2024, ETO), Wang et al. (2024) on learning from agent failures; Arpit et al. (2017), Rolnick et al. (2017) on noisy-label learning; and Yao et al. (2023, ReAct) on the prompting paradigm used. This gap undermines the paper's scholarly contribution and makes the novelty claims appear stronger than they are.
2. **The paper uses 3 seeds but recommends ≥5 — a self-undermining gap.** The paper's own evidence demonstrates that 3 seeds is insufficient for reliable conclusions. This means its own conclusions are, by its own standard, unreliable. The ≥5 recommendation itself lacks formal justification — a power analysis given the observed effect sizes and variances would strengthen it considerably or might reveal that many more seeds are needed.
3. **Core novelty is limited.** "Single-seed fine-tuning results are unreliable" and "more data helps" are well-established findings in the NLP literature (Dodge et al. 2020, Mosbach et al. 2021). The paper's specific contribution — applying this insight to agent SFT with error injection — is incremental. The most novel elements (variance gradient proportional to injection structure, per-operator analysis) are themselves under-powered at n=3.
4. **PALADIN comparison is heavily confounded.** The paper frames its results against PALADIN but does not control for recovery pairing (PALADIN pairs errors with recovery demonstrations; TaxEI injects standalone errors), data scale (50K+ vs 9K), inference-time retrieval (~30pp contribution), base model, or evaluation environment. The recovery-pairing difference alone is a plausible explanation for the null result, making "task structure" an unnecessary hypothesis. The ~30pp retrieval attribution is stated without citing a specific PALADIN ablation.
5. **Data volume confound.** Vanilla (4,358 samples) has roughly half the data of TaxEI/Random (9,029). The paper does not acknowledge or control for this asymmetry.
6. **Qualitative failure analysis is under-powered.** 25 + 20 cases yield cell counts too small for meaningful χ² inference. The p=0.91 is absence of evidence, not evidence of absence.

### Consolidated Questions for Authors
1. Can you provide a formal power analysis for the ≥5 seed recommendation? What is the minimum detectable effect at 80% power with 5 seeds?
2. Why not use ≥5 seeds in this study, given your own recommendation?
3. How do you respond to the concern that the null result is expected given the absence of recovery pairing (unlike PALADIN)?
4. Can you cite the specific PALADIN ablation supporting the ~30pp retrieval attribution?
5. Have you considered a Vanilla-upsampled control to address the data volume asymmetry?
6. The Table 7 0-shot Vanilla SFT recovery rate (61.7%) differs from Table 1 Vanilla mean (65.3%) — can you clarify?

### Experiment Coverage Assessment
All 6 planned experiments from the experimental design are covered:
| Planned Experiment | Paper Section | Coverage |
|---|---|---|
| Training Dynamics Analysis | §3.2 | Full — loss decomposition by sample type, 3-seed mean ± SE |
| Second Environment (WebShop) | §3.4 | Full — 3 conditions × 3 seeds |
| Qualitative Failure Analysis | §3.7 | Full — 25+20 cases, χ² test, operator-error correlation |
| Scale Ablation (25K–50K) | §3.3 | Full — 3 scale points × 2 conditions × 3 seeds |
| Recovery Prompting | §3.6 | Full — 3 base models × 3 shot conditions |
| Per-Operator Deep Dive | §3.5 | Full — 4 operators × 3 seeds with Vanilla comparison |

The paper faithfully covers the full experimental plan. No planned experiment is omitted.

### Missing Experiments That Would Strengthen the Paper
1. **Vanilla-upsampled control** — duplicate clean trajectories to match 9,029 samples, controlling for data volume.
2. **Error-recovery paired injection** — matching PALADIN's design to isolate the recovery-pairing variable from the task-structure variable.
3. **≥5 seed evaluation** on the core 9K comparison to meet the paper's own recommendation.
4. **Formal power analysis** to justify the seed-count recommendation.

### Venue Fit Assessment
The paper is a natural fit for the Insights from Negative Results in NLP workshop. It reports a genuine negative result (error injection doesn't transfer to embodied planning at low data scales), demonstrates the instability of single-seed conclusions (a core workshop theme), and provides actionable methodological advice. The self-correction narrative is exactly what the venue rewards.

However, the inadequate related work, self-undermining seed count, and limited novelty over existing literature on fine-tuning instability prevent a confident accept in the current form.

### Consolidated Scores

| Dimension | R1 | R2 | Consensus |
|---|---|---|---|
| Soundness | 3/5 | 3/5 | **3/5** (Acceptable) |
| Excitement | 3/5 | 3/5 | **3/5** (Somewhat Exciting) |
| Overall | 2.5/5 | 2.5/5 | **2.5/5** (Borderline — Resubmit with Revisions) |
| Confidence | 3/5 | 4/5 | **3.5/5** |

### Recommendation
**Borderline — revise and resubmit next cycle (2.5/5).** The paper reports a legitimate negative result appropriate for the Insights workshop, with a compelling self-correction narrative and clean experimental isolation. However, three issues must be addressed before acceptance: (1) the related work must be expanded from 5 to at least 15–20 references covering fine-tuning instability, noisy-label learning, and agent failure-learning literature; (2) the self-undermining gap between using 3 seeds and recommending 5 should be closed, either by running additional seeds or by including a formal power analysis that acknowledges the limitation; (3) the PALADIN comparison must explicitly discuss the recovery-pairing confound as an alternative explanation for the null result. With these revisions, the paper could be a solid contribution to the workshop.
