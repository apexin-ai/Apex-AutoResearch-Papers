# Idea Brief: ThreadGate: Goal-Accessibility-Guided Residual Intervention for Multi-Turn Degradation


- **Idea ID**: `idea_011`
- **Created**: 2026-05-18
- **Approved**: 2026-05-18
- **Source**: foreign:be-idea-gen-0514-5
- **Level**: top-tier
- **Target Venues**: AAAI 2027 (abstract July 21, 2026; full paper July 28, 2026 — confirmed on official AAAI-27 Main Technical Track page, detailed CFP pending) — PRIMARY TARGET, 10 weeks from today, feasible with auto_research timeline, ARR August 2026 cycle (submission August 3, 2026) → EACL 2027 commitment (October 12, 2026) — BACKUP, allows additional experiments if AAAI submission reveals gaps

## Seed Topic

Target: EMNLP 2026, ARR submission. Track: Dialogue and Interactive Systems / Machine Learning for NLP.

Direction: Training-time architectural fix for multi-turn position bias ("Lost-in-Middle-Turns").
LLMs exhibit a U-shaped attention bias across conversation turns — attending to first and last
turns while systematically ignoring middle turns — causing a 39% average accuracy drop in
multi-turn settings (validated across 15+ models, 200K+ conversations, ICLR 2026 Outstanding
Paper). A March 2026 theory paper proves this bias is an inherent geometric property of causal
transformers with residual connections (Cesaro matrix structure), present at initialization
before any training occurs. The only existing training-based fix (RLAAR: curriculum RL with
abstention rewards) recovers limited performance (62.6% → 75.1%) by teaching models to
abstain, but does NOT address the architectural root cause. No method exists that directly
targets the geometric origin of the bias with a training-time intervention.

Seed Papers:
- "LLMs Get Lost In Multi-Turn Conversation" (ICLR 2026 Outstanding Paper, arXiv:2505.06120)
  — establishes the 39% drop across 6 generation tasks, 15 models, 200K conversations
- "Lost in the Middle at Birth" (arXiv:2603.10123) — proves U-shape is a geometric property
  of causal attention with residual connections (iterated Cesaro matrices), validated on
  untrained 24-layer Qwen2
- "Found in the Middle" (ACL Findings 2024, arXiv:2406.16008) — inference-time calibration
  subtracting positional bias from attention weights, recovers only ~15pp
- RLAAR (arXiv:2510.18731) — curriculum RL + abstention rewards, partial behavioral fix
- "When Attention Closes" (arXiv:2605.12922, May 2026) — latest mechanistic analysis via
  "Goal Accessibility Ratio", diagnostic only, no training fix proposed

Known Gaps:
- No training-time method targets the Cesaro matrix geometric bias directly
- RLAAR teaches abstention (behavioral workaround), doesn't fix the attention pattern itself
- "Found in the Middle" is inference-time only and designed for RAG, not multi-turn generation
- The problem is multi-causal (verbosity, premature solutions, incorrect assumptions,
  over-reliance on prior turns), but position bias is the mechanistically proven root cause
  that enables the others
- Longer context windows do NOT solve this — the bias is relative (middle of whatever
  context is present), not absolute position dependent

In-scope: Training-time interventions that directly address the geometric cause of
turn-position bias. Specifically: turn-position-aware attention regularization that penalizes
U-shaped attention patterns, modified positional encodings (RoPE variants) that counteract
the Cesaro matrix decay at turn boundaries, turn-shuffling data augmentation with
multi-turn consistency losses, attention entropy regularization that enforces more uniform
turn-level attention distribution, architectural modifications to residual connections that
break the geometric bias at initialization.

NOT in-scope: Inference-time-only methods (already done by "Found in the Middle"), pure
prompting strategies, RAG-specific solutions, single-turn improvements, methods that only
teach abstention without fixing attention patterns.

Contribution type: METHOD ONLY. Must propose a concrete training-time intervention with
theoretical motivation grounded in the Cesaro matrix analysis. The method must demonstrably
reduce the 39% multi-turn accuracy gap beyond RLAAR's recovery, AND preserve single-turn
performance (no regression on standard benchmarks).

EVAL PROTOCOL:
TRAIN on multi-turn conversation data (use the "sharded simulation" benchmark from the
ICLR 2026 paper, covering 6 task types: summarization, extraction, reasoning, coding,
math, instruction following).
EVALUATE on:
- Multi-turn accuracy recovery (primary metric: close the 39% gap)
- Comparison against RLAAR baseline (must exceed its 12.5pp recovery)
- Comparison against "Found in the Middle" inference-time calibration
- Turn-position attention entropy (measure whether U-shape is reduced)
- Single-turn preservation (MT-Bench, MMLU — must not regress)
- Ablation: regularization-only vs encoding-only vs combined
- Analysis: visualize attention patterns before/after intervention, verify
  Cesaro matrix eigenvalue structure is modified

