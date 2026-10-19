# Response to Reviewer Eav4 -- SUBMISSION VERSION

We thank the reviewer for recognizing that our work tests a foundational assumption (measurement invariance) that IRT-for-LLM literature has largely taken for granted, and for the detailed engagement with both strengths and limitations.

**W1: Psychometric analogy boundaries need deeper discussion**

We agree the analogy deserves more scrutiny. The reviewer identifies three violations: (1) convenience collection, (2) unclear "ability" definition, and (3) family-level dependence exceeding ICC assumptions.

Our response: the MH procedure's validity depends on *stratification adequacy*, not on the stronger assumptions of IRT model fit or random sampling. Specifically, MH-DIF requires only that the matching variable (total score) adequately captures the latent trait for stratification purposes. We verify this empirically: IRT $\theta$ correlates at **r = 0.9986** with total scores (Sec. 3.2), and K = 3 vs. K = 5 strata yield near-identical power (TPR difference < 0.02; Section A). For non-independence, DEFF correction reduces effective N per item (Section C), the cluster bootstrap provides non-parametric uncertainty (CI: [26.7%, 53.2%]), and graduated de-duplication confirms family structure does not inflate C% (Sec. 4.4). For multidimensionality, domain-level ability profiles are nearly flat across cohorts (Cohen's d range = 0.12; Table 6), and cross-subject vs. within-subject matching agree ($\kappa$ = 0.80).

The reviewer is right that Sec. 3.2 treats these as technical corrections when they deserve a more principled discussion of *where the analogy holds and where it breaks down*. We will add a paragraph to Sec. 5 discussing: (a) what MH-DIF does *not* require (random sampling, unidimensional IRT fit, independence), (b) what it *does* require (adequate stratification, which we verify), and (c) the remaining gap (family structure is partially but not fully addressed by DEFF).

**W2: "Diagnostic lens" overclaim / AUROC = 0.60**

We agree the Monitor/Triage/Correct protocol is somewhat generic. But we note that **AUROC = 0.60 is itself a finding**, not just a limitation: it means unstable items are *emergent cohort-item interactions* that cannot be predicted from item properties alone--they are not "bad items" in a fixed sense (Sec. 5.2). The low predictability precisely motivates *post-hoc auditing* (DIF analysis after deployment) over *pre-screening* (filtering items before use). We will revise Sec. 5.2 to: (a) state this explicitly, (b) acknowledge the domain-level diagnostic (STEM favors 2024, Humanities favors 2023) is coarse, and (c) frame the audit protocol as a *monitoring framework* rather than a *diagnostic tool*, which better matches what the evidence supports.

**W3: Missing citations (ATLAS, Benchmark$^2$)**

We thank the reviewer for these pointers. ATLAS (Li et al., arXiv:2511.04689) applies IRT-based adaptive testing to the same METABENCH data, making it directly relevant. Benchmark$^2$ (Qian et al., arXiv:2601.03986) addresses benchmark evaluation quality more broadly. We will cite both in Sec. 2 and discuss complementarity: ATLAS focuses on efficient scoring assuming measurement invariance; we test whether that assumption holds. If it does not (as our results suggest), adaptive testing protocols may need to account for item instability across cohorts.

**W4: Temporal resolution coarse / rolling-window**

We already include a half-year comparison (C% = 34.4%; Sec. 3.3) that shows DIF persists under finer temporal slicing. This suggests the instability accumulates rather than appearing as a discrete jump. A full rolling-window analysis would further clarify temporal dynamics--we will discuss this as a concrete next step in Sec. 5 and note the practical constraint: METABENCH release dates have limited granularity (monthly at best), setting a floor on temporal resolution. Base-only and instruct-only analyses (C% = 32.1%/36.5%; Sec. 3.3) provide type-specific temporal signals that complement a rolling-window approach.

**Planned revisions**: Add analogy-boundary discussion to Sec. 5; reframe audit protocol as monitoring; cite ATLAS and Benchmark$^2$ in Sec. 2; add rolling-window discussion to Sec. 5.
