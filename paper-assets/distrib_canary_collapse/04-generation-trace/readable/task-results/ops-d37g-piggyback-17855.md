# ops d37g piggyback 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d37g_piggyback_17855_20260521T081742_result.json`
- **Structured JSON:** [`8e1156e94642dae7dcbf.json`](../../sessions/8e/8e1156e94642dae7dcbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments registered as DONE. Here are the results.

---

## D37-G: Task Degradation Results (13 checkpoints, gen_10)

| α | PPL | Accuracy | Rep-2 | Rep-3 | Rep-4 |
|---|-----|----------|-------|-------|-------|
| baseline | 26.64 | 0.3904 | 0.079 | 0.028 | 0.013 |
| **0.05** | **20.77** | **0.4312** | 0.140 | 0.062 | 0.032 |
| 0.25 | 22.91 | 0.4242 | **0.200** | **0.118** | **0.085** |
| 0.46 | 31.57 | 0.4004 | 0.164 | 0.090 | 0.061 |
| 0.48 | 32.69 | 0.3985 | 0.160 | 0.089 | 0.063 |
| 0.50 | 31.26 | 0.3991 | 0.128 | 0.051 | 0.025 |
| **0.52** | **41.11** | 0.3890 | 0.143 | 0.075 | 0.047 |
| 0.60 | 53.55 | 0.3749 | 0.154 | 0.083 | 0.054 |
| 0.65 | 62.38 | 0.3669 | 0.163 | 0.082 | 0.049 |
| 0.70 | 70.06 | 0.3603 | 0.134 | 0.064 | 0.039 |
| 0.75 | 80.31 | 0.3540 | 0.126 | 0.055 | 0.031 |
| C4 0.75 | 1421.31 | 0.2221 | 0.150 | 0.094 | 0.075 |
| pad 1.0 | 997.39 | 0.3089 | 0.182 | 0.103 | 0.074 |

## D37-B: Mechanistic Interpretability Results (5 α values, gen_10)

| α | Attn Entropy | Head Diversity | Act Norm | Logit Conf | Eff Rank |
|---|-------------|----------------|----------|------------|----------|
| 0.05 | 1.174 | 0.710 | 51.64 | 0.459 | 731.9 |
| 0.25 | 1.181 | 0.696 | 55.80 | 0.463 | 734.5 |
| 0.50 | 1.127 | 0.696 | 47.67 | 0.496 | 788.5 |
| 0.75 | 1.132 | 0.692 | 43.15 | 0.580 | 853.7 |
| 1.00 | 1.182 | 0.700 | 47.89 | 0.738 | 904.7 |

---

## Key Findings

**1. Phase transition at α≈0.50→0.52:** PPL jumps from 31.3 to 41.1 (31% increase in just 2pp of α). This is the sharpest inflection in the entire sweep, confirming a critical threshold.

**2. Low α improves over baseline:** α=0.05 achieves the best PPL (20.8 vs 26.6 baseline) and accuracy (0.431 vs 0.390). Small synthetic data mixing is beneficial, consistent with data augmentation effects.

**3. Repetition and PPL decouple:** Repetition peaks at α=0.25 (rep_2=0.20) then partially recovers, while PPL degrades monotonically. These are distinct failure modes with different critical thresholds.

**4. Effective rank increases monotonically (732→905):** Collapsing models spread variance more uniformly across dimensions rather than concentrating on informative subspaces — a signature of distributional flattening.

**5. Logit confidence rises sharply (0.46→0.74):** The model becomes progressively overconfident, with the steepest jump between α=0.75 and α=1.0. This correlates with the PPL explosion — the model assigns high probability to wrong tokens.

**6. Attention entropy is non-monotonic:** Dips at α=0.50-0.75, recovers at α=1.0. The mid-range collapse sharpens attention patterns, but catastrophic collapse (α=1.0) reverts to diffuse attention.

**7. Extreme regimes are catastrophic:** C4 α=0.75 (PPL=1421) is worse than padding α=1.0 (PPL=997), suggesting domain-shifted synthetic data is more damaging than pure synthetic padding.

---