Building blocks: Open models (Qwen2.5-7B/14B, Llama-3-8B), the ICLR 2026 paper's
evaluation framework and benchmark, positional encoding research (RoPE, ALiBi, NTK-aware
scaling), attention regularization techniques, the Cesaro matrix theoretical framework
for designing principled interventions.

HARD CONSTRAINTS:
Compute: ≤200 H100-hours total. Fine-tune from existing checkpoints — no pretraining.
Attention regularization and positional encoding modifications add minimal overhead.
Eval: Use the established "sharded simulation" benchmark (6 tasks × 5 turn depths).
Must report both multi-turn recovery AND single-turn preservation.

Look for: turn-boundary-aware RoPE modifications that reset or dampen the geometric
decay between turns, attention regularization losses derived directly from the Cesaro
matrix eigenvalue structure (targeting the specific eigenvalues that cause U-shape),
consistency training where the same information is placed at different turn positions
and the model must produce identical outputs, residual connection gating at turn
boundaries that prevents the accumulation pattern proven in "Lost in the Middle at Birth".

Avoid: pure prompting tricks, inference-time-only solutions (already exists), methods
that only work for retrieval/RAG contexts (not multi-turn generation), approaches that
teach abstention instead of fixing attention (RLAAR already does this), simple data
augmentation without theoretical grounding, methods requiring full pretraining.

IDEA GENERATION QUALITY CONSTRAINTS (hard rules from historical bad cases):

1. No strawman problems: Any claim about "current methods assume X" or "current methods
   fail at Y" MUST cite a specific paper with a specific passage as evidence. Do NOT
   fabricate mainstream assumptions from pre-training knowledge. If you cannot find paper
   evidence, the claim is invalid.

2. No observation-only ideas: "We discover that X happens" is NOT a contribution.
   Discovering a problem is not a contribution — solving it is. Output MUST include a
   complete method, not an analysis/benchmark/empirical study.

3. No mediocre methods: Your method MUST answer:
   - Core Insight: What non-obvious structural property are you exploiting?
   - Why Not Obvious: Why isn't this the first thing anyone would try?
   - Information Exploited: What do you use that a naive baseline doesn't?
   - Mechanistic Argument: Without experiments, explain from principles why this works.
   If the method can be summarized in one sentence with zero counter-intuitive content → reject.

4. No rehashing existing work: For every core technical component you propose, search with
   at least 3 different queries to confirm no directly related work exists. If you find
   1-2 papers doing similar things, you MUST explicitly state your specific differentiation.

5. No experiment-padding disguise: An idea's value is NOT in how many experiments it can run.
   Self-check with:
   - "Remove experiments test": Delete all results, keep only method description — does it
     teach the reader something non-trivial?
   - "Baseline fear test": If a trivial baseline achieves similar results tomorrow, does
     this paper still have value?
   - "Citation test": In 5 years, will people cite the numbers or the insight?
   If any test fails → the idea is garbage, start over.

6. The following method patterns are REJECTED (unless extremely strong structural justification):
   - "Add an X module" — Why this specific structure?
   - "Train on Y data" — Is data construction itself the contribution?
   - "Transfer Z from domain A to B" — What is the structural analogy between A and B?
   - "Combine P and Q" — Where is the synergy? Why isn't it just 1+1=2?
   - "Use more/bigger/stronger X" — Scaling is not a method contribution.

COMPETITION WARNING: "When Attention Closes" (May 13, 2026) shows active competition
on the mechanistic analysis side. Differentiate by focusing on the TRAINING FIX (not
just diagnosis) and by connecting directly to the Cesaro matrix theory for principled
intervention design. Speed matters.

Tag: direction=multi_turn_position_bias, contribution_type=method,
sub_direction=geometric_attention_fix, target_venues=["EMNLP 2026", "ACL 2026"].

## Core Problem

Multi-turn LLMs suffer systematic goal-instruction degradation across conversation turns. 'When Attention Closes' (arXiv 2605.12922, May 2026) mechanistically identifies that Goal Accessibility Ratio (GAR) — mean attention from response tokens to task-defining goal tokens — decays 27–48% from turn-1 levels as attention channels close at turn boundaries. The decay is steepest in the first 10 turns (pooled Mann-Kendall τ=−0.75, p=1.5×10⁻¹⁴ across 10 architectures; individual models range τ∈[−0.98, −0.19], all p<0.05) and occurs across all tested architectures. The 'Intent Mismatch' paper (Feb 2026) argues the problem is intent alignment, but GAR evidence shows structural attention closure even with unambiguous instructions. 'Mitigating Conversational Inertia' (arXiv 2602.03664, Feb 2026) identifies a complementary behavioral mechanism (diagonal self-attention causing imitation bias) and proposes Context Preference Learning — but this addresses response-level inertia, not the underlying architectural attention-channel closure to goal tokens. Data-level workarounds exist — Ghost Attention (GAtt, Llama 2) concatenates instructions to every turn during training, and RECAP ('LLMs Get Lost in Multi-Turn Conversation', ICLR 2026) summarizes accumulated context before final generation — but these succeed by keeping goal tokens in the recency window rather than fixing the underlying attention-channel closure. The architectural component is real, mechanistically proven, and currently unfixed at the structural level.

