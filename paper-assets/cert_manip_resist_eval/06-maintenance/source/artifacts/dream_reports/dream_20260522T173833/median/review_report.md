---
dream_id: dream_20260522T173833
tier: median
overall_score: 2.5 — Borderline Findings
timestamp: 2026-05-22T18:46:26.231438+00:00
---

# Dream Review Report — Full Roundtable

**Paper:** "Rethinking Diversity in LLM Evaluation Panels: When More Judges Make Things Worse"
**Dream ID:** 20260522T173833
**Venue:** EMNLP 2026 (ARR)
**Review Mode:** Full (2 Reviewers, 4-step roundtable)

---

## Reviewer Assignments
- **R1:** Methods & Experiments
- **R2:** Novelty & Related Work

---

## Step 1: Independent Reviews

### R1 — Methods & Experiments

**Summary:** The paper uses residualized regression across 15 models, 455 exhaustively enumerated three-judge panels, 6 attack types, and 2 MCQ benchmarks to disentangle η_max (individual judge weakness) from K_eff (panel diversity) as predictors of panel attack success rate (ASR). η_max dominates (9/12 significant, partial η²=0.18); K_eff is secondary (7/12 significant, partial η²=0.04). Aggregation rule analysis, within-tier validation, and BFT contrast are provided.

**Strengths:**
- **S1.** Exhaustive combinatorial enumeration of all C(15,3)=455 panels eliminates sampling bias entirely for K=3. Clean design that is stronger than any subsampling approach.
- **S2.** Honest reporting of K_eff attenuation from 7/12 (full pool) to 2/18 (within-tier). Intellectual honesty commendable.
- **S3.** Multi-layered statistical validation: residualized regression, BH FDR correction, Bonferroni as conservative bound, beta regression robustness check (92% concordance with OLS).
- **S4.** Aggregation rule analysis (Table 5) showing threshold amplifies K_eff (1.45×) while Bayesian partially mitigates η_max (0.55×) is practically informative and theoretically coherent.
- **S5.** Attack-type decomposition (transferable vs. shared-bias) provides the most conceptually valuable mechanistic insight. Clear boundary conditions for when diversity matters.

**Weaknesses:**

- **W1 [Major]. Non-linear confounding renders the K_eff claim fragile.** VIF=1.00 by construction eliminates linear collinearity, but the within-tier analysis is the paper's own strongest evidence against itself: K_eff significance drops from 7/12 (full pool) to 2/18 (within-tier). This collapse strongly suggests that the full-pool K_eff effect is substantially driven by non-linear confounding with capability tier mixing — exactly the artifact that linear residualization cannot remove. The paper frames this as "attenuation," but the magnitude (from majority-significant to near-zero) suggests the K_eff effect may be largely artifactual once tier composition is properly controlled. The 2 confound-free conditions (ARC×SM, ARC×PB with r≈0.35) partially address this, but: (a) low linear correlation does not guarantee absence of non-linear confounding; (b) with n=455, even trivial systematic effects achieve very low p-values. The paper should fit a GAM or include tier indicators as additional controls.

- **W2 [Major]. K_eff partial η²=0.04 raises practical significance concerns.** An effect explaining 4% of variance is small by Cohen's conventions. With n=455, statistical significance is cheap. The paper never reports confidence intervals for predicted ASR differences when K_eff moves across its observed range while holding η_max constant. Without these, the reader cannot assess whether the "diversity trap" is practically meaningful or statistically detectable but negligible. The title framing ("When More Judges Make Things Worse") implies large practical effects that partial η²=0.04 does not support.

- **W3 [Significant]. Two-stage algorithm does not significantly outperform Strongest-K.** The paper reports p=0.42 for Two-stage vs. Strongest-K comparison (Section 4.7). The ASR difference is <1 percentage point (0.091 vs 0.091). The practical contribution of the proposed defense is weak — the actionable recommendation reduces to "use robust judges," which is an obvious baseline. The paper partially acknowledges this ("statistically indistinguishable at p=0.42") but the algorithm is still listed as a contribution.

