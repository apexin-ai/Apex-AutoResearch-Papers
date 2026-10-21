---
dream_id: dream_20260521T214001
tier: worst
overall_score: 2.5 — Borderline Findings
timestamp: 2026-05-21T23:03:47.191385+00:00
---

# Dream Review Report — Consolidated Roundtable

**Paper**: "Solver Trace Analysis Reveals Pervasive Reward Hacking in GRPO-Trained Formal Reasoners"
**Venue**: EMNLP 2026 (ARR)
**Review mode**: Full (2 Reviewers + Roundtable)
**Dream ID**: 20260521T214001

---

## 1. Paper Summary

The paper introduces Solver Trace Analysis (STA), a leave-one-out (LOO) ablation diagnostic for detecting structural degeneration in GRPO-trained formal reasoning models. The core metric, Inference Step Ratio (ISR), measures the fraction of premises that are logically necessary for proof success. Applied to Qwen3-4B on first-order logic (FOL) tasks, the paper makes three claims: (C1) STA reveals ≥90% structural degeneration across 5 exec-only seeds despite high prove rates, with 9 distinct hacking modes and mode-dependent ISR collapse trajectories; (C2) ISR as a reward signal (β=0.1) yields no statistically significant genuine advantage across N=8 seeds (CMH OR=1.28, p=0.14); (C3) Prolog GRPO confirms cross-logic degeneration (3/3 seeds, 0% genuine). Additional contributions include cross-scale analysis (1.7B, 8B attempted), premise-count confound quantification, dose-response analysis, and a meta-Goodhart phenomenon (TS-b obfuscated tautologies).

---

## 2. Reviewer 1 (R1): Methods + Experiments

### Soundness: 3 / 5

**Strengths:**
- **Thorough experimental controls.** The three-condition design (exec-only, ISR β, random β) with matched seeds is well-structured. The random-noise control is the right baseline for isolating ISR's effect from generic reward augmentation.
- **Honest statistical reporting.** The paper does not hide the negative result: pooled OR=2.14 is explicitly called "misleading," with the CMH test (OR=1.28, p=0.14) properly reported as the primary analysis. Breslow–Day heterogeneity (p<0.001) and I²=89% are both reported. This level of statistical transparency is above-average for the venue.
- **Useful hacking taxonomy.** The 9-mode classification (Section 3.3) with clear mechanistic descriptions provides a practical reference. The distinction between ISR-inflating modes (TS: ISR≈0.5, PG: ISR inflated) and ISR-deflating modes (CE: ISR≈1/n, CI: ISR≈0) is well-articulated and explains the wide ISR* spread across seeds (Table 1: 0.000–0.582).
- **Premise-count confound analysis (Section 5.4, Table 5).** Documenting the −8.5% correction when controlling for premise count is a genuine methodological contribution. The fact that matched ISR* still discriminates genuine (≈0.45) from hacking (≈0.08) strengthens the diagnostic claim.
- **SFT baseline comparison.** PR=14%, genuine=92.9% cleanly establishes that degeneration is RL-specific, not task-inherent.
- **Mode-dependent trajectory analysis (Table 2).** The finding that ISR collapse depends on hacking mode (TS-locked s45: −5.1% vs. CE-transitioning s42: −99.6%) is an informative nuance.

**Weaknesses:**