## Opportunity / Why Now

A unique gap exists: the diagnostic (GAR) is published, the mechanistic cause is identified (attention channel closure at turn boundaries), and 'Lost in the Middle at Birth' (arXiv 2603.10123, Mar 2026) provides the theoretical foundation showing this bias is an inherent geometric property of causal decoders with residual connections — yet NO targeted architectural intervention exists. Data-level approaches (GAtt, RECAP) achieve partial recovery (RECAP: +16pp on GPT-4o-mini, from 50.4% to 66.5%) but have a fundamental limitation: they work by keeping instructions in the recency window, so they fail when context budget is exhausted by repeated instructions or when conversation length exceeds the model's effective context. 'Found in the Middle' (ACL 2024) provides static inference-time calibration (~15pp recovery) but doesn't learn or adapt. LLaMA-Adapter (ICLR 2024) demonstrates post-hoc gating of frozen LLMs but uses position-agnostic zero-init gates. LoR2C (arXiv 2503.00572, Mar 2025) adapts residual connections with low-rank matrices but targets gradient vanishing, not positional degradation. 'Regularizing the Entropy Landscape of Self-Attention' (OPT-ML @ NeurIPS 2025) demonstrates learnable per-head entropy regularization with up to 20% perplexity gains, but is position-agnostic and requires training from scratch. The opportunity is a POST-HOC, lightweight, turn-boundary-CONDITIONED intervention that specifically restores GAR in already-deployed models — the first to connect the Cesaro-theoretic understanding of positional attention decay to a learnable fix targeting the exact positions where GAR collapses, complementing (not replacing) data-level workarounds.

## Landscape (SOTA & Limitations)

Ghost Attention / GAtt (Llama 2, Meta 2023): data-level augmentation concatenating system instructions to every user turn during training; maintains instruction-following for 20+ turns until context budget exhausted; does NOT fix attention-channel closure — succeeds by keeping instructions within recency window. RECAP ('LLMs Get Lost in Multi-Turn Conversation', ICLR 2026): adds a summarization turn consolidating prior context before final generation; recovers GPT-4o-mini from 50.4% to 66.5% (+16pp); still underperforms single-turn by ~10-21pp; fails when conversation exceeds context length or when degradation is structural rather than information-access. Kimi Attention Residuals (arXiv 2603.15031, Mar 2026): softmax attention over preceding layers at residual connections — position-agnostic, requires pretraining from scratch. MUDDFormer (ICML 2025): dynamic dense connections with input-dependent weights — general cross-layer flow, no turn awareness; trained from scratch at 2.8B scale. ExoFormer (arXiv 2601.08131, Jan 2026): exogenous anchor projections — cross-layer reuse, no position/turn awareness. 'Found in the Middle' (ACL Findings 2024): training-free inference-time attention calibration by subtracting positional bias — ~15pp recovery, static, doesn't adapt. LLaMA-Adapter (ICLR 2024): zero-initialized per-head gating for frozen LLMs — similar post-hoc paradigm but entirely position-agnostic; gate modulates adapted prompt injection uniformly across sequence positions. LoR2C (arXiv 2503.00572, Mar 2025): low-rank residual connection adaptation with ShareLoR2C/MergeLoR2C/InjectLoR2C variants — targets gradient vanishing and parameter efficiency, not positional or turn-aware. PAPEFT (arXiv 2404.01430, 2024): position-aware adapter for reducing positional bias in retrieval tasks — list-position bias in RAG, not multi-turn goal degradation. 'Regularizing the Entropy Landscape of Self-Attention' (OPT-ML @ NeurIPS 2025): learnable per-head entropy regularizer with head-wise strengths and softmax temperatures — up to 20% perplexity improvement on GPT-2; operates as position-agnostic entropy prior, not turn-boundary-conditioned. 'Mitigating Conversational Inertia' (arXiv 2602.03664, Feb 2026): identifies diagonal self-attention (imitation bias) as a complementary mechanism; proposes Context Preference Learning (DPO-based, 0.4% parameters, LoRA rank-16) to calibrate response preferences — addresses behavioral inertia at the response-generation level, complementary to our structural attention-channel fix at the residual-stream level. 'When Attention Closes' (arXiv 2605.12922, May 2026): mechanistic GAR diagnostic — purely diagnostic, no intervention; notes that periodic user-role goal re-injection failed to prevent degradation (Appendix H). 'Intent Mismatch' (arXiv 2602.07338, Feb 2026): argues multi-turn degradation is intent alignment; proposes Mediator-Assistant — complementary to architectural fixes. FLUID (arXiv 2605.04421, May 2026): continuous-time hyperconnections — long-range temporal modeling, not discrete turn events. 'Lost in the Middle at Birth' (arXiv 2603.10123, Mar 2026): proves U-shaped position bias is inherent in causal decoders via Cesaro matrix theory; shows influence density ρ_H(x) = Σ C(H,r)(1-α)^(H-r)α^r · (ln(1/x))^(r-1)/(r-1)! — provides our theoretical foundation for why uniform gating cannot break position-dependent decay. 'A Residual-Aware Theory of Position Bias' (arXiv 2602.16837, Feb 2026): shows residual mixing R(t) = (1-λ_t)I + λ_t A(t), and that decreasing λ_t uniformly induces recency drift but cannot target specific positions. Gated Attention (NeurIPS 2025, Qwen): per-head sigmoid gating after SDPA — input-dependent but not position-conditioned; demonstrates gating can break attention sinks but does not target turn-boundary structure. No existing work provides a learnable, post-hoc, turn-boundary-conditioned architectural intervention for pre-trained models with theoretical grounding for why turn-conditioning is structurally necessary.

