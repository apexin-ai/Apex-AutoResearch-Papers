---
dream_id: dream_20260516
tier: median
overall_score: 4 - Weak Accept
timestamp: 2026-05-16T15:31:53.142238+00:00
---


# Review Report — Reviewer R2 (Novelty, Related Work, Significance)

## Paper: "The Redundancy-Stability Tradeoff: Why CKA-Aware Pruning Helps SFT but Breaks RLVR in Reasoning Models"

---

## Summary

This paper introduces RASP, a CKA-based structural pruning scoring function, and uses it to reveal the "Redundancy-Stability Tradeoff": structures that are safely removable under SFT recovery are precisely those needed for RLVR (GRPO) training stability. The core empirical finding is that GRPO never improves reasoning accuracy on any model (reward-accuracy decoupling), and that structural pruning induces training collapse whose severity correlates with the degree of redundancy removal (RASP collapses at step 10, Standard at step 60, unpruned never). The paper reframes RASP as a diagnostic tool rather than a universally superior pruning method.

---

## Strengths

- **Genuinely novel observation**: The finding that GRPO training collapses on structurally pruned models, with collapse speed monotonically related to redundancy removal, has no direct precedent in the literature. The "Redundancy-Stability Tradeoff" — that SFT-optimal and RLVR-optimal pruning decisions are fundamentally opposed — is a conceptually clean and surprising insight.

- **Well-designed diagnostic narrative**: The paper does not oversell RASP as a method. Using it as a controlled probe to reveal the tradeoff is intellectually honest and more interesting than a "new SOTA" claim would be. The pivot from "RASP enables better recovery" to "RASP reveals a fundamental tension" is well-executed.

- **Rigorous falsification of prior claims**: The reconciliation with Self-Healing (Zhang et al., 2025) — showing that unstructured pruning (as Self-Healing uses) does not trigger GRPO collapse while structural pruning does — is a valuable clarification that resolves an apparent contradiction in the literature.

- **Clean experimental controls**: The three-way comparison (RASP/Standard/Unpruned) under identical GRPO configurations isolates the pruning strategy as the causal variable. The unpruned control definitively establishes pruning-specificity of the collapse phenomenon.

- **Reward-accuracy decoupling finding**: The observation that unpruned GRPO achieves reward 0.661 with literally zero accuracy change (identical 1072/1319 correct before and after) is striking and independently interesting, contributing to the growing literature on reward hacking in RLVR.

---

## Weaknesses

### Major

1. **Extremely narrow model scale (Major)**: Two 7B models from the same architecture family (Qwen-based). The "Redundancy-Stability Tradeoff" is claimed as a general principle, but there is zero evidence it holds at 13B, 32B, or 70B. Larger models have substantially more redundancy — the tradeoff dynamics could be qualitatively different. For a venue with 25% acceptance, a single scale point is a significant limitation for a paper making general claims about "reasoning models."

2. **Single benchmark, single RL algorithm (Major)**: GSM8K is the only evaluation benchmark; GRPO is the only RL algorithm tested. The claim "RLVR breaks" should be tested with PPO, DPO, or REINFORCE. GSM8K is a relatively easy math benchmark — would the same collapse occur on MATH, AIME, or code generation tasks? The paper's strongest claims (C1: "universal") are dramatically under-supported.

3. **GRPO run for only 100 steps with no hyperparameter search for stability (Major)**: The collapse at step 10/60 could potentially be mitigated by lower learning rates, warmup schedules, KL penalty tuning, or curriculum strategies. The paper reports a single configuration and declares GRPO "broken." This is premature — it may be that GRPO on pruned models simply requires different hyperparameters. The extensive decision log (D002-D032) reveals that the authors struggled with 7+ failed GRPO configurations before finding one that ran at all, suggesting the collapse may be partly a tuning issue rather than a fundamental impossibility.

4. **SFT advantage not statistically significant (Major for C3)**: The paper's Claim 3 ("Recovery paradigm conditions optimal pruning") relies on RASP having a SFT advantage. But the full N=1319 eval shows RASP 61.49% vs Standard 59.29% with p=0.25. The "+5.75pp at 25% sparsity, p=0.008" is from a different sparsity level and possibly different sample size. The claim that RASP "helps SFT" is on shaky statistical ground at the primary 20% sparsity setting.

5. **No proposed solution or mitigation (Major for significance)**: The paper identifies a problem but offers no path forward. A diagnostic contribution is valuable, but for a top venue, the lack of any attempted mitigation (e.g., modified GRPO with redundancy-aware constraints, progressive unfreezing, or the RASP-RLVR variant mentioned in the report) weakens practical impact. The RASP-RLVR experiment (D047) was planned but results are not included.

### Minor

