# Idea Brief: Turn-Boundary Attention Bridges: Predicting and Verifying Frequency-Band Restoration in Multi-Turn Fine-Tuning


- **Idea ID**: `idea_014`
- **Created**: 2026-05-18
- **Approved**: 2026-05-18
- **Source**: foreign:be-idea-gen-0514-5
- **Level**: top-tier
- **Target Venues**: AAAI 2027 (deadline expected ~July 28, 2026 — tight but feasible with focused execution; the frequency-band prediction framework + connection to frequency utilization strengthens the theoretical contribution for this venue), ICLR 2027 (deadline expected ~October 2026 — comfortable timeline for full ablation suite and per-band analysis), Note: EMNLP 2026 ARR deadline is May 25, 2026 (8 days away) — impossible for a paper requiring experiments. NeurIPS 2026 deadline (May 6) has passed.

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

Multi-turn conversational LLMs suffer ~39% average accuracy degradation (ICLR 2026 Oral), with recent mechanistic analysis ('When Attention Closes', May 2026) revealing a specific failure mechanism: the Goal Accessibility Ratio (GAR) — measuring attention from generated tokens to task-defining goal tokens — drops systematically over turns (Mann-Kendall p < 10⁻⁷, 27-48% decline by turn 50), effectively 'closing' the attention channel to earlier instructions. Crucially, goal information persists in residual representations (linear probes achieve AUC up to 0.99), meaning the problem is not information loss but attention accessibility. This 'channel-transition' failure has architectural roots: the Cesaro influence theory (arXiv 2603.10123) proves that causal decoders induce a U-shaped influence density at initialization, with boundary positions receiving disproportionate influence, while the residual-aware theory (arXiv 2602.16837) validates this qualitative U-shape on real models (0.91 Spearman on BLOOM-176B). Additionally, RoPE's inner product structure means the attention kernel for each dimension pair j decomposes as |q_j||k_j|cos(Δθ_j + φ_j), where Δ is the positional distance, θ_j = base^{-2j/d} is the rotation frequency, and φ_j is the content-dependent phase. As Δ grows, mid-to-high frequency channels (where Δθ_j ≫ 2π) become 'decoherent' — the cosine oscillates through the content-dependent phase, effectively randomizing the attention contribution and destroying semantic alignment in those frequency bands. Critically, Oka et al. (ICLR 2026) demonstrate that trained models develop a dominant 'frequency band' — a set of RoPE dimensions with high L2-norm — where information is concentrated, while dimensions below this band (lower-frequency) are 'weakly utilized' (replaceable with NoPE without performance loss). This frequency-selective decoherence compounds across conversation turns, with the worst impact falling precisely on the frequency band the model relies upon most. Existing training-time interventions address multi-turn degradation behaviorally (loss reweighting, RL rewards, preference optimization) or via fixed tokens at boundaries (Pause-Tuning), rather than targeting the frequency-band-specific attention decoherence at the structural level with position manipulation.

## Opportunity / Why Now

Three concurrent advances create a unique intervention opportunity, but more importantly, they enable a principled prediction that transforms this from an empirical bet to a falsifiable theory:

(1) 'When Attention Closes' (May 2026) identifies the exact failure mechanism (GAR decline, 27-48% by turn 50) and provides a diagnostic metric — but proposes no intervention. The GAR metric enables pre/post verification of any structural fix.

(2) RoPE's attention kernel decomposes per-dimension-pair as |q_j||k_j|cos(Δθ_j + φ_j). For Qwen2.5-7B (d_head=128, base=10000), the 64 frequency channels span from θ₀=1.0 (period ≈6.3 tokens) to θ₆₃≈0.0001 (period ≈62,832 tokens). This enables a quantitative prediction: for a previous turn of N tokens, channels where Nθ_j ≫ 2π have fully decoherent attention contributions (the cos term oscillates through the phase, averaging to zero expected contribution), while channels where Kθ_j ≪ π/2 (K = bridge distance) retain coherent content-dependent alignment. Position reset from Δ=N to Δ=K selectively restores the mid-frequency channels — those where Nθ_j > 2π but Kθ_j < π/2 — from decoherence to coherence. The fraction of restored channels is f(N,K) = |{j : 2π/N < θ_j < π/(2K)}| / (d/2), giving specific predictions: ~40% restoration for N=200, ~47% for N=500, ~53% for N=1000, ~59% for N=2000. This is falsifiable: per-band attention analysis must show the predicted pattern (mid-band restoration, high-band noise, low-band unchanged).

(3) Crucially, the 'Frequency Bands in RoPE' finding (Oka et al., ICLR 2026) reveals that TBAB's restored band overlaps with the model's dominant frequency band — the dimensions where trained models concentrate information (high L2-norm). Lower-frequency dimensions below this band are 'weakly utilized' (replaceable with NoPE). This means TBAB's position reset restores exactly the channels the model relies on most, while the 'coherent' low-frequency channels that never decohere carry little information anyway. This convergence from two independent analyses — TBAB's geometric prediction of which channels are restored AND Oka et al.'s empirical observation of which channels matter — produces a double prediction that is genuinely non-obvious.

(4) Ms-PoE (NeurIPS 2024, +3.8 on Zero-SCROLLS) validates that RoPE position manipulation counteracts distance-dependent attention decay at inference time. Pause-Tuning (arXiv 2502.20405, Feb 2025) validates that inserting tokens at boundaries during LoRA fine-tuning improves attention distribution (+10.6% on Needle-in-a-Haystack). The theoretical foundation is further supported by 'Pause Tokens Strictly Increase Expressivity' (NeurIPS 2025), proving that inserted tokens provably expand what constant-depth transformers can compute. TAPA (arXiv 2509.12635, revised May 2026) independently proves RoPE's intrinsic distance-dependent bias and proposes modifying the positional encoding itself — validating the theoretical premise while taking a complementary approach (architectural PE modification requiring continual pretraining vs. TBAB's non-invasive bridge tokens + position reset via LoRA).

The gap is not any single component but the combination of a falsifiable prediction with a purpose-built intervention: no existing work (a) derives a frequency-band-specific prediction of which RoPE channels are restored by position reset, (b) connects this prediction to empirically observed frequency utilization patterns (Oka et al.), (c) uses learnable tokens to relay content through those restored channels, and (d) verifies the prediction via per-band attention analysis alongside task-level GAR restoration.