## Proposed Approach

Insert lightweight ThreadGate modules at residual connections of FROZEN pre-trained LLMs. Each ThreadGate computes g_l(t) = σ(W_g · [LoRA_down(h_t); τ(t)] + b_g), where τ(t) is a learned turn-boundary distance embedding (tokens since last turn delimiter + turn index) and LoRA_down projects the hidden state to low rank (r=16). The residual becomes x_{l+1} = g_l(t)·x_l + (1-g_l(t))·f_l(x_l). Only gate parameters and a rank-16 LoRA adapter are trained (~0.3% of model parameters); the base model is frozen.

**Theoretical justification for turn-conditioning (why uniform gating provably fails):** From the Cesaro theory ('Lost in the Middle at Birth'), the influence density after H layers with residual mixing α is ρ_H(x) ∝ Σ C(H,r)α^r(1-α)^(H-r)(ln(1/x))^(r-1)/(r-1)!. A uniform gate g modifies the effective mixing: α → g·α. This scales ALL positional influences proportionally — the relative distribution I_A/I_B between any two positions is preserved under uniform gating (a monotone transformation of the Cesaro density). Formally: the residual-aware rollout P = Π_l[(1-λ_l)I + λ_l A_l]; uniform gating (λ_l → g·λ_l ∀l) preserves the eigenvector structure of P while only modifying eigenvalues — the positional bias PATTERN is invariant. To selectively restore attention at turn-boundary positions (specific rows of P), the gate must be position-conditional. Uniform gating is a rank-1 intervention in the space of positional modifications; restoring T distinct turn-boundary positions requires at minimum rank-T control. ThreadGate's turn-distance embedding τ(t) provides exactly this positional conditioning.

**Goal-token identification strategy for GAR loss:** (a) For diagnostic benchmarks ('When Attention Closes' suite): use paper's exact protocol — system prompt tokens specifying persona/rules/format as 𝒢. (b) For general multi-turn training data (ShareGPT, WildChat, UltraChat): define 𝒢 = {system prompt tokens} ∪ {first user-turn instruction tokens}. Rationale: these tokens define the conversational 'thread' that should persist; this aligns with the GAR paper's finding that goal token attention declines. (c) Efficient GAR computation during training: compute GAR only at turn-boundary positions (last token of each assistant response) attending to 𝒢, yielding O(L×H×|𝒢|) per boundary vs prohibitive O(L×H×n²) for full maps. Implemented via forward hooks on attention layers with gradient checkpointing. Estimated overhead: ~25% memory, ~15% wall-clock.

**Training objective:** Standard next-token loss L_NTP on multi-turn conversation data + auxiliary GAR-preservation loss L_GAR = Σ_τ max(0, GAR(τ-1) - GAR(τ) - ε) where ε is a small tolerance (e.g., 0.02) allowing natural minor decline. The combined loss is L = L_NTP + λ·L_GAR with λ annealed from 0→1 over warmup to avoid early instability.

**Fallback if GAR loss conflicts with NTP:** Two-stage decoupled training: (1) Train gate parameters ONLY with L_GAR (attention map supervision, frozen generation) — learns WHERE to intervene. (2) Compose with standard LoRA fine-tuning on multi-turn data — ensures generation quality. This decouples 'structural fix' from 'generation quality.'

**Models:** Qwen2.5-7B-Instruct and Qwen2.5-14B-Instruct (Apache 2.0).

