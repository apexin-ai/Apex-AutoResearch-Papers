---
dream_id: dream_20260516T235255
tier: worst
overall_score: Borderline Reject (3/6)
timestamp: 2026-05-17T00:31:23.275862+00:00
---

# Dream Review Report

**Paper:** Episode-Level RL for Multi-Turn Agents: Why Step-Independent Training Fails and How to Fix It

**Headline Assessment:** Borderline Reject (3/6)

**Calibration Note:** 3 Major issues identified → score capped at Borderline Reject per calibration rules.

---

## Reviewer 1: Methods + Experiments

### Major Issues

**M1. The γ^(T-h) framework is formally misleading [idea 层面]**

The paper frames the credit assignment problem as discount factor decay (Eq.1: g_t ∝ γ^(T-t) · R · ∇log π). However, standard GRPO does not use temporal discounting in this way. GRPO computes group-normalized advantages from terminal rewards and applies them uniformly to all actions in a trajectory. The actual issue with step-independent training is **context truncation** (the model only sees h steps of context when computing the policy gradient), not multiplicative discount decay.

If γ is not a literal parameter in the GRPO update rule, then §3.2 (Credit Assignment Decay Analysis) is a post-hoc analogy dressed as a theoretical derivation. The correlation between predicted γ^(T-h) and observed performance (Table 3) would be coincidental (both correlate with context window size) rather than causal.

The paper must either: (a) show where γ appears in the actual GRPO implementation and training code, or (b) reframe §3 as an information-theoretic argument about context truncation rather than discount decay.

**Justification for Major:** This undermines Contribution #1 ("identify credit assignment decay as root cause ... providing theoretical analysis"), which is the paper's primary claimed contribution.

**M2. Insufficient statistical rigor across all experiments [idea 层面]**

- **h-sweep (Table 1):** Single seed for all h values. The monotonic ordering h=3 (4.5%) < h=5 (8.0%) < h=8 (14.0%) could be noise. Without multiple seeds, the "sharp cliff below h=5" claim is unsupported statistically.
- **Multi-seed (Table 2):** Only 3 seeds with std=6.0pp. Using t-distribution, the 95% CI for the mean is approximately [15.8%, 32.8%]. This interval is too wide to support precise claims.
- **Cross-environment (Table 5) and model scale (Table 6):** No indication of multiple seeds. The ScienceWorld result (15% vs 2%) and 7B result (38% vs 5%) are single-seed comparisons supporting Contributions #4.
- **Per-task breakdown (Table 7):** N=1-4 per task type. The r=-0.42 correlation with episode length is computed from 6 data points with N=1-4 each. This is not a meaningful statistical test.

**Justification for Major:** Contributions #3 and #4 ("fine-grained context window sweep" and "cross-environment/scale validation") rest on single-seed experiments that could be noise.

**M3. Missing credit assignment baselines [idea 层面]**

The paper compares only step-independent GRPO (h=1) against episode-level GRPO (h=full), with intermediate h values. No comparison with:
- Standard RL algorithms with full-episode returns (PPO, REINFORCE)
- Established credit assignment solutions (GAE/Generalized Advantage Estimation, eligibility traces)
- Reward shaping approaches
- Hindsight experience replay (mentioned in Related Work but not benchmarked)

Without these baselines, the paper cannot claim episode-level GRPO specifically "fixes" the problem. Any full-episode credit assignment method might achieve the same or better results. The contribution reduces to "using full context is better than truncated context," which is expected.

**Justification for Major:** The paper's core claim is that episode-level GRPO resolves a training bottleneck, but without alternative solutions as baselines, the reader cannot assess whether GRPO is the right vehicle or merely one of many equivalent approaches.

### Minor Issues

- **m1.** "Convergence Step" in Table 1 is undefined. Steps to what threshold? [presentation 层面]
- **m2.** Self-verification implementation during training (§4.5) is unexplained. How is verification prompted? Separate forward pass? Cost? [presentation 层面]
- **m3.** "Catastrophic collapse" and "complete collapse" overstate the h=2 result (2% success, 58% action validity). Very poor performance, but not literally zero across all metrics. [presentation 层面]
- **m4.** No figures in the paper. An h-sweep curve (x=h, y=success) and training curves would substantially improve readability and information density. [presentation 层面]
- **m5.** Training details insufficient for reproduction: total training steps, batch size, gradient clipping, hardware, wall-clock time, whether Qwen3 thinking mode was enabled. [presentation 层面]
- **m6.** Table 3 is largely redundant with Table 1 (same h values, adds only the γ^(T-h) column which is a deterministic computation). [presentation 层面]
- **m7.** The paper conducted selective verification experiments (plans 005-013 in the experiment design) that yielded negative results but does not report them. While the narrative pivot to "pure methodology" is reasonable, a brief appendix acknowledging attempted and failed experiments would strengthen transparency. [presentation 层面]

