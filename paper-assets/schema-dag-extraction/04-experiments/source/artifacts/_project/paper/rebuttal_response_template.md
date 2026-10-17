# ARR Rebuttal Response Template — EMNLP 2026
# Paper: How Does Schema Complexity Predict Performance in Training-Free LLM IE?
# Prepared: 2026-05-19 (pre-submission draft based on anticipated concerns)

---

## General Response

We thank all reviewers for their careful reading and constructive feedback. We address each concern below, organized by topic. Changes to the manuscript are marked with **[REVISED]** and new experiments with **[NEW]**.

*Key changes in revision:*
- [placeholder: list 3-5 major changes after receiving actual reviews]

---

## Q1: Novelty — "SCS is not new; findings are not surprising"

> **[Reviewer ?]** [paste reviewer text here]

We acknowledge that the SCS metric shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion in LLM-PEE (Li et al., 2025); this is stated explicitly in Related Work (§2, ¶4). Our contribution is the *controlled experimental framework* that isolates confusability from count via stratified design, not the metric itself.

Three findings lacked prior empirical evidence before this work:

1. **Task asymmetry (C2):** BCS explains 22–53% of cross-batch RE accuracy variance but shows zero batch-level signal in NER, despite significant pairwise effects in both tasks (Table 3). No prior work documented this format-dependent divergence.
2. **Merge amplification (C3):** Schema decomposition fails because precision collapses from 0.563 to 0.210–0.249 as false positives scale with the number of passes (§5). LLM-PEE's union merge suffers the same failure mode.
3. **Few-shot widening:** 5-shot prompting widens the confusability gap by +4.3pp (Appendix K), indicating confusability effects are structural rather than prompt-engineering artifacts.

"Not surprising in hindsight" is not evidence that findings were already known. We are not aware of prior controlled studies that isolate these factors.

---

## Q2: Effect Size — "r²=1.3% is too small; typical batch gap only 2.2pp"

> **[Reviewer ?]** [paste reviewer text here]

The pairwise r²=1.3–1.7% is *unconditional* across all type pairs, including the ~89% with zero observed confusion. Conditional on nonzero confusion, r² rises to 7% (§6). This is consistent with individual-difference predictors in behavioral research, where such magnitudes are considered "small but real" effects (Cohen, 1988; Lakens, 2013).

The practical signal emerges through *correlated aggregation*: a batch of 16 types contains 120 pairwise SCS values whose contributions are correlated, amplifying the per-pair signal to batch-level R²=22% (FewRel) and 53% (DocRED). A Monte Carlo simulation (Appendix M) confirms the ~3× amplification mechanism from conditional pair-level to batch-level R².

The 2.2pp gap reflects the *typical* IQR of BCS variation among random batches. Production schemas with 80–96 types routinely produce extreme-BCS configurations, where gaps reach 25–31pp (§4.3). For high-throughput extraction pipelines processing thousands of instances, even 2.2pp systematic bias is operationally significant.

---

## Q3: Generalizability — "BCS only works for RE, limited practical value"

> **[Reviewer ?]** [paste reviewer text here]

The task asymmetry is a *core finding* (Contribution 2), not a limitation. We provide a mechanistic explanation (§6):

- **RE** uses forced-choice classification where all non-null errors are type substitutions (Tam et al., 2024), making BCS directly predictive of error rates.
- **NER** produces multi-span output where errors scatter across missed entities, boundary misalignment, and type confusion (Schall and de Melo, 2025), diluting the batch-level BCS signal.

Key evidence that confusability affects *both* tasks:

| Evidence | NER | RE |
|----------|-----|-----|
| Pairwise SCS–confusion (Table 3) | r=0.112, p<0.001 | r=0.187, p<0.001 |
| IntraSub monotonic with BCS (Fig. 2) | ρ=1.0, p<0.001 | ρ=0.954, p<0.001 |
| Batch-level BCS–performance | r≈0 (n=450) | R²=0.22–0.53 |

The pair-level signal exists in NER; batch-level aggregation fails because NER's high miss rate (43–65%) drowns type-confusion effects. This diagnosis is itself practically useful: for NER, reducing candidate types per prompt is the primary lever (§6), whereas for RE, confusability-aware pre-screening of type pairs identifies risk.

---

## Q4: Negative Results — "Many failed experiments; 61% success rate"

> **[Reviewer ?]** [paste reviewer text here]

This is an *analysis paper* investigating degradation mechanisms, not a method paper proposing a solution. Negative results are findings:

- **SDGD failure (C3):** Schema decomposition fails due to merge amplification (NER) and routing failure (RE). This explains *why* prior decomposition approaches (LLM-PEE, UniNER) report limited gains.
- **Schema renaming:** Replacing high-SCS labels reduces embedding similarity but decreases accuracy by 3–9pp due to label unfamiliarity (Appendix U), revealing that confusability cannot be trivially engineered away.
- **Few-shot widening:** Confusability gaps widen under 5-shot prompting (+4.3pp; Appendix K), indicating the effect is structural.