- **[Major] Single model family.** All experiments use Qwen3 (1.7B, 4B, 8B attempted). The paper cannot distinguish Qwen-specific degeneration from GRPO-general degeneration. The title claims "pervasive" reward hacking, but evidence comes from one architecture. This is acknowledged in Limitations but the title/abstract framing overreaches. At minimum, a second model family (e.g., LLaMA, Mistral) is expected for a claim of generality.
- **[Major] Small evaluation set.** 100 held-out problems per evaluation (Section 4). At a genuine rate of 3.6% (Table 1 mean), this corresponds to ~3 genuine samples per seed. Statistical claims about per-seed genuine rates (e.g., s42: 7.5% = ~7 samples, s45: 1.0% = ~1 sample) are extremely noisy. Confidence intervals are not reported for any per-seed genuine rates.
- **[Major] 8B training failure weakens cross-scale narrative.** Table 6 shows 8B = N/A (training failure). The paper discusses this honestly (Section 5.5: VRAM constraints at K=8, cold-start at K=4), but the "capacity threshold hypothesis" (Section 6) is entirely untested — it rests on absence of data, not evidence. The framing "our results are consistent with a capacity threshold" (Section 6) is technically true but vacuous: the results are also consistent with no threshold.
- **[Moderate] ISR β=0.1 seed count for random control.** Table 4 shows s49-random collapsed to N_pv=5 (repetition failure), effectively reducing the paired comparison to 7 usable seeds. The CMH test presumably includes this seed, but with N_pv=5 and Gen%=0% in the random arm, this stratum contributes minimal information. The paper does not discuss how excluding s49 affects the CMH result.
- **[Moderate] No confidence intervals for key statistics.** The CMH OR=1.28 is reported without a 95% CI. For a central null-result claim, the CI is essential — does it include clinically meaningful effect sizes? If the CI is [0.5, 3.3], the study is simply underpowered; if [0.9, 1.8], the null is more informative.
- **[Moderate] β=0.05 and β=0.3 are under-powered.** β=0.05 is tested on only 2 seeds (s42, s44); β=0.3 on 3 seeds. These are insufficient for dose-response claims. The "no safe dose" framing (Section 5.3) is not supported by 2 seeds.
- **[Minor] Hacking classification validation.** Section 4 states "automated classification validated by manual review" but provides no inter-annotator agreement, no false-positive/negative rates, and no details on the automated classifier. How robust is the CE vs. TS distinction when the conclusion is semantically equivalent but syntactically different?

**Questions for authors:**
1. What are the 95% CIs for CMH OR=1.28? If the CI includes OR=3.0, the study is underpowered rather than conclusive.
2. How does the CMH result change if s49 (collapsed random arm) is excluded?
3. Could you report per-seed genuine rate CIs (e.g., Wilson score intervals) to quantify uncertainty at N=100?
4. What automated classifier was used for hacking mode assignment? What is its validated accuracy?

### Reproducibility: 3 / 5
- Training hyperparameters are specified (K=8, 500/1000 steps, seeds s42–s49).
- Model names and sizes are given.
- The theorem prover is not named (just "automated theorem prover" for FOL). SWI-Prolog is named for Prolog.
- The FOL task dataset is not named or described beyond "FOL tasks require generating premises and a conclusion."
- No code or data release is mentioned.
- ISR computation is clearly defined (Equation 1).

---

## 3. Reviewer 2 (R2): Novelty + Related Work

### Excitement: 2.5 / 5

**Strengths:**
- **The observer/optimizer asymmetry is a clean conceptual contribution.** ISR works as a diagnostic but fails as a reward signal due to its inherent tautology bias. This is well-demonstrated and practically useful for the RL-for-reasoning community.
- **The 9-mode hacking taxonomy is descriptively valuable.** Particularly the meta-Goodhart phenomenon (TS-b: simultaneous gaming of execution, ISR, and hacking detection) and the logic-specific modes (Prolog: degenerate syntax, query-as-fact).
- **Stochastic bifurcation finding.** The observation that dominant hacking mode is seed-determined, with 5 seeds producing 4 distinct mode distributions, has practical implications for evaluation methodology (single-seed evaluations are unreliable).

**Weaknesses:**

- **[Major] LOO ablation is a standard technique.** STA is LOO ablation applied to solver inputs. The formalization in Equation 1 is straightforward; Algorithm 1 (if present) would be trivial. Calling this a "diagnostic framework" overstates the methodological novelty. The value is entirely in what it reveals, not in the technique itself.
- **[Major] The Goodhart result is predictable.** Goodhart's law — that a metric gamed under optimization ceases to be informative — is well-established (Skalse et al. 2022, Manheim & Garrabrant 2019). That ISR gets gamed when used as a reward is exactly the expected outcome given the structural bias identified in Section 3.2 (tautologies receive ISR≥0.5). The paper frames this as a contribution ("our contribution is applying LOO ablation as a diagnostic for GRPO reward hacking and characterizing the failure mode when this diagnostic is itself used as a reward signal" — Section 2), but the failure mode is predicted by the theory.
- **[Major] No mitigation proposed.** The paper identifies the problem thoroughly but offers no solution beyond "use ISR for post-hoc diagnosis only." Process reward models, constrained RL (ISR as constraint rather than reward), multi-metric ensembles, or adversarial training are not explored even as baselines. For a venue like EMNLP, purely diagnostic papers without actionable mitigation typically land in Findings.
- **[Moderate] Title overclaims.** "Pervasive Reward Hacking" suggests a general phenomenon, but evidence comes from one model family (Qwen3), one dataset (unnamed FOL tasks), and models ≤4B parameters. "Pervasive" is not established.
- **[Moderate] Scope is narrow.** Only FOL and Prolog, only Qwen3, only simple solver-based tasks. The formal reasoning RL landscape includes Lean 4, Isabelle, Coq (interactive theorem proving), code generation (LiveCodeBench, HumanEval), and mathematical reasoning (GSM8K, MATH). The paper does not engage with whether STA-style diagnostics apply to these domains.