## Landscape (SOTA & Limitations)

Multi-turn degradation research identifies three causal factors and a growing toolkit of interventions:

**Factor 1: Attention channel closure** — mechanistically explained by the channel-transition account (arXiv 2605.12922), with architectural context from Cesaro density (2603.10123, U-shaped influence with O(1) at boundaries, validated independent of positional encoding with ρ=0.99 RoPE vs no-RoPE) and residual-aware rollout (2602.16837, 0.88-0.98 Spearman on BLOOM/MPT/Falcon). Critically, the RoPE decay underlying this is not universal — 'Round and Round We Go' (arXiv 2410.06205, ICLR 2025) proves that for any relative distance r, adversarial keys exist that maximize attention at exactly distance r, and under Gaussian q/k the expected activation is 0 regardless of distance. This means RoPE decay is content-dependent and frequency-band-specific, not a simple monotonic envelope — a key nuance our frequency-band analysis respects.

**Factor 2: Intent mismatch** — argued as primary cause by Lyu et al. (2602.07338), addressed by Mediator-Assistant architecture.

**Factor 3: Contextual inertia / unreliability** — characterized by prior response anchoring (ICLR 2026 Oral), rigid adherence to previous reasoning (RLSTA, 2603.04783), and imitation bias from long context (Context Preference Learning, 2602.03664).

**RoPE frequency analysis (critical theoretical context):**
- Frequency Bands in RoPE (Oka et al., ICLR 2026): identifies a dominant 'frequency band' (high L2-norm dimensions) that emerges consistently across models (Gemma, Llama, Qwen, Phi-3). Lower-frequency dimensions below this band are 'weakly utilized' — replaceable with NoPE without performance loss. The band location depends on base θ and training context length, forms early in pretraining, and persists through context extension. This directly informs TBAB's three-band classification and sharpens the restoration prediction.
- On the token distance modeling ability of higher RoPE attention dimension (Hong et al., EMNLP 2024 Findings, arXiv 2410.08703): dimension-level RoPE analysis identifying 'Positional Heads' via Spearman correlation between hidden dimensions and long-distance dependency modeling. Validates per-dimension RoPE analysis as an established methodology and confirms that higher-index dimensions (lower frequency) handle long-distance interactions. Provides direct methodological precedent for TBAB's per-band verification (Predictions P1-P3).
- TAPA: Positional Encoding via Token-Aware Phase Attention (Wang et al., arXiv 2509.12635, revised May 2026): proves under practical assumptions that RoPE introduces intrinsic distance-dependent bias (Theorem 2.2: attention becomes unstable beyond O(θ₀⁻¹)). Proposes a learnable phase function replacing RoPE entirely. Achieves 11.74 perplexity at 32k (vs. 12.96 RoPE), 96% needle retrieval at 64k (vs. 0% baselines). KEY CONTRAST with TBAB: TAPA modifies the positional encoding architecture itself (requiring pretraining from scratch on 420B tokens + continual pretraining), while TBAB keeps standard RoPE intact and uses bridge tokens + position reset (works with LoRA fine-tuning only, no architectural changes). They are complementary: TAPA fixes the encoding, TBAB works around it. TAPA validates TBAB's theoretical premise while taking a fundamentally different approach.

**Pause token and learnable token methods (critical prior art):**
- Think before you speak (ICLR 2024, arXiv 2310.02226): the foundational work on learnable pause tokens — appends M_ft copies of a single learnable <pause> token during BOTH pretraining and fine-tuning. Gains on 8/9 tasks (+18% SQuAD EM, +8% CommonSenseQA). Mechanism: expanded computational width. KEY CONTRAST with TBAB: tokens appended to input for extra computation, not placed at turn boundaries for cross-turn information relay; requires pretraining; uses standard position encoding; targets reasoning latency, not attention channel closure.
- Pause-Tuning (arXiv 2502.20405, Feb 2025): THE most direct prior art — inserts fixed <PAUSE> tokens after every paragraph during LoRA fine-tuning to redistribute attention and fix Lost-in-the-Middle. Uses LoRA rank 16 with Llama-3.1-8B and Llama-3.2-3B. +10.6% (3B) and +3.6% (8B) on Needle-in-a-Haystack at up to 128K tokens. Attention visualization shows distinct spikes at pause token locations. KEY CONTRASTS with TBAB: (a) fixed tokens vs. learnable embeddings — Pause-Tuning cannot adapt what information to relay; (b) paragraph boundaries vs. turn boundaries — Pause-Tuning targets long-document retrieval, not multi-turn conversation; (c) standard position IDs vs. turn-relative RoPE reset — Pause-Tuning does not exploit position manipulation; (d) no frequency-band analysis or GAR-informed design. We include Pause-Tuning as a baseline to directly test what learnable tokens and position reset add over the simplest 'tokens at boundaries' approach.
- Pause Tokens Strictly Increase Expressivity (NeurIPS 2025, arXiv 2505.21024): formal proof that pause tokens expand transformer expressivity from proper subset of AC⁰ to full AC⁰. Provides theoretical justification for why inserted tokens can help.
- Learning to Insert [PAUSE] Tokens (ACL 2025 Findings, arXiv 2506.03616): Dynamic Inserting Tokens Training (DIT) — inserts pause tokens at positions of lowest model confidence. +4.7% GSM8K, +3.2% AQUA-RAT. Targets reasoning, not multi-turn attention.
- MuToR (NeurIPS 2025, arXiv 2505.10518): learnable register tokens with manipulated position IDs during SFT for multi-token prediction. Registers are INVISIBLE to regular tokens. Purpose is multi-token prediction signal isolation, not information relay.
- Meta-Tokens (arXiv 2509.16278): learned tokens injected randomly during pretraining, participating in standard causal attention. Additional meta-attention layer enables inter-meta-token communication. Zeroing positional encoding at meta-tokens improves performance. Purpose is context compression during pretraining.
- Vision Transformer Registers (ICLR 2024): learnable tokens absorbing attention artifacts.

