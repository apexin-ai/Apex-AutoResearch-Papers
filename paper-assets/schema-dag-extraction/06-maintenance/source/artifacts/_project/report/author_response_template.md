# Author Response Template — Schema-DAG-Extraction

Prepared 2026-05-22. Based on v34+ paper (post semipartial R² fix, post cross-model error taxonomy). Covers 5 anticipated attack surfaces from R29.

---

### Q1: BCS scope limited to FewRel RE

**Anticipated Reviewer Question**: "BCS batch-level prediction only works on FewRel RE. The generalizability of your confusability framework is questionable."

**Response Draft**:

> Thank you for this important point. Our design deliberately uses FewRel as the primary testbed for batch-level BCS analysis because its balanced design (700 instances per type) and low multicollinearity (VIF = 1.18; §4.3) cleanly isolate the confusability effect — semipartial R² = 0.273 after partialing centrality. DocRED shows directional consistency (ridge β\_BCS < 0 across all λ ≥ 0; Appendix E.1), but VIF = 50.9 prevents reliable quantification; we explicitly report this as directional evidence (§4.3). The NER batch-level null is consistent across three models (Qwen3-32B, LLaMA-8B, LLaMA-70B) and two prompts, with power analysis confirming minimum detectable |r| ≈ 0.132 (Appendix D.4). Crucially, the *pairwise* confusability signal generalizes across all three tasks: Few-NERD r = 0.112 [0.076, 0.156], MAVEN r = 0.129 [0.104, 0.156] (Table 2), both CIs excluding zero. The NER–RE asymmetry has a structural explanation: NER errors distribute across miss (43–65%), boundary, and type substitution modes rather than concentrating in type confusion (Appendix D.3). Using FewRel to establish the clean effect and other datasets to characterize boundary conditions is a principled analytical strategy, not a limitation of the metric.

---

### Q2: DocRED VIF = 50.9

**Anticipated Reviewer Question**: "DocRED's VIF is 50.9. How can you trust any partial correlation or regression result on this dataset?"

**Response Draft**:

> We agree that VIF = 50.9 renders standard partial correlations unstable on DocRED, and we take three precautions. First, the main text explicitly frames DocRED as "directional evidence that the BCS–accuracy relationship extends beyond FewRel's schema, not as independent quantitative support" (§4.3). Second, we report semipartial R²\_BCS = 5.6% after partialing degree centrality, transparently noting that ~90% of explained variance is shared with centrality (§4.3). Third, ridge regression across a range of λ values confirms the BCS coefficient remains negative (Appendix E.1), establishing directional robustness under regularization. All quantitative claims for BCS's independent contribution rest on FewRel, where VIF = 1.18 and semipartial R² = 0.273 (§4.3). We believe transparently reporting the DocRED collinearity — rather than omitting the dataset — strengthens the paper by showing both where the signal is clean and where BCS and centrality cannot be isolated.

---

### Q3: TOST logit-scale inconclusive

**Anticipated Reviewer Question**: "Dimensional separability only holds on the linear scale. The logit-scale TOST is inconclusive (p = 0.209). Aren't logit transforms standard for bounded accuracy data?"

**Response Draft**:

> We designate probability-scale TOST as the primary analysis because practitioners interpret accuracy differences directly — a 3 pp gap has immediate practical meaning — and our accuracy values (0.37–0.86) remain in the mid-range where logit and linear scales yield similar inference (§4.4). The interaction point estimate is 0.47 pp, well within the ±3 pp equivalence margin on both scales. The logit inconclusive result (p = 0.209; regression-based: p = 0.050; Appendix C) reflects logit variance inflation in the 0.37–0.86 range rather than a qualitative divergence (Limitations §1). Margin sensitivity analysis (Table 7) shows equivalence holds from ±2 pp (p = 0.047) through ±5 pp, confirming the ±3 pp choice does not drive the conclusion. On DocRED, range-matched analysis reduces the raw interaction from −9.4 pp to 0.93 pp (CI [−7.13, 7.44]; Appendix C). We qualify our claim as "approximately additive on the probability scale" and report the logit limitation explicitly (§4.4, Limitations §1).

---

### Q4: NER batch-level null

**Anticipated Reviewer Question**: "BCS has no predictive power for NER. Doesn't this undermine the generality of your confusability framework?"

**Response Draft**:

> Three models (Qwen3-32B, LLaMA-8B, LLaMA-70B) × two prompt variants consistently show no batch-level BCS–F1 correlation for NER (r ≈ 0, n = 450; Table 5, §4.3). Power analysis shows minimum detectable |r| ≈ 0.132 at α = 0.05, power = 0.80 (Appendix D.4). Two structural factors explain the asymmetry. First, NER errors distribute across miss (43–65%), boundary, and type substitution modes rather than concentrating in type confusion — relaxed matching confirms this is not a metric artifact (Appendix D.3). Second, BCS range compression (SD ratio 19% of FewRel's) limits signal-to-noise. Importantly, the *pairwise* SCS signal is significant for NER (r = 0.112, p < 0.001; Table 2), and IntraSub scales monotonically with BCS (ρ = 1.0; Figure 2). The framework's contribution is characterizing *when* confusability aggregates to batch-level prediction (RE) and *when* dispersed error modes prevent aggregation (NER). We explicitly frame this as "absence of evidence rather than evidence of absence" (§4.4).

---

### Q5: "First controlled study" claim

**Anticipated Reviewer Question**: "The claim of being the 'first controlled study' seems overclaimed. How does this differ from LLM-PEE, GoLLIE, or Reflect-then-Learn?"

**Response Draft**:

> We scope this claim carefully: "the first controlled study simultaneously isolating type count and inter-type confusability as independent dimensions via embedding-based metrics and stratified batch design in zero-shot LLM IE" (§1). Each prior work addresses a distinct goal without this controlled isolation. LLM-PEE (Chen et al., 2025) uses embedding similarity to *partition* schemas for improved extraction — an engineering solution that conflates count and confusability without controlled manipulation (§2). GoLLIE (Sainz et al., 2024) explores instruction-based annotation guidelines without isolating count from confusability as independent experimental dimensions. Reflect-then-Learn (Chen et al., 2026) selects in-context examples via introspective confusion but does not employ BCS-controlled batch design that varies confusability while holding count fixed. Our methodological contribution — BCS-controlled batches enabling the factorial analysis (§4.4) and R² attribution (§4.3) — is what prior work could not perform. We already use the qualifier "to our knowledge" in the abstract and would welcome the reviewer identifying any prior study achieving this specific controlled isolation.