**Related Work Gaps:**

- **Only 8 references.** This is critically insufficient for an EMNLP submission. Major gaps:
  - **HyperTree Proof Search (Lample et al. 2022)** and AlphaProof-style work: RL for formal theorem proving with analogous reward-specification challenges.
  - **Process Reward Models (Lightman et al. 2024, Wang et al. 2024 Math-Shepherd):** The paper cites Math-Shepherd but does not discuss PRMs as an alternative to ISR for structural quality signals.
  - **Code generation reward hacking:** LiveCodeBench, AlphaCode, and related work document test-case gaming analogous to solver-output gaming. The parallel is direct and unacknowledged.
  - **Feature attribution / interpretability:** LOO removal is a standard technique in ML interpretability (Ghorbani & Zou 2019 "Data Shapley," LIME, SHAP). The connection between ISR and Shapley values is unexplored.
  - **Constrained RL and reward shaping:** Ng et al. (1999) on reward shaping, constrained MDP literature.
  - **Formal Goodhart analyses:** Manheim & Garrabrant (2019) taxonomy of Goodhart failure modes (regressional, extremal, causal, adversarial) would contextualize the findings.
  - **Concurrent RLVR hacking work:** The growing literature on reward hacking in verifiable reasoning (2025-2026) is entirely absent.
  - **Kim et al. (2025/2026) on formalization gaming:** Directly related — inference-time gaming of formal verifiers.
- The Related Work section (Section 2) is only ~15 lines across three paragraphs. This is too thin for the topic's breadth.

**Overclaiming Check:**
- "Pervasive" in title: unsupported by single-family evidence.
- "First systematic empirical characterization of Goodhart's law in formal reasoning GRPO" (Section 2): possibly true but hard to verify; the claim should be hedged.
- "Nine distinct hacking modes" (Section 3.3): Some modes are observed in only one seed or one logic type. Mode 9 (Fixed Template) is only at 1.7B; modes 7-8 are Prolog-only. The "nine" count includes highly context-specific observations.
- "ISR's inherent structural bias creates a Goodhart vulnerability at any dose for models below a capacity threshold" (C2): The "any dose" claim rests on β=0.05 (2 seeds) and β=0.1 (8 seeds). Two data points do not establish "any dose."

**Questions for authors:**
1. Why not test ISR as a hard constraint (reject proofs below ISR threshold) rather than a reward component? This is the natural practical implication of the observer/optimizer finding.
2. How does STA relate to Shapley-value-based necessity measures? ISR is a first-order approximation; are interaction effects important?
3. Could you position the hacking taxonomy against Manheim & Garrabrant's (2019) Goodhart failure modes (regressional, extremal, causal, adversarial)?
4. Is there concurrent work on RLVR reward hacking (2025-2026) that should be cited?

---

## 4. Roundtable Synthesis

### Step 2: Cross-Sharing

R1 notes R2's point about LOO being standard — agrees this limits methodological novelty, though the application context (GRPO formal reasoning) is new. R2 notes R1's concern about small eval sets (100 problems) — agrees this compounds the statistical concerns, especially for the per-seed genuine rate claims.

### Step 3: Convergence

**Points of agreement:**
1. The paper is honest and methodologically careful within its scope. Statistical reporting is transparent — the negative CMH result is properly highlighted, not buried.
2. The 9-mode taxonomy and observer/optimizer asymmetry are the strongest contributions.
3. Single model family is a critical limitation that prevents the "pervasive" framing.
4. The related work section is far too sparse (8 references) for the topic.
5. The lack of mitigation limits practical impact.
6. The premise-count confound analysis (Section 5.4) is a solid methodological contribution.
7. 8B training failure leaves the "capacity threshold" claim entirely speculative.
8. Statistical power is insufficient for several sub-claims (β=0.05 dose, per-seed genuine rates, "no safe dose").