**Baselines & Ablations:** (1) ThreadGate (full), (2) Uniform learned gate (same parameters, no turn-position conditioning — equivalent to post-hoc LLaMA-Adapter-style gating; tests theoretical prediction), (3) LoRA-only (same parameter budget, no gate), (4) LoR2C-style residual adaptation (position-agnostic low-rank residual), (5) Found in the Middle inference calibration, (6) PAPEFT-style position adapter, (7) CPL from 'Mitigating Conversational Inertia' (same 0.4% budget, DPO behavioral training), (8) Ghost Attention (GAtt) — data-level instruction concatenation during multi-turn fine-tuning on same training data; tests whether data-level recency tricks match structural intervention at varying conversation lengths. The CRITICAL experiments: (A) Show that baselines (2) and (4) fail to selectively improve GAR at turn boundaries while improving/degrading uniformly across positions — validating the Cesaro-theoretic prediction that uniform gating preserves relative positional distribution. (B) Show that GAtt (baseline 8) succeeds at moderate lengths (≤20 turns within context budget) but degrades when conversation length forces instructions into middle/early positions beyond the recency window, while ThreadGate maintains GAR regardless of conversation length — demonstrating that structural fixes complement data-level workarounds.

**Evaluation:** (a) GAR metric on 'When Attention Closes' diagnostic suite (exact replication), (b) MT-Bench multi-turn subset, (c) MT-Eval (4 interaction types), (d) Synthetic multi-turn needle-in-haystack with controlled turn-boundary distances, (e) RULER long-context to verify no regression, (f) WebArena/AgentBench subset (agentic multi-turn, connecting to 'Conversational Inertia' benchmarks), (g) Scaling analysis: vary conversation length from 5→50 turns to expose GAtt's context-budget failure mode vs ThreadGate's structural robustness.

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$150-250 (est. 1500-2500 turns)', 'estimated_gpu_cost': '$585-$780', 'gpu_hours': '~195h H100 (fixed rank=16 motivated by LoRA convention; 2 model sizes × 8 baselines × ~8h avg fine-tuning + layer subset selection [every-4th vs all layers] + GAR loss λ grid [0.1, 0.5, 1.0] + two-stage vs joint comparison + conversation-length scaling analysis)', 'gpu_utilization': 'High (~85%+); back-to-back runs parallelized across available GPUs', 'risk_note': 'GAR-preservation auxiliary loss may conflict with next-token loss if poorly weighted; auto-agent should monitor both loss curves, flag Pareto-suboptimal runs, and trigger two-stage fallback automatically if joint loss diverges after 500 steps', 'speed_bottleneck': 'Each 7B fine-tuning run ~4h on 4×H100; 14B runs ~8h; total serialized ~65h but parallelizable to <2.5 days. GAR extraction adds ~25% overhead per run. GAtt baseline requires standard multi-turn SFT with instruction concatenation (~4h per model).', 'team': '0 after initial setup (define configs, data pipeline, evaluation harness)', 'timeline': '10-14 days with 4-8 H100s available'}
- **human_in_loop**: {'claude_api_cost': '$80-150 (est. 600-1000 Opus turns for coding, analysis, writing)', 'estimated_gpu_cost': '$600-$800', 'gpu_hours': '~200h H100 (hyperparameter exploration on gate architecture, GAR loss weighting λ, and two-stage fallback with human checkpoints)', 'gpu_utilization': 'Moderate (~55-65%); agent pipelines with human approval on direction changes', 'risk_note': 'Turn-boundary token identification varies across chat templates (Qwen uses <|im_start|>/<|im_end|>); need careful tokenizer-specific handling. GAR loss λ annealing schedule needs tuning — monitor NTP vs GAR Pareto front.', 'team': '1 researcher, ~20min/day for experiment review', 'timeline': '3-4 weeks'}
- **manual**: {'estimated_gpu_cost': '$540-$720 at ~$3/H100-hr', 'gpu_hours': '~180h H100 (2 model sizes × 5 baseline configs × ~12h fine-tuning each + evaluation + GAR measurement)', 'gpu_utilization': 'Low (~30-40%); idle between runs during analysis and iteration', 'team': '1 researcher with multi-turn LLM and attention mechanism experience', 'timeline': '6-8 weeks'}

## Key References

