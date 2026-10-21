# Literature Gap Analysis — 2026-05-14

## Overview

Reviewed 45 existing papers in literature_map.yaml against 6 coverage dimensions critical to the paper's narrative ("Diagnostic Analysis of Temporal Abstraction in World-Model RL"). Identified 5 gaps, added 10 papers. Total: 55 papers.

---

## Gap 1: Time Discretization Theory (CRITICAL)

**Problem**: The paper argues variable-dt imagination fails in world-model RL, but the literature map lacked foundational theory on *why* time discretization matters for RL algorithms.

**Added**:
| Paper | Venue | Role |
|-------|-------|------|
| Tallec et al. 2019 — "Making Deep Q-learning Robust to Time Discretization" | ICML | Theoretical foundation: Q-learning is inherently sensitive to δ; architecture + exploration must adapt. Directly supports our claim that RSSM cannot produce δ-invariant predictions. |
| Park et al. 2021 — "SAR: Time Discretization-Invariant Safe Action Repetition" | NeurIPS | Model-free solution achieving δ-invariance via adaptive state reaction during repetition. Contrast: model-free RL *can* be made robust to variable dt, but world-model RL cannot (our finding). |
| Wang & Beltrame 2024 — "SEAC: Elastic Time Steps" | arXiv | Variable-duration actions as part of action space. Model-free analog of our variable-dt imagination. |

**Impact on narrative**: Strengthens C1 (degradation is expected) by grounding in δ-sensitivity theory. Provides clear distinction: model-free temporal abstraction has known solutions, world-model temporal abstraction does not.

---

## Gap 2: Diagnostic Methodology Precedents (IMPORTANT)

**Problem**: Our paper is a diagnostic/analysis paper, not a method paper. The literature map had no references to the "what matters" / factorial analysis tradition in RL.

**Added**:
| Paper | Venue | Role |
|-------|-------|------|
| Engstrom et al. 2020 — "Implementation Matters in Deep Policy Gradients" | ICLR | Methodological precedent: code-level details (not algorithms) drive performance differences. Parallel to our finding that trained vs. untrained dt_embedding is the critical detail. |
| Andrychowicz et al. 2021 — "What Matters for On-Policy Deep Actor-Critic Methods?" | ICLR | Large-scale factorial study template (50+ choices, 250K agents). Direct methodological reference for our factorial design (dt_emb × subsample × horizon). |

**Impact on narrative**: Legitimizes our diagnostic approach by citing established precedents. Useful for Introduction ("following the tradition of systematic diagnostic studies in RL...") and reviewer defense against "no new algorithm" critique (R5).

---

## Gap 3: Delusional Bias Follow-up (MODERATE)

**Problem**: Had Lu et al. 2018 (formalizes delusional bias) but not ConQUR (2020), which proposes the first practical mitigation.

**Added**:
| Paper | Venue | Role |
|-------|-------|------|
| Su et al. 2020 — "ConQUR: Mitigating Delusional Bias in Deep Q-learning" | ICML | Consistency-penalized Q-labels for delusional bias. Model-free mitigation; our delusional critic in MBRL is a different mechanism (temporal conditioning corruption, not policy-class constraint). |

**Impact on narrative**: Completes the delusional bias literature arc: Lu 2018 (definition) → Su 2020 (mitigation in model-free) → our work (new instance in MBRL via dt_embedding).

---

## Gap 4: MBRL Rollout Quality & Value Overestimation (CRITICAL)

**Problem**: The paper's core finding is about imagination rollout quality, but the literature map lacked the most recent (ICLR 2025) work on rollout failures and value overestimation in MBRL.

