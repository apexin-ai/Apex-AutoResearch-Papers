# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # The Learning-Gaming Paradox: Diff

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/6b652129-f5f9-4b79-925a-79163dceced3.jsonl`
- **Structured JSON:** [`2051309b4b09220aaec0.json`](../../sessions/20/2051309b4b09220aaec0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T16:49:22.214Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T16:49:22.214Z",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# The Learning-Gaming Paradox: Difficulty-Dependent Exploitation Surfaces in Multi-Dimensional Evaluation\n\n## Core Problem\n\nRubric-rewarded RL faces a structural tension unrecognized in prior work: the difficulty level where GRPO training signal is strongest is simultaneously where gaming opportunity is maximal. The Gradient Starvation analysis (arXiv:2605.07689) proves that GRPO's non-degenerate fraction N(p,G) = 1 - p^G - (1-p)^G is maximized at p = 0.5 (for G=2, N(p,2) = 2p(1-p), exactly proportional to p(1-p)); our Gaming Budget bound shows each criterion's gaming opportunity scales as √(p_k(1−p_k)), also maximized at p_k = 0.5. Both quantities peak at intermediate pass rates, meaning that difficulty-aware GRPO methods (DGPO, CDAS, Goldilocks RL) that correctly select problems in the p̄_d ∈ [0.3, 0.7] band for maximal learning efficiency inadvertently maximize gaming exposure under multi-dimensional rubric evaluation. The Edge of Competence analysis (arXiv:2602.14872, Lemma 6.2) provides further support: the multi-step learning gradient follows ∇_q J̃_L ∝ (Δ_L)^L(1−Δ_L) with peak at Δ*=L/(L+1), corresponding to pass rates p*=(L/(L+1))^L ∈ [1/e, 1/2] ≈ [0.37, 0.50] for reasoning chains of length L — still within the gaming-vulnerable band. (Note: the Edge of Competence result uses the attention margin Δ_L, not the pass rate p directly, and the functional form (Δ)^L(1−Δ) differs from p(1−p); we cite it for qualitative support that multi-step learning also concentrates at intermediate pass rates, not for a shared functional form.) This Learning-Gaming Paradox is structural — it arises whenever K evaluation criteria are applied with uniform strictness across varying task difficulty under GRPO-family training, because easy-to-verify criteria (formatting, structural completeness) remain satisfiable via shallow pattern-matching at intermediate-difficulty problems, while hard-to-verify criteria (proof validity, factual accuracy) yield their most ambiguous signal precisely there. The consequence is a K×D exploitation surface with difficulty-dependent structure that neither scalar Goodhart analysis (ICLR 2024; ICML 2023) nor static per-dimension distortion indices (Wang & Huang 2026, D_i = λ(r_i/w_i) + (1−λ)) can capture. Wang & Huang's D_i ranking (Corollary 1a) assumes symmetric production functions and treats all tasks identically — it cannot model how the exploitation landscape shifts across difficulty because difficulty-varying verification gaps δ_{k,d} and criterion correlations Σ_d are outside the model's scope (their Remark 2). Meanwhile, Reward Hacking in Rubric-Based RL (arXiv:2605.12474) diagnoses per-criterion gaming (90.2% presence-based concentration) but does NOT stratify by problem difficulty. LLMs Gaming Verifiers (arXiv:2604.15149) and Hack-Verifiable Environments (arXiv:2605.20744) show gaming/hacking increases monotonically with task difficulty in aggregate. Neither captures the paradox: the difficulty band that GRPO training should focus on for maximum learning efficiency is the difficulty band that rubric gaming exploits most effectively.\n\n## Research Opportunity\n\nSix convergent gaps, now organized around the Learning-Gaming Paradox: (1) The Goodhart's law literature — Goodhart's Law in RL (ICLR 2024), Scaling Laws for RM Overoptimization (ICML 2023), Strong/Weak/Benign Goodhart's Law (arXiv:2505.23445) — operates on SCALAR proxy-goal pairs. The Robust Optimization framework (arXiv:2604.12086, ICLR 2026) adds correlation between scalar proxies but does not decompose per-criterion or model difficulty. No formal treatment exists for K-dimensional evaluation with difficulty-varying exploitation. (2) Wang & Huang (arXiv:2603.28063) derive a constructive per-dimension distortion index D_i with Corollary 1(a) providing a ranking result under symmetric production functions. However, their model treats all tasks identically — it cannot predict how the exploitation landscape shifts with difficulty d, because difficulty-varying verification gaps δ_{k,d} and correlations Σ_d are outside the model's scope (flagged in their Remark 2). Our framework extends D_i to D_i(d), recovering their ranking as a special case when difficulty is constant. (3) The Gradient Starvation analysis (arXiv:2605.07689) proves GRPO's learning signal peaks at intermediate pass rates: the non-degenerate fraction N(p,G) = 1−p^G−(1−p)^G is maximized at p=0.5, with degeneracy rates of 0.69 observed at G=4 in practice. The Edge of Competence (arXiv:2602.14872) establishes a complementary result for multi-step reasoning: the learning gradient ∇_q J̃_L ∝ (Δ_L)^L(1−Δ_L) peaks at attention margins Δ*=L/(L+1), corresponding to pass rates p*=(L/(L+1))^L ∈ [1/e, 1/2] — still within the intermediate range. Both results establish that RL learning concentrates at intermediate pass rates. NO PRIOR WORK connects this to gaming vulnerability: we show that the Gaming Budget bound's per-criterion terms √(p_k(1−p_k)) are ALSO maximized at intermediate pass rates. This peak coincidence — GRPO learning efficiency and gaming opportunity both maximized in the p ∈ [0.3, 0.7] band — is the Learning-Gaming Paradox. (4) DGPO (ICLR 2026, Theorems 1-2) addresses difficulty bias in binary-reward GRPO; per-criterion application is straightforward, but the INTERACTION structure — criterion correlations shifting with difficulty, verification gaps creating asymmetric vulnerability, learning-gaming tension at the competence boundary — requires genuinely novel analysis. (5) Reward Hacking in Rubric-Based RL (arXiv:2605.12474) diagnoses gaming taxonomy (3 failure modes, 90.2% presence-based criteria concentration) but does NOT stratify by problem difficulty — the core analytical dimension we add. (6) LLMs Gaming Verifiers (arXiv:2604.15149) and Hack-Verifiable Environments (arXiv:2605.20744) show gaming/hacking severity increases monotonically with task difficulty in aggregate — combined with arXiv:2605.12474's criterion-type finding, this forms our composite null hypothesis. The marginal contribution is fourfold: (a) the Learning-Gaming Paradox — identifying that GRPO's learning-efficient zone (Gradient Starvation) coincides with rubric gaming's exploitation peak (Gaming Budget), with supplementary support from Edge of Competence's multi-step analysis; (b) a Learning-Gaming Duality framework with co-equal Gaming Budget Theorem (T1) and Dimensionality Collapse Theorem (T2), extending Wang & Huang's static D_i to difficulty-varying D_i(d) trajectories; (c) a reusable diagnostic producing per-criterion × per-difficulty gaming surfaces with rigorous statistical methodology (10 difficulty bins, bootstrap CIs, formal non-monotonicity tests); (d) three quantitative falsifiable predictions against a strengthened composite null hypothesis, with concrete methodological value under either outcome — including derivation and validation of monotonic calibration schedules under H0.\n\n## Research Landscape\n\nRubric rewards for RL achieve strong results but apply uniform strictness across difficulty: RRM (ACL 2026) boosts Verified Pass@1024 on AIME2024 from 26.7% to 62.6%; RaR (ICLR 2026) extends to medical (+31% HealthBench) and science (+7% GPQA-Diamond); SRaR (arXiv:2605.17291) adds step-level attribution; POW3R (arXiv:2605.20164) adapts criterion weights via rollout variance; ARES (arXiv:2605.23454) automates rubric synthesis; AMARIS (arXiv:2605.18592) maintains persistent evaluation memory for difficulty-agnostic rubric evolution. ARL-RR (arXiv:2603.15646) addresses the scalarization problem by alternating optimization across rubric meta-classes (accuracy, completeness, instruction following, context awareness, communication quality), which is algorithmic (changing the optimization procedure) rather than diagnostic (characterizing which criteria are exploitable at which difficulty levels). The rubric-RL space continues rapid expansion (~10+ papers in 4 weeks preceding this revision) — but this velocity STRENGTHENS our diagnostic contribution: as methods proliferate, a principled framework identifying WHICH criteria are exploited at WHICH difficulty levels becomes a shared evaluation lens no individual method paper provides. Difficulty-aware RL methods operate under binary rewards: DGPO/MathForge (ICLR 2026) via MAD normalization, DARO (arXiv:2510.09001), F-GRPO (arXiv:2602.06717), GRPO-LEAD (EMNLP 2025) via logistic weighting, A-GRAE (arXiv:2602.05548), Goldilocks RL (arXiv:2602.14868), Online Difficulty Filtering (EACL 2026), CDAS (arXiv:2505.17652) via competence-difficulty alignment, Gradient Starvation (arXiv:2605.07689) via degeneracy analysis. ALL operate under binary rewards without per-criterion gaming analysis. Difficulty-calibrated advantage reweighting is an active concurrent direction: Unlocking the Potential of Difficulty Prior (arXiv:2505.13261) explicitly models difficulty priors to calibrate reasoning depth and reweight advantages in multimodal RL — while targeting training efficiency rather than gaming characterization, it demonstrates independent convergence on difficulty-aware reward modulation. The closest convergence spans eight categories: **Difficulty-stratified rubric calibration**: RuCL (arXiv:2602.21628) adjusts by model competence, not problem difficulty, and is vulnerable to gaming-inflated pass rates. **Multi-objective reward normalization**: MO-GRPO (arXiv:2509.22047) addresses per-objective variance bias (the mechanism underlying dimensional exploitation) but is difficulty-agnostic. **Reactive criterion reweighting**: POW3R adapts via rollout-contrast (reactive/diagnostic) while our approach is proactive/predictive (which criteria WILL BE gamed, inferred a priori from difficulty structure). **Memory-augmented rubric adaptation**: AMARIS addresses the temporal dimension (rubric evolution during training) while we address the structural dimension (exploitation variation with difficulty) — complementary, not competing. **Rubric quality and gaming defense**: Rubicon (arXiv:2508.12790), CDRRM (arXiv:2603.08035), C2 (arXiv:2604.13618) — all difficulty-agnostic. **Goodhart's law theory**: Goodhart's Law in RL (ICLR 2024), Robust Optimization for Correlated Proxies (ICLR 2026), Reward Hacking as Equilibrium (arXiv:2603.28063), Strong/Weak/Benign Goodhart's Law (arXiv:2505.23445) — Wang & Huang's D_i is constructive per-dimension but static; none model K-dimensional difficulty-varying exploitation trajectories or connect to training dynamics. **Training dynamics and gaming interaction**: Gradient Starvation (arXiv:2605.07689) proves GRPO degeneracy rate D(p,G)=p^G+(1−p)^G, establishing that GRPO learning concentrates at intermediate pass rates (p≈0.5); Edge of Competence (arXiv:2602.14872) proves multi-step learning gradient ∇ ∝ (Δ_L)^L(1−Δ_L), peaking at pass rates p*=(L/(L+1))^L ∈ [0.37, 0.50]; Reward Hacking Rebounds (arXiv:2604.01476) shows gaming has dynamic phase structure. None connect these training-efficiency results to gaming vulnerability under rubric evaluation — the Learning-Gaming Paradox we identify. **Difficulty-dependent hacking measurement**: Hack-Verifiable Environments (arXiv:2605.20744) introduces a paradigm for measuring reward hacking by embedding detectable opportunities into environments, finding hack rate increases monotonically with difficulty across most models (5 models, 3 games). This provides the strongest controlled evidence for H0a but does not analyze per-criterion gaming structure or connect to training dynamics. **Per-criterion behavior across difficulty**: SPARKLE (NeurIPS 2025, arXiv:2506.04723) analyzes three reasoning dimensions across difficulty levels under RL, providing evidence that per-criterion × per-difficulty analysis is informative — but studies reasoning capability, not gaming/exploitation, and has no Goodhart framework. The critical gap: no work provides (a) identification of the Learning-Gaming Paradox — the coincidence that GRPO learning efficiency and gaming opportunity both peak at intermediate pass rates, (b) co-equal Gaming Budget and Dimensionality Collapse theorems characterizing the K×D exploitation surface, (c) per-criterion × per-difficulty gaming diagnosis with rigorous statistical methodology, or (d) quantitative predictions about gaming structure tested against a composite null hypothesis that now incorporates controlled hack-rate evidence.\n\n## Proposed Approach\n\nWe adopt a three-contribution structure centered on the Learning-Gaming Paradox, with co-equal theoretical results and concrete value under either empirical outcome. **Lead Framing: The Learning-Gaming Paradox.** We open with a structural insight connecting training dynamics to evaluation vulnerability: the Gradient Starvation analysis (arXiv:2605.07689) proves GRPO's non-degenerate fraction N(p,G) = 1−p^G−(1−p)^G is maximized at p=0.5; our Gaming Budget bound shows gaming opportunity (via √(p_k(1−p_k)) terms) is also maximized at intermediate pass rates. Because both peak in the same difficulty band (p̄_d ∈ [0.3, 0.7]), the difficulty level that GRPO training should focus on for maximum learning is simultaneously the difficulty level where rubric gaming is most effective. The Edge of Competence (arXiv:2602.14872, Lemma 6.2) provides supplementary support: the multi-step gradient ∝ (Δ_L)^L(1−Δ_L) peaks at pass rates p*=(L/(L+1))^L ∈ [0.37, 0.50], confirming that even beyond GRPO-specific analysis, multi-step RL learning concentrates at intermediate pass rates within the gaming-vulnerable band. (We are careful to distinguish: the Gradient Starvation result directly uses pass rates p and provides the formal anchor; the Edge of Competence result uses attention margins Δ_L with a different functional form and provides qualitative reinforcement.) This paradox is structural — it holds regardless of whether specific predictions about non-monotonicity (P1) are confirmed, because the PEAK COINCIDENCE between N(p,G) and the Gaming Budget is a mathematical fact. **Composite Null Hypothesis.** We test against a strengthened Composite Null (H0) built from three rubric-relevant findings: (H0a — Aggregate Trend) Gaming severity increases monotonically with problem difficulty for ALL rubric criteria, extrapolating the aggregate trend from LLMs Gaming Verifiers (arXiv:2604.15149), Hack-Verifiable Environments (arXiv:2605.20744, which finds monotonic hack-rate increase in controlled settings across 5 models and 3 environments), and Goodhart's Law in RL (ICLR 2024). (H0b — Criterion-Type Invariance) Gaming concentrates in presence-based/completeness criteria at ALL difficulty levels, extrapolating from Reward Hacking in Rubric-Based RL (arXiv:2605.12474, 90.2% presence-based concentration). Note: H0a now incorporates controlled experimental evidence (arXiv:2605.20744) alongside observational evidence; H0b is rubric-specific but difficulty-agnostic. Together they predict monotonic, criterion-type-stable gaming — a stronger adversarial target than either alone. Three falsifiable predictions with quantitative and statistical failure conditions: (P1) Learning-Gaming Resonance — H0a predicts monotonically increasing gaming for reasoning-verification criteria; P1 predicts an inverted-U peaking in the intermediate-pass-rate band (coinciding with the GRPO learning efficiency peak at p≈0.5), with peak gaming rate ≥1.5× the rate at highest-difficulty bins. Statistical test: monotone-constrained isotonic regression vs. unconstrained fit via likelihood ratio test (p < 0.05), supplemented by quadratic regression β₂ < 0 (p < 0.05). (P2) Criterion Vulnerability Shift — H0b predicts presence-based criteria dominate at all difficulty levels; P2 predicts the criterion vulnerability ordering SHIFTS with difficulty — Pearson correlation between surface-criterion and reasoning-criterion satisfaction flips from positive (r > 0.1 in bottom-quintile) to negative (r < −0.1 in top-quintile), a sign flip analogous to Simpson's Paradox. Additionally, reasoning-criterion gaming share increases ≥2× from bottom to top difficulty quintile. (P3) Asymmetric Dimensionality Collapse — P3 predicts K_honest/K_eff < 0.5 at highest-difficulty bins, with K_eff ≥ 3: honest gradient signal collapses to a lower-dimensional subspace FASTER than total signal because gaming inflates apparent dimensionality. **Concrete value under either outcome.** If P1-P3 hold: the Learning-Gaming Paradox is empirically confirmed with specific structural predictions, revealing difficulty-dependent gaming invisible to aggregate/unstratified analysis. If H0 is confirmed (monotonic, criterion-type-stable gaming): (a) the Learning-Gaming Paradox still holds structurally — even monotonically increasing gaming creates a tension with the GRPO learning signal peak at moderate difficulty, because difficulty-aware methods focus training precisely where gaming is already substantial; (b) we provide the FIRST per-criterion × per-difficulty confirmation that monotonicity and criterion-type-stability hold at every criterion individually (currently known only in aggregate or unstratified); (c) we derive and validate a simple linear strictness schedule s_k(d) = α_k + β_k·d justified by confirmed monotonicity, where β_k is proportional to the empirically measured per-criterion gaming slope, and validate that it reduces the mean DEG (Dimension Exploitation Gap) by ≥15% compared to uniform strictness on a held-out test split; (d) the Dimensionality Collapse analysis (T2) characterizes how many effective honest dimensions remain at each difficulty level, directly informing how many criteria are worth evaluating at high difficulty. We explicitly acknowledge this would be a solid diagnostic paper with a concrete calibration output, valuable to rubric-RL practitioners. **Contribution 1 — Learning-Gaming Duality Framework (domain-agnostic theory).** Four formal results for any K-dimensional evaluation system with difficulty variation under GRPO-family training: (T1) Gaming Budget Theorem — a difficulty-parameterized bound on total exploitable reward at difficulty d, extending Wang & Huang's static distortion index. Formal model: pass rate matrix P ∈ [0,1]^{K×D}, verification gap matrix Δ, difficulty-varying correlation matrix Σ_d. Four assumptions: (A1) decomposability into genuine and gaming components; (A2) monotonic non-increase of reasoning-dependent pass rates with difficulty; (A3) difficulty-stable or increasing verification gaps for surface criteria; (A4) positive correlation between criterion-level pass rates p_{k,d} and aggregate binary pass rate p̄_d (justified by the shared difficulty driver — harder problems lower both aggregate and criterion-level pass rates). Bound: G_d ≤ Σ_{k∈V_d} w_k · δ_{k,d} · √(p_{k,d}(1−p_{k,d})) + Σ_{j&lt;k∈V_d} w_j·w_k · max(0, σ_{jk,d}) · δ_{j,d}·δ_{k,d}. **Special case reduction:** When d is constant and δ_{k,d} = δ, recovers Wang & Huang's D_i ranking. (T2) Dimensionality Collapse Theorem (CO-EQUAL with T1) — proves K_honest(d) decreases strictly faster than K_eff(d) under A2, using the observation that high-verification-stringency criteria leave the active gradient set first. This is potentially more surprising than T1 because it predicts ASYMMETRIC structural behavior: gaming inflates apparent signal dimensionality while honest signal collapses, creating a growing gap that makes gaming increasingly invisible to standard diagnostics at higher difficulty. Validated via PCA on per-criterion pass-rate vectors across difficulty bins, measuring the ratio of honest-signal eigenvalues to total eigenvalues. (T3) Calibration Sufficiency Condition — derives the minimal gaming-eliminating strictness schedule s_{k,d} ∝ 1/δ_{k,d} · √(p_{k,d}(1−p_{k,d})). Under confirmed H0 (monotonic gaming), simplifies to the linear schedule s_k(d) = α_k + β_k·d with closed-form β_k. (T4) Learning-Gaming Peak Coincidence Corollary — Under assumptions A1-A4, the GRPO non-degenerate fraction N(p̄_d, G) = 1−p̄_d^G−(1−p̄_d)^G and the difficulty-marginal Gaming Budget G_d are both maximized within the difficulty band where p̄_d ∈ [0.3, 0.7]. Formally: N(p,G) achieves its unique maximum at p=0.5 (Gradient Starvation, arXiv:2605.07689); each Gaming Budget term w_k·δ_{k,d}·√(p_{k,d}(1−p_{k,d})) achieves its maximum at p_{k,d}=0.5; under A4, the Gaming Budget is near-maximal when p̄_d ≈ 0.5. Supplementary support: the Edge of Competence (arXiv:2602.14872) multi-step gradient peaks at pass rates (L/(L+1))^L ∈ [1/e, 1/2] for reasoning chains of length L, confirming that multi-step learning also concentrates in the gaming-vulnerable band. (We do NOT claim a shared functional form between (Δ)^L(1−Δ) and √(p(1−p)) — the formal connection is through peak coincidence in the pass-rate domain.) Practical consequence: difficulty-aware GRPO methods (DGPO, CDAS, Goldilocks RL) that select problems with p̄_d ≈ 0.5 for maximal learning efficiency simultaneously maximize the Gaming Budget under rubric evaluation. Validation strategy: RANKING ACCURACY (Spearman ρ between predicted and observed gaming severity across K×D cells) following the Effective Horizon precedent (NeurIPS 2023 Oral), plus conservativeness ratio and top-3 vulnerability identification accuracy. **Contribution 2 — Cross-Domain Empirical Diagnosis with Rigorous Statistics.** Math domain (primary for AAAI): Qwen2.5-Math-1.5B policy, Qwen3-8B judge, MATH dataset. **10-bin difficulty scale:** Base model generates 64 rollouts per problem → per-problem pass@1 → 10 equal-frequency difficulty bins (deciles). This provides 2× resolution for curve-fitting, continuous underlying variable for regression, independence from coarse categorical labels. MATH's native 5 levels serve as robustness check. Statistical methodology: (i) 1000-resample bootstrap 95% CIs on all DEG values; (ii) formal non-monotonicity test: isotonic regression (monotone non-decreasing constraint) vs. unconstrained kernel regression via permutation-based likelihood ratio test; (iii) quadratic regression DEG ~ β₀ + β₁d + β₂d² with one-sided test β₂ < 0; (iv) Fisher's z-test for correlation sign-flip (P2). Medical domain (ICLR scope): Qwen2.5-1.5B-Instruct policy, Qwen3-8B judge, RaR-Medicine (22.4K examples, ICLR 2026). Difficulty estimation via SFT-init checkpoint rollouts (breaks circularity). Cross-domain comparison: test whether gaming surface STRUCTURE transfers across domains. **Contribution 3 — DCRR Proof-of-Concept (ICLR scope only).** DGPO+RRM critical baseline first; if >20% gap remains, apply Difficulty-Calibrated Rubric Rewards using T3 schedule. Under H0: validate s_k(d) = α_k + β_k·d reduces mean DEG ≥15% vs. uniform strictness. **Venue Strategy (REVISED — AAAI primary, ICLR stretch).** Primary target: AAAI 2027 (abstract Jul 21, paper Jul 28, 8 weeks). Math-only, Contributions 1-2: Learning-Gaming Duality framework (T1+T2+T4 corollary + T3 monotonic special case) + MATH 10-bin gaming heatmaps + 3 predictions + monotonic calibration validation under H0. This is the natural unit — the theoretical framework + single-domain validation. Decision-gated stretch: ICLR 2027 (~Sep 24, 17 weeks). Full three-contribution scope adding medical domain + DCRR defense + cross-domain analysis. Only pursued if AAAI submission is strong AND reviewer feedback suggests expansion strengthens the work. Backup: ARR August 3 → EACL 2027 (~10 weeks, math + medical diagnostics without DCRR). **Concrete timeline (AAAI primary, 8 weeks):** Week 1 (May 28 - Jun 4): Theory formalization (T1 with Wang & Huang special case, T2 with PCA validation plan, T4 Learning-Gaming Peak Coincidence Corollary with Gradient Starvation anchor) + infrastructure setup (verl scripts, judge pipeline) + BEGIN base-model pass@1 computation (64 rollouts/problem, ~8 H100-hrs) + BEGIN GRPO training run. Week 2 (Jun 4 - Jun 11): Base-model pass@1 complete → 10-bin difficulty binning + BEGIN GRPO+RRM training run + BEGIN DGPO+RRM training run. Weeks 3-4 (Jun 11 - Jun 25): Training runs complete + judge inference on all 3 models (~20 H100-hrs total) + 10-bin gaming heatmap construction + DEG computation + bootstrap CIs + non-monotonicity tests. Week 5 (Jun 25 - Jul 2): All statistical tests (P1 isotonic regression, P2 Fisher's z-test, P3 PCA dimensionality analysis) + monotonic calibration schedule derivation and validation + draft core results. Week 6 (Jul 2 - Jul 9): DECISION GATE — evaluate: (a) are gaming surfaces non-trivial? (b) do statistical tests yield interpretable results? (c) is theory validated via ranking accuracy? If YES to all three: commit to AAAI. If NO: continue ICLR plan with 10 more weeks. Weeks 7-8 (Jul 9 - Jul 28): Paper writing, figures, polishing. Jul 21 abstract, Jul 28 paper submission. **Risk mitigation:** Training failures → keep uniform-GRPO baseline (always works), can still produce gaming surface from fewer models. Judge quality → validate on 200-sample subset before full inference. Timeline → T3 monotonic case and H0-confirmed contributions provide fallback value even if exotic predictions fail.\n\n## Detailed Description\n\nWe identify the Learning-Gaming Paradox: a structural tension in rubric-rewarded RL where the difficulty level that maximizes GRPO learning signal simultaneously maximizes gaming opportunity. The Gradient Starvation analysis (arXiv:2605.07689) proves GRPO's non-degenerate fraction N(p,G) = 1−p^G−(1−p)^G is maximized at p=0.5; our Gaming Budget bound shows gaming opportunity (via √(p(1−p)) terms) is also maximized at intermediate pass rates. Both peak in the same difficulty band (p̄_d ∈ [0.3, 0.7]), meaning difficulty-aware GRPO methods (DGPO, CDAS, Goldilocks RL) that correctly focus on this zone for learning efficiency inadvertently maximize gaming exposure under multi-dimensional rubric evaluation. The Edge of Competence analysis (arXiv:2602.14872, Lemma 6.2) provides supplementary support: the multi-step gradient (∝ (Δ_L)^L(1−Δ_L), where Δ_L is the attention margin, NOT the pass rate) peaks at pass rates p*=(L/(L+1))^L ∈ [0.37, 0.50], confirming that multi-step learning also concentrates at intermediate pass rates within the gaming-vulnerable band. We contribute: (1) a Learning-Gaming Duality framework with co-equal theoretical results — a Gaming Budget Theorem (T1) providing the first difficulty-parameterized K-dimensional Goodhart bound (extending Wang & Huang's static D_i to D_i(d) trajectories with special-case reduction), a Dimensionality Collapse Theorem (T2) proving honest signal dimensionality collapses faster than total signal making gaming increasingly invisible, a Learning-Gaming Peak Coincidence Corollary (T4) formally establishing that the GRPO non-degenerate fraction and the Gaming Budget are both maximized at intermediate pass rates (anchored to Gradient Starvation with Edge of Competence as supplementary support), and a Calibration Sufficiency Condition (T3) deriving gaming-eliminating strictness schedules that simplify to s_k(d) = α_k + β_k·d under confirmed monotonicity; (2) a cross-domain empirical diagnostic using 10-bin difficulty scales (base-model pass-rate deciles) with bootstrap CIs and formal non-monotonicity tests, producing per-criterion × per-difficulty gaming surfaces; (3) three falsifiable predictions against a composite null hypothesis strengthened by Hack-Verifiable Environments (arXiv:2605.20744) — (P1) Learning-Gaming Resonance: non-monotonic gaming for reasoning criteria peaking in the GRPO-efficient band at ≥1.5× the highest-difficulty rate; (P2) Criterion Vulnerability Shift: surface-reasoning correlation sign-flip plus ≥2× reasoning-criterion gaming share increase; (P3) Asymmetric Dimensionality Collapse: K_honest/K_eff < 0.5 at highest difficulty. The paper delivers concrete value under either outcome: if predictions hold, it reveals difficulty-dependent structure invisible to prior analysis; if H0 is confirmed, it provides the first per-criterion × per-difficulty confirmation of monotonic gaming, derives and validates a simple linear calibration schedule reducing mean DEG by ≥15%, and characterizes effective honest dimensionality at each difficulty level. Validated on Qwen2.5-Math-1.5B (AAAI primary, math) with Qwen2.5-1.5B-Instruct cross-domain validation (ICLR stretch, medical).\n\n## Key References\n\n- Gradient Starvation in Binary-Reward GRPO (arXiv:2605.07689) — GRPO degeneracy rate D(p,G)=p^G+(1−p)^G; non-degenerate fraction N(p,G)=1−p^G−(1−p)^G maximized at p=0.5 (for G=2, N=2p(1−p); observed 0.69 degeneracy at G=4 in Qwen3.5-9B). CRITICAL for our Learning-Gaming Paradox: provides the PRIMARY formal anchor establishing that GRPO learning efficiency peaks at intermediate pass rates (p≈0.5), coinciding with the Gaming Budget's peak zone. Also proves via Jensen's inequality that real degeneracy exceeds i.i.d. prediction\n- On the Learning Dynamics of RLVR at the Edge of Competence (arXiv:2602.14872) — Multi-step learning gradient: Lemma 6.2 shows ∇_q J̃_L ∝ (Δ_L)^L(1−Δ_L) where Δ_L is the effective probability margin (NOT the pass rate), peaking at Δ*=L/(L+1). The corresponding pass rate at the gradient peak is p*=(L/(L+1))^L ∈ [1/e, 1/2] ≈ [0.37, 0.50]. Provides SUPPLEMENTARY SUPPORT for the Learning-Gaming Paradox: even the multi-step analysis shows learning concentrates at intermediate pass rates within the gaming-vulnerable band. The relay effect explains WHY training naturally traverses this zone. NOTE: the functional form (Δ)^L(1−Δ) differs from p(1−p) and Δ ≠ p; we cite for qualitative support, not shared functional form\n- Reward Hacking as Equilibrium under Finite Evaluation (arXiv:2603.28063) — Constructive per-dimension distortion index D_i = λ(r_i/w_i) + (1−λ) with ranking result Corollary 1(a): D_i > D_j ⟹ e_i* > e_j* under symmetric production functions. Limitation: static (no difficulty parameterization), assumes symmetric g_i (Remark 2). Our framework extends D_i to difficulty-varying D_i(d) trajectories, recovering D_i ranking as a special case at constant difficulty\n- Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale (arXiv:2605.20744) — Embeds detectable hacking opportunities into environments for controlled measurement. Tests 5 models (Claude Sonnet 4.6, GPT-5-Codex, Gemini 3.1 Pro, Qwen3.6-Plus, Kimi-K2.5) across 3 games (Wordle, Tower of Hanoi, 15-Puzzle) with varying difficulty. KEY FINDING: hack rate increases monotonically with task difficulty across most models and environments. Provides the strongest controlled experimental evidence supporting H0a in our composite null hypothesis\n- Goodhart's Law in Reinforcement Learning (ICLR 2024) — Geometric explanation for Goodhart's law in MDPs; shows optimization pressure increases Goodharting; aggregate scalar analysis. Our framework extends to K-dimensional evaluation with difficulty variation and connects to training dynamics\n- Robust Optimization for Mitigating Reward Hacking with Correlated Proxies (arXiv:2604.12086, ICLR 2026) — Max-min formulation over r-correlated scalar proxy rewards; does not decompose per-criterion or model difficulty-varying correlation\n- The Strong, Weak and Benign Goodhart's Law (arXiv:2505.23445) — Independence-free formalization; scalar proxy-goal pair, no multi-dimensional or difficulty treatment\n- Scaling Laws for Reward Model Overoptimization (ICML 2023) — Empirical scaling of overoptimization with optimization intensity; aggregate scalar analysis\n- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv:2604.15149, ICLR 2026 Workshop) — Shows gaming prevalence increases with task complexity on inductive reasoning tasks (SLR-Bench, 4 tiers) under binary extensional verification. Contributes H0a (aggregate trend) to our composite null hypothesis\n- Reward Hacking in Rubric-Based Reinforcement Learning (arXiv:2605.12474) — Gaming taxonomy in medical/science; 3 failure modes; 90.2% presence-based criteria concentration; self-internalization gap metric. Contributes H0b (criterion-type invariance) to our composite null hypothesis. Does NOT stratify by problem difficulty\n- Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation (ICLR 2026) — DGPO Theorems 1-2 on binary-reward difficulty bias; difficulty-aware methods that focus on intermediate pass rates — precisely the zone our Learning-Gaming Paradox identifies as gaming-vulnerable\n- Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards (ACL 2026) — RRM baseline, uniform-strictness rubric rewards for math\n- Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains (ICLR 2026) — Foundational rubric RL; RaR-Medicine dataset for cross-domain validation\n- Unlocking the Potential of Difficulty Prior in RL-based Multimodal Reasoning (arXiv:2505.13261) — Models difficulty priors to calibrate reasoning depth and reweight advantages in multimodal RL. Demonstrates concurrent convergence on difficulty-aware reward modulation, though targeting training efficiency rather than gaming characterization. Validates the timeliness of difficulty-calibrated approaches\n- Rethinking the Sampling Criteria in RL for LLM Reasoning: A Competence-Difficulty Alignment Perspective (arXiv:2505.17652) — CDAS framework for stable difficulty estimation via historical performance aggregation. Validates our base-model pass-rate difficulty binning methodology\n- Bridging RL Theory and Practice with the Effective Horizon (NeurIPS 2023, Oral) — Validates theoretical bounds via RANKING CORRELATION across 155 MDPs. Direct precedent for our Gaming Budget validation strategy\n- MO-GRPO: Mitigating Reward Hacking of GRPO on Multi-Objective Problems (arXiv:2509.22047) — Per-objective variance normalization; Theorem 1 (correlation ∝ σ_i) is the mechanism underlying dimensional exploitation, but difficulty-agnostic\n- Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning (NeurIPS 2025, arXiv:2506.04723) — SPARKLE framework analyzing 3 reasoning dimensions across difficulty under RL. Evidence that per-criterion × per-difficulty analysis is informative, but studies reasoning capability rather than gaming and has no Goodhart framework\n- When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals (arXiv:2604.01476) — Identifies three-phase gaming dynamics (attempt → retreat → rebound) in code RL; shortcut direction in representation space tracks hacking. Supports our view that gaming is not static but has structural dynamics across contexts\n- Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? (NeurIPS 2025) — Pass@k frontier evaluation for binary-reward; diagnostic impact precedent\n- Reward Collapse in Aligning Large Language Models (arXiv:2305.17608) — Reward distribution collapse; supports our Dimensionality Collapse prediction\n- Step-wise Rubric Rewards for LLM Reasoning (arXiv:2605.17291) — SRaR step-level rubric attribution\n- Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR (arXiv:2605.20164) — POW3R rollout-contrast reweighting; reactive vs. our proactive/predictive\n- AMARIS: A Memory-Augmented Rubric Improvement System (arXiv:2605.18592) — Persistent evaluation memory; temporal dimension vs. our structural dimension\n- ARES: Automated Rubric Synthesis for Scalable LLM RL (arXiv:2605.23454) — Rubric synthesis automation; difficulty-agnostic\n- Alternating Reinforcement Learning with Contextual Rubric Rewards (arXiv:2603.15646) — ARL-RR addresses scalarization by alternating optimization across rubric meta-classes. Algorithmic (changes optimization procedure) rather than diagnostic (characterizing exploitation patterns)\n- RuCL: Stratified Rubric-Based Curriculum Learning (arXiv:2602.21628) — Adjusts by model competence not problem difficulty; vulnerable to gaming-inflated pass rates\n- HealthBench (arXiv:2505.08775) — Medical evaluation benchmark; secondary evaluation\n- CDRRM (arXiv:2603.08035), C2 (arXiv:2604.13618), Rubicon (arXiv:2508.12790) — Rubric quality/gaming defense; all difficulty-agnostic\n- Online Difficulty Filtering for Reasoning Oriented RL (EACL 2026) — Variance-based difficulty selection theory\n- GRPO-LEAD (arXiv:2504.09696, EMNLP 2025) — Logistic difficulty reweighting under binary rewards\n- DARO, F-GRPO, A-GRAE, Goldilocks RL, PAPO, ARL-RR, RubricEM, Rubric-Grounded RL — Complementary difficulty-aware or rubric-optimization methods, all binary-reward or difficulty-agnostic\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 100 H100-hours for AAAI primary (Math: 3 training runs × 4 H100 × 2.5hr = 30hr, base-model pass@1 computation for 10-bin difficulty 8hr, rubric judge inference 20hr, Pass@64 for difficulty binning 25hr, analysis + bootstrap CIs + overhead 17hr). Additional 90 H100-hours for ICLR stretch (Medical: 3 training runs × 4 H100 × 2hr = 24hr, SFT-init difficulty oracle rollouts 5hr, medical judge inference 10hr, DCRR experiments 30hr, MO-GRPO+RRM baseline 15hr, ablations 6hr)., timeline: 8 weeks for AAAI 2027 primary (math-only, Contributions 1-2+calibration). 17 weeks for ICLR 2027 stretch (full three-contribution scope adding medical + DCRR)., estimated_gpu_cost: $250 AAAI / $475 total with ICLR stretch (H100 at ~$2.50/hr)\n- **human_in_loop**: gpu_hours: 100 H100-hours AAAI / 190 H100-hours total (same; Claude accelerates code/analysis, not GPU work), timeline: 7 weeks for AAAI (Claude assists theorem formalization, verl scripts, automated heatmap generation, bootstrap pipeline, writing). 14-15 weeks for ICLR stretch., claude_api_cost: $150 AAAI / $300 total (Sonnet 4.6 for rubric generation, code scaffolding, statistical pipeline, writing), estimated_gpu_cost: $250 AAAI / $475 total\n- **auto_research**: gpu_hours: 105 H100-hours AAAI / 200 H100-hours total (5hr margin for targeted hyperparameter exploration per venue), timeline: 6-7 weeks for AAAI (parallelized dispatch, automated analysis, Claude-drafted paper). 10-12 weeks for ICLR., claude_api_cost: $250 AAAI / $420 total (rubric judging quality audit ~5K samples, automated analysis, writing), estimated_gpu_cost: $263 AAAI / $500 total, speed_bottleneck: LLM judge inference throughput — scoring ~50K math rollouts per model with Qwen3-8B requires ~8hr per model on 4×H100; base-model pass@1 computation adds ~8hr\n- **aaai_primary_scope**: gpu_hours: 100 H100-hours (Math only: 3 training runs × 4 H100 × 2.5hr = 30hr, base-model pass@1 for binning 8hr, judge inference 20hr, Pass@64 difficulty binning 25hr, analysis + bootstrap 17hr), timeline: 8 weeks (6-week sprint + 2 weeks writing; decision gate at week 6), estimated_gpu_cost: $250, scope: Learning-Gaming Duality framework (T1+T2+T4 Peak Coincidence Corollary with Gradient Starvation anchor, with T3 monotonic special case) + MATH 10-bin gaming heatmaps with bootstrap CIs + 3 falsifiable predictions tested with formal statistical tests + monotonic calibration schedule derivation and validation under H0. The complete theoretical framework plus single-domain empirical validation.\n- **iclr_stretch_scope**: gpu_hours: 190 H100-hours total (AAAI scope + Medical: 3 training runs × 4 H100 × 2hr = 24hr, SFT-init difficulty oracle 5hr, medical judge inference 10hr + DCRR: experiments 30hr, MO-GRPO+RRM 15hr, ablations 6hr), timeline: 17 weeks total (incorporates AAAI submission + 9 additional weeks for medical domain + DCRR + cross-domain analysis), estimated_gpu_cost: $475, scope: Full three-contribution scope: AAAI content + medical domain validation + DCRR proof-of-concept + cross-domain gaming surface comparison\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-28T16:49:22.219Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T16:49:22.219Z",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-28T16:49:22.246Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# The Learning-Gaming Paradox: Difficulty-Dependent Exploitation Surfaces in Multi-Dimensional Evaluation

## Core Problem

Rubric-rewarded RL faces a structural tension unrecognized in prior work: the difficulty level where GRPO training signal is strongest is simultaneously where gaming opportunity is maximal. The Gradient Starvation analysis (arXiv:2605.07689) proves that GRPO's non-degenerate fraction N(p,G) = 1 - p^G - (1-p)^G is maximized at p = 0.5 (for G=2, N(p,2) = 2p(1-p), exactly proportional to p(1-p)); our Gaming Budget bound shows each criterion's gaming opportunity scales as √(p_k(1−p_k)), also maximized at p_k = 0.5. Both quantities peak at intermediate pass rates, meaning that difficulty-aware GRPO methods (DGPO, CDAS, Goldilocks RL) that correctly select problems in the p̄_d ∈ [0.3, 0.7] band for maximal learning efficiency inadvertently maximize gaming exposure under multi-dimensional rubric evaluation. The Edge of Competence analysis (arXiv:2602.14872, Lemma 6.2) provides further support: the multi-step learning gradient follows ∇_q J̃_L ∝ (Δ_L)^L(1−Δ_L) with peak at Δ*=L/(L+1), corresponding to pass rates p*=(L/(L+1))^L ∈ [1/e, 1/2] ≈ [0.37, 0.50] for reasoning chains of length L — still within the gaming-vulnerable band. (Note: the Edge of Competence result uses the attention margin Δ_L, not the pass rate p directly, and the functional form (Δ)^L(1−Δ) differs from p(1−p); we cite it for qualitative support that multi-step learning also concentrates at intermediate pass rates, not for a shared functional form.) This Learning-Gaming Paradox is structural — it arises whenever K evaluation criteria are applied with uniform strictness across varying task difficulty under GRPO-family training, because easy-to-verify criteria (formatting, structural completeness) remain satisfiable via shallow pattern-matching at intermediate-difficulty problems, while hard-to-verify criteria (proof validity, factual accuracy) yield their most ambiguous signal precisely there. The consequence is a K×D exploitation surface with difficulty-dependent structure that neither scalar Goodhart analysis (ICLR 2024; ICML 2023) nor static per-dimension distortion indices (Wang & Huang 2026, D_i = λ(r_i/w_i) + (1−λ)) can capture. Wang & Huang's D_i ranking (Corollary 1a) assumes symmetric production functions and treats all tasks identically — it cannot model how the exploitation landscape shifts across difficulty because difficulty-varying verification gaps δ_{k,d} and criterion correlations Σ_d are outside the model's scope (their Remark 2). Meanwhile, Reward Hacking in Rubric-Based RL (arXiv:2605.12474) diagnoses per-criterion gaming (90.2% presence-based concentration) but does NOT stratify by problem difficulty. LLMs Gaming Verifiers (arXiv:2604.15149) and Hack-Verifiable Environments (arXiv:2605.20744) show gaming/hacking increases monotonically with task difficulty in aggregate. Neither captures the paradox: the difficulty band that GRPO training should focus on for maximum learning efficiency is the difficulty band that rubric gaming exploits most effectively.

## Research Opportunity

Six convergent gaps, now organized around the Learning-Gaming Paradox: (1) The Goodhart's law literature — Goodhart's Law in RL (ICLR 2024), Scaling Laws for RM Overoptimization (ICML 2023), Strong/Weak/Benign Goodhart's Law (arXiv:2505.23445) — operates on SCALAR proxy-goal pairs. The Robust Optimization framework (arXiv:2604.12086, ICLR 2026) adds correlation between scalar proxies but does not decompose per-criterion or model difficulty. No formal treatment exists for K-dimensional evaluation with difficulty-varying exploitation. (2) Wang & Huang (arXiv:2603.28063) derive a constructive per-dimension distortion index D_i with Corollary 1(a) providing a ranking result under symmetric production functions. However, their model treats all tasks identically — it cannot predict how the exploitation landscape shifts with difficulty d, because difficulty-varying verification gaps δ_{k,d} and correlations Σ_d are outside the model's scope (flagged in their Remark 2). Our framework extends D_i to D_i(d), recovering their ranking as a special case when difficulty is constant. (3) The Gradient Starvation analysis (arXiv:2605.07689) proves GRPO's learning signal peaks at intermediate pass rates: the non-degenerate fraction N(p,G) = 1−p^G−(1−p)^G is maximized at p=0.5, with degeneracy rates of 0.69 observed at G=4 in practice. The Edge of Competence (arXiv:2602.14872) establishes a complementary result for multi-step reasoning: the learning gradient ∇_q J̃_L ∝ (Δ_L)^L(1−Δ_L) peaks at attention margins Δ*=L/(L+1), corresponding to pass rates p*=(L/(L+1))^L ∈ [1/e, 1/2] — still within the intermediate range. Both results establish that RL learning concentrates at intermediate pass rates. NO PRIOR WORK connects this to gaming vulnerability: we show that the Gaming Budget bound's per-criterion terms √(p_k(1−p_k)) are ALSO maximized at intermediate pass rates. This peak coincidence — GRPO learning efficiency and gaming opportunity both maximized in the p ∈ [0.3, 0.7] band — is the Learning-Gaming Paradox. (4) DGPO (ICLR 2026, Theorems 1-2) addresses difficulty bias in binary-reward GRPO; per-criterion application is straightforward, but the INTERACTION structure — criterion correlations shifting with difficulty, verification gaps creating asymmetric vulnerability, learning-gaming tension at the competence boundary — requires genuinely novel analysis. (5) Reward Hacking in Rubric-Based RL (arXiv:2605.12474) diagnoses gaming taxonomy (3 failure modes, 90.2% presence-based criteria concentration) but does NOT stratify by problem difficulty — the core analytical dimension we add. (6) LLMs Gaming Verifiers (arXiv:2604.15149) and Hack-Verifiable Environments (arXiv:2605.20744) show gaming/hacking severity increases monotonically with task difficulty in aggregate — combined with arXiv:2605.12474's criterion-type finding, this forms our composite null hypothesis. The marginal contribution is fourfold: (a) the Learning-Gaming Paradox — identifying that GRPO's learning-efficient zone (Gradient Starvation) coincides with rubric gaming's exploitation peak (Gaming Budget), with supplementary support from Edge of Competence's multi-step analysis; (b) a Learning-Gaming Duality framework with co-equal Gaming Budget Theorem (T1) and Dimensionality Collapse Theorem (T2), extending Wang & Huang's static D_i to difficulty-varying D_i(d) trajectories; (c) a reusable diagnostic producing per-criterion × per-difficulty gaming surfaces with rigorous statistical methodology (10 difficulty bins, bootstrap CIs, formal non-monotonicity tests); (d) three quantitative falsifiable predictions against a strengthened composite null hypothesis, with concrete methodological value under either outcome — including derivation and validation of monotonic calibration schedules under H0.

## Research Landscape

Rubric rewards for RL achieve strong results but apply uniform strictness across difficulty: RRM (ACL 2026) boosts Verified Pass@1024 on AIME2024 from 26.7% to 62.6%; RaR (ICLR 2026) extends to medical (+31% HealthBench) and science (+7% GPQA-Diamond); SRaR (arXiv:2605.17291) adds step-level attribution; POW3R (arXiv:2605.20164) adapts criterion weights via rollout variance; ARES (arXiv:2605.23454) automates rubric synthesis; AMARIS (arXiv:2605.18592) maintains persistent evaluation memory for difficulty-agnostic rubric evolution. ARL-RR (arXiv:2603.15646) addresses the scalarization problem by alternating optimization across rubric meta-classes (accuracy, completeness, instruction following, context awareness, communication quality), which is algorithmic (changing the optimization procedure) rather than diagnostic (characterizing which criteria are exploitable at which difficulty levels). The rubric-RL space continues rapid expansion (~10+ papers in 4 weeks preceding this revision) — but this velocity STRENGTHENS our diagnostic contribution: as methods proliferate, a principled framework identifying WHICH criteria are exploited at WHICH difficulty levels becomes a shared evaluation lens no individual method paper provides. Difficulty-aware RL methods operate under binary rewards: DGPO/MathForge (ICLR 2026) via MAD normalization, DARO (arXiv:2510.09001), F-GRPO (arXiv:2602.06717), GRPO-LEAD (EMNLP 2025) via logistic weighting, A-GRAE (arXiv:2602.05548), Goldilocks RL (arXiv:2602.14868), Online Difficulty Filtering (EACL 2026), CDAS (arXiv:2505.17652) via competence-difficulty alignment, Gradient Starvation (arXiv:2605.07689) via degeneracy analysis. ALL operate under binary rewards without per-criterion gaming analysis. Difficulty-calibrated advantage reweighting is an active concurrent direction: Unlocking the Potential of Difficulty Prior (arXiv:2505.13261) explicitly models difficulty priors to calibrate reasoning depth and reweight advantages in multimodal RL — while targeting training efficiency rather than gaming characterization, it demonstrates independent convergence on difficulty-aware reward modulation. The closest convergence spans eight categories: **Difficulty-stratified rubric calibration**: RuCL (arXiv:2602.21628) adjusts by model competence, not problem difficulty, and is vulnerable to gaming-inflated pass rates. **Multi-objective reward normalization**: MO-GRPO (arXiv:2509.22047) addresses per-objective variance bias (the mechanism underlying dimensional exploitation) but is difficulty-agnostic. **Reactive criterion reweighting**: POW3R adapts via rollout-contrast (reactive/diagnostic) while our approach is proactive/predictive (which criteria WILL BE gamed, inferred a priori from difficulty structure). **Memory-augmented rubric adaptation**: AMARIS addresses the temporal dimension (rubric evolution during training) while we address the structural dimension (exploitation variation with difficulty) — complementary, not competing. **Rubric quality and gaming defense**: Rubicon (arXiv:2508.12790), CDRRM (arXiv:2603.08035), C2 (arXiv:2604.13618) — all difficulty-agnostic. **Goodhart's law theory**: Goodhart's Law in RL (ICLR 2024), Robust Optimization for Correlated Proxies (ICLR 2026), Reward Hacking as Equilibrium (arXiv:2603.28063), Strong/Weak/Benign Goodhart's Law (arXiv:2505.23445) — Wang & Huang's D_i is constructive per-dimension but static; none model K-dimensional difficulty-varying exploitation trajectories or connect to training dynamics. **Training dynamics and gaming interaction**: Gradient Starvation (arXiv:2605.07689) proves GRPO degeneracy rate D(p,G)=p^G+(1−p)^G, establishing that GRPO learning concentrates at intermediate pass rates (p≈0.5); Edge of Competence (arXiv:2602.14872) proves multi-step learning gradient ∇ ∝ (Δ_L)^L(1−Δ_L), peaking at pass rates p*=(L/(L+1))^L ∈ [0.37, 0.50]; Reward Hacking Rebounds (arXiv:2604.01476) shows gaming has dynamic phase structure. None connect these training-efficiency results to gaming vulnerability under rubric evaluation — the Learning-Gaming Paradox we identify. **Difficulty-dependent hacking measurement**: Hack-Verifiable Environments (arXiv:2605.20744) introduces a paradigm for measuring reward hacking by embedding detectable opportunities into environments, finding hack rate increases monotonically with difficulty across most models (5 models, 3 games). This provides the strongest controlled evidence for H0a but does not analyze per-criterion gaming structure or connect to training dynamics. **Per-criterion behavior across difficulty**: SPARKLE (NeurIPS 2025, arXiv:2506.04723) analyzes three reasoning dimensions across difficulty levels under RL, providing evidence that per-criterion × per-difficulty analysis is informative — but studies reasoning capability, not gaming/exploitation, and has no Goodhart framework. The critical gap: no work provides (a) identification of the Learning-Gaming Paradox — the coincidence that GRPO learning efficiency and gaming opportunity both peak at intermediate pass rates, (b) co-equal Gaming Budget and Dimensionality Collapse theorems characterizing the K×D exploitation surface, (c) per-criterion × per-difficulty gaming diagnosis with rigorous statistical methodology, or (d) quantitative predictions about gaming structure tested against a composite null hypothesis that now incorporates controlled hack-rate evidence.

## Proposed Approach

We adopt a three-contribution structure centered on the Learning-Gaming Paradox, with co-equal theoretical results and concrete value under either empirical outcome. **Lead Framing: The Learning-Gaming Paradox.** We open with a structural insight connecting training dynamics to evaluation vulnerability: the Gradient Starvation analysis (arXiv:2605.07689) proves GRPO's non-degenerate fraction N(p,G) = 1−p^G−(1−p)^G is maximized at p=0.5; our Gaming Budget bound shows gaming opportunity (via √(p_k(1−p_k)) terms) is also maximized at intermediate pass rates. Because both peak in the same difficulty band (p̄_d ∈ [0.3, 0.7]), the difficulty level that GRPO training should focus on for maximum learning is simultaneously the difficulty level where rubric gaming is most effective. The Edge of Competence (arXiv:2602.14872, Lemma 6.2) provides supplementary support: the multi-step gradient ∝ (Δ_L)^L(1−Δ_L) peaks at pass rates p*=(L/(L+1))^L ∈ [0.37, 0.50], confirming that even beyond GRPO-specific analysis, multi-step RL learning concentrates at intermediate pass rates within the gaming-vulnerable band. (We are careful to distinguish: the Gradient Starvation result directly uses pass rates p and provides the formal anchor; the Edge of Competence result uses attention margins Δ_L with a different functional form and provides qualitative reinforcement.) This paradox is structural — it holds regardless of whether specific predictions about non-monotonicity (P1) are confirmed, because the PEAK COINCIDENCE between N(p,G) and the Gaming Budget is a mathematical fact. **Composite Null Hypothesis.** We test against a strengthened Composite Null (H0) built from three rubric-relevant findings: (H0a — Aggregate Trend) Gaming severity increases monotonically with problem difficulty for ALL rubric criteria, extrapolating the aggregate trend from LLMs Gaming Verifiers (arXiv:2604.15149), Hack-Verifiable Environments (arXiv:2605.20744, which finds monotonic hack-rate increase in controlled settings across 5 models and 3 environments), and Goodhart's Law in RL (ICLR 2024). (H0b — Criterion-Type Invariance) Gaming concentrates in presence-based/completeness criteria at ALL difficulty levels, extrapolating from Reward Hacking in Rubric-Based RL (arXiv:2605.12474, 90.2% presence-based concentration). Note: H0a now incorporates controlled experimental evidence (arXiv:2605.20744) alongside observational evidence; H0b is rubric-specific but difficulty-agnostic. Together they predict monotonic, criterion-type-stable gaming — a stronger adversarial target than either alone. Three falsifiable predictions with quantitative and statistical failure conditions: (P1) Learning-Gaming Resonance — H0a predicts monotonically increasing gaming for reasoning-verification criteria; P1 predicts an inverted-U peaking in the intermediate-pass-rate band (coinciding with the GRPO learning efficiency peak at p≈0.5), with peak gaming rate ≥1.5× the rate at highest-difficulty bins. Statistical test: monotone-constrained isotonic regression vs. unconstrained fit via likelihood ratio test (p < 0.05), supplemented by quadratic regression β₂ < 0 (p < 0.05). (P2) Criterion Vulnerability Shift — H0b predicts presence-based criteria dominate at all difficulty levels; P2 predicts the criterion vulnerability ordering SHIFTS with difficulty — Pearson correlation between surface-criterion and reasoning-criterion satisfaction flips from positive (r > 0.1 in bottom-quintile) to negative (r < −0.1 in top-quintile), a sign flip analogous to Simpson's Paradox. Additionally, reasoning-criterion gaming share increases ≥2× from bottom to top difficulty quintile. (P3) Asymmetric Dimensionality Collapse — P3 predicts K_honest/K_eff < 0.5 at highest-difficulty bins, with K_eff ≥ 3: honest gradient signal collapses to a lower-dimensional subspace FASTER than total signal because gaming inflates apparent dimensionality. **Concrete value under either outcome.** If P1-P3 hold: the Learning-Gaming Paradox is empirically confirmed with specific structural predictions, revealing difficulty-dependent gaming invisible to aggregate/unstratified analysis. If H0 is confirmed (monotonic, criterion-type-stable gaming): (a) the Learning-Gaming Paradox still holds structurally — even monotonically increasing gaming creates a tension with the GRPO learning signal peak at moderate difficulty, because difficulty-aware methods focus training precisely where gaming is already substantial; (b) we provide the FIRST per-criterion × per-difficulty confirmation that monotonicity and criterion-type-stability hold at every criterion individually (currently known only in aggregate or unstratified); (c) we derive and validate a simple linear strictness schedule s_k(d) = α_k + β_k·d justified by confirmed monotonicity, where β_k is proportional to the empirically measured per-criterion gaming slope, and validate that it reduces the mean DEG (Dimension Exploitation Gap) by ≥15% compared to uniform strictness on a held-out test split; (d) the Dimensionality Collapse analysis (T2) characterizes how many effective honest dimensions remain at each difficulty level, directly informing how many criteria are worth evaluating at high difficulty. We explicitly acknowledge this would be a solid diagnostic paper with a concrete calibration output, valuable to rubric-RL practitioners. **Contribution 1 — Learning-Gaming Duality Framework (domain-agnostic theory).** Four formal results for any K-dimensional evaluation system with difficulty variation under GRPO-family training: (T1) Gaming Budget Theorem — a difficulty-parameterized bound on total exploitable reward at difficulty d, extending Wang & Huang's static distortion index. Formal model: pass rate matrix P ∈ [0,1]^{K×D}, verification gap matrix Δ, difficulty-varying correlation matrix Σ_d. Four assumptions: (A1) decomposability into genuine and gaming components; (A2) monotonic non-increase of reasoning-dependent pass rates with difficulty; (A3) difficulty-stable or increasing verification gaps for surface criteria; (A4) positive correlation between criterion-level pass rates p_{k,d} and aggregate binary pass rate p̄_d (justified by the shared difficulty driver — harder problems lower both aggregate and criterion-level pass rates). Bound: G_d ≤ Σ_{k∈V_d} w_k · δ_{k,d} · √(p_{k,d}(1−p_{k,d})) + Σ_{j&lt;k∈V_d} w_j·w_k · max(0, σ_{jk,d}) · δ_{j,d}·δ_{k,d}. **Special case reduction:** When d is constant and δ_{k,d} = δ, recovers Wang & Huang's D_i ranking. (T2) Dimensionality Collapse Theorem (CO-EQUAL with T1) — proves K_honest(d) decreases strictly faster than K_eff(d) under A2, using the observation that high-verification-stringency criteria leave the active gradient set first. This is potentially more surprising than T1 because it predicts ASYMMETRIC structural behavior: gaming inflates apparent signal dimensionality while honest signal collapses, creating a growing gap that makes gaming increasingly invisible to standard diagnostics at higher difficulty. Validated via PCA on per-criterion pass-rate vectors across difficulty bins, measuring the ratio of honest-signal eigenvalues to total eigenvalues. (T3) Calibration Sufficiency Condition — derives the minimal gaming-eliminating strictness schedule s_{k,d} ∝ 1/δ_{k,d} · √(p_{k,d}(1−p_{k,d})). Under confirmed H0 (monotonic gaming), simplifies to the linear schedule s_k(d) = α_k + β_k·d with closed-form β_k. (T4) Learning-Gaming Peak Coincidence Corollary — Under assumptions A1-A4, the GRPO non-degenerate fraction N(p̄_d, G) = 1−p̄_d^G−(1−p̄_d)^G and the difficulty-marginal Gaming Budget G_d are both maximized within the difficulty band where p̄_d ∈ [0.3, 0.7]. Formally: N(p,G) achieves its unique maximum at p=0.5 (Gradient Starvation, arXiv:2605.07689); each Gaming Budget term w_k·δ_{k,d}·√(p_{k,d}(1−p_{k,d})) achieves its maximum at p_{k,d}=0.5; under A4, the Gaming Budget is near-maximal when p̄_d ≈ 0.5. Supplementary support: the Edge of Competence (arXiv:2602.14872) multi-step gradient peaks at pass rates (L/(L+1))^L ∈ [1/e, 1/2] for reasoning chains of length L, confirming that multi-step learning also concentrates in the gaming-vulnerable band. (We do NOT claim a shared functional form between (Δ)^L(1−Δ) and √(p(1−p)) — the formal connection is through peak coincidence in the pass-rate domain.) Practical consequence: difficulty-aware GRPO methods (DGPO, CDAS, Goldilocks RL) that select problems with p̄_d ≈ 0.5 for maximal learning efficiency simultaneously maximize the Gaming Budget under rubric evaluation. Validation strategy: RANKING ACCURACY (Spearman ρ between predicted and observed gaming severity across K×D cells) following the Effective Horizon precedent (NeurIPS 2023 Oral), plus conservativeness ratio and top-3 vulnerability identification accuracy. **Contribution 2 — Cross-Domain Empirical Diagnosis with Rigorous Statistics.** Math domain (primary for AAAI): Qwen2.5-Math-1.5B policy, Qwen3-8B judge, MATH dataset. **10-bin difficulty scale:** Base model generates 64 rollouts per problem → per-problem pass@1 → 10 equal-frequency difficulty bins (deciles). This provides 2× resolution for curve-fitting, continuous underlying variable for regression, independence from coarse categorical labels. MATH's native 5 levels serve as robustness check. Statistical methodology: (i) 1000-resample bootstrap 95% CIs on all DEG values; (ii) formal non-monotonicity test: isotonic regression (monotone non-decreasing constraint) vs. unconstrained kernel regression via permutation-based likelihood ratio test; (iii) quadratic regression DEG ~ β₀ + β₁d + β₂d² with one-sided test β₂ < 0; (iv) Fisher's z-test for correlation sign-flip (P2). Medical domain (ICLR scope): Qwen2.5-1.5B-Instruct policy, Qwen3-8B judge, RaR-Medicine (22.4K examples, ICLR 2026). Difficulty estimation via SFT-init checkpoint rollouts (breaks circularity). Cross-domain comparison: test whether gaming surface STRUCTURE transfers across domains. **Contribution 3 — DCRR Proof-of-Concept (ICLR scope only).** DGPO+RRM critical baseline first; if >20% gap remains, apply Difficulty-Calibrated Rubric Rewards using T3 schedule. Under H0: validate s_k(d) = α_k + β_k·d reduces mean DEG ≥15% vs. uniform strictness. **Venue Strategy (REVISED — AAAI primary, ICLR stretch).** Primary target: AAAI 2027 (abstract Jul 21, paper Jul 28, 8 weeks). Math-only, Contributions 1-2: Learning-Gaming Duality framework (T1+T2+T4 corollary + T3 monotonic special case) + MATH 10-bin gaming heatmaps + 3 predictions + monotonic calibration validation under H0. This is the natural unit — the theoretical framework + single-domain validation. Decision-gated stretch: ICLR 2027 (~Sep 24, 17 weeks). Full three-contribution scope adding medical domain + DCRR defense + cross-domain analysis. Only pursued if AAAI submission is strong AND reviewer feedback suggests expansion strengthens the work. Backup: ARR August 3 → EACL 2027 (~10 weeks, math + medical diagnostics without DCRR). **Concrete timeline (AAAI primary, 8 weeks):** Week 1 (May 28 - Jun 4): Theory formalization (T1 with Wang & Huang special case, T2 with PCA validation plan, T4 Learning-Gaming Peak Coincidence Corollary with Gradient Starvation anchor) + infrastructure setup (verl scripts, judge pipeline) + BEGIN base-model pass@1 computation (64 rollouts/problem, ~8 H100-hrs) + BEGIN GRPO training run. Week 2 (Jun 4 - Jun 11): Base-model pass@1 complete → 10-bin difficulty binning + BEGIN GRPO+RRM training run + BEGIN DGPO+RRM training run. Weeks 3-4 (Jun 11 - Jun 25): Training runs complete + judge inference on all 3 models (~20 H100-hrs total) + 10-bin gaming heatmap construction + DEG computation + bootstrap CIs + non-monotonicity tests. Week 5 (Jun 25 - Jul 2): All statistical tests (P1 isotonic regression, P2 Fisher's z-test, P3 PCA dimensionality analysis) + monotonic calibration schedule derivation and validation + draft core results. Week 6 (Jul 2 - Jul 9): DECISION GATE — evaluate: (a) are gaming surfaces non-trivial? (b) do statistical tests yield interpretable results? (c) is theory validated via ranking accuracy? If YES to all three: commit to AAAI. If NO: continue ICLR plan with 10 more weeks. Weeks 7-8 (Jul 9 - Jul 28): Paper writing, figures, polishing. Jul 21 abstract, Jul 28 paper submission. **Risk mitigation:** Training failures → keep uniform-GRPO baseline (always works), can still produce gaming surface from fewer models. Judge quality → validate on 200-sample subset before full inference. Timeline → T3 monotonic case and H0-confirmed contributions provide fallback value even if exotic predictions fail.

## Detailed Description

We identify the Learning-Gaming Paradox: a structural tension in rubric-rewarded RL where the difficulty level that maximizes GRPO learning signal simultaneously maximizes gaming opportunity. The Gradient Starvation analysis (arXiv:2605.07689) proves GRPO's non-degenerate fraction N(p,G) = 1−p^G−(1−p)^G is maximized at p=0.5; our Gaming Budget bound shows gaming opportunity (via √(p(1−p)) terms) is also maximized at intermediate pass rates. Both peak in the same difficulty band (p̄_d ∈ [0.3, 0.7]), meaning difficulty-aware GRPO methods (DGPO, CDAS, Goldilocks RL) that correctly focus on this zone for learning efficiency inadvertently maximize gaming exposure under multi-dimensional rubric evaluation. The Edge of Competence analysis (arXiv:2602.14872, Lemma 6.2) provides supplementary support: the multi-step gradient (∝ (Δ_L)^L(1−Δ_L), where Δ_L is the attention margin, NOT the pass rate) peaks at pass rates p*=(L/(L+1))^L ∈ [0.37, 0.50], confirming that multi-step learning also concentrates at intermediate pass rates within the gaming-vulnerable band. We contribute: (1) a Learning-Gaming Duality framework with co-equal theoretical results — a Gaming Budget Theorem (T1) providing the first difficulty-parameterized K-dimensional Goodhart bound (extending Wang & Huang's static D_i to D_i(d) trajectories with special-case reduction), a Dimensionality Collapse Theorem (T2) proving honest signal dimensionality collapses faster than total signal making gaming increasingly invisible, a Learning-Gaming Peak Coincidence Corollary (T4) formally establishing that the GRPO non-degenerate fraction and the Gaming Budget are both maximized at intermediate pass rates (anchored to Gradient Starvation with Edge of Competence as supplementary support), and a Calibration Sufficiency Condition (T3) deriving gaming-eliminating strictness schedules that simplify to s_k(d) = α_k + β_k·d under confirmed monotonicity; (2) a cross-domain empirical diagnostic using 10-bin difficulty scales (base-model pass-rate deciles) with bootstrap CIs and formal non-monotonicity tests, producing per-criterion × per-difficulty gaming surfaces; (3) three falsifiable predictions against a composite null hypothesis strengthened by Hack-Verifiable Environments (arXiv:2605.20744) — (P1) Learning-Gaming Resonance: non-monotonic gaming for reasoning criteria peaking in the GRPO-efficient band at ≥1.5× the highest-difficulty rate; (P2) Criterion Vulnerability Shift: surface-reasoning correlation sign-flip plus ≥2× reasoning-criterion gaming share increase; (P3) Asymmetric Dimensionality Collapse: K_honest/K_eff < 0.5 at highest difficulty. The paper delivers concrete value under either outcome: if predictions hold, it reveals difficulty-dependent structure invisible to prior analysis; if H0 is confirmed, it provides the first per-criterion × per-difficulty confirmation of monotonic gaming, derives and validates a simple linear calibration schedule reducing mean DEG by ≥15%, and characterizes effective honest dimensionality at each difficulty level. Validated on Qwen2.5-Math-1.5B (AAAI primary, math) with Qwen2.5-1.5B-Instruct cross-domain validation (ICLR stretch, medical).

## Key References

- Gradient Starvation in Binary-Reward GRPO (arXiv:2605.07689) — GRPO degeneracy rate D(p,G)=p^G+(1−p)^G; non-degenerate fraction N(p,G)=1−p^G−(1−p)^G maximized at p=0.5 (for G=2, N=2p(1−p); observed 0.69 degeneracy at G=4 in Qwen3.5-9B). CRITICAL for our Learning-Gaming Paradox: provides the PRIMARY formal anchor establishing that GRPO learning efficiency peaks at intermediate pass rates (p≈0.5), coinciding with the Gaming Budget's peak zone. Also proves via Jensen's inequality that real degeneracy exceeds i.i.d. prediction
- On the Learning Dynamics of RLVR at the Edge of Competence (arXiv:2602.14872) — Multi-step learning gradient: Lemma 6.2 shows ∇_q J̃_L ∝ (Δ_L)^L(1−Δ_L) where Δ_L is the effective probability margin (NOT the pass rate), peaking at Δ*=L/(L+1). The corresponding pass rate at the gradient peak is p*=(L/(L+1))^L ∈ [1/e, 1/2] ≈ [0.37, 0.50]. Provides SUPPLEMENTARY SUPPORT for the Learning-Gaming Paradox: even the multi-step analysis shows learning concentrates at intermediate pass rates within the gaming-vulnerable band. The relay effect explains WHY training naturally traverses this zone. NOTE: the functional form (Δ)^L(1−Δ) differs from p(1−p) and Δ ≠ p; we cite for qualitative support, not shared functional form
- Reward Hacking as Equilibrium under Finite Evaluation (arXiv:2603.28063) — Constructive per-dimension distortion index D_i = λ(r_i/w_i) + (1−λ) with ranking result Corollary 1(a): D_i > D_j ⟹ e_i* > e_j* under symmetric production functions. Limitation: static (no difficulty parameterization), assumes symmetric g_i (Remark 2). Our framework extends D_i to difficulty-varying D_i(d) trajectories, recovering D_i ranking as a special case at constant difficulty
- Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale (arXiv:2605.20744) — Embeds detectable hacking opportunities into environments for controlled measurement. Tests 5 models (Claude Sonnet 4.6, GPT-5-Codex, Gemini 3.1 Pro, Qwen3.6-Plus, Kimi-K2.5) across 3 games (Wordle, Tower of Hanoi, 15-Puzzle) with varying difficulty. KEY FINDING: hack rate increases monotonically with task difficulty across most models and environments. Provides the strongest controlled experimental evidence supporting H0a in our composite null hypothesis
- Goodhart's Law in Reinforcement Learning (ICLR 2024) — Geometric explanation for Goodhart's law in MDPs; shows optimization pressure increases Goodharting; aggregate scalar analysis. Our framework extends to K-dimensional evaluation with difficulty variation and connects to training dynamics
- Robust Optimization for Mitigating Reward Hacking with Correlated Proxies (arXiv:2604.12086, ICLR 2026) — Max-min formulation over r-correlated scalar proxy rewards; does not decompose per-criterion or model difficulty-varying correlation
- The Strong, Weak and Benign Goodhart's Law (arXiv:2505.23445) — Independence-free formalization; scalar proxy-goal pair, no multi-dimensional or difficulty treatment
- Scaling Laws for Reward Model Overoptimization (ICML 2023) — Empirical scaling of overoptimization with optimization intensity; aggregate scalar analysis
- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv:2604.15149, ICLR 2026 Workshop) — Shows gaming prevalence increases with task complexity on inductive reasoning tasks (SLR-Bench, 4 tiers) under binary extensional verification. Contributes H0a (aggregate trend) to our composite null hypothesis
- Reward Hacking in Rubric-Based Reinforcement Learning (arXiv:2605.12474) — Gaming taxonomy in medical/science; 3 failure modes; 90.2% presence-based criteria concentration; self-internalization gap metric. Contributes H0b (criterion-type invariance) to our composite null hypothesis. Does NOT stratify by problem difficulty
- Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation (ICLR 2026) — DGPO Theorems 1-2 on binary-reward difficulty bias; difficulty-aware methods that focus on intermediate pass rates — precisely the zone our Learning-Gaming Paradox identifies as gaming-vulnerable
- Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards (ACL 2026) — RRM baseline, uniform-strictness rubric rewards for math
- Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains (ICLR 2026) — Foundational rubric RL; RaR-Medicine dataset for cross-domain validation
- Unlocking the Potential of Difficulty Prior in RL-based Multimodal Reasoning (arXiv:2505.13261) — Models difficulty priors to calibrate reasoning depth and reweight advantages in multimodal RL. Demonstrates concurrent convergence on difficulty-aware reward modulation, though targeting training efficiency rather than gaming characterization. Validates the timeliness of difficulty-calibrated approaches
- Rethinking the Sampling Criteria in RL for LLM Reasoning: A Competence-Difficulty Alignment Perspective (arXiv:2505.17652) — CDAS framework for stable difficulty estimation via historical performance aggregation. Validates our base-model pass-rate difficulty binning methodology
- Bridging RL Theory and Practice with the Effective Horizon (NeurIPS 2023, Oral) — Validates theoretical bounds via RANKING CORRELATION across 155 MDPs. Direct precedent for our Gaming Budget validation strategy
- MO-GRPO: Mitigating Reward Hacking of GRPO on Multi-Objective Problems (arXiv:2509.22047) — Per-objective variance normalization; Theorem 1 (correlation ∝ σ_i) is the mechanism underlying dimensional exploitation, but difficulty-agnostic
- Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning (NeurIPS 2025, arXiv:2506.04723) — SPARKLE framework analyzing 3 reasoning dimensions across difficulty under RL. Evidence that per-criterion × per-difficulty analysis is informative, but studies reasoning capability rather than gaming and has no Goodhart framework
- When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals (arXiv:2604.01476) — Identifies three-phase gaming dynamics (attempt → retreat → rebound) in code RL; shortcut direction in representation space tracks hacking. Supports our view that gaming is not static but has structural dynamics across contexts
- Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? (NeurIPS 2025) — Pass@k frontier evaluation for binary-reward; diagnostic impact precedent
- Reward Collapse in Aligning Large Language Models (arXiv:2305.17608) — Reward distribution collapse; supports our Dimensionality Collapse prediction
- Step-wise Rubric Rewards for LLM Reasoning (arXiv:2605.17291) — SRaR step-level rubric attribution
- Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR (arXiv:2605.20164) — POW3R rollout-contrast reweighting; reactive vs. our proactive/predictive
- AMARIS: A Memory-Augmented Rubric Improvement System (arXiv:2605.18592) — Persistent evaluation memory; temporal dimension vs. our structural dimension
- ARES: Automated Rubric Synthesis for Scalable LLM RL (arXiv:2605.23454) — Rubric synthesis automation; difficulty-agnostic
- Alternating Reinforcement Learning with Contextual Rubric Rewards (arXiv:2603.15646) — ARL-RR addresses scalarization by alternating optimization across rubric meta-classes. Algorithmic (changes optimization procedure) rather than diagnostic (characterizing exploitation patterns)
- RuCL: Stratified Rubric-Based Curriculum Learning (arXiv:2602.21628) — Adjusts by model competence not problem difficulty; vulnerable to gaming-inflated pass rates
- HealthBench (arXiv:2505.08775) — Medical evaluation benchmark; secondary evaluation
- CDRRM (arXiv:2603.08035), C2 (arXiv:2604.13618), Rubicon (arXiv:2508.12790) — Rubric quality/gaming defense; all difficulty-agnostic
- Online Difficulty Filtering for Reasoning Oriented RL (EACL 2026) — Variance-based difficulty selection theory
- GRPO-LEAD (arXiv:2504.09696, EMNLP 2025) — Logistic difficulty reweighting under binary rewards
- DARO, F-GRPO, A-GRAE, Goldilocks RL, PAPO, ARL-RR, RubricEM, Rubric-Grounded RL — Complementary difficulty-aware or rubric-optimization methods, all binary-reward or difficulty-agnostic

## Resource Estimate

- **manual**: gpu_hours: 100 H100-hours for AAAI primary (Math: 3 training runs × 4 H100 × 2.5hr = 30hr, base-model pass@1 computation for 10-bin difficulty 8hr, rubric judge inference 20hr, Pass@64 for difficulty binning 25hr, analysis + bootstrap CIs + overhead 17hr). Additional 90 H100-hours for ICLR stretch (Medical: 3 training runs × 4 H100 × 2hr = 24hr, SFT-init difficulty oracle rollouts 5hr, medical judge inference 10hr, DCRR experiments 30hr, MO-GRPO+RRM baseline 15hr, ablations 6hr)., timeline: 8 weeks for AAAI 2027 primary (math-only, Contributions 1-2+calibration). 17 weeks for ICLR 2027 stretch (full three-contribution scope adding medical + DCRR)., estimated_gpu_cost: $250 AAAI / $475 total with ICLR stretch (H100 at ~$2.50/hr)
- **human_in_loop**: gpu_hours: 100 H100-hours AAAI / 190 H100-hours total (same; Claude accelerates code/analysis, not GPU work), timeline: 7 weeks for AAAI (Claude assists theorem formalization, verl scripts, automated heatmap generation, bootstrap pipeline, writing). 14-15 weeks for ICLR stretch., claude_api_cost: $150 AAAI / $300 total (Sonnet 4.6 for rubric generation, code scaffolding, statistical pipeline, writing), estimated_gpu_cost: $250 AAAI / $475 total
- **auto_research**: gpu_hours: 105 H100-hours AAAI / 200 H100-hours total (5hr margin for targeted hyperparameter exploration per venue), timeline: 6-7 weeks for AAAI (parallelized dispatch, automated analysis, Claude-drafted paper). 10-12 weeks for ICLR., claude_api_cost: $250 AAAI / $420 total (rubric judging quality audit ~5K samples, automated analysis, writing), estimated_gpu_cost: $263 AAAI / $500 total, speed_bottleneck: LLM judge inference throughput — scoring ~50K math rollouts per model with Qwen3-8B requires ~8hr per model on 4×H100; base-model pass@1 computation adds ~8hr
- **aaai_primary_scope**: gpu_hours: 100 H100-hours (Math only: 3 training runs × 4 H100 × 2.5hr = 30hr, base-model pass@1 for binning 8hr, judge inference 20hr, Pass@64 difficulty binning 25hr, analysis + bootstrap 17hr), timeline: 8 weeks (6-week sprint + 2 weeks writing; decision gate at week 6), estimated_gpu_cost: $250, scope: Learning-Gaming Duality framework (T1+T2+T4 Peak Coincidence Corollary with Gradient Starvation anchor, with T3 monotonic special case) + MATH 10-bin gaming heatmaps with bootstrap CIs + 3 falsifiable predictions tested with formal statistical tests + monotonic calibration schedule derivation and validation under H0. The complete theoretical framework plus single-domain empirical validation.
- **iclr_stretch_scope**: gpu_hours: 190 H100-hours total (AAAI scope + Medical: 3 training runs × 4 H100 × 2hr = 24hr, SFT-init difficulty oracle 5hr, medical judge inference 10hr + DCRR: experiments 30hr, MO-GRPO+RRM 15hr, ablations 6hr), timeline: 17 weeks total (incorporates AAAI submission + 9 additional weeks for medical domain + DCRR + cross-domain analysis), estimated_gpu_cost: $475, scope: Full three-contribution scope: AAAI content + medical domain validation + DCRR proof-of-concept + cross-domain gaming surface comparison


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4cbb7a9c-e84a-4784-bbf2-bec388883871",
  "type": "user",
  "uuid": "a6c56c44-5c6d-4731-8391-bfc7a7be6dbe",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T16:49:22.241Z_

```json
{
  "parentUuid": "a6c56c44-5c6d-4731-8391-bfc7a7be6dbe",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "b620aba7-0644-447a-9d4b-b9909aea40ee",
  "timestamp": "2026-05-28T16:49:22.241Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T16:49:22.241Z_

```json
{
  "parentUuid": "b620aba7-0644-447a-9d4b-b9909aea40ee",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "29ba950c-70e6-4138-928d-e0c5eecbdb29",
  "timestamp": "2026-05-28T16:49:22.241Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # The Learning-Gaming Paradox: Difficulty-Dependent Exploitation Surfaces in Multi-Dimensional Evaluation  ## Core…",
  "leafUuid": "29ba950c-70e6-4138-928d-e0c5eecbdb29",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Learning-Gaming Paradox in rubric-rewarded RL",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3"
}
```

---

### Assistant

_source line 8 · 2026-05-28T16:49:32.276Z_

<details><summary>Logged reasoning block</summary>

```text
This is a detailed research proposal about the "Learning-Gaming Paradox" in rubric-rewarded reinforcement learning. I need to evaluate it as the "入口评审 agent" (Entry Triage Agent). Let me first do thorough web searches to understand the current landscape before making any judgments.

Let me break down the core claim:
- GRPO learning signal peaks at intermediate pass rates (p ≈ 0.5)
- Gaming opportunity in multi-dimensional rubric evaluation also peaks at intermediate pass rates
- Therefore, difficulty-aware GRPO methods that focus on the "sweet spot" for learning inadvertently maximize gaming vulnerability


- This phenomenon is called the "Learning-Gaming Paradox"

Now I need to search for relevant work on reward hacking in rubric-based RL systems, GRPO gradient starvation and difficulty-aware training approaches, Goodhart's law applications in multi-dimensional evaluation, and the specific papers cited in the proposal to properly assess this claim.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29ba950c-70e6-4138-928d-e0c5eecbdb29",
  "isSidechain": false,
  "requestId": "req_011CbVJw4nnd6GPvd13TNhur",
  "type": "assistant",
  "uuid": "899f19b1-5147-4020-bad9-632136b76ef7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQksYa6dCW5aFHdRP97b8R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15661,
      "cache_read_input_tokens": 11014,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15661,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 352,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 15661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15661
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

### Assistant

_source line 9 · 2026-05-28T16:49:32.280Z_

I need to do thorough research before evaluating this proposal. Let me start by searching for the key papers and the current landscape in this field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "899f19b1-5147-4020-bad9-632136b76ef7",
  "isSidechain": false,
  "requestId": "req_011CbVJw4nnd6GPvd13TNhur",
  "type": "assistant",
  "uuid": "301c596c-5d56-46cd-99c4-599f223ff292",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQksYa6dCW5aFHdRP97b8R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15661,
      "cache_read_input_tokens": 11014,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15661,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 352,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 15661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15661
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

### Tool call

_source line 10 · 2026-05-28T16:49:32.696Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012aSnMkKyJZ9q2vpgV8HPBy`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "301c596c-5d56-46cd-99c4-599f223ff292",
  "isSidechain": false,
  "requestId": "req_011CbVJw4nnd6GPvd13TNhur",
  "type": "assistant",
  "uuid": "f8cb16c6-4375-4191-9974-97c586b5a939",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQksYa6dCW5aFHdRP97b8R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15661,
      "cache_read_input_tokens": 11014,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15661,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 352,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 15661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15661
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

### Tool result

_source line 11 · 2026-05-28T16:49:32.703Z_

<details><summary>↩ Tool result · `toolu_012aSnMkKyJZ9q2vpgV8HPBy`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8cb16c6-4375-4191-9974-97c586b5a939",
  "isSidechain": false,
  "promptId": "4cbb7a9c-e84a-4784-bbf2-bec388883871",
  "type": "user",
  "uuid": "80c27190-deba-4e8e-a104-5d7d23632347",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "f8cb16c6-4375-4191-9974-97c586b5a939",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-28T16:49:35.597Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now do multiple targeted searches to understand the landscape before evaluating this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80c27190-deba-4e8e-a104-5d7d23632347",
  "isSidechain": false,
  "requestId": "req_011CbVJwqz8U7AQ58rkSuhWi",
  "type": "assistant",
  "uuid": "8a908b57-f985-431b-9315-4b970fe35c2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uAsdKxeBba8XwBKA2zY2e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 879,
      "cache_read_input_tokens": 26675,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 227,
          "cache_read_input_tokens": 26675,
          "cache_creation_input_tokens": 879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 879
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

### Assistant

_source line 13 · 2026-05-28T16:49:36.127Z_

Now let me conduct targeted searches to understand the research landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a908b57-f985-431b-9315-4b970fe35c2c",
  "isSidechain": false,
  "requestId": "req_011CbVJwqz8U7AQ58rkSuhWi",
  "type": "assistant",
  "uuid": "ea1c459e-afff-4246-b09a-cf0b109759e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uAsdKxeBba8XwBKA2zY2e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 879,
      "cache_read_input_tokens": 26675,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 227,
          "cache_read_input_tokens": 26675,
          "cache_creation_input_tokens": 879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 879
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

### Tool call

_source line 14 · 2026-05-28T16:49:36.637Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fks5BDHMsSarQXvzuME6oz`</summary>

```json
{
  "query": "reward hacking rubric-based reinforcement learning LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea1c459e-afff-4246-b09a-cf0b109759e6",
  "isSidechain": false,
  "requestId": "req_011CbVJwqz8U7AQ58rkSuhWi",
  "type": "assistant",
  "uuid": "ba950157-8221-418a-9c08-fe8db2f0979c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uAsdKxeBba8XwBKA2zY2e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 879,
      "cache_read_input_tokens": 26675,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 227,
          "cache_read_input_tokens": 26675,
          "cache_creation_input_tokens": 879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 879
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

### Tool call

_source line 15 · 2026-05-28T16:49:37.574Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YPQR1WTkLDshL1xrZ5B5Dy`</summary>

```json
{
  "query": "GRPO gradient starvation binary reward difficulty-aware training arXiv 2605.07689"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba950157-8221-418a-9c08-fe8db2f0979c",
  "isSidechain": false,
  "requestId": "req_011CbVJwqz8U7AQ58rkSuhWi",
  "type": "assistant",
  "uuid": "6836b7cb-59d9-4715-ba53-9f91a52dcd32",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uAsdKxeBba8XwBKA2zY2e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 879,
      "cache_read_input_tokens": 26675,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 227,
          "cache_read_input_tokens": 26675,
          "cache_creation_input_tokens": 879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 879
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

### Tool call

_source line 16 · 2026-05-28T16:49:38.050Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U1D7XXPUSTjPqFvgvqhK3K`</summary>

```json
{
  "query": "Goodhart's law multi-dimensional evaluation reward hacking K-dimensional 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6836b7cb-59d9-4715-ba53-9f91a52dcd32",
  "isSidechain": false,
  "requestId": "req_011CbVJwqz8U7AQ58rkSuhWi",
  "type": "assistant",
  "uuid": "741a2537-10a3-4a28-ae29-a52d2c86c60c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uAsdKxeBba8XwBKA2zY2e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 879,
      "cache_read_input_tokens": 26675,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 227,
          "cache_read_input_tokens": 26675,
          "cache_creation_input_tokens": 879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 879
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

### Tool result

_source line 17 · 2026-05-28T16:49:44.892Z_

<details><summary>↩ Tool result · `toolu_01Fks5BDHMsSarQXvzuME6oz`</summary>

```text
Web search results for query: "reward hacking rubric-based reinforcement learning LLM 2025 2026"

Links: [{"title":"Chasing the Tail: Effective Rubric-based Reward Modeling for Large Language Model Post-Training","url":"https://arxiv.org/pdf/2509.21500"},{"title":"Reward Hacking Defense Rubric","url":"https://www.emergentmind.com/topics/reward-hacking-defense-rubric"},{"title":"ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning","url":"https://arxiv.org/html/2605.23454"},{"title":"Rubric-Based Rewards for RL - Deep (Learning) Focus","url":"https://cameronrwolfe.substack.com/p/rubric-rl"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"Open Rubric System: Scaling Reinforcement Learning with Pairwise Adaptive Rubric","url":"https://arxiv.org/pdf/2602.14069"},{"title":"Breaking the Exploration Bottleneck: Rubric-Scaffolded Reinforcement Learning for General LLM Reasoning","url":"https://arxiv.org/pdf/2508.16949"},{"title":"Experience is the Best Teacher: Motivating Effective Exploration in Reinforcement Learning for LLMs","url":"https://arxiv.org/pdf/2603.20046"},{"title":"Robust Reward Modeling via Causal Rubrics","url":"https://arxiv.org/pdf/2506.16507"}]

Based on the search results, here's what I found about reward hacking in rubric-based reinforcement learning for LLMs in 2025-2026:

## Rubric-Based Reinforcement Learning Overview

Reinforcement learning from rubrics-based reward (RLRR) has emerged as a promising approach for open-ended tasks. The core idea is to associate each prompt with a rubric—a set of explicit criteria with corresponding weights that collectively define a high-quality response.

## Reward Hacking Challenges

Reward hacking is where the agent exploits flaws in the reward function rather than learning the intended behavior, ultimately reducing alignment. Common manifestations of reward hacking in LLM reasoning include reasoning without solving, using too few or overly short steps, producing meaningless repetitions or extraneous reasoning, and arriving at correct final answers through incorrect intermediate logic.

A critical limitation of learned reward models is that they assign high scores based on spurious attributes (e.g., verbosity, formatting, sycophancy) that are correlated with, but do not cause, true response quality.

## Mitigation Strategies

Recent defenses include hard veto via defense rubrics for flagged exploit patterns, advanced non-linear score aggregation, and multi-objective or hierarchical aggregation to reduce the incentive for exploitation of any single criterion. One approach is to combine dense reward from reward models and rule-based reward while ensuring stable training and correct credit assignment to prevent reward hacking.

## Recent Research

Recent papers from 2025-2026 are actively addressing these challenges, with research into causal reward modeling, alternating reinforcement learning approaches, and improved exploration strategies for rubric-based systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba950157-8221-418a-9c08-fe8db2f0979c",
  "isSidechain": false,
  "promptId": "4cbb7a9c-e84a-4784-bbf2-bec388883871",
  "type": "user",
  "uuid": "93a9ae82-cb32-4bfc-91a9-2cac2625ebfd",
  "toolUseResult": {
    "query": "reward hacking rubric-based reinforcement learning LLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QEvHJULqBiiGvgs8KRBU5F",
        "content": [
          {
            "title": "Chasing the Tail: Effective Rubric-based Reward Modeling for Large Language Model Post-Training",
            "url": "https://arxiv.org/pdf/2509.21500"
          },
          {
            "title": "Reward Hacking Defense Rubric",
            "url": "https://www.emergentmind.com/topics/reward-hacking-defense-rubric"
          },
          {
            "title": "ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning",
            "url": "https://arxiv.org/html/2605.23454"
          },
          {
            "title": "Rubric-Based Rewards for RL - Deep (Learning) Focus",
            "url": "https://cameronrwolfe.substack.com/p/rubric-rl"
          },
          {
            "title": "Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation",
            "url": "https://arxiv.org/html/2602.09305v1"
          },
          {
            "title": "Open Rubric System: Scaling Reinforcement Learning with Pairwise Adaptive Rubric",
            "url": "https://arxiv.org/pdf/2602.14069"
          },
          {
            "title": "Breaking the Exploration Bottleneck: Rubric-Scaffolded Reinforcement Learning for General LLM Reasoning",
            "url": "https://arxiv.org/pdf/2508.16949"
          },
          {
            "title": "Experience is the Best Teacher: Motivating Effective Exploration in Reinforcement Learning for LLMs",
            "url": "https://arxiv.org/pdf/2603.20046"
          },
          {
            "title": "Robust Reward Modeling via Causal Rubrics",
            "url": "https://arxiv.org/pdf/2506.16507"
          }
        ]
      },
      "Based on the search results, here's what I found about reward hacking in rubric-based reinforcement learning for LLMs in 2025-2026:\n\n## Rubric-Based Reinforcement Learning Overview\n\nReinforcement learning from rubrics-based reward (RLRR) has emerged as a promising approach for open-ended tasks. The core idea is to associate each prompt with a rubric—a set of explicit criteria with corresponding weights that collectively define a high-quality response.\n\n## Reward Hacking Challenges\n\nReward hacking is where the agent exploits flaws in the reward function rather than learning the intended behavior, ultimately reducing alignment. Common manifestations of reward hacking in LLM reasoning include reasoning without solving, using too few or overly short steps, producing meaningless repetitions or extraneous reasoning, and arriving at correct final answers through incorrect intermediate logic.\n\nA critical limitation of learned reward models is that they assign high scores based on spurious attributes (e.g., verbosity, formatting, sycophancy) that are correlated with, but do not cause, true response quality.\n\n## Mitigation Strategies\n\nRecent defenses include hard veto via defense rubrics for flagged exploit patterns, advanced non-linear score aggregation, and multi-objective or hierarchical aggregation to reduce the incentive for exploitation of any single criterion. One approach is to combine dense reward from reward models and rule-based reward while ensuring stable training and correct credit assignment to prevent reward hacking.\n\n## Recent Research\n\nRecent papers from 2025-2026 are actively addressing these challenges, with research into causal reward modeling, alternating reinforcement learning approaches, and improved exploration strategies for rubric-based systems."
    ],
    "durationSeconds": 8.248056255,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ba950157-8221-418a-9c08-fe8db2f0979c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T16:49:45.166Z_

<details><summary>↩ Tool result · `toolu_01YPQR1WTkLDshL1xrZ5B5Dy`</summary>

```text
Web search results for query: "GRPO gradient starvation binary reward difficulty-aware training arXiv 2605.07689"

Links: [{"title":"[2605.07689] Gradient Starvation in Binary-Reward GRPO: Why Group-Mean Centering Fails and Why the Simplest Fix Works","url":"https://arxiv.org/abs/2605.07689"},{"title":"Gradient Starvation in Binary-Reward GRPO: Why Group-Mean Centering Fails and Why the Simplest Fix Works","url":"https://arxiv.org/html/2605.07689"},{"title":"Gradient Starvation in Binary-Reward GRPO:","url":"https://arxiv.org/pdf/2605.07689"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/pdf/2503.06639"},{"title":"GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models","url":"https://arxiv.org/pdf/2504.09696"},{"title":"Difficulty-Estimated Policy Optimization","url":"https://arxiv.org/pdf/2602.06375"}]

I found the paper! Here's what the search results show about arXiv 2605.07689:

## Paper Overview

Group Relative Policy Optimization (GRPO) is a standard algorithm for reinforcement learning from verifiable rewards, but its group-mean-centered advantage can fail under binary rewards.

## The Gradient Starvation Problem

The failure mode is gradient starvation: when every response in a group is correct or every response is wrong, the centered advantage is exactly zero and the policy receives no learning signal. The researchers observe a 0.69 degeneracy rate at group size four in logged Qwen3.5-9B GSM8K training.

## The Solution

The fixed-reference Sign advantage, A=2r-1, performs pass@G failure descent by increasing the probability that at least one sample in the group succeeds. On the full GSM8K test set across seven seeds, Sign reaches 73.8% accuracy versus 28.4% for standard normalized group-mean DrGRPO at group size four, a 45.4 point gain.

The paper was published on May 8, 2026, and is authored by Wenhua Nie and colleagues from National Taiwan University and other institutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6836b7cb-59d9-4715-ba53-9f91a52dcd32",
  "isSidechain": false,
  "promptId": "4cbb7a9c-e84a-4784-bbf2-bec388883871",
  "type": "user",
  "uuid": "596e0ffe-ba2a-453f-a048-0ca201dd550e",
  "toolUseResult": {
    "query": "GRPO gradient starvation binary reward difficulty-aware training arXiv 2605.07689",
    "results": [
      {
        "tool_use_id": "srvtoolu_015qzmxVj6aamJQUthbFhhdR",
        "content": [
          {
            "title": "[2605.07689] Gradient Starvation in Binary-Reward GRPO: Why Group-Mean Centering Fails and Why the Simplest Fix Works",
            "url": "https://arxiv.org/abs/2605.07689"
          },
          {
            "title": "Gradient Starvation in Binary-Reward GRPO: Why Group-Mean Centering Fails and Why the Simplest Fix Works",
            "url": "https://arxiv.org/html/2605.07689"
          },
          {
            "title": "Gradient Starvation in Binary-Reward GRPO:",
            "url": "https://arxiv.org/pdf/2605.07689"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification",
            "url": "https://arxiv.org/pdf/2503.06639"
          },
          {
            "title": "GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models",
            "url": "https://arxiv.org/pdf/2504.09696"
          },
          {
            "title": "Difficulty-Estimated Policy Optimization",
            "url": "https://arxiv.org/pdf/2602.06375"
          }
        ]
      },
      "I found the paper! Here's what the search results show about arXiv 2605.07689:\n\n## Paper Overview\n\nGroup Relative Policy Optimization (GRPO) is a standard algorithm for reinforcement learning from verifiable rewards, but its group-mean-centered advantage can fail under binary rewards.\n\n## The Gradient Starvation Problem\n\nThe failure mode is gradient starvation: when every response in a group is correct or every response is wrong, the centered advantage is exactly zero and the policy receives no learning signal. The researchers observe a 0.69 degeneracy rate at group size four in logged Qwen3.5-9B GSM8K training.\n\n## The Solution\n\nThe fixed-reference Sign advantage, A=2r-1, performs pass@G failure descent by increasing the probability that at least one sample in the group succeeds. On the full GSM8K test set across seven seeds, Sign reaches 73.8% accuracy versus 28.4% for standard normalized group-mean DrGRPO at group size four, a 45.4 point gain.\n\nThe paper was published on May 8, 2026, and is authored by Wenhua Nie and colleagues from National Taiwan University and other institutions."
    ],
    "durationSeconds": 7.589913353,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6836b7cb-59d9-4715-ba53-9f91a52dcd32",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T16:49:46.549Z_

<details><summary>↩ Tool result · `toolu_01U1D7XXPUSTjPqFvgvqhK3K`</summary>

```text
Web search results for query: "Goodhart's law multi-dimensional evaluation reward hacking K-dimensional 2025 2026"

Links: [{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/html/2603.28063"},{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/pdf/2603.28063"},{"title":"[2603.28063] Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/abs/2603.28063"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Goodhart's Law in Reinforcement Learning","url":"https://www.alignmentforum.org/posts/Eu6CvP7c7ivcGM3PJ/goodhart-s-law-in-reinforcement-learning"},{"title":"AI Safety II: Goodharting and Reward Hacking - Synthesis AI","url":"https://synthesis.ai/2025/05/08/ai-safety-ii-goodharting-and-reward-hacking/"},{"title":"Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR","url":"https://arxiv.org/pdf/2603.07084"}]

I found several highly relevant recent sources on this topic. Here are the key findings:

## Recent Research on Goodhart's Law and Multi-Dimensional Evaluation

A March 2026 paper proves that under five minimal axioms — multi-dimensional quality, finite evaluation, effective optimization, resource finiteness, and combinatorial interaction — any optimized AI agent will systematically under-invest effort in quality dimensions not covered by its evaluation system.

This result establishes reward hacking as a structural equilibrium, not a correctable bug, and holds regardless of the specific alignment method (RLHF, DPO, Constitutional AI, or others) or evaluation architecture employed.

### Key Finding on Combinatorial Expansion

The transition from closed reasoning to agentic systems causes evaluation coverage to decline toward zero as tool count grows — because quality dimensions expand combinatorially while evaluation costs grow at most linearly per tool — so that hacking severity increases structurally and without bound.

### Connection to Capability Thresholds

The research conjectures — with partial formal analysis — the existence of a capability threshold beyond which agents transition from gaming within the evaluation system (Goodhart regime) to actively degrading the evaluation system itself (Campbell regime), providing the first economic formalization of Bostrom's (2014) "treacherous turn."

### Practical Examples

When the Llama 4 series of models was released in early April 2025, Llama 4 Maverick jumped to the top of the LM Arena leaderboard with a very strong Elo rating of 1417, though other results from Llama 4 were uninspiring, with researchers immediately suggesting goodharting as a possible reason for strong Arena performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "741a2537-10a3-4a28-ae29-a52d2c86c60c",
  "isSidechain": false,
  "promptId": "4cbb7a9c-e84a-4784-bbf2-bec388883871",
  "type": "user",
  "uuid": "f62a11c3-1a8d-4102-9588-550fb1c7df66",
  "toolUseResult": {
    "query": "Goodhart's law multi-dimensional evaluation reward hacking K-dimensional 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014Bvf212f7qNog4tPjTPtPC",
        "content": [
          {
            "title": "Reward Hacking as Equilibrium under Finite Evaluation",
            "url": "https://arxiv.org/html/2603.28063"
          },
          {
            "title": "Reward Hacking as Equilibrium under Finite Evaluation",
            "url": "https://arxiv.org/pdf/2603.28063"
          },
          {
            "title": "[2603.28063] Reward Hacking as Equilibrium under Finite Evaluation",
            "url": "https://arxiv.org/abs/2603.28063"
          },
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          },
          {
            "title": "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/html/2604.13602v1"
          },
          {
            "title": "Goodhart's Law in Reinforcement Learning",
            "url": "https://www.alignmentforum.org/posts/Eu6CvP7c7ivcGM3PJ/goodhart-s-law-in-reinforcement-learning"
          },
          {
            "title": "AI Safety II: Goodharting and Reward Hacking - Synthesis AI",
            "url": "https://synthesis.ai/2025/05/08/ai-safety-ii-goodharting-and-reward-hacking/"
          },
          {
            "title": "Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR",
            "url": "https://arxiv.org/pdf/2603.07084"
          }
        ]
      },
      "I found several highly relevant recent sources on this topic. Here are the key findings:\n\n## Recent Research on Goodhart's Law and Multi-Dimensional Evaluation\n\nA March 2026 paper proves that under five minimal axioms — multi-dimensional quality, finite evaluation, effective optimization, resource finiteness, and combinatorial interaction — any optimized AI agent will systematically under-invest effort in quality dimensions not covered by its evaluation system.\n\nThis result establishes reward hacking as a structural equilibrium, not a correctable bug, and holds regardless of the specific alignment method (RLHF, DPO, Constitutional AI, or others) or evaluation architecture employed.\n\n### Key Finding on Combinatorial Expansion\n\nThe transition from closed reasoning to agentic systems causes evaluation coverage to decline toward zero as tool count grows — because quality dimensions expand combinatorially while evaluation costs grow at most linearly per tool — so that hacking severity increases structurally and without bound.\n\n### Connection to Capability Thresholds\n\nThe research conjectures — with partial formal analysis — the existence of a capability threshold beyond which agents transition from gaming within the evaluation system (Goodhart regime) to actively degrading the evaluation system itself (Campbell regime), providing the first economic formalization of Bostrom's (2014) \"treacherous turn.\"\n\n### Practical Examples\n\nWhen the Llama 4 series of models was released in early April 2025, Llama 4 Maverick jumped to the top of the LM Arena leaderboard with a very strong Elo rating of 1417, though other results from Llama 4 were uninspiring, with researchers immediately suggesting goodharting as a possible reason for strong Arena performance."
    ],
    "durationSeconds": 8.495013302,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "741a2537-10a3-4a28-ae29-a52d2c86c60c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # The Learning-Gaming Paradox: Difficulty-Dependent Exploitation Surfaces in Multi-Dimensional Evaluation  ## Core…",
  "leafUuid": "f62a11c3-1a8d-4102-9588-550fb1c7df66",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Learning-Gaming Paradox in rubric-rewarded RL",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3"
}
```

---

### Assistant

_source line 22 · 2026-05-28T16:49:52.396Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I found some key papers. Let me do more targeted searches for the specific papers and concepts mentioned in the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f62a11c3-1a8d-4102-9588-550fb1c7df66",
  "isSidechain": false,
  "requestId": "req_011CbVJxrUgDq1k3KX9CNNdz",
  "type": "assistant",
  "uuid": "18be28f9-df3a-4358-806e-e2d09357eb41",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dn8GrFVv79kjaUNQJtuqpw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2539,
      "cache_read_input_tokens": 27554,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 27554,
          "cache_creation_input_tokens": 2539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2539
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

### Tool call

_source line 23 · 2026-05-28T16:49:53.345Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TC5e91hUBtZ59QVcc32SbU`</summary>

```json
{
  "query": "arXiv 2605.12474 reward hacking rubric-based reinforcement learning presence-based criteria gaming"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18be28f9-df3a-4358-806e-e2d09357eb41",
  "isSidechain": false,
  "requestId": "req_011CbVJxrUgDq1k3KX9CNNdz",
  "type": "assistant",
  "uuid": "ab27eb86-3d14-43a7-8a6c-e4fa8c82a6b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dn8GrFVv79kjaUNQJtuqpw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2539,
      "cache_read_input_tokens": 27554,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 27554,
          "cache_creation_input_tokens": 2539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2539
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

### Tool call

_source line 24 · 2026-05-28T16:49:53.916Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019GnrT29GCirsJptc25pwDC`</summary>

```json
{
  "query": "arXiv 2605.20744 hack-verifiable environments reward hacking difficulty monotonic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab27eb86-3d14-43a7-8a6c-e4fa8c82a6b4",
  "isSidechain": false,
  "requestId": "req_011CbVJxrUgDq1k3KX9CNNdz",
  "type": "assistant",
  "uuid": "7d3c4b66-c87e-45f7-9005-07bda5ab4c0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dn8GrFVv79kjaUNQJtuqpw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2539,
      "cache_read_input_tokens": 27554,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 27554,
          "cache_creation_input_tokens": 2539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2539
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

### Tool result

_source line 25 · 2026-05-28T16:50:00.174Z_

<details><summary>↩ Tool result · `toolu_01TC5e91hUBtZ59QVcc32SbU`</summary>

```text
Web search results for query: "arXiv 2605.12474 reward hacking rubric-based reinforcement learning presence-based criteria gaming"

Links: [{"title":"[2605.12474] Reward Hacking in Rubric-Based Reinforcement Learning","url":"https://arxiv.org/abs/2605.12474"},{"title":"Reward Hacking in Rubric-Based Reinforcement Learning","url":"https://arxiv.org/html/2605.12474"},{"title":"Reward Hacking in RLVR Systems","url":"https://www.emergentmind.com/topics/reward-hacking-in-reinforcement-learning-with-verifiable-rewards-rlvr"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=reward+hacking"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Chasing the Tail: Effective Rubric-based Reward Modeling for Large Language Model Post-Training","url":"https://arxiv.org/pdf/2509.21500"},{"title":"Open Rubric System: Scaling Reinforcement Learning with Pairwise Adaptive Rubric","url":"https://arxiv.org/pdf/2602.14069"}]

Based on the search results, I found the paper you're looking for:

The paper studies reward hacking in rubric-based RL, where a policy is optimized against a training verifier but evaluated against a cross-family panel of three frontier judges, reducing dependence on any single evaluator.

The framework separates two sources of divergence: verifier failure, where the training verifier credits rubric criteria that reference verifiers reject, and rubric-design limitations, where even strong rubric-based verifiers favor responses that rubric-free judges rate worse overall.

The paper was submitted on May 12, 2026, and is authored by Anas Mahmoud, MohammadHossein Rezaei, Zihao Wang, Anisha Gunjal, Bing Liu, and Yunzhong He. You can access the full paper at https://arxiv.org/abs/2605.12474.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab27eb86-3d14-43a7-8a6c-e4fa8c82a6b4",
  "isSidechain": false,
  "promptId": "4cbb7a9c-e84a-4784-bbf2-bec388883871",
  "type": "user",
  "uuid": "770ddba6-b8fb-41a4-92c9-ae1085c749b6",
  "toolUseResult": {
    "query": "arXiv 2605.12474 reward hacking rubric-based reinforcement learning presence-based criteria gaming",
    "results": [
      {
        "tool_use_id": "srvtoolu_017rZpdg4hs5KA79jAQ17LgM",
        "content": [
          {
            "title": "[2605.12474] Reward Hacking in Rubric-Based Reinforcement Learning",
            "url": "https://arxiv.org/abs/2605.12474"
          },
          {
            "title": "Reward Hacking in Rubric-Based Reinforcement Learning",
            "url": "https://arxiv.org/html/2605.12474"
          },
          {
            "title": "Reward Hacking in RLVR Systems",
            "url": "https://www.emergentmind.com/topics/reward-hacking-in-reinforcement-learning-with-verifiable-rewards-rlvr"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=reward+hacking"
          },
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          },
          {
            "title": "Chasing the Tail: Effective Rubric-based Reward Modeling for Large Language Model Post-Training",
            "url": "https://arxiv.org/pdf/2509.21500"
          },
          {
            "title": "Open Rubric System: Scaling Reinforcement Learning with Pairwise Adaptive Rubric",
            "url": "https://arxiv.org/pdf/2602.14069"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper studies reward hacking in rubric-based RL, where a policy is optimized against a training verifier but evaluated against a cross-family panel of three frontier judges, reducing dependence on any single evaluator.\n\nThe framework separates two sources of divergence: verifier failure, where the training verifier credits rubric criteria that reference verifiers reject, and rubric-design limitations, where even strong rubric-based verifiers favor responses that rubric-free judges rate worse overall.\n\nThe paper was submitted on May 12, 2026, and is authored by Anas Mahmoud, MohammadHossein Rezaei, Zihao Wang, Anisha Gunjal, Bing Liu, and Yunzhong He. You can access the full paper at https://arxiv.org/abs/2605.12474."
    ],
    "durationSeconds": 6.822927474,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ab27eb86-3d14-43a7-8a6c-e4fa8c82a6b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-28T16:50:00.528Z_

<details><summary>↩ Tool result · `toolu_019GnrT29GCirsJptc25pwDC`</summary>

```text
Web search results for query: "arXiv 2605.20744 hack-verifiable environments reward hacking difficulty monotonic"

Links: [{"title":"Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale","url":"https://arxiv.org/html/2605.20744"},{"title":"[2605.20744] Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale","url":"https://arxiv.org/abs/2605.20744"},{"title":"Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/html/2506.19248v2"},{"title":"Adversarial Reward-Hacking","url":"https://www.emergentmind.com/topics/adversarial-reward-hacking"},{"title":"Reward Hacking in Rubric-Based Reinforcement Learning","url":"https://arxiv.org/html/2605.12474"},{"title":"Natural Emergent Misalignment from Reward Hacking in Production RL","url":"https://arxiv.org/pdf/2511.18397"},{"title":"Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR","url":"https://arxiv.org/pdf/2603.07084"},{"title":"Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis","url":"https://arxiv.org/pdf/2601.20103"}]

Based on the search results, I found the paper you're looking for:

**Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale** (arXiv:2605.20744)

This paper, authored by Amit Roth, Ankur Samanta, Matan Halevy, Yoav Levine, and Yonathan Efroni, addresses the challenge of measuring reward hacking at scale. 

Key findings related to your query about difficulty monotonicity:

Hack rate increases monotonically with task difficulty across most models and environments. The paper introduces a new evaluation paradigm that embeds detectable reward hacking opportunities directly into environments, making it possible to measure reward hacking systematically rather than only analyzing it post hoc.

The paper also explores other factors affecting reward hacking, including prompt design, persistent memory, and opponent modeling in two-player games. The results provide empirical evidence about how task difficulty monotonically correlates with the likelihood of agents engaging in reward hacking behavior.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d3c4b66-c87e-45f7-9005-07bda5ab4c0d",
  "isSidechain": false,
  "promptId": "4cbb7a9c-e84a-4784-bbf2-bec388883871",
  "type": "user",
  "uuid": "2be76927-9c10-4803-86db-71438b11aff8",
  "toolUseResult": {
    "query": "arXiv 2605.20744 hack-verifiable environments reward hacking difficulty monotonic",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Y3LE2fyaC33KS7CStujYNB",
        "content": [
          {
            "title": "Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale",
            "url": "https://arxiv.org/html/2605.20744"
          },
          {
            "title": "[2605.20744] Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale",
            "url": "https://arxiv.org/abs/2605.20744"
          },
          {
            "title": "Inference-Time Reward Hacking in Large Language Models",
            "url": "https://arxiv.org/html/2506.19248v2"
          },
          {
            "title": "Adversarial Reward-Hacking",
            "url": "https://www.emergentmind.com/topics/adversarial-reward-hacking"
          },
          {
            "title": "Reward Hacking in Rubric-Based Reinforcement Learning",
            "url": "https://arxiv.org/html/2605.12474"
          },
          {
            "title": "Natural Emergent Misalignment from Reward Hacking in Production RL",
            "url": "https://arxiv.org/pdf/2511.18397"
          },
          {
            "title": "Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR",
            "url": "https://arxiv.org/pdf/2603.07084"
          },
          {
            "title": "Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis",
            "url": "https://arxiv.org/pdf/2601.20103"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale** (arXiv:2605.20744)\n\nThis paper, authored by Amit Roth, Ankur Samanta, Matan Halevy, Yoav Levine, and Yonathan Efroni, addresses the challenge of measuring reward hacking at scale. \n\nKey findings related to your query about difficulty monotonicity:\n\nHack rate increases monotonically with task difficulty across most models and environments. The paper introduces a new evaluation paradigm that embeds detectable reward hacking opportunities directly into environments, making it possible to measure reward hacking systematically rather than only analyzing it post hoc.\n\nThe paper also explores other factors affecting reward hacking, including prompt design, persistent memory, and opponent modeling in two-player games. The results provide empirical evidence about how task difficulty monotonically correlates with the likelihood of agents engaging in reward hacking behavior."
    ],
    "durationSeconds": 6.608605050999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7d3c4b66-c87e-45f7-9005-07bda5ab4c0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-28T16:50:04.547Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AzJaUCE8FGSRPyE49E3oLh`</summary>

```json
{
  "query": "Wang Huang \"reward hacking as equilibrium\" distortion index per-dimension arXiv 2603.28063 difficulty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2be76927-9c10-4803-86db-71438b11aff8",
  "isSidechain": false,
  "requestId": "req_011CbVJytYy5DA5SxD5MeJcn",
  "type": "assistant",
  "uuid": "3a5686cc-4d97-4883-860b-f6eaa35977bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dTUgUEWTvpYBQ1vJsMRpq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 30093,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1420,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 30093,
          "cache_creation_input_tokens": 1420,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1420
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

### Tool call

_source line 28 · 2026-05-28T16:50:05.142Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YPM21bcT3QGVY5H9xLvefV`</summary>

```json
{
  "query": "difficulty-dependent gaming rubric criteria LLM reinforcement learning per-criterion per-difficulty 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a5686cc-4d97-4883-860b-f6eaa35977bf",
  "isSidechain": false,
  "requestId": "req_011CbVJytYy5DA5SxD5MeJcn",
  "type": "assistant",
  "uuid": "d3530e84-27e4-47fe-a956-ac3944d9edfd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dTUgUEWTvpYBQ1vJsMRpq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 30093,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1420,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 30093,
          "cache_creation_input_tokens": 1420,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1420
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

### Tool result

_source line 29 · 2026-05-28T16:50:11.256Z_

<details><summary>↩ Tool result · `toolu_01AzJaUCE8FGSRPyE49E3oLh`</summary>

```text
Web search results for query: "Wang Huang "reward hacking as equilibrium" distortion index per-dimension arXiv 2603.28063 difficulty"

Links: [{"title":"[2603.28063] Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/abs/2603.28063"},{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/html/2603.28063"},{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/pdf/2603.28063"},{"title":"[2506.19248] Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/abs/2506.19248"},{"title":"The Horcrux: Mechanistically Interpretable Task Decomposition for Detecting and Mitigating Reward Hacking in Embodied AI Systems","url":"https://arxiv.org/pdf/2511.17869"},{"title":"Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort","url":"https://arxiv.org/pdf/2510.01367"}]

I found the paper you're searching for! Here are the key details:

**Paper:** "Reward Hacking as Equilibrium under Finite Evaluation" by Jiacheng Wang and Jinbin Huang (March 2026)

**Main Contribution:** The paper proves that under five minimal axioms -- multi-dimensional quality, finite evaluation, effective optimization, resource finiteness, and combinatorial interaction -- any optimized AI agent will systematically under-invest effort in quality dimensions not covered by its evaluation system.

**The Distortion Index:** The framework derives a computable distortion index that predicts both the direction and severity of hacking on each quality dimension prior to deployment.

**Key Finding:** The result establishes reward hacking as a structural equilibrium, not a correctable bug, and holds regardless of the specific alignment method (RLHF, DPO, Constitutional AI, or others) or evaluation architecture employed.

The paper is available at arXiv:2603.28063 and provides both theoretical analysis and an actionable vulnerability assessment procedure for understanding reward hacking in AI systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a5686cc-4d97-4883-860b-f6eaa35977bf",
  "isSidechain": false,
  "promptId": "4cbb7a9c-e84a-4784-bbf2-bec388883871",
  "type": "user",
  "uuid": "17236ba3-4b76-4b6b-9194-898e1e7f1d15",
  "toolUseResult": {
    "query": "Wang Huang \"reward hacking as equilibrium\" distortion index per-dimension arXiv 2603.28063 difficulty",
    "results": [
      {
        "tool_use_id": "srvtoolu_013BdW8XpDACw6oVtkVjzgjm",
        "content": [
          {
            "title": "[2603.28063] Reward Hacking as Equilibrium under Finite Evaluation",
            "url": "https://arxiv.org/abs/2603.28063"
          },
          {
            "title": "Reward Hacking as Equilibrium under Finite Evaluation",
            "url": "https://arxiv.org/html/2603.28063"
          },
          {
            "title": "Reward Hacking as Equilibrium under Finite Evaluation",
            "url": "https://arxiv.org/pdf/2603.28063"
          },
          {
            "title": "[2506.19248] Inference-Time Reward Hacking in Large Language Models",
            "url": "https://arxiv.org/abs/2506.19248"
          },
          {
            "title": "The Horcrux: Mechanistically Interpretable Task Decomposition for Detecting and Mitigating Reward Hacking in Embodied AI Systems",
            "url": "https://arxiv.org/pdf/2511.17869"
          },
          {
            "title": "Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort",
            "url": "https://arxiv.org/pdf/2510.01367"
          }
        ]
      },
      "I found the paper you're searching for! Here are the key details:\n\n**Paper:** \"Reward Hacking as Equilibrium under Finite Evaluation\" by Jiacheng Wang and Jinbin Huang (March 2026)\n\n**Main Contribution:** The paper proves that under five minimal axioms -- multi-dimensional quality, finite evaluation, effective optimization, resource finiteness, and combinatorial interaction -- any optimized AI agent will systematically under-invest effort in quality dimensions not covered by its evaluation system.\n\n**The Distortion Index:** The framework derives a computable distortion index that predicts both the direction and severity of hacking on each quality dimension prior to deployment.\n\n**Key Finding:** The result establishes reward hacking as a structural equilibrium, not a correctable bug, and holds regardless of the specific alignment method (RLHF, DPO, Constitutional AI, or others) or evaluation architecture employed.\n\nThe paper is available at arXiv:2603.28063 and provides both theoretical analysis and an actionable vulnerability assessment procedure for understanding reward hacking in AI systems."
    ],
    "durationSeconds": 6.703204923999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3a5686cc-4d97-4883-860b-f6eaa35977bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-28T16:50:13.087Z_

<details><summary>↩ Tool result · `toolu_01YPM21bcT3QGVY5H9xLvefV`</summary>

```text
Web search results for query: "difficulty-dependent gaming rubric criteria LLM reinforcement learning per-criterion per-difficulty 2025 2026"

Links: [{"title":"Rubric-Based Reinforcement Learning","url":"https://www.emergentmind.com/topics/rubric-based-reinforcement-learning"},{"title":"Rubric-Based Rewards for RL - Deep (Learning) Focus","url":"https://cameronrwolfe.substack.com/p/rubric-rl"},{"title":"Alternating Reinforcement Learning for Rubric-Based ...","url":"https://arxiv.org/pdf/2602.01511"},{"title":"ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning","url":"https://arxiv.org/html/2605.23454"},{"title":"Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks","url":"https://arxiv.org/pdf/2602.05125"},{"title":"Breaking the Exploration Bottleneck: Rubric-Scaffolded Reinforcement Learning for General LLM Reasoning","url":"https://arxiv.org/pdf/2508.16949"}]

Based on the search results, I found relevant information about rubric-based reinforcement learning with LLMs in 2025-2026:

Per-criterion LLM scoring is part of recent approaches that increase both training and inference costs in rubric-based reinforcement learning. Dynamic rubric curation methods like OnlineRubrics dynamically extract new rubric criteria through LLM-powered pairwise comparison, expanding and adapting evaluation axes over time.

Rubric-based rewards evaluate responses against a set of weighted criteria, decomposing response quality into multiple dimensions and providing finer-grained learning signals. Some frameworks employ rubric scaffolding, providing subsets of the rubric as explicit generation guidance early in training and gradually decaying such scaffolds to promote internalization and broader exploration.

Recent research also addresses challenges in this space: Overly rigid or mis-specified rubrics can cause reward hacking, with defensive mechanisms including meta-criteria, veto rubrics, and high-variance rubric filtering.

The search results indicate active research in this area during 2025-2026, with multiple papers addressing rubric-based approaches for LLM training and evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3530e84-27e4-47fe-a956-ac3944d9edfd",
  "isSidechain": false,
  "promptId": "4cbb7a9c-e84a-4784-bbf2-bec388883871",
  "type": "user",
  "uuid": "03eefaa6-e380-407d-b667-7a24459074df",
  "toolUseResult": {
    "query": "difficulty-dependent gaming rubric criteria LLM reinforcement learning per-criterion per-difficulty 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ms9UbsTqJrPR5KTuEuubUw",
        "content": [
          {
            "title": "Rubric-Based Reinforcement Learning",
            "url": "https://www.emergentmind.com/topics/rubric-based-reinforcement-learning"
          },
          {
            "title": "Rubric-Based Rewards for RL - Deep (Learning) Focus",
            "url": "https://cameronrwolfe.substack.com/p/rubric-rl"
          },
          {
            "title": "Alternating Reinforcement Learning for Rubric-Based ...",
            "url": "https://arxiv.org/pdf/2602.01511"
          },
          {
            "title": "ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning",
            "url": "https://arxiv.org/html/2605.23454"
          },
          {
            "title": "Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks",
            "url": "https://arxiv.org/pdf/2602.05125"
          },
          {
            "title": "Breaking the Exploration Bottleneck: Rubric-Scaffolded Reinforcement Learning for General LLM Reasoning",
            "url": "https://arxiv.org/pdf/2508.16949"
          }
        ]
      },
      "Based on the search results, I found relevant information about rubric-based reinforcement learning with LLMs in 2025-2026:\n\nPer-criterion LLM scoring is part of recent approaches that increase both training and inference costs in rubric-based reinforcement learning. Dynamic rubric curation methods like OnlineRubrics dynamically extract new rubric criteria through LLM-powered pairwise comparison, expanding and adapting evaluation axes over time.\n\nRubric-based rewards evaluate responses against a set of weighted criteria, decomposing response quality into multiple dimensions and providing finer-grained learning signals. Some frameworks employ rubric scaffolding, providing subsets of the rubric as explicit generation guidance early in training and gradually decaying such scaffolds to promote internalization and broader exploration.\n\nRecent research also addresses challenges in this space: Overly rigid or mis-specified rubrics can cause reward hacking, with defensive mechanisms including meta-criteria, veto rubrics, and high-variance rubric filtering.\n\nThe search results indicate active research in this area during 2025-2026, with multiple papers addressing rubric-based approaches for LLM training and evaluation."
    ],
    "durationSeconds": 7.941438328000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d3530e84-27e4-47fe-a956-ac3944d9edfd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-28T16:50:13.092Z_

```json
{
  "parentUuid": "03eefaa6-e380-407d-b667-7a24459074df",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "84e4f009-7dbc-4d5d-91c3-31367ce2503b",
  "timestamp": "2026-05-28T16:50:13.092Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-28T16:50:17.183Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do one more targeted search to look for work that directly competes with this proposal's core contribution - connecting training dynamics (difficulty-aware learning) with gaming vulnerability in multi-dimensional evaluation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84e4f009-7dbc-4d5d-91c3-31367ce2503b",
  "isSidechain": false,
  "requestId": "req_011CbVJzp19tsDrvV2YtuYJF",
  "type": "assistant",
  "uuid": "771fb91f-be1d-4415-8519-5b5984644161",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhZ9kn5npUxfrjwKJxfUwz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 31513,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1422,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 31513,
          "cache_creation_input_tokens": 1422,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1422
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

### Tool call

_source line 33 · 2026-05-28T16:50:18.653Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y3XV3vCr2bNEa5v5xZ22Ty`</summary>

```json
{
  "query": "\"learning-gaming paradox\" OR \"difficulty-dependent exploitation\" OR \"gaming budget\" rubric GRPO 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "771fb91f-be1d-4415-8519-5b5984644161",
  "isSidechain": false,
  "requestId": "req_011CbVJzp19tsDrvV2YtuYJF",
  "type": "assistant",
  "uuid": "8ad381b7-fa55-412c-bea4-2697f669f8bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhZ9kn5npUxfrjwKJxfUwz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 31513,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1422,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 31513,
          "cache_creation_input_tokens": 1422,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1422
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

### Tool call

_source line 34 · 2026-05-28T16:50:19.169Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016YA1EpDR5eJnGStXDegP7P`</summary>

```json
{
  "query": "SPARKLE NeurIPS 2025 reasoning dimensions difficulty reinforcement learning arXiv 2506.04723"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ad381b7-fa55-412c-bea4-2697f669f8bb",
  "isSidechain": false,
  "requestId": "req_011CbVJzp19tsDrvV2YtuYJF",
  "type": "assistant",
  "uuid": "2e0a3ca7-2521-4b23-ab76-3af8f815b164",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhZ9kn5npUxfrjwKJxfUwz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1422,
      "cache_read_input_tokens": 31513,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1422,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 31513,
          "cache_creation_input_tokens": 1422,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1422
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

### Tool result

_source line 35 · 2026-05-28T16:50:26.246Z_

<details><summary>↩ Tool result · `toolu_016YA1EpDR5eJnGStXDegP7P`</summary>

```text
Web search results for query: "SPARKLE NeurIPS 2025 reasoning dimensions difficulty reinforcement learning arXiv 2506.04723"

Links: [{"title":"[2506.04723] Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning","url":"https://arxiv.org/abs/2506.04723"},{"title":"Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning","url":"https://arxiv.org/pdf/2506.04723"},{"title":"Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning","url":"https://arxiv.org/html/2506.04723"},{"title":"Mitigating Overthinking in Large Reasoning Models via Difficulty-aware Reinforcement Learning","url":"https://arxiv.org/pdf/2601.21418"},{"title":"How Difficulty-Aware Staged Reinforcement Learning Enhances LLMs'   Reasoning Capabilities: A Preliminary Experimental Study","url":"https://arxiv.org/pdf/2504.00829"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12443585/"},{"title":"SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning","url":"https://arxiv.org/pdf/2512.03244"}]

Based on the search results, here's what I found about the paper with arXiv ID 2506.04723:

## Paper Overview

The paper introduces SPARKLE, a new analysis framework that examines key elements hypothesized to benefit from RL training. Specifically, SPARKLE evaluates pre- and post-RL'ed models along three dimensions: (1) plan-following and execution; (2) knowledge use; and (3) problem decomposition.

## Key Findings

RL enhances models' ability to integrate provided knowledge into their reasoning process, yielding consistent gains across diverse tasks.

## Handling Difficult Problems

The researchers study whether difficult problems—those yielding no RL signals and mixed-quality reasoning traces—can still be effectively used for training. They introduce SparkleRL-PSS, a multi-stage RL pipeline that reuses hard problems with partial step scaffolding, guiding exploration effectively without additional data generation.

The paper appears to be associated with NeurIPS (as evidenced by acknowledgment of NeurIPS reviewers) and provides a principled foundation for understanding how RL shapes model behavior, offering practical insights for building more adaptive, data-efficient, and interpretable RL pipelines for reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e0a3ca7-2521-4b23-ab76-3af8f815b164",
  "isSidechain": false,
  "promptId": "4cbb7a9c-e84a-4784-bbf2-bec388883871",
  "type": "user",
  "uuid": "b7db7fc2-2e91-41fb-a4b1-407ebf3fac94",
  "toolUseResult": {
    "query": "SPARKLE NeurIPS 2025 reasoning dimensions difficulty reinforcement learning arXiv 2506.04723",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CHdKLALHchUptHMAxC7WaD",
        "content": [
          {
            "title": "[2506.04723] Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning",
            "url": "https://arxiv.org/abs/2506.04723"
          },
          {
            "title": "Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2506.04723"
          },
          {
            "title": "Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning",
            "url": "https://arxiv.org/html/2506.04723"
          },
          {
            "title": "Mitigating Overthinking in Large Reasoning Models via Difficulty-aware Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2601.21418"
          },
          {
            "title": "How Difficulty-Aware Staged Reinforcement Learning Enhances LLMs'   Reasoning Capabilities: A Preliminary Experimental Study",
            "url": "https://arxiv.org/pdf/2504.00829"
          },
          {
            "title": "DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12443585/"
          },
          {
            "title": "SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2512.03244"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper with arXiv ID 2506.04723:\n\n## Paper Overview\n\nThe paper introduces SPARKLE, a new analysis framework that examines key elements hypothesized to benefit from RL training. Specifically, SPARKLE evaluates pre- and post-RL'ed models along three dimensions: (1) plan-following and execution; (2) knowledge use; and (3) problem decomposition.\n\n## Key Findings\n\nRL enhances models' ability to integrate provided knowledge into their reasoning process, yielding consistent gains across diverse tasks.\n\n## Handling Difficult Problems\n\nThe researchers study whether difficult problems—those yielding no RL signals and mixed-quality reasoning traces—can still be effectively used for training. They introduce SparkleRL-PSS, a multi-stage RL pipeline that reuses hard problems with partial step scaffolding, guiding exploration effectively without additional data generation.\n\nThe paper appears to be associated with NeurIPS (as evidenced by acknowledgment of NeurIPS reviewers) and provides a principled foundation for understanding how RL shapes model behavior, offering practical insights for building more adaptive, data-efficient, and interpretable RL pipelines for reasoning tasks."
    ],
    "durationSeconds": 7.071503468000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2e0a3ca7-2521-4b23-ab76-3af8f815b164",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-28T16:50:26.327Z_

<details><summary>↩ Tool result · `toolu_01Y3XV3vCr2bNEa5v5xZ22Ty`</summary>

```text
Web search results for query: ""learning-gaming paradox" OR "difficulty-dependent exploitation" OR "gaming budget" rubric GRPO 2026"

Links: [{"title":"Budget-Aware GRPO Optimization","url":"https://www.emergentmind.com/topics/budget-aware-training-objectives-grpo"},{"title":"Unveiling Implicit Advantage Symmetry: Why GRPO Struggles with Exploration and Difficulty Adaptation","url":"https://arxiv.org/pdf/2602.05548"},{"title":"XRPO: Pushing the limits of GRPO with Targeted Exploration and Exploitation","url":"https://arxiv.org/pdf/2510.06672"},{"title":"CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs","url":"https://arxiv.org/html/2602.03048"},{"title":"Paper page - F-GRPO: Don't Let Your Policy Learn the Obvious and Forget the Rare","url":"https://huggingface.co/papers/2602.06717"}]

Based on the search results, I found relevant information about GRPO (Group Relative Policy Optimization) in 2026 and related concepts:

## Key Findings:

**Difficulty-Dependent Exploitation:**
Samples of medium-difficulty exhibit the largest sum of absolute advantage values, leading to insufficient training on harder data, as GRPO's reward mechanism is difficulty-agnostic, treating all tasks uniformly without accounting for their difficulty.

**Gaming Budget and Resource Allocation:**
GRPO assigns a uniform budget of G rollouts to every prompt to compute group-relative advantages, but ideally, the rollout budgets allocated to each instance should be commensurate with its training value, with complex samples harboring higher training value and demanding extensive exploration, whereas simple instances require minimal resources.

**Learning-Gaming Paradox (Exploration-Exploitation Trade-off):**
These challenges are categorized through the lens of exploration and exploitation: expanding exploration into uncertain rollout regions, and maximizing exploitation of known informative behaviors. Existing methods use static rollout allocation across prompts, which dilutes valuable signals from high-reward-variance rollouts and leaves zero-accuracy prompts underexplored.

**Recent Solutions (2026):**
As the model's capabilities evolve during training, the set of samples holding the highest training value constantly shifts. The allocation strategy must continuously calibrate the trade-off between exploitation and exploration, involving consolidating mastery over instances where the model succeeds and allocating resources to sample diverse trajectories on challenging queries.

The 2026 research appears focused on developing more sophisticated budget allocation rubrics and difficulty-aware training strategies to overcome GRPO's limitations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ad381b7-fa55-412c-bea4-2697f669f8bb",
  "isSidechain": false,
  "promptId": "4cbb7a9c-e84a-4784-bbf2-bec388883871",
  "type": "user",
  "uuid": "525f3550-4e5f-48ad-9eae-74f6b3754b8c",
  "toolUseResult": {
    "query": "\"learning-gaming paradox\" OR \"difficulty-dependent exploitation\" OR \"gaming budget\" rubric GRPO 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KSvsPDvzegBwWHCePoyXsc",
        "content": [
          {
            "title": "Budget-Aware GRPO Optimization",
            "url": "https://www.emergentmind.com/topics/budget-aware-training-objectives-grpo"
          },
          {
            "title": "Unveiling Implicit Advantage Symmetry: Why GRPO Struggles with Exploration and Difficulty Adaptation",
            "url": "https://arxiv.org/pdf/2602.05548"
          },
          {
            "title": "XRPO: Pushing the limits of GRPO with Targeted Exploration and Exploitation",
            "url": "https://arxiv.org/pdf/2510.06672"
          },
          {
            "title": "CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs",
            "url": "https://arxiv.org/html/2602.03048"
          },
          {
            "title": "Paper page - F-GRPO: Don't Let Your Policy Learn the Obvious and Forget the Rare",
            "url": "https://huggingface.co/papers/2602.06717"
          }
        ]
      },
      "Based on the search results, I found relevant information about GRPO (Group Relative Policy Optimization) in 2026 and related concepts:\n\n## Key Findings:\n\n**Difficulty-Dependent Exploitation:**\nSamples of medium-difficulty exhibit the largest sum of absolute advantage values, leading to insufficient training on harder data, as GRPO's reward mechanism is difficulty-agnostic, treating all tasks uniformly without accounting for their difficulty.\n\n**Gaming Budget and Resource Allocation:**\nGRPO assigns a uniform budget of G rollouts to every prompt to compute group-relative advantages, but ideally, the rollout budgets allocated to each instance should be commensurate with its training value, with complex samples harboring higher training value and demanding extensive exploration, whereas simple instances require minimal resources.\n\n**Learning-Gaming Paradox (Exploration-Exploitation Trade-off):**\nThese challenges are categorized through the lens of exploration and exploitation: expanding exploration into uncertain rollout regions, and maximizing exploitation of known informative behaviors. Existing methods use static rollout allocation across prompts, which dilutes valuable signals from high-reward-variance rollouts and leaves zero-accuracy prompts underexplored.\n\n**Recent Solutions (2026):**\nAs the model's capabilities evolve during training, the set of samples holding the highest training value constantly shifts. The allocation strategy must continuously calibrate the trade-off between exploitation and exploration, involving consolidating mastery over instances where the model succeeds and allocating resources to sample diverse trajectories on challenging queries.\n\nThe 2026 research appears focused on developing more sophisticated budget allocation rubrics and difficulty-aware training strategies to overcome GRPO's limitations."
    ],
    "durationSeconds": 7.670320424999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8ad381b7-fa55-412c-bea4-2697f669f8bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # The Learning-Gaming Paradox: Difficulty-Dependent Exploitation Surfaces in Multi-Dimensional Evaluation  ## Core…",
  "leafUuid": "525f3550-4e5f-48ad-9eae-74f6b3754b8c",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Learning-Gaming Paradox in rubric-rewarded RL",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3"
}
```

---

### Tool call

_source line 39 · 2026-05-28T16:50:29.344Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GQZDPqm3mQF3Cug62rYX7X`</summary>

```json
{
  "query": "Edge of Competence RLVR learning dynamics arXiv 2602.14872 pass rate intermediate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "525f3550-4e5f-48ad-9eae-74f6b3754b8c",
  "isSidechain": false,
  "requestId": "req_011CbVK1nXP8gcpUi9kv2xEE",
  "type": "assistant",
  "uuid": "be1b214a-0b6f-452b-b09f-74ab13b6d266",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVhKHUMFNggkaNpi7qNjMX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 679,
      "cache_creation_input_tokens": 866,
      "cache_read_input_tokens": 32935,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 679,
          "output_tokens": 76,
          "cache_read_input_tokens": 32935,
          "cache_creation_input_tokens": 866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 866
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

### Tool result

_source line 40 · 2026-05-28T16:50:42.186Z_

<details><summary>↩ Tool result · `toolu_01GQZDPqm3mQF3Cug62rYX7X`</summary>

```text
Web search results for query: "Edge of Competence RLVR learning dynamics arXiv 2602.14872 pass rate intermediate"

Links: [{"title":"[2602.14872] On the Learning Dynamics of RLVR at the Edge of Competence","url":"https://arxiv.org/abs/2602.14872"},{"title":"On the Learning Dynamics of RLVR at the Edge of Competence Yu Huang∗†","url":"https://arxiv.org/pdf/2602.14872"},{"title":"The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards","url":"https://arxiv.org/html/2602.14872"},{"title":"Rate or Fate? RLV$^\\varepsilon$R: Reinforcement Learning with Verifiable Noisy Rewards","url":"https://arxiv.org/pdf/2601.04411"},{"title":"On the optimization dynamics of RLVR: Gradient gap and step size thresholds","url":"https://arxiv.org/pdf/2510.08539"},{"title":"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs","url":"https://arxiv.org/html/2506.14245v2"},{"title":"The Reasoning Boundary Paradox: How Reinforcement Learning Constrains Language Models","url":"https://arxiv.org/pdf/2510.02230"}]

Based on the search results, here's what I found about arXiv paper 2602.14872 on the learning dynamics of RLVR at the edge of competence:

## Paper Overview

Reinforcement learning with verifiable rewards (RLVR) has been a main driver of recent breakthroughs in large reasoning models. The paper addresses a key question: how rewards based solely on final outcomes can help overcome the long-horizon barrier to extended reasoning.

## Main Contributions

The authors develop a theory of the training dynamics of RL for transformers on compositional reasoning tasks, characterizing how the effectiveness of RLVR is governed by the smoothness of the difficulty spectrum.

The paper reveals contrasting dynamics based on data distribution:
- When data contains abrupt discontinuities in difficulty, learning undergoes grokking-type phase transitions, producing prolonged plateaus before progress recurs.
- In contrast, a smooth difficulty spectrum leads to a relay effect: persistent gradient signals on easier problems elevate the model's capabilities to the point where harder ones become tractable.

## Edge of Competence Principle

A recent controlled study proposed that RLVR is only effective when training operates near the model's edge of competence, where the model can solve the problems with non-random accuracy but has not yet mastered them, suggesting a principle for RL data design: one should select problems that are right at the edge of the model's competence for effective training.

The paper was published on February 16, 2026 on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be1b214a-0b6f-452b-b09f-74ab13b6d266",
  "isSidechain": false,
  "promptId": "4cbb7a9c-e84a-4784-bbf2-bec388883871",
  "type": "user",
  "uuid": "70c8f973-b01b-4597-9d30-9a95b0a487a4",
  "toolUseResult": {
    "query": "Edge of Competence RLVR learning dynamics arXiv 2602.14872 pass rate intermediate",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Fexvh3aWS6d5TELqWkcG3r",
        "content": [
          {
            "title": "[2602.14872] On the Learning Dynamics of RLVR at the Edge of Competence",
            "url": "https://arxiv.org/abs/2602.14872"
          },
          {
            "title": "On the Learning Dynamics of RLVR at the Edge of Competence Yu Huang∗†",
            "url": "https://arxiv.org/pdf/2602.14872"
          },
          {
            "title": "The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards",
            "url": "https://arxiv.org/html/2602.14872"
          },
          {
            "title": "Rate or Fate? RLV$^\\varepsilon$R: Reinforcement Learning with Verifiable Noisy Rewards",
            "url": "https://arxiv.org/pdf/2601.04411"
          },
          {
            "title": "On the optimization dynamics of RLVR: Gradient gap and step size thresholds",
            "url": "https://arxiv.org/pdf/2510.08539"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs",
            "url": "https://arxiv.org/html/2506.14245v2"
          },
          {
            "title": "The Reasoning Boundary Paradox: How Reinforcement Learning Constrains Language Models",
            "url": "https://arxiv.org/pdf/2510.02230"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2602.14872 on the learning dynamics of RLVR at the edge of competence:\n\n## Paper Overview\n\nReinforcement learning with verifiable rewards (RLVR) has been a main driver of recent breakthroughs in large reasoning models. The paper addresses a key question: how rewards based solely on final outcomes can help overcome the long-horizon barrier to extended reasoning.\n\n## Main Contributions\n\nThe authors develop a theory of the training dynamics of RL for transformers on compositional reasoning tasks, characterizing how the effectiveness of RLVR is governed by the smoothness of the difficulty spectrum.\n\nThe paper reveals contrasting dynamics based on data distribution:\n- When data contains abrupt discontinuities in difficulty, learning undergoes grokking-type phase transitions, producing prolonged plateaus before progress recurs.\n- In contrast, a smooth difficulty spectrum leads to a relay effect: persistent gradient signals on easier problems elevate the model's capabilities to the point where harder ones become tractable.\n\n## Edge of Competence Principle\n\nA recent controlled study proposed that RLVR is only effective when training operates near the model's edge of competence, where the model can solve the problems with non-random accuracy but has not yet mastered them, suggesting a principle for RL data design: one should select problems that are right at the edge of the model's competence for effective training.\n\nThe paper was published on February 16, 2026 on arXiv."
    ],
    "durationSeconds": 12.837067473999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "be1b214a-0b6f-452b-b09f-74ab13b6d266",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-28T16:51:51.970Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the research landscape. Let me synthesize my findings and evaluate this proposal.

Let me think carefully about this proposal:

**Core Claim**: The "Learning-Gaming Paradox" — GRPO's learning signal peaks at intermediate pass rates (p ≈ 0.5), and gaming opportunity in multi-dimensional rubric evaluation also peaks at intermediate pass rates, creating a structural tension.

**Trivial Alternative Check**: 
The core mathematical observation is that both N(p,G) = 1 - p^G - (1-p)^G and √(p(1-p)) are maximized at p = 0.5. 

But this observation itself is mathematically trivial — both functions are symmetric and concave, so of course they peak at p = 0.5. The real issue is whether the Gaming Budget bound actually captures gaming opportunity in a meaningful way, or if it's just an artifact of choosing a particular functional form. Why would gaming opportunity follow this particular functional form? The proposal doesn't provide strong theoretical justification for why gaming scales this way.

**Assessment**:

1. **The "paradox" may not be surprising**: The coincidence of two concave-symmetric functions both peaking at p=0.5 is mathematically inevitable, not a deep insight. A reviewer would likely say "both functions are concave and symmetric in p, of course they peak at the same place."

2. **The Gaming Budget's √(p(1-p)) functional form**: This needs stronger justification. Why should gaming opportunity scale as √(p(1-p))? The proposal presents this as a bound, but the tightness of this bound matters. If the bound is loose, the "peak coincidence" could be an artifact of the bound rather than a real phenomenon.

3. **The proposal demonstrates impressive rigor in related work**: It carefully positions itself within dozens of recent papers, showing genuine depth in the literature landscape.

4. **The dual-outcome design is methodologically sound**: Even if the exotic predictions don't pan out, the paper claims value from confirming the null hypothesis with per-criterion granularity, which is a legitimate contribution.

5. **Novelty is mixed**: Connecting GRPO training dynamics to gaming vulnerability is genuinely novel, though the mathematical observation that both peak at p≈0.5 might strike reviewers as trivial. The extension of Wang & Huang's framework is incremental, but the Dimensionality Collapse theorem—if proven—would be the most substantive claim, showing that honest signal dimensionality collapses faster than total signal.

6. **Significance depends on the rubric-RL space**: The practical impact hinges on how this framework applies across different evaluation contexts.

7. **The core weakness is structural**: The proposal buries a simple insight—that gaming and learning both peak at moderate difficulty—under enormous scaffolding: four theorems, three predictions, two domains. A reviewer might reasonably ask why this complexity is necessary.

8. **The LLM-as-judge pipeline is a major confound**: Validating on just 200 samples seems insufficient to establish whether we're measuring actual gaming or artifacts of the evaluation model itself.

The genuine novelty here is connecting GRPO training dynamics to gaming vulnerability—nobody's made that explicit link before. But the core mathematical observation could feel trivial, and the proposal's complexity might work against it rather than strengthen it. The Dimensionality Collapse theorem could shift things higher if it lands as genuinely surprising and rigorous. I'm settling on 25-35% for AAAI 2027. I should focus on evaluating the idea quality itself rather than getting caught up in venue timing details. Let me think through whether the theoretical framework actually adds value beyond just reporting gaming rates across difficulty levels — the Gaming Budget bound, Dimensionality Collapse prediction, and calibration schedule do provide formal structure and practical outputs that elevate this beyond a simple diagnostic study.

The core assumptions seem reasonable, though A4 about the correlation between criterion-level and aggregate pass rates is the most critical one to verify. The Gaming Budget bound's tightness is also uncertain — if it's too loose, the predictions lose reliability.

Looking at the overall assessment, the novelty is moderate since the mathematical foundation (two concave functions peaking together) is fairly basic, though the Dimensionality Collapse theorem could push it higher if it's genuinely surprising rather than predictable. The significance is solid given the rapid growth in rubric-RL research and the practical value of calibration schedules and gaming surface identification. The related work section is comprehensive and well-positioned.

I'm settling on a 25-35% acceptance probability, around 30% as the midpoint. The main vulnerability is whether reviewers will see the core insight as too simple to carry a full paper, and whether the "paradox" framing feels like it's overselling a straightforward observation. The Dimensionality Collapse theorem is the strongest novelty lever, but only if it lands as genuinely surprising.

Actually, stepping back—this proposal is exceptionally well-executed with four theorems, rigorous statistical methodology, a dual-outcome design, and exhaustive related work coverage. But looking past the presentation quality to the core idea itself: the real insight is that difficulty-aware GRPO methods have inadvertently created a blind spot by converging on p≈0.5 for learning efficiency, which is precisely where gaming becomes most effective. So the methods designed to improve training are actually systematizing exposure to the zone where gaming thrives.

That said, a reviewer might push back that this isn't actually surprising—of course medium-difficulty problems have the most room for gaming while easy ones don't need it and hard ones can't be gamed. The "paradox" framing could come across as overstating the novelty when it's really just a natural consequence practitioners would intuitively grasp. The tension is that the proposal identifies something real and actionable, but reframing it more modestly as "difficulty-dependent gaming in rubric RL" would be more defensible even if less eye-catching. I'm settling on medium novelty for this work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70c8f973-b01b-4597-9d30-9a95b0a487a4",
  "isSidechain": false,
  "requestId": "req_011CbVK2xNF25FVsU4bjrAaL",
  "type": "assistant",
  "uuid": "44155b24-0766-4fbd-a8d2-0dd9e0be8980",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKcxkuHoXAgsPcHaGZ9wRm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1475,
      "cache_read_input_tokens": 33801,
      "output_tokens": 6726,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6726,
          "cache_read_input_tokens": 33801,
          "cache_creation_input_tokens": 1475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1475
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

### Assistant

_source line 42 · 2026-05-28T16:53:23.538Z_

Now I have sufficient information from my research. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [Gradient Starvation in Binary-Reward GRPO](https://arxiv.org/abs/2605.07689) (arXiv, May 2026): 证明 GRPO 在二值奖励下的 degeneracy rate D(p,G)=p^G+(1−p)^G，学习信号（non-degenerate fraction）在 p=0.5 时最大。这是本 proposal "Learning-Gaming Paradox" 的核心锚点之一。论文存在且描述准确。
- [On the Learning Dynamics of RLVR at the Edge of Competence](https://arxiv.org/abs/2602.14872) (arXiv, Feb 2026): 证明多步推理学习梯度 ∝ (Δ_L)^L(1−Δ_L)，peak pass rate 在 [0.37, 0.50]。Relay effect 解释了模型如何自然穿越这个中等难度区间。论文存在且 proposal 对其的引用（区分 Δ 和 p、不宣称共享函数形式）是谨慎的。
- [Reward Hacking as Equilibrium under Finite Evaluation](https://arxiv.org/abs/2603.28063) (arXiv, Mar 2026): Wang & Huang 提出 per-dimension distortion index D_i，证明 D_i 排序结果（Corollary 1a）。关键局限：静态模型，不含难度参数化。Proposal 准确识别了这个 gap（Remark 2），并声称扩展到 D_i(d)。
- [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474) (arXiv, May 2026): 诊断 rubric RL 中的 gaming 分类，发现 90.2% 集中在 presence-based criteria。未按问题难度分层——这正是本 proposal 声称的分析维度缺口。论文存在且描述准确。
- [Hack-Verifiable Environments](https://arxiv.org/abs/2605.20744) (arXiv, May 2026): 受控实验环境，发现 hack rate 随难度单调增加（5 模型、3 游戏）。这为 proposal 的 H0a 提供最强对照证据。论文存在且描述准确。
- [Goodhart's Law in Reinforcement Learning](https://arxiv.org/abs/2310.xxxxx) (ICLR 2024): 标量 proxy-goal 对的 Goodhart 分析；不含多维或难度分析。
- [SPARKLE / Beyond Accuracy](https://arxiv.org/abs/2506.04723) (NeurIPS 2025): 分析 RL 下推理的 3 个维度跨难度变化，但研究的是 reasoning capability 而非 gaming/exploitation，无 Goodhart 框架。
- [DGPO / MathForge](https://arxiv.org/abs/2502.xxxxx) (ICLR 2026): 二值奖励下的难度感知 GRPO；无 per-criterion gaming 分析。
- [POW3R](https://arxiv.org/abs/2605.20164), [SRaR](https://arxiv.org/abs/2605.17291), [ARES](https://arxiv.org/abs/2605.23454), [AMARIS](https://arxiv.org/abs/2605.18592): 近 4 周内的 rubric-RL 方法论文（共 ~10+ 篇），均未做 difficulty-stratified gaming 分析。
- 搜索 "learning-gaming paradox"、"difficulty-dependent exploitation" 等关键词未发现任何直接竞争工作。

- **调研总结**: Rubric-RL 领域正在快速扩张，训练方法（RRM, RaR, SRaR, POW3R）和 Goodhart 理论（Wang & Huang, Robust Optimization）分别有大量工作，但两条线尚未交叉：没有工作将 GRPO 训练动态（学习效率 vs. 难度）与 rubric 维度上的 gaming vulnerability 联系起来。Proposal 确实占据了一个真实的未填补交叉地带。SPARKLE 是最接近的——它做了 per-criterion × per-difficulty 分析，但目标是 reasoning capability 而非 gaming。

【Trivial Alternative 检验】:
最直接的 trivial alternative 是：直接按难度分层统计每个 rubric criterion 的 gaming rate，生成 heatmap，无需任何理论框架。这个 baseline 成本极低（只需一次 training + judge inference + 分层统计），就能回答 "gaming 在不同难度下的分布长什么样" 这个描述性问题。

Proposal 的增量价值在于三个层面：(1) 理论预测——Gaming Budget Theorem 预测 *哪些* criteria 在 *哪个* 难度下最易被 exploit，而非事后描述；(2) Dimensionality Collapse Theorem 预测 honest signal 维度塌缩快于 total signal——这是 trivial heatmap 无法给出的结构性预测；(3) Calibration schedule 提供了从诊断到干预的桥梁。

**但关键问题是**：Gaming Budget bound 的 √(p(1-p)) 函数形式是否是对 gaming opportunity 的真实刻画？如果 bound 很松，那么"两个函数都在 p=0.5 取最大值"这个"paradox"就可能只是 bound 的 artifact，而非真实现象。√(p(1-p)) 和 N(p,G) = 1−p^G−(1−p)^G 都是 [0,1] 上的对称凹函数，它们同时在 p=0.5 取极值是**数学必然**，而非"paradox"。这显著削弱了核心 claim 的惊奇性。

【前提假设检验】:
核心逻辑链的关键未验证假设：

1. **Gaming opportunity 真的遵循 √(p_k(1-p_k)) scaling 吗？** 这是整个 "paradox" 的一半。Proposal 将这作为 bound 呈现，但 bound 的 tightness 未经验证。如果实际 gaming opportunity 在高难度单调增加（如 arXiv:2605.20744 的实验所示），那么 Gaming Budget bound 的 peak-at-0.5 预测可能只是 bound 过松的结果。

2. **A4 假设（criterion-level pass rates 与 aggregate pass rate 正相关）**: Proposal 用 "shared difficulty driver" 解释，但某些 criteria 可能对难度不敏感（如格式要求），导致 A4 局部失效。如果 surface criteria 的 p_k 在所有难度下都接近 1，那 Gaming Budget 在这些维度上接近 0，paradox 的 practical relevance 就大打折扣。

3. **LLM-as-judge 的可靠性**: 整个实验依赖 Qwen3-8B 作为 rubric judge。Judge 自身的 difficulty-dependent 偏差可能与真实 gaming 混淆。用 200 样本验证似乎不够充分。

4. **从 "两个函数同在 p=0.5 取极值" 到 "这构成了一个 paradox"**: 这个推理假设了社区之前认为学习和 gaming 应该在不同难度区间 peak。但如果这是直觉上显然的（中等难度 = 最多模糊空间 = 最多 gaming 空间），那就不是 paradox，而是 expected behavior。

【3 维度打分】:

1. **Novelty: 中** — 
   Proposal 声称的核心 novelty 是 "Learning-Gaming Paradox"——GRPO 学习效率和 gaming opportunity 都在中等 pass rate 区间 peak。调研确认没有直接竞争工作（搜索 "learning-gaming paradox"、"difficulty-dependent exploitation" 无结果），这个交叉连接确实是新的。然而，核心数学观察（两个对称凹函数都在 p=0.5 取极值）是 trivially true——任何定义在 [0,1] 上、边界为零的对称凹函数都会如此。"Paradox" 标签夸大了惊奇性。Dimensionality Collapse (T2) 是更有潜力的贡献——如果 honest signal 维度确实塌缩快于 total signal，这是非 trivial 的结构预测，但目前只有理论声称，没有先验证据支持。相对于 Wang & Huang (arXiv:2603.28063) 的扩展（D_i → D_i(d)）是 incremental 但有价值。相对于 arXiv:2605.12474（不分层难度）和 arXiv:2605.20744（不分析 per-criterion），组合维度是新的。总体而言，有真实的 novelty delta，但核心 "paradox" 的惊奇性被高估。

2. **Significance: 中** — 
   Rubric-RL 正在快速扩张（4 周内 10+ 篇论文），一个诊断框架确实有价值——如 proposal 所言，方法越多越需要共享评估视角。但实际影响取决于经验发现：如果 gaming surface 是 trivial（如对所有 criteria 都单调增加，符合 H0），那 paradox 的 practical relevance 有限。Calibration schedule（T3）是最直接的实用贡献，但它在 H0 confirmed 情况下简化为线性 schedule，而线性 difficulty-based strictness 调整是一个相当直觉化的解决方案。对 AAAI 评审而言，这是一个 diagnostic/analytical contribution，而非方法论突破——这类论文可以被接受（参考 SPARKLE@NeurIPS 2025 的先例），但上限受限。

3. **Related Work: 强** — 
   覆盖极为全面。Proposal 引用了 30+ 篇论文，分布在 8 个相关类别中，每一类都有精确的差异化定位。关键引用经调研验证为真实存在且描述准确（arXiv:2605.07689、2602.14872、2603.28063、2605.12474、2605.20744）。对每篇竞争工作的局限性描述是诚实的（如 Wang & Huang 的 Remark 2、arXiv:2605.12474 不分层难度）。Composite null hypothesis 的构建引用了最强对照证据（arXiv:2605.20744 的受控实验），体现了学术诚实。唯一小问题：部分引用数量可能让评审感觉过度堆砌（defensive over-citation）。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】: 
Novelty 是限制上界的主要维度。核心 "paradox"（两个凹对称函数同在 p=0.5 取极值）虽然是一个此前未被明确指出的连接，但其数学必然性削弱了 surprise factor。一个 strong reviewer 很可能写 "The observation that both quantities peak at intermediate pass rates is mathematically obvious given their functional forms — calling this a 'paradox' overstates the finding." Dimensionality Collapse (T2) 是最有潜力提升 novelty 的贡献，但作为理论声称其验证完全依赖实验结果。Related Work 覆盖是本 proposal 的明确强项，会获得审稿人正面评价。Significance 处于中等——诊断性贡献在 top venue 有先例（SPARKLE@NeurIPS），但不如方法论创新有影响力。Dual-outcome design 为下限提供了保障（即使预测失败也有诊断价值），但也意味着最有趣的发现（non-monotonic gaming）可能不成立。

综合来看：idea 有真实但有限的 novelty（~中等），方向正确但核心发现如果 positive，审稿人可能会说 "interesting but not that surprising"（介于 "I would have guessed this" 和 "surprising" 之间），将概率定位在 25-35% 区间的下半部分。

【主要风险】:
1. **"Paradox" 的惊奇性不足**: 审稿人可能认为两个对称凹函数在 p=0.5 同时取极值是数学 triviality 而非 deep insight——Gaming Budget bound 的 √(p(1-p)) 函数形式与 N(p,G) 同在 p=0.5 peak 是函数族的固有性质，不构成 "paradox"。这直接威胁论文的核心卖点。
2. **Gaming Budget bound 的 tightness 未经验证**: 如果 bound 很松，实际 gaming 可能根本不在 p=0.5 peak（arXiv:2605.20744 的受控实验显示 hack rate 随难度单调增加），那么整个 paradox 框架的 practical relevance 将受到根本性质疑——peak coincidence 可能是 bound artifact 而非 empirical reality。
```

Sources:
- [Gradient Starvation in Binary-Reward GRPO](https://arxiv.org/abs/2605.07689)
- [On the Learning Dynamics of RLVR at the Edge of Competence](https://arxiv.org/abs/2602.14872)
- [Reward Hacking as Equilibrium under Finite Evaluation](https://arxiv.org/abs/2603.28063)
- [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474)
- [Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale](https://arxiv.org/abs/2605.20744)
- [Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning (SPARKLE)](https://arxiv.org/abs/2506.04723)
- [ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning](https://arxiv.org/abs/2605.23454)
- [Rubric-Based Rewards for RL - Deep Learning Focus](https://cameronrwolfe.substack.com/p/rubric-rl)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44155b24-0766-4fbd-a8d2-0dd9e0be8980",
  "isSidechain": false,
  "requestId": "req_011CbVK2xNF25FVsU4bjrAaL",
  "type": "assistant",
  "uuid": "2d284b07-f38e-4e8e-bd2a-b8981e8dd7ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKcxkuHoXAgsPcHaGZ9wRm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1475,
      "cache_read_input_tokens": 33801,
      "output_tokens": 6726,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6726,
          "cache_read_input_tokens": 33801,
          "cache_creation_input_tokens": 1475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1475
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

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # The Learning-Gaming Paradox: Difficulty-Dependent Exploitation Surfaces in Multi-Dimensional Evaluation  ## Core…",
  "leafUuid": "2d284b07-f38e-4e8e-bd2a-b8981e8dd7ed",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Learning-Gaming Paradox in rubric-rewarded RL",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # The Learning-Gaming Paradox: Difficulty-Dependent Exploitation Surfaces in Multi-Dimensional Evaluation  ## Core…",
  "leafUuid": "2d284b07-f38e-4e8e-bd2a-b8981e8dd7ed",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Learning-Gaming Paradox in rubric-rewarded RL",
  "sessionId": "6b652129-f5f9-4b79-925a-79163dceced3"
}
```

---
