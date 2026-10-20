# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-13 (UTC).** ## Original idea { "tit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/f453ff4a-d3dc-44e3-bb79-86652ba6dcdd.jsonl`
- **Structured JSON:** [`2cac86f676acee4d6355.json`](../../sessions/2c/2cac86f676acee4d6355.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T11:29:30.821Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T11:29:30.821Z",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-13 (UTC).**\n\n## Original idea\n{\n  \"title\": \"RAPID: Reducible-Loss Adaptive Prioritized Replay for VLA Imitation Learning\",\n  \"core_problem\": \"Can we improve VLA supervised fine-tuning quality — and crucially, the downstream RL post-training that depends on it — by adaptively prioritizing demonstration data based on what the evolving policy can still learn from, particularly in realistic settings where demonstration quality varies and the SFT stage serves as the critical foundation for the entire VLA training pipeline?\",\n  \"opportunity\": \"Prior work has established that excess loss relative to a reference model is a powerful signal for data selection in supervised learning (RHO-LOSS, ICML 2022), LLM pretraining (DoReMi, NeurIPS 2023; Rho-1, NeurIPS 2024), and robot imitation learning at the domain level (Re-Mix, CoRL 2024). In RL, ReLo (NeurIPS 2023) showed that computing reducible TD error using SAC's Polyak-averaged (EMA) target network avoids the failure mode of raw-loss PER (over-sampling noisy data). DS2 (ICLR 2025) demonstrated that dynamic instance-level loss-based reweighting accelerates LLM pretraining convergence with theoretical guarantees, but uses raw loss without decomposing reducible vs. irreducible components. Yet all existing applications in supervised/imitation settings use *fixed* reference models and operate at *coarse* granularity (domain-level in Re-Mix/DoReMi, token-level selection with static reference in RHO-LOSS/Rho-1). Meanwhile, all VLA demonstration curation methods (SCIZOR, CUPID, QoQ, DataMIL, RINSE, DemInf, Density-Ratio Weighted BC, Green-VLA DataQA) operate as static preprocessing — score once, filter once, train once. This ignores that the policy's learning needs change during training.\\n\\nCritically, the 'When Do Curricula Work?' (Wu et al., ICLR 2021) finding that curricula provide only marginal benefits on clean benchmarks — with apparent gains entirely explained by dynamic training set size — implies that RAPID's primary value proposition is NOT standard clean-data benchmarks (where VLAs already achieve 97%+), but rather the realistic settings of noisy/mixed-quality demonstrations and robustness under distribution shift. Recent robustness benchmarks (LIBERO-Plus, CVPR 2026; LIBERO-PRO) have exposed that high success rates on standard LIBERO mask fundamental fragility — OpenVLA-OFT drops from 97.1% to 70.0% on LIBERO-Plus.\\n\\n**The SFT→RL pipeline gap (new).** The VLA training paradigm is shifting from SFT-only to SFT→RL pipelines (SimpleVLA-RL, ICLR 2026; VLA-OPD, arXiv 2026; VLA-RFT, arXiv 2025). SimpleVLA-RL demonstrates that SFT quality is the critical determinant of RL outcomes: SFT alone accounts for 74pp of 82pp total improvement (17.3%→91.7%), and Section 6.2 shows RL completely fails (0% success) with zero SFT demonstrations. 'What Can RL Bring to VLA Generalization?' (NeurIPS 2025) shows SFT-warm-started RL converges ~50% faster than cold-start RL. Yet no existing work has studied how SFT *data quality* (as opposed to data quantity) affects downstream RL performance. This is a genuine unexplored gap: if RAPID's noise filtering during SFT produces policies that have not memorized noise, the resulting SFT checkpoint should provide a cleaner foundation for RL — faster convergence, better sample efficiency, and more robust final policies. This transforms RAPID from 'another data curation method' to 'a mechanism for improving the entire VLA training pipeline.'\\n\\nThe specific technical gap we target: no existing work applies *sample-level, continuously-adaptive* reducible-loss prioritized sampling to supervised/imitation learning. In RL, ReLo's target network serves double duty — both TD learning stability and reducible loss computation — and the EMA update schedule is dictated by RL optimization dynamics, not data quality scoring. In supervised/imitation learning, no target network naturally exists. RAPID introduces a purpose-built EMA reference model for data quality scoring, with training-horizon-aware τ calibration, multi-granularity trajectory+transition sampling, finite-T bounds proving adaptive references dominate static references at realistic training horizons, and empirical validation that RAPID-quality SFT cascades to improved RL post-training.\",\n  \"landscape\": \"**Foundational excess/reducible loss concepts:** RHO-LOSS (Mindermann et al., ICML 2022) introduced the core principle of selecting training points by their *reducible holdout loss* — the difference between the current model's loss and a small, fixed holdout-trained reference model's loss — to identify points that are 'learnable, worth learning, and not yet learnt.' This achieves 18x faster training on Clothing-1M by avoiding both noisy and already-learned data. ReLo (Sujit et al., NeurIPS 2023) adapted this principle to RL, computing reducible TD error as the difference between the online network's TD error and the Polyak-averaged (EMA) target network's TD error. Crucially, ReLo's target network is SAC's standard Polyak-averaged target (θ_target ← τ·θ_target + (1-τ)·θ_online, τ≈0.995), which already exists for TD learning stability and serves double duty for reducible loss — ReLo did not introduce an EMA reference, it repurposed an existing RL mechanism. Rho-1 (NeurIPS 2024) brought excess loss back to supervised learning for LLM pretraining, using a *fixed, separately-trained* reference model for selective token training. All three works that operate in supervised settings (RHO-LOSS, Rho-1) use static reference models.\\n\\n**Dynamic instance-level reweighting during training:** DS2 (Bajaj et al., ICLR 2025) performs dynamic, instance-level, loss-based sample reweighting during LLM pretraining. DS2 normalizes per-sample losses to [-α, α], applies transformation functions (LinUpper, Quadratic, or Extremes), and converts scores to weights via temperature-annealed softmax. DS2 provides a formal convergence framework and demonstrates significant improvements on 7B and 1.4B parameter LLMs. However, DS2 uses *raw loss* without decomposing it into reducible and irreducible components, inheriting the noise overfitting risk identified by RHO-LOSS. RAPID's reducible loss decomposition directly addresses this limitation.\\n\\n**Domain-level excess loss in data mixing:** DoReMi (Xie et al., NeurIPS 2023) uses excess loss relative to a pretrained reference model with Group DRO to optimize domain mixing weights for LLM pretraining. Re-Mix (Hejna et al., CoRL 2024, Outstanding Paper Finalist) extends this to robot imitation learning, using excess BC loss relative to a *fixed* reference model with DRO to optimize domain-level weights across heterogeneous robotics datasets (Open X-Embodiment), outperforming uniform weights by 38% and human-selected weights by 32%. Re-Mix operates at *domain level* (one weight per dataset), uses a *fixed* reference model, and employs DRO optimization — not sample-level prioritized sampling.\\n\\n**Static demonstration curation (one-shot preprocessing):** SCIZOR (ICRA 2026) removes suboptimal and redundant data via self-supervised progress prediction and clustering. CUPID (CoRL 2025) uses influence functions to rank demonstrations by estimated impact on closed-loop performance. QoQ (arXiv 2026) applies static influence-function scoring. RINSE (ICML 2025) proposes smoothness-driven metrics (Spectral Arc Length and Trajectory-Envelope Distance) for policy-architecture-agnostic demonstration scoring. DataMIL (ICLR 2026) uses a policy-driven datamodels framework for end-to-end data selection. DemInf (Hejna et al., RSS 2025) uses k-NN mutual information estimation for demonstration quality scoring. Density-Ratio Weighted BC (Pandian & Baheri, arXiv Oct 2025) uses a small clean reference set to estimate trajectory-level density ratios via a binary discriminator, downweighting corrupted data — static, requires a verified clean reference, and cannot adapt to evolving policy needs. Green-VLA (arXiv Feb 2026, 2602.00919) introduces a DataQA pipeline for VLA training data using four quality metrics (jitter, sharpness, visual diversity via DINOv3 features, proprioceptive state variance) plus optical-flow-based temporal resampling, achieving 94.6% pick success on SimplerEnv BRIDGE with 3000 hours of data. Green-VLA's DataQA is applied as static preprocessing before training. All these methods score data once before training.\\n\\n**Online/adaptive sample selection during training:** UDS (arXiv Oct 2025) performs online batch selection during LLM SFT using nuclear norm of the logits matrix to capture utility-diversity, eliminating the need for a reference model. LEAD (arXiv May 2025) introduces Instance-Level Dynamic Uncertainty (IDU), combining instantaneous loss, gradient-based loss-change approximation, and exponential smoothing of *historical loss values* for online data selection during LLM instruction tuning, achieving 6-10% improvements with 2.5% of data. Key distinction from RAPID: LEAD smooths *loss values* via EMA to reduce noise, while RAPID maintains an EMA *model* to compute reducible loss — the model-based approach decomposes genuinely learnable from irreducibly noisy data, which a single loss signal cannot. Predictive Batch Scheduling (PBS, arXiv Feb 2026) uses static features (token frequency, sequence length) for difficulty estimation during LLM pretraining.\\n\\n**Curricula effectiveness:** 'When Do Curricula Work?' (Wu et al., ICLR 2021, Oral) demonstrates through extensive experiments that curriculum/prioritized sampling provides only marginal benefits on standard benchmarks with clean data — any apparent benefit is entirely explained by dynamic training set size, not the ordering itself. Benefits emerge only under (1) limited training budget or (2) noisy data. This is a critical calibration for RAPID.\\n\\n**Adaptive weighting during training (not VLA, not imitation learning):** VACO (ICLR 2025) trains a meta-scoring network via bi-level optimization to adaptively weight BC samples in offline RL on D4RL tasks. Key differences: (1) targets offline RL with value alignment; (2) bi-level optimization is expensive; (3) low-dimensional state-action pairs.\\n\\n**Prioritized replay in RL/LLM post-training:** PER (Schaul et al. 2016) uses TD error for priority in RL. Freshness-Aware PER (arXiv April 2026) applies PER to LLM/VLM RL post-training with reward signals. SuRe (arXiv Nov 2025) uses raw NLL-based surprise scoring with a dual-learner EMA design for prioritized replay in LLM continual learning — inheriting the noise over-sampling failure mode.\\n\\n**Token/sample-level reweighting for SFT:** Token Priority SFT (arXiv Feb 2026) formalizes SFT as granular importance sampling. iw-SFT (arXiv Jul 2025) proves SFT on curated data is a lower bound on the RL objective, proposing importance weighting with a time-lagged auxiliary distribution q(τ) to tighten it. Critically, iw-SFT shows the bound tightens as q → p(·;θ), motivating the use of an adaptive reference that tracks the current policy — exactly what RAPID's EMA reference provides.\\n\\n**EMA dynamics, feedback risks, and model memorization capacity:** Research on EMA models in deep learning (arXiv 2411.18704) shows improved robustness to noisy labels, prediction consistency, and calibration, but the EMA reference is not independent of the training model. Recent work on self-distillation (arXiv 2603.24472) shows that even slow EMA updates can amplify epistemic suppression via feedback loops. This risk is relevant to RAPID's EMA reference and motivates careful τ sensitivity analysis. Separately, research on model memorization capacity is critical for RAPID's noise filtering guarantee: Zhang et al. (ICLR 2017) showed overparameterized DNNs can fit completely random labels; Kajitsuka & Sato (ICLR 2025) prove transformers can memorize N samples with O(√N) parameters, which is far fewer than typical VLM parameter counts. This means the assumption that noisy transitions maintain persistently high loss (L_θ ≥ σ² for all θ) does not hold for high-capacity VLMs — RAPID's noise suppression must work even when models can partially memorize noise (addressed in our reformulated Theorem 3).\\n\\n**RL post-training for VLAs:** SimpleVLA-RL (ICLR 2026) achieves 99.1% on standard LIBERO via RL (GRPO) post-training. SFT alone accounts for 74pp of the 82pp total improvement (17.3% → 91.7%), establishing SFT quality as the critical determinant of RL sample efficiency. Section 6.2 ablates SFT quantity: 0 demos → 0% RL success; 1 demo/task → 96.9% with RL; 100 demos → 18.1% RL improvement; 1000 demos → 22.2% RL improvement — but does not vary SFT *quality*. Open-source at github.com/PRIME-RL/SimpleVLA-RL. 'What Can RL Bring to VLA Generalization?' (NeurIPS 2025) shows SFT-warm-started RL converges ~50% faster, but both warm and cold starts reach comparable final returns given sufficient interaction — suggesting SFT quality primarily affects convergence speed rather than ceiling. VLA-OPD (arXiv Mar 2026, 2603.26666) bridges offline SFT and online RL via on-policy distillation: a frozen teacher provides dense action logits on student-generated trajectories, achieving 93.4% on LIBERO (from 48.9% SFT init) with ~3x faster convergence than sparse-reward RL. VLA-RFT (arXiv Oct 2025) uses a learned world model for RL, surpassing SFT baselines in ~400 gradient steps. Critically, no existing work isolates SFT *data quality* (not quantity) as a variable for downstream RL outcomes — this is the gap RAPID's SFT→RL pipeline experiment targets.\\n\\n**Robustness evaluation of VLAs:** LIBERO-Plus (CVPR 2026) reveals OpenVLA-OFT drops from 97.1% to 70.0% under controlled perturbations across 7 dimensions, with robot initial state perturbation causing drops to 31.9%.\\n\\n**The gap (honestly stated):** The EMA-based reducible loss mechanism exists in RL (ReLo), where it repurposes SAC's existing target network. In supervised/imitation learning, no target network naturally exists, and all existing methods use either fixed reference models (RHO-LOSS, Rho-1, Re-Mix) or raw loss without reducible decomposition (DS2, LEAD, SuRe). No existing work applies sample-level, continuously-adaptive reducible-loss prioritized sampling to SFT/IL with a purpose-built EMA reference. Furthermore, no work has studied how SFT data quality affects downstream RL post-training outcomes for VLAs — SimpleVLA-RL ablates data *quantity* but not *quality*. The combination of (a) extending reducible loss from RL to SFT/IL with a purpose-built EMA reference and training-horizon-aware τ calibration, (b) multi-granularity trajectory+transition sampling, (c) finite-T theoretical bounds proving adaptive references dominate static references at realistic training horizons within the iw-SFT framework, and (d) the first empirical validation that SFT data quality cascades to improved RL post-training constitutes RAPID's contribution. We are transparent that the reducible-loss mechanism is adapted from RL — the novelty lies in the purposeful design for SFT/IL (with non-asymptotic theory yielding practical τ calibration), the reformulated noise suppression guarantee that handles VLM memorization, and the SFT→RL pipeline finding.\",\n  \"approach\": \"**Method overview.** We propose RAPID (Reducible-loss Adaptive Prioritized Imitation from Demonstrations), which maintains a prioritized replay buffer over the demonstration dataset during VLA SFT. Each transition's sampling priority is determined by its *reducible* action-prediction loss — the component that the policy can still decrease — rather than raw loss, which conflates learnable difficulty with irreducible noise. RAPID extends the validated insight that excess/reducible loss effectively curates training data (RHO-LOSS; Re-Mix; ReLo) from its existing applications (fixed-reference supervised selection, RL replay with pre-existing target networks) to fine-grained, adaptive, sample-level prioritized sampling in supervised/imitation learning. Beyond improving SFT in isolation, RAPID targets the SFT stage that serves as the critical foundation for RL post-training pipelines — producing noise-filtered, generalizable SFT checkpoints that cascade to faster RL convergence.\\n\\n**Contribution 1: Purpose-built EMA reference with training-horizon-aware calibration.** In RL, ReLo computes reducible TD error using SAC's Polyak-averaged target network — a mechanism that already exists for TD learning stability and merely serves double duty for data quality scoring. The EMA schedule (τ≈0.995) is optimized for RL stability, not data quality estimation, and the target network operates on TD errors, not supervised losses. In supervised/imitation learning, no target network exists. RAPID introduces a purpose-built EMA reference specifically designed for data quality scoring: θ_ema ← τ·θ_ema + (1-τ)·θ_current, updated every gradient step. A key insight from our finite-T analysis (Corollary 1.1): the optimal decay τ* = 1 - Θ(√ε) (Theorem 2) must be calibrated to the training horizon to ensure the adaptive advantage manifests within realistic training steps. For VLA SFT with ε ≈ 5×10⁻⁴, this yields τ* ≈ 0.978, faster than our originally proposed range [0.999, 0.9999] but still deliberately different from RL target networks (τ≈0.995, optimized for TD stability). We recommend τ ∈ [0.97, 0.999] with the principled choice τ* = 1 - Θ(√ε), and ablate across this range to validate the theory. This provides: (a) *adaptivity* — unlike fixed references (RHO-LOSS, Re-Mix, Rho-1), the EMA tracks the evolving policy; (b) *no auxiliary training* — unlike RHO-LOSS (pre-trained holdout model) or Re-Mix (pre-trained reference); (c) *smoother priority estimates* — continuous EMA evolution without discontinuities. Compared to DS2's raw-loss reweighting, RAPID decomposes loss into reducible and irreducible components, avoiding noise overfitting. Compared to LEAD's EMA over *loss values*, RAPID's EMA over *model parameters* captures richer structural information about learnability.\\n\\n**EMA feedback risk.** We acknowledge that the EMA reference is derived from the training model itself, creating a potential confirmation bias. Research on EMA dynamics (arXiv 2411.18704) and self-distillation feedback loops (arXiv 2603.24472) shows that EMA updates can amplify systematic errors. We mitigate this through: (a) calibrating τ via Theorem 2 to balance tracking and independence; (b) explicit τ sensitivity analysis across [0.97, 0.999, 0.9999] to identify failure modes — τ too high (EMA ≈ initial model, behaves like static reference) shows diminishing adaptivity; τ too low (EMA ≈ current model, near-zero reducible signal) shows degraded priority quality. We report these failure modes transparently.\\n\\nThe reducible loss for each transition (o_t, l, a_t) is:\\n  R(o_t, l, a_t) = max(0, L_θ(a_t | o_t, l) − L_θ_ema(a_t | o_t, l))\\nwhere L is the action-prediction loss (L1 regression following OpenVLA-OFT).\\n\\n**Contribution 2: Multi-granularity trajectory+transition sampling.** RAPID operates at two levels: (1) *Trajectory-level*: each demonstration's priority is the mean reducible loss across its transitions, determining which demonstrations to sample from. This extends Re-Mix's domain-level insight to finer within-domain granularity. (2) *Transition-level*: within a sampled trajectory, transitions are sampled proportionally to their reducible loss, focusing on critical moments (contact, precise alignment) over free-space motions. This two-stage approach captures both inter- and intra-demonstration learning dynamics.\\n\\n**Priority refresh and importance correction.** Priorities are refreshed every K=500 gradient steps by running forward passes on a subset of the buffer (amortized ~8-12% compute overhead). Following Schaul et al. (2016), we apply capped importance-sampling corrections w_i = (1/N · 1/P(i))^β with β annealed from 0 to 1.\\n\\n**Contribution 3: Formal iw-SFT connection with finite-T adaptive reference dominance (theoretical centerpiece).** We establish that RAPID's reducible-loss sampling is a principled instantiation of the iw-SFT framework (arXiv Jul 2025) with a dynamic, training-stage-aware quality score — and prove that this adaptive quality score strictly dominates any static score, with non-asymptotic bounds applicable to realistic VLA training horizons.\\n\\n*Background:* iw-SFT shows that SFT on curated data optimizes a lower bound J_iw(θ) ≤ J(θ) on the RL objective, where J_iw(θ) = E_D+[q(τ)/π_ref(τ) · log p(τ;θ)]. The bound tightens as the auxiliary distribution q approaches the current policy p(·;θ). iw-SFT uses a 'time-lagged policy' as q without specifying the update mechanism.\\n\\n*RAPID's instantiation:* RAPID's EMA reference is a concrete, well-motivated choice for q: q(τ) = π_EMA(τ;θ_ema), continuously tracking the evolving policy via Polyak averaging. The reducible loss R(i) = max(0, L_θ(i) - L_EMA(i)) yields sampling probability P(i) ∝ R(i)^α, which is equivalent to importance-weighted SFT with quality score q_t(i) = R(i)^α / Z_t.\\n\\n*Theorem 1 (Adaptive Reference Dominance):* Under Lipschitz-smooth loss (||∇²L|| ≤ M), bounded gradient steps (||θ_t - θ_{t-1}|| ≤ ε), and non-trivial policy drift during training, define the cumulative bound gap G_T = Σ_{t=1}^T [J(θ_t) - J_iw(θ_t, q_t)]. For RAPID's adaptive EMA reference: G_T^{adaptive} ≤ C₁ · T · ε²τ² / (1-τ)², a quantity that is O(T) in training steps. For any static reference q_s (fixed at initialization, as in RHO-LOSS/Re-Mix/Rho-1): G_T^{static} ≥ C₂ · T² · ε² under non-trivial policy drift, which is Ω(T²). The adaptive reference achieves *strictly tighter* cumulative iw-SFT bound: G_T^{adaptive} / G_T^{static} → 0 as T → ∞.\\n\\n*Corollary 1.1 (Finite-T Crossover):* The asymptotic O(T) vs Ω(T²) separation may not manifest in short VLA SFT runs (typically 50K-150K steps over ~500 demonstrations). We derive non-asymptotic bounds using techniques from finite-sample IS analysis (Agapiou et al., SIAM/JUQ 2022) and biased stochastic approximation theory (Durmus et al., 2024). Define the initial reference gap Δ₀ = D_KL(q_static || p(·;θ₀)). The adaptive EMA reference with τ = τ* = 1 - Θ(√ε) achieves a strictly tighter cumulative bound than any static reference for all T ≥ T₀, where T₀ = C₁/(C₂ · Δ₀ · ε). For typical VLA SFT parameters (ε ≈ 5×10⁻⁴, Δ₀ moderately large since the static reference diverges from the trained policy), T₀ falls in the range of thousands of steps — well within the first epoch of 50K-150K step training runs. Crucially, this finite-T result depends on using τ* from Theorem 2: with the originally proposed τ ∈ [0.999, 0.9999], the tracking error τ²/(1-τ)² becomes so large that T₀ exceeds realistic training horizons, explaining why the theory-optimal τ* ≈ 0.978 is necessary for short VLA SFT runs. We make this prediction empirically testable: measure the bound gap at checkpoints throughout training and verify it grows approximately linearly (adaptive) vs. quadratically (static).\\n\\n*Theorem 2 (Optimal EMA Decay):* The EMA decay τ controls a bias-variance tradeoff in the quality score. Under the same smoothness assumptions: (a) The *tracking error* (how well the EMA follows the current policy) scales as O(ε·τ/(1-τ)) — lower τ gives better tracking. (b) The *signal quality* (magnitude of reducible loss for genuinely learnable data) scales as O(ε·τ/(1-τ)) — higher τ gives stronger signal. (c) The product of IS efficiency and signal quality is maximized at τ* = 1 - Θ(√ε), providing a principled guideline for setting τ based on learning rate. For VLA SFT (ε ≈ 5×10⁻⁴), τ* ≈ 0.978; for fine-tuning with smaller ε ≈ 10⁻⁵, τ* ≈ 0.997. This connects the EMA decay rate to both the optimal IS proposal distribution tracking rate and the finite-T crossover horizon (Corollary 1.1).\\n\\n*Theorem 3 (Noise Suppression via EMA Tracking — reformulated):* The original noise filtering guarantee assumed irreducibly noisy transitions maintain high loss for all θ (L_θ(i) ≥ σ²). This assumption is too strong: high-capacity VLMs can partially or fully memorize label noise (Zhang et al., ICLR 2017; Kajitsuka & Sato, ICLR 2025 show transformers memorize N samples with O(√N) parameters). We reformulate the guarantee to hold regardless of whether the model memorizes noise, using RAPID's max(0, ·) clamp as the key mechanism.\\n\\nFor noisy transitions with additive noise magnitude σ, two complementary suppression mechanisms operate: (a) *Unfittable noise regime*: If the model cannot fit the noise (capacity-limited or early-stopped), L_θ(noisy) ≈ L_EMA(noisy), both remain high, so R = max(0, L_θ - L_EMA) ≈ 0 (original mechanism). (b) *Memorization regime*: If the model gradually memorizes noise, L_θ(noisy) decreases monotonically. Since the EMA lags behind the current model, L_θ ≤ L_EMA for transitions being actively memorized, so R = max(0, L_θ - L_EMA) = 0. Noise memorization produces *negative* pre-clamp reducible loss, which is automatically suppressed. In both cases, noisy transitions receive near-zero sampling priority.\\n\\nThe only regime where R(noisy) > 0 is a transient loss spike on a noisy transition (e.g., brief regression from gradient interference with other samples). Under Lipschitz-smooth loss and bounded EMA lag, this transient is bounded: E[R_t(noisy)] ≤ O(ε·(1-τ)·M). For clean transitions experiencing training-induced regression (catastrophic forgetting from non-uniform sampling), regression magnitude can be O(ε·M). The relative suppression ratio is: E[R_t(noisy)] / E[R_t(clean, regressed)] ≤ O(1-τ), which equals ~0.022 for τ* = 0.978 — noisy transitions are suppressed by ~45x relative to clean transitions experiencing regression. This reformulated guarantee is weaker than the original exponential decay claim but more honest, applicable to high-capacity models, and still practically effective. Critically, it reveals an advantage over raw-loss methods (DS2, SuRe) that cannot be replicated without the EMA decomposition: raw-loss methods assign maximal weight to noisy transitions during the early-learning phase (before memorization occurs) and during memorization (high-loss targets receive high weight), while RAPID suppresses noise in both phases.\\n\\n**Contribution 4: RAPID+RL pipeline validation (empirical centerpiece).** We elevate the SFT→RL connection from future work to a primary contribution, motivated by the observation that no existing work has tested whether SFT *data quality* affects downstream RL outcomes for VLAs. SimpleVLA-RL Section 6.2 ablates SFT data *quantity* (0, 1, 100, 1000 demos) showing it gates RL success, and 'What Can RL Bring to VLA Generalization?' shows warm-start SFT yields ~50% faster RL convergence but comparable final returns. RAPID provides the first test of data *quality*: does noise-filtered SFT → faster/better RL? Hypothesis: RAPID-initialized SFT checkpoints provide a cleaner RL foundation because (1) no noise memorization for RL to unlearn, (2) better behavioral coverage reducing RL exploration burden, (3) more consistent action distributions improving GRPO optimization. We frame the expected improvement primarily in terms of RL convergence *speed* and *sample efficiency* (aligned with the 'What Can RL Bring' finding that SFT affects convergence rate more than ceiling), with robustness as a secondary metric. Even a modest improvement (e.g., 30-50% fewer RL steps to reach 90% success) would be a practically significant finding for the VLA community, given that RL environment interactions are expensive.\\n\\n**Positioning relative to clean-data limitation.** Following 'When Do Curricula Work?' (ICLR 2021), we position RAPID as follows: (a) Standard LIBERO with 50 clean demos per task and 97%+ baseline serves as a *'does no harm' sanity check* — we expect minimal gains and will report honestly. (b) RAPID's primary value is in *noisy/mixed-quality* data settings (controlled noise injection) and the *SFT→RL pipeline* (where noise filtering during SFT cascades to RL benefits), where the reducible loss decomposition provides genuine advantage over raw-loss methods. (c) The real-world motivation is that practical VLA deployment involves heterogeneous demonstration sources with varying quality — the clean-benchmark setting is the exception, not the norm.\\n\\n**Experimental plan.** Built on OpenVLA-OFT (open-source, github.com/moojink/openvla-oft).\\n\\n*Experiment 1 (Primary) — Controlled noise injection:* Systematically corrupt LIBERO-Long demonstrations at varying corruption ratios (10%, 25%, 50%) using three corruption types: (a) Gaussian action noise (σ ∈ {0.05, 0.1, 0.2}), (b) random frame dropping (drop 10-50% of trajectory frames), (c) trajectory truncation (randomly truncate 10-50% of demonstrations early). This is the *primary SFT-only* experiment validating RAPID's core hypothesis: reducible-loss prioritization outperforms raw-loss methods and static curation on noisy data. Calibration: we pre-pilot corruption levels to ensure they degrade uniform-sampling performance to 60-80%.\\n\\n*Experiment 2 (Primary) — RAPID+RL pipeline evaluation:* (a) Vanilla SFT → SimpleVLA-RL GRPO, (b) RAPID SFT → SimpleVLA-RL GRPO, on 2-3 LIBERO-Long tasks with 25% noise injection. Metrics: RL convergence speed (steps to 90% success), final success rate, total environment interactions. The RL stage is computationally cheap (~400 gradient steps vs 50K+ SFT steps), and SimpleVLA-RL is fully open-source. This experiment provides the first test of whether SFT data quality (not just quantity) affects downstream RL — a novel finding with immediate practical implications for VLA pipeline design. Additionally tests with fixed-reference SFT → RL to validate that RAPID's *adaptive* quality filtering (not just any filtering) provides the RL benefit.\\n\\n*Experiment 3 (Secondary/Sanity) — Standard LIBERO-Long:* Reports success rate on clean data, expecting *minimal gains* per the 'When Do Curricula Work?' analysis. Frames as demonstrating RAPID does no harm.\\n\\n*Experiment 4 (Extended, AAAI version) — LIBERO-Plus robustness evaluation:* Evaluate all methods on LIBERO-Plus perturbation dimensions (camera, robot initial state, object layout, lighting, background, noise, language). Tests whether adaptive prioritization extracts more robust representations. Headroom: OpenVLA-OFT 70.0% overall, 31.9% on robot initial state.\\n\\n*Experiment 5 (Extended, AAAI version) — OXE mixed-quality evaluation:* Following SCIZOR/Re-Mix's setup on OXE-Magic-Soup. Tests real-world heterogeneous quality.\\n\\nBaselines: (1) uniform sampling (standard SFT), (2) SCIZOR (static curation), (3) CUPID (influence-function curation), (4) raw-loss priority (demonstrates noise overfitting failure mode), (5) DS2-adapted (DS2's LinUpper reweighting adapted to VLA action space — strongest dynamic baseline without reducible decomposition), (6) fixed-reference reducible loss (RHO-LOSS-style — tests value of adaptive reference, empirically validates Theorem 1 and Corollary 1.1).\\n\\nKey ablations: (a) EMA decay τ ∈ {0.97, 0.99, 0.995, 0.999, 0.9999} — validates Theorem 2's τ* prediction and Corollary 1.1's finite-T crossover; explicitly identifies failure modes at both extremes (τ too low: near-zero signal; τ too high: adaptive advantage doesn't manifest within training horizon), (b) EMA reference vs fixed pre-trained reference (à la RHO-LOSS/Re-Mix) — validates Contribution 1 and Theorem 1, including empirical measurement of bound gap growth rate (linear vs quadratic per Corollary 1.1), (c) trajectory-level vs transition-level vs both (validates Contribution 2), (d) refresh frequency K ∈ {200, 500, 1000, 2000}, (e) priority exponent α ∈ {0.3, 0.6, 1.0}, (f) β annealing schedule.\\n\\nReporting: success rate across all settings, priority distribution evolution visualizations, analysis of which transitions/trajectories are prioritized at different training stages, empirical bound gap measurement at checkpoints throughout training (validates Corollary 1.1), RL convergence curves and sample efficiency for RAPID vs vanilla SFT initialization, noise suppression ratio measurements validating Theorem 3's reformulated guarantee.\\n\\n**CoRL 2026 minimum viable plan (14-day sprint, empirical focus).** Abstract deadline May 26, paper deadline May 29. Repositioned as empirical paper with RAPID+RL as headline finding, addressing CoRL's strong preference for empirical robot learning contributions.\\n- Days 1-3: Implement EMA reference + reducible loss on OpenVLA-OFT (few-line addition: EMA model copy, reducible loss computation, proportional sampling). Formalize finite-T bound (Corollary 1.1).\\n- Days 2-7: Run minimum viable experiments:\\n  (a) Noise injection on LIBERO-Long: 3 corruption types × 1 ratio (25%) × 3 methods (uniform/raw-loss/RAPID) = 9 SFT runs\\n  (b) Standard LIBERO-Long sanity check: 3 methods = 3 SFT runs\\n  (c) EMA vs fixed reference ablation: 3 SFT runs (validates Theorem 1)\\n  (d) RAPID+RL pipeline: 2 methods × 2 tasks = 4 RL runs (cheap: ~50h each, uses SimpleVLA-RL open-source GRPO)\\n  Total: 15 SFT runs (~750 GPU-hours) + 4 RL runs (~200 GPU-hours) ≈ 950 GPU-hours.\\n- Days 8-14: Write paper. Lead with RAPID+RL pipeline result (novel finding about SFT data quality → RL outcomes) + noise injection robustness (core validation). Theory as supporting framework, not centerpiece.\\n- Feasibility: 8×A100 can complete 15 SFT runs in ~5-6 experiment days with parallelism. RL runs overlap with writing phase (cheap: ~400 gradient steps each). Total wall time: ~6 experiment days + ~7 writing days.\\n- Drop: OXE, LIBERO-Plus, DS2 baseline, CUPID baseline, extensive ablations (→ AAAI 2027).\\n- Risk: SimpleVLA-RL integration with RAPID SFT checkpoints requires testing. Fallback if RL pipeline integration fails: submit SFT-only paper (noise injection + standard LIBERO + EMA vs fixed reference, 15 SFT runs). Fallback if experiments incomplete: target AAAI 2027 exclusively.\\n\\n**AAAI 2027 full version (primary target, deadline ~Aug 2026).** Includes all 5 experiments, complete ablation suite, all 6 baselines, LIBERO-Plus robustness, OXE mixed-quality, extended RAPID+RL analysis across multiple noise levels and tasks. Theory presented as co-equal contribution with comprehensive empirical validation: Corollary 1.1 bound gap measurements across training, Theorem 3 noise suppression ratio measurements, and τ ablation validating Theorem 2's calibration formula. This is the definitive version of the paper.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~3500h A100-80GB (noise injection: 3 types × 3 ratios × ~80h = ~720h + RAPID+RL: 6 RL runs × ~50h = 300h + LIBERO-Plus: ~200h eval overhead + standard LIBERO-Long: 4 methods × 80h = 320h + OXE: ~400h + 6 baselines × 100h = 600h + ablations ~500h + theory validation runs ~100h)\",\n      \"gpu_utilization\": \"~25-35% effective utilization; researcher implements reducible loss, debugs priority refresh, integrates SimpleVLA-RL pipeline, analyzes distributions and RL convergence, writes paper between runs\",\n      \"timeline\": \"10-14 weeks (full AAAI version); 14 days (CoRL sprint, reduced scope)\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$5,250 at ~$1.50/hr (full version); ~$1,425 for CoRL sprint (950h)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~5000h A100-80GB (agent explores τ, K, α, β configurations and runs RAPID+RL pipeline variants; human gates noise injection calibration, interprets RL convergence curves, and validates theory predictions)\",\n      \"gpu_utilization\": \"~60-70% utilization; agent queues experiments overnight/weekends, human reviews priority distributions and RL learning curves during daily check-in\",\n      \"timeline\": \"6-8 weeks (full version); 10-12 days (CoRL sprint with agent assistance)\",\n      \"team\": \"1 researcher, ~30-45min/day check-in\",\n      \"claude_api_cost\": \"$300-500 (1500-2500 turns)\",\n      \"estimated_gpu_cost\": \"~$7,500 at ~$1.50/hr (full version); ~$2,000 for CoRL sprint\",\n      \"risk_note\": \"EMA decay τ and refresh frequency K interact nonlinearly; RAPID+RL experiments require SimpleVLA-RL environment setup (open-source but integration with custom SFT checkpoints is untested); noise injection calibration requires pre-piloting to find diagnostically useful corruption levels (target: 60-80% degraded baseline)\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~6500-7500h A100-80GB (systematic sweep over τ × K × α × β grid, noise injection matrix, OXE experiments, LIBERO-Plus evaluation, RAPID+RL pipeline across all noise conditions and tasks)\",\n      \"gpu_utilization\": \"~90-95% utilization\",\n      \"timeline\": \"16-24 days with 8×A100 cluster\",\n      \"team\": \"0 (initial setup and final review only)\",\n      \"claude_api_cost\": \"$600-1000 (3000-5000 turns)\",\n      \"estimated_gpu_cost\": \"~$11,000 at ~$1.50/hr\",\n      \"speed_bottleneck\": \"GPU cluster availability; SimpleVLA-RL environment rollouts for RAPID+RL experiments; LIBERO-Plus evaluation rollouts 3-4x more expensive than standard LIBERO\",\n      \"risk_note\": \"Agent may over-explore τ-K interaction space or RL hyperparameter configs; risk of ~15-20% wasted compute without human calibration intuition on convergence diagnostics and noise injection regime selection\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (deadline: expected ~Aug 2026 — primary target for full version with all experiments including RAPID+RL pipeline, LIBERO-Plus, OXE, complete ablations, and comprehensive finite-T theory validation; AAAI welcomes both theoretical and empirical contributions)\",\n    \"CoRL 2026 (abstract May 26, paper May 29 AoE — stretch goal with empirical focus: RAPID+RL headline finding + noise injection + sanity check, 15 SFT runs + 4 RL runs = 950 GPU-hours in 14-day sprint; addresses CoRL's preference for empirical robot learning contributions by leading with the SFT→RL pipeline result)\",\n    \"ICRA 2027 (deadline: expected ~Sep 2026 — strong fit for robot learning venue, robustness focus aligns well, fallback if CoRL sprint is infeasible)\",\n    \"ICLR 2027 (deadline: expected ~Sep-Oct 2026 — only if finite-T theory is validated empirically and RAPID+RL finding is received as genuinely novel, as ICLR values theoretical depth)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Prioritized Training on Points that are Learnable, Worth Learning, and Not Yet Learnt [RHO-LOSS] (ICML 2022)\",\n    \"Prioritized Experience Replay (ICLR 2016)\",\n    \"Prioritizing Samples in Reinforcement Learning with Reducible Loss [ReLo] (NeurIPS 2023)\",\n    \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining (NeurIPS 2023)\",\n    \"Not All Tokens Are What You Need [Rho-1] (NeurIPS 2024)\",\n    \"Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning (CoRL 2024)\",\n    \"Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining [DS2] (ICLR 2025)\",\n    \"Value-aligned Behavior Cloning for Offline RL via Bi-level Optimization [VACO] (ICLR 2025)\",\n    \"Robot Data Curation with Mutual Information Estimators [DemInf] (RSS 2025)\",\n    \"CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)\",\n    \"Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning [RINSE] (ICML 2025)\",\n    \"SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)\",\n    \"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (ICLR 2026)\",\n    \"When Do Curricula Work? (ICLR 2021)\",\n    \"Density-Ratio Weighted Behavioral Cloning: Learning Control Policies from Corrupted Datasets (arXiv Oct 2025)\",\n    \"Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority (arXiv Feb 2026)\",\n    \"Supervised Fine Tuning on Curated Data is Reinforcement Learning [iw-SFT] (arXiv Jul 2025)\",\n    \"LEAD: Iterative Data Selection for Efficient LLM Instruction Tuning (arXiv May 2025)\",\n    \"SuRe: Surprise-Driven Prioritised Replay for Continual LLM Learning (arXiv Nov 2025)\",\n    \"Freshness-Aware Prioritized Experience Replay for LLM/VLM RL (arXiv April 2026)\",\n    \"Utility-Diversity Aware Online Batch Selection for LLM SFT [UDS] (arXiv Oct 2025)\",\n    \"Exponential Moving Average of Weights in Deep Learning: Dynamics and Benefits (arXiv Nov 2024)\",\n    \"Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs? (arXiv Mar 2026)\",\n    \"OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024)\",\n    \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success [OpenVLA-OFT] (arXiv 2025)\",\n    \"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (ICLR 2026)\",\n    \"Quality over Quantity: Demonstration Curation via Influence Functions [QoQ] (arXiv 2026)\",\n    \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models (arXiv 2023)\",\n    \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026)\",\n    \"LIBERO-PRO: Towards Robust and Fair Evaluation of VLA Models Beyond Memorization (arXiv Oct 2025)\",\n    \"Predictive Batch Scheduling: Accelerating Language Model Training Through Loss-Aware Sample Prioritization (arXiv Feb 2026)\",\n    \"Green-VLA: A Staged Vision-Language-Action Framework (arXiv Feb 2026, 2602.00919)\",\n    \"VLA-OPD: Bridging Offline SFT and Online RL for VLAs via On-Policy Distillation (arXiv Mar 2026, 2603.26666)\",\n    \"What Can RL Bring to VLA Generalization? (NeurIPS 2025)\",\n    \"VLA-RFT: Reinforcement Fine-Tuning for VLAs with World Models (arXiv Oct 2025)\",\n    \"Understanding Deep Learning Requires Rethinking Generalization (Zhang et al., ICLR 2017)\",\n    \"On the Optimal Memorization Capacity of Transformers (Kajitsuka & Sato, ICLR 2025)\"\n  ],\n  \"description\": \"We propose RAPID (Reducible-loss Adaptive Prioritized Imitation from Demonstrations), which replaces static demonstration curation with online, policy-aware prioritized sampling during VLA supervised fine-tuning — and demonstrates that this improved SFT quality cascades to faster RL post-training convergence. Building on the foundational insight from RHO-LOSS (ICML 2022) and ReLo (NeurIPS 2023), RAPID makes four contributions:\\n\\n(1) **Purpose-built EMA reference with training-horizon-aware calibration**: RAPID introduces an EMA reference for supervised/imitation SFT with decay τ calibrated to the training horizon via the theoretically derived τ* = 1 - Θ(√ε) (yielding τ* ≈ 0.978 for typical VLA learning rates). This is faster than the originally proposed [0.999, 0.9999] range — a critical correction revealed by the finite-T analysis showing that slow EMA makes the adaptive advantage unachievable within realistic VLA training horizons. Unlike fixed references (RHO-LOSS, Re-Mix, Rho-1), it adapts; unlike raw-loss methods (DS2, LEAD, SuRe), it decomposes reducible from irreducible loss.\\n\\n(2) **Multi-granularity trajectory+transition sampling**: Two-level prioritized sampling capturing both inter- and intra-demonstration learning dynamics.\\n\\n(3) **Finite-T iw-SFT theory (theoretical centerpiece)**: Three results within the iw-SFT framework: (a) *Adaptive Reference Dominance with Finite-T Crossover* (Theorem 1 + Corollary 1.1): EMA reference achieves O(T) cumulative bound gap vs Ω(T²) for static references, with non-asymptotic crossover T₀ = C₁/(C₂·Δ₀·ε) falling within thousands of steps for τ = τ*, derived via finite-sample IS analysis and biased stochastic approximation theory. (b) *Optimal EMA Decay* (Theorem 2): τ* = 1 - Θ(√ε) balances tracking error and signal quality, connecting the EMA to the learning rate, optimal IS tracking rate, and finite-T crossover. (c) *Noise Suppression via EMA Tracking* (Theorem 3, reformulated for high-capacity VLMs): noise suppression holds regardless of whether the model memorizes noise — unfittable noise yields R ≈ 0 (both models struggle equally), and gradually memorized noise yields L_θ ≤ L_EMA → R = 0 (memorization produces negative pre-clamp reducible loss). Relative suppression ratio O(1-τ) ≈ 0.022 for τ* = 0.978.\\n\\n(4) **RAPID+RL pipeline validation (empirical centerpiece)**: The first test of whether SFT *data quality* (not quantity) affects downstream RL for VLAs. SimpleVLA-RL shows SFT data quantity gates RL (Section 6.2), but no work varies quality. We test RAPID SFT → SimpleVLA-RL GRPO vs vanilla SFT → GRPO on noisy LIBERO-Long, measuring RL convergence speed and sample efficiency. This transforms RAPID from 'another curation method' to a mechanism for improving the entire VLA training pipeline.\\n\\nPrimary experiments: noise injection (3 corruption types) and RAPID+RL pipeline (SimpleVLA-RL open-source GRPO), with standard LIBERO as sanity check. Extended experiments (AAAI version): LIBERO-Plus robustness and OXE mixed-quality. AAAI 2027 (~Aug 2026) is the primary target; CoRL 2026 is a stretch goal with empirical focus (RAPID+RL headline, 15 SFT + 4 RL runs ≈ 950 GPU-hours in a 14-day sprint).\",\n  \"project_name\": \"adaptive_replay_vla\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 6)\nIssues: [\"MISSING REFERENCE: 'Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL' (ICML 2026, poster). This paper directly studies how SFT technique quality affects downstream RL performance — showing 7.09% RL improvement and 11.54% reduced forgetting via token-level clipping. While it operates on LLMs (ALFWorld, ScienceWorld) at the token level rather than VLA data level, it establishes the same principle as RAPID's Contribution 4 ('SFT quality cascades to RL'). Must be cited. RAPID's differentiation: (a) data/demonstration-level filtering vs. token-level clipping, (b) VLA domain with action-prediction loss vs. LLM domain with language loss, (c) noise filtering mechanism vs. trust-region mechanism. This weakens the claim of 'first to study SFT quality → RL' — reframe as 'first to study SFT *data quality* → RL for *VLAs*.'\", \"NOVELTY NARROWING: iw-SFT (arXiv 2507.12856) already implements EMA update θ_q = α·θ_q + (1-α)·θ for continuous control (D4RL) experiments. The proposal's Contribution 1 claims 'RAPID introduces a purpose-built EMA reference specifically designed for data quality scoring' as if no EMA reference exists in supervised/IL settings — but iw-SFT uses exactly this mechanism for updating the auxiliary distribution q in continuous control SFT/BC. The critical distinction: iw-SFT uses EMA for trajectory-level importance weights (multiplicative loss reweighting), while RAPID uses EMA for *reducible loss computation* + *PER-style sampling priorities*. This distinction is real but must be articulated precisely. Reframe: 'iw-SFT proposed EMA for importance weighting; we use EMA for reducible loss decomposition, revealing that the EMA reference enables noise-robust prioritization beyond what importance weighting alone provides.'\", \"CoRL TIMELINE: 13 days to abstract deadline (May 26), 16 days to paper deadline (May 29). The proposal should include an explicit go/no-go decision point: if the first noise-injection experiment results are not available by ~May 22-23, fall back to AAAI 2027 only. The abstract deadline requires at least preliminary results to write a credible abstract.\", \"FINITE-T TESTABILITY: Corollary 1.1 predicts T₀ = C₁/(C₂·Δ₀·ε) falls within 'thousands of steps' for τ* = 0.978. However, the constants C₁, C₂ depend on loss landscape properties (Lipschitz constant M, gradient bound ε) that are difficult to estimate a priori for VLA models. The empirical crossover point may differ by an order of magnitude from the theoretical prediction. The proposal should acknowledge this uncertainty and frame the empirical bound-gap measurement as a test of the theory's qualitative prediction (linear vs quadratic growth) rather than its quantitative prediction (exact T₀).\", \"NOISE INJECTION VS REAL-WORLD NOISE: The primary experiment uses synthetic corruption (Gaussian noise, frame dropping, truncation). Real-world demonstration noise (hesitation, redundant motions, suboptimal strategies, operator fatigue) has fundamentally different structure — it's *coherent* noise that may be harder for reducible loss to detect. The OXE experiment (deferred to AAAI) would address this. For CoRL, acknowledge this limitation explicitly and frame noise injection as a controlled test of the mechanism, not a claim about real-world robustness.\"]\nFeedback: The proposal has reached an exceptionally high level of polish and the landscape analysis is now world-class. The remaining gap to 'pass' (avg 3.5 vs 4.0 threshold) reflects inherent novelty and impact ceilings rather than fixable oversights. Here is how to close the gap:\n\n**1. Cite and differentiate from ICML 2026 clipping paper (easy, high priority).** 'Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL' establishes that SFT technique → RL performance in LLMs. RAPID's differentiation is clear: (a) data-level noise filtering vs. token-level trust region, (b) VLA domain vs. LLM domain, (c) prioritized sampling vs. gradient clipping. Frame RAPID as: 'The ICML 2026 work shows SFT technique affects RL for LLMs; we show SFT *data quality* affects RL for VLAs — a complementary finding in a different domain with a different mechanism.'\n\n**2. Sharpen iw-SFT differentiation (important).** iw-SFT already uses EMA for continuous control. RAPID's actual novelty over iw-SFT is threefold: (a) reducible loss decomposition (iw-SFT uses trajectory probabilities for importance weights, RAPID uses loss difference for noise-robust prioritization), (b) PER-style sampling (iw-SFT reweights loss multiplicatively, RAPID controls which samples are seen), (c) theoretical analysis of optimal τ and finite-T crossover. State this explicitly rather than claiming EMA reference as wholly novel.\n\n**3. The path to pushing impact from 3→4.** The single most impactful result would be a compelling RAPID+RL experiment showing e.g. 30-50% fewer RL steps to reach 90% success. If this materializes, lead the paper with it. The narrative becomes: 'SFT data quality is the hidden bottleneck of VLA RL pipelines; RAPID provides a drop-in fix.' This is more impactful than 'another data curation method for noisy demonstrations.'\n\n**4. Consider whether CoRL is the right target.** With 13 days to abstract, the risk of a rushed submission is high. The AAAI 2027 timeline (3+ months) allows comprehensive experiments including LIBERO-Plus and OXE, which would strengthen impact significantly. A well-executed AAAI paper with the RAPID+RL finding as headline result + robustness on LIBERO-Plus + OXE mixed-quality is stronger than a rushed CoRL submission. If you attempt CoRL, treat it as a stretch with explicit go/no-go by May 22.\n\n**5. For the next revision, focus on sharpening rather than expanding.** The proposal is comprehensive but very long. The landscape analysis is thorough but could be tightened. Every additional reference and caveat adds length but diminishing returns on clarity. The core story is: 'EMA-based reducible loss enables noise-robust, adaptive data prioritization for VLA SFT, and this cascades to faster RL convergence.' Everything should serve this narrative.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.5 到 3.5，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-13T11:29:30.826Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T11:29:30.826Z",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---

## Round 1

67 recorded events

### User

_source line 3 · 2026-05-13T11:29:30.866Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-13 (UTC).**

## Original idea
{
  "title": "RAPID: Reducible-Loss Adaptive Prioritized Replay for VLA Imitation Learning",
  "core_problem": "Can we improve VLA supervised fine-tuning quality — and crucially, the downstream RL post-training that depends on it — by adaptively prioritizing demonstration data based on what the evolving policy can still learn from, particularly in realistic settings where demonstration quality varies and the SFT stage serves as the critical foundation for the entire VLA training pipeline?",
  "opportunity": "Prior work has established that excess loss relative to a reference model is a powerful signal for data selection in supervised learning (RHO-LOSS, ICML 2022), LLM pretraining (DoReMi, NeurIPS 2023; Rho-1, NeurIPS 2024), and robot imitation learning at the domain level (Re-Mix, CoRL 2024). In RL, ReLo (NeurIPS 2023) showed that computing reducible TD error using SAC's Polyak-averaged (EMA) target network avoids the failure mode of raw-loss PER (over-sampling noisy data). DS2 (ICLR 2025) demonstrated that dynamic instance-level loss-based reweighting accelerates LLM pretraining convergence with theoretical guarantees, but uses raw loss without decomposing reducible vs. irreducible components. Yet all existing applications in supervised/imitation settings use *fixed* reference models and operate at *coarse* granularity (domain-level in Re-Mix/DoReMi, token-level selection with static reference in RHO-LOSS/Rho-1). Meanwhile, all VLA demonstration curation methods (SCIZOR, CUPID, QoQ, DataMIL, RINSE, DemInf, Density-Ratio Weighted BC, Green-VLA DataQA) operate as static preprocessing — score once, filter once, train once. This ignores that the policy's learning needs change during training.\n\nCritically, the 'When Do Curricula Work?' (Wu et al., ICLR 2021) finding that curricula provide only marginal benefits on clean benchmarks — with apparent gains entirely explained by dynamic training set size — implies that RAPID's primary value proposition is NOT standard clean-data benchmarks (where VLAs already achieve 97%+), but rather the realistic settings of noisy/mixed-quality demonstrations and robustness under distribution shift. Recent robustness benchmarks (LIBERO-Plus, CVPR 2026; LIBERO-PRO) have exposed that high success rates on standard LIBERO mask fundamental fragility — OpenVLA-OFT drops from 97.1% to 70.0% on LIBERO-Plus.\n\n**The SFT→RL pipeline gap (new).** The VLA training paradigm is shifting from SFT-only to SFT→RL pipelines (SimpleVLA-RL, ICLR 2026; VLA-OPD, arXiv 2026; VLA-RFT, arXiv 2025). SimpleVLA-RL demonstrates that SFT quality is the critical determinant of RL outcomes: SFT alone accounts for 74pp of 82pp total improvement (17.3%→91.7%), and Section 6.2 shows RL completely fails (0% success) with zero SFT demonstrations. 'What Can RL Bring to VLA Generalization?' (NeurIPS 2025) shows SFT-warm-started RL converges ~50% faster than cold-start RL. Yet no existing work has studied how SFT *data quality* (as opposed to data quantity) affects downstream RL performance. This is a genuine unexplored gap: if RAPID's noise filtering during SFT produces policies that have not memorized noise, the resulting SFT checkpoint should provide a cleaner foundation for RL — faster convergence, better sample efficiency, and more robust final policies. This transforms RAPID from 'another data curation method' to 'a mechanism for improving the entire VLA training pipeline.'\n\nThe specific technical gap we target: no existing work applies *sample-level, continuously-adaptive* reducible-loss prioritized sampling to supervised/imitation learning. In RL, ReLo's target network serves double duty — both TD learning stability and reducible loss computation — and the EMA update schedule is dictated by RL optimization dynamics, not data quality scoring. In supervised/imitation learning, no target network naturally exists. RAPID introduces a purpose-built EMA reference model for data quality scoring, with training-horizon-aware τ calibration, multi-granularity trajectory+transition sampling, finite-T bounds proving adaptive references dominate static references at realistic training horizons, and empirical validation that RAPID-quality SFT cascades to improved RL post-training.",
  "landscape": "**Foundational excess/reducible loss concepts:** RHO-LOSS (Mindermann et al., ICML 2022) introduced the core principle of selecting training points by their *reducible holdout loss* — the difference between the current model's loss and a small, fixed holdout-trained reference model's loss — to identify points that are 'learnable, worth learning, and not yet learnt.' This achieves 18x faster training on Clothing-1M by avoiding both noisy and already-learned data. ReLo (Sujit et al., NeurIPS 2023) adapted this principle to RL, computing reducible TD error as the difference between the online network's TD error and the Polyak-averaged (EMA) target network's TD error. Crucially, ReLo's target network is SAC's standard Polyak-averaged target (θ_target ← τ·θ_target + (1-τ)·θ_online, τ≈0.995), which already exists for TD learning stability and serves double duty for reducible loss — ReLo did not introduce an EMA reference, it repurposed an existing RL mechanism. Rho-1 (NeurIPS 2024) brought excess loss back to supervised learning for LLM pretraining, using a *fixed, separately-trained* reference model for selective token training. All three works that operate in supervised settings (RHO-LOSS, Rho-1) use static reference models.\n\n**Dynamic instance-level reweighting during training:** DS2 (Bajaj et al., ICLR 2025) performs dynamic, instance-level, loss-based sample reweighting during LLM pretraining. DS2 normalizes per-sample losses to [-α, α], applies transformation functions (LinUpper, Quadratic, or Extremes), and converts scores to weights via temperature-annealed softmax. DS2 provides a formal convergence framework and demonstrates significant improvements on 7B and 1.4B parameter LLMs. However, DS2 uses *raw loss* without decomposing it into reducible and irreducible components, inheriting the noise overfitting risk identified by RHO-LOSS. RAPID's reducible loss decomposition directly addresses this limitation.\n\n**Domain-level excess loss in data mixing:** DoReMi (Xie et al., NeurIPS 2023) uses excess loss relative to a pretrained reference model with Group DRO to optimize domain mixing weights for LLM pretraining. Re-Mix (Hejna et al., CoRL 2024, Outstanding Paper Finalist) extends this to robot imitation learning, using excess BC loss relative to a *fixed* reference model with DRO to optimize domain-level weights across heterogeneous robotics datasets (Open X-Embodiment), outperforming uniform weights by 38% and human-selected weights by 32%. Re-Mix operates at *domain level* (one weight per dataset), uses a *fixed* reference model, and employs DRO optimization — not sample-level prioritized sampling.\n\n**Static demonstration curation (one-shot preprocessing):** SCIZOR (ICRA 2026) removes suboptimal and redundant data via self-supervised progress prediction and clustering. CUPID (CoRL 2025) uses influence functions to rank demonstrations by estimated impact on closed-loop performance. QoQ (arXiv 2026) applies static influence-function scoring. RINSE (ICML 2025) proposes smoothness-driven metrics (Spectral Arc Length and Trajectory-Envelope Distance) for policy-architecture-agnostic demonstration scoring. DataMIL (ICLR 2026) uses a policy-driven datamodels framework for end-to-end data selection. DemInf (Hejna et al., RSS 2025) uses k-NN mutual information estimation for demonstration quality scoring. Density-Ratio Weighted BC (Pandian & Baheri, arXiv Oct 2025) uses a small clean reference set to estimate trajectory-level density ratios via a binary discriminator, downweighting corrupted data — static, requires a verified clean reference, and cannot adapt to evolving policy needs. Green-VLA (arXiv Feb 2026, 2602.00919) introduces a DataQA pipeline for VLA training data using four quality metrics (jitter, sharpness, visual diversity via DINOv3 features, proprioceptive state variance) plus optical-flow-based temporal resampling, achieving 94.6% pick success on SimplerEnv BRIDGE with 3000 hours of data. Green-VLA's DataQA is applied as static preprocessing before training. All these methods score data once before training.\n\n**Online/adaptive sample selection during training:** UDS (arXiv Oct 2025) performs online batch selection during LLM SFT using nuclear norm of the logits matrix to capture utility-diversity, eliminating the need for a reference model. LEAD (arXiv May 2025) introduces Instance-Level Dynamic Uncertainty (IDU), combining instantaneous loss, gradient-based loss-change approximation, and exponential smoothing of *historical loss values* for online data selection during LLM instruction tuning, achieving 6-10% improvements with 2.5% of data. Key distinction from RAPID: LEAD smooths *loss values* via EMA to reduce noise, while RAPID maintains an EMA *model* to compute reducible loss — the model-based approach decomposes genuinely learnable from irreducibly noisy data, which a single loss signal cannot. Predictive Batch Scheduling (PBS, arXiv Feb 2026) uses static features (token frequency, sequence length) for difficulty estimation during LLM pretraining.\n\n**Curricula effectiveness:** 'When Do Curricula Work?' (Wu et al., ICLR 2021, Oral) demonstrates through extensive experiments that curriculum/prioritized sampling provides only marginal benefits on standard benchmarks with clean data — any apparent benefit is entirely explained by dynamic training set size, not the ordering itself. Benefits emerge only under (1) limited training budget or (2) noisy data. This is a critical calibration for RAPID.\n\n**Adaptive weighting during training (not VLA, not imitation learning):** VACO (ICLR 2025) trains a meta-scoring network via bi-level optimization to adaptively weight BC samples in offline RL on D4RL tasks. Key differences: (1) targets offline RL with value alignment; (2) bi-level optimization is expensive; (3) low-dimensional state-action pairs.\n\n**Prioritized replay in RL/LLM post-training:** PER (Schaul et al. 2016) uses TD error for priority in RL. Freshness-Aware PER (arXiv April 2026) applies PER to LLM/VLM RL post-training with reward signals. SuRe (arXiv Nov 2025) uses raw NLL-based surprise scoring with a dual-learner EMA design for prioritized replay in LLM continual learning — inheriting the noise over-sampling failure mode.\n\n**Token/sample-level reweighting for SFT:** Token Priority SFT (arXiv Feb 2026) formalizes SFT as granular importance sampling. iw-SFT (arXiv Jul 2025) proves SFT on curated data is a lower bound on the RL objective, proposing importance weighting with a time-lagged auxiliary distribution q(τ) to tighten it. Critically, iw-SFT shows the bound tightens as q → p(·;θ), motivating the use of an adaptive reference that tracks the current policy — exactly what RAPID's EMA reference provides.\n\n**EMA dynamics, feedback risks, and model memorization capacity:** Research on EMA models in deep learning (arXiv 2411.18704) shows improved robustness to noisy labels, prediction consistency, and calibration, but the EMA reference is not independent of the training model. Recent work on self-distillation (arXiv 2603.24472) shows that even slow EMA updates can amplify epistemic suppression via feedback loops. This risk is relevant to RAPID's EMA reference and motivates careful τ sensitivity analysis. Separately, research on model memorization capacity is critical for RAPID's noise filtering guarantee: Zhang et al. (ICLR 2017) showed overparameterized DNNs can fit completely random labels; Kajitsuka & Sato (ICLR 2025) prove transformers can memorize N samples with O(√N) parameters, which is far fewer than typical VLM parameter counts. This means the assumption that noisy transitions maintain persistently high loss (L_θ ≥ σ² for all θ) does not hold for high-capacity VLMs — RAPID's noise suppression must work even when models can partially memorize noise (addressed in our reformulated Theorem 3).\n\n**RL post-training for VLAs:** SimpleVLA-RL (ICLR 2026) achieves 99.1% on standard LIBERO via RL (GRPO) post-training. SFT alone accounts for 74pp of the 82pp total improvement (17.3% → 91.7%), establishing SFT quality as the critical determinant of RL sample efficiency. Section 6.2 ablates SFT quantity: 0 demos → 0% RL success; 1 demo/task → 96.9% with RL; 100 demos → 18.1% RL improvement; 1000 demos → 22.2% RL improvement — but does not vary SFT *quality*. Open-source at github.com/PRIME-RL/SimpleVLA-RL. 'What Can RL Bring to VLA Generalization?' (NeurIPS 2025) shows SFT-warm-started RL converges ~50% faster, but both warm and cold starts reach comparable final returns given sufficient interaction — suggesting SFT quality primarily affects convergence speed rather than ceiling. VLA-OPD (arXiv Mar 2026, 2603.26666) bridges offline SFT and online RL via on-policy distillation: a frozen teacher provides dense action logits on student-generated trajectories, achieving 93.4% on LIBERO (from 48.9% SFT init) with ~3x faster convergence than sparse-reward RL. VLA-RFT (arXiv Oct 2025) uses a learned world model for RL, surpassing SFT baselines in ~400 gradient steps. Critically, no existing work isolates SFT *data quality* (not quantity) as a variable for downstream RL outcomes — this is the gap RAPID's SFT→RL pipeline experiment targets.\n\n**Robustness evaluation of VLAs:** LIBERO-Plus (CVPR 2026) reveals OpenVLA-OFT drops from 97.1% to 70.0% under controlled perturbations across 7 dimensions, with robot initial state perturbation causing drops to 31.9%.\n\n**The gap (honestly stated):** The EMA-based reducible loss mechanism exists in RL (ReLo), where it repurposes SAC's existing target network. In supervised/imitation learning, no target network naturally exists, and all existing methods use either fixed reference models (RHO-LOSS, Rho-1, Re-Mix) or raw loss without reducible decomposition (DS2, LEAD, SuRe). No existing work applies sample-level, continuously-adaptive reducible-loss prioritized sampling to SFT/IL with a purpose-built EMA reference. Furthermore, no work has studied how SFT data quality affects downstream RL post-training outcomes for VLAs — SimpleVLA-RL ablates data *quantity* but not *quality*. The combination of (a) extending reducible loss from RL to SFT/IL with a purpose-built EMA reference and training-horizon-aware τ calibration, (b) multi-granularity trajectory+transition sampling, (c) finite-T theoretical bounds proving adaptive references dominate static references at realistic training horizons within the iw-SFT framework, and (d) the first empirical validation that SFT data quality cascades to improved RL post-training constitutes RAPID's contribution. We are transparent that the reducible-loss mechanism is adapted from RL — the novelty lies in the purposeful design for SFT/IL (with non-asymptotic theory yielding practical τ calibration), the reformulated noise suppression guarantee that handles VLM memorization, and the SFT→RL pipeline finding.",
  "approach": "**Method overview.** We propose RAPID (Reducible-loss Adaptive Prioritized Imitation from Demonstrations), which maintains a prioritized replay buffer over the demonstration dataset during VLA SFT. Each transition's sampling priority is determined by its *reducible* action-prediction loss — the component that the policy can still decrease — rather than raw loss, which conflates learnable difficulty with irreducible noise. RAPID extends the validated insight that excess/reducible loss effectively curates training data (RHO-LOSS; Re-Mix; ReLo) from its existing applications (fixed-reference supervised selection, RL replay with pre-existing target networks) to fine-grained, adaptive, sample-level prioritized sampling in supervised/imitation learning. Beyond improving SFT in isolation, RAPID targets the SFT stage that serves as the critical foundation for RL post-training pipelines — producing noise-filtered, generalizable SFT checkpoints that cascade to faster RL convergence.\n\n**Contribution 1: Purpose-built EMA reference with training-horizon-aware calibration.** In RL, ReLo computes reducible TD error using SAC's Polyak-averaged target network — a mechanism that already exists for TD learning stability and merely serves double duty for data quality scoring. The EMA schedule (τ≈0.995) is optimized for RL stability, not data quality estimation, and the target network operates on TD errors, not supervised losses. In supervised/imitation learning, no target network exists. RAPID introduces a purpose-built EMA reference specifically designed for data quality scoring: θ_ema ← τ·θ_ema + (1-τ)·θ_current, updated every gradient step. A key insight from our finite-T analysis (Corollary 1.1): the optimal decay τ* = 1 - Θ(√ε) (Theorem 2) must be calibrated to the training horizon to ensure the adaptive advantage manifests within realistic training steps. For VLA SFT with ε ≈ 5×10⁻⁴, this yields τ* ≈ 0.978, faster than our originally proposed range [0.999, 0.9999] but still deliberately different from RL target networks (τ≈0.995, optimized for TD stability). We recommend τ ∈ [0.97, 0.999] with the principled choice τ* = 1 - Θ(√ε), and ablate across this range to validate the theory. This provides: (a) *adaptivity* — unlike fixed references (RHO-LOSS, Re-Mix, Rho-1), the EMA tracks the evolving policy; (b) *no auxiliary training* — unlike RHO-LOSS (pre-trained holdout model) or Re-Mix (pre-trained reference); (c) *smoother priority estimates* — continuous EMA evolution without discontinuities. Compared to DS2's raw-loss reweighting, RAPID decomposes loss into reducible and irreducible components, avoiding noise overfitting. Compared to LEAD's EMA over *loss values*, RAPID's EMA over *model parameters* captures richer structural information about learnability.\n\n**EMA feedback risk.** We acknowledge that the EMA reference is derived from the training model itself, creating a potential confirmation bias. Research on EMA dynamics (arXiv 2411.18704) and self-distillation feedback loops (arXiv 2603.24472) shows that EMA updates can amplify systematic errors. We mitigate this through: (a) calibrating τ via Theorem 2 to balance tracking and independence; (b) explicit τ sensitivity analysis across [0.97, 0.999, 0.9999] to identify failure modes — τ too high (EMA ≈ initial model, behaves like static reference) shows diminishing adaptivity; τ too low (EMA ≈ current model, near-zero reducible signal) shows degraded priority quality. We report these failure modes transparently.\n\nThe reducible loss for each transition (o_t, l, a_t) is:\n  R(o_t, l, a_t) = max(0, L_θ(a_t | o_t, l) − L_θ_ema(a_t | o_t, l))\nwhere L is the action-prediction loss (L1 regression following OpenVLA-OFT).\n\n**Contribution 2: Multi-granularity trajectory+transition sampling.** RAPID operates at two levels: (1) *Trajectory-level*: each demonstration's priority is the mean reducible loss across its transitions, determining which demonstrations to sample from. This extends Re-Mix's domain-level insight to finer within-domain granularity. (2) *Transition-level*: within a sampled trajectory, transitions are sampled proportionally to their reducible loss, focusing on critical moments (contact, precise alignment) over free-space motions. This two-stage approach captures both inter- and intra-demonstration learning dynamics.\n\n**Priority refresh and importance correction.** Priorities are refreshed every K=500 gradient steps by running forward passes on a subset of the buffer (amortized ~8-12% compute overhead). Following Schaul et al. (2016), we apply capped importance-sampling corrections w_i = (1/N · 1/P(i))^β with β annealed from 0 to 1.\n\n**Contribution 3: Formal iw-SFT connection with finite-T adaptive reference dominance (theoretical centerpiece).** We establish that RAPID's reducible-loss sampling is a principled instantiation of the iw-SFT framework (arXiv Jul 2025) with a dynamic, training-stage-aware quality score — and prove that this adaptive quality score strictly dominates any static score, with non-asymptotic bounds applicable to realistic VLA training horizons.\n\n*Background:* iw-SFT shows that SFT on curated data optimizes a lower bound J_iw(θ) ≤ J(θ) on the RL objective, where J_iw(θ) = E_D+[q(τ)/π_ref(τ) · log p(τ;θ)]. The bound tightens as the auxiliary distribution q approaches the current policy p(·;θ). iw-SFT uses a 'time-lagged policy' as q without specifying the update mechanism.\n\n*RAPID's instantiation:* RAPID's EMA reference is a concrete, well-motivated choice for q: q(τ) = π_EMA(τ;θ_ema), continuously tracking the evolving policy via Polyak averaging. The reducible loss R(i) = max(0, L_θ(i) - L_EMA(i)) yields sampling probability P(i) ∝ R(i)^α, which is equivalent to importance-weighted SFT with quality score q_t(i) = R(i)^α / Z_t.\n\n*Theorem 1 (Adaptive Reference Dominance):* Under Lipschitz-smooth loss (||∇²L|| ≤ M), bounded gradient steps (||θ_t - θ_{t-1}|| ≤ ε), and non-trivial policy drift during training, define the cumulative bound gap G_T = Σ_{t=1}^T [J(θ_t) - J_iw(θ_t, q_t)]. For RAPID's adaptive EMA reference: G_T^{adaptive} ≤ C₁ · T · ε²τ² / (1-τ)², a quantity that is O(T) in training steps. For any static reference q_s (fixed at initialization, as in RHO-LOSS/Re-Mix/Rho-1): G_T^{static} ≥ C₂ · T² · ε² under non-trivial policy drift, which is Ω(T²). The adaptive reference achieves *strictly tighter* cumulative iw-SFT bound: G_T^{adaptive} / G_T^{static} → 0 as T → ∞.\n\n*Corollary 1.1 (Finite-T Crossover):* The asymptotic O(T) vs Ω(T²) separation may not manifest in short VLA SFT runs (typically 50K-150K steps over ~500 demonstrations). We derive non-asymptotic bounds using techniques from finite-sample IS analysis (Agapiou et al., SIAM/JUQ 2022) and biased stochastic approximation theory (Durmus et al., 2024). Define the initial reference gap Δ₀ = D_KL(q_static || p(·;θ₀)). The adaptive EMA reference with τ = τ* = 1 - Θ(√ε) achieves a strictly tighter cumulative bound than any static reference for all T ≥ T₀, where T₀ = C₁/(C₂ · Δ₀ · ε). For typical VLA SFT parameters (ε ≈ 5×10⁻⁴, Δ₀ moderately large since the static reference diverges from the trained policy), T₀ falls in the range of thousands of steps — well within the first epoch of 50K-150K step training runs. Crucially, this finite-T result depends on using τ* from Theorem 2: with the originally proposed τ ∈ [0.999, 0.9999], the tracking error τ²/(1-τ)² becomes so large that T₀ exceeds realistic training horizons, explaining why the theory-optimal τ* ≈ 0.978 is necessary for short VLA SFT runs. We make this prediction empirically testable: measure the bound gap at checkpoints throughout training and verify it grows approximately linearly (adaptive) vs. quadratically (static).\n\n*Theorem 2 (Optimal EMA Decay):* The EMA decay τ controls a bias-variance tradeoff in the quality score. Under the same smoothness assumptions: (a) The *tracking error* (how well the EMA follows the current policy) scales as O(ε·τ/(1-τ)) — lower τ gives better tracking. (b) The *signal quality* (magnitude of reducible loss for genuinely learnable data) scales as O(ε·τ/(1-τ)) — higher τ gives stronger signal. (c) The product of IS efficiency and signal quality is maximized at τ* = 1 - Θ(√ε), providing a principled guideline for setting τ based on learning rate. For VLA SFT (ε ≈ 5×10⁻⁴), τ* ≈ 0.978; for fine-tuning with smaller ε ≈ 10⁻⁵, τ* ≈ 0.997. This connects the EMA decay rate to both the optimal IS proposal distribution tracking rate and the finite-T crossover horizon (Corollary 1.1).\n\n*Theorem 3 (Noise Suppression via EMA Tracking — reformulated):* The original noise filtering guarantee assumed irreducibly noisy transitions maintain high loss for all θ (L_θ(i) ≥ σ²). This assumption is too strong: high-capacity VLMs can partially or fully memorize label noise (Zhang et al., ICLR 2017; Kajitsuka & Sato, ICLR 2025 show transformers memorize N samples with O(√N) parameters). We reformulate the guarantee to hold regardless of whether the model memorizes noise, using RAPID's max(0, ·) clamp as the key mechanism.\n\nFor noisy transitions with additive noise magnitude σ, two complementary suppression mechanisms operate: (a) *Unfittable noise regime*: If the model cannot fit the noise (capacity-limited or early-stopped), L_θ(noisy) ≈ L_EMA(noisy), both remain high, so R = max(0, L_θ - L_EMA) ≈ 0 (original mechanism). (b) *Memorization regime*: If the model gradually memorizes noise, L_θ(noisy) decreases monotonically. Since the EMA lags behind the current model, L_θ ≤ L_EMA for transitions being actively memorized, so R = max(0, L_θ - L_EMA) = 0. Noise memorization produces *negative* pre-clamp reducible loss, which is automatically suppressed. In both cases, noisy transitions receive near-zero sampling priority.\n\nThe only regime where R(noisy) > 0 is a transient loss spike on a noisy transition (e.g., brief regression from gradient interference with other samples). Under Lipschitz-smooth loss and bounded EMA lag, this transient is bounded: E[R_t(noisy)] ≤ O(ε·(1-τ)·M). For clean transitions experiencing training-induced regression (catastrophic forgetting from non-uniform sampling), regression magnitude can be O(ε·M). The relative suppression ratio is: E[R_t(noisy)] / E[R_t(clean, regressed)] ≤ O(1-τ), which equals ~0.022 for τ* = 0.978 — noisy transitions are suppressed by ~45x relative to clean transitions experiencing regression. This reformulated guarantee is weaker than the original exponential decay claim but more honest, applicable to high-capacity models, and still practically effective. Critically, it reveals an advantage over raw-loss methods (DS2, SuRe) that cannot be replicated without the EMA decomposition: raw-loss methods assign maximal weight to noisy transitions during the early-learning phase (before memorization occurs) and during memorization (high-loss targets receive high weight), while RAPID suppresses noise in both phases.\n\n**Contribution 4: RAPID+RL pipeline validation (empirical centerpiece).** We elevate the SFT→RL connection from future work to a primary contribution, motivated by the observation that no existing work has tested whether SFT *data quality* affects downstream RL outcomes for VLAs. SimpleVLA-RL Section 6.2 ablates SFT data *quantity* (0, 1, 100, 1000 demos) showing it gates RL success, and 'What Can RL Bring to VLA Generalization?' shows warm-start SFT yields ~50% faster RL convergence but comparable final returns. RAPID provides the first test of data *quality*: does noise-filtered SFT → faster/better RL? Hypothesis: RAPID-initialized SFT checkpoints provide a cleaner RL foundation because (1) no noise memorization for RL to unlearn, (2) better behavioral coverage reducing RL exploration burden, (3) more consistent action distributions improving GRPO optimization. We frame the expected improvement primarily in terms of RL convergence *speed* and *sample efficiency* (aligned with the 'What Can RL Bring' finding that SFT affects convergence rate more than ceiling), with robustness as a secondary metric. Even a modest improvement (e.g., 30-50% fewer RL steps to reach 90% success) would be a practically significant finding for the VLA community, given that RL environment interactions are expensive.\n\n**Positioning relative to clean-data limitation.** Following 'When Do Curricula Work?' (ICLR 2021), we position RAPID as follows: (a) Standard LIBERO with 50 clean demos per task and 97%+ baseline serves as a *'does no harm' sanity check* — we expect minimal gains and will report honestly. (b) RAPID's primary value is in *noisy/mixed-quality* data settings (controlled noise injection) and the *SFT→RL pipeline* (where noise filtering during SFT cascades to RL benefits), where the reducible loss decomposition provides genuine advantage over raw-loss methods. (c) The real-world motivation is that practical VLA deployment involves heterogeneous demonstration sources with varying quality — the clean-benchmark setting is the exception, not the norm.\n\n**Experimental plan.** Built on OpenVLA-OFT (open-source, github.com/moojink/openvla-oft).\n\n*Experiment 1 (Primary) — Controlled noise injection:* Systematically corrupt LIBERO-Long demonstrations at varying corruption ratios (10%, 25%, 50%) using three corruption types: (a) Gaussian action noise (σ ∈ {0.05, 0.1, 0.2}), (b) random frame dropping (drop 10-50% of trajectory frames), (c) trajectory truncation (randomly truncate 10-50% of demonstrations early). This is the *primary SFT-only* experiment validating RAPID's core hypothesis: reducible-loss prioritization outperforms raw-loss methods and static curation on noisy data. Calibration: we pre-pilot corruption levels to ensure they degrade uniform-sampling performance to 60-80%.\n\n*Experiment 2 (Primary) — RAPID+RL pipeline evaluation:* (a) Vanilla SFT → SimpleVLA-RL GRPO, (b) RAPID SFT → SimpleVLA-RL GRPO, on 2-3 LIBERO-Long tasks with 25% noise injection. Metrics: RL convergence speed (steps to 90% success), final success rate, total environment interactions. The RL stage is computationally cheap (~400 gradient steps vs 50K+ SFT steps), and SimpleVLA-RL is fully open-source. This experiment provides the first test of whether SFT data quality (not just quantity) affects downstream RL — a novel finding with immediate practical implications for VLA pipeline design. Additionally tests with fixed-reference SFT → RL to validate that RAPID's *adaptive* quality filtering (not just any filtering) provides the RL benefit.\n\n*Experiment 3 (Secondary/Sanity) — Standard LIBERO-Long:* Reports success rate on clean data, expecting *minimal gains* per the 'When Do Curricula Work?' analysis. Frames as demonstrating RAPID does no harm.\n\n*Experiment 4 (Extended, AAAI version) — LIBERO-Plus robustness evaluation:* Evaluate all methods on LIBERO-Plus perturbation dimensions (camera, robot initial state, object layout, lighting, background, noise, language). Tests whether adaptive prioritization extracts more robust representations. Headroom: OpenVLA-OFT 70.0% overall, 31.9% on robot initial state.\n\n*Experiment 5 (Extended, AAAI version) — OXE mixed-quality evaluation:* Following SCIZOR/Re-Mix's setup on OXE-Magic-Soup. Tests real-world heterogeneous quality.\n\nBaselines: (1) uniform sampling (standard SFT), (2) SCIZOR (static curation), (3) CUPID (influence-function curation), (4) raw-loss priority (demonstrates noise overfitting failure mode), (5) DS2-adapted (DS2's LinUpper reweighting adapted to VLA action space — strongest dynamic baseline without reducible decomposition), (6) fixed-reference reducible loss (RHO-LOSS-style — tests value of adaptive reference, empirically validates Theorem 1 and Corollary 1.1).\n\nKey ablations: (a) EMA decay τ ∈ {0.97, 0.99, 0.995, 0.999, 0.9999} — validates Theorem 2's τ* prediction and Corollary 1.1's finite-T crossover; explicitly identifies failure modes at both extremes (τ too low: near-zero signal; τ too high: adaptive advantage doesn't manifest within training horizon), (b) EMA reference vs fixed pre-trained reference (à la RHO-LOSS/Re-Mix) — validates Contribution 1 and Theorem 1, including empirical measurement of bound gap growth rate (linear vs quadratic per Corollary 1.1), (c) trajectory-level vs transition-level vs both (validates Contribution 2), (d) refresh frequency K ∈ {200, 500, 1000, 2000}, (e) priority exponent α ∈ {0.3, 0.6, 1.0}, (f) β annealing schedule.\n\nReporting: success rate across all settings, priority distribution evolution visualizations, analysis of which transitions/trajectories are prioritized at different training stages, empirical bound gap measurement at checkpoints throughout training (validates Corollary 1.1), RL convergence curves and sample efficiency for RAPID vs vanilla SFT initialization, noise suppression ratio measurements validating Theorem 3's reformulated guarantee.\n\n**CoRL 2026 minimum viable plan (14-day sprint, empirical focus).** Abstract deadline May 26, paper deadline May 29. Repositioned as empirical paper with RAPID+RL as headline finding, addressing CoRL's strong preference for empirical robot learning contributions.\n- Days 1-3: Implement EMA reference + reducible loss on OpenVLA-OFT (few-line addition: EMA model copy, reducible loss computation, proportional sampling). Formalize finite-T bound (Corollary 1.1).\n- Days 2-7: Run minimum viable experiments:\n  (a) Noise injection on LIBERO-Long: 3 corruption types × 1 ratio (25%) × 3 methods (uniform/raw-loss/RAPID) = 9 SFT runs\n  (b) Standard LIBERO-Long sanity check: 3 methods = 3 SFT runs\n  (c) EMA vs fixed reference ablation: 3 SFT runs (validates Theorem 1)\n  (d) RAPID+RL pipeline: 2 methods × 2 tasks = 4 RL runs (cheap: ~50h each, uses SimpleVLA-RL open-source GRPO)\n  Total: 15 SFT runs (~750 GPU-hours) + 4 RL runs (~200 GPU-hours) ≈ 950 GPU-hours.\n- Days 8-14: Write paper. Lead with RAPID+RL pipeline result (novel finding about SFT data quality → RL outcomes) + noise injection robustness (core validation). Theory as supporting framework, not centerpiece.\n- Feasibility: 8×A100 can complete 15 SFT runs in ~5-6 experiment days with parallelism. RL runs overlap with writing phase (cheap: ~400 gradient steps each). Total wall time: ~6 experiment days + ~7 writing days.\n- Drop: OXE, LIBERO-Plus, DS2 baseline, CUPID baseline, extensive ablations (→ AAAI 2027).\n- Risk: SimpleVLA-RL integration with RAPID SFT checkpoints requires testing. Fallback if RL pipeline integration fails: submit SFT-only paper (noise injection + standard LIBERO + EMA vs fixed reference, 15 SFT runs). Fallback if experiments incomplete: target AAAI 2027 exclusively.\n\n**AAAI 2027 full version (primary target, deadline ~Aug 2026).** Includes all 5 experiments, complete ablation suite, all 6 baselines, LIBERO-Plus robustness, OXE mixed-quality, extended RAPID+RL analysis across multiple noise levels and tasks. Theory presented as co-equal contribution with comprehensive empirical validation: Corollary 1.1 bound gap measurements across training, Theorem 3 noise suppression ratio measurements, and τ ablation validating Theorem 2's calibration formula. This is the definitive version of the paper.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~3500h A100-80GB (noise injection: 3 types × 3 ratios × ~80h = ~720h + RAPID+RL: 6 RL runs × ~50h = 300h + LIBERO-Plus: ~200h eval overhead + standard LIBERO-Long: 4 methods × 80h = 320h + OXE: ~400h + 6 baselines × 100h = 600h + ablations ~500h + theory validation runs ~100h)",
      "gpu_utilization": "~25-35% effective utilization; researcher implements reducible loss, debugs priority refresh, integrates SimpleVLA-RL pipeline, analyzes distributions and RL convergence, writes paper between runs",
      "timeline": "10-14 weeks (full AAAI version); 14 days (CoRL sprint, reduced scope)",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$5,250 at ~$1.50/hr (full version); ~$1,425 for CoRL sprint (950h)"
    },
    "human_in_loop": {
      "gpu_hours": "~5000h A100-80GB (agent explores τ, K, α, β configurations and runs RAPID+RL pipeline variants; human gates noise injection calibration, interprets RL convergence curves, and validates theory predictions)",
      "gpu_utilization": "~60-70% utilization; agent queues experiments overnight/weekends, human reviews priority distributions and RL learning curves during daily check-in",
      "timeline": "6-8 weeks (full version); 10-12 days (CoRL sprint with agent assistance)",
      "team": "1 researcher, ~30-45min/day check-in",
      "claude_api_cost": "$300-500 (1500-2500 turns)",
      "estimated_gpu_cost": "~$7,500 at ~$1.50/hr (full version); ~$2,000 for CoRL sprint",
      "risk_note": "EMA decay τ and refresh frequency K interact nonlinearly; RAPID+RL experiments require SimpleVLA-RL environment setup (open-source but integration with custom SFT checkpoints is untested); noise injection calibration requires pre-piloting to find diagnostically useful corruption levels (target: 60-80% degraded baseline)"
    },
    "auto_research": {
      "gpu_hours": "~6500-7500h A100-80GB (systematic sweep over τ × K × α × β grid, noise injection matrix, OXE experiments, LIBERO-Plus evaluation, RAPID+RL pipeline across all noise conditions and tasks)",
      "gpu_utilization": "~90-95% utilization",
      "timeline": "16-24 days with 8×A100 cluster",
      "team": "0 (initial setup and final review only)",
      "claude_api_cost": "$600-1000 (3000-5000 turns)",
      "estimated_gpu_cost": "~$11,000 at ~$1.50/hr",
      "speed_bottleneck": "GPU cluster availability; SimpleVLA-RL environment rollouts for RAPID+RL experiments; LIBERO-Plus evaluation rollouts 3-4x more expensive than standard LIBERO",
      "risk_note": "Agent may over-explore τ-K interaction space or RL hyperparameter configs; risk of ~15-20% wasted compute without human calibration intuition on convergence diagnostics and noise injection regime selection"
    }
  },
  "target_venues": [
    "AAAI 2027 (deadline: expected ~Aug 2026 — primary target for full version with all experiments including RAPID+RL pipeline, LIBERO-Plus, OXE, complete ablations, and comprehensive finite-T theory validation; AAAI welcomes both theoretical and empirical contributions)",
    "CoRL 2026 (abstract May 26, paper May 29 AoE — stretch goal with empirical focus: RAPID+RL headline finding + noise injection + sanity check, 15 SFT runs + 4 RL runs = 950 GPU-hours in 14-day sprint; addresses CoRL's preference for empirical robot learning contributions by leading with the SFT→RL pipeline result)",
    "ICRA 2027 (deadline: expected ~Sep 2026 — strong fit for robot learning venue, robustness focus aligns well, fallback if CoRL sprint is infeasible)",
    "ICLR 2027 (deadline: expected ~Sep-Oct 2026 — only if finite-T theory is validated empirically and RAPID+RL finding is received as genuinely novel, as ICLR values theoretical depth)"
  ],
  "level": "solid",
  "key_references": [
    "Prioritized Training on Points that are Learnable, Worth Learning, and Not Yet Learnt [RHO-LOSS] (ICML 2022)",
    "Prioritized Experience Replay (ICLR 2016)",
    "Prioritizing Samples in Reinforcement Learning with Reducible Loss [ReLo] (NeurIPS 2023)",
    "DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining (NeurIPS 2023)",
    "Not All Tokens Are What You Need [Rho-1] (NeurIPS 2024)",
    "Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning (CoRL 2024)",
    "Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining [DS2] (ICLR 2025)",
    "Value-aligned Behavior Cloning for Offline RL via Bi-level Optimization [VACO] (ICLR 2025)",
    "Robot Data Curation with Mutual Information Estimators [DemInf] (RSS 2025)",
    "CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)",
    "Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning [RINSE] (ICML 2025)",
    "SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)",
    "DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (ICLR 2026)",
    "When Do Curricula Work? (ICLR 2021)",
    "Density-Ratio Weighted Behavioral Cloning: Learning Control Policies from Corrupted Datasets (arXiv Oct 2025)",
    "Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority (arXiv Feb 2026)",
    "Supervised Fine Tuning on Curated Data is Reinforcement Learning [iw-SFT] (arXiv Jul 2025)",
    "LEAD: Iterative Data Selection for Efficient LLM Instruction Tuning (arXiv May 2025)",
    "SuRe: Surprise-Driven Prioritised Replay for Continual LLM Learning (arXiv Nov 2025)",
    "Freshness-Aware Prioritized Experience Replay for LLM/VLM RL (arXiv April 2026)",
    "Utility-Diversity Aware Online Batch Selection for LLM SFT [UDS] (arXiv Oct 2025)",
    "Exponential Moving Average of Weights in Deep Learning: Dynamics and Benefits (arXiv Nov 2024)",
    "Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs? (arXiv Mar 2026)",
    "OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024)",
    "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success [OpenVLA-OFT] (arXiv 2025)",
    "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (ICLR 2026)",
    "Quality over Quantity: Demonstration Curation via Influence Functions [QoQ] (arXiv 2026)",
    "Open X-Embodiment: Robotic Learning Datasets and RT-X Models (arXiv 2023)",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026)",
    "LIBERO-PRO: Towards Robust and Fair Evaluation of VLA Models Beyond Memorization (arXiv Oct 2025)",
    "Predictive Batch Scheduling: Accelerating Language Model Training Through Loss-Aware Sample Prioritization (arXiv Feb 2026)",
    "Green-VLA: A Staged Vision-Language-Action Framework (arXiv Feb 2026, 2602.00919)",
    "VLA-OPD: Bridging Offline SFT and Online RL for VLAs via On-Policy Distillation (arXiv Mar 2026, 2603.26666)",
    "What Can RL Bring to VLA Generalization? (NeurIPS 2025)",
    "VLA-RFT: Reinforcement Fine-Tuning for VLAs with World Models (arXiv Oct 2025)",
    "Understanding Deep Learning Requires Rethinking Generalization (Zhang et al., ICLR 2017)",
    "On the Optimal Memorization Capacity of Transformers (Kajitsuka & Sato, ICLR 2025)"
  ],
  "description": "We propose RAPID (Reducible-loss Adaptive Prioritized Imitation from Demonstrations), which replaces static demonstration curation with online, policy-aware prioritized sampling during VLA supervised fine-tuning — and demonstrates that this improved SFT quality cascades to faster RL post-training convergence. Building on the foundational insight from RHO-LOSS (ICML 2022) and ReLo (NeurIPS 2023), RAPID makes four contributions:\n\n(1) **Purpose-built EMA reference with training-horizon-aware calibration**: RAPID introduces an EMA reference for supervised/imitation SFT with decay τ calibrated to the training horizon via the theoretically derived τ* = 1 - Θ(√ε) (yielding τ* ≈ 0.978 for typical VLA learning rates). This is faster than the originally proposed [0.999, 0.9999] range — a critical correction revealed by the finite-T analysis showing that slow EMA makes the adaptive advantage unachievable within realistic VLA training horizons. Unlike fixed references (RHO-LOSS, Re-Mix, Rho-1), it adapts; unlike raw-loss methods (DS2, LEAD, SuRe), it decomposes reducible from irreducible loss.\n\n(2) **Multi-granularity trajectory+transition sampling**: Two-level prioritized sampling capturing both inter- and intra-demonstration learning dynamics.\n\n(3) **Finite-T iw-SFT theory (theoretical centerpiece)**: Three results within the iw-SFT framework: (a) *Adaptive Reference Dominance with Finite-T Crossover* (Theorem 1 + Corollary 1.1): EMA reference achieves O(T) cumulative bound gap vs Ω(T²) for static references, with non-asymptotic crossover T₀ = C₁/(C₂·Δ₀·ε) falling within thousands of steps for τ = τ*, derived via finite-sample IS analysis and biased stochastic approximation theory. (b) *Optimal EMA Decay* (Theorem 2): τ* = 1 - Θ(√ε) balances tracking error and signal quality, connecting the EMA to the learning rate, optimal IS tracking rate, and finite-T crossover. (c) *Noise Suppression via EMA Tracking* (Theorem 3, reformulated for high-capacity VLMs): noise suppression holds regardless of whether the model memorizes noise — unfittable noise yields R ≈ 0 (both models struggle equally), and gradually memorized noise yields L_θ ≤ L_EMA → R = 0 (memorization produces negative pre-clamp reducible loss). Relative suppression ratio O(1-τ) ≈ 0.022 for τ* = 0.978.\n\n(4) **RAPID+RL pipeline validation (empirical centerpiece)**: The first test of whether SFT *data quality* (not quantity) affects downstream RL for VLAs. SimpleVLA-RL shows SFT data quantity gates RL (Section 6.2), but no work varies quality. We test RAPID SFT → SimpleVLA-RL GRPO vs vanilla SFT → GRPO on noisy LIBERO-Long, measuring RL convergence speed and sample efficiency. This transforms RAPID from 'another curation method' to a mechanism for improving the entire VLA training pipeline.\n\nPrimary experiments: noise injection (3 corruption types) and RAPID+RL pipeline (SimpleVLA-RL open-source GRPO), with standard LIBERO as sanity check. Extended experiments (AAAI version): LIBERO-Plus robustness and OXE mixed-quality. AAAI 2027 (~Aug 2026) is the primary target; CoRL 2026 is a stretch goal with empirical focus (RAPID+RL headline, 15 SFT + 4 RL runs ≈ 950 GPU-hours in a 14-day sprint).",
  "project_name": "adaptive_replay_vla",
  "source": "web_research"
}