- **W4 [Significant]. Full-knowledge adaptive adversary is unrealistic.** The threat model gives the adversary full knowledge of per-judge vulnerability profiles. Under partial-knowledge adversaries (Section 4.5), K_eff significance drops from 7/12 to 3/12, and mean β(K_eff) drops by 33%. The diversity risk factor is thus highly sensitive to adversary capability, substantially diminishing the practical threat. The paper acknowledges this but it's buried in Section 4.5 rather than prominently qualifying the main claims.

- **W5 [Significant]. Only MCQ benchmarks; open-ended results inconclusive.** Findings are established on MMLU and ARC only. The paper reports preliminary open-ended results showing direction-consistent but non-significant K_eff effects (p range 0.065–0.185, R²=0.12), with power analysis indicating N≈1,200 panels needed for 80% power. This limits generalizability to the most common evaluation format.

- **W6 [Moderate]. Attack operationalization details are thin.** The paper categorizes 6 attacks into mechanism types but does not describe how attacks like "sycophancy" or "authority bias" are concretely operationalized on MCQ evaluation tasks. Without seeing attack prompts, ecological validity is difficult to assess.

**R1 Preliminary Scores:**

| Dimension | Score |
|-----------|-------|
| Soundness | 3.0 |
| Excitement | 2.5 |
| Reproducibility | 2.5 |
| Overall | 2.5 (Borderline Findings) |

---

### R2 — Novelty & Related Work

**Summary:** Same as R1. R2 focuses on whether the contributions are novel relative to existing literature and whether the paper is adequately positioned.

**Strengths:**
- **S1.** Genuinely important and timely question. The assumption "diversity = robustness" is pervasive in multi-judge LLM evaluation practice. Subjecting it to rigorous empirical testing at scale is valuable regardless of outcome.
- **S2.** The condition-dependent dominance pattern (transferable 5/6 K_eff sig vs. shared-bias 1/8) has real explanatory power. This goes beyond a simple negative result and provides a predictive framework based on attack transferability.
- **S3.** Aggregation rule analysis reveals meaningful interactions with direct prescriptive value (avoid unanimity in adversarial settings; Bayesian partially mitigates weakness).
- **S4.** Exhaustive enumeration eliminates sampling artifacts.

**Weaknesses:**

- **W1 [Major]. The core finding has substantial precedent in adversarial ML ensemble literature, insufficiently acknowledged.** Tramer et al. (2018, "Ensemble Adversarial Training") showed that ensemble diversity does not protect against transferred adversarial examples and can make ensembles more exploitable. Kariyappa & Qureshi (2019) explicitly studied the diversity-robustness tradeoff. The paper's central mechanism — adaptive adversaries exploit the diverse attack surface — is the LLM-judge instantiation of an established phenomenon. The paper must position against this literature and articulate what is new beyond domain transfer.

- **W2 [Major]. Related work section has significant gaps.** At ~0.5 pages, Section 2 is thin for EMNLP 2026. Critical omissions:
  - **Condorcet Jury Theorem (CJT):** Directly predicts the paper's finding — when weak judges have η_j > 0.5, adding independent voters makes majority voting worse. The "diversity trap" may simply be the CJT prediction under adversarial conditions.
  - **Verga et al. (2024) PoLL:** Directly relevant study on multi-judge panel composition.
  - **Panickssery et al. (2024):** Sycophancy in LLMs, relevant to the sycophancy exception.
  - **Security games / Stackelberg formulations:** The adaptive adversary is essentially a Stackelberg leader-follower game.
  - **Bias-variance-covariance decomposition:** Ueda & Nakano (1996), Liu & Yao (1999) on when ensemble diversity helps vs. hurts.
  Expected reference count for this interdisciplinary scope: 30-40. Current: ~15-20.

- **W3 [Significant]. "First large-scale empirical study" claim needs qualification.** The ensemble adversarial robustness literature has studied composition effects extensively. The claim should be scoped: "the first controlled study disentangling diversity from individual robustness as predictors of panel vulnerability in LLM evaluation."

