---
dream_id: dream_20260515T092545
tier: best
overall_score: borderline accept
timestamp: 2026-05-15T10:19:54.763849+00:00
---

# Reviewer 2 (R2): Novelty and Related Work

## 1. Summary

This paper systematically evaluates five confidence signals from three families (structural, surface, model-internal) for quality estimation (QE) and sample selection in LLM-based information extraction under constrained decoding. The central finding is the "correlation-selection gap": consistency signals achieve strong instance-level QE (voting confidence rho=0.50, AUROC=0.73 on SciERC NER) but universally fail to improve best-of-N selection over greedy decoding. The paper evaluates across NER and RE on three datasets (SciERC, CoNLL-2003, WNUT-17) with two 8B models (Qwen3, LLaMA-3.1), characterizes task-difficulty-dependent signal rankings, and identifies boundary conditions where all signals collapse.

---

## 2. Novelty Assessment

### 2a. The "predict-but-cannot-select" (correlation-selection gap) finding

**Moderately novel, but partially expected.** The conceptual observation that instance-level aggregate signals cannot rank candidates within an instance is, as the authors themselves acknowledge in paper_framing.md, "noted not discovered" -- it follows definitionally from the fact that 4/5 signals produce a single scalar per instance. The more interesting empirical component is that logprob (the only per-sample signal) also fails on NER, and that the gap persists even under free-form decoding. However, the logprob failure is less surprising than presented: in a fine-tuned model producing near-deterministic outputs at high accuracy (greedy NER F1=0.61), logprob compression is an expected consequence of confident, well-calibrated fine-tuning. The paper would benefit from more explicitly engaging with the question of whether this finding would surprise a practitioner familiar with both self-consistency and structured prediction.

