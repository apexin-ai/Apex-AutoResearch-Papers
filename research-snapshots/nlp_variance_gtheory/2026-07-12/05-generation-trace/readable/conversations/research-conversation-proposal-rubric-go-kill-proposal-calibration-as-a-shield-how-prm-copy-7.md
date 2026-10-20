# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Calibration as a Shield: How PRM 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/9aca3988-3e9a-4c46-b710-d33cd95d12d4.jsonl`
- **Structured JSON:** [`46fe13947896811a2c0d.json`](../../sessions/46/46fe13947896811a2c0d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T21:04:56.807Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T21:04:56.807Z",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense\n\n## Description\nWe present the first causally rigorous study connecting PRM calibration quality to adversarial exploitability, and propose Calibration-Gated Step-Level Pessimism (CGSP), a novel defense that transforms calibrated uncertainty into adaptive reward hacking resistance during RL training. Our work bridges two mature but isolated research threads (PRM calibration and PRM hackability) through four contributions. First, an expanded correlation study across 48 configurations (8 PRMs × 6 calibration methods) provides sufficient statistical power (n=48, detecting r≥0.29 at p<0.05) to establish whether calibration quality predicts hackability metrics under gradient attacks, RL-induced hacking (GRPO on AIME), and BoN overoptimization (MATH-500), stratified by problem difficulty. Second, causal isolation experiments separate calibration's true effect from representation change artifacts: we compare post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) that provably preserve model representations against fine-tuning-based methods, with CKA verification and matched-representation-change controls. Third, step-level Hessian spectral analysis goes beyond Ackermann et al.'s outcome-level gradient norm analysis (which applies only to single-scalar reward models) to reveal how calibration affects the multi-reward compositional geometry of PRMs — analyzing how step-level flatness compounds across trajectories. Fourth, CGSP replaces raw PRM rewards during RL training with r̃_t = μ_t − α·σ_t/√c_t, where calibrated uncertainty σ_t and calibration quality c_t adaptively modulate pessimism per-step — trusted when calibration is tight, pessimistic when uncertainty is high — with a Calibration Drift Detector that monitors ECE on current-policy rollouts to flag distribution-shift-induced reward hacking in real time. CGSP differs from existing defenses (Caution uses prediction error, PET uses global pessimism, ensemble methods are uncalibrated) by being step-level, calibration-grounded, and adaptive. We evaluate CGSP against 5 baselines (uncalibrated GRPO, APRM, Caution, ensemble-min, gradient regularization) on MATH-500 and AIME, measuring both reward-accuracy alignment and downstream task accuracy.\n\n## Core Problem\nPRM calibration research and PRM hackability research are entirely separate threads with zero cross-citation — but the deeper problem is that we lack both (a) causal evidence for whether calibration actually determines hackability (vs. being merely correlated), and (b) a principled, step-level defense mechanism that leverages calibrated uncertainty to prevent reward hacking during RL training. Existing ad-hoc defenses (adversarial training, gradient regularization, pessimistic BoN) operate at the outcome level without exploiting the unique step-level structure of PRMs.\n\n## Opportunity\nThree recent developments create a uniquely favorable moment. First, Distributional PRMs (arXiv:2605.06785, May 2026) achieve calibrated step-level uncertainty via conditional optimal transport but never test robustness. Second, Tiwari et al. (arXiv:2603.06621, March 2026) demonstrate that PRMs are catastrophically hackable — near-perfect PRM rewards with <4% actual accuracy — but propose no calibration-based defense. Third, the causal isolation toolkit is mature: post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) modify only the output mapping without changing model representations, enabling controlled experiments that separate calibration effects from representation effects. No existing paper bridges these threads. Ackermann et al.'s gradient regularization work (arXiv:2602.18037) operates exclusively on outcome-level reward models with single-scalar rewards, never touching step-level PRM geometry. The CoT Entropy paper (arXiv:2502.11250) named this connection as future work 16 months ago with no follow-up. The window for a definitive, causally rigorous study is open but narrowing.\n\n## Related Work / Landscape\nTwo parallel research threads have developed with zero cross-citation. Thread 1 (PRM Calibration): Park et al. (arXiv:2506.09338, NeurIPS 2025) demonstrate PRMs systematically overestimate success probabilities on hard problems, proposing quantile regression calibration. Distributional PRMs (arXiv:2605.06785, May 2026) use conditional optimal transport for calibrated monotone quantile functions, improving BoN on MATH-500 and AIME. Neither paper tests robustness. Thread 2 (PRM Hackability): Tiwari et al. (arXiv:2603.06621) show gradient attacks inflate PRM rewards 4× and RL achieves near-perfect PRM rewards with <4% accuracy, with 43% of reward gains from stylistic shortcuts. APRM (arXiv:2511.22888) uses adversarial training for +3.4pp robustness. Thread 3 (Adjacent but distinct): Ackermann et al. (arXiv:2602.18037) prove reward surface flatness correlates with accuracy retention for outcome-level RMs, but work exclusively with single-scalar rewards, analyze only gradient norms (no Hessian spectra), and never consider step-level reward models. Their theoretical framework (Propositions 3.3-3.4) assumes a single reward function R(s,a) over complete responses — inapplicable to step-level PRM geometry where T coupled reward surfaces {R_1,...,R_T} interact compositionally. InferenceTimePessimism (arXiv:2506.19248) and Caution (arXiv:2604.04648) apply pessimism for BoN but use uncalibrated uncertainty proxies (prediction error, hedging), not calibrated probabilities. URM (arXiv:2410.00847) decomposes uncertainty into aleatoric/epistemic for outcome-level RMs but not PRMs. Bayesian reward models (arXiv:2402.13210) use Laplace approximation on LoRA weights. Conformal prediction has been applied to RLHF feedback alignment (arXiv:2601.17329) but never to PRM defense. No paper establishes a causal link between calibration quality and hackability, and no paper proposes using calibrated step-level PRM uncertainty as a defense during RL training.\n\n## Approach\nThe study has four components: (A) Expanded Correlation Study, (B) Causal Isolation Experiments, (C) Step-Level Mechanistic Analysis, and (D) Calibration-Gated Step-Level Pessimism (CGSP) defense.\n\n**Component A — Expanded Correlation Study (n≥24 configurations):** Apply 6 calibration methods across 2 tiers to 8 open-source PRMs. Tier 1 (post-hoc, representation-preserving): temperature scaling, Platt scaling, isotonic regression. Tier 2 (model-modifying): quantile regression fine-tuning, conditional optimal transport, Venn-Abers predictors. The 8 PRMs span discriminative (Qwen2.5-Math-PRM-7B, Qwen2.5-Math-PRM-72B, Skywork-o1-Open-PRM-7B, RLHFlow-Llama3.1-8B-PRM, Math-Shepherd-7B, OpenR-Math-psa-7B), generative (GenPRM-7B), and implicit (EurusPRM-Stage2) architectures. Each of the 48 PRM×calibration configurations is subjected to three attack tiers: (i) gradient-based reward inflation following Tiwari et al., (ii) RL-induced reward hacking via GRPO on AIME, and (iii) BoN overoptimization at N∈{1,4,16,64,256} on MATH-500. Compute rank correlations (Spearman ρ, Kendall τ) between calibration metrics (ECE, Brier score, quantile coverage, reliability diagram sharpness) and hackability metrics (reward-accuracy divergence, attack success rate, BoN degradation onset N*). Stratify analysis by problem difficulty (MATH levels 1-5, AMC vs. AIME) to test whether calibration is more protective on hard problems where PRMs are known to be overconfident.\n\n**Component B — Causal Isolation Experiments:** This is the methodological core addressing the reviewer's causation concern. Design: (B1) Post-hoc calibration control: Apply temperature scaling, Platt scaling, and isotonic regression — which provably modify only the output mapping, not internal representations — and measure hackability change. If hackability decreases under post-hoc calibration alone, this establishes that calibration per se (not representation change) causally affects hackability. (B2) Representation change verification: For fine-tuning-based calibration methods (quantile regression, COT), measure representation change at every transformer layer using Centered Kernel Alignment (CKA) between the base PRM and calibrated PRM. (B3) Matched representation change control: Fine-tune PRMs on an auxiliary task (e.g., next-token prediction on math text) that produces CKA-matched representation changes but does NOT improve calibration. If only calibration-improving fine-tuning reduces hackability (not the CKA-matched control), the causal role of calibration is confirmed. (B4) Conformal prediction as the cleanest test: Apply split-conformal prediction to PRM step scores, providing distribution-free coverage guarantees with zero model modification. Test whether conformal-calibrated PRMs resist hacking better than uncalibrated ones.\n\n**Component C — Step-Level Mechanistic Analysis (differentiating from Ackermann et al.):** Unlike Ackermann et al., who analyze only outcome-level gradient norms and max-perturbation sharpness, we perform Hessian spectral analysis at the step level — computing top-k eigenvalues and spectral density of the step-level reward Hessian ∂²R_t/∂h² (where h is the hidden representation at step t). Key questions: (i) Do calibrated PRMs have flatter step-level reward surfaces (lower top Hessian eigenvalue)? (ii) Does flatness vary by step position (early reasoning steps vs. final answer steps)? (iii) Do hackable reward peaks correspond to isolated large Hessian eigenvalues (sharp directions) that gradient attacks exploit? This extends Ackermann et al.'s framework from single-reward geometry to multi-reward compositional geometry: we analyze how step-level flatness/sharpness compounds across a T-step trajectory to determine outcome-level hackability.\n\n**Component D — Calibration-Gated Step-Level Pessimism (CGSP) Defense:** This transforms the paper from measurement to method. CGSP operates during RL training (GRPO/PPO) by replacing raw PRM step rewards with calibration-modulated rewards: r̃_t = μ_t − α · σ_t / √(c_t), where μ_t is the calibrated step reward mean, σ_t is the calibrated uncertainty (from quantile width or conformal interval), c_t is a calibration quality score (inverse ECE computed on a rolling buffer), and α is a pessimism strength hyperparameter. When calibration is high (small σ_t, high c_t), the reward is trusted; when calibration is low (large σ_t, low c_t), pessimism dominates. This differs from existing pessimism (Caution uses prediction error, PET uses global pessimistic fine-tuning, InferenceTimePessimism uses hedging) because CGSP is (i) step-level, (ii) grounded in calibrated probabilities rather than heuristic proxies, and (iii) adaptive — the pessimism automatically strengthens in distribution-shift regions where the PRM becomes miscalibrated. Additionally, we implement a Calibration Drift Detector: during RL training, periodically measure ECE on current-policy rollouts vs. the initial SFT-distribution calibration. When drift exceeds a threshold, flag those trajectory types as potentially hacked and apply reward clipping. This converts calibration from a static property into a dynamic training signal.\n\nBaseline comparisons for CGSP: (i) uncalibrated PRM + GRPO, (ii) APRM adversarial training, (iii) Caution/prediction-error pessimism, (iv) ensemble minimum (following Coste et al.), (v) KL-regularized GRPO, (vi) gradient regularization (Ackermann et al.).\n\nCodebase starting points: young-j-park/prm-calibration for calibration fitting, Tiwari et al.'s PRM-BiasBench for adversarial evaluation, vwxyzjn/open_instruct for GRPO training infrastructure.\n\n## Inspiration\nField guide gap: PRM overconfidence on OOD problems (Section 5.3 'when more compute hurts'); Untried combination: distributional PRM calibration + PRM hackability analysis; Pattern: connecting two mature but isolated research threads; Reviewer insight: pure measurement is insufficient — the key contribution should be a causal mechanism and a defense method; Methodological insight: post-hoc calibration methods that preserve representations enable clean causal isolation experiments impossible with fine-tuning-based calibration alone\n\n## Key References\n- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (arXiv:2506.09338, NeurIPS 2025)\n- Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport (arXiv:2605.06785, May 2026)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv:2603.06621, March 2026)\n- Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards (arXiv:2602.18037, Feb 2026)\n- Adversarial Training for Process Reward Models (arXiv:2511.22888, Nov 2025)\n- From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism (arXiv:2604.04648, April 2026)\n- Inference-Time Reward Hacking in Large Language Models (arXiv:2506.19248, NeurIPS 2025 Spotlight)\n- Uncertainty-Aware Step-wise Verification with Generative Reward Models (arXiv:2502.11250, ICLR 2025 Workshop)\n- Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242, April 2026)\n- Uncertainty-Aware Reward Model (arXiv:2410.00847)\n- Helping or Herding? Reward Model Ensembles Mitigate but Do Not Eliminate Overoptimization (arXiv:2312.09244)\n- Bayesian Reward Models for LLM Alignment (arXiv:2402.13210)\n- Conformal Feedback Alignment for RLHF (arXiv:2601.17329)\n- Taming Overconfidence in LLMs: Reward Calibration in RLHF (arXiv:2410.09724)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (arXiv:2501.03124)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '4200 H100-hrs (calibration fitting: 200, rollout generation: 600, gradient attacks: 1000, GRPO RL training: 1600 [including CGSP defense training], BoN evaluation: 400, Hessian spectral analysis: 200, causal isolation controls: 200)', 'timeline': '12-14 weeks', 'estimated_gpu_cost': '$10,500 at ~$2.50/H100-hr'}\n- **human_in_loop**: {'gpu_hours': '3600 H100-hrs (fewer failed iterations with AI-assisted debugging)', 'timeline': '10-12 weeks', 'claude_api_cost': '$400-700 (code generation, experiment analysis, paper drafting)', 'estimated_gpu_cost': '$9,000 at ~$2.50/H100-hr'}\n- **auto_research**: {'gpu_hours': '5200 H100-hrs (broader sweeps over α pessimism parameter, calibration drift thresholds, and ablations across all 48 configurations)', 'timeline': '7-9 weeks', 'claude_api_cost': '$1,500-2,000 (automated experiment orchestration, iterative analysis, full draft writing)', 'estimated_gpu_cost': '$13,000 at ~$2.50/H100-hr', 'speed_bottleneck': 'GRPO RL training wall-clock time (~18hrs per PRM×calibration×defense configuration on 4×H100); Hessian spectral analysis requires Lanczos iterations per step per problem; 72B PRM requires 4×H100 for inference'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T21:04:56.811Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T21:04:56.811Z",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4"
}
```

---

## Round 1

42 recorded events

### User

_source line 3 · 2026-05-19T21:04:56.825Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense

## Description
We present the first causally rigorous study connecting PRM calibration quality to adversarial exploitability, and propose Calibration-Gated Step-Level Pessimism (CGSP), a novel defense that transforms calibrated uncertainty into adaptive reward hacking resistance during RL training. Our work bridges two mature but isolated research threads (PRM calibration and PRM hackability) through four contributions. First, an expanded correlation study across 48 configurations (8 PRMs × 6 calibration methods) provides sufficient statistical power (n=48, detecting r≥0.29 at p<0.05) to establish whether calibration quality predicts hackability metrics under gradient attacks, RL-induced hacking (GRPO on AIME), and BoN overoptimization (MATH-500), stratified by problem difficulty. Second, causal isolation experiments separate calibration's true effect from representation change artifacts: we compare post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) that provably preserve model representations against fine-tuning-based methods, with CKA verification and matched-representation-change controls. Third, step-level Hessian spectral analysis goes beyond Ackermann et al.'s outcome-level gradient norm analysis (which applies only to single-scalar reward models) to reveal how calibration affects the multi-reward compositional geometry of PRMs — analyzing how step-level flatness compounds across trajectories. Fourth, CGSP replaces raw PRM rewards during RL training with r̃_t = μ_t − α·σ_t/√c_t, where calibrated uncertainty σ_t and calibration quality c_t adaptively modulate pessimism per-step — trusted when calibration is tight, pessimistic when uncertainty is high — with a Calibration Drift Detector that monitors ECE on current-policy rollouts to flag distribution-shift-induced reward hacking in real time. CGSP differs from existing defenses (Caution uses prediction error, PET uses global pessimism, ensemble methods are uncalibrated) by being step-level, calibration-grounded, and adaptive. We evaluate CGSP against 5 baselines (uncalibrated GRPO, APRM, Caution, ensemble-min, gradient regularization) on MATH-500 and AIME, measuring both reward-accuracy alignment and downstream task accuracy.

## Core Problem
PRM calibration research and PRM hackability research are entirely separate threads with zero cross-citation — but the deeper problem is that we lack both (a) causal evidence for whether calibration actually determines hackability (vs. being merely correlated), and (b) a principled, step-level defense mechanism that leverages calibrated uncertainty to prevent reward hacking during RL training. Existing ad-hoc defenses (adversarial training, gradient regularization, pessimistic BoN) operate at the outcome level without exploiting the unique step-level structure of PRMs.

## Opportunity
Three recent developments create a uniquely favorable moment. First, Distributional PRMs (arXiv:2605.06785, May 2026) achieve calibrated step-level uncertainty via conditional optimal transport but never test robustness. Second, Tiwari et al. (arXiv:2603.06621, March 2026) demonstrate that PRMs are catastrophically hackable — near-perfect PRM rewards with <4% actual accuracy — but propose no calibration-based defense. Third, the causal isolation toolkit is mature: post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) modify only the output mapping without changing model representations, enabling controlled experiments that separate calibration effects from representation effects. No existing paper bridges these threads. Ackermann et al.'s gradient regularization work (arXiv:2602.18037) operates exclusively on outcome-level reward models with single-scalar rewards, never touching step-level PRM geometry. The CoT Entropy paper (arXiv:2502.11250) named this connection as future work 16 months ago with no follow-up. The window for a definitive, causally rigorous study is open but narrowing.

## Related Work / Landscape
Two parallel research threads have developed with zero cross-citation. Thread 1 (PRM Calibration): Park et al. (arXiv:2506.09338, NeurIPS 2025) demonstrate PRMs systematically overestimate success probabilities on hard problems, proposing quantile regression calibration. Distributional PRMs (arXiv:2605.06785, May 2026) use conditional optimal transport for calibrated monotone quantile functions, improving BoN on MATH-500 and AIME. Neither paper tests robustness. Thread 2 (PRM Hackability): Tiwari et al. (arXiv:2603.06621) show gradient attacks inflate PRM rewards 4× and RL achieves near-perfect PRM rewards with <4% accuracy, with 43% of reward gains from stylistic shortcuts. APRM (arXiv:2511.22888) uses adversarial training for +3.4pp robustness. Thread 3 (Adjacent but distinct): Ackermann et al. (arXiv:2602.18037) prove reward surface flatness correlates with accuracy retention for outcome-level RMs, but work exclusively with single-scalar rewards, analyze only gradient norms (no Hessian spectra), and never consider step-level reward models. Their theoretical framework (Propositions 3.3-3.4) assumes a single reward function R(s,a) over complete responses — inapplicable to step-level PRM geometry where T coupled reward surfaces {R_1,...,R_T} interact compositionally. InferenceTimePessimism (arXiv:2506.19248) and Caution (arXiv:2604.04648) apply pessimism for BoN but use uncalibrated uncertainty proxies (prediction error, hedging), not calibrated probabilities. URM (arXiv:2410.00847) decomposes uncertainty into aleatoric/epistemic for outcome-level RMs but not PRMs. Bayesian reward models (arXiv:2402.13210) use Laplace approximation on LoRA weights. Conformal prediction has been applied to RLHF feedback alignment (arXiv:2601.17329) but never to PRM defense. No paper establishes a causal link between calibration quality and hackability, and no paper proposes using calibrated step-level PRM uncertainty as a defense during RL training.

## Approach
The study has four components: (A) Expanded Correlation Study, (B) Causal Isolation Experiments, (C) Step-Level Mechanistic Analysis, and (D) Calibration-Gated Step-Level Pessimism (CGSP) defense.

**Component A — Expanded Correlation Study (n≥24 configurations):** Apply 6 calibration methods across 2 tiers to 8 open-source PRMs. Tier 1 (post-hoc, representation-preserving): temperature scaling, Platt scaling, isotonic regression. Tier 2 (model-modifying): quantile regression fine-tuning, conditional optimal transport, Venn-Abers predictors. The 8 PRMs span discriminative (Qwen2.5-Math-PRM-7B, Qwen2.5-Math-PRM-72B, Skywork-o1-Open-PRM-7B, RLHFlow-Llama3.1-8B-PRM, Math-Shepherd-7B, OpenR-Math-psa-7B), generative (GenPRM-7B), and implicit (EurusPRM-Stage2) architectures. Each of the 48 PRM×calibration configurations is subjected to three attack tiers: (i) gradient-based reward inflation following Tiwari et al., (ii) RL-induced reward hacking via GRPO on AIME, and (iii) BoN overoptimization at N∈{1,4,16,64,256} on MATH-500. Compute rank correlations (Spearman ρ, Kendall τ) between calibration metrics (ECE, Brier score, quantile coverage, reliability diagram sharpness) and hackability metrics (reward-accuracy divergence, attack success rate, BoN degradation onset N*). Stratify analysis by problem difficulty (MATH levels 1-5, AMC vs. AIME) to test whether calibration is more protective on hard problems where PRMs are known to be overconfident.

**Component B — Causal Isolation Experiments:** This is the methodological core addressing the reviewer's causation concern. Design: (B1) Post-hoc calibration control: Apply temperature scaling, Platt scaling, and isotonic regression — which provably modify only the output mapping, not internal representations — and measure hackability change. If hackability decreases under post-hoc calibration alone, this establishes that calibration per se (not representation change) causally affects hackability. (B2) Representation change verification: For fine-tuning-based calibration methods (quantile regression, COT), measure representation change at every transformer layer using Centered Kernel Alignment (CKA) between the base PRM and calibrated PRM. (B3) Matched representation change control: Fine-tune PRMs on an auxiliary task (e.g., next-token prediction on math text) that produces CKA-matched representation changes but does NOT improve calibration. If only calibration-improving fine-tuning reduces hackability (not the CKA-matched control), the causal role of calibration is confirmed. (B4) Conformal prediction as the cleanest test: Apply split-conformal prediction to PRM step scores, providing distribution-free coverage guarantees with zero model modification. Test whether conformal-calibrated PRMs resist hacking better than uncalibrated ones.

**Component C — Step-Level Mechanistic Analysis (differentiating from Ackermann et al.):** Unlike Ackermann et al., who analyze only outcome-level gradient norms and max-perturbation sharpness, we perform Hessian spectral analysis at the step level — computing top-k eigenvalues and spectral density of the step-level reward Hessian ∂²R_t/∂h² (where h is the hidden representation at step t). Key questions: (i) Do calibrated PRMs have flatter step-level reward surfaces (lower top Hessian eigenvalue)? (ii) Does flatness vary by step position (early reasoning steps vs. final answer steps)? (iii) Do hackable reward peaks correspond to isolated large Hessian eigenvalues (sharp directions) that gradient attacks exploit? This extends Ackermann et al.'s framework from single-reward geometry to multi-reward compositional geometry: we analyze how step-level flatness/sharpness compounds across a T-step trajectory to determine outcome-level hackability.

**Component D — Calibration-Gated Step-Level Pessimism (CGSP) Defense:** This transforms the paper from measurement to method. CGSP operates during RL training (GRPO/PPO) by replacing raw PRM step rewards with calibration-modulated rewards: r̃_t = μ_t − α · σ_t / √(c_t), where μ_t is the calibrated step reward mean, σ_t is the calibrated uncertainty (from quantile width or conformal interval), c_t is a calibration quality score (inverse ECE computed on a rolling buffer), and α is a pessimism strength hyperparameter. When calibration is high (small σ_t, high c_t), the reward is trusted; when calibration is low (large σ_t, low c_t), pessimism dominates. This differs from existing pessimism (Caution uses prediction error, PET uses global pessimistic fine-tuning, InferenceTimePessimism uses hedging) because CGSP is (i) step-level, (ii) grounded in calibrated probabilities rather than heuristic proxies, and (iii) adaptive — the pessimism automatically strengthens in distribution-shift regions where the PRM becomes miscalibrated. Additionally, we implement a Calibration Drift Detector: during RL training, periodically measure ECE on current-policy rollouts vs. the initial SFT-distribution calibration. When drift exceeds a threshold, flag those trajectory types as potentially hacked and apply reward clipping. This converts calibration from a static property into a dynamic training signal.

Baseline comparisons for CGSP: (i) uncalibrated PRM + GRPO, (ii) APRM adversarial training, (iii) Caution/prediction-error pessimism, (iv) ensemble minimum (following Coste et al.), (v) KL-regularized GRPO, (vi) gradient regularization (Ackermann et al.).

Codebase starting points: young-j-park/prm-calibration for calibration fitting, Tiwari et al.'s PRM-BiasBench for adversarial evaluation, vwxyzjn/open_instruct for GRPO training infrastructure.

## Inspiration
Field guide gap: PRM overconfidence on OOD problems (Section 5.3 'when more compute hurts'); Untried combination: distributional PRM calibration + PRM hackability analysis; Pattern: connecting two mature but isolated research threads; Reviewer insight: pure measurement is insufficient — the key contribution should be a causal mechanism and a defense method; Methodological insight: post-hoc calibration methods that preserve representations enable clean causal isolation experiments impossible with fine-tuning-based calibration alone

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

## Resource Estimate
- **manual**: {'gpu_hours': '4200 H100-hrs (calibration fitting: 200, rollout generation: 600, gradient attacks: 1000, GRPO RL training: 1600 [including CGSP defense training], BoN evaluation: 400, Hessian spectral analysis: 200, causal isolation controls: 200)', 'timeline': '12-14 weeks', 'estimated_gpu_cost': '$10,500 at ~$2.50/H100-hr'}
- **human_in_loop**: {'gpu_hours': '3600 H100-hrs (fewer failed iterations with AI-assisted debugging)', 'timeline': '10-12 weeks', 'claude_api_cost': '$400-700 (code generation, experiment analysis, paper drafting)', 'estimated_gpu_cost': '$9,000 at ~$2.50/H100-hr'}
- **auto_research**: {'gpu_hours': '5200 H100-hrs (broader sweeps over α pessimism parameter, calibration drift thresholds, and ablations across all 48 configurations)', 'timeline': '7-9 weeks', 'claude_api_cost': '$1,500-2,000 (automated experiment orchestration, iterative analysis, full draft writing)', 'estimated_gpu_cost': '$13,000 at ~$2.50/H100-hr', 'speed_bottleneck': 'GRPO RL training wall-clock time (~18hrs per PRM×calibration×defense configuration on 4×H100); Hessian spectral analysis requires Lanczos iterations per step per problem; 72B PRM requires 4×H100 for inference'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "65edaaff-a340-4d92-8640-ce78a17faf26",
  "type": "user",
  "uuid": "85086281-2693-4c8c-b694-3081d114cbdc",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T21:04:56.824Z_

```json
{
  "parentUuid": "85086281-2693-4c8c-b694-3081d114cbdc",
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
  "uuid": "f542b613-be0d-49fd-9a89-7591adcb1790",
  "timestamp": "2026-05-19T21:04:56.824Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T21:04:56.824Z_

```json
{
  "parentUuid": "f542b613-be0d-49fd-9a89-7591adcb1790",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7e5af106-7c70-41a3-a06d-f74873a80f61",
  "timestamp": "2026-05-19T21:04:56.824Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "7e5af106-7c70-41a3-a06d-f74873a80f61",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration's causal effect on reward hacking resistance",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4"
}
```

---

### Assistant

_source line 8 · 2026-05-19T21:05:02.583Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026 (Conference on Robot Learning). Wait, actually, let me re-read - the system prompt says "CoRL 2026 主会" but this proposal is about PRM calibration and reward hacking in LLMs, which is more of an NLP/ML topic. Let me proceed with the evaluation regardless.

First, I need to do thorough web searches to understand the current landscape before making any judgments. Let me search for the key topics and papers mentioned in this proposal.

Let me load the WebSearch tool first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e5af106-7c70-41a3-a06d-f74873a80f61",
  "isSidechain": false,
  "requestId": "req_011CbCc9Cbb4FNEvmanmtuGu",
  "type": "assistant",
  "uuid": "fa54a753-01e9-4b50-9ec7-4614cf414c06",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019nTPJbD7nds9aKmhsysW4y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5583,
      "cache_read_input_tokens": 13985,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5583,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 220,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 5583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5583
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

_source line 9 · 2026-05-19T21:05:02.981Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SSLDmd9QACUNaSxFDL8AXd`</summary>

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
  "parentUuid": "fa54a753-01e9-4b50-9ec7-4614cf414c06",
  "isSidechain": false,
  "requestId": "req_011CbCc9Cbb4FNEvmanmtuGu",
  "type": "assistant",
  "uuid": "4cca4ec4-891b-40d3-9873-447ed7c3140a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019nTPJbD7nds9aKmhsysW4y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5583,
      "cache_read_input_tokens": 13985,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5583,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 220,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 5583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5583
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

_source line 10 · 2026-05-19T21:05:02.989Z_

<details><summary>↩ Tool result · `toolu_01SSLDmd9QACUNaSxFDL8AXd`</summary>

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
  "parentUuid": "4cca4ec4-891b-40d3-9873-447ed7c3140a",
  "isSidechain": false,
  "promptId": "65edaaff-a340-4d92-8640-ce78a17faf26",
  "type": "user",
  "uuid": "386b01ab-d403-4acd-b728-2aa59bdcc24c",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "4cca4ec4-891b-40d3-9873-447ed7c3140a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-19T21:05:06.124Z_

Now let me conduct thorough research on the key topics in this proposal. I'll run multiple searches in parallel to understand the current landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "386b01ab-d403-4acd-b728-2aa59bdcc24c",
  "isSidechain": false,
  "requestId": "req_011CbCc9f3ZU4JBbqXYnjXRL",
  "type": "assistant",
  "uuid": "63b95741-0df4-4b77-91d5-5936cdf234f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXmhRJ2p6x82n5dRunBBQ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 19568,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 332,
          "cache_read_input_tokens": 19568,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
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

_source line 12 · 2026-05-19T21:05:06.599Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DXuuauqLJQ9y1pLBJ8yVho`</summary>

```json
{
  "query": "PRM calibration process reward model hackability reward hacking 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63b95741-0df4-4b77-91d5-5936cdf234f0",
  "isSidechain": false,
  "requestId": "req_011CbCc9f3ZU4JBbqXYnjXRL",
  "type": "assistant",
  "uuid": "f22caade-9991-42b4-9e22-038b69841336",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXmhRJ2p6x82n5dRunBBQ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 19568,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 332,
          "cache_read_input_tokens": 19568,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
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

_source line 13 · 2026-05-19T21:05:07.518Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FfdfWhJBZQdKxQnVbgU4uV`</summary>

```json
{
  "query": "Tiwari et al \"Reward Under Attack\" process reward model hackability arXiv 2603.06621"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f22caade-9991-42b4-9e22-038b69841336",
  "isSidechain": false,
  "requestId": "req_011CbCc9f3ZU4JBbqXYnjXRL",
  "type": "assistant",
  "uuid": "df5f7889-f740-4e0f-8431-8f4645227ab2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXmhRJ2p6x82n5dRunBBQ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 19568,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 332,
          "cache_read_input_tokens": 19568,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
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

_source line 14 · 2026-05-19T21:05:08.130Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qtua9zhFSEGJAS3DxxRYJ9`</summary>

```json
{
  "query": "Distributional Process Reward Models calibrated conditional optimal transport arXiv 2605.06785"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df5f7889-f740-4e0f-8431-8f4645227ab2",
  "isSidechain": false,
  "requestId": "req_011CbCc9f3ZU4JBbqXYnjXRL",
  "type": "assistant",
  "uuid": "9d932eba-2732-4a17-9e51-af340de5a825",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXmhRJ2p6x82n5dRunBBQ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 19568,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 332,
          "cache_read_input_tokens": 19568,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
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

_source line 15 · 2026-05-19T21:05:08.485Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X4eAPhUP6GK8qpKqqSsjiT`</summary>

```json
{
  "query": "Ackermann gradient regularization reward hacking RLHF arXiv 2602.18037 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d932eba-2732-4a17-9e51-af340de5a825",
  "isSidechain": false,
  "requestId": "req_011CbCc9f3ZU4JBbqXYnjXRL",
  "type": "assistant",
  "uuid": "b084eb28-ebce-4995-868c-131d50dc4866",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXmhRJ2p6x82n5dRunBBQ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 19568,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 332,
          "cache_read_input_tokens": 19568,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
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

_source line 16 · 2026-05-19T21:05:09.018Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GkwXb7C9ZkFsnxKtdw6z7g`</summary>

```json
{
  "query": "calibration reward hacking defense pessimism step-level PRM RL training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b084eb28-ebce-4995-868c-131d50dc4866",
  "isSidechain": false,
  "requestId": "req_011CbCc9f3ZU4JBbqXYnjXRL",
  "type": "assistant",
  "uuid": "8da6e107-8313-4a25-8741-7d814b9d68dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXmhRJ2p6x82n5dRunBBQ6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 19568,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 332,
          "cache_read_input_tokens": 19568,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
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

_source line 17 · 2026-05-19T21:05:15.658Z_

<details><summary>↩ Tool result · `toolu_01DXuuauqLJQ9y1pLBJ8yVho`</summary>

```text
Web search results for query: "PRM calibration process reward model hackability reward hacking 2025 2026"

Links: [{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning","url":"https://arxiv.org/pdf/2504.15275"},{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"},{"title":"Inference-Time Reward Hacking in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=hSX7Dd8dxy"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=reward+hacking"},{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/pdf/2506.09338"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/pdf/2508.04216"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/pdf/2509.26578"},{"title":"Models Know They're Reward Hacking — and Telling Them to Stop Makes It Worse | MindStudio","url":"https://www.mindstudio.ai/blog/models-know-reward-hacking-telling-them-stop-makes-it-worse"}]

I've found several recent papers and resources on PRM (Process Reward Model) calibration, hackability, and reward hacking from 2025-2026. Here are the key findings:

## PRM Hackability and Vulnerabilities

Process Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure. 

A particularly detailed study found that policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts. Additionally, current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.

## Root Causes of PRM-Induced Reward Hacking

The main cause of PRM-induced reward hacking is the canonical summation-form credit assignment in reinforcement learning (RL), which defines the value as cumulative gamma-decayed future rewards, easily induces LLMs to hack steps with high rewards.

External reasoning systems are prone to reward hacking, where high-scoring but logically incorrect paths are assigned high scores by the PRMs, leading to incorrect answers. From a causal inference perspective, this phenomenon is attributed primarily to the presence of confounding semantic features.

## Proposed Solutions

Recent research has introduced several approaches to mitigate these issues, including a min-form credit assignment that formulates the value function as the minimum of future rewards, which significantly alleviates reward hacking by limiting the value function range and distributing advantages more reasonably.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f22caade-9991-42b4-9e22-038b69841336",
  "isSidechain": false,
  "promptId": "65edaaff-a340-4d92-8640-ce78a17faf26",
  "type": "user",
  "uuid": "126c6cbf-ba4d-4724-9bec-61e4028b4599",
  "toolUseResult": {
    "query": "PRM calibration process reward model hackability reward hacking 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SzuPAxBELc6Z3cvMhVv2yQ",
        "content": [
          {
            "title": "GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub",
            "url": "https://github.com/xhwang22/Awesome-Reward-Hacking"
          },
          {
            "title": "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning",
            "url": "https://arxiv.org/pdf/2504.15275"
          },
          {
            "title": "[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/abs/2603.06621"
          },
          {
            "title": "Inference-Time Reward Hacking in Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=hSX7Dd8dxy"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=reward+hacking"
          },
          {
            "title": "Know What You Don't Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://arxiv.org/pdf/2506.09338"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/pdf/2508.04216"
          },
          {
            "title": "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2509.26578"
          },
          {
            "title": "Models Know They're Reward Hacking — and Telling Them to Stop Makes It Worse | MindStudio",
            "url": "https://www.mindstudio.ai/blog/models-know-reward-hacking-telling-them-stop-makes-it-worse"
          }
        ]
      },
      "I've found several recent papers and resources on PRM (Process Reward Model) calibration, hackability, and reward hacking from 2025-2026. Here are the key findings:\n\n## PRM Hackability and Vulnerabilities\n\nProcess Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure. \n\nA particularly detailed study found that policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts. Additionally, current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.\n\n## Root Causes of PRM-Induced Reward Hacking\n\nThe main cause of PRM-induced reward hacking is the canonical summation-form credit assignment in reinforcement learning (RL), which defines the value as cumulative gamma-decayed future rewards, easily induces LLMs to hack steps with high rewards.\n\nExternal reasoning systems are prone to reward hacking, where high-scoring but logically incorrect paths are assigned high scores by the PRMs, leading to incorrect answers. From a causal inference perspective, this phenomenon is attributed primarily to the presence of confounding semantic features.\n\n## Proposed Solutions\n\nRecent research has introduced several approaches to mitigate these issues, including a min-form credit assignment that formulates the value function as the minimum of future rewards, which significantly alleviates reward hacking by limiting the value function range and distributing advantages more reasonably."
    ],
    "durationSeconds": 9.055007279000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f22caade-9991-42b4-9e22-038b69841336",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T21:05:16.483Z_

<details><summary>↩ Tool result · `toolu_01FfdfWhJBZQdKxQnVbgU4uV`</summary>

```text
Web search results for query: "Tiwari et al "Reward Under Attack" process reward model hackability arXiv 2603.06621"

Links: [{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"Beyond Semantic Manipulation: Token-Space Attacks on Reward Models","url":"https://arxiv.org/pdf/2604.02686"},{"title":"Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort","url":"https://arxiv.org/pdf/2510.01367"},{"title":"1 Introduction","url":"https://arxiv.org/html/2603.06621"},{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/pdf/2604.01476"},{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/pdf/2603.28063"}]

I found the paper! Here's what I found:

"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models" by Rishabh Tiwari and colleagues demonstrates that state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure.

The authors introduce a three-tiered diagnostic framework that applies increasing adversarial pressure to quantify vulnerabilities. Static perturbation analysis uncovers a fluency-logic dissociation: high invariance to surface-level style changes yet inconsistent detection of logically-corrupted reasoning, with different models failing on different attack types.

The framework includes three diagnostic tiers: Static Perturbation (model-agnostic), Adversarial Tokens (white-box), and RL-Induced Reward Hacking (black-box), with findings that optimized 100-token adversarial sequences push rewards above 0.9.

The paper was published on arXiv on February 20, 2026, with identifier 2603.06621.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df5f7889-f740-4e0f-8431-8f4645227ab2",
  "isSidechain": false,
  "promptId": "65edaaff-a340-4d92-8640-ce78a17faf26",
  "type": "user",
  "uuid": "f730b3b8-3cfd-4f13-9d44-1c092ceedb75",
  "toolUseResult": {
    "query": "Tiwari et al \"Reward Under Attack\" process reward model hackability arXiv 2603.06621",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WjQX5Pi9eN39Dtfje3tNFd",
        "content": [
          {
            "title": "[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/abs/2603.06621"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub",
            "url": "https://github.com/xhwang22/Awesome-Reward-Hacking"
          },
          {
            "title": "Beyond Semantic Manipulation: Token-Space Attacks on Reward Models",
            "url": "https://arxiv.org/pdf/2604.02686"
          },
          {
            "title": "Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort",
            "url": "https://arxiv.org/pdf/2510.01367"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2603.06621"
          },
          {
            "title": "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals",
            "url": "https://arxiv.org/pdf/2604.01476"
          },
          {
            "title": "Reward Hacking as Equilibrium under Finite Evaluation",
            "url": "https://arxiv.org/pdf/2603.28063"
          }
        ]
      },
      "I found the paper! Here's what I found:\n\n\"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\" by Rishabh Tiwari and colleagues demonstrates that state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure.\n\nThe authors introduce a three-tiered diagnostic framework that applies increasing adversarial pressure to quantify vulnerabilities. Static perturbation analysis uncovers a fluency-logic dissociation: high invariance to surface-level style changes yet inconsistent detection of logically-corrupted reasoning, with different models failing on different attack types.\n\nThe framework includes three diagnostic tiers: Static Perturbation (model-agnostic), Adversarial Tokens (white-box), and RL-Induced Reward Hacking (black-box), with findings that optimized 100-token adversarial sequences push rewards above 0.9.\n\nThe paper was published on arXiv on February 20, 2026, with identifier 2603.06621."
    ],
    "durationSeconds": 8.962118622,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "df5f7889-f740-4e0f-8431-8f4645227ab2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T21:05:16.656Z_

<details><summary>↩ Tool result · `toolu_01Qtua9zhFSEGJAS3DxxRYJ9`</summary>

```text
Web search results for query: "Distributional Process Reward Models calibrated conditional optimal transport arXiv 2605.06785"

Links: [{"title":"[2605.06785] Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/abs/2605.06785"},{"title":"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/html/2605.06785"},{"title":"Aligning Crowd Feedback via Distributional Preference Reward Modeling","url":"https://arxiv.org/pdf/2402.09764"},{"title":"Consistent Optimal Transport with Empirical Conditional Measures","url":"https://arxiv.org/pdf/2305.15901"},{"title":"Distributional Preference Alignment of LLMs via Optimal Transport","url":"https://arxiv.org/pdf/2406.05882"},{"title":"APLOT: Robust Reward Modeling via Adaptive Preference Learning with Optimal Transport","url":"https://arxiv.org/pdf/2510.10963"},{"title":"Neural Conditional Transport Maps","url":"https://arxiv.org/pdf/2505.15808"}]

Based on the search results, I found the paper you're looking for:

**Title:** Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport (arXiv:2605.06785)

**Authors:** Rachel Ma (MIT CSAIL), Dylan Hadfield-Menell (MIT CSAIL), and Kristjan Greenewald (IBM Research)

**Key Contribution:** The paper proposes the first use of conditional optimal transport for calibrating PRMs, modifying conditional OT (CondOT) map learning to estimate a monotonic conditional quantile function over success probabilities estimated by the PRM, conditioned on PRM hidden states.

**Main Problem:** Inference-time scaling methods rely on Process Reward Models (PRMs), which are often poorly calibrated and overestimate success probabilities.

**Approach:** This yields structurally valid quantile estimates and enables efficient extraction of confidence bounds at arbitrary levels, which they integrate into the instance-adaptive scaling (IAS) framework.

**Evaluation:** They evaluate on mathematical reasoning benchmarks spanning moderate-difficulty problems (MATH-500) and harder out-of-distribution problems (AIME), with their method substantially improving calibration over both uncalibrated PRMs and quantile regression for PRMs with reliable ranking signals.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d932eba-2732-4a17-9e51-af340de5a825",
  "isSidechain": false,
  "promptId": "65edaaff-a340-4d92-8640-ce78a17faf26",
  "type": "user",
  "uuid": "e4d42e86-5b77-4c76-b05e-287844b6f79b",
  "toolUseResult": {
    "query": "Distributional Process Reward Models calibrated conditional optimal transport arXiv 2605.06785",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HrnXPSJXW8UfDPZnWhsMAM",
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
            "title": "Aligning Crowd Feedback via Distributional Preference Reward Modeling",
            "url": "https://arxiv.org/pdf/2402.09764"
          },
          {
            "title": "Consistent Optimal Transport with Empirical Conditional Measures",
            "url": "https://arxiv.org/pdf/2305.15901"
          },
          {
            "title": "Distributional Preference Alignment of LLMs via Optimal Transport",
            "url": "https://arxiv.org/pdf/2406.05882"
          },
          {
            "title": "APLOT: Robust Reward Modeling via Adaptive Preference Learning with Optimal Transport",
            "url": "https://arxiv.org/pdf/2510.10963"
          },
          {
            "title": "Neural Conditional Transport Maps",
            "url": "https://arxiv.org/pdf/2505.15808"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Title:** Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport (arXiv:2605.06785)\n\n**Authors:** Rachel Ma (MIT CSAIL), Dylan Hadfield-Menell (MIT CSAIL), and Kristjan Greenewald (IBM Research)\n\n**Key Contribution:** The paper proposes the first use of conditional optimal transport for calibrating PRMs, modifying conditional OT (CondOT) map learning to estimate a monotonic conditional quantile function over success probabilities estimated by the PRM, conditioned on PRM hidden states.\n\n**Main Problem:** Inference-time scaling methods rely on Process Reward Models (PRMs), which are often poorly calibrated and overestimate success probabilities.\n\n**Approach:** This yields structurally valid quantile estimates and enables efficient extraction of confidence bounds at arbitrary levels, which they integrate into the instance-adaptive scaling (IAS) framework.\n\n**Evaluation:** They evaluate on mathematical reasoning benchmarks spanning moderate-difficulty problems (MATH-500) and harder out-of-distribution problems (AIME), with their method substantially improving calibration over both uncalibrated PRMs and quantile regression for PRMs with reliable ranking signals."
    ],
    "durationSeconds": 8.523594410000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9d932eba-2732-4a17-9e51-af340de5a825",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T21:05:18.191Z_

<details><summary>↩ Tool result · `toolu_01X4eAPhUP6GK8qpKqqSsjiT`</summary>

```text
Web search results for query: "Ackermann gradient regularization reward hacking RLHF arXiv 2602.18037 2026"

Links: [{"title":"[2602.18037] Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards","url":"https://arxiv.org/abs/2602.18037"},{"title":"Johannes Ackermann","url":"https://johannesack.github.io/"},{"title":"Gradient Regularization Prevents Reward Hacking in ...","url":"https://arxiv.org/pdf/2602.18037"},{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking | OpenReview","url":"https://openreview.net/forum?id=msEr27EejF"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/html/2604.02986"},{"title":"Unifying Stable Optimization and Reference Regularization in RLHF","url":"https://arxiv.org/html/2602.11523v1"},{"title":"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking","url":"https://arxiv.org/pdf/2501.19358"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"},{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking","url":"https://arxiv.org/html/2403.03185v4"},{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward   Hacking","url":"https://arxiv.org/pdf/2403.03185"}]

Based on the search results, I found information about the paper you're looking for:

The paper is titled "Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards" by Johannes Ackermann and 3 other authors, and it was posted on arXiv on February 20, 2026 with identifier 2602.18037.

**Main Contribution:**

The paper addresses a common problem in RLHF (Reinforcement Learning from Human Feedback) and RLVR (Verifiable Rewards) called reward hacking, where the policy may exploit inaccuracies of the reward and learn an unintended behavior.

**Proposed Solution:**

The authors propose training the LM in a way that biases policy updates towards regions in which the reward is more accurate. They derive a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence, and show that gradient regularization (GR) can be used to bias training to flatter regions and thereby maintain reward model accuracy.

**Empirical Evidence:**

The authors confirm their results by showing that the gradient norm and reward accuracy are empirically correlated in RLHF.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b084eb28-ebce-4995-868c-131d50dc4866",
  "isSidechain": false,
  "promptId": "65edaaff-a340-4d92-8640-ce78a17faf26",
  "type": "user",
  "uuid": "0a8c79f7-df78-44df-bc74-a98c34722434",
  "toolUseResult": {
    "query": "Ackermann gradient regularization reward hacking RLHF arXiv 2602.18037 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JxgwdmU9y4VKJ3j4C6QWvV",
        "content": [
          {
            "title": "[2602.18037] Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards",
            "url": "https://arxiv.org/abs/2602.18037"
          },
          {
            "title": "Johannes Ackermann",
            "url": "https://johannesack.github.io/"
          },
          {
            "title": "Gradient Regularization Prevents Reward Hacking in ...",
            "url": "https://arxiv.org/pdf/2602.18037"
          },
          {
            "title": "Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking | OpenReview",
            "url": "https://openreview.net/forum?id=msEr27EejF"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/html/2604.02986"
          },
          {
            "title": "Unifying Stable Optimization and Reference Regularization in RLHF",
            "url": "https://arxiv.org/html/2602.11523v1"
          },
          {
            "title": "The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking",
            "url": "https://arxiv.org/pdf/2501.19358"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/pdf/2604.02986"
          },
          {
            "title": "Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking",
            "url": "https://arxiv.org/html/2403.03185v4"
          },
          {
            "title": "Correlated Proxies: A New Definition and Improved Mitigation for Reward   Hacking",
            "url": "https://arxiv.org/pdf/2403.03185"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\nThe paper is titled \"Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards\" by Johannes Ackermann and 3 other authors, and it was posted on arXiv on February 20, 2026 with identifier 2602.18037.\n\n**Main Contribution:**\n\nThe paper addresses a common problem in RLHF (Reinforcement Learning from Human Feedback) and RLVR (Verifiable Rewards) called reward hacking, where the policy may exploit inaccuracies of the reward and learn an unintended behavior.\n\n**Proposed Solution:**\n\nThe authors propose training the LM in a way that biases policy updates towards regions in which the reward is more accurate. They derive a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence, and show that gradient regularization (GR) can be used to bias training to flatter regions and thereby maintain reward model accuracy.\n\n**Empirical Evidence:**\n\nThe authors confirm their results by showing that the gradient norm and reward accuracy are empirically correlated in RLHF."
    ],
    "durationSeconds": 9.703516682000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b084eb28-ebce-4995-868c-131d50dc4866",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "0a8c79f7-df78-44df-bc74-a98c34722434",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration's causal effect on reward hacking resistance",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4"
}
```

---

### Tool result

_source line 23 · 2026-05-19T21:05:19.491Z_

<details><summary>↩ Tool result · `toolu_01GkwXb7C9ZkFsnxKtdw6z7g`</summary>

```text
Web search results for query: "calibration reward hacking defense pessimism step-level PRM RL training 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 AGENTIC REINFORCEMENT LEARNING","url":"https://openreview.net/pdf/a1e5782d4488277b71a1a194ebecc820d981e887.pdf"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2512.16917"},{"title":"Reward Hacking Defense Rubric","url":"https://www.emergentmind.com/topics/reward-hacking-defense-rubric"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning","url":"https://arxiv.org/pdf/2504.15275"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"Natural Emergent Misalignment from Reward Hacking in Production RL","url":"https://arxiv.org/pdf/2511.18397"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/pdf/2604.04648"}]

Based on the search results, here's what I found regarding your query about calibration, reward hacking defense, pessimism, step-level PRM, and RL training in 2025-2026:

## Reward Hacking Defenses

Recent approaches using handcrafted step labels provide denser feedback at intermediate steps but are costly, biased, and vulnerable to reward hacking. Several defense mechanisms have emerged:

**Pessimistic Reward Modeling:** Pessimistic reward modeling (PET) embeds pessimism so that even "greedy" policy optimization under the learned reward is robust to overestimation, and requires no KL regularization.

**Slice-Level Rewards with Alignment Regularization:** An approach jointly trains the reasoner and a discriminator under an on-policy scheme, yielding dense slice-level rewards with alignment regularization to curb reward hacking, addressing PRM mis-specification and noisy signals.

## Step-Level Process Reward Models (PRMs)

Implicit PRMs help in single-turn tasks, but token-level process rewards tend to be overly fine-grained in agent training, amplifying variance and destabilizing training as trajectories grow. Other approaches compute step-level advantages by grouping identical states, an assumption that fails in open-ended language environments where state overlap is rare.

## General Reward Hacking Challenge

The standard training framework faces the critical problem of 'reward hacking,' also known as 'reward over-optimization,' which can happen during policy optimization and decrease the learning efficiency of an algorithm.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8da6e107-8313-4a25-8741-7d814b9d68dc",
  "isSidechain": false,
  "promptId": "65edaaff-a340-4d92-8640-ce78a17faf26",
  "type": "user",
  "uuid": "5da2962e-22fe-49d3-a630-b3ab44df0d02",
  "toolUseResult": {
    "query": "calibration reward hacking defense pessimism step-level PRM RL training 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015prNBjnbBpS3npQbLKaXV6",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 AGENTIC REINFORCEMENT LEARNING",
            "url": "https://openreview.net/pdf/a1e5782d4488277b71a1a194ebecc820d981e887.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2512.16917"
          },
          {
            "title": "Reward Hacking Defense Rubric",
            "url": "https://www.emergentmind.com/topics/reward-hacking-defense-rubric"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning",
            "url": "https://arxiv.org/pdf/2504.15275"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/pdf/2505.20556"
          },
          {
            "title": "Natural Emergent Misalignment from Reward Hacking in Production RL",
            "url": "https://arxiv.org/pdf/2511.18397"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism",
            "url": "https://arxiv.org/pdf/2604.04648"
          }
        ]
      },
      "Based on the search results, here's what I found regarding your query about calibration, reward hacking defense, pessimism, step-level PRM, and RL training in 2025-2026:\n\n## Reward Hacking Defenses\n\nRecent approaches using handcrafted step labels provide denser feedback at intermediate steps but are costly, biased, and vulnerable to reward hacking. Several defense mechanisms have emerged:\n\n**Pessimistic Reward Modeling:** Pessimistic reward modeling (PET) embeds pessimism so that even \"greedy\" policy optimization under the learned reward is robust to overestimation, and requires no KL regularization.\n\n**Slice-Level Rewards with Alignment Regularization:** An approach jointly trains the reasoner and a discriminator under an on-policy scheme, yielding dense slice-level rewards with alignment regularization to curb reward hacking, addressing PRM mis-specification and noisy signals.\n\n## Step-Level Process Reward Models (PRMs)\n\nImplicit PRMs help in single-turn tasks, but token-level process rewards tend to be overly fine-grained in agent training, amplifying variance and destabilizing training as trajectories grow. Other approaches compute step-level advantages by grouping identical states, an assumption that fails in open-ended language environments where state overlap is rare.\n\n## General Reward Hacking Challenge\n\nThe standard training framework faces the critical problem of 'reward hacking,' also known as 'reward over-optimization,' which can happen during policy optimization and decrease the learning efficiency of an algorithm."
    ],
    "durationSeconds": 10.470256184000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8da6e107-8313-4a25-8741-7d814b9d68dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-19T21:05:23.843Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've gathered some initial information. Let me do a few more targeted searches to understand the landscape better, particularly around:
1. The "Caution" paper (arXiv:2604.04648)
2. Whether anyone has already connected calibration to hackability
3. The Park et al. NeurIPS 2025 paper on PRM calibration
4. Recent CoRL submission topics to understand if this is even the right venue
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5da2962e-22fe-49d3-a630-b3ab44df0d02",
  "isSidechain": false,
  "requestId": "req_011CbCcAsRUU4VZYRc5keMpT",
  "type": "assistant",
  "uuid": "5db12103-1463-4d7b-bfe1-58b4415ab63b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174rDyyQb1uKFS2EMMHp2bz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 20315,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 20315,
          "cache_creation_input_tokens": 4101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4101
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

_source line 25 · 2026-05-19T21:05:24.351Z_

Let me do a few more targeted searches to fill in gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5db12103-1463-4d7b-bfe1-58b4415ab63b",
  "isSidechain": false,
  "requestId": "req_011CbCcAsRUU4VZYRc5keMpT",
  "type": "assistant",
  "uuid": "2f0decf3-9426-4332-8408-65280ec097a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174rDyyQb1uKFS2EMMHp2bz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 20315,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 20315,
          "cache_creation_input_tokens": 4101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4101
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

_source line 26 · 2026-05-19T21:05:25.288Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GTYQRxzpSH6Ks61ANGSRwB`</summary>

```json
{
  "query": "\"From Curiosity to Caution\" reward hacking pessimism Best-of-N arXiv 2604.04648 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f0decf3-9426-4332-8408-65280ec097a3",
  "isSidechain": false,
  "requestId": "req_011CbCcAsRUU4VZYRc5keMpT",
  "type": "assistant",
  "uuid": "14d1e698-49a6-4f9d-bbec-88a5df028ede",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174rDyyQb1uKFS2EMMHp2bz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 20315,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 20315,
          "cache_creation_input_tokens": 4101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4101
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

_source line 27 · 2026-05-19T21:05:26.234Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019kPjo6MikDcDJayBHozUP5`</summary>

```json
{
  "query": "Park et al \"Know What You Don't Know\" uncertainty calibration process reward models NeurIPS 2025 arXiv 2506.09338"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14d1e698-49a6-4f9d-bbec-88a5df028ede",
  "isSidechain": false,
  "requestId": "req_011CbCcAsRUU4VZYRc5keMpT",
  "type": "assistant",
  "uuid": "687456e7-f1af-4bd7-85b1-f9603730053a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174rDyyQb1uKFS2EMMHp2bz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 20315,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 20315,
          "cache_creation_input_tokens": 4101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4101
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

_source line 28 · 2026-05-19T21:05:26.499Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WDc6TkdhdeQcDFCTnv2f2R`</summary>

```json
{
  "query": "CoRL 2026 conference robot learning topics scope submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "687456e7-f1af-4bd7-85b1-f9603730053a",
  "isSidechain": false,
  "requestId": "req_011CbCcAsRUU4VZYRc5keMpT",
  "type": "assistant",
  "uuid": "ca3a2580-bd16-4219-af5c-51856290e73f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174rDyyQb1uKFS2EMMHp2bz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4101,
      "cache_read_input_tokens": 20315,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 20315,
          "cache_creation_input_tokens": 4101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4101
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

_source line 29 · 2026-05-19T21:05:32.736Z_

<details><summary>↩ Tool result · `toolu_019kPjo6MikDcDJayBHozUP5`</summary>

```text
Web search results for query: "Park et al "Know What You Don't Know" uncertainty calibration process reward models NeurIPS 2025 arXiv 2506.09338"

Links: [{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models for NeurIPS 2025 - IBM Research","url":"https://research.ibm.com/publications/know-what-you-dont-know-uncertainty-calibration-of-process-reward-models"},{"title":"[2506.09338] Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/abs/2506.09338"},{"title":"NeurIPS Poster Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://neurips.cc/virtual/2025/poster/116598"},{"title":"(PDF) Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://www.researchgate.net/publication/392597872_Know_What_You_Don't_Know_Uncertainty_Calibration_of_Process_Reward_Models"},{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models | OpenReview","url":"https://openreview.net/forum?id=hzMkfIrdDT"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/pdf/2506.09338"},{"title":"Machine Learning Jun 2025","url":"https://arxiv.org/list/cs.LG/2025-06?skip=3125&show=2000"},{"title":"I Don't Know: Explicit Modeling of Uncertainty with an [IDK] Token","url":"https://arxiv.org/pdf/2412.06676"}]

I found the paper you're looking for! Here's what I found:

The paper "Know What You Don't Know: Uncertainty Calibration of Process Reward Models" is by Young-Jin Park and colleagues, and it addresses how process reward models (PRMs) play a central role in guiding inference-time scaling algorithms for large language models (LLMs).

The key finding is that even state-of-the-art PRMs can be poorly calibrated, specifically tending to overestimate the success probability that a partial reasoning step will lead to a correct final answer, particularly when smaller LLMs are used to complete the reasoning trajectory.

To address this, the authors present a calibration approach performed via quantile regression that adjusts PRM outputs to better align with true success probabilities. They also introduce an instance-adaptive scaling (IAS) framework that dynamically adjusts the compute budget based on the estimated likelihood that a partial reasoning trajectory will yield a correct final answer.

Experiments on mathematical reasoning benchmarks show that their PRM calibration method achieves small calibration error while outperforming baseline methods, and the proposed IAS strategy reduces inference costs while maintaining final answer accuracy.

The paper was published at NeurIPS 2025 as a poster presentation. The arXiv preprint is available at https://arxiv.org/abs/2506.09338.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "687456e7-f1af-4bd7-85b1-f9603730053a",
  "isSidechain": false,
  "promptId": "65edaaff-a340-4d92-8640-ce78a17faf26",
  "type": "user",
  "uuid": "400f526b-8ebd-452f-9a7b-be959a796bb0",
  "toolUseResult": {
    "query": "Park et al \"Know What You Don't Know\" uncertainty calibration process reward models NeurIPS 2025 arXiv 2506.09338",
    "results": [
      {
        "tool_use_id": "srvtoolu_018NW52J1BaEGY1ZzPfLwPBT",
        "content": [
          {
            "title": "Know What You Don’t Know: Uncertainty Calibration of Process Reward Models for NeurIPS 2025 - IBM Research",
            "url": "https://research.ibm.com/publications/know-what-you-dont-know-uncertainty-calibration-of-process-reward-models"
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
            "title": "(PDF) Know What You Don't Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://www.researchgate.net/publication/392597872_Know_What_You_Don't_Know_Uncertainty_Calibration_of_Process_Reward_Models"
          },
          {
            "title": "Know What You Don't Know: Uncertainty Calibration of Process Reward Models | OpenReview",
            "url": "https://openreview.net/forum?id=hzMkfIrdDT"
          },
          {
            "title": "Know What You Don’t Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://arxiv.org/pdf/2506.09338"
          },
          {
            "title": "Machine Learning Jun 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-06?skip=3125&show=2000"
          },
          {
            "title": "I Don't Know: Explicit Modeling of Uncertainty with an [IDK] Token",
            "url": "https://arxiv.org/pdf/2412.06676"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found:\n\nThe paper \"Know What You Don't Know: Uncertainty Calibration of Process Reward Models\" is by Young-Jin Park and colleagues, and it addresses how process reward models (PRMs) play a central role in guiding inference-time scaling algorithms for large language models (LLMs).\n\nThe key finding is that even state-of-the-art PRMs can be poorly calibrated, specifically tending to overestimate the success probability that a partial reasoning step will lead to a correct final answer, particularly when smaller LLMs are used to complete the reasoning trajectory.\n\nTo address this, the authors present a calibration approach performed via quantile regression that adjusts PRM outputs to better align with true success probabilities. They also introduce an instance-adaptive scaling (IAS) framework that dynamically adjusts the compute budget based on the estimated likelihood that a partial reasoning trajectory will yield a correct final answer.\n\nExperiments on mathematical reasoning benchmarks show that their PRM calibration method achieves small calibration error while outperforming baseline methods, and the proposed IAS strategy reduces inference costs while maintaining final answer accuracy.\n\nThe paper was published at NeurIPS 2025 as a poster presentation. The arXiv preprint is available at https://arxiv.org/abs/2506.09338."
    ],
    "durationSeconds": 6.499437143000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "687456e7-f1af-4bd7-85b1-f9603730053a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T21:05:33.780Z_

<details><summary>↩ Tool result · `toolu_01WDc6TkdhdeQcDFCTnv2f2R`</summary>

```text
Web search results for query: "CoRL 2026 conference robot learning topics scope submission"

Links: [{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI","url":"https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"2025 Conference on Robot Learning - CoRL","url":"https://www.corl.org/home"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026 - About CoRL","url":"https://www.corl.org/about-corl"},{"title":"System and method for robot learning from human demonstrations with formal logic","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12208521"}]

Based on the search results, here's information about CoRL 2026 conference topics and submission scope:

## Conference Overview

CoRL is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.

## Topics and Scope

CoRL welcomes papers in areas such as: learning representations for robotic perception and control, learning robot foundation models or general-purpose knowledge systems for robotics, imitation learning for robotics, reinforcement learning for control of physical robots, learning approaches to robot safety and alignment, applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics, robot systems hardware and sensors for learning, theoretical foundations of robot learning, and video models and latent world models for robot learning.

## Submission Requirements

Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. Submissions without a robotics focus will be returned without review.

## Key Dates and Location

CoRL 2026 will be held at the JW Marriott Austin in Austin, TX (November 9–12, 2026), with a workshop day on November 9 and the main conference on November 10–12, and the paper submission deadline is May 29, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca3a2580-bd16-4219-af5c-51856290e73f",
  "isSidechain": false,
  "promptId": "65edaaff-a340-4d92-8640-ce78a17faf26",
  "type": "user",
  "uuid": "b2e192ef-2b5e-4f2c-96e3-73f6594c2f28",
  "toolUseResult": {
    "query": "CoRL 2026 conference robot learning topics scope submission",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WxmYmYGoqTRkpuroxMDzE2",
        "content": [
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI",
            "url": "https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"
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
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
          },
          {
            "title": "2025 Conference on Robot Learning - CoRL",
            "url": "https://www.corl.org/home"
          },
          {
            "title": "CoRL 2026 - Call for Workshops",
            "url": "https://www.corl.org/contributions/call-for-workshops"
          },
          {
            "title": "CoRL 2026 - About CoRL",
            "url": "https://www.corl.org/about-corl"
          },
          {
            "title": "System and method for robot learning from human demonstrations with formal logic",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12208521"
          }
        ]
      },
      "Based on the search results, here's information about CoRL 2026 conference topics and submission scope:\n\n## Conference Overview\n\nCoRL is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.\n\n## Topics and Scope\n\nCoRL welcomes papers in areas such as: learning representations for robotic perception and control, learning robot foundation models or general-purpose knowledge systems for robotics, imitation learning for robotics, reinforcement learning for control of physical robots, learning approaches to robot safety and alignment, applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics, robot systems hardware and sensors for learning, theoretical foundations of robot learning, and video models and latent world models for robot learning.\n\n## Submission Requirements\n\nSubmissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. Submissions without a robotics focus will be returned without review.\n\n## Key Dates and Location\n\nCoRL 2026 will be held at the JW Marriott Austin in Austin, TX (November 9–12, 2026), with a workshop day on November 9 and the main conference on November 10–12, and the paper submission deadline is May 29, 2026."
    ],
    "durationSeconds": 7.278417331000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ca3a2580-bd16-4219-af5c-51856290e73f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T21:05:34.866Z_

<details><summary>↩ Tool result · `toolu_01GTYQRxzpSH6Ks61ANGSRwB`</summary>

```text
Web search results for query: ""From Curiosity to Caution" reward hacking pessimism Best-of-N arXiv 2604.04648 2026"

Links: [{"title":"[2604.04648] From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/abs/2604.04648"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-𝑁 with Pessimism","url":"https://arxiv.org/html/2604.04648"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/pdf/2604.04648"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-$N$ with Pessimism | OpenReview","url":"https://openreview.net/forum?id=EZn2TmBBfF"},{"title":"Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/pdf/2506.19248"}]

I found the paper you were searching for! Here's what I found about arXiv 2604.04648:

**Paper Title:** "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism"

**Authors:** Zhuohao Yu, Zhiwei Steven Wu (Carnegie Mellon University), and Adam Block (Columbia University)

**Submission Date:** April 6, 2026

**Main Topic:** The paper addresses inference-time compute scaling for language models. It focuses on Best-of-N (BoN) sampling, where N candidate responses are generated, scored according to a reward model, and the highest-scoring response is selected.

**Problem Addressed:** BoN sampling is vulnerable to reward hacking, where performance degrades as N increases due to the selection of responses that exploit imperfections in the reward model instead of genuinely improving generation quality.

**Proposed Solution:** The paper explores the principle of pessimism in RL, which uses lower confidence bounds on value estimates to avoid out-of-distribution actions with uncertain reward estimates. Their approach, termed "caution," can be seen as the reverse of curiosity, and practically trains an error model on typical responses and uses its prediction error to lower reward estimates for atypical ones.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14d1e698-49a6-4f9d-bbec-88a5df028ede",
  "isSidechain": false,
  "promptId": "65edaaff-a340-4d92-8640-ce78a17faf26",
  "type": "user",
  "uuid": "7ebd58c0-e4a1-40a7-b4eb-d3622638f547",
  "toolUseResult": {
    "query": "\"From Curiosity to Caution\" reward hacking pessimism Best-of-N arXiv 2604.04648 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HBPaK2Rp73tjGZMYMnhT4s",
        "content": [
          {
            "title": "[2604.04648] From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism",
            "url": "https://arxiv.org/abs/2604.04648"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-𝑁 with Pessimism",
            "url": "https://arxiv.org/html/2604.04648"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism",
            "url": "https://arxiv.org/pdf/2604.04648"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-$N$ with Pessimism | OpenReview",
            "url": "https://openreview.net/forum?id=EZn2TmBBfF"
          },
          {
            "title": "Inference-Time Reward Hacking in Large Language Models",
            "url": "https://arxiv.org/pdf/2506.19248"
          }
        ]
      },
      "I found the paper you were searching for! Here's what I found about arXiv 2604.04648:\n\n**Paper Title:** \"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism\"\n\n**Authors:** Zhuohao Yu, Zhiwei Steven Wu (Carnegie Mellon University), and Adam Block (Columbia University)\n\n**Submission Date:** April 6, 2026\n\n**Main Topic:** The paper addresses inference-time compute scaling for language models. It focuses on Best-of-N (BoN) sampling, where N candidate responses are generated, scored according to a reward model, and the highest-scoring response is selected.\n\n**Problem Addressed:** BoN sampling is vulnerable to reward hacking, where performance degrades as N increases due to the selection of responses that exploit imperfections in the reward model instead of genuinely improving generation quality.\n\n**Proposed Solution:** The paper explores the principle of pessimism in RL, which uses lower confidence bounds on value estimates to avoid out-of-distribution actions with uncertain reward estimates. Their approach, termed \"caution,\" can be seen as the reverse of curiosity, and practically trains an error model on typical responses and uses its prediction error to lower reward estimates for atypical ones."
    ],
    "durationSeconds": 9.574784439000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "14d1e698-49a6-4f9d-bbec-88a5df028ede",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-19T21:05:34.870Z_

```json
{
  "parentUuid": "7ebd58c0-e4a1-40a7-b4eb-d3622638f547",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6ff11638-a2de-4b0c-ac2d-9262d090e3cf",
  "timestamp": "2026-05-19T21:05:34.870Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-19T21:05:48.851Z_

<details><summary>Logged reasoning block</summary>

```text
This is a critical finding. CoRL 2026 is a **robotics** conference. The call for papers explicitly states: "Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics." and "Submissions without a robotics focus will be returned without review."

This proposal is about PRM calibration and reward hacking in LLM reasoning (math problem solving). It has **zero** robotics content. This is a fundamental venue mismatch that would likely result in a desk reject.

Wait, let me re-read the user's prompt. 

The system prompt says "评估其投稿 CoRL 2026 主会的中稿潜力" - evaluating its acceptance potential at CoRL 2026 main conference. This is a massive issue. The explicit task is to evaluate this for CoRL 2026, but the work has no robotics component whatsoever. This venue mismatch is a critical problem that would almost certainly lead to desk rejection, regardless of the paper's technical quality.

That said, the system also describes itself as a "通用 idea 审核流程" - a general idea review process without preset constraints. And the rubric includes "NLP/CL 领域的影响力" in the Significance dimension, which suggests the actual target might be a general ML venue like ICML, NeurIPS, or ICLR rather than CoRL. I should flag this venue mismatch as a critical issue while evaluating the idea on its technical merits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ff11638-a2de-4b0c-ac2d-9262d090e3cf",
  "isSidechain": false,
  "requestId": "req_011CbCcC18MHyD6VcnsRFPu7",
  "type": "assistant",
  "uuid": "bb7fcd34-aeb5-42da-a1bc-720ad7a0b587",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jTeyZkYKXSiLGyuPPTtSv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1516,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 24416,
      "output_tokens": 637,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1516,
          "output_tokens": 637,
          "cache_read_input_tokens": 24416,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1071
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

_source line 34 · 2026-05-19T21:05:48.853Z_

This is a critical finding — CoRL is a **robotics** conference. Let me do a couple more searches to fully understand the idea's positioning in the NLP/ML landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb7fcd34-aeb5-42da-a1bc-720ad7a0b587",
  "isSidechain": false,
  "requestId": "req_011CbCcC18MHyD6VcnsRFPu7",
  "type": "assistant",
  "uuid": "4145290e-0f5a-4e1a-8f71-f83434badbfa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jTeyZkYKXSiLGyuPPTtSv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1516,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 24416,
      "output_tokens": 637,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1516,
          "output_tokens": 637,
          "cache_read_input_tokens": 24416,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1071
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

_source line 35 · 2026-05-19T21:05:49.447Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016p6Mv7Yr2V6x18wQZynbf6`</summary>

```json
{
  "query": "calibration causally determines reward model robustness hackability causal link 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4145290e-0f5a-4e1a-8f71-f83434badbfa",
  "isSidechain": false,
  "requestId": "req_011CbCcC18MHyD6VcnsRFPu7",
  "type": "assistant",
  "uuid": "1ef20ddd-aca6-4c86-8eaa-d56e1b3629a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jTeyZkYKXSiLGyuPPTtSv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1516,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 24416,
      "output_tokens": 637,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1516,
          "output_tokens": 637,
          "cache_read_input_tokens": 24416,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1071
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

_source line 36 · 2026-05-19T21:05:49.769Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016Jh7xCQ4iT99SwT5Cp1fTn`</summary>

```json
{
  "query": "\"pessimistic reward\" \"step level\" \"process reward model\" defense RL training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ef20ddd-aca6-4c86-8eaa-d56e1b3629a8",
  "isSidechain": false,
  "requestId": "req_011CbCcC18MHyD6VcnsRFPu7",
  "type": "assistant",
  "uuid": "a167f960-f16d-4b9c-8922-b6873386770f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jTeyZkYKXSiLGyuPPTtSv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1516,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 24416,
      "output_tokens": 637,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1516,
          "output_tokens": 637,
          "cache_read_input_tokens": 24416,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1071
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

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "a167f960-f16d-4b9c-8922-b6873386770f",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration's causal effect on reward hacking resistance",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4"
}
```

---

### Tool result

_source line 39 · 2026-05-19T21:05:56.819Z_

<details><summary>↩ Tool result · `toolu_016p6Mv7Yr2V6x18wQZynbf6`</summary>

```text
Web search results for query: "calibration causally determines reward model robustness hackability causal link 2025 2026"

Links: [{"title":"[2506.16507] Robust Reward Modeling via Causal Rubrics","url":"https://arxiv.org/abs/2506.16507"},{"title":"Robust Reward Modeling via Causal Rubrics","url":"https://arxiv.org/pdf/2506.16507"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"Paper page - Robust Reward Modeling via Causal Rubrics","url":"https://huggingface.co/papers/2506.16507"},{"title":"Robust Reward Modeling for Large Language Models via Causal Decomposition","url":"https://arxiv.org/html/2604.13833"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://www.arxiv.org/pdf/2601.21350"}]

I found several recent research papers addressing causal approaches to reward model robustness. Here are the key findings:

## Main Results

A novel framework called Crome (Causally Robust Reward Modeling) has been introduced, grounded in an explicit causal model designed to mitigate reward hacking. Reward models tend to latch on to superficial or spurious attributes, such as response length or formatting, mistaking these cues learned from correlations in training data for the true causal drivers of quality.

Empirically, Crome significantly outperforms standard baselines on RewardBench, improving average accuracy by up to 5.4% and achieving gains of up to 13.2% and 7.2% in specific categories.

## Broader Causal Approaches

A factored causal representation learning method has shown that it learns more robust reward models and consistently improves downstream RLHF performance, with analyses validating effectiveness in mitigating reward hacking behaviors.

Additional research from 2026 has explored causal methods to handle unintentional artifacts, with some approaches reducing reward hacking by eliminating the causal edge from spurious artifacts to reward models.

These papers demonstrate active research into the causal links between model calibration, robustness against reward hacking, and reward model reliability in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ef20ddd-aca6-4c86-8eaa-d56e1b3629a8",
  "isSidechain": false,
  "promptId": "65edaaff-a340-4d92-8640-ce78a17faf26",
  "type": "user",
  "uuid": "9953b26e-59ec-4634-946a-aaf93710ebd0",
  "toolUseResult": {
    "query": "calibration causally determines reward model robustness hackability causal link 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YSVmDcRNJrvQGD8H1zLwG8",
        "content": [
          {
            "title": "[2506.16507] Robust Reward Modeling via Causal Rubrics",
            "url": "https://arxiv.org/abs/2506.16507"
          },
          {
            "title": "Robust Reward Modeling via Causal Rubrics",
            "url": "https://arxiv.org/pdf/2506.16507"
          },
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://arxiv.org/pdf/2601.21350"
          },
          {
            "title": "Paper page - Robust Reward Modeling via Causal Rubrics",
            "url": "https://huggingface.co/papers/2506.16507"
          },
          {
            "title": "Robust Reward Modeling for Large Language Models via Causal Decomposition",
            "url": "https://arxiv.org/html/2604.13833"
          },
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://www.arxiv.org/pdf/2601.21350"
          }
        ]
      },
      "I found several recent research papers addressing causal approaches to reward model robustness. Here are the key findings:\n\n## Main Results\n\nA novel framework called Crome (Causally Robust Reward Modeling) has been introduced, grounded in an explicit causal model designed to mitigate reward hacking. Reward models tend to latch on to superficial or spurious attributes, such as response length or formatting, mistaking these cues learned from correlations in training data for the true causal drivers of quality.\n\nEmpirically, Crome significantly outperforms standard baselines on RewardBench, improving average accuracy by up to 5.4% and achieving gains of up to 13.2% and 7.2% in specific categories.\n\n## Broader Causal Approaches\n\nA factored causal representation learning method has shown that it learns more robust reward models and consistently improves downstream RLHF performance, with analyses validating effectiveness in mitigating reward hacking behaviors.\n\nAdditional research from 2026 has explored causal methods to handle unintentional artifacts, with some approaches reducing reward hacking by eliminating the causal edge from spurious artifacts to reward models.\n\nThese papers demonstrate active research into the causal links between model calibration, robustness against reward hacking, and reward model reliability in 2025-2026."
    ],
    "durationSeconds": 7.367893615000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1ef20ddd-aca6-4c86-8eaa-d56e1b3629a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T21:05:59.471Z_

<details><summary>↩ Tool result · `toolu_016Jh7xCQ4iT99SwT5Cp1fTn`</summary>

```text
Web search results for query: ""pessimistic reward" "step level" "process reward model" defense RL training 2025 2026"

Links: [{"title":"SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning","url":"https://arxiv.org/pdf/2512.03244"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"Agentic Reinforcement Learning with Implicit Step Rewards","url":"https://arxiv.org/pdf/2509.19199"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/html/2505.20556"}]

I found several relevant papers on this topic. Here are the key results:

1. **"Learning a Pessimistic Reward Model in RLHF"** (May 2025, arxiv.org): This work demonstrates the feasibility of learning a pessimistic reward model against reward hacking, allowing agents to greedily search for policies with high pessimistic rewards without suffering from reward hacking.

2. **"SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning"** (2025, arxiv.org): This work discusses Process Reward Models (PRMs) that provide denser, step-level feedback to improve training stability and credit assignment.

3. **"Agentic Reinforcement Learning with Implicit Step Rewards"** (2025, arxiv.org): This paper proposes Online Learning Process Rewards (OPRL), a credit assignment strategy for LLM agents that trains a PRM alongside the policy using only on-policy trajectories and outcome preferences, updating the PRM with a DPO-derived objective.

These papers appear to address defense mechanisms in RL training through pessimistic reward modeling and step-level process reward models, which are techniques aimed at mitigating reward hacking and improving robustness during policy optimization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a167f960-f16d-4b9c-8922-b6873386770f",
  "isSidechain": false,
  "promptId": "65edaaff-a340-4d92-8640-ce78a17faf26",
  "type": "user",
  "uuid": "fa887505-8893-4be3-9bdb-7495e4225814",
  "toolUseResult": {
    "query": "\"pessimistic reward\" \"step level\" \"process reward model\" defense RL training 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MwqFFpvoz9dLqs5zwB1Qcg",
        "content": [
          {
            "title": "SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2512.03244"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/pdf/2505.20556"
          },
          {
            "title": "Agentic Reinforcement Learning with Implicit Step Rewards",
            "url": "https://arxiv.org/pdf/2509.19199"
          },
          {
            "title": "GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub",
            "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/html/2505.20556"
          }
        ]
      },
      "I found several relevant papers on this topic. Here are the key results:\n\n1. **\"Learning a Pessimistic Reward Model in RLHF\"** (May 2025, arxiv.org): This work demonstrates the feasibility of learning a pessimistic reward model against reward hacking, allowing agents to greedily search for policies with high pessimistic rewards without suffering from reward hacking.\n\n2. **\"SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning\"** (2025, arxiv.org): This work discusses Process Reward Models (PRMs) that provide denser, step-level feedback to improve training stability and credit assignment.\n\n3. **\"Agentic Reinforcement Learning with Implicit Step Rewards\"** (2025, arxiv.org): This paper proposes Online Learning Process Rewards (OPRL), a credit assignment strategy for LLM agents that trains a PRM alongside the policy using only on-policy trajectories and outcome preferences, updating the PRM with a DPO-derived objective.\n\nThese papers appear to address defense mechanisms in RL training through pessimistic reward modeling and step-level process reward models, which are techniques aimed at mitigating reward hacking and improving robustness during policy optimization."
    ],
    "durationSeconds": 9.699409643,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a167f960-f16d-4b9c-8922-b6873386770f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-19T21:06:27.452Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to write a comprehensive evaluation. Let me synthesize what I've learned:

## Key Findings

### Venue Mismatch (CRITICAL)
CoRL 2026 explicitly requires robotics focus: "Submissions should focus on a core robotics problem" and "Submissions without a robotics focus will be returned without review." This proposal is about PRM calibration for math reasoning - it has ZERO robotics content. This would almost certainly be desk-rejected.

### The Idea Itself
Let me evaluate the idea on its merits for a top ML venue (e.g., NeurIPS, ICML, ICLR):


The proposal rests on three main claims: that calibration and hackability are separate research problems, that better calibration directly prevents adversarial attacks, and that CGSP offers a novel defense mechanism. The core insight—that calibrated uncertainty makes models harder to exploit—feels somewhat intuitive and predictable. A reviewer could reasonably argue they'd expect this relationship without needing empirical validation. The CGSP formula itself appears incomplete in the thinking, but the novelty concern remains: the connection between calibration and robustness isn't particularly surprising.

The formula combines pessimistic reward shaping with calibration-weighted uncertainty, which is a fairly straightforward pairing of two well-established techniques. Recent work like "Caution" and "Learning a Pessimistic Reward Model in RLHF" already explore pessimism in similar contexts, so while the step-level application adds some freshness, it feels incremental. The causal isolation methodology stands out as the strongest contribution—using post-hoc calibration to cleanly separate calibration effects from representation changes is methodologically rigorous and non-obvious. The Hessian spectral analysis at the step level extends prior work but doesn't represent a major conceptual leap.

Temperature scaling alone might be sufficient to reduce hackability, and since the proposal already tests this simpler baseline, it raises whether the full machinery is necessary. Ensemble disagreement is another straightforward uncertainty proxy that's already well-studied. The research tackles a genuinely important problem in reward hacking, but framing this as bridging two threads oversells the novelty—the connection between calibration and robustness is fairly intuitive even if not formally established. The related work section is comprehensive but may be underweighting "Robust Reward Modeling via Causal Rubrics," which takes a similar causal angle on reward robustness, and "Learning a Pessimistic Reward Model in RLHF" deserves more emphasis given its direct relevance.

For CoRL specifically, the desk reject probability is extremely high—around 90% or more. If this were submitted to a general ML venue like NeurIPS, ICML, or ICLR instead, the novelty would be medium at best since the causal isolation methodology is useful but the core insight about calibration improving robustness isn't particularly surprising. The significance is medium-strong given the importance of the problem, and the experimental planning is thorough, but that core insight may not be novel enough for a top-tier venue. I'd estimate acceptance probability at 25-35% for a proper ML conference, though the venue mismatch with CoRL is the real issue here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa887505-8893-4be3-9bdb-7495e4225814",
  "isSidechain": false,
  "requestId": "req_011CbCcDpJnPTLfyFhESvWCQ",
  "type": "assistant",
  "uuid": "d583e500-942e-4f6e-8e98-87092d3b4ee3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNbFn5yepJ8w2boTwTkXEz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3352,
      "cache_read_input_tokens": 25487,
      "output_tokens": 5092,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3352,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5092,
          "cache_read_input_tokens": 25487,
          "cache_creation_input_tokens": 3352,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3352
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

_source line 42 · 2026-05-19T21:07:48.351Z_

Now I have sufficient information to write a comprehensive evaluation. Let me synthesize my findings.

---

```
【阶段】: Triage

⚠️ 关键前置问题：投稿目标 venue 严重不匹配
CoRL 2026 (Conference on Robot Learning) 的 Call for Papers 明确要求 "Submissions should focus on a core robotics problem" 且 "Submissions without a robotics focus will be returned without review." 本 proposal 关于 PRM 校准与数学推理中的 reward hacking，与机器人学习毫无关联。如投 CoRL，几乎必然 desk reject。以下评估假定投稿目标为匹配的 ML 主会（NeurIPS / ICML / ICLR），仅评估 idea 本身质量。

【领域调研】:
- [Tiwari et al., "Reward Under Attack" arXiv:2603.06621] (March 2026): 建立了 PRM 可被系统性利用的三层诊断框架（静态扰动/对抗 token/RL 诱导 hacking）。核心发现：GRPO 训练可将 PRM 奖励推至 >0.9 而实际准确率 <4%，43% 的奖励增益来自风格捷径。本 proposal 的攻击评估直接复用此框架。该论文未提出基于校准的防御。
- [Park et al., "Know What You Don't Know" arXiv:2506.09338] (NeurIPS 2025): 首次系统研究 PRM 校准问题，发现 PRM 系统性高估困难问题的成功概率，提出分位数回归校准 + instance-adaptive scaling (IAS)。未测试校准对鲁棒性/可利用性的影响。
- [Ma et al., "Distributional PRMs" arXiv:2605.06785] (May 2026): 使用条件最优传输实现校准的单调分位数函数，在 MATH-500 和 AIME 上改善了校准和 BoN 性能。同样未测试对抗鲁棒性。
- [Ackermann et al., "Gradient Regularization Prevents Reward Hacking" arXiv:2602.18037] (Feb 2026): 证明奖励面平坦度与准确性保持相关，提出梯度正则化。仅在 outcome-level RM 上工作，使用梯度范数（非 Hessian 谱），不涉及 step-level PRM。
- [Yu et al., "From Curiosity to Caution" arXiv:2604.04648] (April 2026): 对 BoN 使用悲观主义防御 reward hacking，基于预测误差（非校准概率）降低非典型响应的奖励估计。仅用于推理时 BoN，不涉及 RL 训练。
- ["Learning a Pessimistic Reward Model in RLHF" arXiv:2505.20556] (May 2025): 直接学习悲观奖励模型以抗击 reward hacking，允许贪婪搜索高悲观奖励的策略。在 outcome-level 工作。Proposal 未引用此文。
- ["Robust Reward Modeling via Causal Rubrics" arXiv:2506.16507] (2025): 使用因果模型 (Crome) 来缓解 reward hacking，在 RewardBench 上平均准确率提升 5.4%。从因果角度处理奖励鲁棒性，但不涉及校准-可利用性的因果链条。Proposal 未引用此文。
- ["Factored Causal Representation Learning for Robust Reward Modeling in RLHF" arXiv:2601.21350] (Jan 2026): 因果表征学习方法改善奖励模型鲁棒性。Proposal 未引用此文。
- ["Stop Summation: Min-Form Credit Assignment" arXiv:2504.15275] (April 2025): 将 PRM 的 credit assignment 从累加改为取最小值，显著缓解 reward hacking。Step-level 防御的替代思路。

- **调研总结**: PRM 校准（Park, Ma 等）和 PRM 可利用性（Tiwari 等）确实是两个相对独立的研究线索，proposal 对此定位基本准确。但 reward hacking 防御领域已有大量因果视角的工作（Crome、Factored Causal）和悲观主义防御工作（PET、Caution），且 Min-Form Credit Assignment 提供了一种更简洁的 step-level 防御思路。"校准→鲁棒性"的连接是自然且可预期的，尚无人做≠这个连接本身令人惊讶。

【Trivial Alternative 检验】:
存在显著的 trivial alternative 威胁：
1. **温度缩放 (Temperature Scaling)**：proposal 自己将其列为实验条件之一。如果仅通过一个标量参数的 post-hoc 校准（温度缩放）就能显著降低可利用性，那么整个 CGSP 机制的增量价值将大打折扣。温度缩放是最简单的校准方法，如果它 work，审稿人会质疑为何需要 CGSP。
2. **Min-Form Credit Assignment** (arXiv:2504.15275)：直接将 step reward 的累加改为取最小值，无需校准即可大幅减少 reward hacking。这是一个更简洁的 step-level 防御替代。
3. **简单 ensemble disagreement**：已被 Coste et al. 研究，作为 uncertainty proxy 无需校准即可提供悲观估计。

Proposal 的增量价值在于：(a) 因果隔离方法论——用 representation-preserving 的 post-hoc 校准来解耦校准效果和表征变化效果，这在方法论上是 clean 的；(b) CGSP 的"自适应"特性——根据校准质量 c_t 动态调节悲观程度。但如果 (a) 的结论是"校准确实有因果效应"，审稿人的反应可能是 "unsurprising"。

【前提假设检验】:
核心 claim 的逻辑链条中有以下未经验证的假设：

1. **"校准质量因果决定可利用性"的方向性假设**：proposal 假设校准→鲁棒性的因果方向。但更合理的假设可能是：表征质量同时决定了校准和鲁棒性（共同原因）。即使 post-hoc 校准实验确认"校准本身有因果效应"，效应量可能很小——因为 post-hoc 校准只改变 output mapping，不改变攻击者可利用的内部表征。梯度攻击直接操作 hidden states，而 post-hoc 校准的输出映射变换对此的防御机制不清晰。

2. **CGSP 的核心公式假设**：r̃_t = μ_t − α·σ_t/√c_t 假设 (a) 校准不确定性 σ_t 是可利用性的有效 proxy，(b) 除以 √c_t 是正确的 scaling，(c) 线性悲观调节足够。这些都是工程直觉，没有理论基础。特别是，c_t（基于 rolling buffer 的 inverse ECE）在 RL 训练的快速分布偏移中是否能可靠估计？

3. **"step-level 平坦度跨步骤复合"的假设**：proposal 假设 step-level Hessian 谱分析能揭示 outcome-level 可利用性的来源。但 T 个 step reward 的复合交互方式可能高度非线性，单个 step 的 Hessian 可能不足以解释 trajectory-level 行为。

【3 维度打分】:

1. **Novelty: 弱-中** — 
   核心洞察"校准好的模型更难被利用"在概念上是可预期的——一个完美校准的模型本质上就是其预测更准确，自然更难被攻击"骗"到。Proposal 的真正 novelty 在因果隔离方法论（post-hoc 校准保持表征），但这是一个实验设计层面的 contribution，不是 conceptual breakthrough。CGSP 是 pessimism（Caution, PET, arXiv:2505.20556 已广泛研究）+ calibration（Park et al., Ma et al. 已成熟）的自然组合。Step-level Hessian 分析是 Ackermann et al. 的增量扩展。审稿人极可能的反应："connecting calibration to robustness is natural and expected; the specific instantiation (CGSP) is one of many possible designs without principled justification for its form."

2. **Significance: 中** — 
   研究问题本身是重要的：PRM reward hacking 是阻碍 RL-based reasoning 提升的关键瓶颈（Tiwari et al. 的发现令人震惊）。但本 proposal 解决这个问题的角度（通过校准）可能并非最有效路径。Min-Form Credit Assignment、因果表征学习（Crome）、对抗训练（APRM）等替代方案各有优势。如果校准的因果效应确实存在但效应量小，整篇论文的实际影响力会受限。此外，结果主要在数学推理（MATH-500, AIME）上验证，可推广性有待检验。

3. **Related Work: 中** — 
   对 PRM 校准和 PRM 可利用性两个线索的覆盖比较充分。但缺失了几项直接相关的重要工作：(a) "Learning a Pessimistic Reward Model in RLHF" (arXiv:2505.20556) — 直接做悲观奖励建模防 hacking；(b) "Robust Reward Modeling via Causal Rubrics" (arXiv:2506.16507) — 因果视角的奖励鲁棒性；(c) "Factored Causal Representation Learning for Robust Reward Modeling" (arXiv:2601.21350) — 因果表征学习防 hacking；(d) "Stop Summation: Min-Form Credit Assignment" (arXiv:2504.15275) — 更简洁的 step-level 防御。这些遗漏会被审稿人注意到，尤其是 (a) 和 (d) 与 proposal 的定位直接竞争。

【概率估计】: [15% - 28%] 中位 22%
（注：此概率假设投稿到匹配的 ML 主会如 NeurIPS/ICML/ICLR。若投 CoRL 2026，概率接近 0%——几乎必然 desk reject。）

【估计理由】: 
idea 的核心洞察（校准→鲁棒性）在概念上可预期，不满足"审稿人会说 surprising"的标准，属于 rubric 中 15-25% 区间。因果隔离方法论有真实贡献将其拉向区间上界，但 trivial alternative 威胁（temperature scaling 可能就够了）和核心公式缺乏理论基础将其压回。上界主要受 Novelty 维度限制——即使实验执行完美，核心发现不太可能让审稿人觉得 surprising。Proposal 形式完善度很高（48 配置、causal isolation、Hessian 分析、CGSP + baselines），但形式完善度反映的是工程投入而非 idea 质量。

【主要风险】: 
1. **"Expected finding" 风险**：如果结果确认"校准越好越难被利用"，3 个审稿人中至少 1-2 个会写 "this is intuitive and expected"，这对 novelty 得分是致命的。反过来，如果结果是 negative（校准不影响鲁棒性），则整个 CGSP 防御失去理论基础。这是一个 dual-outcome 都不够 exciting 的局面。
2. **Trivial baseline 风险**：如果 temperature scaling（单参数）就能达到 CGSP 80%+ 的效果，审稿人会质疑 CGSP 的复杂度是否合理——"why not just temperature-scale your PRM?"
```

Sources:
- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)
- [Know What You Don't Know: Uncertainty Calibration of Process Reward Models](https://arxiv.org/abs/2506.09338)
- [Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport](https://arxiv.org/abs/2605.06785)
- [Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards](https://arxiv.org/abs/2602.18037)
- [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/abs/2604.04648)
- [Learning a Pessimistic Reward Model in RLHF](https://arxiv.org/pdf/2505.20556)
- [Robust Reward Modeling via Causal Rubrics](https://arxiv.org/abs/2506.16507)
- [Factored Causal Representation Learning for Robust Reward Modeling in RLHF](https://arxiv.org/pdf/2601.21350)
- [Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning](https://arxiv.org/pdf/2504.15275)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d583e500-942e-4f6e-8e98-87092d3b4ee3",
  "isSidechain": false,
  "requestId": "req_011CbCcDpJnPTLfyFhESvWCQ",
  "type": "assistant",
  "uuid": "5001ba6d-8bb5-4bb7-b33a-3ee36e57cb72",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNbFn5yepJ8w2boTwTkXEz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3352,
      "cache_read_input_tokens": 25487,
      "output_tokens": 5092,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3352,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5092,
          "cache_read_input_tokens": 25487,
          "cache_creation_input_tokens": 3352,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3352
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "5001ba6d-8bb5-4bb7-b33a-3ee36e57cb72",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration's causal effect on reward hacking resistance",
  "sessionId": "9aca3988-3e9a-4c46-b710-d33cd95d12d4"
}
```

---
