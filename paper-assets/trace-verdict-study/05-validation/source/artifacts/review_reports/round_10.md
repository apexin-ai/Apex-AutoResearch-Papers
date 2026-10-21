---
round: 10
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T06:28:31.050254+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 15 Consolidated Review Report
**Paper**: Complete Execution Traces Degrade SFT-Based Verdict Prediction: A Diagnostic Signal Analysis
**Venue**: EMNLP 2026 (ARR)
**Date**: 2026-05-22
**Mode**: Fresh review (no prior round context)
**Reviewers**: R1 (statistical methodology + experimental rigor), R2 (novelty/framing + theoretical grounding)

---

## Summary

The paper investigates how different execution trace representations affect SFT-based verdict prediction (pass/fail classification) across four code LLMs (1.5B-13B, three families). The core finding is that complete traces (72-82%) underperform compact exception events (>=99.33%) by 18+pp, and a decomposition attributes >=74% of this gap to "information overload" at inference time. The paper proposes a two-tier diagnostic signal hierarchy and a two-pathway model (explicit diagnostic tokens vs. implicit terminal state).

The experimental execution is thorough (13 pages of appendix, multi-seed validation, calibration analysis, OOD evaluation, deduplication analysis, robustness checks), placing it in the top tier of empirical studies in this area. However, two structural issues limit the paper's contribution: (1) the near-tautological nature of the exception_only finding combined with a buried strong regex baseline, and (2) a confounded causal decomposition that undermines two of four stated contributions.

---

## Strengths

1. **Comprehensive experimental design.** 7 trace conditions x 4 models x 3 architectures with multi-seed validation. The systematic coverage is exemplary for an empirical study.

2. **Robust statistical infrastructure.** Paired bootstrap resampling (B=10,000), Wilson 95% CIs, calibration analysis (ECE), and extensive robustness checks (deduplication, marker removal, padding control, truncation budget curves).

3. **Non-trivial core finding: complete traces degrade performance.** The full_trace -> no_trace comparison shows -11.9pp degradation (Table 1). Adding more information actively hurts — this is independently interesting regardless of exception_only's performance, and the training dynamics evidence (Figure 3: full_trace oscillates 82-89%, exception_only converges in ~50 steps) provides process-level empirical support.

4. **Practical actionable guidance.** The truncation budget curve (Figure 4) identifying a sharp performance jump at ~384-512 tail tokens, and the exception-first fallback recommendation, are directly useful for practitioners building trace-based tools.

5. **Thorough appendix.** 13 pages covering per-class breakdown, tokenizer analysis, persistent error analysis, exception type breakdown, calibration diagrams, error overlap, DebugBench OOD, and training dynamics — a model of empirical completeness.

---

## Weaknesses

### Must-Fix (4 issues)

**MF-1. Near-tautological finding + B5 regex baseline buried [R2-N1, R1 partial AGREE]**

Exception events structurally encode verdict: fail -> exception present, pass -> `[No exception data in trace]` marker. Regex baseline B5 (Appendix P) achieves 99.31% by exploiting this marker alone, yet B5 is buried in the appendix while the main text uses weaker B4 (93.61%) as the primary comparison. SFT exception_only (99.83%) exceeds B5 by only 0.52pp.

**Director's adjudication**: R1 rebuts "tautological" as too strong, arguing full_trace degradation (-11.9pp vs no_trace) is independently non-trivial. This rebuttal has merit — the paper's value lies in "complete traces hurt" rather than "exceptions help." However, the current framing emphasizes the latter. Both reviewers agree on corrective action: foreground B5 as primary baseline; reframe core contribution as "complete traces degrade SFT performance"; promote marker removal (97.65%) to a formal ablation in the main text.

**MF-2. Confounded causal decomposition (§3.4) [R1-N3, R2-N2, CONSENSUS]**

The "26% gradient dilution + 74% information overload" decomposition packages a confounded ablation residual as an independently measured mechanism. Label-only loss simultaneously changes: (a) gradient selection (loss computed on ~1/500th of tokens), (b) implicit regularization (removing next-token prediction on trace tokens), (c) effective learning rate (~2000x increase per-label). The +4.50pp improvement cannot be cleanly attributed to gradient dilution relief.

Consequence: this undermines Contribution 3 (decomposition) AND Contribution 4 (two-pathway model), which lacks direct evidence (no attention weights, no gradient attribution). Both reviewers agree: downgrade to "confounded upper-bound estimate"; reframe two-pathway model as "descriptive hypothesis" not "finding."