**Added**:
| Paper | Venue | Role |
|-------|-------|------|
| Frauenknecht et al. 2025 — "On Rollouts in Model-Based RL" | ICLR 2025 | Shows trajectory-sampling rollouts diverge after few steps and can *harm* policy learning. Proposes Infoprop (aleatoric/epistemic separation). Directly supports our findings; we identify a *specific* mechanism beyond general compounding error. |
| Voelcker et al. 2025 — "MAD-TD: Model-Augmented Data stabilizes High UTD RL" | ICLR 2025 | Value misgeneralization → instability at high UTD. Uses model data to fix values. Complementary mechanism: they fix replay distribution mismatch, we identify temporal conditioning corruption. |

**Impact on narrative**: Critical for related work positioning. Our paper identifies a *specific, previously unknown* failure mechanism (dt_embedding-induced delusional critic) beyond the general rollout quality issues these papers address. Must cite to show awareness and differentiation.

---

## Gap 5: Latest Dreamer Evolution + Action Repeat (MODERATE)

**Problem**: Literature map stopped at NE-Dreamer/DyMoDreamer for Dreamer extensions. Missing DreamerV4 and latest ICLR 2025 action repeat work.

**Added**:
| Paper | Venue | Role |
|-------|-------|------|
| Hafner & Yan 2025 — "DreamerV4: Training Agents Inside Scalable World Models" | arXiv | Replaces RSSM with transformer; our RSSM-specific diagnosis still relevant as cautionary lesson for transformer world models. |
| Nie et al. 2025 — "SDAR: Spatially Decoupled Action Repetition" | ICLR 2025 | SOTA model-free action repeat. Advances variable-rate control in model-free; our work shows the obstacle in model-based. |

**Impact on narrative**: DreamerV4 is essential for Discussion — our findings are RSSM-specific, but DreamerV4's transformer architecture may exhibit analogous issues if temporal conditioning is naive. SDAR extends the action repeat comparison.

---

## Remaining Coverage Assessment

| Dimension | Coverage | Notes |
|-----------|----------|-------|
| Value overestimation (model-free) | Excellent | Thrun 1993, Double DQN, TD3, SAC |
| Value overestimation (model-based) | Good → Excellent | Added MAD-TD, Frauenknecht |
| Delusional bias | Good → Excellent | Lu 2018 + ConQUR 2020 |
| Temporal abstraction (model-free) | Excellent | Options, FiGAR, TempoRL, SAR, SDAR, SEAC |
| Temporal abstraction (world models) | Excellent | THICK, Hieros, Director |
| Time discretization theory | Gap → Good | Added Tallec, Park, Wang |
| Diagnostic methodology | Gap → Good | Added Engstrom, Andrychowicz |
| MBRL rollout quality | Gap → Good | Added Frauenknecht, Barkley (existing) |
| Dreamer family | Excellent | V1-V4 + DreamerPro-era extensions |
| Reward prediction / objective mismatch | Excellent | DreamSmooth, HarmonyDream, Lambert 2020 |
| Seed variance / training instability | Excellent | Henderson, Nikishin, Qiao, Bjorck, Hussing |
| Evaluation methodology | Good | rliable (Agarwal 2021) |

## No Major Remaining Gaps

The literature map now covers all dimensions needed for the related work section. Papers are tagged with appropriate `category` (background/evaluation/method-component/direct-competitor) and `role` descriptions for drafting.

## Suggested Related Work Section Structure

1. **Temporal abstraction in RL** — Options (Sutton 1999), FiGAR, TempoRL, SAR, SDAR → model-free success; THICK, Hieros, Director → world-model hierarchy approaches
2. **World-model RL** — Dreamer V1-V4, IRIS, TWM → architecture context
3. **Value overestimation and delusional bias** — Thrun 1993, Double DQN, TD3 → model-free; Lu 2018, ConQUR → delusional bias; MBPO, MOPO → model exploitation; MAD-TD, Frauenknecht → recent MBRL-specific
4. **Diagnostic methodology** — Engstrom 2020, Andrychowicz 2021, rliable → precedent for factorial analysis approach
5. **Time discretization** — Tallec 2019, Park 2021 → theoretical grounding for dt-sensitivity
