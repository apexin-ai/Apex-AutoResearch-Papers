---
dream_id: dream_20260517T032843
tier: best
overall_score: weak reject
timestamp: 2026-05-17T03:57:55.996348+00:00
---

# Dream Review Report: Phase-Dependent Compound Sparsity

**Paper:** Phase-Dependent Compound Sparsity: Reasoning Complexity Modulates the Severity of Pruning-Eviction Interactions  
**Review mode:** Full (2 reviewers, roundtable synthesis)  
**Venue standard:** Top ML venue, ~25% acceptance rate, 6-point scale

---

## 1. Paper Summary

This paper demonstrates that compound sparsity (simultaneous attention head pruning + KV cache eviction) produces phase-dependent, strategy-specific degradation during reasoning. Through controlled experiments on three benchmarks (GSM8K, MATH-500, GPQA Diamond) with three 7B-scale model architectures, the authors show that importance-based eviction exhibits a strong phase gradient (severity concentrated in high-perplexity phases) with perfect dose-response monotonicity (Spearman rho=1.0), while random and recency eviction produce null or negligible gradients (triple dissociation). The phase gradient magnitude scales with reasoning chain length (cross-benchmark Pearson r=0.997). The proposed mechanism is "discrimination collapse": head pruning degrades attention score discriminative power (Gini coefficient decline), causing importance-based eviction to degenerate in phases requiring long-range dependencies.

---

## 2. Reviewer Scores

| Criterion | R1 (Methods/Experiments) | R2 (Novelty/Related Work) | Consensus |
|---|---|---|---|
| Soundness / Novelty | 4/6 | 3/6 | 3.5/6 |
| Presentation | 4/6 | 4/6 | 4/6 |
| Contribution / Significance | 3/6 | 3/6 | 3/6 |
| Overall | 3/6 (Weak Reject) | 3/6 (Weak Reject) | **3/6 (Weak Reject)** |
| Confidence | 4/5 | 4/5 | 4/5 |

---

## 3. Roundtable Synthesis

### Step 2: Cross-Share Reactions

**R1 reacting to R2's novelty assessment:** R1 agrees that the core finding is an expected extension of ThinKV (phase-dependent single-axis) + SparK (compound super-additivity). R1 notes the recency control is the strongest novelty contribution, but concurs with R2 that "no precedent" claims are overclaimed since the experimental logic (mechanism-free baseline) is standard.

**R2 reacting to R1's methodology concerns:** R2 agrees that the phase segmentation validation (kappa=0.88 on n=48, GSM8K only, one model) is thin and should extend to MATH-500/GPQA. R2 endorses R1's concern that Spearman rho=1.0 on 4 ordered points is not particularly impressive and is over-emphasized in the Abstract.

### Step 3: Convergence

**Full agreement (high confidence):**

1. **Statistical rigor is a strength.** Paired design, Wilcoxon signed-rank, bootstrap CIs, Bonferroni correction, Jonckheere-Terpstra trend tests. Among the most statistically careful papers in this area.

2. **Triple dissociation design is well-motivated.** The recency control is a genuine methodological contribution that isolates score-dependent mechanisms.

3. **Transparency is commendable.** The paper honestly reports the pilot controller failure (18-32% recovery, CI spanning zero), acknowledges discrimination collapse is correlational, and provides a thorough limitations section.

4. **Discrimination collapse mechanism is insufficient.** Gini drops are near-identical for importance and random eviction, yet severity diverges 15-17x. The "structural specificity" argument (importance pruning removes low-Gini heads) is post-hoc and does not quantitatively account for the observed divergence. This is the paper's central explanatory gap.

5. **No practical method is proposed.** The paper is purely diagnostic. The phase-gated controller pilot failed to meet its own pre-registered gate (18% vs. 30% threshold). For a top venue, a characterization paper needs either a truly surprising finding or immediate actionable impact.

6. **7B-only limitation is real.** All three models are 7B-scale. Two share the Qwen2 backbone, so cross-architecture validation rests primarily on LLaMA-8B alone.

7. **Architecture dependence undermines generality.** The headline strategy specificity (15-17x) holds only for DeepSeek/Qwen2. On LLaMA, it drops to 2.0-2.6x. This order-of-magnitude difference makes it unclear which regime would generalize to other architectures or scales.

8. **Spearman rho=1.0 is over-emphasized.** With only 4 ordered sparsity levels, perfect rank correlation is not statistically impressive (high probability under any true monotone trend). Its prominent placement in the Abstract and contributions list may mislead.

**Partial agreement (moderate confidence):**

9. **Phase segmentation validity.** R1 raises stronger concerns about potential circularity (phases defined by attention sparsity, II measured under attention-based compression). The recency control partially addresses this, but both agree the validation scope (n=48, one model, one benchmark) is thin.

10. **Novelty is moderate.** R2 rates novelty lower (3/6) emphasizing that ThinKV+SparK+HIES already cover the component insights. R1 gives soundness 4/6 acknowledging the experimental design is methodologically sound even if the finding is expected. Consensus: the combination is new but not surprising.

---

## 4. Consolidated Strengths