**MF-3. Multiple comparison correction absent [R1-N1, R2 AGREE]**

50+ pairwise bootstrap comparisons across 7 conditions x 4 models with no Bonferroni/Holm-Bonferroni/FDR correction. The 18+pp main effect survives any correction, but borderline comparisons are at risk: Tier 2 internal comparisons, label_only +4.50pp, truncation condition differences (1-3pp). This compounds MF-2: if label_only's p-value inflates after correction, §3.4's already-fragile decomposition loses further credibility.

**MF-4. Bootstrap CI independence violation (~49% duplicate samples) [R1-N2, R2 AGREE]**

Test set has 1,190 nominal samples but only ~607 unique (Appendix O). Bootstrap CIs are computed on N=1,190, systematically underestimating width. R2 adds: the duplicates are predominantly pass samples containing the `[No exception data in trace]` marker, cross-reinforcing MF-1's concern about format-driven accuracy. Main effect (18+pp) is robust, but Tier 2 internal and label_only borderline comparisons need re-evaluation with deduplicated or problem-level clustered bootstrap.

### Should-Fix (8 issues)

**SF-1. Missing ML theory connections [R2-W1, R1 AGREE]**

"More features can hurt" is a classical ML result (information bottleneck, feature selection, curse of dimensionality). The paper frames its finding as novel without connecting to Tishby et al. (2000), Guyon & Elisseeff (2003), or Zhou et al. (2023) LIMA. This affects novelty calibration: the contribution should be positioned as "empirical validation of classical theory in code trace + SFT setting."

**SF-2. "Information overload" terminology inappropriate [R2-W2, R1 partial AGREE]**

Cognitive science/HCI metaphor applied to model behavior. Models don't experience "overload" — they learn spurious correlations on irrelevant tokens. Use "diagnostic signal dilution," "irrelevant feature noise," or "representation bottleneck." First occurrence can retain "information overload" in quotes as intuitive framing.

**SF-3. Cross-dataset evaluation incomplete [R1-W5, R2-W3, CONSENSUS]**

DebugBench OOD evaluation tests only top conditions (exception_only 100%, VOTA 99.77%). The core claim — complete traces degrade performance — is never validated OOD. If full_trace doesn't degrade on DebugBench, the finding may be dataset-specific. Additionally, DebugBench uses synthetic mutations, not natural bugs.

**SF-4. Training dynamics lack quantitative rigor [R1-W4, R2 AGREE]**

Figure 3 shows only ~150/444 steps, doesn't distinguish train/val, lacks training loss curves, and "oscillation" has no formal definition (no rolling variance, no convergence criterion). Add complete curves, quantify oscillation (coefficient of variation), define convergence formally.

**SF-5. Two-tier hierarchy language overstates evidence [R1-W3, R2 REBUT -> compromise]**

R1 requests k-means/gap statistic validation. R2 rebuts: 7 data points make clustering unreliable; non-overlapping CIs already provide separation evidence. Director's resolution: "two-tier diagnostic hierarchy" should be downgraded to "two groups with non-overlapping CIs" or "observed pattern." Acknowledge CodeLlama loop_only is only +0.93pp above no_trace (n.s.), meaning Tier 2 may not exist for all models.

**SF-6. High no_trace baseline (93%+) under-discussed [R1-W2, R2 AGREE]**

Models predict 93% of verdicts from source code + test input alone. Trace's total incremental value is ~7pp (no_trace -> exception_only). This simultaneously weakens (small incremental value of traces) and strengthens (complete traces are worse than no traces) the narrative. The paper should explicitly discuss this tension.

**SF-7. Single dataset + universal claims [R8-N2, recurring from prior rounds]**

591 problems from HumanEval+MBPP (simple assert-based tests). Universal claims about trace representation don't match this narrow empirical base. DebugBench provides limited additional coverage (synthetic mutations, ceiling effects). Discussion should acknowledge dependence on test structure diversity.

**SF-8. Missing references [R9-W3, R2-W1, recurring]**

Beyond SF-1's theory references, also missing: Paul et al. (2021) "Deep Learning on a Data Diet," Sorscher et al. (2022) "Beyond Neural Scaling Laws" for data selection/pruning connections.

### Minor (5 issues)

**M-1.** Appendix B GPU model (RTX PRO 6000 Blackwell) may narrow anonymity. Obfuscate to "high-end datacenter GPU." [R10-M1, recurring]

**M-2.** Orphan bib entry `pornprasit2021jitline` still present. Bib key `qwen2025coder` should be `qwen2024coder` (year mismatch). [R-BIB, R9-M2, recurring]