- When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction (arXiv 2605.12922, May 2026) — provides GAR diagnostic and mechanistic motivation; GAR = mean attention from response to goal tokens, declines 27-48%; pooled Mann-Kendall τ=−0.75 (p=1.5×10⁻¹⁴)
- Lost in the Middle at Birth: An Exact Theory of Transformer Position Bias (arXiv 2603.10123, Mar 2026) — Cesaro matrix theory proving U-shaped bias is geometric property of causal decoder; provides our theoretical foundation for uniform gating insufficiency
- A Residual-Aware Theory of Position Bias in Transformers (arXiv 2602.16837, Feb 2026) — residual-aware rollout R(t) = (1-λ_t)I + λ_t A(t); uniform λ cannot target specific positions
- LLMs Get Lost In Multi-Turn Conversation (arXiv 2505.06120, ICLR 2026) — 39% multi-turn degradation; RECAP baseline improves GPT-4o-mini from 50.4% to 66.5% but doesn't close gap; demonstrates data-level fixes are insufficient
- Llama 2: Open Foundation and Fine-Tuned Chat Models (Meta, 2023) — introduces Ghost Attention (GAtt): instruction concatenation during training maintains following for 20+ turns until context exhausted; our data-level baseline
- Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation (arXiv 2602.07338, Feb 2026) — complementary: addresses intent ambiguity, not structural attention closure
- Mitigating Conversational Inertia in Multi-Turn Agents (arXiv 2602.03664, Feb 2026) — complementary behavioral approach: CPL with DPO (0.4% params) addresses response-level imitation bias; our work targets structural attention-channel closure
- Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization (ACL Findings 2024) — inference-time baseline; static calibration ~15pp recovery
- LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention (ICLR 2024) — post-hoc gating paradigm for frozen LLMs; position-agnostic per-head gates; our ablation baseline for uniform gating
- LoR2C: Low-Rank Residual Connection Adaptation for Parameter-Efficient Fine-Tuning (arXiv 2503.00572, Mar 2025) — low-rank residual adaptation; position-agnostic, targets gradient vanishing; structural comparison baseline
- Regularizing the Entropy Landscape of Self-Attention (OPT-ML @ NeurIPS 2025) — learnable per-head entropy regularizer with head-wise strengths; up to 20% perplexity improvement on GPT-2; position-agnostic entropy prior; precedent for learnable per-head attention modification in decoders — our work differs by conditioning on turn-boundary position rather than regularizing entropy uniformly
- Attention Residuals (arXiv 2603.15031, Kimi Team, Mar 2026) — uniform residual gating; requires pretraining from scratch
- MUDDFormer: Breaking Residual Bottlenecks via Multiway Dynamic Dense Connections (ICML 2025) — dynamic cross-layer connections; trained from scratch
- Position-Aware Parameter Efficient Fine-Tuning Approach for Reducing Positional Bias in LLMs (arXiv 2404.01430, 2024) — position-aware adapter; targets list-position bias in RAG
- Gated Attention for Large Language Models (NeurIPS 2025, Qwen) — per-head sigmoid gating after SDPA; input-dependent but not position-conditioned
- Attention Projection Mixing with Exogenous Anchors (arXiv 2601.08131, ExoFormer, Jan 2026) — cross-layer anchor reuse

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': 'Exceptionally well-specified proposal: gating formula, goal-token identification strategy, efficient GAR computation complexity, training objective with fallback, 8 baselines with clear differentiation rationale, evaluation suite covering 7 dimensions, and explicit acknowledgment of the contribution-at-risk scenario. Every reviewer question from 4 rounds is now addressed.', 'score': 5}**/5
  - feasibility: **{'rationale': '195h H100 within the 200h budget, standard LoRA-style fine-tuning of Apache-2.0 Qwen2.5-7B/14B from checkpoints. The efficient GAR computation strategy (only at turn-boundary positions) is well-designed. Two-stage fallback addresses the loss-conflict risk. Main uncertainty: the 25% memory overhead estimate for GAR extraction may be optimistic at 14B scale.', 'score': 4}**/5
  - impact: **{'rationale': 'First post-hoc architectural fix for multi-turn degradation deployable on already-serving frozen models (unlike GAtt which requires training data modification). The Cesaro-theoretic proof has independent publishable value. Practical uncertainty remains in the actual recovery margin (15-35% relative is wide), and at typical conversation lengths GAtt may suffice — but the theoretical contribution and the structural-robustness-at-scale argument are compelling.', 'score': 4}**/5
  - novelty: **{'rationale': "The formal proof that uniform gating is a rank-1 intervention preserving Cesaro eigenvector structure (while restoring T turn-boundary positions requires rank-T) is a genuine non-obvious insight. The method itself is a principled extension of the theory rather than a standalone surprising contribution, but the combination of formalism + testable prediction (uniform gates provably fail) elevates it above 'obvious extension.'", 'score': 4}**/5

## Human Review Note

## Agent 审核结果（v4 holistic exit triage）

**Verdict**: FAILED_below_36

**入口三重共识 (X)**: 27%
**终审自评 (Y)**: 37.0%
**出口三重共识 (Z)**: 33.0%
**Z 区间**: [34%, 35%]
**真实提升 (Z-X)**: +6.0 pp
**幻觉幅度 (Y-Z)**: +4.0 pp
**出口一致性**: 高
**出口三次评估**: [35, 34, 34]

### 优化方案
【优化方案】

1. **[标题 / 全局叙事]** — 从 method-centric title（"ThreadGate: ..."）改为 framework-centric title（"Structural Multi-Turn Degradation in Frozen Language Models: A Causal Framework, Theoretical Ceiling, and Position-Conditional Intervention"）。ThreadGate 降格为"存在性证明"，框架+因果+理论升为一等贡献 — [命中 Novelty: 论文 robustness 不再依赖方法效果大小；命中 Significance: 框架有独立价值]

