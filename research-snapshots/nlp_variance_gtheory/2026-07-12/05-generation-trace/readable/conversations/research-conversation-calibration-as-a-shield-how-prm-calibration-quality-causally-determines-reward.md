# Research conversation: Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Def

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/bed47c8a-6f94-4623-a6b5-5269f76a5abe.jsonl`
- **Structured JSON:** [`8fe6e4ada5fa7b7fcf6e.json`](../../sessions/8f/8fe6e4ada5fa7b7fcf6e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:51:19.325Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:51:19.325Z",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "content": "# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense\n\n## Description\nWe present the first causally rigorous study connecting PRM calibration quality to adversarial exploitability, and propose Calibration-Gated Step-Level Pessimism (CGSP), a novel defense that transforms calibrated uncertainty into adaptive reward hacking resistance during RL training. Our work bridges two mature but isolated research threads (PRM calibration and PRM hackability) through four contributions. First, an expanded correlation study across 48 configurations (8 PRMs × 6 calibration methods) provides sufficient statistical power (n=48, detecting r≥0.29 at p<0.05) to establish whether calibration quality predicts hackability metrics under gradient attacks, RL-induced hacking (GRPO on AIME), and BoN overoptimization (MATH-500), stratified by problem difficulty. Second, causal isolation experiments separate calibration's true effect from representation change artifacts: we compare post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) that provably preserve model representations against fine-tuning-based methods, with CKA verification and matched-representation-change controls. Third, step-level Hessian spectral analysis goes beyond Ackermann et al.'s outcome-level gradient norm analysis (which applies only to single-scalar reward models) to reveal how calibration affects the multi-reward compositional geometry of PRMs — analyzing how step-level flatness compounds across trajectories. Fourth, CGSP replaces raw PRM rewards during RL training with r̃_t = μ_t − α·σ_t/√c_t, where calibrated uncertainty σ_t and calibration quality c_t adaptively modulate pessimism per-step — trusted when calibration is tight, pessimistic when uncertainty is high — with a Calibration Drift Detector that monitors ECE on current-policy rollouts to flag distribution-shift-induced reward hacking in real time. CGSP differs from existing defenses (Caution uses prediction error, PET uses global pessimism, ensemble methods are uncalibrated) by being step-level, calibration-grounded, and adaptive. We evaluate CGSP against 5 baselines (uncalibrated GRPO, APRM, Caution, ensemble-min, gradient regularization) on MATH-500 and AIME, measuring both reward-accuracy alignment and downstream task accuracy.\n\n## Core Problem\nPRM calibration research and PRM hackability research are entirely separate threads with zero cross-citation — but the deeper problem is that we lack both (a) causal evidence for whether calibration actually determines hackability (vs. being merely correlated), and (b) a principled, step-level defense mechanism that leverages calibrated uncertainty to prevent reward hacking during RL training. Existing ad-hoc defenses (adversarial training, gradient regularization, pessimistic BoN) operate at the outcome level without exploiting the unique step-level structure of PRMs.\n\n## Opportunity\nThree recent developments create a uniquely favorable moment. First, Distributional PRMs (arXiv:2605.06785, May 2026) achieve calibrated step-level uncertainty via conditional optimal transport but never test robustness. Second, Tiwari et al. (arXiv:2603.06621, March 2026) demonstrate that PRMs are catastrophically hackable — near-perfect PRM rewards with <4% actual accuracy — but propose no calibration-based defense. Third, the causal isolation toolkit is mature: post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) modify only the output mapping without changing model representations, enabling controlled experiments that separate calibration effects from representation effects. No existing paper bridges these threads. Ackermann et al.'s gradient regularization work (arXiv:2602.18037) operates exclusively on outcome-level reward models with single-scalar rewards, never touching step-level PRM geometry. The CoT Entropy paper (arXiv:2502.11250) named this connection as future work 16 months ago with no follow-up. The window for a definitive, causally rigorous study is open but narrowing.\n\n## Landscape\nTwo parallel research threads have developed with zero cross-citation. Thread 1 (PRM Calibration): Park et al. (arXiv:2506.09338, NeurIPS 2025) demonstrate PRMs systematically overestimate success probabilities on hard problems, proposing quantile regression calibration. Distributional PRMs (arXiv:2605.06785, May 2026) use conditional optimal transport for calibrated monotone quantile functions, improving BoN on MATH-500 and AIME. Neither paper tests robustness. Thread 2 (PRM Hackability): Tiwari et al. (arXiv:2603.06621) show gradient attacks inflate PRM rewards 4× and RL achieves near-perfect PRM rewards with <4% accuracy, with 43% of reward gains from stylistic shortcuts. APRM (arXiv:2511.22888) uses adversarial training for +3.4pp robustness. Thread 3 (Adjacent but distinct): Ackermann et al. (arXiv:2602.18037) prove reward surface flatness correlates with accuracy retention for outcome-level RMs, but work exclusively with single-scalar rewards, analyze only gradient norms (no Hessian spectra), and never consider step-level reward models. Their theoretical framework (Propositions 3.3-3.4) assumes a single reward function R(s,a) over complete responses — inapplicable to step-level PRM geometry where T coupled reward surfaces {R_1,...,R_T} interact compositionally. InferenceTimePessimism (arXiv:2506.19248) and Caution (arXiv:2604.04648) apply pessimism for BoN but use uncalibrated uncertainty proxies (prediction error, hedging), not calibrated probabilities. URM (arXiv:2410.00847) decomposes uncertainty into aleatoric/epistemic for outcome-level RMs but not PRMs. Bayesian reward models (arXiv:2402.13210) use Laplace approximation on LoRA weights. Conformal prediction has been applied to RLHF feedback alignment (arXiv:2601.17329) but never to PRM defense. No paper establishes a causal link between calibration quality and hackability, and no paper proposes using calibrated step-level PRM uncertainty as a defense during RL training.\n\n## Approach\nThe study has four components: (A) Expanded Correlation Study, (B) Causal Isolation Experiments, (C) Step-Level Mechanistic Analysis, and (D) Calibration-Gated Step-Level Pessimism (CGSP) defense.\n\n**Component A — Expanded Correlation Study (n≥24 configurations):** Apply 6 calibration methods across 2 tiers to 8 open-source PRMs. Tier 1 (post-hoc, representation-preserving): temperature scaling, Platt scaling, isotonic regression. Tier 2 (model-modifying): quantile regression fine-tuning, conditional optimal transport, Venn-Abers predictors. The 8 PRMs span discriminative (Qwen2.5-Math-PRM-7B, Qwen2.5-Math-PRM-72B, Skywork-o1-Open-PRM-7B, RLHFlow-Llama3.1-8B-PRM, Math-Shepherd-7B, OpenR-Math-psa-7B), generative (GenPRM-7B), and implicit (EurusPRM-Stage2) architectures. Each of the 48 PRM×calibration configurations is subjected to three attack tiers: (i) gradient-based reward inflation following Tiwari et al., (ii) RL-induced reward hacking via GRPO on AIME, and (iii) BoN overoptimization at N∈{1,4,16,64,256} on MATH-500. Compute rank correlations (Spearman ρ, Kendall τ) between calibration metrics (ECE, Brier score, quantile coverage, reliability diagram sharpness) and hackability metrics (reward-accuracy divergence, attack success rate, BoN degradation onset N*). Stratify analysis by problem difficulty (MATH levels 1-5, AMC vs. AIME) to test whether calibration is more protective on hard problems where PRMs are known to be overconfident.\n\n**Component B — Causal Isolation Experiments:** This is the methodological core addressing the reviewer's causation concern. Design: (B1) Post-hoc calibration control: Apply temperature scaling, Platt scaling, and isotonic regression — which provably modify only the output mapping, not internal representations — and measure hackability change. If hackability decreases under post-hoc calibration alone, this establishes that calibration per se (not representation change) causally affects hackability. (B2) Representation change verification: For fine-tuning-based calibration methods (quantile regression, COT), measure representation change at every transformer layer using Centered Kernel Alignment (CKA) between the base PRM and calibrated PRM. (B3) Matched representation change control: Fine-tune PRMs on an auxiliary task (e.g., next-token prediction on math text) that produces CKA-matched representation changes but does NOT improve calibration. If only calibration-improving fine-tuning reduces hackability (not the CKA-matched control), the causal role of calibration is confirmed. (B4) Conformal prediction as the cleanest test: Apply split-conformal prediction to PRM step scores, providing distribution-free coverage guarantees with zero model modification. Test whether conformal-calibrated PRMs resist hacking better than uncalibrated ones.\n\n**Component C — Step-Level Mechanistic Analysis (differentiating from Ackermann et al.):** Unlike Ackermann et al., who analyze only outcome-level gradient norms and max-perturbation sharpness, we perform Hessian spectral analysis at the step level — computing top-k eigenvalues and spectral density of the step-level reward Hessian ∂²R_t/∂h² (where h is the hidden representation at step t). Key questions: (i) Do calibrated PRMs have flatter step-level reward surfaces (lower top Hessian eigenvalue)? (ii) Does flatness vary by step position (early reasoning steps vs. final answer steps)? (iii) Do hackable reward peaks correspond to isolated large Hessian eigenvalues (sharp directions) that gradient attacks exploit? This extends Ackermann et al.'s framework from single-reward geometry to multi-reward compositional geometry: we analyze how step-level flatness/sharpness compounds across a T-step trajectory to determine outcome-level hackability.\n\n**Component D — Calibration-Gated Step-Level Pessimism (CGSP) Defense:** This transforms the paper from measurement to method. CGSP operates during RL training (GRPO/PPO) by replacing raw PRM step rewards with calibration-modulated rewards: r̃_t = μ_t − α · σ_t / √(c_t), where μ_t is the calibrated step reward mean, σ_t is the calibrated uncertainty (from quantile width or conformal interval), c_t is a calibration quality score (inverse ECE computed on a rolling buffer), and α is a pessimism strength hyperparameter. When calibration is high (small σ_t, high c_t), the reward is trusted; when calibration is low (large σ_t, low c_t), pessimism dominates. This differs from existing pessimism (Caution uses prediction error, PET uses global pessimistic fine-tuning, InferenceTimePessimism uses hedging) because CGSP is (i) step-level, (ii) grounded in calibrated probabilities rather than heuristic proxies, and (iii) adaptive — the pessimism automatically strengthens in distribution-shift regions where the PRM becomes miscalibrated. Additionally, we implement a Calibration Drift Detector: during RL training, periodically measure ECE on current-policy rollouts vs. the initial SFT-distribution calibration. When drift exceeds a threshold, flag those trajectory types as potentially hacked and apply reward clipping. This converts calibration from a static property into a dynamic training signal.\n\nBaseline comparisons for CGSP: (i) uncalibrated PRM + GRPO, (ii) APRM adversarial training, (iii) Caution/prediction-error pessimism, (iv) ensemble minimum (following Coste et al.), (v) KL-regularized GRPO, (vi) gradient regularization (Ackermann et al.).\n\nCodebase starting points: young-j-park/prm-calibration for calibration fitting, Tiwari et al.'s PRM-BiasBench for adversarial evaluation, vwxyzjn/open_instruct for GRPO training infrastructure.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '4200 H100-hrs (calibration fitting: 200, rollout generation: 600, gradient attacks: 1000, GRPO RL training: 1600 [including CGSP defense training], BoN evaluation: 400, Hessian spectral analysis: 200, causal isolation controls: 200)', 'timeline': '12-14 weeks', 'estimated_gpu_cost': '$10,500 at ~$2.50/H100-hr'}, 'human_in_loop': {'gpu_hours': '3600 H100-hrs (fewer failed iterations with AI-assisted debugging)', 'timeline': '10-12 weeks', 'claude_api_cost': '$400-700 (code generation, experiment analysis, paper drafting)', 'estimated_gpu_cost': '$9,000 at ~$2.50/H100-hr'}, 'auto_research': {'gpu_hours': '5200 H100-hrs (broader sweeps over α pessimism parameter, calibration drift thresholds, and ablations across all 48 configurations)', 'timeline': '7-9 weeks', 'claude_api_cost': '$1,500-2,000 (automated experiment orchestration, iterative analysis, full draft writing)', 'estimated_gpu_cost': '$13,000 at ~$2.50/H100-hr', 'speed_bottleneck': 'GRPO RL training wall-clock time (~18hrs per PRM×calibration×defense configuration on 4×H100); Hessian spectral analysis requires Lanczos iterations per step per problem; 72B PRM requires 4×H100 for inference'}}\n\n## Inspired By\nField guide gap: PRM overconfidence on OOD problems (Section 5.3 'when more compute hurts'); Untried combination: distributional PRM calibration + PRM hackability analysis; Pattern: connecting two mature but isolated research threads; Reviewer insight: pure measurement is insufficient — the key contribution should be a causal mechanism and a defense method; Methodological insight: post-hoc calibration methods that preserve representations enable clean causal isolation experiments impossible with fine-tuning-based calibration alone\n\n## Target Venues\n- ICLR 2027 (abstract Sep 19, paper Sep 24, 2026)\n- AAAI 2027 (abstract Jul 21, paper Jul 28, 2026)\n- AISTATS 2027 (paper Oct 10, 2026)\n\n## Key References\n- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (arXiv:2506.09338, NeurIPS 2025)\n- Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport (arXiv:2605.06785, May 2026)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv:2603.06621, March 2026)\n- Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards (arXiv:2602.18037, Feb 2026)\n- Adversarial Training for Process Reward Models (arXiv:2511.22888, Nov 2025)\n- From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism (arXiv:2604.04648, April 2026)\n- Inference-Time Reward Hacking in Large Language Models (arXiv:2506.19248, NeurIPS 2025 Spotlight)\n- Uncertainty-Aware Step-wise Verification with Generative Reward Models (arXiv:2502.11250, ICLR 2025 Workshop)\n- Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242, April 2026)\n- Uncertainty-Aware Reward Model (arXiv:2410.00847)\n- Helping or Herding? Reward Model Ensembles Mitigate but Do Not Eliminate Overoptimization (arXiv:2312.09244)\n- Bayesian Reward Models for LLM Alignment (arXiv:2402.13210)\n- Conformal Feedback Alignment for RLHF (arXiv:2601.17329)\n- Taming Overconfidence in LLMs: Reward Calibration in RLHF (arXiv:2410.09724)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (arXiv:2501.03124)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T05:51:19.329Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:51:19.329Z",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe"
}
```

---

## Round 1

47 recorded events

### User

_source line 3 · 2026-05-20T05:51:19.431Z_

# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense

## Description
We present the first causally rigorous study connecting PRM calibration quality to adversarial exploitability, and propose Calibration-Gated Step-Level Pessimism (CGSP), a novel defense that transforms calibrated uncertainty into adaptive reward hacking resistance during RL training. Our work bridges two mature but isolated research threads (PRM calibration and PRM hackability) through four contributions. First, an expanded correlation study across 48 configurations (8 PRMs × 6 calibration methods) provides sufficient statistical power (n=48, detecting r≥0.29 at p<0.05) to establish whether calibration quality predicts hackability metrics under gradient attacks, RL-induced hacking (GRPO on AIME), and BoN overoptimization (MATH-500), stratified by problem difficulty. Second, causal isolation experiments separate calibration's true effect from representation change artifacts: we compare post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) that provably preserve model representations against fine-tuning-based methods, with CKA verification and matched-representation-change controls. Third, step-level Hessian spectral analysis goes beyond Ackermann et al.'s outcome-level gradient norm analysis (which applies only to single-scalar reward models) to reveal how calibration affects the multi-reward compositional geometry of PRMs — analyzing how step-level flatness compounds across trajectories. Fourth, CGSP replaces raw PRM rewards during RL training with r̃_t = μ_t − α·σ_t/√c_t, where calibrated uncertainty σ_t and calibration quality c_t adaptively modulate pessimism per-step — trusted when calibration is tight, pessimistic when uncertainty is high — with a Calibration Drift Detector that monitors ECE on current-policy rollouts to flag distribution-shift-induced reward hacking in real time. CGSP differs from existing defenses (Caution uses prediction error, PET uses global pessimism, ensemble methods are uncalibrated) by being step-level, calibration-grounded, and adaptive. We evaluate CGSP against 5 baselines (uncalibrated GRPO, APRM, Caution, ensemble-min, gradient regularization) on MATH-500 and AIME, measuring both reward-accuracy alignment and downstream task accuracy.

## Core Problem
PRM calibration research and PRM hackability research are entirely separate threads with zero cross-citation — but the deeper problem is that we lack both (a) causal evidence for whether calibration actually determines hackability (vs. being merely correlated), and (b) a principled, step-level defense mechanism that leverages calibrated uncertainty to prevent reward hacking during RL training. Existing ad-hoc defenses (adversarial training, gradient regularization, pessimistic BoN) operate at the outcome level without exploiting the unique step-level structure of PRMs.

## Opportunity
Three recent developments create a uniquely favorable moment. First, Distributional PRMs (arXiv:2605.06785, May 2026) achieve calibrated step-level uncertainty via conditional optimal transport but never test robustness. Second, Tiwari et al. (arXiv:2603.06621, March 2026) demonstrate that PRMs are catastrophically hackable — near-perfect PRM rewards with <4% actual accuracy — but propose no calibration-based defense. Third, the causal isolation toolkit is mature: post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) modify only the output mapping without changing model representations, enabling controlled experiments that separate calibration effects from representation effects. No existing paper bridges these threads. Ackermann et al.'s gradient regularization work (arXiv:2602.18037) operates exclusively on outcome-level reward models with single-scalar rewards, never touching step-level PRM geometry. The CoT Entropy paper (arXiv:2502.11250) named this connection as future work 16 months ago with no follow-up. The window for a definitive, causally rigorous study is open but narrowing.

## Landscape
Two parallel research threads have developed with zero cross-citation. Thread 1 (PRM Calibration): Park et al. (arXiv:2506.09338, NeurIPS 2025) demonstrate PRMs systematically overestimate success probabilities on hard problems, proposing quantile regression calibration. Distributional PRMs (arXiv:2605.06785, May 2026) use conditional optimal transport for calibrated monotone quantile functions, improving BoN on MATH-500 and AIME. Neither paper tests robustness. Thread 2 (PRM Hackability): Tiwari et al. (arXiv:2603.06621) show gradient attacks inflate PRM rewards 4× and RL achieves near-perfect PRM rewards with <4% accuracy, with 43% of reward gains from stylistic shortcuts. APRM (arXiv:2511.22888) uses adversarial training for +3.4pp robustness. Thread 3 (Adjacent but distinct): Ackermann et al. (arXiv:2602.18037) prove reward surface flatness correlates with accuracy retention for outcome-level RMs, but work exclusively with single-scalar rewards, analyze only gradient norms (no Hessian spectra), and never consider step-level reward models. Their theoretical framework (Propositions 3.3-3.4) assumes a single reward function R(s,a) over complete responses — inapplicable to step-level PRM geometry where T coupled reward surfaces {R_1,...,R_T} interact compositionally. InferenceTimePessimism (arXiv:2506.19248) and Caution (arXiv:2604.04648) apply pessimism for BoN but use uncalibrated uncertainty proxies (prediction error, hedging), not calibrated probabilities. URM (arXiv:2410.00847) decomposes uncertainty into aleatoric/epistemic for outcome-level RMs but not PRMs. Bayesian reward models (arXiv:2402.13210) use Laplace approximation on LoRA weights. Conformal prediction has been applied to RLHF feedback alignment (arXiv:2601.17329) but never to PRM defense. No paper establishes a causal link between calibration quality and hackability, and no paper proposes using calibrated step-level PRM uncertainty as a defense during RL training.

## Approach
The study has four components: (A) Expanded Correlation Study, (B) Causal Isolation Experiments, (C) Step-Level Mechanistic Analysis, and (D) Calibration-Gated Step-Level Pessimism (CGSP) defense.

**Component A — Expanded Correlation Study (n≥24 configurations):** Apply 6 calibration methods across 2 tiers to 8 open-source PRMs. Tier 1 (post-hoc, representation-preserving): temperature scaling, Platt scaling, isotonic regression. Tier 2 (model-modifying): quantile regression fine-tuning, conditional optimal transport, Venn-Abers predictors. The 8 PRMs span discriminative (Qwen2.5-Math-PRM-7B, Qwen2.5-Math-PRM-72B, Skywork-o1-Open-PRM-7B, RLHFlow-Llama3.1-8B-PRM, Math-Shepherd-7B, OpenR-Math-psa-7B), generative (GenPRM-7B), and implicit (EurusPRM-Stage2) architectures. Each of the 48 PRM×calibration configurations is subjected to three attack tiers: (i) gradient-based reward inflation following Tiwari et al., (ii) RL-induced reward hacking via GRPO on AIME, and (iii) BoN overoptimization at N∈{1,4,16,64,256} on MATH-500. Compute rank correlations (Spearman ρ, Kendall τ) between calibration metrics (ECE, Brier score, quantile coverage, reliability diagram sharpness) and hackability metrics (reward-accuracy divergence, attack success rate, BoN degradation onset N*). Stratify analysis by problem difficulty (MATH levels 1-5, AMC vs. AIME) to test whether calibration is more protective on hard problems where PRMs are known to be overconfident.

**Component B — Causal Isolation Experiments:** This is the methodological core addressing the reviewer's causation concern. Design: (B1) Post-hoc calibration control: Apply temperature scaling, Platt scaling, and isotonic regression — which provably modify only the output mapping, not internal representations — and measure hackability change. If hackability decreases under post-hoc calibration alone, this establishes that calibration per se (not representation change) causally affects hackability. (B2) Representation change verification: For fine-tuning-based calibration methods (quantile regression, COT), measure representation change at every transformer layer using Centered Kernel Alignment (CKA) between the base PRM and calibrated PRM. (B3) Matched representation change control: Fine-tune PRMs on an auxiliary task (e.g., next-token prediction on math text) that produces CKA-matched representation changes but does NOT improve calibration. If only calibration-improving fine-tuning reduces hackability (not the CKA-matched control), the causal role of calibration is confirmed. (B4) Conformal prediction as the cleanest test: Apply split-conformal prediction to PRM step scores, providing distribution-free coverage guarantees with zero model modification. Test whether conformal-calibrated PRMs resist hacking better than uncalibrated ones.

**Component C — Step-Level Mechanistic Analysis (differentiating from Ackermann et al.):** Unlike Ackermann et al., who analyze only outcome-level gradient norms and max-perturbation sharpness, we perform Hessian spectral analysis at the step level — computing top-k eigenvalues and spectral density of the step-level reward Hessian ∂²R_t/∂h² (where h is the hidden representation at step t). Key questions: (i) Do calibrated PRMs have flatter step-level reward surfaces (lower top Hessian eigenvalue)? (ii) Does flatness vary by step position (early reasoning steps vs. final answer steps)? (iii) Do hackable reward peaks correspond to isolated large Hessian eigenvalues (sharp directions) that gradient attacks exploit? This extends Ackermann et al.'s framework from single-reward geometry to multi-reward compositional geometry: we analyze how step-level flatness/sharpness compounds across a T-step trajectory to determine outcome-level hackability.

**Component D — Calibration-Gated Step-Level Pessimism (CGSP) Defense:** This transforms the paper from measurement to method. CGSP operates during RL training (GRPO/PPO) by replacing raw PRM step rewards with calibration-modulated rewards: r̃_t = μ_t − α · σ_t / √(c_t), where μ_t is the calibrated step reward mean, σ_t is the calibrated uncertainty (from quantile width or conformal interval), c_t is a calibration quality score (inverse ECE computed on a rolling buffer), and α is a pessimism strength hyperparameter. When calibration is high (small σ_t, high c_t), the reward is trusted; when calibration is low (large σ_t, low c_t), pessimism dominates. This differs from existing pessimism (Caution uses prediction error, PET uses global pessimistic fine-tuning, InferenceTimePessimism uses hedging) because CGSP is (i) step-level, (ii) grounded in calibrated probabilities rather than heuristic proxies, and (iii) adaptive — the pessimism automatically strengthens in distribution-shift regions where the PRM becomes miscalibrated. Additionally, we implement a Calibration Drift Detector: during RL training, periodically measure ECE on current-policy rollouts vs. the initial SFT-distribution calibration. When drift exceeds a threshold, flag those trajectory types as potentially hacked and apply reward clipping. This converts calibration from a static property into a dynamic training signal.

Baseline comparisons for CGSP: (i) uncalibrated PRM + GRPO, (ii) APRM adversarial training, (iii) Caution/prediction-error pessimism, (iv) ensemble minimum (following Coste et al.), (v) KL-regularized GRPO, (vi) gradient regularization (Ackermann et al.).

Codebase starting points: young-j-park/prm-calibration for calibration fitting, Tiwari et al.'s PRM-BiasBench for adversarial evaluation, vwxyzjn/open_instruct for GRPO training infrastructure.

## Resource Estimate
{'manual': {'gpu_hours': '4200 H100-hrs (calibration fitting: 200, rollout generation: 600, gradient attacks: 1000, GRPO RL training: 1600 [including CGSP defense training], BoN evaluation: 400, Hessian spectral analysis: 200, causal isolation controls: 200)', 'timeline': '12-14 weeks', 'estimated_gpu_cost': '$10,500 at ~$2.50/H100-hr'}, 'human_in_loop': {'gpu_hours': '3600 H100-hrs (fewer failed iterations with AI-assisted debugging)', 'timeline': '10-12 weeks', 'claude_api_cost': '$400-700 (code generation, experiment analysis, paper drafting)', 'estimated_gpu_cost': '$9,000 at ~$2.50/H100-hr'}, 'auto_research': {'gpu_hours': '5200 H100-hrs (broader sweeps over α pessimism parameter, calibration drift thresholds, and ablations across all 48 configurations)', 'timeline': '7-9 weeks', 'claude_api_cost': '$1,500-2,000 (automated experiment orchestration, iterative analysis, full draft writing)', 'estimated_gpu_cost': '$13,000 at ~$2.50/H100-hr', 'speed_bottleneck': 'GRPO RL training wall-clock time (~18hrs per PRM×calibration×defense configuration on 4×H100); Hessian spectral analysis requires Lanczos iterations per step per problem; 72B PRM requires 4×H100 for inference'}}

## Inspired By
Field guide gap: PRM overconfidence on OOD problems (Section 5.3 'when more compute hurts'); Untried combination: distributional PRM calibration + PRM hackability analysis; Pattern: connecting two mature but isolated research threads; Reviewer insight: pure measurement is insufficient — the key contribution should be a causal mechanism and a defense method; Methodological insight: post-hoc calibration methods that preserve representations enable clean causal isolation experiments impossible with fine-tuning-based calibration alone

## Target Venues
- ICLR 2027 (abstract Sep 19, paper Sep 24, 2026)
- AAAI 2027 (abstract Jul 21, paper Jul 28, 2026)
- AISTATS 2027 (paper Oct 10, 2026)

## Key References
- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (arXiv:2506.09338, NeurIPS 2025)
- Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport (arXiv:2605.06785, May 2026)
- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv:2603.06621, March 2026)
- Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards (arXiv:2602.18037, Feb 2026)
- Adversarial Training for Process Reward Models (arXiv:2511.22888, Nov 2025)
- From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism (arXiv:2604.04648, April 2026)
- Inference-Time Reward Hacking in Large Language Models (arXiv:2506.19248, NeurIPS 2025 Spotlight)
- Uncertainty-Aware Step-wise Verification with Generative Reward Models (arXiv:2502.11250, ICLR 2025 Workshop)
- Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242, April 2026)
- Uncertainty-Aware Reward Model (arXiv:2410.00847)
- Helping or Herding? Reward Model Ensembles Mitigate but Do Not Eliminate Overoptimization (arXiv:2312.09244)
- Bayesian Reward Models for LLM Alignment (arXiv:2402.13210)
- Conformal Feedback Alignment for RLHF (arXiv:2601.17329)
- Taming Overconfidence in LLMs: Reward Calibration in RLHF (arXiv:2410.09724)
- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (arXiv:2501.03124)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "18034a7d-47e3-4c01-b7f9-6c61bf20f18e",
  "type": "user",
  "uuid": "eb4b9029-72cf-4011-8a3b-fb350241b8fe",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:51:19.427Z_