- **W4 [Significant]. Title framing not fully supported by evidence.** "When More Judges Make Things Worse" conflates diversity with capability heterogeneity. The within-tier analysis shows diversity is largely neutral (2/18 sig) when capability is controlled. The accurate characterization is "when diverse panels include weak judges, the weak judges dominate vulnerability" — closer to "weak judges make things worse" than "diversity makes things worse."

- **W5 [Significant]. BFT framing is illustrative, not substantive.** No sign reversal between adaptive and random-fault regimes (K_eff positive in both). The BFT reversal is reduced to a relative importance shift, not a qualitative regime change. The Condorcet Jury Theorem provides a more natural theoretical framework without requiring the BFT analogy.

- **W6 [Moderate]. Practical contribution reduces to "use strong judges."** Two-stage vs. Strongest-K is non-significant (p=0.42). The actionable insight ("screen for robustness before considering diversity") is indistinguishable from "use the strongest available judges." This is not a research contribution.

**R2 Preliminary Scores:**

| Dimension | Score |
|-----------|-------|
| Soundness | 3.0 |
| Excitement | 2.5 |
| Reproducibility | 3.0 |
| Overall | 2.5 (Borderline Findings) |

---

## Step 2: Cross-Sharing — Key Observations

After exchanging reviews:

- **R1 and R2 converge on** the within-tier collapse (7/12 → 2/18) as the paper's Achilles' heel. R1 frames this as a methodological concern (non-linear confounding); R2 frames it as undermining the title claim. Both are valid and complementary.
- **R1 and R2 converge on** the two-stage algorithm's non-significance vs. Strongest-K (p=0.42) as weakening the practical contribution.
- **R2's CJT point resonates with R1:** The "diversity trap" under adversarial conditions may be a straightforward CJT prediction when η_max > 0.5. This connection, if acknowledged, would reframe the paper's contribution as an empirical validation in a new domain rather than a novel insight.
- **R1's concern about attack operationalization** is reinforced by R2's observation that the paper needs to position against adversarial ML ensemble literature — without concrete attack descriptions, it's unclear whether the LLM-judge setting introduces genuinely new phenomena.

---

## Step 3: Convergence — Consolidated Assessment

### Agreed Strengths
1. **Scale and design rigor** — exhaustive C(15,3)=455 enumeration, 15 models × 6 families × 3 tiers, is a strong design that eliminates sampling bias
2. **Attack-type taxonomy** — the transferable vs. shared-bias decomposition provides genuine mechanistic insight and is the most novel empirical contribution
3. **Aggregation rule analysis** — threshold amplifying K_eff (1.45×) and Bayesian partially mitigating η_max (0.55×) has direct prescriptive value
4. **Honest self-limiting** — prominently reporting within-tier attenuation and BFT non-reversal as limitations rather than burying them

### Agreed Weaknesses (ranked by severity)
1. **[Critical] Tier-mixing confound inadequately resolved.** The within-tier collapse (7/12 → 2/18) is the most damaging evidence against the primary K_eff claim. Linear residualization (VIF=1.00) does not address non-linear confounding. The paper honestly reports this but does not deploy appropriate countermeasures (GAM, polynomial regression, tier-indicator controls, mediation analysis). The 2 confound-free conditions (ARC×SM, ARC×PB) are suggestive but narrow.

2. **[Major] Small effect size and overclaimed framing.** Partial η²=0.04 for K_eff is a small effect. The title "When More Judges Make Things Worse" and the narrative framing ("diversity trap") imply practical consequences that the data do not clearly support. Within capability tiers, diversity is approximately neutral. The accurate headline is: "in heterogeneous model pools mixing capability tiers, panel diversity is a secondary risk amplifier for transferable attacks, with a small effect size."