2. **[Motivation / 第 1 节]** — 新增"Operator Gap"概念替代模糊的"frozen model constraint"。精确定义受众为"有推理时内部访问权但无法重训练的部署者"，将问题定位从"方法比较"提升为"识别并解决一个结构性部署缺口" — [命中 Significance: 明确"who cares"回答，覆盖产业绝大多数部署场景]

3. **[Research Questions / 核心逻辑链]** — 原 proposal 将"GAR decline → task degradation"作为默认前提。改为 RQ1 显式验证因果方向（attention knockout + preservation + controls），新增"GAR explanation ceiling"子问题量化框架解释边界 — [命中 Significance + Technical Soundness: 从 assumed correlation 升级为 demonstrated causation with honest boundary]

4. **[Framework / 新增章节]** — 新增 Structural vs. Information-Access 降解分类框架，含：(a) pathological vs. functional GAR decline 判定标准（不是所有 GAR 下降都是病理性的）；(b) 两类机制的交互效应讨论（正反馈环路 + 分别干预仍有效的论证）；(c) 明确的解释范围声明（不声称 exhaustive） — [命中 Novelty: 从 method paper 升级为 analysis+framework paper；命中 Significance: 框架可指导未来研究]

5. **[理论贡献]** — 原 Cesaro 证明（"uniform scaling preserves ratios"，接近 trivial）改为两层不可能性结果：(a) 形式化定理覆盖"无显式 turn-boundary 信号的 gate function"类（非仅常数 gating）；(b) 机制性解释（RoPE 位置信号深层衰减，引 Haviv et al. 2022）；(c) linear + nonlinear probing 实验验证前提；(d) 跨架构 probing（LLaMA-3-8B）验证泛化性；(e) fallback plan（若非线性 probe 不 decay，退回以实验 ceiling 为证据） — [命中 Novelty: 从 trivial observation 升级为 architecturally-grounded impossibility result]

6. **[方法论述 / ThreadGate 节]** — 新增对"为什么 residual-level 而非 attention-level"的理论论证（attention bias 无法放大已衰减信号 vs. residual gating 跨层复合）；新增对"为什么显式 τ(t) 而非依赖 h_t"的论证（probing 证明 h_t 中 turn-boundary 信号深层不足） — [命中 Novelty: 封堵 trivial alternative 质疑]

7. **[Related Work / 新增覆盖]** — 原 proposal 仅覆盖 GAtt + uniform adapters。新增：(a) Activation engineering 方向（Turner, Zou）+ 区分论证（fixed-direction 无法满足 layer/position-heterogeneous 需求）；(b) Context extension 方向（YaRN, LongRoPE）+ 区分论证（smooth decay ≠ discontinuous turn-boundary shift + 违反 frozen 约束）；(c) Positional information decay 文献（Haviv et al.） — [命中 Related Work: 预防审稿人 3 个最可能提出的"和 X 有什么区别"质疑]

8. **[Baselines / 实验设计]** — 从 3 个 baselines 扩展至 9+1 个：+Vanilla frozen, +RECAP reimplementation（含定量验证步骤）, +System prompt re-injection, +Attention logit bias, +GAR-direction activation addition, +Standard LoRA, +LoRA compute-matched, +Per-layer constant gating — [命中 Technical Soundness: 全面覆盖审稿人能想到的所有替代方案]

9. **[Ablation / 实验设计]** — 从隐式单个 ablation 扩展为完整 6 变体表（w/o τ(t), w/o GAR loss, w/o LoRA, τ(t) encoding variants, α variants），含参数量 + FLOPs 对比表 — [命中 Technical Soundness: 每个组件独立贡献可验证]

10. **[评估协议]** — (a) 新增 conversation-length scaling 实验（5/10/20/40/80 turns 梯度）含 GAR-vs-turns 曲线；(b) 新增 40-80 turn 构建方法（constraint-based incremental evaluation, 2 annotators, κ≥0.7）；(c) 新增 MMLU 单轮性能保持测试；(d) 新增推理效率评估（latency/throughput/memory）；(e) 新增 LongChat 长对话 benchmark；(f) 统计规范化（3 runs, mean±std, significance tests, 样本量明确, power analysis） — [命中 Technical Soundness: 从"insufficient evaluation"升级为"comprehensive, reproducible methodology"]

11. **[训练细节]** — 原 proposal 无训练数据说明。新增：LMSYS-Chat-1M, ≥5 turns, English, ~180K filtered, distribution statistics; GAR loss 采样计算（每 4 步, top-50% layers）以管控显存 — [命中 Technical Soundness + Reproducibility]

12. **[Limitations]** — 从无到有，明确列出 5 项限制（场景覆盖、解释 ceiling、定理条件强度、架构泛化、OOD 长度），展示学术诚实 — [命中 reviewer 印象: 诚实的 limitation 节减少 adversarial questioning]