```json
{
  "parentUuid": "eb4b9029-72cf-4011-8a3b-fb350241b8fe",
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
  "uuid": "d125a61e-392c-44e7-89f1-e11473c41da0",
  "timestamp": "2026-05-20T05:51:19.427Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:51:19.427Z_

```json
{
  "parentUuid": "d125a61e-392c-44e7-89f1-e11473c41da0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b4d127c9-2022-4544-86cd-41778ee942e0",
  "timestamp": "2026-05-20T05:51:19.427Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
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
  "lastPrompt": "# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense  ## Description We present the first causally rigorous study connecting P…",
  "leafUuid": "b4d127c9-2022-4544-86cd-41778ee942e0",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Calibration quality and PRM reward hacking resistance",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:51:23.660Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal carefully. It's about connecting PRM (Process Reward Model) calibration quality to reward hacking resistance, and proposing a defense mechanism called CGSP. Let me first do thorough literature research to understand the current landscape before making any judgments.

Let me search for the key papers and recent developments in this area.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4d127c9-2022-4544-86cd-41778ee942e0",
  "isSidechain": false,
  "requestId": "req_011CbDJHHqz3zBh3dRAm3nWp",
  "type": "assistant",
  "uuid": "edcd39b0-dccb-4d2d-9d7e-75b3b1ec19ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMYJm4Hir2CiTWSHdthsJ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5589,
      "cache_read_input_tokens": 14549,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5589,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 195,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 5589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5589
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

_source line 9 · 2026-05-20T05:51:24.223Z_

I need to do thorough literature research before making any assessments. Let me start by searching for the key papers and recent developments in this area.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edcd39b0-dccb-4d2d-9d7e-75b3b1ec19ad",
  "isSidechain": false,
  "requestId": "req_011CbDJHHqz3zBh3dRAm3nWp",
  "type": "assistant",
  "uuid": "c27cc859-6dd7-4725-abe0-4bed6e9418e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMYJm4Hir2CiTWSHdthsJ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5589,
      "cache_read_input_tokens": 14549,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5589,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 195,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 5589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5589
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

_source line 10 · 2026-05-20T05:51:24.564Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TPQeeKAM2rb1jKCpjg3AWJ`</summary>

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
  "parentUuid": "c27cc859-6dd7-4725-abe0-4bed6e9418e4",
  "isSidechain": false,
  "requestId": "req_011CbDJHHqz3zBh3dRAm3nWp",
  "type": "assistant",
  "uuid": "70398a77-9bd6-405f-9182-ee1ffdb24ddf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMYJm4Hir2CiTWSHdthsJ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5589,
      "cache_read_input_tokens": 14549,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5589,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 195,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 5589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5589
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

_source line 11 · 2026-05-20T05:51:24.571Z_

<details><summary>↩ Tool result · `toolu_01TPQeeKAM2rb1jKCpjg3AWJ`</summary>

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
  "parentUuid": "70398a77-9bd6-405f-9182-ee1ffdb24ddf",
  "isSidechain": false,
  "promptId": "18034a7d-47e3-4c01-b7f9-6c61bf20f18e",
  "type": "user",
  "uuid": "10c523c5-614d-4d1d-8ce1-ef41efda5475",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "70398a77-9bd6-405f-9182-ee1ffdb24ddf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T05:51:27.458Z_

Now let me conduct my pre-assessment literature research. I'll run multiple searches in parallel to cover the key threads.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10c523c5-614d-4d1d-8ce1-ef41efda5475",
  "isSidechain": false,
  "requestId": "req_011CbDJHfs4CKXqpJEdVYTgq",
  "type": "assistant",
  "uuid": "5174b157-b544-4e75-9333-16d8496deccd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTm88BA4tjggGoXpvgVcG8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 722,
      "cache_read_input_tokens": 20138,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 20138,
          "cache_creation_input_tokens": 722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 722
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

_source line 13 · 2026-05-20T05:51:27.850Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012mZZhKNa3Cesvv5QH2tKu2`</summary>

```json
{
  "query": "PRM calibration process reward model calibration 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5174b157-b544-4e75-9333-16d8496deccd",
  "isSidechain": false,
  "requestId": "req_011CbDJHfs4CKXqpJEdVYTgq",
  "type": "assistant",
  "uuid": "e65c3172-70af-4530-984a-728e963f4510",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HTm88BA4tjggGoXpvgVcG8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 722,
      "cache_read_input_tokens": 20138,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 20138,
          "cache_creation_input_tokens": 722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 722
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

_source line 14 · 2026-05-20T05:51:36.873Z_

<details><summary>↩ Tool result · `toolu_012mZZhKNa3Cesvv5QH2tKu2`</summary>

```text
Web search results for query: "PRM calibration process reward model calibration 2025 2026"

Links: [{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models | OpenReview","url":"https://openreview.net/forum?id=hzMkfIrdDT"},{"title":"[2506.09338] Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/abs/2506.09338"},{"title":"NeurIPS Poster Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://neurips.cc/virtual/2025/poster/116598"},{"title":"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/html/2605.06785"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models for NeurIPS 2025 - IBM Research","url":"https://research.ibm.com/publications/know-what-you-dont-know-uncertainty-calibration-of-process-reward-models"},{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/pdf/2506.09338"},{"title":"Process Reward Models (PRMs): Calibration & Scaling","url":"https://www.emergentmind.com/topics/process-reward-models-prms"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+(PRMs)"}]

Based on the search results, here's what I found about PRM calibration:

## Key Findings on PRM Calibration (2025-2026)

Process reward models (PRMs) play a central role in guiding inference-time scaling algorithms for large language models (LLMs), but even state-of-the-art PRMs can be poorly calibrated. Specifically, they tend to overestimate the success probability that a partial reasoning step will lead to a correct final answer, particularly when smaller LLMs are used to complete the reasoning trajectory.

### Calibration Approach

The solution is a calibration approach—performed via quantile regression—that adjusts PRM outputs to better align with true success probabilities. This leverages calibrated success estimates and their associated confidence bounds to introduce an instance-adaptive scaling (IAS) framework that dynamically adjusts the compute budget based on the estimated likelihood that a partial reasoning trajectory will yield a correct final answer.

### Recent Results

Experiments on mathematical reasoning benchmarks show that the PRM calibration method achieves small calibration error, outperforming baseline methods, calibration is crucial for enabling effective instance-adaptive scaling, and the proposed IAS strategy reduces inference costs while maintaining final answer accuracy, utilizing less compute on more confident problems as desired.

Recent research in this area has been published at NeurIPS 2025, with papers being finalized in late 2025 and into 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e65c3172-70af-4530-984a-728e963f4510",
  "isSidechain": false,
  "promptId": "18034a7d-47e3-4c01-b7f9-6c61bf20f18e",
  "type": "user",
  "uuid": "dc3e08fb-f339-4662-9aa2-706e79f35fcd",
  "toolUseResult": {
    "query": "PRM calibration process reward model calibration 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011reJLBU4X7esF1r6U1xCdT",
        "content": [
          {
            "title": "Know What You Don't Know: Uncertainty Calibration of Process Reward Models | OpenReview",
            "url": "https://openreview.net/forum?id=hzMkfIrdDT"
          },
          {
            "title": "[2506.09338] Know What You Don't Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://arxiv.org/abs/2506.09338"
          },
          {
            "title": "NeurIPS Poster Know What You Don't Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://neurips.cc/virtual/2025/poster/116598"
          },
          {
            "title": "Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport",
            "url": "https://arxiv.org/html/2605.06785"
          },
          {
            "title": "Know What You Don’t Know: Uncertainty Calibration of Process Reward Models for NeurIPS 2025 - IBM Research",
            "url": "https://research.ibm.com/publications/know-what-you-dont-know-uncertainty-calibration-of-process-reward-models"
          },
          {
            "title": "Know What You Don't Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://arxiv.org/pdf/2506.09338"
          },
          {
            "title": "Process Reward Models (PRMs): Calibration & Scaling",
            "url": "https://www.emergentmind.com/topics/process-reward-models-prms"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Process+Reward+Models+(PRMs)"
          }
        ]
      },
      "Based on the search results, here's what I found about PRM calibration:\n\n## Key Findings on PRM Calibration (2025-2026)\n\nProcess reward models (PRMs) play a central role in guiding inference-time scaling algorithms for large language models (LLMs), but even state-of-the-art PRMs can be poorly calibrated. Specifically, they tend to overestimate the success probability that a partial reasoning step will lead to a correct final answer, particularly when smaller LLMs are used to complete the reasoning trajectory.\n\n### Calibration Approach\n\nThe solution is a calibration approach—performed via quantile regression—that adjusts PRM outputs to better align with true success probabilities. This leverages calibrated success estimates and their associated confidence bounds to introduce an instance-adaptive scaling (IAS) framework that dynamically adjusts the compute budget based on the estimated likelihood that a partial reasoning trajectory will yield a correct final answer.\n\n### Recent Results\n\nExperiments on mathematical reasoning benchmarks show that the PRM calibration method achieves small calibration error, outperforming baseline methods, calibration is crucial for enabling effective instance-adaptive scaling, and the proposed IAS strategy reduces inference costs while maintaining final answer accuracy, utilizing less compute on more confident problems as desired.\n\nRecent research in this area has been published at NeurIPS 2025, with papers being finalized in late 2025 and into 2026."
    ],
    "durationSeconds": 9.015585298999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e65c3172-70af-4530-984a-728e963f4510",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T05:51:39.319Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019dHY8sRNubWzkM9eQgMR6e`</summary>

```json
{
  "query": "process reward model hackability adversarial attack reward hacking PRM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc3e08fb-f339-4662-9aa2-706e79f35fcd",
  "isSidechain": false,
  "requestId": "req_011CbDJJaGjTns4thGqJR8z8",
  "type": "assistant",
  "uuid": "cb68ef0a-68ff-4ed1-a06e-ce01235ef46d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXF8c3cVLF2P2giRbUM27F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 837,
      "cache_read_input_tokens": 20860,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 837,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 20860,
          "cache_creation_input_tokens": 837,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 837
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

_source line 16 · 2026-05-20T05:51:46.839Z_

<details><summary>↩ Tool result · `toolu_019dHY8sRNubWzkM9eQgMR6e`</summary>

```text
Web search results for query: "process reward model hackability adversarial attack reward hacking PRM 2025 2026"

Links: [{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"Adversarial Reward-Hacking","url":"https://www.emergentmind.com/topics/adversarial-reward-hacking"},{"title":"Adversarial Training of Reward Models","url":"https://arxiv.org/pdf/2504.06141"},{"title":"Beyond Semantic Manipulation: Token-Space Attacks on Reward Models","url":"https://arxiv.org/pdf/2604.02686"},{"title":"1 Introduction","url":"https://arxiv.org/html/2603.06621"},{"title":"Adversarial Reward Auditing for Active Detection and ...","url":"https://arxiv.org/pdf/2602.01750"}]

Based on the search results, here's what I found about process reward model hackability and adversarial attacks:

## Key Recent Research (2025-2026)

Adversarial optimization demonstrates that gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks. A particularly significant finding is that policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.

Current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.

## Types of Attacks and Vulnerabilities

Static perturbation analysis uncovers a fluency-logic dissociation: high invariance to surface-level style changes with reward changes <0.1, yet inconsistent detection of logically-corrupted reasoning.

Reward hacking arises both from adversarial attacks—malicious manipulation of reward models, data, or environment signals—and from optimization pressure in agents exploiting misspecifications or learned model blind spots.

## Defenses

Adversarially trained reward models are more robust against attacks and mitigate reward hacking, allowing RLHF to proceed for three times as many steps without exhibiting reward hacking.

The research indicates that PRM robustness is a critical safety concern for AI alignment, with systematic vulnerabilities requiring both detection mechanisms and architectural improvements to address.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb68ef0a-68ff-4ed1-a06e-ce01235ef46d",
  "isSidechain": false,
  "promptId": "18034a7d-47e3-4c01-b7f9-6c61bf20f18e",
  "type": "user",
  "uuid": "d1985b7b-2320-4e98-bf5b-de5bc84f5e71",
  "toolUseResult": {
    "query": "process reward model hackability adversarial attack reward hacking PRM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X3eJUgwreUHtWzAEWifJdQ",
        "content": [
          {
            "title": "GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub",
            "url": "https://github.com/xhwang22/Awesome-Reward-Hacking"
          },
          {
            "title": "[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/abs/2603.06621"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "Adversarial Reward-Hacking",
            "url": "https://www.emergentmind.com/topics/adversarial-reward-hacking"
          },
          {
            "title": "Adversarial Training of Reward Models",
            "url": "https://arxiv.org/pdf/2504.06141"
          },
          {
            "title": "Beyond Semantic Manipulation: Token-Space Attacks on Reward Models",
            "url": "https://arxiv.org/pdf/2604.02686"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2603.06621"
          },
          {
            "title": "Adversarial Reward Auditing for Active Detection and ...",
            "url": "https://arxiv.org/pdf/2602.01750"
          }
        ]
      },
      "Based on the search results, here's what I found about process reward model hackability and adversarial attacks:\n\n## Key Recent Research (2025-2026)\n\nAdversarial optimization demonstrates that gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks. A particularly significant finding is that policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.\n\nCurrent PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.\n\n## Types of Attacks and Vulnerabilities\n\nStatic perturbation analysis uncovers a fluency-logic dissociation: high invariance to surface-level style changes with reward changes <0.1, yet inconsistent detection of logically-corrupted reasoning.\n\nReward hacking arises both from adversarial attacks—malicious manipulation of reward models, data, or environment signals—and from optimization pressure in agents exploiting misspecifications or learned model blind spots.\n\n## Defenses\n\nAdversarially trained reward models are more robust against attacks and mitigate reward hacking, allowing RLHF to proceed for three times as many steps without exhibiting reward hacking.\n\nThe research indicates that PRM robustness is a critical safety concern for AI alignment, with systematic vulnerabilities requiring both detection mechanisms and architectural improvements to address."
    ],
    "durationSeconds": 7.5170985450000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cb68ef0a-68ff-4ed1-a06e-ce01235ef46d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T05:51:49.441Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UV4DsSdCTKhK6vVELjwTcq`</summary>

```json
{
  "query": "calibration reward hacking defense pessimism RL training 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1985b7b-2320-4e98-bf5b-de5bc84f5e71",
  "isSidechain": false,
  "requestId": "req_011CbDJKJs4CbCPkooLFDYLB",
  "type": "assistant",
  "uuid": "798c6b17-fa40-444d-ba0b-44679570e34c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015zMEQzzohFcQL8KHsPgvjL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 21697,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 21697,
          "cache_creation_input_tokens": 794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 794
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

_source line 18 · 2026-05-20T05:51:57.952Z_

<details><summary>↩ Tool result · `toolu_01UV4DsSdCTKhK6vVELjwTcq`</summary>

```text
Web search results for query: "calibration reward hacking defense pessimism RL training 2025 2026 arxiv"

Links: [{"title":"[2604.04648] From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/abs/2604.04648"},{"title":"[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/abs/2502.18770"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/pdf/2604.04648"},{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"Natural Emergent Misalignment from Reward Hacking in Production RL","url":"https://arxiv.org/pdf/2511.18397"},{"title":"Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study","url":"https://arxiv.org/html/2507.05619v1"},{"title":"Natural emergent misalignment from reward hacking in production RL","url":"https://arxiv.org/html/2511.18397v1"}]

I found several recent arxiv papers related to your search query about calibration, reward hacking, defense mechanisms, pessimism, and RL training from 2025-2026:

## Key Papers Found:

1. **"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism"** (April 2026)
   - Uses lower confidence bounds on value estimates to avoid out-of-distribution actions, with an approach called "caution" that penalizes prediction error as a signal of distributional uncertainty.

2. **"Reward Shaping to Mitigate Reward Hacking in RLHF"** (January 2026)
   - Addresses reward hacking through reward shaping, with design principles including that RL rewards should be bounded and benefit from rapid initial growth followed by gradual convergence. Proposes "Preference As Reward" (PAR), leveraging latent preferences in the reward model.

3. **"Learning a Pessimistic Reward Model in RLHF"** (May 2025)
   - Demonstrates feasibility of learning a pessimistic reward model against reward hacking, allowing greedy policy search without suffering from reward hacking.

4. **"Natural Emergent Misalignment from Reward Hacking in Production RL"** (November 2025)
   - Multiple major AI labs have reported reward hacking in their training runs, with research exploring generalization effects of reward hacking.

5. **"Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems"** (July 2025)
   - A comprehensive empirical study on detection and mitigation approaches.

These papers represent recent research advances in addressing reward hacking through pessimistic approaches and improved calibration methods in RL systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "798c6b17-fa40-444d-ba0b-44679570e34c",
  "isSidechain": false,
  "promptId": "18034a7d-47e3-4c01-b7f9-6c61bf20f18e",
  "type": "user",
  "uuid": "f2ef6f3f-5d21-4983-8be2-55cce5a0f15f",
  "toolUseResult": {
    "query": "calibration reward hacking defense pessimism RL training 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_016dcLQH4wn6HZt81bW6iaVC",
        "content": [
          {
            "title": "[2604.04648] From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism",
            "url": "https://arxiv.org/abs/2604.04648"
          },
          {
            "title": "[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/abs/2502.18770"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/pdf/2505.20556"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism",
            "url": "https://arxiv.org/pdf/2604.04648"
          },
          {
            "title": "GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub",
            "url": "https://github.com/xhwang22/Awesome-Reward-Hacking"
          },
          {
            "title": "Natural Emergent Misalignment from Reward Hacking in Production RL",
            "url": "https://arxiv.org/pdf/2511.18397"
          },
          {
            "title": "Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study",
            "url": "https://arxiv.org/html/2507.05619v1"
          },
          {
            "title": "Natural emergent misalignment from reward hacking in production RL",
            "url": "https://arxiv.org/html/2511.18397v1"
          }
        ]
      },
      "I found several recent arxiv papers related to your search query about calibration, reward hacking, defense mechanisms, pessimism, and RL training from 2025-2026:\n\n## Key Papers Found:\n\n1. **\"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism\"** (April 2026)\n   - Uses lower confidence bounds on value estimates to avoid out-of-distribution actions, with an approach called \"caution\" that penalizes prediction error as a signal of distributional uncertainty.\n\n2. **\"Reward Shaping to Mitigate Reward Hacking in RLHF\"** (January 2026)\n   - Addresses reward hacking through reward shaping, with design principles including that RL rewards should be bounded and benefit from rapid initial growth followed by gradual convergence. Proposes \"Preference As Reward\" (PAR), leveraging latent preferences in the reward model.\n\n3. **\"Learning a Pessimistic Reward Model in RLHF\"** (May 2025)\n   - Demonstrates feasibility of learning a pessimistic reward model against reward hacking, allowing greedy policy search without suffering from reward hacking.\n\n4. **\"Natural Emergent Misalignment from Reward Hacking in Production RL\"** (November 2025)\n   - Multiple major AI labs have reported reward hacking in their training runs, with research exploring generalization effects of reward hacking.\n\n5. **\"Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems\"** (July 2025)\n   - A comprehensive empirical study on detection and mitigation approaches.\n\nThese papers represent recent research advances in addressing reward hacking through pessimistic approaches and improved calibration methods in RL systems."
    ],
    "durationSeconds": 8.50740452,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "798c6b17-fa40-444d-ba0b-44679570e34c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T05:52:00.663Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SE7yM7iDEs5gPrYFwdQpPp`</summary>

```json
{
  "query": "\"reward hacking\" \"step-level\" defense \"process reward\" uncertainty calibration causal 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2ef6f3f-5d21-4983-8be2-55cce5a0f15f",
  "isSidechain": false,
  "requestId": "req_011CbDJL8U1Lm1Q6koxnGgHp",
  "type": "assistant",
  "uuid": "ac2d058a-1abd-49f5-89a4-706d53b55bc2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEKvsKb6eCJSVFao7kLtbc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 22491,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 22491,
          "cache_creation_input_tokens": 951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 951
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

_source line 20 · 2026-05-20T05:52:08.721Z_

<details><summary>↩ Tool result · `toolu_01SE7yM7iDEs5gPrYFwdQpPp`</summary>

```text
Web search results for query: ""reward hacking" "step-level" defense "process reward" uncertainty calibration causal 2026"

Links: [{"title":"Reward Hacking Defense Rubric","url":"https://www.emergentmind.com/topics/reward-hacking-defense-rubric"},{"title":"Reward Hacking Trap","url":"https://www.emergentmind.com/topics/reward-hacking-trap"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/pdf/2508.04216"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/pdf/2602.10623"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/pdf/2603.06621"}]

Based on the search results, here's what I found regarding your query about reward hacking, step-level defense, process reward models, and related concepts from 2026:

## Recent Research on Reward Hacking Defenses

Open research avenues include integrating causal and reference-based paradigms, hybridizing adversarial feedback with uncertainty quantification, and formalizing optimal defense-stopping conditions.

## Process Reward Models and Vulnerabilities

Process Reward Models (PRMs) provide step-level supervision for chain-of-thought reasoning, enabling finer-grained credit assignment than outcome-based alternatives. However, policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.

## Causal Approaches to Mitigation

Causal Reward Adjustment (CRA) mitigates reward hacking by estimating the true reward of a reasoning path, training sparse autoencoders on the PRM's internal activations to recover interpretable features, then correcting confounding by using backdoor adjustment.

Additionally, CausalRM is a causal reward model that filters out reward-irrelevant information via factored representation learning.

## Uncertainty-Aware Methods

Recent work focuses on uncertainty-aware modeling, primarily through computationally intensive model ensembles or by adding post-hoc uncertainty penalties to the reward signal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac2d058a-1abd-49f5-89a4-706d53b55bc2",
  "isSidechain": false,
  "promptId": "18034a7d-47e3-4c01-b7f9-6c61bf20f18e",
  "type": "user",
  "uuid": "79184a10-ea17-4b9c-b1ff-ea528c5c8530",
  "toolUseResult": {
    "query": "\"reward hacking\" \"step-level\" defense \"process reward\" uncertainty calibration causal 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SWUJgU4bAwCEMB8nEf5e6f",
        "content": [
          {
            "title": "Reward Hacking Defense Rubric",
            "url": "https://www.emergentmind.com/topics/reward-hacking-defense-rubric"
          },
          {
            "title": "Reward Hacking Trap",
            "url": "https://www.emergentmind.com/topics/reward-hacking-trap"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/pdf/2508.04216"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/pdf/2602.10623"
          },
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://arxiv.org/pdf/2601.21350"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/pdf/2603.06621"
          }
        ]
      },
      "Based on the search results, here's what I found regarding your query about reward hacking, step-level defense, process reward models, and related concepts from 2026:\n\n## Recent Research on Reward Hacking Defenses\n\nOpen research avenues include integrating causal and reference-based paradigms, hybridizing adversarial feedback with uncertainty quantification, and formalizing optimal defense-stopping conditions.\n\n## Process Reward Models and Vulnerabilities\n\nProcess Reward Models (PRMs) provide step-level supervision for chain-of-thought reasoning, enabling finer-grained credit assignment than outcome-based alternatives. However, policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.\n\n## Causal Approaches to Mitigation\n\nCausal Reward Adjustment (CRA) mitigates reward hacking by estimating the true reward of a reasoning path, training sparse autoencoders on the PRM's internal activations to recover interpretable features, then correcting confounding by using backdoor adjustment.\n\nAdditionally, CausalRM is a causal reward model that filters out reward-irrelevant information via factored representation learning.\n\n## Uncertainty-Aware Methods\n\nRecent work focuses on uncertainty-aware modeling, primarily through computationally intensive model ensembles or by adding post-hoc uncertainty penalties to the reward signal."
    ],
    "durationSeconds": 8.053241512000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ac2d058a-1abd-49f5-89a4-706d53b55bc2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense  ## Description We present the first causally rigorous study connecting P…",
  "leafUuid": "79184a10-ea17-4b9c-b1ff-ea528c5c8530",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Calibration quality and PRM reward hacking resistance",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe"
}
```

---

### Tool call

_source line 23 · 2026-05-20T05:52:11.731Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Juv6q2baoBwYW855F3Mzxv`</summary>

```json
{
  "query": "Ackermann gradient regularization reward hacking Hessian reward model flatness 2026 arxiv 2602.18037"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79184a10-ea17-4b9c-b1ff-ea528c5c8530",
  "isSidechain": false,
  "requestId": "req_011CbDJLvSEoLxjqXbEHy6tQ",
  "type": "assistant",
  "uuid": "4fb7bbf0-83ad-4167-a5c2-786945b69bdf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YDeLyCNzFyrm8AMnYg6Ey8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 23442,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 23442,
          "cache_creation_input_tokens": 717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 717
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

_source line 24 · 2026-05-20T05:52:18.817Z_

<details><summary>↩ Tool result · `toolu_01Juv6q2baoBwYW855F3Mzxv`</summary>

```text
Web search results for query: "Ackermann gradient regularization reward hacking Hessian reward model flatness 2026 arxiv 2602.18037"

Links: [{"title":"[2602.18037] Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards","url":"https://arxiv.org/abs/2602.18037"},{"title":"Detecting and Suppressing Reward Hacking with Gradient Fingerprints","url":"https://arxiv.org/html/2604.16242v1"},{"title":"Gradient Regularization Prevents Reward Hacking in ...","url":"https://arxiv.org/pdf/2602.18037"},{"title":"Johannes Ackermann","url":"https://johannesack.github.io/"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/html/2604.02986v1"},{"title":"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking","url":"https://arxiv.org/pdf/2501.19358"},{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking","url":"https://arxiv.org/html/2403.03185v3"},{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward   Hacking","url":"https://arxiv.org/pdf/2403.03185"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"}]

I found the paper you're looking for. Here's what I found about arxiv 2602.18037:

The paper is titled "Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards" by Johannes Ackermann, Michael Noukhovitch, Takashi Ishida, and Masashi Sugiyama, submitted on February 20, 2026.

The paper addresses reward hacking, where a policy may exploit inaccuracies of the reward and learn unintended behavior. The authors propose training language models in a way that biases policy updates towards regions where the reward is more accurate, deriving a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence, and showing that gradient regularization can be used to bias training to flatter regions to maintain reward model accuracy. They confirm these results by showing that the gradient norm and reward accuracy are empirically correlated in RLHF.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fb7bbf0-83ad-4167-a5c2-786945b69bdf",
  "isSidechain": false,
  "promptId": "18034a7d-47e3-4c01-b7f9-6c61bf20f18e",
  "type": "user",
  "uuid": "698b284b-1e08-4aa3-bec4-b7ca0f3370cc",
  "toolUseResult": {
    "query": "Ackermann gradient regularization reward hacking Hessian reward model flatness 2026 arxiv 2602.18037",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DU7v8QrRDzeeV5EcPmHEWi",
        "content": [
          {
            "title": "[2602.18037] Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards",
            "url": "https://arxiv.org/abs/2602.18037"
          },
          {
            "title": "Detecting and Suppressing Reward Hacking with Gradient Fingerprints",
            "url": "https://arxiv.org/html/2604.16242v1"
          },
          {
            "title": "Gradient Regularization Prevents Reward Hacking in ...",
            "url": "https://arxiv.org/pdf/2602.18037"
          },
          {
            "title": "Johannes Ackermann",
            "url": "https://johannesack.github.io/"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/html/2604.02986v1"
          },
          {
            "title": "The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking",
            "url": "https://arxiv.org/pdf/2501.19358"
          },
          {
            "title": "Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking",
            "url": "https://arxiv.org/html/2403.03185v3"
          },
          {
            "title": "Correlated Proxies: A New Definition and Improved Mitigation for Reward   Hacking",
            "url": "https://arxiv.org/pdf/2403.03185"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/pdf/2604.02986"
          }
        ]
      },
      "I found the paper you're looking for. Here's what I found about arxiv 2602.18037:\n\nThe paper is titled \"Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards\" by Johannes Ackermann, Michael Noukhovitch, Takashi Ishida, and Masashi Sugiyama, submitted on February 20, 2026.\n\nThe paper addresses reward hacking, where a policy may exploit inaccuracies of the reward and learn unintended behavior. The authors propose training language models in a way that biases policy updates towards regions where the reward is more accurate, deriving a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence, and showing that gradient regularization can be used to bias training to flatter regions to maintain reward model accuracy. They confirm these results by showing that the gradient norm and reward accuracy are empirically correlated in RLHF."
    ],
    "durationSeconds": 7.081541963000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4fb7bbf0-83ad-4167-a5c2-786945b69bdf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T05:52:21.475Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CqXfohmAAQMNT6DjxvCmET`</summary>

```json
{
  "query": "distributional process reward model conditional optimal transport calibrated arxiv 2605.06785"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "698b284b-1e08-4aa3-bec4-b7ca0f3370cc",
  "isSidechain": false,
  "requestId": "req_011CbDJMfb3VruQVomTaT7yo",
  "type": "assistant",
  "uuid": "ba64c979-933c-4d8b-8b94-5d15c25d8bc2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014j7NVjJrKWLCpginpWb7zX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 757,
      "cache_read_input_tokens": 24159,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 757,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 24159,
          "cache_creation_input_tokens": 757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 757
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

_source line 26 · 2026-05-20T05:52:31.228Z_

<details><summary>↩ Tool result · `toolu_01CqXfohmAAQMNT6DjxvCmET`</summary>

```text
Web search results for query: "distributional process reward model conditional optimal transport calibrated arxiv 2605.06785"

Links: [{"title":"[2605.06785] Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/abs/2605.06785"},{"title":"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/html/2605.06785"},{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/new"},{"title":"Consistent Optimal Transport with Empirical Conditional Measures","url":"https://arxiv.org/pdf/2305.15901"},{"title":"APLOT: Robust Reward Modeling via Adaptive Preference Learning with Optimal Transport","url":"https://arxiv.org/pdf/2510.10963"},{"title":"Distributional Preference Alignment of LLMs via Optimal Transport","url":"https://arxiv.org/pdf/2406.05882"},{"title":"Conditional Risk Minimization with Side Information: A Tractable, Universal Optimal Transport Framework","url":"https://arxiv.org/pdf/2509.23128"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

## Paper Summary

**Title:** "Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport"

**Authors:** Rachel Ma, Dylan Hadfield-Menell, and Kristjan Greenewald

**Submitted:** May 7, 2026

## Key Contributions

The paper addresses the problem that Process Reward Models (PRMs) used in inference-time scaling are often poorly calibrated and overestimate success probabilities. The authors propose the first use of conditional optimal transport for calibrating PRMs, modifying conditional OT map learning to estimate a monotonic conditional quantile function over success probabilities estimated by the PRM, conditioned on PRM hidden states.

This approach yields structurally valid quantile estimates and enables efficient extraction of confidence bounds at arbitrary levels, which they integrate into the instance-adaptive scaling (IAS) framework.

## Evaluation

The method is evaluated on mathematical reasoning benchmarks spanning moderate-difficulty problems (MATH-500) and harder out-of-distribution problems (AIME), where it substantially improves calibration over both uncalibrated PRMs and quantile regression for PRMs with reliable ranking signals.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba64c979-933c-4d8b-8b94-5d15c25d8bc2",
  "isSidechain": false,
  "promptId": "18034a7d-47e3-4c01-b7f9-6c61bf20f18e",
  "type": "user",
  "uuid": "fe43214e-7c07-43f4-8a5a-6f64b4f1a7cb",
  "toolUseResult": {
    "query": "distributional process reward model conditional optimal transport calibrated arxiv 2605.06785",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DpnN2VDt677urR6TRpYvM1",
        "content": [
          {
            "title": "[2605.06785] Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport",
            "url": "https://arxiv.org/abs/2605.06785"
          },
          {
            "title": "Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport",
            "url": "https://arxiv.org/html/2605.06785"
          },
          {
            "title": "Machine Learning",
            "url": "https://arxiv.org/list/cs.LG/new"
          },
          {
            "title": "Consistent Optimal Transport with Empirical Conditional Measures",
            "url": "https://arxiv.org/pdf/2305.15901"
          },
          {
            "title": "APLOT: Robust Reward Modeling via Adaptive Preference Learning with Optimal Transport",
            "url": "https://arxiv.org/pdf/2510.10963"
          },
          {
            "title": "Distributional Preference Alignment of LLMs via Optimal Transport",
            "url": "https://arxiv.org/pdf/2406.05882"
          },
          {
            "title": "Conditional Risk Minimization with Side Information: A Tractable, Universal Optimal Transport Framework",
            "url": "https://arxiv.org/pdf/2509.23128"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what I found:\n\n## Paper Summary\n\n**Title:** \"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport\"\n\n**Authors:** Rachel Ma, Dylan Hadfield-Menell, and Kristjan Greenewald\n\n**Submitted:** May 7, 2026\n\n## Key Contributions\n\nThe paper addresses the problem that Process Reward Models (PRMs) used in inference-time scaling are often poorly calibrated and overestimate success probabilities. The authors propose the first use of conditional optimal transport for calibrating PRMs, modifying conditional OT map learning to estimate a monotonic conditional quantile function over success probabilities estimated by the PRM, conditioned on PRM hidden states.\n\nThis approach yields structurally valid quantile estimates and enables efficient extraction of confidence bounds at arbitrary levels, which they integrate into the instance-adaptive scaling (IAS) framework.\n\n## Evaluation\n\nThe method is evaluated on mathematical reasoning benchmarks spanning moderate-difficulty problems (MATH-500) and harder out-of-distribution problems (AIME), where it substantially improves calibration over both uncalibrated PRMs and quantile regression for PRMs with reliable ranking signals."
    ],
    "durationSeconds": 9.749505184000009,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ba64c979-933c-4d8b-8b94-5d15c25d8bc2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T05:52:34.278Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mj1KsYfqcQpAd2hSyamUie`</summary>

```json
{
  "query": "causal reward adjustment sparse autoencoder PRM reward hacking defense 2026 arxiv 2508.04216"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe43214e-7c07-43f4-8a5a-6f64b4f1a7cb",
  "isSidechain": false,
  "requestId": "req_011CbDJNanbiAkA4jGGrVaUB",
  "type": "assistant",
  "uuid": "5d192480-3c84-4686-8159-f8f0f971a734",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jix1oHgbbDgW41cW5uv164",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 24916,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 686,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 24916,
          "cache_creation_input_tokens": 686,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 686
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

_source line 28 · 2026-05-20T05:52:40.448Z_

<details><summary>↩ Tool result · `toolu_01Mj1KsYfqcQpAd2hSyamUie`</summary>

```text
Web search results for query: "causal reward adjustment sparse autoencoder PRM reward hacking defense 2026 arxiv 2508.04216"

Links: [{"title":"[2508.04216] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/abs/2508.04216"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in ...","url":"https://arxiv.org/pdf/2508.04216"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/html/2508.04216v1"},{"title":"IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/pdf/2602.19416"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/pdf/2603.06621"},{"title":"Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment","url":"https://arxiv.org/pdf/2501.09620"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/pdf/2602.10623"}]

Based on the search results, I found the paper you're looking for:

**Causal Reward Adjustment (CRA)** is a method that mitigates reward hacking by estimating the true reward of a reasoning path. 

The method trains sparse autoencoders on the PRM's internal activations to recover interpretable features, then corrects confounding by using backdoor adjustment.

**Context of the Problem:**
External reasoning systems with process reward models (PRMs) are prone to reward hacking, where high-scoring but logically incorrect paths are assigned high scores by the PRMs, leading to incorrect answers. From a causal inference perspective, this phenomenon is primarily attributed to the presence of confounding semantic features.

**Results:**
Experiments on math solving datasets demonstrate that CRA mitigates reward hacking and improves final accuracy, without modifying the policy model or retraining PRM.

The paper (arXiv 2508.04216) was published on August 6, 2025, and represents a novel approach to addressing reward hacking in reasoning systems by combining sparse autoencoder interpretability with causal inference techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d192480-3c84-4686-8159-f8f0f971a734",
  "isSidechain": false,
  "promptId": "18034a7d-47e3-4c01-b7f9-6c61bf20f18e",
  "type": "user",
  "uuid": "0d8e6b9c-e0c7-40d8-a74c-243dba2de897",
  "toolUseResult": {
    "query": "causal reward adjustment sparse autoencoder PRM reward hacking defense 2026 arxiv 2508.04216",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TKztL8iPYwbXRA78tJqrhs",
        "content": [
          {
            "title": "[2508.04216] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/abs/2508.04216"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in ...",
            "url": "https://arxiv.org/pdf/2508.04216"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/html/2508.04216v1"
          },
          {
            "title": "IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking",
            "url": "https://arxiv.org/pdf/2602.19416"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment",
            "url": "https://arxiv.org/pdf/2501.09620"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/pdf/2602.10623"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Causal Reward Adjustment (CRA)** is a method that mitigates reward hacking by estimating the true reward of a reasoning path. \n\nThe method trains sparse autoencoders on the PRM's internal activations to recover interpretable features, then corrects confounding by using backdoor adjustment.\n\n**Context of the Problem:**\nExternal reasoning systems with process reward models (PRMs) are prone to reward hacking, where high-scoring but logically incorrect paths are assigned high scores by the PRMs, leading to incorrect answers. From a causal inference perspective, this phenomenon is primarily attributed to the presence of confounding semantic features.\n\n**Results:**\nExperiments on math solving datasets demonstrate that CRA mitigates reward hacking and improves final accuracy, without modifying the policy model or retraining PRM.\n\nThe paper (arXiv 2508.04216) was published on August 6, 2025, and represents a novel approach to addressing reward hacking in reasoning systems by combining sparse autoencoder interpretability with causal inference techniques."
    ],
    "durationSeconds": 6.163535770000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5d192480-3c84-4686-8159-f8f0f971a734",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T05:52:40.453Z_

```json
{
  "parentUuid": "0d8e6b9c-e0c7-40d8-a74c-243dba2de897",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3e3f711a-697b-494d-afd3-155d1334a215",
  "timestamp": "2026-05-20T05:52:40.453Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-20T05:52:43.807Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N9HPbH2vGXf4eEY2ux4JRo`</summary>

```json
{
  "query": "\"pessimistic reward\" \"learning pessimistic reward model\" RLHF overoptimization defense 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e3f711a-697b-494d-afd3-155d1334a215",
  "isSidechain": false,
  "requestId": "req_011CbDJPG6yZqzgpBahL3EoA",
  "type": "assistant",
  "uuid": "f0d27af2-e5d6-4bf6-85cc-5ed1ad501037",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Vz8Y1ZkGGv47hsceYZ6Pa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 821,
      "cache_read_input_tokens": 25602,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 821,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 25602,
          "cache_creation_input_tokens": 821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 821
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

_source line 31 · 2026-05-20T05:52:52.338Z_

<details><summary>↩ Tool result · `toolu_01N9HPbH2vGXf4eEY2ux4JRo`</summary>

```text
Web search results for query: ""pessimistic reward" "learning pessimistic reward model" RLHF overoptimization defense 2025 2026 arxiv"

Links: [{"title":"Learning a Pessimistic Reward Model in RLHF | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.20556v1"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"Pessimistic Reward Tuning (PET) in RLHF","url":"https://www.emergentmind.com/topics/pessimistic-reward-tuning-pet"},{"title":"[2505.20556] Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/abs/2505.20556"},{"title":"Learning from Failures: Understanding LLM Alignment through Failure-Aware Inverse RL","url":"https://arxiv.org/html/2510.06092v1"},{"title":"Circuit-Aware Reward Training: A Mechanistic Framework for Longtail Robustness in RLHF","url":"https://arxiv.org/html/2509.24713v1"}]

Based on the search results, I found relevant information about pessimistic reward models and RLHF overoptimization defense from recent 2025-2026 research on arxiv:

## Key Findings

**Main Paper: Learning a Pessimistic Reward Model in RLHF**

A recent work proposes 'PET', a novel pessimistic reward fine-tuning method, to learn a pessimistic reward model robust against reward hacking in offline reinforcement learning from human feedback (RLHF).

**How it Works**

Traditional reward modeling techniques in RLHF train an imperfect reward model, on which a KL regularization plays a pivotal role in mitigating reward hacking when optimizing a policy, but such an intuition-based method still suffers from reward hacking. In contrast, when optimizing a policy on a pessimistic reward model fine-tuned through PET, reward hacking can be prevented without relying on any regularization.

**Empirical Results**

The method is tested on the standard TL;DR summarization dataset, and one can learn a high-quality policy on the pessimistic reward without using any regularization.

**Broader Context**

Recent RLHF work highlights that PET (Xu et al., 2025) trains pessimistic reward models to mitigate reward hacking, alongside other approaches like REFORM which discovers adversarial failure modes to improve robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0d27af2-e5d6-4bf6-85cc-5ed1ad501037",
  "isSidechain": false,
  "promptId": "18034a7d-47e3-4c01-b7f9-6c61bf20f18e",
  "type": "user",
  "uuid": "f6c87478-3567-4d56-8300-24cddb54ce80",
  "toolUseResult": {
    "query": "\"pessimistic reward\" \"learning pessimistic reward model\" RLHF overoptimization defense 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xz2Nrp1m2wUvD8EMYoTbPp",
        "content": [
          {
            "title": "Learning a Pessimistic Reward Model in RLHF | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2505.20556v1"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/pdf/2505.20556"
          },
          {
            "title": "Pessimistic Reward Tuning (PET) in RLHF",
            "url": "https://www.emergentmind.com/topics/pessimistic-reward-tuning-pet"
          },
          {
            "title": "[2505.20556] Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/abs/2505.20556"
          },
          {
            "title": "Learning from Failures: Understanding LLM Alignment through Failure-Aware Inverse RL",
            "url": "https://arxiv.org/html/2510.06092v1"
          },
          {
            "title": "Circuit-Aware Reward Training: A Mechanistic Framework for Longtail Robustness in RLHF",
            "url": "https://arxiv.org/html/2509.24713v1"
          }
        ]
      },
      "Based on the search results, I found relevant information about pessimistic reward models and RLHF overoptimization defense from recent 2025-2026 research on arxiv:\n\n## Key Findings\n\n**Main Paper: Learning a Pessimistic Reward Model in RLHF**\n\nA recent work proposes 'PET', a novel pessimistic reward fine-tuning method, to learn a pessimistic reward model robust against reward hacking in offline reinforcement learning from human feedback (RLHF).\n\n**How it Works**\n\nTraditional reward modeling techniques in RLHF train an imperfect reward model, on which a KL regularization plays a pivotal role in mitigating reward hacking when optimizing a policy, but such an intuition-based method still suffers from reward hacking. In contrast, when optimizing a policy on a pessimistic reward model fine-tuned through PET, reward hacking can be prevented without relying on any regularization.\n\n**Empirical Results**\n\nThe method is tested on the standard TL;DR summarization dataset, and one can learn a high-quality policy on the pessimistic reward without using any regularization.\n\n**Broader Context**\n\nRecent RLHF work highlights that PET (Xu et al., 2025) trains pessimistic reward models to mitigate reward hacking, alongside other approaches like REFORM which discovers adversarial failure modes to improve robustness."
    ],
    "durationSeconds": 8.527452629999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f0d27af2-e5d6-4bf6-85cc-5ed1ad501037",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T05:52:55.206Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G8aAxeK6z3ZMuSLCLrKopx`</summary>

```json
{
  "query": "reward model calibration causes robustness hackability causal link evidence 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6c87478-3567-4d56-8300-24cddb54ce80",
  "isSidechain": false,
  "requestId": "req_011CbDJQ8w9m21N8gXCLJE5L",
  "type": "assistant",
  "uuid": "1e207c44-82a2-4af9-9c20-1efbe3cd3b19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7XcrtjWnj7nscCtn8mRMv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 26423,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 758,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 26423,
          "cache_creation_input_tokens": 758,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 758
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

_source line 33 · 2026-05-20T05:53:03.099Z_

<details><summary>↩ Tool result · `toolu_01G8aAxeK6z3ZMuSLCLrKopx`</summary>

```text
Web search results for query: "reward model calibration causes robustness hackability causal link evidence 2025 2026"

Links: [{"title":"Robust Reward Modeling for Large Language Models via Causal Decomposition","url":"https://arxiv.org/html/2604.13833"},{"title":"Robust Reward Modeling via Causal Rubrics | OpenReview","url":"https://openreview.net/forum?id=oP99JQiDYp"},{"title":"RRM: Robust Reward Model Training Mitigates Reward Hacking | OpenReview","url":"https://openreview.net/forum?id=88AS5MQnmC"},{"title":"Robust Reward Modeling via Causal Rubrics","url":"https://www.researchgate.net/publication/392918827_Robust_Reward_Modeling_via_Causal_Rubrics"},{"title":"Robust Reward Modeling via Causal Rubrics","url":"https://arxiv.org/pdf/2506.16507"},{"title":"Paper page - Robust Reward Modeling via Causal Rubrics","url":"https://huggingface.co/papers/2506.16507"},{"title":"[2506.16507] Robust Reward Modeling via Causal Rubrics","url":"https://arxiv.org/abs/2506.16507"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"}]

Based on the search results, I found several recent papers (2025-2026) that establish causal links between reward model calibration and robustness to hacking:

## Key Findings:

The first paper to point out the reason for reward hacking from a causal perspective identifies that traditional RM training struggles to disentangle prompt-driven preferences from prompt-independent artifacts, and RMs fail to effectively distinguish between contextual signals and irrelevant artifacts when determining preferences.

RMs often learn to assign high scores based on superficial or spurious attributes like response length, formatting patterns, or stylistic quirks because standard training objectives do not explicitly require the RM to disentangle the true causal drivers of response quality from these spurious correlates, leading to brittle RMs.

## Causal Framework Approaches:

Researchers introduced a causal framework that learns preferences independent of artifacts and proposed a novel data augmentation technique designed to eliminate them, showing that this approach successfully filters out undesirable artifacts, yielding a more robust reward model.

CROME (Causally Robust Reward Modeling) is a novel framework grounded in an explicit causal model designed to mitigate reward hacking.

## Empirical Evidence:

CROME significantly outperforms standard baselines on RewardBench, improving average accuracy by up to 5.4% and achieving gains of up to 13.2% and 7.2% in specific categories, with consistent gains in Best-of-N inference across various benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e207c44-82a2-4af9-9c20-1efbe3cd3b19",
  "isSidechain": false,
  "promptId": "18034a7d-47e3-4c01-b7f9-6c61bf20f18e",
  "type": "user",
  "uuid": "3b985b39-ed40-4404-863a-d35f0b0e2849",
  "toolUseResult": {
    "query": "reward model calibration causes robustness hackability causal link evidence 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XsxmX8BdjCGCWJo7qq5RE1",
        "content": [
          {
            "title": "Robust Reward Modeling for Large Language Models via Causal Decomposition",
            "url": "https://arxiv.org/html/2604.13833"
          },
          {
            "title": "Robust Reward Modeling via Causal Rubrics | OpenReview",
            "url": "https://openreview.net/forum?id=oP99JQiDYp"
          },
          {
            "title": "RRM: Robust Reward Model Training Mitigates Reward Hacking | OpenReview",
            "url": "https://openreview.net/forum?id=88AS5MQnmC"
          },
          {
            "title": "Robust Reward Modeling via Causal Rubrics",
            "url": "https://www.researchgate.net/publication/392918827_Robust_Reward_Modeling_via_Causal_Rubrics"
          },
          {
            "title": "Robust Reward Modeling via Causal Rubrics",
            "url": "https://arxiv.org/pdf/2506.16507"
          },
          {
            "title": "Paper page - Robust Reward Modeling via Causal Rubrics",
            "url": "https://huggingface.co/papers/2506.16507"
          },
          {
            "title": "[2506.16507] Robust Reward Modeling via Causal Rubrics",
            "url": "https://arxiv.org/abs/2506.16507"
          },
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://arxiv.org/pdf/2601.21350"
          }
        ]
      },
      "Based on the search results, I found several recent papers (2025-2026) that establish causal links between reward model calibration and robustness to hacking:\n\n## Key Findings:\n\nThe first paper to point out the reason for reward hacking from a causal perspective identifies that traditional RM training struggles to disentangle prompt-driven preferences from prompt-independent artifacts, and RMs fail to effectively distinguish between contextual signals and irrelevant artifacts when determining preferences.\n\nRMs often learn to assign high scores based on superficial or spurious attributes like response length, formatting patterns, or stylistic quirks because standard training objectives do not explicitly require the RM to disentangle the true causal drivers of response quality from these spurious correlates, leading to brittle RMs.\n\n## Causal Framework Approaches:\n\nResearchers introduced a causal framework that learns preferences independent of artifacts and proposed a novel data augmentation technique designed to eliminate them, showing that this approach successfully filters out undesirable artifacts, yielding a more robust reward model.\n\nCROME (Causally Robust Reward Modeling) is a novel framework grounded in an explicit causal model designed to mitigate reward hacking.\n\n## Empirical Evidence:\n\nCROME significantly outperforms standard baselines on RewardBench, improving average accuracy by up to 5.4% and achieving gains of up to 13.2% and 7.2% in specific categories, with consistent gains in Best-of-N inference across various benchmarks."
    ],
    "durationSeconds": 7.887748992999986,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1e207c44-82a2-4af9-9c20-1efbe3cd3b19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense  ## Description We present the first causally rigorous study connecting P…",
  "leafUuid": "3b985b39-ed40-4404-863a-d35f0b0e2849",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Calibration quality and PRM reward hacking resistance",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe"
}
```

---

### Tool call

_source line 36 · 2026-05-20T05:53:05.896Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XWfgq3cG2gBdTme154JKC4`</summary>

```json
{
  "query": "Hessian spectral analysis reward model loss landscape step level PRM geometry 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b985b39-ed40-4404-863a-d35f0b0e2849",
  "isSidechain": false,
  "requestId": "req_011CbDJQvw7JAcf3otztHth1",
  "type": "assistant",
  "uuid": "c37e1c50-ec43-49cb-ae6d-5e3a67ac14e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1osKBURaHccgbwrboN2B7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 811,
      "cache_read_input_tokens": 27181,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 811,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 27181,
          "cache_creation_input_tokens": 811,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 811
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

_source line 37 · 2026-05-20T05:53:12.956Z_

<details><summary>↩ Tool result · `toolu_01XWfgq3cG2gBdTme154JKC4`</summary>

```text
Web search results for query: "Hessian spectral analysis reward model loss landscape step level PRM geometry 2025 2026"

Links: [{"title":"Unraveling the Hessian: A Key to Smooth Convergence in Loss Function Landscapes | Doklady Mathematics | Springer Nature Link","url":"https://link.springer.com/article/10.1134/S1064562424601987"},{"title":"Unraveling the Hessian: A Key to Smooth Convergence in Loss Function Landscapes","url":"https://arxiv.org/html/2409.11995v1"},{"title":"Topological Exploration of High-Dimensional Empirical Risk Landscapes: general approach, and applications to phase retrieval","url":"https://arxiv.org/pdf/2602.17779"},{"title":"Investigating generalization capabilities of neural networks by means of   loss landscapes and Hessian analysis","url":"https://arxiv.org/pdf/2412.10146"},{"title":"The Role of the Time-Dependent Hessian in High-Dimensional Optimization","url":"https://arxiv.org/pdf/2403.02418"},{"title":"Evaluating Loss Landscapes from a Topology Perspective","url":"https://arxiv.org/pdf/2411.09807"},{"title":"Visualizing high-dimensional loss landscapes with Hessian directions","url":"https://arxiv.org/pdf/2208.13219"}]

I found several recent research papers related to Hessian spectral analysis and loss landscape geometry. Here's what the search revealed:

## Recent Research on Hessian Spectral Analysis and Loss Landscapes (2024-2026)

**Spectral Analysis and Loss Landscape Geometry:**

The geometry of neural network loss landscapes through the Hessian matrix has been extensively studied, with random matrix theory and spectral analysis used to understand loss surface dynamics and optimization.

**Key Research Areas:**

1. **Hessian-Based Loss Landscape Visualization**: Analyzing geometric properties like local curvature can help understand neural network performance, with research proposing projections along Hessian directions associated with the largest and smallest principal curvatures.

2. **Generalization and Hessian Analysis**: Spectra of Hessian eigendecomposition are studied to show typical spectra exist across neural networks, allowing quantitative criteria for Hessian analysis to evaluate performance and assess generalization capabilities.

3. **Topological Approaches**: Research uses topological data analysis tools to characterize the topology of loss landscapes, computing Hessian-based metrics like largest eigenvalue, trace, and eigenvalue spectral density.

4. **Time-Dependent Hessian Evolution**: Recent analytical studies examine the evolution of the Hessian during gradient descent dynamics and relate transitions in its spectral properties to finding good minima.

However, the search results don't contain specific research on "step-level PRM" (Process Reward Models) combined with Hessian spectral analysis. You may want to refine your search with more specific terms if you're looking for research on reward model loss landscapes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c37e1c50-ec43-49cb-ae6d-5e3a67ac14e4",
  "isSidechain": false,
  "promptId": "18034a7d-47e3-4c01-b7f9-6c61bf20f18e",
  "type": "user",
  "uuid": "477d117a-73ca-4875-b2c9-57d2bfa32d12",
  "toolUseResult": {
    "query": "Hessian spectral analysis reward model loss landscape step level PRM geometry 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016QvN9xFKZBtP12cMoWitzW",
        "content": [
          {
            "title": "Unraveling the Hessian: A Key to Smooth Convergence in Loss Function Landscapes | Doklady Mathematics | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1134/S1064562424601987"
          },
          {
            "title": "Unraveling the Hessian: A Key to Smooth Convergence in Loss Function Landscapes",
            "url": "https://arxiv.org/html/2409.11995v1"
          },
          {
            "title": "Topological Exploration of High-Dimensional Empirical Risk Landscapes: general approach, and applications to phase retrieval",
            "url": "https://arxiv.org/pdf/2602.17779"
          },
          {
            "title": "Investigating generalization capabilities of neural networks by means of   loss landscapes and Hessian analysis",
            "url": "https://arxiv.org/pdf/2412.10146"
          },
          {
            "title": "The Role of the Time-Dependent Hessian in High-Dimensional Optimization",
            "url": "https://arxiv.org/pdf/2403.02418"
          },
          {
            "title": "Evaluating Loss Landscapes from a Topology Perspective",
            "url": "https://arxiv.org/pdf/2411.09807"
          },
          {
            "title": "Visualizing high-dimensional loss landscapes with Hessian directions",
            "url": "https://arxiv.org/pdf/2208.13219"
          }
        ]
      },
      "I found several recent research papers related to Hessian spectral analysis and loss landscape geometry. Here's what the search revealed:\n\n## Recent Research on Hessian Spectral Analysis and Loss Landscapes (2024-2026)\n\n**Spectral Analysis and Loss Landscape Geometry:**\n\nThe geometry of neural network loss landscapes through the Hessian matrix has been extensively studied, with random matrix theory and spectral analysis used to understand loss surface dynamics and optimization.\n\n**Key Research Areas:**\n\n1. **Hessian-Based Loss Landscape Visualization**: Analyzing geometric properties like local curvature can help understand neural network performance, with research proposing projections along Hessian directions associated with the largest and smallest principal curvatures.\n\n2. **Generalization and Hessian Analysis**: Spectra of Hessian eigendecomposition are studied to show typical spectra exist across neural networks, allowing quantitative criteria for Hessian analysis to evaluate performance and assess generalization capabilities.\n\n3. **Topological Approaches**: Research uses topological data analysis tools to characterize the topology of loss landscapes, computing Hessian-based metrics like largest eigenvalue, trace, and eigenvalue spectral density.\n\n4. **Time-Dependent Hessian Evolution**: Recent analytical studies examine the evolution of the Hessian during gradient descent dynamics and relate transitions in its spectral properties to finding good minima.\n\nHowever, the search results don't contain specific research on \"step-level PRM\" (Process Reward Models) combined with Hessian spectral analysis. You may want to refine your search with more specific terms if you're looking for research on reward model loss landscapes."
    ],
    "durationSeconds": 7.055206021000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c37e1c50-ec43-49cb-ae6d-5e3a67ac14e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T05:53:17.223Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MXsMac4Vp5L2UGSDEBJ6pp`</summary>

```json
{
  "query": "\"reward shaping\" \"reward as preference\" PAR bounded reward mitigate hacking RLHF 2025 2026 arxiv 2502.18770"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "477d117a-73ca-4875-b2c9-57d2bfa32d12",
  "isSidechain": false,
  "requestId": "req_011CbDJRf3Aar2aFsnkDkRLL",
  "type": "assistant",
  "uuid": "ed1a76e6-bf84-4a3b-93a2-bf51e6e9be18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013neXzFrkCUdwicLQ5fHcco",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 817,
      "cache_read_input_tokens": 27992,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 90,
          "cache_read_input_tokens": 27992,
          "cache_creation_input_tokens": 817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 817
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

_source line 39 · 2026-05-20T05:53:23.664Z_

<details><summary>↩ Tool result · `toolu_01MXsMac4Vp5L2UGSDEBJ6pp`</summary>

```text
Web search results for query: ""reward shaping" "reward as preference" PAR bounded reward mitigate hacking RLHF 2025 2026 arxiv 2502.18770"

Links: [{"title":"[2502.18770v1] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/abs/2502.18770v1"},{"title":"[2502.18770v2] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/abs/2502.18770v2"},{"title":"[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/abs/2502.18770"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/pdf/2502.18770"},{"title":"(PDF) Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://www.researchgate.net/publication/389392526_Reward_Shaping_to_Mitigate_Reward_Hacking_in_RLHF"},{"title":"Paper page - Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://huggingface.co/papers/2502.18770"},{"title":"[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://ar5iv.labs.arxiv.org/html/2502.18770"},{"title":"Mitigating Attention Hacking in Preference-Based Reward Modeling via Interaction Distillation","url":"https://arxiv.org/html/2508.02618v1"}]

I found the paper you're looking for. Here's what the research is about:

## Overview

Reinforcement Learning from Human Feedback (RLHF) is essential for aligning large language models (LLMs) with human values, but RLHF is susceptible to reward hacking, where the agent exploits flaws in the reward function rather than learning the intended behavior.

## Key Design Principles

The paper identifies three key design principles: (1) RL reward is ideally bounded, (2) RL benefits from rapid initial growth followed by gradual convergence, and (3) RL reward is best formulated as a function of centered reward.

## The PAR Method

The paper proposes Preference As Reward (PAR), a novel approach that leverages the latent preferences embedded within the reward model as the signal for reinforcement learning.

## Performance Results

On the AlpacaEval 2.0 benchmark, PAR achieves a win rate at least 5 percentage points higher than competing approaches. Additionally, PAR exhibits remarkable data efficiency, requiring only a single reference reward for optimal performance, and maintains robustness against reward hacking even after two full epochs of training.

The paper was posted on arXiv on February 26, 2025 (arxiv:2502.18770).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed1a76e6-bf84-4a3b-93a2-bf51e6e9be18",
  "isSidechain": false,
  "promptId": "18034a7d-47e3-4c01-b7f9-6c61bf20f18e",
  "type": "user",
  "uuid": "9f866639-88a0-4e3e-9143-43a468035f25",
  "toolUseResult": {
    "query": "\"reward shaping\" \"reward as preference\" PAR bounded reward mitigate hacking RLHF 2025 2026 arxiv 2502.18770",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JxJoEj6YhMJwYKByB79wWR",
        "content": [
          {
            "title": "[2502.18770v1] Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/abs/2502.18770v1"
          },
          {
            "title": "[2502.18770v2] Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/abs/2502.18770v2"
          },
          {
            "title": "[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/abs/2502.18770"
          },
          {
            "title": "Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/pdf/2502.18770"
          },
          {
            "title": "(PDF) Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://www.researchgate.net/publication/389392526_Reward_Shaping_to_Mitigate_Reward_Hacking_in_RLHF"
          },
          {
            "title": "Paper page - Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://huggingface.co/papers/2502.18770"
          },
          {
            "title": "[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://ar5iv.labs.arxiv.org/html/2502.18770"
          },
          {
            "title": "Mitigating Attention Hacking in Preference-Based Reward Modeling via Interaction Distillation",
            "url": "https://arxiv.org/html/2508.02618v1"
          }
        ]
      },
      "I found the paper you're looking for. Here's what the research is about:\n\n## Overview\n\nReinforcement Learning from Human Feedback (RLHF) is essential for aligning large language models (LLMs) with human values, but RLHF is susceptible to reward hacking, where the agent exploits flaws in the reward function rather than learning the intended behavior.\n\n## Key Design Principles\n\nThe paper identifies three key design principles: (1) RL reward is ideally bounded, (2) RL benefits from rapid initial growth followed by gradual convergence, and (3) RL reward is best formulated as a function of centered reward.\n\n## The PAR Method\n\nThe paper proposes Preference As Reward (PAR), a novel approach that leverages the latent preferences embedded within the reward model as the signal for reinforcement learning.\n\n## Performance Results\n\nOn the AlpacaEval 2.0 benchmark, PAR achieves a win rate at least 5 percentage points higher than competing approaches. Additionally, PAR exhibits remarkable data efficiency, requiring only a single reference reward for optimal performance, and maintains robustness against reward hacking even after two full epochs of training.\n\nThe paper was posted on arXiv on February 26, 2025 (arxiv:2502.18770)."
    ],
    "durationSeconds": 6.435936218999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ed1a76e6-bf84-4a3b-93a2-bf51e6e9be18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T05:53:26.132Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0148QgD8xreDrEq7xvfMd7ct`</summary>

```json
{
  "query": "conformal prediction reward model RLHF alignment calibration coverage guarantee 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f866639-88a0-4e3e-9143-43a468035f25",
  "isSidechain": false,
  "requestId": "req_011CbDJSSqEM3CurTaNunD3p",
  "type": "assistant",
  "uuid": "50b13b12-86bc-452c-8a2c-401556030c6e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VpdM9pxMmAFEqsHHpYGvrx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 889,
      "cache_read_input_tokens": 28809,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 889,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 28809,
          "cache_creation_input_tokens": 889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 889
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

_source line 41 · 2026-05-20T05:53:36.391Z_

<details><summary>↩ Tool result · `toolu_0148QgD8xreDrEq7xvfMd7ct`</summary>

```text
Web search results for query: "conformal prediction reward model RLHF alignment calibration coverage guarantee 2025 2026"

Links: [{"title":"Conformal Feedback Alignment: Quantifying Answer-Level Reliability for Robust LLM Alignment","url":"https://arxiv.org/html/2601.17329v1"},{"title":"Backward Conformal Prediction","url":"https://arxiv.org/pdf/2505.13732"},{"title":"Conformal Feedback Alignment: Quantifying Answer-Level Reliability for","url":"https://www.arxiv.org/pdf/2601.17329"},{"title":"[2601.17329] Conformal Feedback Alignment: Quantifying Answer-Level Reliability for Robust LLM Alignment","url":"https://arxiv.org/abs/2601.17329"},{"title":"Conformal Prediction Beyond the Horizon: Distribution-Free Inference for Policy Evaluation","url":"https://arxiv.org/pdf/2510.26026"},{"title":"Conformal prediction without knowledge of labeled calibration data","url":"https://arxiv.org/pdf/2509.10321"},{"title":"CoVeR: Conformal Calibration for Versatile and Reliable Autoregressive Next-Token Prediction","url":"https://arxiv.org/pdf/2509.04733"},{"title":"Towards Reliable Alignment: Uncertainty-aware RLHF","url":"https://arxiv.org/html/2410.23726v1"},{"title":"Adjusting Regression Models for Conditional Uncertainty Calibration","url":"https://arxiv.org/pdf/2409.17466"}]

Based on the search results, I found highly relevant recent research on this topic:

## Key Finding: Conformal Feedback Alignment (CFA)

The most directly relevant work is Conformal Feedback Alignment (CFA), a framework that grounds preference weighting in the statistical guarantees of Conformal Prediction (CP), which quantifies answer-level reliability by constructing conformal prediction sets with controllable coverage and aggregates these reliabilities into principled weights for both DPO- and PPO-style training.

This work addresses the problem that preference-based alignment like RLHF learns from pairwise preferences which are often noisy and inconsistent, with existing uncertainty-aware approaches weighting preferences but ignoring the reliability of the answers being compared.

Experiments across different datasets show that CFA improves alignment robustness and data efficiency, highlighting that modeling answer-side uncertainty complements preference-level weighting and yields more robust, data-efficient alignment. This paper was published in January 2026.

## Related Work

The search also revealed several complementary approaches to calibration and uncertainty in alignment:

- A conservative policy optimization method incorporating uncertainty measures derived from reward model training that rigorously demonstrates through theoretical analysis and experiments on LLMs that their risk-aware conservative policy scheme significantly reduces the likelihood of policy degradation.

- CoVER, a model-free decoding strategy within the conformal prediction framework that maintains compact search space while ensuring high coverage probability, with theoretical guarantees that asymptotically achieves a coverage rate of at least 1-α for any target level α.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50b13b12-86bc-452c-8a2c-401556030c6e",
  "isSidechain": false,
  "promptId": "18034a7d-47e3-4c01-b7f9-6c61bf20f18e",
  "type": "user",
  "uuid": "fcaf9826-c196-4cbb-97c4-70d05a2a0182",
  "toolUseResult": {
    "query": "conformal prediction reward model RLHF alignment calibration coverage guarantee 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013o43xVAe1KYTs1fGyHgXPh",
        "content": [
          {
            "title": "Conformal Feedback Alignment: Quantifying Answer-Level Reliability for Robust LLM Alignment",
            "url": "https://arxiv.org/html/2601.17329v1"
          },
          {
            "title": "Backward Conformal Prediction",
            "url": "https://arxiv.org/pdf/2505.13732"
          },
          {
            "title": "Conformal Feedback Alignment: Quantifying Answer-Level Reliability for",
            "url": "https://www.arxiv.org/pdf/2601.17329"
          },
          {
            "title": "[2601.17329] Conformal Feedback Alignment: Quantifying Answer-Level Reliability for Robust LLM Alignment",
            "url": "https://arxiv.org/abs/2601.17329"
          },
          {
            "title": "Conformal Prediction Beyond the Horizon: Distribution-Free Inference for Policy Evaluation",
            "url": "https://arxiv.org/pdf/2510.26026"
          },
          {
            "title": "Conformal prediction without knowledge of labeled calibration data",
            "url": "https://arxiv.org/pdf/2509.10321"
          },
          {
            "title": "CoVeR: Conformal Calibration for Versatile and Reliable Autoregressive Next-Token Prediction",
            "url": "https://arxiv.org/pdf/2509.04733"
          },
          {
            "title": "Towards Reliable Alignment: Uncertainty-aware RLHF",
            "url": "https://arxiv.org/html/2410.23726v1"
          },
          {
            "title": "Adjusting Regression Models for Conditional Uncertainty Calibration",
            "url": "https://arxiv.org/pdf/2409.17466"
          }
        ]
      },
      "Based on the search results, I found highly relevant recent research on this topic:\n\n## Key Finding: Conformal Feedback Alignment (CFA)\n\nThe most directly relevant work is Conformal Feedback Alignment (CFA), a framework that grounds preference weighting in the statistical guarantees of Conformal Prediction (CP), which quantifies answer-level reliability by constructing conformal prediction sets with controllable coverage and aggregates these reliabilities into principled weights for both DPO- and PPO-style training.\n\nThis work addresses the problem that preference-based alignment like RLHF learns from pairwise preferences which are often noisy and inconsistent, with existing uncertainty-aware approaches weighting preferences but ignoring the reliability of the answers being compared.\n\nExperiments across different datasets show that CFA improves alignment robustness and data efficiency, highlighting that modeling answer-side uncertainty complements preference-level weighting and yields more robust, data-efficient alignment. This paper was published in January 2026.\n\n## Related Work\n\nThe search also revealed several complementary approaches to calibration and uncertainty in alignment:\n\n- A conservative policy optimization method incorporating uncertainty measures derived from reward model training that rigorously demonstrates through theoretical analysis and experiments on LLMs that their risk-aware conservative policy scheme significantly reduces the likelihood of policy degradation.\n\n- CoVER, a model-free decoding strategy within the conformal prediction framework that maintains compact search space while ensuring high coverage probability, with theoretical guarantees that asymptotically achieves a coverage rate of at least 1-α for any target level α."
    ],
    "durationSeconds": 10.255107768000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "50b13b12-86bc-452c-8a2c-401556030c6e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T05:53:39.414Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MauX7TfU3SqmxwM6K9xsw3`</summary>

```json
{
  "query": "CKA representation similarity causal isolation calibration fine-tuning post-hoc 2025 2026 neural network"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcaf9826-c196-4cbb-97c4-70d05a2a0182",
  "isSidechain": false,
  "requestId": "req_011CbDJTPGCEAaPiRoeZedVL",
  "type": "assistant",
  "uuid": "538aa2e6-117b-49c7-ba0e-b787a50f8de3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vs5YrtyWwKGQHMcPUEv1aT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 843,
      "cache_read_input_tokens": 29698,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 843,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 29698,
          "cache_creation_input_tokens": 843,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 843
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

_source line 43 · 2026-05-20T05:53:48.750Z_

<details><summary>↩ Tool result · `toolu_01MauX7TfU3SqmxwM6K9xsw3`</summary>

```text
Web search results for query: "CKA representation similarity causal isolation calibration fine-tuning post-hoc 2025 2026 neural network"

Links: [{"title":"Fine-Tuned Transformers Show Clusters of Similar Representations Across   Layers","url":"https://arxiv.org/pdf/2109.08406"},{"title":"Centered Kernel Alignment (CKA) Overview","url":"https://www.emergentmind.com/topics/centered-kernel-alignment-cka"},{"title":"Estimating Neural Representation Alignment","url":"https://arxiv.org/pdf/2502.15104"},{"title":"Centered Kernel Alignment (CKA) Similarity","url":"https://www.emergentmind.com/topics/centered-kernel-alignment-cka-similarity"},{"title":"[1905.00414] Similarity of Neural Network Representations Revisited","url":"https://arxiv.org/abs/1905.00414"},{"title":"GitHub - RistoAle97/centered-kernel-alignment: CKA (Centered Kernel Alignment) implemented in PyTorch · GitHub","url":"https://github.com/RistoAle97/centered-kernel-alignment"},{"title":"Similarity of Neural Network Representations Revisited","url":"https://arxiv.org/pdf/1905.00414"},{"title":"Pre-trained Models Succeed in Medical Imaging with Representation Similarity Degradation","url":"https://arxiv.org/html/2503.07958v1"},{"title":"Deconfounded Representation Similarity for Comparison of Neural Networks","url":"https://arxiv.org/pdf/2202.00095"}]

Based on the search results, I found relevant research on CKA (Centered Kernel Alignment) and its application to neural networks, fine-tuning, and representation analysis:

## Key Findings:

**CKA for Representation Analysis:**
CKA (centered kernel alignment) is used to measure representation similarity and analyze how learned representations change via fine-tuning. CKA is invariant to both orthogonal transformation and isotropic scaling of the compared representations, making it ideal for measuring the similarity of neural network representations.

**Fine-Tuning Studies:**
Researchers use CKA to analyze how learned representations change via fine-tuning, and can compare the similarity of representations between different layers of the same model or even different models. Recent work from 2025 explores this further: Research tracks the variations of CKA and ECE (Expected Calibration Error) during fine-tuning, and visualizes the similarity space to quantify and predict model variations.

**Calibration and Limitations:**
High CKA does not guarantee functionally similar or transferable features, nor does low CKA conclusively reflect divergent model behavior, and complementary diagnostics are advised.

**Recent Advances:**
Recent research has introduced "deconfounded" approaches to CKA, as similarity metrics are confounded by the population structure of data items in the input space, and researchers have proposed a fix using covariate adjustment regression.

The search results show active research in this area, particularly regarding the reliability and interpretation of CKA for neural network analysis in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "538aa2e6-117b-49c7-ba0e-b787a50f8de3",
  "isSidechain": false,
  "promptId": "18034a7d-47e3-4c01-b7f9-6c61bf20f18e",
  "type": "user",
  "uuid": "6ec200e6-5374-40c2-a7e0-bfe64ff4d6f4",
  "toolUseResult": {
    "query": "CKA representation similarity causal isolation calibration fine-tuning post-hoc 2025 2026 neural network",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RCvPWuoXLnDBxzVeB8tSn9",
        "content": [
          {
            "title": "Fine-Tuned Transformers Show Clusters of Similar Representations Across   Layers",
            "url": "https://arxiv.org/pdf/2109.08406"
          },
          {
            "title": "Centered Kernel Alignment (CKA) Overview",
            "url": "https://www.emergentmind.com/topics/centered-kernel-alignment-cka"
          },
          {
            "title": "Estimating Neural Representation Alignment",
            "url": "https://arxiv.org/pdf/2502.15104"
          },
          {
            "title": "Centered Kernel Alignment (CKA) Similarity",
            "url": "https://www.emergentmind.com/topics/centered-kernel-alignment-cka-similarity"
          },
          {
            "title": "[1905.00414] Similarity of Neural Network Representations Revisited",
            "url": "https://arxiv.org/abs/1905.00414"
          },
          {
            "title": "GitHub - RistoAle97/centered-kernel-alignment: CKA (Centered Kernel Alignment) implemented in PyTorch · GitHub",
            "url": "https://github.com/RistoAle97/centered-kernel-alignment"
          },
          {
            "title": "Similarity of Neural Network Representations Revisited",
            "url": "https://arxiv.org/pdf/1905.00414"
          },
          {
            "title": "Pre-trained Models Succeed in Medical Imaging with Representation Similarity Degradation",
            "url": "https://arxiv.org/html/2503.07958v1"
          },
          {
            "title": "Deconfounded Representation Similarity for Comparison of Neural Networks",
            "url": "https://arxiv.org/pdf/2202.00095"
          }
        ]
      },
      "Based on the search results, I found relevant research on CKA (Centered Kernel Alignment) and its application to neural networks, fine-tuning, and representation analysis:\n\n## Key Findings:\n\n**CKA for Representation Analysis:**\nCKA (centered kernel alignment) is used to measure representation similarity and analyze how learned representations change via fine-tuning. CKA is invariant to both orthogonal transformation and isotropic scaling of the compared representations, making it ideal for measuring the similarity of neural network representations.\n\n**Fine-Tuning Studies:**\nResearchers use CKA to analyze how learned representations change via fine-tuning, and can compare the similarity of representations between different layers of the same model or even different models. Recent work from 2025 explores this further: Research tracks the variations of CKA and ECE (Expected Calibration Error) during fine-tuning, and visualizes the similarity space to quantify and predict model variations.\n\n**Calibration and Limitations:**\nHigh CKA does not guarantee functionally similar or transferable features, nor does low CKA conclusively reflect divergent model behavior, and complementary diagnostics are advised.\n\n**Recent Advances:**\nRecent research has introduced \"deconfounded\" approaches to CKA, as similarity metrics are confounded by the population structure of data items in the input space, and researchers have proposed a fix using covariate adjustment regression.\n\nThe search results show active research in this area, particularly regarding the reliability and interpretation of CKA for neural network analysis in 2025-2026."
    ],
    "durationSeconds": 9.329755241999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "538aa2e6-117b-49c7-ba0e-b787a50f8de3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-20T05:54:41.793Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough background research. Let me synthesize my findings and provide a thorough analysis of this proposal as the "发掘 agent."

Key findings from my research:

1. **PRM Calibration (Thread 1)**: Park et al. (NeurIPS 2025) showed PRMs are poorly calibrated (overestimate success probabilities), proposed quantile regression calibration. Distributional PRMs (May 2026) use conditional optimal transport for better calibration. Neither tests robustness.

2. **PRM Hackability (Thread 2)**: Tiwari et al. 
(March 2026) demonstrated that PRMs can be manipulated to show near-perfect rewards despite <4% actual accuracy, while APRM applies adversarial training to improve robustness.

3. **Reward Hacking Defenses**: Several mitigation strategies have emerged—gradient regularization, pessimistic reward approaches, reward shaping, and causal reward adjustment using sparse autoencoders. The causal approach is particularly compelling because it intervenes directly on the PRM's internal representations rather than just the outputs.

4. **Causal Approaches**: CROME and CausalRM apply causal frameworks to reward modeling, though they primarily target outcome-level RMs rather than process-level ones.

5. Examining confidence levels and limitations...

6. **Critical Gap**: The CRA paper (arXiv:2508.04216) is highly relevant and poses a novelty risk—it already uses causal intervention with sparse autoencoders and backdoor adjustment on PRM representations to prevent reward hacking, and it's not mentioned in the proposal.

Looking at the proposal's strengths now: the connection between PRM calibration and vulnerability to hacking is genuinely novel, the causal isolation methodology with post-hoc versus fine-tuning comparisons and matched controls is well-structured, and extending Hessian analysis to the step level goes beyond prior outcome-level work.

But there are some concerns. Beyond CRA, the proposal doesn't fully engage with PET (arXiv:2505.20556), which proposes a complete pessimistic reward model fine-tuning approach rather than just mentioning it in passing. There's also the broader question of how this relates to reward shaping and other mitigation strategies.

The causal isolation design is genuinely clever, but I'm noticing some potential vulnerabilities. Post-hoc calibration might just work by compressing the reward signal—making rewards less extreme through temperature scaling—which wouldn't really be about calibration at all. And the matched representation control is conceptually sound but practically tricky to execute without accidentally introducing calibration effects. There's also a simpler threat: basic reward clipping or scaling might achieve the same robustness without needing all this machinery.

Looking at the CGSP formula with the inverse ECE term, dividing by √c_t creates numerical instability when the model is already well-calibrated, and ECE itself isn't a reliable estimator with limited data. The CRA paper takes a complementary angle by identifying confounding semantic features in PRM representations, which is worth acknowledging as a different approach to the same problem.

The key novelty opportunities are distinguishing whether calibration's effect on hackability comes from genuine probability alignment or just reward compression—I should design experiments comparing calibrated models against ones with artificially clipped rewards to isolate the true mechanism. More importantly, the calibration drift detector during RL training is the most practically valuable contribution and deserves more emphasis, since it essentially functions as a real-time reward hacking detector.

I also need to address the CRA paper (arXiv:2508.04216) which tackles PRM reward hacking through feature-level interventions rather than calibration, so I should clearly differentiate the approaches.

But stepping back, I'm questioning whether the core logic actually holds—does calibration really prevent hacking? A well-calibrated PRM should avoid systematically overscoring wrong answers by definition, but the critical issue is whether that calibration generalizes to adversarial examples or only holds in-distribution.

The proposal does touch on this with the Calibration Drift Detector monitoring ECE on policy rollouts, but the claim needs tighter framing: calibration predicts hackability because well-calibrated models have learned more robust representations that generalize better, resulting in flatter reward surfaces that resist exploitation. This actually ties back to the Ackermann et al. finding on flatness and reward robustness, and extending that to step-level is a solid contribution.

Now I'm noting the venue mismatch—the proposal targets ICLR/AAAI/AISTATS 2027 while the user wants EMNLP 2026 evaluation—but I should focus on the academic rigor regardless. Looking at the core novelty gaps: the reward compression versus true calibration distinction needs clearer causal grounding, the CRA paper is a critical missing reference, the Calibration Drift Detector should be positioned more centrally, and the step-level compositional geometry claim is interesting but needs sharper differentiation from Ackermann et al. I'm settling on a rating that acknowledges genuine novelty with four to five specific refinement points.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ec200e6-5374-40c2-a7e0-bfe64ff4d6f4",
  "isSidechain": false,
  "requestId": "req_011CbDJUJ8QYoEMLFYbY5M7Z",
  "type": "assistant",
  "uuid": "ed95c329-89c7-462c-9324-1b7e7e950f9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3u2JfpQURzsAusnVgW2ea",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 30541,
      "output_tokens": 6022,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 852,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6022,
          "cache_read_input_tokens": 30541,
          "cache_creation_input_tokens": 852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 852
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

_source line 45 · 2026-05-20T05:56:00.760Z_

Now I have sufficient research to provide a thorough assessment. Let me compile my analysis.

---

【状态】: 有发掘空间

【前置调研发现】

- **Causal Reward Adjustment (CRA, arXiv:2508.04216, Aug 2025)**: 直接用因果推断（sparse autoencoder + backdoor adjustment）在 PRM 内部表征上干预，缓解 reward hacking。**本 proposal 未引用，但高度相关**——同样是因果角度解决 PRM reward hacking，只是从 confounding features 而非 calibration 切入。
- **Robust Reward Modeling via Causal Rubrics / CROME (arXiv:2506.16507, NeurIPS 2025)**: 用显式因果模型分离 prompt-driven preferences 和 spurious artifacts，在 RewardBench 上提升 5.4%。证明因果分解能增强 RM 鲁棒性这条路径已有先例。
- **Learning a Pessimistic Reward Model / PET (arXiv:2505.20556, May 2025)**: 通过 pessimistic fine-tuning 学习悲观 reward model，不需要 KL regularization 即可防 hacking。这是 CGSP 最直接的方法层竞争者。
- **Reward Shaping / PAR (arXiv:2502.18770, Feb 2025)**: 提出 bounded reward + centered reward 设计原则缓解 hacking，win rate 提升 5pp。提供了一种简单得多的 reward 变换方案。
- **Conformal Feedback Alignment / CFA (arXiv:2601.17329, Jan 2026)**: 将 conformal prediction 用于 RLHF 偏好权重校准，但仅在 answer level，未涉及 step-level PRM。
- **Distributional PRMs (arXiv:2605.06785, May 2026)**: 用 conditional optimal transport 实现 calibrated quantile functions，但完全未测试鲁棒性。
- **Tiwari et al. (arXiv:2603.06621, Mar 2026)**: PRM 可被 hack 到 reward >0.9 而准确率 <4%，43% reward gains 来自 stylistic shortcuts。

- **调研总结**: 当前领域有两个并行但独立的推进方向：(1) 因果/结构化方法增强 reward model 鲁棒性（CRA、CROME、CausalRM），(2) pessimism/uncertainty 方法约束 RL 优化（PET、Caution、PAR）。将 calibration 质量作为 hackability 的因果决定因素这一特定桥梁确实没人搭建过，但 CRA 已经从因果角度切入 PRM hacking 问题，与本 proposal 的因果 claim 存在交叉。

---

【发掘点 1】
- 维度: trivial alternative 威胁 / 前提假设质疑
- 内容: **Proposal 的因果 claim 面临一个关键 confound："calibration = reward compression" 混淆。** Post-hoc calibration（特别是 temperature scaling）本质上是对 reward logits 做 rescaling，使输出分布更温和、更不极端。如果 temperature scaling 降低了 hackability，原因可能并非"校准使概率估计更准确"，而仅仅是"reward 信号变得更平坦，gradient attack 的 reward gradient 变小了"。这是一个 trivial mechanism。建议在 Component B 中增加一个 **reward range-matched control**：对 uncalibrated PRM 施加简单的线性缩放或 sigmoid clipping，使其 reward range 与 calibrated PRM 匹配，但不改善 calibration（ECE 不变或变差），然后测试 hackability。如果 hackability 仍然下降，说明机制是 reward compression 而非 calibration per se；如果只有真正改善 calibration 的方法才降低 hackability，因果 claim 才成立。**不解决这个 confound，审稿人一定会提出此质疑，而且这会直接动摇核心 claim 的说服力。**
- 价值: 直接强化核心因果 claim 的逻辑严密性（命中 Novelty + Significance），将 proposal 从"calibration 和 hackability 相关"提升到"calibration 因果性地决定 hackability，排除 trivial 解释"。
- 调研依据: Ackermann et al. (arXiv:2602.18037) 已证明 flatness 与 reward accuracy retention 相关；PAR (arXiv:2502.18770) 表明简单的 bounded/centered reward 变换即可缓解 hacking。两者共同暗示"让 reward 不那么极端"本身就可能是一个有效但 trivial 的防御机制。

【发掘点 2】
- 维度: related work 差异化
- 内容: **CRA (Causal Reward Adjustment, arXiv:2508.04216) 是一个重大遗漏，可能威胁 novelty claim。** CRA 同样从因果角度解决 PRM reward hacking——用 sparse autoencoder 提取 PRM 内部表征的可解释特征，然后通过 backdoor adjustment 消除 confounding semantic features 的影响。虽然 CRA 的因果干预对象是"features"而非"calibration"，但审稿人很可能问："你们的 calibration-based causal story 和 CRA 的 feature-based causal story 是什么关系？有没有可能 calibration 改善 hackability 的真正机制就是消除了 confounding features（CRA 已经做了的事）？" Proposal 必须 (a) 引用并详细讨论 CRA，(b) 明确两者的因果干预点不同（CRA 干预 representation space，CGSP 干预 output space），(c) 最好设计实验测试两种方法是否互补（e.g., CRA + calibration 是否比单独任何一个更好）。
- 价值: 消除审稿人发现高度相关未引用工作后直接 reject 的风险，同时将 proposal 定位在一个更丰富的"因果鲁棒 reward modeling"大图景中（命中 Related Work 差异化 + Novelty）。
- 调研依据: CRA (arXiv:2508.04216) 和 CROME (arXiv:2506.16507) 表明因果方法增强 RM 鲁棒性已有成熟先例，proposal 必须在这个 landscape 中定位自己。

【发掘点 3】
- 维度: significance 提升 / 核心 claim 强化
- 内容: **Calibration Drift Detector 是全文潜在最有影响力的贡献，但当前被埋在 CGSP 的子组件里，严重低估了其独立价值。** 目前已有的 reward hacking detection 方法（gradient fingerprints, arXiv:2604.16242 等）需要事后分析或对抗性评估。而 Calibration Drift Detector 本质上是一个**zero-cost, real-time, model-agnostic 的 reward hacking 预警系统**——在 RL training 过程中实时监测 ECE drift，当 policy distribution shift 导致 PRM 失准时自动触发警报。这比任何事后检测方法都更实用。建议将 Calibration Drift Detector **提升为一个独立贡献（Component E）**，而非 CGSP 的附属组件：(1) 给出明确的理论动机：为什么 calibration drift 是 reward hacking 的充分早期信号？(2) 在 RL training 过程中系统性地测量 ECE drift 与 reward-accuracy divergence 的时序关系——如果 ECE drift 稳定地先于 reward hacking 出现，这本身就是一个重要的 empirical finding。(3) 可独立于 CGSP 使用——任何 PRM-based RL pipeline 都可以插入这个 detector。
- 价值: 将一个技术组件升级为独立贡献，增加论文的"贡献密度"和实践影响力。如果 ECE drift 确实是 reward hacking 的可靠 leading indicator，这个发现的 significance 甚至可能超过 CGSP 本身（命中 Significance）。
- 调研依据: Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242) 是当前最接近的检测方法，但需要 gradient 计算；本 proposal 的 drift detector 基于 ECE 统计量，计算成本更低，更易部署。

【发掘点 4】
- 维度: novelty 锐化
- 内容: **Step-level compositional geometry 的 novelty claim 需要更锐利地表述"为什么 outcome-level 分析不够"。** 当前 proposal 正确指出 Ackermann et al. 只分析 outcome-level gradient norms，但仅说"inapplicable to step-level PRM geometry"还不够——需要给出一个具体的、直觉上 compelling 的例子说明 **step-level 分析会揭示 outcome-level 分析遗漏的现象**。例如：一个 PRM 可能在大多数 step 上是 flat 的（难以 hack），但在某个关键 step（如最终答案步）上有一个 sharp peak，使得 adversary 只需在那一步 inject noise 就能获得高 reward。Outcome-level 分析会将这种"局部 sharp + 整体 flat"的模式平均掉，产生错误的安全感。如果实验中确实发现这种 step-heterogeneous sharpness pattern，这将是一个非常有说服力的、仅 step-level 分析能捕捉到的 finding，直接证明 Component C 的必要性。
- 价值: 将 Component C 从"Ackermann et al. 的自然扩展"提升为"揭示了 outcome-level 分析的盲区"，显著增强 novelty 感知（命中 Novelty）。
- 调研依据: Ackermann et al. (arXiv:2602.18037) 的 Propositions 3.3-3.4 确实假设单一标量 reward R(s,a)，proposal 对此的批评是准确的。但需要从"不适用"升级到"会遗漏具体什么现象"才能让 novelty claim 真正锐利。

【发掘点 5】
- 维度: 前提假设质疑
- 内容: **核心逻辑链条中有一个未经验证的关键假设：calibration 在 distribution shift 下是否仍有意义？** Calibration 通常在 held-out test set（与训练分布相同）上衡量。但 reward hacking 的核心场景恰恰是 OOD——adversarial attacks 和 RL policy shift 产生的轨迹不在 calibration 数据的分布内。一个 PRM 可能在 MATH-500 上完美 calibrated，但面对 RL-optimized trajectories 时 calibration 完全崩溃。如果 calibration 只在 in-distribution 有效，那么"calibration 决定 hackability"这个因果 claim 的适用范围就非常有限——它只能解释 mild overoptimization（小幅度的 distribution shift），但不能解释 severe hacking（大幅度的 OOD exploitation）。建议 proposal 明确讨论这个 scope limitation，并在 Component A 中增加一个分析维度：**测量 hackability 与 OOD calibration（而非 in-distribution calibration）的相关性**。这实际上可以将 Calibration Drift Detector 的动机嵌入更早的实验设计中——drift 的速度和幅度本身就是衡量 calibration 在 OOD 下脆弱性的指标。
- 价值: 预防审稿人"your calibration is only measured in-distribution, but hacking is OOD by definition"的致命攻击，同时使 proposal 的理论框架更加自洽——将 in-distribution calibration、OOD calibration degradation、和 Calibration Drift Detector 串联成一个连贯的故事线（命中 Novelty + Significance）。
- 调研依据: 基于领域整体趋势判断——calibration 的 distribution sensitivity 是 calibration 文献中的已知问题（Guo et al. 2017 原始 temperature scaling 论文就强调了 in-distribution 假设），但 PRM 场景下这个问题因 RL training 的 non-stationarity 被极度放大。

---

Sources:
- [Know What You Don't Know: Uncertainty Calibration of PRMs (NeurIPS 2025)](https://arxiv.org/abs/2506.09338)
- [Distributional Process Reward Models (May 2026)](https://arxiv.org/abs/2605.06785)
- [Reward Under Attack: PRM Hackability (March 2026)](https://arxiv.org/abs/2603.06621)
- [Gradient Regularization Prevents Reward Hacking (Feb 2026)](https://arxiv.org/abs/2602.18037)
- [Causal Reward Adjustment via Backdoor Correction (Aug 2025)](https://arxiv.org/abs/2508.04216)
- [Robust Reward Modeling via Causal Rubrics / CROME](https://arxiv.org/abs/2506.16507)
- [Learning a Pessimistic Reward Model / PET (May 2025)](https://arxiv.org/abs/2505.20556)
- [Reward Shaping / PAR (Feb 2025)](https://arxiv.org/abs/2502.18770)
- [Conformal Feedback Alignment (Jan 2026)](https://arxiv.org/abs/2601.17329)
- [From Curiosity to Caution / Pessimism for BoN (April 2026)](https://arxiv.org/abs/2604.04648)
- [Detecting and Suppressing Reward Hacking with Gradient Fingerprints (April 2026)](https://arxiv.org/abs/2604.16242)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed95c329-89c7-462c-9324-1b7e7e950f9f",
  "isSidechain": false,
  "requestId": "req_011CbDJUJ8QYoEMLFYbY5M7Z",
  "type": "assistant",
  "uuid": "aa95f3cd-2a84-4254-9f71-33ecf75af6ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3u2JfpQURzsAusnVgW2ea",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 30541,
      "output_tokens": 6022,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 852,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6022,
          "cache_read_input_tokens": 30541,
          "cache_creation_input_tokens": 852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 852
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

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense  ## Description We present the first causally rigorous study connecting P…",
  "leafUuid": "aa95f3cd-2a84-4254-9f71-33ecf75af6ac",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Calibration quality and PRM reward hacking resistance",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense  ## Description We present the first causally rigorous study connecting P…",
  "leafUuid": "aa95f3cd-2a84-4254-9f71-33ecf75af6ac",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "Calibration quality and PRM reward hacking resistance",
  "sessionId": "bed47c8a-6f94-4623-a6b5-5269f76a5abe"
}
```

---