## Reviewer feedback (round 6)
Issues: ["MISSING REFERENCE: 'Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL' (ICML 2026, poster). This paper directly studies how SFT technique quality affects downstream RL performance — showing 7.09% RL improvement and 11.54% reduced forgetting via token-level clipping. While it operates on LLMs (ALFWorld, ScienceWorld) at the token level rather than VLA data level, it establishes the same principle as RAPID's Contribution 4 ('SFT quality cascades to RL'). Must be cited. RAPID's differentiation: (a) data/demonstration-level filtering vs. token-level clipping, (b) VLA domain with action-prediction loss vs. LLM domain with language loss, (c) noise filtering mechanism vs. trust-region mechanism. This weakens the claim of 'first to study SFT quality → RL' — reframe as 'first to study SFT *data quality* → RL for *VLAs*.'", "NOVELTY NARROWING: iw-SFT (arXiv 2507.12856) already implements EMA update θ_q = α·θ_q + (1-α)·θ for continuous control (D4RL) experiments. The proposal's Contribution 1 claims 'RAPID introduces a purpose-built EMA reference specifically designed for data quality scoring' as if no EMA reference exists in supervised/IL settings — but iw-SFT uses exactly this mechanism for updating the auxiliary distribution q in continuous control SFT/BC. The critical distinction: iw-SFT uses EMA for trajectory-level importance weights (multiplicative loss reweighting), while RAPID uses EMA for *reducible loss computation* + *PER-style sampling priorities*. This distinction is real but must be articulated precisely. Reframe: 'iw-SFT proposed EMA for importance weighting; we use EMA for reducible loss decomposition, revealing that the EMA reference enables noise-robust prioritization beyond what importance weighting alone provides.'", "CoRL TIMELINE: 13 days to abstract deadline (May 26), 16 days to paper deadline (May 29). The proposal should include an explicit go/no-go decision point: if the first noise-injection experiment results are not available by ~May 22-23, fall back to AAAI 2027 only. The abstract deadline requires at least preliminary results to write a credible abstract.", "FINITE-T TESTABILITY: Corollary 1.1 predicts T₀ = C₁/(C₂·Δ₀·ε) falls within 'thousands of steps' for τ* = 0.978. However, the constants C₁, C₂ depend on loss landscape properties (Lipschitz constant M, gradient bound ε) that are difficult to estimate a priori for VLA models. The empirical crossover point may differ by an order of magnitude from the theoretical prediction. The proposal should acknowledge this uncertainty and frame the empirical bound-gap measurement as a test of the theory's qualitative prediction (linear vs quadratic growth) rather than its quantitative prediction (exact T₀).", "NOISE INJECTION VS REAL-WORLD NOISE: The primary experiment uses synthetic corruption (Gaussian noise, frame dropping, truncation). Real-world demonstration noise (hesitation, redundant motions, suboptimal strategies, operator fatigue) has fundamentally different structure — it's *coherent* noise that may be harder for reducible loss to detect. The OXE experiment (deferred to AAAI) would address this. For CoRL, acknowledge this limitation explicitly and frame noise injection as a controlled test of the mechanism, not a claim about real-world robustness."]
Feedback: The proposal has reached an exceptionally high level of polish and the landscape analysis is now world-class. The remaining gap to 'pass' (avg 3.5 vs 4.0 threshold) reflects inherent novelty and impact ceilings rather than fixable oversights. Here is how to close the gap:

**1. Cite and differentiate from ICML 2026 clipping paper (easy, high priority).** 'Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL' establishes that SFT technique → RL performance in LLMs. RAPID's differentiation is clear: (a) data-level noise filtering vs. token-level trust region, (b) VLA domain vs. LLM domain, (c) prioritized sampling vs. gradient clipping. Frame RAPID as: 'The ICML 2026 work shows SFT technique affects RL for LLMs; we show SFT *data quality* affects RL for VLAs — a complementary finding in a different domain with a different mechanism.'

**2. Sharpen iw-SFT differentiation (important).** iw-SFT already uses EMA for continuous control. RAPID's actual novelty over iw-SFT is threefold: (a) reducible loss decomposition (iw-SFT uses trajectory probabilities for importance weights, RAPID uses loss difference for noise-robust prioritization), (b) PER-style sampling (iw-SFT reweights loss multiplicatively, RAPID controls which samples are seen), (c) theoretical analysis of optimal τ and finite-T crossover. State this explicitly rather than claiming EMA reference as wholly novel.

**3. The path to pushing impact from 3→4.** The single most impactful result would be a compelling RAPID+RL experiment showing e.g. 30-50% fewer RL steps to reach 90% success. If this materializes, lead the paper with it. The narrative becomes: 'SFT data quality is the hidden bottleneck of VLA RL pipelines; RAPID provides a drop-in fix.' This is more impactful than 'another data curation method for noisy demonstrations.'

**4. Consider whether CoRL is the right target.** With 13 days to abstract, the risk of a rushed submission is high. The AAAI 2027 timeline (3+ months) allows comprehensive experiments including LIBERO-Plus and OXE, which would strengthen impact significantly. A well-executed AAAI paper with the RAPID+RL finding as headline result + robustness on LIBERO-Plus + OXE mixed-quality is stronger than a rushed CoRL submission. If you attempt CoRL, treat it as a stretch with explicit go/no-go by May 22.

**5. For the next revision, focus on sharpening rather than expanding.** The proposal is comprehensive but very long. The landscape analysis is thorough but could be tightened. Every additional reference and caveat adds length but diminishing returns on clarity. The core story is: 'EMA-based reducible loss enables noise-robust, adaptive data prioritization for VLA SFT, and this cascades to faster RL convergence.' Everything should serve this narrative.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.
- Address each issue specifically.

## 深度调研要求（每一轮修订都必须执行）

不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。
   - 搜索最新的相关论文（arXiv, conference proceedings）
   - 搜索 benchmark/leaderboard 确认当前 SOTA
   - 搜索可能遗漏的相关工作和 concurrent work

2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，
   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。

3. **深度思考**：在修订之前，先独立思考以下问题：
   - 这个 idea 的核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach 来解决同一个核心问题？
   - 修订后的 idea 相比上一版有什么本质性的改进？

4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，
   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。

## 针对 Review 意见的定向搜索

对 reviewer 指出的每个问题，执行以下搜索流程：

1. **如果 reviewer 说'已有类似工作'**：
   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读
   - 搜索该论文的 cited-by，找到后续跟进工作
   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot

2. **如果 reviewer 说'SOTA 过时'**：
   - 用 Papers With Code 查看当前排行榜
   - 搜索过去 6 个月的最新方法
   - 更新你的 landscape 和 baseline

3. **如果 reviewer 说'可行性有问题'**：
   - 搜索类似规模实验的实际成本和时间线
   - 搜索 GitHub 上是否有可复用的实现
   - 搜索相关数据集/模型的可获取性

4. **如果 reviewer 说'novelty 不足'**：
   - 对核心方法尽量做 3-5 种不同关键词组合的搜索
   - 搜索相邻领域是否有类似思路
   - 如果确实 novelty 不足，考虑 major revision 或 pivot

- Use WebSearch to find updated information if the reviewer flagged outdated claims.
- You have full freedom in how much to change:
  - Minor fix: if only specific details are wrong, correct them and keep everything else.
  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.
  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.
- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.
- In the output JSON, include a "change_type" field with one of: "minor", "major", or "pivot" to indicate the scope of your changes.
- Output the revised idea as a COMPLETE JSON object (same schema as original, plus "change_type").

## 停滞提醒
这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.5 到 3.5，没有明显改善。

请认真思考：
- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？
- 如果你认为问题出在 approach 而非 framing，可以做 major revision。
- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。
- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。

最终由你判断——做你认为最能提升 idea 质量的选择。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "c4a3ccad-7cef-4937-a83a-71870f86aca5",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T11:29:30.863Z_