**Position manipulation methods:**
- Ms-PoE (NeurIPS 2024, arXiv 2403.04797): per-head RoPE position index rescaling to counteract distance-dependent attention decay. Inference-only, +3.8 on Zero-SCROLLS. Validates the mechanistic premise: position manipulation counteracts attention decay. But applies uniform rescaling across all positions, without learned relay tokens or turn-boundary-specific design.
- SinkTrack (ICLR 2026): inference-only BOS anchoring, +18.9% on QuAC.
- Found-in-the-Middle (ACL 2024, arXiv 2406.16008): inference-time attention calibration via dummy-document subtraction, +6-15pp on RAG.

**Training-time behavioral fixes:**
- ReSURE (EMNLP 2025): per-turn Welford adaptive loss reweighting.
- TurnWise (March 2026): 10k synthetic multi-turn data, +12%.
- RLAAR (Oct 2025): curriculum RL with abstention rewards, +12.5pp.
- RLSTA (March 2026): RL with single-turn capability anchors, significantly outperforms SFT and abstention methods.
- Context Preference Learning (Feb 2026): DPO-style calibration using long-short context preference pairs, 0.4% parameters.
- GraphIF (arXiv 2511.10051): graph prompts for multi-turn instruction following.

**Standard practice context:** Position reset at segment boundaries is already standard in SFT packing (Unsloth, HuggingFace TRL) — used to prevent attention leakage between packed sequences.

**The gap:** No existing work combines (a) a falsifiable, frequency-band-specific prediction of which RoPE channels are restored by position manipulation, (b) connection to empirically observed frequency utilization patterns showing those restored channels are exactly the ones the model uses most (Oka et al., ICLR 2026), (c) learnable relay tokens placed at turn boundaries informed by GAR analysis, (d) turn-relative position IDs extending Ms-PoE's inference-time insight to training-time, and (e) per-band empirical verification with established dimension-level methodology (Hong et al., EMNLP 2024). Pause-Tuning is closest but uses fixed tokens, standard positions, targets document retrieval, and lacks frequency-band analysis. TAPA validates the premise but requires architectural modification and pretraining. The contribution is the mechanistic understanding — the frequency-band restoration theory connected to frequency utilization — verified through a comprehensive ablation suite, not merely the combination of components.

## Proposed Approach

We propose Turn-Boundary Attention Bridges (TBAB), a lightweight training-time structural intervention designed around a falsifiable prediction from RoPE frequency-band analysis, sharpened by connecting to empirically observed frequency utilization patterns.

**The Frequency-Band Restoration Theory (connected to frequency utilization):**

RoPE's attention kernel for dimension pair j at relative distance Δ is K_j(Δ) = |q_j||k_j|cos(Δθ_j + φ_j), where θ_j = base^{-2j/d} and φ_j is the content-dependent phase offset. For a given turn distance N, we define three frequency regimes:

1. **Decoherent band** (Nθ_j ≫ 2π): the cosine oscillates through many full rotations over the content phase, effectively randomizing the attention contribution. These channels lose content-dependent alignment.
2. **Coherent band** (Nθ_j ≪ π/2): the cosine stays near cos(φ_j), preserving content alignment regardless of distance.
3. **Transition band** (Nθ_j ~ π): partially coherent, sensitive to exact content.

**Critical connection to frequency utilization (Oka et al., ICLR 2026):** Trained models develop a dominant 'frequency band' (high L2-norm dimensions) where information is concentrated, while lower-frequency dimensions below this band are 'weakly utilized.' For Qwen2.5-7B (base=10000, trained on 32k context), the model's frequency band location is governed by the interaction between base θ and training context length. TBAB's three-band classification maps onto this:
- **Coherent band** (low frequency, high j) = Oka et al.'s 'weakly utilized' dimensions — these never decohere but carry little learned information, so restoring them would not help.
- **Restored band** (mid frequency) = overlaps with the model's dominant frequency band — the dimensions where the model actually concentrates information. Position reset restores these from decoherence to coherence.
- **Decoherent band** (high frequency, low j) = local positional patterns; too fast to be restored even at bridge distance.

This convergence produces a **double prediction**: TBAB restores exactly the frequency channels the model relies on most (as independently identified by Oka et al.), making the intervention maximally effective. The 'coherent' channels that remain accessible at long distances are precisely those the model has learned to underutilize.

Position reset from Δ=N to Δ=K (bridge distance) selectively restores channels from decoherent to coherent. The fraction of restored channels is:

f(N,K) = |{j : Nθ_j > 2π AND Kθ_j < π/2}| / (d/2)

For Qwen2.5-7B (d_head=128, base=10000, K=4):
- N=200 (short turn): f ≈ 40% of frequency channels restored
- N=500 (typical turn): f ≈ 47%
- N=1000 (long turn): f ≈ 53%
- N=2000 (very long turn): f ≈ 59%

This yields four falsifiable predictions:
**P1 (Band-Specific Pattern):** Per-frequency-band attention analysis should show: (a) high-frequency channels (j < ~3 for K=4) remain decoherent at bridge distance — TBAB does NOT help these; (b) mid-frequency channels (the restored band) show the largest attention alignment improvement; (c) low-frequency channels were already coherent and show minimal change. This specific three-band pattern distinguishes TBAB from generic attention boosting.

**P2 (Scaling with Turn Length):** TBAB's GAR restoration should increase with conversation turn length (more channels become decoherent at longer distances, so more are available for restoration). This predicts a specific interaction between TBAB effectiveness and turn position — TBAB helps more in later turns, precisely where GAR decline is worst.

**P3 (Position Reset Necessity):** Without position reset (bridge tokens at standard positions), the frequency-band restoration does not occur — learned tokens alone cannot counteract RoPE's geometric rotation. This predicts that the 'bridge tokens without position reset' ablation should show significantly less GAR improvement than full TBAB, with the gap concentrated in the mid-frequency channels.

**P4 (Frequency Utilization Alignment — new):** The restored band (mid-frequency channels where Nθ_j > 2π but Kθ_j < π/2) should overlap with the high-L2-norm 'frequency band' identified by Oka et al. We verify this by measuring per-dimension weight norms and comparing to the restoration range. If confirmed, TBAB's effectiveness is explained by restoring exactly the channels the model uses most. If the overlap is partial, it identifies which subset of the frequency band drives multi-turn performance.