6. **Only ~10 references in the paper (Minor)**: The literature map shows awareness of 40+ relevant papers, but the paper itself cites only ~10. For a paper making broad claims about pruning-alignment interaction, key missing citations include: FANG (function-aware neuron grouping), FuncNet (functional network preservation), Davari et al. (CKA reliability limitations), "From LLMs to LRMs" (width vs depth for reasoning), "Doing More With Less" (pruning and test-time scaling), and RestoreLCC (alternative recovery paradigms). This sparse citation density will appear under-contextualized to reviewers.

7. **CKA reliability not discussed (Minor)**: Davari et al. (ICLR 2023) showed CKA can be manipulated without changing functional behavior and is sensitive to outliers. The paper should acknowledge why these failure modes don't invalidate the intra-model application here.

8. **Sparsity range limited (Minor)**: Only 20% and (partially) 25% sparsity tested. The U-shape in alpha ablation and the transition from "no collapse" to "collapse" likely have interesting dynamics across the 15-40% range that are unexplored.

9. **Per-structure regression evidence is weak (Minor)**: r=-0.42 and r=0.55 correlations are moderate at best. With how many data points? If this is across ~92 MLP groups within a single model, the effective degrees of freedom may be limited due to layer-level structure.

---

## Questions for Authors

1. Have you attempted GRPO with substantially lower learning rates (e.g., 10x reduction), gradient clipping, or progressive unfreezing? How confident are you that the collapse is fundamental rather than a hyperparameter sensitivity issue specific to pruned models?

2. The unpruned model shows identical accuracy before and after GRPO (81.27%, same 1072/1319 correct). Does this suggest the GRPO+GSM8K+greedy evaluation pipeline itself is insensitive, rather than revealing something about pruning? Have you checked with sampling-based evaluation (pass@k)?

3. What is the causal mechanism by which removing "redundant" structures (high CKA overlap) destabilizes RL training? Is it that these structures provide gradient diversity, policy exploration capacity, or simply numerical stability through parameter redundancy?

4. The Self-Healing comparison states their method uses "unstructured" pruning. Have you verified this is the source of the divergence, e.g., by running unstructured pruning at 20% and confirming no GRPO collapse?

5. The 25% sparsity result (p=0.008) — how many subjects/comparisons went into this? Is there a multiple comparisons correction issue given that 20% sparsity showed p=0.25?

6. Would the findings hold with DPO or offline RL methods that don't require online generation? The collapse mechanism seems tied to GRPO's reliance on model-generated rollouts.

---

## Missing Related Work

1. **FANG (Yu et al., 2025)** — Function-aware neuron grouping for structured pruning. Closest conceptual parallel to CKA-based functional analysis; should be discussed as related method.

2. **Davari et al. (ICLR 2023)** — "Reliability of CKA as a Similarity Measure." Must-cite for honest CKA justification and limitations discussion.

3. **"From LLMs to LRMs" (Ding et al., 2026)** — Width vs depth pruning for reasoning models. Directly motivates the structural pruning focus.

4. **"Doing More With Less" (2026)** — Shows structured pruning degrades test-time scaling while unstructured doesn't. Strongly supports the structural vs unstructured distinction found here.

5. **"Boiling Frog" (Zhao et al., 2026)** — Iterative prune-tune for reasoning models. Most similar paradigm paper.

6. **Lottery Ticket Hypothesis (Frankle & Carlin, 2019)** — Foundational work on which structures can be removed. The "redundancy as stability buffer" concept relates to over-parameterization arguments.

7. **PPO/DPO alternatives** — Work on RL stability in language models (e.g., InstructGPT's PPO instabilities, DPO as a more stable alternative) should be cited to contextualize why GRPO specifically might be collapse-prone.

8. **Knowledge distillation for compressed models** — An entire family of recovery methods (TinyBERT, DistilBERT, MiniLLM) is unmentioned. Since the models tested are already distilled (DeepSeek-R1-Distill), the interaction between distillation and pruning recoverability is relevant.

9. **RestoreLCC (Feng et al., NeurIPS 2025 Spotlight)** — Alternative plug-and-play recovery paradigm via activation compensation.

10. **"RL Squeezes, SFT Expands" (ICLR 2026)** — Cited in framing but apparently not in the paper itself. Essential theoretical grounding for the tradeoff.

---

## Score: 4 (Weak Accept)

The core observation (Redundancy-Stability Tradeoff) is novel and thought-provoking. The experimental design, while narrow in scope, is internally well-controlled. The paper identifies a real and practically important failure mode that the community should know about. However, the generalization concerns (single scale, single benchmark, single RL algorithm), lack of proposed mitigation, non-significant SFT results at the primary sparsity, and sparse related work significantly limit the contribution. The paper is above the acceptance threshold for novelty and insight but below it for completeness and scope.

## Confidence: 4/5

I am confident in my assessment of the novelty (genuinely new finding), related work gaps (clearly under-cited), and significance limitations (narrow scope). I am slightly less confident about whether the GRPO collapse is truly fundamental vs. a tuning issue, which is the key uncertainty that could move this paper up or down by a full point.
