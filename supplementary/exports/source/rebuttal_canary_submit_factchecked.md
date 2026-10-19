# Submission Version -- OpenReview Per-Reviewer Threads

> Paste each section below into the corresponding reviewer thread on OpenReview.
> Character counts verified with `wc -m` (target <= 4250 per thread).

---

## -> Thread: Response to Reviewer gjTb

We thank Reviewer gjTb for the detailed evaluation and the recognition of our early-signal identification and cross-model generalizability.

**The non-monotonic dose-response is our central finding, not evidence against the paper's claims (G2).**

Our paper does not claim that detection rate increases monotonically with $\alpha$. The non-monotonic pattern is one of our core contributions (contribution 2, Sec. 1). PermG dose-response across the 13-point $\alpha$ sweep:

| $\alpha$ | $\leq 0.45$ (5 values) | 0.50 | 0.60 | 0.75 | 1.00 |
|---|---|---|---|---|---|
| PermG sig. pairs | 0/8 | 6/8 | 0/8 | 5-6/8 | 6/8 |

All replicated across 2-3 independent seeds. This pattern is predicted by our $S \times R$ competition framework (Sec. 4.4): signal strength $S(\alpha)$ increases monotonically, but temporal resolution $R(\alpha)$ drops at $\alpha \approx 0.60$ when canary and downstream collapse simultaneously (zero-lag synchronization; Deshpande et al., 2010), destroying the lag structure Granger tests require. Detectability $\propto S(\alpha) \times R(\alpha)$ produces four regimes: blind, onset, sync dip, detection plateau. Non-monotonic dose-response is a recognized cross-disciplinary phenomenon (hormesis; Calabrese and Baldwin, 2003).

The sync dip at $\alpha = 0.60$ is confirmed across all three fp32 seeds on Pythia-410M (0/8); it is architecture-dependent -- on Pythia-1.4B the dip does not appear (4/6 at T=10) -- consistent with $R(\alpha)$ depending on model dynamics. Bidirectional differenced cross-correlation (DiffXCorr) still detects 6/8 pairs at $\alpha = 0.60$, confirming the signal exists but PermG cannot capture it under synchronous collapse.

We recognize the manuscript presents dose-response data before the explanatory framework, likely causing this reading. **Revision plan**: reorder Sec. 4 to introduce $S \times R$ intuition before dose-response results.

**Steep onset rests on model-free evidence, not sigmoid fitting (G1).**

We agree the sigmoid should not bear the primary argumentative weight and will reframe it as a descriptive summary. Model-free evidence for steep onset:

1. Fisher's exact test: 0/64 sig. pairs at $\alpha \leq 0.45$ vs. 18/32 at $\alpha \geq 0.50$ (excl. sync-dip $\alpha = 0.60$). **$p = 3.45 \times 10^{-11}$** -- no parametric assumption.
2. Bootstrap transition width: **$\Delta\alpha = 0.022$** (median; 95% CI [0.008, 0.060]). The $\alpha_c$ location CI [0.43, 0.56] is 6x wider -- position is uncertain, but the transition is sharp.
3. Raw pattern: five consecutive $\alpha$ values (0.25-0.45) yield 0/8, with sub-threshold p-values at $\alpha = 0.45$ (FDR $p = 0.059$-$0.091$) confirming proximity to the boundary; detection jumps to 6/8 at $\alpha = 0.50$, replicated across three fp32 seeds.

The sigmoid-data discrepancy at $\alpha \approx 0.60$ is the sync dip -- a distinct mechanism from the onset. **Revision plan**: (1) Fisher exact as primary evidence; (2) sigmoid labeled as descriptive convenience; (3) bootstrap $\Delta\alpha$ as sharpness measure.

**Planned revisions for Minor items**: (G3) Sec. 5 will add a "Practical Relevance" paragraph mapping regimes to deployment scenarios -- self-instruct pipelines, iterative RLHF, web-scale contamination, data flywheel products -- and clarifying the framework as a confirmation tool; the blind zone (~40% diversity loss undetectable) itself motivates data provenance. (G4) All symbols (PermG, FPR, FDR, ECE, MMCT, $S \times R$) will be defined at first use in Sec. 1-5; all figure/table captions will include metric descriptions.

---

## -> Thread: Response to Reviewer ohXJ

We thank Reviewer ohXJ for the thorough evaluation and recognition of our study's breadth and practical insights.

**Detectability regimes map to practical LLM training scenarios (O1).**

We agree this connection should be more explicit:

| Regime | $\alpha$ range | Practical implication |
|---|---|---|
| Blind zone | < 0.50 | ~40% diversity loss undetectable; data provenance essential |
| Onset | ~0.50 | Monitoring becomes actionable (PermG 6/8) |
| Sync dip | ~0.60 | Single-threshold monitoring misses this regime |
| Plateau | $\geq 0.75$ | Framework serves as confirmation tool |

Concrete scenarios where $\alpha \geq 0.50$ arises: (1) self-instruct / synthetic augmentation (often >50% synthetic); (2) iterative RLHF / self-play where synthetic fraction accumulates; (3) web-scale contamination with growing AI-generated content; (4) data flywheel products. The framework is a confirmation tool, not a universal early-warning system (Sec. 1). The blind zone is itself actionable: it demonstrates a fundamental detection lower bound, motivating complementary approaches (provenance, watermarking). **Revision plan**: add a dedicated "Practical Relevance" paragraph in Sec. 5 with these scenarios and scope clarification.

**Canary signals require negligible overhead (O2).**

- Computation: single forward pass over a held-out set -- negligible vs. a training epoch
- Temporal lead: $\geq 1$ generation ahead, available during the current training cycle
- Efficacy: early cessation (15% entropy threshold) reduces peak perplexity by **64%** (56.99 vs. 157.09 reactive at $\alpha = 1.0$; Sec. 4.6); a two-seed fp32/bf16 bootstrap gives a 95% CI of [28.5%, 63.7%], intervening 1 generation before reactive approaches

**Planned revisions for Minor items**: (O2) computation/integration paragraph in Sec. 5; (O3) Sec. 3.3 method comparison consolidated into summary table, per-method detail to Appendix; (O4) Figure 1 redesigned with labeled regime boundaries, caption reading guide, and repositioned to page 1 (or nearest feasible placement under the ACL template); (O5) citations added for SmolLM, OPT, Qwen, WikiText-103, C4; (O6) figure/table proportions unified throughout.

---

## -> Thread: Response to Reviewer fbQy

We thank Reviewer fbQy for the positive assessment and recognition of our research questions' novelty.

**All abbreviations will be defined at first use (F1).**

| Abbreviation | Definition |
|---|---|
| ECE | Expected Calibration Error -- predicted confidence vs. actual accuracy |
| FDR | False Discovery Rate -- Benjamini-Hochberg multiple-testing correction |
| FPR | False Positive Rate -- incorrect detections in null-control experiments |
| PermG | Permutation Granger -- permutation-based temporal precedence test |
| MMCT | Multi-Method Consensus Test -- five-method FPR-inverse-weighted framework |

**Planned revision**: full definition audit across Sec. 1-5 + expanded figure/table captions with metric descriptions.