3. **[Major] Related work and novelty positioning.** Section 2 is too thin. The paper does not engage with CJT (which directly predicts the core finding under adversarial conditions), adversarial ensemble robustness literature (Tramer et al. 2018, Kariyappa & Qureshi 2019), PoLL (Verga et al. 2024), or security games formulations. The "first large-scale" claim is over-scoped. These gaps leave the paper's novelty claim vulnerable to a "domain transfer, not new insight" critique.

4. **[Significant] Practical contribution is weak.** Two-stage ≈ Strongest-K (p=0.42, <1pp difference). The actionable recommendation is "use robust judges," which is the obvious default. The diversity tiebreaker contributes negligibly.

5. **[Significant] BFT without sign reversal.** The theoretical motivation (BFT predicts diversity helps under random faults, hurts under adaptive) is not confirmed: K_eff is positive in both regimes. The paper correctly notes this as a limitation but still lists BFT contrast as a contribution. The CJT is a more natural and parsimonious theoretical framework.

6. **[Moderate] Scope limited to MCQ.** MMLU and ARC only. Open-ended evaluation results are inconclusive (p=0.065–0.185). Generalizability to the increasingly important open-ended evaluation setting is unestablished.

7. **[Moderate] Adversary realism.** Full-knowledge adversary is a worst case. Under partial knowledge, K_eff effect attenuates 57%. The practical threat is substantially diminished under realistic adversary models.

### Points of Divergence (resolved)
- R1 initially scored Reproducibility lower (2.0) citing missing attack prompts; R2 scored 3.0 noting that K_eff is properly formalized (Equation 1). **Resolved at 2.5:** The statistical framework is well-specified but attack operationalization details are insufficient for independent replication.
- R2 raised the CJT connection more forcefully; R1 focused on specification checks. **Both are valid and complementary:** CJT frames the novelty question; specification checks frame the soundness question. They should appear as separate concerns in the report.

---

## Step 4: Consolidated Scores and Recommendation

### Final Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| **Soundness** | 3.0 / 5 | Statistical framework (residualized regression, FDR, beta regression robustness check) is competent. But the core K_eff claim is undermined by the within-tier collapse, which the linear residualization does not adequately address. Effect size is small (η²=0.04). Theorem 1 is near-trivial. |
| **Excitement** | 2.5 / 5 | Important question, timely for the LLM-as-judge community. The attack taxonomy and aggregation modulation are moderately interesting. But the core finding (weak judges dominate vulnerability; diversity is a secondary, condition-dependent amplifier) is predictable from CJT and adversarial ensemble ML. The practical recommendation is trivially obvious. |
| **Reproducibility** | 2.5 / 5 | Panel enumeration and regression specification are well-described. K_eff is properly formalized. But attack operationalization details are thin (no prompts shown), no code/data release is mentioned, and the adversary implementation is underspecified. |

### Overall Assessment: **2.5 — Borderline Findings**

### Justification

The paper addresses an important and timely question — whether diversity in multi-judge LLM evaluation panels improves adversarial robustness — with substantial experimental scale (455 panels, 15 models, 6 attacks). The exhaustive combinatorial design is a clear strength, and the attack-type taxonomy (transferable vs. shared-bias) provides genuine mechanistic insight.

However, the paper has several compounding weaknesses that place it below the Findings threshold:

1. The primary K_eff claim is fragile: within-tier analysis reduces significance from 7/12 to 2/18, indicating the effect is largely a tier-mixing artifact inadequately addressed by linear residualization. The effect size (partial η²=0.04) is small.

2. The novelty positioning is weak: the core mechanism (adaptive adversaries exploit weak links introduced by diversity) is predicted by the Condorcet Jury Theorem and established in the adversarial ensemble ML literature. The paper does not adequately engage with this prior work.

3. The practical contribution collapses: the proposed two-stage algorithm is statistically indistinguishable from "use the strongest judges" (p=0.42).

4. The BFT theoretical contribution is weakened by the absence of the predicted sign reversal.

5. Related work is too thin for the interdisciplinary scope of the paper.

