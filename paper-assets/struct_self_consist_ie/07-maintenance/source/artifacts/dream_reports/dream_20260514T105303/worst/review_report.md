---
dream_id: dream_20260514T105303
tier: worst
overall_score: 3 — Weak Reject
timestamp: 2026-05-14T12:06:37.830742+00:00
---

# Dream Review Report

**Paper**: "Log-Probability Is All You Need? A Systematic Evaluation of Confidence Signals for Test-Time Scaling in Structured Information Extraction"

**Review Mode**: Full (2 Reviewers, complete roundtable)
**Venue Standard**: Top ML venue, ~25% acceptance, 6-point scale

---

## Roundtable Summary

### Step 1: Independent Reviews

---

### Reviewer 1 — Methods & Experiments

#### Strengths

**S1. Comprehensive signal comparison with consistent protocol.** Five confidence signal families (log-prob, SJ, FK, exact-match, entity voting) are evaluated under identical conditions across all datasets and models. This ensures fair comparison and prevents cherry-picking (Tables 1–12).

**S2. Multi-axis evaluation prevents metric bias.** Using Spearman ρ, AUROC, Kendall τ, ECE, and downstream best-of-N F1 (Tables 2–4) is commendable. Notably, the AUROC gap (0.72 vs 0.63, Δ=+0.09; Table 2) is larger than the ρ gap (0.41 vs 0.38, Δ=+0.03), revealing that log-prob's advantage is more pronounced in binary good/bad discrimination than in full ranking — a nuance that single-metric studies would miss.

**S3. Thorough robustness checks.** LOO-SJ for circularity (Table 2: ρ=0.36 vs 0.38, Δ=−0.02), multi-seed N=16 (Table 5: σ=0.012), cross-model validation (Table 8: Qwen3 vs LLaMA), temperature sensitivity (Table 9: T=0.7 vs 1.0), OOD evaluation (Table 12), and difficulty stratification (Table 11) collectively rule out many alternative explanations for the negative result.

**S4. Diagnostic depth in RE analysis.** Per-relation-type breakdown (Table 7) — showing semantically ambiguous relations (Compare ρ=0.14, Hyponym-of ρ=0.16) as main failure sources — and full vs conditional evaluation with bootstrap CIs (Table 6) go beyond surface-level reporting.

**S5. Good experiment coverage.** Approximately 13 of 15 planned experiments are represented. The selection curves (exp-010) figure is absent but the underlying data is partially captured in Section 5.5.

#### Weaknesses

**W1 [Major]. Log-prob definition ambiguity in best-of-N context.** Eq. 1 defines c_lp(x) as the normalized log-probability of the *greedy output* y₀ only. However, Table 4 shows "log-prob selection" achieving 69.2 F1 vs greedy 66.2 on SciERC NER — implying selection among multiple candidates using their individual generation log-probabilities. If each sample's log-prob is used for ranking (the natural interpretation for best-of-N), this must be stated explicitly in Section 3.2. The current text leaves readers uncertain whether log-prob scores a single output or ranks among N candidates.

**W2 [Major]. Misleading cost comparison in Table 4.** Log-prob is listed at "0× extra cost" vs consistency methods at "N×". If log-prob selection ranks among N candidates, it also requires N forward passes for generation; the only savings is in the ranking computation (free byproduct vs O(N² × matching) for SJ). Presenting this as "0× vs N×" vastly overstates the practical cost advantage. A fairer representation: "All best-of-N methods require N forward passes; log-prob adds zero ranking overhead while consistency methods add pairwise comparison cost." Alternatively, if log-prob truly uses only the greedy output (as Eq. 1 states), it is not doing best-of-N selection and should not be in the same table.

**W3 [Major]. Only 8B-parameter models tested.** Both Qwen3-8B and LLaMA-3.1-8B are 8B-scale. Larger models (70B+) are known to have improved calibration properties, which could narrow or reverse the log-prob vs consistency gap. This limitation significantly weakens the generalizability of the central claim.

**W4 [Major]. RE evaluated on a single dataset.** The "task-complexity boundary" (Claim 2) rests entirely on SciERC RE. Testing on ACE05, TACRED, or DocRED would substantially strengthen this finding. Without additional RE datasets, the claim is about SciERC RE specifically, not about relation extraction or structured prediction complexity in general.

**W5 [Major]. Complete absence of figures.** The 10-page PDF contains 12 tables and zero figures. Key visualizations from the experiment plan are missing:
- Selection curves (F1 vs N for each signal with oracle ceiling) — arguably the paper's most compelling potential visual
- Reliability diagrams (calibration plots for log-prob vs SJ)
- Cost-effectiveness scatter (F1 gain vs inference cost multiplier)
- N-scaling line plots, SJ distribution histograms

For a venue like EMNLP, this is a significant presentation weakness. Even 2–3 figures would dramatically improve readability and persuasiveness.