### Strengths (R1)

- S1. The h-sweep ablation is a well-designed experiment that provides actionable guidance for practitioners (even if single-seed).
- S2. The verification ablation (Table 4) cleanly separates training methodology from inference strategy, showing step-independent fails regardless of verification.
- S3. Testing on two environments and two model scales is the right experimental design for generalization claims.
- S4. The Limitations section is honest about the weaknesses (3 seeds, moderate absolute performance, simulated environments, small per-task N).

---

## Reviewer 2: Novelty + Related Work

### Major Issues

**M4. Core contribution has limited novelty for a top venue [idea 层面]**

The paper's central message is: "use full episode context instead of truncated context for RL training of multi-turn agents." In classical RL, episode-level returns are the default (REINFORCE, policy gradient with Monte Carlo returns). The paper essentially identifies that RAGEN's step-independent default is a poor configuration for long-horizon tasks and proposes reverting to the standard approach.

This is a valuable observation for practitioners, but it is closer to a configuration insight than a methodological contribution. The paper needs to argue more convincingly why this observation, applied to the LLM agent GRPO setting, produces non-obvious findings or requires non-trivial adaptation. As written, the "method" (§3.3) is a single equation (Eq.3) that removes context truncation from GRPO.

For a top ML venue (acceptance rate ~25%), the contribution bar requires either: (a) a novel algorithm with provable or empirically demonstrated advantages over multiple alternatives, (b) a surprising empirical finding that changes how the community thinks about the problem, or (c) a comprehensive empirical study with rigorous methodology. This paper attempts (b) and (c) but the finding (full context > truncated context) is not surprising, and the methodology lacks rigor (see M2).

**Justification for Major:** The novelty threshold for a top venue is not met. The observation is useful but incremental.

**M5. Severely insufficient references [presentation 层面, but borderline idea 层面]**

10 references is far below the 30-50 typical for top ML venue submissions. Critical missing citations:

- **Foundational RL:** PPO (Schulman et al., 2017), REINFORCE (Williams, 1992), A3C (Mnih et al., 2016) — the paper discusses policy gradient methods without citing them
- **Credit assignment:** GAE (Schulman et al., 2016), eligibility traces (Singh & Sutton, 1996), HER (Andrychowicz et al., 2017) — all mentioned or implied in §2 but not cited
- **AgentQ:** Mentioned by name in §2 but has no reference entry
- **Multi-turn LLM agent training:** WebAgent, AgentTuning, FireAct, Agent-FLAN, OpenDevin — major recent works in this space entirely absent
- **GRPO applications:** DeepSeek-R1 and related work applying GRPO at scale

The Related Work section (§2) consists of four short paragraphs with minimal synthesis. Each paragraph lists works with one-sentence descriptions rather than providing comparative analysis. A reviewer would conclude the literature survey is incomplete.

**Justification for Major:** Missing references make it impossible to verify the novelty claim ("to our knowledge, no prior work has systematically studied this failure mode"). The claim may be false if unreferenced works have addressed this.

### Minor Issues

- **m8.** Self-Guide [2] achieves 72.7% on ALFWorld with Qwen-1.7B (same model size), while this paper's episode-level training achieves only 25%. The paper does not adequately address this 3x gap. The Discussion mentions "model capacity" as a bottleneck, but Self-Guide uses the same model capacity. The real explanation (Self-Guide uses carefully engineered prompts at inference time vs. this paper training with RL from scratch) should be stated explicitly. [idea 层面]
- **m9.** The title "How to Fix It" overpromises. The "fix" achieves 25% on ALFWorld. The Discussion correctly notes this is a "necessary condition, not sufficient," which contradicts the title's implication of a complete solution. [presentation 层面]
- **m10.** Abstract claims "complete collapse" for step-independent training, but Table 5 shows ScienceWorld step-independent achieves 2% (not 0%), and Table 6 shows 7B step-independent achieves 5%. "Near-complete collapse" would be more accurate. [presentation 层面]
- **m11.** The pivot away from selective verification (visible in the experiment design) leaves traces: the Future Directions paragraph discusses selective verification in detail, suggesting it was originally central to the paper. This creates a slight mismatch between the paper's focused "pure methodology" narrative and the detailed forward-looking discussion of a feature that was tried and abandoned. [presentation 层面]

### Strengths (R2)

- S5. The paper has a clear, focused narrative arc: problem identification → analysis → fix → validation.
- S6. The Introduction effectively motivates the problem with a concrete numerical example (γ^47 ≈ 0.006).
- S7. The practical guidance in §5 (ensure γ^(T-h) > 0.1) is directly actionable.
- S8. Limitations are honestly stated, which is refreshing.

---

## Cross-Dimensional Synthesis

### R1 × R2 Interaction

