---
dream_id: dream_20260520T185641
tier: median
overall_score: weak reject
timestamp: 2026-05-20T19:54:05.357365+00:00
---

# Reviewer 2 (R2): Novelty and Related Work

## Summary
The paper systematically evaluates whether English-trained correctness probes transfer cross-lingually, testing 3 architectures, 20-52 languages, and 5 transfer conditions. The main findings are largely negative: zero-shot transfer fails for most languages, CaCLR's consistency loss is inert, and simple linear projection matches or beats the proposed method. The paper frames itself as a "field-level diagnostic."

## Strengths

**S1. Genuine gap identification.** No prior work has tested correctness probe transfer at this scale. Xiao et al. (2025) probed answerability (input-level), not correctness (output-dependent). The distinction is meaningful and well-articulated.

**S2. Thorough experimental design.** 3 architectures spanning MoE and dense, 5 transfer conditions forming a natural hierarchy of supervision, and extension to 52 languages. The Pareto frontier analysis (depth vs. transferability) is a useful conceptual contribution.

**S3. Honest negative results.** The CaCLR inertness finding (beta sweep over 3 OOM with <0.3pp change) is valuable. The community benefits from knowing that naive consistency regularization does not solve cross-lingual probe transfer.

**S4. Orthogonality extension.** Extending Miao & Ungar's English-only orthogonality finding to 20 languages with a resource-tier gradient (high: 0.054, low: 0.098) adds empirical substance to a mechanistic claim.

## Weaknesses

**W1. Limited novelty beyond scale.** The core finding — that probes trained on high-resource language representations degrade on low-resource languages — is highly predictable from domain adaptation theory. Ben-David et al. (2010) established that transfer degrades proportionally to distribution divergence. The paper lacks any formal connection to this theory, which could have predicted the resource-tier gradient a priori.

**W2. CaCLR is simultaneously the method contribution and a negative result — this is incoherent framing.** If the consistency loss is inert across 3 OOM of beta, CaCLR reduces to L_BCE + alpha*L_SB-ECE, which is just calibration-regularized logistic regression. Calling this "CaCLR" and positioning it as a method contribution when its distinguishing component (L_consistency) provably does nothing is misleading. The paper should either (a) present CaCLR as purely a negative result, or (b) explain why the consistency term fails and propose a fix.

**W3. Missing related work — representation alignment literature.** The paper ignores the extensive cross-lingual representation alignment literature:
- **MUSE / VecMap** (Conneau et al. 2018, Artetxe et al. 2018): Linear projection for cross-lingual alignment is well-studied; the finding that linear projection "matches or beats CaCLR" is unsurprising given this literature.
- **CKA/SVCCA for cross-lingual analysis** (Kudugunta et al. 2019, Muller et al. 2021): Representation similarity metrics that quantify when/why cross-lingual transfer degrades — directly relevant to explaining the Pareto frontier.
- **Probing methodology critiques** (Hewitt & Liang 2019 control tasks, Voita & Titov 2020 MDL probes): The paper uses vanilla logistic regression probes without discussing selectivity or information-theoretic controls. High AUROC may reflect memorized dataset artifacts rather than genuine "correctness directions."

**W4. No mechanistic explanation for WHY transfer fails.** The paper documents transfer failure and correlates it with resource tier, but never explains the mechanism. Is it because low-resource representations occupy different subspaces? Because the correctness direction rotates? Because probe confidence is miscalibrated due to representation density differences? CKA analysis between English and target-language representations at each layer would directly answer this.

**W5. "Difficulty-capability entanglement" finding is under-theorized.** Projecting out difficulty hurts by 1.3-1.4pp, contradicting prior English-only work. But why? Is it because difficulty and correctness are more entangled in multilingual settings (e.g., translation quality confounds difficulty), or because the IRT difficulty estimates themselves are less reliable cross-lingually? Without this analysis, the finding is descriptive rather than explanatory.

**W6. Missing calibration alternatives.** Conformal prediction (Angelopoulos & Bates 2023) provides distribution-free coverage guarantees that are inherently language-agnostic. This is a serious omission — if the goal is reliable uncertainty for non-English users, conformal methods may dominate without requiring any representation analysis.

## Questions for Authors

Q1. What is the actual CaCLR contribution if L_consistency is inert? Is L_BCE + alpha*L_SB-ECE (minus consistency) itself novel, or is it standard calibration-regularized training?

Q2. Have you measured cross-lingual representation similarity (CKA) at each layer? This would directly explain the Pareto frontier mechanistically.

Q3. The 52-language extension shows 0% pass rate for very-low resource languages. Does this merely reflect poor base model performance (low accuracy = no signal to calibrate), or genuine representation misalignment? What are the base accuracies?

Q4. How do you ensure probing AUROC reflects a genuine correctness direction vs. dataset artifacts? Any control task analysis (Hewitt & Liang 2019)?

Q5. Why not compare against conformal prediction, which provides language-agnostic coverage guarantees without probing?

## Minor Issues

- The cross-architecture agreement tau=0.33 is low but not contextualized — what would random agreement be? What does this imply practically?
- "Pass rate" thresholds (AUROC>=0.65) seem arbitrary. Sensitivity analysis needed.
- Paper targets EACL but the scale (3 architectures, 52 languages) seems designed for a broader venue. The mismatch between ambition and venue is confusing.

## Score: 3 (Weak Reject)

**Justification:** The paper fills a genuine empirical gap and the negative results are informative. However, the novelty is limited: (1) the main finding (transfer fails for low-resource languages) is predictable from first principles and domain adaptation theory; (2) the method contribution (CaCLR) is self-defeating since its novel component is experimentally inert; (3) significant related work is missing (alignment literature, probing critiques, conformal prediction); (4) the paper is descriptive rather than explanatory — it documents what happens without explaining why at a mechanistic level. For a top venue (~25% acceptance), I expect either a strong positive method contribution OR deep mechanistic insight. This paper offers neither — it is a competent empirical survey with negative results but insufficient theoretical depth to compensate. The "field-level diagnostic" framing is partially convincing but needs the missing mechanistic analysis (W4) to truly close the question rather than merely report failure.