The registry "success rate" includes infrastructure failures (environment issues, vLLM version mismatches) correctly tagged as engineering failures, not scientific conclusions. All scientific experiments produced interpretable results that inform the paper's findings.

---

## Q5: "Correlational only, no concrete examples"

> **[Reviewer ?]** [paste reviewer text here]

We provide both statistical evidence and qualitative grounding:

- **Appendix V** lists the top-10 most confused type pairs for RE and NER, with SCS values and confusion rates.
- **Three concrete error examples** (Appendix V, Table 17) illustrate specific confusion patterns: argument reversal (*participant* vs. *participant of*, SCS=0.98), containment reversal (*contains administrative territorial entity* vs. *located in*, SCS=0.95), and part-whole confusion (*part of* vs. *member of*, SCS=0.92).
- **Error taxonomy decomposition** (Figure 2) shows IntraSub scales monotonically with BCS in both tasks (ρ≥0.954).

Establishing causality at the attention/logit level would require mechanistic interpretability analysis, which we identify as future work (Limitations §4). The controlled stratification design (fixing count, varying BCS) provides stronger evidence than purely observational correlation.

---

## Q6: "Why not rename labels to reduce confusability?"

> **[Reviewer ?]** [paste reviewer text here]

We conducted this experiment (Appendix U). Replacing 12 high-SCS relation labels with semantically distinct paraphrases *reduced* pairwise embedding similarity (mean SCS 0.87→lower) but *decreased* accuracy by 3–9pp. The label unfamiliarity confound outweighed any confusability reduction: models perform worse on unfamiliar label strings even when semantic overlap is reduced.

This result is informative: SCS captures semantic proximity in the model's internal representation space, not just surface-form overlap. Renaming labels changes the surface form but introduces a new error source (model unfamiliarity with novel labels). A clean causal intervention would require controlling the model's vocabulary during pretraining, which is outside the scope of training-free IE.

We discuss this in Limitations §4 as evidence that the confusability mechanism operates at a deeper level than label string similarity.

---

## Q7: "Additivity only holds for FewRel, not DocRED"

> **[Reviewer ?]** [paste reviewer text here]

We report this transparently in §4.4 and restrict the bounded-interaction claim to sentence-level RE:

| Dataset | Interaction | 95% CI | TOST ±3pp |
|---------|-------------|--------|-----------|
| FewRel | +0.3pp | within ±3pp | p=0.003 (established) |
| DocRED | +5.7pp | [−1.6, 13.0] | p=0.77 (not established) |

Two factors explain the divergence:

1. **Baseline compression:** At count=32, DocRED accuracy approaches chance (~49%), leaving less room for confusability to further reduce performance.
2. **Document-level complexity:** Cross-sentence coreference and multi-hop reasoning introduce additional interactions with schema complexity beyond pairwise type similarity.

The CI includes zero, so the DocRED interaction is technically *inconclusive* rather than confirmed non-additive. The core Dim1+Dim2 decomposition framework holds across both datasets; only the quantitative interaction bound is dataset-dependent. We explicitly scope this claim in Introduction (Finding 1), Results (§4.4), and Conclusion.

---

## Q8: "Unconstrained ablation shows null BCS effect — undermines the whole paper"

> **[Reviewer ?]** [paste reviewer text here]

The unconstrained ablation (n=25) *precisely confirms* the error-channeling hypothesis (§6): constrained decoding forces all non-null errors into type substitution, making BCS predictive at batch level; without this constraint, errors disperse across free-text failure modes and the batch-level signal dissipates.

This does not undermine the underlying semantic relationship:

1. **Pairwise SCS still predicts type confusion** across all tasks (r=0.112–0.187, p<0.001; Table 3).
2. **IntraSub scales monotonically with BCS** in both NER and RE (ρ≥0.954; Figure 2).
3. **99.92% of unconstrained outputs** stayed within prompt candidates (2398/2400 responses), confirming models semantically comply with schema instructions even without structural enforcement.

The format dependency is about *batch-level aggregation*, not the underlying semantic relationship. Since most production IE pipelines use structured output (JSON mode, function calling, constrained decoding), the forced-choice regime is the practical default, not an artificial restriction. We discuss this explicitly in §6 and Limitations §3.

---

## Summary of Changes

| # | Change | Location | Status |
|---|--------|----------|--------|
| 1 | [placeholder] | §X | [REVISED] / [NEW] |
| 2 | [placeholder] | §Y | [REVISED] / [NEW] |
| ... | | | |

---

*Notes for authors (remove before submission):*
- Replace [Reviewer ?] placeholders with actual reviewer IDs
- Update table/figure/appendix references to match final manuscript
- Add any new experiments run during rebuttal period with [NEW] tag
- Check ARR rebuttal word limit (typically 3000–5000 characters per reviewer)
- Verify cross-reviewer consistency: claims narrowed for one reviewer must be narrowed for all