R1's concern about the γ^(T-h) formalization (M1) directly reinforces R2's novelty concern (M4). If the mathematical framework is not how GRPO actually works, then the paper's primary "theoretical contribution" (Contribution #1) is an analogy rather than analysis. This reduces the paper to a single empirical observation: full context works better than truncated context for long-horizon GRPO training.

R2's observation about Self-Guide's 72.7% with the same model (m8) interacts with R1's missing baselines concern (M3). If prompted self-verification (no RL training) dramatically outperforms RL-trained agents, the practical motivation for the training methodology contribution is weakened. The paper should position its contribution as orthogonal (training vs. inference) more explicitly and discuss whether combining both could close the gap.

### Overall Assessment

The paper identifies a real and practically important issue (step-independent GRPO fails for long-horizon tasks) and provides a clean experimental demonstration. The h-sweep ablation is well-designed and the cross-environment/scale validation shows the right experimental instincts.

However, for a top ML venue:
1. The core finding (full context > truncated context) is not surprising
2. The mathematical formalization appears to misrepresent how GRPO actually works
3. Statistical rigor is insufficient (single-seed experiments supporting main claims)
4. References are far below venue standards
5. No comparison with established credit assignment methods

The paper would be better suited as a short paper/findings paper, or could be strengthened to full paper quality by: (a) fixing the formal framework, (b) adding multi-seed experiments for all conditions, (c) comparing with GAE/eligibility traces/PPO baselines, (d) expanding related work substantially, and (e) addressing the Self-Guide performance gap.

---

## Summary of Issues

| # | Issue | Severity | Category | Reviewer |
|---|-------|----------|----------|----------|
| M1 | γ^(T-h) framework misrepresents GRPO mechanics | Major | idea | R1 |
| M2 | Single-seed experiments, insufficient statistical power | Major | idea | R1 |
| M3 | No credit assignment baselines (GAE, PPO, etc.) | Major | idea | R1 |
| M4 | Limited novelty (configuration fix, not methodological advance) | Major | idea | R2 |
| M5 | Only 10 references, critical citations missing | Major | presentation | R2 |
| m1 | "Convergence Step" undefined | Minor | presentation | R1 |
| m2 | Verification implementation unexplained | Minor | presentation | R1 |
| m3 | "Complete collapse" overstated for h=2 | Minor | presentation | R1 |
| m4 | No figures in paper | Minor | presentation | R1 |
| m5 | Insufficient training details for reproduction | Minor | presentation | R1 |
| m6 | Table 3 redundant with Table 1 | Minor | presentation | R1 |
| m7 | Negative results (selective verification) unreported | Minor | presentation | R1 |
| m8 | Self-Guide 72.7% gap unaddressed | Minor | idea | R2 |
| m9 | Title "How to Fix It" overpromises | Minor | presentation | R2 |
| m10 | "Complete collapse" inaccurate for ScienceWorld/7B | Minor | presentation | R2 |
| m11 | Selective verification traces in Future Directions | Minor | presentation | R2 |

**Major issues: 5 (4 idea-level, 1 presentation-level)**
**Minor issues: 11 (1 idea-level, 10 presentation-level)**

---

## Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Soundness | 2/4 | Core formalization (γ decay) may misrepresent GRPO mechanics; single-seed experiments |
| Novelty | 1.5/4 | Full-episode returns is default in classical RL; contribution is configuration insight |
| Significance | 2/4 | Practical value for GRPO practitioners, but 25% absolute performance limits impact |
| Clarity | 3/4 | Well-written, focused narrative; but missing figures and definitions |
| Overall | **3/6 (Borderline Reject)** | Real problem, clean experiment design, but insufficient novelty and rigor for top venue |

**Confidence:** 4/5 (high confidence — the issues are structural, not judgment calls)

---

## Actionable Recommendations for Revision

1. **Fix the formalization (M1):** Either demonstrate γ is a real GRPO parameter or reframe the analysis as information-theoretic (context truncation → information loss → gradient signal degradation). The latter would be more honest and potentially more interesting.

2. **Add multi-seed experiments (M2):** Run 5 seeds minimum for h∈{1, 5, 10, full} and report mean±std. This is the minimum bar for credible ablation.

3. **Add credit assignment baselines (M3):** Compare episode-level GRPO against at least PPO with full returns and GRPO+GAE. If episode-level GRPO matches PPO, that's still publishable (showing GRPO can work for multi-turn tasks when configured correctly), but the claim would shift.

4. **Expand references (M5):** Target 30+ citations. Cite all mentioned works, add foundational RL, and survey recent multi-turn LLM agent training papers.

5. **Address Self-Guide gap (m8):** Explicitly explain why prompted verification (72.7%) outperforms RL training (25%) and position episode-level GRPO as a training-time complement, not a replacement.

6. **Add figures:** At minimum, an h-sweep curve and multi-seed training curves with shaded std bands.