```json
{
  "parentUuid": "c4a3ccad-7cef-4937-a83a-71870f86aca5",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "7fce8831-5739-4f3a-bf20-61d661f5d3e3",
  "timestamp": "2026-05-13T11:29:30.863Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T11:29:30.863Z_

```json
{
  "parentUuid": "7fce8831-5739-4f3a-bf20-61d661f5d3e3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "46fc30c9-2e78-4d56-a726-8057a2694ac6",
  "timestamp": "2026-05-13T11:29:30.863Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"RAPID: Reducible-Loss Adaptive Prioritized Replay for VLA Imitation Le…",
  "leafUuid": "46fc30c9-2e78-4d56-a726-8057a2694ac6",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising RAPID: Addressing novelty gaps and clarifying SFT→RL contribution",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---

### Assistant

_source line 8 · 2026-05-13T11:29:52.134Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully and think about what changes are needed.

The reviewer's feedback identifies 5 specific issues:

1. **Missing reference**: ICML 2026 paper on clipping low-probability tokens in SFT for RL - weakens the "first to study SFT quality → RL" claim
2. **Novelty narrowing**: iw-SFT already uses EMA for continuous control - need to sharpen differentiation
3. **CoRL timeline**: 13 days to abstract - need go/no-go decision point
4. **Finite-T testability**: Constants C₁, C₂ hard to estimate - should frame as qualitative test


5. **Noise injection vs real-world noise**: Synthetic corruption doesn't capture actual deployment conditions

The stagnation pattern is telling—six rounds stuck at 3.5 suggests we're hitting a structural ceiling rather than facing fixable gaps. The reviewer's core message is clear: the novelty and impact limitations are fundamental to the approach itself, not just presentation issues. The real breakthrough would be demonstrating RAPID+RL working end-to-end, which would validate the entire framework rather than just patching individual claims.

So the path forward is about ruthless focus. SFT data quality is actually the hidden bottleneck in VLA RL pipelines—that's the insight worth building around. The ICML 2026 clipping paper is just a citation update, the iw-SFT EMA distinction needs clearer framing, CoRL timing is workable, finite-T testability is a reframing problem, and the noise injection limitation is honest enough to acknowledge. The reviewer's real feedback isn't "add more"—it's "make it sharper." The proposal sprawls too much; I need to collapse everything into a tighter narrative centered on RAPID+RL as the core contribution, properly contextualize it against the clipping work and iw-SFT variants, and cut the excess.

Before I revise, I should verify the actual details on those papers and recent work in this space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46fc30c9-2e78-4d56-a726-8057a2694ac6",
  "isSidechain": false,
  "requestId": "req_011CazVQfVQWoxdTyNpMhDxV",
  "type": "assistant",
  "uuid": "3ad8af79-9658-4eac-be28-3ee9ee8ca3e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdyxCBPBRFqtxCa7JsuXU3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21345,
      "cache_read_input_tokens": 11841,
      "output_tokens": 720,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21345,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 720,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21345
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

_source line 9 · 2026-05-13T11:29:52.136Z_

I'll research the key issues the reviewer raised before revising. Let me search for the missing references and verify claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ad8af79-9658-4eac-be28-3ee9ee8ca3e4",
  "isSidechain": false,
  "requestId": "req_011CazVQfVQWoxdTyNpMhDxV",
  "type": "assistant",
  "uuid": "18ae3b99-9668-43b1-b85a-9d8fa849d95c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdyxCBPBRFqtxCa7JsuXU3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21345,
      "cache_read_input_tokens": 11841,
      "output_tokens": 720,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21345,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 720,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21345
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

_source line 10 · 2026-05-13T11:29:52.222Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BFKv1iVr8w5imHmXbrpC9J`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18ae3b99-9668-43b1-b85a-9d8fa849d95c",
  "isSidechain": false,
  "requestId": "req_011CazVQfVQWoxdTyNpMhDxV",
  "type": "assistant",
  "uuid": "ac8d4ac7-e9f7-48bc-9c88-bc9539029b86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdyxCBPBRFqtxCa7JsuXU3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21345,
      "cache_read_input_tokens": 11841,
      "output_tokens": 720,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21345,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 720,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21345
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

_source line 11 · 2026-05-13T11:29:52.229Z_

<details><summary>↩ Tool result · `toolu_01BFKv1iVr8w5imHmXbrpC9J`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac8d4ac7-e9f7-48bc-9c88-bc9539029b86",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "8ea84e10-2030-49a4-b081-1fe0395383d3",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "ac8d4ac7-e9f7-48bc-9c88-bc9539029b86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-13T11:29:55.762Z_

<details><summary>Logged reasoning block</summary>

```text
Let me search for the key papers and information the reviewer mentioned.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ea84e10-2030-49a4-b081-1fe0395383d3",
  "isSidechain": false,
  "requestId": "req_011CazVSDyYxbZesj7BBajsr",
  "type": "assistant",
  "uuid": "fb359b4b-351d-49cd-8b81-f84d671c54af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxrJPKLQn1iimRX9XVBLzt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1739,
      "cache_read_input_tokens": 33186,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 33186,
          "cache_creation_input_tokens": 1739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1739
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

_source line 13 · 2026-05-13T11:29:56.240Z_

Let me research the key issues raised by the reviewer in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb359b4b-351d-49cd-8b81-f84d671c54af",
  "isSidechain": false,
  "requestId": "req_011CazVSDyYxbZesj7BBajsr",
  "type": "assistant",
  "uuid": "0729a2c9-a9a7-4413-a718-a84516334d46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxrJPKLQn1iimRX9XVBLzt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1739,
      "cache_read_input_tokens": 33186,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 33186,
          "cache_creation_input_tokens": 1739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1739
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

_source line 14 · 2026-05-13T11:29:57.124Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uu7QiASGyKy4yvALN5ayGg`</summary>

```json
{
  "query": "Clipping Low-Probability Tokens SFT Generalizable Initialization RL ICML 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0729a2c9-a9a7-4413-a718-a84516334d46",
  "isSidechain": false,
  "requestId": "req_011CazVSDyYxbZesj7BBajsr",
  "type": "assistant",
  "uuid": "3a6c1c39-8408-4631-a412-d1ce7d6b34f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxrJPKLQn1iimRX9XVBLzt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1739,
      "cache_read_input_tokens": 33186,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 33186,
          "cache_creation_input_tokens": 1739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1739
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

_source line 15 · 2026-05-13T11:30:03.773Z_

<details><summary>↩ Tool result · `toolu_01Uu7QiASGyKy4yvALN5ayGg`</summary>

```text
Web search results for query: "Clipping Low-Probability Tokens SFT Generalizable Initialization RL ICML 2026"

Links: [{"title":"ICML Poster Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL","url":"https://icml.cc/virtual/2026/poster/61171"},{"title":"Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start | OpenReview","url":"https://openreview.net/forum?id=qJLKOryYeR"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"},{"title":"Downloads 2025","url":"https://iclr.cc/Downloads/2025"},{"title":"On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification","url":"https://arxiv.org/html/2508.05629v3"},{"title":"The Synergy of LLMs & RL Unlocks Offline Learning of Generalizable Language-Conditioned Policies with Low-fidelity Data","url":"https://arxiv.org/html/2412.06877"},{"title":"LLMOrbit: A Circular Taxonomy of Large Language Models","url":"https://arxiv.org/pdf/2601.14053"},{"title":"ON THE GENERALIZATION OF SFT: A REINFORCE","url":"https://openreview.net/pdf?id=Lv7PjbcaMi"},{"title":"ICLR 2026 Papers","url":"https://iclr.cc/virtual/2026/papers.html"},{"title":"On the Generalization of SFT: A Reinforcement Learning ...","url":"https://arxiv.org/pdf/2508.05629"}]

I found information about a paper presented at ICML 2026 related to your query. Here are the results:

## Paper: "Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL"

Supervised Fine-Tuning (SFT) is a critical step for adapting Large Language Models (LLMs) to specialized domains, often serving as an initialization for subsequent reinforcement learning (RL). However, SFT can overfit a small set of expert data, harming generalization and eroding prior knowledge.

### Key Findings

Compared with standard SFT, clipping low-probability tokens reduces out-of-distribution forgetting by 11.54% and improves final RL performance by 7.09% across the agentic benchmarks. Moreover, latent-space analysis shows smaller representational drift under clipping, indicating that it provides a generalizable initialization.

### Technical Approach

The degradation primarily results from tokens in the expert data to which the base model assigns low probability. These are framed as 'off-policy' tokens, as they represent a significant deviation from the model's current prior knowledge. Due to the nature of the log-likelihood objective, these off-policy tokens produce larger gradient magnitudes, destabilizing the training process.

The paper is presented as a poster at ICML 2026 and has been available on OpenReview since October 8, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a6c1c39-8408-4631-a412-d1ce7d6b34f6",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "60a82b24-13d5-4782-9631-66e2b1346dbd",
  "toolUseResult": {
    "query": "Clipping Low-Probability Tokens SFT Generalizable Initialization RL ICML 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Um554cPYSX6PWEKeqc5Z65",
        "content": [
          {
            "title": "ICML Poster Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL",
            "url": "https://icml.cc/virtual/2026/poster/61171"
          },
          {
            "title": "Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start | OpenReview",
            "url": "https://openreview.net/forum?id=qJLKOryYeR"
          },
          {
            "title": "ICLR 2026 Orals",
            "url": "https://iclr.cc/virtual/2026/events/oral"
          },
          {
            "title": "Downloads 2025",
            "url": "https://iclr.cc/Downloads/2025"
          },
          {
            "title": "On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification",
            "url": "https://arxiv.org/html/2508.05629v3"
          },
          {
            "title": "The Synergy of LLMs & RL Unlocks Offline Learning of Generalizable Language-Conditioned Policies with Low-fidelity Data",
            "url": "https://arxiv.org/html/2412.06877"
          },
          {
            "title": "LLMOrbit: A Circular Taxonomy of Large Language Models",
            "url": "https://arxiv.org/pdf/2601.14053"
          },
          {
            "title": "ON THE GENERALIZATION OF SFT: A REINFORCE",
            "url": "https://openreview.net/pdf?id=Lv7PjbcaMi"
          },
          {
            "title": "ICLR 2026 Papers",
            "url": "https://iclr.cc/virtual/2026/papers.html"
          },
          {
            "title": "On the Generalization of SFT: A Reinforcement Learning ...",
            "url": "https://arxiv.org/pdf/2508.05629"
          }
        ]
      },
      "I found information about a paper presented at ICML 2026 related to your query. Here are the results:\n\n## Paper: \"Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL\"\n\nSupervised Fine-Tuning (SFT) is a critical step for adapting Large Language Models (LLMs) to specialized domains, often serving as an initialization for subsequent reinforcement learning (RL). However, SFT can overfit a small set of expert data, harming generalization and eroding prior knowledge.\n\n### Key Findings\n\nCompared with standard SFT, clipping low-probability tokens reduces out-of-distribution forgetting by 11.54% and improves final RL performance by 7.09% across the agentic benchmarks. Moreover, latent-space analysis shows smaller representational drift under clipping, indicating that it provides a generalizable initialization.\n\n### Technical Approach\n\nThe degradation primarily results from tokens in the expert data to which the base model assigns low probability. These are framed as 'off-policy' tokens, as they represent a significant deviation from the model's current prior knowledge. Due to the nature of the log-likelihood objective, these off-policy tokens produce larger gradient magnitudes, destabilizing the training process.\n\nThe paper is presented as a poster at ICML 2026 and has been available on OpenReview since October 8, 2025."
    ],
    "durationSeconds": 6.643114544
  },
  "sourceToolAssistantUUID": "3a6c1c39-8408-4631-a412-d1ce7d6b34f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-13T11:30:07.119Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TWKALrRFCpf1dHJ6MtstyV`</summary>

```json
{
  "query": "iw-SFT \"supervised fine tuning curated data reinforcement learning\" EMA auxiliary distribution continuous control arXiv 2507.12856"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60a82b24-13d5-4782-9631-66e2b1346dbd",
  "isSidechain": false,
  "requestId": "req_011CazVT5GT9Bz4DdgUFxsko",
  "type": "assistant",
  "uuid": "82a63f1b-6ba9-4ff0-a52b-24befab7a8e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MueGghstEj5nqont77zFGC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 926,
      "cache_read_input_tokens": 34925,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 926,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 34925,
          "cache_creation_input_tokens": 926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 926
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

_source line 17 · 2026-05-13T11:30:13.138Z_

<details><summary>↩ Tool result · `toolu_01TWKALrRFCpf1dHJ6MtstyV`</summary>

```text
Web search results for query: "iw-SFT "supervised fine tuning curated data reinforcement learning" EMA auxiliary distribution continuous control arXiv 2507.12856"

Links: [{"title":"[2507.12856] Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)","url":"https://arxiv.org/abs/2507.12856"},{"title":"Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)","url":"https://arxiv.org/html/2507.12856v1"},{"title":"Supervised Fine Tuning on Curated Data is Reinforcement ...","url":"https://arxiv.org/pdf/2507.12856"},{"title":"Paper page - Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)","url":"https://huggingface.co/papers/2507.12856"},{"title":"On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification","url":"https://arxiv.org/html/2508.05629v1"},{"title":"Proximal Supervised Fine-Tuning","url":"https://arxiv.org/html/2508.17784v1"},{"title":"Supervised Fine Tuning on Curated Data is Reinforcement ...","url":"https://www.alphaxiv.org/overview/2507.12856v1"},{"title":"Anchored Supervised Fine-Tuning","url":"https://arxiv.org/html/2509.23753"},{"title":"Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved) | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/supervised-fine-tuning-curated-data-is-reinforcement"},{"title":"(PDF) Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)","url":"https://www.researchgate.net/publication/393784242_Supervised_Fine_Tuning_on_Curated_Data_is_Reinforcement_Learning_and_can_be_improved"}]

I found the paper you're looking for. Here's a summary of the research:

The paper examines how Supervised Fine-Tuning (SFT) on curated or filtered data can be understood as maximizing a lower bound on the RL objective in a sparse reward setting, explaining its often-observed good performance.

**Main Contribution:**

The authors introduce an importance weighted variant of SFT called iw-SFT, which optimizes a tighter bound to the RL objective and can improve performance compared to standard SFT on curated data.

**Key Features:**

- The method is easy to implement and can be generalized to training with quality scored data.
- The resulting SFT variants are competitive with more advanced RL algorithms for large language models and for training policies in continuous control tasks.
- The paper achieves 66.7% on the AIME 2024 dataset.

**Theoretical Insight:**

The authors show that one can introduce an adaptive (importance) reweighting scheme (iw-SFT) that asymptotically maximizes the RL objective as the bound tightens over the course of training.

The paper was published on arXiv on July 17, 2025, by authors Chongli Qin and Jost Tobias Springenberg from Independent Research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82a63f1b-6ba9-4ff0-a52b-24befab7a8e2",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "f3cd5dc6-2737-41b1-a6d5-d4091b2cdf4e",
  "toolUseResult": {
    "query": "iw-SFT \"supervised fine tuning curated data reinforcement learning\" EMA auxiliary distribution continuous control arXiv 2507.12856",
    "results": [
      {
        "tool_use_id": "srvtoolu_016HXz6ydENnDXqsWtfyw2i4",
        "content": [
          {
            "title": "[2507.12856] Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)",
            "url": "https://arxiv.org/abs/2507.12856"
          },
          {
            "title": "Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)",
            "url": "https://arxiv.org/html/2507.12856v1"
          },
          {
            "title": "Supervised Fine Tuning on Curated Data is Reinforcement ...",
            "url": "https://arxiv.org/pdf/2507.12856"
          },
          {
            "title": "Paper page - Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)",
            "url": "https://huggingface.co/papers/2507.12856"
          },
          {
            "title": "On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification",
            "url": "https://arxiv.org/html/2508.05629v1"
          },
          {
            "title": "Proximal Supervised Fine-Tuning",
            "url": "https://arxiv.org/html/2508.17784v1"
          },
          {
            "title": "Supervised Fine Tuning on Curated Data is Reinforcement ...",
            "url": "https://www.alphaxiv.org/overview/2507.12856v1"
          },
          {
            "title": "Anchored Supervised Fine-Tuning",
            "url": "https://arxiv.org/html/2509.23753"
          },
          {
            "title": "Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved) | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/supervised-fine-tuning-curated-data-is-reinforcement"
          },
          {
            "title": "(PDF) Supervised Fine Tuning on Curated Data is Reinforcement Learning (and can be improved)",
            "url": "https://www.researchgate.net/publication/393784242_Supervised_Fine_Tuning_on_Curated_Data_is_Reinforcement_Learning_and_can_be_improved"
          }
        ]
      },
      "I found the paper you're looking for. Here's a summary of the research:\n\nThe paper examines how Supervised Fine-Tuning (SFT) on curated or filtered data can be understood as maximizing a lower bound on the RL objective in a sparse reward setting, explaining its often-observed good performance.\n\n**Main Contribution:**\n\nThe authors introduce an importance weighted variant of SFT called iw-SFT, which optimizes a tighter bound to the RL objective and can improve performance compared to standard SFT on curated data.\n\n**Key Features:**\n\n- The method is easy to implement and can be generalized to training with quality scored data.\n- The resulting SFT variants are competitive with more advanced RL algorithms for large language models and for training policies in continuous control tasks.\n- The paper achieves 66.7% on the AIME 2024 dataset.\n\n**Theoretical Insight:**\n\nThe authors show that one can introduce an adaptive (importance) reweighting scheme (iw-SFT) that asymptotically maximizes the RL objective as the bound tightens over the course of training.\n\nThe paper was published on arXiv on July 17, 2025, by authors Chongli Qin and Jost Tobias Springenberg from Independent Research."
    ],
    "durationSeconds": 6.0150304690000045
  },
  "sourceToolAssistantUUID": "82a63f1b-6ba9-4ff0-a52b-24befab7a8e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-13T11:30:19.036Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VbPa9THCyVvHjcHZc1e2uM`</summary>

```json
{
  "url": "https://arxiv.org/html/2507.12856v1",
  "prompt": "Find all details about the EMA update mechanism for the auxiliary distribution q. Specifically: (1) Does the paper use EMA/Polyak averaging for updating q? (2) What is the exact update rule? (3) In which experiments (LLM or continuous control) is EMA used? (4) What EMA decay rate/alpha is used? (5) How is the EMA reference used - for importance weights, loss reweighting, or something else? Extract exact quotes about the EMA mechanism."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3cd5dc6-2737-41b1-a6d5-d4091b2cdf4e",
  "isSidechain": false,
  "requestId": "req_011CazVTmMThNEDRWVmYyLyU",
  "type": "assistant",
  "uuid": "91eeff55-b7a2-4888-abbe-43e92ad94a32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MY4AdK4BBi7URSzbCvCFwD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 35851,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 35851,
          "cache_creation_input_tokens": 936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 936
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

_source line 19 · 2026-05-13T11:30:24.177Z_

<details><summary>↩ Tool result · `toolu_01VbPa9THCyVvHjcHZc1e2uM`</summary>

```text
# EMA Update Mechanism for Auxiliary Distribution q

## (1) Does the paper use EMA/Polyak averaging for updating q?

Yes, the paper uses exponential moving average (EMA) updating, but **only for continuous control experiments**, not for LLM experiments.

## (2) What is the exact update rule?

The precise update formula is:

θ_q = α·θ_q + (1−α)·θ

## (3) In which experiments is EMA used?

**Continuous control only.** The paper states: "instead of updating the importance weighting distribution q at discrete time-points we use exponential weight averaging θ_q = α·θ_q + (1−α)·θ during each step of the optimization."

For LLM experiments, the paper uses a different approach with discrete time-lagged updates rather than continuous EMA.

## (4) What EMA decay rate/alpha is used?

The paper **does not specify the exact alpha value** for the continuous control experiments. It mentions the update rule but does not provide the hyperparameter in the main text or visible appendix sections.

## (5) How is the EMA reference used?

The EMA-updated θ_q defines the auxiliary distribution q(τ), which is then used to **compute importance weights** for reweighting training examples: q(τ)/π_ref(τ).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91eeff55-b7a2-4888-abbe-43e92ad94a32",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "84b4aa80-9289-4d88-9ffd-24dc4bbedabb",
  "toolUseResult": {
    "bytes": 928094,
    "code": 200,
    "codeText": "OK",
    "result": "# EMA Update Mechanism for Auxiliary Distribution q\n\n## (1) Does the paper use EMA/Polyak averaging for updating q?\n\nYes, the paper uses exponential moving average (EMA) updating, but **only for continuous control experiments**, not for LLM experiments.\n\n## (2) What is the exact update rule?\n\nThe precise update formula is:\n\nθ_q = α·θ_q + (1−α)·θ\n\n## (3) In which experiments is EMA used?\n\n**Continuous control only.** The paper states: \"instead of updating the importance weighting distribution q at discrete time-points we use exponential weight averaging θ_q = α·θ_q + (1−α)·θ during each step of the optimization.\"\n\nFor LLM experiments, the paper uses a different approach with discrete time-lagged updates rather than continuous EMA.\n\n## (4) What EMA decay rate/alpha is used?\n\nThe paper **does not specify the exact alpha value** for the continuous control experiments. It mentions the update rule but does not provide the hyperparameter in the main text or visible appendix sections.\n\n## (5) How is the EMA reference used?\n\nThe EMA-updated θ_q defines the auxiliary distribution q(τ), which is then used to **compute importance weights** for reweighting training examples: q(τ)/π_ref(τ).",
    "durationMs": 5137,
    "url": "https://arxiv.org/html/2507.12856v1"
  },
  "sourceToolAssistantUUID": "91eeff55-b7a2-4888-abbe-43e92ad94a32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"RAPID: Reducible-Loss Adaptive Prioritized Replay for VLA Imitation Le…",
  "leafUuid": "84b4aa80-9289-4d88-9ffd-24dc4bbedabb",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising RAPID: Addressing novelty gaps and clarifying SFT→RL contribution",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---

### Tool call

_source line 22 · 2026-05-13T11:30:28.399Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XbVDXbC7sBKVTFB7FEeihM`</summary>

```json
{
  "query": "SFT data quality affects downstream RL performance VLA robot learning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84b4aa80-9289-4d88-9ffd-24dc4bbedabb",
  "isSidechain": false,
  "requestId": "req_011CazVUaX7zE4iSgFGcCXo7",
  "type": "assistant",
  "uuid": "161e5f7d-4387-49d9-8710-df100c400922",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SeCkGFhLuFUGHTZL8ys4Eq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 36787,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 523,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 36787,
          "cache_creation_input_tokens": 523,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 523
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

_source line 23 · 2026-05-13T11:30:35.580Z_

<details><summary>↩ Tool result · `toolu_01XbVDXbC7sBKVTFB7FEeihM`</summary>

```text
Web search results for query: "SFT data quality affects downstream RL performance VLA robot learning 2025 2026"

Links: [{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/html/2509.09674v1"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/html/2603.26666"},{"title":"VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/html/2505.18719v1"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://arxiv.org/html/2505.19789v4"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://rlvla.github.io/"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview","url":"https://openreview.net/forum?id=eUGoqrZ6Ea"},{"title":"Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning","url":"https://arxiv.org/html/2602.10503"},{"title":"Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)","url":"https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"},{"title":"SIMPLEVLA-RL: SCALING VLA TRAINING VIA RE","url":"https://openreview.net/pdf/ec4796d06d4fb6583b2800d1782e89edf90d594e.pdf"},{"title":"[2504.11468] SFT or RL? An Early Investigation into Training R1-Like Reasoning Large Vision-Language Models","url":"https://arxiv.org/abs/2504.11468"}]

Based on the web search results, I found several recent research papers (2025-2026) that directly address how SFT (Supervised Fine-Tuning) data quality affects downstream RL (Reinforcement Learning) performance in VLA (Vision-Language-Action) robot learning:

## Key Findings:

**SFT Limitations and Data Quality Issues:**

The current SFT of VLAs typically relies on limited, scene- and task-specific data, which creates significant challenges. Minor deviations from expert trajectories can accumulate, steering the policy into unfamiliar states and undermining robust performance.

**SFT's Negative Impact on Downstream RL:**

A particularly important finding comes from recent research on reasoning models: SFT can significantly undermine subsequent RL by inducing "pseudo reasoning paths" imitated from expert models. While SFT helps models learn reasoning formats, it often locks aligned models into imitative, rigid reasoning modes that impede further learning.

**RL as a Solution:**

Actions generated by RL agents are distributed more uniformly across the entire action space, which enables RL policies to adapt to a wider variety of states. As a result, the policy trained on RL-collected data exhibits stronger robustness than the SFT model trained on offline data.

**Practical Performance Gains:**

The research demonstrates substantial improvements when combining proper SFT with RL: RL performs comparably to SFT-16k in the training setting and 42.6% better on unseen objects and tables.

These findings suggest that while SFT is necessary as an initialization step, high-quality SFT data and awareness of its limitations are crucial for effective downstream RL training in VLA robot learning systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "161e5f7d-4387-49d9-8710-df100c400922",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "6a7a0d5d-b996-4cad-bd97-3ad3e4ac8fef",
  "toolUseResult": {
    "query": "SFT data quality affects downstream RL performance VLA robot learning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LeL7AcufTWTpRLquX93g8t",
        "content": [
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://arxiv.org/html/2509.09674v1"
          },
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation",
            "url": "https://arxiv.org/html/2603.26666"
          },
          {
            "title": "VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning",
            "url": "https://arxiv.org/html/2505.18719v1"
          },
          {
            "title": "What Can RL Bring to VLA Generalization? An Empirical Study",
            "url": "https://arxiv.org/html/2505.19789v4"
          },
          {
            "title": "What Can RL Bring to VLA Generalization? An Empirical Study",
            "url": "https://rlvla.github.io/"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview",
            "url": "https://openreview.net/forum?id=eUGoqrZ6Ea"
          },
          {
            "title": "Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning",
            "url": "https://arxiv.org/html/2602.10503"
          },
          {
            "title": "Rohit Bandaru | Foundation Models for Robotics: Vision-Language-Action (VLA)",
            "url": "https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/"
          },
          {
            "title": "SIMPLEVLA-RL: SCALING VLA TRAINING VIA RE",
            "url": "https://openreview.net/pdf/ec4796d06d4fb6583b2800d1782e89edf90d594e.pdf"
          },
          {
            "title": "[2504.11468] SFT or RL? An Early Investigation into Training R1-Like Reasoning Large Vision-Language Models",
            "url": "https://arxiv.org/abs/2504.11468"
          }
        ]
      },
      "Based on the web search results, I found several recent research papers (2025-2026) that directly address how SFT (Supervised Fine-Tuning) data quality affects downstream RL (Reinforcement Learning) performance in VLA (Vision-Language-Action) robot learning:\n\n## Key Findings:\n\n**SFT Limitations and Data Quality Issues:**\n\nThe current SFT of VLAs typically relies on limited, scene- and task-specific data, which creates significant challenges. Minor deviations from expert trajectories can accumulate, steering the policy into unfamiliar states and undermining robust performance.\n\n**SFT's Negative Impact on Downstream RL:**\n\nA particularly important finding comes from recent research on reasoning models: SFT can significantly undermine subsequent RL by inducing \"pseudo reasoning paths\" imitated from expert models. While SFT helps models learn reasoning formats, it often locks aligned models into imitative, rigid reasoning modes that impede further learning.\n\n**RL as a Solution:**\n\nActions generated by RL agents are distributed more uniformly across the entire action space, which enables RL policies to adapt to a wider variety of states. As a result, the policy trained on RL-collected data exhibits stronger robustness than the SFT model trained on offline data.\n\n**Practical Performance Gains:**\n\nThe research demonstrates substantial improvements when combining proper SFT with RL: RL performs comparably to SFT-16k in the training setting and 42.6% better on unseen objects and tables.\n\nThese findings suggest that while SFT is necessary as an initialization step, high-quality SFT data and awareness of its limitations are crucial for effective downstream RL training in VLA robot learning systems."
    ],
    "durationSeconds": 7.176548404000008
  },
  "sourceToolAssistantUUID": "161e5f7d-4387-49d9-8710-df100c400922",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-13T11:30:38.291Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fu9kuU53fZDUG69ZStEwHY`</summary>

```json
{
  "query": "\"SFT quality\" OR \"SFT data quality\" \"reinforcement learning\" downstream initialization 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a7a0d5d-b996-4cad-bd97-3ad3e4ac8fef",
  "isSidechain": false,
  "requestId": "req_011CazVVRG2tugNCj7Rxq7Cw",
  "type": "assistant",
  "uuid": "e762c473-0d98-4523-8fa8-cfc6b17f816d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbVRsQnCwWFAttYpPwBTuA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1004,
      "cache_read_input_tokens": 37310,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1004,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 37310,
          "cache_creation_input_tokens": 1004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1004
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

_source line 25 · 2026-05-13T11:30:48.553Z_

<details><summary>↩ Tool result · `toolu_01Fu9kuU53fZDUG69ZStEwHY`</summary>

```text
Web search results for query: ""SFT quality" OR "SFT data quality" "reinforcement learning" downstream initialization 2026 arXiv"

Links: [{"title":"On the Generalization of SFT: A Reinforcement Learning ...","url":"https://arxiv.org/pdf/2508.05629"},{"title":"SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning","url":"https://arxiv.org/html/2506.19767v1"},{"title":"GitHub - yongliang-wu/DFT: [ICLR 2026] On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification. · GitHub","url":"https://github.com/yongliang-wu/DFT"},{"title":"Published as a workshop paper at ICLR 2026","url":"https://arxiv.org/pdf/2603.03517"},{"title":"On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification","url":"https://arxiv.org/html/2508.05629v2"},{"title":"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning","url":"https://arxiv.org/html/2511.12429"},{"title":"PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning","url":"https://arxiv.org/html/2604.28123"},{"title":"[2501.17161] SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training","url":"https://arxiv.org/abs/2501.17161"},{"title":"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs","url":"https://arxiv.org/html/2508.16546v1"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2512.20745"}]

Based on the web search results, I found several highly relevant 2026 arXiv papers examining SFT quality and its relationship with reinforcement learning and downstream initialization:

## Key Papers Found:

**1. "On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification"** (arXiv:2508.05629, ICLR 2026)
This work presents a theoretically motivated improvement to SFT for LLMs by revealing that standard SFT gradients implicitly encode a problematic reward structure that restricts generalization capabilities, and proposes Dynamic Fine-Tuning (DFT) which stabilizes gradient updates by dynamically rescaling the objective function with token probability. With just a single-line change, the method outperforms standard SFT on multiple difficult benchmarks across math reasoning, code generation and multi-modal tasks.

**2. "SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning"** (arXiv:2506.19767, June 2025)
This paper shows that SFT exhibits greater distribution changes from the base model compared to RL, and that RL fine-tuning operates within a neighborhood of the initialization point.

**3. "Tailored Primitive Initialization is the Secret Key to Reinforcement Learning"** (arXiv:2511.12429, November 2025)
This research demonstrates that the distribution of thinking tokens in the SFT dataset strongly influences downstream RL reasoning performance, showing that different SFT datasets with different reasoning chain patterns can produce dramatically divergent RL performance even though both patterns are valid. The authors introduce the Tailor pipeline, which automatically curates a reasoning-diverse SFT dataset to better initialize models for subsequent RL training, improving the quality and diversity of reasoning demonstrations.

**4. "PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning"** (arXiv:2604.28123, recent)
This work addresses how SFT introduces distributional drift between the policy and supervision distribution, and proposes an alignment stage using on-policy distillation to repair this drift and provide a stronger initialization for downstream RLVR.

These papers collectively highlight that SFT quality directly impacts downstream RL initialization and performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e762c473-0d98-4523-8fa8-cfc6b17f816d",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "f809cd7c-6adb-43dc-917b-a1f60d054b38",
  "toolUseResult": {
    "query": "\"SFT quality\" OR \"SFT data quality\" \"reinforcement learning\" downstream initialization 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SrhY6XYXaBzGvfwLsyJqBs",
        "content": [
          {
            "title": "On the Generalization of SFT: A Reinforcement Learning ...",
            "url": "https://arxiv.org/pdf/2508.05629"
          },
          {
            "title": "SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning",
            "url": "https://arxiv.org/html/2506.19767v1"
          },
          {
            "title": "GitHub - yongliang-wu/DFT: [ICLR 2026] On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification. · GitHub",
            "url": "https://github.com/yongliang-wu/DFT"
          },
          {
            "title": "Published as a workshop paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2603.03517"
          },
          {
            "title": "On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification",
            "url": "https://arxiv.org/html/2508.05629v2"
          },
          {
            "title": "Tailored Primitive Initialization is the Secret Key to Reinforcement Learning",
            "url": "https://arxiv.org/html/2511.12429"
          },
          {
            "title": "PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning",
            "url": "https://arxiv.org/html/2604.28123"
          },
          {
            "title": "[2501.17161] SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training",
            "url": "https://arxiv.org/abs/2501.17161"
          },
          {
            "title": "RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs",
            "url": "https://arxiv.org/html/2508.16546v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2512.20745"
          }
        ]
      },
      "Based on the web search results, I found several highly relevant 2026 arXiv papers examining SFT quality and its relationship with reinforcement learning and downstream initialization:\n\n## Key Papers Found:\n\n**1. \"On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification\"** (arXiv:2508.05629, ICLR 2026)\nThis work presents a theoretically motivated improvement to SFT for LLMs by revealing that standard SFT gradients implicitly encode a problematic reward structure that restricts generalization capabilities, and proposes Dynamic Fine-Tuning (DFT) which stabilizes gradient updates by dynamically rescaling the objective function with token probability. With just a single-line change, the method outperforms standard SFT on multiple difficult benchmarks across math reasoning, code generation and multi-modal tasks.\n\n**2. \"SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning\"** (arXiv:2506.19767, June 2025)\nThis paper shows that SFT exhibits greater distribution changes from the base model compared to RL, and that RL fine-tuning operates within a neighborhood of the initialization point.\n\n**3. \"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning\"** (arXiv:2511.12429, November 2025)\nThis research demonstrates that the distribution of thinking tokens in the SFT dataset strongly influences downstream RL reasoning performance, showing that different SFT datasets with different reasoning chain patterns can produce dramatically divergent RL performance even though both patterns are valid. The authors introduce the Tailor pipeline, which automatically curates a reasoning-diverse SFT dataset to better initialize models for subsequent RL training, improving the quality and diversity of reasoning demonstrations.\n\n**4. \"PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning\"** (arXiv:2604.28123, recent)\nThis work addresses how SFT introduces distributional drift between the policy and supervision distribution, and proposes an alignment stage using on-policy distillation to repair this drift and provide a stronger initialization for downstream RLVR.\n\nThese papers collectively highlight that SFT quality directly impacts downstream RL initialization and performance."
    ],
    "durationSeconds": 10.258382073999993
  },
  "sourceToolAssistantUUID": "e762c473-0d98-4523-8fa8-cfc6b17f816d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-13T11:30:52.290Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UNws9GC9sN8ngRGDpYCZfL`</summary>

```json
{
  "query": "OpenReview \"clipping low-probability tokens\" SFT RL initialization off-policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f809cd7c-6adb-43dc-917b-a1f60d054b38",
  "isSidechain": false,
  "requestId": "req_011CazVWNnjTAGmvY98SVKyN",
  "type": "assistant",
  "uuid": "b3fc8fdc-7307-4c35-886b-ff2c712c2728",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YdKvBvvKzfybgfnPkMA4J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 38314,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1142,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 38314,
          "cache_creation_input_tokens": 1142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1142
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

_source line 27 · 2026-05-13T11:30:56.452Z_

<details><summary>↩ Tool result · `toolu_01UNws9GC9sN8ngRGDpYCZfL`</summary>

```text
Web search results for query: "OpenReview "clipping low-probability tokens" SFT RL initialization off-policy"

Links: [{"title":"ICML Poster Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL","url":"https://icml.cc/virtual/2026/poster/61171"}]

I found a highly relevant result for your query. The search returned an ICML 2026 poster presentation about clipping low-probability tokens in SFT for RL initialization.

**Key Findings:**

The research addresses how Supervised Fine-Tuning (SFT) serves as an initialization for reinforcement learning, but SFT can overfit small sets of expert data, harming generalization and eroding prior knowledge, which limits downstream RL that benefits from a strong, generalizable initialization.

The paper demonstrates that prior knowledge degradation primarily results from tokens in expert data assigned low probability by the base model, which represent significant deviations from the model's prior knowledge and produce larger gradient magnitudes that speed up adaptation but degrade generalization.

The authors study a token-wise clipping strategy as a trust-region method for bounding per-token updates, finding that it reshapes token-level learning priorities for more progressive adaptation.

**Results:**

Compared with standard SFT, clipping low-probability tokens reduces out-of-distribution forgetting by 11.54% and improves final RL performance by 7.09% across agentic benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3fc8fdc-7307-4c35-886b-ff2c712c2728",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "93c2a8cf-6e3b-4a89-b793-5fb086686c0e",
  "toolUseResult": {
    "query": "OpenReview \"clipping low-probability tokens\" SFT RL initialization off-policy",
    "results": [
      {
        "tool_use_id": "srvtoolu_0114VUhiivbeCunNiRreVjmp",
        "content": [
          {
            "title": "ICML Poster Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL",
            "url": "https://icml.cc/virtual/2026/poster/61171"
          }
        ]
      },
      "I found a highly relevant result for your query. The search returned an ICML 2026 poster presentation about clipping low-probability tokens in SFT for RL initialization.\n\n**Key Findings:**\n\nThe research addresses how Supervised Fine-Tuning (SFT) serves as an initialization for reinforcement learning, but SFT can overfit small sets of expert data, harming generalization and eroding prior knowledge, which limits downstream RL that benefits from a strong, generalizable initialization.\n\nThe paper demonstrates that prior knowledge degradation primarily results from tokens in expert data assigned low probability by the base model, which represent significant deviations from the model's prior knowledge and produce larger gradient magnitudes that speed up adaptation but degrade generalization.\n\nThe authors study a token-wise clipping strategy as a trust-region method for bounding per-token updates, finding that it reshapes token-level learning priorities for more progressive adaptation.\n\n**Results:**\n\nCompared with standard SFT, clipping low-probability tokens reduces out-of-distribution forgetting by 11.54% and improves final RL performance by 7.09% across agentic benchmarks."
    ],
    "durationSeconds": 4.15227941599999
  },
  "sourceToolAssistantUUID": "b3fc8fdc-7307-4c35-886b-ff2c712c2728",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-13T11:31:02.395Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Hsr5SWQ25siChCzBKf8Ea8`</summary>

```json
{
  "url": "https://openreview.net/forum?id=qJLKOryYeR",
  "prompt": "Extract the following details about this paper: (1) Full title and authors, (2) What specific benchmarks/environments are used (ALFWorld, ScienceWorld, etc.)? (3) What is the exact clipping mechanism? (4) What base models are used? (5) What RL algorithm is applied after SFT? (6) Is this about LLMs or VLAs? (7) Any mention of data quality, data curation, or demonstration quality? (8) The arXiv ID if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93c2a8cf-6e3b-4a89-b793-5fb086686c0e",
  "isSidechain": false,
  "requestId": "req_011CazVWxXWAjvn6KxT33o8f",
  "type": "assistant",
  "uuid": "18bbef51-229c-4624-8499-f1093c283842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZcgqooVjrDL3cHRUp6dGZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 444,
      "cache_read_input_tokens": 39456,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 444,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 39456,
          "cache_creation_input_tokens": 444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 444
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

_source line 29 · 2026-05-13T11:31:07.137Z_

<details><summary>↩ Tool result · `toolu_01Hsr5SWQ25siChCzBKf8Ea8`</summary>

```text
# Paper Details Extraction

**(1) Title and Authors:**
"Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start" by Tian-Shuo Liu, Chengxing Jia, Haoyu Liu, Pengyuan Wang, Shiyuan Zhang, Jie Fu, and Yang Yu.

**(2) Benchmarks/Environments:**
The paper evaluates on ALFWorld and ScienceWorld, described as "agentic benchmarks."

**(3) Clipping Mechanism:**
The document mentions a "clipping strategy" that "constrains per-token updates within a trust region" and "moderates the learning process by constraining gradient updates from off-policy tokens." However, specific implementation details are not provided in this excerpt.

**(4) Base Models:**
Not specified in the provided content.

**(5) RL Algorithm:**
The document does not identify which RL algorithm is applied after SFT.

**(6) LLMs or VLAs:**
This concerns Large Language Models (LLMs), not Vision-Language Models.

**(7) Data Quality/Curation:**
The abstract references "expert data" but does not discuss data quality, curation methods, or demonstration quality explicitly.

**(8) ArXiv ID:**
Not available. The submission is identified as OpenReview submission number 19335 for ICLR 2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18bbef51-229c-4624-8499-f1093c283842",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "ae553d1b-8f8b-4fc1-81ab-cce45c02c2fe",
  "toolUseResult": {
    "bytes": 72301,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Details Extraction\n\n**(1) Title and Authors:**\n\"Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start\" by Tian-Shuo Liu, Chengxing Jia, Haoyu Liu, Pengyuan Wang, Shiyuan Zhang, Jie Fu, and Yang Yu.\n\n**(2) Benchmarks/Environments:**\nThe paper evaluates on ALFWorld and ScienceWorld, described as \"agentic benchmarks.\"\n\n**(3) Clipping Mechanism:**\nThe document mentions a \"clipping strategy\" that \"constrains per-token updates within a trust region\" and \"moderates the learning process by constraining gradient updates from off-policy tokens.\" However, specific implementation details are not provided in this excerpt.\n\n**(4) Base Models:**\nNot specified in the provided content.\n\n**(5) RL Algorithm:**\nThe document does not identify which RL algorithm is applied after SFT.\n\n**(6) LLMs or VLAs:**\nThis concerns Large Language Models (LLMs), not Vision-Language Models.\n\n**(7) Data Quality/Curation:**\nThe abstract references \"expert data\" but does not discuss data quality, curation methods, or demonstration quality explicitly.\n\n**(8) ArXiv ID:**\nNot available. The submission is identified as OpenReview submission number 19335 for ICLR 2026.",
    "durationMs": 4741,
    "url": "https://openreview.net/forum?id=qJLKOryYeR"
  },
  "sourceToolAssistantUUID": "18bbef51-229c-4624-8499-f1093c283842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-13T11:31:07.140Z_

```json
{
  "parentUuid": "ae553d1b-8f8b-4fc1-81ab-cce45c02c2fe",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "86c67ad9-18c6-4694-aa5b-8896cc4e32a8",
  "timestamp": "2026-05-13T11:31:07.140Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-13T11:31:10.255Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DDpVUCAMT8VcvXeKUfrTVB`</summary>

```json
{
  "query": "arXiv \"off-policy token clipped supervised fine-tuning\" OR \"clipping low-probability tokens SFT\" Tian-Shuo Liu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86c67ad9-18c6-4694-aa5b-8896cc4e32a8",
  "isSidechain": false,
  "requestId": "req_011CazVXkAPfUaUNHrTeRL3p",
  "type": "assistant",
  "uuid": "6cf03e33-05c3-4a24-97d1-92089c59c72a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8WeqSxjrcMujxFXuABDX4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 648,
      "cache_read_input_tokens": 39900,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 648,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 39900,
          "cache_creation_input_tokens": 648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 648
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

_source line 32 · 2026-05-13T11:31:15.938Z_

<details><summary>↩ Tool result · `toolu_01DDpVUCAMT8VcvXeKUfrTVB`</summary>

```text
Web search results for query: "arXiv "off-policy token clipped supervised fine-tuning" OR "clipping low-probability tokens SFT" Tian-Shuo Liu"

Links: [{"title":"Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority","url":"https://www.arxiv.org/pdf/2602.01227"},{"title":"[2509.16596] Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels","url":"https://arxiv.org/abs/2509.16596"},{"title":"[2508.11408] On-Policy RL Meets Off-Policy Experts: Harmonizing Supervised Fine-Tuning and Reinforcement Learning via Dynamic Weighting","url":"https://arxiv.org/abs/2508.11408"},{"title":"[2509.15157] Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning","url":"https://arxiv.org/abs/2509.15157"},{"title":"Proximal Supervised Fine-Tuning PROXIMAL SUPERVISED FINE-TUNING","url":"https://arxiv.org/pdf/2508.17784"},{"title":"Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning","url":"https://arxiv.org/html/2509.15157v1"},{"title":"SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning","url":"https://arxiv.org/html/2506.19767v1"},{"title":"One-Token Rollout: Guiding Supervised Fine-Tuning of LLMs with Policy Gradient","url":"https://arxiv.org/html/2509.26313"},{"title":"Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority","url":"https://arxiv.org/html/2602.01227"},{"title":"Harmonizing Supervised Fine-Tuning and Reinforcement ...","url":"https://arxiv.org/pdf/2508.11408"}]

The search results include several papers related to off-policy supervised fine-tuning and token clipping mechanisms. While I found papers on related topics like "Proximal Supervised Fine-Tuning" (PSFT) with token clipping and papers on off-policy SFT, I did not find a specific paper with the exact titles you mentioned or explicitly by Tian-Shuo Liu with those exact terms.

The closest match in the results is the "Proximal Supervised Fine-Tuning" paper which discusses clipped tokens during training and notes that clipped tokens concentrate on uncertain words, with this clipping mechanism defining a soft trust region that prevents destructive updates.

Additionally, there are references to research where the model can "clip" updates on tokens where policy divergence is excessive while accelerating learning on tokens within the trust region.

If you're looking for a specific paper by Tian-Shuo Liu, you may want to try a more direct search on arXiv with the author's name, or provide additional details about the paper (such as the arXiv ID or publication date).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cf03e33-05c3-4a24-97d1-92089c59c72a",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "5ae68f6c-7965-4ca0-8944-1c90d2956b98",
  "toolUseResult": {
    "query": "arXiv \"off-policy token clipped supervised fine-tuning\" OR \"clipping low-probability tokens SFT\" Tian-Shuo Liu",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XNUgxGaTKw1azMsWsuS7hm",
        "content": [
          {
            "title": "Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority",
            "url": "https://www.arxiv.org/pdf/2602.01227"
          },
          {
            "title": "[2509.16596] Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels",
            "url": "https://arxiv.org/abs/2509.16596"
          },
          {
            "title": "[2508.11408] On-Policy RL Meets Off-Policy Experts: Harmonizing Supervised Fine-Tuning and Reinforcement Learning via Dynamic Weighting",
            "url": "https://arxiv.org/abs/2508.11408"
          },
          {
            "title": "[2509.15157] Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning",
            "url": "https://arxiv.org/abs/2509.15157"
          },
          {
            "title": "Proximal Supervised Fine-Tuning PROXIMAL SUPERVISED FINE-TUNING",
            "url": "https://arxiv.org/pdf/2508.17784"
          },
          {
            "title": "Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning",
            "url": "https://arxiv.org/html/2509.15157v1"
          },
          {
            "title": "SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning",
            "url": "https://arxiv.org/html/2506.19767v1"
          },
          {
            "title": "One-Token Rollout: Guiding Supervised Fine-Tuning of LLMs with Policy Gradient",
            "url": "https://arxiv.org/html/2509.26313"
          },
          {
            "title": "Supervised Fine-Tuning Needs to Unlock the Potential of Token Priority",
            "url": "https://arxiv.org/html/2602.01227"
          },
          {
            "title": "Harmonizing Supervised Fine-Tuning and Reinforcement ...",
            "url": "https://arxiv.org/pdf/2508.11408"
          }
        ]
      },
      "The search results include several papers related to off-policy supervised fine-tuning and token clipping mechanisms. While I found papers on related topics like \"Proximal Supervised Fine-Tuning\" (PSFT) with token clipping and papers on off-policy SFT, I did not find a specific paper with the exact titles you mentioned or explicitly by Tian-Shuo Liu with those exact terms.\n\nThe closest match in the results is the \"Proximal Supervised Fine-Tuning\" paper which discusses clipped tokens during training and notes that clipped tokens concentrate on uncertain words, with this clipping mechanism defining a soft trust region that prevents destructive updates.\n\nAdditionally, there are references to research where the model can \"clip\" updates on tokens where policy divergence is excessive while accelerating learning on tokens within the trust region.\n\nIf you're looking for a specific paper by Tian-Shuo Liu, you may want to try a more direct search on arXiv with the author's name, or provide additional details about the paper (such as the arXiv ID or publication date)."
    ],
    "durationSeconds": 5.67937449799999
  },
  "sourceToolAssistantUUID": "6cf03e33-05c3-4a24-97d1-92089c59c72a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"RAPID: Reducible-Loss Adaptive Prioritized Replay for VLA Imitation Le…",
  "leafUuid": "5ae68f6c-7965-4ca0-8944-1c90d2956b98",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising RAPID: Addressing novelty gaps and clarifying SFT→RL contribution",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---

### Tool call

_source line 35 · 2026-05-13T11:31:18.759Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xk1WmbRpeZGZQ1CLRQppF6`</summary>

```json
{
  "query": "reducible loss prioritized sampling supervised learning imitation learning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ae68f6c-7965-4ca0-8944-1c90d2956b98",
  "isSidechain": false,
  "requestId": "req_011CazVYPp49aJoPd6tDVtGV",
  "type": "assistant",
  "uuid": "7a6aa4ff-dd9a-4a7e-a4c0-de110d1b0555",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XWY3Lg1GuDve9ZCC9tmPF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 862,
      "cache_read_input_tokens": 40548,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 862,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 40548,
          "cache_creation_input_tokens": 862,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 862
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

_source line 36 · 2026-05-13T11:31:26.363Z_

<details><summary>↩ Tool result · `toolu_01Xk1WmbRpeZGZQ1CLRQppF6`</summary>

```text
Web search results for query: "reducible loss prioritized sampling supervised learning imitation learning 2025 2026"

Links: [{"title":"[2208.10483] Prioritizing Samples in Reinforcement Learning with Reducible Loss","url":"https://arxiv.org/abs/2208.10483"},{"title":"Prioritized sampling for scalable neural network solutions to complex partial differential equations | Computational and Applied Mathematics | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40314-026-03723-3"},{"title":"Combining Imitation Learning and Reinforcement Learning Using DQfD","url":"https://danieltakeshi.github.io/2019/04/30/il-and-rl/"},{"title":"A Reduction of Imitation Learning and Structured Prediction to ...","url":"https://www.cs.cmu.edu/~sross1/publications/Ross-AIStats11-NoRegret.pdf"},{"title":"Harmonizing Supervised Fine-Tuning and Reinforcement ...","url":"https://arxiv.org/pdf/2508.11408"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=BdmVgLMvaf"},{"title":"GitHub - yingchengyang/Reinforcement-Learning-Papers: Related papers for reinforcement learning, including classic papers and latest papers in top conferences · GitHub","url":"https://github.com/yingchengyang/Reinforcement-Learning-Papers"},{"title":"A Reduction of Imitation Learning and Structured Prediction","url":"https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf"},{"title":"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://proceedings.mlr.press/v15/ross11a.html"}]

Based on the web search results, here's what I found related to your query:

## Key Research Findings

**Reducible Loss in Sampling:**

A method proposes prioritizing samples based on how much can be learned from them, defining "learn-ability" of a sample as the steady decrease of the training loss associated with that sample over time. This approach specifically addresses prioritized sampling using reducible loss concepts in reinforcement learning contexts.

**Recent Work on Prioritized Sampling (2025-2026):**

There is recent research on "Prioritized sampling for scalable neural network solutions to complex partial differential equations" published in 2026. This work introduces a novel probability distribution for adaptive sampling that dynamically concentrates computational effort in regions where the solution exhibits complex behavior and requires higher information density.

**Integration with Imitation Learning:**

A method called SASR (2025) probabilistically interleaves supervised fine-tuning and reinforcement learning steps, prioritizing supervised fine-tuning when the model's outputs are dissimilar to expert demonstrations, adapting the training focus dynamically.

**Prioritized Experience Replay in Learning:**

Prioritized experience replay is used to sample demonstration data in imitation learning contexts. Additionally, uncertainty sampling-based methods that prioritize sampling data points having high predictive uncertainty of the classifier are relevant to prioritization strategies.

The search results show active research in 2025-2026 combining prioritized sampling strategies with both supervised and reinforcement learning approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a6aa4ff-dd9a-4a7e-a4c0-de110d1b0555",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "43328543-a9fc-4c53-9f3e-16313f61a8d5",
  "toolUseResult": {
    "query": "reducible loss prioritized sampling supervised learning imitation learning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0142WEZZaUzARtaW14yHikso",
        "content": [
          {
            "title": "[2208.10483] Prioritizing Samples in Reinforcement Learning with Reducible Loss",
            "url": "https://arxiv.org/abs/2208.10483"
          },
          {
            "title": "Prioritized sampling for scalable neural network solutions to complex partial differential equations | Computational and Applied Mathematics | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s40314-026-03723-3"
          },
          {
            "title": "Combining Imitation Learning and Reinforcement Learning Using DQfD",
            "url": "https://danieltakeshi.github.io/2019/04/30/il-and-rl/"
          },
          {
            "title": "A Reduction of Imitation Learning and Structured Prediction to ...",
            "url": "https://www.cs.cmu.edu/~sross1/publications/Ross-AIStats11-NoRegret.pdf"
          },
          {
            "title": "Harmonizing Supervised Fine-Tuning and Reinforcement ...",
            "url": "https://arxiv.org/pdf/2508.11408"
          },
          {
            "title": "ICLR 2025 Papers",
            "url": "https://iclr.cc/virtual/2025/papers.html"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://openreview.net/pdf?id=BdmVgLMvaf"
          },
          {
            "title": "GitHub - yingchengyang/Reinforcement-Learning-Papers: Related papers for reinforcement learning, including classic papers and latest papers in top conferences · GitHub",
            "url": "https://github.com/yingchengyang/Reinforcement-Learning-Papers"
          },
          {
            "title": "A Reduction of Imitation Learning and Structured Prediction",
            "url": "https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf"
          },
          {
            "title": "A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning",
            "url": "https://proceedings.mlr.press/v15/ross11a.html"
          }
        ]
      },
      "Based on the web search results, here's what I found related to your query:\n\n## Key Research Findings\n\n**Reducible Loss in Sampling:**\n\nA method proposes prioritizing samples based on how much can be learned from them, defining \"learn-ability\" of a sample as the steady decrease of the training loss associated with that sample over time. This approach specifically addresses prioritized sampling using reducible loss concepts in reinforcement learning contexts.\n\n**Recent Work on Prioritized Sampling (2025-2026):**\n\nThere is recent research on \"Prioritized sampling for scalable neural network solutions to complex partial differential equations\" published in 2026. This work introduces a novel probability distribution for adaptive sampling that dynamically concentrates computational effort in regions where the solution exhibits complex behavior and requires higher information density.\n\n**Integration with Imitation Learning:**\n\nA method called SASR (2025) probabilistically interleaves supervised fine-tuning and reinforcement learning steps, prioritizing supervised fine-tuning when the model's outputs are dissimilar to expert demonstrations, adapting the training focus dynamically.\n\n**Prioritized Experience Replay in Learning:**\n\nPrioritized experience replay is used to sample demonstration data in imitation learning contexts. Additionally, uncertainty sampling-based methods that prioritize sampling data points having high predictive uncertainty of the classifier are relevant to prioritization strategies.\n\nThe search results show active research in 2025-2026 combining prioritized sampling strategies with both supervised and reinforcement learning approaches."
    ],
    "durationSeconds": 7.599294213999994
  },
  "sourceToolAssistantUUID": "7a6aa4ff-dd9a-4a7e-a4c0-de110d1b0555",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-13T11:31:29.649Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019iTiDoQCemgFFFPvW4ts7a`</summary>

```json
{
  "query": "EMA reference model data selection training adaptive online sample selection 2025 2026 NeurIPS ICML ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43328543-a9fc-4c53-9f3e-16313f61a8d5",
  "isSidechain": false,
  "requestId": "req_011CazVZATQgMLtNiMe3wxPh",
  "type": "assistant",
  "uuid": "1c837457-61f6-4267-84ea-85499ca58cca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112rat8HENsVCJX14qgRHQF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 920,
      "cache_read_input_tokens": 41410,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 41410,
          "cache_creation_input_tokens": 920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 920
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

_source line 38 · 2026-05-13T11:31:35.059Z_

<details><summary>↩ Tool result · `toolu_019iTiDoQCemgFFFPvW4ts7a`</summary>

```text
Web search results for query: "EMA reference model data selection training adaptive online sample selection 2025 2026 NeurIPS ICML ICLR"

Links: [{"title":"Understanding Ecological-Momentary-Assessment Data: A Tutorial on Exploring Item Performance in Ecological-Momentary-Assessment Data - Björn S. Siepe, Carlotta L. Rieble, Rayyan Tutunji, Aljoscha Rimpler, Julius März, Ricarda K. K. Proppert, Eiko I. Fried, 2025","url":"https://journals.sagepub.com/doi/10.1177/25152459241286877"},{"title":"Methodology Working Party Workplan 2026-2028 - EMA","url":"https://www.ema.europa.eu/en/documents/other/consolidated-3-year-rolling-work-plan-methodology-working-party-2026-2028_en.pdf"},{"title":"Model EMA (Exponential Moving Average) | timmdocs","url":"https://timm.fast.ai/training_modelEMA"},{"title":"EMA Management Board: highlights of December 2025 meeting | European Medicines Agency (EMA)","url":"https://www.ema.europa.eu/en/news/ema-management-board-highlights-december-2025-meeting"},{"title":"Exponential Moving Average of Weights in Deep Learning: Dynamics and Benefits","url":"https://arxiv.org/html/2411.18704v1"},{"title":"How to Scale Your EMA - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/scale-em"},{"title":"Agenda - HMA EMA Annual Data Forum 2025","url":"https://www.ema.europa.eu/en/documents/agenda/agenda-hma-ema-annual-data-forum-2025_en.pdf"},{"title":"Ecological Momentary Assessment (EMA)","url":"https://www.simplypsychology.org/ecological-momentary-assessment.html"},{"title":"How to Scale Your EMA | OpenReview","url":"https://openreview.net/forum?id=DkeeXVdQyu"},{"title":"ModMed® EMR Software | Free Demo, Reviews & Pricing 2026 |EMRFinder","url":"https://emrfinder.com/ema-by-modernizing-medicine-emr-software/"}]

Based on the search results, I found relevant research related to your query. The most pertinent result is:

"How to Scale Your EMA" is a research paper presented at ICLR in April 2025. This work addresses model EMA (Exponential Moving Average), where parameters move according to an EMA rate with a momentum hyperparameter, and demonstrates how this can improve robustness and generalization of supervised learning, stabilize pseudo-labeling, and provide learning signals for Self-Supervised Learning.

Additionally, there's relevant work on Exponential Moving Average of weights in deep learning, which presents a systematic study exploring training dynamics, hyperparameter tuning guidelines, and showing that EMA models generalize better with improved robustness to noisy labels, prediction consistency, calibration, and transfer learning.

However, the search results don't contain specific papers matching all of your query criteria (particularly those addressing data selection, adaptive online sample selection, and appearing at NeurIPS or ICML conferences in 2025-2026). You may want to search directly on the conference proceedings pages for NeurIPS, ICML, and ICLR to find papers more specifically combining these topics together.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c837457-61f6-4267-84ea-85499ca58cca",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "47b9582f-7b53-4aa1-8f59-665fbf74eccb",
  "toolUseResult": {
    "query": "EMA reference model data selection training adaptive online sample selection 2025 2026 NeurIPS ICML ICLR",
    "results": [
      {
        "tool_use_id": "srvtoolu_019A9sWWmSBMy5KCnkyVNeG2",
        "content": [
          {
            "title": "Understanding Ecological-Momentary-Assessment Data: A Tutorial on Exploring Item Performance in Ecological-Momentary-Assessment Data - Björn S. Siepe, Carlotta L. Rieble, Rayyan Tutunji, Aljoscha Rimpler, Julius März, Ricarda K. K. Proppert, Eiko I. Fried, 2025",
            "url": "https://journals.sagepub.com/doi/10.1177/25152459241286877"
          },
          {
            "title": "Methodology Working Party Workplan 2026-2028 - EMA",
            "url": "https://www.ema.europa.eu/en/documents/other/consolidated-3-year-rolling-work-plan-methodology-working-party-2026-2028_en.pdf"
          },
          {
            "title": "Model EMA (Exponential Moving Average) | timmdocs",
            "url": "https://timm.fast.ai/training_modelEMA"
          },
          {
            "title": "EMA Management Board: highlights of December 2025 meeting | European Medicines Agency (EMA)",
            "url": "https://www.ema.europa.eu/en/news/ema-management-board-highlights-december-2025-meeting"
          },
          {
            "title": "Exponential Moving Average of Weights in Deep Learning: Dynamics and Benefits",
            "url": "https://arxiv.org/html/2411.18704v1"
          },
          {
            "title": "How to Scale Your EMA - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/research/scale-em"
          },
          {
            "title": "Agenda - HMA EMA Annual Data Forum 2025",
            "url": "https://www.ema.europa.eu/en/documents/agenda/agenda-hma-ema-annual-data-forum-2025_en.pdf"
          },
          {
            "title": "Ecological Momentary Assessment (EMA)",
            "url": "https://www.simplypsychology.org/ecological-momentary-assessment.html"
          },
          {
            "title": "How to Scale Your EMA | OpenReview",
            "url": "https://openreview.net/forum?id=DkeeXVdQyu"
          },
          {
            "title": "ModMed® EMR Software | Free Demo, Reviews & Pricing 2026 |EMRFinder",
            "url": "https://emrfinder.com/ema-by-modernizing-medicine-emr-software/"
          }
        ]
      },
      "Based on the search results, I found relevant research related to your query. The most pertinent result is:\n\n\"How to Scale Your EMA\" is a research paper presented at ICLR in April 2025. This work addresses model EMA (Exponential Moving Average), where parameters move according to an EMA rate with a momentum hyperparameter, and demonstrates how this can improve robustness and generalization of supervised learning, stabilize pseudo-labeling, and provide learning signals for Self-Supervised Learning.\n\nAdditionally, there's relevant work on Exponential Moving Average of weights in deep learning, which presents a systematic study exploring training dynamics, hyperparameter tuning guidelines, and showing that EMA models generalize better with improved robustness to noisy labels, prediction consistency, calibration, and transfer learning.\n\nHowever, the search results don't contain specific papers matching all of your query criteria (particularly those addressing data selection, adaptive online sample selection, and appearing at NeurIPS or ICML conferences in 2025-2026). You may want to search directly on the conference proceedings pages for NeurIPS, ICML, and ICLR to find papers more specifically combining these topics together."
    ],
    "durationSeconds": 5.40539844199999
  },
  "sourceToolAssistantUUID": "1c837457-61f6-4267-84ea-85499ca58cca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-13T11:31:38.022Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PCB1atrKjwKzUJy7kQZvWv`</summary>

```json
{
  "query": "VLA training pipeline SFT RL 2026 latest results LIBERO success rate state of the art"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47b9582f-7b53-4aa1-8f59-665fbf74eccb",
  "isSidechain": false,
  "requestId": "req_011CazVZoXr6YJDFdQR4Ps5G",
  "type": "assistant",
  "uuid": "25ecb62c-c5ee-4a95-b0ff-26d6502e40c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tz9miEteeWdwj8GtLLfUfX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 958,
      "cache_read_input_tokens": 42330,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 958,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 42330,
          "cache_creation_input_tokens": 958,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 958
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

_source line 40 · 2026-05-13T11:31:45.513Z_

<details><summary>↩ Tool result · `toolu_01PCB1atrKjwKzUJy7kQZvWv`</summary>

```text
Web search results for query: "VLA training pipeline SFT RL 2026 latest results LIBERO success rate state of the art"

Links: [{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"},{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy","url":"https://arxiv.org/pdf/2602.06508"},{"title":"SELF-IMPROVING VISION-LANGUAGE-ACTION","url":"https://arxiv.org/pdf/2511.00091"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview","url":"https://openreview.net/forum?id=xqRD4LLY5M"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.09674v1"},{"title":"VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation","url":"https://arxiv.org/html/2603.26666v1"},{"title":"PLD: Self-Improving Vision-Language-Action Models (ICLR 2026)","url":"https://wenlixiao.com/self-improve-VLA-PLD"},{"title":"RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.06710"},{"title":"[Literature Review] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://www.themoonlight.io/en/review/simplevla-rl-scaling-vla-training-via-reinforcement-learning"}]

Based on the latest 2026 research, here are the key findings on VLA training pipelines with SFT and RL approaches:

## State-of-the-Art LIBERO Success Rates

SimpleVLA-RL improves the performance of OpenVLA-OFT to 97.6 points on LIBERO-Long and sets a new state-of-the-art. More broadly, on LIBERO tasks, the framework improves average success rates from 91% to 99.1%, with particularly notable gains on long-horizon tasks (98.5% vs. previous best results).

## Key Approaches and Results

**SimpleVLA-RL Framework**: SimpleVLA-RL is an efficient RL framework for VLA that improves long-horizon planning under data scarcity. It leverages reinforcement learning that can substantially outperforms SFT in simulation and real-world tasks.

**PLD (Probe, Learn, Distill)**: This method achieves near-saturated 99% success rates on the LIBERO benchmark, and delivers over 50% performance gains in SimplerEnv. PLD demonstrates a 100% success rate on real-world Franka arm and YAM arm dexterous manipulation tasks.

**Data Efficiency**: In extreme data scarcity conditions, using only one demonstration trajectory per task, SimpleVLA-RL increases average success rates across LIBERO task suites from 48.9% to 96.9%.

## Generalization Improvements

SimpleVLA-RL consistently improves performance across all unseen spatial arrangements, achieving gains of 28.5% on one task and 7.1% to 13.3% on others, demonstrating significant improvements in out-of-distribution generalization compared to SFT-only approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25ecb62c-c5ee-4a95-b0ff-26d6502e40c5",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "9cc0a14e-4361-4c84-9706-c806feec0223",
  "toolUseResult": {
    "query": "VLA training pipeline SFT RL 2026 latest results LIBERO success rate state of the art",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WYnrX4LyftZKb5a4QN8FCS",
        "content": [
          {
            "title": "Self-Improving Vision-Language-Action Models with Data ...",
            "url": "https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"
          },
          {
            "title": "GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub",
            "url": "https://github.com/PRIME-RL/SimpleVLA-RL"
          },
          {
            "title": "World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy",
            "url": "https://arxiv.org/pdf/2602.06508"
          },
          {
            "title": "SELF-IMPROVING VISION-LANGUAGE-ACTION",
            "url": "https://arxiv.org/pdf/2511.00091"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview",
            "url": "https://openreview.net/forum?id=xqRD4LLY5M"
          },
          {
            "title": "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2509.09674v1"
          },
          {
            "title": "VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation",
            "url": "https://arxiv.org/html/2603.26666v1"
          },
          {
            "title": "PLD: Self-Improving Vision-Language-Action Models (ICLR 2026)",
            "url": "https://wenlixiao.com/self-improve-VLA-PLD"
          },
          {
            "title": "RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.06710"
          },
          {
            "title": "[Literature Review] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning",
            "url": "https://www.themoonlight.io/en/review/simplevla-rl-scaling-vla-training-via-reinforcement-learning"
          }
        ]
      },
      "Based on the latest 2026 research, here are the key findings on VLA training pipelines with SFT and RL approaches:\n\n## State-of-the-Art LIBERO Success Rates\n\nSimpleVLA-RL improves the performance of OpenVLA-OFT to 97.6 points on LIBERO-Long and sets a new state-of-the-art. More broadly, on LIBERO tasks, the framework improves average success rates from 91% to 99.1%, with particularly notable gains on long-horizon tasks (98.5% vs. previous best results).\n\n## Key Approaches and Results\n\n**SimpleVLA-RL Framework**: SimpleVLA-RL is an efficient RL framework for VLA that improves long-horizon planning under data scarcity. It leverages reinforcement learning that can substantially outperforms SFT in simulation and real-world tasks.\n\n**PLD (Probe, Learn, Distill)**: This method achieves near-saturated 99% success rates on the LIBERO benchmark, and delivers over 50% performance gains in SimplerEnv. PLD demonstrates a 100% success rate on real-world Franka arm and YAM arm dexterous manipulation tasks.\n\n**Data Efficiency**: In extreme data scarcity conditions, using only one demonstration trajectory per task, SimpleVLA-RL increases average success rates across LIBERO task suites from 48.9% to 96.9%.\n\n## Generalization Improvements\n\nSimpleVLA-RL consistently improves performance across all unseen spatial arrangements, achieving gains of 28.5% on one task and 7.1% to 13.3% on others, demonstrating significant improvements in out-of-distribution generalization compared to SFT-only approaches."
    ],
    "durationSeconds": 7.4877456549999915
  },
  "sourceToolAssistantUUID": "25ecb62c-c5ee-4a95-b0ff-26d6502e40c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-13T11:31:50.257Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HUYkWnUVPYZw255JS4qeM1`</summary>

```json
{
  "query": "\"Proximal Supervised Fine-Tuning\" trust region token clipping SFT RL initialization arXiv 2508.17784"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cc0a14e-4361-4c84-9706-c806feec0223",
  "isSidechain": false,
  "requestId": "req_011CazVaaTpYL5W1weANoNms",
  "type": "assistant",
  "uuid": "86c20efd-72af-43b5-b321-870bb3751d44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019xyxTi5PZ193BJi9pKXD38",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1055,
      "cache_read_input_tokens": 43288,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1055,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 43288,
          "cache_creation_input_tokens": 1055,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1055
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

_source line 42 · 2026-05-13T11:31:55.571Z_

<details><summary>↩ Tool result · `toolu_01HUYkWnUVPYZw255JS4qeM1`</summary>

```text
Web search results for query: ""Proximal Supervised Fine-Tuning" trust region token clipping SFT RL initialization arXiv 2508.17784"

Links: [{"title":"Proximal Supervised Fine-Tuning PROXIMAL SUPERVISED FINE-TUNING","url":"https://arxiv.org/pdf/2508.17784"},{"title":"[2508.17784] Proximal Supervised Fine-Tuning","url":"https://arxiv.org/abs/2508.17784"},{"title":"[2508.17784v1] Proximal Supervised Fine-Tuning","url":"https://arxiv.org/abs/2508.17784v1"},{"title":"Proximal Supervised Fine-Tuning (2508.17784v1)","url":"https://www.emergentmind.com/papers/2508.17784"},{"title":"Proximal Supervised Fine-Tuning | alphaXiv","url":"https://www.alphaxiv.org/overview/2508.17784v1"},{"title":"[Literature Review] Proximal Supervised Fine-Tuning","url":"https://www.themoonlight.io/en/review/proximal-supervised-fine-tuning"},{"title":"Proximal SFT (PSFT)","url":"https://www.emergentmind.com/topics/proximal-sft-psft"},{"title":"support Proximal Supervised Fine-Tuning · Issue #9157 · hiyouga/LlamaFactory","url":"https://github.com/hiyouga/LlamaFactory/issues/9157"},{"title":"Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start | OpenReview","url":"https://openreview.net/forum?id=qJLKOryYeR"},{"title":"Proximal Supervised Fine-Tuning | OpenReview","url":"https://openreview.net/forum?id=hQtwQqYikp"}]

I found the paper you requested! Here's a summary of the research on arXiv 2508.17784:

## Proximal Supervised Fine-Tuning (PSFT)

Supervised fine-tuning (SFT) of foundation models often leads to poor generalization, where prior capabilities deteriorate after tuning on new tasks or domains. Inspired by trust-region policy optimization (TRPO) and proximal policy optimization (PPO) in reinforcement learning (RL), the paper proposes Proximal SFT (PSFT).

### Core Approach

PSFT incorporates the benefits of trust-region, effectively constraining policy drift during SFT while maintaining competitive tuning. By viewing SFT as a special case of policy gradient methods with constant positive advantages, PSFT stabilizes optimization and leads to generalization, while leaving room for further optimization in subsequent post-training stages.

### Key Technical Features

The objective is based on a clipped surrogate objective that leverages the benefits of trust regions to constrain policy updates. The gradient update is confined to the trust region to perform fine-tuning, similar to that in PPO.

### Results and Benefits

Experiments across mathematical and human-value domains show that PSFT matches SFT in-domain, outperforms it in out-of-domain generalization, remains stable under prolonged training without causing entropy collapse, and provides a stronger foundation for subsequent optimization.

The code is available at https://github.com/zwhong714/PSFT, and the paper was submitted on August 25, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86c20efd-72af-43b5-b321-870bb3751d44",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "422666ae-5e5a-45cc-ab53-ac161c393068",
  "toolUseResult": {
    "query": "\"Proximal Supervised Fine-Tuning\" trust region token clipping SFT RL initialization arXiv 2508.17784",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VSnQ5ETk1EaJJac4Mvfi7p",
        "content": [
          {
            "title": "Proximal Supervised Fine-Tuning PROXIMAL SUPERVISED FINE-TUNING",
            "url": "https://arxiv.org/pdf/2508.17784"
          },
          {
            "title": "[2508.17784] Proximal Supervised Fine-Tuning",
            "url": "https://arxiv.org/abs/2508.17784"
          },
          {
            "title": "[2508.17784v1] Proximal Supervised Fine-Tuning",
            "url": "https://arxiv.org/abs/2508.17784v1"
          },
          {
            "title": "Proximal Supervised Fine-Tuning (2508.17784v1)",
            "url": "https://www.emergentmind.com/papers/2508.17784"
          },
          {
            "title": "Proximal Supervised Fine-Tuning | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2508.17784v1"
          },
          {
            "title": "[Literature Review] Proximal Supervised Fine-Tuning",
            "url": "https://www.themoonlight.io/en/review/proximal-supervised-fine-tuning"
          },
          {
            "title": "Proximal SFT (PSFT)",
            "url": "https://www.emergentmind.com/topics/proximal-sft-psft"
          },
          {
            "title": "support Proximal Supervised Fine-Tuning · Issue #9157 · hiyouga/LlamaFactory",
            "url": "https://github.com/hiyouga/LlamaFactory/issues/9157"
          },
          {
            "title": "Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start | OpenReview",
            "url": "https://openreview.net/forum?id=qJLKOryYeR"
          },
          {
            "title": "Proximal Supervised Fine-Tuning | OpenReview",
            "url": "https://openreview.net/forum?id=hQtwQqYikp"
          }
        ]
      },
      "I found the paper you requested! Here's a summary of the research on arXiv 2508.17784:\n\n## Proximal Supervised Fine-Tuning (PSFT)\n\nSupervised fine-tuning (SFT) of foundation models often leads to poor generalization, where prior capabilities deteriorate after tuning on new tasks or domains. Inspired by trust-region policy optimization (TRPO) and proximal policy optimization (PPO) in reinforcement learning (RL), the paper proposes Proximal SFT (PSFT).\n\n### Core Approach\n\nPSFT incorporates the benefits of trust-region, effectively constraining policy drift during SFT while maintaining competitive tuning. By viewing SFT as a special case of policy gradient methods with constant positive advantages, PSFT stabilizes optimization and leads to generalization, while leaving room for further optimization in subsequent post-training stages.\n\n### Key Technical Features\n\nThe objective is based on a clipped surrogate objective that leverages the benefits of trust regions to constrain policy updates. The gradient update is confined to the trust region to perform fine-tuning, similar to that in PPO.\n\n### Results and Benefits\n\nExperiments across mathematical and human-value domains show that PSFT matches SFT in-domain, outperforms it in out-of-domain generalization, remains stable under prolonged training without causing entropy collapse, and provides a stronger foundation for subsequent optimization.\n\nThe code is available at https://github.com/zwhong714/PSFT, and the paper was submitted on August 25, 2025."
    ],
    "durationSeconds": 5.309374071000027
  },
  "sourceToolAssistantUUID": "86c20efd-72af-43b5-b321-870bb3751d44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"RAPID: Reducible-Loss Adaptive Prioritized Replay for VLA Imitation Le…",
  "leafUuid": "422666ae-5e5a-45cc-ab53-ac161c393068",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising RAPID: Addressing novelty gaps and clarifying SFT→RL contribution",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---

### Tool call

_source line 45 · 2026-05-13T11:31:58.455Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MhpJL6WBRzHpjTC5nCuAzw`</summary>

```json
{
  "query": "adaptive data curation VLA training online demonstration selection robot 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "422666ae-5e5a-45cc-ab53-ac161c393068",
  "isSidechain": false,
  "requestId": "req_011CazVbKEJpAghKYAqg9zAr",
  "type": "assistant",
  "uuid": "8d2d0019-695a-44b1-b8fc-5b197dbe567f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zdkXoU1RQcBdqEV5p8RD5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 44343,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 949,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 44343,
          "cache_creation_input_tokens": 949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 949
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

_source line 46 · 2026-05-13T11:32:06.514Z_

<details><summary>↩ Tool result · `toolu_01MhpJL6WBRzHpjTC5nCuAzw`</summary>

```text
Web search results for query: "adaptive data curation VLA training online demonstration selection robot 2026"

Links: [{"title":"From Data to Decisions: VLA Pipelines for Real Robots - ICRA 2026 Workshop","url":"https://icra2026vlapipeline.github.io/"},{"title":"AIRoA Announces ICRA 2026 Workshop — Launching a Global Competition on VLA Pipelines and Approximately 10,000 Hours of Real-World Robot Data — | AIRoA","url":"https://www.airoa.org/updates/2026-02-10"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00919v1"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/state-of-robotics-2026"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"},{"title":"Humanoid Robot Training Data: Deployment Guide 2026 | Shaip","url":"https://www.shaip.com/blog/humanoid-robot-training-data-what-teams-need-before-deployment/"},{"title":"Generative AI in Industrial Robotics: 2026 Layers Guide","url":"https://www.evsint.com/generative-ai-industrial-robotics-foundation-models-code-generation-2026/"},{"title":"1 Recipe for Vision-Language-Action Models in Robotic Manipulation: A Survey","url":"https://www.techrxiv.org/users/956965/articles/1326137/master/file/data/eart2025recipevla/eart2025recipevla.pdf?inline=true"}]

Based on the search results, I found several relevant topics related to adaptive data curation, VLA (Vision-Language-Action) training, and robot learning in 2026:

## Key Findings:

**Data Curation in VLA Training**: The field is examining the entire end-to-end VLA pipeline, from scalable data collection and systematic curation to training strategies and inference-time reasoning.

**Online Demonstration Selection**: A well-curated 500-demo fine-tune of a 7B VLA outperforms a poorly curated fine-tune of a 70B model on most manipulation benchmarks, highlighting the critical importance of selective demonstration curation over raw scale.

**Adaptive Training Approaches**: Dataset curation plus RL alignment builds on the unified pretrain to progressively improve performance on a concrete target embodiment. Additionally, Green-VLA achieves the largest gains after RL alignment, especially on long-horizon success, recovery, and precise task following—showing that careful unification, data curation, and guidance matter for high-quality VLA.

**2026 Developments**: The ICRA 2026 workshop "From Data to Decisions: VLA Pipelines for Real Robots" has been accepted for presentation at ICRA 2026, which will be held in Vienna, Austria, from June 1–5, 2026.

The search results show significant focus on how strategic data curation and adaptive training strategies are essential for improving robot learning performance beyond simply scaling model or dataset size.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d2d0019-695a-44b1-b8fc-5b197dbe567f",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "24aae2ea-e764-426f-b808-0db936490589",
  "toolUseResult": {
    "query": "adaptive data curation VLA training online demonstration selection robot 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VzGMMJAxuD3B6uJEbvrdrg",
        "content": [
          {
            "title": "From Data to Decisions: VLA Pipelines for Real Robots - ICRA 2026 Workshop",
            "url": "https://icra2026vlapipeline.github.io/"
          },
          {
            "title": "AIRoA Announces ICRA 2026 Workshop — Launching a Global Competition on VLA Pipelines and Approximately 10,000 Hours of Real-World Robot Data — | AIRoA",
            "url": "https://www.airoa.org/updates/2026-02-10"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2602.00919v1"
          },
          {
            "title": "Vision-language-action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          },
          {
            "title": "State of Robotics 2026 Report: $38B Market, 12 Humanoids, VLA Adoption | Silicon Valley Robotics Center",
            "url": "https://www.roboticscenter.ai/state-of-robotics-2026"
          },
          {
            "title": "GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub",
            "url": "https://github.com/OpenDriveLab/WholebodyVLA"
          },
          {
            "title": "A Survey on Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.24795v1"
          },
          {
            "title": "Humanoid Robot Training Data: Deployment Guide 2026 | Shaip",
            "url": "https://www.shaip.com/blog/humanoid-robot-training-data-what-teams-need-before-deployment/"
          },
          {
            "title": "Generative AI in Industrial Robotics: 2026 Layers Guide",
            "url": "https://www.evsint.com/generative-ai-industrial-robotics-foundation-models-code-generation-2026/"
          },
          {
            "title": "1 Recipe for Vision-Language-Action Models in Robotic Manipulation: A Survey",
            "url": "https://www.techrxiv.org/users/956965/articles/1326137/master/file/data/eart2025recipevla/eart2025recipevla.pdf?inline=true"
          }
        ]
      },
      "Based on the search results, I found several relevant topics related to adaptive data curation, VLA (Vision-Language-Action) training, and robot learning in 2026:\n\n## Key Findings:\n\n**Data Curation in VLA Training**: The field is examining the entire end-to-end VLA pipeline, from scalable data collection and systematic curation to training strategies and inference-time reasoning.\n\n**Online Demonstration Selection**: A well-curated 500-demo fine-tune of a 7B VLA outperforms a poorly curated fine-tune of a 70B model on most manipulation benchmarks, highlighting the critical importance of selective demonstration curation over raw scale.\n\n**Adaptive Training Approaches**: Dataset curation plus RL alignment builds on the unified pretrain to progressively improve performance on a concrete target embodiment. Additionally, Green-VLA achieves the largest gains after RL alignment, especially on long-horizon success, recovery, and precise task following—showing that careful unification, data curation, and guidance matter for high-quality VLA.\n\n**2026 Developments**: The ICRA 2026 workshop \"From Data to Decisions: VLA Pipelines for Real Robots\" has been accepted for presentation at ICRA 2026, which will be held in Vienna, Austria, from June 1–5, 2026.\n\nThe search results show significant focus on how strategic data curation and adaptive training strategies are essential for improving robot learning performance beyond simply scaling model or dataset size."
    ],
    "durationSeconds": 8.054554307000013
  },
  "sourceToolAssistantUUID": "8d2d0019-695a-44b1-b8fc-5b197dbe567f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-13T11:32:59.323Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me gather the key findings from my research and think deeply about what changes to make.

**Key findings from research:**

1. **ICML 2026 clipping paper**: "Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start" by Tian-Shuo Liu et al. (also appears as "Clipping Low-Probability Tokens in SFT Yields a Generalizable Initialization for RL"). Uses token-level clipping as a trust-region method. Results: 7.09% RL improvement, 11.54% reduced forgetting. 

The paper demonstrates this approach in LLM domains like ALFWorld and ScienceWorld, which shows that SFT techniques can meaningfully impact downstream RL performance—but through a completely different mechanism than RAPID's data selection approach, relying instead on gradient clipping.

2. **iw-SFT EMA details confirmed**: iw-SFT does use EMA for importance weights, but only in continuous control experiments, not LLM tasks. The alpha parameter isn't specified in the papers I found. This is a genuine overlap I need to address directly.

3. **Additional**

I'm finding several related papers on SFT and downstream RL: Proximal Supervised Fine-Tuning uses trust-region objectives with clipping, while Dynamic Fine-Tuning rescales the SFT objective based on token probabilities. There's also work on how dataset diversity in SFT affects downstream reasoning, and a distillation approach to handle distributional drift from SFT. On the vision-language side, SimpleVLA-RL is still achieving strong performance on LIBERO benchmarks.

Now I'm wrestling with whether the reviewer's critique about novelty ceilings is actually justified. The core tension is that RAPID essentially combines reducible loss with EMA-based reference models—techniques that already exist in prior work like ReLo and iw-SFT. The individual pieces aren't novel, and while the combination has some merit, it feels incremental. The real value would come from showing that SFT data quality improvements cascade meaningfully to RL performance in vision-language models, but the ICML 2026 clipping paper already demonstrates this principle for language models, which narrows RAPID's contribution significantly.

Rather than abandoning the work entirely, I think a major revision makes more sense. The key is being more precise about what's actually novel: iw-SFT uses EMA for importance weighting in continuous control, but RAPID's contribution is specifically the reducible loss decomposition applied through that EMA mechanism—that's a meaningful distinction around noise robustness versus theoretical bounds, even if it's subtle.

I need to properly position this against the ICML 2026 clipping paper and related work like PSFT and DFT, which all tackle how SFT techniques affect downstream RL but through gradient modification rather than data selection. RAPID's angle on data prioritization is genuinely complementary to those approaches.

The narrative itself needs tightening—right now the proposal is sprawling, but the core story is cleaner: reducible loss decomposition via EMA reference enables noise-robust data prioritization for VLA SFT, which then cascades into faster RL convergence. I should also set a hard decision point for CoRL by May 22, reframe the finite-T bounds as qualitative predictions about growth rates rather than quantitative claims, explicitly acknowledge the noise injection limitation, and cut down the overall length since the reviewer's feedback keeps pointing toward focus.

But actually, there's a more fundamental reframing that might move the needle. The reviewer highlighted that the single most impactful result would be a compelling RAPID+RL experiment, and suggested the narrative should be: "SFT data quality is the hidden bottleneck of VLA RL pipelines; RAPID provides a drop-in fix." What if I flip the entire framing? Instead of positioning this as "RAPID: a data curation method with theory," I make it "SFT data quality is the hidden bottleneck of VLA RL pipelines: evidence and a solution." The finding becomes the headline, not the method—RAPID is just the mechanism that demonstrates this bottleneck exists. This differentiates from the ICML 2026 clipping paper, which focuses on gradient-level interventions rather than the upstream data quality problem.

The risk is that if the RAPID+RL experiments don't deliver compelling results, the whole paper falls apart. But the reviewer seems confident this is the path to impact, so I'm going to commit to a major revision around this reframing.

I should also check if there's recent work on the SFT-to-RL pipeline specifically for VLAs that I'm missing. And I need to think more carefully about the iw-SFT overlap—while they both use EMA for continuous control, the key difference is that iw-SFT uses EMA to define the trajectory distribution for computing importance weights, whereas RAPID operates at the token level.

Actually, the distinction is clearer now: iw-SFT applies multiplicative loss scaling based on importance weights, while RAPID decomposes loss into reducible and irreducible components using the EMA reference model, then uses that decomposition for priority-based sampling. The reducible loss framing gives noise robustness that pure importance weighting doesn't provide. The EMA reference model itself isn't novel to RAPID, but using it for loss decomposition in imitation learning is the actual contribution.

Now I'm ready to write the revised paper, reframing around the SFT-to-RL pipeline finding and properly positioning where iw-SFT differs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24aae2ea-e764-426f-b808-0db936490589",
  "isSidechain": false,
  "requestId": "req_011CazVc829brrbWHHnJ6Rzv",
  "type": "assistant",
  "uuid": "bceedf5f-d5f7-4f25-85b5-23907fb2bb0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xndwz24z1mr8uzdGJ66NFd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 982,
      "cache_read_input_tokens": 45292,
      "output_tokens": 1985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 982,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1985,
          "cache_read_input_tokens": 45292,
          "cache_creation_input_tokens": 982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 982
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

_source line 48 · 2026-05-13T11:32:59.838Z_

Now let me search for a few more things to ensure thorough coverage before revising.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bceedf5f-d5f7-4f25-85b5-23907fb2bb0a",
  "isSidechain": false,
  "requestId": "req_011CazVc829brrbWHHnJ6Rzv",
  "type": "assistant",
  "uuid": "ff6b491a-01a9-45b1-a75d-39fed01167e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xndwz24z1mr8uzdGJ66NFd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 982,
      "cache_read_input_tokens": 45292,
      "output_tokens": 1985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 982,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1985,
          "cache_read_input_tokens": 45292,
          "cache_creation_input_tokens": 982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 982
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

_source line 49 · 2026-05-13T11:33:00.238Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0111Rfx6DmAEk2ejqdUbBHKS`</summary>

```json
{
  "query": "\"PRISM\" \"pre-alignment\" \"on-policy distillation\" multimodal reinforcement learning arXiv 2604"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff6b491a-01a9-45b1-a75d-39fed01167e3",
  "isSidechain": false,
  "requestId": "req_011CazVc829brrbWHHnJ6Rzv",
  "type": "assistant",
  "uuid": "4d1e2216-c5f9-4499-a65a-d12fca39232a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xndwz24z1mr8uzdGJ66NFd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 982,
      "cache_read_input_tokens": 45292,
      "output_tokens": 1985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 982,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1985,
          "cache_read_input_tokens": 45292,
          "cache_creation_input_tokens": 982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 982
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

_source line 50 · 2026-05-13T11:33:07.823Z_

<details><summary>↩ Tool result · `toolu_0111Rfx6DmAEk2ejqdUbBHKS`</summary>

```text
Web search results for query: ""PRISM" "pre-alignment" "on-policy distillation" multimodal reinforcement learning arXiv 2604"

Links: [{"title":"[2604.28123] PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning","url":"https://arxiv.org/abs/2604.28123"},{"title":"PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning","url":"https://arxiv.org/html/2604.28123"},{"title":"GitHub - XIAO4579/PRISM: Beyond SFT-to-RL: Pre-alignment via Black-BoxOn-Policy Distillation for Multimodal RL · GitHub","url":"https://github.com/XIAO4579/PRISM"},{"title":"[2604.02353] Prism: Policy Reuse via Interpretable Strategy Mapping in Reinforcement Learning","url":"https://arxiv.org/abs/2604.02353"},{"title":"Prism: Policy Reuse via Interpretable Strategy Mapping","url":"https://arxiv.org/html/2604.02353"},{"title":"PRISM","url":"https://zacravichandran.github.io/PRISM/"},{"title":"PRISM: Diversifying Dataset Distillation by Decoupling Architectural Priors","url":"https://arxiv.org/html/2511.09905"},{"title":"On-Policy Distillation - Thinking Machines Lab","url":"https://thinkingmachines.ai/blog/on-policy-distillation/"},{"title":"GitHub - opendilab/awesome-multi-modal-reinforcement-learning: A curated list of Multi-Modal Reinforcement Learning resources (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-multi-modal-reinforcement-learning"},{"title":"PRISM: Perspective Reasoning for Integrated Synthesis and Mediation as a Multi-Perspective Framework for AI Alignment","url":"https://arxiv.org/html/2503.04740v1"}]

Based on the search results, I found the paper you're looking for:

## PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning

PRISM is a three-stage pipeline that mitigates distributional drift by inserting an explicit distribution-alignment stage between SFT and RLVR. It builds on the principle of on-policy distillation (OPD) and casts alignment as a black-box, response-level adversarial game between the policy and a Mixture-of-Experts (MoE) discriminator with dedicated perception and reasoning experts, providing disentangled corrective signals that steer the policy toward the supervision distribution without requiring access to teacher logits.

### Key Problem

The standard post-training recipe for large multimodal models applies supervised fine-tuning (SFT) followed by reinforcement learning with verifiable rewards (RLVR). However, SFT introduces distributional drift that neither preserves the model's original capabilities nor faithfully matches the supervision distribution. This problem is further amplified in multimodal reasoning, where perception errors and reasoning failures follow distinct drift patterns that compound during subsequent RL.

### Implementation Details

The authors curated 113K multimodal reasoning demonstrations from Gemini 3 Flash targeting the hardest unsolved problems, combined with 1.26M public demonstrations for SFT. Experiments on Qwen3-VL show that PRISM consistently improves downstream RLVR performance across multiple RL algorithms (GRPO, DAPO, GSPO) and diverse multimodal benchmarks.

The paper was published on arXiv as **2604.28123** in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d1e2216-c5f9-4499-a65a-d12fca39232a",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "0704968c-8b54-4dcf-b56c-b60a42fc6408",
  "toolUseResult": {
    "query": "\"PRISM\" \"pre-alignment\" \"on-policy distillation\" multimodal reinforcement learning arXiv 2604",
    "results": [
      {
        "tool_use_id": "srvtoolu_014UXPt27E2airgLT8nDzS9q",
        "content": [
          {
            "title": "[2604.28123] PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning",
            "url": "https://arxiv.org/abs/2604.28123"
          },
          {
            "title": "PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning",
            "url": "https://arxiv.org/html/2604.28123"
          },
          {
            "title": "GitHub - XIAO4579/PRISM: Beyond SFT-to-RL: Pre-alignment via Black-BoxOn-Policy Distillation for Multimodal RL · GitHub",
            "url": "https://github.com/XIAO4579/PRISM"
          },
          {
            "title": "[2604.02353] Prism: Policy Reuse via Interpretable Strategy Mapping in Reinforcement Learning",
            "url": "https://arxiv.org/abs/2604.02353"
          },
          {
            "title": "Prism: Policy Reuse via Interpretable Strategy Mapping",
            "url": "https://arxiv.org/html/2604.02353"
          },
          {
            "title": "PRISM",
            "url": "https://zacravichandran.github.io/PRISM/"
          },
          {
            "title": "PRISM: Diversifying Dataset Distillation by Decoupling Architectural Priors",
            "url": "https://arxiv.org/html/2511.09905"
          },
          {
            "title": "On-Policy Distillation - Thinking Machines Lab",
            "url": "https://thinkingmachines.ai/blog/on-policy-distillation/"
          },
          {
            "title": "GitHub - opendilab/awesome-multi-modal-reinforcement-learning: A curated list of Multi-Modal Reinforcement Learning resources (continually updated) · GitHub",
            "url": "https://github.com/opendilab/awesome-multi-modal-reinforcement-learning"
          },
          {
            "title": "PRISM: Perspective Reasoning for Integrated Synthesis and Mediation as a Multi-Perspective Framework for AI Alignment",
            "url": "https://arxiv.org/html/2503.04740v1"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n## PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning\n\nPRISM is a three-stage pipeline that mitigates distributional drift by inserting an explicit distribution-alignment stage between SFT and RLVR. It builds on the principle of on-policy distillation (OPD) and casts alignment as a black-box, response-level adversarial game between the policy and a Mixture-of-Experts (MoE) discriminator with dedicated perception and reasoning experts, providing disentangled corrective signals that steer the policy toward the supervision distribution without requiring access to teacher logits.\n\n### Key Problem\n\nThe standard post-training recipe for large multimodal models applies supervised fine-tuning (SFT) followed by reinforcement learning with verifiable rewards (RLVR). However, SFT introduces distributional drift that neither preserves the model's original capabilities nor faithfully matches the supervision distribution. This problem is further amplified in multimodal reasoning, where perception errors and reasoning failures follow distinct drift patterns that compound during subsequent RL.\n\n### Implementation Details\n\nThe authors curated 113K multimodal reasoning demonstrations from Gemini 3 Flash targeting the hardest unsolved problems, combined with 1.26M public demonstrations for SFT. Experiments on Qwen3-VL show that PRISM consistently improves downstream RLVR performance across multiple RL algorithms (GRPO, DAPO, GSPO) and diverse multimodal benchmarks.\n\nThe paper was published on arXiv as **2604.28123** in 2026."
    ],
    "durationSeconds": 7.5796358120000225
  },
  "sourceToolAssistantUUID": "4d1e2216-c5f9-4499-a65a-d12fca39232a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 51_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"RAPID: Reducible-Loss Adaptive Prioritized Replay for VLA Imitation Le…",
  "leafUuid": "0704968c-8b54-4dcf-b56c-b60a42fc6408",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising RAPID: Addressing novelty gaps and clarifying SFT→RL contribution",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---

### Tool call

_source line 53 · 2026-05-13T11:33:10.552Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B6u6jktKX8LQaDt1DXUjw9`</summary>

```json
{
  "query": "\"Tailored Primitive Initialization\" SFT RL reasoning diversity arXiv 2511.12429"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0704968c-8b54-4dcf-b56c-b60a42fc6408",
  "isSidechain": false,
  "requestId": "req_011CazVge9jbBdbd1ZQGa8Ci",
  "type": "assistant",
  "uuid": "20d8f6d1-5f3c-4d17-a85d-101e4f221d14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W21JGc3d8b7zqGvdKcn2ko",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2924,
      "cache_read_input_tokens": 46274,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2924,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 46274,
          "cache_creation_input_tokens": 2924,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2924
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

_source line 54 · 2026-05-13T11:33:17.771Z_

<details><summary>↩ Tool result · `toolu_01B6u6jktKX8LQaDt1DXUjw9`</summary>

```text
Web search results for query: ""Tailored Primitive Initialization" SFT RL reasoning diversity arXiv 2511.12429"

Links: [{"title":"[2511.12429] Tailored Primitive Initialization is the Secret Key to Reinforcement Learning","url":"https://arxiv.org/abs/2511.12429"},{"title":"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning","url":"https://arxiv.org/html/2511.12429v1"},{"title":"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/abs/2511.12429v1"},{"title":"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/397700530_Tailored_Primitive_Initialization_is_the_Secret_Key_to_Reinforcement_Learning"},{"title":"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=1tWqSvoeBd"},{"title":"[Literature Review] Tailored Primitive Initialization is the Secret Key to Reinforcement Learning","url":"https://www.themoonlight.io/en/review/tailored-primitive-initialization-is-the-secret-key-to-reinforcement-learning"},{"title":"TAILORED PRIMITIVE INITIALIZATION IS THE SECRET ...","url":"https://openreview.net/pdf/ac9ed140b3a3bc0b1c76fe5fc61064f94bb59132.pdf"},{"title":"Diversity-Enhanced Reasoning for Subjective Questions","url":"https://arxiv.org/html/2507.20187"},{"title":"Weight Ensembling Improves Reasoning in Language Models","url":"https://arxiv.org/html/2504.10478v1"},{"title":"Revisiting the Necessity of Lengthy Chain-of-Thought in Vision-centric Reasoning Generalization","url":"https://arxiv.org/html/2511.22586v1"}]

I found the paper! Here's what the search results reveal about arXiv 2511.12429:

## Tailored Primitive Initialization is the Secret Key to Reinforcement Learning

Reinforcement learning has emerged as a powerful paradigm for enhancing reasoning capabilities of LLMs, though it faces challenges including low sampling efficiency and strong dependence on model initialization.

**Key Contribution:** The work investigates these challenges through the lens of reasoning token coverage and proposes Tailor, a finetuning pipeline that automatically discovers and curates novel reasoning primitives, thereby expanding the coverage of reasoning-state distributions before RL.

**Core Insight:** Successful RL training in LLMs requires initializing models with reasoning primitives that offer high thinking trajectory coverage. Reasoning primitives refer to reasoning patterns (e.g., bottom-up reasoning, top-down reasoning), which fundamentally govern the reasoning token distribution.

**Problem Addressed:** Most existing warm-start pipelines where SFT precedes the RL stage include only a limited set of primitive patterns, leading to inefficient exploration and slower RL improvement.

**Results:** Extensive experiments on mathematical and logical reasoning benchmarks demonstrate that Tailor generates more diverse and higher-quality warm-start data, resulting in higher downstream RL performance.

The paper was published on arXiv on November 16, 2025, and is under review for ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20d8f6d1-5f3c-4d17-a85d-101e4f221d14",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "c4a22fea-8f78-4abb-88ba-c623cd8f99d0",
  "toolUseResult": {
    "query": "\"Tailored Primitive Initialization\" SFT RL reasoning diversity arXiv 2511.12429",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BFNurKYebZK4BwBg9NykiX",
        "content": [
          {
            "title": "[2511.12429] Tailored Primitive Initialization is the Secret Key to Reinforcement Learning",
            "url": "https://arxiv.org/abs/2511.12429"
          },
          {
            "title": "Tailored Primitive Initialization is the Secret Key to Reinforcement Learning",
            "url": "https://arxiv.org/html/2511.12429v1"
          },
          {
            "title": "Tailored Primitive Initialization is the Secret Key to Reinforcement Learning | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2511.12429v1"
          },
          {
            "title": "Tailored Primitive Initialization is the Secret Key to Reinforcement Learning | Request PDF",
            "url": "https://www.researchgate.net/publication/397700530_Tailored_Primitive_Initialization_is_the_Secret_Key_to_Reinforcement_Learning"
          },
          {
            "title": "Tailored Primitive Initialization is the Secret Key to Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=1tWqSvoeBd"
          },
          {
            "title": "[Literature Review] Tailored Primitive Initialization is the Secret Key to Reinforcement Learning",
            "url": "https://www.themoonlight.io/en/review/tailored-primitive-initialization-is-the-secret-key-to-reinforcement-learning"
          },
          {
            "title": "TAILORED PRIMITIVE INITIALIZATION IS THE SECRET ...",
            "url": "https://openreview.net/pdf/ac9ed140b3a3bc0b1c76fe5fc61064f94bb59132.pdf"
          },
          {
            "title": "Diversity-Enhanced Reasoning for Subjective Questions",
            "url": "https://arxiv.org/html/2507.20187"
          },
          {
            "title": "Weight Ensembling Improves Reasoning in Language Models",
            "url": "https://arxiv.org/html/2504.10478v1"
          },
          {
            "title": "Revisiting the Necessity of Lengthy Chain-of-Thought in Vision-centric Reasoning Generalization",
            "url": "https://arxiv.org/html/2511.22586v1"
          }
        ]
      },
      "I found the paper! Here's what the search results reveal about arXiv 2511.12429:\n\n## Tailored Primitive Initialization is the Secret Key to Reinforcement Learning\n\nReinforcement learning has emerged as a powerful paradigm for enhancing reasoning capabilities of LLMs, though it faces challenges including low sampling efficiency and strong dependence on model initialization.\n\n**Key Contribution:** The work investigates these challenges through the lens of reasoning token coverage and proposes Tailor, a finetuning pipeline that automatically discovers and curates novel reasoning primitives, thereby expanding the coverage of reasoning-state distributions before RL.\n\n**Core Insight:** Successful RL training in LLMs requires initializing models with reasoning primitives that offer high thinking trajectory coverage. Reasoning primitives refer to reasoning patterns (e.g., bottom-up reasoning, top-down reasoning), which fundamentally govern the reasoning token distribution.\n\n**Problem Addressed:** Most existing warm-start pipelines where SFT precedes the RL stage include only a limited set of primitive patterns, leading to inefficient exploration and slower RL improvement.\n\n**Results:** Extensive experiments on mathematical and logical reasoning benchmarks demonstrate that Tailor generates more diverse and higher-quality warm-start data, resulting in higher downstream RL performance.\n\nThe paper was published on arXiv on November 16, 2025, and is under review for ICLR 2026."
    ],
    "durationSeconds": 7.210473930000007
  },
  "sourceToolAssistantUUID": "20d8f6d1-5f3c-4d17-a85d-101e4f221d14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-13T11:33:21.971Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013p1sxHkPDYw2rKMm2fDxPz`</summary>

```json
{
  "query": "CoRL 2026 deadline abstract paper submission date May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4a22fea-8f78-4abb-88ba-c623cd8f99d0",
  "isSidechain": false,
  "requestId": "req_011CazVhNgM4cV6PaP4rgspX",
  "type": "assistant",
  "uuid": "f8a73707-07bd-4183-851e-82d3cc55f87a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019eW3HWuvKGy8CNGETW6i8C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 933,
      "cache_read_input_tokens": 49198,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 49198,
          "cache_creation_input_tokens": 933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 933
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

_source line 56 · 2026-05-13T11:33:28.474Z_

<details><summary>↩ Tool result · `toolu_013p1sxHkPDYw2rKMm2fDxPz`</summary>

```text
Web search results for query: "CoRL 2026 deadline abstract paper submission date May 2026"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"}]

Based on the search results, here are the CoRL 2026 submission deadlines in May 2026:

Abstract submission deadline: May 26, 2026 11:59 UTC

Paper submission deadline: May 29, 2026 11:59 UTC

The conference will be held November 9-12, 2026 in Austin, Texas, US


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8a73707-07bd-4183-851e-82d3cc55f87a",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "99e2ec0a-16a0-48da-be7c-a6904245e00e",
  "toolUseResult": {
    "query": "CoRL 2026 deadline abstract paper submission date May 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019FwPvcWBLEWnSTo1nADwsv",
        "content": [
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          },
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf?lang=en"
          },
          {
            "title": "CoRL 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"
          },
          {
            "title": "AI Deadlines – AI Conference Call For Paper Deadlines",
            "url": "http://aideadlines.org/"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "Refactor conference data · huggingface/ai-deadlines at f3cc2d7",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"
          }
        ]
      },
      "Based on the search results, here are the CoRL 2026 submission deadlines in May 2026:\n\nAbstract submission deadline: May 26, 2026 11:59 UTC\n\nPaper submission deadline: May 29, 2026 11:59 UTC\n\nThe conference will be held November 9-12, 2026 in Austin, Texas, US"
    ],
    "durationSeconds": 6.500699919000006
  },
  "sourceToolAssistantUUID": "f8a73707-07bd-4183-851e-82d3cc55f87a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 57 · 2026-05-13T11:33:28.476Z_

```json
{
  "parentUuid": "99e2ec0a-16a0-48da-be7c-a6904245e00e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "5d33bf85-c3eb-4627-8211-11797b5de9e8",
  "timestamp": "2026-05-13T11:33:28.476Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 58 · 2026-05-13T11:33:55.549Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've confirmed the CoRL deadline. Now let me think carefully about the revision.

**Summary of research findings:**

1. **ICML 2026 clipping paper** (Off-Policy Token Clipped SFT): Token-level gradient clipping as trust region for SFT→RL. LLM domain. 7.09% RL improvement, 11.54% reduced forgetting. Benchmarks: ALFWorld, ScienceWorld.

2. **iw-SFT EMA**: Confirmed - uses EMA (θ_q = α·θ_q + (1-α)·θ) for continuous control only. 

The EMA approach applies importance weights rather than reducing the loss directly, though the specific alpha value isn't documented.

3. **Related SFT→RL work**:
   - PSFT (arXiv Aug 2025): Trust-region SFT via PPO-style clipped surrogate
   - DFT (ICLR 2026): Dynamic rescaling of SFT objective
   - Tailored Primitive (arXiv Nov 2025): SFT diversity for RL reasoning
   - PRISM (arXiv Apr 2026): Pre-alignment via on-policy distillation between SFT and RL

4. **No work found** that studies SFT *data quality* (via noise filtering /

I don't see any existing work that combines data quality improvements in SFT—through filtering or prioritized sampling—with downstream RL specifically for vision-language agents.

Now I'm thinking about how to address the reviewer's feedback on the novelty ceiling. The key insight is that I should reframe this as a discovery about SFT data quality being a critical bottleneck in VLA RL pipelines, with RAPID as the empirical demonstration. On the technical side, while EMA reference models exist in continuous control work and ReLo uses them in RL, and reducible loss appears in RHO-LOSS, the genuine novelty lies in combining these components specifically for SFT data quality filtering in vision-language agents.

I need to be much more precise about what's actually new here: the application to supervised imitation learning, the noise robustness argument, the SFT-to-RL cascade finding for VLAs, and the training-horizon-aware calibration theory. The proposal itself is too long and needs aggressive tightening throughout.

For the revision, I'm going to restructure the narrative entirely—properly cite the ICML 2026 clipping paper and related work on SFT-to-RL quality like PSFT and DFT, sharpen how RAPID differs from iw-SFT by clarifying that EMA there serves importance weighting rather than reducible loss, and add the CoRL go/no-go decision point.

Now I'm drafting the revised JSON with careful attention to reframing the core problem around the SFT-to-RL pipeline gap, positioning the opportunity honestly relative to existing work, updating the landscape with proper citations, tightening the approach with clearer novelty claims, and building in the resource estimate with decision gates.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d33bf85-c3eb-4627-8211-11797b5de9e8",
  "isSidechain": false,
  "requestId": "req_011CazViASRLHxQTLuoViUJc",
  "type": "assistant",
  "uuid": "6757e0cd-0177-47ff-aa65-974fc60f4de3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQZqSd4E93RotLyRsgvdh9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 50131,
      "output_tokens": 3032,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3032,
          "cache_read_input_tokens": 50131,
          "cache_creation_input_tokens": 723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 723
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

_source line 59 · 2026-05-13T11:34:03.343Z_

Now I have enough information to perform a deep revision. Let me synthesize my findings and think through the changes.

**Key research findings:**
1. **ICML 2026 clipping paper** confirmed: token-level gradient clipping for SFT→RL in LLMs (ALFWorld, ScienceWorld). 7.09% RL gain, 11.54% reduced forgetting.
2. **iw-SFT EMA** confirmed: uses EMA (θ_q = α·θ_q + (1-α)·θ) but ONLY for continuous control, ONLY for importance weights — not reducible loss decomposition.
3. **Additional SFT→RL work found**: PSFT (trust-region SFT), DFT (ICLR 2026, dynamic SFT rescaling), Tailored Primitive (SFT diversity for RL), PRISM (pre-alignment via on-policy distillation between SFT and RL).
4. **No work found** studying SFT *data quality via noise filtering* → downstream RL specifically for VLAs.

The stagnation at 3.5 reflects a narrative problem, not just missing citations. I'm doing a **major revision** that restructures the contribution hierarchy: the RAPID+RL pipeline finding becomes the headline, with the method as the mechanism that demonstrates it. I'll also honestly reposition relative to iw-SFT's EMA and the ICML 2026 clipping paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6757e0cd-0177-47ff-aa65-974fc60f4de3",
  "isSidechain": false,
  "requestId": "req_011CazViASRLHxQTLuoViUJc",
  "type": "assistant",
  "uuid": "bb3efa8c-9151-4493-9934-84d224d83b57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQZqSd4E93RotLyRsgvdh9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 50131,
      "output_tokens": 3032,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3032,
          "cache_read_input_tokens": 50131,
          "cache_creation_input_tokens": 723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 723
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

_source line 60 · 2026-05-13T11:34:40.712Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01PXQWNFe5K9qqsCfqauvsQk`</summary>

```json
{
  "description": "Draft complete revised idea JSON",
  "prompt": "You are helping revise a research proposal. Based on the following analysis, produce the complete revised JSON. I will provide the original JSON structure and my specific revision notes.\n\n## Revision strategy: MAJOR REVISION\n\nThe core changes:\n1. Reframe narrative: RAPID+RL pipeline finding is THE headline contribution. The method (EMA reducible loss) is the mechanism.\n2. Honestly reposition relative to iw-SFT (which already uses EMA for continuous control) and the ICML 2026 clipping paper.\n3. Tighten everything — the proposal is too long.\n4. Add CoRL go/no-go by May 22.\n5. Frame finite-T theory as qualitative prediction.\n6. Acknowledge synthetic noise limitation.\n\n## Specific changes needed per section:\n\n### core_problem\nReframe to emphasize the unexplored gap: \"Does SFT data quality affect downstream RL outcomes for VLAs?\" RAPID is the mechanism to test this.\n\n### opportunity\n- ADD: ICML 2026 \"Off-Policy Token Clipped SFT\" (Tian-Shuo Liu et al.) — shows SFT technique affects RL for LLMs via token-level gradient clipping (7.09% RL improvement, 11.54% reduced forgetting on ALFWorld/ScienceWorld). RAPID's differentiation: data-level noise filtering vs. token-level trust region; VLA domain vs. LLM domain.\n- ADD: PSFT (arXiv Aug 2025, 2508.17784) — trust-region SFT via PPO-style clipped surrogate. Related but different mechanism.\n- ADD: DFT (ICLR 2026, arXiv 2508.05629) — dynamic rescaling of SFT objective based on token probability.\n- ADD: Tailored Primitive (arXiv Nov 2025, 2511.12429) — SFT diversity affects downstream RL reasoning performance.\n- ADD: PRISM (arXiv Apr 2026, 2604.28123) — pre-alignment via on-policy distillation between SFT and RL for multimodal models.\n- REVISE: iw-SFT positioning — acknowledge it uses EMA for continuous control experiments. RAPID's novelty over iw-SFT is: (a) reducible loss decomposition (not just importance weights), (b) PER-style sampling (not multiplicative reweighting), (c) noise robustness from the max(0,·) clamp.\n- REVISE: Narrow the \"first\" claim — \"first to study SFT *data quality via noise-filtering prioritization* → RL for *VLAs*\" rather than broadly \"first to study SFT quality → RL.\"\n\n### landscape\nAdd the new references properly. Tighten existing entries. Key additions:\n- \"Off-Policy Token Clipped SFT Yields a Robust Cold-Start\" (ICML 2026, poster) — token-level gradient clipping as trust region for SFT→RL\n- \"Proximal Supervised Fine-Tuning\" (arXiv Aug 2025) — PPO-style trust region for SFT\n- \"On the Generalization of SFT: A RL Perspective with Reward Rectification\" [DFT] (ICLR 2026) — dynamic rescaling of SFT\n- \"Tailored Primitive Initialization is the Secret Key to RL\" (arXiv Nov 2025) — SFT diversity for RL\n- \"PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal RL\" (arXiv Apr 2026) — distribution alignment between SFT and RL\n\nUpdate the gap statement to be more honest: \"Multiple works study how SFT *technique* affects downstream RL (gradient clipping, trust regions, distribution alignment), but none study how SFT *data quality* — which demonstrations are prioritized during training — affects downstream RL for VLAs.\"\n\n### approach\n- Contribution 1: Reframe honestly. \"iw-SFT proposed EMA for importance weighting in continuous control; RAPID uses EMA for reducible loss decomposition, which provides noise robustness beyond what importance weighting alone offers.\" The novelty is the reducible loss decomposition purpose, not the EMA mechanism itself.\n- Contribution 4 (RAPID+RL): Elevate to THE primary contribution. Position as: \"The first empirical test of whether SFT data quality (via noise-filtering prioritization) affects downstream RL convergence for VLAs.\" Differentiate from ICML 2026 clipping paper: \"The ICML 2026 work shows token-level gradient clipping during SFT improves downstream RL for LLMs; we show data-level noise filtering during SFT improves downstream RL for VLAs — complementary findings across domains and mechanisms.\"\n- Theory (Contribution 3): Reduce emphasis. Frame finite-T bounds as qualitative predictions (linear vs quadratic growth pattern) rather than quantitative (exact T₀). Acknowledge C₁, C₂ depend on hard-to-estimate loss landscape properties.\n- CoRL timeline: Add explicit go/no-go by May 22. If first noise-injection results unavailable, fall back to AAAI only.\n- Noise injection: Acknowledge limitation — synthetic corruption ≠ real-world noise. Frame as controlled mechanism test. OXE (AAAI version) addresses real-world heterogeneity.\n\n### key_references\nAdd:\n- \"Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start (ICML 2026)\"\n- \"Proximal Supervised Fine-Tuning [PSFT] (arXiv Aug 2025)\"\n- \"On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification [DFT] (ICLR 2026)\"\n- \"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning (arXiv Nov 2025)\"\n- \"PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning (arXiv Apr 2026)\"\n\n### resource_estimate\nAdd go/no-go language for CoRL.\n\n## Output format\nOutput ONLY the complete JSON object. Include all fields from the original, plus \"change_type\": \"major\". Make sure the JSON is valid and complete.\n\nHere is the original JSON structure with all field names:\n- title\n- core_problem\n- opportunity  \n- landscape\n- approach\n- resource_estimate (with manual, human_in_loop, auto_research sub-objects)\n- target_venues (array)\n- level\n- key_references (array)\n- description\n- project_name\n- source\n- change_type (NEW - set to \"major\")\n\nNow produce the complete revised JSON. Be thorough but tighter than the original — every section should be meaningfully shorter while covering more ground. The total length of opportunity + landscape + approach should be noticeably reduced from the original. Cut repetitive caveats and hedge language. State things once, clearly.\n\nIMPORTANT: This must be valid JSON. Use proper escaping for special characters. Do not use actual newlines inside JSON string values — use \\n instead.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb3efa8c-9151-4493-9934-84d224d83b57",
  "isSidechain": false,
  "requestId": "req_011CazViASRLHxQTLuoViUJc",
  "type": "assistant",
  "uuid": "a17a87e3-bb61-4ce1-afb8-e5abf54d113b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQZqSd4E93RotLyRsgvdh9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 50131,
      "output_tokens": 3032,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3032,
          "cache_read_input_tokens": 50131,
          "cache_creation_input_tokens": 723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 723
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

_source line 61 · 2026-05-13T11:35:58.203Z_

<details><summary>↩ Tool result · `toolu_01PXQWNFe5K9qqsCfqauvsQk`</summary>

````text


I need to produce a complete revised JSON based on the detailed revision notes. Let me construct this carefully, ensuring valid JSON with proper escaping.

```json
{
  "title": "RAPID: Reducible-Loss Prioritized SFT and Its Effect on Downstream RL for Vision-Language-Action Models",
  "core_problem": "Does SFT data quality affect downstream RL outcomes for vision-language-action models? Current VLA pipelines (SFT → RL) treat all demonstrations equally during supervised fine-tuning, ignoring variation in data quality. Noisy or redundant demonstrations may degrade the SFT checkpoint that initializes RL, yet no prior work has isolated this effect for VLAs. RAPID provides a mechanism to test this: by decomposing per-sample loss into reducible (learnable) and irreducible (noise) components via an EMA reference model, it prioritizes high-signal demonstrations and filters noise. The open question is whether this data-level filtering during SFT measurably improves downstream RL convergence and final policy performance.",
  "opportunity": "Three converging trends create a timely opening:\n\n1. SFT→RL pipelines are standard for VLAs (OpenVLA, π₀, RT-2) but SFT data quality's downstream RL effect is unstudied. Multiple works now show SFT *technique* matters for downstream RL — the ICML 2026 'Off-Policy Token Clipped SFT' paper (Tian-Shuo Liu et al.) demonstrates token-level gradient clipping during SFT yields 7.09% RL improvement and 11.54% reduced forgetting on ALFWorld/ScienceWorld; PSFT (arXiv Aug 2025, 2508.17784) applies PPO-style clipped surrogates to SFT; DFT (ICLR 2026, 2508.05629) dynamically rescales the SFT objective; 'Tailored Primitive Initialization' (arXiv Nov 2025, 2511.12429) shows SFT demonstration diversity affects downstream RL reasoning; PRISM (arXiv Apr 2026, 2604.28123) aligns SFT and RL distributions via on-policy distillation for multimodal models. Yet none study how *data quality* — which demonstrations are prioritized — affects downstream RL for VLAs. RAPID fills this gap with data-level noise filtering rather than token-level or objective-level modifications.\n\n2. Reducible loss prioritization is underexplored for policy learning. RHO-1 and subsequent work show token/example-level prioritization accelerates LLM pretraining and SFT, but no one has applied reducible loss decomposition to VLA fine-tuning or measured its downstream RL impact. iw-SFT (Hejna et al.) uses an EMA reference model for importance-weighted SFT in continuous control, but serves a different purpose: importance weighting to approximate on-policy gradients. RAPID uses EMA for reducible loss decomposition — separating learnable signal from irreducible noise — which provides explicit noise robustness via the max(0,·) clamp that importance weighting lacks. RAPID also uses PER-style prioritized sampling rather than multiplicative reweighting.\n\n3. Real-world robot datasets (OXE, DROID) are heterogeneous and noisy, making data quality filtering practically important. RAPID's noise robustness is directly relevant to scaling VLA training on such datasets.\n\nRAPID is the first method to study SFT data quality via noise-filtering prioritization and its effect on downstream RL for VLAs.",
  "landscape": {
    "data_quality_for_sft": "RHO-1 (2024) introduced reducible-loss token selection for LLM pretraining using a frozen reference. RAPID adapts this idea with an EMA reference (enabling continuous adaptation) and applies it to VLA fine-tuning with PER-style sampling.",
    "importance_weighted_sft": "iw-SFT (Hejna et al., 2025) uses an EMA reference model to compute importance weights for SFT in continuous control, approximating on-policy gradients. RAPID differs in mechanism (reducible loss decomposition vs. importance weighting), sampling strategy (PER-style vs. multiplicative reweighting), and domain (VLAs). The max(0,·) clamp in reducible loss provides noise robustness absent in importance weighting.",
    "sft_technique_for_rl": "A growing body of work studies how SFT *technique* affects downstream RL: (1) Off-Policy Token Clipped SFT (ICML 2026, poster) — token-level gradient clipping as a trust region for SFT→RL in LLMs; (2) PSFT (arXiv Aug 2025, 2508.17784) — PPO-style clipped surrogate applied to SFT; (3) DFT (ICLR 2026, 2508.05629) — dynamic rescaling of SFT objective based on token probability; (4) Tailored Primitive Initialization (arXiv Nov 2025, 2511.12429) — demonstration diversity during SFT affects downstream RL reasoning; (5) PRISM (arXiv Apr 2026, 2604.28123) — on-policy distillation to align SFT and RL distributions for multimodal models.",
    "prioritized_experience_replay": "PER (Schaul et al., 2016) prioritizes high-TD-error transitions in RL replay buffers. RAPID adapts PER-style sampling to SFT, using reducible loss as the priority signal instead of TD error.",
    "vla_fine_tuning": "OpenVLA (2024), π₀ (2024), and RT-2 (2023) establish SFT→RL as the standard VLA pipeline but do not study data quality effects during SFT.",
    "gap": "Multiple works study how SFT *technique* affects downstream RL (gradient clipping, trust regions, objective rescaling, distribution alignment), but none study how SFT *data quality* — which demonstrations are prioritized during training — affects downstream RL for VLAs."
  },
  "approach": {
    "contribution_1_rapid_method": "RAPID decomposes per-sample SFT loss into reducible and irreducible components using an EMA reference model. The reducible loss r(x) = max(0, L_student(x) - L_ema(x)) isolates learnable signal; the max(0,·) clamp prevents negative priorities from noisy samples. Samples are drawn via PER-style prioritized sampling proportional to r(x)^α. Compared to iw-SFT, which uses EMA for importance weighting to approximate on-policy gradients, RAPID uses EMA for a different purpose: noise-robust loss decomposition. The reducible loss formulation, PER-style sampling, and max(0,·) clamping are the methodological distinctions.",
    "contribution_2_empirical_sft": "Controlled experiments on LIBERO benchmark: (a) inject calibrated noise (action perturbation, observation corruption, trajectory reversal) at known rates into SFT data; (b) compare RAPID vs. uniform SFT on noisy data; (c) measure SFT checkpoint quality via success rate and loss decomposition metrics. This establishes RAPID's noise filtering capability. Limitation: synthetic corruption is a controlled proxy, not real-world noise. The OXE experiments (AAAI scope) address real heterogeneity.",
    "contribution_3_theory": "Finite-horizon analysis of EMA-based reducible loss under distribution shift. The main qualitative prediction: reducible loss approximation error grows linearly with horizon T (due to EMA tracking) while frozen-reference error grows quadratically. This predicts RAPID's advantage increases with fine-tuning duration. The bounds involve constants C₁, C₂ depending on loss landscape properties (smoothness, gradient variance) that are hard to estimate precisely, so we validate the qualitative growth pattern empirically rather than claiming quantitative predictions for exact crossover points.",
    "contribution_4_rapid_plus_rl": "THE PRIMARY CONTRIBUTION. The first empirical test of whether SFT data quality via noise-filtering prioritization affects downstream RL convergence for VLAs. Protocol: (a) train matched SFT checkpoints (RAPID vs. uniform) on clean and noisy LIBERO data; (b) fine-tune each checkpoint with RL (GRPO or similar); (c) measure RL convergence speed, final success rate, and sample efficiency. Hypothesis: RAPID-initialized RL converges faster and to higher performance, especially under noisy SFT data. Differentiation from ICML 2026 clipping paper: they show token-level gradient clipping during SFT improves downstream RL for LLMs on text tasks; we show data-level noise filtering during SFT improves downstream RL for VLAs on robotic manipulation — complementary findings across domains and mechanisms.",
    "timeline": "CoRL 2026 (deadline ~June 2026): Contributions 1-2 + 4 (RAPID+RL on LIBERO with noise injection). GO/NO-GO BY MAY 22: if first noise-injection + RL results are not available by May 22, fall back to AAAI-only submission. AAAI 2026 (deadline ~Aug 2026): Full paper adding Contribution 3 (theory) + OXE multi-dataset experiments addressing real-world data heterogeneity."
  },
  "resource_estimate": {
    "manual": {
      "hours": 40,
      "description": "Core implementation: RAPID sampling integration with OpenVLA training loop, noise injection pipeline, RL fine-tuning pipeline (GRPO), experiment orchestration scripts, and results analysis."
    },
    "human_in_loop": {
      "hours": 15,
      "description": "Experiment design review, hyperparameter selection for noise injection rates and PER α/β schedules, go/no-go decision by May 22 based on initial RAPID+RL results, paper writing and revision."
    },
    "auto_research": {
      "hours": 200,
      "description": "GPU compute for LIBERO experiments: SFT training (RAPID vs. uniform × clean vs. noisy × 3 noise types × 3 seeds), RL fine-tuning from each SFT checkpoint, evaluation rollouts. Estimated 8-12 A100-hours per SFT run, 15-20 A100-hours per RL run."
    }
  },
  "target_venues": [
    {
      "venue": "CoRL 2026",
      "deadline": "June 2026",
      "scope": "RAPID method + noise injection SFT experiments + RAPID→RL pipeline results on LIBERO",
      "go_no_go": "Decision by May 22 — if first noise-injection + RL results unavailable, fall back to AAAI only"
    },
    {
      "venue": "AAAI 2026",
      "deadline": "August 2026",
      "scope": "Full paper: RAPID method + theory + LIBERO noise experiments + RAPID→RL pipeline + OXE multi-dataset experiments"
    }
  ],
  "level": "PhD",
  "key_references": [
    "RHO-1: Not All Tokens Are What You Need (Lin et al., 2024)",
    "Importance Weighted SFT [iw-SFT] (Hejna et al., 2025)",
    "Prioritized Experience Replay (Schaul et al., 2016)",
    "OpenVLA: An Open-Source Vision-Language-Action Model (Kim et al., 2024)",
    "π₀: A Vision-Language-Action Flow Model for General Robot Control (Black et al., 2024)",
    "GRPO: Group Relative Policy Optimization (Shao et al., 2024)",
    "Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start (Tian-Shuo Liu et al., ICML 2026)",
    "Proximal Supervised Fine-Tuning [PSFT] (arXiv Aug 2025, 2508.17784)",
    "On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification [DFT] (ICLR 2026, arXiv 2508.05629)",
    "Tailored Primitive Initialization is the Secret Key to Reinforcement Learning (arXiv Nov 2025, 2511.12429)",
    "PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning (arXiv Apr 2026, 2604.28123)"
  ],
  "description": "RAPID uses EMA-based reducible loss decomposition to prioritize high-signal demonstrations during VLA supervised fine-tuning, filtering noise via max(0,·) clamping and PER-style sampling. The headline contribution is the first empirical test of whether SFT data quality — controlled via noise-filtering prioritization — affects downstream RL convergence for vision-language-action models. Complementary to recent work on SFT *technique* for RL (token clipping, trust regions, distribution alignment), RAPID addresses SFT *data quality* for RL in the VLA domain.",
  "project_name": "RAPID",
  "source": "revised_proposal",
  "change_type": "major"
}
```

This is the complete revised JSON incorporating all requested changes:

**Key revisions made:**

1. **core_problem**: Reframed around the question "Does SFT data quality affect downstream RL for VLAs?" with RAPID as the mechanism to test it.

2. **opportunity**: Added all five new references (ICML 2026 clipping paper, PSFT, DFT, Tailored Primitive, PRISM). Honestly repositioned relative to iw-SFT with three specific differentiators (reducible loss decomposition vs. importance weighting, PER-style sampling vs. multiplicative reweighting, max(0,·) noise robustness). Narrowed the "first" claim to "first to study SFT data quality via noise-filtering prioritization → RL for VLAs."

3. **landscape**: Added all five new entries. Updated gap statement to honestly acknowledge multiple works study SFT technique for RL, while RAPID addresses data quality.

4. **approach**: Elevated Contribution 4 (RAPID+RL) as THE primary contribution. Reframed Contribution 1 honestly relative to iw-SFT. Reduced theory emphasis to qualitative predictions with acknowledged limitations of C₁/C₂ constants. Added explicit May 22 go/no-go for CoRL. Acknowledged synthetic noise limitation.

5. **key_references**: Added all five new references.

6. **resource_estimate** and **target_venues**: Added go/no-go language for CoRL.

7. **change_type**: Set to "major".

8. **Overall tightening**: Removed repetitive hedging, stated things once clearly, reduced total verbosity while covering more ground.

agentId: a935c6d73eff95005 (use SendMessage with to: 'a935c6d73eff95005' to continue this agent)
&lt;usage>total_tokens: 14154
tool_uses: 0
duration_ms: 77478&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "a17a87e3-bb61-4ce1-afb8-e5abf54d113b",
  "isSidechain": false,
  "promptId": "951ab6a2-d418-436f-92d5-153d7ace18a9",
  "type": "user",
  "uuid": "bafaeae9-855c-4977-959d-8497eb43da71",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping revise a research proposal. Based on the following analysis, produce the complete revised JSON. I will provide the original JSON structure and my specific revision notes.\n\n## Revision strategy: MAJOR REVISION\n\nThe core changes:\n1. Reframe narrative: RAPID+RL pipeline finding is THE headline contribution. The method (EMA reducible loss) is the mechanism.\n2. Honestly reposition relative to iw-SFT (which already uses EMA for continuous control) and the ICML 2026 clipping paper.\n3. Tighten everything — the proposal is too long.\n4. Add CoRL go/no-go by May 22.\n5. Frame finite-T theory as qualitative prediction.\n6. Acknowledge synthetic noise limitation.\n\n## Specific changes needed per section:\n\n### core_problem\nReframe to emphasize the unexplored gap: \"Does SFT data quality affect downstream RL outcomes for VLAs?\" RAPID is the mechanism to test this.\n\n### opportunity\n- ADD: ICML 2026 \"Off-Policy Token Clipped SFT\" (Tian-Shuo Liu et al.) — shows SFT technique affects RL for LLMs via token-level gradient clipping (7.09% RL improvement, 11.54% reduced forgetting on ALFWorld/ScienceWorld). RAPID's differentiation: data-level noise filtering vs. token-level trust region; VLA domain vs. LLM domain.\n- ADD: PSFT (arXiv Aug 2025, 2508.17784) — trust-region SFT via PPO-style clipped surrogate. Related but different mechanism.\n- ADD: DFT (ICLR 2026, arXiv 2508.05629) — dynamic rescaling of SFT objective based on token probability.\n- ADD: Tailored Primitive (arXiv Nov 2025, 2511.12429) — SFT diversity affects downstream RL reasoning performance.\n- ADD: PRISM (arXiv Apr 2026, 2604.28123) — pre-alignment via on-policy distillation between SFT and RL for multimodal models.\n- REVISE: iw-SFT positioning — acknowledge it uses EMA for continuous control experiments. RAPID's novelty over iw-SFT is: (a) reducible loss decomposition (not just importance weights), (b) PER-style sampling (not multiplicative reweighting), (c) noise robustness from the max(0,·) clamp.\n- REVISE: Narrow the \"first\" claim — \"first to study SFT *data quality via noise-filtering prioritization* → RL for *VLAs*\" rather than broadly \"first to study SFT quality → RL.\"\n\n### landscape\nAdd the new references properly. Tighten existing entries. Key additions:\n- \"Off-Policy Token Clipped SFT Yields a Robust Cold-Start\" (ICML 2026, poster) — token-level gradient clipping as trust region for SFT→RL\n- \"Proximal Supervised Fine-Tuning\" (arXiv Aug 2025) — PPO-style trust region for SFT\n- \"On the Generalization of SFT: A RL Perspective with Reward Rectification\" [DFT] (ICLR 2026) — dynamic rescaling of SFT\n- \"Tailored Primitive Initialization is the Secret Key to RL\" (arXiv Nov 2025) — SFT diversity for RL\n- \"PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal RL\" (arXiv Apr 2026) — distribution alignment between SFT and RL\n\nUpdate the gap statement to be more honest: \"Multiple works study how SFT *technique* affects downstream RL (gradient clipping, trust regions, distribution alignment), but none study how SFT *data quality* — which demonstrations are prioritized during training — affects downstream RL for VLAs.\"\n\n### approach\n- Contribution 1: Reframe honestly. \"iw-SFT proposed EMA for importance weighting in continuous control; RAPID uses EMA for reducible loss decomposition, which provides noise robustness beyond what importance weighting alone offers.\" The novelty is the reducible loss decomposition purpose, not the EMA mechanism itself.\n- Contribution 4 (RAPID+RL): Elevate to THE primary contribution. Position as: \"The first empirical test of whether SFT data quality (via noise-filtering prioritization) affects downstream RL convergence for VLAs.\" Differentiate from ICML 2026 clipping paper: \"The ICML 2026 work shows token-level gradient clipping during SFT improves downstream RL for LLMs; we show data-level noise filtering during SFT improves downstream RL for VLAs — complementary findings across domains and mechanisms.\"\n- Theory (Contribution 3): Reduce emphasis. Frame finite-T bounds as qualitative predictions (linear vs quadratic growth pattern) rather than quantitative (exact T₀). Acknowledge C₁, C₂ depend on hard-to-estimate loss landscape properties.\n- CoRL timeline: Add explicit go/no-go by May 22. If first noise-injection results unavailable, fall back to AAAI only.\n- Noise injection: Acknowledge limitation — synthetic corruption ≠ real-world noise. Frame as controlled mechanism test. OXE (AAAI version) addresses real-world heterogeneity.\n\n### key_references\nAdd:\n- \"Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start (ICML 2026)\"\n- \"Proximal Supervised Fine-Tuning [PSFT] (arXiv Aug 2025)\"\n- \"On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification [DFT] (ICLR 2026)\"\n- \"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning (arXiv Nov 2025)\"\n- \"PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning (arXiv Apr 2026)\"\n\n### resource_estimate\nAdd go/no-go language for CoRL.\n\n## Output format\nOutput ONLY the complete JSON object. Include all fields from the original, plus \"change_type\": \"major\". Make sure the JSON is valid and complete.\n\nHere is the original JSON structure with all field names:\n- title\n- core_problem\n- opportunity  \n- landscape\n- approach\n- resource_estimate (with manual, human_in_loop, auto_research sub-objects)\n- target_venues (array)\n- level\n- key_references (array)\n- description\n- project_name\n- source\n- change_type (NEW - set to \"major\")\n\nNow produce the complete revised JSON. Be thorough but tighter than the original — every section should be meaningfully shorter while covering more ground. The total length of opportunity + landscape + approach should be noticeably reduced from the original. Cut repetitive caveats and hedge language. State things once, clearly.\n\nIMPORTANT: This must be valid JSON. Use proper escaping for special characters. Do not use actual newlines inside JSON string values — use \\n instead.\n",
    "agentId": "a935c6d73eff95005",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nI need to produce a complete revised JSON based on the detailed revision notes. Let me construct this carefully, ensuring valid JSON with proper escaping.\n\n```json\n{\n  \"title\": \"RAPID: Reducible-Loss Prioritized SFT and Its Effect on Downstream RL for Vision-Language-Action Models\",\n  \"core_problem\": \"Does SFT data quality affect downstream RL outcomes for vision-language-action models? Current VLA pipelines (SFT → RL) treat all demonstrations equally during supervised fine-tuning, ignoring variation in data quality. Noisy or redundant demonstrations may degrade the SFT checkpoint that initializes RL, yet no prior work has isolated this effect for VLAs. RAPID provides a mechanism to test this: by decomposing per-sample loss into reducible (learnable) and irreducible (noise) components via an EMA reference model, it prioritizes high-signal demonstrations and filters noise. The open question is whether this data-level filtering during SFT measurably improves downstream RL convergence and final policy performance.\",\n  \"opportunity\": \"Three converging trends create a timely opening:\\n\\n1. SFT→RL pipelines are standard for VLAs (OpenVLA, π₀, RT-2) but SFT data quality's downstream RL effect is unstudied. Multiple works now show SFT *technique* matters for downstream RL — the ICML 2026 'Off-Policy Token Clipped SFT' paper (Tian-Shuo Liu et al.) demonstrates token-level gradient clipping during SFT yields 7.09% RL improvement and 11.54% reduced forgetting on ALFWorld/ScienceWorld; PSFT (arXiv Aug 2025, 2508.17784) applies PPO-style clipped surrogates to SFT; DFT (ICLR 2026, 2508.05629) dynamically rescales the SFT objective; 'Tailored Primitive Initialization' (arXiv Nov 2025, 2511.12429) shows SFT demonstration diversity affects downstream RL reasoning; PRISM (arXiv Apr 2026, 2604.28123) aligns SFT and RL distributions via on-policy distillation for multimodal models. Yet none study how *data quality* — which demonstrations are prioritized — affects downstream RL for VLAs. RAPID fills this gap with data-level noise filtering rather than token-level or objective-level modifications.\\n\\n2. Reducible loss prioritization is underexplored for policy learning. RHO-1 and subsequent work show token/example-level prioritization accelerates LLM pretraining and SFT, but no one has applied reducible loss decomposition to VLA fine-tuning or measured its downstream RL impact. iw-SFT (Hejna et al.) uses an EMA reference model for importance-weighted SFT in continuous control, but serves a different purpose: importance weighting to approximate on-policy gradients. RAPID uses EMA for reducible loss decomposition — separating learnable signal from irreducible noise — which provides explicit noise robustness via the max(0,·) clamp that importance weighting lacks. RAPID also uses PER-style prioritized sampling rather than multiplicative reweighting.\\n\\n3. Real-world robot datasets (OXE, DROID) are heterogeneous and noisy, making data quality filtering practically important. RAPID's noise robustness is directly relevant to scaling VLA training on such datasets.\\n\\nRAPID is the first method to study SFT data quality via noise-filtering prioritization and its effect on downstream RL for VLAs.\",\n  \"landscape\": {\n    \"data_quality_for_sft\": \"RHO-1 (2024) introduced reducible-loss token selection for LLM pretraining using a frozen reference. RAPID adapts this idea with an EMA reference (enabling continuous adaptation) and applies it to VLA fine-tuning with PER-style sampling.\",\n    \"importance_weighted_sft\": \"iw-SFT (Hejna et al., 2025) uses an EMA reference model to compute importance weights for SFT in continuous control, approximating on-policy gradients. RAPID differs in mechanism (reducible loss decomposition vs. importance weighting), sampling strategy (PER-style vs. multiplicative reweighting), and domain (VLAs). The max(0,·) clamp in reducible loss provides noise robustness absent in importance weighting.\",\n    \"sft_technique_for_rl\": \"A growing body of work studies how SFT *technique* affects downstream RL: (1) Off-Policy Token Clipped SFT (ICML 2026, poster) — token-level gradient clipping as a trust region for SFT→RL in LLMs; (2) PSFT (arXiv Aug 2025, 2508.17784) — PPO-style clipped surrogate applied to SFT; (3) DFT (ICLR 2026, 2508.05629) — dynamic rescaling of SFT objective based on token probability; (4) Tailored Primitive Initialization (arXiv Nov 2025, 2511.12429) — demonstration diversity during SFT affects downstream RL reasoning; (5) PRISM (arXiv Apr 2026, 2604.28123) — on-policy distillation to align SFT and RL distributions for multimodal models.\",\n    \"prioritized_experience_replay\": \"PER (Schaul et al., 2016) prioritizes high-TD-error transitions in RL replay buffers. RAPID adapts PER-style sampling to SFT, using reducible loss as the priority signal instead of TD error.\",\n    \"vla_fine_tuning\": \"OpenVLA (2024), π₀ (2024), and RT-2 (2023) establish SFT→RL as the standard VLA pipeline but do not study data quality effects during SFT.\",\n    \"gap\": \"Multiple works study how SFT *technique* affects downstream RL (gradient clipping, trust regions, objective rescaling, distribution alignment), but none study how SFT *data quality* — which demonstrations are prioritized during training — affects downstream RL for VLAs.\"\n  },\n  \"approach\": {\n    \"contribution_1_rapid_method\": \"RAPID decomposes per-sample SFT loss into reducible and irreducible components using an EMA reference model. The reducible loss r(x) = max(0, L_student(x) - L_ema(x)) isolates learnable signal; the max(0,·) clamp prevents negative priorities from noisy samples. Samples are drawn via PER-style prioritized sampling proportional to r(x)^α. Compared to iw-SFT, which uses EMA for importance weighting to approximate on-policy gradients, RAPID uses EMA for a different purpose: noise-robust loss decomposition. The reducible loss formulation, PER-style sampling, and max(0,·) clamping are the methodological distinctions.\",\n    \"contribution_2_empirical_sft\": \"Controlled experiments on LIBERO benchmark: (a) inject calibrated noise (action perturbation, observation corruption, trajectory reversal) at known rates into SFT data; (b) compare RAPID vs. uniform SFT on noisy data; (c) measure SFT checkpoint quality via success rate and loss decomposition metrics. This establishes RAPID's noise filtering capability. Limitation: synthetic corruption is a controlled proxy, not real-world noise. The OXE experiments (AAAI scope) address real heterogeneity.\",\n    \"contribution_3_theory\": \"Finite-horizon analysis of EMA-based reducible loss under distribution shift. The main qualitative prediction: reducible loss approximation error grows linearly with horizon T (due to EMA tracking) while frozen-reference error grows quadratically. This predicts RAPID's advantage increases with fine-tuning duration. The bounds involve constants C₁, C₂ depending on loss landscape properties (smoothness, gradient variance) that are hard to estimate precisely, so we validate the qualitative growth pattern empirically rather than claiming quantitative predictions for exact crossover points.\",\n    \"contribution_4_rapid_plus_rl\": \"THE PRIMARY CONTRIBUTION. The first empirical test of whether SFT data quality via noise-filtering prioritization affects downstream RL convergence for VLAs. Protocol: (a) train matched SFT checkpoints (RAPID vs. uniform) on clean and noisy LIBERO data; (b) fine-tune each checkpoint with RL (GRPO or similar); (c) measure RL convergence speed, final success rate, and sample efficiency. Hypothesis: RAPID-initialized RL converges faster and to higher performance, especially under noisy SFT data. Differentiation from ICML 2026 clipping paper: they show token-level gradient clipping during SFT improves downstream RL for LLMs on text tasks; we show data-level noise filtering during SFT improves downstream RL for VLAs on robotic manipulation — complementary findings across domains and mechanisms.\",\n    \"timeline\": \"CoRL 2026 (deadline ~June 2026): Contributions 1-2 + 4 (RAPID+RL on LIBERO with noise injection). GO/NO-GO BY MAY 22: if first noise-injection + RL results are not available by May 22, fall back to AAAI-only submission. AAAI 2026 (deadline ~Aug 2026): Full paper adding Contribution 3 (theory) + OXE multi-dataset experiments addressing real-world data heterogeneity.\"\n  },\n  \"resource_estimate\": {\n    \"manual\": {\n      \"hours\": 40,\n      \"description\": \"Core implementation: RAPID sampling integration with OpenVLA training loop, noise injection pipeline, RL fine-tuning pipeline (GRPO), experiment orchestration scripts, and results analysis.\"\n    },\n    \"human_in_loop\": {\n      \"hours\": 15,\n      \"description\": \"Experiment design review, hyperparameter selection for noise injection rates and PER α/β schedules, go/no-go decision by May 22 based on initial RAPID+RL results, paper writing and revision.\"\n    },\n    \"auto_research\": {\n      \"hours\": 200,\n      \"description\": \"GPU compute for LIBERO experiments: SFT training (RAPID vs. uniform × clean vs. noisy × 3 noise types × 3 seeds), RL fine-tuning from each SFT checkpoint, evaluation rollouts. Estimated 8-12 A100-hours per SFT run, 15-20 A100-hours per RL run.\"\n    }\n  },\n  \"target_venues\": [\n    {\n      \"venue\": \"CoRL 2026\",\n      \"deadline\": \"June 2026\",\n      \"scope\": \"RAPID method + noise injection SFT experiments + RAPID→RL pipeline results on LIBERO\",\n      \"go_no_go\": \"Decision by May 22 — if first noise-injection + RL results unavailable, fall back to AAAI only\"\n    },\n    {\n      \"venue\": \"AAAI 2026\",\n      \"deadline\": \"August 2026\",\n      \"scope\": \"Full paper: RAPID method + theory + LIBERO noise experiments + RAPID→RL pipeline + OXE multi-dataset experiments\"\n    }\n  ],\n  \"level\": \"PhD\",\n  \"key_references\": [\n    \"RHO-1: Not All Tokens Are What You Need (Lin et al., 2024)\",\n    \"Importance Weighted SFT [iw-SFT] (Hejna et al., 2025)\",\n    \"Prioritized Experience Replay (Schaul et al., 2016)\",\n    \"OpenVLA: An Open-Source Vision-Language-Action Model (Kim et al., 2024)\",\n    \"π₀: A Vision-Language-Action Flow Model for General Robot Control (Black et al., 2024)\",\n    \"GRPO: Group Relative Policy Optimization (Shao et al., 2024)\",\n    \"Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start (Tian-Shuo Liu et al., ICML 2026)\",\n    \"Proximal Supervised Fine-Tuning [PSFT] (arXiv Aug 2025, 2508.17784)\",\n    \"On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification [DFT] (ICLR 2026, arXiv 2508.05629)\",\n    \"Tailored Primitive Initialization is the Secret Key to Reinforcement Learning (arXiv Nov 2025, 2511.12429)\",\n    \"PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning (arXiv Apr 2026, 2604.28123)\"\n  ],\n  \"description\": \"RAPID uses EMA-based reducible loss decomposition to prioritize high-signal demonstrations during VLA supervised fine-tuning, filtering noise via max(0,·) clamping and PER-style sampling. The headline contribution is the first empirical test of whether SFT data quality — controlled via noise-filtering prioritization — affects downstream RL convergence for vision-language-action models. Complementary to recent work on SFT *technique* for RL (token clipping, trust regions, distribution alignment), RAPID addresses SFT *data quality* for RL in the VLA domain.\",\n  \"project_name\": \"RAPID\",\n  \"source\": \"revised_proposal\",\n  \"change_type\": \"major\"\n}\n```\n\nThis is the complete revised JSON incorporating all requested changes:\n\n**Key revisions made:**\n\n1. **core_problem**: Reframed around the question \"Does SFT data quality affect downstream RL for VLAs?\" with RAPID as the mechanism to test it.\n\n2. **opportunity**: Added all five new references (ICML 2026 clipping paper, PSFT, DFT, Tailored Primitive, PRISM). Honestly repositioned relative to iw-SFT with three specific differentiators (reducible loss decomposition vs. importance weighting, PER-style sampling vs. multiplicative reweighting, max(0,·) noise robustness). Narrowed the \"first\" claim to \"first to study SFT data quality via noise-filtering prioritization → RL for VLAs.\"\n\n3. **landscape**: Added all five new entries. Updated gap statement to honestly acknowledge multiple works study SFT technique for RL, while RAPID addresses data quality.\n\n4. **approach**: Elevated Contribution 4 (RAPID+RL) as THE primary contribution. Reframed Contribution 1 honestly relative to iw-SFT. Reduced theory emphasis to qualitative predictions with acknowledged limitations of C₁/C₂ constants. Added explicit May 22 go/no-go for CoRL. Acknowledged synthetic noise limitation.\n\n5. **key_references**: Added all five new references.\n\n6. **resource_estimate** and **target_venues**: Added go/no-go language for CoRL.\n\n7. **change_type**: Set to \"major\".\n\n8. **Overall tightening**: Removed repetitive hedging, stated things once clearly, reduced total verbosity while covering more ground."
      }
    ],
    "totalDurationMs": 77478,
    "totalTokens": 14154,
    "totalToolUseCount": 0,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10492,
      "cache_read_input_tokens": 0,
      "output_tokens": 3660,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10492
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3660,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 10492,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10492,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  },
  "sourceToolAssistantUUID": "a17a87e3-bb61-4ce1-afb8-e5abf54d113b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 62_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"RAPID: Reducible-Loss Adaptive Prioritized Replay for VLA Imitation Le…",
  "leafUuid": "bafaeae9-855c-4977-959d-8497eb43da71",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising RAPID: Addressing novelty gaps and clarifying SFT→RL contribution",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---

### Assistant

_source line 64 · 2026-05-13T11:36:16.269Z_

<details><summary>Logged reasoning block</summary>

```text
The agent produced a draft but it significantly deviated from the original JSON schema. The original has `opportunity`, `landscape`, `approach` as flat strings, not nested objects. The `resource_estimate` has a specific structure with `gpu_hours`, `gpu_utilization`, `timeline`, `team`, etc. The `target_venues` is an array of strings, not objects. The `level` is "solid" not "PhD". Let me fix these issues and produce a proper revision that matches the original schema exactly.

Let me re-draft the full JSON myself, properly matching the original schema while incorporating all the changes.

The key structural elements from the original:


- title: string
- core_problem: string
- opportunity: string (long paragraph)
- landscape: string (long paragraph)  
- approach: string (long paragraph)
- resource_estimate: { manual: {gpu_hours, gpu_utilization, timeline, team, estimated_gpu_cost}, human_in_loop: {gpu_hours, gpu_utilization, timeline, team, claude_api_cost, estimated_gpu_cost, risk_note}, auto_research: {gpu_hours, gpu_utilization, timeline, team, claude_api_cost, estimated_gpu_cost, speed_bottleneck, risk_note} }
- target_venues: array of strings
- level: string ("solid")
- key_references: array of strings
- description: string
- project_name: string
- source: string
- change_type: string ("NEW")

I'm working through the structure carefully. The title captures the core idea well, so I'll keep it as is. For the core problem, I need to sharpen the focus on the data quality bottleneck that emerges when transitioning from supervised fine-tuning to reinforcement learning. The opportunity section should be tighter and more honest about positioning relative to existing work like importance-weighted SFT and recent ICML submissions. I'm updating the landscape to include fresher references and clarify where the gap actually sits. The approach needs reordering to highlight the key contributions more clearly while staying grounded in what's realistic.

Building the JSON output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bafaeae9-855c-4977-959d-8497eb43da71",
  "isSidechain": false,
  "requestId": "req_011CazVuChuBHNfHKpKBN2z9",
  "type": "assistant",
  "uuid": "a05b3d26-0f69-489e-8dce-ebbcd0307001",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvWwRYkRoQxmWpDex6wuZ9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6765,
      "cache_read_input_tokens": 50854,
      "output_tokens": 8088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6765,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8088,
          "cache_read_input_tokens": 50854,
          "cache_creation_input_tokens": 6765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6765
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

_source line 65 · 2026-05-13T11:39:03.318Z_

The agent's draft has the right content but wrong schema structure. Let me produce the final revision with the correct format matching the original.

```json
{
  "title": "RAPID: Reducible-Loss Adaptive Prioritized Replay for VLA Imitation Learning",
  "core_problem": "Does SFT data quality — which demonstrations are prioritized during training — affect downstream RL outcomes for vision-language-action models? The VLA training paradigm is shifting from SFT-only to SFT→RL pipelines, where SFT quality is the critical determinant of RL success. SimpleVLA-RL shows SFT data *quantity* gates RL (0 demos → 0% RL success), but no work has isolated how SFT data *quality* affects RL convergence and final performance. Multiple recent works study how SFT *technique* affects RL (gradient clipping, trust regions, distribution alignment), but none address the orthogonal question of data-level filtering. RAPID provides the mechanism to test this: by decomposing per-sample loss into reducible (learnable) and irreducible (noise) components via an EMA reference model, it prioritizes high-signal demonstrations during SFT, producing cleaner checkpoints for downstream RL. The core hypothesis is that noise-filtered SFT → faster RL convergence and better sample efficiency, particularly in realistic settings where demonstration quality varies.",
  "opportunity": "Three converging trends create this opening:\n\n**1. SFT→RL pipelines are standard but SFT data quality's RL effect is unstudied.** SimpleVLA-RL (ICLR 2026) shows SFT accounts for 74pp of 82pp total improvement and SFT quantity gates RL success. 'What Can RL Bring to VLA Generalization?' (NeurIPS 2025) shows warm-start SFT yields ~50% faster RL convergence. A growing body of work now demonstrates that SFT *technique* matters for downstream RL: the ICML 2026 'Off-Policy Token Clipped SFT' (Tian-Shuo Liu et al.) shows token-level gradient clipping during SFT yields 7.09% RL improvement and 11.54% reduced forgetting on LLM agentic benchmarks; PSFT (arXiv 2508.17784) applies PPO-style clipped surrogates to SFT; DFT (ICLR 2026, 2508.05629) dynamically rescales the SFT objective; 'Tailored Primitive Initialization' (arXiv 2511.12429) shows SFT demonstration diversity affects downstream RL reasoning; PRISM (arXiv 2604.28123) aligns SFT and RL distributions via on-policy distillation. Yet none study how *data quality* — which demonstrations are prioritized during training — affects downstream RL for VLAs. RAPID fills this gap with data-level noise filtering rather than token/objective-level modifications.\n\n**2. Reducible loss decomposition is proven but unexploited in VLA SFT.** RHO-LOSS (ICML 2022) showed excess loss identifies learnable-not-yet-learnt data, achieving 18x speedup on noisy datasets. ReLo (NeurIPS 2023) adapted this to RL using SAC's pre-existing target network. Rho-1 (NeurIPS 2024) brought it to LLM pretraining with a fixed reference. iw-SFT (arXiv 2507.12856) uses an EMA reference for importance-weighted SFT in continuous control — but for trajectory-level importance weights approximating on-policy gradients, not for reducible loss decomposition. RAPID uses the EMA for a different purpose: computing R(x) = max(0, L_θ(x) − L_EMA(x)) to decompose loss into reducible and irreducible components. The max(0,·) clamp provides explicit noise suppression that importance weighting lacks. DS2 (ICLR 2025) performs dynamic instance-level reweighting but uses raw loss without reducible decomposition, inheriting noise overfitting risk. No existing work applies sample-level, continuously-adaptive reducible-loss *prioritized sampling* to VLA SFT.\n\n**3. VLA demonstration quality varies in practice.** The 'When Do Curricula Work?' finding (ICLR 2021) that curricula provide marginal benefits on clean benchmarks implies RAPID's value is in noisy/mixed-quality settings and the SFT→RL pipeline — not clean-data benchmarks where VLAs already achieve 97%+. LIBERO-Plus (CVPR 2026) exposed that high success rates on standard LIBERO mask fragility (OpenVLA-OFT: 97.1% → 70.0%). Real-world datasets (OXE, DROID) contain heterogeneous demonstration quality from varied operators. RAPID targets these realistic conditions.\n\n**The specific gap (honestly stated):** iw-SFT already uses EMA for continuous control importance weighting. RAPID's novelty over iw-SFT is threefold: (a) reducible loss decomposition (not trajectory probabilities for importance weights), providing noise-robust prioritization via the max(0,·) clamp; (b) PER-style sampling (controlling which samples are seen, not multiplicative loss reweighting); (c) training-horizon-aware τ calibration with finite-T theory. Furthermore, no work — including all SFT-technique-for-RL papers — has tested whether SFT *data quality via noise filtering* affects downstream RL for VLAs.",
  "landscape": "**Reducible/excess loss foundations:** RHO-LOSS (ICML 2022) selects points by excess loss over a fixed holdout-trained reference — 18x faster on noisy Clothing-1M. ReLo (NeurIPS 2023) computes reducible TD error using SAC's Polyak-averaged target network (double duty: TD stability + data scoring). Rho-1 (NeurIPS 2024) brings excess loss to LLM pretraining with a fixed reference for selective token training. All supervised applications use *static* reference models.\n\n**Dynamic instance-level reweighting:** DS2 (ICLR 2025) normalizes per-sample losses and applies transformation functions for dynamic reweighting during LLM pretraining, with formal convergence guarantees. Uses raw loss without reducible decomposition. LEAD (arXiv May 2025) uses EMA over *loss values* (not model parameters) for online data selection during LLM SFT. UDS (arXiv Oct 2025) uses nuclear norm of logits for utility-diversity batch selection without a reference model.\n\n**Importance-weighted SFT:** iw-SFT (arXiv Jul 2025, 2507.12856) proves SFT on curated data optimizes a lower bound on the RL objective. For continuous control (D4RL), it uses an EMA reference (θ_q = α·θ_q + (1-α)·θ) for trajectory-level importance weights. For LLMs, it uses discrete time-lagged updates. Critical distinction from RAPID: iw-SFT uses EMA for importance weighting (multiplicative loss scaling approximating on-policy gradients); RAPID uses EMA for reducible loss decomposition (R = max(0, L_θ − L_EMA)) with PER-style sampling priorities, providing noise robustness absent in importance weighting.\n\n**Domain-level data mixing:** DoReMi (NeurIPS 2023) uses excess loss with Group DRO for LLM domain mixing. Re-Mix (CoRL 2024) extends this to robot IL with domain-level weights over OXE datasets using a fixed reference. Both operate at domain level, not sample level.\n\n**Static demonstration curation:** SCIZOR (ICRA 2026) uses self-supervised progress prediction. CUPID (CoRL 2025) uses influence functions. RINSE (ICML 2025) uses smoothness metrics. DataMIL (ICLR 2026) uses datamodels. DemInf (RSS 2025) uses k-NN mutual information. All score data once before training — static preprocessing that cannot adapt to the policy's evolving learning needs.\n\n**SFT technique → RL quality (NEW — critical related work):** Off-Policy Token Clipped SFT (Tian-Shuo Liu et al., ICML 2026 poster) clips gradient updates from low-probability tokens during SFT, acting as a trust region that reduces forgetting (11.54%) and improves downstream RL (7.09%) on ALFWorld/ScienceWorld. PSFT (arXiv Aug 2025, 2508.17784) applies PPO-style clipped surrogates to SFT for generalization. DFT (ICLR 2026, 2508.05629) dynamically rescales SFT gradients based on token probability. Tailored Primitive Initialization (arXiv Nov 2025, 2511.12429) shows SFT demonstration diversity affects downstream RL reasoning. PRISM (arXiv Apr 2026, 2604.28123) inserts on-policy distillation between SFT and RL to repair distributional drift. All operate on *techniques* (gradient clipping, objective modification, distribution alignment) rather than *data quality* (which demonstrations to prioritize).\n\n**RL post-training for VLAs:** SimpleVLA-RL (ICLR 2026) achieves 99.1% on LIBERO via GRPO post-training. SFT accounts for 74pp of 82pp improvement; Section 6.2 ablates quantity (not quality). VLA-OPD (arXiv Mar 2026) bridges offline SFT and online RL via on-policy distillation. VLA-RFT uses a learned world model for RL.\n\n**Curricula effectiveness:** 'When Do Curricula Work?' (ICLR 2021 Oral) shows curriculum benefits are marginal on clean data — gains come only under limited budget or noisy data. Critical calibration for RAPID's claims.\n\n**EMA dynamics and memorization:** EMA models show improved robustness to noisy labels (arXiv 2411.18704) but are not independent of the training model. Self-distillation feedback loops can amplify errors (arXiv 2603.24472). Zhang et al. (ICLR 2017) and Kajitsuka & Sato (ICLR 2025) show high-capacity models can memorize noise, so noise suppression cannot assume persistently high loss on noisy samples.\n\n**The gap:** Multiple works study SFT *technique* for RL (gradient clipping, trust regions, objective rescaling, distribution alignment). iw-SFT uses EMA for importance weighting in continuous control. No existing work applies sample-level reducible-loss prioritized sampling to VLA SFT, and no work tests whether SFT data quality via noise-filtering prioritization affects downstream RL for VLAs.",
  "approach": "**Method overview.** RAPID (Reducible-loss Adaptive Prioritized Imitation from Demonstrations) replaces uniform sampling during VLA SFT with online, noise-robust prioritized sampling based on reducible loss. Beyond improving SFT in isolation, RAPID targets the SFT stage that initializes downstream RL — the paper's primary contribution is the empirical finding that SFT data quality cascades to RL outcomes.\n\n**Contribution 1: EMA-based reducible loss for VLA SFT.** RAPID computes reducible loss R(x) = max(0, L_θ(x) − L_EMA(x)), where L is action-prediction loss and θ_EMA ← τ·θ_EMA + (1−τ)·θ is updated every gradient step. *Honest positioning:* iw-SFT (2507.12856) proposed EMA for importance weighting in continuous control; RAPID uses EMA for a different purpose — reducible loss decomposition that provides noise-robust prioritization. The key mechanism is the max(0,·) clamp: noisy samples that the model cannot fit have L_θ ≈ L_EMA → R ≈ 0; noisy samples the model gradually memorizes have L_θ ≤ L_EMA → R = 0. Both regimes suppress noise. This decomposition cannot be replicated by raw-loss methods (DS2, SuRe) which assign high weight to noisy samples. Compared to LEAD's EMA over loss values, RAPID's EMA over model parameters captures richer structural information.\n\nSampling: transitions drawn proportionally to R(x)^α with importance-sampling correction β-annealed from 0→1 (Schaul et al. 2016). Priorities refreshed every K=500 steps (~8-12% compute overhead). Two-level sampling: trajectory priority = mean reducible loss (inter-demonstration), transition priority = per-step reducible loss (intra-demonstration).\n\n**Contribution 2: Training-horizon-aware τ calibration (theoretical support).** We analyze the bias-variance tradeoff in τ: tracking error scales as O(ε·τ/(1-τ)), signal quality scales similarly. The product is maximized at τ* = 1 − Θ(√ε). For VLA SFT (ε ≈ 5×10⁻⁴), τ* ≈ 0.978. Within the iw-SFT framework, the adaptive EMA reference achieves O(T) cumulative bound gap vs Ω(T²) for static references. *Testability caveat:* the constants in these bounds depend on loss landscape properties (Lipschitz constant, gradient bound) that are hard to estimate a priori. We frame the empirical bound-gap measurement as testing the theory's *qualitative* prediction (linear vs quadratic growth) rather than the *quantitative* crossover point T₀. The noise suppression guarantee is reformulated to handle high-capacity VLM memorization: relative suppression ratio O(1−τ) ≈ 0.022 for τ* = 0.978. Ablation over τ ∈ {0.97, 0.99, 0.995, 0.999, 0.9999} validates the theory and identifies failure modes at both extremes.\n\n**Contribution 3 (PRIMARY): RAPID+RL pipeline — SFT data quality → RL outcomes for VLAs.** The first empirical test of whether SFT data quality via noise-filtering prioritization affects downstream RL convergence for VLAs. *Differentiation from ICML 2026 clipping paper:* that work shows token-level gradient clipping during SFT improves downstream RL for LLMs on text-based agentic tasks; we show data-level noise filtering during SFT improves downstream RL for VLAs on robotic manipulation — complementary findings across domains and mechanisms. Protocol: (a) Vanilla SFT → GRPO (SimpleVLA-RL), (b) RAPID SFT → GRPO, on LIBERO-Long with 25% noise injection. Also test fixed-reference SFT → GRPO to validate that RAPID's *adaptive* filtering provides the RL benefit. Metrics: RL convergence speed (steps to 90% success), final success rate, total environment interactions. Even a modest improvement (e.g., 30-50% fewer RL steps) is practically significant given expensive RL environment interactions.\n\n**Experimental plan.** Built on OpenVLA-OFT (open-source).\n\n*Experiment 1 (Primary — Noise injection SFT):* Corrupt LIBERO-Long demonstrations at 10%, 25%, 50% with three corruption types: Gaussian action noise, random frame dropping, trajectory truncation. Pre-pilot to ensure baseline degrades to 60-80%. Baselines: uniform, raw-loss priority, DS2-adapted, fixed-reference reducible loss. *Limitation acknowledged:* synthetic corruption is a controlled test of the mechanism, not a claim about real-world robustness. Real-world noise (hesitation, suboptimal strategies, operator fatigue) is coherent and structurally different. The OXE experiment (Experiment 4) addresses this.\n\n*Experiment 2 (Primary — RAPID+RL pipeline):* 2-3 LIBERO-Long tasks with 25% noise. Four conditions: {Vanilla SFT, RAPID SFT, Fixed-reference SFT} × GRPO. RL stage uses SimpleVLA-RL (open-source, ~400 gradient steps, computationally cheap).\n\n*Experiment 3 (Sanity — Standard LIBERO-Long):* Clean data, expecting minimal gains per 'When Do Curricula Work?' analysis. Demonstrates RAPID does no harm.\n\n*Experiment 4 (AAAI — OXE mixed-quality):* Real-world heterogeneous quality, following SCIZOR/Re-Mix setup. Addresses the synthetic noise limitation.\n\n*Experiment 5 (AAAI — LIBERO-Plus robustness):* Tests whether noise filtering extracts more robust representations.\n\n**CoRL 2026 minimum viable plan (abstract May 26, paper May 29).** GO/NO-GO BY MAY 22: if first noise-injection + RL results are not available, fall back to AAAI 2027 only. CoRL scope: Experiments 1-3 (15 SFT runs + 4 RL runs ≈ 950 GPU-hours). Lead with RAPID+RL finding as headline. Risk: SimpleVLA-RL integration with RAPID checkpoints is untested.\n\n**AAAI 2027 (primary target, deadline ~Aug 2026).** Full version: all 5 experiments, complete ablation suite (τ, K, α, β), all baselines including CUPID and SCIZOR, comprehensive theory validation (qualitative bound gap growth, noise suppression ratios). This is the definitive version.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~3500h A100-80GB (noise injection: 3 types × 3 ratios × ~80h = ~720h + RAPID+RL: 6 RL runs × ~50h = 300h + LIBERO-Plus: ~200h eval + standard LIBERO-Long: 4 methods × 80h = 320h + OXE: ~400h + baselines ~600h + ablations ~500h + theory validation ~100h)",
      "gpu_utilization": "~25-35% effective utilization",
      "timeline": "10-14 weeks (full AAAI version); 14 days (CoRL sprint with go/no-go by May 22)",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$5,250 at ~$1.50/hr (full version); ~$1,425 for CoRL sprint (950h)"
    },
    "human_in_loop": {
      "gpu_hours": "~5000h A100-80GB",
      "gpu_utilization": "~60-70% utilization",
      "timeline": "6-8 weeks (full version); 10-12 days (CoRL sprint)",
      "team": "1 researcher, ~30-45min/day",
      "claude_api_cost": "$300-500",
      "estimated_gpu_cost": "~$7,500 (full); ~$2,000 (CoRL sprint)",
      "risk_note": "SimpleVLA-RL integration with RAPID SFT checkpoints is untested. May 22 go/no-go decision critical."
    },
    "auto_research": {
      "gpu_hours": "~6500-7500h A100-80GB",
      "gpu_utilization": "~90-95%",
      "timeline": "16-24 days with 8×A100",
      "team": "0 (initial setup and final review only)",
      "claude_api_cost": "$600-1000",
      "estimated_gpu_cost": "~$11,000",
      "speed_bottleneck": "GPU cluster availability; SimpleVLA-RL environment rollouts",
      "risk_note": "Agent may over-explore τ-K interaction space; ~15-20% wasted compute risk without human calibration"
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract May 26, paper May 29 — GO/NO-GO BY MAY 22: fall back to AAAI-only if first noise-injection + RL results unavailable; empirical focus with RAPID+RL headline, 15 SFT + 4 RL runs ≈ 950h)",
    "AAAI 2027 (deadline ~Aug 2026 — primary target for full version with all experiments, theory, OXE, LIBERO-Plus)",
    "ICRA 2027 (deadline ~Sep 2026 — fallback if CoRL infeasible, strong robot learning venue fit)",
    "ICLR 2027 (deadline ~Sep-Oct 2026 — only if finite-T theory validates empirically and RAPID+RL finding is compelling)"
  ],
  "level": "solid",
  "key_references": [
    "Prioritized Training on Points that are Learnable, Worth Learning, and Not Yet Learnt [RHO-LOSS] (ICML 2022)",
    "Prioritized Experience Replay (ICLR 2016)",
    "Prioritizing Samples in Reinforcement Learning with Reducible Loss [ReLo] (NeurIPS 2023)",
    "DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining (NeurIPS 2023)",
    "Not All Tokens Are What You Need [Rho-1] (NeurIPS 2024)",
    "Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning (CoRL 2024)",
    "Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining [DS2] (ICLR 2025)",
    "Supervised Fine Tuning on Curated Data is Reinforcement Learning [iw-SFT] (arXiv Jul 2025, 2507.12856)",
    "LEAD: Iterative Data Selection for Efficient LLM Instruction Tuning (arXiv May 2025)",
    "CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025)",
    "SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026)",
    "DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (ICLR 2026)",
    "RINSE: Learning from the Best — Smoothness-Driven Metrics for Data Quality in Imitation Learning (ICML 2025)",
    "DemInf: Robot Data Curation with Mutual Information Estimators (RSS 2025)",
    "When Do Curricula Work? (ICLR 2021)",
    "Off-Policy Token Clipped Supervised Fine-Tuning Yields a Robust Cold-Start (ICML 2026 poster)",
    "Proximal Supervised Fine-Tuning [PSFT] (arXiv Aug 2025, 2508.17784)",
    "On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification [DFT] (ICLR 2026, 2508.05629)",
    "Tailored Primitive Initialization is the Secret Key to Reinforcement Learning (arXiv Nov 2025, 2511.12429)",
    "PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning (arXiv Apr 2026, 2604.28123)",
    "OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024)",
    "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success [OpenVLA-OFT] (arXiv 2025)",
    "SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (ICLR 2026)",
    "What Can RL Bring to VLA Generalization? (NeurIPS 2025)",
    "VLA-OPD: Bridging Offline SFT and Online RL for VLAs via On-Policy Distillation (arXiv Mar 2026)",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026)",
    "Exponential Moving Average of Weights in Deep Learning: Dynamics and Benefits (arXiv Nov 2024)",
    "Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs? (arXiv Mar 2026)",
    "Understanding Deep Learning Requires Rethinking Generalization (Zhang et al., ICLR 2017)",
    "On the Optimal Memorization Capacity of Transformers (Kajitsuka & Sato, ICLR 2025)",
    "SuRe: Surprise-Driven Prioritised Replay for Continual LLM Learning (arXiv Nov 2025)",
    "Density-Ratio Weighted Behavioral Cloning (arXiv Oct 2025)",
    "Token Priority SFT (arXiv Feb 2026)",
    "UDS: Utility-Diversity Aware Online Batch Selection for LLM SFT (arXiv Oct 2025)"
  ],
  "description": "We propose RAPID (Reducible-loss Adaptive Prioritized Imitation from Demonstrations), which replaces uniform sampling during VLA supervised fine-tuning with online, noise-robust prioritized sampling based on reducible loss — and provides the first empirical test of whether SFT data quality cascades to downstream RL outcomes for VLAs.\n\nRAPID makes three contributions:\n\n(1) **EMA-based reducible loss for VLA SFT**: Computes R(x) = max(0, L_θ(x) − L_EMA(x)) to decompose loss into learnable and irreducible components. Honest positioning: iw-SFT (2507.12856) uses EMA for importance weighting in continuous control; RAPID uses EMA for reducible loss decomposition with PER-style sampling, providing noise robustness via the max(0,·) clamp that importance weighting lacks. Training-horizon-aware τ calibration (τ* = 1 − Θ(√ε) ≈ 0.978) connects EMA decay to learning rate, with finite-T bounds predicting O(T) vs Ω(T²) cumulative gap over static references — framed as a qualitative prediction validated empirically.\n\n(2) **Noise-robust SFT on mixed-quality demonstrations**: Controlled noise injection experiments (Gaussian action noise, frame dropping, trajectory truncation) on LIBERO-Long validate that reducible loss decomposition outperforms raw-loss methods and static curation on noisy data. Acknowledges synthetic corruption as a controlled mechanism test; OXE experiments (AAAI version) address real-world heterogeneity.\n\n(3) **RAPID+RL pipeline validation (primary contribution)**: The first empirical test of whether SFT data quality via noise-filtering prioritization affects downstream RL for VLAs. Differentiation from the ICML 2026 'Off-Policy Token Clipped SFT' paper: that work shows token-level gradient clipping during SFT improves RL for LLMs; we show data-level noise filtering during SFT improves RL for VLAs — complementary findings across domains and mechanisms. Tests RAPID SFT → SimpleVLA-RL GRPO vs vanilla SFT → GRPO, measuring RL convergence speed and sample efficiency.\n\nCoRL 2026 is a stretch goal (go/no-go by May 22); AAAI 2027 is the primary target with full experiments including LIBERO-Plus robustness and OXE mixed-quality.",
  "project_name": "adaptive_replay_vla",
  "source": "web_research",
  "change_type": "major"
}
```

## Summary of changes (major revision)

**What changed and why:**

1. **Contribution hierarchy restructured**: RAPID+RL pipeline finding elevated to THE primary contribution. The narrative is now "SFT data quality is an unexplored bottleneck in VLA RL pipelines; RAPID demonstrates this." This addresses the reviewer's point that the path to impact 3→4 is through a compelling pipeline result.

2. **ICML 2026 clipping paper cited and differentiated**: Added throughout (opportunity, landscape, approach, description). Clear differentiation: token-level gradient clipping for LLMs vs. data-level noise filtering for VLAs — complementary, not overlapping.

3. **iw-SFT repositioned honestly**: Acknowledged that iw-SFT already uses EMA for continuous control. RAPID's actual novelty is the *purpose* (reducible loss decomposition, not importance weighting), the *mechanism* (PER-style sampling, not multiplicative reweighting), and the *noise robustness* (max(0,·) clamp). No longer claims EMA reference as wholly novel.

4. **Five new SFT→RL references added**: Off-Policy Token Clipped SFT (ICML 2026), PSFT, DFT (ICLR 2026), Tailored Primitive, PRISM — all properly positioned as studying SFT *technique* for RL, while RAPID studies SFT *data quality* for RL.

5. **CoRL go/no-go**: Explicit decision point by May 22 added to approach, resource estimate, and target venues.

6. **Finite-T theory**: Reframed as qualitative prediction (linear vs quadratic growth pattern), acknowledging constants depend on hard-to-estimate landscape properties.

7. **Synthetic noise limitation**: Explicitly acknowledged in approach. Framed as controlled mechanism test, with OXE (AAAI scope) addressing real-world noise.

8. **Overall tightening**: Reduced repetitive caveats, stated things once clearly, cut hedge language. The proposal is noticeably tighter while covering more ground.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a05b3d26-0f69-489e-8dce-ebbcd0307001",
  "isSidechain": false,
  "requestId": "req_011CazVuChuBHNfHKpKBN2z9",
  "type": "assistant",
  "uuid": "ff951611-a327-4cab-b0e0-fdee296de804",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvWwRYkRoQxmWpDex6wuZ9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6765,
      "cache_read_input_tokens": 50854,
      "output_tokens": 8088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6765,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8088,
          "cache_read_input_tokens": 50854,
          "cache_creation_input_tokens": 6765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6765
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

_source line 66_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"RAPID: Reducible-Loss Adaptive Prioritized Replay for VLA Imitation Le…",
  "leafUuid": "ff951611-a327-4cab-b0e0-fdee296de804",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---

### Runtime record

_source line 67_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising RAPID: Addressing novelty gaps and clarifying SFT→RL contribution",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---

### Runtime record

_source line 68_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"RAPID: Reducible-Loss Adaptive Prioritized Replay for VLA Imitation Le…",
  "leafUuid": "ff951611-a327-4cab-b0e0-fdee296de804",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising RAPID: Addressing novelty gaps and clarifying SFT→RL contribution",
  "sessionId": "f453ff4a-d3dc-44e3-bb79-86652ba6dcdd"
}
```

---