**Strength**: The quantification of the gap with bootstrap CIs (p=0.39, Cohen's d=0.038) is rigorous. The oracle headroom analysis (NER +16pp, RE +18.7pp) effectively demonstrates that information exists but signals cannot access it.

### 2b. QE-vs-selection conceptual distinction

**Useful clarification, modest novelty.** Disentangling QE from selection is a genuine contribution to clarity in the IE confidence literature. However, this distinction is well-established in adjacent fields: quality estimation vs. reranking is a standard dichotomy in machine translation (Fomicheva et al. 2020, TACL), and selective prediction vs. best-of-N is implicit in the test-time scaling literature (Snell et al. 2024). The novelty lies in demonstrating that this distinction matters specifically for structured IE and explaining mechanistically why it does (instance-level aggregation vs. per-sample discrimination). This is incremental but useful.

### 2c. Free-form ablation as diagnostic

**The ablation result is genuinely informative.** The finding that removing constrained decoding does NOT recover logprob variance (std ratio 0.97) is a well-designed controlled experiment that falsifies a natural hypothesis. This is the most novel empirical contribution in the paper, as it rules out a plausible explanation and establishes that score compression is model/task intrinsic. However, this result appears only in the project framing documents and the ablation report -- it is NOT present in the current paper draft (the experiments.tex, discussion.tex, etc. do not contain the ablation results). If this is not included in the final submission, the paper loses its strongest novelty claim.

### 2d. Supervised verifier baseline (DeBERTa)

**Not yet available.** The abstract mentions "supervised DeBERTa verifier captures 15.9% of oracle headroom," but exp-019 is listed as "waiting for approval" and no results exist in the artifacts. If this is included in the final paper, it provides a useful "so what" anchor. A 15.9% headroom capture rate is modest but establishes that the gap is partially closable, transforming a pure negative result into an actionable one. The novelty of using a supervised verifier for IE selection is low (this is standard in the reasoning literature via Cobbe et al. 2021), but its application to structured IE is new.

### 2e. Overall novelty verdict

This is best characterized as a **systematic empirical study that extends self-consistency to a new domain (structured IE) and identifies a non-trivial negative result**. It is not a methodological contribution -- no new method is proposed. The novelty is in the empirical finding (the gap), the diagnostic rigor (the ablation, the bootstrap analysis), and the practical characterization (task-difficulty-dependent signal rankings). For EMNLP Findings, this level of novelty is appropriate if the execution is clean. The paper does not claim to introduce a new method, and the framing as an empirical analysis paper is honest.

---

## 3. Related Work Coverage

### 3a. Overall assessment

The related work section (as written in related_work.tex) is **comprehensive and well-organized**. The three-subsection structure (self-consistency/TTS, consistency for structured IE, uncertainty/calibration) covers the main threads effectively. The literature map contains 55 papers, and the paper cites 30+. This is adequate for EMNLP.

### 3b. Key works cited and positioned

- **Wang et al. 2023 (self-consistency)**: Properly cited as foundation, with clear differentiation (discrete answers vs. set-valued outputs). Good.
- **CISC, Self-Certainty, ReASC**: All cited with explicit positioning. The dialogue with Self-Certainty (Kang et al.) in the introduction is effective -- "reward-free selection succeeds for reasoning; our results demonstrate this does not transfer to structured extraction."
- **Nedellec and Xia 2026**: Thoroughly discussed with three specific limitations (surface matching, no selection, single domain). The differentiation is convincing and fair.
- **CoCoA (Vashurin et al. 2025a)**: Cited but discussed in only one sentence. Given that CoCoA is the closest methodological analog (MBR-based confidence+consistency fusion for UQ), it deserves more discussion. Specifically: how does CoCoA's MBR formulation relate to the paper's consensus-proximity analysis? Does the CoCoA framework predict the correlation-selection gap?
- **Snell et al. 2024, Brown et al. 2024**: Properly cited as TTS foundations.
- **Verifiers (Cobbe, Lightman)**: Cited as alternative paradigm. Adequate.

### 3c. Critical missing references

1. **Eikema and Aziz 2022 (MBR decoding)**: Listed in the abstract's reference set but I do not see it cited in related_work.tex. Given that the paper's SJ-based selection is conceptually related to MBR with set Jaccard as the utility function, MBR decoding should be explicitly discussed. The claim that "set-based IE metrics create different optimization landscape where consensus-proximity fails" needs MBR as the explicit foil.

2. **Universal Self-Consistency (Chen et al. 2024)**: Cited in introduction and related work, but the discussion could be deeper. USC uses the LLM itself as a judge to select the most consistent answer -- this is a viable alternative to the metric-based signals the paper evaluates. The paper should discuss why USC was not included as a baseline (presumably cost, but this should be stated).

3. **Fomicheva et al. 2020 (Unsupervised QE for MT)**: In the literature map but not in the paper. This is the closest analog from MT -- using MC dropout and ensemble uncertainty for quality estimation without supervision. The QE-vs-selection distinction the paper emphasizes is well-established in MT QE literature, and acknowledging this precedent would strengthen rather than weaken the paper.

4. **Structured prediction under constrained decoding**: The paper uses Outlines/XGrammar for constrained decoding but does not discuss the growing literature on how grammar constraints affect model distributions. Work on how constrained decoding distorts logprob distributions (e.g., Park et al. 2024 on grammar-constrained decoding effects) would directly contextualize the logprob compression finding.

5. **GenIE (Josifoski et al. 2022)**: In the literature map and cited in the related work, but its bi-level constrained decoding approach is directly relevant to understanding how constraints affect confidence signals. Could be discussed more.

### 3d. Is the claim "none address structured IE" accurate?

**Mostly accurate, with a caveat.** The claim that no prior self-consistency work addresses structured IE outputs is true in the strict sense -- Wang et al., CISC, Self-Certainty, ReASC all target discrete answers. However, Nedellec and Xia 2026 do study consistency for IE (NER and RE), and Atomic SC (Thirukovalluru et al. 2024) addresses non-discrete structured outputs (atomic sub-claims). The paper should soften this to "no prior work systematically compares confidence signal families for set-valued structured IE outputs or evaluates their selection utility" rather than implying no one has studied consistency for IE at all.

### 3e. Differentiation from Nedellec and Xia 2026

**Convincing.** The three-point differentiation (surface matching vs. SJ, no selection analysis, single domain) is concrete and fair. The paper directly quotes Nedellec and Xia's own acknowledged limitation about overlooking semantically consistent outputs, which is effective positioning. This is well-handled.

### 3f. CoCoA discussion sufficiency

**Insufficient.** CoCoA is the most methodologically similar work -- it fuses model confidence (logprob) with inter-sample consistency via an MBR framework. The paper's ensemble of SJ+logprob (Table 3) is conceptually similar. The paper should discuss: (a) whether CoCoA's formulation would predict the correlation-selection gap, (b) why the ensemble underperforms the best single signal (EM), and (c) how CoCoA's success on QA/summarization/translation contrasts with the paper's failure on structured IE. This contrast would strengthen the "structured IE is different" argument.

---

## 4. Framing and Positioning

### 4a. Venue fit

**Good fit for EMNLP Findings.** The paper is a systematic empirical study with a well-characterized negative result. It does not propose a new method, which makes it marginal for main conference, but the diagnostic rigor and practical guidance are valuable for Findings. The comparison-plus-boundary-conditions contribution pattern is well-suited to this venue.

### 4b. "Correlation-selection gap" terminology

**Clear and useful.** The term is well-defined, easy to remember, and captures the phenomenon precisely. It has potential to become a standard reference term if the paper is published. Minor concern: the term appears only in the NER context where it is absolute (no signal beats greedy). On RE, logprob does improve over greedy (+2.3pp), so the "gap" is partial. The paper should acknowledge this more prominently -- the gap is task-dependent, not universal, despite the paper_framing.md claiming universality.

### 4c. Three contributions -- scope vs. evidence

- **Contribution 1 (first systematic comparison)**: Well-supported by the evidence. Five signals, three datasets, two models. The scope is appropriate.
- **Contribution 2 (correlation-selection gap)**: Supported for NER, partially for RE. The bootstrap analysis (p=0.39) is rigorous. However, the claim would be stronger with the free-form ablation included in the paper (currently missing from the draft).
- **Contribution 3 (task-complexity boundary)**: The weakest contribution. The EM-dominates-easy / SJ-dominates-hard / all-converge-when-insufficient characterization is useful but somewhat obvious -- simpler signals suffice for simpler tasks. The WNUT-17 boundary analysis (logprob rho=-0.411, overconfidence on novel entities) is more interesting and could be elevated.

### 4d. Title

The current draft does not have a single consistent title. The abstract suggests the framing is about "confidence signals for test-time scaling in generative IE." The paper_framing.md proposes "Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction." The prompt's title is "Confidence Signals Predict but Cannot Select in Constrained-Decoding Information Extraction."

The prompt's title includes "Constrained-Decoding" which is misleading if the ablation shows the gap is NOT constrained-decoding-specific. The paper_framing title "Strong Predictors, Weak Selectors" is more accurate and catchier. However, "Cannot Scale" overstates -- the paper shows signals cannot *select*, not that they cannot scale IE in general (e.g., QE-based routing could still help). I would recommend: **"Confidence Signals Predict but Cannot Select: The Correlation-Selection Gap in LLM-Based Information Extraction"**.

---

## 5. Potential Impact

### 5a. Who benefits?

- Practitioners deploying LLM-based IE systems who need to decide whether to invest in multi-sample generation and selection strategies. The paper's practical recommendation (use consistency for QE/routing, not for selection) is immediately actionable.
- Researchers working on test-time scaling who need to understand domain boundaries for self-consistency methods.
- Researchers developing confidence estimation for structured prediction tasks beyond IE.

### 5b. Research directions opened

- **Supervised verifiers for structured IE**: The oracle headroom analysis motivates training dedicated verifiers, analogous to the reasoning literature.
- **Per-sample signals for structured outputs**: The paper identifies that instance-level signals cannot select, motivating research into per-sample structural quality signals.
- **Constrained decoding effects on model distributions**: The ablation opens questions about when and how constrained decoding affects different aspects of generation quality.

### 5c. Citation likelihood

**Moderate.** The paper would likely be cited by: (a) future work on self-consistency for structured tasks, (b) papers on LLM-based IE that need to discuss confidence estimation, (c) test-time scaling papers that discuss domain limitations. The "correlation-selection gap" term could become a standard reference if the finding is robust. I estimate 15-30 citations in the first two years.

---

## 6. Weaknesses

### W1. Novelty is primarily negative/empirical, not methodological.
The paper identifies a limitation (signals cannot select) but does not propose a solution. The free-form ablation and supervised verifier are diagnostic, not prescriptive. For Findings this is acceptable, but it limits impact.

### W2. The free-form ablation -- the strongest novelty claim -- is missing from the paper draft.
The experiments.tex, discussion.tex, and conclusion.tex I reviewed do not contain the ablation results. The abstract mentions constrained decoding analysis, but the current paper body appears to be from an earlier draft (pre-D072). If this is not included in the final submission, the paper loses its most distinctive empirical contribution and reverts to a descriptive comparison study.

### W3. Inconsistency between abstract/framing and paper body.
The abstract provided in the prompt mentions "removing grammar constraints recovers logprob variance ~3.5x" and "supervised DeBERTa verifier captures 15.9% of oracle headroom." The paper_framing.md (D072) says the ablation FALSIFIED the 3.5x claim (actual ratio is 0.97x, NOT 3.5x). The abstract appears to be from an older version. Additionally, the supervised verifier (exp-019) has not been completed. This creates a coherence risk if the final submission mixes old and new claims.

### W4. Single RE benchmark limits the correlation-selection gap generalizability claim.
SciERC RE has 44% zero-F1 instances, creating a severe floor effect. The gap on RE may be partly an artifact of the model simply not being capable enough at this task. A second RE dataset (e.g., TACRED, DocRED) would substantially strengthen the claim.

### W5. CoCoA and MBR under-discussed.
As noted in Section 3, CoCoA is the closest methodological analog and deserves deeper engagement. The SJ-based selection is essentially MBR with Jaccard utility, and the paper should make this connection explicit and explain why MBR fails here despite succeeding in MT.

### W6. The "universality" claim requires nuance.
The paper_framing claims the gap is "universal" based on the free-form ablation. But "universal" is a strong word -- it has been demonstrated on one task family (IE), two datasets for NER, one for RE, with two 8B models. The gap may not hold for larger models, different IE formulations (e.g., code-generation-based IE), or different output structures (e.g., event extraction). "Robust across our experimental conditions" is more defensible than "universal."

### W7. Logprob RE selection gain (+2.3pp) somewhat undermines the gap narrative.
The paper frames the gap as the central finding, but logprob does help on RE. The narrative needs to more clearly articulate that the gap is absolute for NER but partial for RE, rather than presenting it as a universal failure. The current framing oscillates between "no signal helps" and "logprob helps on RE."

---

## 7. Questions for Authors

**Q1.** The free-form ablation (exp_freeform_ablation) shows LP std ratio of 0.97x, falsifying the constrained decoding bottleneck hypothesis. But the abstract provided for review mentions "removing grammar constraints recovers logprob variance ~3.5x." Which is the correct claim for the final submission? This is a critical inconsistency that must be resolved.

**Q2.** CoCoA (Vashurin et al. 2025a) unifies confidence and consistency via MBR, achieving strong results on QA and summarization. Your SJ-based selection is conceptually an MBR approach with Jaccard utility. Can you explain mechanistically why this MBR-like approach fails for IE when it succeeds for other generation tasks? Is it the discreteness of the output space, the set structure, or something else?

**Q3.** The supervised verifier (DeBERTa, 15.9% headroom capture) is mentioned in the abstract but exp-019 appears incomplete. Will this be included in the final submission? If so, what is the training setup (how many labeled examples, cross-validation strategy)?

**Q4.** You evaluate at N=8 and N=16. Given that RE signals improve substantially from N=8 to N=16 (voting rho from 0.340 to 0.448 per paper_framing.md), have you considered whether the correlation-selection gap might narrow at N=32 or N=64? The gap could be a sample budget artifact for RE rather than a fundamental limitation.

**Q5.** The WNUT-17 finding (logprob rho=-0.411, strong negative correlation) is striking and arguably the most practically important result. Have you investigated whether this negative correlation is specific to novel/emerging entities, or whether it occurs for any OOD shift? This has implications for whether logprob should be used as a *negative* signal for abstention on OOD inputs.

---

## 8. Scores

### Soundness: 3.5 / 5
**Justification**: The experimental methodology is rigorous -- bootstrap CIs, multiple seeds, leave-one-out circularity checks, cross-model validation. The statistical analysis is appropriate (Spearman rho, AUROC, bootstrap p-values, Cohen's d). However, the inconsistency between the abstract (3.5x variance recovery) and the actual ablation result (0.97x ratio) raises concerns about which claims will appear in the final paper. The single RE dataset and the incomplete supervised verifier experiment also reduce confidence. If the final paper resolves these issues, soundness would be 4.0.

### Excitement: 2.5 / 5
**Justification**: The correlation-selection gap is a useful finding but not a surprising one. The definitional component (instance-level signals cannot rank per-sample) is straightforward. The empirical component (logprob also fails due to score compression) is more interesting but is partially expected for fine-tuned models. The free-form ablation proving intrinsic compression is the most exciting finding, but it is not in the current paper draft. Without the ablation and verifier, this is a competent empirical comparison study with a negative result -- useful for the community but not exciting. With the ablation included and well-framed, excitement would rise to 3.0.

### Overall Assessment: 3.0 / 5 (Borderline)
**Justification**: This is a well-executed empirical study that makes a useful contribution to the structured IE and test-time scaling communities. The QE evaluation framework is thorough, the cross-model and cross-dataset validation is appropriate for the scope, and the correlation-selection gap is clearly demonstrated. The paper is honest about its limitations. However, the novelty is incremental -- extending self-consistency analysis to a new domain and documenting where it fails. The lack of a proposed solution limits impact. The critical question for accept/reject is whether the free-form ablation and supervised verifier are included: with them, this is a solid Findings paper (3.5); without them, it is a descriptive comparison study that sits at the borderline (2.5-3.0). I score at 3.0 assuming partial inclusion of the ablation but noting the uncertainty.

For EMNLP Findings, I lean toward **borderline accept** contingent on: (1) including the free-form ablation results with correct numbers, (2) resolving the abstract inconsistency, (3) expanding CoCoA/MBR discussion, and (4) toning down universality claims.

### Confidence: 4 / 5
I am confident in this assessment. I have expertise in LLM uncertainty estimation and structured prediction, and I have reviewed the full paper draft, experimental results, and project documentation carefully. My main uncertainty is about what the final submission will contain, given the discrepancies between the abstract provided for review and the actual experimental results.

---

## Summary Recommendation

**Borderline accept for EMNLP Findings**, pending resolution of the abstract/ablation inconsistency and inclusion of the free-form ablation as a first-class contribution. The paper's strengths are its systematic evaluation, rigorous statistical analysis, and the practically useful correlation-selection gap finding. Its weaknesses are limited novelty beyond the negative result, under-discussion of CoCoA/MBR, and an incomplete supervised verifier experiment. The free-form ablation is the paper's best claim to novelty and must be prominently included with correct numbers.
