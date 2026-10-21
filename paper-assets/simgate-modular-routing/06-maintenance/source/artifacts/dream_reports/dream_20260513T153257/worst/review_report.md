---
dream_id: dream_20260513T153257
tier: worst
overall_score: reject
timestamp: 2026-05-13T16:23:56.518710+00:00
---

# Dream Review Report: "When Does Deterministic Computation Help LLM Agents?"

**Dream ID**: 20260513T153257 | **Review Mode**: Full | **Date**: 2026-05-13

---

## Roundtable Summary

Two reviewers conducted independent reviews, then cross-shared and converged.

- **R1** (Methods + Experiments): Initial 3/6 → revised to **2/6** after cross-sharing
- **R2** (Novelty + Related Work): **2/6** throughout
- **Consensus**: **Reject (2/6)**

---

## Paper Overview

The paper introduces a counterfactual evaluation methodology that forks agent trajectories at each decision step across three computation modalities (fast internal, deep CoT, deterministic simulation) and measures per-step value via hindsight scoring. Applied to 15 ScienceWorld task types (300 episodes, 6,600 labeled steps), the key findings are:

1. Learned per-step routing (SimGate, 65.2) ≈ always-simulate (64.8), Δ=0.4, 90% CI [−4.8, 5.6]
2. Explicit modular router ≈ implicit backbone routing, Δ=1.2, p=0.38
3. Deterministic computation helps only 4/15 death-risk task types (+16–29 points)
4. Routing patterns do not transfer across task domains

The paper pivots from a methods contribution to a diagnostic/negative-result paper, arguing per-step routing is the wrong granularity and task-level computation planning is the right approach.

---

## Consolidated Strengths

**S1. Honest negative-result framing (R1, R2).** The paper does not disguise weak routing results. Statistical reporting is appropriate: bootstrap 90% CIs for all key comparisons, p-values reported, non-significant results clearly identified. This candor is commendable and rare.

**S2. Clean per-task diagnostic partition (R1, R2).** The sharp separation of 4 death-risk task types (where simulation yields +16–29 points) from 11 other task types (where it provides no benefit) is the paper's most valuable empirical contribution. The finding is actionable: apply deterministic computation unconditionally to catastrophic-failure-prone task categories.

**S3. Comprehensive ablation coverage (R1).** Five baselines (always-internal, always-det, random, confidence-threshold, oracle), plus ablations on routing granularity (2-way vs 3-way), router size (1.5B/1.7B/3B), explicit vs implicit routing, and cross-task transfer. Each ablation reinforces a consistent narrative.

**S4. Controlled experimental design (R2).** Same backbone, same evaluation protocol across all comparisons. The inclusion of oracle routing (70.0) quantifies the theoretical ceiling for per-step routing.

---

## Consolidated Weaknesses

### Critical

**W1. Oracle construction circularity undermines the central negative claim (R1, endorsed by R2).** ScienceWorld has sparse rewards—95%+ of steps yield zero score delta. Under the tie-break rule, the oracle defaults to deterministic when Δ=0, meaning the oracle itself behaves approximately like always-deterministic. The router was trained on labels that are themselves approximately always-det, making SimGate ≈ always-det nearly tautological. The paper does not discuss this circularity or attempt multi-step rollout labeling to mitigate it. This is the single most important methodological flaw.

**W2. Core pipeline is standard tool-use learning, entirely unpositioned (R2, endorsed by R1).** The method—collect labels for when to invoke an external tool, SFT-train a small classifier, selectively invoke at inference—is the established paradigm in Toolformer (Schick et al.), ART (Paranjape et al.), Chameleon (Lu et al.), ToolkenGPT (Hao et al.), and CREATOR (Qian et al.). None are cited. Without positioning against this literature, the paper implicitly claims the routing framework as novel when it is not.

**W3. Unacceptable bibliography (R1, R2).** Eight references total, two with placeholder arXiv IDs (CogRouter: arXiv:2405.XXXXX, ITP-R: arXiv:2405.XXXXX). No dedicated Related Work section. Missing entire subfields: adaptive computation (Mixture-of-Depths, CALM), MoE routing (Switch Transformers), world models (DreamerV3, IRIS), safe RL, neuro-symbolic integration (Logic-LM, SatLM), off-policy evaluation (Precup et al.), LLM agent frameworks (Voyager, AgentBench, WebArena). This level of engagement with prior work is insufficient for any venue.

### Major

**W4. 42% label ambiguity is a methodological limitation, not just a finding (R1, R2).** The paper treats the high ambiguity rate as a discovery about task structure, but alternative labeling strategies (multi-step rollouts, N-step returns, class-weighted loss, filtering low-margin samples) are never explored. It is impossible to distinguish "routing genuinely doesn't matter" from "our labeling method is too noisy to detect when routing matters."

**W5. Negative result may be expected rather than surprising (R2).** The finding can be predicted from first principles: sparse rewards → degenerate labels, low oracle ceiling (only 5.2 points above always-det) → limited theoretical headroom, 42% ambiguous labels → noisy training signal. The paper does not argue that the negative result was non-obvious ex ante.

**W6. Single backbone, single environment (R1, R2).** All results use Qwen2.5-7B on ScienceWorld. The sweeping claim that "per-step routing is the wrong granularity" may not generalize to weaker backbones (more steps needing external computation) or environments with denser rewards (clearer step-level signals). The MATH track (plan-009) was not attempted—the only planned cross-domain validation.

