# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Difficulty-Adaptive Joint Generat

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/35379f54-0bee-4fcc-978e-25da424a7e94.jsonl`
- **Structured JSON:** [`f28440aa2328f2db7161.json`](../../sessions/f2/f28440aa2328f2db7161.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T06:51:04.353Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:51:04.353Z",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Difficulty-Adaptive Joint Generation-Verification Compute Allocation for LLM Reasoning\n\n## Core Problem and Motivation\n\nDifferent verification methods exhibit heterogeneous reliability profiles across problem difficulty levels: lightweight verifiers may achieve adequate TNR on easy problems, while GenRM achieves substantially higher TPR on hard problems (Variation in Verification, ICLR 2026, arXiv 2509.17995). This heterogeneity means selecting a single verification type is structurally suboptimal regardless of compute budget.\n\nThe current aggregate consensus — \"self-consistency beats GenRM under most practical budgets\" (Singhi et al., COLM 2025, arXiv 2504.01005) — masks this difficulty-heterogeneous value structure, analogous to Simpson's Paradox: the aggregate trend (SC > GenRM) may reverse in difficulty strata where GenRM's higher TPR on hard problems dominates. JOVA reveals and exploits this blind spot by enabling per-instance verification type selection conditioned on difficulty.\n\nSimultaneously, under a shared inference budget, K (candidate count) and d (verification type) are coupled through C(K,d) = K·(c_g + c_v(d)), where c_v spans ~2% (latent-ORM) to ~76× (GenRM) of c_g. We ask: how should a system jointly select (K, d) per-instance to maximize accuracy, exploiting both the reliability mismatch and the cost structure?\n\n**Structural insight: K-d interaction is maximally non-decomposable in the medium-difficulty regime.** For easy problems, optimal (K, d) ≈ (high K, low d) — both K-only and d-only optimization independently converge here. For hard problems, optimal (K, d) ≈ (low K, high d) — again independently recoverable. But for medium-difficulty problems, the iso-compute Pareto tradeoff is sharpest: switching from PRM to GenRM requires reducing K from ~16 to ~3, and whether this trade improves accuracy depends on the verifier's difficulty-specific TPR/TNR. Under a simplified analytical model where verifier d at difficulty h has TPR(d,h) and TNR(d,h), and K candidates each have correctness probability p(h), the expected BoN accuracy is a function of K, d, and h. When p(h) is extreme (easy/hard), optimal (K,d) is insensitive to boundary perturbations; when p(h) is moderate, small TPR/TNR shifts cause discontinuous jumps in optimal (K,d). This composition gap — the accuracy loss from independently optimizing K and d vs. jointly — is predicted to peak in the medium-difficulty regime. The experiments will quantify this.\n\n**Practical relevance.** When serving infrastructure deploys multiple verifiers (latent-ORM near-free, disc-ORM moderate cost, GenRM expensive), JOVA provides a principled routing policy to maximize accuracy within a fixed serving budget — answering the deployment question \"given these verifiers, how do I use them optimally per query?\"\n\n## Research Landscape\n\n**Generation-verification tradeoff foundations.** Singhi et al. (COLM 2025, arXiv 2504.01005) established aggregate scaling laws showing SC beats GenRM under most practical budgets, but this is difficulty-averaged. Rethinking Reward Models (arXiv 2510.00492) characterizes verifier effectiveness across domains with uniform strategies. Trust but Verify (arXiv 2508.16665) provides a verification taxonomy (discriminative/generative, process/outcome, prompt-based/fine-tuned).\n\n**Adaptive K (fixed verifier).** Strategic Scaling bandit (Zuo et al., arXiv 2506.12721) achieves up to 11.10% improvement on MATH-500 via UCB-adaptive K, but assumes a fixed reward oracle and ignores verification cost. AdaBoN (arXiv 2505.12050) adapts K for alignment, not verification selection.\n\n**Adaptive verification (fixed K or type).** VG-Search (Chen et al., arXiv 2505.11730) introduces a continuous granularity parameter unifying beam search and BoN with 52% FLOPs reduction but does not select between verification types. FlexiVe/SDV (arXiv 2505.11966) introduces fast/slow binary verification gated by consensus via GRPO, limited to binary hierarchy. Budget-aware Verification (Montgomery et al., arXiv 2510.14913) demonstrates hybrid discriminative+generative verification surpasses pure generative by up to 15.3% on AIME25 under fixed compute, but applies uniform per-dataset strategy. GenPRM (arXiv 2504.00891, AAAI 2026) trains generative PRMs with CoT reasoning + code verification; 1.5B GenPRM surpasses GPT-4o in BoN selection, 7B surpasses Qwen2.5-Math-PRM-72B — establishing the current verification SOTA but using a single fixed verifier type. \"Putting the Value Back in RL\" (arXiv 2505.04842) jointly trains reasoner and verifier with dynamic compute via confidence thresholds — a unified-model alternative to JOVA's modular approach.\n\n**Heterogeneous verifier combination.** Multi-Agent Verification (MAV, arXiv 2502.20379) scales test-time compute by combining multiple heterogeneous Aspect Verifiers via voting (BoN-MAV). MAV **combines** all available verifiers simultaneously (ensemble); JOVA **routes** to a single optimal verifier per instance (selection). MAV does not consider per-instance difficulty conditioning or compute budget constraints — under budget constraints, running all verifiers is infeasible, making difficulty-conditioned routing the appropriate strategy.\n\n**Adaptive reasoning length (orthogonal axis).** DiffAdapt (ICLR 2026) adapts reasoning length per instance. CODA (arXiv 2603.08659) formalizes difficulty-aware allocation as utility maximization over reasoning length. CPO (arXiv 2604.14853) uses constrained optimization with Lagrangian dual for reasoning strategy selection (12.8% relative improvement). LATTS (arXiv 2509.20368) performs step-level adaptive scaling via verifier acceptance criteria.\n\n**Adaptive routing (model-level).** ODAR (arXiv 2602.23681) uses active-inference-based difficulty estimation to route between fast/slow agents (82% cost savings), routing between models rather than verification types.\n\n**Multi-dimensional budget allocation.** AVA (Anytime Verified Agents, OpenReview 2026) dynamically allocates compute across search, sampling, and verification using calibrated uncertainty and selective verification cascades with early exits. JOVA differs in three dimensions: (1) Signal — difficulty (intrinsic problem property via DTR) vs. uncertainty (model-problem interaction); (2) Space — discrete (K, d) menu with bilinear cost vs. continuous search/sampling/verification allocation; (3) Mechanism — cross-type switching (latent-ORM → GenRM with distinct TPR/TNR) vs. early exit within a single verification pipeline.\n\n**Difficulty signals and lightweight verifiers.** DTR (arXiv 2602.13517) provides a difficulty signal with r=0.828 average accuracy correlation (validated on GPT-OSS-120B, DeepSeek-R1-70B, Qwen3-30B-Thinking across AIME 24/25, HMMT 25, GPQA-diamond; not yet validated on distilled ≤14B models). LiLaVe (arXiv 2504.16760) enables near-free hidden-state-based verification. TrajSelector (arXiv 2510.16449) uses hidden states for process-level scoring via a 0.6B verifier, exceeding majority voting by 4.61%.\n\n**Gap.** All existing work optimizes a single variable (K, granularity, binary type, reasoning length, or model routing), or combines all verifiers without selection (MAV). AVA allocates multi-dimensionally but uses uncertainty-driven cascades, not difficulty-driven type switching. No work jointly optimizes (K, d) over a verifier type hierarchy under a shared budget with a continuous difficulty signal, nor reveals the difficulty-dependent composition gap structure.\n\n## Proposed Approach: JOVA\n\n**Formulation.** Per-instance allocation over a discrete (K, d) menu under C(K,d) = K·(c_g + c_v(d)) ≤ B.\n\n**Verifier type hierarchy.** We treat the four-tier ordering (latent-ORM < disc-ORM < PRM < GenRM in cost and expected precision) as an empirical hypothesis to be validated in Phase 0, not an assumption. If the actual reliability structure is non-monotonic (e.g., PRM outperforms GenRM on certain problem types), the (K, d) menu is reorganized accordingly.\n\n**Difficulty routing.** DTR-based router estimates difficulty from short prefix hidden states. Honest limitation: DTR primarily captures reasoning effort intensity; domain-specific factors (algebraic vs. geometric vs. combinatorial) and generator confidence may additionally influence optimal verification type. DTR provides a strong but not exhaustive routing signal; multi-signal routing is a natural future extension.\n\n**Fallback difficulty signals.** DTR has been validated only on ≥30B models. For ≤14B distilled models, we include fallbacks: (a) generator logit entropy (zero-overhead, extracted during generation), (b) two-stage SC agreement rate (fixed K_0=4 pilot samples to estimate difficulty, then allocate remaining budget B − K_0·c_g adaptively; cost model explicitly includes pilot overhead: C_total = K_0·c_g + K·(c_g + c_v(d))). Phase 0 selects the best signal for the target model scale.\n\n**Online refinement.** UCB bandit refines (K, d) via correctness feedback. Protocol: bandit pre-trained on held-out validation split, then frozen for test evaluation. For small benchmarks (AIME25), transfer policy learned on MATH-500 validation split.\n\n**Why learned routing exceeds static lookup.** Grid-Search-(K,d)-per-bucket (exhaustive search per difficulty tercile on validation data) is a strong trivial alternative. JOVA's advantages: (a) difficulty is continuous — discrete bins lose boundary information; (b) optimal (K, d) depends on domain-specific factors beyond scalar difficulty; (c) UCB adapts to distribution shift across benchmarks.\n\n## Experimental Design\n\n**Phase 0 (pilot, ~50 A100-hours).** (a) DTR correlation on DeepSeek-R1-Distill-14B and Qwen3-8B using MATH-500; compare DTR vs. SC agreement rate vs. logit entropy vs. prompt perplexity; proceed if best signal achieves r ≥ 0.6. (b) Validate verifier hierarchy: measure TPR/TNR of each verifier tier per difficulty bin; test whether ordering is monotonic. (c) Profile LiLaVe hidden state extraction overhead.\n\n**Benchmarks.** MATH-500 (primary per-difficulty analysis), AIME25 (aggregate + qualitative case study; ≥10 seeds due to n=30), GPQA-Diamond (aggregate). Optional: LiveCodeBench for cross-domain generalization.\n\n**Models.** Primary: DeepSeek-R1-Distill-Qwen-14B, Qwen3-8B. Extended: DeepSeek-R1-Distill-Qwen-32B. Supplementary: DeepSeek-R1 full (671B MoE) if resources permit.\n\n**Verifier specification:**\n\n| Tier | Implementation | Params | Approx. Cost |\n|---|---|---|---|\n| Latent-ORM | LiLaVe: XGBoost on hidden states (arXiv 2504.16760) | ~0 (reuses forward pass) | ~2% of c_g |\n| Disc-ORM | InternLM2-7B-Reward (or comparable open-source outcome RM) | 7B | ~50% of c_g |\n| PRM | Skywork-o1-Open-PRM-Qwen-2.5-7B, step-level scoring (note: robustness limitations per arXiv 2603.06621; Phase 0 validates on target generations) | 7B | ~60% of c_g |\n| GenRM | Generator self-verification via CoT | same as generator | ~76× of c_g |\n\nDisc-ORM and PRM intentionally use different model families to ensure the hierarchy captures genuine type diversity rather than scoring-granularity-within-one-model artifacts. FLOPs cost table calibrated per model-verifier pair; distinguishes prefill vs decode.\n\n**Baselines (compute-matched via FLOPs as primary metric; wall-clock as supplementary):**\n1. Static Best-of-N with each single verifier type (4 configs)\n2. Self-Consistency (majority voting)\n3. Strategic Scaling bandit (Zuo et al., arXiv 2506.12721) — adaptive K + fixed best verifier\n4. VG-Search (Chen et al., arXiv 2505.11730) — adaptive granularity, uniform type\n5. FlexiVe/SDV (arXiv 2505.11966) — fast/slow binary verification\n6. Grid-Search-(K,d)-per-bucket — static lookup per difficulty tercile\n7. Montgomery et al. hybrid disc+gen verification (arXiv 2510.14913) — uniform per-dataset\n8. GenPRM-7B BoN (arXiv 2504.00891, AAAI 2026) — fixed GenPRM verifier + best K\n\n**Ablations:**\n\n| Configuration | K | d | Router | Purpose |\n|---|---|---|---|---|\n| JOVA-full | adaptive | adaptive | DTR+UCB | Complete system |\n| Fix-d-best | adaptive | fixed best d | DTR+UCB | Isolate d-selection gain |\n| Fix-K-best | fixed best K | adaptive | DTR+UCB | Isolate K-selection gain |\n| DTR-only | DTR preset | DTR preset | DTR only | Isolate UCB refinement gain |\n| UCB-only | UCB learned | UCB learned | UCB only | Isolate DTR initialization gain |\n| Oracle-router | adaptive | adaptive | Oracle | Performance upper bound |\n\nAdditional analyses: (a) difficulty signal comparison (DTR vs SC-agreement vs logit entropy vs perplexity); (b) tier dropout: 2-tier (Latent-ORM + GenRM only) vs 3-tier (drop Disc-ORM or PRM) vs 4-tier (full) — quantifies marginal contribution of intermediate tiers; (c) binning sensitivity (2/3/5-bin vs continuous mapping); (d) router robustness (10%/20%/30% simulated routing error); (e) per-difficulty-bin (K,d) allocation distribution (MATH-500 only); (f) composition gap measurement: compare JOVA-full accuracy vs max(Fix-d-best, Fix-K-best), stratified by difficulty, to directly quantify the joint optimization benefit per regime.\n\n**Evaluation protocol:**\n- 8 budget levels at log-spacing: 1×, 2×, 4×, 8×, 16×, 32×, 64×, 128× of pass@1 cost\n- Accuracy-vs-FLOPs Pareto curves (primary) + accuracy-vs-wall-clock (supplementary, measured on single A100-80G, batch size 1)\n- Bootstrap 95% CI; ≥5 seeds (MATH-500, GPQA), ≥10 seeds (AIME25)\n- Gains reported in two tiers: (a) vs static BoN, (b) vs best adaptive-K-only baseline\n\n**Compute estimate (~350-550 A100-hours total):**\n- Phase 0 (pilot): ~50 hours\n- Phase 1 (core): MATH-500 + 14B + main ablations + Grid-Search baseline (~120 hours)\n- Phase 2 (extension): AIME25 + GPQA + Qwen3-8B + all baselines (~180 hours)\n- Phase 3 (analysis): difficulty breakdown, tier dropout, router robustness, Pareto curves, binning sensitivity, 32B model (~100 hours)\n\nPrimary target: AAAI 2027 (Jul 28).\n\n## Key References\n\n- When To Solve, When To Verify (Singhi et al., COLM 2025, arXiv 2504.01005)\n- Strategic Scaling of Test-Time Compute: A Bandit Approach (Zuo et al., arXiv 2506.12721)\n- VG-Search: Rethinking Optimal Verification Granularity (Chen et al., arXiv 2505.11730)\n- FlexiVe/SDV: Flexible Generative Verifier (arXiv 2505.11966)\n- Variation in Verification (ICLR 2026, arXiv 2509.17995)\n- Think Deep, Not Just Long: DTR via Deep-Thinking Tokens (arXiv 2602.13517)\n- Lightweight Latent Verifiers for Meta-Generation: LiLaVe (arXiv 2504.16760)\n- TrajSelector: Latent Representations for Best-of-N (arXiv 2510.16449)\n- Rethinking Reward Models for Multi-Domain Scaling (arXiv 2510.00492)\n- Budget-aware Test-time Scaling via Discriminative Verification (Montgomery et al., arXiv 2510.14913)\n- DiffAdapt: Difficulty-Adaptive Reasoning (ICLR 2026)\n- CODA: Difficulty-Aware Compute Allocation (arXiv 2603.08659)\n- ODAR: Principled Adaptive Routing via Active Inference (arXiv 2602.23681)\n- Adaptive TTC via Constrained Policy Optimization (arXiv 2604.14853)\n- LATTS: Locally Adaptive Test-Time Scaling (arXiv 2509.20368)\n- AdaBoN: Adaptive Best-of-N (arXiv 2505.12050)\n- AVA: Anytime Verified Agents (OpenReview 2026)\n- Putting the Value Back in RL: Unifying Reasoners With Verifiers (arXiv 2505.04842)\n- Trust but Verify! Survey on Verification Design (arXiv 2508.16665)\n- Multi-Agent Verification: BoN-MAV (arXiv 2502.20379)\n- GenPRM: Generative Process Reward Model (arXiv 2504.00891, AAAI 2026)\n- Reward Under Attack: PRM Robustness (arXiv 2603.06621)"
}
```

