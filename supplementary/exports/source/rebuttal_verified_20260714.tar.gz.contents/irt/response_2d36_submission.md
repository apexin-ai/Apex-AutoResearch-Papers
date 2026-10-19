# Response to Reviewer 2d36 -- SUBMISSION VERSION

We thank the reviewer for this rigorous and detailed evaluation. The five concerns address core methodological questions; we respond to each with existing evidence and concrete revision plans.

**W1: DIF causal over-claim / "not driven by contamination" too strong**

We agree. DIF is mechanism-agnostic by design (Sec. 5.1): it detects *that* items function differently, not *why*. We will revise to: "DIF flags are near-independent of web-overlap labels ($\phi$ = 0.012), suggesting that existing contamination proxies do not explain the observed instability"--throughout abstract, introduction, and conclusion. The mixed-mechanism analysis (Section B) provides one constructive constraint: tailored contamination schemes cannot replicate the near-zero instruct gradient (simulated r = -0.302 vs. observed -0.079), but we will frame this as "consistent with non-contamination drivers" rather than proving causation.

**W2: Non-independence / headline 31% vs. bracketed range**

We report three uncertainty layers: uncorrected 31.3%; simple-mean DEFF 29.2% ($\bar{m}$ = 62.8); weighted-mean DEFF 13.5% (Kish $\bar{m}$ = 254.5); **cluster bootstrap 95% CI [26.7%, 53.2%]**. The CI *excludes* 13.5%, providing model-independent evidence that the weighted-mean over-corrects. Size-stratified DEFF (Section C) reveals why: tier-level ICC decreases from 0.246 (families of 2-10) to 0.082 (>200 members); the 13.5% bound is driven entirely by two mega-families. We will revise the abstract to report the **13.5-29.2% bracketed range** with cluster bootstrap CI.

**W3: Cohort coarseness and confounders**

Calendar-year boundaries are coarse (Sec. 3.3). Four controls reduce confounders: (1) half-year C% = 34.4%, (2) base-only/instruct-only C% = 32.1%/36.5%, (3) within-architecture $\Delta$ = 1.08 pp, (4) within-family Llama-2 vs. 3 C% = 61.3%. These reduce, but do not eliminate, confounders from scale, training data, and evaluation practices. We will add a paragraph to Sec. 5.1 listing which confounders each control addresses vs. which remain, and discuss rolling-window protocols as future work.

**W4: "Score incomparability" framing too strong**

We agree the framing needs precision. The paper's own results show aggregate rankings are near-perfect ($\rho$ $\approx$ 0.997, $\tau$ = 0.962, flip rate $\leq$ 2.9%). The incomparability we document is item-level measurement non-invariance: individual items function differently across cohorts, but these effects largely cancel in aggregate. We will revise to distinguish explicitly: (a) item-level measurement non-invariance (31.3%, our primary finding), (b) individual model rank displacement ($\pm$561 positions at 99th percentile, which is real but rare), and (c) aggregate ranking stability ($\rho$ $\approx$ 0.997, preserved). The title "Temporal Score Incomparability" refers to (a), not (c); Sec. 5.2 will clarify this taxonomy.

**W5: ETS Category C thresholds from human testing**

We use ETS thresholds as standardized reference points, not as validated decision rules for LLMs (Sec. 3.2). Three empirical justifications support their applicability: (1) Random-split calibration: the 99th percentile |$\Delta$MH| under the null is 1.45, just below the ETS C threshold of 1.5, confirming the threshold separates signal from noise in this population. (2) Threshold sensitivity: qualitative conclusions hold across thresholds (18.4% at |$\Delta$MH| $\geq$ 2.0, 10.2% at $\geq$ 2.5; Sec. 4.2). (3) The dual criterion (effect size *and* significance) guards against unreliable large effects. We will add a paragraph in Sec. 3.2 making this justification explicit, and will note that a data-driven threshold calibration (e.g., from the random-split null distribution) is a valuable direction for future LLM-specific DIF work.
