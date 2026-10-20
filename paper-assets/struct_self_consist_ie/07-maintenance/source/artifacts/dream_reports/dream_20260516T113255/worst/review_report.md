---
dream_id: dream_20260516T113255
tier: worst
overall_score: borderline findings (2.5/5)
timestamp: 2026-05-16T12:19:18.482723+00:00
---

# Dream Review Report: "Not All Correlations Transfer: When Population-Level Quality Signals Fail at Instance-Level Selection"

**Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review)
**Review Mode**: Full (2-Reviewer Roundtable)
**Date**: 2026-05-16

---

## Consolidated Scores (Post-Roundtable)

| Dimension | R1 (Methods+Experiments) | R2 (Novelty+Related Work) | Consensus |
|---|---|---|---|
| Soundness | 3.5 | 3.5 | **3.5** (between Acceptable and Strong) |
| Excitement | 2.5 | 2.0 | **2** (Potentially Interesting) |
| Overall Assessment | 2.75 | 2.75 | **2.5** (Borderline Findings) |
| Confidence | 4 | 4 | **4** |

**Recommendation**: Borderline Findings — below the EMNLP main conference threshold (~22% acceptance). The paper documents a real phenomenon with above-average experimental effort, but limited novelty, narrow experimental scope, numerical inconsistencies, and a weak verifier baseline prevent acceptance.

---

## 1. Paper Summary

The paper formalizes a "correlation–selection gap" in test-time scaling (TTS) for structured information extraction: confidence signals that correlate with output quality at the population level (quality estimation, QE; ρ up to 0.45, AUROC up to 0.75) fail to select better candidates at the instance level (Δ < 0.3pp vs greedy, all p > 0.05) despite 13–18pp oracle headroom. Two causal mechanisms are identified — instance degeneracy (21–58% of instances yield identical quality across samples) and logprob score compression (within-instance range 0.041 nats). Controlled ablations (LoRA rank, free-form decoding, scale, supervised verifier) establish the gap as multi-causal. Experiments span 3 datasets (SciERC, CoNLL-2003, WNUT-17), 3 models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B), and 5 confidence signal families.

---

## 2. Strengths

**S1. Clear conceptual contribution (R1+R2 agree).** The QE vs. selection decomposition is well-formulated and genuinely useful. The paper correctly identifies that conflating population-level correlation with instance-level selection capability has led to overoptimistic conclusions about TTS for structured tasks. This distinction, while not entirely new, has not been articulated with this clarity for structured outputs.

**S2. Thorough ablation chain (R1+R2 agree).** The diagnostic chain — free-form decoding, entity-token LP isolation, LoRA rank ablation, verbalized confidence, scale ablation, supervised verifier, cross-model replication — is commendably comprehensive for a negative-result paper. The LoRA rank ablation showing degeneracy reduction is necessary-but-not-sufficient is the strongest experimental contribution.

**S3. Difficulty gradient design (R1).** Using SciERC (medium difficulty), CoNLL (ceiling control), and WNUT-17 (signal-collapse boundary) with explicit roles for each dataset is sound experimental design.

**S4. Statistical methodology (partial — R1).** The paper deploys bootstrap CIs, TOST equivalence testing, Cohen's d, Bonferroni correction, and Fisher's z-test. While application is inconsistent in places (see W4), the ambition is above average.

**S5. Practical QE value (R2).** The positive result — that structural signals reliably predict output quality with difficulty-dependent rankings — is independently useful. Practitioner guidance (VC for medium-difficulty, EM for easy/binary) is actionable.

**S6. Honest limitations (R1+R2 agree).** The paper is transparent about scope: decoder-only models only, 4–8B scale, limited RE coverage, no trained verifier with input representations.

---

## 3. Weaknesses

### Major