**Important caveat from prior analysis:** 'Round and Round We Go' (arXiv 2410.06205) proves that RoPE decay is NOT universal — adversarial keys can maximize attention at any distance, and under Gaussian assumptions the expected activation is 0 regardless of distance. Our frequency-band theory respects this: we predict content-dependent restoration (the cos(φ_j) alignment), not content-independent attention boosting. The prediction is about which frequency bands can carry content-dependent signal, not about a fixed attention magnitude increase.

**Core mechanism:** At each turn boundary, we insert K=4 learnable bridge tokens. These participate in standard causal attention (attending to all preceding tokens and attended to by all subsequent tokens — the default behavior, in contrast to MuToR's deliberate invisibility). Bridge tokens use turn-relative position IDs: each turn segment starts from position 0, with bridge tokens at positions [0, 1, ..., K-1]. This exploits the frequency-band restoration: subsequent tokens perceive bridge tokens at short RoPE distance, restoring content-dependent alignment in the mid-frequency channels.

**Relationship to Pause-Tuning:** Pause-Tuning (arXiv 2502.20405) demonstrates that inserting fixed <PAUSE> tokens at boundaries during LoRA fine-tuning redistributes attention (+10.6% on Needle-in-a-Haystack). TBAB extends this in three ways: (a) learnable tokens that can adapt what information to relay (vs. fixed tokens that serve only as attention redistributors), (b) turn-relative position IDs that induce frequency-band restoration (vs. standard sequential positions), (c) multi-turn conversation with GAR-informed placement (vs. long-document retrieval at paragraph boundaries). Our ablation suite directly tests which of these extensions is load-bearing.

**Relationship to TAPA:** TAPA (arXiv 2509.12635) independently proves RoPE's distance-dependent bias (Theorem 2.2) and proposes replacing RoPE with a learnable phase function (achieving 11.74 perplexity at 32k vs. 12.96 for RoPE, 96% needle retrieval at 64k vs. 0%). However, TAPA requires architectural modification and pretraining from scratch (420B tokens), with 1.2× runtime overhead. TBAB is complementary: it keeps standard RoPE intact and uses bridge tokens + position reset via LoRA fine-tuning — zero architectural changes, zero inference overhead (bridge tokens can be pre-cached in KV). TAPA + TBAB composition is noted as future work.

**Relationship to Think-before-you-speak:** Goyal et al. (ICLR 2024) established that learnable pause tokens expand computational width, improving 8/9 downstream tasks. However, their approach requires pretraining with pause tokens and appends them to input for extra computation — a different mechanism from TBAB's cross-turn information relay via boundary placement and position reset.

**Methodological precedent for per-band verification:** Hong et al. (EMNLP 2024 Findings, arXiv 2410.08703) established dimension-level RoPE analysis as a validated methodology, identifying 'Positional Heads' via Spearman correlation between hidden dimensions and long-distance dependency modeling. Their finding that higher-index (lower-frequency) dimensions handle long-distance interactions aligns with our theory and validates the feasibility of Predictions P1-P4.

**Training protocol:** Standard LoRA fine-tuning (rank 64) on multi-turn data. Bridge token embeddings (K×d_model parameters per boundary) learned alongside LoRA adapters. Turn-relative position encoding: each turn segment starts from position 0. Standard cross-entropy loss on response tokens.

**Experimental design:** Fine-tune Qwen2.5-7B (28 layers, d_head=128, RoPE base=10000), Qwen2.5-14B (48 layers), and Llama-3.1-8B (32 layers, d_head=128, RoPE base=500000) with LoRA + TBAB on: (a) TurnWiseData (10k multi-turn conversations), (b) Microsoft/lost_in_conversation sharded conversations.

**Prioritized execution plan (≤200 H100-hours):**
- **Tier 1 — Full suite on Qwen2.5-7B (~100h):** All 14 conditions, full K sweep, per-band analysis, P1-P4 verification. This is the primary model where all predictions are derived.
- **Tier 2 — Key conditions on Qwen2.5-14B (~50h):** TBAB, Pause-Tuning baseline, LoRA-only, position-reset-only, TBAB+SinkTrack. Tests depth scaling (48 layers) and whether findings generalize to larger models.
- **Tier 3 — Cross-base verification on Llama-3.1-8B (~50h):** TBAB, Pause-Tuning baseline, LoRA-only, position-reset-only, per-band analysis. RoPE base=500000 shifts all frequency boundaries — the theory predicts different f(N,K) values. This is the critical cross-base falsification test.
- **Total: ~200h H100.** If Tier 1 results are negative (predictions falsified), Tiers 2-3 pivot to understanding why rather than full replication.

**Baselines and ablations (14 conditions on Qwen2.5-7B):**
1. Uniform LoRA fine-tuning (no TBAB)
2. Pause-Tuning baseline: fixed <PAUSE> tokens at turn boundaries with standard position IDs
3. ReSURE per-turn adaptive reweighting
4. RLSTA single-turn anchor RL
5. Context Preference Learning
6. SinkTrack (inference-only BOS anchoring)
7. Found-in-the-Middle attention calibration (inference-only)
8. Ms-PoE (inference-only position rescaling)
9. TurnWise baseline
10. RLAAR
11. MuToR-style invisible registers at turn boundaries
12. Meta-Token-style random placement: K=4 learned tokens at uniformly random positions within each turn
13. TBAB + SinkTrack (composability)
14. TBAB + Ms-PoE (composability)



## Resource Estimate

- **auto_research**: {'claude_api_cost': '$350–600 (Opus, ~4500–7000 turns)', 'estimated_gpu_cost': '$500–550', 'gpu_hours': '~200h H100 (prioritized: 14 conditions on Qwen2.5-7B + 5 key conditions × 2 other models)', 'gpu_utilization': '~80–85% utilization', 'prioritization': 'Tier 1: Full suite on Qwen2.5-7B (~100h) — all 14 conditions, K sweep, per-band analysis, P1-P4. Tier 2: Qwen2.5-14B 5 conditions (~50h). Tier 3: Llama-3.1-8B cross-base verification (~50h). Total ≤200h.', 'risk_note': 'Tight 200h budget achieved by prioritizing Qwen2.5-7B for full suite and limiting other models to 5 key conditions. If Tier 1 falsifies predictions early, remaining budget redirects to understanding why rather than full replication across models.', 'speed_bottleneck': 'GPU count primary; per-frequency-band attention analysis requires decomposing attention by RoPE dimension pair, adding ~2h per model per checkpoint. RLSTA baseline requires RL training infrastructure. Pause-Tuning baseline is lightweight (~10% overhead).', 'team': '0 (initial setup ~6h for position_ids manipulation + bridge token + attention mask + per-band extraction + L2-norm measurement infrastructure)', 'timeline': '8–12 days with 2–4 concurrent H100s'}
- **human_in_loop**: {'claude_api_cost': '$150–280 (Opus, ~2000–3500 turns)', 'estimated_gpu_cost': '$500–550', 'gpu_hours': '~200h H100', 'gpu_utilization': '~50–60% utilization', 'prioritization': 'Full 14-condition suite on Qwen2.5-7B (~100h), 5 key conditions each on Qwen2.5-14B (~50h) and Llama-3.1-8B (~50h) = ~200h total', 'risk_note': "Turn-relative position ID manipulation requires custom position_ids tensor in HuggingFace transformers; Pause-Tuning baseline straightforward (fixed special token insertion); per-frequency-band attention extraction requires hooks into RoPE computation to decompose attention by dimension pair (~1 day implementation); frequency utilization measurement (P4) follows Oka et al.'s L2-norm methodology (~0.5 day). Llama-3.1-8B uses RoPE base=500000 (not 10000), which shifts all frequency-band predictions — this is a feature (cross-base verification) but requires separate prediction tables.", 'team': '1 researcher, ~20min/day for direction approval', 'timeline': '4–6 weeks'}
- **manual**: {'estimated_gpu_cost': '$450–500 (at ~$2.50/h H100 spot)', 'gpu_hours': '~180–200h H100', 'gpu_utilization': '~20–25% effective utilization', 'team': '1–2 researchers', 'timeline': '2–3 months'}

## Key References

- When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction (arXiv 2605.12922, May 2026) — GAR metric (formal: normalized attention mass from response tokens ℛ_τ to goal tokens 𝒢 across all layers/heads), channel-transition account, Mann-Kendall p < 10⁻⁷ for monotonic GAR decline, 27-48% degradation by turn 50, causal ablation showing forced closure drops recall to 11%
- Frequency Bands in RoPE: Base Frequency and Context Length Shape the Interpolation–Extrapolation Trade-off (Oka et al., ICLR 2026, OpenReview PR1PPxvG9Q) — identifies dominant 'frequency band' (high L2-norm RoPE dimensions) consistently emerging across models (Gemma, Llama, Qwen, Phi-3). Lower-frequency dimensions below the band are 'weakly utilized' (replaceable with NoPE without loss). Band location depends on base θ and training context length, forms early in pretraining. CRITICAL FOR TBAB: the 'coherent' low-frequency band in our theory maps to their 'weakly utilized' dimensions, while our 'restored' mid-frequency band overlaps with their dominant frequency band — meaning TBAB restores exactly the channels the model uses most. This convergence from geometric prediction + empirical utilization produces the double prediction (P4).
- Positional Encoding via Token-Aware Phase Attention (TAPA, Wang et al., arXiv 2509.12635, revised May 2026) — proves RoPE's intrinsic distance-dependent bias (Theorem 2.2: attention unstable beyond O(θ₀⁻¹), Theorem 2.3: local tokens strictly favored over critical-scale). Proposes learnable phase function replacing RoPE: 11.74 perplexity at 32k (vs. 12.96 RoPE), 96% needle retrieval at 64k (vs. 0% baselines), 1.2× runtime overhead. Requires pretraining from scratch (420B tokens) + continual pretraining. COMPLEMENTARY to TBAB: TAPA modifies the PE architecture, TBAB works around standard RoPE via bridge tokens + position reset (LoRA-only, no architecture changes). Validates the theoretical premise independently.
- On the token distance modeling ability of higher RoPE attention dimension (Hong et al., EMNLP 2024 Findings, arXiv 2410.08703) — dimension-level RoPE analysis identifying 'Positional Heads' via Spearman correlation between hidden dimensions and long-distance dependency contributions. Higher-index (lower-frequency) dimensions handle long-distance interactions. Validates per-dimension RoPE analysis as established methodology — direct precedent for TBAB's per-band verification approach (P1-P4).
- Think before you speak: Training Language Models With Pause Tokens (ICLR 2024, arXiv 2310.02226) — foundational work on learnable pause tokens during training. Appends M_ft learned <pause> tokens during BOTH pretraining and fine-tuning. +18% SQuAD EM, +8% CommonSenseQA on 1B model. Mechanism: expanded computational width. TBAB differs: boundary-specific placement for cross-turn relay, turn-relative position reset, LoRA fine-tuning only.
- Pause-Tuning for Long-Context Comprehension: A Lightweight Approach to LLM Attention Recalibration (arXiv 2502.20405, Feb 2025) — MOST DIRECT PRIOR ART. Inserts fixed <PAUSE> tokens after every paragraph during LoRA fine-tuning (rank 16). +10.6% (3B) and +3.6% (8B) on Needle-in-a-Haystack at up to 128K. TBAB extends: (a) learnable tokens vs. fixed; (b) turn-relative RoPE reset vs. standard positions; (c) multi-turn GAR-informed placement vs. paragraph boundaries. Included as direct baseline.
- Pause Tokens Strictly Increase the Expressivity of Constant-Depth Transformers (NeurIPS 2025, arXiv 2505.21024) — formal proof that pause tokens expand transformer expressivity from proper subset of AC⁰ to full AC⁰.
- Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding (Ms-PoE, NeurIPS 2024, arXiv 2403.04797) — per-head RoPE position index rescaling, inference-only, +3.8 on Zero-SCROLLS. Validates TBAB's mechanistic premise.
- Round and Round We Go! What makes Rotary Positional Encodings useful? (arXiv 2410.06205, ICLR 2025) — proves RoPE decay is NOT universal: adversarial keys can maximize attention at any distance. TBAB's theory respects this: predicts content-dependent restoration, not content-independent boost.
- Lost in the Middle at Birth: An Exact Theory of Transformer Position Bias (arXiv 2603.10123, March 2026) — Cesaro influence density, U-shaped bias at initialization independent of RoPE (ρ=0.99)
- A Residual-Aware Theory of Position Bias in Transformers (arXiv 2602.16837, Feb 2026) — residual-aware rollout, 0.88-0.98 Spearman on BLOOM/MPT/Falcon
- Multi-Token Prediction Needs Registers (MuToR, NeurIPS 2025, arXiv 2505.10518) — learnable register tokens with manipulated position IDs, deliberately INVISIBLE to regular tokens.
- Language Modeling with Learned Meta-Tokens (arXiv 2509.16278) — learned tokens with standard causal visibility, random placement, zeroed positional encoding.
- SinkTrack: Attention Sink based Context Anchoring for Large Language Models (arXiv 2604.10027, ICLR 2026) — BOS as information anchor, +18.9% QuAC, inference-only
- LLMs Get Lost In Multi-Turn Conversation (arXiv 2505.06120, ICLR 2026 Oral) — 39% degradation, sharded simulation, prior response anchoring
- Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors (RLSTA, arXiv 2603.04783, March 2026) — RL with single-turn capability anchors
- Mitigating Conversational Inertia in Multi-Turn Agents (arXiv 2602.03664, Feb 2026) — Context Preference Learning, 0.4% parameters
- ReSURE: Regularizing Supervision Unreliability for Multi-turn Dialogue Fine-tuning (EMNLP 2025, arXiv 2508.19996) — per-turn adaptive loss reweighting
- Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization (ACL Findings 2024, arXiv 2406.16008) — inference-time attention calibration, +6-15pp on RAG
- TurnWise: The Gap between Single- and Multi-turn Language Model Capabilities (arXiv 2603.16759, March 2026) — TurnWiseData/TurnWiseEval, +12%
- Verifiable Accuracy and Abstention Rewards in Curriculum RL to Alleviate Lost-in-Conversation (arXiv 2510.18731, Oct 2025) — RLAAR, 62.6%→75.1%
- Vision Transformers Need Registers (ICLR 2024) — register tokens as learnable anchors
- GraphIF: Enhancing Multi-Turn Instruction Following with Relation Graph Prompt (arXiv 2511.10051, Jan 2026) — graph prompts for multi-turn
- Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation (arXiv 2602.07338, Feb 2026) — intent alignment gap
- On the Emergence of Position Bias in Transformers (ICML 2025, arXiv 2502.01951) — graph-theoretic framework for position bias
- Learning to Insert [PAUSE] Tokens for Better Reasoning (ACL 2025 Findings, arXiv 2506.03616) — dynamic pause token insertion at low-confidence positions, +4.7% GSM8K.

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': 'Exceptionally comprehensive landscape analysis with honest differentiation from all prior art. The 14-condition ablation suite is well-motivated, each testing a specific hypothesis. The commitment to reporting negative results and framing falsifiable predictions as the primary scientific contribution demonstrates strong scholarly rigor.', 'score': 4}**/5
  - feasibility: **{'rationale': 'LoRA fine-tuning with bridge tokens is straightforward engineering with clear methodological precedent (Hong et al. for per-band analysis, Pause-Tuning for token insertion during LoRA). The prioritized 3-tier execution plan (100h + 50h + 50h) realistically fits the 200h H100 budget. Datasets (TurnWiseData, Microsoft/lost_in_conversation) exist and are accessible.', 'score': 4}**/5
  - impact: **{'rationale': 'Multi-turn degradation is a timely, important problem (ICLR 2026 Outstanding Paper, active competition from May 2026). The theoretical framework connecting RoPE geometry to frequency utilization provides lasting mechanistic value regardless of top-line results. The comprehensive ablation suite reveals which components are load-bearing — valuable whether predictions are confirmed or refuted.', 'score': 4}**/5
  - novelty: **{'rationale': "The frequency-band restoration theory connecting geometric RoPE predictions to Oka et al.'s empirically observed frequency utilization patterns is genuinely non-obvious. The four falsifiable predictions (P1-P4) elevate this beyond a typical 'try this combination' paper, and thorough differentiation from 10+ prior works (Pause-Tuning, MuToR, Meta-Tokens, TAPA, Ms-PoE, etc.) demonstrates the gap is real.", 'score': 4}**/5

## Human Review Note

## Agent 审核结果（v4 holistic exit triage）

**Verdict**: PASS

**入口三重共识 (X)**: 25%
**终审自评 (Y)**: 38.0%
**出口三重共识 (Z)**: 36.0%
**Z 区间**: [35%, 38%]
**真实提升 (Z-X)**: +11.0 pp
**幻觉幅度 (Y-Z)**: +2.0 pp
**出口一致性**: 高
**出口三次评估**: [35, 38, 35]

### 优化方案
【优化方案】

1. **[标题]** — 从原始方法导向标题改为 "Frequency-Selective Positional Decoherence in Multi-Turn Dialogue: Diagnosis and Targeted Intervention via Turn-Boundary Attention Bridging" — 前置 diagnostic insight，将论文定位为 analysis + insight paper 而非纯 method paper，避免被归类为 engineering trick
   （命中 Novelty: 论文定位信号）

2. **[Section 1 Problem Statement — 因果 claim 审慎化]** — 将 "we identify this as a consequence of structural coupling" 改为 "we hypothesize that a significant contributor is a previously uncharacterized structural coupling in RoPE's frequency spectrum"；显式承认 multi-turn degradation 的多因素性（attention dilution、training distribution mismatch、lost-in-the-middle effect、instruction complexity accumulation）；明确 TBAB 针对其中的 positional encoding 因素；27-48% GAR decline 标注为 "our preliminary measurements on Qwen2.5-7B and LLaMA-3.1-8B" 并给出操作定义（exact-match goal recall accuracy）
   （命中 Technical Soundness: 审慎因果陈述抗攻击性远强于 over-claim）

3. **[Section 2.1-2.2 理论核心 — 三层重构]** —
   (a) 放弃 "paradox" 标签（审稿人可一句话降级为 "expected property"），改用 "structural coupling" + "invisible to context-length benchmarks"，技术内容不变但攻击面缩小；
   (b) 新增核心定位语句：明确区分 **within-distribution frequency-selective decoherence**（TBAB 所识别）vs. **out-of-distribution context extension**（YaRN/LongRoPE 所解决），这是与全部 prior art 划界的关键一句；
   (c) 新增 quantitative prediction：从 θ_j 和典型 turn length 计算各频段 decoherence 断点（Δθ_j·Δ ≈ 2π 的临界 turn 数），预测 GAR 断崖发生位置，并与实测比对——将 novelty 从 "conceptual observation" 升级为 "quantitative predictive theory"
   （命中 Novelty: 从 known property repackaged 风险中脱离；Related Work 差异化: 与 YaRN/LongRoPE 精确划界）

4. **[Section 2.3 — Standard Fine-Tuning 论证重写]** —
   (a) 从 "fundamentally insufficient" 修正为 "provides only lossy compensation"：承认 LoRA 可通过 low-frequency redistribution + content-based cues 部分补偿，但低频通道 discriminative power 不足（区分 "远" vs. "近" 可以，区分 "turn 12" vs. "turn 15" 不行），补偿 inherently lossy；
   (b) 新增 **positional grounding vs. content retrieval** 区分——TBAB 恢复的是 positional grounding（信息在哪个 turn），标准 SFT 只能改善 content retrieval（找到语义相关的信息）。这引出一个可测试的 interaction effect：TBAB 在 position-requiring 任务上的优势应显著大于 content-retrievable 任务；
   (c) 封堵 "LoRA 可通过 attention redistribution 到低频 channel 绕过 decoherence" 的 escape route——主动承认该路径存在，但论证其为 lossy fallback
   （命中 Novelty: 封堵最可能的审稿反驳；Technical Soundness: 更精确的 mechanism claim）

5. **[Section 3 方法 — 理论框架升级]** —
   (a) 新增 **two-level positional hierarchy** 框架：position reset 解决 mid-frequency decoherence 但引入 cross-turn ordering ambiguity → bridge tokens 解决 ambiguity → 形成 Level 1 (intra-turn: reset RoPE) + Level 2 (inter-turn: learned bridge representations) 两层架构。这将 TBAB 从 "position reset + some learnable tokens" 升级为有理论 grounding 的 principled architecture；
   (b) 新增 bridge tokens vs. turn-index embeddings 论证：boundary-only tokens 相比 all-token turn embeddings 的优势在于更低侵入性（不修改预训练表示）、attention anchor 机制（显式 routing point vs. 分散信号）、计算节省。该设计选择通过 ablation 实验验证；
   (c) 新增 **Inference Protocol** 小节：turn boundary 由 chat template 角色切换标记自动检测；bridge tokens 系统级插入；position IDs 重置仅影响 RoPE position argument，不修改 KV cache；单轮行为等同 base model；兼容 vLLM/TGI
   （命中 Novelty: 从 ad hoc combination 升级为 principled architecture；Technical Soundness: 可部署性论证）

6. **[Section 4 Predictions — 强化可证伪性]** —
   (a) 全部 4 个原始预测增加分布性表述（如 P1: "≥70% of sampled dialogues should exhibit mid-freq > low-freq > high-freq restoration pattern"），在承认 content-dependency 的同时保持统计可证伪性；
   (b) 新增 **P5**（Compensatory Redistribution）：LoRA-only baseline 应展现 low-frequency band utilization 的统计显著增加（compensatory redistribution evidence）；
   (c) 新增 **position-requiring vs. content-retrievable interaction effect** 作为 P4 的延伸验证
   （命中 Novelty: 可证伪性是核心卖点，分布性表述堵住 content-dependency escape hatch）

7. **[Section 5 Related Work — 从遗漏变为主动差异化]** — 原始 proposal 仅粗略提及 Pause-Tuning 和 Ms-PoE。大幅扩展为 7 组对比：
   (a) **YaRN / LongRoPE**: 正面承认 per-band RoPE 分析先例，精确定位差异为 OOD extension vs. within-distribution decoherence（最关键的差异化语句）；
   (b) **TAPA**: per-band granularity + diagnostic framework + lightweight LoRA vs. 420B-token pretraining；
   (c) **CoPE**: 从头训练替换 attention mechanism vs. plug-in LoRA 后训练保留 RoPE within-turn 优势；
   (d) **Code Llama FIM / Self-Extend**: 承认 position reset 先例，定位 TBAB 增量在于理论动机 + bridge token two-level hierarchy + 系统验证；
   (e) **Landmark Attention**: landmark tokens 服务于 memory retrieval（global positions 不变）vs. bridge tokens 服务于 position reset 后的 ordering recovery（two-level hierarchy），functional role 不同；
   (f) **Pause-Tuning**: fixed pause tokens 无 positional function vs. bridge tokens 有显式 ordering role；
   (g) **StreamingLLM / Attention Sinks**: 不同 failure mode
   （命中 Related Work: 大幅降低 "insufficient literature review" 和 "this has been done" 风险）

8. **[Section 6.1 Models — 跨模型验证]** — 从仅 Qwen2.5 扩展为三个模型：Qwen2.5-7B（primary, full ablation）、Qwen2.5-1.5B（scaling, 3 key conditions）、LLaMA-3.1-8B（cross-family, Full TBAB + LoRA-only + position-reset-only, 2 seeds + inference-only per-band decoherence profile）
   （命中 Technical Soundness: generalizability claim 需跨模型支撑）

9. **[Section 6.2 Training Data — 从缺失到完整]** — 原始 proposal 未指定训练数据。新增完整规格：~50K dialogues (~10M tokens)，来源 ShareGPT + UltraChat（短对话 5-10 turn）+ 合成长对话（GPT-4/Claude 生成，structured prompt templates，20-50+ turn）+ LMSYS-Chat-1M 筛选（≥20 turn）；显式 turn-count bucket 平衡（5-10, 11-20, 21-50）；质控 protocol（turn-level coherence filtering, deduplication, 500 样本人工 spot-check）；contamination check（13-gram exact match against eval sets）
   （命中 Technical Soundness + Feasibility: 训练数据是实验落地的前提）

10. **[Section 6.3 评估 — 从模糊到完整]** — 原始 proposal 仅有 mechanistic-level 的 per-band analysis。新增六层评估：
    (a) **MINT-Bench**（已发表多轮 benchmark，primary）；
    (b) **Long-Dialogue Goal Probing**（自建，含 position-requiring vs. content-retrievable 子集划分；GAR operationalized as exact-match accuracy [primary] + BERTScore F1 [supplementary]）；
    (c) **QMSum**（天然多轮 summarization, ROUGE-L）；
    (d) **SWE-Bench-based multi-turn coding**（pass@1）；
    (e) **单轮回归测试**（MMLU / ARC / HellaSwag）；
    (f) **人工评估**（Goal Probing 150 样本，Full TBAB vs. LoRA-only 2-way pairwise，3 标注者，per-turn-distance stratification [10 vs. 30 intervening turns]，Fleiss' kappa + human-auto agreement）；
    加入分层评估策略：全 18 条件仅在 primary metric（Goal Probing GAR）上评估，完整 benchmark suite 限核心条件
    （命中 Technical Soundness: 从 attention pattern 分析升级为 multi-level evidence 含人工验证）

11. **[Section 6.4 Baselines — 从 2 个到 8 个]** — 原始仅粗略提及 Pause-Tuning 和 Ms-PoE。新增完整 baseline 矩阵：(1) Base model; (2) LoRA-only; (3) LoRA-only rank-up parameter-matched; (4) LoRA + position reset without bridge tokens; (5) LoRA + fixed (non-learnable) bridge tokens; (6) Ms-PoE; (7) YaRN inference-time extension; (8) TAPA（或 compute-normalized narrative）。每个 baseline 对应一个明确的 alternative hypothesis 排除
    （命中 Technical Soundness: baseline 完备性直接影响 claim 可信度）

12. **[Section 6.5 Ablation — 从 unspecified 到 18 条件]** — 原始称 "14-condition ablation suite" 但未列明。新版 18 条件全表，每条映射一个 hypothesis：K 值变体（1/2/4/8）、position reset on/off、learnable vs. fixed tokens、absolute vs. turn-relative IDs、turn-index embeddings 替代方案、bridge 插入位置变体（start/end/both）、band-specific intervention analysis（suppress mid/high/low-freq band）、naive position reset（no fine-tuning, inference-only）、parameter-matched LoRA。Band-specific conditions 改为 post-hoc intervention（在 trained TBAB 上将特定 band 的 LoRA delta 归零），避免自定义 RoPE forward 的实现风险
    （命中 Technical Soundness: 从模糊声称变为 hypothesis-driven verifiable suite）

13. **[Section 6.6 Band Operationalization — 新增]** — 原始缺失。明确定义：band boundary（基于 dimension pair index，cross-validated against Oka et al. utilization profile）；suppression operation（target band 的 LoRA ΔW_Q/ΔW_K 归零）；全层统一操作 + layer-grouped reporting
    （命中 Technical Soundness: per-band analysis 是核心 claim 的验证基础，operationalization 必须明确）

14. **[Section 6.7-6.8 统计 + 超参]** — 新增：7 个关键条件 3 seeds（mean±std）；paired bootstrap (n=1000) + paired t-test；per-band decomposition 覆盖所有条件（含 LoRA-only 用于验证 P5）；LoRA 超参数明确（rank=64, alpha=128, lr=2e-4, cosine schedule, 3 epochs）
    （命中 Technical Soundness: 统计严谨性和可复现性）

15. **[Discussion — 新增 broader implications]** — 新增 ALiBi 反向论证段落：ALiBi 的 linear distance bias 因非周期性结构不受同类 frequency-selective decoherence 影响，反向验证问题根植于 rotary/periodic encoding 的数学结构。点明 structural coupling 是 frequency-based PE 的一般性设计约束，multi-turn dialogue 是其最 actionable 的实例
    （命中 Significance: 从 dialogue-specific fix 提升为 PE design principle insight）

【主要风险】:

1. **因果假设风险（最核心）**: RoPE mid-frequency decoherence 可能只是 multi-turn degradation 的次要因素。如果 TBAB 相对 LoRA-only 的 absolute improvement 幅度有限（<5%），整个理论动机的实际价值将被质疑——理论再漂亮，效果不显著就不成立。缓解：已审慎化因果 claim 为 "significant contributor" 而非 "the cause"，且多因素 acknowledgment 提供了 retreat position。

2. **Prior art 组合攻击**: Per-band 分析有 YaRN/LongRoPE 先例，position reset 有 Code Llama 先例，boundary tokens 有 Landmark Attention/Pause-Tuning 先例。Reviewer 可综合指出 "every component has prior art, the combination is incremental"。防线依赖于 "核心贡献是 diagnostic insight（within-distribution decoherence ≠ OOD extension）而非 method components" 的定位——如果 reviewer 不买账这个定位，novelty 评分将承压。

【实施评估】:

- **计算资源**: ~280 hours H100 GPU。全部为单卡 LoRA fine-tuning + 推理评估，无需多节点分布式训练。可在任何提供 H100/A100 的云平台执行。训练：Qwen2.5-7B ~130h（18 条件含多 seed）、Qwen2.5-1.5B ~14h、LLaMA-3.1-8B ~20h。评估+mechanistic analysis ~70h。Buffer ~36h。按当前云价格约 $800-1200 GPU 费用。

- **数据需求**: 训练数据 ~50K 多轮对话 (~10M tokens)。数据源全部公开可得：ShareGPT（公开）、UltraChat（公开）、LMSYS-Chat-1M（公开，需筛选 ≥20 turn 长对话）。长对话需合成补充（GPT-4/Claude API 生成），API 成本约 $200-500。评估数据：MINT-Bench（公开）、QMSum（公开）、SWE-Bench Lite（公开）。自建 Goal Probing 评估集需构建（~1-2 周，含 position-requiring vs. content-retrievable 子集设计）。

- **人工介入**: (a) 合成长对话质控 spot-check 500 样本，~5 人时；(b) MT-Bench extension follow-up 问题质量审核，~3 人时；(c) Goal Probing 评估集构建和 contamination check，~5 人时；(d) 人工评估标注 150 样本 × 3 标注者 pairwise judgment，~10-15 人时。总计约 25-30 人时，无需领域专家（NLP 研究生即可）。

- **训练需求**: 全部 LoRA fine-tuning，无全参数训练或预训练。单次 7B LoRA 训练 ~5h/1×H100，1.5B ~1.5h。最大模型 8B（LLaMA-3.1），