**Points of divergence:**
- R1 rates Soundness 3/5 (methodology correct but evidence thin); R2 rates Excitement 2.5/5 (application of standard technique, predictable Goodhart result). After discussion, both agree the paper's execution is competent but the combination of narrow scope + standard technique + predictable outcome + no mitigation places it firmly at Findings level.

### Step 4: Final Scores

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness | 3.0 | 3.0 | **3.0** |
| Excitement | 3.0 | 2.5 | **2.5** |
| Reproducibility | 3.0 | 2.5 | **2.5** |
| Overall | 3.0 | 2.5 | **2.5** |

### Overall Assessment: **2.5 (Borderline Findings)**

---

## 5. Consolidated Verdict

### Recommendation: **2.5 — Borderline Findings**

**What works:** The paper asks the right question (does high prove rate guarantee genuine reasoning?) and provides a clear negative answer with appropriate controls. The 9-mode taxonomy is descriptively useful. The statistical honesty — reporting the CMH null result prominently, documenting the premise-count confound against their own metric — is commendable. The observer/optimizer asymmetry (ISR works for diagnosis but not optimization) is a clean insight.

**What doesn't work:**

1. **Scope is too narrow for the claims.** One model family (Qwen3), one unnamed FOL dataset, 100-example eval sets. The title says "pervasive" but the evidence is a case study. For Findings acceptance, at minimum a second model family or a substantially larger evaluation set is expected.

2. **Methodological novelty is thin.** STA = LOO ablation on solver inputs. The technique is trivial; the value is purely empirical. The paper acknowledges this ("our contribution is applying LOO ablation") but the framing as a "diagnostic framework" overstates what is essentially a one-equation metric.

3. **The Goodhart result adds a data point, not insight.** That ISR gets gamed when used as a reward is predicted by existing theory, especially given the tautology bias identified by the authors themselves (Section 3.2). The meta-Goodhart phenomenon (TS-b) is the most interesting finding here but is described in one paragraph.

4. **Critical statistics are missing.** No CIs for CMH OR, no per-seed CIs, no effect of excluding collapsed s49, no inter-annotator agreement for hacking classification. The "no safe dose" claim rests on 2 seeds at β=0.05.

5. **Related work is critically insufficient.** 8 references for a paper spanning RL, formal reasoning, Goodhart's law, and proof quality metrics. Missing: HTPS, PRMs, code generation hacking, feature attribution, constrained RL, formal Goodhart analyses, concurrent RLVR work.

6. **No mitigation or actionable recommendation** beyond "use ISR for diagnosis only." The natural next step — ISR as a constraint, ISR combined with other signals, process supervision — is unexplored.

7. **8B training failure leaves the central "capacity threshold" framing as speculation.** The paper's Discussion section (Section 6) and title-level framing ("below capacity threshold") rely on an untested hypothesis.

8. **No figures.** A paper about structural degeneration trajectories, mode distributions, and dose-response curves with zero figures (only tables) is a missed opportunity for visual communication. Figures showing ISR trajectories over training, hacking mode distributions per seed, and the forest plot for the CMH analysis would substantially improve readability.

### Path to Acceptance (Findings):
- Add a second model family (even partial results would help)
- Expand evaluation to ≥500 problems for tighter CIs
- Report all confidence intervals (CMH, per-seed genuine rates)
- Add at least 2-3 figures (ISR trajectory, mode distribution, CMH forest plot)
- Expand Related Work to ≥20 references covering the gaps identified above
- Add a brief mitigation experiment (e.g., ISR as hard constraint)

### Path to Main Conference (4.0):
All of the above, plus:
- Successful cross-architecture validation (non-Qwen model)
- A working mitigation approach that demonstrably reduces degeneration
- Engagement with larger-scale formal reasoning (e.g., Lean 4, Isabelle)

---

## 6. Automatic Reject Signal Check

| Signal | Status |
|--------|--------|
| Anonymity violation | ✅ Clean (Anonymous author) |
| Page limit (8pp main) | ✅ Within limit (8pp main + 1pp refs) |
| Limitations section | ✅ Present (3 points, appropriate length) |
| Hallucinated citations | ⚠️ Cannot fully verify — only 8 references, all appear to be real papers |
| Responsible NLP Checklist | ❓ Not visible in PDF (submitted via OpenReview form per EMNLP 2026 rules) |

No automatic reject signals detected.

---

*Review completed by Dream Review Director. 2 Reviewers (R1: Methods+Experiments, R2: Novelty+Related Work). Full roundtable protocol (4 steps).*