**W1. Limited novelty of the core observation (R2, endorsed by R1).** The finding that "capable models produce similar outputs, leaving little room for selection" is a straightforward consequence of model convergence already documented in adjacent settings:
- Kirk et al. (2024): diversity collapse in RLHF-trained models
- Brown et al. (2024, "Large Language Monkeys"): diminishing returns of best-of-N
- Eikema & Aziz (2022): MBR gains diminish when hypothesis space concentrates

The "correlation–selection gap" terminology is new, but the underlying phenomenon is not. The paper's contribution is rigorous empirical quantification in NER rather than conceptual discovery. For a 22% acceptance-rate venue, the novelty bar requires more than careful confirmation of expected behavior. **Both reviewers independently assessed novelty as medium-low.**

**W2. Narrow experimental scope undermines generality claims (R1+R2 agree).** The paper evaluates only decoder-only models (3B–8B) with LoRA fine-tuning. The "model-agnostic" claim rests on Qwen3-8B and LLaMA-3.1-8B — two 8B decoder-only models with identical LoRA recipes. No encoder-based model (DeBERTa, BERT-CRF), no 70B+ model, and no closed-source API model is tested. The instance degeneracy phenomenon could plausibly be specific to LoRA fine-tuning of mid-scale decoder-only models. The title ("Not All Correlations Transfer") and framing suggest a general lesson for TTS, but the evidence is from one task family (NER + exploratory RE) with one model architecture class.

**W3. Weak supervised verifier baseline (R1+R2 agree).** The logistic regression on 5 signals is not a meaningful test of whether learned scoring can close the oracle gap. R1's decomposition is sharp: 4 of 5 features (SJ, FK, EM, VC) are instance-level aggregates identical across candidates within an instance. This makes the LR effectively a univariate LP selector with regularization. The conclusion that "the bottleneck is in the features, not the aggregation" is valid only for these specific features. A verifier using hidden states, output embeddings, or a cross-encoder reranker was not tested. The paper's claim that "closing the gap requires content-aware verifiers" is a plausible hypothesis, not a demonstrated finding.

**W4. Numerical inconsistencies across the paper (R1, endorsed by R2).** Multiple version-drift issues undermine reporting reliability:
- **AUROC headline**: Abstract/intro claim "AUROC up to 0.82" but this comes from CoNLL EM (0.816 rounded), not the primary test bed SciERC (0.749). This is misleading as a headline figure.
- **P-value discrepancy**: Table 2 reports LP selection p = 0.39 (bootstrap), but the paper also references different statistical tests in different places without reconciliation.
- **Supervised verifier**: Main text references gap closed and AUROC values that may reflect different experimental configurations (3-fold vs 5-fold CV) without clearly stating which is definitive.
- **Oracle NER**: Minor discrepancy between 0.776 and 0.778 across different references.
- **Greedy F1**: 0.644 vs 0.645 appears in different locations.

None suggest fabrication — they reflect version drift across experiment iterations — but they indicate insufficient quality control in the final manuscript. **R2 downgraded Soundness from 4 to 3.5 after reviewing R1's numerical audit.**

**W5. Instance degeneracy on CoNLL is partially tautological (R2).** CoNLL with 92% greedy F1 and 58% degeneracy reduces to: "a near-perfect model produces the same near-perfect output every time." Including CoNLL's 58% in the headline "21–58%" range inflates the apparent severity. The informative case is SciERC (21% degeneracy at 66% F1), which is already acknowledged as the primary test bed.

### Minor

**W6. Statistical power concerns (R1+R2).** The primary selection analysis uses limited seeds on n=529 (SciERC). Power to detect small but real improvements (1–2pp) is limited. TOST equivalence results are configuration-dependent.

**W7. Temperature sensitivity under-explored (R1).** Only T=0.7 and T=1.0 tested. Higher temperatures (T=1.5, T=2.0) would directly test the degeneracy and compression mechanisms — the most natural experimental lever for the paper's own hypotheses.

