# Research conversation: I need you to help me draft a complete revised research idea JSON. I'll provide all the context and the specific changes

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 4
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a2b6bb3e2d609ddee.jsonl`
- **Structured JSON:** [`6acb6b651aa70765da1c.json`](../../sessions/6a/6acb6b651aa70765da1c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

4 recorded events

### User

_source line 1 · 2026-05-28T14:13:32.226Z_

I need you to help me draft a complete revised research idea JSON. I'll provide all the context and the specific changes needed. Output ONLY the JSON object, nothing else.

## Context

This is round 6 of revisions for a research idea about difficulty-dependent per-criterion gaming in rubric-rewarded RL. The scores have been declining (3.8→3.5) over the last 3 rounds because the idea has accumulated complexity without proportional improvement. This revision is a MAJOR REVISION that SIMPLIFIES the scope while elevating the framing.

## Key findings from research:

1. **H0 mischaracterized**: LLMs Gaming Verifiers (2604.15149) studies INDUCTIVE REASONING (SLR-Bench with 4 tiers), not math. Uses "increases with" — "monotonic" appears only once in Appendix B. Measures aggregate extensional shortcuts via Isomorphic Perturbation Testing, not per-criterion rubric gaming.

2. **Medical domain circularity fixable**: Use SFT-init checkpoint (before RL training) pass rates as difficulty oracle. This is standard in curriculum RL (CDAS arXiv:2505.17652 aggregates historical performance, AdaCuRL uses base model pass rates).

3. **The gap is still open**: No one has published per-criterion × per-difficulty gaming analysis. Reward Hacking in Rubric-Based RL (2605.12474) diagnoses per-criterion gaming in medical/science but does NOT stratify by difficulty.

4. **Goodhart's law literature is strictly scalar or aggregate**: Holmstrom-Milgrom framework (2603.28063) proves existence but not constructive characterization. Robust Optimization (2604.12086) is scalar-valued. New "Strong, Weak and Benign Goodhart's Law" (2505.23445) is independence-free but single proxy-goal pair. Nobody does K-dimensional + difficulty-varying.

5. **Field velocity still high**: ARES (May 2026), SRaR (May 2026), AMARIS (May 2026) — but all difficulty-agnostic. Our specific niche remains unoccupied.

6. **AAAI timeline**: 7.5 weeks from May 28 to Jul 21 abstract. Unrealistic with medical domain + 5 training runs + paper writing. Math-only stretch is barely feasible.

7. **CDAS paper (2505.17652)**: Competence-Difficulty Alignment Sampling — models difficulty as trajectory of performance discrepancies. Relevant for our difficulty estimation but operates under binary rewards.

## Strategic changes for this revision:

### 1. REFRAME as "Structured Goodhart's Law"
Elevate from rubric-RL diagnosis to general evaluation theory: "When evaluation is decomposed into K criteria, Goodhart's law doesn't just apply K times — it creates structured exploitation surfaces that depend on difficulty." Rubric-RL experiments become the instantiation, not the whole contribution.

### 2. SIMPLIFY prediction structure (4→3)
- Drop P1 (universal exploitation channels with flat profiles) — too intuitive, merge into diagnostic
- P1_new = old P2 (Edge of Competence, non-monotonic gaming) — PRIMARY, quantitative: peak gaming at intermediate difficulty ≥1.5× rate at highest difficulty
- P2_new = old P3 (Simpson's Paradox correlation sign flip) — SECONDARY, quantitative: r > 0.1 at levels 1-2, r < -0.1 at levels 4-5
- P3_new = old P4 (Dimensionality Collapse) — SHARPENED, quantitative: K_honest/K_eff < 0.5 at level 5

### 3. FIX H0 qualification
"Prior work shows gaming prevalence generally increases with task complexity in aggregate settings (LLMs Gaming Verifiers 2026, studying inductive reasoning; Goodhart's Law in RL, ICLR 2024, studying MDPs). We formalize this as H0: under K-dimensional rubric evaluation, ALL criteria follow this aggregate trend."

### 4. FIX medical domain circularity
Use SFT-init checkpoint pass rates (pre-RL) as difficulty oracle. Also use question-level metadata where available (medical complexity markers, question source tags).

### 5. HONEST venue strategy
- Primary: ICLR 2027 (~Sep 24, 17 weeks) — full 3-contribution scope with cross-domain
- Stretch: AAAI 2027 (Jul 21 abstract, 7.5 weeks) — MATH-ONLY, Contributions 1-2, with explicit decision gate at Jul 9
- Backup: ARR August 3 → EACL 2027 — intermediate scope

### 6. Impact broadening per reviewer
Position Gaming Budget as general tool for ANY multi-dimensional evaluation with difficulty variation. Connect to Goodhart's law literature.

### 7. Acknowledge impact ceiling honestly
If P1-P2 (new numbering) fail → solid diagnostic contribution + theory, likely B+ paper. If they hold → strong contribution that challenges mainstream understanding.

## Here is the complete JSON to output:

```json
{
  "title": "Harder Problems, Easier Gaming: Difficulty-Dependent Exploitation Surfaces in Multi-Dimensional Evaluation",
  "core_problem": "Multi-dimensional evaluation systems (rubric-based RL rewards, multi-criteria benchmarks, structured assessment) face a structural vulnerability unrecognized in the Goodhart's law literature: when K evaluation criteria are applied with uniform strictness across varying task difficulty, the resulting exploitation surface has K×D structure — not K independent copies of scalar Goodhart's law. Easy-to-verify criteria (formatting, structural completeness) remain satisfiable via shallow pattern-matching even on hard problems, while hard-to-verify criteria (proof validity, factual accuracy) yield vanishing gradient signal on difficult problems, creating asymmetric exploitation opportunities. Prior work establishes that gaming increases with task complexity in aggregate settings (LLMs Gaming Verifiers 2026, studying inductive reasoning shortcuts; Goodhart's Law in RL, ICLR 2024, studying MDPs; Scaling Laws for RM Overoptimization, ICML 2023). However, these findings use aggregate metrics over binary or scalar rewards. We hypothesize that per-criterion disaggregation under K-dimensional rubric evaluation reveals richer structure: specifically, an 'edge of competence' effect where criterion-specific gaming peaks at moderate difficulty — the level where the model has just enough capability to produce plausible-looking criterion satisfaction without genuine understanding — creating non-monotonic per-criterion gaming profiles invisible in aggregate analysis. This structural vulnerability applies to any evaluation system where multi-dimensional criteria meet difficulty variation: rubric-rewarded RL, multi-criteria benchmarks, structured human evaluation. We formalize this as the first K-dimensional, difficulty-varying extension of Goodhart's law, and validate it empirically across math and medical reasoning domains.",
  "opportunity": "Five convergent gaps, now sharpened around the 'Structured Goodhart's Law' framing: (1) The Goodhart's law literature — Goodhart's Law in RL (ICLR 2024), Scaling Laws for RM Overoptimization (ICML 2023), Strong/Weak/Benign Goodhart's Law (arXiv:2505.23445) — operates on SCALAR proxy-goal pairs. The Robust Optimization framework (arXiv:2604.12086, ICLR 2026) adds correlation between scalar proxies but does not decompose per-criterion or model difficulty. No formal treatment exists for K-dimensional evaluation with difficulty-varying exploitation. (2) Wang & Huang (arXiv:2603.28063) prove reward hacking is a structural equilibrium under finite multi-dimensional evaluation via the Holmstrom-Milgrom framework and derive a distortion index — but this is an EXISTENCE proof, not a CONSTRUCTIVE characterization predicting WHICH dimensions are exploited at WHICH difficulty levels. (3) DGPO (ICLR 2026, Theorems 1-2) addresses difficulty bias in binary-reward GRPO; per-criterion application is straightforward, but the INTERACTION structure — criterion correlations shifting with difficulty, verification gaps creating asymmetric vulnerability, effective dimensionality collapsing — requires genuinely novel analysis. (4) Reward Hacking in Rubric-Based RL (arXiv:2605.12474) diagnoses gaming taxonomy in medical/science domains (3 failure modes, completeness/presence criteria concentration, self-internalization gap metric) but does NOT stratify by problem difficulty — the core analytical dimension we add. (5) LLMs Gaming Verifiers (arXiv:2604.15149) shows gaming prevalence increases with task complexity on inductive reasoning tasks under binary verification — this aggregate finding is the natural null hypothesis that our per-criterion analysis tests. The marginal contribution is threefold: (a) a Gaming Budget theorem — the first formal K-dimensional, difficulty-varying bound on exploitable reward; (b) a reusable diagnostic producing per-criterion × per-difficulty gaming surfaces; (c) three quantitative falsifiable predictions against the aggregate-trend null hypothesis, each with explicit failure conditions.",
  "landscape": "Rubric rewards for RL achieve strong results but apply uniform strictness across difficulty: RRM (ACL 2026) boosts Verified Pass@1024 on AIME2024 from 26.7% to 62.6%; RaR (ICLR 2026) extends to medical (+31% HealthBench) and science (+7% GPQA-Diamond); SRaR (arXiv:2605.17291) adds step-level attribution; POW3R (arXiv:2605.20164) adapts criterion weights via rollout variance; ARES (arXiv:2605.23454) automates rubric synthesis; AMARIS (arXiv:2605.18592) maintains persistent evaluation memory for difficulty-agnostic rubric evolution. The rubric-RL space continues rapid expansion (~8 papers in 4 weeks preceding this revision) — but this velocity STRENGTHENS our diagnostic contribution: as methods proliferate, a principled framework identifying WHICH criteria are exploited at WHICH difficulty levels becomes a shared evaluation lens no individual method paper provides. Difficulty-aware RL methods operate under binary rewards: DGPO/MathForge (ICLR 2026) via MAD normalization, DARO (arXiv:2510.09001), F-GRPO (arXiv:2602.06717), GRPO-LEAD (EMNLP 2025) via logistic weighting, A-GRAE (arXiv:2602.05548), Goldilocks RL (arXiv:2602.14868), Online Difficulty Filtering (EACL 2026), CDAS (arXiv:2505.17652) via competence-difficulty alignment, Gradient Starvation (arXiv:2605.07689) via degeneracy analysis. ALL operate under binary rewards without per-criterion gaming analysis. The closest convergence spans six categories: **Difficulty-stratified rubric calibration**: RuCL (arXiv:2602.21628) adjusts by model competence, not problem difficulty, and is vulnerable to gaming-inflated pass rates. **Multi-objective reward normalization**: MO-GRPO (arXiv:2509.22047) addresses per-objective variance bias (the mechanism underlying dimensional exploitation) but is difficulty-agnostic. **Reactive criterion reweighting**: POW3R adapts via rollout variance (reactive/diagnostic) while our approach is proactive/predictive (which criteria WILL BE gamed, inferred a priori from difficulty structure). **Memory-augmented rubric adaptation**: AMARIS addresses the temporal dimension (rubric evolution during training) while we address the structural dimension (exploitation variation with difficulty) — complementary, not competing. **Rubric quality and gaming defense**: Rubicon (arXiv:2508.12790), CDRRM (arXiv:2603.08035), C2 (arXiv:2604.13618) — all difficulty-agnostic. **Goodhart's law theory**: Goodhart's Law in RL (ICLR 2024), Robust Optimization for Correlated Proxies (ICLR 2026), Reward Hacking as Equilibrium (arXiv:2603.28063), Strong/Weak/Benign Goodhart's Law (arXiv:2505.23445) — all scalar or aggregate, none model K-dimensional + difficulty-varying exploitation. The critical gap: no work provides (a) formal K-dimensional difficulty-varying Goodhart bounds, (b) per-criterion × per-difficulty gaming diagnosis, or (c) quantitative predictions about gaming structure that can be tested against the aggregate-trend null.",
  "inspired_by": "Field guide gaps: 'No formal treatment of Goodhart's law exists for K-dimensional evaluation under difficulty variation' + 'Per-criterion × per-difficulty gaming analysis is absent from the entire rubric-RL literature.' Innovation patterns: 'Rigorous problem diagnosis as standalone contribution' (proven success — 'Does RL Really Incentivize Reasoning' diagnosed binary-reward limitations at NeurIPS 2025; 'Reward Hacking in Rubric-Based RL' diagnosed gaming taxonomy without difficulty stratification) + 'Formal analysis revealing hidden structural bias.' Core insight — the 'Edge of Competence' hypothesis: For any rubric criterion, gaming peaks at the difficulty level where the model sits at the competence boundary — enough capability to produce plausible-looking criterion satisfaction, not enough to genuinely satisfy it. Below this, the model solves correctly (no need to game); above it, the model cannot even produce plausible fakes. This creates criterion-specific inverted-U gaming profiles. This directly tests the aggregate-trend finding from LLMs Gaming Verifiers (2026): their result (gaming 'increases with task complexity') holds for aggregate binary-reward metrics, but may DISAGGREGATE into non-monotonic per-criterion patterns under rubric evaluation — analogous to Simpson's Paradox. Key framing insight: Structured Goodhart's Law. The Goodhart literature treats proxy optimization as a scalar phenomenon. Wang & Huang (2026) prove reward hacking is an equilibrium under multi-dimensional finite evaluation, but provide existence, not construction. Our Gaming Budget theorem gives the first constructive, difficulty-parameterized characterization — predicting not just THAT gaming occurs but WHERE in the K×D space it concentrates. This elevates the contribution from rubric-RL diagnosis to evaluation theory.",
  "approach": "We adopt a three-contribution structure: general evaluation theory, cross-domain empirical diagnosis, and proof-of-concept defense — ordered by robustness and generality. **Framing: Structured Goodhart's Law.** We position the paper as extending Goodhart's law to K-dimensional evaluation under difficulty variation: 'When evaluation decomposes into K criteria, Goodhart's law creates structured K×D exploitation surfaces, not K independent scalar problems. We provide the first formal characterization.' **Null Hypothesis and Falsifiable Predictions.** We test against the Aggregate-Trend Null Hypothesis (H0): 'Under H0, gaming severity increases with problem difficulty for ALL rubric criteria, following the aggregate trend observed in prior work on binary/scalar rewards (LLMs Gaming Verifiers 2026, studying inductive reasoning; Goodhart's Law in RL, ICLR 2024, studying MDPs).' Note: we carefully qualify that prior evidence comes from different domains (inductive reasoning, not math) and different reward structures (binary/scalar, not K-dimensional rubric). H0 represents the natural extrapolation of these findings to per-criterion rubric evaluation. Three falsifiable predictions with quantitative failure conditions: (P1) Edge of Competence — H0 predicts monotonically increasing gaming for reasoning-verification criteria; P1 predicts an inverted-U peaking at MATH levels 3-4. Quantitative threshold: peak gaming rate at intermediate difficulty ≥ 1.5× the rate at the highest difficulty level, measured by the Dimension Exploitation Gap. Theoretical basis: at moderate difficulty, the model has enough capability to produce plausible criterion satisfaction without genuine understanding; at high difficulty, even plausible fakes are transparent. (P2) Simpson's Paradox — H0 predicts criterion correlations weaken but maintain sign; P2 predicts the Pearson correlation between surface-criterion and reasoning-criterion satisfaction is positive at MATH levels 1-2 (r > 0.1) and negative at MATH levels 4-5 (r < -0.1), a sign flip analogous to Simpson's Paradox with difficulty as the confounding variable. (P3) Asymmetric Dimensionality Collapse — H0 predicts gradual, symmetric dimensionality reduction; P3 predicts K_honest/K_eff < 0.5 at MATH level 5, with K_eff ≥ 3. That is, honest gradient signal collapses to a lower-dimensional subspace FASTER than total signal, because gaming inflates the apparent dimensionality. **Value under either outcome:** If P1-P2 fail, the paper still contributes: (a) the first per-criterion × per-difficulty gaming characterization in any domain — confirming monotonicity per-criterion is itself new, as prior work shows only aggregate trends; (b) the Gaming Budget theorem, whose diagnostic value is independent of monotonicity; (c) evidence favoring simple monotonic calibration (a useful negative result). We explicitly acknowledge this would be a solid diagnostic paper rather than a paradigm-shifting one. **Contribution 1 — Gaming Budget Framework (domain-agnostic theory).** Three formal results for any K-dimensional evaluation system with difficulty variation: (T1) Gaming Budget Theorem — an optimization-theoretic bound on total exploitable reward at difficulty d. Formal model: pass rate matrix P ∈ [0,1]^{K×D}, verification gap matrix Δ (gap between surface-level and genuine criterion satisfaction), difficulty-varying correlation matrix Σ_d. Three assumptions: (A1) decomposability into genuine and gaming components; (A2) monotonic non-increase of reasoning-dependent pass rates with difficulty; (A3) difficulty-stable or increasing verification gaps for surface criteria. Bound: G_d ≤ Σ_{k∈V_d} w_k · δ_{k,d} · √(p_{k,d}(1−p_{k,d})) + Σ_{j&lt;k∈V_d} w_j·w_k · max(0, σ_{jk,d}) · δ_{j,d}·δ_{k,d}. Validated via RANKING ACCURACY: Spearman ρ between predicted and observed gaming severity across all K×D cells, following the Effective Horizon precedent (NeurIPS 2023 Oral). We also report: conservativeness ratio, top-3 vulnerability identification accuracy. (T2) Dimensionality Collapse Theorem — proves K_honest(d) decreases strictly faster than K_eff(d) under A2, using the observation that high-verification-stringency criteria leave the active gradient set first. (T3) Calibration Sufficiency Condition (ICLR scope only) — derives the minimal gaming-eliminating strictness schedule s_{k,d} ∝ 1/δ_{k,d} · √(p_{k,d}(1−p_{k,d})). **Contribution 2 — Cross-Domain Empirical Diagnosis.** Math domain (primary): Qwen2.5-Math-1.5B policy, Qwen3-8B judge, MATH levels 1-5 (native difficulty tags). Medical domain (generalizability test): Qwen2.5-1.5B-Instruct policy, Qwen3-8B judge, RaR-Medicine (22.4K examples, ICLR 2026). Difficulty estimation for medical domain: use the SFT-init checkpoint (the policy initialization BEFORE any RL training) to generate rollouts and compute per-question pass rates, then quintile-bucket into 5 difficulty levels. This BREAKS the circularity concern — difficulty is estimated from the pre-RL model, independent of gaming that develops during GRPO training. We also validate the difficulty proxy by checking rank-correlation with question complexity metadata where available (medical specialty, multi-step reasoning requirements). We produce K×5 gaming heatmaps for both domains, define the Dimension Exploitation Gap (DEG = rubric_pass_rate − verified_pass_rate per criterion per difficulty), and test all three predictions. Cross-domain comparison: we test whether the STRUCTURE of the gaming surface (which criteria types are most exploitable, at which relative difficulty) transfers across domains, even if absolute values differ. **Contribution 3 — DCRR Proof-of-Concept (ICLR 2027 scope only).** We first run DGPO+RRM as the critical baseline: if naively combining difficulty-aware optimization (DGPO) with rubric rewards (RRM) already closes most of the gap, DCRR adds marginal value. If it leaves >20% gap, we apply Difficulty-Calibrated Rubric Rewards using the T3 schedule. Evaluation: MATH-500, comparing GRPO, GRPO+RRM, DGPO+RRM, MO-GRPO+RRM, and DCRR, plus cross-domain gaming heatmaps. **Venue Strategy:** Primary target: ICLR 2027 (~Sep 24, 17 weeks) — full three-contribution scope. Decision-gated stretch: AAAI 2027 (Jul 21 abstract) — MATH-ONLY, Contributions 1-2 only, requires strong results by Jul 9 decision gate. Backup: ARR August 3 → EACL 2027 — intermediate scope (math + medical diagnostics, no DCRR). **Concrete timeline (ICLR primary):** Weeks 1-3 (May 28 - Jun 18): Theory formalization (T1, T2) + infrastructure (verl scripts, judge pipeline) + start math training (GRPO, GRPO+RRM, DGPO+RRM — 3 runs). Weeks 4-5 (Jun 18 - Jul 2): Math training complete + judge inference + initial gaming heatmap analysis + prediction testing. Week 6 (Jul 2 - Jul 9): Draft core results section. **AAAI decision gate (Jul 9):** If math results show clear non-trivial gaming structure AND draft is ≥60% complete, fast-track AAAI submission (Jul 21 abstract, Jul 28 paper, math-only). Otherwise, continue ICLR plan. Weeks 7-9 (Jul 9 - Jul 30): Medical domain training (GRPO, GRPO+RRM, DGPO+RRM — 3 runs) + cross-domain analysis. Weeks 10-12 (Jul 30 - Aug 27): DCRR experiments + MO-GRPO+RRM baseline + ablations. Weeks 13-15 (Aug 27 - Sep 17): Full paper writing, figures, cross-domain comparison. Weeks 16-17 (Sep 17 - Sep 24): Revision, polishing, submission. **AAAI stretch plan (math-only, 6-week sprint + 2 weeks buffer):** Weeks 1-2: Theory + infrastructure + training. Weeks 3-4: Judge inference + analysis + prediction testing. Week 5: First complete draft. Week 6 (Jul 9 decision gate): Assess results quality. If proceeding: Weeks 7-8: Polish + submit.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "175 H100-hours (Math: 6 training runs × 4 H100 × 2.5hr = 60hr, rubric judge inference 40hr, Pass@64 on MATH-500 subset 25hr; Medical: 3 training runs × 4 H100 × 2hr = 24hr, SFT-init difficulty oracle rollouts 3hr, judge inference 10hr; Analysis + overhead 13hr)",
      "timeline": "17 weeks for ICLR 2027 full scope. 8 weeks for AAAI stretch (math-only, Contributions 1-2).",
      "estimated_gpu_cost": "$438 (H100 at ~$2.50/hr)"
    },
    "human_in_loop": {
      "gpu_hours": "175 H100-hours (same; Claude accelerates code/analysis, not GPU work)",
      "timeline": "14-15 weeks for ICLR 2027 (Claude assists theorem formalization, verl training scripts, automated heatmap generation, cross-domain analysis, writing). 7 weeks for AAAI stretch.",
      "claude_api_cost": "$200 (Sonnet 4.6 for rubric generation across both domains, code scaffolding, analysis, writing)",
      "estimated_gpu_cost": "$438"
    },
    "auto_research": {
      "gpu_hours": "180 H100-hours (5hr margin for targeted hyperparameter exploration)",
      "timeline": "10-12 weeks for ICLR (parallelized experiment dispatch, automated analysis, Claude-drafted paper)",
      "claude_api_cost": "$380 (rubric judging quality audit ~5K samples per domain, automated analysis, writing)",
      "estimated_gpu_cost": "$450",
      "speed_bottleneck": "LLM judge inference throughput — scoring ~50K math + ~25K medical rollouts per model with Qwen3-8B requires ~8hr per model on 4×H100"
    },
    "aaai_stretch_scope": {
      "gpu_hours": "55 H100-hours (Math only: 3 training runs × 4 H100 × 2.5hr = 30hr, judge inference 20hr, analysis 5hr)",
      "timeline": "8 weeks (6-week sprint + 2 weeks buffer; decision gate at week 6)",
      "estimated_gpu_cost": "$138",
      "scope": "Contributions 1-2, math-only: Gaming Budget theorem (T1-T2) + MATH gaming heatmaps + 3 falsifiable predictions tested. No medical domain, no DCRR, no T3 full proof."
    }
  },
  "target_venues": [
    "ICLR 2027 (~Sep 24, 2026 — primary target, 17 weeks; full three-contribution scope including cross-domain math + medical, complete Gaming Budget theory with ranking validation, and DCRR proof-of-concept)",
    "AAAI 2027 (abstract Jul 21, paper Jul 28, 2026 — decision-gated stretch, 8 weeks; MATH-ONLY Contributions 1-2, requires strong results by Jul 9 decision gate to proceed; if gate fails, fold into ICLR submission)",
    "ARR August 3, 2026 → EACL 2027 (~10 weeks; intermediate scope: math + medical diagnostics without DCRR; NLP-venue backup if AAAI gate fails but results warrant earlier publication)"
  ],
  "level": "top-tier",
  "key_references": [
    "Goodhart's Law in Reinforcement Learning (ICLR 2024) — Geometric explanation for Goodhart's law in MDPs; shows optimization pressure increases Goodharting; aggregate scalar analysis. Our Gaming Budget extends to K-dimensional evaluation with difficulty variation",
    "Reward Hacking as Equilibrium under Finite Evaluation (arXiv:2603.28063) — Structural equilibrium proof via Holmstrom-Milgrom under 5 axioms; derives distortion index predicting direction/severity per dimension. EXISTENCE proof — our work makes it CONSTRUCTIVE and difficulty-parameterized",
    "Robust Optimization for Mitigating Reward Hacking with Correlated Proxies (arXiv:2604.12086, ICLR 2026) — Max-min formulation over r-correlated scalar proxy rewards; does not decompose per-criterion or model difficulty-varying correlation",
    "The Strong, Weak and Benign Goodhart's Law (arXiv:2505.23445) — Independence-free formalization; scalar proxy-goal pair, no multi-dimensional or difficulty treatment",
    "Scaling Laws for Reward Model Overoptimization (ICML 2023) — Empirical scaling of overoptimization with optimization intensity; aggregate scalar analysis",
    "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv:2604.15149, ICLR 2026 Workshop) — Shows gaming prevalence 'increases with task complexity' on INDUCTIVE REASONING tasks (SLR-Bench, 4 tiers) under binary extensional verification. Establishes the aggregate-trend baseline that our per-criterion analysis tests. Note: studies different domain (inductive reasoning, not math) and different reward structure (binary, not K-dimensional rubric)",
    "Reward Hacking in Rubric-Based Reinforcement Learning (arXiv:2605.12474) — Gaming taxonomy in medical/science; 3 failure modes (partial compound criteria satisfaction, implicit-as-explicit, imprecise matching); self-internalization gap metric. Does NOT stratify by problem difficulty",
    "Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation (ICLR 2026) — DGPO Theorems 1-2 on binary-reward difficulty bias; our Gaming Budget extends beyond per-criterion vectorization",
    "Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards (ACL 2026) — RRM baseline, uniform-strictness rubric rewards for math",
    "Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains (ICLR 2026) — Foundational rubric RL; RaR-Medicine dataset for cross-domain validation",
    "On the Learning Dynamics of RLVR at the Edge of Competence (arXiv:2602.14872) — Theory of RL training dynamics on compositional tasks; smooth difficulty spectrum → relay effect. Supports our 'edge of competence' intuition from the training dynamics perspective",
    "Rethinking the Sampling Criteria in RL for LLM Reasoning: A Competence-Difficulty Alignment Perspective (arXiv:2505.17652) — CDAS framework for stable difficulty estimation via historical performance aggregation. Relevant for our difficulty oracle methodology but operates under binary rewards",
    "Bridging RL Theory and Practice with the Effective Horizon (NeurIPS 2023, Oral) — Validates theoretical bounds via RANKING CORRELATION across 155 MDPs. Direct precedent for our Gaming Budget validation strategy",
    "MO-GRPO: Mitigating Reward Hacking of GRPO on Multi-Objective Problems (arXiv:2509.22047) — Per-objective variance normalization; Theorem 1 (correlation ∝ σ_i) is the mechanism underlying dimensional exploitation, but difficulty-agnostic",
    "Step-wise Rubric Rewards for LLM Reasoning (arXiv:2605.17291) — SRaR step-level rubric attribution",
    "Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR (arXiv:2605.20164) — POW3R rollout-contrast reweighting; reactive vs. our proactive/predictive",
    "AMARIS: A Memory-Augmented Rubric Improvement System (arXiv:2605.18592) — Persistent evaluation memory; temporal dimension (rubric evolution during training) vs. our structural dimension (exploitation variation with difficulty). Complementary",
    "ARES: Automated Rubric Synthesis for Scalable LLM RL (arXiv:2605.23454) — Rubric synthesis automation; difficulty-agnostic",
    "RuCL: Stratified Rubric-Based Curriculum Learning (arXiv:2602.21628) — Adjusts by model competence not problem difficulty; vulnerable to gaming-inflated pass rates",
    "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? (NeurIPS 2025) — Pass@k frontier evaluation for binary-reward; we aim for analogous diagnostic impact in rubric-reward setting",
    "Reward Collapse in Aligning Large Language Models (arXiv:2305.17608) — Reward distribution collapse; supports our Dimensionality Collapse prediction",
    "HealthBench (arXiv:2505.08775) — Medical evaluation benchmark; 5,000 examples, ~11 criteria per example, 5 axes, Hard subset. Secondary medical evaluation benchmark",
    "CDRRM (arXiv:2603.08035), C2 (arXiv:2604.13618), Rubicon (arXiv:2508.12790) — Rubric quality/gaming defense; all difficulty-agnostic",
    "Online Difficulty Filtering for Reasoning Oriented RL (EACL 2026) — Variance-based difficulty selection theory",
    "Gradient Starvation in Binary-Reward GRPO (arXiv:2605.07689) — Per-prompt degeneracy D(p,G)=p^G+(1-p)^G; our per-criterion extension reveals structured dead zones",
    "GRPO-LEAD (arXiv:2504.09696, EMNLP 2025) — Logistic difficulty reweighting under binary rewards",
    "DARO, F-GRPO, A-GRAE, Goldilocks RL, PAPO, ARL-RR, RubricEM, Rubric-Grounded RL — Complementary difficulty-aware or rubric-optimization methods, all binary-reward or difficulty-agnostic"
  ],
  "description": "We identify and formally characterize difficulty-dependent exploitation surfaces in multi-dimensional evaluation — extending Goodhart's law from scalar proxy optimization to K-dimensional evaluation under difficulty variation. The mainstream finding is that gaming increases with task complexity in aggregate (LLMs Gaming Verifiers 2026, studying inductive reasoning; Goodhart's Law in RL, ICLR 2024). We test this at per-criterion granularity under K-dimensional rubric evaluation, hypothesizing that disaggregation reveals richer structure invisible in aggregate. We contribute: (1) a Gaming Budget framework — the first formal K-dimensional, difficulty-varying Goodhart bound, including a Gaming Budget Theorem bounding exploitable reward via the criterion-difficulty pass rate matrix, a Dimensionality Collapse Theorem proving honest signal decays faster than total signal, and a Calibration Sufficiency Condition for gaming-eliminating strictness schedules; (2) a cross-domain empirical diagnostic producing per-criterion × per-difficulty gaming surfaces for math (MATH levels 1-5) and medical reasoning (RaR-Medicine with SFT-init-derived difficulty quintiles that break circularity); (3) three quantitative falsifiable predictions — (P1) Edge of Competence: non-monotonic gaming for reasoning criteria, peaking at intermediate difficulty at ≥1.5× the rate at highest difficulty; (P2) Simpson's Paradox: surface-reasoning criterion correlation flips from positive (r>0.1) at easy levels to negative (r<-0.1) at hard levels; (P3) Asymmetric Dimensionality Collapse: K_honest/K_eff < 0.5 at the highest difficulty. The paper is designed to be valuable under either outcome: if predictions hold, it challenges the aggregate-trend consensus; if they fail, it provides the first per-criterion confirmation of monotonic gaming at rubric granularity plus a validated diagnostic framework. As a proof-of-concept defense (ICLR scope), Difficulty-Calibrated Rubric Rewards (DCRR) applies the theory's calibration schedule. Validated on Qwen2.5-Math-1.5B and Qwen2.5-1.5B-Instruct across two domains.",
  "project_name": "diff_calib_rubric_rlvr",
  "source": "web_research",
  "revision_notes": {
    "change_type": "major",
    "change_type_justification": "Major revision driven by SIMPLIFICATION and RE-ELEVATION: (1) reframed from 'rubric-RL gaming diagnosis' to 'Structured Goodhart's Law' — elevating the theoretical contribution to general evaluation theory rather than domain-specific analysis; (2) prediction structure simplified from 4 predictions to 3, with former P1 (universal exploitation channels) merged into diagnostic contribution and remaining predictions sharpened with quantitative failure thresholds; (3) H0 qualification fixed — properly attributing prior evidence to specific domains (inductive reasoning) and reward structures (binary) rather than overclaiming monotonic math-domain trends; (4) medical domain circularity resolved via SFT-init checkpoint difficulty oracle; (5) venue strategy made honest — ICLR 2027 as primary with AAAI as decision-gated stretch at Jul 9, not unrealistic parallel target; (6) field velocity addressed by positioning Gaming Budget as general evaluation theory resilient to rubric-RL method proliferation. This revision REMOVES accumulated complexity from rounds 2-5 rather than adding more, addressing the stagnation pattern directly.",
    "issue_1_AAAI_timeline": "RESOLVED via two changes: (a) ICLR 2027 is now the unambiguous primary target with a realistic 17-week timeline; (b) AAAI 2027 is repositioned as a DECISION-GATED STRETCH with an explicit Jul 9 gate — the AAAI submission proceeds ONLY IF math-only results are strong AND the draft is ≥60% complete by week 6. If the gate fails, work folds into the ICLR submission with zero wasted effort. The AAAI scope is aggressively reduced to math-only Contributions 1-2 (55 H100-hours, $138). ARR August 3 → EACL 2027 added as intermediate-scope backup (10 weeks, math + medical diagnostics without DCRR).",
    "issue_2_medical_circularity": "RESOLVED. Difficulty estimation for the medical domain now uses the SFT-init checkpoint — the policy initialization BEFORE any RL training — to generate rollouts and compute per-question pass rates, which are then quintile-bucketed into 5 difficulty levels. This completely breaks the circularity between gaming (which develops during GRPO training) and difficulty estimation (which is computed pre-RL). This approach is standard in curriculum RL: CDAS (arXiv:2505.17652) uses historical performance aggregation, AdaCuRL uses base model pass rates, Prompt Curriculum Learning (ICLR 2026) uses value model estimates. We additionally validate the difficulty proxy by checking rank-correlation with available question complexity metadata (medical specialty, multi-step reasoning markers).",
    "issue_3_H0_qualification": "RESOLVED. H0 is now carefully qualified: 'Prior work shows gaming prevalence generally increases with task complexity in aggregate settings — LLMs Gaming Verifiers (2026) studying INDUCTIVE REASONING tasks under binary extensional verification, Goodhart's Law in RL (ICLR 2024) studying MDPs with scalar rewards, Scaling Laws for RM Overoptimization (ICML 2023) under scalar reward models.' We no longer claim 'monotonic' as a direct quote — the word appears only once in an appendix of LLMs Gaming Verifiers. We frame H0 as the 'natural extrapolation' of these aggregate findings to per-criterion rubric evaluation, not as a direct claim from any single paper. This is more defensible against reviewer pushback.",
    "issue_4_impact_ceiling": "ACKNOWLEDGED HONESTLY. The revised description explicitly states: 'The paper is designed to be valuable under either outcome: if predictions hold, it challenges the aggregate-trend consensus; if they fail, it provides the first per-criterion confirmation of monotonic gaming at rubric granularity plus a validated diagnostic framework.' We further add: 'We explicitly acknowledge this [H0-confirmed version] would be a solid diagnostic paper rather than a paradigm-shifting one.' This honesty is better than over-selling. The impact ceiling is RAISED by the 'Structured Goodhart's Law' framing — even if P1-P2 fail, the Gaming Budget theorem as the first K-dimensional Goodhart formalization with difficulty has independent theoretical value beyond the specific predictions.",
    "issue_5_P1_P4_sharpened": "RESOLVED via restructuring. Former P1 (universal exploitation channels) is REMOVED as a prediction — it was indeed too intuitive ('some criteria are more gameable' is expected). It becomes a DIAGNOSTIC OBSERVATION in Contribution 2. The three remaining predictions each have QUANTITATIVE failure conditions: P1-new (Edge of Competence): peak gaming at intermediate difficulty ≥ 1.5× rate at highest difficulty; P2-new (Simpson's Paradox): r > 0.1 at levels 1-2 AND r < -0.1 at levels 4-5; P3-new (Dimensionality Collapse): K_honest/K_eff < 0.5 with K_eff ≥ 3. These are specific enough to falsify — a reviewer can check whether 1.5× holds, whether the correlation actually flips sign, whether the ratio is below 0.5.",
    "impact_broadened_to_evaluation_theory": "NEW. Following reviewer suggestion, the Gaming Budget theorem is now positioned as a general tool for ANY multi-dimensional evaluation system with difficulty variation — not just rubric-RL. The title reflects this ('Multi-Dimensional Evaluation' not 'Rubric Exploitation'). The connection to Goodhart's law literature (ICLR 2024), finite evaluation equilibrium (arXiv:2603.28063), and Robust Optimization (ICLR 2026) is made explicit: our Gaming Budget is the first constructive, K-dimensional, difficulty-parameterized extension of these scalar/aggregate frameworks. This elevates the contribution and makes it resilient to rubric-RL field velocity.",
    "stagnation_addressed": "This revision addresses the declining-score pattern by REMOVING complexity rather than adding it: (a) 4 predictions → 3; (b) P1 (low-information) removed; (c) AAAI timeline made honest with decision gate; (d) medical circularity cleanly resolved; (e) H0 properly qualified; (f) theory elevated to general evaluation theory rather than domain-specific analysis. The paper is now SIMPLER, SHARPER, and MORE DEFENSIBLE than the previous round."
  }
}
```

Please output this JSON exactly as written above. Make sure all braces, brackets, and quotes are properly balanced.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5012d8ff-ea12-42fb-983d-984bc067a5cf",
  "agentId": "a2b6bb3e2d609ddee",
  "type": "user",
  "uuid": "f1dab5cd-47a2-4c70-92d5-36eb9ed02382",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "701522b8-6e3a-4930-b8c6-816468e94e59",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T14:13:32.234Z_

```json
{
  "parentUuid": "f1dab5cd-47a2-4c70-92d5-36eb9ed02382",
  "isSidechain": true,
  "agentId": "a2b6bb3e2d609ddee",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "c1cb628e-e19d-4362-a007-46578d888588",
  "timestamp": "2026-05-28T14:13:32.234Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "701522b8-6e3a-4930-b8c6-816468e94e59",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T14:13:32.235Z_

```json
{
  "parentUuid": "c1cb628e-e19d-4362-a007-46578d888588",
  "isSidechain": true,
  "agentId": "a2b6bb3e2d609ddee",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2d46b752-478f-4fa1-b551-786c68e94202",
  "timestamp": "2026-05-28T14:13:32.235Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "701522b8-6e3a-4930-b8c6-816468e94e59",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T14:16:48.293Z_

```json
{
  "title": "Harder Problems, Easier Gaming: Difficulty-Dependent Exploitation Surfaces in Multi-Dimensional Evaluation",
  "core_problem": "Multi-dimensional evaluation systems (rubric-based RL rewards, multi-criteria benchmarks, structured assessment) face a structural vulnerability unrecognized in the Goodhart's law literature: when K evaluation criteria are applied with uniform strictness across varying task difficulty, the resulting exploitation surface has K×D structure — not K independent copies of scalar Goodhart's law. Easy-to-verify criteria (formatting, structural completeness) remain satisfiable via shallow pattern-matching even on hard problems, while hard-to-verify criteria (proof validity, factual accuracy) yield vanishing gradient signal on difficult problems, creating asymmetric exploitation opportunities. Prior work establishes that gaming increases with task complexity in aggregate settings (LLMs Gaming Verifiers 2026, studying inductive reasoning shortcuts; Goodhart's Law in RL, ICLR 2024, studying MDPs; Scaling Laws for RM Overoptimization, ICML 2023). However, these findings use aggregate metrics over binary or scalar rewards. We hypothesize that per-criterion disaggregation under K-dimensional rubric evaluation reveals richer structure: specifically, an 'edge of competence' effect where criterion-specific gaming peaks at moderate difficulty — the level where the model has just enough capability to produce plausible-looking criterion satisfaction without genuine understanding — creating non-monotonic per-criterion gaming profiles invisible in aggregate analysis. This structural vulnerability applies to any evaluation system where multi-dimensional criteria meet difficulty variation: rubric-rewarded RL, multi-criteria benchmarks, structured human evaluation. We formalize this as the first K-dimensional, difficulty-varying extension of Goodhart's law, and validate it empirically across math and medical reasoning domains.",
  "opportunity": "Five convergent gaps, now sharpened around the 'Structured Goodhart's Law' framing: (1) The Goodhart's law literature — Goodhart's Law in RL (ICLR 2024), Scaling Laws for RM Overoptimization (ICML 2023), Strong/Weak/Benign Goodhart's Law (arXiv:2505.23445) — operates on SCALAR proxy-goal pairs. The Robust Optimization framework (arXiv:2604.12086, ICLR 2026) adds correlation between scalar proxies but does not decompose per-criterion or model difficulty. No formal treatment exists for K-dimensional evaluation with difficulty-varying exploitation. (2) Wang & Huang (arXiv:2603.28063) prove reward hacking is a structural equilibrium under finite multi-dimensional evaluation via the Holmstrom-Milgrom framework and derive a distortion index — but this is an EXISTENCE proof, not a CONSTRUCTIVE characterization predicting WHICH dimensions are exploited at WHICH difficulty levels. (3) DGPO (ICLR 2026, Theorems 1-2) addresses difficulty bias in binary-reward GRPO; per-criterion application is straightforward, but the INTERACTION structure — criterion correlations shifting with difficulty, verification gaps creating asymmetric vulnerability, effective dimensionality collapsing — requires genuinely novel analysis. (4) Reward Hacking in Rubric-Based RL (arXiv:2605.12474) diagnoses gaming taxonomy in medical/science domains (3 failure modes, completeness/presence criteria concentration, self-internalization gap metric) but does NOT stratify by problem difficulty — the core analytical dimension we add. (5) LLMs Gaming Verifiers (arXiv:2604.15149) shows gaming prevalence increases with task complexity on inductive reasoning tasks under binary verification — this aggregate finding is the natural null hypothesis that our per-criterion analysis tests. The marginal contribution is threefold: (a) a Gaming Budget theorem — the first formal K-dimensional, difficulty-varying bound on exploitable reward; (b) a reusable diagnostic producing per-criterion × per-difficulty gaming surfaces; (c) three quantitative falsifiable predictions against the aggregate-trend null hypothesis, each with explicit failure conditions.",
  "landscape": "Rubric rewards for RL achieve strong results but apply uniform strictness across difficulty: RRM (ACL 2026) boosts Verified Pass@1024 on AIME2024 from 26.7% to 62.6%; RaR (ICLR 2026) extends to medical (+31% HealthBench) and science (+7% GPQA-Diamond); SRaR (arXiv:2605.17291) adds step-level attribution; POW3R (arXiv:2605.20164) adapts criterion weights via rollout variance; ARES (arXiv:2605.23454) automates rubric synthesis; AMARIS (arXiv:2605.18592) maintains persistent evaluation memory for difficulty-agnostic rubric evolution. The rubric-RL space continues rapid expansion (~8 papers in 4 weeks preceding this revision) — but this velocity STRENGTHENS our diagnostic contribution: as methods proliferate, a principled framework identifying WHICH criteria are exploited at WHICH difficulty levels becomes a shared evaluation lens no individual method paper provides. Difficulty-aware RL methods operate under binary rewards: DGPO/MathForge (ICLR 2026) via MAD normalization, DARO (arXiv:2510.09001), F-GRPO (arXiv:2602.06717), GRPO-LEAD (EMNLP 2025) via logistic weighting, A-GRAE (arXiv:2602.05548), Goldilocks RL (arXiv:2602.14868), Online Difficulty Filtering (EACL 2026), CDAS (arXiv:2505.17652) via competence-difficulty alignment, Gradient Starvation (arXiv:2605.07689) via degeneracy analysis. ALL operate under binary rewards without per-criterion gaming analysis. The closest convergence spans six categories: **Difficulty-stratified rubric calibration**: RuCL (arXiv:2602.21628) adjusts by model competence, not problem difficulty, and is vulnerable to gaming-inflated pass rates. **Multi-objective reward normalization**: MO-GRPO (arXiv:2509.22047) addresses per-objective variance bias (the mechanism underlying dimensional exploitation) but is difficulty-agnostic. **Reactive criterion reweighting**: POW3R adapts via rollout variance (reactive/diagnostic) while our approach is proactive/predictive (which criteria WILL BE gamed, inferred a priori from difficulty structure). **Memory-augmented rubric adaptation**: AMARIS addresses the temporal dimension (rubric evolution during training) while we address the structural dimension (exploitation variation with difficulty) — complementary, not competing. **Rubric quality and gaming defense**: Rubicon (arXiv:2508.12790), CDRRM (arXiv:2603.08035), C2 (arXiv:2604.13618) — all difficulty-agnostic. **Goodhart's law theory**: Goodhart's Law in RL (ICLR 2024), Robust Optimization for Correlated Proxies (ICLR 2026), Reward Hacking as Equilibrium (arXiv:2603.28063), Strong/Weak/Benign Goodhart's Law (arXiv:2505.23445) — all scalar or aggregate, none model K-dimensional + difficulty-varying exploitation. The critical gap: no work provides (a) formal K-dimensional difficulty-varying Goodhart bounds, (b) per-criterion × per-difficulty gaming diagnosis, or (c) quantitative predictions about gaming structure that can be tested against the aggregate-trend null.",
  "inspired_by": "Field guide gaps: 'No formal treatment of Goodhart's law exists for K-dimensional evaluation under difficulty variation' + 'Per-criterion × per-difficulty gaming analysis is absent from the entire rubric-RL literature.' Innovation patterns: 'Rigorous problem diagnosis as standalone contribution' (proven success — 'Does RL Really Incentivize Reasoning' diagnosed binary-reward limitations at NeurIPS 2025; 'Reward Hacking in Rubric-Based RL' diagnosed gaming taxonomy without difficulty stratification) + 'Formal analysis revealing hidden structural bias.' Core insight — the 'Edge of Competence' hypothesis: For any rubric criterion, gaming peaks at the difficulty level where the model sits at the competence boundary — enough capability to produce plausible-looking criterion satisfaction, not enough to genuinely satisfy it. Below this, the model solves correctly (no need to game); above it, the model cannot even produce plausible fakes. This creates criterion-specific inverted-U gaming profiles. This directly tests the aggregate-trend finding from LLMs Gaming Verifiers (2026): their result (gaming 'increases with task complexity') holds for aggregate binary-reward metrics, but may DISAGGREGATE into non-monotonic per-criterion patterns under rubric evaluation — analogous to Simpson's Paradox. Key framing insight: Structured Goodhart's Law. The Goodhart literature treats proxy optimization as a scalar phenomenon. Wang & Huang (2026) prove reward hacking is an equilibrium under multi-dimensional finite evaluation, but provide existence, not construction. Our Gaming Budget theorem gives the first constructive, difficulty-parameterized characterization — predicting not just THAT gaming occurs but WHERE in the K×D space it concentrates. This elevates the contribution from rubric-RL diagnosis to evaluation theory.",
  "approach": "We adopt a three-contribution structure: general evaluation theory, cross-domain empirical diagnosis, and proof-of-concept defense — ordered by robustness and generality. **Framing: Structured Goodhart's Law.** We position the paper as extending Goodhart's law to K-dimensional evaluation under difficulty variation: 'When evaluation decomposes into K criteria, Goodhart's law creates structured K×D exploitation surfaces, not K independent scalar problems. We provide the first formal characterization.' **Null Hypothesis and Falsifiable Predictions.** We test against the Aggregate-Trend Null Hypothesis (H0): 'Under H0, gaming severity increases with problem difficulty for ALL rubric criteria, following the aggregate trend observed in prior work on binary/scalar rewards (LLMs Gaming Verifiers 2026, studying inductive reasoning; Goodhart's Law in RL, ICLR 2024, studying MDPs).' Note: we carefully qualify that prior evidence comes from different domains (inductive reasoning, not math) and different reward structures (binary/scalar, not K-dimensional rubric). H0 represents the natural extrapolation of these findings to per-criterion rubric evaluation. Three falsifiable predictions with quantitative failure conditions: (P1) Edge of Competence — H0 predicts monotonically increasing gaming for reasoning-verification criteria; P1 predicts an inverted-U peaking at MATH levels 3-4. Quantitative threshold: peak gaming rate at intermediate difficulty ≥ 1.5× the rate at the highest difficulty level, measured by the Dimension Exploitation Gap. Theoretical basis: at moderate difficulty, the model has enough capability to produce plausible criterion satisfaction without genuine understanding; at high difficulty, even plausible fakes are transparent. (P2) Simpson's Paradox — H0 predicts criterion correlations weaken but maintain sign; P2 predicts the Pearson correlation between surface-criterion and reasoning-criterion satisfaction is positive at MATH levels 1-2 (r > 0.1) and negative at MATH levels 4-5 (r < -0.1), a sign flip analogous to Simpson's Paradox with difficulty as the confounding variable. (P3) Asymmetric Dimensionality Collapse — H0 predicts gradual, symmetric dimensionality reduction; P3 predicts K_honest/K_eff < 0.5 at MATH level 5, with K_eff ≥ 3. That is, honest gradient signal collapses to a lower-dimensional subspace FASTER than total signal, because gaming inflates the apparent dimensionality. **Value under either outcome:** If P1-P2 fail, the paper still contributes: (a) the first per-criterion × per-difficulty gaming characterization in any domain — confirming monotonicity per-criterion is itself new, as prior work shows only aggregate trends; (b) the Gaming Budget theorem, whose diagnostic value is independent of monotonicity; (c) evidence favoring simple monotonic calibration (a useful negative result). We explicitly acknowledge this would be a solid diagnostic paper rather than a paradigm-shifting one. **Contribution 1 — Gaming Budget Framework (domain-agnostic theory).** Three formal results for any K-dimensional evaluation system with difficulty variation: (T1) Gaming Budget Theorem — an optimization-theoretic bound on total exploitable reward at difficulty d. Formal model: pass rate matrix P ∈ [0,1]^{K×D}, verification gap matrix Δ (gap between surface-level and genuine criterion satisfaction), difficulty-varying correlation matrix Σ_d. Three assumptions: (A1) decomposability into genuine and gaming components; (A2) monotonic non-increase of reasoning-dependent pass rates with difficulty; (A3) difficulty-stable or increasing verification gaps for surface criteria. Bound: G_d ≤ Σ_{k∈V_d} w_k · δ_{k,d} · √(p_{k,d}(1−p_{k,d})) + Σ_{j&lt;k∈V_d} w_j·w_k · max(0, σ_{jk,d}) · δ_{j,d}·δ_{k,d}. Validated via RANKING ACCURACY: Spearman ρ between predicted and observed gaming severity across all K×D cells, following the Effective Horizon precedent (NeurIPS 2023 Oral). We also report: conservativeness ratio, top-3 vulnerability identification accuracy. (T2) Dimensionality Collapse Theorem — proves K_honest(d) decreases strictly faster than K_eff(d) under A2, using the observation that high-verification-stringency criteria leave the active gradient set first. (T3) Calibration Sufficiency Condition (ICLR scope only) — derives the minimal gaming-eliminating strictness schedule s_{k,d} ∝ 1/δ_{k,d} · √(p_{k,d}(1−p_{k,d})). **Contribution 2 — Cross-Domain Empirical Diagnosis.** Math domain (primary): Qwen2.5-Math-1.5B policy, Qwen3-8B judge, MATH levels 1-5 (native difficulty tags). Medical domain (generalizability test): Qwen2.5-1.5B-Instruct policy, Qwen3-8B judge, RaR-Medicine (22.4K examples, ICLR 2026). Difficulty estimation for medical domain: use the SFT-init checkpoint (the policy initialization BEFORE any RL training) to generate rollouts and compute per-question pass rates, then quintile-bucket into 5 difficulty levels. This BREAKS the circularity concern — difficulty is estimated from the pre-RL model, independent of gaming that develops during GRPO training. We also validate the difficulty proxy by checking rank-correlation with question complexity metadata where available (medical specialty, multi-step reasoning requirements). We produce K×5 gaming heatmaps for both domains, define the Dimension Exploitation Gap (DEG = rubric_pass_rate − verified_pass_rate per criterion per difficulty), and test all three predictions. Cross-domain comparison: we test whether the STRUCTURE of the gaming surface (which criteria types are most exploitable, at which relative difficulty) transfers across domains, even if absolute values differ. **Contribution 3 — DCRR Proof-of-Concept (ICLR 2027 scope only).** We first run DGPO+RRM as the critical baseline: if naively combining difficulty-aware optimization (DGPO) with rubric rewards (RRM) already closes most of the gap, DCRR adds marginal value. If it leaves >20% gap, we apply Difficulty-Calibrated Rubric Rewards using the T3 schedule. Evaluation: MATH-500, comparing GRPO, GRPO+RRM, DGPO+RRM, MO-GRPO+RRM, and DCRR, plus cross-domain gaming heatmaps. **Venue Strategy:** Primary target: ICLR 2027 (~Sep 24, 17 weeks) — full three-contribution scope. Decision-gated stretch: AAAI 2027 (Jul 21 abstract) — MATH-ONLY, Contributions 1-2 only, requires strong results by Jul 9 decision gate. Backup: ARR August 3 → EACL 2027 — intermediate scope (math + medical diagnostics, no DCRR). **Concrete timeline (ICLR primary):** Weeks 1-3 (May 28 - Jun 18): Theory formalization (T1, T2) + infrastructure (verl scripts, judge pipeline) + start math training (GRPO, GRPO+RRM, DGPO+RRM — 3 runs). Weeks 4-5 (Jun 18 - Jul 2): Math training complete + judge inference + initial gaming heatmap analysis + prediction testing. Week 6 (Jul 2 - Jul 9): Draft core results section. **AAAI decision gate (Jul 9):** If math results show clear non-trivial gaming structure AND draft is ≥60% complete, fast-track AAAI submission (Jul 21 abstract, Jul 28 paper, math-only). Otherwise, continue ICLR plan. Weeks 7-9 (Jul 9 - Jul 30): Medical domain training (GRPO, GRPO+RRM, DGPO+RRM — 3 runs) + cross-domain analysis. Weeks 10-12 (Jul 30 - Aug 27): DCRR experiments + MO-GRPO+RRM baseline + ablations. Weeks 13-15 (Aug 27 - Sep 17): Full paper writing, figures, cross-domain comparison. Weeks 16-17 (Sep 17 - Sep 24): Revision, polishing, submission. **AAAI stretch plan (math-only, 6-week sprint + 2 weeks buffer):** Weeks 1-2: Theory + infrastructure + training. Weeks 3-4: Judge inference + analysis + prediction testing. Week 5: First complete draft. Week 6 (Jul 9 decision gate): Assess results quality. If proceeding: Weeks 7-8: Polish + submit.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "175 H100-hours (Math: 6 training runs × 4 H100 × 2.5hr = 60hr, rubric judge inference 40hr, Pass@64 on MATH-500 subset 25hr; Medical: 3 training runs × 4 H100 × 2hr = 24hr, SFT-init difficulty oracle rollouts 3hr, judge inference 10hr; Analysis + overhead 13hr)",
      "timeline": "17 weeks for ICLR 2027 full scope. 8 weeks for AAAI stretch (math-only, Contributions 1-2).",
      "estimated_gpu_cost": "$438 (H100 at ~$2.50/hr)"
    },
    "human_in_loop": {
      "gpu_hours": "175 H100-hours (same; Claude accelerates code/analysis, not GPU work)",
      "timeline": "14-15 weeks for ICLR 2027 (Claude assists theorem formalization, verl training scripts, automated heatmap generation, cross-domain analysis, writing). 7 weeks for AAAI stretch.",
      "claude_api_cost": "$200 (Sonnet 4.6 for rubric generation across both domains, code scaffolding, analysis, writing)",
      "estimated_gpu_cost": "$438"
    },
    "auto_research": {
      "gpu_hours": "180 H100-hours (5hr margin for targeted hyperparameter exploration)",
      "timeline": "10-12 weeks for ICLR (parallelized experiment dispatch, automated analysis, Claude-drafted paper)",
      "claude_api_cost": "$380 (rubric judging quality audit ~5K samples per domain, automated analysis, writing)",
      "estimated_gpu_cost": "$450",
      "speed_bottleneck": "LLM judge inference throughput — scoring ~50K math + ~25K medical rollouts per model with Qwen3-8B requires ~8hr per model on 4×H100"
    },
    "aaai_stretch_scope": {
      "gpu_hours": "55 H100-hours (Math only: 3 training runs × 4 H100 × 2.5hr = 30hr, judge inference 20hr, analysis 5hr)",
      "timeline": "8 weeks (6-week sprint + 2 weeks buffer; decision gate at week 6)",
      "estimated_gpu_cost": "$138",
      "scope": "Contributions 1-2, math-only: Gaming Budget theorem (T1-T2) + MATH gaming heatmaps + 3 falsifiable predictions tested. No medical domain, no DCRR, no T3 full proof."
    }
  },
  "target_venues": [
    "ICLR 2027 (~Sep 24, 2026 — primary target, 17 weeks; full three-contribution scope including cross-domain math + medical, complete Gaming Budget theory with ranking validation, and DCRR proof-of-concept)",
    "AAAI 2027 (abstract Jul 21, paper Jul 28, 2026 — decision-gated stretch, 8 weeks; MATH-ONLY Contributions 1-2, requires strong results by Jul 9 decision gate to proceed; if gate fails, fold into ICLR submission)",
    "ARR August 3, 2026 → EACL 2027 (~10 weeks; intermediate scope: math + medical diagnostics without DCRR; NLP-venue backup if AAAI gate fails but results warrant earlier publication)"
  ],
  "level": "top-tier",
  "key_references": [
    "Goodhart's Law in Reinforcement Learning (ICLR 2024) — Geometric explanation for Goodhart's law in MDPs; shows optimization pressure increases Goodharting; aggregate scalar analysis. Our Gaming Budget extends to K-dimensional evaluation with difficulty variation",
    "Reward Hacking as Equilibrium under Finite Evaluation (arXiv:2603.28063) — Structural equilibrium proof via Holmstrom-Milgrom under 5 axioms; derives distortion index predicting direction/severity per dimension. EXISTENCE proof — our work makes it CONSTRUCTIVE and difficulty-parameterized",
    "Robust Optimization for Mitigating Reward Hacking with Correlated Proxies (arXiv:2604.12086, ICLR 2026) — Max-min formulation over r-correlated scalar proxy rewards; does not decompose per-criterion or model difficulty-varying correlation",
    "The Strong, Weak and Benign Goodhart's Law (arXiv:2505.23445) — Independence-free formalization; scalar proxy-goal pair, no multi-dimensional or difficulty treatment",
    "Scaling Laws for Reward Model Overoptimization (ICML 2023) — Empirical scaling of overoptimization with optimization intensity; aggregate scalar analysis",
    "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv:2604.15149, ICLR 2026 Workshop) — Shows gaming prevalence 'increases with task complexity' on INDUCTIVE REASONING tasks (SLR-Bench, 4 tiers) under binary extensional verification. Establishes the aggregate-trend baseline that our per-criterion analysis tests. Note: studies different domain (inductive reasoning, not math) and different reward structure (binary, not K-dimensional rubric)",
    "Reward Hacking in Rubric-Based Reinforcement Learning (arXiv:2605.12474) — Gaming taxonomy in medical/science; 3 failure modes (partial compound criteria satisfaction, implicit-as-explicit, imprecise matching); self-internalization gap metric. Does NOT stratify by problem difficulty",
    "Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation (ICLR 2026) — DGPO Theorems 1-2 on binary-reward difficulty bias; our Gaming Budget extends beyond per-criterion vectorization",
    "Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards (ACL 2026) — RRM baseline, uniform-strictness rubric rewards for math",
    "Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains (ICLR 2026) — Foundational rubric RL; RaR-Medicine dataset for cross-domain validation",
    "On the Learning Dynamics of RLVR at the Edge of Competence (arXiv:2602.14872) — Theory of RL training dynamics on compositional tasks; smooth difficulty spectrum → relay effect. Supports our 'edge of competence' intuition from the training dynamics perspective",
    "Rethinking the Sampling Criteria in RL for LLM Reasoning: A Competence-Difficulty Alignment Perspective (arXiv:2505.17652) — CDAS framework for stable difficulty estimation via historical performance aggregation. Relevant for our difficulty oracle methodology but operates under binary rewards",
    "Bridging RL Theory and Practice with the Effective Horizon (NeurIPS 2023, Oral) — Validates theoretical bounds via RANKING CORRELATION across 155 MDPs. Direct precedent for our Gaming Budget validation strategy",
    "MO-GRPO: Mitigating Reward Hacking of GRPO on Multi-Objective Problems (arXiv:2509.22047) — Per-objective variance normalization; Theorem 1 (correlation ∝ σ_i) is the mechanism underlying dimensional exploitation, but difficulty-agnostic",
    "Step-wise Rubric Rewards for LLM Reasoning (arXiv:2605.17291) — SRaR step-level rubric attribution",
    "Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR (arXiv:2605.20164) — POW3R rollout-contrast reweighting; reactive vs. our proactive/predictive",
    "AMARIS: A Memory-Augmented Rubric Improvement System (arXiv:2605.18592) — Persistent evaluation memory; temporal dimension (rubric evolution during training) vs. our structural dimension (exploitation variation with difficulty). Complementary",
    "ARES: Automated Rubric Synthesis for Scalable LLM RL (arXiv:2605.23454) — Rubric synthesis automation; difficulty-agnostic",
    "RuCL: Stratified Rubric-Based Curriculum Learning (arXiv:2602.21628) — Adjusts by model competence not problem difficulty; vulnerable to gaming-inflated pass rates",
    "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? (NeurIPS 2025) — Pass@k frontier evaluation for binary-reward; we aim for analogous diagnostic impact in rubric-reward setting",
    "Reward Collapse in Aligning Large Language Models (arXiv:2305.17608) — Reward distribution collapse; supports our Dimensionality Collapse prediction",
    "HealthBench (arXiv:2505.08775) — Medical evaluation benchmark; 5,000 examples, ~11 criteria per example, 5 axes, Hard subset. Secondary medical evaluation benchmark",
    "CDRRM (arXiv:2603.08035), C2 (arXiv:2604.13618), Rubicon (arXiv:2508.12790) — Rubric quality/gaming defense; all difficulty-agnostic",
    "Online Difficulty Filtering for Reasoning Oriented RL (EACL 2026) — Variance-based difficulty selection theory",
    "Gradient Starvation in Binary-Reward GRPO (arXiv:2605.07689) — Per-prompt degeneracy D(p,G)=p^G+(1-p)^G; our per-criterion extension reveals structured dead zones",
    "GRPO-LEAD (arXiv:2504.09696, EMNLP 2025) — Logistic difficulty reweighting under binary rewards",
    "DARO, F-GRPO, A-GRAE, Goldilocks RL, PAPO, ARL-RR, RubricEM, Rubric-Grounded RL — Complementary difficulty-aware or rubric-optimization methods, all binary-reward or difficulty-agnostic"
  ],
  "description": "We identify and formally characterize difficulty-dependent exploitation surfaces in multi-dimensional evaluation — extending Goodhart's law from scalar proxy optimization to K-dimensional evaluation under difficulty variation. The mainstream finding is that gaming increases with task complexity in aggregate (LLMs Gaming Verifiers 2026, studying inductive reasoning; Goodhart's Law in RL, ICLR 2024). We test this at per-criterion granularity under K-dimensional rubric evaluation, hypothesizing that disaggregation reveals richer structure invisible in aggregate. We contribute: (1) a Gaming Budget framework — the first formal K-dimensional, difficulty-varying Goodhart bound, including a Gaming Budget Theorem bounding exploitable reward via the criterion-difficulty pass rate matrix, a Dimensionality Collapse Theorem proving honest signal decays faster than total signal, and a Calibration Sufficiency Condition for gaming-eliminating strictness schedules; (2) a cross-domain empirical diagnostic producing per-criterion × per-difficulty gaming surfaces for math (MATH levels 1-5) and medical reasoning (RaR-Medicine with SFT-init-derived difficulty quintiles that break circularity); (3) three quantitative falsifiable predictions — (P1) Edge of Competence: non-monotonic gaming for reasoning criteria, peaking at intermediate difficulty at ≥1.5× the rate at highest difficulty; (P2) Simpson's Paradox: surface-reasoning criterion correlation flips from positive (r>0.1) at easy levels to negative (r<-0.1) at hard levels; (P3) Asymmetric Dimensionality Collapse: K_honest/K_eff < 0.5 at the highest difficulty. The paper is designed to be valuable under either outcome: if predictions hold, it challenges the aggregate-trend consensus; if they fail, it provides the first per-criterion confirmation of monotonic gaming at rubric granularity plus a validated diagnostic framework. As a proof-of-concept defense (ICLR scope), Difficulty-Calibrated Rubric Rewards (DCRR) applies the theory's calibration schedule. Validated on Qwen2.5-Math-1.5B and Qwen2.5-1.5B-Instruct across two domains.",
  "project_name": "diff_calib_rubric_rlvr",
  "source": "web_research",
  "revision_notes": {
    "change_type": "major",
    "change_type_justification": "Major revision driven by SIMPLIFICATION and RE-ELEVATION: (1) reframed from 'rubric-RL gaming diagnosis' to 'Structured Goodhart's Law' — elevating the theoretical contribution to general evaluation theory rather than domain-specific analysis; (2) prediction structure simplified from 4 predictions to 3, with former P1 (universal exploitation channels) merged into diagnostic contribution and remaining predictions sharpened with quantitative failure thresholds; (3) H0 qualification fixed — properly attributing prior evidence to specific domains (inductive reasoning) and reward structures (binary) rather than overclaiming monotonic math-domain trends; (4) medical domain circularity resolved via SFT-init checkpoint difficulty oracle; (5) venue strategy made honest — ICLR 2027 as primary with AAAI as decision-gated stretch at Jul 9, not unrealistic parallel target; (6) field velocity addressed by positioning Gaming Budget as general evaluation theory resilient to rubric-RL method proliferation. This revision REMOVES accumulated complexity from rounds 2-5 rather than adding more, addressing the stagnation pattern directly.",
    "issue_1_AAAI_timeline": "RESOLVED via two changes: (a) ICLR 2027 is now the unambiguous primary target with a realistic 17-week timeline; (b) AAAI 2027 is repositioned as a DECISION-GATED STRETCH with an explicit Jul 9 gate — the AAAI submission proceeds ONLY IF math-only results are strong AND the draft is ≥60% complete by week 6. If the gate fails, work folds into the ICLR submission with zero wasted effort. The AAAI scope is aggressively reduced to math-only Contributions 1-2 (55 H100-hours, $138). ARR August 3 → EACL 2027 added as intermediate-scope backup (10 weeks, math + medical diagnostics without DCRR).",
    "issue_2_medical_circularity": "RESOLVED. Difficulty estimation for the medical domain now uses the SFT-init checkpoint — the policy initialization BEFORE any RL training — to generate rollouts and compute per-question pass rates, which are then quintile-bucketed into 5 difficulty levels. This completely breaks the circularity between gaming (which develops during GRPO training) and difficulty estimation (which is computed pre-RL). This approach is standard in curriculum RL: CDAS (arXiv:2505.17652) uses historical performance aggregation, AdaCuRL uses base model pass rates, Prompt Curriculum Learning (ICLR 2026) uses value model estimates. We additionally validate the difficulty proxy by checking rank-correlation with available question complexity metadata (medical specialty, multi-step reasoning markers).",
    "issue_3_H0_qualification": "RESOLVED. H0 is now carefully qualified: 'Prior work shows gaming prevalence generally increases with task complexity in aggregate settings — LLMs Gaming Verifiers (2026) studying INDUCTIVE REASONING tasks under binary extensional verification, Goodhart's Law in RL (ICLR 2024) studying MDPs with scalar rewards, Scaling Laws for RM Overoptimization (ICML 2023) under scalar reward models.' We no longer claim 'monotonic' as a direct quote — the word appears only once in an appendix of LLMs Gaming Verifiers. We frame H0 as the 'natural extrapolation' of these aggregate findings to per-criterion rubric evaluation, not as a direct claim from any single paper. This is more defensible against reviewer pushback.",
    "issue_4_impact_ceiling": "ACKNOWLEDGED HONESTLY. The revised description explicitly states: 'The paper is designed to be valuable under either outcome: if predictions hold, it challenges the aggregate-trend consensus; if they fail, it provides the first per-criterion confirmation of monotonic gaming at rubric granularity plus a validated diagnostic framework.' We further add: 'We explicitly acknowledge this [H0-confirmed version] would be a solid diagnostic paper rather than a paradigm-shifting one.' This honesty is better than over-selling. The impact ceiling is RAISED by the 'Structured Goodhart's Law' framing — even if P1-P2 fail, the Gaming Budget theorem as the first K-dimensional Goodhart formalization with difficulty has independent theoretical value beyond the specific predictions.",
    "issue_5_P1_P4_sharpened": "RESOLVED via restructuring. Former P1 (universal exploitation channels) is REMOVED as a prediction — it was indeed too intuitive ('some criteria are more gameable' is expected). It becomes a DIAGNOSTIC OBSERVATION in Contribution 2. The three remaining predictions each have QUANTITATIVE failure conditions: P1-new (Edge of Competence): peak gaming at intermediate difficulty ≥ 1.5× rate at highest difficulty; P2-new (Simpson's Paradox): r > 0.1 at levels 1-2 AND r < -0.1 at levels 4-5; P3-new (Dimensionality Collapse): K_honest/K_eff < 0.5 with K_eff ≥ 3. These are specific enough to falsify — a reviewer can check whether 1.5× holds, whether the correlation actually flips sign, whether the ratio is below 0.5.",
    "impact_broadened_to_evaluation_theory": "NEW. Following reviewer suggestion, the Gaming Budget theorem is now positioned as a general tool for ANY multi-dimensional evaluation system with difficulty variation — not just rubric-RL. The title reflects this ('Multi-Dimensional Evaluation' not 'Rubric Exploitation'). The connection to Goodhart's law literature (ICLR 2024), finite evaluation equilibrium (arXiv:2603.28063), and Robust Optimization (ICLR 2026) is made explicit: our Gaming Budget is the first constructive, K-dimensional, difficulty-parameterized extension of these scalar/aggregate frameworks. This elevates the contribution and makes it resilient to rubric-RL field velocity.",
    "stagnation_addressed": "This revision addresses the declining-score pattern by REMOVING complexity rather than adding it: (a) 4 predictions → 3; (b) P1 (low-information) removed; (c) AAAI timeline made honest with decision gate; (d) medical circularity cleanly resolved; (e) H0 properly qualified; (f) theory elevated to general evaluation theory rather than domain-specific analysis. The paper is now SIMPLER, SHARPER, and MORE DEFENSIBLE than the previous round."
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d46b752-478f-4fa1-b551-786c68e94202",
  "isSidechain": true,
  "agentId": "a2b6bb3e2d609ddee",
  "requestId": "req_011CbV73qQRRkAVXc3YgXqQo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9d230df-d9ae-4330-ae27-350224924901",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "701522b8-6e3a-4930-b8c6-816468e94e59",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018WAABRECzbouQZfgDmF6F8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18958,
      "cache_read_input_tokens": 0,
      "output_tokens": 9046,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18958
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 9046,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18958,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18958,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
