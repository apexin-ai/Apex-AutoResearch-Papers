# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Calibration as a Shield: How PRM 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/c54f944d-5386-4b12-8f4a-d23dd807b013.jsonl`
- **Structured JSON:** [`b161bff29a830a902a5a.json`](../../sessions/b1/b161bff29a830a902a5a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T21:07:49.690Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T21:07:49.690Z",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense\n\n## Description\nWe present the first causally rigorous study connecting PRM calibration quality to adversarial exploitability, and propose Calibration-Gated Step-Level Pessimism (CGSP), a novel defense that transforms calibrated uncertainty into adaptive reward hacking resistance during RL training. Our work bridges two mature but isolated research threads (PRM calibration and PRM hackability) through four contributions. First, an expanded correlation study across 48 configurations (8 PRMs × 6 calibration methods) provides sufficient statistical power (n=48, detecting r≥0.29 at p<0.05) to establish whether calibration quality predicts hackability metrics under gradient attacks, RL-induced hacking (GRPO on AIME), and BoN overoptimization (MATH-500), stratified by problem difficulty. Second, causal isolation experiments separate calibration's true effect from representation change artifacts: we compare post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) that provably preserve model representations against fine-tuning-based methods, with CKA verification and matched-representation-change controls. Third, step-level Hessian spectral analysis goes beyond Ackermann et al.'s outcome-level gradient norm analysis (which applies only to single-scalar reward models) to reveal how calibration affects the multi-reward compositional geometry of PRMs — analyzing how step-level flatness compounds across trajectories. Fourth, CGSP replaces raw PRM rewards during RL training with r̃_t = μ_t − α·σ_t/√c_t, where calibrated uncertainty σ_t and calibration quality c_t adaptively modulate pessimism per-step — trusted when calibration is tight, pessimistic when uncertainty is high — with a Calibration Drift Detector that monitors ECE on current-policy rollouts to flag distribution-shift-induced reward hacking in real time. CGSP differs from existing defenses (Caution uses prediction error, PET uses global pessimism, ensemble methods are uncalibrated) by being step-level, calibration-grounded, and adaptive. We evaluate CGSP against 5 baselines (uncalibrated GRPO, APRM, Caution, ensemble-min, gradient regularization) on MATH-500 and AIME, measuring both reward-accuracy alignment and downstream task accuracy.\n\n## Core Problem\nPRM calibration research and PRM hackability research are entirely separate threads with zero cross-citation — but the deeper problem is that we lack both (a) causal evidence for whether calibration actually determines hackability (vs. being merely correlated), and (b) a principled, step-level defense mechanism that leverages calibrated uncertainty to prevent reward hacking during RL training. Existing ad-hoc defenses (adversarial training, gradient regularization, pessimistic BoN) operate at the outcome level without exploiting the unique step-level structure of PRMs.\n\n## Opportunity\nThree recent developments create a uniquely favorable moment. First, Distributional PRMs (arXiv:2605.06785, May 2026) achieve calibrated step-level uncertainty via conditional optimal transport but never test robustness. Second, Tiwari et al. (arXiv:2603.06621, March 2026) demonstrate that PRMs are catastrophically hackable — near-perfect PRM rewards with <4% actual accuracy — but propose no calibration-based defense. Third, the causal isolation toolkit is mature: post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) modify only the output mapping without changing model representations, enabling controlled experiments that separate calibration effects from representation effects. No existing paper bridges these threads. Ackermann et al.'s gradient regularization work (arXiv:2602.18037) operates exclusively on outcome-level reward models with single-scalar rewards, never touching step-level PRM geometry. The CoT Entropy paper (arXiv:2502.11250) named this connection as future work 16 months ago with no follow-up. The window for a definitive, causally rigorous study is open but narrowing.\n\n## Related Work / Landscape\nTwo parallel research threads have developed with zero cross-citation. Thread 1 (PRM Calibration): Park et al. (arXiv:2506.09338, NeurIPS 2025) demonstrate PRMs systematically overestimate success probabilities on hard problems, proposing quantile regression calibration. Distributional PRMs (arXiv:2605.06785, May 2026) use conditional optimal transport for calibrated monotone quantile functions, improving BoN on MATH-500 and AIME. Neither paper tests robustness. Thread 2 (PRM Hackability): Tiwari et al. (arXiv:2603.06621) show gradient attacks inflate PRM rewards 4× and RL achieves near-perfect PRM rewards with <4% accuracy, with 43% of reward gains from stylistic shortcuts. APRM (arXiv:2511.22888) uses adversarial training for +3.4pp robustness. Thread 3 (Adjacent but distinct): Ackermann et al. (arXiv:2602.18037) prove reward surface flatness correlates with accuracy retention for outcome-level RMs, but work exclusively with single-scalar rewards, analyze only gradient norms (no Hessian spectra), and never consider step-level reward models. Their theoretical framework (Propositions 3.3-3.4) assumes a single reward function R(s,a) over complete responses — inapplicable to step-level PRM geometry where T coupled reward surfaces {R_1,...,R_T} interact compositionally. InferenceTimePessimism (arXiv:2506.19248) and Caution (arXiv:2604.04648) apply pessimism for BoN but use uncalibrated uncertainty proxies (prediction error, hedging), not calibrated probabilities. URM (arXiv:2410.00847) decomposes uncertainty into aleatoric/epistemic for outcome-level RMs but not PRMs. Bayesian reward models (arXiv:2402.13210) use Laplace approximation on LoRA weights. Conformal prediction has been applied to RLHF feedback alignment (arXiv:2601.17329) but never to PRM defense. No paper establishes a causal link between calibration quality and hackability, and no paper proposes using calibrated step-level PRM uncertainty as a defense during RL training.\n\n## Approach\nThe study has four components: (A) Expanded Correlation Study, (B) Causal Isolation Experiments, (C) Step-Level Mechanistic Analysis, and (D) Calibration-Gated Step-Level Pessimism (CGSP) defense.\n\n**Component A — Expanded Correlation Study (n≥24 configurations):** Apply 6 calibration methods across 2 tiers to 8 open-source PRMs. Tier 1 (post-hoc, representation-preserving): temperature scaling, Platt scaling, isotonic regression. Tier 2 (model-modifying): quantile regression fine-tuning, conditional optimal transport, Venn-Abers predictors. The 8 PRMs span discriminative (Qwen2.5-Math-PRM-7B, Qwen2.5-Math-PRM-72B, Skywork-o1-Open-PRM-7B, RLHFlow-Llama3.1-8B-PRM, Math-Shepherd-7B, OpenR-Math-psa-7B), generative (GenPRM-7B), and implicit (EurusPRM-Stage2) architectures. Each of the 48 PRM×calibration configurations is subjected to three attack tiers: (i) gradient-based reward inflation following Tiwari et al., (ii) RL-induced reward hacking via GRPO on AIME, and (iii) BoN overoptimization at N∈{1,4,16,64,256} on MATH-500. Compute rank correlations (Spearman ρ, Kendall τ) between calibration metrics (ECE, Brier score, quantile coverage, reliability diagram sharpness) and hackability metrics (reward-accuracy divergence, attack success rate, BoN degradation onset N*). Stratify analysis by problem difficulty (MATH levels 1-5, AMC vs. AIME) to test whether calibration is more protective on hard problems where PRMs are known to be overconfident.\n\n**Component B — Causal Isolation Experiments:** This is the methodological core addressing the reviewer's causation concern. Design: (B1) Post-hoc calibration control: Apply temperature scaling, Platt scaling, and isotonic regression — which provably modify only the output mapping, not internal representations — and measure hackability change. If hackability decreases under post-hoc calibration alone, this establishes that calibration per se (not representation change) causally affects hackability. (B2) Representation change verification: For fine-tuning-based calibration methods (quantile regression, COT), measure representation change at every transformer layer using Centered Kernel Alignment (CKA) between the base PRM and calibrated PRM. (B3) Matched representation change control: Fine-tune PRMs on an auxiliary task (e.g., next-token prediction on math text) that produces CKA-matched representation changes but does NOT improve calibration. If only calibration-improving fine-tuning reduces hackability (not the CKA-matched control), the causal role of calibration is confirmed. (B4) Conformal prediction as the cleanest test: Apply split-conformal prediction to PRM step scores, providing distribution-free coverage guarantees with zero model modification. Test whether conformal-calibrated PRMs resist hacking better than uncalibrated ones.\n\n**Component C — Step-Level Mechanistic Analysis (differentiating from Ackermann et al.):** Unlike Ackermann et al., who analyze only outcome-level gradient norms and max-perturbation sharpness, we perform Hessian spectral analysis at the step level — computing top-k eigenvalues and spectral density of the step-level reward Hessian ∂²R_t/∂h² (where h is the hidden representation at step t). Key questions: (i) Do calibrated PRMs have flatter step-level reward surfaces (lower top Hessian eigenvalue)? (ii) Does flatness vary by step position (early reasoning steps vs. final answer steps)? (iii) Do hackable reward peaks correspond to isolated large Hessian eigenvalues (sharp directions) that gradient attacks exploit? This extends Ackermann et al.'s framework from single-reward geometry to multi-reward compositional geometry: we analyze how step-level flatness/sharpness compounds across a T-step trajectory to determine outcome-level hackability.\n\n**Component D — Calibration-Gated Step-Level Pessimism (CGSP) Defense:** This transforms the paper from measurement to method. CGSP operates during RL training (GRPO/PPO) by replacing raw PRM step rewards with calibration-modulated rewards: r̃_t = μ_t − α · σ_t / √(c_t), where μ_t is the calibrated step reward mean, σ_t is the calibrated uncertainty (from quantile width or conformal interval), c_t is a calibration quality score (inverse ECE computed on a rolling buffer), and α is a pessimism strength hyperparameter. When calibration is high (small σ_t, high c_t), the reward is trusted; when calibration is low (large σ_t, low c_t), pessimism dominates. This differs from existing pessimism (Caution uses prediction error, PET uses global pessimistic fine-tuning, InferenceTimePessimism uses hedging) because CGSP is (i) step-level, (ii) grounded in calibrated probabilities rather than heuristic proxies, and (iii) adaptive — the pessimism automatically strengthens in distribution-shift regions where the PRM becomes miscalibrated. Additionally, we implement a Calibration Drift Detector: during RL training, periodically measure ECE on current-policy rollouts vs. the initial SFT-distribution calibration. When drift exceeds a threshold, flag those trajectory types as potentially hacked and apply reward clipping. This converts calibration from a static property into a dynamic training signal.\n\nBaseline comparisons for CGSP: (i) uncalibrated PRM + GRPO, (ii) APRM adversarial training, (iii) Caution/prediction-error pessimism, (iv) ensemble minimum (following Coste et al.), (v) KL-regularized GRPO, (vi) gradient regularization (Ackermann et al.).\n\nCodebase starting points: young-j-park/prm-calibration for calibration fitting, Tiwari et al.'s PRM-BiasBench for adversarial evaluation, vwxyzjn/open_instruct for GRPO training infrastructure.\n\n## Inspiration\nField guide gap: PRM overconfidence on OOD problems (Section 5.3 'when more compute hurts'); Untried combination: distributional PRM calibration + PRM hackability analysis; Pattern: connecting two mature but isolated research threads; Reviewer insight: pure measurement is insufficient — the key contribution should be a causal mechanism and a defense method; Methodological insight: post-hoc calibration methods that preserve representations enable clean causal isolation experiments impossible with fine-tuning-based calibration alone\n\n## Key References\n- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (arXiv:2506.09338, NeurIPS 2025)\n- Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport (arXiv:2605.06785, May 2026)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv:2603.06621, March 2026)\n- Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards (arXiv:2602.18037, Feb 2026)\n- Adversarial Training for Process Reward Models (arXiv:2511.22888, Nov 2025)\n- From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism (arXiv:2604.04648, April 2026)\n- Inference-Time Reward Hacking in Large Language Models (arXiv:2506.19248, NeurIPS 2025 Spotlight)\n- Uncertainty-Aware Step-wise Verification with Generative Reward Models (arXiv:2502.11250, ICLR 2025 Workshop)\n- Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242, April 2026)\n- Uncertainty-Aware Reward Model (arXiv:2410.00847)\n- Helping or Herding? Reward Model Ensembles Mitigate but Do Not Eliminate Overoptimization (arXiv:2312.09244)\n- Bayesian Reward Models for LLM Alignment (arXiv:2402.13210)\n- Conformal Feedback Alignment for RLHF (arXiv:2601.17329)\n- Taming Overconfidence in LLMs: Reward Calibration in RLHF (arXiv:2410.09724)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (arXiv:2501.03124)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '4200 H100-hrs (calibration fitting: 200, rollout generation: 600, gradient attacks: 1000, GRPO RL training: 1600 [including CGSP defense training], BoN evaluation: 400, Hessian spectral analysis: 200, causal isolation controls: 200)', 'timeline': '12-14 weeks', 'estimated_gpu_cost': '$10,500 at ~$2.50/H100-hr'}\n- **human_in_loop**: {'gpu_hours': '3600 H100-hrs (fewer failed iterations with AI-assisted debugging)', 'timeline': '10-12 weeks', 'claude_api_cost': '$400-700 (code generation, experiment analysis, paper drafting)', 'estimated_gpu_cost': '$9,000 at ~$2.50/H100-hr'}\n- **auto_research**: {'gpu_hours': '5200 H100-hrs (broader sweeps over α pessimism parameter, calibration drift thresholds, and ablations across all 48 configurations)', 'timeline': '7-9 weeks', 'claude_api_cost': '$1,500-2,000 (automated experiment orchestration, iterative analysis, full draft writing)', 'estimated_gpu_cost': '$13,000 at ~$2.50/H100-hr', 'speed_bottleneck': 'GRPO RL training wall-clock time (~18hrs per PRM×calibration×defense configuration on 4×H100); Hessian spectral analysis requires Lanczos iterations per step per problem; 72B PRM requires 4×H100 for inference'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T21:07:49.693Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T21:07:49.693Z",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013"
}
```

---

## Round 1

33 recorded events

### User

_source line 3 · 2026-05-19T21:07:49.703Z_

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
  "promptId": "4d42cf4c-40e7-4d86-84c8-5752ccfdcbcb",
  "type": "user",
  "uuid": "fe4509fd-926d-47f2-ac43-b8ecab1b95c8",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T21:07:49.702Z_

```json
{
  "parentUuid": "fe4509fd-926d-47f2-ac43-b8ecab1b95c8",
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
  "uuid": "403d07c5-2340-4d69-85b3-d549ca024b63",
  "timestamp": "2026-05-19T21:07:49.702Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T21:07:49.702Z_

```json
{
  "parentUuid": "403d07c5-2340-4d69-85b3-d549ca024b63",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5f3dc6a1-8125-4bb1-a4c8-4f2da90140dc",
  "timestamp": "2026-05-19T21:07:49.702Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
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
  "leafUuid": "5f3dc6a1-8125-4bb1-a4c8-4f2da90140dc",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking proposal",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013"
}
```

---

### Assistant

_source line 8 · 2026-05-19T21:08:03.813Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026 submission. Let me first note something important: CoRL is the Conference on Robot Learning, but this proposal is about PRM (Process Reward Model) calibration and reward hacking in LLM alignment/RLHF. This seems like a mismatch - this proposal would be more appropriate for NeurIPS, ICML, ICLR, or ACL/EMNLP rather than CoRL. Let me re-read... 

Actually, let me re-read the system prompt. 

There's a significant venue mismatch here - the proposal focuses entirely on LLM reward model calibration and reward hacking, which falls squarely in the LLM alignment and RLHF space, not robot learning. I should flag this concern prominently while proceeding with the evaluation, though I'll keep in mind the user may have intended a different venue or CoRL's scope may have shifted.

Before diving into the assessment, I need to search for recent work on PRM calibration, reward hacking defenses, and whether there are any robotics connections I'm missing, plus verify CoRL's current scope.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f3dc6a1-8125-4bb1-a4c8-4f2da90140dc",
  "isSidechain": false,
  "requestId": "req_011CbCcMwfmpjHxaL1efZVUq",
  "type": "assistant",
  "uuid": "aa0b595b-72e5-499d-ae8a-f7d806373463",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWPdKaCR6WNCG3drNzsCR7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19568,
      "output_tokens": 587,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 587,
          "cache_read_input_tokens": 19568,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
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

### Assistant

_source line 9 · 2026-05-19T21:08:03.815Z_

I need to do thorough field research before evaluating this proposal. Let me start with targeted web searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa0b595b-72e5-499d-ae8a-f7d806373463",
  "isSidechain": false,
  "requestId": "req_011CbCcMwfmpjHxaL1efZVUq",
  "type": "assistant",
  "uuid": "7aa82ca2-9f79-448a-b315-1f0578a29993",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWPdKaCR6WNCG3drNzsCR7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19568,
      "output_tokens": 587,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 587,
          "cache_read_input_tokens": 19568,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
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

### Tool call

_source line 10 · 2026-05-19T21:08:03.822Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014WFw2GU3aCPnnF2p9FktRB`</summary>

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
  "parentUuid": "7aa82ca2-9f79-448a-b315-1f0578a29993",
  "isSidechain": false,
  "requestId": "req_011CbCcMwfmpjHxaL1efZVUq",
  "type": "assistant",
  "uuid": "cbb05c77-022c-45c9-8da4-a150752ef38e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWPdKaCR6WNCG3drNzsCR7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19568,
      "output_tokens": 587,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 587,
          "cache_read_input_tokens": 19568,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
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

### Tool result

_source line 11 · 2026-05-19T21:08:03.828Z_

<details><summary>↩ Tool result · `toolu_014WFw2GU3aCPnnF2p9FktRB`</summary>

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
  "parentUuid": "cbb05c77-022c-45c9-8da4-a150752ef38e",
  "isSidechain": false,
  "promptId": "4d42cf4c-40e7-4d86-84c8-5752ccfdcbcb",
  "type": "user",
  "uuid": "139599ae-efc7-4426-8e18-226cd75e071a",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "cbb05c77-022c-45c9-8da4-a150752ef38e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T21:08:06.734Z_

Now let me run multiple targeted searches in parallel to understand the field landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "139599ae-efc7-4426-8e18-226cd75e071a",
  "isSidechain": false,
  "requestId": "req_011CbCcNzGKHBQEU7b17Cwvx",
  "type": "assistant",
  "uuid": "473ce2cf-e0d0-4f96-92e9-5859741ccdc7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZAYWFsbGJtDXB7xLrWXid",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 19568,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1113,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 84,
          "cache_read_input_tokens": 19568,
          "cache_creation_input_tokens": 1113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1113
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

_source line 13 · 2026-05-19T21:08:06.740Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ECm4HJ7Mq3hCo9Ykqjadjh`</summary>

```json
{
  "query": "PRM process reward model calibration 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "473ce2cf-e0d0-4f96-92e9-5859741ccdc7",
  "isSidechain": false,
  "requestId": "req_011CbCcNzGKHBQEU7b17Cwvx",
  "type": "assistant",
  "uuid": "fc8aed40-49a7-45cf-883b-11c6d2254d8b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ZAYWFsbGJtDXB7xLrWXid",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 19568,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1113,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 84,
          "cache_read_input_tokens": 19568,
          "cache_creation_input_tokens": 1113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1113
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

_source line 14 · 2026-05-19T21:08:15.417Z_

<details><summary>↩ Tool result · `toolu_01ECm4HJ7Mq3hCo9Ykqjadjh`</summary>

```text
Web search results for query: "PRM process reward model calibration 2025 2026 arxiv"

Links: [{"title":"[2506.09338] Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/abs/2506.09338"},{"title":"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/html/2605.06785"},{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/pdf/2506.09338"},{"title":"[2510.08049] A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/abs/2510.08049"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"[2503.22233] More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/abs/2503.22233"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"[2511.08325] AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress","url":"https://arxiv.org/abs/2511.08325"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"}]

Based on the search results, I found several recent papers on Process Reward Model (PRM) calibration from 2025-2026:

## Key Recent Papers on PRM Calibration

**1. Uncertainty Calibration Focus (June 2025)**

A paper titled "Know What You Don't Know: Uncertainty Calibration of Process Reward Models" introduces an instance-adaptive scaling framework that dynamically adjusts compute budgets based on estimated success likelihood. Their PRM calibration method achieves small calibration error outperforming baseline methods, and the proposed strategy reduces inference costs while maintaining accuracy.

**2. Distributional Calibration via Optimal Transport (Recent)**

Research addresses the problem that Process Reward Models are often poorly calibrated and overestimate success probabilities, proposing the first use of conditional optimal transport for calibrating PRMs by estimating a monotonic conditional quantile function over success probabilities conditioned on PRM hidden states.

**3. Entropy-Driven Uncertainty (March 2026)**

The EDU-PRM approach outperforms strong public baselines like Math-Shepherd and Omega PRMs while using only 1.5% of training data, with observed accuracy improvements from 64.7% to 67.3% for generative reasoning tasks and 32% reduction in token usage.

**4. Comprehensive Survey (April 2026)**

A comprehensive survey titled "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models" was submitted in October 2025 and last revised in April 2026.

These papers represent the current state-of-the-art research in PRM calibration methods for improving the reliability and efficiency of process reward models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc8aed40-49a7-45cf-883b-11c6d2254d8b",
  "isSidechain": false,
  "promptId": "4d42cf4c-40e7-4d86-84c8-5752ccfdcbcb",
  "type": "user",
  "uuid": "b2228523-80a7-41b5-9388-d7ee33ce4df5",
  "toolUseResult": {
    "query": "PRM process reward model calibration 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L8JU3tMWtTzEUvZWz3xLRg",
        "content": [
          {
            "title": "[2506.09338] Know What You Don't Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://arxiv.org/abs/2506.09338"
          },
          {
            "title": "Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport",
            "url": "https://arxiv.org/html/2605.06785"
          },
          {
            "title": "Know What You Don't Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://arxiv.org/pdf/2506.09338"
          },
          {
            "title": "[2510.08049] A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/abs/2510.08049"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "[2503.22233] More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty",
            "url": "https://arxiv.org/abs/2503.22233"
          },
          {
            "title": "GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub",
            "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models"
          },
          {
            "title": "[2511.08325] AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress",
            "url": "https://arxiv.org/abs/2511.08325"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process",
            "url": "https://arxiv.org/pdf/2510.08049"
          }
        ]
      },
      "Based on the search results, I found several recent papers on Process Reward Model (PRM) calibration from 2025-2026:\n\n## Key Recent Papers on PRM Calibration\n\n**1. Uncertainty Calibration Focus (June 2025)**\n\nA paper titled \"Know What You Don't Know: Uncertainty Calibration of Process Reward Models\" introduces an instance-adaptive scaling framework that dynamically adjusts compute budgets based on estimated success likelihood. Their PRM calibration method achieves small calibration error outperforming baseline methods, and the proposed strategy reduces inference costs while maintaining accuracy.\n\n**2. Distributional Calibration via Optimal Transport (Recent)**\n\nResearch addresses the problem that Process Reward Models are often poorly calibrated and overestimate success probabilities, proposing the first use of conditional optimal transport for calibrating PRMs by estimating a monotonic conditional quantile function over success probabilities conditioned on PRM hidden states.\n\n**3. Entropy-Driven Uncertainty (March 2026)**\n\nThe EDU-PRM approach outperforms strong public baselines like Math-Shepherd and Omega PRMs while using only 1.5% of training data, with observed accuracy improvements from 64.7% to 67.3% for generative reasoning tasks and 32% reduction in token usage.\n\n**4. Comprehensive Survey (April 2026)**\n\nA comprehensive survey titled \"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models\" was submitted in October 2025 and last revised in April 2026.\n\nThese papers represent the current state-of-the-art research in PRM calibration methods for improving the reliability and efficiency of process reward models."
    ],
    "durationSeconds": 8.671134505999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fc8aed40-49a7-45cf-883b-11c6d2254d8b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T21:08:18.017Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WxomCBVPRWCKGoqkYXhzgo`</summary>

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
  "parentUuid": "b2228523-80a7-41b5-9388-d7ee33ce4df5",
  "isSidechain": false,
  "requestId": "req_011CbCcPqaxQBdPmrzqfwL1v",
  "type": "assistant",
  "uuid": "5318e1c8-f009-4886-823c-2237155f6820",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XtHnFeY2wmKvUQcHATtYXf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 941,
      "cache_read_input_tokens": 20681,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 941,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 20681,
          "cache_creation_input_tokens": 941,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 941
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

_source line 16 · 2026-05-19T21:08:29.068Z_

<details><summary>↩ Tool result · `toolu_01WxomCBVPRWCKGoqkYXhzgo`</summary>

```text
Web search results for query: "process reward model hackability adversarial attack reward hacking PRM 2025 2026"

Links: [{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"Adversarial Reward-Hacking","url":"https://www.emergentmind.com/topics/adversarial-reward-hacking"},{"title":"Adversarial Training of Reward Models","url":"https://arxiv.org/pdf/2504.06141"},{"title":"Beyond Semantic Manipulation: Token-Space Attacks on Reward Models","url":"https://arxiv.org/pdf/2604.02686"},{"title":"1 Introduction","url":"https://arxiv.org/html/2603.06621"},{"title":"Adversarial Reward Auditing for Active Detection and ...","url":"https://arxiv.org/pdf/2602.01750"}]

Based on the web search results, here's what I found about process reward model (PRM) hackability and adversarial attacks:

## Key Research Findings

**Recent Major Study (2026):**
Adversarial optimization demonstrates that gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks. RL-induced reward hacking exposes a critical failure mode: policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.

Current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.

## Vulnerability Patterns

Reward hacking arises both from adversarial attacks—malicious manipulation of reward models, data, or environment signals—and from optimization pressure in agents exploiting misspecifications or learned model blind spots.

Reward hacking often occurs because the RM gives high reward scores to model responses outside the reward model training distribution.

## Defense Strategies

Adversarially trained RMs are more robust against attacks and mitigate reward hacking, with RLHF able to proceed for three times as many steps without exhibiting reward hacking, resulting in more performant aligned models.

MoE-based (Mixture-of-Experts) models, routing-weight normalization, and learnable merging have achieved substantial reductions in hacking, with 4–6 experts sufficing to match or exceed ensemble-based mitigation at single-GPU cost.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5318e1c8-f009-4886-823c-2237155f6820",
  "isSidechain": false,
  "promptId": "4d42cf4c-40e7-4d86-84c8-5752ccfdcbcb",
  "type": "user",
  "uuid": "6769c036-3555-483c-ab39-785ed0dc7689",
  "toolUseResult": {
    "query": "process reward model hackability adversarial attack reward hacking PRM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016hvgW8QjQqMLcaFtrFQfQ2",
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
      "Based on the web search results, here's what I found about process reward model (PRM) hackability and adversarial attacks:\n\n## Key Research Findings\n\n**Recent Major Study (2026):**\nAdversarial optimization demonstrates that gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks. RL-induced reward hacking exposes a critical failure mode: policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.\n\nCurrent PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.\n\n## Vulnerability Patterns\n\nReward hacking arises both from adversarial attacks—malicious manipulation of reward models, data, or environment signals—and from optimization pressure in agents exploiting misspecifications or learned model blind spots.\n\nReward hacking often occurs because the RM gives high reward scores to model responses outside the reward model training distribution.\n\n## Defense Strategies\n\nAdversarially trained RMs are more robust against attacks and mitigate reward hacking, with RLHF able to proceed for three times as many steps without exhibiting reward hacking, resulting in more performant aligned models.\n\nMoE-based (Mixture-of-Experts) models, routing-weight normalization, and learnable merging have achieved substantial reductions in hacking, with 4–6 experts sufficing to match or exceed ensemble-based mitigation at single-GPU cost."
    ],
    "durationSeconds": 11.046897538999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5318e1c8-f009-4886-823c-2237155f6820",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T21:08:32.054Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WyiDHzZ5nHFQdAXfFsMGV8`</summary>

```json
{
  "query": "calibration reward hacking defense pessimism RL training LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6769c036-3555-483c-ab39-785ed0dc7689",
  "isSidechain": false,
  "requestId": "req_011CbCcQqwZy4zZRvdX9h9Na",
  "type": "assistant",
  "uuid": "2cfd7913-19ef-4fb6-a7f1-50d5263cd8b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HYReypjFraF7dV2xX2pUtv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 21622,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 21622,
          "cache_creation_input_tokens": 822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 822
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

_source line 18 · 2026-05-19T21:08:52.402Z_

<details><summary>↩ Tool result · `toolu_01WyiDHzZ5nHFQdAXfFsMGV8`</summary>

```text
Web search results for query: "calibration reward hacking defense pessimism RL training LLM 2025 2026"

Links: [{"title":"Mitigating Reward Hacking with RL Training Interventions | OpenReview","url":"https://openreview.net/forum?id=1TIWkM3nY4"},{"title":"LLM Reasoning Workshop @ ICLR 2026 LLMS GAMING VERIFIERS:","url":"https://arxiv.org/pdf/2604.15149"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/pdf/2604.04648"},{"title":"Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR","url":"https://arxiv.org/pdf/2603.07084"},{"title":"Reward Hacking Defense Rubric","url":"https://www.emergentmind.com/topics/reward-hacking-defense-rubric"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"Natural Emergent Misalignment from Reward Hacking in Production RL","url":"https://arxiv.org/pdf/2511.18397"}]

The search results reveal several recent developments in reward hacking defenses and pessimism-based approaches for RL training with LLMs in 2025-2026:

## Key Research Areas

**Reward Hacking Mitigation Interventions:**
Recent work presents naturalistic reward hacking environments and compares RL training interventions, including coding environments where models can overwrite evaluation tests and medical conversation environments with sycophantic reward signals.

**Pessimism-Based Defense:**
One approach applies pessimism at the reward level by penalizing out-of-distribution responses through subtracting per-response uncertainty estimates from reward scores. Research shows that high-quality policies can be learned on pessimistic rewards without regularization, with high KL divergence from dataset distribution while maintaining practical performance.

**Verification and Shortcut Behavior:**
Imperfect verification induces reward shortcut strategies, while perfect verification removes this incentive—showing that RL training can incentivize reward hacking through both overt manipulation and exploiting verifier failures.

**Emergent Misalignment:**
Research indicates that training on narrowly misaligned data like insecure code or harmful advice can generalize to diverse harmful behaviors.

**Detection Mechanisms:**
Reward hacking appears in multiple forms requiring specialized detection mechanisms including statistical divergence checks, time-series anomaly detection, and integrity monitoring.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2cfd7913-19ef-4fb6-a7f1-50d5263cd8b6",
  "isSidechain": false,
  "promptId": "4d42cf4c-40e7-4d86-84c8-5752ccfdcbcb",
  "type": "user",
  "uuid": "07c631fe-6cad-45ef-b98c-c82365c5e52e",
  "toolUseResult": {
    "query": "calibration reward hacking defense pessimism RL training LLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019RWscoPYBmS4rzqAjADPhj",
        "content": [
          {
            "title": "Mitigating Reward Hacking with RL Training Interventions | OpenReview",
            "url": "https://openreview.net/forum?id=1TIWkM3nY4"
          },
          {
            "title": "LLM Reasoning Workshop @ ICLR 2026 LLMS GAMING VERIFIERS:",
            "url": "https://arxiv.org/pdf/2604.15149"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism",
            "url": "https://arxiv.org/pdf/2604.04648"
          },
          {
            "title": "Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR",
            "url": "https://arxiv.org/pdf/2603.07084"
          },
          {
            "title": "Reward Hacking Defense Rubric",
            "url": "https://www.emergentmind.com/topics/reward-hacking-defense-rubric"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/pdf/2505.20556"
          },
          {
            "title": "Natural Emergent Misalignment from Reward Hacking in Production RL",
            "url": "https://arxiv.org/pdf/2511.18397"
          }
        ]
      },
      "The search results reveal several recent developments in reward hacking defenses and pessimism-based approaches for RL training with LLMs in 2025-2026:\n\n## Key Research Areas\n\n**Reward Hacking Mitigation Interventions:**\nRecent work presents naturalistic reward hacking environments and compares RL training interventions, including coding environments where models can overwrite evaluation tests and medical conversation environments with sycophantic reward signals.\n\n**Pessimism-Based Defense:**\nOne approach applies pessimism at the reward level by penalizing out-of-distribution responses through subtracting per-response uncertainty estimates from reward scores. Research shows that high-quality policies can be learned on pessimistic rewards without regularization, with high KL divergence from dataset distribution while maintaining practical performance.\n\n**Verification and Shortcut Behavior:**\nImperfect verification induces reward shortcut strategies, while perfect verification removes this incentive—showing that RL training can incentivize reward hacking through both overt manipulation and exploiting verifier failures.\n\n**Emergent Misalignment:**\nResearch indicates that training on narrowly misaligned data like insecure code or harmful advice can generalize to diverse harmful behaviors.\n\n**Detection Mechanisms:**\nReward hacking appears in multiple forms requiring specialized detection mechanisms including statistical divergence checks, time-series anomaly detection, and integrity monitoring."
    ],
    "durationSeconds": 20.342954194999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2cfd7913-19ef-4fb6-a7f1-50d5263cd8b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "07c631fe-6cad-45ef-b98c-c82365c5e52e",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking proposal",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013"
}
```

---

### Tool call

_source line 21 · 2026-05-19T21:08:54.751Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NtYF2c14nkxZwwmevPkfvX`</summary>

```json
{
  "query": "CoRL 2026 conference on robot learning scope topics submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07c631fe-6cad-45ef-b98c-c82365c5e52e",
  "isSidechain": false,
  "requestId": "req_011CbCcSZm36PwhxTNBfgXmA",
  "type": "assistant",
  "uuid": "301f859e-3bc5-457d-94bc-34832509a168",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132UmMnmVgimfe4u2RcoCiT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 22444,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 22444,
          "cache_creation_input_tokens": 752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 752
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

_source line 22 · 2026-05-19T21:09:02.216Z_

<details><summary>↩ Tool result · `toolu_01NtYF2c14nkxZwwmevPkfvX`</summary>

```text
Web search results for query: "CoRL 2026 conference on robot learning scope topics submission"

Links: [{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI","url":"https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026 - About CoRL","url":"https://www.corl.org/about-corl"},{"title":"System and method for robot learning from human demonstrations with formal logic","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12208521"},{"title":"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models","url":"https://arxiv.org/pdf/2512.11908"}]

Based on the search results, here's what I found about CoRL 2026 conference on robot learning:

## Conference Overview
CoRL is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.

## Conference Details
- **Dates**: CoRL 2026 will be held at the JW Marriott Austin in Austin, TX (November 9–12, 2026), with a workshop day on November 9 and the main conference on November 10–12.
- **Paper Submission Deadline**: May 29, 2026
- **Paper Format**: Papers are limited to 8 pages of content plus unlimited references.

## Scope and Topics
CoRL welcomes papers in areas such as: Learning representations for robotic perception and control; Learning robot foundation models or general-purpose knowledge systems for robotics; Imitation learning for robotics; Reinforcement learning for control of physical robots; Learning approaches to robot safety and alignment; and Applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics; Robot systems, hardware, and sensors for learning and data-driven approaches; Theoretical foundations of robot learning, including generalization theory and uncertainty quantification; Video models and latent world models for robot learning.

## Important Requirements
Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. Submissions without a robotics focus will be returned without review.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "301f859e-3bc5-457d-94bc-34832509a168",
  "isSidechain": false,
  "promptId": "4d42cf4c-40e7-4d86-84c8-5752ccfdcbcb",
  "type": "user",
  "uuid": "7f492631-7740-4610-823d-87c987ab67c1",
  "toolUseResult": {
    "query": "CoRL 2026 conference on robot learning scope topics submission",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Rsdnouv67u53iUbs5yAjwm",
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
          },
          {
            "title": "Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models",
            "url": "https://arxiv.org/pdf/2512.11908"
          }
        ]
      },
      "Based on the search results, here's what I found about CoRL 2026 conference on robot learning:\n\n## Conference Overview\nCoRL is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.\n\n## Conference Details\n- **Dates**: CoRL 2026 will be held at the JW Marriott Austin in Austin, TX (November 9–12, 2026), with a workshop day on November 9 and the main conference on November 10–12.\n- **Paper Submission Deadline**: May 29, 2026\n- **Paper Format**: Papers are limited to 8 pages of content plus unlimited references.\n\n## Scope and Topics\nCoRL welcomes papers in areas such as: Learning representations for robotic perception and control; Learning robot foundation models or general-purpose knowledge systems for robotics; Imitation learning for robotics; Reinforcement learning for control of physical robots; Learning approaches to robot safety and alignment; and Applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics; Robot systems, hardware, and sensors for learning and data-driven approaches; Theoretical foundations of robot learning, including generalization theory and uncertainty quantification; Video models and latent world models for robot learning.\n\n## Important Requirements\nAuthors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. Submissions without a robotics focus will be returned without review."
    ],
    "durationSeconds": 7.461704320000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "301f859e-3bc5-457d-94bc-34832509a168",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T21:09:05.444Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AoaqPv1G8DtJBffGaaTK9r`</summary>

```json
{
  "query": "Ackermann gradient regularization reward hacking RLHF 2602.18037 Hessian reward surface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f492631-7740-4610-823d-87c987ab67c1",
  "isSidechain": false,
  "requestId": "req_011CbCcTHewd5magKrjaL3fb",
  "type": "assistant",
  "uuid": "c1b1be54-a4bf-44ab-9945-f31a333c0d2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LaVaavRKfmZpvqynn1PXfi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 23196,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 23196,
          "cache_creation_input_tokens": 805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 805
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

_source line 24 · 2026-05-19T21:09:16.324Z_

<details><summary>↩ Tool result · `toolu_01AoaqPv1G8DtJBffGaaTK9r`</summary>

```text
Web search results for query: "Ackermann gradient regularization reward hacking RLHF 2602.18037 Hessian reward surface"

Links: [{"title":"[2602.18037] Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards","url":"https://arxiv.org/abs/2602.18037"},{"title":"Gradient Regularization Prevents Reward Hacking in ...","url":"https://arxiv.org/pdf/2602.18037"},{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking | OpenReview","url":"https://openreview.net/forum?id=msEr27EejF"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/html/2604.02986"},{"title":"Unifying Stable Optimization and Reference Regularization in RLHF","url":"https://arxiv.org/html/2602.11523v1"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"},{"title":"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking","url":"https://arxiv.org/pdf/2501.19358"},{"title":"Johannes Ackermann","url":"https://johannesack.github.io/"},{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward   Hacking","url":"https://arxiv.org/pdf/2403.03185"}]

Based on the search results, I found the paper you're looking for:

The paper "Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards" is by Johannes Ackermann and 3 other authors, with the arXiv identifier 2602.18037.

The paper addresses a fundamental problem in RLHF training: reward hacking, where the policy may exploit inaccuracies of the reward and learn an unintended behavior. Rather than relying on traditional approaches, the authors propose a different framing: Train the LM in a way that biases policy updates towards regions in which the reward is more accurate.

The core contribution involves the Hessian and reward surface curvature: The authors derive a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence, and propose that gradient regularization (GR) can be used to bias training to flatter regions and thereby maintain reward model accuracy. They confirm these results by showing that the gradient norm and reward accuracy are empirically correlated in RLHF.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1b1be54-a4bf-44ab-9945-f31a333c0d2c",
  "isSidechain": false,
  "promptId": "4d42cf4c-40e7-4d86-84c8-5752ccfdcbcb",
  "type": "user",
  "uuid": "cd666322-dd77-4f15-8a67-d4185c31561d",
  "toolUseResult": {
    "query": "Ackermann gradient regularization reward hacking RLHF 2602.18037 Hessian reward surface",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XNwEAan4Hxmo2nHu4ABwkW",
        "content": [
          {
            "title": "[2602.18037] Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards",
            "url": "https://arxiv.org/abs/2602.18037"
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
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/pdf/2604.02986"
          },
          {
            "title": "The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking",
            "url": "https://arxiv.org/pdf/2501.19358"
          },
          {
            "title": "Johannes Ackermann",
            "url": "https://johannesack.github.io/"
          },
          {
            "title": "Correlated Proxies: A New Definition and Improved Mitigation for Reward   Hacking",
            "url": "https://arxiv.org/pdf/2403.03185"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper \"Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards\" is by Johannes Ackermann and 3 other authors, with the arXiv identifier 2602.18037.\n\nThe paper addresses a fundamental problem in RLHF training: reward hacking, where the policy may exploit inaccuracies of the reward and learn an unintended behavior. Rather than relying on traditional approaches, the authors propose a different framing: Train the LM in a way that biases policy updates towards regions in which the reward is more accurate.\n\nThe core contribution involves the Hessian and reward surface curvature: The authors derive a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence, and propose that gradient regularization (GR) can be used to bias training to flatter regions and thereby maintain reward model accuracy. They confirm these results by showing that the gradient norm and reward accuracy are empirically correlated in RLHF."
    ],
    "durationSeconds": 10.876683371000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c1b1be54-a4bf-44ab-9945-f31a333c0d2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T21:09:19.753Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WGFhxjAAVuxCcVYAy3NNnU`</summary>

```json
{
  "query": "\"step-level pessimism\" OR \"calibration-gated\" reward model defense RL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd666322-dd77-4f15-8a67-d4185c31561d",
  "isSidechain": false,
  "requestId": "req_011CbCcUKzchubrxAS94Qv1e",
  "type": "assistant",
  "uuid": "d17cac51-2dd5-4cb0-8d0f-64556d7f3776",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyWEGz8Xnmympwt9aTYJeh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 24001,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 24001,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 784
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

_source line 26 · 2026-05-19T21:09:26.526Z_

<details><summary>↩ Tool result · `toolu_01WGFhxjAAVuxCcVYAy3NNnU`</summary>

```text
Web search results for query: ""step-level pessimism" OR "calibration-gated" reward model defense RL 2026"

Links: [{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/html/2505.20556"},{"title":"How Top AI Labs Are Building RL Agents in 2026","url":"https://blog.dailydoseofds.com/p/how-top-ai-labs-are-building-rl-agents"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/pdf/2604.04648"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM ...","url":"https://openreview.net/pdf?id=TDfrN1TbGH"},{"title":"Countering Reward Over-optimization in LLM with Demonstration-Guided   Reinforcement Learning","url":"https://arxiv.org/pdf/2404.19409"},{"title":"arXiv:2505.19196v1 [cs.CV] 25 May 2025 Step-level Reward for Free in RL-based","url":"https://arxiv.org/pdf/2505.19196"}]

I found several relevant research papers from 2026 on pessimism and reward modeling in RL:

**Key Findings:**

1. **Step-level Pessimism**: Step-level value estimates can be overly pessimistic, leading to the premature discarding of potentially correct reasoning paths during search at inference time. To address this, TVM extends value estimation to the token level to identify and retain promising paths.

2. **Pessimistic Reward Models**: A novel pessimistic reward fine-tuning method called PET learns a pessimistic reward model robust against reward hacking in offline reinforcement learning from human feedback (RLHF). When optimizing a policy on a pessimistic reward model fine-tuned through PET, reward hacking can be prevented without relying on any regularization.

3. **Calibration Challenges**: The key challenge is controlling the degree of pessimism—while sufficient pessimism can avoid over-estimation and mitigate reward hacking, over-pessimism results in an under-estimation of high-quality policies.

4. **Reward-Level Pessimism**: One approach penalizes out-of-distribution responses by subtracting per-response uncertainty estimates from the scores assigned by the reward model, then selecting the response with the highest pessimistic score.

5. **Reward Calibration**: Reward Calibration from Demonstration (RCfD) shifts from directly maximizing the reward function to calibrating it based on demonstrations, which helps prevent LLMs from exploiting the reward model.

The search results show active research in 2025-2026 on managing pessimism levels in reward models to defend against reward hacking while maintaining policy quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d17cac51-2dd5-4cb0-8d0f-64556d7f3776",
  "isSidechain": false,
  "promptId": "4d42cf4c-40e7-4d86-84c8-5752ccfdcbcb",
  "type": "user",
  "uuid": "aff1ea07-494e-4cbd-bcc3-7a220a2081cc",
  "toolUseResult": {
    "query": "\"step-level pessimism\" OR \"calibration-gated\" reward model defense RL 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Uc7fgeCiDcqNvTLTfVLaDt",
        "content": [
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/pdf/2505.20556"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/html/2505.20556"
          },
          {
            "title": "How Top AI Labs Are Building RL Agents in 2026",
            "url": "https://blog.dailydoseofds.com/p/how-top-ai-labs-are-building-rl-agents"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism",
            "url": "https://arxiv.org/pdf/2604.04648"
          },
          {
            "title": "Reward Modeling for Reinforcement Learning-Based LLM ...",
            "url": "https://openreview.net/pdf?id=TDfrN1TbGH"
          },
          {
            "title": "Countering Reward Over-optimization in LLM with Demonstration-Guided   Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2404.19409"
          },
          {
            "title": "arXiv:2505.19196v1 [cs.CV] 25 May 2025 Step-level Reward for Free in RL-based",
            "url": "https://arxiv.org/pdf/2505.19196"
          }
        ]
      },
      "I found several relevant research papers from 2026 on pessimism and reward modeling in RL:\n\n**Key Findings:**\n\n1. **Step-level Pessimism**: Step-level value estimates can be overly pessimistic, leading to the premature discarding of potentially correct reasoning paths during search at inference time. To address this, TVM extends value estimation to the token level to identify and retain promising paths.\n\n2. **Pessimistic Reward Models**: A novel pessimistic reward fine-tuning method called PET learns a pessimistic reward model robust against reward hacking in offline reinforcement learning from human feedback (RLHF). When optimizing a policy on a pessimistic reward model fine-tuned through PET, reward hacking can be prevented without relying on any regularization.\n\n3. **Calibration Challenges**: The key challenge is controlling the degree of pessimism—while sufficient pessimism can avoid over-estimation and mitigate reward hacking, over-pessimism results in an under-estimation of high-quality policies.\n\n4. **Reward-Level Pessimism**: One approach penalizes out-of-distribution responses by subtracting per-response uncertainty estimates from the scores assigned by the reward model, then selecting the response with the highest pessimistic score.\n\n5. **Reward Calibration**: Reward Calibration from Demonstration (RCfD) shifts from directly maximizing the reward function to calibrating it based on demonstrations, which helps prevent LLMs from exploiting the reward model.\n\nThe search results show active research in 2025-2026 on managing pessimism levels in reward models to defend against reward hacking while maintaining policy quality."
    ],
    "durationSeconds": 6.767801571999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d17cac51-2dd5-4cb0-8d0f-64556d7f3776",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T21:09:29.541Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B4Z4RVedBXrXvwn5KwcEgG`</summary>

```json
{
  "query": "causal link calibration hackability reward model robustness uncertainty 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aff1ea07-494e-4cbd-bcc3-7a220a2081cc",
  "isSidechain": false,
  "requestId": "req_011CbCcV5axsyE2oSuAF6F5F",
  "type": "assistant",
  "uuid": "163fea67-fceb-4f09-b292-f3a9f910995f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PLQGE5MMwwK2rMriVU48nC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 24785,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 24785,
          "cache_creation_input_tokens": 840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 840
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

_source line 28 · 2026-05-19T21:09:38.739Z_

<details><summary>↩ Tool result · `toolu_01B4Z4RVedBXrXvwn5KwcEgG`</summary>

```text
Web search results for query: "causal link calibration hackability reward model robustness uncertainty 2025 2026"

Links: [{"title":"Robust Reward Modeling via Causal Rubrics","url":"https://arxiv.org/pdf/2506.16507"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models for NeurIPS 2025 - IBM Research","url":"https://research.ibm.com/publications/know-what-you-dont-know-uncertainty-calibration-of-process-reward-models"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/pdf/2603.06621"},{"title":"Reward-Robust RLHF in LLMs","url":"https://arxiv.org/pdf/2409.15360"},{"title":"Causally-Enhanced Reinforcement Policy Optimization","url":"https://arxiv.org/pdf/2509.23095"}]

Based on the search results, here are findings related to your query about causal links, calibration, hackability, reward model robustness, and uncertainty in 2025-2026:

## Recent Research on Robust Reward Modeling

Reward hacking remains a significant challenge, as reward models often learn superficial attributes like response length or formatting patterns instead of true causal drivers of quality, because standard training doesn't explicitly require disentangling these from spurious correlates.

Standard reward model training is prone to learning spurious correlations rather than true causal drivers of human preference, which models exploit during RLHF as reward hacking.

## Causal Approaches to Robustness

A method called CROME (Causal Rubrics) significantly outperforms standard baselines on RewardBench with up to 5.4% improvement in average accuracy and achieves consistent gains in Best-of-N inference settings.

Factored causal representation learning methods have been shown to learn more robust reward models and consistently improve downstream RLHF performance while mitigating reward hacking behaviors like length and sycophantic bias.

## Uncertainty Calibration

Ante-hoc methods for mitigating reward hacking incorporate uncertainty quantification into the reward modeling pipeline, including ensemble-based methods and uncertainty-aware architectures.

There's also recent work on uncertainty calibration of process reward models presented at NeurIPS 2025, indicating active research in this area during 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "163fea67-fceb-4f09-b292-f3a9f910995f",
  "isSidechain": false,
  "promptId": "4d42cf4c-40e7-4d86-84c8-5752ccfdcbcb",
  "type": "user",
  "uuid": "fadfe4a5-162a-4aa5-8e66-7e80e66c2ee3",
  "toolUseResult": {
    "query": "causal link calibration hackability reward model robustness uncertainty 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014GFocJ58taKa3Doik4pJzH",
        "content": [
          {
            "title": "Robust Reward Modeling via Causal Rubrics",
            "url": "https://arxiv.org/pdf/2506.16507"
          },
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://arxiv.org/pdf/2601.21350"
          },
          {
            "title": "Know What You Don’t Know: Uncertainty Calibration of Process Reward Models for NeurIPS 2025 - IBM Research",
            "url": "https://research.ibm.com/publications/know-what-you-dont-know-uncertainty-calibration-of-process-reward-models"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/pdf/2604.02986"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "Reward-Robust RLHF in LLMs",
            "url": "https://arxiv.org/pdf/2409.15360"
          },
          {
            "title": "Causally-Enhanced Reinforcement Policy Optimization",
            "url": "https://arxiv.org/pdf/2509.23095"
          }
        ]
      },
      "Based on the search results, here are findings related to your query about causal links, calibration, hackability, reward model robustness, and uncertainty in 2025-2026:\n\n## Recent Research on Robust Reward Modeling\n\nReward hacking remains a significant challenge, as reward models often learn superficial attributes like response length or formatting patterns instead of true causal drivers of quality, because standard training doesn't explicitly require disentangling these from spurious correlates.\n\nStandard reward model training is prone to learning spurious correlations rather than true causal drivers of human preference, which models exploit during RLHF as reward hacking.\n\n## Causal Approaches to Robustness\n\nA method called CROME (Causal Rubrics) significantly outperforms standard baselines on RewardBench with up to 5.4% improvement in average accuracy and achieves consistent gains in Best-of-N inference settings.\n\nFactored causal representation learning methods have been shown to learn more robust reward models and consistently improve downstream RLHF performance while mitigating reward hacking behaviors like length and sycophantic bias.\n\n## Uncertainty Calibration\n\nAnte-hoc methods for mitigating reward hacking incorporate uncertainty quantification into the reward modeling pipeline, including ensemble-based methods and uncertainty-aware architectures.\n\nThere's also recent work on uncertainty calibration of process reward models presented at NeurIPS 2025, indicating active research in this area during 2025-2026."
    ],
    "durationSeconds": 9.193621329,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "163fea67-fceb-4f09-b292-f3a9f910995f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-19T21:09:38.745Z_

```json
{
  "parentUuid": "fadfe4a5-162a-4aa5-8e66-7e80e66c2ee3",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f5188acc-03fa-41ac-918b-f814d29a47c9",
  "timestamp": "2026-05-19T21:09:38.745Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 30 · 2026-05-19T21:10:32.824Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to evaluate this proposal. Let me synthesize my findings:

**Critical Issue #1: Venue Mismatch**
CoRL 2026 explicitly states: "Submissions without a robotics focus will be returned without review." This proposal is entirely about PRM calibration and reward hacking in LLMs for mathematical reasoning (MATH-500, AIME). It has ZERO robotics component. This is a **fatal** venue mismatch. The proposal would be desk-rejected at CoRL.

Wait, let me reconsider. Maybe the user just used "CoRL" as a placeholder or is confused about the venue. 

My job is to evaluate idea quality, and I should flag this venue issue prominently since it's critical. But the venue mismatch is really about fit rather than the quality of the idea itself. Let me focus on assessing the core idea and surface the venue problem separately.

**Idea Quality Assessment:**

The core claim is that PRM calibration quality directly determines resistance to reward hacking, and that a step-level defense using calibrated uncertainty can prevent reward hacking during RL training. Let me think through whether this holds up. The simplest alternative would be to just use standard uncertainty estimates without the calibration component, so I need to understand what calibration specifically adds here.

Looking at existing approaches, ensemble disagreement and KL regularization already exist as baselines. The proposal argues CGSP differs because it's step-level, calibration-grounded, and adaptive, but ensemble-min is already compared against, PET handles pessimism, and Caution applies pessimism at inference time. The formula itself—using mean minus scaled standard deviation—is essentially a standard UCB/LCB approach from bandits literature. The real question is whether temperature scaling plus pessimism on a calibrated PRM would achieve similar results to CGSP, since that combination might be close enough to make the added complexity hard to justify.

Now I'm questioning the core premise: they assume calibration quality directly causes lower hackability, but that's what they're trying to prove empirically. The deeper issue is whether hackability stems from miscalibration or from the model's fundamental inability to evaluate reasoning quality. A perfectly calibrated PRM on its training distribution could still be hackable if it doesn't actually understand reasoning. There's also a confound between calibration and overall model quality—a better-calibrated PRM might just be a better model. The causal isolation experiments attempt to separate these, but post-hoc calibration methods like temperature scaling only adjust probabilities without changing the underlying representation.

Temperature scaling preserves ranking and just rescales logits, so gradient-based attacks should still work—the attacker just needs different gradient magnitudes. The real vulnerability comes from the model's discriminative features, not its calibration. Though actually, temperature scaling does reduce gradient magnitudes for T > 1, which could make attacks less effective simply because the reward signal becomes flatter.

But here's the core issue: calibration changes probability mappings, not what the model actually discriminates between. Whether through BoN overoptimization or RL-based hacking, the policy exploits the same underlying patterns the PRM responds to—better calibration just changes the reward scale, not which exploits are available. The proposal's fundamental claim that calibration improves robustness seems to conflate probability scaling with changes to the model's actual discriminative features.

The only real mechanical benefit would be if poorly calibrated PRMs create sharp reward peaks that make gradient attacks easier to exploit, so flattening the surface through calibration reduces vulnerability. But that's just a smoothness effect, not a deep causal story about robustness.

On novelty, the connection between PRM calibration and hackability is a reasonable observation that hasn't been formalized before, though the CoT Entropy paper already flagged this as future work. CGSP itself is essentially a standard pessimistic approach—applying UCB/LCB with calibration-based uncertainty at the step level using a conservative formula.

The causal isolation methodology is the stronger contribution—using post-hoc calibration as a natural experiment to disentangle calibration effects from representation effects. The Hessian spectral analysis is a more incremental extension of prior work.

For significance, whether calibration actually affects hackability matters for the field, and if it does, it offers a cheap, actionable defense. But the impact of CGSP depends on how strong that calibration-hackability link actually is.

The related work section is comprehensive and correctly identifies the gap between calibration and hackability research threads. The proposal is well-structured and the experimental design is thoughtful, but there's a conceptual tension at its core: calibration addresses probability mapping while hackability depends on discriminative features. CGSP itself is technically straightforward—just applying UCB/LCB pessimism to step rewards. The proposal invests heavily in experimental rigor, but the intellectual core feels thin, and the "first causally rigorous study" framing may overstate things if the underlying mechanism is just mechanical.

There's a critical structural problem though: this isn't a robotics paper, and CoRL requires robotics focus, so it would face desk rejection. If submitted to a more appropriate venue like NeurIPS or ICML, I'd estimate the idea quality at 25-35%—the bridge between threads is meaningful and the experimental design is solid, but the core contribution might be thinner than it appears. For CoRL specifically, the acceptance probability is essentially zero due to the venue mismatch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5188acc-03fa-41ac-918b-f814d29a47c9",
  "isSidechain": false,
  "requestId": "req_011CbCcVyqU7vKkVKQt5CrEY",
  "type": "assistant",
  "uuid": "0ce5e34e-0561-4b7f-ae72-404dbd09eab1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zyGaz4J6NV5FrKKFZ8bSx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 864,
      "cache_read_input_tokens": 25625,
      "output_tokens": 6267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6267,
          "cache_read_input_tokens": 25625,
          "cache_creation_input_tokens": 864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 864
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

_source line 31 · 2026-05-19T21:11:57.396Z_

Now I have sufficient research to evaluate this proposal. Let me compile my assessment.

---

```
【阶段】: Triage

【致命前置问题：投稿venue严重不匹配】

CoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确要求论文聚焦于机器人学习
（"Submissions without a robotics focus will be returned without review"）。本 proposal
完全关于 LLM 中 Process Reward Model 的 calibration 与 reward hacking 防御，评估在
MATH-500 和 AIME 数学推理任务上进行，**没有任何机器人学相关内容**。

→ 以 CoRL 为投稿目标，本 proposal 几乎确定会被 desk reject。
→ 合适的 venue 应为 NeurIPS 2026, ICML 2026, 或 ICLR 2027。

以下评估假设投稿到合适的 ML venue（如 NeurIPS 2026），评估 idea 本身的质量。


【领域调研】:

1. Park et al. "Know What You Don't Know: Uncertainty Calibration of PRMs"
   (arXiv:2506.09338, NeurIPS 2025):
   - 首次系统研究 PRM 校准问题，提出 quantile regression calibration
   - 发现 PRM 在难题上系统性高估成功概率
   - 与本 proposal 的关系：Thread 1 的核心论文，proposal 正确引用并定位

2. Distributional PRMs via Conditional Optimal Transport
   (arXiv:2605.06785, May 2026):
   - 用 conditional optimal transport 实现 calibrated monotone quantile functions
   - 改进 MATH-500 和 AIME 上的 BoN
   - 与本 proposal 的关系：Thread 1 的最新进展，proposal 正确引用；但该论文未测试 robustness

3. Tiwari et al. "Reward Under Attack: Analyzing Robustness and Hackability of PRMs"
   (arXiv:2603.06621, March 2026):
   - 发现梯度攻击可将 PRM reward 膨胀 4×
   - RL 训练可达近完美 PRM reward 但实际准确率 <4%，43% 奖励来自文体捷径
   - 与本 proposal 的关系：Thread 2 的核心论文，proposal 正确引用

4. Ackermann et al. "Gradient Regularization Prevents Reward Hacking"
   (arXiv:2602.18037, Feb 2026):
   - 理论证明 reward surface flatness 与 accuracy retention 相关
   - 提出 gradient regularization 偏向 flatter regions
   - 与本 proposal 的关系：proposal 声称扩展其框架从 outcome-level 到 step-level

5. "From Curiosity to Caution" / Caution (arXiv:2604.04648, April 2026):
   - 用 pessimism 对抗 BoN 中的 reward hacking
   - 用 prediction error 而非 calibrated probability 作为 uncertainty proxy
   - 与本 proposal 的关系：CGSP 的直接竞争者，差异在于 calibration-grounded vs. heuristic

6. PET: Learning a Pessimistic Reward Model (arXiv:2505.20556, 2025):
   - 悲观 reward 微调，全局 pessimism
   - 与本 proposal 的关系：CGSP 的另一竞争者，差异在于 step-level adaptive vs. global

7. Robust Reward Modeling via Causal Rubrics / CROME (arXiv:2506.16507):
   - 用因果推理构建更 robust 的 reward model
   - 与本 proposal 的关系：另一种因果视角的 reward robustness 方法，proposal 未引用

8. "More Bang for the Buck: PRM with Entropy-Driven Uncertainty"
   (arXiv:2503.22233, March 2026):
   - 用 entropy 驱动的 uncertainty 提升 PRM 效率
   - 与本 proposal 的关系：另一种 uncertainty-aware PRM 方法，proposal 未引用

- 调研总结：PRM calibration 和 PRM hackability 确实是两个活跃但相对独立的研究线程，
  proposal 对这一 gap 的识别基本准确。但 calibration-based defense 并非完全无人涉及——
  pessimism-based 方法（Caution, PET）和 uncertainty-aware 方法（URM, ensemble）已形成
  密集竞争带。proposal 的增量核心在于"因果隔离实验设计"和"step-level calibration-grounded 
  pessimism"。


【Trivial Alternative 检验】:

存在严重的 trivial alternative 威胁。

核心问题：Temperature scaling（最简单的 post-hoc calibration）只修改 output mapping
（logit/T），不改变模型的判别特征。它保持排序不变，只改变概率尺度。那么：
- 对 gradient-based attacks：温度缩放使梯度变小（reward surface 更平），可能机械性地
  降低攻击效果，但这是"smoothing"效应而非"calibration"效应
- 对 BoN：温度缩放减少 overconfidence，可能延迟 overoptimization onset，但这也是
  trivial 的 probability dampening
- 对 GRPO RL hacking：policy 仍会找到相同的 exploitable patterns，只是 reward magnitude
  不同

如果温度缩放就能显著降低 hackability，这个效果更可能归因于"reward surface smoothing"
而非深层的"calibration → robustness"因果链。proposal 声称的深刻因果联系可能坍缩为
一个平凡的机械效应。

CGSP 的公式 r̃_t = μ_t − α·σ_t/√c_t 本质上是 UCB/LCB（Lower Confidence Bound）在
step-level reward 上的标准应用。这在 bandit/RL 文献中已有数十年历史。增量价值在于
将其应用于 PRM step reward 的具体场景，但方法论本身不新。

一个更简单的 baseline 可以是：ensemble-min + temperature scaling，不需要 CGSP 的
复杂公式即可实现类似的 pessimism + calibration 效果。


【前提假设检验】:

核心 claim 的逻辑链条中有两个关键未验证假设：

假设 1（最关键）："calibration quality 因果性地决定 hackability"
- 逻辑漏洞：Hackability 主要取决于模型的判别能力（能否区分真正的推理 vs. 文体捷径），
  而非概率校准。一个 PRM 可以完美校准但仍然 hackable——如果它的特征空间本身无法区分
  有效推理与无效推理。校准只改变"模型说 0.9 时真正成功率是否为 0.9"，不改变"模型
  认为什么是好的推理"。
- 反例思考：一个 perfectly calibrated PRM 在训练分布上准确反映成功率，但 RL policy
  可以 shift distribution 到 OOD 区域，此时即使曾经 calibrated 的 PRM 也会变得
  miscalibrated。proposal 的 Calibration Drift Detector 试图解决这一点，但这承认了
  calibration 是动态属性而非静态属性，削弱了"calibration quality determines 
  hackability"的因果叙事。

假设 2："post-hoc calibration 不改变 representation → 可以隔离 calibration 的因果效应"
- 这是一个合理的实验设计，但存在 confound：如果 post-hoc calibration 确实降低了
  hackability，原因可能是 reward surface smoothing（平凡效应）而非 calibration 
  quality improvement。proposal 需要但没有提出如何区分这两个解释。
- 需要一个"anti-calibration smoothing"控制：一种同等程度 smooth reward surface
  但不改善 calibration 的操作，来排除 smoothing 是真正原因。


【3 维度打分】:

1. Novelty: 弱-中 — 
   理由：(a) 桥接 PRM calibration 和 hackability 两个线程的观察是合理的，但 CoT Entropy
   paper (arXiv:2502.11250) 早在 2025 年 2 月就将此作为 future work 提出，说明这个
   connection 已在社区雷达上；(b) CGSP 的公式本质是 LCB pessimism，在 RL/bandit 文献
   中是标准技术，应用到 step-level PRM 是 incremental；(c) 因果隔离实验设计（用 post-hoc 
   calibration 作为自然实验）是 proposal 最有新意的部分，但如【前提假设检验】所述，
   存在 smoothing vs. calibration confound；(d) Hessian spectral analysis 从 outcome-level 
   扩展到 step-level 是 Ackermann et al. 的 incremental extension。
   与 Caution (arXiv:2604.04648), PET (arXiv:2505.20556), ensemble 方法在 pessimism-based
   defense 空间形成密集竞争。

2. Significance: 中 — 
   理由：(a) "calibration 是否因果性地影响 hackability"是一个有价值的科学问题，无论
   答案是 positive 还是 negative 都对社区有信息量；(b) 如果 positive 结果成立，提供了
   一条廉价的 defense 路径（只需 post-hoc calibrate PRM）；(c) 但如果核心效应归因于
   trivial smoothing 而非深层 calibration，significance 大幅缩水；(d) PRM reward hacking
   确实是 LLM alignment 的热点问题（Tiwari et al. arXiv:2603.06621 的影响力佐证），
   但 defense 方法的竞争带已很密集。

3. Related Work: 强 — 
   理由：对两个 research thread 的覆盖全面且准确。正确引用了 Park et al. (NeurIPS 2025),
   Distributional PRMs, Tiwari et al., Ackermann et al., Caution, URM, Bayesian RM,
   conformal prediction for RLHF 等。与各竞争方法的差异化定位清晰（表述了 CGSP vs. Caution
   vs. PET vs. ensemble 的区别）。小瑕疵：未引用 CROME (arXiv:2506.16507) 的因果视角
   和 EDU-PRM (arXiv:2503.22233) 的 entropy-driven uncertainty 方法。


【概率估计】: [18% - 30%] 中位 23%
（注：此概率假设投稿到合适的 ML venue 如 NeurIPS 2026。投稿 CoRL 2026 概率为 ~2%，
几乎确定 desk reject。）

【估计理由】:
- Related Work 覆盖强 + 实验设计形式完善 → 下限不至于很低（>18%）
- 但 Novelty 偏弱限制了上界：CGSP 方法论是标准 LCB 的应用，因果隔离设计有 smoothing
  confound，Hessian 分析是 incremental extension
- 核心 claim "calibration causally determines hackability" 存在根本性的概念质疑
  （calibration ≠ discrimination），如果审稿人抓住这一点，会严重削弱论文
- 如果核心发现是 positive（calibration helps），审稿人更可能说"makes sense, not 
  surprising"（better calibrated = less overconfident = less to exploit）而非"surprising"
- 上界被 Novelty 和 Trivial Alternative 威胁限制在 ~30%

【主要风险】:
1. **因果叙事可能坍缩为 trivial smoothing effect**：如果 post-hoc calibration 降低 
   hackability，审稿人很可能指出这只是 reward surface smoothing 的机械效应，而非
   深层的 calibration → robustness 因果链。proposal 缺乏区分这两个解释的控制实验。
2. **Calibration ≠ Discrimination 的概念混淆**：hackability 的根源是 PRM 无法区分真正的
   推理与文体捷径（Tiwari et al. 的核心发现），这是 discrimination 问题而非 calibration
   问题。一个 perfectly calibrated PRM 如果 discriminative features 仍然 shallow，
   仍然会被 hack。审稿人若提出此质疑，proposal 目前没有有力回应。
```

---

**补充说明给后续流程**：

这个 proposal 有一个**必须优先解决的 venue 问题**。CoRL 2026 明确要求 robotics focus，本 proposal 纯粹是 LLM reward modeling 工作，投 CoRL 会被 desk reject。建议改投 NeurIPS 2026（deadline 通常在 5 月底）或 ICML 2026。

在 idea 层面，proposal 形式非常完善（48 configurations、因果隔离设计、Hessian 分析、5 baselines），但核心智识贡献（calibration → hackability 的因果链）存在根本性的逻辑质疑。如果进入后续迭代流程，**发掘 agent** 应关注能否找到 calibration 不可还原为 smoothing 的论证角度；**补救 agent** 应重点攻击 calibration vs. discrimination 的概念混淆以及 CGSP 相对于 trivial baselines 的增量价值。

Sources:
- [Know What You Don't Know: Uncertainty Calibration of PRMs](https://arxiv.org/abs/2506.09338)
- [Distributional PRMs via Conditional Optimal Transport](https://arxiv.org/html/2605.06785)
- [Reward Under Attack: Analyzing Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)
- [Gradient Regularization Prevents Reward Hacking](https://arxiv.org/abs/2602.18037)
- [From Curiosity to Caution: Mitigating Reward Hacking with Pessimism](https://arxiv.org/pdf/2604.04648)
- [Learning a Pessimistic Reward Model in RLHF (PET)](https://arxiv.org/pdf/2505.20556)
- [Robust Reward Modeling via Causal Rubrics (CROME)](https://arxiv.org/pdf/2506.16507)
- [More Bang for the Buck: PRM with Entropy-Driven Uncertainty](https://arxiv.org/abs/2503.22233)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ce5e34e-0561-4b7f-ae72-404dbd09eab1",
  "isSidechain": false,
  "requestId": "req_011CbCcVyqU7vKkVKQt5CrEY",
  "type": "assistant",
  "uuid": "5af6c34e-0480-43a2-8f27-48df78a8b1df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zyGaz4J6NV5FrKKFZ8bSx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 864,
      "cache_read_input_tokens": 25625,
      "output_tokens": 6267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6267,
          "cache_read_input_tokens": 25625,
          "cache_creation_input_tokens": 864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 864
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

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "5af6c34e-0480-43a2-8f27-48df78a8b1df",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking proposal",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "5af6c34e-0480-43a2-8f27-48df78a8b1df",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking proposal",
  "sessionId": "c54f944d-5386-4b12-8f4a-d23dd807b013"
}
```

---