- **Rigorous experimental design:** The three-way strategy comparison (importance/random/recency) with the recency control isolating score-dependent mechanisms is well-conceived and cleanly executed.
- **Statistical sophistication:** Paired nonparametric tests, bootstrap CIs, multiple comparison correction, dose-response trend tests, post-hoc power analyses. The paper practices what it preaches about rigorous characterization.
- **Honest self-assessment:** The paper explicitly concedes the mechanism is correlational, the pilot controller failed, architecture dependence exists, and GSM8K is underpowered. This transparency is rare and valuable.
- **Clean metric:** The Interaction Index decomposition by phase is a reusable diagnostic framework that others can apply.
- **Consistent cross-model replication:** The within-importance phase gradient (d_z = 0.81-1.15) is robust across all three architectures, establishing the phenomenon's existence.

---

## 5. Consolidated Weaknesses

- **W1 (Critical): No practical method.** The paper identifies a problem but provides no solution. The pilot controller failed its own pre-registered efficacy gate. A top venue characterization paper needs either a surprising finding or actionable impact; this paper's core finding (compound severity is phase-dependent) is predictable from prior single-axis work.

- **W2 (Major): Mechanism is admittedly insufficient.** Discrimination collapse (Gini decline) explains the direction but not the magnitude. Near-identical Gini drops across strategies with 15-17x severity divergence leaves the mechanism's explanatory power unclear. The paper correctly identifies this gap but does not resolve it.

- **W3 (Major): Architecture dependence.** Strategy specificity varies by nearly an order of magnitude across architectures (2.0-2.6x LLaMA vs. 15-17x Qwen2-family). The GQA vs. MHA hypothesis is plausible but untested. This makes the headline numbers difficult to generalize.

- **W4 (Major): Scale limitation.** All models are 7B. Two of three share the Qwen2 backbone. No evidence that findings transfer to 13B/70B+ scales relevant for deployment. The Discussion mentions 14B experiments but no results are presented.

- **W5 (Moderate): Phase segmentation validation is thin.** Validated only on GSM8K (n=48, one model, kappa=0.88). The main claims rest on MATH-500 and GPQA, where no segmentation validation exists. Tercile boundaries are arbitrary (quartile/quintile robustness checked only at n=50).

- **W6 (Moderate): Overstated statistics.** Spearman rho=1.0 on 4 points and Pearson r=0.997 on 3 benchmarks are featured prominently but lack statistical power for strong inference. These numbers sound impressive but carry limited information.

- **W7 (Minor): Related work gaps.** H2O is the foundation of the importance scoring mechanism used throughout but is never properly introduced in Related Work. DefensiveKV deserves more discussion given overlapping insights. Some citations appear as [?] placeholders.

- **W8 (Minor): Symmetric sparsity only.** Equal head pruning and KV eviction rates are not realistic deployment configurations. The paper acknowledges this but the limitation reduces practical relevance.

---

## 6. Questions for Authors

1. The Gini drop is near-identical for importance and random strategies, yet severity diverges 15-17x. The "structural specificity" argument restates the observation rather than explaining it. Have you attempted any mediation analysis or causal path model that quantitatively connects Gini decline to the observed severity ratio?

2. The strategy specificity drops from 15-17x (DeepSeek/Qwen2) to 2.0-2.6x (LLaMA). Under what conditions should a practitioner expect the larger vs. smaller ratio? Can you provide a predictive criterion (e.g., based on attention head configuration)?

3. How would a practitioner implement phase-gated compression without access to the dense model's attention patterns for phase segmentation? The oracle phase assignment used in experiments is not available at deployment time.

4. The pilot controller achieved 18% recovery (CI spanning zero). Does this suggest the phase gradient, while statistically real, is too small in absolute terms to be practically exploitable? What recovery level would be needed for deployment relevance?

5. Have you tested under asymmetric sparsity (e.g., 30% head pruning + 10% KV eviction)? Deployment configurations rarely use equal compression rates.

6. The phase segmentation validation (kappa=0.88) was on GSM8K only (n=48, short chains). Can you provide validation on MATH-500 or GPQA where reasoning chains are 5-12x longer and phase boundaries may be less distinct?

7. With only 4 sparsity levels, Spearman rho=1.0 is not very informative. Would you consider a finer-grained sparsity sweep (e.g., 8-10 levels) to establish the dose-response shape more convincingly?

---

## 7. Overall Assessment

**Score: 3/6 (Weak Reject)**

This is a methodologically careful empirical study that identifies a real phenomenon (phase-dependent compound sparsity severity) and characterizes it rigorously across multiple conditions. The statistical framework is exemplary, the triple dissociation design is well-motivated, and the paper is unusually transparent about its limitations.

However, the paper faces several barriers to acceptance at a top venue:

(a) The core finding (compound severity varies by phase) is an expected extension of known single-axis phase dependence (ThinKV) combined with known compound super-additivity (SparK). The novelty is in the specific combination and quantification, not in a surprising insight.

(b) The proposed mechanism (discrimination collapse) is acknowledged as correlational and fails to explain the magnitude of observed effects (15-17x divergence despite near-identical Gini drops).

(c) No practical method is proposed. The pilot phase-gated controller failed its own efficacy gate (18% recovery, CI spanning zero), leaving the contribution purely diagnostic.

(d) Architecture dependence (order-of-magnitude variation in headline numbers) and scale limitation (7B only) weaken generalizability.

The paper would be strengthened by: (1) a working phase-aware compression method, (2) a mechanistic explanation that accounts for the 15-17x divergence quantitatively, (3) validation at 13B+ scale, and (4) resolution of the architecture-dependent specificity question.

**Recommendation:** Weak Reject. The empirical characterization is solid but incremental, the mechanism is unsatisfying, and the absence of a practical contribution limits significance. If the authors can demonstrate a working phase-gated controller with meaningful recovery AND provide scale validation, this could become a borderline accept.