**W6 [Minor]. Statistical testing inconsistency.** Table 1 reports p-values for Δ(SJ−LP) without specifying the test used (paired permutation? bootstrap? Steiger's z for comparing dependent correlations?). Table 6 provides bootstrap CIs, but Tables 2–5, 7–12 do not. A paper making quantitative comparison claims needs consistent statistical reporting.

**W7 [Minor]. Narrow temperature range.** Only T=0.7 and T=1.0 are tested (Table 9). Lower temperatures (T≤0.5) where samples are near-deterministic, and higher temperatures (T≥1.2) with greater diversity, could reveal qualitatively different dynamics for consistency methods.

**R1 Preliminary Score: 3 (Weak Reject)**

---

### Reviewer 2 — Novelty & Related Work

#### Strengths

**S1. Well-motivated, practically relevant research question.** "Does multi-sampling consistency provide information beyond what log-probability already encodes?" is directly useful for practitioners deciding whether to invest in multi-sampling infrastructure for IE. The cost-effectiveness framing gives clear, actionable guidance.

**S2. Appropriate "systematic negative result" positioning.** The paper correctly identifies its contribution pattern. EMNLP has a track record of accepting high-information negative results in calibration/evaluation tracks when they reveal under-examined assumptions.

**S3. Three-tier finding hierarchy is well-structured.** (1) Log-prob dominates NER, (2) task-complexity boundary on RE, (3) SJ best within consistency — each claim has clear scope and is separately supported. The hierarchy from strong (Claim 1) to moderate (Claim 3) is appropriate.

**S4. Useful failure mode taxonomy.** Section 6.2 identifies three distinct failure modes — ceiling effect (CoNLL: mean SJ=0.84), floor/hallucination consistency (WNUT: 31.5% F1=0), and compound error (RE) — providing conceptual vocabulary that extends beyond this specific study.

**S5. Clear practical recommendation.** "Start with log-prob as default; only invest in multi-sampling when log-prob is unavailable" (Section 7) is concrete and directly implementable.

#### Weaknesses

**W1 [Major]. Negative result is partially predictable.** For fine-tuned models, log-probability is a direct reflection of the learned output distribution. That it correlates well with output quality is essentially what calibration means. The paper needs to explicitly address why this finding is non-obvious — e.g., by discussing that self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023) and articulating why structured prediction might fundamentally differ.

**W2 [Major]. Related work is critically incomplete.** All citations appear as "?" placeholders — a fundamental submission readiness issue. Beyond formatting, substantive references appear to be missing:
- **Calibration fundamentals**: Guo et al. 2017 (On Calibration of Modern Neural Networks); Kadavath et al. 2022 (Language Models (Mostly) Know What They Know)
- **TTS scaling theory**: Snell et al. 2024 (Scaling LLM Test-Time Compute Optimally); Brown et al. 2024 (Large Language Monkeys)
- **Self-consistency variants**: Li et al. 2023 (Making Language Models Better Reasoners with Step-Aware Verifier); Aggarwal et al. 2023
- **Structured prediction confidence**: Culotta & McCallum 2004 (Confidence Estimation for IE); CRF-based confidence methods
- **Semantic uncertainty**: Kuhn et al. 2023 is mentioned but the distinction from the current work deserves deeper discussion

The Related Work section (Section 2) is only 4 brief paragraphs for a paper whose primary contribution is empirically challenging prior assumptions — this needs substantial expansion.

**W3 [Major]. "Diagnostic framework" is overclaimed.** The Abstract and Conclusion claim to provide "a diagnostic framework for assessing confidence signal effectiveness as a function of task complexity." In practice, Section 6.2 offers three post-hoc observations (ceiling, floor, compound error) without:
- Formal definitions of when each failure mode activates
- Metrics to predict *a priori* which mode applies to a new task
- Procedures for practitioners to apply the framework
This is descriptive analysis, not a reusable framework. Either develop it into a true framework or soften the claim.

**W4 [Moderate]. Generalizability narrower than framing suggests.** The title ("Log-Probability Is All You Need?") and abstract imply broad applicability, but findings are specific to:
- Fine-tuned 8B LLMs (not in-context learning, not API models without logprob access)
- Text-to-structure generation paradigm (not span-based or encoder-only NER)
- LoRA fine-tuning specifically (full fine-tuning may yield different calibration)
The Limitations section acknowledges model size and IE paradigm constraints but the title/abstract framing remains overreaching.

**W5 [Moderate]. No discussion of when consistency WOULD help.** The paper is entirely one-sided. A stronger contribution would identify or hypothesize conditions under which consistency should outperform log-prob: models with poor calibration, in-context learning without fine-tuning, closed-source APIs, ensemble/mixture settings, or tasks where the model is systematically overconfident. Section 6.3 briefly mentions "applications where log-probability is unavailable" but this deserves much more space.

**W6 [Moderate]. Claim 2 under-supported by single RE dataset.** "Task-complexity boundary" is a general claim supported by one dataset (SciERC RE). Extending to ACE05, TACRED, or even event extraction would validate the generality. As stated, the finding is about SciERC RE, not about "task complexity" broadly.