---

### Runtime record

_source line 2 · 2026-05-29T06:51:04.359Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:51:04.359Z",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94"
}
```

---

## Round 1

38 recorded events

### User

_source line 3 · 2026-05-29T06:51:04.386Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Difficulty-Adaptive Joint Generation-Verification Compute Allocation for LLM Reasoning

## Core Problem and Motivation

Different verification methods exhibit heterogeneous reliability profiles across problem difficulty levels: lightweight verifiers may achieve adequate TNR on easy problems, while GenRM achieves substantially higher TPR on hard problems (Variation in Verification, ICLR 2026, arXiv 2509.17995). This heterogeneity means selecting a single verification type is structurally suboptimal regardless of compute budget.

The current aggregate consensus — "self-consistency beats GenRM under most practical budgets" (Singhi et al., COLM 2025, arXiv 2504.01005) — masks this difficulty-heterogeneous value structure, analogous to Simpson's Paradox: the aggregate trend (SC > GenRM) may reverse in difficulty strata where GenRM's higher TPR on hard problems dominates. JOVA reveals and exploits this blind spot by enabling per-instance verification type selection conditioned on difficulty.

Simultaneously, under a shared inference budget, K (candidate count) and d (verification type) are coupled through C(K,d) = K·(c_g + c_v(d)), where c_v spans ~2% (latent-ORM) to ~76× (GenRM) of c_g. We ask: how should a system jointly select (K, d) per-instance to maximize accuracy, exploiting both the reliability mismatch and the cost structure?

**Structural insight: K-d interaction is maximally non-decomposable in the medium-difficulty regime.** For easy problems, optimal (K, d) ≈ (high K, low d) — both K-only and d-only optimization independently converge here. For hard problems, optimal (K, d) ≈ (low K, high d) — again independently recoverable. But for medium-difficulty problems, the iso-compute Pareto tradeoff is sharpest: switching from PRM to GenRM requires reducing K from ~16 to ~3, and whether this trade improves accuracy depends on the verifier's difficulty-specific TPR/TNR. Under a simplified analytical model where verifier d at difficulty h has TPR(d,h) and TNR(d,h), and K candidates each have correctness probability p(h), the expected BoN accuracy is a function of K, d, and h. When p(h) is extreme (easy/hard), optimal (K,d) is insensitive to boundary perturbations; when p(h) is moderate, small TPR/TNR shifts cause discontinuous jumps in optimal (K,d). This composition gap — the accuracy loss from independently optimizing K and d vs. jointly — is predicted to peak in the medium-difficulty regime. The experiments will quantify this.

**Practical relevance.** When serving infrastructure deploys multiple verifiers (latent-ORM near-free, disc-ORM moderate cost, GenRM expensive), JOVA provides a principled routing policy to maximize accuracy within a fixed serving budget — answering the deployment question "given these verifiers, how do I use them optimally per query?"

## Research Landscape

**Generation-verification tradeoff foundations.** Singhi et al. (COLM 2025, arXiv 2504.01005) established aggregate scaling laws showing SC beats GenRM under most practical budgets, but this is difficulty-averaged. Rethinking Reward Models (arXiv 2510.00492) characterizes verifier effectiveness across domains with uniform strategies. Trust but Verify (arXiv 2508.16665) provides a verification taxonomy (discriminative/generative, process/outcome, prompt-based/fine-tuned).

**Adaptive K (fixed verifier).** Strategic Scaling bandit (Zuo et al., arXiv 2506.12721) achieves up to 11.10% improvement on MATH-500 via UCB-adaptive K, but assumes a fixed reward oracle and ignores verification cost. AdaBoN (arXiv 2505.12050) adapts K for alignment, not verification selection.

**Adaptive verification (fixed K or type).** VG-Search (Chen et al., arXiv 2505.11730) introduces a continuous granularity parameter unifying beam search and BoN with 52% FLOPs reduction but does not select between verification types. FlexiVe/SDV (arXiv 2505.11966) introduces fast/slow binary verification gated by consensus via GRPO, limited to binary hierarchy. Budget-aware Verification (Montgomery et al., arXiv 2510.14913) demonstrates hybrid discriminative+generative verification surpasses pure generative by up to 15.3% on AIME25 under fixed compute, but applies uniform per-dataset strategy. GenPRM (arXiv 2504.00891, AAAI 2026) trains generative PRMs with CoT reasoning + code verification; 1.5B GenPRM surpasses GPT-4o in BoN selection, 7B surpasses Qwen2.5-Math-PRM-72B — establishing the current verification SOTA but using a single fixed verifier type. "Putting the Value Back in RL" (arXiv 2505.04842) jointly trains reasoner and verifier with dynamic compute via confidence thresholds — a unified-model alternative to JOVA's modular approach.

**Heterogeneous verifier combination.** Multi-Agent Verification (MAV, arXiv 2502.20379) scales test-time compute by combining multiple heterogeneous Aspect Verifiers via voting (BoN-MAV). MAV **combines** all available verifiers simultaneously (ensemble); JOVA **routes** to a single optimal verifier per instance (selection). MAV does not consider per-instance difficulty conditioning or compute budget constraints — under budget constraints, running all verifiers is infeasible, making difficulty-conditioned routing the appropriate strategy.

**Adaptive reasoning length (orthogonal axis).** DiffAdapt (ICLR 2026) adapts reasoning length per instance. CODA (arXiv 2603.08659) formalizes difficulty-aware allocation as utility maximization over reasoning length. CPO (arXiv 2604.14853) uses constrained optimization with Lagrangian dual for reasoning strategy selection (12.8% relative improvement). LATTS (arXiv 2509.20368) performs step-level adaptive scaling via verifier acceptance criteria.

**Adaptive routing (model-level).** ODAR (arXiv 2602.23681) uses active-inference-based difficulty estimation to route between fast/slow agents (82% cost savings), routing between models rather than verification types.

**Multi-dimensional budget allocation.** AVA (Anytime Verified Agents, OpenReview 2026) dynamically allocates compute across search, sampling, and verification using calibrated uncertainty and selective verification cascades with early exits. JOVA differs in three dimensions: (1) Signal — difficulty (intrinsic problem property via DTR) vs. uncertainty (model-problem interaction); (2) Space — discrete (K, d) menu with bilinear cost vs. continuous search/sampling/verification allocation; (3) Mechanism — cross-type switching (latent-ORM → GenRM with distinct TPR/TNR) vs. early exit within a single verification pipeline.

**Difficulty signals and lightweight verifiers.** DTR (arXiv 2602.13517) provides a difficulty signal with r=0.828 average accuracy correlation (validated on GPT-OSS-120B, DeepSeek-R1-70B, Qwen3-30B-Thinking across AIME 24/25, HMMT 25, GPQA-diamond; not yet validated on distilled ≤14B models). LiLaVe (arXiv 2504.16760) enables near-free hidden-state-based verification. TrajSelector (arXiv 2510.16449) uses hidden states for process-level scoring via a 0.6B verifier, exceeding majority voting by 4.61%.

**Gap.** All existing work optimizes a single variable (K, granularity, binary type, reasoning length, or model routing), or combines all verifiers without selection (MAV). AVA allocates multi-dimensionally but uses uncertainty-driven cascades, not difficulty-driven type switching. No work jointly optimizes (K, d) over a verifier type hierarchy under a shared budget with a continuous difficulty signal, nor reveals the difficulty-dependent composition gap structure.

## Proposed Approach: JOVA

**Formulation.** Per-instance allocation over a discrete (K, d) menu under C(K,d) = K·(c_g + c_v(d)) ≤ B.

**Verifier type hierarchy.** We treat the four-tier ordering (latent-ORM < disc-ORM < PRM < GenRM in cost and expected precision) as an empirical hypothesis to be validated in Phase 0, not an assumption. If the actual reliability structure is non-monotonic (e.g., PRM outperforms GenRM on certain problem types), the (K, d) menu is reorganized accordingly.

**Difficulty routing.** DTR-based router estimates difficulty from short prefix hidden states. Honest limitation: DTR primarily captures reasoning effort intensity; domain-specific factors (algebraic vs. geometric vs. combinatorial) and generator confidence may additionally influence optimal verification type. DTR provides a strong but not exhaustive routing signal; multi-signal routing is a natural future extension.

**Fallback difficulty signals.** DTR has been validated only on ≥30B models. For ≤14B distilled models, we include fallbacks: (a) generator logit entropy (zero-overhead, extracted during generation), (b) two-stage SC agreement rate (fixed K_0=4 pilot samples to estimate difficulty, then allocate remaining budget B − K_0·c_g adaptively; cost model explicitly includes pilot overhead: C_total = K_0·c_g + K·(c_g + c_v(d))). Phase 0 selects the best signal for the target model scale.

**Online refinement.** UCB bandit refines (K, d) via correctness feedback. Protocol: bandit pre-trained on held-out validation split, then frozen for test evaluation. For small benchmarks (AIME25), transfer policy learned on MATH-500 validation split.

**Why learned routing exceeds static lookup.** Grid-Search-(K,d)-per-bucket (exhaustive search per difficulty tercile on validation data) is a strong trivial alternative. JOVA's advantages: (a) difficulty is continuous — discrete bins lose boundary information; (b) optimal (K, d) depends on domain-specific factors beyond scalar difficulty; (c) UCB adapts to distribution shift across benchmarks.

## Experimental Design

**Phase 0 (pilot, ~50 A100-hours).** (a) DTR correlation on DeepSeek-R1-Distill-14B and Qwen3-8B using MATH-500; compare DTR vs. SC agreement rate vs. logit entropy vs. prompt perplexity; proceed if best signal achieves r ≥ 0.6. (b) Validate verifier hierarchy: measure TPR/TNR of each verifier tier per difficulty bin; test whether ordering is monotonic. (c) Profile LiLaVe hidden state extraction overhead.

**Benchmarks.** MATH-500 (primary per-difficulty analysis), AIME25 (aggregate + qualitative case study; ≥10 seeds due to n=30), GPQA-Diamond (aggregate). Optional: LiveCodeBench for cross-domain generalization.

**Models.** Primary: DeepSeek-R1-Distill-Qwen-14B, Qwen3-8B. Extended: DeepSeek-R1-Distill-Qwen-32B. Supplementary: DeepSeek-R1 full (671B MoE) if resources permit.

**Verifier specification:**

| Tier | Implementation | Params | Approx. Cost |
|---|---|---|---|
| Latent-ORM | LiLaVe: XGBoost on hidden states (arXiv 2504.16760) | ~0 (reuses forward pass) | ~2% of c_g |
| Disc-ORM | InternLM2-7B-Reward (or comparable open-source outcome RM) | 7B | ~50% of c_g |
| PRM | Skywork-o1-Open-PRM-Qwen-2.5-7B, step-level scoring (note: robustness limitations per arXiv 2603.06621; Phase 0 validates on target generations) | 7B | ~60% of c_g |
| GenRM | Generator self-verification via CoT | same as generator | ~76× of c_g |

Disc-ORM and PRM intentionally use different model families to ensure the hierarchy captures genuine type diversity rather than scoring-granularity-within-one-model artifacts. FLOPs cost table calibrated per model-verifier pair; distinguishes prefill vs decode.

**Baselines (compute-matched via FLOPs as primary metric; wall-clock as supplementary):**
1. Static Best-of-N with each single verifier type (4 configs)
2. Self-Consistency (majority voting)
3. Strategic Scaling bandit (Zuo et al., arXiv 2506.12721) — adaptive K + fixed best verifier
4. VG-Search (Chen et al., arXiv 2505.11730) — adaptive granularity, uniform type
5. FlexiVe/SDV (arXiv 2505.11966) — fast/slow binary verification
6. Grid-Search-(K,d)-per-bucket — static lookup per difficulty tercile
7. Montgomery et al. hybrid disc+gen verification (arXiv 2510.14913) — uniform per-dataset
8. GenPRM-7B BoN (arXiv 2504.00891, AAAI 2026) — fixed GenPRM verifier + best K

**Ablations:**

| Configuration | K | d | Router | Purpose |
|---|---|---|---|---|
| JOVA-full | adaptive | adaptive | DTR+UCB | Complete system |
| Fix-d-best | adaptive | fixed best d | DTR+UCB | Isolate d-selection gain |
| Fix-K-best | fixed best K | adaptive | DTR+UCB | Isolate K-selection gain |
| DTR-only | DTR preset | DTR preset | DTR only | Isolate UCB refinement gain |
| UCB-only | UCB learned | UCB learned | UCB only | Isolate DTR initialization gain |
| Oracle-router | adaptive | adaptive | Oracle | Performance upper bound |

Additional analyses: (a) difficulty signal comparison (DTR vs SC-agreement vs logit entropy vs perplexity); (b) tier dropout: 2-tier (Latent-ORM + GenRM only) vs 3-tier (drop Disc-ORM or PRM) vs 4-tier (full) — quantifies marginal contribution of intermediate tiers; (c) binning sensitivity (2/3/5-bin vs continuous mapping); (d) router robustness (10%/20%/30% simulated routing error); (e) per-difficulty-bin (K,d) allocation distribution (MATH-500 only); (f) composition gap measurement: compare JOVA-full accuracy vs max(Fix-d-best, Fix-K-best), stratified by difficulty, to directly quantify the joint optimization benefit per regime.

**Evaluation protocol:**
- 8 budget levels at log-spacing: 1×, 2×, 4×, 8×, 16×, 32×, 64×, 128× of pass@1 cost
- Accuracy-vs-FLOPs Pareto curves (primary) + accuracy-vs-wall-clock (supplementary, measured on single A100-80G, batch size 1)
- Bootstrap 95% CI; ≥5 seeds (MATH-500, GPQA), ≥10 seeds (AIME25)
- Gains reported in two tiers: (a) vs static BoN, (b) vs best adaptive-K-only baseline

**Compute estimate (~350-550 A100-hours total):**
- Phase 0 (pilot): ~50 hours
- Phase 1 (core): MATH-500 + 14B + main ablations + Grid-Search baseline (~120 hours)
- Phase 2 (extension): AIME25 + GPQA + Qwen3-8B + all baselines (~180 hours)
- Phase 3 (analysis): difficulty breakdown, tier dropout, router robustness, Pareto curves, binning sensitivity, 32B model (~100 hours)

Primary target: AAAI 2027 (Jul 28).

## Key References

- When To Solve, When To Verify (Singhi et al., COLM 2025, arXiv 2504.01005)
- Strategic Scaling of Test-Time Compute: A Bandit Approach (Zuo et al., arXiv 2506.12721)
- VG-Search: Rethinking Optimal Verification Granularity (Chen et al., arXiv 2505.11730)
- FlexiVe/SDV: Flexible Generative Verifier (arXiv 2505.11966)
- Variation in Verification (ICLR 2026, arXiv 2509.17995)
- Think Deep, Not Just Long: DTR via Deep-Thinking Tokens (arXiv 2602.13517)
- Lightweight Latent Verifiers for Meta-Generation: LiLaVe (arXiv 2504.16760)
- TrajSelector: Latent Representations for Best-of-N (arXiv 2510.16449)
- Rethinking Reward Models for Multi-Domain Scaling (arXiv 2510.00492)
- Budget-aware Test-time Scaling via Discriminative Verification (Montgomery et al., arXiv 2510.14913)
- DiffAdapt: Difficulty-Adaptive Reasoning (ICLR 2026)
- CODA: Difficulty-Aware Compute Allocation (arXiv 2603.08659)
- ODAR: Principled Adaptive Routing via Active Inference (arXiv 2602.23681)
- Adaptive TTC via Constrained Policy Optimization (arXiv 2604.14853)
- LATTS: Locally Adaptive Test-Time Scaling (arXiv 2509.20368)
- AdaBoN: Adaptive Best-of-N (arXiv 2505.12050)
- AVA: Anytime Verified Agents (OpenReview 2026)
- Putting the Value Back in RL: Unifying Reasoners With Verifiers (arXiv 2505.04842)
- Trust but Verify! Survey on Verification Design (arXiv 2508.16665)
- Multi-Agent Verification: BoN-MAV (arXiv 2502.20379)
- GenPRM: Generative Process Reward Model (arXiv 2504.00891, AAAI 2026)
- Reward Under Attack: PRM Robustness (arXiv 2603.06621)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "7418c215-ebe6-4e47-98f1-b1f363ffe1e7",
  "type": "user",
  "uuid": "4e66c2a6-22dd-40db-a014-9c998c357f53",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T06:51:04.384Z_

```json
{
  "parentUuid": "4e66c2a6-22dd-40db-a014-9c998c357f53",
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
  "uuid": "a06058e5-0637-40fc-8c3d-57d5a7dfcb69",
  "timestamp": "2026-05-29T06:51:04.384Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T06:51:04.384Z_

```json
{
  "parentUuid": "a06058e5-0637-40fc-8c3d-57d5a7dfcb69",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "09ad9ac6-8b95-4ade-b558-03437e598abd",
  "timestamp": "2026-05-29T06:51:04.384Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Difficulty-Adaptive Joint Generation-Verification Compute Allocation for LLM Reasoning  ## Core Problem and Moti…",
  "leafUuid": "09ad9ac6-8b95-4ade-b558-03437e598abd",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate difficulty-adaptive verification type selection proposal",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94"
}
```

---

### Assistant

_source line 8 · 2026-05-29T06:51:09.891Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for AAAI 2026 (though the proposal itself says "AAAI 2027" as its target). Let me first do thorough web searches to understand the current landscape, then provide my evaluation.

Let me search for the key topics:
1. Test-time compute scaling, generation-verification tradeoffs
2. Adaptive verification for LLM reasoning
3. Difficulty-adaptive compute allocation
4. Joint optimization of generation and verification

Let me start the web searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09ad9ac6-8b95-4ade-b558-03437e598abd",
  "isSidechain": false,
  "requestId": "req_011CbWR7oS4tBQweCPz2Agrw",
  "type": "assistant",
  "uuid": "ab65a319-de7b-4cf3-9f3d-52a659763482",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EfLBwH8Yv6pWuyQqthsBaA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8518,
      "cache_read_input_tokens": 11014,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8518,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 241,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8518,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8518
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

_source line 9 · 2026-05-29T06:51:10.643Z_

I'll start by conducting thorough web searches to understand the current research landscape before making any judgments. Let me search for the key topics in this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab65a319-de7b-4cf3-9f3d-52a659763482",
  "isSidechain": false,
  "requestId": "req_011CbWR7oS4tBQweCPz2Agrw",
  "type": "assistant",
  "uuid": "2e243a00-d1cd-41d9-98b2-e64ed683411f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EfLBwH8Yv6pWuyQqthsBaA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8518,
      "cache_read_input_tokens": 11014,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8518,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 241,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8518,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8518
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

_source line 10 · 2026-05-29T06:51:14.292Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FGLppMuP4vkZHdYyWvnE3R`</summary>

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
  "parentUuid": "2e243a00-d1cd-41d9-98b2-e64ed683411f",
  "isSidechain": false,
  "requestId": "req_011CbWR7oS4tBQweCPz2Agrw",
  "type": "assistant",
  "uuid": "5a61fe26-0f2e-4ac5-a1cd-b86c0b7417ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EfLBwH8Yv6pWuyQqthsBaA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8518,
      "cache_read_input_tokens": 11014,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8518,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 241,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8518,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8518
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

_source line 11 · 2026-05-29T06:51:14.300Z_

<details><summary>↩ Tool result · `toolu_01FGLppMuP4vkZHdYyWvnE3R`</summary>

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
  "parentUuid": "5a61fe26-0f2e-4ac5-a1cd-b86c0b7417ae",
  "isSidechain": false,
  "promptId": "7418c215-ebe6-4e47-98f1-b1f363ffe1e7",
  "type": "user",
  "uuid": "4947d546-47bd-4d40-a9ae-9835360a4fec",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "5a61fe26-0f2e-4ac5-a1cd-b86c0b7417ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-29T06:51:20.545Z_

Now let me conduct multiple targeted searches to understand the research landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4947d546-47bd-4d40-a9ae-9835360a4fec",
  "isSidechain": false,
  "requestId": "req_011CbWR8XpzAiGZ9mrCDPies",
  "type": "assistant",
  "uuid": "7e72111d-327c-4652-8bad-97125a82a857",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cb4KKmd9BGoz3VoYFYTbeA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 19532,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 189,
          "cache_read_input_tokens": 19532,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 769
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

_source line 13 · 2026-05-29T06:51:21.031Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U1FuGMDK4gky7qsg15i7LN`</summary>

```json
{
  "query": "adaptive test-time compute allocation LLM reasoning verification 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e72111d-327c-4652-8bad-97125a82a857",
  "isSidechain": false,
  "requestId": "req_011CbWR8XpzAiGZ9mrCDPies",
  "type": "assistant",
  "uuid": "6730556e-7cac-43fc-8aed-ac3ff344ccec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cb4KKmd9BGoz3VoYFYTbeA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 19532,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 189,
          "cache_read_input_tokens": 19532,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 769
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

_source line 14 · 2026-05-29T06:51:21.461Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HWekqLCSpke5uQD3E1AdGx`</summary>

```json
{
  "query": "difficulty-adaptive verification LLM reasoning best-of-N scaling 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6730556e-7cac-43fc-8aed-ac3ff344ccec",
  "isSidechain": false,
  "requestId": "req_011CbWR8XpzAiGZ9mrCDPies",
  "type": "assistant",
  "uuid": "e55e6bb9-12c9-4f64-ba5a-4ce8627742a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cb4KKmd9BGoz3VoYFYTbeA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 19532,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 189,
          "cache_read_input_tokens": 19532,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 769
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

_source line 15 · 2026-05-29T06:51:21.874Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PFi1QRMeQEy8Mw1M9rgFnC`</summary>

```json
{
  "query": "GenRM discriminative generative reward model joint optimization compute budget 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e55e6bb9-12c9-4f64-ba5a-4ce8627742a1",
  "isSidechain": false,
  "requestId": "req_011CbWR8XpzAiGZ9mrCDPies",
  "type": "assistant",
  "uuid": "06688451-c0d8-41ed-ba4b-9eac4677d520",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cb4KKmd9BGoz3VoYFYTbeA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 19532,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 189,
          "cache_read_input_tokens": 19532,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 769
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

_source line 16 · 2026-05-29T06:51:28.661Z_

<details><summary>↩ Tool result · `toolu_01HWekqLCSpke5uQD3E1AdGx`</summary>

```text
Web search results for query: "difficulty-adaptive verification LLM reasoning best-of-N scaling 2025 2026"

Links: [{"title":"Improving LLM Reasoning through Scaling Inference Computation with   Collaborative Verification","url":"https://arxiv.org/pdf/2410.05318"},{"title":"Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs","url":"https://arxiv.org/pdf/2506.12509"},{"title":"How Difficulty-Aware Staged Reinforcement Learning Enhances LLMs'   Reasoning Capabilities: A Preliminary Experimental Study","url":"https://arxiv.org/pdf/2504.00829"},{"title":"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable Language Model Reasoning","url":"https://arxiv.org/pdf/2408.13940"},{"title":"Generative Verifiers: Reward Modeling as Next-Token Prediction","url":"https://arxiv.org/pdf/2408.15240"},{"title":"DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference","url":"https://arxiv.org/pdf/2510.19669"},{"title":"Multi-Agent Verification: Scaling Test-Time Compute with Multiple   Verifiers","url":"https://arxiv.org/pdf/2502.20379"},{"title":"Putting the Value Back in RL: Better Test-Time Scaling by Unifying LLM Reasoners With Verifiers","url":"https://arxiv.org/html/2505.04842v2"}]

I found several relevant research papers on your search topic. Here's a summary of the results:

**Key Papers Found:**

1. **DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference** - This work introduces a framework that designs different inference strategies for three distinct difficulty regions, each equipped with different generation length and decoding hyperparameters. DiffAdapt achieves superior performance with up to 62% token reduction and 18% performance improvement.

2. **Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers** - This paper explores best-of-N sampling where n candidate outputs are sampled from a generator LLM and a verifier model scores each candidate, with the highest-scoring output selected. It proposes scaling the number of verifiers, introducing Multi-Agent Verification (MAV), a test-time compute paradigm that combines multiple verifiers.

3. **Putting the Value Back in RL: Better Test-Time Scaling by Unifying LLM Reasoners With Verifiers** - This work proposes training a generative verifier concurrently with the policy, leveraging data generated during RL training.

4. **Derailer-Rerailer: Adaptive Verification for Efficient and Reliable Language Model Reasoning** - This approach balances efficiency and reasoning depth based on problem complexity.

These papers represent recent research addressing difficulty-adaptive verification and best-of-N scaling for LLM reasoning in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e55e6bb9-12c9-4f64-ba5a-4ce8627742a1",
  "isSidechain": false,
  "promptId": "7418c215-ebe6-4e47-98f1-b1f363ffe1e7",
  "type": "user",
  "uuid": "9ff10d5c-b1e0-486d-9db5-66a8a27df1a4",
  "toolUseResult": {
    "query": "difficulty-adaptive verification LLM reasoning best-of-N scaling 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01J8jrmSkavMniFVZWwLU3s3",
        "content": [
          {
            "title": "Improving LLM Reasoning through Scaling Inference Computation with   Collaborative Verification",
            "url": "https://arxiv.org/pdf/2410.05318"
          },
          {
            "title": "Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs",
            "url": "https://arxiv.org/pdf/2506.12509"
          },
          {
            "title": "How Difficulty-Aware Staged Reinforcement Learning Enhances LLMs'   Reasoning Capabilities: A Preliminary Experimental Study",
            "url": "https://arxiv.org/pdf/2504.00829"
          },
          {
            "title": "Derailer-Rerailer: Adaptive Verification for Efficient and Reliable Language Model Reasoning",
            "url": "https://arxiv.org/pdf/2408.13940"
          },
          {
            "title": "Generative Verifiers: Reward Modeling as Next-Token Prediction",
            "url": "https://arxiv.org/pdf/2408.15240"
          },
          {
            "title": "DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference",
            "url": "https://arxiv.org/pdf/2510.19669"
          },
          {
            "title": "Multi-Agent Verification: Scaling Test-Time Compute with Multiple   Verifiers",
            "url": "https://arxiv.org/pdf/2502.20379"
          },
          {
            "title": "Putting the Value Back in RL: Better Test-Time Scaling by Unifying LLM Reasoners With Verifiers",
            "url": "https://arxiv.org/html/2505.04842v2"
          }
        ]
      },
      "I found several relevant research papers on your search topic. Here's a summary of the results:\n\n**Key Papers Found:**\n\n1. **DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference** - This work introduces a framework that designs different inference strategies for three distinct difficulty regions, each equipped with different generation length and decoding hyperparameters. DiffAdapt achieves superior performance with up to 62% token reduction and 18% performance improvement.\n\n2. **Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers** - This paper explores best-of-N sampling where n candidate outputs are sampled from a generator LLM and a verifier model scores each candidate, with the highest-scoring output selected. It proposes scaling the number of verifiers, introducing Multi-Agent Verification (MAV), a test-time compute paradigm that combines multiple verifiers.\n\n3. **Putting the Value Back in RL: Better Test-Time Scaling by Unifying LLM Reasoners With Verifiers** - This work proposes training a generative verifier concurrently with the policy, leveraging data generated during RL training.\n\n4. **Derailer-Rerailer: Adaptive Verification for Efficient and Reliable Language Model Reasoning** - This approach balances efficiency and reasoning depth based on problem complexity.\n\nThese papers represent recent research addressing difficulty-adaptive verification and best-of-N scaling for LLM reasoning in 2025-2026."
    ],
    "durationSeconds": 7.194913744000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e55e6bb9-12c9-4f64-ba5a-4ce8627742a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-29T06:51:29.661Z_

