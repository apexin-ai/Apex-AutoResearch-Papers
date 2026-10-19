# Response to Reviewer jRZT -- SUBMISSION VERSION

We thank the reviewer for engaging deeply with the statistical methodology. We address each concern below and begin with an important factual correction.

**Datasets = 1: Factual correction**

The submission includes both code and data access. The anonymous repository link appears on page 1 (footnote): https://anonymous.4open.science/r/irt_equated_bench_regen-2431/. The repository contains 90+ analysis scripts, figure generation code, and instructions for reproducing the response matrix from METABENCH. Furthermore, our analysis spans six benchmarks (MMLU, ARC, HellaSwag, WinoGrande, TruthfulQA, GSM8K; Table 2), not one. We respectfully ask the reviewer to reconsider the Datasets score in light of these materials.

**W1: Headline 31% and non-independence**

We agree the headline number requires context. The DEFF-bracketed range is **13.5-29.2%**, and the cluster bootstrap 95% CI is [26.7%, 53.2%]. Importantly, the CI *excludes* 13.5%, providing model-independent evidence that the weighted-mean DEFF over-corrects. Size-stratified analysis (Section C) explains why: the conservative bound is driven entirely by two mega-families; at small family sizes, DEFF has negligible impact (Adj. C% = 31.3%). The abstract will be revised to report the bracketed range. Regarding MH $\chi^2$ independence: DEFF divides each item's $\chi^2$ by its item-specific design effect before re-applying ETS thresholds (Section C); the cluster bootstrap provides a complementary non-parametric bound. We additionally note the random-split baseline (C% = 0.62%) as an empirical null: even the most conservative estimate (13.5%) is **22$\times$ above this baseline**.

**W2: Web-overlap proxy weakness**

We agree that near-independence with web-overlap labels is consistent with multiple interpretations, including that "2024 models contaminate via non-verbatim pathways." This is precisely why we frame DIF as *complementary* to contamination detection (Sec. 1, Figure 2), not as a contamination test. The base-vs-instruct direction reversal ($\chi^2$ = 562.7) provides label-independent evidence: if contamination were the sole driver, base and instruct models trained on similar corpora should exhibit similar DIF directions, not opposite ones. Mixed-mechanism injection cannot replicate this pattern (simulated instruct r = -0.302 vs. observed -0.079; Section B). We will soften "not driven by contamination" to "not explained by existing web-overlap labels" throughout.

**W3: Cohort coarseness and confounders**

Four controls in the paper reduce these confounders: half-year comparison (C% = 34.4%; Sec. 3.3), base-only/instruct-only analyses (C% = 32.1%/36.5%; Sec. 3.3), within-architecture analysis ($\Delta$ = 1.08 pp; Sec. 5.1), and within-family comparison (Llama-2 vs. 3, C% = 61.3%; Table 1). These controls reduce, but do not eliminate, confounding from scale, training data, and evaluation practices--as we acknowledge in Limitations. We will add a paragraph to Sec. 5.1 explicitly listing residual confounders and discuss rolling-window protocols as future work.

**W4-W5: Limited practical stakes / diagnostic deflation**

The reviewer identifies a genuine tension. Our resolution: item-level measurement non-invariance (31.3%) coexists with aggregate ranking stability ($\rho$ $\approx$ 0.997). This is not self-undermining--it is the core finding: DIF isolates *differential* signal that cancels in aggregate but is real at the item level (individual models shift by $\pm$561 positions at the 99th percentile; Section K). The "diagnostic lens" framing acknowledges that DIF reveals *structured signal* (STEM favors 2024, Humanities favors 2023) without claiming causal identification. We will revise Sec. 5.2 to clarify this nuance and distinguish item-level non-invariance from aggregate invalidity.

**Planned revisions**: Soften contamination framing; report bracketed range in abstract; add confounder-residual discussion to Sec. 5.1; clarify incomparability taxonomy in Sec. 5.2.