**W7. ScienceWorld's penalty structure confounds the diagnostic finding (R2).** The -100 death penalty means a single hallucinated state transition collapses an entire episode score. The 4-vs-11 partition may simply reflect "tasks where the backbone triggers -100" vs "tasks where it doesn't"—a property of the reward function, not a deep insight about when deterministic computation helps. On a benchmark with graduated penalties, the sharp partition would likely dissolve.

### Moderate

**W8. Suspicious uniformity in per-task scores (R1, endorsed by R2).** All 8 low-risk tasks show exactly Δ=-2 (SimGate minus Internal) in Table 3. This perfect uniformity across diverse task types (use-thermometer, find-living, move-object, etc.) with 20 episodes each is statistically implausible, suggesting either aggressive rounding or a systematic artifact. If rounding, exact numbers should be reported; if artifact, it deserves investigation and undermines the task taxonomy's credibility.

**W9. CogRouter comparison is misleading (R1).** CogRouter (84.6) uses a fundamentally different training paradigm (CoPO RL), different backbone, and possibly different ScienceWorld version. The 19.4-point gap makes SimGate look ineffective, but the comparison is not apples-to-apples. With a placeholder arXiv ID, the number cannot even be verified.

**W10. Post-hoc task taxonomy (R1).** The death-risk/marginal/low-risk grouping appears defined after seeing results. If the taxonomy was pre-registered, the paper should state this; if post-hoc, this is data dredging that inflates the apparent sharpness of the partition.

---

## Key Questions to Authors

1. **Oracle tie-breaking**: What fraction of oracle labels reflect genuine score differences vs. tie-break artifacts? What is the oracle's simulator invocation rate? If the oracle routes to deterministic on ~100% of steps, the entire framework collapses to always-det.

2. **Filtered training**: What happens if the router is trained exclusively on death-risk task steps (the 27% with clear signal)? Class-weighted loss? Filtering steps with margin < 5? These obvious interventions could change the negative conclusions.

3. **Multi-step rollout labeling**: Have you tried N-step (3 or 5) rollout scoring instead of full-episode rollout? This would provide denser signal in the sparse-reward setting.

4. **Low-risk uniformity**: Are the Δ=-2 values in Table 3 exact or rounded? What are the per-task bootstrap CIs?

5. **Placeholder references**: Can you provide actual arXiv IDs for CogRouter and ITP-R?

6. **Rule-based baseline**: Given that routing features are described as "surface-level keywords" (temperature, heat, phase-change), how does a simple keyword-matching heuristic perform?

7. **Backbone sensitivity**: Would a weaker backbone (e.g., Qwen2.5-3B) or stronger backbone (Qwen2.5-72B) change the death-risk task partition?

---

## Experiment Coverage Assessment

| Planned Experiment | Status | Notes |
|---|---|---|
| plan-001: Counterfactual trajectories | ✅ Covered | 15 tasks, 300 episodes, 6,600 steps |
| plan-002: Router SFT training | ✅ Covered | Qwen3-1.7B, 3-way |
| plan-003: SimGate E2E evaluation | ✅ Covered | Full baseline comparison |
| plan-004: Explicit vs implicit | ✅ Covered | But confounded by model size (1.7B vs 7B) |
| plan-005: Per-task routing analysis | ⚠️ Partial | Phase analysis (36/39/38%) and entropy mentioned in text; routing heatmap and figures absent |
| plan-006: 2-way vs 3-way | ✅ Covered | |
| plan-007: Boil task v3 rerun | ❌ Not reported | May be folded into main results but no validation table shown |
| plan-008: Router size ablation | ✅ Covered | |
| plan-009: MATH track | ❌ Not attempted | Acknowledged in limitations; most significant omission |
| plan-010: Cross-task transfer | ✅ Covered | |

---

## Scores

| Criterion | R1 | R2 | Consensus |
|---|---|---|---|
| Soundness | 3/5 | — | 2.5/5 |
| Significance | — | 2/5 | 2/5 |
| Novelty | — | 2/5 | 2/5 |
| Overall | 2/6 | 2/6 | **2/6 (Reject)** |
| Confidence | 4/5 | 4/5 | 4/5 |

---

## Final Assessment

**Score: 2/6 — Reject**

The paper is honest and well-structured, presenting a clean experimental design with appropriate statistical reporting. However, it fails to meet the acceptance threshold on three fronts:

1. **Methodological validity**: The oracle construction circularity (sparse rewards → oracle ≈ always-det → router trained on always-det labels → SimGate ≈ always-det) undermines the central negative claim. The 42% label ambiguity is a limitation of the labeling method, not a proven property of the routing problem, and obvious mitigations (filtered training, multi-step rollouts) are unexplored.

2. **Novelty**: The core pipeline is standard tool-use learning (Toolformer paradigm), entirely unpositioned. The counterfactual methodology is a straightforward application of off-policy evaluation ideas. The remaining novel content—a single empirical observation about 4 death-risk tasks on one benchmark—is too narrow.

3. **Scholarship**: Eight references (two unverifiable) with no Related Work section. Multiple directly relevant subfields (tool-use learning, adaptive computation, safe RL, MoE routing, off-policy evaluation) are entirely absent.

**Path to acceptance**: (a) Resolve oracle circularity by implementing multi-step rollout labeling and filtered/class-weighted training to test whether the negative result survives. (b) Add a proper Related Work section engaging with tool-use learning and adaptive computation literatures. (c) Validate on at least one additional environment (or backbone) to support generalizability claims. (d) Add a rule-based routing baseline to calibrate the learned router's value. With these changes, a strengthened version targeting EMNLP Findings could be viable, with the counterfactual methodology and per-task diagnostic as contributions.
