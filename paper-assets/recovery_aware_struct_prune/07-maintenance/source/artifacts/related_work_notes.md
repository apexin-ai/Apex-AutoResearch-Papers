# Related Work Notes — RASP (Recovery-Aware Structured Pruning)

> Prepared 2026-05-14. Literature map: 24 papers. Target: EMNLP 2026 ARR May 25.

---

## 1. Structured Pruning for LLMs

**Core methods.** LLM-Pruner (Ma et al., 2023) established the structured pruning pipeline for LLMs: dependency-graph-based group identification → importance scoring → one-shot removal → LoRA recovery. GRASPrune [`grasprune_2026`] advances this with global gating under budget constraints, achieving SOTA at ACL 2026 — we use it as our pruning backbone. GPrune-LLM [`gprune_llm_2026`] addresses calibration bias via cross-distribution neuron behavior partitioning. DieT [`diet_2026`] proposes dimension-wise task-specific importance for width pruning at 20–40% sparsity. DDP [`ddp_2026`] introduces deterministic differentiable mask optimization, eliminating the stochastic train-test mismatch of hard-concrete relaxations. Bonsai [`bonsai_2025`] shows competitive gradient-free structured pruning.

**Pruning for reasoning models.** RESP [`resp_2025`] achieves GSM8K 81.3% at 40% structured sparsity via self-reflective importance, but applies no post-pruning recovery. From LLMs to LRMs [`from_llms_to_lrms_2026`] demonstrates that width pruning preserves reasoning better than depth pruning — motivating our width-level focus. Doing More With Less [`doing_more_with_less_2026`] shows that structured pruning significantly degrades test-time scaling (TTS) performance while unstructured pruning can augment it, directly motivating why structured pruning needs a recovery mechanism.

**Usable claims:**
- Structured pruning degrades reasoning more than general NLP tasks → [`doing_more_with_less_2026`, `resp_2025`]
- Width pruning > depth pruning for reasoning preservation → [`from_llms_to_lrms_2026`]
- Global importance scoring outperforms local → [`grasprune_2026`, `gprune_llm_2026`]
- Current methods lack recovery-awareness in the pruning decision itself → gap we fill

---

## 2. Post-Pruning Recovery

**RLVR recovery.** Self-Healing [`self_healing_2025`] is our primary baseline: RLVR recovers 95%+ reasoning at 25% compression where SFT only reaches ~80%. This is the first work to apply RL-based recovery to pruned reasoning models, but it operates at a single sparsity ratio without predicting recoverability.

**Alternative recovery strategies.** RAC [`rac_2025`] reconstructs chain-of-thought for pruned reasoning models (NeurIPS 2025), showing CoT-targeted recovery works for unstructured/2:4 sparsity. PASER [`paser_2025`] demonstrates that selective training data improves recovery efficiency. PAT [`pat_2025`] co-optimizes pruning mask and fine-tuning jointly (AAAI 2025). The VLM pruning study [`pruning_vlm_recovery_2026`] finds that width pruning + KD recovery outperforms layer pruning + SFT, validating our paradigm choice.

**Scaling and theory.** P² Law [`p2_law_2025`] establishes predictable scaling for recovery compute/data (ACL 2025) — we extend this to RLVR-specific scaling. RL Squeezes, SFT Expands [`rl_squeezes_2026`] (ICLR 2026) provides the theoretical basis: RLVR compresses representations while SFT expands them, explaining why RLVR is the superior recovery mechanism post-pruning.

**Task-specific neuron dynamics.** Task-specific neuron analysis [`task_neurons_2026`] finds that removing just ~10% of task-critical neurons causes complete performance collapse, with a robustness threshold at 15–20%. Fine-tuning substantially recovers performance across pruning levels — supporting the need for recovery-aware pruning that identifies which neurons are critical.

**Usable claims:**
- RLVR >> SFT for post-pruning recovery → [`self_healing_2025`]
- RLVR compresses representations (theoretical justification) → [`rl_squeezes_2026`]
- Recovery compute follows scaling laws → [`p2_law_2025`]
- Task-specific neurons exist; small removal causes collapse → [`task_neurons_2026`]
- No prior work predicts recoverability before pruning → gap we fill