<details><summary>↩ Tool result · `toolu_01U1FuGMDK4gky7qsg15i7LN`</summary>

```text
Web search results for query: "adaptive test-time compute allocation LLM reasoning verification 2025 2026"

Links: [{"title":"Adaptive Test-Time Compute Allocation","url":"https://www.emergentmind.com/topics/adaptive-test-time-compute-allocation"},{"title":"What If We Allocate Test-Time Compute Adaptively?","url":"https://arxiv.org/html/2602.01070"},{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/html/2602.03975v1"},{"title":"Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization","url":"https://arxiv.org/html/2604.14853v1"},{"title":"Adaptive Test-Time Compute Allocation for Reasoning LLMs via...","url":"https://arxiv.org/abs/2604.14853"},{"title":"[2602.03975] Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/abs/2602.03975"}]

I found several highly relevant research papers and resources on adaptive test-time compute allocation for LLM reasoning verification from 2025-2026. Here's what the search revealed:

## Key Research Areas

Allocating test-time compute adaptively rather than uniformly provides a foundation for more efficient and reliable LLM reasoning.

## Recent Approaches (2025-2026)

Several specific methods have emerged recently:

1. **LATTS (Locally Adaptive Test-Time Scaling)**: In chain-of-thought settings, LATTS employs step-level verifier scores to decide whether to accept, resample, backtrack, or terminate each reasoning step, allowing per-step compute adaptivity.

2. **State-Level Selective Verification**: A state-level selective verification framework combines deterministic feasibility gating, pre-verification ranking using learned state-distance and residual scoring, and adaptive allocation of verifier calls based on local uncertainty. This approach achieves higher accuracy than best-of-N, majority voting, and beam search while using 44% fewer verifier calls on the MATH benchmark.

3. **Constrained Policy Optimization**: A method using three LLMs (DeepSeek-V3, GPT-4o-mini, Qwen2.5-7B) shows up to 12.8% relative accuracy improvement on MATH under matched budget constraints.

## Implementation Considerations

Implementation of adaptive compute allocation requires careful proxy selection and calibration through difficulty or uncertainty estimation, and budget and penalty tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6730556e-7cac-43fc-8aed-ac3ff344ccec",
  "isSidechain": false,
  "promptId": "7418c215-ebe6-4e47-98f1-b1f363ffe1e7",
  "type": "user",
  "uuid": "0cbbfffb-998a-47b1-9bef-6ea3926782b0",
  "toolUseResult": {
    "query": "adaptive test-time compute allocation LLM reasoning verification 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DyVpvySAewvG3zqmxmEEsQ",
        "content": [
          {
            "title": "Adaptive Test-Time Compute Allocation",
            "url": "https://www.emergentmind.com/topics/adaptive-test-time-compute-allocation"
          },
          {
            "title": "What If We Allocate Test-Time Compute Adaptively?",
            "url": "https://arxiv.org/html/2602.01070"
          },
          {
            "title": "Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure",
            "url": "https://arxiv.org/html/2602.03975v1"
          },
          {
            "title": "Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization",
            "url": "https://arxiv.org/html/2604.14853v1"
          },
          {
            "title": "Adaptive Test-Time Compute Allocation for Reasoning LLMs via...",
            "url": "https://arxiv.org/abs/2604.14853"
          },
          {
            "title": "[2602.03975] Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure",
            "url": "https://arxiv.org/abs/2602.03975"
          }
        ]
      },
      "I found several highly relevant research papers and resources on adaptive test-time compute allocation for LLM reasoning verification from 2025-2026. Here's what the search revealed:\n\n## Key Research Areas\n\nAllocating test-time compute adaptively rather than uniformly provides a foundation for more efficient and reliable LLM reasoning.\n\n## Recent Approaches (2025-2026)\n\nSeveral specific methods have emerged recently:\n\n1. **LATTS (Locally Adaptive Test-Time Scaling)**: In chain-of-thought settings, LATTS employs step-level verifier scores to decide whether to accept, resample, backtrack, or terminate each reasoning step, allowing per-step compute adaptivity.\n\n2. **State-Level Selective Verification**: A state-level selective verification framework combines deterministic feasibility gating, pre-verification ranking using learned state-distance and residual scoring, and adaptive allocation of verifier calls based on local uncertainty. This approach achieves higher accuracy than best-of-N, majority voting, and beam search while using 44% fewer verifier calls on the MATH benchmark.\n\n3. **Constrained Policy Optimization**: A method using three LLMs (DeepSeek-V3, GPT-4o-mini, Qwen2.5-7B) shows up to 12.8% relative accuracy improvement on MATH under matched budget constraints.\n\n## Implementation Considerations\n\nImplementation of adaptive compute allocation requires careful proxy selection and calibration through difficulty or uncertainty estimation, and budget and penalty tuning."
    ],
    "durationSeconds": 8.621465227999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6730556e-7cac-43fc-8aed-ac3ff344ccec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-29T06:51:30.394Z_

<details><summary>↩ Tool result · `toolu_01PFi1QRMeQEy8Mw1M9rgFnC`</summary>

```text
Web search results for query: "GenRM discriminative generative reward model joint optimization compute budget 2025 2026"