**W7 [Minor]. No theoretical grounding for the main finding.** Section 6.1 provides intuitive explanations ("the softmax distribution over tokens implicitly reflects the model's certainty") but no formal analysis. Even a simple argument — e.g., log-prob captures all token-level uncertainty while SJ discards information through set-level aggregation — would strengthen the paper's explanatory contribution.

**W8 [Minor]. Discussion section under-explores implications.** Section 6 is 1.5 pages for 3 subsections. The "Why Does Log-Prob Win?" analysis (6.1) could go deeper with information-theoretic framing. "When Does Consistency Fail?" (6.2) could connect to calibration theory. "SJ as Best-Practice Consistency" (6.3) could discuss API-only scenarios more thoroughly.

**R2 Preliminary Score: 3 (Weak Reject)**

---

### Step 2: Cross-Sharing

**R1 → R2**: The log-prob definition ambiguity (Eq. 1 vs best-of-N usage) is not just a methodological issue — it also affects how the novelty claim is interpreted. If log-prob selection truly requires zero sampling, the comparison with consistency methods is fundamentally asymmetric (one-pass vs multi-pass), which is less surprising as a result. The complete absence of figures weakens all three claims and makes the paper harder to evaluate.

**R2 → R1**: The predictability of the negative result for fine-tuned models lowers the effective novelty even if the experimental execution is solid. The incomplete related work (especially missing calibration and TTS scaling references) means the paper doesn't adequately contextualize what is already known about log-prob as a confidence signal. The "diagnostic framework" overclaim should be noted as both a novelty and a presentation issue.

---

### Step 3: Convergence

Both reviewers converge on the following assessment:

**Agreements:**
1. The research question is well-motivated and practically relevant
2. Experimental execution is competent within its scope, with good robustness checks
3. The paper has four convergent major issues:
   - (a) Log-prob usage ambiguity between Eq. 1 and best-of-N (methods clarity)
   - (b) Only 8B models + single RE dataset limit generalizability
   - (c) Incomplete related work and placeholder citations (submission readiness)
   - (d) Zero figures despite data-rich results (presentation)
4. Contribution level is below Main conference threshold; potentially suitable for Findings with revisions
5. The "diagnostic framework" claim needs to be either developed or softened

**Nuances:**
- R1 places more weight on the cost comparison misrepresentation (Table 4), seeing it as potentially misleading for practitioners
- R2 places more weight on novelty (partially predictable finding for fine-tuned models) and scholarly context (missing references)
- Both agree the paper's core finding is correct and useful, but insufficiently novel and incomplete in presentation for a top venue main track

---

### Step 4: Consolidated Assessment

**Overall Score: 3 — Weak Reject**

**Summary:** The paper presents a systematic empirical comparison of five confidence signals for test-time scaling in structured information extraction. The core finding — that log-probability matches or exceeds multi-sampling consistency methods on NER while requiring no additional inference — is well-supported within the evaluated scope and practically useful. However, the paper falls below the acceptance threshold for a top ML venue due to: (1) limited novelty (the negative result is partially predictable for fine-tuned models), (2) critical presentation gaps (no figures, placeholder citations, ambiguous log-prob definition), (3) insufficient scope for its claims (8B models only, single RE dataset), and (4) an overclaimed "diagnostic framework" that is descriptive rather than prescriptive.

**Recommendation:** Revise and resubmit, targeting EMNLP Findings as a realistic floor. Priority revisions:

| Priority | Issue | Action Required |
|----------|-------|----------------|
| P0 | Placeholder citations ("?") | Complete all references before any submission |
| P0 | Log-prob ambiguity | Clarify Eq. 1 vs best-of-N usage; fix Table 4 cost column |
| P1 | No figures | Add ≥3 figures: selection curves, reliability diagram, cost-effectiveness scatter |
| P1 | Related work | Expand Section 2 to ≥1.5 pages; add calibration, TTS scaling, structured prediction confidence references |
| P2 | RE scope | Add ≥1 additional RE dataset (ACE05 or TACRED) |
| P2 | "Diagnostic framework" | Either formalize with a priori metrics/procedures or reframe as "diagnostic analysis" |
| P3 | Model scale | Discuss or experiment with ≥1 larger model (70B); alternatively, explicitly scope claims to 8B-class |
| P3 | Statistical reporting | Specify tests consistently; add bootstrap CIs to all main tables |

**Experiment Coverage:** 13/15 planned experiments are covered in the paper. Notable gap: selection curves (exp-010) — the N vs F1 line plot is described in the experiment plan as "one of the most intuitive visualizations" but is completely absent. RE N=16 confirmation (exp-008) is mentioned in text but lacks a dedicated table.

**What Would Change the Score:**
- **To 4 (Borderline):** Fix P0 issues, add 2–3 key figures, expand related work, clarify cost comparison
- **To 5 (Weak Accept):** Additionally add ≥1 RE dataset, formalize the diagnostic framework, include a larger model or explicitly scope all claims
- **To 2 (Reject):** If the log-prob ambiguity turns out to be a genuine methodological flaw (i.e., the comparison is fundamentally unfair)