**M-3.** Table 1 dagger annotation for single-seed entries is subtle. Mention in first text reference. [R11-W2, recurring]

**M-4.** Conclusion (§6) is minimal — 4 lines repeating core numbers. Consider adding 2-3 sentences on broader implications or concrete next steps. [R13-W1, R1 REBUT as minor]

**M-5.** Figure 2 (page 4) is cramped in single-column format. Consider `figure*` (full-width). Figure 5 (page 18) axis tick labels are small. [Visual check]

---

## Questions for Authors

1. **Marker removal experimental setup**: Is §3.3's marker removal (97.65%) train-without/test-without, or train-with/test-without? The latter would overestimate non-marker signal.

2. **Random gradient masking ablation** [R1-Q4]: Would you consider an ablation that randomly masks gradients on the same proportion of tokens as full_trace but retains exception_only content? This would cleanly isolate gradient dilution from content effects.

3. **Logistic regression baseline** [R1-Q5]: Has a simple logistic regression on exception presence/absence been tested? If it achieves 99%+, SFT's contribution would need further justification.

4. **Full_trace on DebugBench**: Why was full_trace not evaluated on DebugBench? This is the most direct test of the core claim's generalizability.

5. **Scaling behavior** [R1-Q3]: At 30B+ scale, do you expect full_trace degradation to persist? Larger models may have stronger noise filtering.

---

## Missing References

- Tishby, Pereira & Bialek (2000). The Information Bottleneck Method.
- Guyon & Elisseeff (2003). An Introduction to Variable and Feature Selection.
- Zhou et al. (2023). LIMA: Less Is More for Alignment.
- Paul, Ganguli & Dziugaite (2021). Deep Learning on a Data Diet.
- Sorscher, Geirhos, Shekhar, Ganguli & Morcos (2022). Beyond Neural Scaling Laws.

---

## External Review

**Status**: Not requested.

---

## Visual Layout Check (non-scoring)

| Severity | Page | Finding |
|----------|------|---------|
| Warning | 1-2 | 连续 2 页纯文本无 display item，第一个 Table 在 page 3，第一个 Figure 在 page 4。实证论文建议前 2 页内放置概览图或核心结果表。 |
| Warning | 21 | 尾页仅 ~25% 有内容，~75% 空白。建议重新分布 appendix 内容。 |
| Info | 4 | Figure 2（单栏 bar chart）字号偏小，4 组 × 多条件在单栏宽度下拥挤。建议 `figure*` 或简化分组。 |
| Info | 18 | Figure 5 reliability diagram subplot axis tick labels 较小，打印/缩放时可能不够清晰。 |
| Info | 1-8 | 主文 8 页共 6 个 display items（3 fig + 3 table），处于实证论文推荐密度（5-8）下限。 |

---

## Overall Assessment

**Score: 3.0 (Findings)**

**Reviewer scores**: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings).

**Director's rationale for 3.0:**

R1 correctly argues that full_trace degradation (-11.9pp vs no_trace) is independently non-trivial and not reducible to exception_only's format design. This partially salvages the novelty concern. However:

1. **Two of four contributions are structurally undermined.** C3 (decomposition) is confounded beyond repair without new experiments (random gradient masking or equivalent). C4 (two-pathway model) is a post-hoc narrative without direct evidence. Both reviewers reached this conclusion independently.

2. **The remaining contributions need significant reframing.** C1 ("complete traces impair SFT") is valid but the paper currently emphasizes "exceptions help" — the less interesting direction given B5's 99.31%. C2 ("exception events as minimal sufficient signal") faces the near-tautological concern: exceptions structurally encode verdicts.

3. **Statistical methodology gaps are fixable but currently present.** Multiple comparison correction (MF-3) and bootstrap independence violation (MF-4) don't threaten the main finding but undermine borderline claims that support the more nuanced contributions.

4. **Missing theoretical grounding.** The phenomenon maps directly onto classical ML results (information bottleneck, feature selection), but the paper frames it as novel without this connection.

The paper's experimental thoroughness (13-page appendix, comprehensive robustness checks) is genuinely impressive and exceeds most Findings-track papers. With major revision — reframing around "traces hurt" (not "exceptions help"), honest treatment of B5, downgrading decomposition/two-pathway to preliminary/hypothesis, adding theory connections, fixing statistics — the paper could reach Conference level. In its current form, Findings is the appropriate venue.

**Confidence**: High. Both reviewers converged on core issues independently; cross-sharing produced no fundamental disagreements.