Links: [{"title":"Generative Reward Models (GRMs)","url":"https://www.emergentmind.com/topics/generative-reward-models-grms"},{"title":"GitHub - RyanLiu112/GenPRM: [AAAI 2026] Official codebase for \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\".","url":"https://github.com/RyanLiu112/GenPRM"},{"title":"Generative Reward Models","url":"https://www.emergentmind.com/topics/generative-reward-models-genrm"},{"title":"R-Align: Enhancing Generative Reward Models through ...","url":"https://arxiv.org/pdf/2602.06763"},{"title":"GRM-OMNI: GENERATIVE OMNI-MODALITY RE","url":"https://openreview.net/pdf/aa17dc394f91584f717cd1768792b32c61f42a04.pdf"},{"title":"Joint Reward Modeling: Internalizing Chain-of-Thought for Efficient Visual Reward Models","url":"https://arxiv.org/pdf/2602.07533"},{"title":"Generative Reward Models | OpenReview","url":"https://openreview.net/forum?id=MwU2SGLKpS"}]

Based on the search results, here's what I found about GenRM, discriminative/generative reward models, and related topics for 2025-2026:

## Generative Reward Models (GenRM)

GenRM is a paradigm where evaluation of model outputs is framed as a next-token prediction or text generation task, with GenRMs natively leveraging the text generation capabilities of LLMs, integrating verification and solution generation into a unified architecture.

GenRM can efficiently convert extra inference-time compute into accuracy gains by generating more verification chains per candidate and averaging their outputs, with scalability spanning both compute (test-time majority voting) and data/model size.

## Joint Optimization and Compute Budget

Joint Reward Modeling (JRM) compares Generative, Discriminative, and Joint Reward Modeling paradigms, with JRM achieving state-of-the-art accuracy on benchmarks and significantly boosting downstream RL performance.

Generative reward models commonly support inference-time scalability through repeated CoT steps, ensembling via sampling, or parallel generation, with additional compute directly increasing scoring reliability and discrimination.

## Recent Work (2025-2026)