**What would raise the score to 3.0–3.5 (Findings):**
- Address non-linear confounding with proper specification checks (GAM, polynomial, tier-indicator controls)
- Report practical effect magnitudes (predicted ASR change across K_eff range)
- Substantially expand related work: engage with CJT, Kariyappa & Qureshi 2019, Tramer et al. 2018, PoLL, security games
- Reframe title and contributions to match the evidence: "diversity is a conditional, small-effect amplifier in heterogeneous pools" rather than "diversity makes things worse"
- Either validate open-ended evaluation results or explicitly scope the paper to MCQ evaluation
- Provide attack implementation details (prompts, perturbation procedures)

**What would raise the score to 3.5–4.0 (Conference):**
- All of the above, plus:
- Demonstrate a residual K_eff effect after non-linear confound control (GAM, matching designs)
- Include instrumental variable or causal identification strategy
- Show results on open-ended benchmarks with adequate power
- Develop a non-trivial panel design algorithm that significantly outperforms Strongest-K

---

## Experiment Coverage Assessment

Comparing the paper against the imagined experiment list (12 plans):

| Plan | Coverage | Quality |
|------|----------|---------|
| plan_001: 15-model residualized regression | ✓ Full | Table 1 matches expected results closely |
| plan_002: Attack expansion (6+3 types) | ✓ Full | Table 2, Section 4.2 — 18 conditions covered |
| plan_003: BFT contrast | ✓ Full | Table 4, Section 4.4 — no sign reversal honestly reported |
| plan_004: Within-tier validation | ✓ Full | Table 3, Section 4.3 — 2/18 sig matches expected |
| plan_005: Two-stage benchmark | ✓ Full | Table 6, Section 4.7 — p=0.42 vs Strongest-K |
| plan_006: ASR concentration | ✓ Partial | Section 5.4, Gini=0.45 reported but limited detail |
| plan_007: Tradeoff decomposition | ✓ Full | Section 5.1, r=0.72, 72% between-tier |
| plan_008: Panel size sensitivity | ✓ Full | Section 4.5, K=3,5,7,9 |
| plan_009: VIF diagnostics | ✓ Full | Section 3.3, partial η² in 4.1 |
| plan_010: Aggregation rules | ✓ Full | Table 5, Section 4.6 |
| plan_011: Open-ended MT-Bench | ○ Partial | Section 6 only (limitations), not full results section |
| plan_012: Partial-knowledge adversary | ✓ Partial | Section 4.5, limited detail |

**Coverage: 10/12 full, 2/12 partial.** The paper covers the experimental design comprehensively. The two partial-coverage items (open-ended evaluation, partial-knowledge adversary) appear in appropriate sections (Limitations, When Diversity Helps) but lack the detail of full experimental write-ups.

---

## Summary for Research Director

**Bottom line:** The paper has strong experimental design and honest reporting but is undermined by a fragile primary claim (K_eff effect is largely tier-mixing artifact, η²=0.04), insufficient novelty positioning (CJT and adversarial ensemble ML predict the core finding), and a practical contribution that is statistically indistinguishable from the trivial baseline. Current assessment: **Borderline Findings (2.5)**. A revision addressing confounding methodology, related work expansion, and honest reframing of contributions could lift it to 3.0–3.5.


---

## 引用验证结果

**统计**: 29 篇文献 / 43 处引用 / 在线验证 29/29 篇

### 问题 (6)

- ⚠️ `almasoud2026security` — 元数据不匹配: first_author: bib=al masoud vs api=masoud
- ⚠️ `tramer2018ensemble` — 元数据不匹配: first_author: bib=tram\`er vs api=tramèr
- ⚠️ `schneier2000secrets` — 元数据不匹配: first_author: bib=schneier vs api=1963-
- ⚠️ `hendrycks2021mmlu` — 元数据不匹配: year: bib=2021 vs api=2025, first_author: bib=hendrycks vs api=son
- ⚠️ `jung2026logarithmic` — 在 .bib 中但正文未引用
- ⚠️ `zheng2024lmsyschat` — 在 .bib 中但正文未引用

### ✅ 通过 (25)