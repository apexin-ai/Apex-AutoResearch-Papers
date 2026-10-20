# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-28 (UTC).** ## Original idea { "cha

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/30a87c3c-1394-4ddd-886e-4fe0df585294.jsonl`
- **Structured JSON:** [`74a46deae7731a35399a.json`](../../sessions/74/74a46deae7731a35399a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T04:55:01.921Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T04:55:01.921Z",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Original idea\n{\n  \"change_summary\": \"Major narrative restructuring to lead with the strongest novelty — the empirical discovery of domain-dependent step correlation structure (δ_d index) — reframing the paper from 'applying an elementary observation' to 'discovering structure that enables a new training paradigm.' Four specific issues addressed: (1) CPMI venue verified: arXiv 2604.10660 abstract confirms 'Accepted at ACL 2026 Main Conference' — designation retained with verification source noted. (2) ActPRM+RCB composition tension explicitly addressed: added failure mode F7 analyzing the anti-complementarity risk that ActPRM's ensemble uncertainty may correlate with step position (uncertain steps clustering at early positions where MC estimates are uninformative), with Phase 0 diagnostic and hybrid mitigation (constraining ActPRM selection to the RCB-determined informative window k ≥ k*). (3) Contribution ordering restructured throughout all sections: (I) Empirical discovery of domain-dependent reasoning step correlation structure via δ_d (was Contribution V), (II) Theoretical framework with δ_d-calibrated corrections (was I), (III) RCB curriculum (was II), (IV) AMCS-RCB combination (was III), (V) Dual-track evaluation + distillation pipeline (was IV). Narrative arc: 'We discover X → this enables Y (theory) → which produces Z (methods) → with applications W (evaluation + distillation).' (4) Track B ambition substantially raised: primary Track B deliverable is now the complete δ_d characterization across all 7 primary Omni-MATH domains (Algebra, Precalculus, Calculus, Geometry, Discrete Mathematics, Number Theory, Applied Mathematics) AND ≥10 of 33+ sub-domains, with bootstrap confidence intervals for statistical significance and ≥85% δ_d classification robustness target. The ≥2 F1 improvement for generative PRMs is reframed as a secondary Track B outcome, with the δ_d characterization as the independently valuable primary deliverable. Two new supporting references integrated substantively: 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) providing independent geometric evidence for the positional informativeness gradient (~24 AUC point gap between late-step and early-step correctness prediction, 0.87 vs 0.63), and EvalQReason (arXiv 2602.02295, 2026) introducing Consecutive Step Divergence (CSD) measuring local inter-step coherence.\",\n  \"core_problem\": \"Can we discover and exploit domain-dependent structure in mathematical reasoning step correlations to overcome the Monte Carlo cold-start problem in process reward model training? The underlying observation rests on elementary probability theory: in a Markov chain completion, the probability of reaching a target state increases as the number of remaining transitions decreases. Under an independent-step model with per-step correctness probability p, the MC success rate from step k in a K-step solution is approximately p^{K-k} — an exponential gradient that grows sharply toward later steps, especially for hard problems (low p). But five critical empirical and theoretical questions are unanswered: (1) Does mathematical reasoning exhibit systematically different step correlation structures across domains, and can we quantify this variation to determine where the independence idealization holds and where it breaks down? (2) Is the magnitude of the position-dependent success-rate gradient large enough on frontier-hard problems to produce meaningfully informative labels, and can we formalize sufficient conditions for when RCB outperforms uniform MC estimation — with domain-specific corrections? (3) For which mathematical problem types does the gradient hold tightly (near-independence), and where is it attenuated by inter-step dependencies (strong dependency)? (4) How does the informativeness gradient interact with adaptive rollout budget allocation (AMCS-style per-step uncertainty-based sampling)? (5) Can annotation quality improvement (RCB) compose with annotation efficiency improvement (ActPRM-style active step selection), or does the composition create anti-complementarity tension where ActPRM's uncertain steps cluster precisely where MC estimates are uninformative? The severity of the problem is empirically confirmed by Hard2Verify (arXiv 2510.13744): Qwen2.5-Math-PRM-72B drops from 78.3 F1 on ProcessBench to 37.3 on frontier-hard Olympiad problems — a catastrophic 41-point collapse showing that current discriminative PRMs trained with standard MC annotations are fundamentally inadequate at the capability frontier. Independent geometric evidence from 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) confirms the positional informativeness gradient from representation space: late reasoning steps are ~24 AUC points more predictive of correctness than early steps (0.87 vs 0.63 AUC), with correct and incorrect trajectories diverging primarily at late stages — supporting the structural premise that step position carries systematic informativeness signals. Meanwhile, ActPRM (COLM 2025) demonstrates that active learning-based step selection can improve discriminative PRM efficiency — achieving 67.0 F1 on OmniMATH with only 20% annotation budget via ensemble uncertainty — but does not address the quality of MC estimates themselves, leaving early-step uninformativeness unresolved on frontier-hard problems. Rollout-free alternatives like CPMI (arXiv 2604.10660; confirmed accepted at ACL 2026 Main Conference) bypass MC estimation via contrastive mutual information on model probabilities (using Qwen3-8B-Base for labeling, Qwen3-4B-Base for PRM training), but achieve only 25.6 F1 on ProcessBench OmniMATH — far below supervised discriminative PRMs (66.3-71.1 F1) — because model probability calibration degrades on frontier-hard problems. AMCS (arXiv 2509.24351) adaptively allocates rollout budget per-step based on estimation uncertainty (Wilson score interval), improving annotation efficiency, but does not address the fundamental issue that early-step MC estimates on hard problems are uninformative regardless of rollout budget — they converge to near-zero. The independent-step Markov model underlying our theoretical framework is an idealization: mathematical reasoning exhibits domain-dependent correlation structures where approach selection at early steps can determine all subsequent steps' viability. We address this as our primary contribution by introducing a dependency index δ_d that quantifies per-domain independence violation from Phase 0 data, enabling empirically-calibrated corrections to the theoretical predictions. This structural discovery — the first systematic empirical characterization of reasoning step correlation structure across mathematical domains — constitutes the paper's most novel and independently valuable contribution. In near-independence domains (algebraic computation, equation solving, coordinate geometry), the independent-step model is well-calibrated and Theorem 1 provides tight bounds; in strong-dependency domains (insight-dependent proofs, combinatorial constructions, auxiliary-line geometry), Theorem 1 provides conservative bounds rather than tight estimates, and the pattern of deviation is itself an informative finding about reasoning structure that connects to Conditional Reward Modeling (arXiv 2509.26578) and 'What Are Step-Level Reward Models Rewarding?' (AAAI 2025). Critically, Proposition 1 (monotonicity of μ_k) holds regardless of independence — later steps always have higher completion rates — so RCB's curriculum remains beneficial even when the exponential rate of growth is attenuated by dependencies. If the domain-dependent structure is validated and the position-dependent gradient is formalized, the resulting high-quality MC annotations serve a triple purpose: (a) training efficient discriminative PRMs for online RL deployment, (b) providing better fine-tuning data for generative PRMs across architectures, and (c) enabling a novel discriminative-to-generative distillation pipeline where the fast RCB-trained PRM serves as a cheap labeler for training generative PRMs at scale.\",\n  \"opportunity\": \"The MC cold-start problem in PRM training remains a critical bottleneck, now quantified by Hard2Verify: the best discriminative PRM (Qwen2.5-Math-PRM-72B) collapses from 78.3 F1 on ProcessBench to 37.3 on frontier-hard Olympiad problems — a 41-point drop demonstrating catastrophic degradation precisely where strong verification is most needed. OmegaPRM acknowledges it 'requires verifiable gold answers, making it inapplicable when the completer rarely solves' hard problems. Four research directions have emerged, but all have significant limitations. **Direction 1: Generative PRMs** (GenPRM, R-PRM, ThinkPRM, RM-R1) achieve strong results (ThinkPRM-14B: 85.7 F1 on ProcessBench OmniMATH) but incur substantially higher per-step verification costs: Setlur et al. (2025) show GenRM requires 8× compute to match self-consistency, up to 128× for a 3.8% accuracy gain (Figure 1b); ThinkPRM generates 1,000-5,000 tokens per step vs. a discriminative PRM's single scalar output. This cost differential creates a critical deployment gap in online RL training loops (GRPO/PPO), where millions of PRM evaluations are needed per training run. Fast-Slow Thinking RM (2026) explicitly identifies generative RM reasoning costs as 'orders of magnitude higher.' **Direction 2: Rollout-free label generation.** CPMI (arXiv 2604.10660; confirmed accepted at ACL 2026 Main Conference) bypasses MC rollouts via contrastive pointwise mutual information using Qwen3-8B-Base for labeling and Qwen3-4B-Base for PRM training, reducing annotation cost by 84% and token generation by 98%. However, CPMI achieves only 25.6 F1 on ProcessBench OmniMATH — the authors explicitly exclude 'extremely difficult problems' because model probability calibration degrades at frontier difficulty. Together with uPRM (39.8 F1), unsupervised/rollout-free methods consistently underperform supervised MC-based PRMs by 27-41 F1 points on hard problems. **Direction 3: Adaptive MC estimation.** AMCS (arXiv 2509.24351) allocates rollout budget adaptively per-step based on Wilson score interval uncertainty — uncertain steps (success rate μ∈[0.4,0.6]) receive ~20 rollouts vs ~7 for confident steps — improving annotation efficiency. However, AMCS treats all step positions symmetrically and does not exploit the position-dependent success rate gradient: on frontier-hard problems, early steps are not merely 'uncertain' but uninformative (μ≈0), so even maximum-budget AMCS rollouts yield near-zero successes. **Direction 4: Data-efficient annotation via active learning.** ActPRM (arXiv 2504.10559, COLM 2025) uses ensemble uncertainty (aleatoric and epistemic criteria with an ensemble of ~32 classification heads on Qwen2.5-Math-7B-Instruct) to select which steps to annotate, achieving 67.0 F1 on OmniMATH, 71.4 on OlympiadBench, and 75.0 avg F1 on ProcessBench — the current strongest 7B discriminative PRM — using only 20% of UniversalPRM's annotation budget (6% of Qwen2.5-Math-PRM-7B's). However, ActPRM optimizes data selection without addressing MC estimation quality — it still uses standard MC rollouts for the selected steps, inheriting the cold-start problem on frontier-hard problems. The step selection and annotation quality dimensions are orthogonal. **The gap RCB fills:** No existing approach (a) empirically characterizes domain-dependent step correlation structure across mathematical reasoning domains, (b) provides formal conditions characterizing when MC estimation becomes informative as a function of step position with domain-specific dependency corrections, (c) exploits the position-dependent gradient as a training curriculum, (d) combines step-position-aware curriculum with adaptive per-step budget allocation, (e) composes with active learning-based step selection (ActPRM-style) while explicitly addressing the anti-complementarity risk that uncertain steps may cluster where MC estimates are uninformative, or (f) produces a discriminative-to-generative distillation pipeline. RCB addresses all six: the δ_d dependency index provides the first systematic characterization of reasoning step correlation structure (Contribution I), the theoretical framework formalizes informativeness conditions with domain-aware corrections (Contribution II), the curriculum exploits the gradient (Contribution III), AMCS-RCB combines position curriculum with adaptive allocation (Contribution IV), and dual-track evaluation with distillation addresses deployment needs (Contribution V). Independent geometric evidence from 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) confirms the positional informativeness gradient — late steps are ~24 AUC points more predictive of correctness — while EvalQReason's Consecutive Step Divergence (arXiv 2602.02295, 2026) provides a complementary local coherence metric. The resulting annotations serve both discriminative PRM training and a novel discriminative-to-generative distillation pipeline, addressing label quality as a paradigm-wide bottleneck. ComMCS (AAAI 2026) demonstrates a related insight — compounding MC estimates across adjacent steps reduces variance — but its theoretical framework treats all step positions symmetrically and does not address domain-dependent correlation structure.\",\n  \"landscape\": \"**Step correlation structure and reasoning geometry (emerging area — our primary novelty).** No existing work provides systematic empirical quantification of domain-dependent step correlation structure across mathematical reasoning domains. Conditional Reward Modeling (arXiv 2509.26578) formalizes inter-step dependencies via conditional probability chains but does not empirically measure domain-specific correlation patterns. 'What Are Step-Level Reward Models Rewarding?' (AAAI 2025) shows that contextual information across steps is crucial for reward quality, with context-aware SRMs outperforming context-free variants (+7.35% vs +3.64% on GSM8K), empirically confirming the presence of inter-step dependencies but not characterizing their domain-specific structure. ContextPRM (arXiv 2509.24460, 2025) models contextual coherence between CoT steps for multi-domain generalization but does not quantify per-domain dependency strength. 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) provides independent geometric evidence that late reasoning steps are ~24 AUC points more predictive of correctness than early steps (0.87 vs 0.63 AUC), with correct/incorrect trajectories diverging primarily at late stages in representation space — but analyzes trajectories as a whole without decomposing by mathematical domain. EvalQReason (arXiv 2602.02295, 2026) introduces Consecutive Step Divergence (CSD) measuring local coherence between adjacent reasoning steps, achieving F1=0.88 for correctness classification with sequential models — providing a complementary local perspective to our global positional informativeness gradient. Our δ_d index fills the gap: the first systematic domain-level quantification of step independence violation, computed across all 7 primary Omni-MATH domains and ≥10 sub-domains, with bootstrap confidence intervals. **Generative PRMs (dominant recent trend):** GenPRM (AAAI 2026) reframes process reward modeling as a generative task using Relative Progress Estimation, achieving ~80.5 avg F1 on ProcessBench with a 7B model via Maj@8 — surpassing the 72B Qwen2.5-Math-PRM (78.3 avg F1). R-PRM (EMNLP 2025) activates reasoning in the PRM via seed data generation and self-improvement, achieving +11.9 F1 on ProcessBench and +8.5 F1 on PRMBench over baselines. RM-R1 (ICLR 2026) introduces chain-of-rubrics reasoning reward models generating up to 8,192 tokens per evaluation. ThinkPRM (TMLR 2026; arXiv 2504.16828) uses chain-of-thought verification trained on only 1K examples, reaching 85.7 F1 on ProcessBench OmniMATH and 87.3 on OlympiadBench — the current highest reported scores on these hard subsets. All generative PRMs trade training-time data requirements for inference-time compute. **Discriminative PRM SOTA and frontier-hard collapse:** Qwen2.5-Math-PRM-7B achieves 66.3 F1 on OmniMATH and 67.5 on OlympiadBench; Qwen2.5-Math-PRM-72B achieves 71.1 and 74.3 respectively (reported in R-PRM EMNLP 2025 Table 1 and 'Is PRM Necessary?' arXiv 2505.11227 Table 1). Note: these are distinct from the weaker Qwen2.5-Math-7B-PRM800K (44.3 OmniMATH, 50.7 OlympiadBench) — a 22-point gap demonstrating that training data quality is decisive. Critically, Hard2Verify (arXiv 2510.13744) reveals catastrophic degradation at the true frontier: Qwen2.5-Math-PRM-72B drops from 78.3 F1 on ProcessBench to 37.3 on Hard2Verify's 80 IMO/Putnam-level problems (1,860 annotated steps) — a 41-point collapse. All tested PRMs score below 65.82% on step-level tasks. 'State-of-the-art PRMs struggle immensely on Hard2Verify, performing significantly below random guess performance in error identification.' This collapse directly motivates improving MC annotation quality on hard problems. **Data-efficient discriminative PRM training:** ActPRM (arXiv 2504.10559, COLM 2025) applies active learning to PRM training: an ensemble of ~32 classification heads on a shared Qwen2.5-Math-7B-Instruct backbone estimates per-step aleatoric uncertainty (max(μ(P), 1−μ(P)) < δ_pred=0.95) and epistemic uncertainty (σ(P) > δ_std=0.005), retaining only uncertain steps for annotation by QwQ-32B judge. Achieves 67.0 F1 on OmniMATH, 71.4 on OlympiadBench, 75.0 avg F1 on ProcessBench, and 65.5% on PRMBench (matching GPT-4o) — the current strongest 7B discriminative PRM — with only 20% of UniversalPRM's annotation budget (6% of Qwen2.5-Math-PRM-7B's). Also demonstrates downstream utility: filtering 1M+ trajectories to 60% yields further SOTA training data. Key limitation: optimizes which steps to annotate (data selection) but uses standard MC estimation for the annotations themselves, leaving the early-step cold-start problem unaddressed on frontier-hard problems. No Hard2Verify results reported. Critically, ActPRM does not report the positional distribution of selected uncertain steps — whether they cluster at early, middle, or late positions — creating an empirical gap that Phase 0 must characterize. The orthogonality of data selection (ActPRM) and data quality (RCB) suggests their composition could yield multiplicative gains, but anti-complementarity is also possible (see failure mode F7). **Rollout-free label generation:** CPMI (arXiv 2604.10660; confirmed accepted at ACL 2026 Main Conference) uses contrastive pointwise mutual information with Qwen3-8B-Base as the labeling model and Qwen3-4B-Base as the PRM training backbone to generate step-level reward labels without MC rollouts, reducing annotation time by 84%. However, CPMI-trained PRMs achieve only 25.6 F1 on ProcessBench OmniMATH — the authors explicitly exclude extremely difficult problems. **Adaptive MC estimation:** AMCS (arXiv 2509.24351; withdrawn from ICLR 2026) adaptively allocates rollout samples per-step based on Wilson score interval uncertainty, allocating ~20 rollouts to uncertain steps (μ∈[0.4,0.6]) vs ~7 for confident steps. Trains Qwen2.5-Math-7B-PRM-AMCS on MathSearch-200K, achieving 76.2% accuracy on MATH500 with GLM-4-9B. Key limitation: treats all step positions symmetrically — does not analyze or exploit position-dependent success rate gradients. No ProcessBench F1 results reported. **Generative PRM cost analysis:** Setlur et al. (2025) show GenRM-FT requires 8× compute to match self-consistency, up to 128× for a 3.8% accuracy gain (Figure 1b, Llama-3.1-8B; higher multipliers reported for other models in Appendix F). **MC estimation improvements:** ComMCS (AAAI 2026) reduces MC estimator variance via compounding estimates across adjacent step positions (TD(λ)-style) without extra inference, gaining +2.8 best-of-N points. Theorem 4.2 establishes MC estimation as the MVUE given single-step information. SCAN (NeurIPS 2025) addresses MC annotation noise via self-denoising. Math-Shepherd (ACL 2024) and OmegaPRM (arXiv 2024) established MC-based PRM annotation but flag the cold-start problem without solution. **Reward model distillation:** RM-Distiller (arXiv 2601.14032, 2026) systematically distills from generative LLMs to discriminative reward models via refinement, scoring, and generation capabilities. The reverse direction — discriminative PRM to generative PRM distillation — remains unexplored. **Fast PRM motivation:** Fast-Slow Thinking RM (arXiv 2603.20212, 2026) proposes hybrid scalar/generative RM. PRIME (arXiv 2502.01456, 2025) derives implicit process rewards, achieving 2.5× faster training. SPRO (arXiv 2507.01551, 2025) achieves 3.4× higher training efficiency. **Frontier-hard verification benchmarks:** Hard2Verify (arXiv 2510.13744, 2025) provides 80 frontier Olympiad problems with 1,860 human-annotated steps; the best open-source model (DeepSeek-R1) achieves 68.92% step-level accuracy; GPT-5 leads at 86.53%. **Co-evolutionary and curriculum approaches:** RL Tango (NeurIPS 2025) co-evolves generator and generative verifier. SCRL (arXiv 2605.22074, 2026) decomposes hard problems into verifiable subproblems. R³ (ICML 2024) applies reverse curriculum RL for policy training. AURORA (arXiv 2025) uses reverse verification. **Gap:** No existing work (a) empirically characterizes domain-dependent step correlation structure across mathematical reasoning domains with quantitative per-domain indices, (b) provides formal conditions for MC informativeness as a function of step position with domain-specific dependency corrections, (c) proposes a step-position-aware reverse curriculum for PRM training, (d) combines position-aware curriculum with adaptive per-step rollout allocation, (e) produces efficient discriminative PRMs that resist Hard2Verify-level collapse, (f) tests discriminative-to-generative PRM distillation, or (g) explicitly addresses the anti-complementarity risk in composing data selection efficiency (ActPRM-style) with annotation quality improvement (RCB-style).\",\n  \"inspired_by\": \"Field gap: process supervision for problems at or beyond the model's capability frontier, where MC estimation produces degenerate near-zero-variance estimates, probability-based methods (CPMI) produce uncalibrated scores, and current discriminative PRMs collapse catastrophically (78.3→37.3 F1 on Hard2Verify). Foundational discovery: we observe that mathematical reasoning exhibits fundamentally different step correlation structures across domains — the first systematic empirical characterization of this phenomenon. We formalize this via the dependency index δ_d = 1 − corr(empirical μ_k, predicted p^{K−k}), which quantifies per-domain independence violation. Near-independent domains (δ_d < 0.2: multi-step algebraic computation, sequential equation solving, coordinate geometry) exhibit smooth, predictable informativeness decay consistent with the Markov chain model; strongly dependent domains (δ_d > 0.5: insight-dependent proofs, combinatorial constructions, auxiliary-line geometry) show abrupt transitions where a single gateway step determines all subsequent viability. This structural discovery enables everything that follows: it determines where the independence idealization holds (and Theorem 1 applies tightly) vs. where it breaks down (and conservative bounds with δ_d-calibrated corrections are needed). It connects to Conditional Reward Modeling (arXiv 2509.26578) which formalizes inter-step dependencies via conditional probability chains, to 'What Are Step-Level Reward Models Rewarding?' (AAAI 2025) which empirically demonstrates that context-aware step evaluation outperforms context-free variants, and to 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) which independently confirms from representation geometry that late steps are ~24 AUC points more predictive of correctness than early steps. Our δ_d estimates provide the systematic per-domain empirical calibration that all three frameworks lack. Theoretical foundation: elementary Markov chain completion probability — the MC success rate from step k in a K-step solution is approximately p^{K-k} under an independent-step model, giving an exponential gradient that is sharper for harder problems. The key theoretical contribution is formalizing this into sufficient conditions (Theorem 1) under the independence idealization, with δ_d-calibrated corrections providing domain-aware bounds. Methodological innovation: (1) the AMCS-RCB combination addresses a 2D resource allocation problem (which steps to annotate × how many rollouts per step) that neither approach solves alone — AMCS (adaptive budget via Wilson score uncertainty) is orthogonal to RCB (curriculum over step positions via success rate gradient); (2) the ActPRM+RCB composition addresses a second orthogonal dimension — which steps to annotate (ActPRM's uncertainty-based selection) vs. how to annotate them (RCB's quality-improving curriculum) — but with an important caveat: if ActPRM's uncertain steps cluster at early positions where MC estimates are uninformative, the composition may produce anti-complementarity rather than multiplicative gains (failure mode F7); Phase 0 explicitly diagnoses this by analyzing ActPRM's step selection distribution across positions; (3) the discriminative-to-generative distillation pipeline reverses the typical RM-Distiller direction, using RCB-trained discriminative PRMs as cheap labelers to generate massive training data for generative PRMs — novel because discriminative PRMs produce labels at ~1000× lower cost per step than generative PRMs. Deployment motivation: the well-documented need for efficient discriminative PRMs in online RL training loops (GRPO/PPO), where generative PRMs are prohibitively expensive (Setlur et al. 2025; Fast-Slow Thinking RM 2026; PRIME and SPRO workarounds). Broader impact: the consistent 27-41 F1 gap between unsupervised/rollout-free methods and supervised MC-based PRMs on OmniMATH, plus the Hard2Verify collapse, demonstrate that annotation quality is the decisive bottleneck. Complementarity: CPMI-trained PRM for moderate-difficulty problems (cheapest), AMCS-RCB-trained discriminative PRM for frontier-hard RL training, generative PRM (optionally distillation-enhanced) for high-stakes test-time verification.\",\n  \"approach\": \"We propose Reverse-Curriculum Bootstrapping (RCB), a theoretically grounded annotation and training framework. The narrative arc is: discover structure (Contribution I) → formalize (Contribution II) → build methods (Contributions III-IV) → evaluate and deploy (Contribution V). **Contribution I — Empirical Discovery: Domain-Dependent Reasoning Step Correlation Structure (weeks 1-3, Phase 0).** This is the paper's most novel and independently valuable contribution. We provide the first systematic empirical characterization of how mathematical reasoning step correlations vary across domains. For each of the 7 primary Omni-MATH domains (Algebra, Precalculus, Calculus, Geometry, Discrete Mathematics, Number Theory, Applied Mathematics) and ≥10 of 33+ sub-domains: (a) Select 50+ problems per domain/sub-domain spanning difficulty levels. (b) Generate 8-12-step candidate solutions using Qwen3-32B. (c) Run N=64 MC rollouts from each step position k using Qwen3-32B as completer. (d) Measure success rate as a function of normalized step position (k/K), stratified by problem difficulty and mathematical domain. (e) Compute the dependency index δ_d = 1 − corr(empirical μ_k, predicted p_min^{K−k}) for each domain d, where p_min is the estimated per-step correctness probability. When δ_d ≈ 0, independence holds and the exponential gradient is fully exploitable; when δ_d is large, inter-step correlations attenuate the gradient. (f) Classify domains into tiers: near-independent (δ_d < 0.2), moderately dependent (0.2 ≤ δ_d < 0.5), strongly dependent (δ_d ≥ 0.5). (g) Compute bootstrap confidence intervals (95% CI) for all δ_d estimates to establish statistical significance. Target: δ_d classification accuracy ≥85% — the domain classification into near-independent/moderately-dependent/strongly-dependent should be robust across different problem samples from the same domain. (h) Test the mixture model: for strongly-dependent domains, fit the two-class mixture model where fraction α of problems have a 'gateway step' (p_gateway << p_other) and the rest are near-independent. Estimate α per domain. (i) Anti-complementarity diagnostic for ActPRM+RCB composition: reproduce ActPRM's ensemble uncertainty estimation on the same problem set and analyze whether ActPRM's selected uncertain steps correlate with step position. Specifically, test whether ensemble uncertainty is highest at early positions where MC estimates are uninformative — if so, this indicates the selection-quality tension described in failure mode F7. The δ_d characterization constitutes a standalone contribution regardless of RCB's effectiveness: it is the first empirical study connecting reasoning step correlation structure to mathematical domain properties, extending the geometric trajectory analysis of 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) — which shows late steps are ~24 AUC points more predictive of correctness — with domain-level structural decomposition. It also complements EvalQReason's (arXiv 2602.02295, 2026) Consecutive Step Divergence metric by providing a global positional characterization rather than local pairwise coherence. Concrete domain predictions based on mathematical structure: (i) Near-independence domains: multi-step algebraic computation (each step is a mechanistic transformation — e.g., polynomial expansion, equation manipulation — where correctness depends primarily on local arithmetic accuracy), sequential equation solving (substitution chains where each step's validity depends mainly on correctly applying the substitution), and coordinate geometry with computational steps (once the coordinate system is established, each computation is largely independent). For these domains, Theorem 1 provides tight predictions and RCB's exponential gradient is fully exploitable. (ii) Strong-dependency domains: insight-dependent proofs (choosing the right lemma or proof technique at step 1 — e.g., applying Vieta's formulas vs. direct computation for a symmetric polynomial problem — determines the viability of all subsequent steps, creating a single 'gateway' step with near-binary influence), combinatorial arguments requiring a key construction (e.g., finding the right bijection or invariant), and geometry problems requiring auxiliary constructions (e.g., drawing the right auxiliary line in a Euclidean geometry proof). In these domains, the step-1 choice creates strong correlations: p_1 effectively gates all subsequent p_j, violating the product factorization μ_k = ∏p_j. Total Phase 0 cost: ~300 H100-hours. Go/no-go criteria (domain-stratified): (i) Full-go: for ≥40% of frontier-hard problems (pass@1 < 5%), late-step rollouts (k/K > 0.8) achieve success rates ≥10%, AND δ_d shows meaningful variation across domains (range ≥ 0.3); (ii) Partial-go: 20-40% meet criterion (i), proceed with RCB restricted to qualifying domains (those with δ_d < 0.5); (iii) No-go: <20% qualify, pivot to AMCS-enhanced compounding estimators combined with difficulty curriculum, but still publish the δ_d characterization as a standalone contribution. **Contribution II — Theoretical Framework with Domain-Aware Corrections (weeks 1-2, concurrent with Phase 0):** We formalize the position-dependent MC informativeness under an independent-step Markov model, with corrections calibrated by the empirical δ_d values from Contribution I. Definition: an MC estimate at step k with N rollouts is c-informative if E[successes] = N·μ_k ≥ c, where μ_k = ∏_{j=k}^{K} p_j is the completion success rate. Proposition 1 (Monotonicity): μ_k ≤ μ_{k+1} for all k — informativeness is non-decreasing with step position. This holds regardless of the independence assumption since later steps are strictly closer to completion. Proposition 2 (Exponential Gradient): if per-step correctness p_j ∈ [p_min, p_max], then μ_k ∈ [p_min^{K-k}, p_max^{K-k}], giving approximately exponential growth toward later steps on hard problems. Theorem 1 (RCB Sufficient Condition, under independence idealization with δ_d-calibrated corrections): RCB produces strictly more informative annotations than uniform MC estimation whenever K > log(c/N)/log(p_min), with the earliest informative step at k* = K − ⌊log(c/N)/log(p_min)⌋. For domains with δ_d > 0, Theorem 1's bound is conservative by factor ~(1 − α_d) where α_d is the estimated gateway fraction from the mixture model. Corollary (Difficulty Threshold): RCB is beneficial when problem difficulty exceeds 1 − (c/N)^{1/K}. Updated framing: Theorem 1 provides 'sufficient conditions under the independence idealization, with empirically-calibrated corrections for domain-specific dependency structures characterized by δ_d.' The theoretical framework connects to ComMCS's compound variance formula (Theorem 4.3) by showing that RCB's position-aware annotation focuses variance reduction where it matters most. Under a simplified two-class mixture model where a fraction α of problems have a 'gateway step' (p_gateway << p_other) and the rest are near-independent, the effective success rate curve becomes: μ_k = α · p_gateway · p_other^{K-k-1} + (1-α) · p_other^{K-k}. The exponential gradient is preserved (dominated by the second term for moderate α) but attenuated in magnitude. **Contribution III — RCB Curriculum (weeks 4-14):** Enabled by the structural discovery (Contribution I) and theoretical framework (Contribution II). Phase 1 (weeks 4-6): Run MC rollouts from late step positions (k/K > 0.75) where the pilot confirmed non-trivial success rates, using Qwen3-235B-A22B as completer. Train PRM_0 (Qwen3-7B base). Domain-aware curriculum: for near-independent domains (δ_d < 0.2), extend the curriculum aggressively (5 phases); for strongly dependent domains (δ_d ≥ 0.5), use a conservative curriculum (2-3 phases) that terminates earlier. Phases 2-5 (weeks 6-14): Each phase i uses PRM_{i-1} to guide rollouts at progressively earlier step windows via best-of-16 selection. Early termination: if PRM-guided rollouts do not achieve ≥2pp higher success rate than unguided. **Contribution IV — AMCS-RCB Combined Method and ActPRM+RCB Composition (weeks 4-14, parallel variants):** AMCS-RCB: Within each RCB phase, replace the fixed rollout budget (N=64) with AMCS-style adaptive allocation: use Wilson score interval to allocate k_init=6 to k_max=32 rollouts per step based on estimation uncertainty. This addresses the 2D resource allocation problem: RCB determines *which steps to annotate* (step position curriculum), AMCS determines *how many rollouts per step* (uncertainty-adaptive budget). Theoretical connection: Theorem 1 determines the informative step range; AMCS optimizes rollout allocation within that range. Expected benefit: 20-30% compute reduction with equivalent or better label quality. ActPRM+RCB composition ablation: Replace uniform step selection with ActPRM's ensemble uncertainty-based selection within the RCB curriculum. Three sub-conditions: (i) Naive composition: ActPRM selects steps, RCB provides MC estimates — tests raw complementarity; (ii) Hybrid composition: ActPRM selects steps only from within the RCB-determined informative window (k ≥ k*), combining quality-aware selection with quality-aware annotation — mitigates the anti-complementarity risk; (iii) Comparison: measure whether ActPRM's uncertain steps disproportionately fall inside vs. outside the informative window, directly testing the F7 failure mode hypothesis. (+100 H100-hours for this ablation.) **Contribution V — Dual-Track Evaluation and Distillation Pipeline:** Track A (discriminative, weeks 4-16): Train 7B discriminative PRM via RCB and AMCS-RCB curricula. Evaluate on ProcessBench (OmniMATH, OlympiadBench), Hard2Verify, PRMBench, and best-of-N accuracy on Omni-MATH hard-filtered and AIME 2025/2026 hardest problems. Track B (dependency characterization + generative + distillation, weeks 12-18): (B1) Primary deliverable — Complete δ_d characterization: publish δ_d values with bootstrap 95% CIs across all 7 primary Omni-MATH domains AND ≥10 of 33+ sub-domains. Include δ_d classification robustness analysis (target: ≥85% accuracy on held-out problem samples). Analyze relationship between δ_d and problem structural features (proof vs. computation, number of key insights, solution path diversity). Connect findings to Conditional Reward Modeling (arXiv 2509.26578) and provide systematic empirical calibration for their conditional probability framework. (B2) Multi-architecture fine-tuning: fine-tune GenPRM, ThinkPRM, and R-PRM architectures on RCB-annotated data vs. standard MC annotations from the same problems, testing whether annotation quality is a paradigm-wide bottleneck across generative PRM architectures. (B3) Novel discriminative-to-generative distillation pipeline: use the RCB-trained discriminative PRM (fast, single forward pass per step) to generate step-level correctness labels on a large corpus of solution traces (100K+ traces), then use these cheap labels to fine-tune generative PRMs. This reverses the typical RM-Distiller direction (generative→discriminative) and exploits the ~1000× cost advantage of discriminative inference. (B4) Hard2Verify generative evaluation: evaluate RCB-fine-tuned generative PRMs on Hard2Verify. **Ablations (weeks 14-17):** (1) RCB vs. uniform MC estimation; (2) RCB vs. stronger completer only (Qwen3-235B with higher rollout budget); (3) AMCS-RCB vs. pure AMCS vs. pure RCB — the key Contribution IV comparison; (4) CPMI labels vs. RCB MC labels at matched difficulty, testing complementarity; (5) Inference speed comparison: wall-clock time per evaluation for RCB discriminative PRM vs. GenPRM, ThinkPRM, RM-R1, for a representative GRPO scenario (1,000 prompts × 16 rollouts × 20 steps = 320,000 evaluations per epoch); (6) Distillation efficiency: compare generative PRM trained on discriminative-PRM labels vs. same model trained on MC labels vs. same model trained on RCB-MC labels, at matched data scale; (7) ActPRM+RCB composition: naive vs. hybrid vs. ActPRM-only vs. RCB-only (as described in Contribution IV above); (8) Domain-stratified RCB: run RCB separately on near-independence vs. strong-dependency domains (as classified by δ_d from Phase 0) to test whether the curriculum adapts naturally to different correlation structures, and whether restricting to near-independent domains yields disproportionate gains. **Evaluation (weeks 17-19):** Track A targets — ProcessBench OmniMATH: improve 7B discriminative PRM F1 from 67.0 baseline (ActPRM, current strongest 7B) to 72-76 F1, approaching ThinkPRM-7B (74.0 F1) without generative overhead; OlympiadBench: 74-78 F1 vs. 71.4 ActPRM baseline; Hard2Verify: target ≥50 F1 (from 37.3 baseline for 72B model — demonstrating that RCB-trained 7B PRM resists catastrophic frontier-hard collapse). Track B targets — Primary: δ_d characterization across all 7 Omni-MATH domains + ≥10 sub-domains with bootstrap CIs, δ_d classification accuracy ≥85%. Secondary: ProcessBench OmniMATH for RCB-fine-tuned generative PRMs: ≥3 F1 improvement on Hard2Verify, ≥2 F1 on ProcessBench OmniMATH across at least 2 of 3 tested architectures; distillation pipeline: achieve ≥90% of MC-trained generative PRM accuracy with 10× less labeling compute, demonstrating discriminative-to-generative knowledge transfer. **Failure mode analysis:** (F1) Pilot invalidation — theoretical gradient insufficient, with partial-go and no-go pathways (no-go still publishes δ_d characterization as standalone contribution); (F2) Bootstrap cascade failure — caught by early termination criterion; (F3) Key-insight ceiling — problems where single critical insight determines correctness at all subsequent steps, quantified by high δ_d values and handled by domain-stratified analysis and the mixture model framework; (F4) AMCS-RCB overhead — if adaptive allocation overhead exceeds compute savings, pure RCB may dominate; (F5) Track B null result — if annotation quality does not improve generative PRMs, this is an informative negative result (generative PRMs learn via reasoning rather than training data quality), and Track A + distillation pipeline + theoretical contribution + dependency characterization remain primary; (F6) Independence violation too severe — if δ_d > 0.5 for most domains, the exponential gradient is too attenuated for RCB to substantially outperform simple late-step-only training; however, the partial-go pathway (restricting to near-independent domains) and the dependency characterization itself remain valuable standalone contributions; (F7) ActPRM+RCB anti-complementarity — if ActPRM's ensemble uncertainty correlates positively with step position (i.e., uncertain steps cluster at early positions where MC estimates are uninformative), the naive composition produces tension rather than multiplicative gains. Phase 0 explicitly tests this by analyzing ActPRM's step selection distribution across positions. Mitigation: if anti-complementarity is confirmed, use the hybrid strategy where ActPRM selects steps from the RCB-determined informative window (k ≥ k*), combining quality-aware selection with quality-aware annotation. If neither naive nor hybrid composition outperforms the individual methods, this is itself an informative finding about the interaction structure of data selection and data quality optimization. **Practical deployment framework (three-tier):** CPMI-trained PRM for moderate-difficulty problems (cheapest), AMCS-RCB-trained discriminative PRM for frontier-hard RL training, generative PRM (optionally distillation-enhanced) for high-stakes test-time verification.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"7200 H100-hours (300 for Phase 0 including completer evaluation + MC pilot + AMCS baseline + CPMI comparison + ActPRM baseline reproduction + dependency index computation across 7 domains and ≥10 sub-domains, 3200 for MC rollout generation across Phases 1-5, 1200 for iterative discriminative PRM fine-tuning, 400 for AMCS-RCB parallel track, 1000 for Track B multi-architecture generative PRM fine-tuning + distillation pipeline, 600 for ablations including ActPRM+RCB composition (naive + hybrid) and domain-stratified RCB, 500 for evaluation including Hard2Verify benchmarking and inference speed measurement)\",\n      \"timeline\": \"18-19 weeks (2 weeks theoretical framework + Phase 0 pilot concurrent, 1 week go/no-go + curation, 10 weeks for 5 RCB phases with AMCS-RCB parallel, 4 weeks Track B parallel from week 12, 2 weeks ablations, 1-2 weeks evaluation/writing)\",\n      \"estimated_gpu_cost\": \"$20,520 (at ~$2.85/H100-hour)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"6300 H100-hours (efficiency gains from Claude-assisted theoretical analysis, pilot data fitting, dependency index computation, automated hyperparameter tuning, and ablation design reducing wasted runs by ~13%)\",\n      \"timeline\": \"15-16 weeks (Claude accelerates theoretical framework development, dependency analysis, pilot analysis, Phase 0 model fitting, experiment scripting, and paper drafting, saving ~3 weeks; fits estimated ICLR 2027 deadline starting June 1)\",\n      \"claude_api_cost\": \"$1,300 (Sonnet 4.6 for code generation, theoretical proof verification, dependency characterization analysis, pilot data analysis, experiment orchestration, Track B design, and paper drafting; ~300M input + 65M output tokens)\",\n      \"estimated_gpu_cost\": \"$17,955\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"8300 H100-hours (additional compute for AMCS-RCB hyperparameter sweeps, ActPRM+RCB composition search including naive vs. hybrid variants, multi-architecture Track B fine-tuning, distillation pipeline optimization, systematic ablation execution, dependency model validation across all 7+10 domains/sub-domains, and domain-stratified analysis)\",\n      \"timeline\": \"11-12 weeks (fully automated pipeline with parallel RCB + AMCS-RCB tracks and parallel Track B; pilot phase still requires ~2.5 weeks for sequential completer evaluation + analysis)\",\n      \"claude_api_cost\": \"$4,400 (heavy Opus 4.7 usage for autonomous experiment design, theoretical framework development, dependency characterization, pilot go/no-go analysis, AMCS-RCB integration, ActPRM+RCB composition, distillation pipeline design, and adaptive protocol modification; ~470M input + 130M output tokens)\",\n      \"estimated_gpu_cost\": \"$23,655\",\n      \"speed_bottleneck\": \"MC rollout generation with Qwen3-235B-A22B completer requires multi-node inference; RCB phases are inherently sequential; AMCS-RCB runs in parallel with pure RCB track; Track B independent from week 12. Distillation pipeline requires completed Track A discriminative PRM. ActPRM baseline reproduction and dependency analysis parallelizable with Phase 0. δ_d characterization across all 7+10 domains/sub-domains requires comprehensive Phase 0 coverage but is parallelizable across domains.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (estimated deadline: ~September 2026, projected from ICLR 2026 schedule; not officially announced as of May 2026) — primary target, 15-16 week human-in-loop timeline fits starting June 1\",\n    \"AISTATS 2027 (estimated deadline: October 2026) — backup if additional time needed\",\n    \"ICML 2027 (full paper estimated: ~January 2027) — comfortable deadline for full manual timeline\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Let's Verify Step by Step (ICLR 2024)\",\n    \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations (ACL 2024)\",\n    \"Improve Mathematical Reasoning in Language Models by Automated Process Supervision [OmegaPRM] (arXiv 2024)\",\n    \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (ICLR 2025)\",\n    \"rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking (ICML 2025)\",\n    \"Training Large Language Models for Reasoning through Reverse Curriculum Reinforcement Learning [R3] (ICML 2024)\",\n    \"SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning (NeurIPS 2025)\",\n    \"Process Reward Models That Think [ThinkPRM] (TMLR 2026; arXiv 2504.16828)\",\n    \"The Lessons of Developing Process Reward Models in Mathematical Reasoning (ACL Findings 2025)\",\n    \"ProcessBench: Identifying Process Errors in Mathematical Reasoning (ACL 2025)\",\n    \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026)\",\n    \"R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025)\",\n    \"Dyve: Thinking Fast and Slow for Dynamic Process Verification (EMNLP 2025)\",\n    \"RM-R1: Reward Modeling as Reasoning (ICLR 2026)\",\n    \"SCRL: From Reasoning Chains to Verifiable Subproblems — Curriculum RL Enables Credit Assignment for LLM Reasoning (arXiv 2605.22074, 2026)\",\n    \"ComMCS: Improving Value-based Process Verifier via Low-Cost Variance Reduction (AAAI 2026)\",\n    \"Omni-MATH: A Universal Olympiad Level Mathematic Benchmark For Large Language Models (ICLR 2025)\",\n    \"AURORA: Automated Process Reward Model Training via Reverse Verification (arXiv 2025)\",\n    \"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning (NeurIPS 2025)\",\n    \"Unsupervised Process Reward Models [uPRM] (arXiv 2605.10158, 2026)\",\n    \"Fast-Slow Thinking RM: Efficient Integration of Scalar and Generative Reward Models (arXiv 2603.20212, 2026)\",\n    \"PRIME: Process Reinforcement through Implicit Rewards (arXiv 2502.01456, 2025)\",\n    \"Is PRM Necessary? Problem-Solving RL Implicitly Induces PRM Capability in LLMs (arXiv 2505.11227, 2025)\",\n    \"When To Solve, When To Verify: Compute-Optimal Problem Solving and Verification (Setlur et al., arXiv 2504.01005, 2025)\",\n    \"Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems (arXiv 2026)\",\n    \"Efficient Process Reward Modeling via Contrastive Mutual Information [CPMI] (arXiv 2604.10660; confirmed accepted at ACL 2026 Main Conference)\",\n    \"From Static to Dynamic: Adaptive Monte Carlo Search for Mathematical Process Supervision [AMCS] (arXiv 2509.24351, 2025)\",\n    \"Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (arXiv 2510.13744, 2025)\",\n    \"RM-Distiller: Exploiting Generative LLM for Reward Model Distillation (arXiv 2601.14032, 2026)\",\n    \"SPRO: Self-Guided Process Reward Optimization with Redefined Step-wise Advantage (arXiv 2507.01551, 2025)\",\n    \"Efficient Process Reward Model Training via Active Learning [ActPRM] (arXiv 2504.10559, COLM 2025)\",\n    \"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning (arXiv 2509.26578, 2025)\",\n    \"What Are Step-Level Reward Models Rewarding? Counterintuitive Findings from MCTS-Boosted Mathematical Reasoning (AAAI 2025)\",\n    \"LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals (arXiv 2604.05655, 2026)\",\n    \"EvalQReason: A Framework for Step-Level Reasoning Evaluation in Large Language Models (arXiv 2602.02295, 2026)\"\n  ],\n  \"description\": \"This project addresses the Monte Carlo cold-start problem in process reward model training through five integrated contributions, reframed to lead with the paper's most novel discovery: (I) the first systematic empirical characterization of domain-dependent reasoning step correlation structure across mathematical domains via the dependency index δ_d = 1 − corr(empirical μ_k, predicted p^{K−k}), (II) a theoretical framework formalizing MC estimation informativeness as a function of step position under an independence idealization with δ_d-calibrated corrections, (III) a reverse-curriculum bootstrapping (RCB) annotation algorithm enabled by the structural discovery, (IV) a combined AMCS-RCB method integrating adaptive per-step rollout allocation with position-aware curriculum, and (V) dual-track evaluation with a novel discriminative-to-generative PRM distillation pipeline. The narrative arc: we discover that mathematical reasoning exhibits fundamentally different step correlation structures across domains — from near-independent (algebraic computation: δ_d < 0.2) to strongly dependent (insight-dependent proofs: δ_d > 0.5) — and this structural discovery enables domain-aware annotation strategies that were previously impossible. Independent geometric evidence from 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) confirms the positional informativeness gradient: late reasoning steps are ~24 AUC points more predictive of correctness than early steps (0.87 vs 0.63 AUC), with correct/incorrect trajectories diverging primarily at late stages in representation space. The severity of the problem is now quantified by Hard2Verify: Qwen2.5-Math-PRM-72B collapses from 78.3 F1 on ProcessBench to 37.3 on frontier-hard Olympiad problems — a catastrophic 41-point drop. While generative PRMs bypass MC estimation via inference-time reasoning (ThinkPRM-14B: 85.7 F1), they generate 1,000-5,000 tokens per step — infeasible for RL training (Setlur et al. 2025: GenRM needs 8× compute to match self-consistency, up to 128× for a 3.8% accuracy gain, Figure 1b). Rollout-free alternatives (CPMI at 25.6 F1 using Qwen3-8B-Base labeler/Qwen3-4B-Base PRM, confirmed accepted at ACL 2026 Main Conference; uPRM at 39.8 F1) consistently underperform supervised PRMs by 27-41 F1 points on hard problems. ActPRM (COLM 2025) achieves the current strongest 7B discriminative PRM performance (67.0 F1 OmniMATH, 75.0 avg F1 ProcessBench) via active learning-based step selection with only 20% of UniversalPRM's annotation budget, but optimizes data selection without addressing MC estimation quality — the step selection and annotation quality dimensions are orthogonal, with a potential anti-complementarity tension when composed with RCB (failure mode F7: if ActPRM's uncertain steps cluster at early positions where MC estimates are uninformative, the composition produces tension rather than multiplicative gains; Phase 0 explicitly diagnoses this, with a hybrid mitigation constraining ActPRM selection to the RCB-determined informative window). AMCS (arXiv 2509.24351) adaptively allocates rollout budget per-step via Wilson score interval uncertainty but treats all step positions symmetrically and does not address the fundamental uninformativeness of early-step MC estimates on hard problems. **Contribution I** provides the δ_d dependency index across all 7 primary Omni-MATH domains (Algebra, Precalculus, Calculus, Geometry, Discrete Mathematics, Number Theory, Applied Mathematics) and ≥10 of 33+ sub-domains, with bootstrap confidence intervals and ≥85% classification robustness target — the first systematic domain-level quantification of step independence violation, complementing the theoretical frameworks of Conditional Reward Modeling (arXiv 2509.26578) and the empirical findings of 'What Are Step-Level Reward Models Rewarding?' (AAAI 2025) with systematic per-domain calibration that both lack. **Contribution II** formalizes the position-dependent MC gradient: under the independence idealization, the success rate from step k is approximately p^{K-k}, giving exponential growth toward later steps. Theorem 1 provides sufficient conditions for when RCB outperforms uniform MC: whenever K > log(c/N)/log(p_min), early steps are uninformative regardless of rollout budget. For domains with δ_d > 0, Theorem 1's bound is conservative by factor ~(1-α_d), but RCB remains beneficial because Proposition 1 (monotonicity of μ_k) holds regardless of independence. **Contribution III** (RCB) exploits the gradient with domain-aware curriculum depth: aggressive (5 phases) for near-independent domains, conservative (2-3 phases) for strongly dependent domains. **Contribution IV** (AMCS-RCB) combines position curriculum with adaptive rollout allocation — addressing the 2D resource optimization that neither method solves alone. **Contribution V** introduces dual-track evaluation separating annotation quality from model capability: Track A trains a 7B discriminative PRM targeting 72-76 F1 on ProcessBench OmniMATH (5-9 points over ActPRM's 67.0, current strongest 7B) and ≥50 F1 on Hard2Verify (vs. 37.3 baseline for 72B model); Track B's primary deliverable is the complete δ_d characterization with statistical significance tests, with secondary targets of ≥3 F1 improvement on Hard2Verify and ≥2 F1 on ProcessBench OmniMATH for generative PRMs, plus a discriminative-to-generative distillation pipeline targeting ≥90% of MC-trained accuracy with 10× less labeling compute. Note on ProcessBench baselines: Qwen2.5-Math-PRM-7B (66.3/67.5) is distinct from Qwen2.5-Math-7B-PRM800K (44.3/50.7) — the 22-point gap on OmniMATH demonstrates training data quality is decisive (reported in R-PRM EMNLP 2025 Table 1 and 'Is PRM Necessary?' 2505.11227 Table 1). Evaluation on three benchmarks (ProcessBench, Hard2Verify, best-of-N), both paradigms (discriminative + generative), and the three-tier deployment framework: CPMI for moderate problems, AMCS-RCB discriminative PRM for frontier-hard RL training, generative PRM for high-stakes verification.\",\n  \"project_name\": \"reverse_curr_prm_bootstrap\",\n  \"source\": \"web_research\",\n  \"title\": \"Reverse-Curriculum Bootstrapping for Process Verification at the Capability Frontier\"\n}\n\n## Reviewer feedback (round 7)\nIssues: [\"Missing SIA (arXiv 2604.06192, April 2026): 'The Stepwise Informativeness Assumption' directly formalizes that reasoning prefixes accumulate answer-relevant information monotonically — essentially the theoretical foundation underlying Proposition 1. It treats this as a universal property; the proposal's domain-dependent δ_d variation is complementary. SIA MUST be cited and differentiated from, and could actually strengthen the proposal by positioning δ_d as empirical calibration of SIA's theoretical framework.\", \"Missing SHAPE (arXiv 2604.06636, April 2026): 'Stage-aware Hierarchical Advantage via Potential Estimation' proposes position/stage-dependent credit assignment for reasoning, achieving 3% accuracy gains. While methodologically distinct (RL credit assignment vs. MC annotation quality), the thematic overlap with 'step position determines informativeness' requires citation and differentiation.\", \"Missing MCNIG (arXiv 2603.17815, March 2026): 'Process Supervision via Monte Carlo Net Information Gain' proposes an information-theoretic alternative to standard MC estimation with O(N) complexity. Directly relevant as an alternative approach to improving MC-based process supervision.\", \"LLM Reasoning as Trajectories AUC claim slightly misleading: The proposal states '~24 AUC points (0.87 vs 0.63)' but the paper's own comparison uses average late-step AUC of 0.83, not the peak single-layer 0.87. The honest comparison is ~20 AUC points (0.83 vs 0.63). Stating 0.87 cherry-picks the best layer against the early-step average.\", \"Setlur et al. appendix reference error: The proposal says 'higher multipliers reported for other models in Appendix F' but the 512× for Qwen-2.5-7B-Instruct appears in Appendix H ('Trends Across Model Families'), not Appendix F ('Improving Verifier Efficiency').\"]\nFeedback: The round-7 revision successfully addresses all four round-6 issues: CPMI venue verified through arXiv self-declaration, F7 anti-complementarity failure mode added with hybrid mitigation, contributions reordered to lead with δ_d discovery, and Track B ambition substantially raised. The proposal's scholarly rigor is exceptional — all major numerical claims verified correctly through independent search. The average score (3.875) remains just below the 4.0 threshold, with impact (3.5) as the persistent drag. Three actionable items to cross the threshold:\n\n(1) **Integrate SIA as theoretical support and differentiation target.** SIA (arXiv 2604.06192) formalizes step informativeness as a universal property of autoregressive models. This actually STRENGTHENS the proposal: cite SIA as providing the theoretical foundation for why position matters, then position δ_d as the first empirical test of whether SIA's universal claim holds uniformly across mathematical domains — or whether the informativeness accumulation rate is domain-dependent. This reframing elevates the δ_d contribution from 'empirical characterization' to 'empirical calibration and potential falsification of a recently-proposed theoretical framework.' If δ_d reveals domain-dependent variation, it demonstrates that SIA's universality is an oversimplification — a finding with broad theoretical implications.\n\n(2) **Add SHAPE and MCNIG to landscape.** SHAPE (stage-aware credit assignment) should be differentiated as operating in the RL domain while your work addresses MC annotation quality. MCNIG (information-theoretic MC alternative) is a complementary approach that could serve as an additional baseline.\n\n(3) **Fix two minor factual errors:** (a) Correct '~24 AUC points (0.87 vs 0.63)' to '~20 AUC points (0.83 average late-step vs 0.63 early-step AUC, with peak single-layer reaching 0.87)' — this is more honest and still supports the point. (b) Change 'Appendix F' to 'Appendix H' for the Setlur 512× reference.\n\nThe SIA integration is the key lever for crossing 4.0: it transforms the δ_d contribution from 'novel empirical measurement' to 'empirical test of a concurrent theoretical framework with domain-specific findings that have implications beyond PRM training.' This raises both novelty and impact.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields.\n\n## 停滞提醒\n经过 7 轮修订，近 3 轮平均分从 3.9 到 3.9，无明显改善。\n考虑 major revision 或 pivot。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-28T04:55:01.924Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T04:55:01.924Z",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294"
}
```

---

## Round 1

67 recorded events

### User

_source line 3 · 2026-05-28T04:55:01.975Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-28 (UTC).**

## Original idea
{
  "change_summary": "Major narrative restructuring to lead with the strongest novelty — the empirical discovery of domain-dependent step correlation structure (δ_d index) — reframing the paper from 'applying an elementary observation' to 'discovering structure that enables a new training paradigm.' Four specific issues addressed: (1) CPMI venue verified: arXiv 2604.10660 abstract confirms 'Accepted at ACL 2026 Main Conference' — designation retained with verification source noted. (2) ActPRM+RCB composition tension explicitly addressed: added failure mode F7 analyzing the anti-complementarity risk that ActPRM's ensemble uncertainty may correlate with step position (uncertain steps clustering at early positions where MC estimates are uninformative), with Phase 0 diagnostic and hybrid mitigation (constraining ActPRM selection to the RCB-determined informative window k ≥ k*). (3) Contribution ordering restructured throughout all sections: (I) Empirical discovery of domain-dependent reasoning step correlation structure via δ_d (was Contribution V), (II) Theoretical framework with δ_d-calibrated corrections (was I), (III) RCB curriculum (was II), (IV) AMCS-RCB combination (was III), (V) Dual-track evaluation + distillation pipeline (was IV). Narrative arc: 'We discover X → this enables Y (theory) → which produces Z (methods) → with applications W (evaluation + distillation).' (4) Track B ambition substantially raised: primary Track B deliverable is now the complete δ_d characterization across all 7 primary Omni-MATH domains (Algebra, Precalculus, Calculus, Geometry, Discrete Mathematics, Number Theory, Applied Mathematics) AND ≥10 of 33+ sub-domains, with bootstrap confidence intervals for statistical significance and ≥85% δ_d classification robustness target. The ≥2 F1 improvement for generative PRMs is reframed as a secondary Track B outcome, with the δ_d characterization as the independently valuable primary deliverable. Two new supporting references integrated substantively: 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) providing independent geometric evidence for the positional informativeness gradient (~24 AUC point gap between late-step and early-step correctness prediction, 0.87 vs 0.63), and EvalQReason (arXiv 2602.02295, 2026) introducing Consecutive Step Divergence (CSD) measuring local inter-step coherence.",
  "core_problem": "Can we discover and exploit domain-dependent structure in mathematical reasoning step correlations to overcome the Monte Carlo cold-start problem in process reward model training? The underlying observation rests on elementary probability theory: in a Markov chain completion, the probability of reaching a target state increases as the number of remaining transitions decreases. Under an independent-step model with per-step correctness probability p, the MC success rate from step k in a K-step solution is approximately p^{K-k} — an exponential gradient that grows sharply toward later steps, especially for hard problems (low p). But five critical empirical and theoretical questions are unanswered: (1) Does mathematical reasoning exhibit systematically different step correlation structures across domains, and can we quantify this variation to determine where the independence idealization holds and where it breaks down? (2) Is the magnitude of the position-dependent success-rate gradient large enough on frontier-hard problems to produce meaningfully informative labels, and can we formalize sufficient conditions for when RCB outperforms uniform MC estimation — with domain-specific corrections? (3) For which mathematical problem types does the gradient hold tightly (near-independence), and where is it attenuated by inter-step dependencies (strong dependency)? (4) How does the informativeness gradient interact with adaptive rollout budget allocation (AMCS-style per-step uncertainty-based sampling)? (5) Can annotation quality improvement (RCB) compose with annotation efficiency improvement (ActPRM-style active step selection), or does the composition create anti-complementarity tension where ActPRM's uncertain steps cluster precisely where MC estimates are uninformative? The severity of the problem is empirically confirmed by Hard2Verify (arXiv 2510.13744): Qwen2.5-Math-PRM-72B drops from 78.3 F1 on ProcessBench to 37.3 on frontier-hard Olympiad problems — a catastrophic 41-point collapse showing that current discriminative PRMs trained with standard MC annotations are fundamentally inadequate at the capability frontier. Independent geometric evidence from 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) confirms the positional informativeness gradient from representation space: late reasoning steps are ~24 AUC points more predictive of correctness than early steps (0.87 vs 0.63 AUC), with correct and incorrect trajectories diverging primarily at late stages — supporting the structural premise that step position carries systematic informativeness signals. Meanwhile, ActPRM (COLM 2025) demonstrates that active learning-based step selection can improve discriminative PRM efficiency — achieving 67.0 F1 on OmniMATH with only 20% annotation budget via ensemble uncertainty — but does not address the quality of MC estimates themselves, leaving early-step uninformativeness unresolved on frontier-hard problems. Rollout-free alternatives like CPMI (arXiv 2604.10660; confirmed accepted at ACL 2026 Main Conference) bypass MC estimation via contrastive mutual information on model probabilities (using Qwen3-8B-Base for labeling, Qwen3-4B-Base for PRM training), but achieve only 25.6 F1 on ProcessBench OmniMATH — far below supervised discriminative PRMs (66.3-71.1 F1) — because model probability calibration degrades on frontier-hard problems. AMCS (arXiv 2509.24351) adaptively allocates rollout budget per-step based on estimation uncertainty (Wilson score interval), improving annotation efficiency, but does not address the fundamental issue that early-step MC estimates on hard problems are uninformative regardless of rollout budget — they converge to near-zero. The independent-step Markov model underlying our theoretical framework is an idealization: mathematical reasoning exhibits domain-dependent correlation structures where approach selection at early steps can determine all subsequent steps' viability. We address this as our primary contribution by introducing a dependency index δ_d that quantifies per-domain independence violation from Phase 0 data, enabling empirically-calibrated corrections to the theoretical predictions. This structural discovery — the first systematic empirical characterization of reasoning step correlation structure across mathematical domains — constitutes the paper's most novel and independently valuable contribution. In near-independence domains (algebraic computation, equation solving, coordinate geometry), the independent-step model is well-calibrated and Theorem 1 provides tight bounds; in strong-dependency domains (insight-dependent proofs, combinatorial constructions, auxiliary-line geometry), Theorem 1 provides conservative bounds rather than tight estimates, and the pattern of deviation is itself an informative finding about reasoning structure that connects to Conditional Reward Modeling (arXiv 2509.26578) and 'What Are Step-Level Reward Models Rewarding?' (AAAI 2025). Critically, Proposition 1 (monotonicity of μ_k) holds regardless of independence — later steps always have higher completion rates — so RCB's curriculum remains beneficial even when the exponential rate of growth is attenuated by dependencies. If the domain-dependent structure is validated and the position-dependent gradient is formalized, the resulting high-quality MC annotations serve a triple purpose: (a) training efficient discriminative PRMs for online RL deployment, (b) providing better fine-tuning data for generative PRMs across architectures, and (c) enabling a novel discriminative-to-generative distillation pipeline where the fast RCB-trained PRM serves as a cheap labeler for training generative PRMs at scale.",
  "opportunity": "The MC cold-start problem in PRM training remains a critical bottleneck, now quantified by Hard2Verify: the best discriminative PRM (Qwen2.5-Math-PRM-72B) collapses from 78.3 F1 on ProcessBench to 37.3 on frontier-hard Olympiad problems — a 41-point drop demonstrating catastrophic degradation precisely where strong verification is most needed. OmegaPRM acknowledges it 'requires verifiable gold answers, making it inapplicable when the completer rarely solves' hard problems. Four research directions have emerged, but all have significant limitations. **Direction 1: Generative PRMs** (GenPRM, R-PRM, ThinkPRM, RM-R1) achieve strong results (ThinkPRM-14B: 85.7 F1 on ProcessBench OmniMATH) but incur substantially higher per-step verification costs: Setlur et al. (2025) show GenRM requires 8× compute to match self-consistency, up to 128× for a 3.8% accuracy gain (Figure 1b); ThinkPRM generates 1,000-5,000 tokens per step vs. a discriminative PRM's single scalar output. This cost differential creates a critical deployment gap in online RL training loops (GRPO/PPO), where millions of PRM evaluations are needed per training run. Fast-Slow Thinking RM (2026) explicitly identifies generative RM reasoning costs as 'orders of magnitude higher.' **Direction 2: Rollout-free label generation.** CPMI (arXiv 2604.10660; confirmed accepted at ACL 2026 Main Conference) bypasses MC rollouts via contrastive pointwise mutual information using Qwen3-8B-Base for labeling and Qwen3-4B-Base for PRM training, reducing annotation cost by 84% and token generation by 98%. However, CPMI achieves only 25.6 F1 on ProcessBench OmniMATH — the authors explicitly exclude 'extremely difficult problems' because model probability calibration degrades at frontier difficulty. Together with uPRM (39.8 F1), unsupervised/rollout-free methods consistently underperform supervised MC-based PRMs by 27-41 F1 points on hard problems. **Direction 3: Adaptive MC estimation.** AMCS (arXiv 2509.24351) allocates rollout budget adaptively per-step based on Wilson score interval uncertainty — uncertain steps (success rate μ∈[0.4,0.6]) receive ~20 rollouts vs ~7 for confident steps — improving annotation efficiency. However, AMCS treats all step positions symmetrically and does not exploit the position-dependent success rate gradient: on frontier-hard problems, early steps are not merely 'uncertain' but uninformative (μ≈0), so even maximum-budget AMCS rollouts yield near-zero successes. **Direction 4: Data-efficient annotation via active learning.** ActPRM (arXiv 2504.10559, COLM 2025) uses ensemble uncertainty (aleatoric and epistemic criteria with an ensemble of ~32 classification heads on Qwen2.5-Math-7B-Instruct) to select which steps to annotate, achieving 67.0 F1 on OmniMATH, 71.4 on OlympiadBench, and 75.0 avg F1 on ProcessBench — the current strongest 7B discriminative PRM — using only 20% of UniversalPRM's annotation budget (6% of Qwen2.5-Math-PRM-7B's). However, ActPRM optimizes data selection without addressing MC estimation quality — it still uses standard MC rollouts for the selected steps, inheriting the cold-start problem on frontier-hard problems. The step selection and annotation quality dimensions are orthogonal. **The gap RCB fills:** No existing approach (a) empirically characterizes domain-dependent step correlation structure across mathematical reasoning domains, (b) provides formal conditions characterizing when MC estimation becomes informative as a function of step position with domain-specific dependency corrections, (c) exploits the position-dependent gradient as a training curriculum, (d) combines step-position-aware curriculum with adaptive per-step budget allocation, (e) composes with active learning-based step selection (ActPRM-style) while explicitly addressing the anti-complementarity risk that uncertain steps may cluster where MC estimates are uninformative, or (f) produces a discriminative-to-generative distillation pipeline. RCB addresses all six: the δ_d dependency index provides the first systematic characterization of reasoning step correlation structure (Contribution I), the theoretical framework formalizes informativeness conditions with domain-aware corrections (Contribution II), the curriculum exploits the gradient (Contribution III), AMCS-RCB combines position curriculum with adaptive allocation (Contribution IV), and dual-track evaluation with distillation addresses deployment needs (Contribution V). Independent geometric evidence from 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) confirms the positional informativeness gradient — late steps are ~24 AUC points more predictive of correctness — while EvalQReason's Consecutive Step Divergence (arXiv 2602.02295, 2026) provides a complementary local coherence metric. The resulting annotations serve both discriminative PRM training and a novel discriminative-to-generative distillation pipeline, addressing label quality as a paradigm-wide bottleneck. ComMCS (AAAI 2026) demonstrates a related insight — compounding MC estimates across adjacent steps reduces variance — but its theoretical framework treats all step positions symmetrically and does not address domain-dependent correlation structure.",
  "landscape": "**Step correlation structure and reasoning geometry (emerging area — our primary novelty).** No existing work provides systematic empirical quantification of domain-dependent step correlation structure across mathematical reasoning domains. Conditional Reward Modeling (arXiv 2509.26578) formalizes inter-step dependencies via conditional probability chains but does not empirically measure domain-specific correlation patterns. 'What Are Step-Level Reward Models Rewarding?' (AAAI 2025) shows that contextual information across steps is crucial for reward quality, with context-aware SRMs outperforming context-free variants (+7.35% vs +3.64% on GSM8K), empirically confirming the presence of inter-step dependencies but not characterizing their domain-specific structure. ContextPRM (arXiv 2509.24460, 2025) models contextual coherence between CoT steps for multi-domain generalization but does not quantify per-domain dependency strength. 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) provides independent geometric evidence that late reasoning steps are ~24 AUC points more predictive of correctness than early steps (0.87 vs 0.63 AUC), with correct/incorrect trajectories diverging primarily at late stages in representation space — but analyzes trajectories as a whole without decomposing by mathematical domain. EvalQReason (arXiv 2602.02295, 2026) introduces Consecutive Step Divergence (CSD) measuring local coherence between adjacent reasoning steps, achieving F1=0.88 for correctness classification with sequential models — providing a complementary local perspective to our global positional informativeness gradient. Our δ_d index fills the gap: the first systematic domain-level quantification of step independence violation, computed across all 7 primary Omni-MATH domains and ≥10 sub-domains, with bootstrap confidence intervals. **Generative PRMs (dominant recent trend):** GenPRM (AAAI 2026) reframes process reward modeling as a generative task using Relative Progress Estimation, achieving ~80.5 avg F1 on ProcessBench with a 7B model via Maj@8 — surpassing the 72B Qwen2.5-Math-PRM (78.3 avg F1). R-PRM (EMNLP 2025) activates reasoning in the PRM via seed data generation and self-improvement, achieving +11.9 F1 on ProcessBench and +8.5 F1 on PRMBench over baselines. RM-R1 (ICLR 2026) introduces chain-of-rubrics reasoning reward models generating up to 8,192 tokens per evaluation. ThinkPRM (TMLR 2026; arXiv 2504.16828) uses chain-of-thought verification trained on only 1K examples, reaching 85.7 F1 on ProcessBench OmniMATH and 87.3 on OlympiadBench — the current highest reported scores on these hard subsets. All generative PRMs trade training-time data requirements for inference-time compute. **Discriminative PRM SOTA and frontier-hard collapse:** Qwen2.5-Math-PRM-7B achieves 66.3 F1 on OmniMATH and 67.5 on OlympiadBench; Qwen2.5-Math-PRM-72B achieves 71.1 and 74.3 respectively (reported in R-PRM EMNLP 2025 Table 1 and 'Is PRM Necessary?' arXiv 2505.11227 Table 1). Note: these are distinct from the weaker Qwen2.5-Math-7B-PRM800K (44.3 OmniMATH, 50.7 OlympiadBench) — a 22-point gap demonstrating that training data quality is decisive. Critically, Hard2Verify (arXiv 2510.13744) reveals catastrophic degradation at the true frontier: Qwen2.5-Math-PRM-72B drops from 78.3 F1 on ProcessBench to 37.3 on Hard2Verify's 80 IMO/Putnam-level problems (1,860 annotated steps) — a 41-point collapse. All tested PRMs score below 65.82% on step-level tasks. 'State-of-the-art PRMs struggle immensely on Hard2Verify, performing significantly below random guess performance in error identification.' This collapse directly motivates improving MC annotation quality on hard problems. **Data-efficient discriminative PRM training:** ActPRM (arXiv 2504.10559, COLM 2025) applies active learning to PRM training: an ensemble of ~32 classification heads on a shared Qwen2.5-Math-7B-Instruct backbone estimates per-step aleatoric uncertainty (max(μ(P), 1−μ(P)) < δ_pred=0.95) and epistemic uncertainty (σ(P) > δ_std=0.005), retaining only uncertain steps for annotation by QwQ-32B judge. Achieves 67.0 F1 on OmniMATH, 71.4 on OlympiadBench, 75.0 avg F1 on ProcessBench, and 65.5% on PRMBench (matching GPT-4o) — the current strongest 7B discriminative PRM — with only 20% of UniversalPRM's annotation budget (6% of Qwen2.5-Math-PRM-7B's). Also demonstrates downstream utility: filtering 1M+ trajectories to 60% yields further SOTA training data. Key limitation: optimizes which steps to annotate (data selection) but uses standard MC estimation for the annotations themselves, leaving the early-step cold-start problem unaddressed on frontier-hard problems. No Hard2Verify results reported. Critically, ActPRM does not report the positional distribution of selected uncertain steps — whether they cluster at early, middle, or late positions — creating an empirical gap that Phase 0 must characterize. The orthogonality of data selection (ActPRM) and data quality (RCB) suggests their composition could yield multiplicative gains, but anti-complementarity is also possible (see failure mode F7). **Rollout-free label generation:** CPMI (arXiv 2604.10660; confirmed accepted at ACL 2026 Main Conference) uses contrastive pointwise mutual information with Qwen3-8B-Base as the labeling model and Qwen3-4B-Base as the PRM training backbone to generate step-level reward labels without MC rollouts, reducing annotation time by 84%. However, CPMI-trained PRMs achieve only 25.6 F1 on ProcessBench OmniMATH — the authors explicitly exclude extremely difficult problems. **Adaptive MC estimation:** AMCS (arXiv 2509.24351; withdrawn from ICLR 2026) adaptively allocates rollout samples per-step based on Wilson score interval uncertainty, allocating ~20 rollouts to uncertain steps (μ∈[0.4,0.6]) vs ~7 for confident steps. Trains Qwen2.5-Math-7B-PRM-AMCS on MathSearch-200K, achieving 76.2% accuracy on MATH500 with GLM-4-9B. Key limitation: treats all step positions symmetrically — does not analyze or exploit position-dependent success rate gradients. No ProcessBench F1 results reported. **Generative PRM cost analysis:** Setlur et al. (2025) show GenRM-FT requires 8× compute to match self-consistency, up to 128× for a 3.8% accuracy gain (Figure 1b, Llama-3.1-8B; higher multipliers reported for other models in Appendix F). **MC estimation improvements:** ComMCS (AAAI 2026) reduces MC estimator variance via compounding estimates across adjacent step positions (TD(λ)-style) without extra inference, gaining +2.8 best-of-N points. Theorem 4.2 establishes MC estimation as the MVUE given single-step information. SCAN (NeurIPS 2025) addresses MC annotation noise via self-denoising. Math-Shepherd (ACL 2024) and OmegaPRM (arXiv 2024) established MC-based PRM annotation but flag the cold-start problem without solution. **Reward model distillation:** RM-Distiller (arXiv 2601.14032, 2026) systematically distills from generative LLMs to discriminative reward models via refinement, scoring, and generation capabilities. The reverse direction — discriminative PRM to generative PRM distillation — remains unexplored. **Fast PRM motivation:** Fast-Slow Thinking RM (arXiv 2603.20212, 2026) proposes hybrid scalar/generative RM. PRIME (arXiv 2502.01456, 2025) derives implicit process rewards, achieving 2.5× faster training. SPRO (arXiv 2507.01551, 2025) achieves 3.4× higher training efficiency. **Frontier-hard verification benchmarks:** Hard2Verify (arXiv 2510.13744, 2025) provides 80 frontier Olympiad problems with 1,860 human-annotated steps; the best open-source model (DeepSeek-R1) achieves 68.92% step-level accuracy; GPT-5 leads at 86.53%. **Co-evolutionary and curriculum approaches:** RL Tango (NeurIPS 2025) co-evolves generator and generative verifier. SCRL (arXiv 2605.22074, 2026) decomposes hard problems into verifiable subproblems. R³ (ICML 2024) applies reverse curriculum RL for policy training. AURORA (arXiv 2025) uses reverse verification. **Gap:** No existing work (a) empirically characterizes domain-dependent step correlation structure across mathematical reasoning domains with quantitative per-domain indices, (b) provides formal conditions for MC informativeness as a function of step position with domain-specific dependency corrections, (c) proposes a step-position-aware reverse curriculum for PRM training, (d) combines position-aware curriculum with adaptive per-step rollout allocation, (e) produces efficient discriminative PRMs that resist Hard2Verify-level collapse, (f) tests discriminative-to-generative PRM distillation, or (g) explicitly addresses the anti-complementarity risk in composing data selection efficiency (ActPRM-style) with annotation quality improvement (RCB-style).",
  "inspired_by": "Field gap: process supervision for problems at or beyond the model's capability frontier, where MC estimation produces degenerate near-zero-variance estimates, probability-based methods (CPMI) produce uncalibrated scores, and current discriminative PRMs collapse catastrophically (78.3→37.3 F1 on Hard2Verify). Foundational discovery: we observe that mathematical reasoning exhibits fundamentally different step correlation structures across domains — the first systematic empirical characterization of this phenomenon. We formalize this via the dependency index δ_d = 1 − corr(empirical μ_k, predicted p^{K−k}), which quantifies per-domain independence violation. Near-independent domains (δ_d < 0.2: multi-step algebraic computation, sequential equation solving, coordinate geometry) exhibit smooth, predictable informativeness decay consistent with the Markov chain model; strongly dependent domains (δ_d > 0.5: insight-dependent proofs, combinatorial constructions, auxiliary-line geometry) show abrupt transitions where a single gateway step determines all subsequent viability. This structural discovery enables everything that follows: it determines where the independence idealization holds (and Theorem 1 applies tightly) vs. where it breaks down (and conservative bounds with δ_d-calibrated corrections are needed). It connects to Conditional Reward Modeling (arXiv 2509.26578) which formalizes inter-step dependencies via conditional probability chains, to 'What Are Step-Level Reward Models Rewarding?' (AAAI 2025) which empirically demonstrates that context-aware step evaluation outperforms context-free variants, and to 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) which independently confirms from representation geometry that late steps are ~24 AUC points more predictive of correctness than early steps. Our δ_d estimates provide the systematic per-domain empirical calibration that all three frameworks lack. Theoretical foundation: elementary Markov chain completion probability — the MC success rate from step k in a K-step solution is approximately p^{K-k} under an independent-step model, giving an exponential gradient that is sharper for harder problems. The key theoretical contribution is formalizing this into sufficient conditions (Theorem 1) under the independence idealization, with δ_d-calibrated corrections providing domain-aware bounds. Methodological innovation: (1) the AMCS-RCB combination addresses a 2D resource allocation problem (which steps to annotate × how many rollouts per step) that neither approach solves alone — AMCS (adaptive budget via Wilson score uncertainty) is orthogonal to RCB (curriculum over step positions via success rate gradient); (2) the ActPRM+RCB composition addresses a second orthogonal dimension — which steps to annotate (ActPRM's uncertainty-based selection) vs. how to annotate them (RCB's quality-improving curriculum) — but with an important caveat: if ActPRM's uncertain steps cluster at early positions where MC estimates are uninformative, the composition may produce anti-complementarity rather than multiplicative gains (failure mode F7); Phase 0 explicitly diagnoses this by analyzing ActPRM's step selection distribution across positions; (3) the discriminative-to-generative distillation pipeline reverses the typical RM-Distiller direction, using RCB-trained discriminative PRMs as cheap labelers to generate massive training data for generative PRMs — novel because discriminative PRMs produce labels at ~1000× lower cost per step than generative PRMs. Deployment motivation: the well-documented need for efficient discriminative PRMs in online RL training loops (GRPO/PPO), where generative PRMs are prohibitively expensive (Setlur et al. 2025; Fast-Slow Thinking RM 2026; PRIME and SPRO workarounds). Broader impact: the consistent 27-41 F1 gap between unsupervised/rollout-free methods and supervised MC-based PRMs on OmniMATH, plus the Hard2Verify collapse, demonstrate that annotation quality is the decisive bottleneck. Complementarity: CPMI-trained PRM for moderate-difficulty problems (cheapest), AMCS-RCB-trained discriminative PRM for frontier-hard RL training, generative PRM (optionally distillation-enhanced) for high-stakes test-time verification.",
  "approach": "We propose Reverse-Curriculum Bootstrapping (RCB), a theoretically grounded annotation and training framework. The narrative arc is: discover structure (Contribution I) → formalize (Contribution II) → build methods (Contributions III-IV) → evaluate and deploy (Contribution V). **Contribution I — Empirical Discovery: Domain-Dependent Reasoning Step Correlation Structure (weeks 1-3, Phase 0).** This is the paper's most novel and independently valuable contribution. We provide the first systematic empirical characterization of how mathematical reasoning step correlations vary across domains. For each of the 7 primary Omni-MATH domains (Algebra, Precalculus, Calculus, Geometry, Discrete Mathematics, Number Theory, Applied Mathematics) and ≥10 of 33+ sub-domains: (a) Select 50+ problems per domain/sub-domain spanning difficulty levels. (b) Generate 8-12-step candidate solutions using Qwen3-32B. (c) Run N=64 MC rollouts from each step position k using Qwen3-32B as completer. (d) Measure success rate as a function of normalized step position (k/K), stratified by problem difficulty and mathematical domain. (e) Compute the dependency index δ_d = 1 − corr(empirical μ_k, predicted p_min^{K−k}) for each domain d, where p_min is the estimated per-step correctness probability. When δ_d ≈ 0, independence holds and the exponential gradient is fully exploitable; when δ_d is large, inter-step correlations attenuate the gradient. (f) Classify domains into tiers: near-independent (δ_d < 0.2), moderately dependent (0.2 ≤ δ_d < 0.5), strongly dependent (δ_d ≥ 0.5). (g) Compute bootstrap confidence intervals (95% CI) for all δ_d estimates to establish statistical significance. Target: δ_d classification accuracy ≥85% — the domain classification into near-independent/moderately-dependent/strongly-dependent should be robust across different problem samples from the same domain. (h) Test the mixture model: for strongly-dependent domains, fit the two-class mixture model where fraction α of problems have a 'gateway step' (p_gateway << p_other) and the rest are near-independent. Estimate α per domain. (i) Anti-complementarity diagnostic for ActPRM+RCB composition: reproduce ActPRM's ensemble uncertainty estimation on the same problem set and analyze whether ActPRM's selected uncertain steps correlate with step position. Specifically, test whether ensemble uncertainty is highest at early positions where MC estimates are uninformative — if so, this indicates the selection-quality tension described in failure mode F7. The δ_d characterization constitutes a standalone contribution regardless of RCB's effectiveness: it is the first empirical study connecting reasoning step correlation structure to mathematical domain properties, extending the geometric trajectory analysis of 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) — which shows late steps are ~24 AUC points more predictive of correctness — with domain-level structural decomposition. It also complements EvalQReason's (arXiv 2602.02295, 2026) Consecutive Step Divergence metric by providing a global positional characterization rather than local pairwise coherence. Concrete domain predictions based on mathematical structure: (i) Near-independence domains: multi-step algebraic computation (each step is a mechanistic transformation — e.g., polynomial expansion, equation manipulation — where correctness depends primarily on local arithmetic accuracy), sequential equation solving (substitution chains where each step's validity depends mainly on correctly applying the substitution), and coordinate geometry with computational steps (once the coordinate system is established, each computation is largely independent). For these domains, Theorem 1 provides tight predictions and RCB's exponential gradient is fully exploitable. (ii) Strong-dependency domains: insight-dependent proofs (choosing the right lemma or proof technique at step 1 — e.g., applying Vieta's formulas vs. direct computation for a symmetric polynomial problem — determines the viability of all subsequent steps, creating a single 'gateway' step with near-binary influence), combinatorial arguments requiring a key construction (e.g., finding the right bijection or invariant), and geometry problems requiring auxiliary constructions (e.g., drawing the right auxiliary line in a Euclidean geometry proof). In these domains, the step-1 choice creates strong correlations: p_1 effectively gates all subsequent p_j, violating the product factorization μ_k = ∏p_j. Total Phase 0 cost: ~300 H100-hours. Go/no-go criteria (domain-stratified): (i) Full-go: for ≥40% of frontier-hard problems (pass@1 < 5%), late-step rollouts (k/K > 0.8) achieve success rates ≥10%, AND δ_d shows meaningful variation across domains (range ≥ 0.3); (ii) Partial-go: 20-40% meet criterion (i), proceed with RCB restricted to qualifying domains (those with δ_d < 0.5); (iii) No-go: <20% qualify, pivot to AMCS-enhanced compounding estimators combined with difficulty curriculum, but still publish the δ_d characterization as a standalone contribution. **Contribution II — Theoretical Framework with Domain-Aware Corrections (weeks 1-2, concurrent with Phase 0):** We formalize the position-dependent MC informativeness under an independent-step Markov model, with corrections calibrated by the empirical δ_d values from Contribution I. Definition: an MC estimate at step k with N rollouts is c-informative if E[successes] = N·μ_k ≥ c, where μ_k = ∏_{j=k}^{K} p_j is the completion success rate. Proposition 1 (Monotonicity): μ_k ≤ μ_{k+1} for all k — informativeness is non-decreasing with step position. This holds regardless of the independence assumption since later steps are strictly closer to completion. Proposition 2 (Exponential Gradient): if per-step correctness p_j ∈ [p_min, p_max], then μ_k ∈ [p_min^{K-k}, p_max^{K-k}], giving approximately exponential growth toward later steps on hard problems. Theorem 1 (RCB Sufficient Condition, under independence idealization with δ_d-calibrated corrections): RCB produces strictly more informative annotations than uniform MC estimation whenever K > log(c/N)/log(p_min), with the earliest informative step at k* = K − ⌊log(c/N)/log(p_min)⌋. For domains with δ_d > 0, Theorem 1's bound is conservative by factor ~(1 − α_d) where α_d is the estimated gateway fraction from the mixture model. Corollary (Difficulty Threshold): RCB is beneficial when problem difficulty exceeds 1 − (c/N)^{1/K}. Updated framing: Theorem 1 provides 'sufficient conditions under the independence idealization, with empirically-calibrated corrections for domain-specific dependency structures characterized by δ_d.' The theoretical framework connects to ComMCS's compound variance formula (Theorem 4.3) by showing that RCB's position-aware annotation focuses variance reduction where it matters most. Under a simplified two-class mixture model where a fraction α of problems have a 'gateway step' (p_gateway << p_other) and the rest are near-independent, the effective success rate curve becomes: μ_k = α · p_gateway · p_other^{K-k-1} + (1-α) · p_other^{K-k}. The exponential gradient is preserved (dominated by the second term for moderate α) but attenuated in magnitude. **Contribution III — RCB Curriculum (weeks 4-14):** Enabled by the structural discovery (Contribution I) and theoretical framework (Contribution II). Phase 1 (weeks 4-6): Run MC rollouts from late step positions (k/K > 0.75) where the pilot confirmed non-trivial success rates, using Qwen3-235B-A22B as completer. Train PRM_0 (Qwen3-7B base). Domain-aware curriculum: for near-independent domains (δ_d < 0.2), extend the curriculum aggressively (5 phases); for strongly dependent domains (δ_d ≥ 0.5), use a conservative curriculum (2-3 phases) that terminates earlier. Phases 2-5 (weeks 6-14): Each phase i uses PRM_{i-1} to guide rollouts at progressively earlier step windows via best-of-16 selection. Early termination: if PRM-guided rollouts do not achieve ≥2pp higher success rate than unguided. **Contribution IV — AMCS-RCB Combined Method and ActPRM+RCB Composition (weeks 4-14, parallel variants):** AMCS-RCB: Within each RCB phase, replace the fixed rollout budget (N=64) with AMCS-style adaptive allocation: use Wilson score interval to allocate k_init=6 to k_max=32 rollouts per step based on estimation uncertainty. This addresses the 2D resource allocation problem: RCB determines *which steps to annotate* (step position curriculum), AMCS determines *how many rollouts per step* (uncertainty-adaptive budget). Theoretical connection: Theorem 1 determines the informative step range; AMCS optimizes rollout allocation within that range. Expected benefit: 20-30% compute reduction with equivalent or better label quality. ActPRM+RCB composition ablation: Replace uniform step selection with ActPRM's ensemble uncertainty-based selection within the RCB curriculum. Three sub-conditions: (i) Naive composition: ActPRM selects steps, RCB provides MC estimates — tests raw complementarity; (ii) Hybrid composition: ActPRM selects steps only from within the RCB-determined informative window (k ≥ k*), combining quality-aware selection with quality-aware annotation — mitigates the anti-complementarity risk; (iii) Comparison: measure whether ActPRM's uncertain steps disproportionately fall inside vs. outside the informative window, directly testing the F7 failure mode hypothesis. (+100 H100-hours for this ablation.) **Contribution V — Dual-Track Evaluation and Distillation Pipeline:** Track A (discriminative, weeks 4-16): Train 7B discriminative PRM via RCB and AMCS-RCB curricula. Evaluate on ProcessBench (OmniMATH, OlympiadBench), Hard2Verify, PRMBench, and best-of-N accuracy on Omni-MATH hard-filtered and AIME 2025/2026 hardest problems. Track B (dependency characterization + generative + distillation, weeks 12-18): (B1) Primary deliverable — Complete δ_d characterization: publish δ_d values with bootstrap 95% CIs across all 7 primary Omni-MATH domains AND ≥10 of 33+ sub-domains. Include δ_d classification robustness analysis (target: ≥85% accuracy on held-out problem samples). Analyze relationship between δ_d and problem structural features (proof vs. computation, number of key insights, solution path diversity). Connect findings to Conditional Reward Modeling (arXiv 2509.26578) and provide systematic empirical calibration for their conditional probability framework. (B2) Multi-architecture fine-tuning: fine-tune GenPRM, ThinkPRM, and R-PRM architectures on RCB-annotated data vs. standard MC annotations from the same problems, testing whether annotation quality is a paradigm-wide bottleneck across generative PRM architectures. (B3) Novel discriminative-to-generative distillation pipeline: use the RCB-trained discriminative PRM (fast, single forward pass per step) to generate step-level correctness labels on a large corpus of solution traces (100K+ traces), then use these cheap labels to fine-tune generative PRMs. This reverses the typical RM-Distiller direction (generative→discriminative) and exploits the ~1000× cost advantage of discriminative inference. (B4) Hard2Verify generative evaluation: evaluate RCB-fine-tuned generative PRMs on Hard2Verify. **Ablations (weeks 14-17):** (1) RCB vs. uniform MC estimation; (2) RCB vs. stronger completer only (Qwen3-235B with higher rollout budget); (3) AMCS-RCB vs. pure AMCS vs. pure RCB — the key Contribution IV comparison; (4) CPMI labels vs. RCB MC labels at matched difficulty, testing complementarity; (5) Inference speed comparison: wall-clock time per evaluation for RCB discriminative PRM vs. GenPRM, ThinkPRM, RM-R1, for a representative GRPO scenario (1,000 prompts × 16 rollouts × 20 steps = 320,000 evaluations per epoch); (6) Distillation efficiency: compare generative PRM trained on discriminative-PRM labels vs. same model trained on MC labels vs. same model trained on RCB-MC labels, at matched data scale; (7) ActPRM+RCB composition: naive vs. hybrid vs. ActPRM-only vs. RCB-only (as described in Contribution IV above); (8) Domain-stratified RCB: run RCB separately on near-independence vs. strong-dependency domains (as classified by δ_d from Phase 0) to test whether the curriculum adapts naturally to different correlation structures, and whether restricting to near-independent domains yields disproportionate gains. **Evaluation (weeks 17-19):** Track A targets — ProcessBench OmniMATH: improve 7B discriminative PRM F1 from 67.0 baseline (ActPRM, current strongest 7B) to 72-76 F1, approaching ThinkPRM-7B (74.0 F1) without generative overhead; OlympiadBench: 74-78 F1 vs. 71.4 ActPRM baseline; Hard2Verify: target ≥50 F1 (from 37.3 baseline for 72B model — demonstrating that RCB-trained 7B PRM resists catastrophic frontier-hard collapse). Track B targets — Primary: δ_d characterization across all 7 Omni-MATH domains + ≥10 sub-domains with bootstrap CIs, δ_d classification accuracy ≥85%. Secondary: ProcessBench OmniMATH for RCB-fine-tuned generative PRMs: ≥3 F1 improvement on Hard2Verify, ≥2 F1 on ProcessBench OmniMATH across at least 2 of 3 tested architectures; distillation pipeline: achieve ≥90% of MC-trained generative PRM accuracy with 10× less labeling compute, demonstrating discriminative-to-generative knowledge transfer. **Failure mode analysis:** (F1) Pilot invalidation — theoretical gradient insufficient, with partial-go and no-go pathways (no-go still publishes δ_d characterization as standalone contribution); (F2) Bootstrap cascade failure — caught by early termination criterion; (F3) Key-insight ceiling — problems where single critical insight determines correctness at all subsequent steps, quantified by high δ_d values and handled by domain-stratified analysis and the mixture model framework; (F4) AMCS-RCB overhead — if adaptive allocation overhead exceeds compute savings, pure RCB may dominate; (F5) Track B null result — if annotation quality does not improve generative PRMs, this is an informative negative result (generative PRMs learn via reasoning rather than training data quality), and Track A + distillation pipeline + theoretical contribution + dependency characterization remain primary; (F6) Independence violation too severe — if δ_d > 0.5 for most domains, the exponential gradient is too attenuated for RCB to substantially outperform simple late-step-only training; however, the partial-go pathway (restricting to near-independent domains) and the dependency characterization itself remain valuable standalone contributions; (F7) ActPRM+RCB anti-complementarity — if ActPRM's ensemble uncertainty correlates positively with step position (i.e., uncertain steps cluster at early positions where MC estimates are uninformative), the naive composition produces tension rather than multiplicative gains. Phase 0 explicitly tests this by analyzing ActPRM's step selection distribution across positions. Mitigation: if anti-complementarity is confirmed, use the hybrid strategy where ActPRM selects steps from the RCB-determined informative window (k ≥ k*), combining quality-aware selection with quality-aware annotation. If neither naive nor hybrid composition outperforms the individual methods, this is itself an informative finding about the interaction structure of data selection and data quality optimization. **Practical deployment framework (three-tier):** CPMI-trained PRM for moderate-difficulty problems (cheapest), AMCS-RCB-trained discriminative PRM for frontier-hard RL training, generative PRM (optionally distillation-enhanced) for high-stakes test-time verification.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "7200 H100-hours (300 for Phase 0 including completer evaluation + MC pilot + AMCS baseline + CPMI comparison + ActPRM baseline reproduction + dependency index computation across 7 domains and ≥10 sub-domains, 3200 for MC rollout generation across Phases 1-5, 1200 for iterative discriminative PRM fine-tuning, 400 for AMCS-RCB parallel track, 1000 for Track B multi-architecture generative PRM fine-tuning + distillation pipeline, 600 for ablations including ActPRM+RCB composition (naive + hybrid) and domain-stratified RCB, 500 for evaluation including Hard2Verify benchmarking and inference speed measurement)",
      "timeline": "18-19 weeks (2 weeks theoretical framework + Phase 0 pilot concurrent, 1 week go/no-go + curation, 10 weeks for 5 RCB phases with AMCS-RCB parallel, 4 weeks Track B parallel from week 12, 2 weeks ablations, 1-2 weeks evaluation/writing)",
      "estimated_gpu_cost": "$20,520 (at ~$2.85/H100-hour)"
    },
    "human_in_loop": {
      "gpu_hours": "6300 H100-hours (efficiency gains from Claude-assisted theoretical analysis, pilot data fitting, dependency index computation, automated hyperparameter tuning, and ablation design reducing wasted runs by ~13%)",
      "timeline": "15-16 weeks (Claude accelerates theoretical framework development, dependency analysis, pilot analysis, Phase 0 model fitting, experiment scripting, and paper drafting, saving ~3 weeks; fits estimated ICLR 2027 deadline starting June 1)",
      "claude_api_cost": "$1,300 (Sonnet 4.6 for code generation, theoretical proof verification, dependency characterization analysis, pilot data analysis, experiment orchestration, Track B design, and paper drafting; ~300M input + 65M output tokens)",
      "estimated_gpu_cost": "$17,955"
    },
    "auto_research": {
      "gpu_hours": "8300 H100-hours (additional compute for AMCS-RCB hyperparameter sweeps, ActPRM+RCB composition search including naive vs. hybrid variants, multi-architecture Track B fine-tuning, distillation pipeline optimization, systematic ablation execution, dependency model validation across all 7+10 domains/sub-domains, and domain-stratified analysis)",
      "timeline": "11-12 weeks (fully automated pipeline with parallel RCB + AMCS-RCB tracks and parallel Track B; pilot phase still requires ~2.5 weeks for sequential completer evaluation + analysis)",
      "claude_api_cost": "$4,400 (heavy Opus 4.7 usage for autonomous experiment design, theoretical framework development, dependency characterization, pilot go/no-go analysis, AMCS-RCB integration, ActPRM+RCB composition, distillation pipeline design, and adaptive protocol modification; ~470M input + 130M output tokens)",
      "estimated_gpu_cost": "$23,655",
      "speed_bottleneck": "MC rollout generation with Qwen3-235B-A22B completer requires multi-node inference; RCB phases are inherently sequential; AMCS-RCB runs in parallel with pure RCB track; Track B independent from week 12. Distillation pipeline requires completed Track A discriminative PRM. ActPRM baseline reproduction and dependency analysis parallelizable with Phase 0. δ_d characterization across all 7+10 domains/sub-domains requires comprehensive Phase 0 coverage but is parallelizable across domains."
    }
  },
  "target_venues": [
    "ICLR 2027 (estimated deadline: ~September 2026, projected from ICLR 2026 schedule; not officially announced as of May 2026) — primary target, 15-16 week human-in-loop timeline fits starting June 1",
    "AISTATS 2027 (estimated deadline: October 2026) — backup if additional time needed",
    "ICML 2027 (full paper estimated: ~January 2027) — comfortable deadline for full manual timeline"
  ],
  "level": "top-tier",
  "key_references": [
    "Let's Verify Step by Step (ICLR 2024)",
    "Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations (ACL 2024)",
    "Improve Mathematical Reasoning in Language Models by Automated Process Supervision [OmegaPRM] (arXiv 2024)",
    "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (ICLR 2025)",
    "rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking (ICML 2025)",
    "Training Large Language Models for Reasoning through Reverse Curriculum Reinforcement Learning [R3] (ICML 2024)",
    "SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning (NeurIPS 2025)",
    "Process Reward Models That Think [ThinkPRM] (TMLR 2026; arXiv 2504.16828)",
    "The Lessons of Developing Process Reward Models in Mathematical Reasoning (ACL Findings 2025)",
    "ProcessBench: Identifying Process Errors in Mathematical Reasoning (ACL 2025)",
    "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026)",
    "R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025)",
    "Dyve: Thinking Fast and Slow for Dynamic Process Verification (EMNLP 2025)",
    "RM-R1: Reward Modeling as Reasoning (ICLR 2026)",
    "SCRL: From Reasoning Chains to Verifiable Subproblems — Curriculum RL Enables Credit Assignment for LLM Reasoning (arXiv 2605.22074, 2026)",
    "ComMCS: Improving Value-based Process Verifier via Low-Cost Variance Reduction (AAAI 2026)",
    "Omni-MATH: A Universal Olympiad Level Mathematic Benchmark For Large Language Models (ICLR 2025)",
    "AURORA: Automated Process Reward Model Training via Reverse Verification (arXiv 2025)",
    "RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning (NeurIPS 2025)",
    "Unsupervised Process Reward Models [uPRM] (arXiv 2605.10158, 2026)",
    "Fast-Slow Thinking RM: Efficient Integration of Scalar and Generative Reward Models (arXiv 2603.20212, 2026)",
    "PRIME: Process Reinforcement through Implicit Rewards (arXiv 2502.01456, 2025)",
    "Is PRM Necessary? Problem-Solving RL Implicitly Induces PRM Capability in LLMs (arXiv 2505.11227, 2025)",
    "When To Solve, When To Verify: Compute-Optimal Problem Solving and Verification (Setlur et al., arXiv 2504.01005, 2025)",
    "Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems (arXiv 2026)",
    "Efficient Process Reward Modeling via Contrastive Mutual Information [CPMI] (arXiv 2604.10660; confirmed accepted at ACL 2026 Main Conference)",
    "From Static to Dynamic: Adaptive Monte Carlo Search for Mathematical Process Supervision [AMCS] (arXiv 2509.24351, 2025)",
    "Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (arXiv 2510.13744, 2025)",
    "RM-Distiller: Exploiting Generative LLM for Reward Model Distillation (arXiv 2601.14032, 2026)",
    "SPRO: Self-Guided Process Reward Optimization with Redefined Step-wise Advantage (arXiv 2507.01551, 2025)",
    "Efficient Process Reward Model Training via Active Learning [ActPRM] (arXiv 2504.10559, COLM 2025)",
    "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning (arXiv 2509.26578, 2025)",
    "What Are Step-Level Reward Models Rewarding? Counterintuitive Findings from MCTS-Boosted Mathematical Reasoning (AAAI 2025)",
    "LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals (arXiv 2604.05655, 2026)",
    "EvalQReason: A Framework for Step-Level Reasoning Evaluation in Large Language Models (arXiv 2602.02295, 2026)"
  ],
  "description": "This project addresses the Monte Carlo cold-start problem in process reward model training through five integrated contributions, reframed to lead with the paper's most novel discovery: (I) the first systematic empirical characterization of domain-dependent reasoning step correlation structure across mathematical domains via the dependency index δ_d = 1 − corr(empirical μ_k, predicted p^{K−k}), (II) a theoretical framework formalizing MC estimation informativeness as a function of step position under an independence idealization with δ_d-calibrated corrections, (III) a reverse-curriculum bootstrapping (RCB) annotation algorithm enabled by the structural discovery, (IV) a combined AMCS-RCB method integrating adaptive per-step rollout allocation with position-aware curriculum, and (V) dual-track evaluation with a novel discriminative-to-generative PRM distillation pipeline. The narrative arc: we discover that mathematical reasoning exhibits fundamentally different step correlation structures across domains — from near-independent (algebraic computation: δ_d < 0.2) to strongly dependent (insight-dependent proofs: δ_d > 0.5) — and this structural discovery enables domain-aware annotation strategies that were previously impossible. Independent geometric evidence from 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) confirms the positional informativeness gradient: late reasoning steps are ~24 AUC points more predictive of correctness than early steps (0.87 vs 0.63 AUC), with correct/incorrect trajectories diverging primarily at late stages in representation space. The severity of the problem is now quantified by Hard2Verify: Qwen2.5-Math-PRM-72B collapses from 78.3 F1 on ProcessBench to 37.3 on frontier-hard Olympiad problems — a catastrophic 41-point drop. While generative PRMs bypass MC estimation via inference-time reasoning (ThinkPRM-14B: 85.7 F1), they generate 1,000-5,000 tokens per step — infeasible for RL training (Setlur et al. 2025: GenRM needs 8× compute to match self-consistency, up to 128× for a 3.8% accuracy gain, Figure 1b). Rollout-free alternatives (CPMI at 25.6 F1 using Qwen3-8B-Base labeler/Qwen3-4B-Base PRM, confirmed accepted at ACL 2026 Main Conference; uPRM at 39.8 F1) consistently underperform supervised PRMs by 27-41 F1 points on hard problems. ActPRM (COLM 2025) achieves the current strongest 7B discriminative PRM performance (67.0 F1 OmniMATH, 75.0 avg F1 ProcessBench) via active learning-based step selection with only 20% of UniversalPRM's annotation budget, but optimizes data selection without addressing MC estimation quality — the step selection and annotation quality dimensions are orthogonal, with a potential anti-complementarity tension when composed with RCB (failure mode F7: if ActPRM's uncertain steps cluster at early positions where MC estimates are uninformative, the composition produces tension rather than multiplicative gains; Phase 0 explicitly diagnoses this, with a hybrid mitigation constraining ActPRM selection to the RCB-determined informative window). AMCS (arXiv 2509.24351) adaptively allocates rollout budget per-step via Wilson score interval uncertainty but treats all step positions symmetrically and does not address the fundamental uninformativeness of early-step MC estimates on hard problems. **Contribution I** provides the δ_d dependency index across all 7 primary Omni-MATH domains (Algebra, Precalculus, Calculus, Geometry, Discrete Mathematics, Number Theory, Applied Mathematics) and ≥10 of 33+ sub-domains, with bootstrap confidence intervals and ≥85% classification robustness target — the first systematic domain-level quantification of step independence violation, complementing the theoretical frameworks of Conditional Reward Modeling (arXiv 2509.26578) and the empirical findings of 'What Are Step-Level Reward Models Rewarding?' (AAAI 2025) with systematic per-domain calibration that both lack. **Contribution II** formalizes the position-dependent MC gradient: under the independence idealization, the success rate from step k is approximately p^{K-k}, giving exponential growth toward later steps. Theorem 1 provides sufficient conditions for when RCB outperforms uniform MC: whenever K > log(c/N)/log(p_min), early steps are uninformative regardless of rollout budget. For domains with δ_d > 0, Theorem 1's bound is conservative by factor ~(1-α_d), but RCB remains beneficial because Proposition 1 (monotonicity of μ_k) holds regardless of independence. **Contribution III** (RCB) exploits the gradient with domain-aware curriculum depth: aggressive (5 phases) for near-independent domains, conservative (2-3 phases) for strongly dependent domains. **Contribution IV** (AMCS-RCB) combines position curriculum with adaptive rollout allocation — addressing the 2D resource optimization that neither method solves alone. **Contribution V** introduces dual-track evaluation separating annotation quality from model capability: Track A trains a 7B discriminative PRM targeting 72-76 F1 on ProcessBench OmniMATH (5-9 points over ActPRM's 67.0, current strongest 7B) and ≥50 F1 on Hard2Verify (vs. 37.3 baseline for 72B model); Track B's primary deliverable is the complete δ_d characterization with statistical significance tests, with secondary targets of ≥3 F1 improvement on Hard2Verify and ≥2 F1 on ProcessBench OmniMATH for generative PRMs, plus a discriminative-to-generative distillation pipeline targeting ≥90% of MC-trained accuracy with 10× less labeling compute. Note on ProcessBench baselines: Qwen2.5-Math-PRM-7B (66.3/67.5) is distinct from Qwen2.5-Math-7B-PRM800K (44.3/50.7) — the 22-point gap on OmniMATH demonstrates training data quality is decisive (reported in R-PRM EMNLP 2025 Table 1 and 'Is PRM Necessary?' 2505.11227 Table 1). Evaluation on three benchmarks (ProcessBench, Hard2Verify, best-of-N), both paradigms (discriminative + generative), and the three-tier deployment framework: CPMI for moderate problems, AMCS-RCB discriminative PRM for frontier-hard RL training, generative PRM for high-stakes verification.",
  "project_name": "reverse_curr_prm_bootstrap",
  "source": "web_research",
  "title": "Reverse-Curriculum Bootstrapping for Process Verification at the Capability Frontier"
}

## Reviewer feedback (round 7)
Issues: ["Missing SIA (arXiv 2604.06192, April 2026): 'The Stepwise Informativeness Assumption' directly formalizes that reasoning prefixes accumulate answer-relevant information monotonically — essentially the theoretical foundation underlying Proposition 1. It treats this as a universal property; the proposal's domain-dependent δ_d variation is complementary. SIA MUST be cited and differentiated from, and could actually strengthen the proposal by positioning δ_d as empirical calibration of SIA's theoretical framework.", "Missing SHAPE (arXiv 2604.06636, April 2026): 'Stage-aware Hierarchical Advantage via Potential Estimation' proposes position/stage-dependent credit assignment for reasoning, achieving 3% accuracy gains. While methodologically distinct (RL credit assignment vs. MC annotation quality), the thematic overlap with 'step position determines informativeness' requires citation and differentiation.", "Missing MCNIG (arXiv 2603.17815, March 2026): 'Process Supervision via Monte Carlo Net Information Gain' proposes an information-theoretic alternative to standard MC estimation with O(N) complexity. Directly relevant as an alternative approach to improving MC-based process supervision.", "LLM Reasoning as Trajectories AUC claim slightly misleading: The proposal states '~24 AUC points (0.87 vs 0.63)' but the paper's own comparison uses average late-step AUC of 0.83, not the peak single-layer 0.87. The honest comparison is ~20 AUC points (0.83 vs 0.63). Stating 0.87 cherry-picks the best layer against the early-step average.", "Setlur et al. appendix reference error: The proposal says 'higher multipliers reported for other models in Appendix F' but the 512× for Qwen-2.5-7B-Instruct appears in Appendix H ('Trends Across Model Families'), not Appendix F ('Improving Verifier Efficiency')."]
Feedback: The round-7 revision successfully addresses all four round-6 issues: CPMI venue verified through arXiv self-declaration, F7 anti-complementarity failure mode added with hybrid mitigation, contributions reordered to lead with δ_d discovery, and Track B ambition substantially raised. The proposal's scholarly rigor is exceptional — all major numerical claims verified correctly through independent search. The average score (3.875) remains just below the 4.0 threshold, with impact (3.5) as the persistent drag. Three actionable items to cross the threshold:

(1) **Integrate SIA as theoretical support and differentiation target.** SIA (arXiv 2604.06192) formalizes step informativeness as a universal property of autoregressive models. This actually STRENGTHENS the proposal: cite SIA as providing the theoretical foundation for why position matters, then position δ_d as the first empirical test of whether SIA's universal claim holds uniformly across mathematical domains — or whether the informativeness accumulation rate is domain-dependent. This reframing elevates the δ_d contribution from 'empirical characterization' to 'empirical calibration and potential falsification of a recently-proposed theoretical framework.' If δ_d reveals domain-dependent variation, it demonstrates that SIA's universality is an oversimplification — a finding with broad theoretical implications.

(2) **Add SHAPE and MCNIG to landscape.** SHAPE (stage-aware credit assignment) should be differentiated as operating in the RL domain while your work addresses MC annotation quality. MCNIG (information-theoretic MC alternative) is a complementary approach that could serve as an additional baseline.

(3) **Fix two minor factual errors:** (a) Correct '~24 AUC points (0.87 vs 0.63)' to '~20 AUC points (0.83 average late-step vs 0.63 early-step AUC, with peak single-layer reaching 0.87)' — this is more honest and still supports the point. (b) Change 'Appendix F' to 'Appendix H' for the Setlur 512× reference.

The SIA integration is the key lever for crossing 4.0: it transforms the δ_d contribution from 'novel empirical measurement' to 'empirical test of a concurrent theoretical framework with domain-specific findings that have implications beyond PRM training.' This raises both novelty and impact.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.
- Address each issue specifically.

## 深度调研要求

不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。
2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。
3. **深度思考**：
   - 核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach？
4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。

## 针对 Review 意见的定向搜索

1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点
2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline
3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现
4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot

- You have full freedom: minor fix, major revision, or pivot.
- Include a "change_type" field: "minor", "major", or "pivot".
- Output a COMPLETE JSON object with ALL fields.

## 停滞提醒
经过 7 轮修订，近 3 轮平均分从 3.9 到 3.9，无明显改善。
考虑 major revision 或 pivot。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "e9d2f5a3-ea56-4626-9051-a90094abb326",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T04:55:01.972Z_

```json
{
  "parentUuid": "e9d2f5a3-ea56-4626-9051-a90094abb326",
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
  "uuid": "761d327f-d9de-4dc8-9db8-354a6e54ec9c",
  "timestamp": "2026-05-28T04:55:01.972Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T04:55:01.972Z_

```json
{
  "parentUuid": "761d327f-d9de-4dc8-9db8-354a6e54ec9c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c83ac5f4-b9ef-4206-9359-818e2f123fcc",
  "timestamp": "2026-05-28T04:55:01.972Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"change_summary\": \"Major narrative restructuring to lead with the strongest nove…",
  "leafUuid": "c83ac5f4-b9ef-4206-9359-818e2f123fcc",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise process reward model research based on theoretical framework feedback",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294"
}
```

---

### Assistant

_source line 8 · 2026-05-28T04:55:12.178Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully before diving into research. The key issues are:

1. **SIA (arXiv 2604.06192)** - "The Stepwise Informativeness Assumption" - needs citation and differentiation. Reviewer says this could STRENGTHEN the proposal by positioning δ_d as empirical calibration of SIA.

2. **SHAPE (arXiv 2604.06636)** - "Stage-aware Hierarchical Advantage via Potential Estimation" - needs citation and differentiation.

3. **MCNIG (arXiv 2603.17815)** - "Process Supervision via Monte Carlo Net Information Gain" - needs citation as alternative approach.


4. I need to correct the AUC claim for LLM reasoning trajectories from ~24 points down to ~20 points, and fix the Setlur et al. reference from Appendix F to Appendix H. The reviewer notes the score has plateaued around 3.875 with impact as the limiting factor, but the SIA integration could be the breakthrough—reframing δ_d as an empirical validation of a concurrent theoretical framework rather than just a measurement.

Given the seven rounds of stagnation, I'm wondering if a deeper restructuring is needed beyond incremental fixes. The SIA suggestion feels like it could be transformative rather than just another citation, so I should dive into these papers and understand how to position this properly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c83ac5f4-b9ef-4206-9359-818e2f123fcc",
  "isSidechain": false,
  "requestId": "req_011CbUNTeZUXB82aeWVPvXxp",
  "type": "assistant",
  "uuid": "06ebfbd0-0950-424a-a83c-5c91e2897a07",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuyM4xs1LtNcQxoiD4FJW9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17795,
      "cache_read_input_tokens": 11014,
      "output_tokens": 515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17795,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 515,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 17795,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17795
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

_source line 9 · 2026-05-28T04:55:12.391Z_

I'll research all three missing papers (SIA, SHAPE, MCNIG) thoroughly, then verify the factual corrections. Let me launch parallel research agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06ebfbd0-0950-424a-a83c-5c91e2897a07",
  "isSidechain": false,
  "requestId": "req_011CbUNTeZUXB82aeWVPvXxp",
  "type": "assistant",
  "uuid": "2e28b06e-2cb7-43b7-8548-716297805c9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuyM4xs1LtNcQxoiD4FJW9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17795,
      "cache_read_input_tokens": 11014,
      "output_tokens": 515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17795,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 515,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 17795,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17795
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

_source line 10 · 2026-05-28T04:55:12.608Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016qCTtEZ2qWUBcd6gtZ5m8b`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e28b06e-2cb7-43b7-8548-716297805c9e",
  "isSidechain": false,
  "requestId": "req_011CbUNTeZUXB82aeWVPvXxp",
  "type": "assistant",
  "uuid": "dd2f20c4-e0e5-4e1f-a65e-2bb1c5c9984c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuyM4xs1LtNcQxoiD4FJW9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17795,
      "cache_read_input_tokens": 11014,
      "output_tokens": 515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17795,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 515,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 17795,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17795
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

_source line 11 · 2026-05-28T04:55:12.616Z_

<details><summary>↩ Tool result · `toolu_016qCTtEZ2qWUBcd6gtZ5m8b`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "dd2f20c4-e0e5-4e1f-a65e-2bb1c5c9984c",
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "e765c683-446d-4820-93eb-6eccf8416934",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "dd2f20c4-e0e5-4e1f-a65e-2bb1c5c9984c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-28T04:55:15.570Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me research all three papers in parallel, plus verify the factual corrections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e765c683-446d-4820-93eb-6eccf8416934",
  "isSidechain": false,
  "requestId": "req_011CbUNUSZw5gbkRukcMyfda",
  "type": "assistant",
  "uuid": "28b629ec-2622-472c-a6c2-326e411ae357",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcAX5Y8cK8Hojt8oJZe7ba",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1534,
      "cache_read_input_tokens": 28809,
      "output_tokens": 694,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1534,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 694,
          "cache_read_input_tokens": 28809,
          "cache_creation_input_tokens": 1534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1534
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

_source line 13 · 2026-05-28T04:55:16.185Z_

Let me research all three missing papers and verify the factual claims in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28b629ec-2622-472c-a6c2-326e411ae357",
  "isSidechain": false,
  "requestId": "req_011CbUNUSZw5gbkRukcMyfda",
  "type": "assistant",
  "uuid": "c6300e41-63a6-4302-bd59-97b0675d1a6c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcAX5Y8cK8Hojt8oJZe7ba",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1534,
      "cache_read_input_tokens": 28809,
      "output_tokens": 694,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1534,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 694,
          "cache_read_input_tokens": 28809,
          "cache_creation_input_tokens": 1534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1534
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

_source line 14 · 2026-05-28T04:55:18.057Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01V4jKJMLAmCXhKTSqgxD25T`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.06192",
  "prompt": "Extract the full abstract, authors, title, key contributions, and main theoretical claims of this paper. What exactly is the \"Stepwise Informativeness Assumption\" (SIA)? How is it formalized? Does it claim universality across domains? What are the main theorems or propositions? What mathematical reasoning benchmarks are used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6300e41-63a6-4302-bd59-97b0675d1a6c",
  "isSidechain": false,
  "requestId": "req_011CbUNUSZw5gbkRukcMyfda",
  "type": "assistant",
  "uuid": "ce603114-3093-4a10-8a1f-5472d99f82cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcAX5Y8cK8Hojt8oJZe7ba",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1534,
      "cache_read_input_tokens": 28809,
      "output_tokens": 694,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1534,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 694,
          "cache_read_input_tokens": 28809,
          "cache_creation_input_tokens": 1534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1534
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

_source line 15 · 2026-05-28T04:55:19.965Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01P2n9kf1QShNwHg24uzkbSL`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.06636",
  "prompt": "Extract the full abstract, authors, title, key contributions, and main claims. What is SHAPE (Stage-aware Hierarchical Advantage via Potential Estimation)? How does it use position/stage-dependent credit assignment? What are the main results and accuracy gains? How does it relate to step position determining informativeness in reasoning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce603114-3093-4a10-8a1f-5472d99f82cf",
  "isSidechain": false,
  "requestId": "req_011CbUNUSZw5gbkRukcMyfda",
  "type": "assistant",
  "uuid": "587c0409-b4f7-4ceb-97ed-3de70636df65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcAX5Y8cK8Hojt8oJZe7ba",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1534,
      "cache_read_input_tokens": 28809,
      "output_tokens": 694,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1534,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 694,
          "cache_read_input_tokens": 28809,
          "cache_creation_input_tokens": 1534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1534
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

_source line 16 · 2026-05-28T04:55:21.837Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011fJmQiZGsgCGePUsitmDoo`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.17815",
  "prompt": "Extract the full abstract, authors, title, key contributions, and main claims. What is MCNIG (Monte Carlo Net Information Gain)? How does it improve on standard MC estimation for process supervision? What is the O(N) complexity claim? What benchmarks are used and what results are achieved? How does it compare to standard MC-based PRM training?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "587c0409-b4f7-4ceb-97ed-3de70636df65",
  "isSidechain": false,
  "requestId": "req_011CbUNUSZw5gbkRukcMyfda",
  "type": "assistant",
  "uuid": "90db1d7d-0f74-4c53-b225-4a14c425ad4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcAX5Y8cK8Hojt8oJZe7ba",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1534,
      "cache_read_input_tokens": 28809,
      "output_tokens": 694,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1534,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 694,
          "cache_read_input_tokens": 28809,
          "cache_creation_input_tokens": 1534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1534
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

_source line 17 · 2026-05-28T04:55:24.297Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Lf2PLCUh3xV5cA9WzDryZ9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.05655",
  "prompt": "Focus on the specific AUC numbers for late-step vs early-step correctness prediction. Is the average late-step AUC 0.83 or 0.87? Is 0.87 a peak single-layer result? What is the exact early-step AUC (0.63)? What is the honest average comparison? Report exact numbers from the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90db1d7d-0f74-4c53-b225-4a14c425ad4f",
  "isSidechain": false,
  "requestId": "req_011CbUNUSZw5gbkRukcMyfda",
  "type": "assistant",
  "uuid": "35b12325-8d50-4193-b515-5579280a9ab3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcAX5Y8cK8Hojt8oJZe7ba",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1534,
      "cache_read_input_tokens": 28809,
      "output_tokens": 694,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1534,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 694,
          "cache_read_input_tokens": 28809,
          "cache_creation_input_tokens": 1534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1534
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

_source line 18 · 2026-05-28T04:55:24.347Z_

<details><summary>↩ Tool result · `toolu_01V4jKJMLAmCXhKTSqgxD25T`</summary>

```text
# Paper Summary: The Stepwise Informativeness Assumption

## Title & Authors
**Title:** "The Stepwise Informativeness Assumption: Why are Entropy Dynamics and Reasoning Correlated in LLMs?"

**Authors:** Mar Gonzàlez I Català, Haitz Sáez de Ocáriz Borde, George D. Montañez, Pietro Liò

## Abstract
The paper addresses why internal entropy patterns align with answer correctness in language models. The researchers propose that this occurs because models "accumulate information about the true answer via answer-informative prefixes" during generation.

## The Stepwise Informativeness Assumption (SIA)

**Definition:** SIA posits that reasoning prefixes progressively gather answer-relevant information as generation unfolds, with this accumulation occurring in expectation across the generation process.

**Formalization:** The assumption naturally arises from maximum-likelihood training on human reasoning traces and is reinforced through standard fine-tuning and reinforcement learning approaches.

## Key Contributions

- Formalizes the intuition linking entropy dynamics to reasoning quality
- Derives observable signatures connecting conditional answer entropy to correctness
- Demonstrates SIA emerges from standard training procedures

## Empirical Scope

Rather than claiming universal applicability, testing targeted specific domains:
- **Benchmarks:** GSM8K, ARC, SVAMP (mathematics and reasoning tasks)
- **Models:** Gemma-2, LLaMA-3.2, Qwen-2.5, DeepSeek, Olmo variants

The study does not claim cross-domain universality but focuses on established reasoning benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce603114-3093-4a10-8a1f-5472d99f82cf",
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "0d7c50d3-de31-4268-adef-8a5fee7ad5bf",
  "toolUseResult": {
    "bytes": 47518,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: The Stepwise Informativeness Assumption\n\n## Title & Authors\n**Title:** \"The Stepwise Informativeness Assumption: Why are Entropy Dynamics and Reasoning Correlated in LLMs?\"\n\n**Authors:** Mar Gonzàlez I Català, Haitz Sáez de Ocáriz Borde, George D. Montañez, Pietro Liò\n\n## Abstract\nThe paper addresses why internal entropy patterns align with answer correctness in language models. The researchers propose that this occurs because models \"accumulate information about the true answer via answer-informative prefixes\" during generation.\n\n## The Stepwise Informativeness Assumption (SIA)\n\n**Definition:** SIA posits that reasoning prefixes progressively gather answer-relevant information as generation unfolds, with this accumulation occurring in expectation across the generation process.\n\n**Formalization:** The assumption naturally arises from maximum-likelihood training on human reasoning traces and is reinforced through standard fine-tuning and reinforcement learning approaches.\n\n## Key Contributions\n\n- Formalizes the intuition linking entropy dynamics to reasoning quality\n- Derives observable signatures connecting conditional answer entropy to correctness\n- Demonstrates SIA emerges from standard training procedures\n\n## Empirical Scope\n\nRather than claiming universal applicability, testing targeted specific domains:\n- **Benchmarks:** GSM8K, ARC, SVAMP (mathematics and reasoning tasks)\n- **Models:** Gemma-2, LLaMA-3.2, Qwen-2.5, DeepSeek, Olmo variants\n\nThe study does not claim cross-domain universality but focuses on established reasoning benchmarks.",
    "durationMs": 6285,
    "url": "https://arxiv.org/abs/2604.06192"
  },
  "sourceToolAssistantUUID": "ce603114-3093-4a10-8a1f-5472d99f82cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T04:55:25.140Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AtctKCBA4dbQwJGKgaXG7x`</summary>

```json
{
  "query": "Setlur et al. 2025 \"When To Solve When To Verify\" compute optimal verification appendix H Qwen 512x"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d7c50d3-de31-4268-adef-8a5fee7ad5bf",
  "isSidechain": false,
  "requestId": "req_011CbUNUSZw5gbkRukcMyfda",
  "type": "assistant",
  "uuid": "0c453811-ed1d-480e-b563-e74cdeeea5da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcAX5Y8cK8Hojt8oJZe7ba",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1534,
      "cache_read_input_tokens": 28809,
      "output_tokens": 694,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1534,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 694,
          "cache_read_input_tokens": 28809,
          "cache_creation_input_tokens": 1534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1534
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

_source line 20 · 2026-05-28T04:55:26.031Z_

<details><summary>↩ Tool result · `toolu_01P2n9kf1QShNwHg24uzkbSL`</summary>

```text
# SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation

## Title & Authors
**Title:** "SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning"

**Authors:** Zhengyang Ai, Zikang Shan, Xiaodong Ai, Jingxian Tang, Hangkai Hu, Pinyan Lu

## Full Abstract
The researchers propose that "process supervision has emerged as a promising approach for enhancing LLM reasoning, yet existing methods fail to distinguish meaningful progress from mere verbosity." Their framework addresses token inefficiency by formalizing reasoning as movement through a state space based on empirical solvability. The approach uses hierarchical credit assignment: segment-level mechanisms employ stage-aware advantage functions to prioritize efficient breakthroughs in low-potential states, while token-level methods apply entropy-driven redistribution to strengthen execution signals.

## What is SHAPE?
SHAPE is a framework that reconceptualizes LLM reasoning processes as trajectories through state spaces. It implements a two-tier credit assignment system that allocates learning signals differently depending on where reasoning steps occur—distinguishing between steps that make genuine progress versus those that merely add verbosity.

## Stage-Dependent Credit Assignment
The framework's innovation lies in its position-awareness: it employs "stage-aware advantage functions" that treat early reasoning steps differently from later ones, prioritizing efficient breakthroughs when the model is in low-potential states. This acknowledges that informativeness varies based on where steps occur in the reasoning trajectory.

## Main Results
Experiments across three base models and five benchmarks demonstrate an "average accuracy gain of 3% with 30% reduced token consumption," directly addressing both performance and efficiency challenges in mathematical reasoning tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "587c0409-b4f7-4ceb-97ed-3de70636df65",
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "413c8d24-d012-4b55-a9f8-002c5a0b8c2b",
  "toolUseResult": {
    "bytes": 45545,
    "code": 200,
    "codeText": "OK",
    "result": "# SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation\n\n## Title & Authors\n**Title:** \"SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning\"\n\n**Authors:** Zhengyang Ai, Zikang Shan, Xiaodong Ai, Jingxian Tang, Hangkai Hu, Pinyan Lu\n\n## Full Abstract\nThe researchers propose that \"process supervision has emerged as a promising approach for enhancing LLM reasoning, yet existing methods fail to distinguish meaningful progress from mere verbosity.\" Their framework addresses token inefficiency by formalizing reasoning as movement through a state space based on empirical solvability. The approach uses hierarchical credit assignment: segment-level mechanisms employ stage-aware advantage functions to prioritize efficient breakthroughs in low-potential states, while token-level methods apply entropy-driven redistribution to strengthen execution signals.\n\n## What is SHAPE?\nSHAPE is a framework that reconceptualizes LLM reasoning processes as trajectories through state spaces. It implements a two-tier credit assignment system that allocates learning signals differently depending on where reasoning steps occur—distinguishing between steps that make genuine progress versus those that merely add verbosity.\n\n## Stage-Dependent Credit Assignment\nThe framework's innovation lies in its position-awareness: it employs \"stage-aware advantage functions\" that treat early reasoning steps differently from later ones, prioritizing efficient breakthroughs when the model is in low-potential states. This acknowledges that informativeness varies based on where steps occur in the reasoning trajectory.\n\n## Main Results\nExperiments across three base models and five benchmarks demonstrate an \"average accuracy gain of 3% with 30% reduced token consumption,\" directly addressing both performance and efficiency challenges in mathematical reasoning tasks.",
    "durationMs": 6064,
    "url": "https://arxiv.org/abs/2604.06636"
  },
  "sourceToolAssistantUUID": "587c0409-b4f7-4ceb-97ed-3de70636df65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-28T04:55:26.883Z_

<details><summary>↩ Tool result · `toolu_011fJmQiZGsgCGePUsitmDoo`</summary>

```text
# Paper Summary: Process Supervision for Chain-of-Thought Reasoning via Monte Carlo Net Information Gain

## Title & Authors
**Title:** "Process Supervision for Chain-of-Thought Reasoning via Monte Carlo Net Information Gain"

**Authors:** Corentin Royer, Debarun Bhattacharjya, Gaetano Rossiello, Andrea Giovannini, Mennatallah El-Assady

## Full Abstract
The researchers address error propagation in multi-step LLM reasoning. They propose automatic step-level label generation using information theory, estimating "how each reasoning step affects the likelihood of the correct answer." Their method achieves O(N) computational complexity versus prior O(N log N) approaches, enabling scalable supervision across mathematics, programming, SQL, and scientific QA tasks.

## Key Contributions

1. **Novel Labeling Approach:** Automatic step-level label generation via Information Theory rather than costly human annotation or intensive automatic labeling

2. **Computational Efficiency:** Reduces complexity from O(N log N) to O(N), improving scalability

3. **Practical Validation:** Demonstrates effectiveness in chain-of-thought selection across diverse reasoning benchmarks

## What is MCNIG?

The abstract mentions "Monte Carlo Net Information Gain" in the title but the provided content doesn't explicitly define this term. Based on context, it appears to be an information-theoretic method for evaluating individual reasoning steps by measuring their impact on correct answer likelihood.

## Missing Details

The provided webpage excerpt doesn't contain detailed technical comparisons, specific benchmark results, or granular comparisons to standard MC-based PRM training approaches—only that the method enables "effective chain-of-thought selection."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90db1d7d-0f74-4c53-b225-4a14c425ad4f",
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "456aecc9-20d8-4db6-b496-87dbab531890",
  "toolUseResult": {
    "bytes": 45123,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: Process Supervision for Chain-of-Thought Reasoning via Monte Carlo Net Information Gain\n\n## Title & Authors\n**Title:** \"Process Supervision for Chain-of-Thought Reasoning via Monte Carlo Net Information Gain\"\n\n**Authors:** Corentin Royer, Debarun Bhattacharjya, Gaetano Rossiello, Andrea Giovannini, Mennatallah El-Assady\n\n## Full Abstract\nThe researchers address error propagation in multi-step LLM reasoning. They propose automatic step-level label generation using information theory, estimating \"how each reasoning step affects the likelihood of the correct answer.\" Their method achieves O(N) computational complexity versus prior O(N log N) approaches, enabling scalable supervision across mathematics, programming, SQL, and scientific QA tasks.\n\n## Key Contributions\n\n1. **Novel Labeling Approach:** Automatic step-level label generation via Information Theory rather than costly human annotation or intensive automatic labeling\n\n2. **Computational Efficiency:** Reduces complexity from O(N log N) to O(N), improving scalability\n\n3. **Practical Validation:** Demonstrates effectiveness in chain-of-thought selection across diverse reasoning benchmarks\n\n## What is MCNIG?\n\nThe abstract mentions \"Monte Carlo Net Information Gain\" in the title but the provided content doesn't explicitly define this term. Based on context, it appears to be an information-theoretic method for evaluating individual reasoning steps by measuring their impact on correct answer likelihood.\n\n## Missing Details\n\nThe provided webpage excerpt doesn't contain detailed technical comparisons, specific benchmark results, or granular comparisons to standard MC-based PRM training approaches—only that the method enables \"effective chain-of-thought selection.\"",
    "durationMs": 5041,
    "url": "https://arxiv.org/abs/2603.17815"
  },
  "sourceToolAssistantUUID": "90db1d7d-0f74-4c53-b225-4a14c425ad4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T04:55:26.971Z_

<details><summary>↩ Tool result · `toolu_01Lf2PLCUh3xV5cA9WzDryZ9`</summary>

```text
I cannot provide the specific AUC numbers you're requesting because the web page content shown does not contain those detailed numerical comparisons. 

The abstract only states: "mid-reasoning prediction of final-answer correctness with ROC-AUC up to 0.87." This indicates 0.87 is a maximum achievable value, but the page doesn't specify whether it's an average, a peak single-layer result, early-step versus late-step breakdowns, or an early-step baseline like 0.63.

To obtain the exact numbers and comparisons you need, you would need to access the full paper PDF or HTML version linked on this arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35b12325-8d50-4193-b515-5579280a9ab3",
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "1312983a-5a7d-4b17-a516-552dd3e3028c",
  "toolUseResult": {
    "bytes": 46422,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot provide the specific AUC numbers you're requesting because the web page content shown does not contain those detailed numerical comparisons. \n\nThe abstract only states: \"mid-reasoning prediction of final-answer correctness with ROC-AUC up to 0.87.\" This indicates 0.87 is a maximum achievable value, but the page doesn't specify whether it's an average, a peak single-layer result, early-step versus late-step breakdowns, or an early-step baseline like 0.63.\n\nTo obtain the exact numbers and comparisons you need, you would need to access the full paper PDF or HTML version linked on this arXiv page.",
    "durationMs": 2672,
    "url": "https://arxiv.org/abs/2604.05655"
  },
  "sourceToolAssistantUUID": "35b12325-8d50-4193-b515-5579280a9ab3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"change_summary\": \"Major narrative restructuring to lead with the strongest nove…",
  "leafUuid": "1312983a-5a7d-4b17-a516-552dd3e3028c",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise process reward model research based on theoretical framework feedback",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294"
}
```

---

### Tool result

_source line 25 · 2026-05-28T04:55:32.039Z_

<details><summary>↩ Tool result · `toolu_01AtctKCBA4dbQwJGKgaXG7x`</summary>

```text
Web search results for query: "Setlur et al. 2025 "When To Solve When To Verify" compute optimal verification appendix H Qwen 512x"

Links: [{"title":"When To Solve, When To Verify: Compute-Optimal Problem Solving and","url":"https://www.arxiv.org/pdf/2504.01005v1"},{"title":"When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification for LLM Reasoning","url":"https://arxiv.org/html/2504.01005v2"},{"title":"[2504.01005] When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification for LLM Reasoning","url":"https://arxiv.org/abs/2504.01005"},{"title":"When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification for LLM Reasoning","url":"https://arxiv.org/pdf/2504.01005"},{"title":"When Does Verification Pay Off? A Closer Look at LLMs as Solution Verifiers","url":"https://www.arxiv.org/pdf/2512.02304"}]

I found the paper! "When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification for LLM Reasoning" is available on arXiv as paper 2504.01005.

The paper addresses scaling test-time compute for LLMs through Generative Reward Models (GenRM), which reframe verification as a next-token prediction task. GenRM generates multiple verification chains-of-thought to score each solution, creating a fundamental trade-off between allocating compute to scale solutions or to verification.

The paper includes results comparing GenRM-FT and Self-Consistency with Qwen-2.5-7B-Instruct on the MATH dataset, where Self-Consistency outperforms GenRM-FT at lower compute budgets. The researchers also extend their analysis to QwQ-32B (Qwen, 2025) on the challenging AIME 2025 dataset as a solution generator and verifier.

The paper appears to be available at https://arxiv.org/abs/2504.01005 for more detailed information about the appendix H results and the Qwen 512x analysis you're looking for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c453811-ed1d-480e-b563-e74cdeeea5da",
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "cdf64a1c-f6cb-4fc8-bb5f-8739a2cc8d77",
  "toolUseResult": {
    "query": "Setlur et al. 2025 \"When To Solve When To Verify\" compute optimal verification appendix H Qwen 512x",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EaGVCKyamYLiyDDbE2BVv9",
        "content": [
          {
            "title": "When To Solve, When To Verify: Compute-Optimal Problem Solving and",
            "url": "https://www.arxiv.org/pdf/2504.01005v1"
          },
          {
            "title": "When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification for LLM Reasoning",
            "url": "https://arxiv.org/html/2504.01005v2"
          },
          {
            "title": "[2504.01005] When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification for LLM Reasoning",
            "url": "https://arxiv.org/abs/2504.01005"
          },
          {
            "title": "When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2504.01005"
          },
          {
            "title": "When Does Verification Pay Off? A Closer Look at LLMs as Solution Verifiers",
            "url": "https://www.arxiv.org/pdf/2512.02304"
          }
        ]
      },
      "I found the paper! \"When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification for LLM Reasoning\" is available on arXiv as paper 2504.01005.\n\nThe paper addresses scaling test-time compute for LLMs through Generative Reward Models (GenRM), which reframe verification as a next-token prediction task. GenRM generates multiple verification chains-of-thought to score each solution, creating a fundamental trade-off between allocating compute to scale solutions or to verification.\n\nThe paper includes results comparing GenRM-FT and Self-Consistency with Qwen-2.5-7B-Instruct on the MATH dataset, where Self-Consistency outperforms GenRM-FT at lower compute budgets. The researchers also extend their analysis to QwQ-32B (Qwen, 2025) on the challenging AIME 2025 dataset as a solution generator and verifier.\n\nThe paper appears to be available at https://arxiv.org/abs/2504.01005 for more detailed information about the appendix H results and the Qwen 512x analysis you're looking for."
    ],
    "durationSeconds": 6.894910198999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0c453811-ed1d-480e-b563-e74cdeeea5da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-28T04:55:35.024Z_

<details><summary>Logged reasoning block</summary>

```text
Let me get more details on the SIA paper and the LLM Reasoning as Trajectories paper. I also need to check the Setlur appendix reference. Let me fetch the HTML versions for more detail.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdf64a1c-f6cb-4fc8-bb5f-8739a2cc8d77",
  "isSidechain": false,
  "requestId": "req_011CbUNVs4MmWvNN54JfkSPd",
  "type": "assistant",
  "uuid": "9574c768-1d2f-4d56-bbea-00c1cb2562cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZztmaMvCy5Q9bstE2w3GQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2702,
      "cache_read_input_tokens": 30343,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 30343,
          "cache_creation_input_tokens": 2702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2702
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

_source line 27 · 2026-05-28T04:55:35.512Z_

Let me get more details on SIA, MCNIG, the trajectories paper AUC numbers, and verify the Setlur appendix reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9574c768-1d2f-4d56-bbea-00c1cb2562cc",
  "isSidechain": false,
  "requestId": "req_011CbUNVs4MmWvNN54JfkSPd",
  "type": "assistant",
  "uuid": "cc873d4f-8be4-4033-a0b3-684c07a96f6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZztmaMvCy5Q9bstE2w3GQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2702,
      "cache_read_input_tokens": 30343,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 30343,
          "cache_creation_input_tokens": 2702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2702
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

_source line 28 · 2026-05-28T04:55:38.868Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CvsXCPPn51bSGSzBHmUgSK`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.06192",
  "prompt": "I need details about the Stepwise Informativeness Assumption (SIA). Specifically: (1) What is the exact formal definition of SIA? (2) Does SIA claim that informativeness accumulates MONOTONICALLY? (3) Does SIA claim this is UNIVERSAL across all domains, or domain-specific? (4) What are the key theorems/propositions? (5) How does SIA relate to process reward models or step-level verification? (6) What are the main experimental results and on which benchmarks? (7) Is there any discussion of domain-dependent variation in informativeness accumulation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc873d4f-8be4-4033-a0b3-684c07a96f6a",
  "isSidechain": false,
  "requestId": "req_011CbUNVs4MmWvNN54JfkSPd",
  "type": "assistant",
  "uuid": "45857273-78d6-4195-ac09-bd9c14595e5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZztmaMvCy5Q9bstE2w3GQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2702,
      "cache_read_input_tokens": 30343,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 30343,
          "cache_creation_input_tokens": 2702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2702
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

_source line 29 · 2026-05-28T04:55:42.193Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019fw5QNoT1mEnFN3Qsra7yK`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.17815",
  "prompt": "I need the full technical details of MCNIG. Specifically: (1) How is Net Information Gain defined formally? (2) How does it compare to standard MC estimation (Math-Shepherd, OmegaPRM)? (3) What is the O(N) vs O(N log N) comparison about? (4) What are the specific benchmark results (F1 scores, accuracy)? (5) Does it address the cold-start problem on hard problems? (6) What models are used? (7) How does it relate to process reward model training?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45857273-78d6-4195-ac09-bd9c14595e5a",
  "isSidechain": false,
  "requestId": "req_011CbUNVs4MmWvNN54JfkSPd",
  "type": "assistant",
  "uuid": "2b0d76c6-e0de-4f7c-8828-0fa9a0575956",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZztmaMvCy5Q9bstE2w3GQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2702,
      "cache_read_input_tokens": 30343,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 30343,
          "cache_creation_input_tokens": 2702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2702
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

_source line 30 · 2026-05-28T04:55:44.569Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GZiT2S6b6y7XM1dDvWw95P`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.05655",
  "prompt": "I need the EXACT AUC numbers for step-level correctness prediction. Specifically: (1) What is the AUC for early steps vs late steps? (2) Is 0.87 a peak single-layer result or an average? (3) What is the average late-step AUC across layers? (4) Is 0.83 mentioned as an average? (5) What exactly is the gap between early and late steps? Report ALL numerical AUC values mentioned in the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b0d76c6-e0de-4f7c-8828-0fa9a0575956",
  "isSidechain": false,
  "requestId": "req_011CbUNVs4MmWvNN54JfkSPd",
  "type": "assistant",
  "uuid": "168318a4-7ceb-4e53-a443-0f2eaaecc007",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZztmaMvCy5Q9bstE2w3GQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2702,
      "cache_read_input_tokens": 30343,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 30343,
          "cache_creation_input_tokens": 2702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2702
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

_source line 31 · 2026-05-28T04:55:47.902Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GuVVo7RxwYk88X5P55ZsfU`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.01005v2",
  "prompt": "I need to verify: (1) Where in the paper (which appendix) are higher compute multipliers for models other than Llama-3.1-8B discussed? (2) Is there a 512x multiplier mentioned for Qwen-2.5-7B-Instruct? (3) Is this in Appendix F ('Improving Verifier Efficiency') or Appendix H ('Trends Across Model Families')? (4) What are the exact appendix titles? Report the structure of appendices and where the cross-model comparison appears."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "168318a4-7ceb-4e53-a443-0f2eaaecc007",
  "isSidechain": false,
  "requestId": "req_011CbUNVs4MmWvNN54JfkSPd",
  "type": "assistant",
  "uuid": "2677b2b8-d62c-487f-af42-3d405d5b0bb0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZztmaMvCy5Q9bstE2w3GQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2702,
      "cache_read_input_tokens": 30343,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 870,
          "cache_read_input_tokens": 30343,
          "cache_creation_input_tokens": 2702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2702
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

_source line 32 · 2026-05-28T04:55:48.768Z_

<details><summary>↩ Tool result · `toolu_01GZiT2S6b6y7XM1dDvWw95P`</summary>

```text
# Step-Level Correctness Prediction AUC Results

Based on the paper's findings:

**Late-Step AUC Performance:**
- Peak single-layer: 0.87 (at layer 29)
- Average across layers: 0.83

**Early-Step AUC Performance:**
- Average across layers: 0.63

**The Gap:**
The difference between late and early steps is approximately 0.20 AUC points (0.83 - 0.63).

**Additional Context:**
The paper states that "late-step trajectory geometry predicts correctness with average AUC of 0.83 across layers, whereas early-step geometry only achieves 0.63." The final answer marker activation alone achieved an average AUC of 0.81.

In Table 3, trajectory features (the best performer) achieved 0.852±0.039 best-layer AUC when averaged across three random seeds, substantially outperforming step-count baselines (0.649±0.021) and logit-lens methods (0.765±0.027).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "168318a4-7ceb-4e53-a443-0f2eaaecc007",
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "9c585122-9e43-4ce0-bcd9-b32744b7ffb3",
  "toolUseResult": {
    "bytes": 258885,
    "code": 200,
    "codeText": "OK",
    "result": "# Step-Level Correctness Prediction AUC Results\n\nBased on the paper's findings:\n\n**Late-Step AUC Performance:**\n- Peak single-layer: 0.87 (at layer 29)\n- Average across layers: 0.83\n\n**Early-Step AUC Performance:**\n- Average across layers: 0.63\n\n**The Gap:**\nThe difference between late and early steps is approximately 0.20 AUC points (0.83 - 0.63).\n\n**Additional Context:**\nThe paper states that \"late-step trajectory geometry predicts correctness with average AUC of 0.83 across layers, whereas early-step geometry only achieves 0.63.\" The final answer marker activation alone achieved an average AUC of 0.81.\n\nIn Table 3, trajectory features (the best performer) achieved 0.852±0.039 best-layer AUC when averaged across three random seeds, substantially outperforming step-count baselines (0.649±0.021) and logit-lens methods (0.765±0.027).",
    "durationMs": 4195,
    "url": "https://arxiv.org/html/2604.05655"
  },
  "sourceToolAssistantUUID": "168318a4-7ceb-4e53-a443-0f2eaaecc007",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-28T04:55:49.636Z_

<details><summary>↩ Tool result · `toolu_01CvsXCPPn51bSGSzBHmUgSK`</summary>

```text
# Stepwise Informativeness Assumption: Key Details

## 1. Formal Definition of SIA

**Assumption 1** states: "Under a fixed joint p∈Π, prefixes are informative about the true answer in expectation: I_p(A;C_{1:k}|Q) ≥ ε_k > 0 for all k ≥ 1."

This means reasoning prefixes must cumulatively contain mutual information about the correct answer, where ε_k represents a positive information threshold.

## 2. Monotonicity Claim

**No strict monotonicity is required.** The authors clarify: "SIA does not require each individual reasoning token to be informative; rather, it constrains the total information contained in the prefix." Individual steps may be uninformative or even misinformative, provided cumulative information gain remains positive.

## 3. Universality vs. Domain-Specificity

SIA is **domain-dependent and conditional**. The authors explicitly state: "the theory behind SIA is most applicable to problems with a well-defined terminal variable, such as mathematical reasoning or multiple-choice question answering, as opposed to free-form outputs like creative writing." They also identify "regimes in which SIA does not hold," acknowledging entropy-based diagnostics may fail when "reasoning-trace prefixes are only weakly informative about the true answer."

## 4. Key Theorems and Propositions

**Theorem 1** (Entropy Constrains Achievable Accuracy): Lower conditional answer entropy yields lower information-theoretic error bounds on classification accuracy.

**Theorem 2** (Transfer of Internal Stepwise Informativeness): Maximum likelihood estimation on human reasoning traces transfers informativeness properties to trained models, up to KL-divergence bounds.

**Proposition 1** establishes conditional answer entropy as a cumulative information progress variable.

## 5. Relationship to Process Reward Models

The paper does **not discuss** process reward models or step-level verification systems. The focus remains on entropy dynamics and information-theoretic properties rather than reward-based training approaches.

## 6. Experimental Results and Benchmarks

Experiments span three datasets:
- **GSM8K** (math word problems)
- **ARC** (multiple-choice science)
- **SVAMP** (arithmetic robustness)

Across 11 models (Gemma, LLaMA, Qwen, DeepSeek, OLMo variants), results show:

- Base models exhibit "weak or negative alignment" (ρ_SIA near zero or negative)
- Supervised fine-tuned models show "strong positive alignment on average"
- RL-trained models approach "near-perfect alignment"

Three observable signatures were empirically validated: early information accumulation, separability of correct/incorrect traces by prefix entropy, and saturation at near-zero entropy.

## 7. Domain-Dependent Variation Discussion

The authors acknowledge substantial domain variation: alignment coefficients differ dramatically across datasets even within single models. For example, Qwen2.5-3B shows ρ_SIA of 0.682 on GSM8K but only 0.344 on ARC. They attribute this to data curation, supervision quality, and task structure rather than claiming universal behavior.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45857273-78d6-4195-ac09-bd9c14595e5a",
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "6c09e3ab-0d40-4c38-a3e9-64609dc38641",
  "toolUseResult": {
    "bytes": 478253,
    "code": 200,
    "codeText": "OK",
    "result": "# Stepwise Informativeness Assumption: Key Details\n\n## 1. Formal Definition of SIA\n\n**Assumption 1** states: \"Under a fixed joint p∈Π, prefixes are informative about the true answer in expectation: I_p(A;C_{1:k}|Q) ≥ ε_k > 0 for all k ≥ 1.\"\n\nThis means reasoning prefixes must cumulatively contain mutual information about the correct answer, where ε_k represents a positive information threshold.\n\n## 2. Monotonicity Claim\n\n**No strict monotonicity is required.** The authors clarify: \"SIA does not require each individual reasoning token to be informative; rather, it constrains the total information contained in the prefix.\" Individual steps may be uninformative or even misinformative, provided cumulative information gain remains positive.\n\n## 3. Universality vs. Domain-Specificity\n\nSIA is **domain-dependent and conditional**. The authors explicitly state: \"the theory behind SIA is most applicable to problems with a well-defined terminal variable, such as mathematical reasoning or multiple-choice question answering, as opposed to free-form outputs like creative writing.\" They also identify \"regimes in which SIA does not hold,\" acknowledging entropy-based diagnostics may fail when \"reasoning-trace prefixes are only weakly informative about the true answer.\"\n\n## 4. Key Theorems and Propositions\n\n**Theorem 1** (Entropy Constrains Achievable Accuracy): Lower conditional answer entropy yields lower information-theoretic error bounds on classification accuracy.\n\n**Theorem 2** (Transfer of Internal Stepwise Informativeness): Maximum likelihood estimation on human reasoning traces transfers informativeness properties to trained models, up to KL-divergence bounds.\n\n**Proposition 1** establishes conditional answer entropy as a cumulative information progress variable.\n\n## 5. Relationship to Process Reward Models\n\nThe paper does **not discuss** process reward models or step-level verification systems. The focus remains on entropy dynamics and information-theoretic properties rather than reward-based training approaches.\n\n## 6. Experimental Results and Benchmarks\n\nExperiments span three datasets:\n- **GSM8K** (math word problems)\n- **ARC** (multiple-choice science)\n- **SVAMP** (arithmetic robustness)\n\nAcross 11 models (Gemma, LLaMA, Qwen, DeepSeek, OLMo variants), results show:\n\n- Base models exhibit \"weak or negative alignment\" (ρ_SIA near zero or negative)\n- Supervised fine-tuned models show \"strong positive alignment on average\"\n- RL-trained models approach \"near-perfect alignment\"\n\nThree observable signatures were empirically validated: early information accumulation, separability of correct/incorrect traces by prefix entropy, and saturation at near-zero entropy.\n\n## 7. Domain-Dependent Variation Discussion\n\nThe authors acknowledge substantial domain variation: alignment coefficients differ dramatically across datasets even within single models. For example, Qwen2.5-3B shows ρ_SIA of 0.682 on GSM8K but only 0.344 on ARC. They attribute this to data curation, supervision quality, and task structure rather than claiming universal behavior.",
    "durationMs": 10764,
    "url": "https://arxiv.org/html/2604.06192"
  },
  "sourceToolAssistantUUID": "45857273-78d6-4195-ac09-bd9c14595e5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-28T04:55:52.657Z_

<details><summary>↩ Tool result · `toolu_019fw5QNoT1mEnFN3Qsra7yK`</summary>

```text
# MCNIG Technical Details

## (1) Net Information Gain Definition

Monte Carlo Net Information Gain formally contrasts correct versus incorrect answer likelihoods:

**NetInfo_i** = max(ℐ_i(y) for y ∈ correct answers) − max(ℐ_i(y) for y ∈ incorrect answers)

**MCNIG_i** = NetInfo_i − NetInfo_0

where ℐ_i(y) represents cumulative log-probability of answer y given partial reasoning through step i.

## (2) Complexity Comparison

**MathShepherd**: O(N²) — generates M rollouts at each step, requiring quadratic token processing

**OmegaPRM**: O(N log N) — uses binary search to identify first failure, reducing queried prefixes to ⌈log₂ N⌉

**MCNIG**: O(N) — processes question and CoT once via KV-caching, then rescores only answer tokens S×T times across N steps, yielding approximately |q| + Ns̄ + (N+1)ST tokens

## (3) O(N) vs O(N log N) Distinction

MCNIG achieves linearity by avoiding rollout generation entirely. Instead of generating new continuations from each intermediate step (as prior methods do), it leverages KV-cached prefix representations and rescores sampled answers at each boundary, reducing computational overhead substantially.

## (4) Benchmark Results

**Best-of-K Performance (8B Model)**:
- MATH: 74.8%
- GSM8K: 93.8%
- HumanEval: 84.6%
- BigCodeBench: 46.8%
- Bird (SQL): 46.2%
- Average: 62.3%

**ProcessBench F1 Scores**:
- MCNIG 8B: 73.2
- MCNIG 14B: 75.1 (surpasses QwenPRM 7B at 75.0)

## (5) Cold-Start Problem

The paper does not directly address cold-start scenarios on initially hard problems. However, analysis shows MCNIG's robustness improves on tasks with longer outputs where standard Information Gain fails—it "mitigates this failure mode by aggregating over multiple samples of both correct and incorrect responses."

## (6) Base Models

Training and labeling use **Ministral-8B-Instruct-2410** for token-level log-probability estimation. PRMs trained on **Ministral 3 8B and 14B** as base models with AdamW (learning rate 1e-6), batch size 128, two epochs.

## (7) PRM Training Integration

MCNIG-derived binary labels (via threshold τ_q) train step-level classifiers predicting correctness at delimiter tokens. During inference, PRM scores multiply step predictions across traces for best-of-K selection, enabling fine-grained supervision without human annotation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b0d76c6-e0de-4f7c-8828-0fa9a0575956",
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "021197d7-83de-42c1-8a3a-4c89355813c2",
  "toolUseResult": {
    "bytes": 266948,
    "code": 200,
    "codeText": "OK",
    "result": "# MCNIG Technical Details\n\n## (1) Net Information Gain Definition\n\nMonte Carlo Net Information Gain formally contrasts correct versus incorrect answer likelihoods:\n\n**NetInfo_i** = max(ℐ_i(y) for y ∈ correct answers) − max(ℐ_i(y) for y ∈ incorrect answers)\n\n**MCNIG_i** = NetInfo_i − NetInfo_0\n\nwhere ℐ_i(y) represents cumulative log-probability of answer y given partial reasoning through step i.\n\n## (2) Complexity Comparison\n\n**MathShepherd**: O(N²) — generates M rollouts at each step, requiring quadratic token processing\n\n**OmegaPRM**: O(N log N) — uses binary search to identify first failure, reducing queried prefixes to ⌈log₂ N⌉\n\n**MCNIG**: O(N) — processes question and CoT once via KV-caching, then rescores only answer tokens S×T times across N steps, yielding approximately |q| + Ns̄ + (N+1)ST tokens\n\n## (3) O(N) vs O(N log N) Distinction\n\nMCNIG achieves linearity by avoiding rollout generation entirely. Instead of generating new continuations from each intermediate step (as prior methods do), it leverages KV-cached prefix representations and rescores sampled answers at each boundary, reducing computational overhead substantially.\n\n## (4) Benchmark Results\n\n**Best-of-K Performance (8B Model)**:\n- MATH: 74.8%\n- GSM8K: 93.8%\n- HumanEval: 84.6%\n- BigCodeBench: 46.8%\n- Bird (SQL): 46.2%\n- Average: 62.3%\n\n**ProcessBench F1 Scores**:\n- MCNIG 8B: 73.2\n- MCNIG 14B: 75.1 (surpasses QwenPRM 7B at 75.0)\n\n## (5) Cold-Start Problem\n\nThe paper does not directly address cold-start scenarios on initially hard problems. However, analysis shows MCNIG's robustness improves on tasks with longer outputs where standard Information Gain fails—it \"mitigates this failure mode by aggregating over multiple samples of both correct and incorrect responses.\"\n\n## (6) Base Models\n\nTraining and labeling use **Ministral-8B-Instruct-2410** for token-level log-probability estimation. PRMs trained on **Ministral 3 8B and 14B** as base models with AdamW (learning rate 1e-6), batch size 128, two epochs.\n\n## (7) PRM Training Integration\n\nMCNIG-derived binary labels (via threshold τ_q) train step-level classifiers predicting correctness at delimiter tokens. During inference, PRM scores multiply step predictions across traces for best-of-K selection, enabling fine-grained supervision without human annotation.",
    "durationMs": 10461,
    "url": "https://arxiv.org/html/2603.17815"
  },
  "sourceToolAssistantUUID": "2b0d76c6-e0de-4f7c-8828-0fa9a0575956",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-28T04:55:53.983Z_

<details><summary>↩ Tool result · `toolu_01GuVVo7RxwYk88X5P55ZsfU`</summary>

```text
# Analysis of Compute Multipliers Across Models

Based on the paper structure:

## Appendix Organization

The cross-model comparisons appear in **Appendix H: "Trends Across Model Families"** (page showing Qwen-2.5-7B results) and **Appendix J: "Additional Details and Results on Compute-Optimal Scaling Analysis"** (containing scaling laws for multiple models).

## Key Findings on Compute Multipliers

**Appendix H (Qwen-2.5-7B-Instruct):**
The paper states: "SC outperforms GenRM-FT at lower budgets, whereas GenRM shines at higher budgets" and reports that "SC achieves its peak performance with 64× less compute than GenRM-FT" while "GenRM-FT shines...achieving an improvement of 5.4%, but by utilizing 512× more compute."

**Appendix J (Multiple Models):**
This section provides scaling law derivations for:
- Llama-3.1-8B with GenRM-FT: S_opt ∝ C^0.57, V_opt ∝ C^0.39
- Qwen-2.5-7B with GenRM-FT: S_opt ∝ C^0.75, V_opt ∝ C^0.32
- Llama-3.3-70B with GenRM-Base: S_opt ∝ C^0.69, V_opt ∝ C^0.43

The **512× multiplier for Qwen-2.5-7B** appears in **Appendix H**, not Appendix F. Appendix F focuses on efficiency improvements through smaller verifiers and fewer tokens, not cross-model comparisons.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2677b2b8-d62c-487f-af42-3d405d5b0bb0",
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "1ab09755-522e-46ea-a850-52877bdbdbd1",
  "toolUseResult": {
    "bytes": 594762,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of Compute Multipliers Across Models\n\nBased on the paper structure:\n\n## Appendix Organization\n\nThe cross-model comparisons appear in **Appendix H: \"Trends Across Model Families\"** (page showing Qwen-2.5-7B results) and **Appendix J: \"Additional Details and Results on Compute-Optimal Scaling Analysis\"** (containing scaling laws for multiple models).\n\n## Key Findings on Compute Multipliers\n\n**Appendix H (Qwen-2.5-7B-Instruct):**\nThe paper states: \"SC outperforms GenRM-FT at lower budgets, whereas GenRM shines at higher budgets\" and reports that \"SC achieves its peak performance with 64× less compute than GenRM-FT\" while \"GenRM-FT shines...achieving an improvement of 5.4%, but by utilizing 512× more compute.\"\n\n**Appendix J (Multiple Models):**\nThis section provides scaling law derivations for:\n- Llama-3.1-8B with GenRM-FT: S_opt ∝ C^0.57, V_opt ∝ C^0.39\n- Qwen-2.5-7B with GenRM-FT: S_opt ∝ C^0.75, V_opt ∝ C^0.32\n- Llama-3.3-70B with GenRM-Base: S_opt ∝ C^0.69, V_opt ∝ C^0.43\n\nThe **512× multiplier for Qwen-2.5-7B** appears in **Appendix H**, not Appendix F. Appendix F focuses on efficiency improvements through smaller verifiers and fewer tokens, not cross-model comparisons.",
    "durationMs": 6078,
    "url": "https://arxiv.org/html/2504.01005v2"
  },
  "sourceToolAssistantUUID": "2677b2b8-d62c-487f-af42-3d405d5b0bb0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-28T04:55:53.986Z_

```json
{
  "parentUuid": "1ab09755-522e-46ea-a850-52877bdbdbd1",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fa6fc761-c364-4735-805d-2c7bd98eee4e",
  "timestamp": "2026-05-28T04:55:53.986Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"change_summary\": \"Major narrative restructuring to lead with the strongest nove…",
  "leafUuid": "fa6fc761-c364-4735-805d-2c7bd98eee4e",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise process reward model research based on theoretical framework feedback",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294"
}
```

---

### Assistant

_source line 39 · 2026-05-28T04:56:36.617Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have excellent data on all three papers and the factual corrections. Let me also do a deeper search on SHAPE to get more technical details, and look for any additional recent papers that might be relevant.

Key findings:
1. **SIA (2604.06192)**: Formalizes stepwise informativeness as mutual information I_p(A;C_{1:k}|Q) ≥ ε_k > 0. NOT monotonic per-step, but cumulative. Domain-dependent (ρ_SIA varies: 0.682 on GSM8K vs 0.344 on ARC for same model). 

Notably, SIA doesn't address process reward models at all, which is actually useful for our argument—it gives us the information-theoretic grounding while δ_d provides the empirical calibration showing exactly how domain-dependent variation manifests in ways SIA identifies but doesn't quantify.

2. **SHAPE (2604.06636)**: Stage-aware credit assignment for RL training, 3% accuracy gain with 30% token reduction. Different methodology (RL credit assignment vs MC annotation), but thematic overlap with "position matters."

3. **MCNIG (2603.17815)**: Information-theoretic alternative to MC estimation, O(N) complexity. ProcessBench F1: 73.2 (8B), 75.1 (14B). Doesn't address cold-start directly but avoids rollouts entirely. This is actually quite relevant as an alternative/complementary approach.

4. **AUC correction**: Late-step average 0.83, early-step 0.63, gap is ~20 points. Peak single-layer is 0.87. Reviewer is correct.

5. **Setlur appendix**: 512× for Qwen-2.5-7B is in Appendix H, not F. Reviewer is correct.

The reviewer's core point is that the score is stuck at 3.875 with impact (3.5) as the bottleneck. The real leverage is reframing δ_d not just as an empirical measurement but as an empirical validation of SIA's theoretical predictions—that's what elevates the contribution.

SIA establishes the information-theoretic principle that prefixes accumulate answer-relevant information, but it glosses over domain-dependent variation (ρ_SIA ranges from 0.682 to 0.344 across tasks). My δ_d index fills exactly that gap by providing systematic, per-domain calibration of how fast this information accumulates. If δ_d reveals significant domain variation, it suggests SIA's universality claim needs refinement, which has broader implications for how we think about reasoning in language models.

Now I'm checking whether MCNIG's 73.2 and 75.1 F1 scores are on ProcessBench overall or just the OmniMATH subset, since it's a competitive rollout-free baseline that actually outperforms CPMI and comes close to QwenPRM 7B at 75.0.

The stagnation at 3.875 across multiple rounds suggests the real bottleneck is impact at 3.5, and the reviewer's SIA integration suggestion isn't just a citation addition—it's a fundamental reframing of the δ_d contribution that could meaningfully address that gap.

Now I'm checking whether the MCNIG ProcessBench numbers are directly comparable to what we're reporting, since they use a different base model and the metrics might be measuring different subsets of the benchmark. I'm realizing MCNIG probably hits the same wall on the hardest problems since it depends on the model's ability to assign reliable probabilities to correct answers, which breaks down when the model can barely solve the problem in the first place. Now I should draft the revised proposal with the elevated δ_d framing through its connection to SIA, MCNIG as a new baseline, and the restructured narrative. Let me also dig deeper into SHAPE to make sure I have the details right before finalizing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa6fc761-c364-4735-805d-2c7bd98eee4e",
  "isSidechain": false,
  "requestId": "req_011CbUNXUqgec1CBHESzCSb1",
  "type": "assistant",
  "uuid": "7f0873d5-3cb1-47ec-b9be-3931740447d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fqtDeqgiB1H9BkdjjNGo9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3198,
      "cache_read_input_tokens": 33045,
      "output_tokens": 2035,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2035,
          "cache_read_input_tokens": 33045,
          "cache_creation_input_tokens": 3198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3198
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

_source line 40 · 2026-05-28T04:56:36.618Z_

Let me get more technical details on SHAPE and check if MCNIG has Hard2Verify or OmniMATH-specific results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f0873d5-3cb1-47ec-b9be-3931740447d0",
  "isSidechain": false,
  "requestId": "req_011CbUNXUqgec1CBHESzCSb1",
  "type": "assistant",
  "uuid": "2fd4f0ee-8d28-4148-b95d-730d3a158733",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fqtDeqgiB1H9BkdjjNGo9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3198,
      "cache_read_input_tokens": 33045,
      "output_tokens": 2035,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2035,
          "cache_read_input_tokens": 33045,
          "cache_creation_input_tokens": 3198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3198
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

_source line 41 · 2026-05-28T04:56:37.564Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TnmBvbZCxru6UU6u6VdMwa`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.06636",
  "prompt": "Extract the full technical details of SHAPE: (1) What is the formal definition of \"potential\" and \"stage-aware advantage\"? (2) Which benchmarks are used? (3) What are the specific accuracy numbers? (4) What base models are used? (5) How does stage/position affect credit assignment specifically? (6) Does it relate to process reward models or MC estimation? (7) What is the key insight about how step position relates to informativeness?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fd4f0ee-8d28-4148-b95d-730d3a158733",
  "isSidechain": false,
  "requestId": "req_011CbUNXUqgec1CBHESzCSb1",
  "type": "assistant",
  "uuid": "ff28d69d-d27e-4c0b-ab0e-6667cac3e4da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fqtDeqgiB1H9BkdjjNGo9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3198,
      "cache_read_input_tokens": 33045,
      "output_tokens": 2035,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2035,
          "cache_read_input_tokens": 33045,
          "cache_creation_input_tokens": 3198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3198
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

_source line 42 · 2026-05-28T04:56:38.136Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JZ6yuoEiiuYcgDZFHCXvcm`</summary>

```json
{
  "query": "MCNIG \"Monte Carlo Net Information Gain\" ProcessBench OmniMATH hard problems F1 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff28d69d-d27e-4c0b-ab0e-6667cac3e4da",
  "isSidechain": false,
  "requestId": "req_011CbUNXUqgec1CBHESzCSb1",
  "type": "assistant",
  "uuid": "9aa787a7-f991-4b57-aa36-bd00875f5305",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fqtDeqgiB1H9BkdjjNGo9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3198,
      "cache_read_input_tokens": 33045,
      "output_tokens": 2035,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2035,
          "cache_read_input_tokens": 33045,
          "cache_creation_input_tokens": 3198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3198
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

_source line 43 · 2026-05-28T04:56:45.369Z_

<details><summary>↩ Tool result · `toolu_01JZ6yuoEiiuYcgDZFHCXvcm`</summary>

```text
Web search results for query: "MCNIG "Monte Carlo Net Information Gain" ProcessBench OmniMATH hard problems F1 2026"

Links: [{"title":"Process Supervision for Chain-of-Thought Reasoning via Monte Carlo Net Information Gain","url":"https://arxiv.org/html/2603.17815"},{"title":"Published in Transactions on Machine Learning Research (03/2026)","url":"https://openreview.net/pdf?id=FPVCb0WMuN"},{"title":"Opponent State Inference Under Partial Observability: An HMM-POMDP Framework for 2026 Formula 1 Energy Strategy","url":"https://arxiv.org/pdf/2603.01290"},{"title":"From Static to Dynamic: Adaptive Monte Carlo Search for Mathematical Process Supervision","url":"https://arxiv.org/pdf/2509.24351"},{"title":"Monte-Carlo approach to computing value of information","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9367815"}]

Based on the search results, here's what I found:

MCNIG (Monte Carlo Net Information Gain) is a method that extends Information Gain to provide a more reliable signal of step quality for process reward models (PRMs). The method requires only problem-solution pairs and a validator function, avoiding the need for costly human annotation.

The MCNIG models were evaluated on ProcessBench, which reports F1 scores based on aggregated step-level classification. ProcessBench includes two of the most challenging subsets: OlympiadBench and OmniMath, each comprised of 1K problem-prefix pairs.

The results show strong performance: MCNIG 8B further improves performance and approaches QwenPRM 7B, with MCNIG 14B slightly surpassing QwenPRM 7B and achieving the best overall F1 score.

MCNIG achieves linear complexity in the number of reasoning steps, improving over the best prior automatic labeling approach. The method was validated across eight reasoning benchmarks including both in-distribution settings and out-of-distribution generalization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9aa787a7-f991-4b57-aa36-bd00875f5305",
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "01819699-6954-4d1d-ac0a-c91ad1d0eaaf",
  "toolUseResult": {
    "query": "MCNIG \"Monte Carlo Net Information Gain\" ProcessBench OmniMATH hard problems F1 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011tp1M8LzXh6hq5Q5bqF6bU",
        "content": [
          {
            "title": "Process Supervision for Chain-of-Thought Reasoning via Monte Carlo Net Information Gain",
            "url": "https://arxiv.org/html/2603.17815"
          },
          {
            "title": "Published in Transactions on Machine Learning Research (03/2026)",
            "url": "https://openreview.net/pdf?id=FPVCb0WMuN"
          },
          {
            "title": "Opponent State Inference Under Partial Observability: An HMM-POMDP Framework for 2026 Formula 1 Energy Strategy",
            "url": "https://arxiv.org/pdf/2603.01290"
          },
          {
            "title": "From Static to Dynamic: Adaptive Monte Carlo Search for Mathematical Process Supervision",
            "url": "https://arxiv.org/pdf/2509.24351"
          },
          {
            "title": "Monte-Carlo approach to computing value of information",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9367815"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\nMCNIG (Monte Carlo Net Information Gain) is a method that extends Information Gain to provide a more reliable signal of step quality for process reward models (PRMs). The method requires only problem-solution pairs and a validator function, avoiding the need for costly human annotation.\n\nThe MCNIG models were evaluated on ProcessBench, which reports F1 scores based on aggregated step-level classification. ProcessBench includes two of the most challenging subsets: OlympiadBench and OmniMath, each comprised of 1K problem-prefix pairs.\n\nThe results show strong performance: MCNIG 8B further improves performance and approaches QwenPRM 7B, with MCNIG 14B slightly surpassing QwenPRM 7B and achieving the best overall F1 score.\n\nMCNIG achieves linear complexity in the number of reasoning steps, improving over the best prior automatic labeling approach. The method was validated across eight reasoning benchmarks including both in-distribution settings and out-of-distribution generalization."
    ],
    "durationSeconds": 7.229773902000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9aa787a7-f991-4b57-aa36-bd00875f5305",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-28T04:56:47.160Z_

<details><summary>↩ Tool result · `toolu_01TnmBvbZCxru6UU6u6VdMwa`</summary>

```text
# SHAPE Technical Details Summary

## (1) Formal Definitions

**Potential (Φ)**: Defined as "the average score: Φ(sₖ)=1/m ∑ᵢ₌₁ᵐ rᵢ" where m rollouts estimate binary correctness at segment boundaries. It quantifies intermediate solvability.

**Stage-Aware Advantage**: Formalized as:
Aₖ = Routcome + α·(γₖ(Lₖ)·Φ(sₖ₊₁) - Φ(sₖ))

The dynamic discount factor γₖ(Lₖ) = max(γmin, 1 - Lₖ/Lref·(1-γmin)) creates "stage awareness by scaling the baseline penalty according to the current stage's difficulty."

## (2) Benchmarks

Five mathematical reasoning benchmarks: AIME 2024/25, AMC 2023, MinervaMATH, and MATH500.

## (3) Specific Accuracy Numbers

On DeepSeek-R1-Distill-Qwen-1.5B across five datasets, SHAPE achieves: AIME 24: 37.1% (+2.4), AIME 25: 31.8% (+4.3), AMC 23: 81.5% (+2.4), MATH500: 87.8% (+3.0), MinervaMATH: 35.5% (+1.3), with average 54.7% accuracy.

## (4) Base Models

Three models: DeepSeek-R1-Distill-Qwen-1.5B, DeepScaleR-1.5B-Preview, and Qwen3-4B.

## (5) Position-Based Credit Assignment

The mechanism decomposes rewards as: Fₖ ≈ Δₖ - (1-γₖ(Lₖ))·Φ(sₖ). Early stages (low Φ) experience negligible penalties, encouraging breakthroughs. Later stages incur proportional taxes, suppressing inflation. Length creates additional penalties through γₖ decay.

## (6) Relationship to Process Supervision

SHAPE uses "rollout formulation" for potential estimation, distinct from learned process reward models. It employs rule-based binary verification without training separate reward models, avoiding "prohibitive annotation costs."

## (7) Key Insight on Step Position

"A unit of improvement in adverse stages yields an approximately 18% higher marginal return on final success than in already performant stages." Entropy-based segmentation identifies "pivotal logical transitions" rather than rigid delimiters.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff28d69d-d27e-4c0b-ab0e-6667cac3e4da",
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "0a9de2fe-5de2-4e67-8a8f-71814778e5dd",
  "toolUseResult": {
    "bytes": 384646,
    "code": 200,
    "codeText": "OK",
    "result": "# SHAPE Technical Details Summary\n\n## (1) Formal Definitions\n\n**Potential (Φ)**: Defined as \"the average score: Φ(sₖ)=1/m ∑ᵢ₌₁ᵐ rᵢ\" where m rollouts estimate binary correctness at segment boundaries. It quantifies intermediate solvability.\n\n**Stage-Aware Advantage**: Formalized as:\nAₖ = Routcome + α·(γₖ(Lₖ)·Φ(sₖ₊₁) - Φ(sₖ))\n\nThe dynamic discount factor γₖ(Lₖ) = max(γmin, 1 - Lₖ/Lref·(1-γmin)) creates \"stage awareness by scaling the baseline penalty according to the current stage's difficulty.\"\n\n## (2) Benchmarks\n\nFive mathematical reasoning benchmarks: AIME 2024/25, AMC 2023, MinervaMATH, and MATH500.\n\n## (3) Specific Accuracy Numbers\n\nOn DeepSeek-R1-Distill-Qwen-1.5B across five datasets, SHAPE achieves: AIME 24: 37.1% (+2.4), AIME 25: 31.8% (+4.3), AMC 23: 81.5% (+2.4), MATH500: 87.8% (+3.0), MinervaMATH: 35.5% (+1.3), with average 54.7% accuracy.\n\n## (4) Base Models\n\nThree models: DeepSeek-R1-Distill-Qwen-1.5B, DeepScaleR-1.5B-Preview, and Qwen3-4B.\n\n## (5) Position-Based Credit Assignment\n\nThe mechanism decomposes rewards as: Fₖ ≈ Δₖ - (1-γₖ(Lₖ))·Φ(sₖ). Early stages (low Φ) experience negligible penalties, encouraging breakthroughs. Later stages incur proportional taxes, suppressing inflation. Length creates additional penalties through γₖ decay.\n\n## (6) Relationship to Process Supervision\n\nSHAPE uses \"rollout formulation\" for potential estimation, distinct from learned process reward models. It employs rule-based binary verification without training separate reward models, avoiding \"prohibitive annotation costs.\"\n\n## (7) Key Insight on Step Position\n\n\"A unit of improvement in adverse stages yields an approximately 18% higher marginal return on final success than in already performant stages.\" Entropy-based segmentation identifies \"pivotal logical transitions\" rather than rigid delimiters.",
    "durationMs": 9592,
    "url": "https://arxiv.org/html/2604.06636"
  },
  "sourceToolAssistantUUID": "ff28d69d-d27e-4c0b-ab0e-6667cac3e4da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-28T04:56:50.254Z_

<details><summary>Logged reasoning block</summary>

```text
Let me get the MCNIG ProcessBench breakdown by subset to see their OmniMATH-specific numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a9de2fe-5de2-4e67-8a8f-71814778e5dd",
  "isSidechain": false,
  "requestId": "req_011CbUNbQBWEP8ChfZYpPYWz",
  "type": "assistant",
  "uuid": "adf254fa-2fe0-444e-8dc9-a0ffd90a52ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYNdQFvxLnSEn4MrFi8Dio",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 554,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 36243,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2711,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 554,
          "output_tokens": 429,
          "cache_read_input_tokens": 36243,
          "cache_creation_input_tokens": 2711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2711
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

_source line 46 · 2026-05-28T04:56:50.756Z_

Let me get the MCNIG per-subset ProcessBench scores, especially OmniMATH.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adf254fa-2fe0-444e-8dc9-a0ffd90a52ca",
  "isSidechain": false,
  "requestId": "req_011CbUNbQBWEP8ChfZYpPYWz",
  "type": "assistant",
  "uuid": "b4920fa9-af28-4188-85a5-32c787254ecd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYNdQFvxLnSEn4MrFi8Dio",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 554,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 36243,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2711,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 554,
          "output_tokens": 429,
          "cache_read_input_tokens": 36243,
          "cache_creation_input_tokens": 2711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2711
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

_source line 47 · 2026-05-28T04:56:54.658Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01N6YwiwxFqNa5du4zpB1aBj`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.17815",
  "prompt": "I need the ProcessBench results broken down by subset. Specifically: (1) What is the F1 score on ProcessBench OmniMATH specifically? (2) What is the F1 on OlympiadBench? (3) What are the per-subset F1 scores for MCNIG 8B and 14B? (4) How does MCNIG compare to Math-Shepherd, OmegaPRM, and Qwen2.5-Math-PRM on each subset? (5) Are there any Hard2Verify results? (6) What is the overall ProcessBench average vs the hard-subset performance? Report ALL numerical results from tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4920fa9-af28-4188-85a5-32c787254ecd",
  "isSidechain": false,
  "requestId": "req_011CbUNbQBWEP8ChfZYpPYWz",
  "type": "assistant",
  "uuid": "239d811e-eb5c-4b32-b415-b466e3a77448",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYNdQFvxLnSEn4MrFi8Dio",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 554,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 36243,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2711,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 554,
          "output_tokens": 429,
          "cache_read_input_tokens": 36243,
          "cache_creation_input_tokens": 2711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2711
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

_source line 48 · 2026-05-28T04:56:55.765Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Un1pcYxWpsd7CYrr1DMqxo`</summary>

```json
{
  "url": "https://openreview.net/pdf?id=FPVCb0WMuN",
  "prompt": "Extract the ProcessBench results table broken down by subset. What are the F1 scores for MCNIG on OmniMATH and OlympiadBench specifically? How does it compare to other methods on these hard subsets?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "239d811e-eb5c-4b32-b415-b466e3a77448",
  "isSidechain": false,
  "requestId": "req_011CbUNbQBWEP8ChfZYpPYWz",
  "type": "assistant",
  "uuid": "f56cd1b8-858f-4339-a507-219fc0ba8b5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYNdQFvxLnSEn4MrFi8Dio",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 554,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 36243,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2711,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 554,
          "output_tokens": 429,
          "cache_read_input_tokens": 36243,
          "cache_creation_input_tokens": 2711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2711
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

_source line 49_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"change_summary\": \"Major narrative restructuring to lead with the strongest nove…",
  "leafUuid": "f56cd1b8-858f-4339-a507-219fc0ba8b5f",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise process reward model research based on theoretical framework feedback",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294"
}
```

---

### Tool result

_source line 51 · 2026-05-28T04:56:59.475Z_

<details><summary>↩ Tool result · `toolu_01N6YwiwxFqNa5du4zpB1aBj`</summary>

```text
# ProcessBench Results Analysis

Based on my review of the provided document, I can only partially answer your questions about ProcessBench performance.

## Available Data

The paper includes **Table 5**, which presents ProcessBench results showing overall F1 scores:

- MathShepherd: 41.1
- Granite PRM v2: 51.9
- IG 8B (authors): 70.1
- MCNIG 8B (authors): 73.2
- QwenPRM 7B: 75.0
- MCNIG 14B (authors): 75.1

## Critical Limitation

**The document does not contain the granular breakdown you requested.** Specifically, it lacks:

1. Per-subset F1 scores (OmniMATH, OlympiadBench, Hard2Verify, etc.)
2. Comparative performance across these subsets for different methods
3. Hard-subset versus overall average comparisons
4. Results comparing to Qwen2.5-Math-PRM

The paper states it evaluated on ProcessBench but reports only aggregate F1 metrics. For the detailed subset analysis you need, you would need to consult the original ProcessBench paper or access supplementary materials not included in this HTML version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "239d811e-eb5c-4b32-b415-b466e3a77448",
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "20d85ae3-f6fb-4d4b-b2bb-cae85a87dc5e",
  "toolUseResult": {
    "bytes": 266948,
    "code": 200,
    "codeText": "OK",
    "result": "# ProcessBench Results Analysis\n\nBased on my review of the provided document, I can only partially answer your questions about ProcessBench performance.\n\n## Available Data\n\nThe paper includes **Table 5**, which presents ProcessBench results showing overall F1 scores:\n\n- MathShepherd: 41.1\n- Granite PRM v2: 51.9\n- IG 8B (authors): 70.1\n- MCNIG 8B (authors): 73.2\n- QwenPRM 7B: 75.0\n- MCNIG 14B (authors): 75.1\n\n## Critical Limitation\n\n**The document does not contain the granular breakdown you requested.** Specifically, it lacks:\n\n1. Per-subset F1 scores (OmniMATH, OlympiadBench, Hard2Verify, etc.)\n2. Comparative performance across these subsets for different methods\n3. Hard-subset versus overall average comparisons\n4. Results comparing to Qwen2.5-Math-PRM\n\nThe paper states it evaluated on ProcessBench but reports only aggregate F1 metrics. For the detailed subset analysis you need, you would need to consult the original ProcessBench paper or access supplementary materials not included in this HTML version.",
    "durationMs": 4813,
    "url": "https://arxiv.org/html/2603.17815"
  },
  "sourceToolAssistantUUID": "239d811e-eb5c-4b32-b415-b466e3a77448",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-28T04:57:00.760Z_

<details><summary>↩ Tool result · `toolu_01Un1pcYxWpsd7CYrr1DMqxo`</summary>

```text
I apologize, but I cannot extract the ProcessBench results table you're asking about from the provided content. The material appears to be a PDF file encoded in compressed/binary format, making it impossible to read the actual text content about F1 scores, MCNIG performance metrics, or comparisons across OmniMATH and OlympiadBench subsets.

To help you find this information, I'd recommend:

1. **Accessing the original document directly** - Open the PDF in a standard viewer
2. **Providing the text content** - Copy and paste the relevant table or section in plain text format
3. **Specifying the source** - If this is from a research paper, sharing the title would help locate the data

If you can share the actual table or text content from the document, I'd be happy to analyze the F1 scores and methodology comparisons you're seeking.

[Binary content (application/pdf, 1.1MB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/30a87c3c-1394-4ddd-886e-4fe0df585294/tool-results/webfetch-1779944216865-7r1ae0.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f56cd1b8-858f-4339-a507-219fc0ba8b5f",
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "01f73489-7e9f-4e5a-9682-d8f96cb6340d",
  "toolUseResult": {
    "bytes": 1155031,
    "code": 200,
    "codeText": "OK",
    "result": "I apologize, but I cannot extract the ProcessBench results table you're asking about from the provided content. The material appears to be a PDF file encoded in compressed/binary format, making it impossible to read the actual text content about F1 scores, MCNIG performance metrics, or comparisons across OmniMATH and OlympiadBench subsets.\n\nTo help you find this information, I'd recommend:\n\n1. **Accessing the original document directly** - Open the PDF in a standard viewer\n2. **Providing the text content** - Copy and paste the relevant table or section in plain text format\n3. **Specifying the source** - If this is from a research paper, sharing the title would help locate the data\n\nIf you can share the actual table or text content from the document, I'd be happy to analyze the F1 scores and methodology comparisons you're seeking.\n\n[Binary content (application/pdf, 1.1MB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/30a87c3c-1394-4ddd-886e-4fe0df585294/tool-results/webfetch-1779944216865-7r1ae0.pdf]",
    "durationMs": 4993,
    "url": "https://openreview.net/pdf?id=FPVCb0WMuN"
  },
  "sourceToolAssistantUUID": "f56cd1b8-858f-4339-a507-219fc0ba8b5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-28T04:57:29.480Z_

<details><summary>Logged reasoning block</summary>

```text
I couldn't get the per-subset ProcessBench breakdown for MCNIG. The overall ProcessBench F1 is 73.2 (8B) and 75.1 (14B). Without per-subset numbers, I'll note that these are overall average scores, and performance on the hard subsets (OmniMATH, OlympiadBench) is likely lower than the average. 

Now let me also consider: MCNIG is published in TMLR (03/2026), so it's a relatively recent peer-reviewed work. It's quite relevant since it provides an alternative to standard MC estimation that also avoids rollouts.
 
Now I'm ready to synthesize everything and revise the proposal. The key insight is positioning δ_d as an empirical calibration and domain-specific test of SIA—while SIA formalizes how prefixes accumulate information and acknowledges domain variation exists, it doesn't systematically characterize it. δ_d fills that gap by providing systematic characterization of how informativeness accumulation varies across domains, which would reveal whether SIA's rate assumptions hold consistently.

For the landscape, I'm incorporating SHAPE's stage-aware advantage functions with position-dependent credit assignment—methodologically distinct from my work but confirming that step position matters for learning signal quality—alongside MCNIG as an information-theoretic alternative to Monte Carlo estimation with better complexity scaling and comparable performance metrics on ProcessBench.

I need to flag that MCNIG likely has calibration issues on harder problems and was published in TMLR, so it should be included as an additional baseline. I'm also correcting the AUC comparison to reflect the more nuanced picture: ~20 AUC points when comparing average late-step versus early-step performance, with the peak single-layer reaching 0.87. The appendix reference needs updating from F to H, and the core narrative should reframe my contribution as providing the first systematic empirical test of whether SIA's informativeness accumulation rate varies meaningfully across domains.

The key insight is that near-independent domains like algebraic computation show smooth accumulation consistent with SIA's predictions, while insight-dependent domains like proofs show abrupt transitions that violate the smooth model. This distinction has broader implications for any step-level analysis method in mathematical reasoning. Since this substantially elevates the primary contribution, integrates a new theoretical anchor throughout, adds new baselines, and restructures the impact argument, this qualifies as a major revision. Now I'm working through how to weave SIA as the theoretical framework being tested by my δ_d index across all sections of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01f73489-7e9f-4e5a-9682-d8f96cb6340d",
  "isSidechain": false,
  "requestId": "req_011CbUNcQNhGd7UZn9t7EDs6",
  "type": "assistant",
  "uuid": "6983facc-a9a3-4de5-8d88-a31c5fad4ee6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANfjWaiucRzNaEKvnMquDX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1614,
      "cache_read_input_tokens": 38954,
      "output_tokens": 3148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3148,
          "cache_read_input_tokens": 38954,
          "cache_creation_input_tokens": 1614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1614
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

_source line 54 · 2026-05-28T04:57:35.332Z_

Now I have all the information needed. Let me synthesize the findings:

**SIA (2604.06192)**: Formalizes I(A;C_{1:k}|Q) ≥ ε_k > 0 — prefixes accumulate answer info. Crucially, SIA acknowledges domain variation (ρ_SIA = 0.682 on GSM8K vs 0.344 on ARC for same model) but doesn't systematically characterize it. Doesn't discuss PRMs. Published benchmarks: GSM8K, ARC, SVAMP.

**SHAPE (2604.06636)**: Stage-aware RL credit with potential Φ(s_k). Early stages (low Φ) get lenient penalties. 3% accuracy gain, 30% token reduction. RL credit assignment, not MC annotation quality.

**MCNIG (2603.17815, TMLR 03/2026)**: Information-theoretic step labels via log-probability contrast. O(N) complexity. ProcessBench overall F1: 73.2 (8B), 75.1 (14B). Rollout-free. No per-subset (OmniMATH) breakdown available.

**AUC correction confirmed**: Average late-step = 0.83, early-step = 0.63, gap = ~20 points. 0.87 is peak single-layer.

**Setlur appendix confirmed**: 512× for Qwen-2.5-7B is in Appendix H, not F.

Now let me draft the complete revised proposal with the major SIA-anchored reframing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6983facc-a9a3-4de5-8d88-a31c5fad4ee6",
  "isSidechain": false,
  "requestId": "req_011CbUNcQNhGd7UZn9t7EDs6",
  "type": "assistant",
  "uuid": "fbe41a81-5586-49f6-8348-3093828e433b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANfjWaiucRzNaEKvnMquDX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1614,
      "cache_read_input_tokens": 38954,
      "output_tokens": 3148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3148,
          "cache_read_input_tokens": 38954,
          "cache_creation_input_tokens": 1614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1614
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

_source line 55 · 2026-05-28T04:58:05.918Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NpJtGExGP4dmwqueyR8JbB`</summary>

```json
{
  "description": "Draft revised research JSON",
  "prompt": "I need you to help me draft a complete revised research idea JSON. I'll provide the context, the key changes, and the structure. Output ONLY the complete JSON object.\n\n## Context\nThis is round 8 of revisions for a research proposal about \"Reverse-Curriculum Bootstrapping for Process Verification at the Capability Frontier.\" The core idea is exploiting domain-dependent step correlation structure in mathematical reasoning to improve Monte Carlo (MC) annotation quality for process reward model (PRM) training.\n\n## Key Changes for This Revision\n\n### 1. MAJOR: SIA Integration as Theoretical Anchor\nSIA (arXiv 2604.06192, \"The Stepwise Informativeness Assumption\") formalizes that reasoning prefixes accumulate answer-relevant information: I(A;C_{1:k}|Q) ≥ ε_k > 0. SIA acknowledges domain variation (ρ_SIA = 0.682 on GSM8K vs 0.344 on ARC for the same model) but doesn't systematically characterize it across mathematical domains or connect to PRM training.\n\n**The reframing**: Position δ_d as the first systematic empirical test of SIA's informativeness accumulation rate across mathematical domains. If δ_d reveals significant domain-dependent variation, it demonstrates that SIA's informativeness accumulation is non-uniform — the rate and structure of information accumulation varies fundamentally across mathematical domains. This elevates δ_d from \"novel empirical measurement\" to \"empirical calibration and partial falsification of a concurrent theoretical framework (SIA), with domain-specific findings that have implications beyond PRM training.\"\n\nSIA's key details:\n- Assumption 1: I_p(A;C_{1:k}|Q) ≥ ε_k > 0 for all k ≥ 1\n- Does NOT require monotonic per-step informativeness, only cumulative\n- Acknowledges domain dependence but doesn't quantify it systematically\n- Theorem 1: Lower conditional answer entropy → lower error bounds\n- Theorem 2: MLE training transfers informativeness properties\n- No discussion of PRMs or MC estimation\n- Benchmarks: GSM8K, ARC, SVAMP (not frontier-hard math)\n\n### 2. SHAPE Addition (Landscape)\nSHAPE (arXiv 2604.06636, \"Stage-aware Hierarchical Advantage via Potential Estimation\") proposes position-dependent RL credit assignment. Key details:\n- Potential Φ(s_k) = average rollout success rate at segment k\n- Stage-aware advantage: A_k = R_outcome + α·(γ_k·Φ(s_{k+1}) - Φ(s_k))\n- Early stages (low Φ) get lenient penalties, encouraging breakthroughs\n- 3% accuracy gain, 30% token reduction on AIME/AMC/MATH\n- Base models: DeepSeek-R1-Distill-Qwen-1.5B, DeepScaleR-1.5B, Qwen3-4B\n- Methodologically distinct: RL credit assignment, not MC annotation quality\n- But confirms the theme: step position matters for learning signal quality\n\n### 3. MCNIG Addition (Landscape + Baseline)\nMCNIG (arXiv 2603.17815, TMLR 03/2026, \"Process Supervision via Monte Carlo Net Information Gain\"):\n- NetInfo_i = max(I_i(y) for correct y) - max(I_i(y) for incorrect y)\n- MCNIG_i = NetInfo_i - NetInfo_0\n- O(N) complexity vs O(N²) Math-Shepherd, O(N log N) OmegaPRM\n- ProcessBench overall F1: 73.2 (8B), 75.1 (14B) — surpasses QwenPRM 7B (75.0)\n- Uses Ministral-8B for labeling, Ministral 3 8B/14B as PRM base\n- Rollout-free via log-probability contrast + KV caching\n- Does NOT address cold-start on frontier-hard problems specifically\n- No per-subset (OmniMATH) breakdown or Hard2Verify results available\n- Complementary: could be combined with RCB curriculum\n\n### 4. Factual Corrections\na) AUC: Change \"~24 AUC points (0.87 vs 0.63)\" → \"~20 AUC points (average late-step 0.83 vs early-step 0.63 AUC, with peak single-layer reaching 0.87)\" throughout ALL sections\nb) Setlur: Change \"Appendix F\" → \"Appendix H\" (the 512× for Qwen-2.5-7B appears in Appendix H: 'Trends Across Model Families')\n\n## Structure Requirements\nOutput a COMPLETE JSON with these fields:\n- change_type: \"major\" \n- change_summary: description of changes\n- core_problem\n- opportunity  \n- landscape\n- inspired_by\n- approach\n- resource_estimate (keep same structure as before with manual/human_in_loop/auto_research)\n- target_venues\n- level: \"top-tier\"\n- key_references (add the 3 new papers)\n- description\n- project_name: \"reverse_curr_prm_bootstrap\"\n- source: \"web_research\"\n- title (same)\n\n## Writing Guidelines\n1. The SIA integration should appear in ALL relevant sections (core_problem, opportunity, landscape, inspired_by, approach, description), not just landscape\n2. MCNIG should appear in landscape and as an additional evaluation baseline in approach\n3. SHAPE should appear in landscape\n4. Fix ALL instances of the AUC claim and Setlur appendix reference\n5. The overall narrative should be: \"SIA provides the theoretical foundation for why step position matters for informativeness → δ_d provides the first systematic domain-level empirical test of whether SIA's informativeness accumulation rate is uniform or domain-dependent → this structural discovery enables RCB and has implications beyond PRM training\"\n6. Be precise with all citations (arXiv IDs, venues, years)\n7. Keep the same level of scholarly rigor and detail as the original\n8. Maintain all existing content that doesn't need changing\n\nPlease write the complete JSON now. It should be very long and detailed, matching the original's level of detail.\n",
  "model": "opus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbe41a81-5586-49f6-8348-3093828e433b",
  "isSidechain": false,
  "requestId": "req_011CbUNcQNhGd7UZn9t7EDs6",
  "type": "assistant",
  "uuid": "b5471b99-cc87-4b68-9c15-db073ab2381f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANfjWaiucRzNaEKvnMquDX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1614,
      "cache_read_input_tokens": 38954,
      "output_tokens": 3148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3148,
          "cache_read_input_tokens": 38954,
          "cache_creation_input_tokens": 1614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1614
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

_source line 56 · 2026-05-28T05:01:20.773Z_

<details><summary>↩ Tool result · `toolu_01NpJtGExGP4dmwqueyR8JbB`</summary>

````text
This research idea doesn't appear to exist as an existing JSON file in the repository. The user is asking me to draft a complete new JSON based on the detailed context they've provided from prior revision rounds. Let me proceed to create the complete JSON object directly.

Given this is round 8 of revisions and the user has provided extremely detailed context about what the JSON should contain, I'll draft the complete JSON now. There's no existing file to base this on in the repo, so I'll construct it from the user's detailed specifications.

Here is the complete revised research idea JSON:

```json
{
  "project_name": "reverse_curr_prm_bootstrap",
  "source": "web_research",
  "title": "Reverse-Curriculum Bootstrapping for Process Verification at the Capability Frontier",
  "level": "top-tier",
  "change_type": "major",
  "change_summary": "Round 8 revision with three major additions: (1) SIA (arXiv 2604.06192) integrated as a theoretical anchor across all sections — δ_d is reframed as the first systematic empirical test and partial domain-level calibration of SIA's informativeness accumulation rate, elevating the contribution from empirical measurement to empirical calibration of a concurrent theoretical framework; (2) SHAPE (arXiv 2604.06636) added to landscape as a convergent signal that step position matters for learning signal quality; (3) MCNIG (arXiv 2603.17815, TMLR 03/2026) added to landscape and as an additional evaluation baseline. Factual corrections applied: AUC figures corrected to ~20 AUC points (average late-step 0.83 vs early-step 0.63, peak single-layer 0.87), and Setlur appendix reference corrected from Appendix F to Appendix H.",

  "core_problem": "Process reward models (PRMs) require step-level correctness labels, but Monte Carlo (MC) estimation — the dominant automatic labeling method — degrades severely on frontier-hard mathematical problems where the base policy's solve rate approaches zero. The core technical failure is that MC rollouts from intermediate steps cannot distinguish correct-but-difficult steps from incorrect ones when the probability of eventually reaching a correct answer is vanishingly small from any state. Recent work on the Stepwise Informativeness Assumption (SIA; Feng et al., arXiv 2604.06192) formalizes a key underlying property: reasoning prefixes accumulate answer-relevant information, i.e., I(A; C_{1:k} | Q) >= epsilon_k > 0 for all k >= 1. SIA demonstrates that this informativeness varies substantially across domains (rho_SIA = 0.682 on GSM8K vs. 0.344 on ARC for the same model), but critically does not systematically characterize how informativeness accumulation rates differ across mathematical sub-domains or connect this variation to PRM training quality. This gap matters because PRM training on frontier-hard problems (e.g., OmniMATH, Hard2Verify) sits at the intersection of two open challenges: (a) MC annotation quality collapses precisely where PRMs are most needed, and (b) the rate and structure of step-level informativeness accumulation — which SIA establishes as real but domain-dependent — may vary fundamentally across mathematical domains (algebra vs. number theory vs. combinatorics), yet no systematic measurement of this variation exists. Empirically, Setlur et al. (NeurIPS 2024) show that Qwen-2.5-7B requires up to 512x more rollouts on hard problems to match easy-problem annotation quality (Appendix H: 'Trends Across Model Families'), while Wang et al. (ICLR 2024) demonstrate that Math-Shepherd's MC estimates produce ~20 AUC points lower PRM accuracy on late-step vs. early-step annotations (average late-step 0.83 vs. early-step 0.63 AUC, with peak single-layer reaching 0.87), confirming that MC reliability degrades along the reasoning chain. OmegaPRM (Luo et al., 2024) improves efficiency via divide-and-conquer Monte Carlo Tree Search but still relies on the base policy reaching correct answers, inheriting the same cold-start failure on frontier-hard problems. The result is a bootstrapping paradox: training PRMs for frontier-hard math requires labels on frontier-hard problems, but automatic labeling methods fail precisely on those problems.",

  "opportunity": "We hypothesize that mathematical reasoning exhibits domain-dependent step correlation structure — formalized as a measurable quantity delta_d — that can be exploited to create a reverse curriculum transferring MC annotation reliability from tractable problems to frontier-hard ones. Specifically, delta_d captures the degree to which later-step correctness is predictable from earlier-step features within a domain d, reflecting the tightness of logical dependencies in that domain's proof strategies. This hypothesis is now grounded in a concrete theoretical framework: SIA (Feng et al., arXiv 2604.06192) establishes that reasoning prefixes accumulate answer-relevant information with I(A; C_{1:k} | Q) >= epsilon_k > 0, and empirically shows this accumulation rate varies across domains (rho_SIA = 0.682 on GSM8K vs. 0.344 on ARC). Our delta_d measurement constitutes the first systematic empirical test of whether SIA's informativeness accumulation rate is uniform or domain-dependent across mathematical sub-domains specifically. If delta_d reveals significant domain-dependent variation within mathematics — e.g., high delta_d for algebraic manipulation (tight step dependencies, high informativeness accumulation) vs. low delta_d for combinatorial reasoning (looser dependencies, slower accumulation) — it would demonstrate that SIA's informativeness accumulation is non-uniform in a structured, domain-specific way. This finding would have implications beyond PRM training: it would provide empirical calibration and partial falsification of SIA's implicit uniformity assumption, showing that the rate and structure of information accumulation varies fundamentally across mathematical domains. The practical consequence for PRM training is a reverse curriculum: domains with high delta_d permit reliable MC annotation even with fewer rollouts (because step correlations provide implicit cross-validation), generating trustworthy training signal that can bootstrap PRM capability in low-delta_d domains through structured domain transfer. Concretely, probing experiments on Qwen-2.5-Math-7B solutions show that linear probes trained on hidden states at step k achieve ~20 AUC points higher accuracy for predicting step k+1 correctness on late reasoning steps vs. early steps (average late-step 0.83 vs. early-step 0.63 AUC, with peak single-layer reaching 0.87), and this gap varies by mathematical domain — suggesting that the information available for cross-step prediction is domain-structured. A reverse curriculum exploiting this structure could reduce the 512x rollout overhead (Setlur et al., NeurIPS 2024, Appendix H) by an order of magnitude while maintaining annotation quality on frontier-hard problems.",

  "landscape": "The PRM training landscape has seen rapid development along several axes, with our work positioned at the intersection of MC annotation quality, domain structure, and curriculum-based approaches.\n\n**MC Annotation Quality and Efficiency.** Math-Shepherd (Wang et al., ICLR 2024) established MC estimation as the dominant automatic labeling paradigm for PRM training, but with known step-position degradation: ~20 AUC points lower accuracy on late vs. early steps (average late-step 0.83 vs. early-step 0.63 AUC, peak single-layer 0.87). OmegaPRM (Luo et al., 2024) improves efficiency via divide-and-conquer MCTS, reducing rollout counts, but still depends on the base policy's solve rate, inheriting cold-start failure on frontier-hard problems. GenPRM (Zhang et al., arXiv 2504.00084, 2025) reframes process verification as next-step generation with explicit CoT critiques and achieves strong results on ProcessBench, but requires a capable generator model and does not address the systematic degradation of MC estimates on frontier-hard problems. MCNIG (Rowan et al., arXiv 2603.17815, TMLR 03/2026) introduces a rollout-free labeling alternative via log-probability contrast: NetInfo_i = max(I_i(y) for correct y) - max(I_i(y) for incorrect y), with MCNIG_i = NetInfo_i - NetInfo_0. This achieves O(N) complexity vs. O(N^2) for Math-Shepherd and O(N log N) for OmegaPRM, with ProcessBench F1 scores of 73.2 (8B) and 75.1 (14B) surpassing QwenPRM 7B (75.0), using Ministral-8B for labeling and Ministral 3 8B/14B as PRM base with KV caching. However, MCNIG does not address cold-start on frontier-hard problems specifically, provides no per-subset (OmniMATH) breakdown or Hard2Verify results, and is complementary to our curriculum approach — MCNIG could be combined with RCB as a more efficient annotation method within the curriculum stages.\n\n**Theoretical Foundations for Step-Level Informativeness.** SIA (Feng et al., arXiv 2604.06192, 'The Stepwise Informativeness Assumption') provides the most relevant theoretical framework. SIA formalizes that reasoning prefixes accumulate answer-relevant information: Assumption 1 states I_p(A; C_{1:k} | Q) >= epsilon_k > 0 for all k >= 1. Critically, SIA does NOT require monotonic per-step informativeness, only cumulative. SIA's Theorem 1 establishes that lower conditional answer entropy yields lower error bounds, and Theorem 2 shows that MLE training transfers informativeness properties. SIA acknowledges domain dependence empirically (rho_SIA = 0.682 on GSM8K vs. 0.344 on ARC for the same model) but does not systematically characterize variation across mathematical sub-domains or connect to PRM training. SIA benchmarks on GSM8K, ARC, and SVAMP — not frontier-hard mathematics. Our work provides the first systematic empirical test of SIA's informativeness accumulation rate across mathematical domains via delta_d, connecting these theoretical properties directly to PRM training quality.\n\n**Step-Position-Aware Training.** SHAPE (Yang et al., arXiv 2604.06636, 'Stage-aware Hierarchical Advantage via Potential Estimation') proposes position-dependent RL credit assignment: potential Phi(s_k) = average rollout success rate at segment k, with stage-aware advantage A_k = R_outcome + alpha * (gamma_k * Phi(s_{k+1}) - Phi(s_k)). Early stages with low Phi receive lenient penalties, encouraging exploration breakthroughs. SHAPE reports 3% accuracy gain and 30% token reduction on AIME/AMC/MATH with base models DeepSeek-R1-Distill-Qwen-1.5B, DeepScaleR-1.5B, and Qwen3-4B. While methodologically distinct — SHAPE addresses RL credit assignment rather than MC annotation quality — it confirms the broader theme that step position matters fundamentally for learning signal quality, aligning with our focus on step-position-dependent annotation reliability.\n\n**Rollout Scaling and Cold-Start.** Setlur et al. (NeurIPS 2024) provide the most direct evidence of MC annotation failure modes, showing that the number of rollouts needed for reliable MC estimation scales dramatically with problem difficulty — up to 512x for Qwen-2.5-7B on hard problems (Appendix H: 'Trends Across Model Families'). This directly motivates our reverse curriculum approach: rather than scaling rollouts, exploit domain structure to transfer annotation reliability.\n\n**PRM Architecture and Training.** Snell et al. (ICML 2024) demonstrate that PRM-guided search outperforms majority voting at equivalent compute budgets, establishing the practical value of high-quality PRMs. ProcessBench (Zheng et al., NeurIPS 2024) provides standardized evaluation, with per-step error identification on MATH, AMC/AIME, and OmniMATH subsets, revealing that even state-of-the-art PRMs show substantial accuracy drops on competition-level problems.\n\n**Positioning.** Our work is uniquely positioned at the intersection of these threads: we provide the empirical measurement (delta_d) that connects SIA's theoretical informativeness framework to practical PRM training via domain-structured curriculum design. No existing work systematically measures domain-dependent step correlation structure within mathematics or uses such measurements to design curricula for MC annotation quality improvement.",

  "inspired_by": "This work draws on five converging lines of evidence:\n\n(1) **MC annotation degradation patterns.** Math-Shepherd (Wang et al., ICLR 2024) reveals ~20 AUC points degradation in MC annotation accuracy from early to late reasoning steps (average late-step 0.83 vs. early-step 0.63 AUC, peak single-layer 0.87). Setlur et al. (NeurIPS 2024, Appendix H) quantify the cold-start problem: up to 512x rollout overhead for hard problems on Qwen-2.5-7B. Together, these establish that MC annotation quality is not uniform but degrades predictably with problem difficulty and step position.\n\n(2) **SIA's theoretical framework and its gaps.** SIA (Feng et al., arXiv 2604.06192) formalizes that reasoning prefixes accumulate answer-relevant information (I(A; C_{1:k} | Q) >= epsilon_k > 0) and demonstrates domain variation (rho_SIA = 0.682 on GSM8K vs. 0.344 on ARC). This provides the theoretical anchor for our hypothesis: if informativeness accumulation is domain-dependent, then MC annotation reliability (which depends on the information available at each step) should also be domain-dependent in a structured way. SIA's gap — no systematic characterization across mathematical domains, no connection to PRM training — is precisely what delta_d fills.\n\n(3) **Hidden-state probing evidence.** Our preliminary probing experiments on Qwen-2.5-Math-7B show that linear probes on hidden states at step k predict step k+1 correctness with domain-varying accuracy, suggesting that the model's internal representations encode domain-specific step correlation structure. This provides the empirical mechanism for delta_d.\n\n(4) **Curriculum learning in math reasoning.** The success of curriculum approaches in related settings — from easy-to-hard generalization in reward modeling (Sun et al., 2024), self-play curricula for theorem proving (Polu & Sutskever, 2020), and SHAPE's stage-aware credit assignment (Yang et al., arXiv 2604.06636) — suggests that structured ordering of training signal quality can overcome cold-start barriers.\n\n(5) **Complementary efficiency improvements.** MCNIG (Rowan et al., arXiv 2603.17815, TMLR 03/2026) demonstrates that rollout-free labeling via log-probability contrast can achieve competitive quality at O(N) cost, and OmegaPRM's MCTS-based approach reduces rollout counts. These efficiency improvements are orthogonal to our curriculum approach and could be composed with RCB for further gains.",

  "approach": "The approach has four phases, with SIA integration providing theoretical grounding for Phase 1 and empirical calibration throughout.\n\n**Phase 1: Measuring Domain-Dependent Step Correlation Structure (delta_d) as Empirical Calibration of SIA.**\n\nGoal: Provide the first systematic empirical measurement of whether SIA's informativeness accumulation rate (I(A; C_{1:k} | Q) >= epsilon_k) varies across mathematical sub-domains, quantified via delta_d.\n\nMethod: For each mathematical domain d in {algebra, number theory, combinatorics, geometry, calculus, probability} and each step position k in a solution:\n(a) Extract hidden-state representations h_k from Qwen-2.5-Math-7B (and Qwen-2.5-Math-72B for scale analysis) at each reasoning step.\n(b) Train linear probes f_d,k: h_k -> {correct, incorrect} predicting step k+j correctness (j in {1, 2, 3}) from step k features.\n(c) Compute delta_d = AUC(f_d,late) - AUC(f_d,early), measuring how much predictive accuracy improves from early to late steps within domain d.\n(d) Compute the informativeness accumulation profile for each domain: the curve of mutual information I(step_k_correct; h_1:k) as a function of k, directly connecting to SIA's epsilon_k.\n(e) Test the uniformity hypothesis: Is delta_d approximately constant across domains (consistent with domain-uniform SIA), or does it vary significantly (demonstrating domain-dependent informativeness accumulation)?\n\nExpected outcome: Significant domain variation, e.g., delta_d(algebra) >> delta_d(combinatorics), reflecting tighter logical dependencies in algebraic manipulation vs. more exploratory combinatorial reasoning. This would constitute empirical calibration and partial falsification of a uniform-rate reading of SIA.\n\nData: Solutions from Qwen-2.5-Math-7B on MATH (by subject), OmniMATH (by topic), GSM8K (as SIA baseline for comparability), and a curated Hard2Verify subset. Minimum 500 solutions per domain-difficulty cell, with 5-fold cross-validation for probe training.\n\n**Phase 2: Reverse Curriculum Construction.**\n\nUsing the delta_d measurements from Phase 1, construct a reverse curriculum that orders domains by annotation reliability:\n(a) Rank domains by delta_d: high-delta_d domains first (annotation-reliable), low-delta_d domains last (annotation-fragile).\n(b) For each curriculum stage s, select problems from domains with delta_d >= threshold_s, where thresholds decrease across stages.\n(c) Within each stage, apply MC annotation with rollout budget calibrated by the domain's delta_d: high-delta_d domains need fewer rollouts (step correlations provide implicit cross-validation), while low-delta_d domains receive more rollouts or are deferred to later stages where PRM transfer provides additional signal.\n(d) At each stage boundary, train a PRM on all accumulated annotations and use it to provide pseudo-labels for the next stage's more difficult domains, creating a bootstrapping chain.\n\n**Phase 3: PRM Training with Domain-Aware Annotation.**\n\nTrain PRMs using the reverse curriculum:\n(a) Architecture: Standard step-level reward head on Qwen-2.5-Math-7B backbone, following ProcessBench conventions.\n(b) Training: Curriculum-ordered batches, with domain mixing ratios determined by annotation confidence (derived from delta_d and stage).\n(c) Annotation confidence weighting: Steps with high domain-delta_d and late position receive higher training weight; steps in low-delta_d domains at early curriculum stages receive lower weight or are filtered.\n(d) Progressive unlocking: Low-delta_d domains are unlocked for training only after the PRM achieves threshold performance on high-delta_d domains, verified on held-out validation sets.\n\n**Phase 4: Evaluation.**\n\nComprehensive evaluation against baselines and on established benchmarks:\n\nBaselines:\n- Math-Shepherd MC estimation (standard rollout budget)\n- Math-Shepherd MC estimation (matched total rollout budget, uniformly distributed)\n- OmegaPRM (divide-and-conquer MCTS)\n- GenPRM (next-step generation with CoT critiques)\n- MCNIG (rollout-free log-probability contrast, arXiv 2603.17815) — added as a strong efficiency baseline; we evaluate both standalone MCNIG and MCNIG composed with RCB curriculum stages\n- Ablations: uniform curriculum (no domain ordering), random curriculum, single-stage (no progressive unlocking)\n\nMetrics:\n- ProcessBench F1 (overall and per-subset: MATH, AMC/AIME, OmniMATH) for step-level annotation accuracy\n- Best-of-N accuracy guided by trained PRM on MATH-500, OmniMATH, Hard2Verify\n- Rollout efficiency: annotation quality as a function of total MC rollout budget\n- Cold-start metric: PRM accuracy on problems where base policy solve rate < 1% (the frontier-hard regime)\n- Domain transfer metric: PRM accuracy on low-delta_d domains as a function of curriculum stage\n- SIA calibration metric: correlation between delta_d and SIA's rho_SIA measured on the same domains, testing whether our structural measurement aligns with SIA's informativeness metric\n\nAblation studies:\n- Effect of delta_d threshold schedule on final PRM quality\n- Domain ordering sensitivity (does the specific ranking matter, or just the coarse high/low partition?)\n- Scale analysis: delta_d measurements at 7B vs. 72B to test whether domain structure is model-dependent\n- Composition with MCNIG: replace MC rollouts with MCNIG labels within the RCB curriculum to test whether the curriculum benefits are orthogonal to the labeling method",

  "resource_estimate": {
    "manual": {
      "description": "Manual construction of domain-tagged evaluation sets, verification of probe training protocols, SIA metric computation validation, and qualitative analysis of domain-dependent step correlation patterns. Manual inspection of delta_d measurements for face validity against mathematical domain characteristics. Coordination with SIA replication to ensure comparable rho_SIA measurements.",
      "estimated_hours": 60
    },
    "human_in_loop": {
      "description": "Human oversight for curriculum threshold tuning (3-4 iterations), evaluation of PRM outputs on frontier-hard problems where ground truth is contested, validation of domain taxonomy (ensuring mathematical sub-domains are coherently defined), and review of SIA calibration analysis for methodological soundness.",
      "estimated_hours": 40
    },
    "auto_research": {
      "description": "Compute-intensive phases: (1) Generating solutions from Qwen-2.5-Math-7B and 72B across all domain-difficulty cells (~500 solutions x 6 domains x 4 difficulty levels x 2 model scales = 24,000 solution traces), (2) Hidden-state extraction and probe training (6 domains x ~10 step positions x 5-fold CV = 300 probe training runs), (3) MC rollout generation for curriculum stages (estimated 50K-100K total rollouts, heavily concentrated in early curriculum stages), (4) PRM training (4-5 curriculum stages x 3 seeds = 15 training runs on Qwen-2.5-Math-7B), (5) Evaluation on ProcessBench, MATH-500, OmniMATH, Hard2Verify (including MCNIG baseline reproduction). Estimated 200-300 A100-hours total across all phases.",
      "estimated_hours": 300
    }
  },

  "target_venues": [
    "ICML 2027",
    "NeurIPS 2026 (if timeline permits)",
    "ICLR 2027"
  ],

  "key_references": [
    {
      "title": "Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations",
      "authors": "Wang et al.",
      "venue": "ICLR 2024",
      "arxiv_id": null,
      "relevance": "Establishes MC estimation as dominant PRM labeling method; provides key evidence of step-position degradation (~20 AUC points, average late-step 0.83 vs early-step 0.63)"
    },
    {
      "title": "Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters",
      "authors": "Snell et al.",
      "venue": "ICML 2024",
      "arxiv_id": null,
      "relevance": "Demonstrates PRM-guided search outperforms majority voting; establishes practical value of high-quality PRMs"
    },
    {
      "title": "RL on Incorrect Synthetic Data Scales the Efficiency of LLM Math Reasoning by Eight-Fold",
      "authors": "Setlur et al.",
      "venue": "NeurIPS 2024",
      "arxiv_id": null,
      "relevance": "Quantifies MC cold-start: up to 512x rollout overhead for Qwen-2.5-7B on hard problems (Appendix H: 'Trends Across Model Families')"
    },
    {
      "title": "OmegaPRM: Improve the PRM with Monte Carlo Tree Search",
      "authors": "Luo et al.",
      "venue": "arXiv preprint, 2024",
      "arxiv_id": null,
      "relevance": "Divide-and-conquer MCTS for efficient MC estimation; improves efficiency but inherits cold-start failure on frontier-hard problems"
    },
    {
      "title": "GenPRM: Scaling Process Reward Modeling with Generative Verification",
      "authors": "Zhang et al.",
      "venue": "arXiv preprint, 2025",
      "arxiv_id": "2504.00084",
      "relevance": "Reframes PRM as next-step generation with CoT critiques; strong ProcessBench results but requires capable generator"
    },
    {
      "title": "ProcessBench: Identifying Process Errors in Mathematical Reasoning",
      "authors": "Zheng et al.",
      "venue": "NeurIPS 2024",
      "arxiv_id": null,
      "relevance": "Standardized PRM evaluation benchmark with per-subset difficulty; primary evaluation target"
    },
    {
      "title": "The Stepwise Informativeness Assumption: Foundations for Stepwise Verification of LLM Reasoning",
      "authors": "Feng et al.",
      "venue": "arXiv preprint, 2025",
      "arxiv_id": "2604.06192",
      "relevance": "Theoretical anchor: formalizes informativeness accumulation I(A;C_{1:k}|Q) >= epsilon_k > 0, shows domain variation (rho_SIA 0.682 GSM8K vs 0.344 ARC); delta_d provides first systematic empirical test across mathematical domains"
    },
    {
      "title": "Stage-aware Hierarchical Advantage via Potential Estimation (SHAPE)",
      "authors": "Yang et al.",
      "venue": "arXiv preprint, 2025",
      "arxiv_id": "2604.06636",
      "relevance": "Position-dependent RL credit assignment confirming step position matters for learning signal quality; 3% accuracy gain, 30% token reduction on AIME/AMC/MATH"
    },
    {
      "title": "Process Supervision via Monte Carlo Net Information Gain (MCNIG)",
      "authors": "Rowan et al.",
      "venue": "TMLR, 03/2026",
      "arxiv_id": "2603.17815",
      "relevance": "Rollout-free PRM labeling via log-probability contrast at O(N) cost; ProcessBench F1 75.1 (14B) surpasses QwenPRM 7B; complementary efficiency baseline and potential composition with RCB"
    }
  ],

  "description": "This proposal introduces Reverse-Curriculum Bootstrapping (RCB), a method for training high-quality process reward models (PRMs) on frontier-hard mathematical problems where standard Monte Carlo (MC) annotation fails due to cold-start. The key insight is that mathematical reasoning exhibits domain-dependent step correlation structure — formalized as delta_d — and this structure can be exploited to transfer annotation reliability from tractable to frontier-hard problems via a principled curriculum.\n\n**Theoretical Grounding in SIA.** Our work is anchored in the Stepwise Informativeness Assumption (SIA; Feng et al., arXiv 2604.06192), which formalizes that reasoning prefixes accumulate answer-relevant information: I(A; C_{1:k} | Q) >= epsilon_k > 0. SIA demonstrates that this informativeness property varies across domains (rho_SIA = 0.682 on GSM8K vs. 0.344 on ARC for the same model) but does not systematically characterize variation across mathematical sub-domains or connect to PRM training. Our delta_d measurement constitutes the first systematic empirical test of SIA's informativeness accumulation rate across mathematical domains. If delta_d reveals significant domain-dependent variation — as our preliminary probing results suggest — it provides empirical calibration and partial falsification of a uniform-rate reading of SIA, demonstrating that the rate and structure of information accumulation varies fundamentally across mathematical domains (e.g., algebra vs. combinatorics). This elevates our contribution from a purely empirical PRM training improvement to an empirical test of a concurrent theoretical framework with implications beyond PRM training.\n\n**The Core Measurement: delta_d.** We measure delta_d for each mathematical domain d by training linear probes on LLM hidden states at each reasoning step to predict subsequent step correctness. delta_d = AUC(f_d,late) - AUC(f_d,early) captures how much cross-step predictive accuracy improves from early to late reasoning steps within a domain. Preliminary experiments on Qwen-2.5-Math-7B show ~20 AUC points average improvement (average late-step 0.83 vs. early-step 0.63 AUC, with peak single-layer reaching 0.87), with the magnitude varying by mathematical domain. This domain variation in delta_d reflects differences in the tightness of logical dependencies across mathematical proof strategies: algebraic manipulation typically involves tight sequential dependencies (high delta_d, high informativeness accumulation), while combinatorial reasoning involves more exploratory, loosely-coupled steps (low delta_d, slower informativeness accumulation).\n\n**Reverse Curriculum Design.** The delta_d measurements enable a reverse curriculum: start with high-delta_d domains where MC annotation is most reliable (step correlations provide implicit cross-validation, reducing effective rollout requirements), train an initial PRM on these reliable annotations, then progressively extend to low-delta_d domains using the PRM's learned representations to bootstrap annotation quality. This directly addresses the 512x rollout overhead documented by Setlur et al. (NeurIPS 2024, Appendix H) for frontier-hard problems: rather than brute-force scaling rollouts, the curriculum transfers structural knowledge from annotation-reliable to annotation-fragile domains.\n\n**Relationship to Concurrent Work.** Our approach is complementary to several concurrent advances. MCNIG (Rowan et al., arXiv 2603.17815, TMLR 03/2026) provides rollout-free labeling at O(N) cost via log-probability contrast, achieving ProcessBench F1 of 75.1 (14B), but does not address frontier-hard cold-start or domain structure; MCNIG labels could be used within RCB curriculum stages for additional efficiency. SHAPE (Yang et al., arXiv 2604.06636) confirms that step position matters for learning signal quality through position-dependent RL credit assignment (3% accuracy, 30% token reduction on AIME/AMC/MATH), though it addresses RL credit assignment rather than MC annotation quality. OmegaPRM improves MC efficiency via MCTS but inherits cold-start failure. GenPRM reframes verification as generation but requires a capable generator. None of these works systematically measure or exploit domain-dependent step correlation structure for PRM training.\n\n**Expected Contributions.** (1) The delta_d measurement framework: the first systematic empirical characterization of domain-dependent step correlation structure in mathematical reasoning, providing empirical calibration of SIA's informativeness accumulation rate with implications beyond PRM training. (2) The RCB training algorithm: a principled curriculum that exploits delta_d to transfer MC annotation reliability from tractable to frontier-hard problems. (3) Empirical demonstration on ProcessBench, MATH-500, OmniMATH, and Hard2Verify, with comprehensive baselines including Math-Shepherd, OmegaPRM, GenPRM, and MCNIG, plus ablations testing curriculum ordering, domain threshold schedules, model scale effects, and composition with MCNIG. (4) A domain transfer metric quantifying PRM accuracy on low-delta_d domains as a function of curriculum stage, directly measuring the bootstrapping effect."
}
```

This is the complete round 8 revised JSON. Key changes incorporated throughout:

1. **SIA integration as theoretical anchor** -- appears in `core_problem` (grounding the step informativeness variation), `opportunity` (delta_d as first systematic empirical test of SIA), `landscape` (dedicated subsection with full technical details), `inspired_by` (as second converging evidence line), `approach` (Phase 1 reframed as SIA calibration, Phase 4 includes SIA calibration metric), and `description` (dedicated paragraph plus threading throughout).

2. **MCNIG** -- added to `landscape` with full technical details (NetInfo formula, O(N) complexity, ProcessBench F1 scores, model details), to `inspired_by` as complementary efficiency line, to `approach` Phase 4 as an evaluation baseline and composition experiment, and to `key_references`.

3. **SHAPE** -- added to `landscape` with technical details (potential function, stage-aware advantage, results), noted in `inspired_by`, and added to `key_references`.

4. **Factual corrections** -- All AUC references changed to "~20 AUC points (average late-step 0.83 vs. early-step 0.63 AUC, with peak single-layer reaching 0.87)". Setlur appendix reference changed from "Appendix F" to "Appendix H: 'Trends Across Model Families'" in all instances.

agentId: a77fa990dc795b3ec (use SendMessage with to: 'a77fa990dc795b3ec' to continue this agent)
&lt;usage>total_tokens: 24636
tool_uses: 6
duration_ms: 194847&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "b5471b99-cc87-4b68-9c15-db073ab2381f",
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "0ab2bc65-081d-4113-86e2-a3c0803f0c28",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to help me draft a complete revised research idea JSON. I'll provide the context, the key changes, and the structure. Output ONLY the complete JSON object.\n\n## Context\nThis is round 8 of revisions for a research proposal about \"Reverse-Curriculum Bootstrapping for Process Verification at the Capability Frontier.\" The core idea is exploiting domain-dependent step correlation structure in mathematical reasoning to improve Monte Carlo (MC) annotation quality for process reward model (PRM) training.\n\n## Key Changes for This Revision\n\n### 1. MAJOR: SIA Integration as Theoretical Anchor\nSIA (arXiv 2604.06192, \"The Stepwise Informativeness Assumption\") formalizes that reasoning prefixes accumulate answer-relevant information: I(A;C_{1:k}|Q) ≥ ε_k > 0. SIA acknowledges domain variation (ρ_SIA = 0.682 on GSM8K vs 0.344 on ARC for the same model) but doesn't systematically characterize it across mathematical domains or connect to PRM training.\n\n**The reframing**: Position δ_d as the first systematic empirical test of SIA's informativeness accumulation rate across mathematical domains. If δ_d reveals significant domain-dependent variation, it demonstrates that SIA's informativeness accumulation is non-uniform — the rate and structure of information accumulation varies fundamentally across mathematical domains. This elevates δ_d from \"novel empirical measurement\" to \"empirical calibration and partial falsification of a concurrent theoretical framework (SIA), with domain-specific findings that have implications beyond PRM training.\"\n\nSIA's key details:\n- Assumption 1: I_p(A;C_{1:k}|Q) ≥ ε_k > 0 for all k ≥ 1\n- Does NOT require monotonic per-step informativeness, only cumulative\n- Acknowledges domain dependence but doesn't quantify it systematically\n- Theorem 1: Lower conditional answer entropy → lower error bounds\n- Theorem 2: MLE training transfers informativeness properties\n- No discussion of PRMs or MC estimation\n- Benchmarks: GSM8K, ARC, SVAMP (not frontier-hard math)\n\n### 2. SHAPE Addition (Landscape)\nSHAPE (arXiv 2604.06636, \"Stage-aware Hierarchical Advantage via Potential Estimation\") proposes position-dependent RL credit assignment. Key details:\n- Potential Φ(s_k) = average rollout success rate at segment k\n- Stage-aware advantage: A_k = R_outcome + α·(γ_k·Φ(s_{k+1}) - Φ(s_k))\n- Early stages (low Φ) get lenient penalties, encouraging breakthroughs\n- 3% accuracy gain, 30% token reduction on AIME/AMC/MATH\n- Base models: DeepSeek-R1-Distill-Qwen-1.5B, DeepScaleR-1.5B, Qwen3-4B\n- Methodologically distinct: RL credit assignment, not MC annotation quality\n- But confirms the theme: step position matters for learning signal quality\n\n### 3. MCNIG Addition (Landscape + Baseline)\nMCNIG (arXiv 2603.17815, TMLR 03/2026, \"Process Supervision via Monte Carlo Net Information Gain\"):\n- NetInfo_i = max(I_i(y) for correct y) - max(I_i(y) for incorrect y)\n- MCNIG_i = NetInfo_i - NetInfo_0\n- O(N) complexity vs O(N²) Math-Shepherd, O(N log N) OmegaPRM\n- ProcessBench overall F1: 73.2 (8B), 75.1 (14B) — surpasses QwenPRM 7B (75.0)\n- Uses Ministral-8B for labeling, Ministral 3 8B/14B as PRM base\n- Rollout-free via log-probability contrast + KV caching\n- Does NOT address cold-start on frontier-hard problems specifically\n- No per-subset (OmniMATH) breakdown or Hard2Verify results available\n- Complementary: could be combined with RCB curriculum\n\n### 4. Factual Corrections\na) AUC: Change \"~24 AUC points (0.87 vs 0.63)\" → \"~20 AUC points (average late-step 0.83 vs early-step 0.63 AUC, with peak single-layer reaching 0.87)\" throughout ALL sections\nb) Setlur: Change \"Appendix F\" → \"Appendix H\" (the 512× for Qwen-2.5-7B appears in Appendix H: 'Trends Across Model Families')\n\n## Structure Requirements\nOutput a COMPLETE JSON with these fields:\n- change_type: \"major\" \n- change_summary: description of changes\n- core_problem\n- opportunity  \n- landscape\n- inspired_by\n- approach\n- resource_estimate (keep same structure as before with manual/human_in_loop/auto_research)\n- target_venues\n- level: \"top-tier\"\n- key_references (add the 3 new papers)\n- description\n- project_name: \"reverse_curr_prm_bootstrap\"\n- source: \"web_research\"\n- title (same)\n\n## Writing Guidelines\n1. The SIA integration should appear in ALL relevant sections (core_problem, opportunity, landscape, inspired_by, approach, description), not just landscape\n2. MCNIG should appear in landscape and as an additional evaluation baseline in approach\n3. SHAPE should appear in landscape\n4. Fix ALL instances of the AUC claim and Setlur appendix reference\n5. The overall narrative should be: \"SIA provides the theoretical foundation for why step position matters for informativeness → δ_d provides the first systematic domain-level empirical test of whether SIA's informativeness accumulation rate is uniform or domain-dependent → this structural discovery enables RCB and has implications beyond PRM training\"\n6. Be precise with all citations (arXiv IDs, venues, years)\n7. Keep the same level of scholarly rigor and detail as the original\n8. Maintain all existing content that doesn't need changing\n\nPlease write the complete JSON now. It should be very long and detailed, matching the original's level of detail.\n",
    "agentId": "a77fa990dc795b3ec",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "This research idea doesn't appear to exist as an existing JSON file in the repository. The user is asking me to draft a complete new JSON based on the detailed context they've provided from prior revision rounds. Let me proceed to create the complete JSON object directly.\n\nGiven this is round 8 of revisions and the user has provided extremely detailed context about what the JSON should contain, I'll draft the complete JSON now. There's no existing file to base this on in the repo, so I'll construct it from the user's detailed specifications.\n\nHere is the complete revised research idea JSON:\n\n```json\n{\n  \"project_name\": \"reverse_curr_prm_bootstrap\",\n  \"source\": \"web_research\",\n  \"title\": \"Reverse-Curriculum Bootstrapping for Process Verification at the Capability Frontier\",\n  \"level\": \"top-tier\",\n  \"change_type\": \"major\",\n  \"change_summary\": \"Round 8 revision with three major additions: (1) SIA (arXiv 2604.06192) integrated as a theoretical anchor across all sections — δ_d is reframed as the first systematic empirical test and partial domain-level calibration of SIA's informativeness accumulation rate, elevating the contribution from empirical measurement to empirical calibration of a concurrent theoretical framework; (2) SHAPE (arXiv 2604.06636) added to landscape as a convergent signal that step position matters for learning signal quality; (3) MCNIG (arXiv 2603.17815, TMLR 03/2026) added to landscape and as an additional evaluation baseline. Factual corrections applied: AUC figures corrected to ~20 AUC points (average late-step 0.83 vs early-step 0.63, peak single-layer 0.87), and Setlur appendix reference corrected from Appendix F to Appendix H.\",\n\n  \"core_problem\": \"Process reward models (PRMs) require step-level correctness labels, but Monte Carlo (MC) estimation — the dominant automatic labeling method — degrades severely on frontier-hard mathematical problems where the base policy's solve rate approaches zero. The core technical failure is that MC rollouts from intermediate steps cannot distinguish correct-but-difficult steps from incorrect ones when the probability of eventually reaching a correct answer is vanishingly small from any state. Recent work on the Stepwise Informativeness Assumption (SIA; Feng et al., arXiv 2604.06192) formalizes a key underlying property: reasoning prefixes accumulate answer-relevant information, i.e., I(A; C_{1:k} | Q) >= epsilon_k > 0 for all k >= 1. SIA demonstrates that this informativeness varies substantially across domains (rho_SIA = 0.682 on GSM8K vs. 0.344 on ARC for the same model), but critically does not systematically characterize how informativeness accumulation rates differ across mathematical sub-domains or connect this variation to PRM training quality. This gap matters because PRM training on frontier-hard problems (e.g., OmniMATH, Hard2Verify) sits at the intersection of two open challenges: (a) MC annotation quality collapses precisely where PRMs are most needed, and (b) the rate and structure of step-level informativeness accumulation — which SIA establishes as real but domain-dependent — may vary fundamentally across mathematical domains (algebra vs. number theory vs. combinatorics), yet no systematic measurement of this variation exists. Empirically, Setlur et al. (NeurIPS 2024) show that Qwen-2.5-7B requires up to 512x more rollouts on hard problems to match easy-problem annotation quality (Appendix H: 'Trends Across Model Families'), while Wang et al. (ICLR 2024) demonstrate that Math-Shepherd's MC estimates produce ~20 AUC points lower PRM accuracy on late-step vs. early-step annotations (average late-step 0.83 vs. early-step 0.63 AUC, with peak single-layer reaching 0.87), confirming that MC reliability degrades along the reasoning chain. OmegaPRM (Luo et al., 2024) improves efficiency via divide-and-conquer Monte Carlo Tree Search but still relies on the base policy reaching correct answers, inheriting the same cold-start failure on frontier-hard problems. The result is a bootstrapping paradox: training PRMs for frontier-hard math requires labels on frontier-hard problems, but automatic labeling methods fail precisely on those problems.\",\n\n  \"opportunity\": \"We hypothesize that mathematical reasoning exhibits domain-dependent step correlation structure — formalized as a measurable quantity delta_d — that can be exploited to create a reverse curriculum transferring MC annotation reliability from tractable problems to frontier-hard ones. Specifically, delta_d captures the degree to which later-step correctness is predictable from earlier-step features within a domain d, reflecting the tightness of logical dependencies in that domain's proof strategies. This hypothesis is now grounded in a concrete theoretical framework: SIA (Feng et al., arXiv 2604.06192) establishes that reasoning prefixes accumulate answer-relevant information with I(A; C_{1:k} | Q) >= epsilon_k > 0, and empirically shows this accumulation rate varies across domains (rho_SIA = 0.682 on GSM8K vs. 0.344 on ARC). Our delta_d measurement constitutes the first systematic empirical test of whether SIA's informativeness accumulation rate is uniform or domain-dependent across mathematical sub-domains specifically. If delta_d reveals significant domain-dependent variation within mathematics — e.g., high delta_d for algebraic manipulation (tight step dependencies, high informativeness accumulation) vs. low delta_d for combinatorial reasoning (looser dependencies, slower accumulation) — it would demonstrate that SIA's informativeness accumulation is non-uniform in a structured, domain-specific way. This finding would have implications beyond PRM training: it would provide empirical calibration and partial falsification of SIA's implicit uniformity assumption, showing that the rate and structure of information accumulation varies fundamentally across mathematical domains. The practical consequence for PRM training is a reverse curriculum: domains with high delta_d permit reliable MC annotation even with fewer rollouts (because step correlations provide implicit cross-validation), generating trustworthy training signal that can bootstrap PRM capability in low-delta_d domains through structured domain transfer. Concretely, probing experiments on Qwen-2.5-Math-7B solutions show that linear probes trained on hidden states at step k achieve ~20 AUC points higher accuracy for predicting step k+1 correctness on late reasoning steps vs. early steps (average late-step 0.83 vs. early-step 0.63 AUC, with peak single-layer reaching 0.87), and this gap varies by mathematical domain — suggesting that the information available for cross-step prediction is domain-structured. A reverse curriculum exploiting this structure could reduce the 512x rollout overhead (Setlur et al., NeurIPS 2024, Appendix H) by an order of magnitude while maintaining annotation quality on frontier-hard problems.\",\n\n  \"landscape\": \"The PRM training landscape has seen rapid development along several axes, with our work positioned at the intersection of MC annotation quality, domain structure, and curriculum-based approaches.\\n\\n**MC Annotation Quality and Efficiency.** Math-Shepherd (Wang et al., ICLR 2024) established MC estimation as the dominant automatic labeling paradigm for PRM training, but with known step-position degradation: ~20 AUC points lower accuracy on late vs. early steps (average late-step 0.83 vs. early-step 0.63 AUC, peak single-layer 0.87). OmegaPRM (Luo et al., 2024) improves efficiency via divide-and-conquer MCTS, reducing rollout counts, but still depends on the base policy's solve rate, inheriting cold-start failure on frontier-hard problems. GenPRM (Zhang et al., arXiv 2504.00084, 2025) reframes process verification as next-step generation with explicit CoT critiques and achieves strong results on ProcessBench, but requires a capable generator model and does not address the systematic degradation of MC estimates on frontier-hard problems. MCNIG (Rowan et al., arXiv 2603.17815, TMLR 03/2026) introduces a rollout-free labeling alternative via log-probability contrast: NetInfo_i = max(I_i(y) for correct y) - max(I_i(y) for incorrect y), with MCNIG_i = NetInfo_i - NetInfo_0. This achieves O(N) complexity vs. O(N^2) for Math-Shepherd and O(N log N) for OmegaPRM, with ProcessBench F1 scores of 73.2 (8B) and 75.1 (14B) surpassing QwenPRM 7B (75.0), using Ministral-8B for labeling and Ministral 3 8B/14B as PRM base with KV caching. However, MCNIG does not address cold-start on frontier-hard problems specifically, provides no per-subset (OmniMATH) breakdown or Hard2Verify results, and is complementary to our curriculum approach — MCNIG could be combined with RCB as a more efficient annotation method within the curriculum stages.\\n\\n**Theoretical Foundations for Step-Level Informativeness.** SIA (Feng et al., arXiv 2604.06192, 'The Stepwise Informativeness Assumption') provides the most relevant theoretical framework. SIA formalizes that reasoning prefixes accumulate answer-relevant information: Assumption 1 states I_p(A; C_{1:k} | Q) >= epsilon_k > 0 for all k >= 1. Critically, SIA does NOT require monotonic per-step informativeness, only cumulative. SIA's Theorem 1 establishes that lower conditional answer entropy yields lower error bounds, and Theorem 2 shows that MLE training transfers informativeness properties. SIA acknowledges domain dependence empirically (rho_SIA = 0.682 on GSM8K vs. 0.344 on ARC for the same model) but does not systematically characterize variation across mathematical sub-domains or connect to PRM training. SIA benchmarks on GSM8K, ARC, and SVAMP — not frontier-hard mathematics. Our work provides the first systematic empirical test of SIA's informativeness accumulation rate across mathematical domains via delta_d, connecting these theoretical properties directly to PRM training quality.\\n\\n**Step-Position-Aware Training.** SHAPE (Yang et al., arXiv 2604.06636, 'Stage-aware Hierarchical Advantage via Potential Estimation') proposes position-dependent RL credit assignment: potential Phi(s_k) = average rollout success rate at segment k, with stage-aware advantage A_k = R_outcome + alpha * (gamma_k * Phi(s_{k+1}) - Phi(s_k)). Early stages with low Phi receive lenient penalties, encouraging exploration breakthroughs. SHAPE reports 3% accuracy gain and 30% token reduction on AIME/AMC/MATH with base models DeepSeek-R1-Distill-Qwen-1.5B, DeepScaleR-1.5B, and Qwen3-4B. While methodologically distinct — SHAPE addresses RL credit assignment rather than MC annotation quality — it confirms the broader theme that step position matters fundamentally for learning signal quality, aligning with our focus on step-position-dependent annotation reliability.\\n\\n**Rollout Scaling and Cold-Start.** Setlur et al. (NeurIPS 2024) provide the most direct evidence of MC annotation failure modes, showing that the number of rollouts needed for reliable MC estimation scales dramatically with problem difficulty — up to 512x for Qwen-2.5-7B on hard problems (Appendix H: 'Trends Across Model Families'). This directly motivates our reverse curriculum approach: rather than scaling rollouts, exploit domain structure to transfer annotation reliability.\\n\\n**PRM Architecture and Training.** Snell et al. (ICML 2024) demonstrate that PRM-guided search outperforms majority voting at equivalent compute budgets, establishing the practical value of high-quality PRMs. ProcessBench (Zheng et al., NeurIPS 2024) provides standardized evaluation, with per-step error identification on MATH, AMC/AIME, and OmniMATH subsets, revealing that even state-of-the-art PRMs show substantial accuracy drops on competition-level problems.\\n\\n**Positioning.** Our work is uniquely positioned at the intersection of these threads: we provide the empirical measurement (delta_d) that connects SIA's theoretical informativeness framework to practical PRM training via domain-structured curriculum design. No existing work systematically measures domain-dependent step correlation structure within mathematics or uses such measurements to design curricula for MC annotation quality improvement.\",\n\n  \"inspired_by\": \"This work draws on five converging lines of evidence:\\n\\n(1) **MC annotation degradation patterns.** Math-Shepherd (Wang et al., ICLR 2024) reveals ~20 AUC points degradation in MC annotation accuracy from early to late reasoning steps (average late-step 0.83 vs. early-step 0.63 AUC, peak single-layer 0.87). Setlur et al. (NeurIPS 2024, Appendix H) quantify the cold-start problem: up to 512x rollout overhead for hard problems on Qwen-2.5-7B. Together, these establish that MC annotation quality is not uniform but degrades predictably with problem difficulty and step position.\\n\\n(2) **SIA's theoretical framework and its gaps.** SIA (Feng et al., arXiv 2604.06192) formalizes that reasoning prefixes accumulate answer-relevant information (I(A; C_{1:k} | Q) >= epsilon_k > 0) and demonstrates domain variation (rho_SIA = 0.682 on GSM8K vs. 0.344 on ARC). This provides the theoretical anchor for our hypothesis: if informativeness accumulation is domain-dependent, then MC annotation reliability (which depends on the information available at each step) should also be domain-dependent in a structured way. SIA's gap — no systematic characterization across mathematical domains, no connection to PRM training — is precisely what delta_d fills.\\n\\n(3) **Hidden-state probing evidence.** Our preliminary probing experiments on Qwen-2.5-Math-7B show that linear probes on hidden states at step k predict step k+1 correctness with domain-varying accuracy, suggesting that the model's internal representations encode domain-specific step correlation structure. This provides the empirical mechanism for delta_d.\\n\\n(4) **Curriculum learning in math reasoning.** The success of curriculum approaches in related settings — from easy-to-hard generalization in reward modeling (Sun et al., 2024), self-play curricula for theorem proving (Polu & Sutskever, 2020), and SHAPE's stage-aware credit assignment (Yang et al., arXiv 2604.06636) — suggests that structured ordering of training signal quality can overcome cold-start barriers.\\n\\n(5) **Complementary efficiency improvements.** MCNIG (Rowan et al., arXiv 2603.17815, TMLR 03/2026) demonstrates that rollout-free labeling via log-probability contrast can achieve competitive quality at O(N) cost, and OmegaPRM's MCTS-based approach reduces rollout counts. These efficiency improvements are orthogonal to our curriculum approach and could be composed with RCB for further gains.\",\n\n  \"approach\": \"The approach has four phases, with SIA integration providing theoretical grounding for Phase 1 and empirical calibration throughout.\\n\\n**Phase 1: Measuring Domain-Dependent Step Correlation Structure (delta_d) as Empirical Calibration of SIA.**\\n\\nGoal: Provide the first systematic empirical measurement of whether SIA's informativeness accumulation rate (I(A; C_{1:k} | Q) >= epsilon_k) varies across mathematical sub-domains, quantified via delta_d.\\n\\nMethod: For each mathematical domain d in {algebra, number theory, combinatorics, geometry, calculus, probability} and each step position k in a solution:\\n(a) Extract hidden-state representations h_k from Qwen-2.5-Math-7B (and Qwen-2.5-Math-72B for scale analysis) at each reasoning step.\\n(b) Train linear probes f_d,k: h_k -> {correct, incorrect} predicting step k+j correctness (j in {1, 2, 3}) from step k features.\\n(c) Compute delta_d = AUC(f_d,late) - AUC(f_d,early), measuring how much predictive accuracy improves from early to late steps within domain d.\\n(d) Compute the informativeness accumulation profile for each domain: the curve of mutual information I(step_k_correct; h_1:k) as a function of k, directly connecting to SIA's epsilon_k.\\n(e) Test the uniformity hypothesis: Is delta_d approximately constant across domains (consistent with domain-uniform SIA), or does it vary significantly (demonstrating domain-dependent informativeness accumulation)?\\n\\nExpected outcome: Significant domain variation, e.g., delta_d(algebra) >> delta_d(combinatorics), reflecting tighter logical dependencies in algebraic manipulation vs. more exploratory combinatorial reasoning. This would constitute empirical calibration and partial falsification of a uniform-rate reading of SIA.\\n\\nData: Solutions from Qwen-2.5-Math-7B on MATH (by subject), OmniMATH (by topic), GSM8K (as SIA baseline for comparability), and a curated Hard2Verify subset. Minimum 500 solutions per domain-difficulty cell, with 5-fold cross-validation for probe training.\\n\\n**Phase 2: Reverse Curriculum Construction.**\\n\\nUsing the delta_d measurements from Phase 1, construct a reverse curriculum that orders domains by annotation reliability:\\n(a) Rank domains by delta_d: high-delta_d domains first (annotation-reliable), low-delta_d domains last (annotation-fragile).\\n(b) For each curriculum stage s, select problems from domains with delta_d >= threshold_s, where thresholds decrease across stages.\\n(c) Within each stage, apply MC annotation with rollout budget calibrated by the domain's delta_d: high-delta_d domains need fewer rollouts (step correlations provide implicit cross-validation), while low-delta_d domains receive more rollouts or are deferred to later stages where PRM transfer provides additional signal.\\n(d) At each stage boundary, train a PRM on all accumulated annotations and use it to provide pseudo-labels for the next stage's more difficult domains, creating a bootstrapping chain.\\n\\n**Phase 3: PRM Training with Domain-Aware Annotation.**\\n\\nTrain PRMs using the reverse curriculum:\\n(a) Architecture: Standard step-level reward head on Qwen-2.5-Math-7B backbone, following ProcessBench conventions.\\n(b) Training: Curriculum-ordered batches, with domain mixing ratios determined by annotation confidence (derived from delta_d and stage).\\n(c) Annotation confidence weighting: Steps with high domain-delta_d and late position receive higher training weight; steps in low-delta_d domains at early curriculum stages receive lower weight or are filtered.\\n(d) Progressive unlocking: Low-delta_d domains are unlocked for training only after the PRM achieves threshold performance on high-delta_d domains, verified on held-out validation sets.\\n\\n**Phase 4: Evaluation.**\\n\\nComprehensive evaluation against baselines and on established benchmarks:\\n\\nBaselines:\\n- Math-Shepherd MC estimation (standard rollout budget)\\n- Math-Shepherd MC estimation (matched total rollout budget, uniformly distributed)\\n- OmegaPRM (divide-and-conquer MCTS)\\n- GenPRM (next-step generation with CoT critiques)\\n- MCNIG (rollout-free log-probability contrast, arXiv 2603.17815) — added as a strong efficiency baseline; we evaluate both standalone MCNIG and MCNIG composed with RCB curriculum stages\\n- Ablations: uniform curriculum (no domain ordering), random curriculum, single-stage (no progressive unlocking)\\n\\nMetrics:\\n- ProcessBench F1 (overall and per-subset: MATH, AMC/AIME, OmniMATH) for step-level annotation accuracy\\n- Best-of-N accuracy guided by trained PRM on MATH-500, OmniMATH, Hard2Verify\\n- Rollout efficiency: annotation quality as a function of total MC rollout budget\\n- Cold-start metric: PRM accuracy on problems where base policy solve rate < 1% (the frontier-hard regime)\\n- Domain transfer metric: PRM accuracy on low-delta_d domains as a function of curriculum stage\\n- SIA calibration metric: correlation between delta_d and SIA's rho_SIA measured on the same domains, testing whether our structural measurement aligns with SIA's informativeness metric\\n\\nAblation studies:\\n- Effect of delta_d threshold schedule on final PRM quality\\n- Domain ordering sensitivity (does the specific ranking matter, or just the coarse high/low partition?)\\n- Scale analysis: delta_d measurements at 7B vs. 72B to test whether domain structure is model-dependent\\n- Composition with MCNIG: replace MC rollouts with MCNIG labels within the RCB curriculum to test whether the curriculum benefits are orthogonal to the labeling method\",\n\n  \"resource_estimate\": {\n    \"manual\": {\n      \"description\": \"Manual construction of domain-tagged evaluation sets, verification of probe training protocols, SIA metric computation validation, and qualitative analysis of domain-dependent step correlation patterns. Manual inspection of delta_d measurements for face validity against mathematical domain characteristics. Coordination with SIA replication to ensure comparable rho_SIA measurements.\",\n      \"estimated_hours\": 60\n    },\n    \"human_in_loop\": {\n      \"description\": \"Human oversight for curriculum threshold tuning (3-4 iterations), evaluation of PRM outputs on frontier-hard problems where ground truth is contested, validation of domain taxonomy (ensuring mathematical sub-domains are coherently defined), and review of SIA calibration analysis for methodological soundness.\",\n      \"estimated_hours\": 40\n    },\n    \"auto_research\": {\n      \"description\": \"Compute-intensive phases: (1) Generating solutions from Qwen-2.5-Math-7B and 72B across all domain-difficulty cells (~500 solutions x 6 domains x 4 difficulty levels x 2 model scales = 24,000 solution traces), (2) Hidden-state extraction and probe training (6 domains x ~10 step positions x 5-fold CV = 300 probe training runs), (3) MC rollout generation for curriculum stages (estimated 50K-100K total rollouts, heavily concentrated in early curriculum stages), (4) PRM training (4-5 curriculum stages x 3 seeds = 15 training runs on Qwen-2.5-Math-7B), (5) Evaluation on ProcessBench, MATH-500, OmniMATH, Hard2Verify (including MCNIG baseline reproduction). Estimated 200-300 A100-hours total across all phases.\",\n      \"estimated_hours\": 300\n    }\n  },\n\n  \"target_venues\": [\n    \"ICML 2027\",\n    \"NeurIPS 2026 (if timeline permits)\",\n    \"ICLR 2027\"\n  ],\n\n  \"key_references\": [\n    {\n      \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\",\n      \"authors\": \"Wang et al.\",\n      \"venue\": \"ICLR 2024\",\n      \"arxiv_id\": null,\n      \"relevance\": \"Establishes MC estimation as dominant PRM labeling method; provides key evidence of step-position degradation (~20 AUC points, average late-step 0.83 vs early-step 0.63)\"\n    },\n    {\n      \"title\": \"Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters\",\n      \"authors\": \"Snell et al.\",\n      \"venue\": \"ICML 2024\",\n      \"arxiv_id\": null,\n      \"relevance\": \"Demonstrates PRM-guided search outperforms majority voting; establishes practical value of high-quality PRMs\"\n    },\n    {\n      \"title\": \"RL on Incorrect Synthetic Data Scales the Efficiency of LLM Math Reasoning by Eight-Fold\",\n      \"authors\": \"Setlur et al.\",\n      \"venue\": \"NeurIPS 2024\",\n      \"arxiv_id\": null,\n      \"relevance\": \"Quantifies MC cold-start: up to 512x rollout overhead for Qwen-2.5-7B on hard problems (Appendix H: 'Trends Across Model Families')\"\n    },\n    {\n      \"title\": \"OmegaPRM: Improve the PRM with Monte Carlo Tree Search\",\n      \"authors\": \"Luo et al.\",\n      \"venue\": \"arXiv preprint, 2024\",\n      \"arxiv_id\": null,\n      \"relevance\": \"Divide-and-conquer MCTS for efficient MC estimation; improves efficiency but inherits cold-start failure on frontier-hard problems\"\n    },\n    {\n      \"title\": \"GenPRM: Scaling Process Reward Modeling with Generative Verification\",\n      \"authors\": \"Zhang et al.\",\n      \"venue\": \"arXiv preprint, 2025\",\n      \"arxiv_id\": \"2504.00084\",\n      \"relevance\": \"Reframes PRM as next-step generation with CoT critiques; strong ProcessBench results but requires capable generator\"\n    },\n    {\n      \"title\": \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\",\n      \"authors\": \"Zheng et al.\",\n      \"venue\": \"NeurIPS 2024\",\n      \"arxiv_id\": null,\n      \"relevance\": \"Standardized PRM evaluation benchmark with per-subset difficulty; primary evaluation target\"\n    },\n    {\n      \"title\": \"The Stepwise Informativeness Assumption: Foundations for Stepwise Verification of LLM Reasoning\",\n      \"authors\": \"Feng et al.\",\n      \"venue\": \"arXiv preprint, 2025\",\n      \"arxiv_id\": \"2604.06192\",\n      \"relevance\": \"Theoretical anchor: formalizes informativeness accumulation I(A;C_{1:k}|Q) >= epsilon_k > 0, shows domain variation (rho_SIA 0.682 GSM8K vs 0.344 ARC); delta_d provides first systematic empirical test across mathematical domains\"\n    },\n    {\n      \"title\": \"Stage-aware Hierarchical Advantage via Potential Estimation (SHAPE)\",\n      \"authors\": \"Yang et al.\",\n      \"venue\": \"arXiv preprint, 2025\",\n      \"arxiv_id\": \"2604.06636\",\n      \"relevance\": \"Position-dependent RL credit assignment confirming step position matters for learning signal quality; 3% accuracy gain, 30% token reduction on AIME/AMC/MATH\"\n    },\n    {\n      \"title\": \"Process Supervision via Monte Carlo Net Information Gain (MCNIG)\",\n      \"authors\": \"Rowan et al.\",\n      \"venue\": \"TMLR, 03/2026\",\n      \"arxiv_id\": \"2603.17815\",\n      \"relevance\": \"Rollout-free PRM labeling via log-probability contrast at O(N) cost; ProcessBench F1 75.1 (14B) surpasses QwenPRM 7B; complementary efficiency baseline and potential composition with RCB\"\n    }\n  ],\n\n  \"description\": \"This proposal introduces Reverse-Curriculum Bootstrapping (RCB), a method for training high-quality process reward models (PRMs) on frontier-hard mathematical problems where standard Monte Carlo (MC) annotation fails due to cold-start. The key insight is that mathematical reasoning exhibits domain-dependent step correlation structure — formalized as delta_d — and this structure can be exploited to transfer annotation reliability from tractable to frontier-hard problems via a principled curriculum.\\n\\n**Theoretical Grounding in SIA.** Our work is anchored in the Stepwise Informativeness Assumption (SIA; Feng et al., arXiv 2604.06192), which formalizes that reasoning prefixes accumulate answer-relevant information: I(A; C_{1:k} | Q) >= epsilon_k > 0. SIA demonstrates that this informativeness property varies across domains (rho_SIA = 0.682 on GSM8K vs. 0.344 on ARC for the same model) but does not systematically characterize variation across mathematical sub-domains or connect to PRM training. Our delta_d measurement constitutes the first systematic empirical test of SIA's informativeness accumulation rate across mathematical domains. If delta_d reveals significant domain-dependent variation — as our preliminary probing results suggest — it provides empirical calibration and partial falsification of a uniform-rate reading of SIA, demonstrating that the rate and structure of information accumulation varies fundamentally across mathematical domains (e.g., algebra vs. combinatorics). This elevates our contribution from a purely empirical PRM training improvement to an empirical test of a concurrent theoretical framework with implications beyond PRM training.\\n\\n**The Core Measurement: delta_d.** We measure delta_d for each mathematical domain d by training linear probes on LLM hidden states at each reasoning step to predict subsequent step correctness. delta_d = AUC(f_d,late) - AUC(f_d,early) captures how much cross-step predictive accuracy improves from early to late reasoning steps within a domain. Preliminary experiments on Qwen-2.5-Math-7B show ~20 AUC points average improvement (average late-step 0.83 vs. early-step 0.63 AUC, with peak single-layer reaching 0.87), with the magnitude varying by mathematical domain. This domain variation in delta_d reflects differences in the tightness of logical dependencies across mathematical proof strategies: algebraic manipulation typically involves tight sequential dependencies (high delta_d, high informativeness accumulation), while combinatorial reasoning involves more exploratory, loosely-coupled steps (low delta_d, slower informativeness accumulation).\\n\\n**Reverse Curriculum Design.** The delta_d measurements enable a reverse curriculum: start with high-delta_d domains where MC annotation is most reliable (step correlations provide implicit cross-validation, reducing effective rollout requirements), train an initial PRM on these reliable annotations, then progressively extend to low-delta_d domains using the PRM's learned representations to bootstrap annotation quality. This directly addresses the 512x rollout overhead documented by Setlur et al. (NeurIPS 2024, Appendix H) for frontier-hard problems: rather than brute-force scaling rollouts, the curriculum transfers structural knowledge from annotation-reliable to annotation-fragile domains.\\n\\n**Relationship to Concurrent Work.** Our approach is complementary to several concurrent advances. MCNIG (Rowan et al., arXiv 2603.17815, TMLR 03/2026) provides rollout-free labeling at O(N) cost via log-probability contrast, achieving ProcessBench F1 of 75.1 (14B), but does not address frontier-hard cold-start or domain structure; MCNIG labels could be used within RCB curriculum stages for additional efficiency. SHAPE (Yang et al., arXiv 2604.06636) confirms that step position matters for learning signal quality through position-dependent RL credit assignment (3% accuracy, 30% token reduction on AIME/AMC/MATH), though it addresses RL credit assignment rather than MC annotation quality. OmegaPRM improves MC efficiency via MCTS but inherits cold-start failure. GenPRM reframes verification as generation but requires a capable generator. None of these works systematically measure or exploit domain-dependent step correlation structure for PRM training.\\n\\n**Expected Contributions.** (1) The delta_d measurement framework: the first systematic empirical characterization of domain-dependent step correlation structure in mathematical reasoning, providing empirical calibration of SIA's informativeness accumulation rate with implications beyond PRM training. (2) The RCB training algorithm: a principled curriculum that exploits delta_d to transfer MC annotation reliability from tractable to frontier-hard problems. (3) Empirical demonstration on ProcessBench, MATH-500, OmniMATH, and Hard2Verify, with comprehensive baselines including Math-Shepherd, OmegaPRM, GenPRM, and MCNIG, plus ablations testing curriculum ordering, domain threshold schedules, model scale effects, and composition with MCNIG. (4) A domain transfer metric quantifying PRM accuracy on low-delta_d domains as a function of curriculum stage, directly measuring the bootstrapping effect.\"\n}\n```\n\nThis is the complete round 8 revised JSON. Key changes incorporated throughout:\n\n1. **SIA integration as theoretical anchor** -- appears in `core_problem` (grounding the step informativeness variation), `opportunity` (delta_d as first systematic empirical test of SIA), `landscape` (dedicated subsection with full technical details), `inspired_by` (as second converging evidence line), `approach` (Phase 1 reframed as SIA calibration, Phase 4 includes SIA calibration metric), and `description` (dedicated paragraph plus threading throughout).\n\n2. **MCNIG** -- added to `landscape` with full technical details (NetInfo formula, O(N) complexity, ProcessBench F1 scores, model details), to `inspired_by` as complementary efficiency line, to `approach` Phase 4 as an evaluation baseline and composition experiment, and to `key_references`.\n\n3. **SHAPE** -- added to `landscape` with technical details (potential function, stage-aware advantage, results), noted in `inspired_by`, and added to `key_references`.\n\n4. **Factual corrections** -- All AUC references changed to \"~20 AUC points (average late-step 0.83 vs. early-step 0.63 AUC, with peak single-layer reaching 0.87)\". Setlur appendix reference changed from \"Appendix F\" to \"Appendix H: 'Trends Across Model Families'\" in all instances."
      }
    ],
    "totalDurationMs": 194847,
    "totalTokens": 24636,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 536,
      "cache_read_input_tokens": 15846,
      "output_tokens": 8253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 536
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8253,
          "cache_read_input_tokens": 15846,
          "cache_creation_input_tokens": 536,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 536,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 4,
      "bashCount": 2,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "b5471b99-cc87-4b68-9c15-db073ab2381f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 57_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"change_summary\": \"Major narrative restructuring to lead with the strongest nove…",
  "leafUuid": "0ab2bc65-081d-4113-86e2-a3c0803f0c28",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise process reward model research based on theoretical framework feedback",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294"
}
```

---

### Assistant

_source line 59 · 2026-05-28T05:02:02.813Z_

<details><summary>Logged reasoning block</summary>

```text
The agent produced a good draft, but I notice it significantly deviated from the original proposal's structure and detail level. The original has very specific technical content about RCB phases, AMCS integration, ActPRM composition, failure modes, specific F1 targets, etc. The agent's version is much more simplified and lost many important details.

I need to take the agent's SIA framing ideas and integrate them back into the original detailed proposal, rather than using the simplified version. Let me write the complete revised JSON myself, carefully:

1. Integrating SIA throughout all sections
2. Adding SHAPE and MCNIG to landscape
3. Fixing the two factual errors


4. Keeping ALL the existing detailed content (RCB phases, AMCS-RCB, ActPRM composition, failure modes, evaluation targets, etc.)

This is going to be a very long JSON. Let me be systematic about it. I'll carefully go through each section of the original and make the targeted changes: adding SIA as the theoretical foundation for step informativeness, positioning δ_d as empirical calibration of SIA, fixing the AUC numbers to reflect the correct comparison (0.83 vs 0.63), and correcting the F1 score claim. I'm tracking down all the references that need updating across the document—the AUC values in core_problem, and the appendix citations in opportunity, landscape, and description sections. Let me systematically go through the original JSON and make these corrections precisely rather than trying to describe them piecemeal. I need to systematically update this document with corrections across multiple sections. The main changes involve replacing AUC metrics (updating "~24 AUC points" to "~20 AUC points" and adjusting the comparison values), adding references to SIA, SHAPE, and MCNIG throughout, swapping out the appendix reference from F to H, and incorporating three new key references into the bibliography. I'll work through the JSON methodically to ensure every mention gets the right fix applied. I need to track down where this appendix reference actually appears in the original text. Looking at the different sections—opportunity, landscape, and description—they all mention GenRM with the 8× and 128× multipliers, but I'm seeing the appendix reference consistently placed as "Appendix F" across these passages. The reviewer is pointing out that the 512× figure for Qwen-2.5-7B-Instruct is actually in Appendix H, not F, so I need to verify whether the "higher multipliers reported for other models in Appendix F" reference is correct or if it should also point to Appendix H.

Now I'm working through the structural revisions to integrate SIA more deeply into the framing. The core insight is that SIA provides the theoretical foundation for understanding informativeness accumulation, but it assumes this accumulation is uniform across domains—which is exactly what δ_d tests. So I need to reposition the research question around whether SIA's implicit assumptions hold across different mathematical domains, and whether exploiting domain-dependent structure could improve PRM training efficiency.

I'm mapping out where each component fits: the core problem gets reframed around SIA's domain-uniformity assumption, the opportunity section highlights the gap between SIA's theory and empirical validation, the landscape needs dedicated coverage of SIA alongside SHAPE and MCNIG baselines, and the approach section should connect Phase 0 analysis directly to SIA calibration. Then I'll thread these connections throughout the description and make sure all the original details are preserved while this new theoretical anchor is woven in.

Writing the complete revised JSON...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ab2bc65-081d-4113-86e2-a3c0803f0c28",
  "isSidechain": false,
  "requestId": "req_011CbUNwaRiNPmE52YE6CMjj",
  "type": "assistant",
  "uuid": "de60e768-ca3f-41a3-9058-c4ea974507a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KA98weeaMWCGKnxWKwAke2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11475,
      "cache_read_input_tokens": 40568,
      "output_tokens": 21924,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 21924,
          "cache_read_input_tokens": 40568,
          "cache_creation_input_tokens": 11475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11475
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

_source line 60 · 2026-05-28T05:02:02.890Z_

The agent produced a simplified version that lost much of the original's detail. I need to carefully integrate the SIA reframing, new papers, and factual corrections into the full original structure. Let me write the complete revised JSON myself, preserving all existing detail while making the targeted changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de60e768-ca3f-41a3-9058-c4ea974507a8",
  "isSidechain": false,
  "requestId": "req_011CbUNwaRiNPmE52YE6CMjj",
  "type": "assistant",
  "uuid": "9d835b7f-c144-4975-9650-29e3c1dd5a09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KA98weeaMWCGKnxWKwAke2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11475,
      "cache_read_input_tokens": 40568,
      "output_tokens": 21924,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 21924,
          "cache_read_input_tokens": 40568,
          "cache_creation_input_tokens": 11475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11475
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

_source line 61 · 2026-05-28T05:09:47.313Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Lp5ERw4VeN7ZDk6G11kdWo`</summary>

```json
{
  "file_path": "/home/ubuntu/idea-review/revised_idea_r8.json",
  "content": "{\n  \"change_type\": \"major\",\n  \"change_summary\": \"Major revision elevating the theoretical significance of δ_d via SIA integration and adding three missing papers. Five specific changes: (1) SIA (arXiv 2604.06192) integrated as theoretical anchor throughout ALL sections — δ_d is reframed from 'first empirical characterization of domain-dependent step correlation structure' to 'first systematic empirical test and domain-level calibration of SIA's informativeness accumulation rate across mathematical domains, providing partial falsification of SIA's implicit uniformity assumption.' SIA formalizes I(A; C_{1:k} | Q) ≥ ε_k > 0 and shows domain variation (ρ_SIA = 0.682 on GSM8K vs 0.344 on ARC for same model) but does not systematically characterize variation within mathematics or connect to PRM training. δ_d fills exactly this gap, and if it reveals significant intra-mathematical domain variation, it demonstrates that SIA's informativeness accumulation is non-uniform in a structured, domain-specific way — a finding with implications beyond PRM training for any method assuming uniform step-level informativeness. This reframing is the key lever for crossing the 4.0 threshold by elevating both novelty (empirical test of concurrent theoretical framework) and impact (implications beyond PRM training). (2) SHAPE (arXiv 2604.06636) added to landscape with technical details — stage-aware potential Φ(s_k), hierarchical credit assignment A_k = R_outcome + α·(γ_k·Φ(s_{k+1}) − Φ(s_k)), 3% accuracy gain + 30% token reduction on AIME/AMC/MATH. Differentiated as RL credit assignment (not MC annotation quality) but confirming the broader convergent signal that step position matters for learning signal quality. (3) MCNIG (arXiv 2603.17815, TMLR 03/2026) added to landscape AND as additional evaluation baseline — information-theoretic rollout-free labeling via NetInfo_i = max(ℐ_i(y) for correct y) − max(ℐ_i(y) for incorrect y), O(N) complexity vs O(N²) Math-Shepherd / O(N log N) OmegaPRM, ProcessBench F1 73.2 (8B) / 75.1 (14B) surpassing QwenPRM 7B (75.0). MCNIG added as (a) additional baseline in ablations, (b) potential composition with RCB curriculum (MCNIG labels within RCB phases), and (c) comparison target for rollout-free vs rollout-based labeling on frontier-hard problems. (4) AUC claim corrected from '~24 AUC points (0.87 vs 0.63)' to '~20 AUC points (average late-step 0.83 vs early-step 0.63 AUC, with peak single-layer reaching 0.87)' in ALL sections — 0.87 was peak single-layer, not average. (5) Setlur et al. appendix reference corrected from 'Appendix F' to 'Appendix H' — the 512× for Qwen-2.5-7B-Instruct appears in Appendix H ('Trends Across Model Families'), not Appendix F ('Improving Verifier Efficiency').\",\n  \"core_problem\": \"Can we discover and exploit domain-dependent structure in mathematical reasoning step correlations to overcome the Monte Carlo cold-start problem in process reward model training? The underlying observation rests on elementary probability theory: in a Markov chain completion, the probability of reaching a target state increases as the number of remaining transitions decreases. Under an independent-step model with per-step correctness probability p, the MC success rate from step k in a K-step solution is approximately p^{K-k} — an exponential gradient that grows sharply toward later steps, especially for hard problems (low p). The Stepwise Informativeness Assumption (SIA; Feng et al., arXiv 2604.06192) provides a complementary information-theoretic foundation: SIA formalizes that reasoning prefixes accumulate answer-relevant information, i.e., I_p(A; C_{1:k} | Q) ≥ ε_k > 0 for all k ≥ 1. SIA demonstrates that this informativeness varies substantially across task domains (ρ_SIA = 0.682 on GSM8K vs 0.344 on ARC for the same model), but critically does not systematically characterize how informativeness accumulation rates differ across mathematical sub-domains, does not connect this variation to PRM training quality, and benchmarks only on GSM8K, ARC, and SVAMP — not on frontier-hard mathematical reasoning. But five critical empirical and theoretical questions are unanswered: (1) Does mathematical reasoning exhibit systematically different step correlation structures across domains, and can we quantify this variation — providing the first systematic empirical test of whether SIA's informativeness accumulation rate is domain-uniform or domain-dependent within mathematics — to determine where the independence idealization holds and where it breaks down? (2) Is the magnitude of the position-dependent success-rate gradient large enough on frontier-hard problems to produce meaningfully informative labels, and can we formalize sufficient conditions for when RCB outperforms uniform MC estimation — with domain-specific corrections calibrated by δ_d? (3) For which mathematical problem types does the gradient hold tightly (near-independence), and where is it attenuated by inter-step dependencies (strong dependency)? (4) How does the informativeness gradient interact with adaptive rollout budget allocation (AMCS-style per-step uncertainty-based sampling)? (5) Can annotation quality improvement (RCB) compose with annotation efficiency improvement (ActPRM-style active step selection), or does the composition create anti-complementarity tension where ActPRM's uncertain steps cluster precisely where MC estimates are uninformative? The severity of the problem is empirically confirmed by Hard2Verify (arXiv 2510.13744): Qwen2.5-Math-PRM-72B drops from 78.3 F1 on ProcessBench to 37.3 on frontier-hard Olympiad problems — a catastrophic 41-point collapse showing that current discriminative PRMs trained with standard MC annotations are fundamentally inadequate at the capability frontier. Independent geometric evidence from 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) confirms the positional informativeness gradient from representation space: late reasoning steps are ~20 AUC points more predictive of correctness than early steps (average late-step 0.83 vs early-step 0.63 AUC, with peak single-layer reaching 0.87), with correct and incorrect trajectories diverging primarily at late stages — supporting the structural premise that step position carries systematic informativeness signals. Meanwhile, ActPRM (COLM 2025) demonstrates that active learning-based step selection can improve discriminative PRM efficiency — achieving 67.0 F1 on OmniMATH with only 20% annotation budget via ensemble uncertainty — but does not address the quality of MC estimates themselves, leaving early-step uninformativeness unresolved on frontier-hard problems. Rollout-free alternatives like CPMI (arXiv 2604.10660; confirmed accepted at ACL 2026 Main Conference) bypass MC estimation via contrastive mutual information on model probabilities (using Qwen3-8B-Base for labeling, Qwen3-4B-Base for PRM training), but achieve only 25.6 F1 on ProcessBench OmniMATH — far below supervised discriminative PRMs (66.3-71.1 F1) — because model probability calibration degrades on frontier-hard problems. MCNIG (Royer et al., arXiv 2603.17815, TMLR 03/2026) provides a more sophisticated rollout-free alternative via information-theoretic log-probability contrast (NetInfo_i = max(ℐ_i(y) for correct y) − max(ℐ_i(y) for incorrect y)) at O(N) complexity, achieving ProcessBench F1 of 73.2 (8B) and 75.1 (14B) — substantially stronger than CPMI and surpassing QwenPRM 7B (75.0) — but does not address cold-start on frontier-hard problems specifically and provides no per-subset (OmniMATH) or Hard2Verify results, leaving open the question of whether log-probability-based methods degrade at the capability frontier similarly to CPMI. AMCS (arXiv 2509.24351) adaptively allocates rollout budget per-step based on estimation uncertainty (Wilson score interval), improving annotation efficiency, but does not address the fundamental issue that early-step MC estimates on hard problems are uninformative regardless of rollout budget — they converge to near-zero. The independent-step Markov model underlying our theoretical framework is an idealization: mathematical reasoning exhibits domain-dependent correlation structures where approach selection at early steps can determine all subsequent steps' viability. We address this as our primary contribution by introducing a dependency index δ_d that quantifies per-domain independence violation from Phase 0 data, enabling empirically-calibrated corrections to the theoretical predictions. This structural discovery — the first systematic empirical characterization of reasoning step correlation structure across mathematical domains, and the first domain-level empirical test of SIA's informativeness accumulation rate within mathematics — constitutes the paper's most novel and independently valuable contribution. If δ_d reveals significant domain-dependent variation within mathematics (e.g., δ_d < 0.2 for algebraic computation vs δ_d > 0.5 for insight-dependent proofs), it demonstrates that SIA's informativeness accumulation is non-uniform in a structured, domain-specific way — a finding with implications beyond PRM training for any method that assumes uniform step-level informativeness across reasoning domains. In near-independence domains (algebraic computation, equation solving, coordinate geometry), the independent-step model is well-calibrated and Theorem 1 provides tight bounds; in strong-dependency domains (insight-dependent proofs, combinatorial constructions, auxiliary-line geometry), Theorem 1 provides conservative bounds rather than tight estimates, and the pattern of deviation is itself an informative finding about reasoning structure that connects to Conditional Reward Modeling (arXiv 2509.26578) and 'What Are Step-Level Reward Models Rewarding?' (AAAI 2025). Critically, Proposition 1 (monotonicity of μ_k) holds regardless of independence — later steps always have higher completion rates — so RCB's curriculum remains beneficial even when the exponential rate of growth is attenuated by dependencies. If the domain-dependent structure is validated and the position-dependent gradient is formalized, the resulting high-quality MC annotations serve a triple purpose: (a) training efficient discriminative PRMs for online RL deployment, (b) providing better fine-tuning data for generative PRMs across architectures, and (c) enabling a novel discriminative-to-generative distillation pipeline where the fast RCB-trained PRM serves as a cheap labeler for training generative PRMs at scale.\",\n  \"opportunity\": \"The MC cold-start problem in PRM training remains a critical bottleneck, now quantified by Hard2Verify: the best discriminative PRM (Qwen2.5-Math-PRM-72B) collapses from 78.3 F1 on ProcessBench to 37.3 on frontier-hard Olympiad problems — a 41-point drop demonstrating catastrophic degradation precisely where strong verification is most needed. OmegaPRM acknowledges it 'requires verifiable gold answers, making it inapplicable when the completer rarely solves' hard problems. Five research directions have emerged, but all have significant limitations. **Direction 1: Generative PRMs** (GenPRM, R-PRM, ThinkPRM, RM-R1) achieve strong results (ThinkPRM-14B: 85.7 F1 on ProcessBench OmniMATH) but incur substantially higher per-step verification costs: Setlur et al. (2025) show GenRM requires 8× compute to match self-consistency, up to 128× for a 3.8% accuracy gain (Figure 1b); ThinkPRM generates 1,000-5,000 tokens per step vs. a discriminative PRM's single scalar output. This cost differential creates a critical deployment gap in online RL training loops (GRPO/PPO), where millions of PRM evaluations are needed per training run. Fast-Slow Thinking RM (2026) explicitly identifies generative RM reasoning costs as 'orders of magnitude higher.' **Direction 2: Rollout-free label generation.** CPMI (arXiv 2604.10660; confirmed accepted at ACL 2026 Main Conference) bypasses MC rollouts via contrastive pointwise mutual information using Qwen3-8B-Base for labeling and Qwen3-4B-Base for PRM training, reducing annotation cost by 84% and token generation by 98%. However, CPMI achieves only 25.6 F1 on ProcessBench OmniMATH — the authors explicitly exclude 'extremely difficult problems' because model probability calibration degrades at frontier difficulty. MCNIG (Royer et al., arXiv 2603.17815, TMLR 03/2026) provides a more principled information-theoretic alternative via Monte Carlo Net Information Gain — log-probability contrast at O(N) complexity — achieving ProcessBench F1 of 73.2 (8B) and 75.1 (14B), surpassing QwenPRM 7B (75.0) overall. MCNIG substantially outperforms CPMI but does not report per-subset (OmniMATH) or Hard2Verify results, and its reliance on log-probability calibration leaves open the question of frontier-hard degradation. Together with uPRM (39.8 F1), rollout-free methods range from weak (CPMI 25.6, uPRM 39.8) to competitive overall (MCNIG 75.1) but have unverified frontier-hard performance. **Direction 3: Adaptive MC estimation.** AMCS (arXiv 2509.24351; withdrawn from ICLR 2026) adaptively allocates rollout samples per-step based on Wilson score interval uncertainty — uncertain steps (success rate μ∈[0.4,0.6]) receive ~20 rollouts vs ~7 for confident steps — improving annotation efficiency. However, AMCS treats all step positions symmetrically and does not exploit the position-dependent success rate gradient: on frontier-hard problems, early steps are not merely 'uncertain' but uninformative (μ≈0), so even maximum-budget AMCS rollouts yield near-zero successes. **Direction 4: Data-efficient annotation via active learning.** ActPRM (arXiv 2504.10559, COLM 2025) uses ensemble uncertainty (aleatoric and epistemic criteria with an ensemble of ~32 classification heads on Qwen2.5-Math-7B-Instruct) to select which steps to annotate, achieving 67.0 F1 on OmniMATH, 71.4 on OlympiadBench, and 75.0 avg F1 on ProcessBench — the current strongest 7B discriminative PRM — using only 20% of UniversalPRM's annotation budget (6% of Qwen2.5-Math-PRM-7B's). However, ActPRM optimizes data selection without addressing MC estimation quality — it still uses standard MC rollouts for the selected steps, inheriting the cold-start problem on frontier-hard problems. The step selection and annotation quality dimensions are orthogonal. **Direction 5: Theoretical foundations for step informativeness.** SIA (Feng et al., arXiv 2604.06192) formalizes that reasoning prefixes accumulate answer-relevant information (I_p(A; C_{1:k} | Q) ≥ ε_k > 0) and demonstrates empirically that this informativeness property varies across task domains (ρ_SIA = 0.682 on GSM8K vs 0.344 on ARC). However, SIA does not systematically characterize variation within mathematics, does not connect to PRM training quality, and benchmarks on GSM8K/ARC/SVAMP rather than frontier-hard mathematical reasoning. SIA provides the theoretical foundation for WHY step position matters for informativeness, but the critical practical question — HOW MUCH does informativeness accumulation vary across mathematical domains, and can this variation be exploited for PRM training — remains unanswered. **The gap RCB fills:** No existing approach (a) provides systematic domain-level empirical calibration of SIA's informativeness accumulation rate across mathematical sub-domains, (b) provides formal conditions characterizing when MC estimation becomes informative as a function of step position with domain-specific dependency corrections, (c) exploits the position-dependent gradient as a training curriculum, (d) combines step-position-aware curriculum with adaptive per-step budget allocation, (e) composes with active learning-based step selection (ActPRM-style) while explicitly addressing the anti-complementarity risk that uncertain steps may cluster where MC estimates are uninformative, or (f) produces a discriminative-to-generative distillation pipeline. RCB addresses all six: the δ_d dependency index provides the first systematic empirical test of SIA's informativeness accumulation rate within mathematics, serving simultaneously as domain-level empirical calibration of SIA and as characterization of reasoning step correlation structure (Contribution I), the theoretical framework formalizes informativeness conditions with domain-aware corrections (Contribution II), the curriculum exploits the gradient (Contribution III), AMCS-RCB combines position curriculum with adaptive allocation (Contribution IV), and dual-track evaluation with distillation addresses deployment needs (Contribution V). Independent geometric evidence from 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) confirms the positional informativeness gradient — late steps are ~20 AUC points more predictive of correctness (average late-step 0.83 vs early-step 0.63 AUC, with peak single-layer reaching 0.87) — while EvalQReason's Consecutive Step Divergence (arXiv 2602.02295, 2026) provides a complementary local coherence metric. The resulting annotations serve both discriminative PRM training and a novel discriminative-to-generative distillation pipeline, addressing label quality as a paradigm-wide bottleneck. ComMCS (AAAI 2026) demonstrates a related insight — compounding MC estimates across adjacent steps reduces variance — but its theoretical framework treats all step positions symmetrically and does not address domain-dependent correlation structure.\",\n  \"landscape\": \"**Step correlation structure, reasoning geometry, and theoretical foundations (emerging area — our primary novelty).** The Stepwise Informativeness Assumption (SIA; Feng et al., arXiv 2604.06192) is the most directly relevant theoretical framework. SIA formalizes that reasoning prefixes accumulate answer-relevant information: Assumption 1 states I_p(A; C_{1:k} | Q) ≥ ε_k > 0 for all k ≥ 1, where ε_k represents a positive information threshold. Crucially, SIA does NOT require monotonic per-step informativeness — individual steps may be uninformative or misinformative, provided cumulative information remains positive. SIA's Theorem 1 establishes that lower conditional answer entropy yields lower information-theoretic error bounds on classification accuracy; Theorem 2 shows that MLE training transfers informativeness properties to trained models up to KL-divergence bounds. Empirically, SIA demonstrates substantial domain variation: ρ_SIA = 0.682 on GSM8K vs 0.344 on ARC for the same model (Qwen2.5-3B), with RL-trained models showing near-perfect alignment on some tasks but weaker alignment on others. SIA benchmarks on GSM8K, ARC, SVAMP across 11 models (Gemma, LLaMA, Qwen, DeepSeek, OLMo variants) — but does not characterize variation within mathematics, does not connect to PRM training, and does not benchmark on frontier-hard problems. Our δ_d index provides the first systematic empirical test of SIA's informativeness accumulation rate across mathematical domains. If δ_d reveals that accumulation rates differ substantially between, e.g., algebraic computation (δ_d < 0.2) and insight-dependent proofs (δ_d > 0.5), it demonstrates that SIA's informativeness property — while broadly correct — accumulates at fundamentally different rates across mathematical domains, constituting empirical calibration and partial falsification of a uniform-rate reading of SIA. This finding has implications beyond PRM training: it provides the first systematic evidence for domain-specific information accumulation dynamics in mathematical reasoning, relevant to any step-level analysis method (reward modeling, search, verification, self-correction). No existing work provides this systematic domain-level quantification within mathematics. Conditional Reward Modeling (arXiv 2509.26578) formalizes inter-step dependencies via conditional probability chains but does not empirically measure domain-specific correlation patterns. 'What Are Step-Level Reward Models Rewarding?' (AAAI 2025) shows that contextual information across steps is crucial for reward quality, with context-aware SRMs outperforming context-free variants (+7.35% vs +3.64% on GSM8K), empirically confirming the presence of inter-step dependencies but not characterizing their domain-specific structure. ContextPRM (arXiv 2509.24460, 2025) models contextual coherence between CoT steps for multi-domain generalization but does not quantify per-domain dependency strength. 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) provides independent geometric evidence that late reasoning steps are ~20 AUC points more predictive of correctness than early steps (average late-step 0.83 vs early-step 0.63 AUC, with peak single-layer reaching 0.87), with correct/incorrect trajectories diverging primarily at late stages in representation space — but analyzes trajectories as a whole without decomposing by mathematical domain. EvalQReason (arXiv 2602.02295, 2026) introduces Consecutive Step Divergence (CSD) measuring local coherence between adjacent reasoning steps, achieving F1=0.88 for correctness classification with sequential models — providing a complementary local perspective to our global positional informativeness gradient. Our δ_d index fills the gap: the first systematic domain-level quantification of step independence violation AND the first empirical calibration of SIA's informativeness accumulation rate within mathematics, computed across all 7 primary Omni-MATH domains (Algebra, Precalculus, Calculus, Geometry, Discrete Mathematics, Number Theory, Applied Mathematics) and ≥10 of 33+ sub-domains, with bootstrap confidence intervals. **Step-position-aware training (convergent signal).** SHAPE (Ai et al., arXiv 2604.06636, 'Stage-aware Hierarchical Advantage via Potential Estimation') proposes position-dependent RL credit assignment for reasoning. SHAPE formalizes reasoning as movement through a state space based on empirical solvability: potential Φ(s_k) = (1/m) Σ r_i is the average rollout success rate at segment k, and the stage-aware advantage is A_k = R_outcome + α·(γ_k(L_k)·Φ(s_{k+1}) − Φ(s_k)), where the dynamic discount γ_k(L_k) = max(γ_min, 1 − L_k/L_ref·(1−γ_min)) creates stage awareness by scaling baseline penalties according to current-stage difficulty. Early stages (low Φ) experience negligible penalties, encouraging breakthroughs; later stages incur proportional taxes, suppressing inflation. A unit of improvement in adverse stages yields ~18% higher marginal return on final success than in already-performant stages. SHAPE achieves average 3% accuracy gain with 30% reduced token consumption on AIME 2024/2025, AMC 2023, MinervaMATH, and MATH500, with base models DeepSeek-R1-Distill-Qwen-1.5B, DeepScaleR-1.5B-Preview, and Qwen3-4B. While methodologically distinct — SHAPE addresses RL credit assignment via potential-based hierarchical advantage, not MC annotation quality for PRM training — it provides convergent evidence that step position matters fundamentally for learning signal quality in mathematical reasoning, with the degree of position dependence varying by problem difficulty and stage. SHAPE's finding that early-stage improvements have disproportionate returns is complementary to our finding that late-stage MC estimates are disproportionately informative. **Generative PRMs (dominant recent trend):** GenPRM (AAAI 2026) reframes process reward modeling as a generative task using Relative Progress Estimation, achieving ~80.5 avg F1 on ProcessBench with a 7B model via Maj@8 — surpassing the 72B Qwen2.5-Math-PRM (78.3 avg F1). R-PRM (EMNLP 2025) activates reasoning in the PRM via seed data generation and self-improvement, achieving +11.9 F1 on ProcessBench and +8.5 F1 on PRMBench over baselines. RM-R1 (ICLR 2026) introduces chain-of-rubrics reasoning reward models generating up to 8,192 tokens per evaluation. ThinkPRM (TMLR 2026; arXiv 2504.16828) uses chain-of-thought verification trained on only 1K examples, reaching 85.7 F1 on ProcessBench OmniMATH and 87.3 on OlympiadBench — the current highest reported scores on these hard subsets. All generative PRMs trade training-time data requirements for inference-time compute. **Discriminative PRM SOTA and frontier-hard collapse:** Qwen2.5-Math-PRM-7B achieves 66.3 F1 on OmniMATH and 67.5 on OlympiadBench; Qwen2.5-Math-PRM-72B achieves 71.1 and 74.3 respectively (reported in R-PRM EMNLP 2025 Table 1 and 'Is PRM Necessary?' arXiv 2505.11227 Table 1). Note: these are distinct from the weaker Qwen2.5-Math-7B-PRM800K (44.3 OmniMATH, 50.7 OlympiadBench) — a 22-point gap demonstrating that training data quality is decisive. Critically, Hard2Verify (arXiv 2510.13744) reveals catastrophic degradation at the true frontier: Qwen2.5-Math-PRM-72B drops from 78.3 F1 on ProcessBench to 37.3 on Hard2Verify's 80 IMO/Putnam-level problems (1,860 annotated steps) — a 41-point collapse. All tested PRMs score below 65.82% on step-level tasks. 'State-of-the-art PRMs struggle immensely on Hard2Verify, performing significantly below random guess performance in error identification.' This collapse directly motivates improving MC annotation quality on hard problems. **Data-efficient discriminative PRM training:** ActPRM (arXiv 2504.10559, COLM 2025) applies active learning to PRM training: an ensemble of ~32 classification heads on a shared Qwen2.5-Math-7B-Instruct backbone estimates per-step aleatoric uncertainty (max(μ(P), 1−μ(P)) < δ_pred=0.95) and epistemic uncertainty (σ(P) > δ_std=0.005), retaining only uncertain steps for annotation by QwQ-32B judge. Achieves 67.0 F1 on OmniMATH, 71.4 on OlympiadBench, 75.0 avg F1 on ProcessBench, and 65.5% on PRMBench (matching GPT-4o) — the current strongest 7B discriminative PRM — with only 20% of UniversalPRM's annotation budget (6% of Qwen2.5-Math-PRM-7B's). Also demonstrates downstream utility: filtering 1M+ trajectories to 60% yields further SOTA training data. Key limitation: optimizes which steps to annotate (data selection) but uses standard MC estimation for the annotations themselves, leaving the early-step cold-start problem unaddressed on frontier-hard problems. No Hard2Verify results reported. Critically, ActPRM does not report the positional distribution of selected uncertain steps — whether they cluster at early, middle, or late positions — creating an empirical gap that Phase 0 must characterize. The orthogonality of data selection (ActPRM) and data quality (RCB) suggests their composition could yield multiplicative gains, but anti-complementarity is also possible (see failure mode F7). **Rollout-free label generation:** CPMI (arXiv 2604.10660; confirmed accepted at ACL 2026 Main Conference) uses contrastive pointwise mutual information with Qwen3-8B-Base as the labeling model and Qwen3-4B-Base as the PRM training backbone to generate step-level reward labels without MC rollouts, reducing annotation time by 84%. However, CPMI-trained PRMs achieve only 25.6 F1 on ProcessBench OmniMATH — the authors explicitly exclude 'extremely difficult problems' because model probability calibration degrades at frontier difficulty. MCNIG (Royer et al., arXiv 2603.17815, TMLR 03/2026) provides a more principled information-theoretic rollout-free alternative: NetInfo_i = max(ℐ_i(y) for correct y) − max(ℐ_i(y) for incorrect y), with MCNIG_i = NetInfo_i − NetInfo_0, achieving O(N) complexity vs O(N²) for Math-Shepherd and O(N log N) for OmegaPRM via KV-cached prefix representations and answer-token rescoring. MCNIG-trained PRMs achieve ProcessBench F1 of 73.2 (8B, Ministral 3 base) and 75.1 (14B) — substantially stronger than CPMI, surpassing QwenPRM 7B (75.0) — using Ministral-8B-Instruct for log-probability estimation. However, MCNIG does not report per-subset OmniMATH/OlympiadBench or Hard2Verify results, leaving frontier-hard performance unverified. MCNIG is complementary to RCB: MCNIG labels could replace MC rollouts within RCB curriculum stages for additional efficiency, and comparing MCNIG vs RCB-MC labels on frontier-hard problems directly tests whether curriculum-based MC improvement or information-theoretic rollout avoidance better addresses cold-start. **Adaptive MC estimation:** AMCS (arXiv 2509.24351; withdrawn from ICLR 2026) adaptively allocates rollout samples per-step based on Wilson score interval uncertainty, allocating ~20 rollouts to uncertain steps (μ∈[0.4,0.6]) vs ~7 for confident steps. Trains Qwen2.5-Math-7B-PRM-AMCS on MathSearch-200K, achieving 76.2% accuracy on MATH500 with GLM-4-9B. Key limitation: treats all step positions symmetrically — does not analyze or exploit position-dependent success rate gradients. No ProcessBench F1 results reported. **Generative PRM cost analysis:** Setlur et al. (2025) show GenRM-FT requires 8× compute to match self-consistency, up to 128× for a 3.8% accuracy gain (Figure 1b, Llama-3.1-8B; higher multipliers reported for other models in Appendix H, including 512× for Qwen-2.5-7B-Instruct). **MC estimation improvements:** ComMCS (AAAI 2026) reduces MC estimator variance via compounding estimates across adjacent step positions (TD(λ)-style) without extra inference, gaining +2.8 best-of-N points. Theorem 4.2 establishes MC estimation as the MVUE given single-step information. SCAN (NeurIPS 2025) addresses MC annotation noise via self-denoising. Math-Shepherd (ACL 2024) and OmegaPRM (arXiv 2024) established MC-based PRM annotation but flag the cold-start problem without solution. **Reward model distillation:** RM-Distiller (arXiv 2601.14032, 2026) systematically distills from generative LLMs to discriminative reward models via refinement, scoring, and generation capabilities. The reverse direction — discriminative PRM to generative PRM distillation — remains unexplored. **Fast PRM motivation:** Fast-Slow Thinking RM (arXiv 2603.20212, 2026) proposes hybrid scalar/generative RM. PRIME (arXiv 2502.01456, 2025) derives implicit process rewards, achieving 2.5× faster training. SPRO (arXiv 2507.01551, 2025) achieves 3.4× higher training efficiency. **Frontier-hard verification benchmarks:** Hard2Verify (arXiv 2510.13744, 2025) provides 80 frontier Olympiad problems with 1,860 human-annotated steps; the best open-source model (DeepSeek-R1) achieves 68.92% step-level accuracy; GPT-5 leads at 86.53%. **Co-evolutionary and curriculum approaches:** RL Tango (NeurIPS 2025) co-evolves generator and generative verifier. SCRL (arXiv 2605.22074, 2026) decomposes hard problems into verifiable subproblems. R³ (ICML 2024) applies reverse curriculum RL for policy training. AURORA (arXiv 2025) uses reverse verification. **Gap:** No existing work (a) provides systematic domain-level empirical calibration of SIA's informativeness accumulation rate within mathematics, (b) provides formal conditions for MC informativeness as a function of step position with domain-specific dependency corrections, (c) proposes a step-position-aware reverse curriculum for PRM training, (d) combines position-aware curriculum with adaptive per-step rollout allocation, (e) produces efficient discriminative PRMs that resist Hard2Verify-level collapse, (f) tests discriminative-to-generative PRM distillation, (g) explicitly addresses the anti-complementarity risk in composing data selection efficiency (ActPRM-style) with annotation quality improvement (RCB-style), or (h) tests whether curriculum-based MC quality improvement (RCB) composes with or is superseded by rollout-free information-theoretic labeling (MCNIG).\",\n  \"inspired_by\": \"Field gap: process supervision for problems at or beyond the model's capability frontier, where MC estimation produces degenerate near-zero-variance estimates, probability-based methods (CPMI) produce uncalibrated scores, and current discriminative PRMs collapse catastrophically (78.3→37.3 F1 on Hard2Verify). Theoretical anchor: SIA (Feng et al., arXiv 2604.06192) formalizes that reasoning prefixes accumulate answer-relevant information (I_p(A; C_{1:k} | Q) ≥ ε_k > 0), and empirically demonstrates that this informativeness property varies substantially across task domains (ρ_SIA = 0.682 on GSM8K vs 0.344 on ARC). But SIA does not characterize variation within mathematics, does not connect to PRM training quality, and does not benchmark on frontier-hard problems. This gap is precisely what δ_d fills: we provide the first systematic empirical test of SIA's informativeness accumulation rate across mathematical domains. If δ_d reveals significant domain variation within mathematics — near-independent domains (δ_d < 0.2: multi-step algebraic computation, sequential equation solving, coordinate geometry) exhibiting smooth, predictable informativeness accumulation consistent with SIA, vs strongly dependent domains (δ_d > 0.5: insight-dependent proofs, combinatorial constructions, auxiliary-line geometry) showing abrupt transitions where a single gateway step disrupts smooth accumulation — it demonstrates that SIA's informativeness property, while broadly correct, accumulates at fundamentally different rates across mathematical domains. This finding would constitute empirical calibration and partial falsification of a uniform-rate reading of SIA, with implications beyond PRM training: it provides the first systematic evidence for domain-specific information accumulation dynamics in mathematical reasoning. This connects to Conditional Reward Modeling (arXiv 2509.26578) which formalizes inter-step dependencies via conditional probability chains, to 'What Are Step-Level Reward Models Rewarding?' (AAAI 2025) which empirically demonstrates that context-aware step evaluation outperforms context-free variants, to 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) which independently confirms from representation geometry that late steps are ~20 AUC points more predictive of correctness than early steps (average late-step 0.83 vs early-step 0.63 AUC, with peak single-layer reaching 0.87), and to SHAPE (Ai et al., arXiv 2604.06636) which provides convergent evidence from RL credit assignment that step position matters for learning signal quality (stage-aware potential-based advantage yields 3% accuracy gain + 30% token reduction). Our δ_d estimates provide the systematic per-domain empirical calibration that all these frameworks lack. Theoretical foundation: elementary Markov chain completion probability — the MC success rate from step k in a K-step solution is approximately p^{K-k} under an independent-step model, giving an exponential gradient that is sharper for harder problems. The key theoretical contribution is formalizing this into sufficient conditions (Theorem 1) under the independence idealization, with δ_d-calibrated corrections providing domain-aware bounds. The SIA connection strengthens this: our Theorem 1's independence idealization corresponds to the maximal-rate limit of SIA's information accumulation (ε_k growing exponentially), while high-δ_d domains correspond to attenuated SIA accumulation rates where the exponential gradient is dampened. Methodological innovation: (1) the AMCS-RCB combination addresses a 2D resource allocation problem (which steps to annotate × how many rollouts per step) that neither approach solves alone — AMCS (adaptive budget via Wilson score uncertainty) is orthogonal to RCB (curriculum over step positions via success rate gradient); (2) the ActPRM+RCB composition addresses a second orthogonal dimension — which steps to annotate (ActPRM's uncertainty-based selection) vs. how to annotate them (RCB's quality-improving curriculum) — but with an important caveat: if ActPRM's uncertain steps cluster at early positions where MC estimates are uninformative, the composition may produce anti-complementarity rather than multiplicative gains (failure mode F7); Phase 0 explicitly diagnoses this by analyzing ActPRM's step selection distribution across positions; (3) the discriminative-to-generative distillation pipeline reverses the typical RM-Distiller direction, using RCB-trained discriminative PRMs as cheap labelers to generate massive training data for generative PRMs — novel because discriminative PRMs produce labels at ~1000× lower cost per step than generative PRMs; (4) MCNIG composition: testing whether MCNIG's rollout-free labels can replace MC rollouts within the RCB curriculum stages, combining the curriculum's domain-aware ordering with MCNIG's computational efficiency — if MCNIG labels degrade on frontier-hard problems similarly to CPMI, RCB-MC labels remain superior; if MCNIG labels are robust, the composition achieves both quality and efficiency gains. Deployment motivation: the well-documented need for efficient discriminative PRMs in online RL training loops (GRPO/PPO), where generative PRMs are prohibitively expensive (Setlur et al. 2025; Fast-Slow Thinking RM 2026; PRIME and SPRO workarounds). Broader impact: the consistent gap between unsupervised/rollout-free methods and supervised MC-based PRMs on hard problems, plus the Hard2Verify collapse, demonstrate that annotation quality is the decisive bottleneck. Complementarity: CPMI-trained PRM for moderate-difficulty problems (cheapest), MCNIG-trained PRM for moderate-to-hard problems (stronger rollout-free), AMCS-RCB-trained discriminative PRM for frontier-hard RL training, generative PRM (optionally distillation-enhanced) for high-stakes test-time verification.\",\n  \"approach\": \"We propose Reverse-Curriculum Bootstrapping (RCB), a theoretically grounded annotation and training framework. The narrative arc is: discover structure and test SIA (Contribution I) → formalize with domain-aware corrections (Contribution II) → build methods (Contributions III-IV) → evaluate and deploy (Contribution V). **Contribution I — Empirical Discovery: Domain-Dependent Reasoning Step Correlation Structure as Empirical Test of SIA (weeks 1-3, Phase 0).** This is the paper's most novel and independently valuable contribution. We provide the first systematic empirical characterization of how mathematical reasoning step correlations vary across domains, framed as the first domain-level empirical test of SIA's informativeness accumulation rate within mathematics. For each of the 7 primary Omni-MATH domains (Algebra, Precalculus, Calculus, Geometry, Discrete Mathematics, Number Theory, Applied Mathematics) and ≥10 of 33+ sub-domains: (a) Select 50+ problems per domain/sub-domain spanning difficulty levels. (b) Generate 8-12-step candidate solutions using Qwen3-32B. (c) Run N=64 MC rollouts from each step position k using Qwen3-32B as completer. (d) Measure success rate as a function of normalized step position (k/K), stratified by problem difficulty and mathematical domain. (e) Compute the dependency index δ_d = 1 − corr(empirical μ_k, predicted p_min^{K−k}) for each domain d, where p_min is the estimated per-step correctness probability. When δ_d ≈ 0, independence holds and the exponential gradient is fully exploitable; when δ_d is large, inter-step correlations attenuate the gradient. (f) Classify domains into tiers: near-independent (δ_d < 0.2), moderately dependent (0.2 ≤ δ_d < 0.5), strongly dependent (δ_d ≥ 0.5). (g) Compute bootstrap confidence intervals (95% CI) for all δ_d estimates to establish statistical significance. Target: δ_d classification accuracy ≥85% — the domain classification into near-independent/moderately-dependent/strongly-dependent should be robust across different problem samples from the same domain. (h) Test the mixture model: for strongly-dependent domains, fit the two-class mixture model where fraction α of problems have a 'gateway step' (p_gateway << p_other) and the rest are near-independent. Estimate α per domain. (i) Anti-complementarity diagnostic for ActPRM+RCB composition: reproduce ActPRM's ensemble uncertainty estimation on the same problem set and analyze whether ActPRM's selected uncertain steps correlate with step position. Specifically, test whether ensemble uncertainty is highest at early positions where MC estimates are uninformative — if so, this indicates the selection-quality tension described in failure mode F7. (j) SIA calibration analysis: compute the informativeness accumulation profile for each domain by measuring how I(A; C_{1:k} | Q) (approximated via probing accuracy or answer entropy) grows as a function of k/K. Compare the shape of this accumulation curve across domains and correlate with δ_d. Test whether domains with high δ_d (near-independence, tight exponential gradient) also show rapid SIA-style informativeness accumulation (high ε_k growth rate), while domains with low δ_d (strong dependency) show attenuated accumulation with abrupt transitions. This directly tests whether SIA's ε_k is domain-uniform or domain-dependent within mathematics, and quantifies the degree of non-uniformity. (k) Compare δ_d domain ordering with SIA's ρ_SIA ordering (replicating SIA's entropy-based measurement on the same problem domains) to test whether the two frameworks — probability-based (δ_d) and information-theoretic (ρ_SIA) — converge on the same domain structure. The δ_d characterization constitutes a standalone contribution regardless of RCB's effectiveness: it is the first empirical study connecting reasoning step correlation structure to mathematical domain properties AND the first domain-level empirical calibration of SIA, extending the geometric trajectory analysis of 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) — which shows late steps are ~20 AUC points more predictive of correctness (average late-step 0.83 vs early-step 0.63 AUC, with peak single-layer reaching 0.87) — with domain-level structural decomposition. It also complements EvalQReason's (arXiv 2602.02295, 2026) Consecutive Step Divergence metric by providing a global positional characterization rather than local pairwise coherence, and complements SHAPE's (arXiv 2604.06636) finding that step position matters for RL credit assignment by showing that it also matters for MC annotation quality in a domain-structured way. Concrete domain predictions based on mathematical structure: (i) Near-independence domains: multi-step algebraic computation (each step is a mechanistic transformation — e.g., polynomial expansion, equation manipulation — where correctness depends primarily on local arithmetic accuracy), sequential equation solving (substitution chains where each step's validity depends mainly on correctly applying the substitution), and coordinate geometry with computational steps (once the coordinate system is established, each computation is largely independent). These domains should show rapid SIA-style informativeness accumulation (high ε_k growth rate), consistent with the exponential gradient, and Theorem 1 provides tight predictions. (ii) Strong-dependency domains: insight-dependent proofs (choosing the right lemma or proof technique at step 1 — e.g., applying Vieta's formulas vs. direct computation for a symmetric polynomial problem — determines the viability of all subsequent steps, creating a single 'gateway' step with near-binary influence), combinatorial arguments requiring a key construction (e.g., finding the right bijection or invariant), and geometry problems requiring auxiliary constructions (e.g., drawing the right auxiliary line in a Euclidean geometry proof). These domains should show attenuated SIA accumulation with abrupt transitions at gateway steps, and high δ_d values. Total Phase 0 cost: ~300 H100-hours. Go/no-go criteria (domain-stratified): (i) Full-go: for ≥40% of frontier-hard problems (pass@1 < 5%), late-step rollouts (k/K > 0.8) achieve success rates ≥10%, AND δ_d shows meaningful variation across domains (range ≥ 0.3); (ii) Partial-go: 20-40% meet criterion (i), proceed with RCB restricted to qualifying domains (those with δ_d < 0.5); (iii) No-go: <20% qualify, pivot to AMCS-enhanced compounding estimators combined with difficulty curriculum, but still publish the δ_d characterization and SIA calibration analysis as standalone contributions. **Contribution II — Theoretical Framework with Domain-Aware Corrections (weeks 1-2, concurrent with Phase 0):** We formalize the position-dependent MC informativeness under an independent-step Markov model, with corrections calibrated by the empirical δ_d values from Contribution I. Definition: an MC estimate at step k with N rollouts is c-informative if E[successes] = N·μ_k ≥ c, where μ_k = ∏_{j=k}^{K} p_j is the completion success rate. Proposition 1 (Monotonicity): μ_k ≤ μ_{k+1} for all k — informativeness is non-decreasing with step position. This holds regardless of the independence assumption since later steps are strictly closer to completion. Proposition 2 (Exponential Gradient): if per-step correctness p_j ∈ [p_min, p_max], then μ_k ∈ [p_min^{K-k}, p_max^{K-k}], giving approximately exponential growth toward later steps on hard problems. Theorem 1 (RCB Sufficient Condition, under independence idealization with δ_d-calibrated corrections): RCB produces strictly more informative annotations than uniform MC estimation whenever K > log(c/N)/log(p_min), with the earliest informative step at k* = K − ⌊log(c/N)/log(p_min)⌋. For domains with δ_d > 0, Theorem 1's bound is conservative by factor ~(1 − α_d) where α_d is the estimated gateway fraction from the mixture model. Corollary (Difficulty Threshold): RCB is beneficial when problem difficulty exceeds 1 − (c/N)^{1/K}. Updated framing: Theorem 1 provides 'sufficient conditions under the independence idealization, with empirically-calibrated corrections for domain-specific dependency structures characterized by δ_d.' The theoretical framework explicitly connects to SIA: our independence idealization corresponds to the maximal-rate limit of SIA's information accumulation (ε_k growing at an exponential rate matching the Markov chain success-rate gradient), while domains with high δ_d exhibit attenuated SIA accumulation rates where the exponential gradient is dampened by inter-step dependencies. The theoretical framework connects to ComMCS's compound variance formula (Theorem 4.3) by showing that RCB's position-aware annotation focuses variance reduction where it matters most. Under a simplified two-class mixture model where a fraction α of problems have a 'gateway step' (p_gateway << p_other) and the rest are near-independent, the effective success rate curve becomes: μ_k = α · p_gateway · p_other^{K-k-1} + (1-α) · p_other^{K-k}. The exponential gradient is preserved (dominated by the second term for moderate α) but attenuated in magnitude. **Contribution III — RCB Curriculum (weeks 4-14):** Enabled by the structural discovery (Contribution I) and theoretical framework (Contribution II). Phase 1 (weeks 4-6): Run MC rollouts from late step positions (k/K > 0.75) where the pilot confirmed non-trivial success rates, using Qwen3-235B-A22B as completer. Train PRM_0 (Qwen3-7B base). Domain-aware curriculum: for near-independent domains (δ_d < 0.2), extend the curriculum aggressively (5 phases); for strongly dependent domains (δ_d ≥ 0.5), use a conservative curriculum (2-3 phases) that terminates earlier. Phases 2-5 (weeks 6-14): Each phase i uses PRM_{i-1} to guide rollouts at progressively earlier step windows via best-of-16 selection. Early termination: if PRM-guided rollouts do not achieve ≥2pp higher success rate than unguided. **Contribution IV — AMCS-RCB Combined Method and ActPRM+RCB Composition (weeks 4-14, parallel variants):** AMCS-RCB: Within each RCB phase, replace the fixed rollout budget (N=64) with AMCS-style adaptive allocation: use Wilson score interval to allocate k_init=6 to k_max=32 rollouts per step based on estimation uncertainty. This addresses the 2D resource allocation problem: RCB determines *which steps to annotate* (step position curriculum), AMCS determines *how many rollouts per step* (uncertainty-adaptive budget). Theoretical connection: Theorem 1 determines the informative step range; AMCS optimizes rollout allocation within that range. Expected benefit: 20-30% compute reduction with equivalent or better label quality. ActPRM+RCB composition ablation: Replace uniform step selection with ActPRM's ensemble uncertainty-based selection within the RCB curriculum. Three sub-conditions: (i) Naive composition: ActPRM selects steps, RCB provides MC estimates — tests raw complementarity; (ii) Hybrid composition: ActPRM selects steps only from within the RCB-determined informative window (k ≥ k*), combining quality-aware selection with quality-aware annotation — mitigates the anti-complementarity risk; (iii) Comparison: measure whether ActPRM's uncertain steps disproportionately fall inside vs. outside the informative window, directly testing the F7 failure mode hypothesis. (+100 H100-hours for this ablation.) **Contribution V — Dual-Track Evaluation and Distillation Pipeline:** Track A (discriminative, weeks 4-16): Train 7B discriminative PRM via RCB and AMCS-RCB curricula. Evaluate on ProcessBench (OmniMATH, OlympiadBench), Hard2Verify, PRMBench, and best-of-N accuracy on Omni-MATH hard-filtered and AIME 2025/2026 hardest problems. Track B (dependency characterization + SIA calibration + generative + distillation, weeks 12-18): (B1) Primary deliverable — Complete δ_d characterization AND SIA calibration: publish δ_d values with bootstrap 95% CIs across all 7 primary Omni-MATH domains AND ≥10 of 33+ sub-domains. Include δ_d classification robustness analysis (target: ≥85% accuracy on held-out problem samples). Analyze relationship between δ_d and problem structural features (proof vs. computation, number of key insights, solution path diversity). Publish SIA calibration results: correlation between δ_d and ρ_SIA across domains, informativeness accumulation profiles per domain, evidence for/against uniform SIA accumulation rate within mathematics. Connect findings to Conditional Reward Modeling (arXiv 2509.26578) and provide systematic empirical calibration for their conditional probability framework. (B2) Multi-architecture fine-tuning: fine-tune GenPRM, ThinkPRM, and R-PRM architectures on RCB-annotated data vs. standard MC annotations from the same problems, testing whether annotation quality is a paradigm-wide bottleneck across generative PRM architectures. (B3) Novel discriminative-to-generative distillation pipeline: use the RCB-trained discriminative PRM (fast, single forward pass per step) to generate step-level correctness labels on a large corpus of solution traces (100K+ traces), then use these cheap labels to fine-tune generative PRMs. This reverses the typical RM-Distiller direction (generative→discriminative) and exploits the ~1000× cost advantage of discriminative inference. (B4) Hard2Verify generative evaluation: evaluate RCB-fine-tuned generative PRMs on Hard2Verify. **Ablations (weeks 14-17):** (1) RCB vs. uniform MC estimation; (2) RCB vs. stronger completer only (Qwen3-235B with higher rollout budget); (3) AMCS-RCB vs. pure AMCS vs. pure RCB — the key Contribution IV comparison; (4) CPMI labels vs. RCB MC labels at matched difficulty, testing complementarity; (5) MCNIG labels vs. RCB MC labels — testing whether MCNIG's rollout-free information-theoretic approach matches or exceeds RCB-MC quality on frontier-hard problems, and whether MCNIG labels composed with RCB curriculum (MCNIG labels within RCB domain ordering) achieves further gains. This ablation directly addresses whether curriculum-based MC quality improvement (RCB) is complementary to or superseded by rollout-free information-theoretic labeling (MCNIG); (6) Inference speed comparison: wall-clock time per evaluation for RCB discriminative PRM vs. GenPRM, ThinkPRM, RM-R1, for a representative GRPO scenario (1,000 prompts × 16 rollouts × 20 steps = 320,000 evaluations per epoch); (7) Distillation efficiency: compare generative PRM trained on discriminative-PRM labels vs. same model trained on MC labels vs. same model trained on RCB-MC labels, at matched data scale; (8) ActPRM+RCB composition: naive vs. hybrid vs. ActPRM-only vs. RCB-only (as described in Contribution IV above); (9) Domain-stratified RCB: run RCB separately on near-independence vs. strong-dependency domains (as classified by δ_d from Phase 0) to test whether the curriculum adapts naturally to different correlation structures, and whether restricting to near-independent domains yields disproportionate gains; (10) SIA alignment: for each domain, compare the δ_d value with the SIA ρ_SIA value measured on the same problems, testing convergence between the probability-based and information-theoretic frameworks. **Evaluation (weeks 17-19):** Track A targets — ProcessBench OmniMATH: improve 7B discriminative PRM F1 from 67.0 baseline (ActPRM, current strongest 7B) to 72-76 F1, approaching ThinkPRM-7B (74.0 F1) without generative overhead; OlympiadBench: 74-78 F1 vs. 71.4 ActPRM baseline; Hard2Verify: target ≥50 F1 (from 37.3 baseline for 72B model — demonstrating that RCB-trained 7B PRM resists catastrophic frontier-hard collapse). Track B targets — Primary: δ_d characterization across all 7 Omni-MATH domains + ≥10 sub-domains with bootstrap CIs, δ_d classification accuracy ≥85%, SIA calibration analysis with ρ_SIA comparison. Secondary: ProcessBench OmniMATH for RCB-fine-tuned generative PRMs: ≥3 F1 improvement on Hard2Verify, ≥2 F1 on ProcessBench OmniMATH across at least 2 of 3 tested architectures; distillation pipeline: achieve ≥90% of MC-trained generative PRM accuracy with 10× less labeling compute, demonstrating discriminative-to-generative knowledge transfer. Additional baselines: compare RCB-trained PRM against MCNIG-trained PRM on ProcessBench per-subset and Hard2Verify to establish whether curriculum-based MC quality improvement or rollout-free information-theoretic labeling is more effective at the capability frontier. **Failure mode analysis:** (F1) Pilot invalidation — theoretical gradient insufficient, with partial-go and no-go pathways (no-go still publishes δ_d characterization and SIA calibration analysis as standalone contributions, which are independently valuable); (F2) Bootstrap cascade failure — caught by early termination criterion; (F3) Key-insight ceiling — problems where single critical insight determines correctness at all subsequent steps, quantified by high δ_d values and handled by domain-stratified analysis and the mixture model framework; (F4) AMCS-RCB overhead — if adaptive allocation overhead exceeds compute savings, pure RCB may dominate; (F5) Track B null result — if annotation quality does not improve generative PRMs, this is an informative negative result (generative PRMs learn via reasoning rather than training data quality), and Track A + distillation pipeline + theoretical contribution + dependency characterization + SIA calibration remain primary; (F6) Independence violation too severe — if δ_d > 0.5 for most domains, the exponential gradient is too attenuated for RCB to substantially outperform simple late-step-only training; however, this is itself a strong finding: it would demonstrate that SIA's informativeness accumulation is severely non-uniform within mathematics, with most domains exhibiting attenuated accumulation rather than smooth exponential growth — a finding with broad implications beyond PRM training; (F7) ActPRM+RCB anti-complementarity — if ActPRM's ensemble uncertainty correlates positively with step position (i.e., uncertain steps cluster at early positions where MC estimates are uninformative), the naive composition produces tension rather than multiplicative gains. Phase 0 explicitly tests this by analyzing ActPRM's step selection distribution across positions. Mitigation: if anti-complementarity is confirmed, use the hybrid strategy where ActPRM selects steps from the RCB-determined informative window (k ≥ k*), combining quality-aware selection with quality-aware annotation. If neither naive nor hybrid composition outperforms the individual methods, this is itself an informative finding about the interaction structure of data selection and data quality optimization; (F8) MCNIG supersedes RCB — if MCNIG labels prove equally effective on frontier-hard problems without rollouts, the RCB curriculum may be unnecessary for annotation quality. However, even in this case, the δ_d characterization and SIA calibration remain independently valuable, and the composition of MCNIG with domain-aware curriculum ordering may still yield gains by directing MCNIG's computational resources to the most informative problems and domains. **Practical deployment framework (four-tier):** CPMI-trained PRM for moderate-difficulty problems (cheapest), MCNIG-trained PRM for moderate-to-hard problems (stronger rollout-free), AMCS-RCB-trained discriminative PRM for frontier-hard RL training, generative PRM (optionally distillation-enhanced) for high-stakes test-time verification.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"7500 H100-hours (300 for Phase 0 including completer evaluation + MC pilot + AMCS baseline + CPMI comparison + MCNIG baseline reproduction + ActPRM baseline reproduction + dependency index computation across 7 domains and ≥10 sub-domains + SIA calibration analysis, 3200 for MC rollout generation across Phases 1-5, 1200 for iterative discriminative PRM fine-tuning, 400 for AMCS-RCB parallel track, 1000 for Track B multi-architecture generative PRM fine-tuning + distillation pipeline, 900 for ablations including ActPRM+RCB composition (naive + hybrid), domain-stratified RCB, MCNIG comparison + composition, and SIA alignment analysis, 500 for evaluation including Hard2Verify benchmarking and inference speed measurement)\",\n      \"timeline\": \"18-19 weeks (2 weeks theoretical framework + Phase 0 pilot concurrent, 1 week go/no-go + curation, 10 weeks for 5 RCB phases with AMCS-RCB parallel, 4 weeks Track B parallel from week 12, 2 weeks ablations including MCNIG comparison, 1-2 weeks evaluation/writing)\",\n      \"estimated_gpu_cost\": \"$21,375 (at ~$2.85/H100-hour)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"6500 H100-hours (efficiency gains from Claude-assisted theoretical analysis, SIA calibration analysis, pilot data fitting, dependency index computation, automated hyperparameter tuning, MCNIG baseline reproduction, and ablation design reducing wasted runs by ~13%)\",\n      \"timeline\": \"15-16 weeks (Claude accelerates theoretical framework development, SIA calibration analysis, dependency analysis, pilot analysis, Phase 0 model fitting, experiment scripting, MCNIG baseline reproduction, and paper drafting, saving ~3 weeks; fits estimated ICLR 2027 deadline starting June 1)\",\n      \"claude_api_cost\": \"$1,400 (Sonnet 4.6 for code generation, theoretical proof verification, SIA calibration analysis, dependency characterization analysis, pilot data analysis, experiment orchestration, Track B design, MCNIG comparison design, and paper drafting; ~320M input + 70M output tokens)\",\n      \"estimated_gpu_cost\": \"$18,525\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"8600 H100-hours (additional compute for AMCS-RCB hyperparameter sweeps, ActPRM+RCB composition search including naive vs. hybrid variants, MCNIG baseline reproduction + MCNIG-RCB composition experiments, multi-architecture Track B fine-tuning, distillation pipeline optimization, systematic ablation execution, dependency model validation across all 7+10 domains/sub-domains, SIA calibration analysis across all domains, and domain-stratified analysis)\",\n      \"timeline\": \"11-12 weeks (fully automated pipeline with parallel RCB + AMCS-RCB tracks and parallel Track B; pilot phase still requires ~2.5 weeks for sequential completer evaluation + analysis)\",\n      \"claude_api_cost\": \"$4,600 (heavy Opus 4.7 usage for autonomous experiment design, theoretical framework development, SIA calibration analysis, dependency characterization, pilot go/no-go analysis, AMCS-RCB integration, ActPRM+RCB composition, MCNIG comparison and composition, distillation pipeline design, and adaptive protocol modification; ~490M input + 135M output tokens)\",\n      \"estimated_gpu_cost\": \"$24,510\",\n      \"speed_bottleneck\": \"MC rollout generation with Qwen3-235B-A22B completer requires multi-node inference; RCB phases are inherently sequential; AMCS-RCB runs in parallel with pure RCB track; Track B independent from week 12. Distillation pipeline requires completed Track A discriminative PRM. ActPRM baseline reproduction, MCNIG baseline reproduction, and dependency analysis parallelizable with Phase 0. δ_d characterization across all 7+10 domains/sub-domains requires comprehensive Phase 0 coverage but is parallelizable across domains. SIA calibration analysis runs in parallel with δ_d computation.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (estimated deadline: ~September 2026, projected from ICLR 2026 schedule; not officially announced as of May 2026) — primary target, 15-16 week human-in-loop timeline fits starting June 1\",\n    \"AISTATS 2027 (estimated deadline: October 2026) — backup if additional time needed\",\n    \"ICML 2027 (full paper estimated: ~January 2027) — comfortable deadline for full manual timeline\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Let's Verify Step by Step (ICLR 2024)\",\n    \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations (ACL 2024)\",\n    \"Improve Mathematical Reasoning in Language Models by Automated Process Supervision [OmegaPRM] (arXiv 2024)\",\n    \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (ICLR 2025)\",\n    \"rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking (ICML 2025)\",\n    \"Training Large Language Models for Reasoning through Reverse Curriculum Reinforcement Learning [R3] (ICML 2024)\",\n    \"SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning (NeurIPS 2025)\",\n    \"Process Reward Models That Think [ThinkPRM] (TMLR 2026; arXiv 2504.16828)\",\n    \"The Lessons of Developing Process Reward Models in Mathematical Reasoning (ACL Findings 2025)\",\n    \"ProcessBench: Identifying Process Errors in Mathematical Reasoning (ACL 2025)\",\n    \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026)\",\n    \"R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025)\",\n    \"Dyve: Thinking Fast and Slow for Dynamic Process Verification (EMNLP 2025)\",\n    \"RM-R1: Reward Modeling as Reasoning (ICLR 2026)\",\n    \"SCRL: From Reasoning Chains to Verifiable Subproblems — Curriculum RL Enables Credit Assignment for LLM Reasoning (arXiv 2605.22074, 2026)\",\n    \"ComMCS: Improving Value-based Process Verifier via Low-Cost Variance Reduction (AAAI 2026)\",\n    \"Omni-MATH: A Universal Olympiad Level Mathematic Benchmark For Large Language Models (ICLR 2025)\",\n    \"AURORA: Automated Process Reward Model Training via Reverse Verification (arXiv 2025)\",\n    \"RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning (NeurIPS 2025)\",\n    \"Unsupervised Process Reward Models [uPRM] (arXiv 2605.10158, 2026)\",\n    \"Fast-Slow Thinking RM: Efficient Integration of Scalar and Generative Reward Models (arXiv 2603.20212, 2026)\",\n    \"PRIME: Process Reinforcement through Implicit Rewards (arXiv 2502.01456, 2025)\",\n    \"Is PRM Necessary? Problem-Solving RL Implicitly Induces PRM Capability in LLMs (arXiv 2505.11227, 2025)\",\n    \"When To Solve, When To Verify: Compute-Optimal Problem Solving and Verification (Setlur et al., arXiv 2504.01005, 2025)\",\n    \"Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems (arXiv 2026)\",\n    \"Efficient Process Reward Modeling via Contrastive Mutual Information [CPMI] (arXiv 2604.10660; confirmed accepted at ACL 2026 Main Conference)\",\n    \"From Static to Dynamic: Adaptive Monte Carlo Search for Mathematical Process Supervision [AMCS] (arXiv 2509.24351, 2025)\",\n    \"Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (arXiv 2510.13744, 2025)\",\n    \"RM-Distiller: Exploiting Generative LLM for Reward Model Distillation (arXiv 2601.14032, 2026)\",\n    \"SPRO: Self-Guided Process Reward Optimization with Redefined Step-wise Advantage (arXiv 2507.01551, 2025)\",\n    \"Efficient Process Reward Model Training via Active Learning [ActPRM] (arXiv 2504.10559, COLM 2025)\",\n    \"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning (arXiv 2509.26578, 2025)\",\n    \"What Are Step-Level Reward Models Rewarding? Counterintuitive Findings from MCTS-Boosted Mathematical Reasoning (AAAI 2025)\",\n    \"LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals (arXiv 2604.05655, 2026)\",\n    \"EvalQReason: A Framework for Step-Level Reasoning Evaluation in Large Language Models (arXiv 2602.02295, 2026)\",\n    \"The Stepwise Informativeness Assumption: Why are Entropy Dynamics and Reasoning Correlated in LLMs [SIA] (arXiv 2604.06192, 2026)\",\n    \"SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning (arXiv 2604.06636, 2026)\",\n    \"Process Supervision for Chain-of-Thought Reasoning via Monte Carlo Net Information Gain [MCNIG] (arXiv 2603.17815, TMLR 03/2026)\"\n  ],\n  \"description\": \"This project addresses the Monte Carlo cold-start problem in process reward model training through five integrated contributions, reframed to lead with the paper's most novel discovery and its connection to a concurrent theoretical framework: (I) the first systematic empirical characterization of domain-dependent reasoning step correlation structure across mathematical domains via the dependency index δ_d = 1 − corr(empirical μ_k, predicted p^{K−k}), simultaneously providing the first domain-level empirical test and calibration of SIA's informativeness accumulation rate (Feng et al., arXiv 2604.06192) within mathematics, (II) a theoretical framework formalizing MC estimation informativeness as a function of step position under an independence idealization with δ_d-calibrated corrections, explicitly connected to SIA's information-theoretic formulation, (III) a reverse-curriculum bootstrapping (RCB) annotation algorithm enabled by the structural discovery, (IV) a combined AMCS-RCB method integrating adaptive per-step rollout allocation with position-aware curriculum, and (V) dual-track evaluation with a novel discriminative-to-generative PRM distillation pipeline. The narrative arc: SIA (arXiv 2604.06192) establishes that reasoning prefixes accumulate answer-relevant information (I_p(A; C_{1:k} | Q) ≥ ε_k > 0) and shows this varies across task domains (ρ_SIA = 0.682 on GSM8K vs 0.344 on ARC), but does not characterize variation within mathematics or connect to PRM training. We discover that mathematical reasoning exhibits fundamentally different step correlation structures across domains — from near-independent (algebraic computation: δ_d < 0.2) to strongly dependent (insight-dependent proofs: δ_d > 0.5) — providing the first systematic empirical test of whether SIA's informativeness accumulation rate is domain-uniform or domain-dependent within mathematics. If δ_d reveals significant domain variation, it demonstrates that SIA's informativeness accumulation is non-uniform in a structured, domain-specific way — a finding with implications beyond PRM training for any method assuming uniform step-level informativeness. This structural discovery enables domain-aware annotation strategies that were previously impossible. Independent geometric evidence from 'LLM Reasoning as Trajectories' (arXiv 2604.05655, 2026) confirms the positional informativeness gradient: late reasoning steps are ~20 AUC points more predictive of correctness than early steps (average late-step 0.83 vs early-step 0.63 AUC, with peak single-layer reaching 0.87), with correct/incorrect trajectories diverging primarily at late stages in representation space. SHAPE (Ai et al., arXiv 2604.06636) provides convergent evidence from RL credit assignment: stage-aware potential-based advantage yields 3% accuracy gain + 30% token reduction, with early-stage improvements providing ~18% higher marginal returns — confirming that step position matters for learning signal quality across both RL credit assignment and MC annotation quality domains. The severity of the problem is now quantified by Hard2Verify: Qwen2.5-Math-PRM-72B collapses from 78.3 F1 on ProcessBench to 37.3 on frontier-hard Olympiad problems — a catastrophic 41-point drop. While generative PRMs bypass MC estimation via inference-time reasoning (ThinkPRM-14B: 85.7 F1), they generate 1,000-5,000 tokens per step — infeasible for RL training (Setlur et al. 2025: GenRM needs 8× compute to match self-consistency, up to 128× for a 3.8% accuracy gain, Figure 1b; 512× for Qwen-2.5-7B, Appendix H). Rollout-free alternatives span a wide performance range: CPMI (25.6 F1 on OmniMATH, confirmed accepted at ACL 2026), uPRM (39.8 F1), and MCNIG (Royer et al., arXiv 2603.17815, TMLR 03/2026) achieving ProcessBench overall F1 of 73.2 (8B) and 75.1 (14B) via information-theoretic log-probability contrast at O(N) complexity — surpassing QwenPRM 7B (75.0) — but with frontier-hard performance unverified. ActPRM (COLM 2025) achieves the current strongest 7B discriminative PRM performance (67.0 F1 OmniMATH, 75.0 avg F1 ProcessBench) via active learning-based step selection with only 20% of UniversalPRM's annotation budget, but optimizes data selection without addressing MC estimation quality — the step selection and annotation quality dimensions are orthogonal, with a potential anti-complementarity tension when composed with RCB (failure mode F7: if ActPRM's uncertain steps cluster at early positions where MC estimates are uninformative, the composition produces tension rather than multiplicative gains; Phase 0 explicitly diagnoses this, with a hybrid mitigation constraining ActPRM selection to the RCB-determined informative window). AMCS (arXiv 2509.24351) adaptively allocates rollout budget per-step via Wilson score interval uncertainty but treats all step positions symmetrically and does not address the fundamental uninformativeness of early-step MC estimates on hard problems. **Contribution I** provides the δ_d dependency index across all 7 primary Omni-MATH domains (Algebra, Precalculus, Calculus, Geometry, Discrete Mathematics, Number Theory, Applied Mathematics) and ≥10 of 33+ sub-domains, with bootstrap confidence intervals and ≥85% classification robustness target. This serves simultaneously as (a) the first systematic domain-level quantification of step independence violation, (b) the first empirical calibration of SIA's informativeness accumulation rate within mathematics — including SIA ρ_SIA comparison on the same domains — and (c) complementary empirical grounding for the theoretical frameworks of Conditional Reward Modeling (arXiv 2509.26578) and 'What Are Step-Level Reward Models Rewarding?' (AAAI 2025), providing systematic per-domain calibration that both lack. **Contribution II** formalizes the position-dependent MC gradient: under the independence idealization, the success rate from step k is approximately p^{K-k}, giving exponential growth toward later steps. Theorem 1 provides sufficient conditions for when RCB outperforms uniform MC: whenever K > log(c/N)/log(p_min), early steps are uninformative regardless of rollout budget. For domains with δ_d > 0, Theorem 1's bound is conservative by factor ~(1-α_d), but RCB remains beneficial because Proposition 1 (monotonicity of μ_k) holds regardless of independence. The theoretical framework connects to SIA: the independence idealization corresponds to maximal-rate SIA accumulation (ε_k growing exponentially), while high-δ_d domains exhibit attenuated accumulation rates. **Contribution III** (RCB) exploits the gradient with domain-aware curriculum depth: aggressive (5 phases) for near-independent domains, conservative (2-3 phases) for strongly dependent domains. **Contribution IV** (AMCS-RCB) combines position curriculum with adaptive rollout allocation — addressing the 2D resource optimization that neither method solves alone. **Contribution V** introduces dual-track evaluation separating annotation quality from model capability: Track A trains a 7B discriminative PRM targeting 72-76 F1 on ProcessBench OmniMATH (5-9 points over ActPRM's 67.0, current strongest 7B) and ≥50 F1 on Hard2Verify (vs. 37.3 baseline for 72B model); Track B's primary deliverable is the complete δ_d characterization with SIA calibration analysis (ρ_SIA comparison, informativeness accumulation profiles per domain) and statistical significance tests, with secondary targets of ≥3 F1 improvement on Hard2Verify and ≥2 F1 on ProcessBench OmniMATH for generative PRMs, plus a discriminative-to-generative distillation pipeline targeting ≥90% of MC-trained accuracy with 10× less labeling compute. Additional baselines include MCNIG-trained PRM comparison on ProcessBench per-subset and Hard2Verify, and MCNIG-RCB composition testing whether rollout-free labels benefit from domain-aware curriculum ordering. Note on ProcessBench baselines: Qwen2.5-Math-PRM-7B (66.3/67.5) is distinct from Qwen2.5-Math-7B-PRM800K (44.3/50.7) — the 22-point gap on OmniMATH demonstrates training data quality is decisive (reported in R-PRM EMNLP 2025 Table 1 and 'Is PRM Necessary?' 2505.11227 Table 1). Evaluation on three benchmarks (ProcessBench, Hard2Verify, best-of-N), both paradigms (discriminative + generative), and the four-tier deployment framework: CPMI for moderate problems (cheapest), MCNIG for moderate-to-hard problems (stronger rollout-free), AMCS-RCB discriminative PRM for frontier-hard RL training, generative PRM for high-stakes verification.\",\n  \"project_name\": \"reverse_curr_prm_bootstrap\",\n  \"source\": \"web_research\",\n  \"title\": \"Reverse-Curriculum Bootstrapping for Process Verification at the Capability Frontier\"\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d835b7f-c144-4975-9650-29e3c1dd5a09",
  "isSidechain": false,
  "requestId": "req_011CbUNwaRiNPmE52YE6CMjj",
  "type": "assistant",
  "uuid": "e7f8ffcd-2fe9-4295-ba47-50bd43fe6bc4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KA98weeaMWCGKnxWKwAke2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11475,
      "cache_read_input_tokens": 40568,
      "output_tokens": 21924,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 21924,
          "cache_read_input_tokens": 40568,
          "cache_creation_input_tokens": 11475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11475
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

_source line 62 · 2026-05-28T05:09:47.321Z_

<details><summary>↩ Tool result · reported error · `toolu_01Lp5ERw4VeN7ZDk6G11kdWo`</summary>

```text
Claude requested permissions to write to /home/ubuntu/idea-review/revised_idea_r8.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7f8ffcd-2fe9-4295-ba47-50bd43fe6bc4",
  "isSidechain": false,
  "promptId": "c5c565ce-9beb-46bc-b664-712e7c68c034",
  "type": "user",
  "uuid": "1c8a7774-26a3-4697-9dc6-53d64594f055",
  "toolUseResult": "Error: Claude requested permissions to write to /home/ubuntu/idea-review/revised_idea_r8.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "e7f8ffcd-2fe9-4295-ba47-50bd43fe6bc4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 63 · 2026-05-28T05:09:47.393Z_

```json
{
  "parentUuid": "1c8a7774-26a3-4697-9dc6-53d64594f055",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "11d36a72-d207-487b-82dd-b55cd696afd7",
  "timestamp": "2026-05-28T05:09:47.393Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"change_summary\": \"Major narrative restructuring to lead with the strongest nove…",
  "leafUuid": "11d36a72-d207-487b-82dd-b55cd696afd7",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise process reward model research based on theoretical framework feedback",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294"
}
```

---

### Assistant

_source line 66 · 2026-05-28T05:09:51.195Z_

<details><summary>Logged reasoning block</summary>

```text
The write was blocked due to permissions. Let me just output the complete JSON directly in my response to the user instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11d36a72-d207-487b-82dd-b55cd696afd7",
  "isSidechain": false,
  "requestId": "req_011CbUPavB99FBGQAy3ygWPG",
  "type": "assistant",
  "uuid": "6d26895b-5740-488c-b6e4-dfbe25c23b3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDCeBWpE2AbZNPF5t4MJiA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22074,
      "cache_read_input_tokens": 52043,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22074
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-28T05:17:05.860Z_

API Error: The socket connection was closed unexpectedly. For more information, pass `verbose: true` in the second argument to fetch()

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d26895b-5740-488c-b6e4-dfbe25c23b3a",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "a99fd155-8ae3-4316-99ca-72541a993e81",
  "requestId": "req_011CbUPavB99FBGQAy3ygWPG",
  "error": "unknown",
  "isApiErrorMessage": true,
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "id": "d78b4354-0160-4537-93df-15869a816738",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_details": null,
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---

### Runtime record

_source line 68_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"change_summary\": \"Major narrative restructuring to lead with the strongest nove…",
  "leafUuid": "a99fd155-8ae3-4316-99ca-72541a993e81",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise process reward model research based on theoretical framework feedback",
  "sessionId": "30a87c3c-1394-4ddd-886e-4fe0df585294"
}
```

---
