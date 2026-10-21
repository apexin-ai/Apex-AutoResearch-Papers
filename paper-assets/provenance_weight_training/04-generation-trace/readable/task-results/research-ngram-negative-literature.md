# research ngram negative literature

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ngram-negative-literature_20260518T192113_result.json`
- **Structured JSON:** [`360cc6a62798a6aa9a34.json`](../../sessions/36/360cc6a62798a6aa9a34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Literature Search Results

### Most Relevant Papers

**1. "Does the Definition of Difficulty Matter? Scoring Functions and their Role for Curriculum Learning"** (Rampp et al., CVPR 2024 Workshop)
- Scoring function robustness across random seeds positively correlates with curriculum learning performance. Noisy/unstable scorers produce worse outcomes.
- **Direct parallel**: weak detector = noisy scorer → degraded weighting; strong detector = robust scorer → improved training.

**2. "Classification with Noisy Labels by Importance Reweighting"** (Liu & Tao, IEEE TPAMI 2016)
- Proves importance reweighting converges to the optimal classifier **only when noise rates are accurately known**. Misestimated noise rates introduce irreducible bias.
- **Theoretical grounding** for why AUC=0.73 weights are biased enough to hurt.

**3. "Rethinking Importance Weighting for Deep Learning under Distribution Shift"** (Fang et al., NeurIPS 2020)
- Poorly estimated importance weights degrade deep learning performance. Static weight estimation (fixed weak detector) is insufficient.
- Supports the framing that weight estimation fidelity is a prerequisite, not a nice-to-have.

**4. "The Data-Quality Illusion: Rethinking Classifier-Based Quality Filtering for LLM Pretraining"** (Nait Saada et al., arXiv 2025, Apple)
- Classifier-based quality filtering doesn't necessarily help because imperfect classifiers implicitly filter out parts of the target distribution too.
- Directly explains how a weak detector can **systematically misweight** good data.

**5. "DsDm: Model-Aware Dataset Selection with Datamodels"** (Engstrom, Feldmann, Madry, ICML 2024)
- Heuristic quality scores don't align with data that actually impacts model performance. Selection by heuristic quality can hurt vs. random.
- Supports the claim that AUC=0.73 n-gram detector is essentially a heuristic proxy that introduces harmful bias.

**6. "FIRE: Flexible Integration of Data Quality Ratings for Effective Pre-Training"** (Xu et al., EMNLP 2025)
- Single quality signals are insufficient; rater reliability must be explicitly modeled. Accounting for reliability outperforms naive single-rater weighting by 2.9%.
- Provides a framework for discussing **when and how** quality signals should be trusted.

**7. "DSIR: Data Selection for Language Models via Importance Resampling"** (Xie et al., NeurIPS 2023)
- KL reduction (how well the proxy captures the true distribution ratio) correlates with downstream accuracy (r=0.82). Signal fidelity directly determines selection effectiveness.

---

### How This Relates to the N-gram Negative Result

The literature strongly supports a **"detector quality threshold"** framing:

- **Theoretical**: Liu & Tao (2016) and Fang et al. (2020) establish that importance weighting guarantees require accurate weight estimation. Below some accuracy threshold, the bias introduced by misestimation **overwhelms** any benefit from selective weighting.
- **Empirical**: Engstrom et al. (2024) and Nait Saada et al. (2025) show this isn't theoretical — heuristic/imperfect quality classifiers actively hurt LLM pretraining vs. uniform sampling.
- **Curriculum learning**: Rampp et al. (2024) show scoring function robustness directly predicts whether curriculum strategies help or hurt.

The n-gram PPL detector at AUC=0.73 misclassifies ~27% of samples. These errors systematically bias the weight distribution — upweighting some contaminated data and downweighting clean data. The net effect is worse than uniform weighting, consistent with the theoretical prediction that biased importance weights can increase variance and bias simultaneously.

---

### Suggestions for Discussion Section

1. **Frame as a "signal fidelity requirement"**: Cite Liu & Tao (2016) and Fang et al. (2020) to argue that adaptive weighting has a theoretical minimum detector accuracy below which it's counterproductive. Your results empirically demonstrate this threshold exists between AUC 0.73 and 0.9.

2. **Position the negative result as a contribution**: Following Engstrom et al. (2024) and Nait Saada et al. (2025), argue that this is a cautionary finding — practitioners should not assume any quality signal is better than none.

3. **Connect to the FIRE framework**: Cite Xu et al. (2025) to argue that if only weak detectors are available, explicit reliability modeling (rather than naive weighting) is needed.

4. **Practical implication**: The gap between n-gram and neural detector results suggests a cost-benefit analysis — the computational cost of a better detector pays for itself through improved training, while a cheap but inaccurate detector is worse than doing nothing.

---