**W8. WNUT gold-empty filtering.** 46.5% of WNUT instances removed due to empty gold labels. This aggressive filtering is not adequately justified and may bias results.

**W9. Instance degeneracy definition.** "Constant F1" conflates two distinct phenomena: (a) all N outputs are identical strings, and (b) outputs differ but coincidentally achieve the same F1. The paper reports both (11% identical vs 21% constant-F1 on SciERC) but the headline uses the broader definition without sufficient clarification.

**W10. Missing direct comparison with Yao et al. (R2).** The most directly comparable prior work (consistency–accuracy correlations for LLM-based IE) is not quantitatively compared. Without Yao et al.'s numbers, the marginal contribution is hard to assess.

---

## 4. Questions for Authors

1. The abstract claims "AUROC up to 0.82" — is this from CoNLL EM (0.816 rounded)? If so, the primary test bed (SciERC) reaches only 0.749. Should the headline reflect the primary test bed?

2. The non-tied LP subset shows +2.9pp (p=0.004), surviving Bonferroni correction. This is a genuine positive selection result. What characterizes these ~210 instances? Could a meta-classifier predict which instances have sufficient LP spread for successful selection? This seems like the paper's most interesting finding and deserves more prominence.

3. The RE free-form ablation shows LP selection consistently improves (+1.8pp across seeds). Why is this relegated to the appendix rather than developed as a positive contribution?

4. Have you considered diversity-promoting decoding (diverse beam search, higher nucleus sampling p) rather than standard temperature sampling? Instance degeneracy might partly reflect the decoding strategy.

5. What are Yao et al.'s specific correlation values? How do they compare to your ρ values? Did they attempt selection?

6. At higher temperatures (T=1.5, T=2.0), degeneracy should decrease. Is there a temperature sweet spot where selection becomes viable?

7. What happens if the supervised verifier uses model hidden states or output embeddings instead of the 5 hand-crafted signals?

---

## 5. Missing Experiments (Priority-Ordered)

1. **Higher temperature ablation** (T=1.5, T=2.0) — directly tests the paper's own mechanisms
2. **Stronger verifier** (MLP on hidden states or cross-encoder reranker) — would test whether the oracle gap is truly unclosable
3. **Encoder-based model** (DeBERTa-NER or BERT-CRF) — tests whether degeneracy is decoder-only specific
4. **70B+ or API model** — tests scale generalization
5. **Develop the non-tied LP positive result** — the +2.9pp finding deserves its own analysis
6. **Additional RE benchmarks** (TACRED, ACE05) — would elevate RE from "exploratory"

---

## 6. Missing Related Work

- **Diverse decoding**: Vijayakumar et al. (2016, Diverse Beam Search), Ippolito et al. (2019), Li et al. (2016) — directly relevant since the paper diagnoses output concentration but does not consider diversity-promoting alternatives
- **Broader MBR**: Bertsch et al. (2023, "It's MBR All the Way Down"), Trabelsi et al. (2024, Efficient MBR)
- **Structured prediction calibration**: Wiseman et al. (2016), Belanger & McCallum (2016)
- **Ensemble selection in NLP**: Florian et al. (2003), Sim et al. (2007), Rosti et al. (2007)
- **Mode collapse in fine-tuning**: Shumailov et al. (2024, "The Curse of Recursion")
- **Token-level vs sequence-level scoring**: Murray & Chiang (2018)

---

## 7. Novelty Assessment

**Medium-Low.** The core findings decompose into:
- (a) Instance-level aggregate signals (SJ, FK, EM, VC) cannot by construction discriminate among candidates for a given input — this is partly definitional, not empirical
- (b) Capable fine-tuned models produce concentrated outputs — known from diversity collapse and MBR literature
- (c) Log-probability is a weak per-sample signal for structured extraction — expected given known calibration issues