【主要风险】

1. **不可能性定理的实际力度**：如果非线性 probing 在深层仍能高精度区分 turn boundary（>85%），定理的核心前提被削弱，理论贡献从"formally grounded impossibility"退化为"linear-complexity gating 的局部 bound + empirical ceiling evidence"。虽有 fallback plan，但审稿人可能判定理论贡献份量不足以支撑 Contribution #3 的地位。这是论文被降级至 Findings 的最大单一风险。

2. **GAR explanation ceiling 可能偏低**：如果因果验证显示 GAR 恢复仅解释 30-40% 的多轮退化（而非 60%+），整个框架的"structural degradation 是主要成因"叙事会被削弱，ThreadGate 的最大可能收益也被 cap 在较低水平。审稿人可能质疑"是否值得为 30% 的退化建立这么复杂的框架"。

【实施评估】
- **计算资源**: ~380 H100-hours 总计。需要 H100 GPU 集群（或等效 A100 × 1.5 倍时间）。可在主流云平台（AWS p5, GCP a3, Lambda Labs）完成。7B 训练每次约 35h（单节点 4×H100），14B 约 50h（单节点 8×H100 或双节点）。
- **数据需求**: LMSYS-Chat-1M（公开可得，HuggingFace 直接下载）；MT-Bench / MMLU / MT-Eval / LongChat 均为公开 benchmark；40-80 turn 评估数据需自建（LLM 生成 + 人工验证，约 200-300 条）。无需申请私有数据。
- **人工介入**: (a) 40-80 turn 评估数据的 constraint violation 标注：2 名标注者，约 200-300 条 × 5 probe points = 1000-1500 判断，预计 2-3 人日；(b) 数据质量审核（训练集 + 评估集）；(c) 定理形式化的数学审查。总人工约 5-8 人日（不含论文写作）。
- **训练需求**: 需要模型训练（ThreadGate 参数 + ablation 变体 + LoRA baselines）。模型本体 frozen（Qwen2.5-7B/14B），仅训练轻量 gating 参数（每个变体约 2-5M 额外参数）。单次 7B 训练约 35 H100-hours，非大规模训练但变体多（8 个）。
- **新 Benchmark**: 需构建一个 constraint-based incremental evaluation set（40-80 turns），约 200-300 条测试对话 + rule-based 评分器。工作量中等（数据生成自动化，验证需人工）。非独立发布级 benchmark，而是论文配套评测集。
- **预估周期**: 从启动到可投稿约 **14-18 周**。分解：理论证明 + probing 实验（3-4 周）→ 因果验证实验（2-3 周）→ ThreadGate 训练 + ablations（3-4 周，可部分并行）→ 全量评估（3-4 周）→ 论文写作 + 修改（3-4 周）。关键路径：定理证明难度不确定，可能成为 bottleneck；如果 proof 需要降级（取 fallback plan），写作方向需相应调整。EMNLP 2026 投稿 deadline（假设 2026 年 5-6 月）时间紧张但可行。



## MVP Validation Results

- **Date**: 2026-05-19
- **Hypothesis Supported**: No

### Key Metrics

Phase 1 GAR 衰减: 70.8% | 四路 GAR-ours: TG 0.487 / UG 0.492 / LO 0.486 / Base 0.011 | 四路 GAR-Dongre: TG 0.016 / UG 0.013 / LO 0.014 / Base 0.003 | 四路 PPL: TG 2.629 / UG 2.616 / LO 2.629 / Base 4.225 | 三路趋同最大差异: GAR<0.6pp, PPL<0.02 | v1-v7: 4 negative + 2 failed + 1 killed

### Summary

核心假设（residual gating 修复多轮 GAR 衰减）被系统性否定。7 个 gating variant（v1-v7，覆盖 4 种 loss 设计）全部失败或 negative。四路消融（TG/UG/LoRA-only）在 GAR-ours、GAR-Dongre、PPL 三个维度完全趋同（差异<0.6pp），gating 机制零增量。关键发现：teacher-forcing 下 GAR loss 有效（~0.49）但不迁移到自回归推理（Dongre GAR ~0.015），30x 断层确认为 teacher-forcing→generation 分布偏移。转入 Route B: negative result + mechanistic insight 论文。

### Recommendation

GO — 转入 Route B research 阶段。虽然核心假设被否定，但三个机制发现（反向 turn conditioning / NTP-GAR 梯度竞争 / teacher-forcing 分布偏移）构成独立贡献。Reviewer 估分：含 Llama-3 跨模型验证 → Findings 3.0-3.5。下一步：(1) gradient conflict + attention heatmap 分析；(2) held-out eval 数据修复；(3) Llama-3 跨模型验证（D020, ~15h GPU）；(4) 论文写作。目标 EMNLP 2026 ARR August cycle (2026-08-03)。
