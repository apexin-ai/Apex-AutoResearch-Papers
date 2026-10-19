# Response to Reviewer pZkb -- SUBMISSION VERSION

We thank the reviewer for the thorough and supportive evaluation, and for recognizing the cross-subject matching guarantee and cross-benchmark replication as substantive contributions.

**W1: "Not driven by contamination" framing too strong**

We agree. The abstract will be revised to: "DIF flags are near-independent of web-overlap labels ($\phi$ = 0.012), suggesting that existing contamination proxies do not explain the observed instability." This more precise phrasing acknowledges that web-overlap labels are a noisy proxy for training-set membership and that near-independence with this proxy does not rule out non-verbatim contamination pathways. The same softening will apply throughout (introduction, conclusion).

**W2: Headline 31% vs. DEFF-bracketed range**

The abstract will be revised to report the DEFF-bracketed range: "**13.5-29.2% of items exhibit large temporal DIF** (cluster bootstrap 95% CI: [26.7%, 53.2%])." The current section title (Sec. 4.2) already reads "$\sim$29% of Items"; the revision brings the abstract into alignment with the body text. The wide bracket reflects the uncertainty in effective sample size under family structure--the cluster bootstrap CI excludes 13.5%, suggesting the weighted-mean DEFF over-corrects (driven by two mega-families; see Section C for size-stratified analysis).

**Citation: Fluid Language Model Benchmarking (COLM 2025)**

We thank the reviewer for this pointer. This work shares our motivation of bringing psychometric methodology to LLM evaluation, using IRT as its foundation. We will cite it in Sec. 2 (Related Work) and briefly discuss the complementarity: their focus is on IRT-based adaptive testing efficiency, while ours is on measurement invariance testing via DIF. Both contribute to the broader agenda of psychometric monitoring for LLM benchmarks.

**Planned revisions**: Soften contamination framing (abstract, Sec. 1, Sec. 6); report DEFF-bracketed range in abstract; add Fluid LM Benchmarking citation in Sec. 2.