The conceptual advance beyond "best-of-N has diminishing returns when the model is already good" is present but modest. The QE-vs-selection framework is a useful contribution, and the multi-causal diagnostic chain (especially the LoRA rank necessity-but-not-sufficiency result) adds empirical depth. However, for a 22% acceptance venue, the novelty requires more than careful empirical confirmation of expected behavior in a specific domain.

---

## 8. Experiment Design Coverage

Checked against the full experiment plan:
- **ner_llama_conll (exp-017)**: Covered in Table 3. Cross-model validation is present but weak — two 8B decoder-only models with identical LoRA recipe is internally consistent but does not constitute model-agnostic evidence.
- **simple_verifier_baseline (exp-019)**: Covered in Table 4. LR on 5 correlated signals is effectively a weighted average; closes less gap than best single signal. Validates the negative but does not test the constructive hypothesis.
- **claim_audit (exp-024)**: Partially addressed — the paper includes Appendix A (Numerical Consistency Notes) and the abstract AUROC was adjusted from 0.82 to 0.75 in the text (though 0.82 may persist in some locations). Several inconsistencies remain unresolved.

---

## 9. Roundtable Narrative

**Step 1 (Independent)**: R1 focused on methods/experiments and identified numerical inconsistencies, narrow cross-model validation, and the weak verifier. Scored Soundness 3.5, Excitement 3, Overall 3.0. R2 focused on novelty/related work and found the core observation to be an expected consequence of model convergence, with medium-low novelty. Scored Soundness 4, Excitement 2, Overall 3.0.

**Step 2 (Cross-sharing)**: R1 accepted R2's novelty critique and lowered Excitement from 3 to 2.5. R1 highlighted the non-tied LP subset (+2.9pp) as an underexploited positive finding. R2 accepted R1's numerical consistency analysis and lowered Soundness from 4 to 3.5. R2 pushed back on R1's "statistical rigor" strength, arguing that deploying many tests inconsistently is not rigor.

**Step 3 (Convergence)**: Both reviewers converged on Soundness 3.5, Overall 2.75. Key areas of agreement: (1) narrow model diversity undermines generality claims, (2) weak verifier is not a fair test, (3) numerical inconsistencies indicate insufficient quality control, (4) limited novelty for a top venue. The strongest disagreement was on Excitement (R1: 2.5, R2: 2), resolved to 2 in the consensus given the confirmed low novelty.

**Step 4 (Synthesis)**: Final consensus is **Overall 2.5 (Borderline Findings)**. The paper has a defensible core idea and above-average experimental effort, but the combination of (a) limited novelty over known phenomena, (b) narrow scope that cannot support the generality claims, (c) a weak verifier baseline that leaves the most important question unanswered, and (d) numerical version-drift issues places it below even the Findings threshold as currently written. A revision addressing the verifier gap (hidden-state verifier), broadening model diversity (encoder model or 70B+), developing the positive sub-results (non-tied LP, RE free-form), and resolving numerical inconsistencies could elevate this to a solid Findings paper.

---

## 10. Actionable Revision Priorities

1. **Fix numerical inconsistencies**: Reconcile AUROC headline, p-values, verifier numbers, greedy F1 across all sections. Use a single definitive experiment run for each claim.
2. **Develop the non-tied LP positive finding**: The +2.9pp (p=0.004) result is the paper's most interesting finding. Characterize what makes these instances amenable to selection. This transforms the paper from pure negative result to "selection works under specific conditions."
3. **Implement a stronger verifier**: Even a 2-layer MLP on hidden states would test whether the oracle gap is closable. The current LR baseline proves nothing about learned verifiers.
4. **Add one encoder-based model**: A DeBERTa or BERT-CRF on SciERC would test whether degeneracy is architecture-dependent.
5. **Test higher temperatures**: T=1.5 or T=2.0 directly tests the degeneracy mechanism.
6. **Reframe the narrative**: Lead with the conditions under which selection succeeds vs fails (the non-tied LP analysis), rather than a blanket negative result. This is both more accurate and more useful.