---

## 3. CKA in Neural Networks

**Layer-level CKA for pruning.** MPruner [`mpruner_2024`] uses CKA similarity between consecutive layers to identify redundant layers for removal, achieving 50% parameter reduction with minimal accuracy loss. Lachance's thesis [`lachance_thesis_2024`] provides theoretical grounding that CKA layer similarity correlates with pruning recoverability. MIPP [`mipp_2024`] uses mutual information (related to CKA) as a pruning criterion.

**Our extension.** We adapt CKA from layer-level redundancy detection to width-level functional overlap prediction. Specifically, we compute CKA between pre- and post-pruning intermediate representations to predict whether RLVR can recover the pruned model — a novel application of CKA as a recoverability signal rather than an importance signal.

**Usable claims:**
- CKA identifies redundant layers → [`mpruner_2024`]
- CKA correlates with recoverability → [`lachance_thesis_2024`]
- No prior work uses CKA for width-level recoverability prediction → our contribution

---

## 4. RLVR / Reasoning Enhancement

**RLVR foundations.** RL Squeezes [`rl_squeezes_2026`] shows RLVR and SFT have fundamentally different mechanisms (compression vs expansion). Self-Distilled RLVR [`self_distilled_rlvr_2026`] improves RLVR training stability and sample efficiency via self-distillation. OPSD [`opsd_2026`] compresses post-RL models via one-shot structured distillation — a complementary approach to our pruning+recovery pipeline.

**RLVR training efficiency.** DPPO [`dppo_2026`] achieves 2.37× GRPO speedup via importance-sampling-based rollout pruning while preserving unbiased gradients. ARRoL [`arrol_2026`] uses a lightweight quality head to predict and prune low-value rollouts during RLVR generation. Both are complementary to our work — they could accelerate the GRPO recovery phase in RASP.

**Usable claims:**
- RLVR compresses while SFT expands → [`rl_squeezes_2026`]
- GRPO training can be accelerated 2× without accuracy loss → [`dppo_2026`, `arrol_2026`]
- Post-RL distillation is complementary to pruning+recovery → [`opsd_2026`]

---

## 5. Our Positioning: RASP Fills the Gap

### Gap analysis

The literature reveals a clear gap at the intersection of three directions:

1. **Structured pruning for LLMs** is mature (GRASPrune, GPrune-LLM, Bonsai, DDP) but no method accounts for post-pruning recoverability when making pruning decisions.
2. **Post-pruning recovery** via RLVR is demonstrated (Self-Healing) but operates as a black-box second stage — the pruning step is unaware of whether the removed structures can be recovered.
3. **CKA-based analysis** has been applied to layer-level redundancy (MPruner) but never to predict width-level recoverability under RLVR.

### RASP's contribution

RASP bridges these three threads by introducing CKA functional overlap as a predictive signal for RLVR recoverability. Concretely:

- **Before pruning:** We compute CKA overlap between candidate pruning configurations and the full model to estimate how much functional capacity is preserved. High CKA overlap → the pruned model retains the representational substrate that RLVR can rebuild upon.
- **During pruning:** CKA scores guide which structures to remove, preferring configurations that maximize predicted recoverability at the target sparsity ratio.
- **After pruning:** RLVR (specifically GRPO) recovers reasoning capability, and we show that CKA-guided pruning requires less recovery compute than importance-only pruning.

This is distinct from: (a) Self-Healing, which uses RLVR recovery but with standard importance-based pruning; (b) RESP/GRASPrune, which optimize pruning quality without considering recovery; (c) MPruner, which uses CKA for layer redundancy, not width-level recoverability.

### Narrative for Related Work section

We position RASP as the first method to close the loop between pruning and recovery by making the pruning decision recovery-aware. While prior work treats pruning and recovery as independent stages (prune first, recover later), RASP shows that predicting recoverability — via CKA functional overlap — at the pruning stage yields better final accuracy at the same sparsity ratio and recovery budget. This is analogous to how PAT co-optimizes pruning and tuning, but RASP operates at a higher level: it does not require joint optimization, instead using CKA as a cheap predictive proxy that can be computed before any training begins.
