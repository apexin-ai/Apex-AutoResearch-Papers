# Response to Reviewer NK3v -- SUBMISSION VERSION

We thank the reviewer for the careful reading and for accurately summarizing the MH-DIF methodology, cross-subject matching framework, and DIF-contamination independence finding.

**W1: DIF cannot identify causes (contamination vs. instruction tuning vs. architecture vs. prompt format)**

We fully agree, and this is by design: DIF is mechanism-agnostic (Sec. 5.1), detecting *that* items function differently, not *why*. Where we interpret DIF as "capability dimension shift," the evidence is the base-vs-instruct direction reversal ($\chi^2$ = 562.7) combined with the difficulty-direction interaction (r = -0.597): hard items favor 2024 models while easy items favor 2023 models, a structured pattern inconsistent with random noise. We acknowledge this is consistent with *multiple* mechanisms (capability evolution, post-training effects, format sensitivity) and will revise to present these as competing hypotheses rather than conclusions. The mixed-mechanism analysis (Section B) provides one constructive constraint: simulated contamination cannot replicate the near-zero instruct gradient (simulated r = -0.302 vs. observed -0.079), but this rules out one mechanism rather than confirming another.

**W2: Binary injection is stylized (too clean)**

We agree and explicitly acknowledge this in Sec. 3.4: "binary response flipping represents a stylized uniform injection pattern; realistic contamination (partial memorization, format-specific advantages) would produce weaker signals." To bound this concern, we report difficulty-dependent injection (Section A), which yields $\Delta$TPR $\approx$ 0.41 at p = 0.5 (vs. 0.51 for uniform), a $\sim$20% overestimation bound. The key insight is that the injection framework validates *detection power* (can MH-DIF detect differential behavior when present?), not contamination realism. The $\Delta$FPR = 0 guarantee under cross-subject matching holds regardless of injection mechanism, as it depends only on the matching variable construction. We will add a sentence in Sec. 3.4 clarifying that more realistic injection patterns (partial memorization, paraphrase-level familiarity) are a valuable extension.

**W3: Cross-subject matching assumes contamination is domain-limited**

The multi-subject injection analysis (Table 7) directly addresses this: $\Delta$FPR < 0.007 for k $\leq$ 5 contaminated subjects (out of 57), with graceful degradation beyond. At k = 20, $\Delta$FPR rises to 0.167--still insufficient to account for 31% C%. Only at k $\geq$ 30 (>50% of subjects) does matching break down. We will add a sentence in Sec. 3.4 stating the boundary condition more explicitly.

**W4: Need qualitative DIF item analysis**

We agree this would strengthen the interpretation. Existing results provide partial characterization: (1) STEM items are 55.4% focal-favoring while Humanities are 64.4% reference-favoring (Sec. 4.2). (2) The difficulty gradient (r = -0.597): hardest-decile C items are **88.7% focal-favoring vs. 96.2%** reference-favoring for easiest-decile (Section B). (3) Item-quality defects do not explain DIF (enrichment with MMLU-Redux error annotations = 1.10, 95% CI [0.92, 1.27]; Section B). However, item-level qualitative examples (specific questions, reasoning patterns, knowledge domains) showing reference- vs. focal-preferential behavior would add interpretive depth. We will add representative examples and a brief taxonomy of DIF item characteristics to the appendix.

**Comments (source distinction, non-MCQ benchmarks)**: We stratify by base/instruct (C% = 32.1%/36.5%; Section O) and by family (within-family Llama-2 vs. 3; DEFF correction and leave-one-family-out; Sec. 4.4). A closed-vs-open comparison is not available in this data: METABENCH is drawn from the Open LLM Leaderboard, which contains only open-weight models, so closed/API models are not represented -- we will state this scope boundary explicitly. Non-MCQ applicability is noted in Limitations as an important boundary.

**Planned revisions**: Soften mechanism interpretation in Sec. 5.1; add injection realism caveat to Sec. 3.4; clarify cross-subject matching boundary; add qualitative DIF item examples to appendix.