GenPRM was accepted by AAAI 2026, and GenPRM focuses on scaling test-time compute of process reward models via generative reasoning. Additionally, recent work includes optimization of GenRMs for accurate preference label prediction from 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06688451-c0d8-41ed-ba4b-9eac4677d520",
  "isSidechain": false,
  "promptId": "7418c215-ebe6-4e47-98f1-b1f363ffe1e7",
  "type": "user",
  "uuid": "7889e69b-e320-43d2-9272-59ad552eb544",
  "toolUseResult": {
    "query": "GenRM discriminative generative reward model joint optimization compute budget 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BLb17Ax8MaHnTfYY2QnoHj",
        "content": [
          {
            "title": "Generative Reward Models (GRMs)",
            "url": "https://www.emergentmind.com/topics/generative-reward-models-grms"
          },
          {
            "title": "GitHub - RyanLiu112/GenPRM: [AAAI 2026] Official codebase for \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\".",
            "url": "https://github.com/RyanLiu112/GenPRM"
          },
          {
            "title": "Generative Reward Models",
            "url": "https://www.emergentmind.com/topics/generative-reward-models-genrm"
          },
          {
            "title": "R-Align: Enhancing Generative Reward Models through ...",
            "url": "https://arxiv.org/pdf/2602.06763"
          },
          {
            "title": "GRM-OMNI: GENERATIVE OMNI-MODALITY RE",
            "url": "https://openreview.net/pdf/aa17dc394f91584f717cd1768792b32c61f42a04.pdf"
          },
          {
            "title": "Joint Reward Modeling: Internalizing Chain-of-Thought for Efficient Visual Reward Models",
            "url": "https://arxiv.org/pdf/2602.07533"
          },
          {
            "title": "Generative Reward Models | OpenReview",
            "url": "https://openreview.net/forum?id=MwU2SGLKpS"
          }
        ]
      },
      "Based on the search results, here's what I found about GenRM, discriminative/generative reward models, and related topics for 2025-2026:\n\n## Generative Reward Models (GenRM)\n\nGenRM is a paradigm where evaluation of model outputs is framed as a next-token prediction or text generation task, with GenRMs natively leveraging the text generation capabilities of LLMs, integrating verification and solution generation into a unified architecture.\n\nGenRM can efficiently convert extra inference-time compute into accuracy gains by generating more verification chains per candidate and averaging their outputs, with scalability spanning both compute (test-time majority voting) and data/model size.\n\n## Joint Optimization and Compute Budget\n\nJoint Reward Modeling (JRM) compares Generative, Discriminative, and Joint Reward Modeling paradigms, with JRM achieving state-of-the-art accuracy on benchmarks and significantly boosting downstream RL performance.\n\nGenerative reward models commonly support inference-time scalability through repeated CoT steps, ensembling via sampling, or parallel generation, with additional compute directly increasing scoring reliability and discrimination.\n\n## Recent Work (2025-2026)\n\nGenPRM was accepted by AAAI 2026, and GenPRM focuses on scaling test-time compute of process reward models via generative reasoning. Additionally, recent work includes optimization of GenRMs for accurate preference label prediction from 2025."
    ],
    "durationSeconds": 8.517777376999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "06688451-c0d8-41ed-ba4b-9eac4677d520",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-29T06:51:33.610Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SgbRD2U1qATiifgN76HTCy`</summary>

```json
{
  "query": "Strategic Scaling bandit test-time compute Zuo 2025 adaptive K verification arXiv 2506.12721"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7889e69b-e320-43d2-9272-59ad552eb544",
  "isSidechain": false,
  "requestId": "req_011CbWR9iZBoqaqXpR6Jdkgm",
  "type": "assistant",
  "uuid": "99a4d5c6-51c8-4d19-8d2b-1aab636d3c24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zWqMQahEfdqBYBFLzTXpK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2352,
      "cache_read_input_tokens": 20301,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2352,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 20301,
          "cache_creation_input_tokens": 2352,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2352
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

_source line 20 · 2026-05-29T06:51:33.968Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0114YLQzTUvD4MRM8hAaV7ZQ`</summary>

```json
{
  "query": "budget-aware hybrid verification discriminative generative Montgomery 2025 arXiv 2510.14913"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99a4d5c6-51c8-4d19-8d2b-1aab636d3c24",
  "isSidechain": false,
  "requestId": "req_011CbWR9iZBoqaqXpR6Jdkgm",
  "type": "assistant",
  "uuid": "2426dcda-b6ae-4674-aaf1-4dc3fe0efe9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zWqMQahEfdqBYBFLzTXpK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2352,
      "cache_read_input_tokens": 20301,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2352,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 20301,
          "cache_creation_input_tokens": 2352,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2352
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

_source line 21 · 2026-05-29T06:51:41.117Z_

<details><summary>↩ Tool result · `toolu_01SgbRD2U1qATiifgN76HTCy`</summary>

```text
Web search results for query: "Strategic Scaling bandit test-time compute Zuo 2025 adaptive K verification arXiv 2506.12721"

Links: [{"title":"[PDF] Strategic Scaling of Test-Time Compute: A Bandit Learning Approach | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Strategic-Scaling-of-Test-Time-Compute:-A-Bandit-Zuo-Zhu/45c71d6853d52774ae6ad5d8f66ed72bda99f99d"},{"title":"[2506.12721] Strategic Scaling of Test-Time Compute: A Bandit Learning Approach","url":"https://arxiv.org/abs/2506.12721"},{"title":"(PDF) Strategic Scaling of Test-Time Compute: A Bandit Learning Approach","url":"https://www.researchgate.net/publication/392736240_Strategic_Scaling_of_Test-Time_Compute_A_Bandit_Learning_Approach"},{"title":"Strategic Scaling of Test-Time Compute: A Bandit Learning Approach Bowen Zuo","url":"https://arxiv.org/pdf/2506.12721"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=20225&show=25"},{"title":"Artificial Intelligence Jun 2025","url":"https://www.arxiv.org/list/cs.AI/2025-06?skip=400&show=25"},{"title":"Computation and Language Jun 2025","url":"https://www.arxiv.org/list/cs.CL/2025-06?skip=2150&show=25"},{"title":"ADAPTIVE TEST-TIME REASONING VIA REWARD- GUIDED DUAL-PHASE SEARCH","url":"https://www.arxiv.org/pdf/2509.25420"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

## Paper Information

The paper "Strategic Scaling of Test-Time Compute: A Bandit Learning Approach" by Bowen Zuo and Yinglun Zhu was submitted on June 15, 2025 (arXiv:2506.12721).

## Core Contribution

The authors formulate test-time compute allocation as a novel bandit learning problem and propose adaptive algorithms that estimate query difficulty on the fly and allocate compute accordingly. Scaling test-time compute has emerged as an effective strategy for improving the performance of large language models, but existing methods typically allocate compute uniformly across all queries, overlooking variation in query difficulty.

## Key Results

Their algorithms allocate more compute to challenging queries while maintaining accuracy on easier ones, and further learn to prioritize solvable instances among challenging queries, effectively reducing excessive computing on unsolvable queries. 

Empirically, the method achieves up to 11.10% absolute (15.04% relative) improvement on the MATH-500 dataset, 10.82% absolute (14.44% relative) on AIME25, and 11.23% absolute (15.29% relative) on LiveCodeBench—all under the same compute budget as baselines.

The authors theoretically prove that their algorithms achieve better compute efficiency than uniform allocation and empirically validate their effectiveness on math and code benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99a4d5c6-51c8-4d19-8d2b-1aab636d3c24",
  "isSidechain": false,
  "promptId": "7418c215-ebe6-4e47-98f1-b1f363ffe1e7",
  "type": "user",
  "uuid": "c9d6e069-9ba1-4c41-b541-372404769667",
  "toolUseResult": {
    "query": "Strategic Scaling bandit test-time compute Zuo 2025 adaptive K verification arXiv 2506.12721",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PCoQDwmRAoVq5oabzayTkJ",
        "content": [
          {
            "title": "[PDF] Strategic Scaling of Test-Time Compute: A Bandit Learning Approach | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Strategic-Scaling-of-Test-Time-Compute:-A-Bandit-Zuo-Zhu/45c71d6853d52774ae6ad5d8f66ed72bda99f99d"
          },
          {
            "title": "[2506.12721] Strategic Scaling of Test-Time Compute: A Bandit Learning Approach",
            "url": "https://arxiv.org/abs/2506.12721"
          },
          {
            "title": "(PDF) Strategic Scaling of Test-Time Compute: A Bandit Learning Approach",
            "url": "https://www.researchgate.net/publication/392736240_Strategic_Scaling_of_Test-Time_Compute_A_Bandit_Learning_Approach"
          },
          {
            "title": "Strategic Scaling of Test-Time Compute: A Bandit Learning Approach Bowen Zuo",
            "url": "https://arxiv.org/pdf/2506.12721"
          },
          {
            "title": "Computation and Language 2025",
            "url": "https://arxiv.org/list/cs.CL/2025?skip=20225&show=25"
          },
          {
            "title": "Artificial Intelligence Jun 2025",
            "url": "https://www.arxiv.org/list/cs.AI/2025-06?skip=400&show=25"
          },
          {
            "title": "Computation and Language Jun 2025",
            "url": "https://www.arxiv.org/list/cs.CL/2025-06?skip=2150&show=25"
          },
          {
            "title": "ADAPTIVE TEST-TIME REASONING VIA REWARD- GUIDED DUAL-PHASE SEARCH",
            "url": "https://www.arxiv.org/pdf/2509.25420"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what I found:\n\n## Paper Information\n\nThe paper \"Strategic Scaling of Test-Time Compute: A Bandit Learning Approach\" by Bowen Zuo and Yinglun Zhu was submitted on June 15, 2025 (arXiv:2506.12721).\n\n## Core Contribution\n\nThe authors formulate test-time compute allocation as a novel bandit learning problem and propose adaptive algorithms that estimate query difficulty on the fly and allocate compute accordingly. Scaling test-time compute has emerged as an effective strategy for improving the performance of large language models, but existing methods typically allocate compute uniformly across all queries, overlooking variation in query difficulty.\n\n## Key Results\n\nTheir algorithms allocate more compute to challenging queries while maintaining accuracy on easier ones, and further learn to prioritize solvable instances among challenging queries, effectively reducing excessive computing on unsolvable queries. \n\nEmpirically, the method achieves up to 11.10% absolute (15.04% relative) improvement on the MATH-500 dataset, 10.82% absolute (14.44% relative) on AIME25, and 11.23% absolute (15.29% relative) on LiveCodeBench—all under the same compute budget as baselines.\n\nThe authors theoretically prove that their algorithms achieve better compute efficiency than uniform allocation and empirically validate their effectiveness on math and code benchmarks."
    ],
    "durationSeconds": 7.4999336150000016,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "99a4d5c6-51c8-4d19-8d2b-1aab636d3c24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Difficulty-Adaptive Joint Generation-Verification Compute Allocation for LLM Reasoning  ## Core Problem and Moti…",
  "leafUuid": "c9d6e069-9ba1-4c41-b541-372404769667",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate difficulty-adaptive verification type selection proposal",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94"
}
```

---

### Tool result

_source line 24 · 2026-05-29T06:51:41.685Z_

<details><summary>↩ Tool result · `toolu_0114YLQzTUvD4MRM8hAaV7ZQ`</summary>

```text
Web search results for query: "budget-aware hybrid verification discriminative generative Montgomery 2025 arXiv 2510.14913"

Links: [{"title":"[2510.14913] Budget-aware Test-time Scaling via Discriminative Verification","url":"https://arxiv.org/abs/2510.14913"},{"title":"[2510.14913v1] Budget-aware Test-time Scaling via Discriminative Verification","url":"https://arxiv.org/abs/2510.14913v1"},{"title":"dblp: Budget-aware Test-time Scaling via Discriminative Verification.","url":"https://dblp.org/rec/journals/corr/abs-2510-14913.html"},{"title":"Budget-aware Test-time Scaling via Discriminative Verification","url":"https://arxiv.org/html/2510.14913"},{"title":"Budget-aware Test-time Scaling via Discriminative Verification","url":"https://arxiv.org/pdf/2510.14913"}]

I found the paper! Here are the key details:

The paper discusses test-time scaling as a powerful strategy for boosting the performance of large language models on complex reasoning tasks. 

While state-of-the-art approaches often employ generative verifiers to select the best solution from a pool of candidates, this method incurs prohibitive computational costs, limiting its practicality. The work shifts the focus to a more budget-aware paradigm: discriminative verification, and demonstrates that combining discriminative verifiers with self-consistency in a hybrid approach creates a powerful and efficient test-time scaling mechanism.

Under a fixed compute budget, this hybrid approach surpasses state-of-the-art generative verification by a significant margin: achieving up to 15.3% higher accuracy on AIME2025.

The paper was submitted on October 16, 2025, and authored by Kyle Montgomery, Sijun Tan, Yuqi Chen, Siyuan Zhuang, Tianjun Zhang, Raluca Ada Popa, and Chenguang Wang. The code is available at https://github.com/wang-research-lab/verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2426dcda-b6ae-4674-aaf1-4dc3fe0efe9f",
  "isSidechain": false,
  "promptId": "7418c215-ebe6-4e47-98f1-b1f363ffe1e7",
  "type": "user",
  "uuid": "e2980f48-4757-469b-8dad-bd7af3325824",
  "toolUseResult": {
    "query": "budget-aware hybrid verification discriminative generative Montgomery 2025 arXiv 2510.14913",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XqK9hnaJaiKP26X3vN7bHk",
        "content": [
          {
            "title": "[2510.14913] Budget-aware Test-time Scaling via Discriminative Verification",
            "url": "https://arxiv.org/abs/2510.14913"
          },
          {
            "title": "[2510.14913v1] Budget-aware Test-time Scaling via Discriminative Verification",
            "url": "https://arxiv.org/abs/2510.14913v1"
          },
          {
            "title": "dblp: Budget-aware Test-time Scaling via Discriminative Verification.",
            "url": "https://dblp.org/rec/journals/corr/abs-2510-14913.html"
          },
          {
            "title": "Budget-aware Test-time Scaling via Discriminative Verification",
            "url": "https://arxiv.org/html/2510.14913"
          },
          {
            "title": "Budget-aware Test-time Scaling via Discriminative Verification",
            "url": "https://arxiv.org/pdf/2510.14913"
          }
        ]
      },
      "I found the paper! Here are the key details:\n\nThe paper discusses test-time scaling as a powerful strategy for boosting the performance of large language models on complex reasoning tasks. \n\nWhile state-of-the-art approaches often employ generative verifiers to select the best solution from a pool of candidates, this method incurs prohibitive computational costs, limiting its practicality. The work shifts the focus to a more budget-aware paradigm: discriminative verification, and demonstrates that combining discriminative verifiers with self-consistency in a hybrid approach creates a powerful and efficient test-time scaling mechanism.\n\nUnder a fixed compute budget, this hybrid approach surpasses state-of-the-art generative verification by a significant margin: achieving up to 15.3% higher accuracy on AIME2025.\n\nThe paper was submitted on October 16, 2025, and authored by Kyle Montgomery, Sijun Tan, Yuqi Chen, Siyuan Zhuang, Tianjun Zhang, Raluca Ada Popa, and Chenguang Wang. The code is available at https://github.com/wang-research-lab/verification."
    ],
    "durationSeconds": 7.712852573,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2426dcda-b6ae-4674-aaf1-4dc3fe0efe9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-29T06:51:45.046Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vndg2voZkkhYju3DEJokRn`</summary>

```json
{
  "query": "AVA anytime verified agents dynamic compute allocation search verification 2026 OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2980f48-4757-469b-8dad-bd7af3325824",
  "isSidechain": false,
  "requestId": "req_011CbWRAYPXXm4hSypW317Cu",
  "type": "assistant",
  "uuid": "45d546fd-d510-4d56-878b-3f7d9a8a3df2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAyU8De9TB1BXto51SMx51",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1520,
      "cache_read_input_tokens": 22653,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 22653,
          "cache_creation_input_tokens": 1520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1520
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

_source line 26 · 2026-05-29T06:51:46.258Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VaPm7nJZLsHUQfG4kpxwAz`</summary>

```json
{
  "query": "\"variation in verification\" ICLR 2026 verifier reliability difficulty heterogeneous arXiv 2509.17995"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45d546fd-d510-4d56-878b-3f7d9a8a3df2",
  "isSidechain": false,
  "requestId": "req_011CbWRAYPXXm4hSypW317Cu",
  "type": "assistant",
  "uuid": "2a117974-c32f-43ac-846a-61c1d2333582",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAyU8De9TB1BXto51SMx51",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1520,
      "cache_read_input_tokens": 22653,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 22653,
          "cache_creation_input_tokens": 1520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1520
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

_source line 27 · 2026-05-29T06:51:51.736Z_

<details><summary>↩ Tool result · `toolu_01Vndg2voZkkhYju3DEJokRn`</summary>

```text
Web search results for query: "AVA anytime verified agents dynamic compute allocation search verification 2026 OpenReview"

Links: [{"title":"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints | OpenReview","url":"https://openreview.net/forum?id=JMDCMf7mlF"},{"title":"What If We Allocate Test-Time Compute Adaptively?","url":"https://arxiv.org/pdf/2602.01070"},{"title":"Pushing Test-Time Scaling Limits of Deep Search with Asymmetric Verification","url":"https://arxiv.org/pdf/2510.06135"},{"title":"Verified Multi-Agent Orchestration: A Plan-Execute-Verify-Replan Framework for Complex Query Resolution | OpenReview","url":"https://openreview.net/forum?id=WUmz4LUbvU"},{"title":"Unified Plan Verification with Static Rubrics and Dynamic Policies for Reliable LLM Planning | OpenReview","url":"https://openreview.net/forum?id=qDFegAnCin"},{"title":"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure","url":"https://arxiv.org/pdf/2602.03975"},{"title":"Agentic Test-Time Scaling for WebAgents","url":"https://arxiv.org/pdf/2602.12276"}]

Based on the search results, I found the paper you're looking for:

**Anytime Verified Agents (AVA)** is a framework that dynamically allocates compute across search, sampling, and verification within a user-specified budget, with an extensible interface for tool use.

The paper was posted on OpenReview in April 2026 and addresses a key limitation in existing approaches. Existing methods allocate computational resources using static strategies such as fixed search depths, constant self-consistency sampling, or uniform verification, so simple problems can consume as much compute as complex tasks.

AVA combines calibrated uncertainty estimation, value-of-information-guided search expansion, and selective verification cascades with early exits. The controller allocates compute based on uncertainty and estimated marginal reliability gains.

AVA is evaluated on mathematical reasoning (GSM8K and MATH), multi-hop question answering (HotpotQA), and code generation (HumanEval), with two model backends.

You can find the full paper on OpenReview at: https://openreview.net/forum?id=JMDCMf7mlF


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45d546fd-d510-4d56-878b-3f7d9a8a3df2",
  "isSidechain": false,
  "promptId": "7418c215-ebe6-4e47-98f1-b1f363ffe1e7",
  "type": "user",
  "uuid": "9b494285-3b48-48ec-9584-0aafe8bdae3e",
  "toolUseResult": {
    "query": "AVA anytime verified agents dynamic compute allocation search verification 2026 OpenReview",
    "results": [
      {
        "tool_use_id": "srvtoolu_015eTx1NHAQE4XAnks17Tvi7",
        "content": [
          {
            "title": "Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints | OpenReview",
            "url": "https://openreview.net/forum?id=JMDCMf7mlF"
          },
          {
            "title": "What If We Allocate Test-Time Compute Adaptively?",
            "url": "https://arxiv.org/pdf/2602.01070"
          },
          {
            "title": "Pushing Test-Time Scaling Limits of Deep Search with Asymmetric Verification",
            "url": "https://arxiv.org/pdf/2510.06135"
          },
          {
            "title": "Verified Multi-Agent Orchestration: A Plan-Execute-Verify-Replan Framework for Complex Query Resolution | OpenReview",
            "url": "https://openreview.net/forum?id=WUmz4LUbvU"
          },
          {
            "title": "Unified Plan Verification with Static Rubrics and Dynamic Policies for Reliable LLM Planning | OpenReview",
            "url": "https://openreview.net/forum?id=qDFegAnCin"
          },
          {
            "title": "Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure",
            "url": "https://arxiv.org/pdf/2602.03975"
          },
          {
            "title": "Agentic Test-Time Scaling for WebAgents",
            "url": "https://arxiv.org/pdf/2602.12276"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Anytime Verified Agents (AVA)** is a framework that dynamically allocates compute across search, sampling, and verification within a user-specified budget, with an extensible interface for tool use.\n\nThe paper was posted on OpenReview in April 2026 and addresses a key limitation in existing approaches. Existing methods allocate computational resources using static strategies such as fixed search depths, constant self-consistency sampling, or uniform verification, so simple problems can consume as much compute as complex tasks.\n\nAVA combines calibrated uncertainty estimation, value-of-information-guided search expansion, and selective verification cascades with early exits. The controller allocates compute based on uncertainty and estimated marginal reliability gains.\n\nAVA is evaluated on mathematical reasoning (GSM8K and MATH), multi-hop question answering (HotpotQA), and code generation (HumanEval), with two model backends.\n\nYou can find the full paper on OpenReview at: https://openreview.net/forum?id=JMDCMf7mlF"
    ],
    "durationSeconds": 6.686793726999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "45d546fd-d510-4d56-878b-3f7d9a8a3df2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-29T06:51:54.639Z_

<details><summary>↩ Tool result · `toolu_01VaPm7nJZLsHUQfG4kpxwAz`</summary>

```text
Web search results for query: ""variation in verification" ICLR 2026 verifier reliability difficulty heterogeneous arXiv 2509.17995"

Links: [{"title":"[2509.17995] Variation in Verification: Understanding Verification Dynamics in Large Language Models","url":"https://arxiv.org/abs/2509.17995"},{"title":"Variation in Verification: Understanding Verification Dynamics in Large Language Models","url":"https://arxiv.org/html/2509.17995"},{"title":"Preprint VARIATION IN VERIFICATION: UNDERSTANDING VERI-","url":"https://arxiv.org/pdf/2509.17995"},{"title":"GitHub - Zhengsh123/SCI-Verifier: Official GitHub repo for SCI-Verifier: Scientific Verifier with Thinking (ICLR2026). · GitHub","url":"https://github.com/Zhengsh123/SCI-Verifier"},{"title":"VerifAI: AI Verification in the Wild - ICLR 2026","url":"https://iclr.cc/virtual/2025/workshop/23973"},{"title":"Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers","url":"https://arxiv.org/pdf/2510.00915"},{"title":"Aletheia: What Makes RLVR For Code Verifiers Tick?","url":"https://arxiv.org/pdf/2601.12186"},{"title":"ICLR 2026 arxiv template · GitHub","url":"https://gist.github.com/dtch1997/2a0ca15ee1dff663c2911170b5475875"}]

Based on the search results, I found the paper you're looking for:

"Variation in Verification" systematically analyzes verification dynamics across three dimensions - problem difficulty, generator capability, and verifier generation capability - with empirical studies on 12 benchmarks across mathematical reasoning, knowledge, and natural language reasoning tasks using 14 open-source models (2B to 72B parameter range) and GPT-4o.

The analysis reveals three patterns: problem difficulty governs recognition of correct responses (true positives); generator generation capability determines error detectability (true negatives); and verifier generation capability correlates with performance.

The research focuses on LLM generators producing multiple solution candidates, with LLM verifiers assessing the correctness of these candidates without reference answers, studying generative verifiers which perform verification by generating chain-of-thought (CoT) reasoning followed by a binary verdict.

The paper was posted on arXiv on April 14, 2026 (with the original version from September 22, 2025) and examines how heterogeneity across problem difficulty, generator capability, and verifier capability affects verification reliability in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a117974-c32f-43ac-846a-61c1d2333582",
  "isSidechain": false,
  "promptId": "7418c215-ebe6-4e47-98f1-b1f363ffe1e7",
  "type": "user",
  "uuid": "9cf28cb1-06b1-48b3-ad88-bb411f3edfe5",
  "toolUseResult": {
    "query": "\"variation in verification\" ICLR 2026 verifier reliability difficulty heterogeneous arXiv 2509.17995",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JC1tY3DyeMrpusxTe4YNV1",
        "content": [
          {
            "title": "[2509.17995] Variation in Verification: Understanding Verification Dynamics in Large Language Models",
            "url": "https://arxiv.org/abs/2509.17995"
          },
          {
            "title": "Variation in Verification: Understanding Verification Dynamics in Large Language Models",
            "url": "https://arxiv.org/html/2509.17995"
          },
          {
            "title": "Preprint VARIATION IN VERIFICATION: UNDERSTANDING VERI-",
            "url": "https://arxiv.org/pdf/2509.17995"
          },
          {
            "title": "GitHub - Zhengsh123/SCI-Verifier: Official GitHub repo for SCI-Verifier: Scientific Verifier with Thinking (ICLR2026). · GitHub",
            "url": "https://github.com/Zhengsh123/SCI-Verifier"
          },
          {
            "title": "VerifAI: AI Verification in the Wild - ICLR 2026",
            "url": "https://iclr.cc/virtual/2025/workshop/23973"
          },
          {
            "title": "Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers",
            "url": "https://arxiv.org/pdf/2510.00915"
          },
          {
            "title": "Aletheia: What Makes RLVR For Code Verifiers Tick?",
            "url": "https://arxiv.org/pdf/2601.12186"
          },
          {
            "title": "ICLR 2026 arxiv template · GitHub",
            "url": "https://gist.github.com/dtch1997/2a0ca15ee1dff663c2911170b5475875"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"Variation in Verification\" systematically analyzes verification dynamics across three dimensions - problem difficulty, generator capability, and verifier generation capability - with empirical studies on 12 benchmarks across mathematical reasoning, knowledge, and natural language reasoning tasks using 14 open-source models (2B to 72B parameter range) and GPT-4o.\n\nThe analysis reveals three patterns: problem difficulty governs recognition of correct responses (true positives); generator generation capability determines error detectability (true negatives); and verifier generation capability correlates with performance.\n\nThe research focuses on LLM generators producing multiple solution candidates, with LLM verifiers assessing the correctness of these candidates without reference answers, studying generative verifiers which perform verification by generating chain-of-thought (CoT) reasoning followed by a binary verdict.\n\nThe paper was posted on arXiv on April 14, 2026 (with the original version from September 22, 2025) and examines how heterogeneity across problem difficulty, generator capability, and verifier capability affects verification reliability in large language models."
    ],
    "durationSeconds": 8.375921523000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2a117974-c32f-43ac-846a-61c1d2333582",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-29T06:51:54.643Z_

```json
{
  "parentUuid": "9cf28cb1-06b1-48b3-ad88-bb411f3edfe5",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9da8261b-8ab8-41a7-a0cd-c6322fa84382",
  "timestamp": "2026-05-29T06:51:54.643Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 30 · 2026-05-29T06:51:58.639Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the research landscape. Let me synthesize my findings and provide the evaluation.

Let me also search for one more thing - the DTR paper and LiLaVe to confirm those exist.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9da8261b-8ab8-41a7-a0cd-c6322fa84382",
  "isSidechain": false,
  "requestId": "req_011CbWRBVn3KXC9po6GwAGPA",
  "type": "assistant",
  "uuid": "9498767b-2d35-499b-a615-098841da9c95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzpEtR6Br36x1cHC1B7MfW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 24173,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 24173,
          "cache_creation_input_tokens": 1585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1585
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

_source line 31 · 2026-05-29T06:51:59.557Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V3dT3rajrzo86iAevfrYLN`</summary>

```json
{
  "query": "DTR deep thinking tokens difficulty estimation LLM reasoning arXiv 2602.13517 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9498767b-2d35-499b-a615-098841da9c95",
  "isSidechain": false,
  "requestId": "req_011CbWRBVn3KXC9po6GwAGPA",
  "type": "assistant",
  "uuid": "264c5eaa-4f4e-4154-86ea-e0de75a8ec18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzpEtR6Br36x1cHC1B7MfW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 24173,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 24173,
          "cache_creation_input_tokens": 1585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1585
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

_source line 32 · 2026-05-29T06:51:59.944Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FqvsNsVqKKCvVRyHfBJiWe`</summary>

```json
{
  "query": "LiLaVe lightweight latent verifier hidden state verification LLM arXiv 2504.16760"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "264c5eaa-4f4e-4154-86ea-e0de75a8ec18",
  "isSidechain": false,
  "requestId": "req_011CbWRBVn3KXC9po6GwAGPA",
  "type": "assistant",
  "uuid": "bdf08b5e-6dcc-4470-9c55-c38788f89d28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzpEtR6Br36x1cHC1B7MfW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1585,
      "cache_read_input_tokens": 24173,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 24173,
          "cache_creation_input_tokens": 1585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1585
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

_source line 33 · 2026-05-29T06:52:06.495Z_

<details><summary>↩ Tool result · `toolu_01V3dT3rajrzo86iAevfrYLN`</summary>

```text
Web search results for query: "DTR deep thinking tokens difficulty estimation LLM reasoning arXiv 2602.13517 2026"

Links: [{"title":"Deep-Thinking Tokens in LLM Reasoning","url":"https://www.emergentmind.com/papers/2602.13517"},{"title":"Measuring LLM Reasoning Effort via Deep-Thinking Tokens","url":"https://arxiv.org/pdf/2602.13517"},{"title":"Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens","url":"https://arxiv.org/html/2602.13517v1"},{"title":"Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens","url":"https://arxiviq.substack.com/p/think-deep-not-just-long-measuring"},{"title":"[2602.13517v1] Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens","url":"https://arxiv.org/abs/2602.13517v1"},{"title":"A New Google AI Research Proposes Deep-Thinking Ratio to Improve LLM Accuracy While Cutting Total Inference Costs by Half - MarkTechPost","url":"https://www.marktechpost.com/2026/02/21/a-new-google-ai-research-proposes-deep-thinking-ratio-to-improve-llm-accuracy-while-cutting-total-inference-costs-by-half/"},{"title":"Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260213517C/abstract"},{"title":"[2602.13517] Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens","url":"https://arxiv.org/abs/2602.13517"},{"title":"Paper page - Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens","url":"https://huggingface.co/papers/2602.13517"}]

I found comprehensive information about the paper arXiv 2602.13517. Here's what the research is about:

## Overview

The paper "Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens" (arXiv:2602.13517) was submitted on February 13, 2026.

## Key Concept: Deep-Thinking Tokens

The research quantifies inference-time effort by identifying deep-thinking tokens -- tokens where internal predictions undergo significant revisions in deeper model layers prior to convergence. The deep-thinking ratio (DTR) for an output sequence is simply the fraction of its tokens classified as deep-thinking.

## Main Finding: DTR vs. Token Length

Raw token counts are unreliable proxies for reasoning quality: increased generation length does not consistently correlate with accuracy and may instead signal "overthinking," leading to performance degradation. In contrast, DTR showed a strong average positive correlation of r = 0.683 with accuracy across models like DeepSeek-R1-70B, Qwen3-30B-Thinking, and GPT-OSS-120B.

## Methodology

DTR isolates "deep-thinking tokens" by tracking the layer-wise predictive distributions of intermediate hidden states—tokens whose probability distributions undergo sustained, depth-wise revisions before stabilizing in the latest transformer layers.

## Practical Application

The paper demonstrates a test-time compute scaling approach, Think@n, that reduces inference cost while maintaining or improving performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "264c5eaa-4f4e-4154-86ea-e0de75a8ec18",
  "isSidechain": false,
  "promptId": "7418c215-ebe6-4e47-98f1-b1f363ffe1e7",
  "type": "user",
  "uuid": "6d46ea79-4003-4d64-949e-136ee5e78479",
  "toolUseResult": {
    "query": "DTR deep thinking tokens difficulty estimation LLM reasoning arXiv 2602.13517 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GPWwjiFQQcdYij2GNhW4g6",
        "content": [
          {
            "title": "Deep-Thinking Tokens in LLM Reasoning",
            "url": "https://www.emergentmind.com/papers/2602.13517"
          },
          {
            "title": "Measuring LLM Reasoning Effort via Deep-Thinking Tokens",
            "url": "https://arxiv.org/pdf/2602.13517"
          },
          {
            "title": "Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens",
            "url": "https://arxiv.org/html/2602.13517v1"
          },
          {
            "title": "Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens",
            "url": "https://arxiviq.substack.com/p/think-deep-not-just-long-measuring"
          },
          {
            "title": "[2602.13517v1] Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens",
            "url": "https://arxiv.org/abs/2602.13517v1"
          },
          {
            "title": "A New Google AI Research Proposes Deep-Thinking Ratio to Improve LLM Accuracy While Cutting Total Inference Costs by Half - MarkTechPost",
            "url": "https://www.marktechpost.com/2026/02/21/a-new-google-ai-research-proposes-deep-thinking-ratio-to-improve-llm-accuracy-while-cutting-total-inference-costs-by-half/"
          },
          {
            "title": "Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2026arXiv260213517C/abstract"
          },
          {
            "title": "[2602.13517] Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens",
            "url": "https://arxiv.org/abs/2602.13517"
          },
          {
            "title": "Paper page - Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens",
            "url": "https://huggingface.co/papers/2602.13517"
          }
        ]
      },
      "I found comprehensive information about the paper arXiv 2602.13517. Here's what the research is about:\n\n## Overview\n\nThe paper \"Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens\" (arXiv:2602.13517) was submitted on February 13, 2026.\n\n## Key Concept: Deep-Thinking Tokens\n\nThe research quantifies inference-time effort by identifying deep-thinking tokens -- tokens where internal predictions undergo significant revisions in deeper model layers prior to convergence. The deep-thinking ratio (DTR) for an output sequence is simply the fraction of its tokens classified as deep-thinking.\n\n## Main Finding: DTR vs. Token Length\n\nRaw token counts are unreliable proxies for reasoning quality: increased generation length does not consistently correlate with accuracy and may instead signal \"overthinking,\" leading to performance degradation. In contrast, DTR showed a strong average positive correlation of r = 0.683 with accuracy across models like DeepSeek-R1-70B, Qwen3-30B-Thinking, and GPT-OSS-120B.\n\n## Methodology\n\nDTR isolates \"deep-thinking tokens\" by tracking the layer-wise predictive distributions of intermediate hidden states—tokens whose probability distributions undergo sustained, depth-wise revisions before stabilizing in the latest transformer layers.\n\n## Practical Application\n\nThe paper demonstrates a test-time compute scaling approach, Think@n, that reduces inference cost while maintaining or improving performance."
    ],
    "durationSeconds": 6.9313610059999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "264c5eaa-4f4e-4154-86ea-e0de75a8ec18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-29T06:52:06.762Z_

<details><summary>↩ Tool result · `toolu_01FqvsNsVqKKCvVRyHfBJiWe`</summary>

```text
Web search results for query: "LiLaVe lightweight latent verifier hidden state verification LLM arXiv 2504.16760"

Links: [{"title":"[2504.16760] Lightweight Latent Verifiers for Efficient Meta-Generation Strategies","url":"https://arxiv.org/abs/2504.16760"},{"title":"Lightweight Latent Verifiers for Efficient Meta-Generation Strategies | OpenReview","url":"https://openreview.net/forum?id=JQ0OdJHOsQ"},{"title":"Lightweight Latent Verifiers for Efficient Meta-Generation Strategies","url":"https://arxiv.org/html/2504.16760"},{"title":"Preprint. Under review. Lightweight Latent Verifiers","url":"https://arxiv.org/pdf/2504.16760"},{"title":"Exposing the Ghost in the Transformer: Abnormal Detection for Large Language Models via Hidden State Forensics","url":"https://arxiv.org/pdf/2504.00446"},{"title":"CLUE: Non-parametric Verification from Experience via Hidden-State Clustering","url":"https://arxiv.org/pdf/2510.01591"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018.full.pdf"}]

Based on the search results, I found information about the LiLaVe paper (arXiv 2504.16760):

## LiLaVe: Lightweight Latent Verifier

LiLaVe is a novel lightweight verification approach that reliably extracts correctness signals from the hidden states of the base LLM. 

### Key Advantages

Traditional verifiers are typically LLMs themselves, often as large or larger than the base model, making them computationally expensive, while LiLaVe operates with only a small fraction of the computational budget required by traditional LLM-based verifiers.

### Applications

LiLaVe is coupled with popular meta-generation strategies like best-of-n or self-consistency, and novel LiLaVe-based approaches like conditional self-correction or conditional majority voting have been designed that significantly improve both accuracy and efficiency in generation tasks.

### Performance

LiLaVe achieves comparably good results as large, LLM-based verifiers trained on datasets a couple of orders of magnitude larger.

The paper demonstrates that extracting latent information from the hidden states of LLMs can provide a scalable and resource-efficient approach to verification in reasoning-intensive tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdf08b5e-6dcc-4470-9c55-c38788f89d28",
  "isSidechain": false,
  "promptId": "7418c215-ebe6-4e47-98f1-b1f363ffe1e7",
  "type": "user",
  "uuid": "3b00b940-6f34-4c27-b636-5a45d0c3f851",
  "toolUseResult": {
    "query": "LiLaVe lightweight latent verifier hidden state verification LLM arXiv 2504.16760",
    "results": [
      {
        "tool_use_id": "srvtoolu_012dGGMBZcVxFsY8HQDnZybZ",
        "content": [
          {
            "title": "[2504.16760] Lightweight Latent Verifiers for Efficient Meta-Generation Strategies",
            "url": "https://arxiv.org/abs/2504.16760"
          },
          {
            "title": "Lightweight Latent Verifiers for Efficient Meta-Generation Strategies | OpenReview",
            "url": "https://openreview.net/forum?id=JQ0OdJHOsQ"
          },
          {
            "title": "Lightweight Latent Verifiers for Efficient Meta-Generation Strategies",
            "url": "https://arxiv.org/html/2504.16760"
          },
          {
            "title": "Preprint. Under review. Lightweight Latent Verifiers",
            "url": "https://arxiv.org/pdf/2504.16760"
          },
          {
            "title": "Exposing the Ghost in the Transformer: Abnormal Detection for Large Language Models via Hidden State Forensics",
            "url": "https://arxiv.org/pdf/2504.00446"
          },
          {
            "title": "CLUE: Non-parametric Verification from Experience via Hidden-State Clustering",
            "url": "https://arxiv.org/pdf/2510.01591"
          },
          {
            "title": "Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs",
            "url": "https://www.medrxiv.org/content/10.1101/2025.09.17.25336018.full.pdf"
          }
        ]
      },
      "Based on the search results, I found information about the LiLaVe paper (arXiv 2504.16760):\n\n## LiLaVe: Lightweight Latent Verifier\n\nLiLaVe is a novel lightweight verification approach that reliably extracts correctness signals from the hidden states of the base LLM. \n\n### Key Advantages\n\nTraditional verifiers are typically LLMs themselves, often as large or larger than the base model, making them computationally expensive, while LiLaVe operates with only a small fraction of the computational budget required by traditional LLM-based verifiers.\n\n### Applications\n\nLiLaVe is coupled with popular meta-generation strategies like best-of-n or self-consistency, and novel LiLaVe-based approaches like conditional self-correction or conditional majority voting have been designed that significantly improve both accuracy and efficiency in generation tasks.\n\n### Performance\n\nLiLaVe achieves comparably good results as large, LLM-based verifiers trained on datasets a couple of orders of magnitude larger.\n\nThe paper demonstrates that extracting latent information from the hidden states of LLMs can provide a scalable and resource-efficient approach to verification in reasoning-intensive tasks."
    ],
    "durationSeconds": 6.814862563000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bdf08b5e-6dcc-4470-9c55-c38788f89d28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Difficulty-Adaptive Joint Generation-Verification Compute Allocation for LLM Reasoning  ## Core Problem and Moti…",
  "leafUuid": "3b00b940-6f34-4c27-b636-5a45d0c3f851",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate difficulty-adaptive verification type selection proposal",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94"
}
```

---

### Assistant

_source line 37 · 2026-05-29T06:52:44.029Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the research landscape. Let me synthesize everything and produce my evaluation.

Let me think carefully about this proposal:

**What is JOVA proposing?**
JOVA proposes jointly optimizing two variables: K (number of candidate generations) and d (verification type) per instance, conditioned on problem difficulty, under a shared compute budget. The key insight is that different difficulty levels benefit from different (K, d) combinations, and optimizing them independently loses performance especially in the medium-difficulty regime.

**Strengths I see:**
1. The problem formulation is well-motivated — there IS a real gap in jointly optimizing (K, d) since existing work only optimizes one dimension.


2. The Simpson's Paradox framing elegantly captures how aggregate performance rankings can flip when stratified by difficulty.
3. The experimental rigor is impressive across the board — multiple baselines and ablations, diverse benchmarks and model scales, explicit compute budgeting, and a well-specified verifier hierarchy with concrete costs.
4. The composition gap analysis provides solid theoretical grounding, and the Phase 0 pilot design demonstrates maturity by validating assumptions upfront.
5. The proposal thoughtfully addresses its own limitations, acknowledging DTR's scope constraints and including fallback mechanisms.

**Concerns:**
1. **Incrementality**: This is essentially a routing and scheduling problem layered over existing components, so the novelty lies in the joint optimization framework rather than any fundamentally new verification method or model architecture. A reviewer might dismiss this as engineering rather than scientific contribution.
2. **DTR dependency**: The difficulty signal hasn't been validated at the target model scales (≤14B), and if it underperforms, the fallback signals like logit entropy and SC agreement are considerably weaker. The entire approach depends on having a reliable difficulty measure.
3. **Grid-Search baseline threat**: The per-bucket grid search baseline could be surprisingly competitive, and if it matches JOVA within noise margins, the learned routing adds complexity without meaningful gains. The proposal acknowledges this risk but the arguments for JOVA's advantage remain somewhat speculative.
4. **Composition gap may be small**: The theoretical prediction that the composition gap peaks at medium difficulty is unvalidated empirically, and if the actual gap turns out modest, the whole motivation weakens.
5. **Compute budget**: 350-550 A100-hours is reasonable and feasible.
6. **Evaluation on small benchmarks**: AIME25 only has ~30 problems, so even with 10 seeds the statistical power is limited.
7. **The verifier hierarchy may not hold**: If PRM or Disc-ORM underperforms on the target models, the 4-tier hierarchy breaks down and the routing story loses its foundation.

Looking at how this compares to related work, Strategic Scaling adapts K with a fixed verifier while JOVA jointly optimizes both K and d, which is a clear extension. Montgomery et al. use hybrid verification but apply it uniformly across datasets, whereas JOVA conditions on per-instance difficulty. AVA handles multi-dimensional allocation but...

The uncertainty-driven approach differs from difficulty-driven routing, though a reviewer might push back that these signals are correlated. MAV ensembles all verifiers while JOVA routes to one, and under budget constraints JOVA's approach is more sensible. FlexiVe and SDV use binary fast/slow hierarchies, so generalizing to four tiers is a natural extension.

The proposal is well-executed with clear positioning and thorough experimental design, but the main risk is that empirical gains could be modest—a simple grid-search baseline might be surprisingly competitive—and reviewers might dismiss this as "just routing" rather than a fundamental contribution. The experimental rigor is impressive and the framing is sophisticated, though the novelty concern remains a real vulnerability.

Reconsidering the acceptance odds more carefully: the research problem is strong and well-motivated, the method is solid but incremental as a routing framework over existing components, the experimental design is comprehensive with proper baselines and ablations, and the writing is clear. Against this, the novelty is limited, empirical gains might be marginal, and everything hinges on validating the DTR assumption. Given that AAAI typically accepts around 20-25% of submissions, this sits at roughly 30-35% chance—above average in preparation and problem framing, but facing real risks on novelty and whether the empirical results will actually demonstrate meaningful improvements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b00b940-6f34-4c27-b636-5a45d0c3f851",
  "isSidechain": false,
  "requestId": "req_011CbWRCR1LL9NxCqU1vBLc7",
  "type": "assistant",
  "uuid": "134b831d-2e04-469b-8ff3-026800f6d3e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VV6CzRjCBJqjfHmM3DGqmt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1790,
      "cache_read_input_tokens": 25758,
      "output_tokens": 5754,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5754,
          "cache_read_input_tokens": 25758,
          "cache_creation_input_tokens": 1790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1790
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

_source line 38 · 2026-05-29T06:54:24.969Z_

Now I have sufficient information to make a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- "Variation in Verification" (arXiv 2509.17995, ICLR 2026): 直接奠基论文。揭示了验证器在不同问题难度/生成器能力下的异构可靠性（TPR/TNR随难度变化），为JOVA的difficulty-conditioned routing提供了核心empirical motivation。JOVA可视为对该发现的operational化。
- Strategic Scaling Bandit (Zuo et al., arXiv 2506.12721): 最接近的adaptive-K工作。用UCB bandit自适应调整K，MATH-500上+11.1%。但固定verifier类型不变。JOVA在此基础上增加了d维度的联合优化，差异化清晰。
- Montgomery et al. Budget-aware Verification (arXiv 2510.14913): 最接近的hybrid verification工作。证明discriminative+generative hybrid在固定budget下surpass纯generative达15.3%（AIME25）。但采用per-dataset uniform策略，无per-instance difficulty conditioning。JOVA的per-instance routing是明确的增量贡献。
- AVA: Anytime Verified Agents (OpenReview 2026): 最接近的multi-dimensional allocation工作。动态分配compute across search/sampling/verification，用calibrated uncertainty + early exit cascades。与JOVA的关键差异：uncertainty-driven vs difficulty-driven，continuous allocation vs discrete (K,d) menu。两者在机制层面有实质差异，但reviewer可能质疑difficulty和uncertainty的相关性。
- GenPRM (arXiv 2504.00891, AAAI 2026): 当前verification SOTA，1.5B GenPRM超GPT-4o。但仍是单一fixed verifier，不做adaptive routing。JOVA将其作为verifier hierarchy最高层，定位合理。
- DiffAdapt (ICLR 2026): 难度自适应推理长度（非verification type选择），token reduction 62%。与JOVA正交但共享difficulty-adaptive思路，说明difficulty conditioning是当前热点。
- DTR (arXiv 2602.13517): JOVA依赖的difficulty signal。r=0.683 average accuracy correlation，但仅在≥30B模型上验证。≤14B模型上的有效性是JOVA的关键风险点。
- LiLaVe (arXiv 2504.16760): JOVA最底层verifier（Latent-ORM）。几乎零开销的hidden-state verification，与大型LLM verifier comparable。可行性已验证。
- MAV: Multi-Agent Verification (arXiv 2502.20379): ensemble所有verifiers vs JOVA的per-instance selection/routing。在budget-constrained场景下，routing比ensemble更合理。差异化论证充分。
- FlexiVe/SDV (arXiv 2505.11966): binary fast/slow verification via GRPO。JOVA推广至4-tier hierarchy，是明确的generalization。
- CPO (arXiv 2604.14853): constrained policy optimization for reasoning strategy selection，12.8% relative improvement under matched budget。方法论上与JOVA互补（CPO优化reasoning策略，JOVA优化verification策略）。

- 调研总结: Test-time compute的adaptive allocation是2025-2026年的核心热点，但现有工作均沿单一维度优化（K、verification granularity、binary type、reasoning length、model routing）。JOVA提出的(K,d)联合优化在文献中确实没有直接先例，gap identification成立。但该领域进展极快，竞争激烈，JOVA需要在empirical gains上给出convincing evidence才能脱颖而出。

【整体印象】: 
作为审稿人，第一反应是"这是一篇非常well-prepared的proposal"。文献覆盖广泛且精准（引用了~25篇高度相关工作并逐一区分），问题formulation清晰（(K,d)联合优化under shared budget），实验设计极其详尽（8个baselines、6个ablation、8个budget levels、多benchmark多模型）。Simpson's Paradox类比很巧妙，composition gap的分析框架有理论深度。

然而，核心concern是这本质上是一个routing/scheduling problem over existing components——没有提出新的verification方法，没有训练新模型，创新在于"如何组合已有工具"。一个tough reviewer可能将其定性为"systems/engineering contribution"而非"scientific contribution"。另一个关键风险是Grid-Search-(K,d)-per-bucket这个strong trivial baseline：如果简单的per-difficulty-bin lookup table就能capture大部分joint optimization gain，JOVA的learned routing的marginal value会很小。

总体倾向：borderline，偏向weak accept方向。如果empirical results显示composition gap显著（>3%）且JOVA大幅超越grid-search baseline，可以push到accept。

【核心贡献】: 
1. 识别并formalize了(K,d)联合优化问题——在shared compute budget下，generation数量与verification类型的耦合关系。这一formulation本身有价值。
2. 提出composition gap概念——independent optimization of K and d vs joint optimization的accuracy差距在medium-difficulty regime最大。这是一个可验证的structural prediction。
3. Difficulty-conditioned routing over a verifier hierarchy——从latent-ORM到GenRM的4-tier hierarchy，per-instance选择最优(K,d)组合。
4. 极其完备的实验方案——从Phase 0 pilot到完整ablation，包含了几乎所有可能被reviewer要求的分析。

贡献的核心价值：中等偏上。(K,d)联合优化的gap确实存在且被系统性忽视，但贡献本质是"更好的组合策略"而非"新方法"。如果composition gap empirically显著，价值会上升；如果marginal，价值有限。

【方法合理性】: 
方法在技术上是合理的。DTR→difficulty estimation→(K,d) routing是自然的pipeline。UCB bandit refinement有理论基础。4-tier verifier hierarchy的cost structure是realistic的（latent-ORM ~2% of c_g, GenRM ~76× of c_g）。

**更简单的替代方案风险**：Grid-Search-(K,d)-per-bucket（per difficulty tercile的static lookup）是一个非常强的trivial baseline。Proposal承认了这一点并给出了三个反驳论证（continuous difficulty, domain-specific factors, distribution shift），但这些论证偏理论化，需要empirical验证。如果grid-search baseline在MATH-500上只差1-2%，continuous routing的复杂性难以justify。

DTR dependency是另一个concern——DTR在≤14B模型上未验证，fallback signals（logit entropy, SC agreement）可能显著弱于DTR。如果fallback signal只有r~0.4-0.5，routing quality会大幅下降。不过proposal设计了Phase 0来explicitly验证这一点，并设定了r≥0.6的proceed threshold，这是负责任的设计。

方法本身没有致命缺陷，但其有效性高度依赖于：(1) difficulty signal的质量，(2) composition gap的实际大小，(3) grid-search baseline的competitiveness。

【5 维度打分】:
  1. 研究问题: [强] — (K,d)联合优化的gap在文献中确实系统性未被addressed。Variation in Verification (ICLR 2026)揭示了heterogeneous reliability，Montgomery et al.证明了hybrid verification的价值，Strategic Scaling bandit证明了adaptive K的价值，但没有work将这些dimension joint起来。问题重要性和timeliness都很好。唯一的minor concern是这个问题是否"足够大"——如果composition gap只有1-2%，研究问题的significance就打折扣。
  
  2. 方法与创新: [中] — 方法在技术上合理，(K,d) formulation清晰，UCB+DTR pipeline自然。但创新主要在formulation和组合层面，没有新的verification method、新的training paradigm或新的theoretical result。与Strategic Scaling bandit (Zuo et al.)相比，增量是加了d维度；与Montgomery et al.相比，增量是per-instance conditioning。每个增量都合理但不transformative。Grid-search baseline的潜在competitiveness进一步压缩了novelty空间。AVA (OpenReview 2026)在multi-dimensional allocation上也做了类似的工作，虽然机制不同，但narrative上有overlap。
  
  3. 实验设计: [强] — 这可能是proposal最突出的优势。8个compute-matched baselines（覆盖了所有主要competing approaches），6个ablation configurations（完整分离K/d/router各component的贡献），8个log-spaced budget levels，多benchmark（MATH-500/AIME25/GPQA），多model scale（8B/14B/32B，optional 671B），Phase 0 pilot验证核心假设，bootstrap CI + multi-seed。特别值得肯定的：(a) composition gap的direct measurement（JOVA-full vs max(Fix-d-best, Fix-K-best)），(b) tier dropout分析（验证4-tier vs 2/3-tier的marginal value），(c) router robustness分析（simulated routing error），(d) grid-search baseline的explicit inclusion。这套实验设计在AAAI投稿中属于top-tier水平。
  
  4. 可行性: [中] — 总compute ~350-550 A100-hours，对academic lab是可承受的。所有components（DTR, LiLaVe, open-source PRMs, GenRM via self-verification）都有现成实现或straightforward复现。主要风险：(a) DTR在≤14B模型上可能失效（mitigated by Phase 0 + fallback signals），(b) verifier hierarchy可能non-monotonic（mitigated by Phase 0验证 + 声明hierarchy是hypothesis not assumption），(c) AIME25只有30题，statistical power有限（mitigated by ≥10 seeds，但仍然marginal）。时间线合理（target AAAI 2027 = Jul 28 deadline），但如果Phase 0结果不理想需要pivot，时间会紧。
  
  5. 写作与呈现: [强] — Proposal结构清晰，逻辑链完整：motivation（heterogeneous reliability + cost coupling）→ structural insight（composition gap in medium difficulty）→ method（JOVA）→ experiments。文献review非常thorough且有differentiation。Simpson's Paradox类比增强了可读性。Honest limitation acknowledgment（DTR仅验证在≥30B，hierarchy是hypothesis不是assumption）增加了可信度。技术细节（cost model C(K,d) = K·(c_g + c_v(d))，FLOPs calibration，pilot overhead inclusion in cost model）体现了严谨性。

【概率估计】: [25% - 38%] 中位 32%

【估计理由】: 
这是一篇preparation质量远高于average AAAI submission的proposal——literature coverage、experimental design、problem framing都是professional级别的。研究问题genuine且timely，gap identification成立。实验设计的completeness本身是significant加分项。

然而，以下因素压制了概率上限：
(1) **Novelty concern**：核心贡献是routing/scheduling over existing components，没有new method或new model。一个tough reviewer（尤其是方法论导向的）可能给"limited novelty"。在AAAI这种large venue，novelty bar比workshop高但比ICML/NeurIPS稍低，这有一定buffer。
(2) **Empirical risk**：composition gap的实际大小未知。如果grid-search per-bucket baseline已经capture了80%+的joint optimization gain，JOVA的learned routing marginal value变小，paper的story会被削弱。
(3) **领域拥挤**：Test-time compute allocation是2025-2026最热门的方向之一，AVA、CPO、Strategic Scaling等多个concurrent work在抢占类似的narrative space。reviewer可能因为"yet another adaptive allocation paper"而打低分。
(4) **执行依赖**：DTR在target model scale上的有效性、verifier hierarchy的实际shape都是unknowns。Phase 0设计虽好，但如果结果不理想，pivot成本高。

综合来看，32%中位数反映了"solid preparation + clear gap + strong experiment design"vs "novelty concern + empirical uncertainty + crowded field"的balance。如果empirical results strong（composition gap >3%, JOVA大幅超越grid-search），可以push到40%+区间。

【主要风险】: 
1. **Composition gap可能很小**：如果independently optimizing K and d只比jointly优化差1-2%，整篇论文的核心contribution被undermined。Grid-search per-bucket baseline可能surprisingly competitive，让learned routing的marginal value不足以justify complexity。这是最可能导致reject的风险。
2. **Novelty perceived as incremental**：Reviewer可能认为"routing over existing verifiers conditioned on difficulty"是一个engineering contribution而非scientific contribution，尤其在concurrent work（AVA、CPO、Strategic Scaling）已经占据了adaptive allocation narrative的背景下。即使gap identification正确，"just putting existing pieces together"的perception可能导致borderline reject。

【实施评估】:
  - 计算资源: ~350-550 A100-hours，对有GPU集群access的academic lab可行。Phase 0 pilot (~50h)可快速验证核心假设，降低sunk cost风险。
  - 数据需求: 使用公开benchmark（MATH-500, AIME25, GPQA-Diamond），无custom数据集需求。所有verifier模型均为open-source（InternLM2-7B-Reward, Skywork-o1-Open-PRM等）。
  - 人工介入: 无human annotation需求。需要moderate engineering effort搭建multi-verifier pipeline、DTR extraction、UCB bandit training。
  - 训练需求: 极少。LiLaVe需训练XGBoost（trivial）。UCB bandit需在validation split上pre-train（lightweight）。无LLM fine-tuning。
  - 新 Benchmark: 不需要。使用现有established benchmarks。
  - 预估周期: Phase 0 (1-2周) + Phase 1 (2-3周) + Phase 2 (2-3周) + Phase 3 (1-2周) + 写作 (2-3周) ≈ 8-13周。对AAAI 2027 (Jul 28 deadline) timeline充裕。
```

Sources:
- [Variation in Verification (arXiv 2509.17995)](https://arxiv.org/abs/2509.17995)
- [Strategic Scaling of Test-Time Compute: A Bandit Learning Approach (arXiv 2506.12721)](https://arxiv.org/abs/2506.12721)
- [Budget-aware Test-time Scaling via Discriminative Verification (arXiv 2510.14913)](https://arxiv.org/abs/2510.14913)
- [AVA: Anytime Verified Agents (OpenReview 2026)](https://openreview.net/forum?id=JMDCMf7mlF)
- [GenPRM: Scaling Test-Time Compute of Process Reward Models (AAAI 2026)](https://github.com/RyanLiu112/GenPRM)
- [DiffAdapt: Difficulty-Adaptive Reasoning (ICLR 2026)](https://arxiv.org/pdf/2510.19669)
- [Think Deep, Not Just Long: DTR via Deep-Thinking Tokens (arXiv 2602.13517)](https://arxiv.org/abs/2602.13517)
- [LiLaVe: Lightweight Latent Verifiers (arXiv 2504.16760)](https://arxiv.org/abs/2504.16760)
- [Multi-Agent Verification: BoN-MAV (arXiv 2502.20379)](https://arxiv.org/pdf/2502.20379)
- [FlexiVe/SDV (arXiv 2505.11966)](https://arxiv.org/pdf/2505.11966)
- [Adaptive TTC via Constrained Policy Optimization (arXiv 2604.14853)](https://arxiv.org/abs/2604.14853)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "134b831d-2e04-469b-8ff3-026800f6d3e4",
  "isSidechain": false,
  "requestId": "req_011CbWRCR1LL9NxCqU1vBLc7",
  "type": "assistant",
  "uuid": "a1b9a5c5-83c4-4e71-bafe-18356a5d9e70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VV6CzRjCBJqjfHmM3DGqmt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1790,
      "cache_read_input_tokens": 25758,
      "output_tokens": 5754,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5754,
          "cache_read_input_tokens": 25758,
          "cache_creation_input_tokens": 1790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1790
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

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Difficulty-Adaptive Joint Generation-Verification Compute Allocation for LLM Reasoning  ## Core Problem and Moti…",
  "leafUuid": "a1b9a5c5-83c4-4e71-bafe-18356a5d9e70",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate difficulty-adaptive verification type selection proposal",
  "sessionId": "35379f54-0bee-4fcc-978e-25da424a7e94"
}
```

---
