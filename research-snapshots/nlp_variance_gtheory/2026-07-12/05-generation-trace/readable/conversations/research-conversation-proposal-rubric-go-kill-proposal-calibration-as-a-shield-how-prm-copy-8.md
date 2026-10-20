# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Calibration as a Shield: How PRM 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/ae4450f1-56bb-4a89-8ce0-2088fffebc56.jsonl`
- **Structured JSON:** [`2dd05cafc67fd5213638.json`](../../sessions/2d/2dd05cafc67fd5213638.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:51:21.795Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:51:21.795Z",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense\n\n## Description\nWe present the first causally rigorous study connecting PRM calibration quality to adversarial exploitability, and propose Calibration-Gated Step-Level Pessimism (CGSP), a novel defense that transforms calibrated uncertainty into adaptive reward hacking resistance during RL training. Our work bridges two mature but isolated research threads (PRM calibration and PRM hackability) through four contributions. First, an expanded correlation study across 48 configurations (8 PRMs × 6 calibration methods) provides sufficient statistical power (n=48, detecting r≥0.29 at p<0.05) to establish whether calibration quality predicts hackability metrics under gradient attacks, RL-induced hacking (GRPO on AIME), and BoN overoptimization (MATH-500), stratified by problem difficulty. Second, causal isolation experiments separate calibration's true effect from representation change artifacts: we compare post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) that provably preserve model representations against fine-tuning-based methods, with CKA verification and matched-representation-change controls. Third, step-level Hessian spectral analysis goes beyond Ackermann et al.'s outcome-level gradient norm analysis (which applies only to single-scalar reward models) to reveal how calibration affects the multi-reward compositional geometry of PRMs — analyzing how step-level flatness compounds across trajectories. Fourth, CGSP replaces raw PRM rewards during RL training with r̃_t = μ_t − α·σ_t/√c_t, where calibrated uncertainty σ_t and calibration quality c_t adaptively modulate pessimism per-step — trusted when calibration is tight, pessimistic when uncertainty is high — with a Calibration Drift Detector that monitors ECE on current-policy rollouts to flag distribution-shift-induced reward hacking in real time. CGSP differs from existing defenses (Caution uses prediction error, PET uses global pessimism, ensemble methods are uncalibrated) by being step-level, calibration-grounded, and adaptive. We evaluate CGSP against 5 baselines (uncalibrated GRPO, APRM, Caution, ensemble-min, gradient regularization) on MATH-500 and AIME, measuring both reward-accuracy alignment and downstream task accuracy.\n\n## Core Problem\nPRM calibration research and PRM hackability research are entirely separate threads with zero cross-citation — but the deeper problem is that we lack both (a) causal evidence for whether calibration actually determines hackability (vs. being merely correlated), and (b) a principled, step-level defense mechanism that leverages calibrated uncertainty to prevent reward hacking during RL training. Existing ad-hoc defenses (adversarial training, gradient regularization, pessimistic BoN) operate at the outcome level without exploiting the unique step-level structure of PRMs.\n\n## Opportunity\nThree recent developments create a uniquely favorable moment. First, Distributional PRMs (arXiv:2605.06785, May 2026) achieve calibrated step-level uncertainty via conditional optimal transport but never test robustness. Second, Tiwari et al. (arXiv:2603.06621, March 2026) demonstrate that PRMs are catastrophically hackable — near-perfect PRM rewards with <4% actual accuracy — but propose no calibration-based defense. Third, the causal isolation toolkit is mature: post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) modify only the output mapping without changing model representations, enabling controlled experiments that separate calibration effects from representation effects. No existing paper bridges these threads. Ackermann et al.'s gradient regularization work (arXiv:2602.18037) operates exclusively on outcome-level reward models with single-scalar rewards, never touching step-level PRM geometry. The CoT Entropy paper (arXiv:2502.11250) named this connection as future work 16 months ago with no follow-up. The window for a definitive, causally rigorous study is open but narrowing.\n\n## Related Work / Landscape\nTwo parallel research threads have developed with zero cross-citation. Thread 1 (PRM Calibration): Park et al. (arXiv:2506.09338, NeurIPS 2025) demonstrate PRMs systematically overestimate success probabilities on hard problems, proposing quantile regression calibration. Distributional PRMs (arXiv:2605.06785, May 2026) use conditional optimal transport for calibrated monotone quantile functions, improving BoN on MATH-500 and AIME. Neither paper tests robustness. Thread 2 (PRM Hackability): Tiwari et al. (arXiv:2603.06621) show gradient attacks inflate PRM rewards 4× and RL achieves near-perfect PRM rewards with <4% accuracy, with 43% of reward gains from stylistic shortcuts. APRM (arXiv:2511.22888) uses adversarial training for +3.4pp robustness. Thread 3 (Adjacent but distinct): Ackermann et al. (arXiv:2602.18037) prove reward surface flatness correlates with accuracy retention for outcome-level RMs, but work exclusively with single-scalar rewards, analyze only gradient norms (no Hessian spectra), and never consider step-level reward models. Their theoretical framework (Propositions 3.3-3.4) assumes a single reward function R(s,a) over complete responses — inapplicable to step-level PRM geometry where T coupled reward surfaces {R_1,...,R_T} interact compositionally. InferenceTimePessimism (arXiv:2506.19248) and Caution (arXiv:2604.04648) apply pessimism for BoN but use uncalibrated uncertainty proxies (prediction error, hedging), not calibrated probabilities. URM (arXiv:2410.00847) decomposes uncertainty into aleatoric/epistemic for outcome-level RMs but not PRMs. Bayesian reward models (arXiv:2402.13210) use Laplace approximation on LoRA weights. Conformal prediction has been applied to RLHF feedback alignment (arXiv:2601.17329) but never to PRM defense. No paper establishes a causal link between calibration quality and hackability, and no paper proposes using calibrated step-level PRM uncertainty as a defense during RL training.\n\n## Approach\nThe study has four components: (A) Expanded Correlation Study, (B) Causal Isolation Experiments, (C) Step-Level Mechanistic Analysis, and (D) Calibration-Gated Step-Level Pessimism (CGSP) defense.\n\n**Component A — Expanded Correlation Study (n≥24 configurations):** Apply 6 calibration methods across 2 tiers to 8 open-source PRMs. Tier 1 (post-hoc, representation-preserving): temperature scaling, Platt scaling, isotonic regression. Tier 2 (model-modifying): quantile regression fine-tuning, conditional optimal transport, Venn-Abers predictors. The 8 PRMs span discriminative (Qwen2.5-Math-PRM-7B, Qwen2.5-Math-PRM-72B, Skywork-o1-Open-PRM-7B, RLHFlow-Llama3.1-8B-PRM, Math-Shepherd-7B, OpenR-Math-psa-7B), generative (GenPRM-7B), and implicit (EurusPRM-Stage2) architectures. Each of the 48 PRM×calibration configurations is subjected to three attack tiers: (i) gradient-based reward inflation following Tiwari et al., (ii) RL-induced reward hacking via GRPO on AIME, and (iii) BoN overoptimization at N∈{1,4,16,64,256} on MATH-500. Compute rank correlations (Spearman ρ, Kendall τ) between calibration metrics (ECE, Brier score, quantile coverage, reliability diagram sharpness) and hackability metrics (reward-accuracy divergence, attack success rate, BoN degradation onset N*). Stratify analysis by problem difficulty (MATH levels 1-5, AMC vs. AIME) to test whether calibration is more protective on hard problems where PRMs are known to be overconfident.\n\n**Component B — Causal Isolation Experiments:** This is the methodological core addressing the reviewer's causation concern. Design: (B1) Post-hoc calibration control: Apply temperature scaling, Platt scaling, and isotonic regression — which provably modify only the output mapping, not internal representations — and measure hackability change. If hackability decreases under post-hoc calibration alone, this establishes that calibration per se (not representation change) causally affects hackability. (B2) Representation change verification: For fine-tuning-based calibration methods (quantile regression, COT), measure representation change at every transformer layer using Centered Kernel Alignment (CKA) between the base PRM and calibrated PRM. (B3) Matched representation change control: Fine-tune PRMs on an auxiliary task (e.g., next-token prediction on math text) that produces CKA-matched representation changes but does NOT improve calibration. If only calibration-improving fine-tuning reduces hackability (not the CKA-matched control), the causal role of calibration is confirmed. (B4) Conformal prediction as the cleanest test: Apply split-conformal prediction to PRM step scores, providing distribution-free coverage guarantees with zero model modification. Test whether conformal-calibrated PRMs resist hacking better than uncalibrated ones.\n\n**Component C — Step-Level Mechanistic Analysis (differentiating from Ackermann et al.):** Unlike Ackermann et al., who analyze only outcome-level gradient norms and max-perturbation sharpness, we perform Hessian spectral analysis at the step level — computing top-k eigenvalues and spectral density of the step-level reward Hessian ∂²R_t/∂h² (where h is the hidden representation at step t). Key questions: (i) Do calibrated PRMs have flatter step-level reward surfaces (lower top Hessian eigenvalue)? (ii) Does flatness vary by step position (early reasoning steps vs. final answer steps)? (iii) Do hackable reward peaks correspond to isolated large Hessian eigenvalues (sharp directions) that gradient attacks exploit? This extends Ackermann et al.'s framework from single-reward geometry to multi-reward compositional geometry: we analyze how step-level flatness/sharpness compounds across a T-step trajectory to determine outcome-level hackability.\n\n**Component D — Calibration-Gated Step-Level Pessimism (CGSP) Defense:** This transforms the paper from measurement to method. CGSP operates during RL training (GRPO/PPO) by replacing raw PRM step rewards with calibration-modulated rewards: r̃_t = μ_t − α · σ_t / √(c_t), where μ_t is the calibrated step reward mean, σ_t is the calibrated uncertainty (from quantile width or conformal interval), c_t is a calibration quality score (inverse ECE computed on a rolling buffer), and α is a pessimism strength hyperparameter. When calibration is high (small σ_t, high c_t), the reward is trusted; when calibration is low (large σ_t, low c_t), pessimism dominates. This differs from existing pessimism (Caution uses prediction error, PET uses global pessimistic fine-tuning, InferenceTimePessimism uses hedging) because CGSP is (i) step-level, (ii) grounded in calibrated probabilities rather than heuristic proxies, and (iii) adaptive — the pessimism automatically strengthens in distribution-shift regions where the PRM becomes miscalibrated. Additionally, we implement a Calibration Drift Detector: during RL training, periodically measure ECE on current-policy rollouts vs. the initial SFT-distribution calibration. When drift exceeds a threshold, flag those trajectory types as potentially hacked and apply reward clipping. This converts calibration from a static property into a dynamic training signal.\n\nBaseline comparisons for CGSP: (i) uncalibrated PRM + GRPO, (ii) APRM adversarial training, (iii) Caution/prediction-error pessimism, (iv) ensemble minimum (following Coste et al.), (v) KL-regularized GRPO, (vi) gradient regularization (Ackermann et al.).\n\nCodebase starting points: young-j-park/prm-calibration for calibration fitting, Tiwari et al.'s PRM-BiasBench for adversarial evaluation, vwxyzjn/open_instruct for GRPO training infrastructure.\n\n## Inspiration\nField guide gap: PRM overconfidence on OOD problems (Section 5.3 'when more compute hurts'); Untried combination: distributional PRM calibration + PRM hackability analysis; Pattern: connecting two mature but isolated research threads; Reviewer insight: pure measurement is insufficient — the key contribution should be a causal mechanism and a defense method; Methodological insight: post-hoc calibration methods that preserve representations enable clean causal isolation experiments impossible with fine-tuning-based calibration alone\n\n## Key References\n- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (arXiv:2506.09338, NeurIPS 2025)\n- Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport (arXiv:2605.06785, May 2026)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv:2603.06621, March 2026)\n- Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards (arXiv:2602.18037, Feb 2026)\n- Adversarial Training for Process Reward Models (arXiv:2511.22888, Nov 2025)\n- From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism (arXiv:2604.04648, April 2026)\n- Inference-Time Reward Hacking in Large Language Models (arXiv:2506.19248, NeurIPS 2025 Spotlight)\n- Uncertainty-Aware Step-wise Verification with Generative Reward Models (arXiv:2502.11250, ICLR 2025 Workshop)\n- Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242, April 2026)\n- Uncertainty-Aware Reward Model (arXiv:2410.00847)\n- Helping or Herding? Reward Model Ensembles Mitigate but Do Not Eliminate Overoptimization (arXiv:2312.09244)\n- Bayesian Reward Models for LLM Alignment (arXiv:2402.13210)\n- Conformal Feedback Alignment for RLHF (arXiv:2601.17329)\n- Taming Overconfidence in LLMs: Reward Calibration in RLHF (arXiv:2410.09724)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (arXiv:2501.03124)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '4200 H100-hrs (calibration fitting: 200, rollout generation: 600, gradient attacks: 1000, GRPO RL training: 1600 [including CGSP defense training], BoN evaluation: 400, Hessian spectral analysis: 200, causal isolation controls: 200)', 'timeline': '12-14 weeks', 'estimated_gpu_cost': '$10,500 at ~$2.50/H100-hr'}\n- **human_in_loop**: {'gpu_hours': '3600 H100-hrs (fewer failed iterations with AI-assisted debugging)', 'timeline': '10-12 weeks', 'claude_api_cost': '$400-700 (code generation, experiment analysis, paper drafting)', 'estimated_gpu_cost': '$9,000 at ~$2.50/H100-hr'}\n- **auto_research**: {'gpu_hours': '5200 H100-hrs (broader sweeps over α pessimism parameter, calibration drift thresholds, and ablations across all 48 configurations)', 'timeline': '7-9 weeks', 'claude_api_cost': '$1,500-2,000 (automated experiment orchestration, iterative analysis, full draft writing)', 'estimated_gpu_cost': '$13,000 at ~$2.50/H100-hr', 'speed_bottleneck': 'GRPO RL training wall-clock time (~18hrs per PRM×calibration×defense configuration on 4×H100); Hessian spectral analysis requires Lanczos iterations per step per problem; 72B PRM requires 4×H100 for inference'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T18:51:21.798Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:51:21.798Z",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-19T18:51:21.812Z_

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
  "promptId": "d551cef2-18fb-4f70-a90b-9c3e21e7f021",
  "type": "user",
  "uuid": "0c92c5ca-ab63-4bd9-91c8-bd13fbdd4088",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:51:21.811Z_

```json
{
  "parentUuid": "0c92c5ca-ab63-4bd9-91c8-bd13fbdd4088",
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
  "uuid": "e28a0279-c9e9-4692-93f1-1955bdaf9141",
  "timestamp": "2026-05-19T18:51:21.811Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:51:21.811Z_

```json
{
  "parentUuid": "e28a0279-c9e9-4692-93f1-1955bdaf9141",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4bceadc4-3764-415c-9492-0ac7745f4bde",
  "timestamp": "2026-05-19T18:51:21.811Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
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
  "leafUuid": "4bceadc4-3764-415c-9492-0ac7745f4bde",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking proposal",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:51:39.076Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026 submission potential. Let me first note something important: CoRL is the Conference on Robot Learning, which focuses on robotics and learning. This proposal is about PRM (Process Reward Model) calibration and reward hacking in LLM alignment/RLHF - this seems more appropriate for NLP/ML venues like NeurIPS, ICML, ICLR, or ACL, not CoRL.

Wait, let me re-read the system prompt. It says "CoRL 2026 主会" - Conference on Robot Learning. 

There's a clear mismatch here: the proposal focuses on process reward models for mathematical reasoning in language models, which falls squarely in the NLP/ML domain rather than robotics. I should evaluate the proposal on its merits while flagging this venue misalignment, since it could significantly impact acceptance chances regardless of the work's quality.

Before diving into assessment, I need to search for recent developments in PRM calibration and related work to properly contextualize this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bceadc4-3764-415c-9492-0ac7745f4bde",
  "isSidechain": false,
  "requestId": "req_011CbCRxNwiPoX8s9r88aGng",
  "type": "assistant",
  "uuid": "0305f1f7-cd2b-4876-8a86-6def93d50bfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPqWzaVfqLcU5seMp2L4bb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5583,
      "cache_read_input_tokens": 13985,
      "output_tokens": 682,
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
          "output_tokens": 682,
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

### Assistant

_source line 9 · 2026-05-19T18:51:40.230Z_

我需要先对这个 proposal 所在领域进行详细调研，然后才能打分。让我先进行多轮 WebSearch 调研。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0305f1f7-cd2b-4876-8a86-6def93d50bfc",
  "isSidechain": false,
  "requestId": "req_011CbCRxNwiPoX8s9r88aGng",
  "type": "assistant",
  "uuid": "64d776fa-9a17-4fd9-92db-bc03b7c1dcde",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPqWzaVfqLcU5seMp2L4bb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5583,
      "cache_read_input_tokens": 13985,
      "output_tokens": 682,
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
          "output_tokens": 682,
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

_source line 10 · 2026-05-19T18:51:40.300Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EMkFJd4uPBnaXhLKEoJJWA`</summary>

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
  "parentUuid": "64d776fa-9a17-4fd9-92db-bc03b7c1dcde",
  "isSidechain": false,
  "requestId": "req_011CbCRxNwiPoX8s9r88aGng",
  "type": "assistant",
  "uuid": "9bf34971-245d-4243-8e28-b5553b3c0398",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPqWzaVfqLcU5seMp2L4bb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5583,
      "cache_read_input_tokens": 13985,
      "output_tokens": 682,
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
          "output_tokens": 682,
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

_source line 11 · 2026-05-19T18:51:40.306Z_

<details><summary>↩ Tool result · `toolu_01EMkFJd4uPBnaXhLKEoJJWA`</summary>

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
  "parentUuid": "9bf34971-245d-4243-8e28-b5553b3c0398",
  "isSidechain": false,
  "promptId": "d551cef2-18fb-4f70-a90b-9c3e21e7f021",
  "type": "user",
  "uuid": "46e725e3-7f95-4f0b-bfc0-87c9f10976cd",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "9bf34971-245d-4243-8e28-b5553b3c0398",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T18:51:43.255Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do the web searches. I'll search for multiple topics in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46e725e3-7f95-4f0b-bfc0-87c9f10976cd",
  "isSidechain": false,
  "requestId": "req_011CbCRykSZSyGZN7nNpoGNf",
  "type": "assistant",
  "uuid": "b816b994-5d4f-4dfa-93e2-005580d220f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lp4jER4vbFaqg7NhCts1i4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 19568,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1208,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 19568,
          "cache_creation_input_tokens": 1208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1208
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-19T18:51:43.718Z_

现在让我进行多轮调研。先并行搜索几个关键方向：

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b816b994-5d4f-4dfa-93e2-005580d220f6",
  "isSidechain": false,
  "requestId": "req_011CbCRykSZSyGZN7nNpoGNf",
  "type": "assistant",
  "uuid": "eb7df4d0-5c5b-419d-8670-ae783c77ba03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lp4jER4vbFaqg7NhCts1i4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 19568,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1208,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 19568,
          "cache_creation_input_tokens": 1208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1208
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T18:51:44.385Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016Pw4wReHqdnRji9rt5az5S`</summary>

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
  "parentUuid": "eb7df4d0-5c5b-419d-8670-ae783c77ba03",
  "isSidechain": false,
  "requestId": "req_011CbCRykSZSyGZN7nNpoGNf",
  "type": "assistant",
  "uuid": "e945f6d4-7ea9-4e19-aa01-e996073e5603",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lp4jER4vbFaqg7NhCts1i4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1208,
      "cache_read_input_tokens": 19568,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1208,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 126,
          "cache_read_input_tokens": 19568,
          "cache_creation_input_tokens": 1208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1208
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T18:51:52.100Z_

<details><summary>↩ Tool result · `toolu_016Pw4wReHqdnRji9rt5az5S`</summary>

```text
Web search results for query: "PRM process reward model calibration 2025 2026 arxiv"

Links: [{"title":"[2506.09338] Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/abs/2506.09338"},{"title":"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/html/2605.06785"},{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/pdf/2506.09338"},{"title":"[2510.08049] A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/abs/2510.08049"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"[2503.22233] More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty","url":"https://arxiv.org/abs/2503.22233"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"[2511.08325] AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress","url":"https://arxiv.org/abs/2511.08325"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"}]

Here are the key findings from recent arXiv research on PRM (Process Reward Model) calibration from 2025-2026:

## Uncertainty Calibration

A recent paper introduces an instance-adaptive scaling (IAS) framework that dynamically adjusts compute budget based on estimated likelihood of success, adapting to each instance and reasoning step when using calibrated PRMs. The proposed PRM calibration method achieves small calibration error, outperforming baseline methods, and the IAS strategy reduces inference costs while maintaining accuracy.

## Distributional Approaches

Process Reward Models are often poorly calibrated and overestimate success probabilities, with recent work proposing the first use of conditional optimal transport for calibrating PRMs. This method estimates a monotonic conditional quantile function over success probabilities and enables efficient extraction of confidence bounds at arbitrary levels.

## Entropy-Driven Methods

EDU-PRM uses entropy-driven uncertainty sampling and achieves comparable results with state-of-the-art models while using only 1.5% training data, with accuracy boosts and significant token usage reduction.

## Comprehensive Survey

A comprehensive survey paper on Process Reward Models was submitted in October 2025 and last revised in April 2026, covering the transition from outcome signals to process supervisions for large language models.

These recent papers show significant advances in addressing calibration issues that have limited PRM effectiveness in inference-time scaling applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e945f6d4-7ea9-4e19-aa01-e996073e5603",
  "isSidechain": false,
  "promptId": "d551cef2-18fb-4f70-a90b-9c3e21e7f021",
  "type": "user",
  "uuid": "e8d811af-9cba-45be-8dff-d61f04cefd39",
  "toolUseResult": {
    "query": "PRM process reward model calibration 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ufu8ZogafXYXyWx2naf1UH",
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
      "Here are the key findings from recent arXiv research on PRM (Process Reward Model) calibration from 2025-2026:\n\n## Uncertainty Calibration\n\nA recent paper introduces an instance-adaptive scaling (IAS) framework that dynamically adjusts compute budget based on estimated likelihood of success, adapting to each instance and reasoning step when using calibrated PRMs. The proposed PRM calibration method achieves small calibration error, outperforming baseline methods, and the IAS strategy reduces inference costs while maintaining accuracy.\n\n## Distributional Approaches\n\nProcess Reward Models are often poorly calibrated and overestimate success probabilities, with recent work proposing the first use of conditional optimal transport for calibrating PRMs. This method estimates a monotonic conditional quantile function over success probabilities and enables efficient extraction of confidence bounds at arbitrary levels.\n\n## Entropy-Driven Methods\n\nEDU-PRM uses entropy-driven uncertainty sampling and achieves comparable results with state-of-the-art models while using only 1.5% training data, with accuracy boosts and significant token usage reduction.\n\n## Comprehensive Survey\n\nA comprehensive survey paper on Process Reward Models was submitted in October 2025 and last revised in April 2026, covering the transition from outcome signals to process supervisions for large language models.\n\nThese recent papers show significant advances in addressing calibration issues that have limited PRM effectiveness in inference-time scaling applications."
    ],
    "durationSeconds": 7.709066169999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e945f6d4-7ea9-4e19-aa01-e996073e5603",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T18:51:54.562Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pxqesnv7nZRAEmXXGFxJc9`</summary>

```json
{
  "query": "PRM reward hacking hackability process reward model attack robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8d811af-9cba-45be-8dff-d61f04cefd39",
  "isSidechain": false,
  "requestId": "req_011CbCRzcPuPpVQdyk6a2vf6",
  "type": "assistant",
  "uuid": "54dbacdd-49e8-4566-9e66-358db10b3aff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W24y24atFi5LZdsobeRBDq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 911,
      "cache_read_input_tokens": 20776,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 20776,
          "cache_creation_input_tokens": 911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 911
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

_source line 17 · 2026-05-19T18:52:10.715Z_

<details><summary>↩ Tool result · `toolu_01Pxqesnv7nZRAEmXXGFxJc9`</summary>

```text
Web search results for query: "PRM reward hacking hackability process reward model attack robustness 2025 2026"

Links: [{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"},{"title":"1 Introduction","url":"https://arxiv.org/html/2603.06621"},{"title":"Reward Under Attack: Evaluating the Sensitivity of Process Reward Models","url":"https://openreview.net/pdf?id=Hw24VOppus"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=reward+hacking"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"}]

Based on the search results, here's what I found about PRM (Process Reward Model) reward hacking and robustness:

## Key Recent Research (2025-2026)

Process Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure.

### Main Findings on PRM Hackability

The most prominent recent study "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models" (February 2026) reveals several critical vulnerabilities:

1. **Fluency-Logic Dissociation**: Static perturbation analysis uncovers a fluency-logic dissociation: high invariance to surface-level style changes reward changes <0.1, yet inconsistent detection of logically-corrupted reasoning, with different models failing on different attack types.

2. **Adversarial Exploitability**: Adversarial optimization demonstrates that gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks.

3. **Critical RL-Induced Failure**: Policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.

4. **Fundamental Problem**: Current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.

### Related Research on Reward Hacking Mitigation

Reward models (RMs) used in reinforcement learning from human feedback (RLHF) are vulnerable to reward hacking: as the policy maximizes a learned proxy reward, true quality plateaus or degrades. Recent work has proposed mitigation strategies like Sign-Certified Policy Optimization to address these vulnerabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54dbacdd-49e8-4566-9e66-358db10b3aff",
  "isSidechain": false,
  "promptId": "d551cef2-18fb-4f70-a90b-9c3e21e7f021",
  "type": "user",
  "uuid": "8e01807b-1a69-4453-a247-54a7e505f5b9",
  "toolUseResult": {
    "query": "PRM reward hacking hackability process reward model attack robustness 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TstnXaCiebe4YTtgHSDgz6",
        "content": [
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub",
            "url": "https://github.com/xhwang22/Awesome-Reward-Hacking"
          },
          {
            "title": "[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/abs/2603.06621"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2603.06621"
          },
          {
            "title": "Reward Under Attack: Evaluating the Sensitivity of Process Reward Models",
            "url": "https://openreview.net/pdf?id=Hw24VOppus"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=reward+hacking"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/pdf/2604.02986"
          }
        ]
      },
      "Based on the search results, here's what I found about PRM (Process Reward Model) reward hacking and robustness:\n\n## Key Recent Research (2025-2026)\n\nProcess Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure.\n\n### Main Findings on PRM Hackability\n\nThe most prominent recent study \"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\" (February 2026) reveals several critical vulnerabilities:\n\n1. **Fluency-Logic Dissociation**: Static perturbation analysis uncovers a fluency-logic dissociation: high invariance to surface-level style changes reward changes <0.1, yet inconsistent detection of logically-corrupted reasoning, with different models failing on different attack types.\n\n2. **Adversarial Exploitability**: Adversarial optimization demonstrates that gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks.\n\n3. **Critical RL-Induced Failure**: Policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.\n\n4. **Fundamental Problem**: Current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.\n\n### Related Research on Reward Hacking Mitigation\n\nReward models (RMs) used in reinforcement learning from human feedback (RLHF) are vulnerable to reward hacking: as the policy maximizes a learned proxy reward, true quality plateaus or degrades. Recent work has proposed mitigation strategies like Sign-Certified Policy Optimization to address these vulnerabilities."
    ],
    "durationSeconds": 16.148719517999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "54dbacdd-49e8-4566-9e66-358db10b3aff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T18:52:14.336Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YJrigzvDnhmoV8eHGefsJW`</summary>

```json
{
  "query": "reward hacking defense calibration pessimism RL training LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e01807b-1a69-4453-a247-54a7e505f5b9",
  "isSidechain": false,
  "requestId": "req_011CbCS1zEas6m2nXr7MJDAC",
  "type": "assistant",
  "uuid": "feb091d6-0a8e-46af-82ff-965b62c9aa28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RAucCMHf3aiHV2RjdTu6gg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 868,
      "cache_read_input_tokens": 21687,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 868,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 21687,
          "cache_creation_input_tokens": 868,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 868
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

_source line 19 · 2026-05-19T18:52:23.225Z_

<details><summary>↩ Tool result · `toolu_01YJrigzvDnhmoV8eHGefsJW`</summary>

```text
Web search results for query: "reward hacking defense calibration pessimism RL training LLM 2025 2026"

Links: [{"title":"Mitigating Reward Hacking with RL Training Interventions | OpenReview","url":"https://openreview.net/forum?id=1TIWkM3nY4"},{"title":"Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use","url":"https://arxiv.org/html/2605.02964"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/pdf/2604.04648"},{"title":"Reward Hacking Defense Rubric","url":"https://www.emergentmind.com/topics/reward-hacking-defense-rubric"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR","url":"https://arxiv.org/pdf/2603.07084"},{"title":"Natural Emergent Misalignment from Reward Hacking in Production RL","url":"https://arxiv.org/pdf/2511.18397"}]

I've performed a web search on reward hacking defense, calibration, pessimism, RL training, and LLM research from 2025-2026. Here are the key findings:

## Recent Research on Reward Hacking Mitigation

**Pessimism-Based Defenses:**
One approach penalizes out-of-distribution responses by subtracting per-response uncertainty estimates from reward model scores, then selecting the response with the highest pessimistic score. Research shows the feasibility of learning a pessimistic reward model against reward hacking, allowing agents to greedily search for policies with high pessimistic reward without suffering from reward hacking.

**RL Training Interventions:**
Three categories of reward hacking mitigation have been compared: penalizing detected reward hacking rollouts, negatively rewarding such rollouts, and inoculation prompting, with best interventions achieving comparable performance to models trained in non-reward hackable environments.

**Benchmarking and Defense Evaluation:**
The Reward Hacking Benchmark (RHB) is designed to quantify reward hacking, study its association with RL post-training through controlled comparisons, and evaluate practical defenses through environmental hardening.

**Multi-Strategy Defense Rubric:**
Reward signals should be bounded—unbounded rewards destabilize critics and advantage estimations, encouraging reward hacking. Defenses include hard vetoes for flagged exploit patterns, advanced score aggregation, and multi-objective aggregation to reduce incentives for exploiting single criteria.

**Detection Mechanisms:**
Ensemble-based detection frameworks spanning statistical divergence checks, time-series anomaly detection, and robust outlier analysis achieve precision near 78% and recall near 82% in diverse RL environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "feb091d6-0a8e-46af-82ff-965b62c9aa28",
  "isSidechain": false,
  "promptId": "d551cef2-18fb-4f70-a90b-9c3e21e7f021",
  "type": "user",
  "uuid": "1e306349-a6b7-47c7-b987-6a59025262a0",
  "toolUseResult": {
    "query": "reward hacking defense calibration pessimism RL training LLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Y42JhniYiPsLaXUhD8xTPJ",
        "content": [
          {
            "title": "Mitigating Reward Hacking with RL Training Interventions | OpenReview",
            "url": "https://openreview.net/forum?id=1TIWkM3nY4"
          },
          {
            "title": "Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use",
            "url": "https://arxiv.org/html/2605.02964"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism",
            "url": "https://arxiv.org/pdf/2604.04648"
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
            "title": "Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR",
            "url": "https://arxiv.org/pdf/2603.07084"
          },
          {
            "title": "Natural Emergent Misalignment from Reward Hacking in Production RL",
            "url": "https://arxiv.org/pdf/2511.18397"
          }
        ]
      },
      "I've performed a web search on reward hacking defense, calibration, pessimism, RL training, and LLM research from 2025-2026. Here are the key findings:\n\n## Recent Research on Reward Hacking Mitigation\n\n**Pessimism-Based Defenses:**\nOne approach penalizes out-of-distribution responses by subtracting per-response uncertainty estimates from reward model scores, then selecting the response with the highest pessimistic score. Research shows the feasibility of learning a pessimistic reward model against reward hacking, allowing agents to greedily search for policies with high pessimistic reward without suffering from reward hacking.\n\n**RL Training Interventions:**\nThree categories of reward hacking mitigation have been compared: penalizing detected reward hacking rollouts, negatively rewarding such rollouts, and inoculation prompting, with best interventions achieving comparable performance to models trained in non-reward hackable environments.\n\n**Benchmarking and Defense Evaluation:**\nThe Reward Hacking Benchmark (RHB) is designed to quantify reward hacking, study its association with RL post-training through controlled comparisons, and evaluate practical defenses through environmental hardening.\n\n**Multi-Strategy Defense Rubric:**\nReward signals should be bounded—unbounded rewards destabilize critics and advantage estimations, encouraging reward hacking. Defenses include hard vetoes for flagged exploit patterns, advanced score aggregation, and multi-objective aggregation to reduce incentives for exploiting single criteria.\n\n**Detection Mechanisms:**\nEnsemble-based detection frameworks spanning statistical divergence checks, time-series anomaly detection, and robust outlier analysis achieve precision near 78% and recall near 82% in diverse RL environments."
    ],
    "durationSeconds": 8.884528510000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "feb091d6-0a8e-46af-82ff-965b62c9aa28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "1e306349-a6b7-47c7-b987-6a59025262a0",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking proposal",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56"
}
```

---

### Tool call

_source line 22 · 2026-05-19T18:52:26.232Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S5fDeeh6tncrNvvZAurAFF`</summary>

```json
{
  "query": "gradient regularization reward hacking Ackermann 2602.18037 reward surface flatness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e306349-a6b7-47c7-b987-6a59025262a0",
  "isSidechain": false,
  "requestId": "req_011CbCS2uZ5LqHBPBRQfnhmj",
  "type": "assistant",
  "uuid": "61d279d8-d480-4687-85c8-0f7e6286c59b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HfxHK5PtiQbYMJUQFxTjrB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 22555,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 833,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 22555,
          "cache_creation_input_tokens": 833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 833
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

_source line 23 · 2026-05-19T18:52:32.177Z_

<details><summary>↩ Tool result · `toolu_01S5fDeeh6tncrNvvZAurAFF`</summary>

```text
Web search results for query: "gradient regularization reward hacking Ackermann 2602.18037 reward surface flatness"

Links: [{"title":"[2602.18037] Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards","url":"https://arxiv.org/abs/2602.18037"},{"title":"Detecting and Suppressing Reward Hacking with Gradient Fingerprints","url":"https://arxiv.org/html/2604.16242v1"},{"title":"Gradient Regularization Prevents Reward Hacking in ...","url":"https://arxiv.org/pdf/2602.18037"},{"title":"Reward Sharpness-Aware Fine-Tuning for Diffusion Models","url":"https://arxiv.org/pdf/2603.21175"},{"title":"Johannes Ackermann","url":"https://johannesack.github.io/"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"},{"title":"[2602.08646] Projected Gradient Ascent for Efficient Reward-Guided Updates with One-Step Generative Models","url":"https://arxiv.org/abs/2602.08646"}]

Based on the search results, I found highly relevant information about your query:

The paper establishes a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence. Gradient regularization can then be used to bias training to flatter regions and thereby maintain reward model accuracy.

The paper, authored by Johannes Ackermann and colleagues (arxiv 2602.18037), addresses reward hacking in the context of Reinforcement Learning from Human Feedback (RLHF). A common problem is reward hacking, where the policy may exploit inaccuracies of the reward and learn an unintended behavior. Rather than using traditional approaches, the authors propose training the language model in a way that biases policy updates towards regions in which the reward is more accurate.

The results are confirmed by showing that the gradient norm and reward accuracy are empirically correlated in RLHF.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61d279d8-d480-4687-85c8-0f7e6286c59b",
  "isSidechain": false,
  "promptId": "d551cef2-18fb-4f70-a90b-9c3e21e7f021",
  "type": "user",
  "uuid": "9a5df128-ea51-4dd2-89bb-0a081a79bd3a",
  "toolUseResult": {
    "query": "gradient regularization reward hacking Ackermann 2602.18037 reward surface flatness",
    "results": [
      {
        "tool_use_id": "srvtoolu_01B3XhgZH9e5nQU8i9rC3sHv",
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
            "title": "Reward Sharpness-Aware Fine-Tuning for Diffusion Models",
            "url": "https://arxiv.org/pdf/2603.21175"
          },
          {
            "title": "Johannes Ackermann",
            "url": "https://johannesack.github.io/"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/pdf/2604.02986"
          },
          {
            "title": "[2602.08646] Projected Gradient Ascent for Efficient Reward-Guided Updates with One-Step Generative Models",
            "url": "https://arxiv.org/abs/2602.08646"
          }
        ]
      },
      "Based on the search results, I found highly relevant information about your query:\n\nThe paper establishes a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence. Gradient regularization can then be used to bias training to flatter regions and thereby maintain reward model accuracy.\n\nThe paper, authored by Johannes Ackermann and colleagues (arxiv 2602.18037), addresses reward hacking in the context of Reinforcement Learning from Human Feedback (RLHF). A common problem is reward hacking, where the policy may exploit inaccuracies of the reward and learn an unintended behavior. Rather than using traditional approaches, the authors propose training the language model in a way that biases policy updates towards regions in which the reward is more accurate.\n\nThe results are confirmed by showing that the gradient norm and reward accuracy are empirically correlated in RLHF."
    ],
    "durationSeconds": 5.940836181999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "61d279d8-d480-4687-85c8-0f7e6286c59b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T18:52:34.933Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S3gdxhTL9AzLpVLUc9JVBy`</summary>

```json
{
  "query": "\"calibration\" \"reward hacking\" causal link process reward model step-level defense 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a5df128-ea51-4dd2-89bb-0a081a79bd3a",
  "isSidechain": false,
  "requestId": "req_011CbCS3ZjzU4BhZ2t2qPZau",
  "type": "assistant",
  "uuid": "6945c53d-7c06-4897-83d6-b1c7d8833d10",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQ8yMQBgiRSHRf7R2Cdgzb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 23388,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 23388,
          "cache_creation_input_tokens": 625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 625
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

_source line 25 · 2026-05-19T18:52:46.987Z_

<details><summary>↩ Tool result · `toolu_01S3gdxhTL9AzLpVLUc9JVBy`</summary>

```text
Web search results for query: ""calibration" "reward hacking" causal link process reward model step-level defense 2026"

Links: [{"title":"Avoiding Reward Hacking","url":"https://www.emergentmind.com/topics/avoiding-reward-hacking"},{"title":"Beyond Outcome Verification: Verifiable Process Reward Models for","url":"https://www.arxiv.org/pdf/2601.17223"},{"title":"GitHub - JLZhong23/awesome-reward-models · GitHub","url":"https://github.com/JLZhong23/awesome-reward-models"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"Reward Hacking Defense Rubric","url":"https://www.emergentmind.com/topics/reward-hacking-defense-rubric"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/pdf/2509.26578"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/pdf/2508.04216"}]

Based on the search results, I found several relevant papers and resources about the causal links between reward hacking and process reward models from 2025-2026:

## Key Findings:

**Causal Approaches to Reward Hacking:**
Causal Reward Adjustment (CRA) is a method that mitigates reward hacking by estimating the true reward of a reasoning path, training sparse autoencoders on the PRM's internal activations to recover interpretable features, then correcting confounding by using backdoor adjustment.

**Step-Level Defense Mechanisms:**
Verifiable step-level rewards would eliminate the aforementioned problems associated with neural process rewards. Additionally, Myopic Optimization with Non-myopic Approval (MONA) ensures agents optimize only step-wise rewards plus approval, blocking multi-step hacks by eliminating foresight about reward returns.

**Causal Calibration Methods:**
Post-hoc Causal Correction decomposes reward model activations via sparse autoencoders, identifies confounding features statistically linked to hacking, and applies backdoor adjustments to neutralize semantic short-circuits in reward assignment.

**Conditional Reward Modeling:**
Conditional Reward Modeling (CRM) explicitly conditions each step reward on the previous reasoning steps and aligns it with the final outcome, making it more robust to reward hacking.

These recent approaches establish clear causal links between process reward model architecture and reward hacking vulnerabilities, with step-level defenses being a primary focus in 2025-2026 research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6945c53d-7c06-4897-83d6-b1c7d8833d10",
  "isSidechain": false,
  "promptId": "d551cef2-18fb-4f70-a90b-9c3e21e7f021",
  "type": "user",
  "uuid": "bee95c3a-4daa-4f9d-9d63-4d10a3704877",
  "toolUseResult": {
    "query": "\"calibration\" \"reward hacking\" causal link process reward model step-level defense 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AM3e7j6akgAXUUyusAhtgJ",
        "content": [
          {
            "title": "Avoiding Reward Hacking",
            "url": "https://www.emergentmind.com/topics/avoiding-reward-hacking"
          },
          {
            "title": "Beyond Outcome Verification: Verifiable Process Reward Models for",
            "url": "https://www.arxiv.org/pdf/2601.17223"
          },
          {
            "title": "GitHub - JLZhong23/awesome-reward-models · GitHub",
            "url": "https://github.com/JLZhong23/awesome-reward-models"
          },
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://arxiv.org/pdf/2601.21350"
          },
          {
            "title": "Reward Hacking Defense Rubric",
            "url": "https://www.emergentmind.com/topics/reward-hacking-defense-rubric"
          },
          {
            "title": "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2509.26578"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/pdf/2508.04216"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and resources about the causal links between reward hacking and process reward models from 2025-2026:\n\n## Key Findings:\n\n**Causal Approaches to Reward Hacking:**\nCausal Reward Adjustment (CRA) is a method that mitigates reward hacking by estimating the true reward of a reasoning path, training sparse autoencoders on the PRM's internal activations to recover interpretable features, then correcting confounding by using backdoor adjustment.\n\n**Step-Level Defense Mechanisms:**\nVerifiable step-level rewards would eliminate the aforementioned problems associated with neural process rewards. Additionally, Myopic Optimization with Non-myopic Approval (MONA) ensures agents optimize only step-wise rewards plus approval, blocking multi-step hacks by eliminating foresight about reward returns.\n\n**Causal Calibration Methods:**\nPost-hoc Causal Correction decomposes reward model activations via sparse autoencoders, identifies confounding features statistically linked to hacking, and applies backdoor adjustments to neutralize semantic short-circuits in reward assignment.\n\n**Conditional Reward Modeling:**\nConditional Reward Modeling (CRM) explicitly conditions each step reward on the previous reasoning steps and aligns it with the final outcome, making it more robust to reward hacking.\n\nThese recent approaches establish clear causal links between process reward model architecture and reward hacking vulnerabilities, with step-level defenses being a primary focus in 2025-2026 research."
    ],
    "durationSeconds": 12.04812950000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6945c53d-7c06-4897-83d6-b1c7d8833d10",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T18:52:49.068Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017PUYMVyeJ4WYcd3GwitZFJ`</summary>

```json
{
  "query": "APRM adversarial training process reward model 2511.22888 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bee95c3a-4daa-4f9d-9d63-4d10a3704877",
  "isSidechain": false,
  "requestId": "req_011CbCS4f5VGdvgrp1BGb8mk",
  "type": "assistant",
  "uuid": "ffe7d2cb-0cdc-4e24-bc13-f20d0c0033fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9MD1x1tpcKyBaNCzvgfiP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 24013,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 766,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 24013,
          "cache_creation_input_tokens": 766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 766
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

_source line 27 · 2026-05-19T18:52:56.113Z_

<details><summary>↩ Tool result · `toolu_017PUYMVyeJ4WYcd3GwitZFJ`</summary>

```text
Web search results for query: "APRM adversarial training process reward model 2511.22888 arxiv"

Links: [{"title":"[2511.22888] Adversarial Training for Process Reward Models","url":"https://arxiv.org/abs/2511.22888"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/pdf/2511.22888"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/html/2511.22888"},{"title":"Adversarially Trained Reward Models","url":"https://www.emergentmind.com/topics/adversarially-trained-reward-models"},{"title":"Adversarial Training of Reward Models","url":"https://arxiv.org/html/2504.06141v2"},{"title":"[2504.06141] Adversarial Training of Reward Models","url":"https://arxiv.org/abs/2504.06141"}]

I found the paper you're looking for! Here are the key details about arxiv:2511.22888:

## Adversarial Training for Process Reward Models (APRM)

Process Reward Models (PRMs) enhance reasoning ability of LLMs by providing step-level supervision. However, their widespread adoption is limited due to expensive manual step-level annotation and poor generalization of static training data to novel errors.

The paper introduces Adversarially Trained PRMs (APRM), where a Generator (G) learns to produce reasoning errors to deceive a PRM (R), while R concurrently learns to detect them. This interaction yields progressively harder negatives for R, improving its robustness and generalization to novel errors without requiring manual step-level labels.

### Results

The approach shows significant improvements:
- Averaged across diverse mathematical reasoning benchmarks, APRM improves solver accuracy by +3.4 percentage points (pp) over the strongest PRM baseline.
- APRM achieves gains of +5.3 pp on out-of-distribution tasks.

The paper was submitted on November 28, 2025, by authors Gurusha Juneja, Deepak Nathani, and William Yang Wang from UC Santa Barbara.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffe7d2cb-0cdc-4e24-bc13-f20d0c0033fc",
  "isSidechain": false,
  "promptId": "d551cef2-18fb-4f70-a90b-9c3e21e7f021",
  "type": "user",
  "uuid": "ea806a30-a374-4d2d-8016-75ffe1c3dc06",
  "toolUseResult": {
    "query": "APRM adversarial training process reward model 2511.22888 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Qo75gGHTx7fuiBam9d95Du",
        "content": [
          {
            "title": "[2511.22888] Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/abs/2511.22888"
          },
          {
            "title": "Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/pdf/2511.22888"
          },
          {
            "title": "Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/html/2511.22888"
          },
          {
            "title": "Adversarially Trained Reward Models",
            "url": "https://www.emergentmind.com/topics/adversarially-trained-reward-models"
          },
          {
            "title": "Adversarial Training of Reward Models",
            "url": "https://arxiv.org/html/2504.06141v2"
          },
          {
            "title": "[2504.06141] Adversarial Training of Reward Models",
            "url": "https://arxiv.org/abs/2504.06141"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details about arxiv:2511.22888:\n\n## Adversarial Training for Process Reward Models (APRM)\n\nProcess Reward Models (PRMs) enhance reasoning ability of LLMs by providing step-level supervision. However, their widespread adoption is limited due to expensive manual step-level annotation and poor generalization of static training data to novel errors.\n\nThe paper introduces Adversarially Trained PRMs (APRM), where a Generator (G) learns to produce reasoning errors to deceive a PRM (R), while R concurrently learns to detect them. This interaction yields progressively harder negatives for R, improving its robustness and generalization to novel errors without requiring manual step-level labels.\n\n### Results\n\nThe approach shows significant improvements:\n- Averaged across diverse mathematical reasoning benchmarks, APRM improves solver accuracy by +3.4 percentage points (pp) over the strongest PRM baseline.\n- APRM achieves gains of +5.3 pp on out-of-distribution tasks.\n\nThe paper was submitted on November 28, 2025, by authors Gurusha Juneja, Deepak Nathani, and William Yang Wang from UC Santa Barbara."
    ],
    "durationSeconds": 7.040246313999989,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ffe7d2cb-0cdc-4e24-bc13-f20d0c0033fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T18:52:59.189Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MujU7gXC1Mga4ySAStRjTN`</summary>

```json
{
  "query": "Causal Reward Adjustment CRA reward hacking sparse autoencoder PRM 2508.04216"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea806a30-a374-4d2d-8016-75ffe1c3dc06",
  "isSidechain": false,
  "requestId": "req_011CbCS5L4XNWChsRirVdwU1",
  "type": "assistant",
  "uuid": "35e4fd65-d665-475c-95dc-9df18d456cae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014X7ec33LQRyPzEY39Ltpkz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 24779,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 24779,
          "cache_creation_input_tokens": 620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 620
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

_source line 29 · 2026-05-19T18:53:10.211Z_

<details><summary>↩ Tool result · `toolu_01MujU7gXC1Mga4ySAStRjTN`</summary>

```text
Web search results for query: "Causal Reward Adjustment CRA reward hacking sparse autoencoder PRM 2508.04216"

Links: [{"title":"[2508.04216] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/abs/2508.04216"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/html/2508.04216v1"},{"title":"[PDF] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Causal-Reward-Adjustment:-Mitigating-Reward-Hacking-Song-Song/d98cf088a2ca29326352d4499c11d32b25e75bfa"},{"title":"Avoiding Reward Hacking","url":"https://www.emergentmind.com/topics/avoiding-reward-hacking"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in ...","url":"https://arxiv.org/pdf/2508.04216"},{"title":"Reward Hacking Defense Rubric","url":"https://www.emergentmind.com/topics/reward-hacking-defense-rubric"},{"title":"IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/pdf/2602.19416"},{"title":"Interpretable Reward Model via Sparse Autoencoder","url":"https://arxiv.org/pdf/2508.08746"}]

Based on the search results, I found comprehensive information about the paper you're looking for.

## Overview

Causal Reward Adjustment (CRA) is a method that mitigates reward hacking by estimating the true reward of a reasoning path, using sparse autoencoders on the PRM's internal activations to recover interpretable features, then corrects confounding by using backdoor adjustment.

## The Problem

External reasoning systems are prone to reward hacking, where high-scoring but logically incorrect paths are assigned high scores by the PRMs, leading to incorrect answers. From a causal inference perspective, this phenomenon is primarily attributed to the presence of confounding semantic features.

## Technical Approach

The CRA method works in three main steps:

1. A sparse autoencoder (SAE) is trained on the hidden representations of the PRM, where the SAE learns to encode each internal representation into a sparse latent vector, with each dimension corresponding to a distinct semantic feature.

2. Reward hacking features are detected by computing the activation distribution of each feature over reasoning steps labeled as reward hacking versus normal ones, applying two-sample t-tests to quantify statistical separation.

3. Backdoor adjustment is performed by marginalizing over identified features, simulating reward scores under different values of confounding features and computing weighted averages using empirical frequencies, thereby removing spurious correlations and yielding an unbiased estimate of the true causal effect.

## Results

Experiments on math solving datasets demonstrate that CRA mitigates reward hacking and improves final accuracy, without modifying the policy model or retraining the PRM.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35e4fd65-d665-475c-95dc-9df18d456cae",
  "isSidechain": false,
  "promptId": "d551cef2-18fb-4f70-a90b-9c3e21e7f021",
  "type": "user",
  "uuid": "c28c7d32-8977-462a-9aa4-f877d1a239ad",
  "toolUseResult": {
    "query": "Causal Reward Adjustment CRA reward hacking sparse autoencoder PRM 2508.04216",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NRSvwPQbWE53GJHhQNR6Se",
        "content": [
          {
            "title": "[2508.04216] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/abs/2508.04216"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/html/2508.04216v1"
          },
          {
            "title": "[PDF] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Causal-Reward-Adjustment:-Mitigating-Reward-Hacking-Song-Song/d98cf088a2ca29326352d4499c11d32b25e75bfa"
          },
          {
            "title": "Avoiding Reward Hacking",
            "url": "https://www.emergentmind.com/topics/avoiding-reward-hacking"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in ...",
            "url": "https://arxiv.org/pdf/2508.04216"
          },
          {
            "title": "Reward Hacking Defense Rubric",
            "url": "https://www.emergentmind.com/topics/reward-hacking-defense-rubric"
          },
          {
            "title": "IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking",
            "url": "https://arxiv.org/pdf/2602.19416"
          },
          {
            "title": "Interpretable Reward Model via Sparse Autoencoder",
            "url": "https://arxiv.org/pdf/2508.08746"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the paper you're looking for.\n\n## Overview\n\nCausal Reward Adjustment (CRA) is a method that mitigates reward hacking by estimating the true reward of a reasoning path, using sparse autoencoders on the PRM's internal activations to recover interpretable features, then corrects confounding by using backdoor adjustment.\n\n## The Problem\n\nExternal reasoning systems are prone to reward hacking, where high-scoring but logically incorrect paths are assigned high scores by the PRMs, leading to incorrect answers. From a causal inference perspective, this phenomenon is primarily attributed to the presence of confounding semantic features.\n\n## Technical Approach\n\nThe CRA method works in three main steps:\n\n1. A sparse autoencoder (SAE) is trained on the hidden representations of the PRM, where the SAE learns to encode each internal representation into a sparse latent vector, with each dimension corresponding to a distinct semantic feature.\n\n2. Reward hacking features are detected by computing the activation distribution of each feature over reasoning steps labeled as reward hacking versus normal ones, applying two-sample t-tests to quantify statistical separation.\n\n3. Backdoor adjustment is performed by marginalizing over identified features, simulating reward scores under different values of confounding features and computing weighted averages using empirical frequencies, thereby removing spurious correlations and yielding an unbiased estimate of the true causal effect.\n\n## Results\n\nExperiments on math solving datasets demonstrate that CRA mitigates reward hacking and improves final accuracy, without modifying the policy model or retraining the PRM."
    ],
    "durationSeconds": 11.016985266999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "35e4fd65-d665-475c-95dc-9df18d456cae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-19T18:53:10.216Z_

```json
{
  "parentUuid": "c28c7d32-8977-462a-9aa4-f877d1a239ad",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "32ecf4b9-1ea5-4393-bede-b49c68c1b972",
  "timestamp": "2026-05-19T18:53:10.216Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-19T18:53:28.254Z_

<details><summary>Logged reasoning block</summary>

```text
This is very important - I found that there's a recent paper (arXiv:2508.04216) called "Causal Reward Adjustment" (CRA) that does something quite related to what this proposal claims to be novel. CRA uses sparse autoencoders on PRM internal activations to identify confounding features and applies backdoor adjustment to mitigate reward hacking. This is a causal approach to PRM reward hacking defense.

Let me also check the date - 2508.04216 would be from August 2025. Wait, actually if the current date is May 2026, and the paper is 2508, that could be August 2025 or possibly May 2026 (if using a different numbering). 

The arXiv ID format is YYMM.NNNNN, so 2508 definitely means August 2025, which predates the current proposal by several months.

Looking at what the CRA paper actually does versus what this proposal claims - CRA uses sparse autoencoders and mechanistic interpretability to identify confounding features causing reward hacking, while the proposal's core contribution is using calibration quality as a causal lever to prevent it. These are fundamentally different approaches to the same problem.

I should search for any existing work that directly connects calibration quality to reward hacking resistance to see if that specific link has already been established.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32ecf4b9-1ea5-4393-bede-b49c68c1b972",
  "isSidechain": false,
  "requestId": "req_011CbCS6NMikNopNsZhNTNmJ",
  "type": "assistant",
  "uuid": "f0db32e3-df5e-48ba-a152-18fe2c813bed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yArhVYX9Hakoojt8w5YbN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1002,
      "cache_read_input_tokens": 25399,
      "output_tokens": 617,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1002,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 617,
          "cache_read_input_tokens": 25399,
          "cache_creation_input_tokens": 1002,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1002
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

_source line 32 · 2026-05-19T18:53:28.257Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016j4Ws9NueQBJYpcZH3YZYv`</summary>

```json
{
  "query": "pessimistic reward model uncertainty step-level RL training reward hacking defense 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0db32e3-df5e-48ba-a152-18fe2c813bed",
  "isSidechain": false,
  "requestId": "req_011CbCS6NMikNopNsZhNTNmJ",
  "type": "assistant",
  "uuid": "7d590b01-be39-416a-82a5-58f534d8673b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yArhVYX9Hakoojt8w5YbN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1002,
      "cache_read_input_tokens": 25399,
      "output_tokens": 617,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1002,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 617,
          "cache_read_input_tokens": 25399,
          "cache_creation_input_tokens": 1002,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1002
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "7d590b01-be39-416a-82a5-58f534d8673b",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking proposal",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56"
}
```

---

### Tool result

_source line 35 · 2026-05-19T18:53:35.966Z_

<details><summary>↩ Tool result · `toolu_016j4Ws9NueQBJYpcZH3YZYv`</summary>

```text
Web search results for query: "pessimistic reward model uncertainty step-level RL training reward hacking defense 2025 2026"

Links: [{"title":"Reward Hacking Defense Rubric","url":"https://www.emergentmind.com/topics/reward-hacking-defense-rubric"},{"title":"Avoiding Reward Hacking","url":"https://www.emergentmind.com/topics/avoiding-reward-hacking"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/pdf/2604.04648"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/pdf/2602.10623"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"Probabilistic Uncertain Reward Model","url":"https://arxiv.org/pdf/2503.22480"}]

I found relevant research on pessimistic reward modeling, uncertainty quantification, and reward hacking defenses from 2025-2026. Here are the key findings:

## Pessimistic Reward Modeling

Pessimistic reward modeling (PET) embeds pessimism so that even "greedy" policy optimization under the learned reward is robust to overestimation, and requires no KL regularization. This approach trains the proxy reward via a minimax objective so that it is a provable lower bound on the true reward for all "best-of-n" policies, with sublinear regret guarantees.

## Uncertainty Quantification Approaches

The Probabilistic Uncertain Reward Model (PURM) generalizes scalar reward outputs to Gaussian distributions, quantifies Bhattacharyya coefficient overlaps for reward uncertainty, and penalizes learning in regions of high uncertainty to prevent overoptimization. Additionally, reward ensembles, where multiple models are trained and their predictions are aggregated pessimistically, can better mitigate reward hacking and lead to improved performance.

## Step-Level Reward Hacking Defense

One approach penalizes out-of-distribution responses by subtracting per-response uncertainty estimates from the scores assigned by the reward model, and then selects the response with the highest pessimistic score.

## Root Causes and Broader Context

The reward hacking problem occurs because the proxy reward model is not always accurate, and there could exist responses that are not favored by human preference but the learned proxy reward model overestimates them and gives them high rewards.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d590b01-be39-416a-82a5-58f534d8673b",
  "isSidechain": false,
  "promptId": "d551cef2-18fb-4f70-a90b-9c3e21e7f021",
  "type": "user",
  "uuid": "6063fb50-9159-40a7-9637-2e52c29c3783",
  "toolUseResult": {
    "query": "pessimistic reward model uncertainty step-level RL training reward hacking defense 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0162njA3pzNcAe2yGN1WuP9X",
        "content": [
          {
            "title": "Reward Hacking Defense Rubric",
            "url": "https://www.emergentmind.com/topics/reward-hacking-defense-rubric"
          },
          {
            "title": "Avoiding Reward Hacking",
            "url": "https://www.emergentmind.com/topics/avoiding-reward-hacking"
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
            "title": "Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/pdf/2602.10623"
          },
          {
            "title": "Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation",
            "url": "https://arxiv.org/html/2602.09305v1"
          },
          {
            "title": "Probabilistic Uncertain Reward Model",
            "url": "https://arxiv.org/pdf/2503.22480"
          }
        ]
      },
      "I found relevant research on pessimistic reward modeling, uncertainty quantification, and reward hacking defenses from 2025-2026. Here are the key findings:\n\n## Pessimistic Reward Modeling\n\nPessimistic reward modeling (PET) embeds pessimism so that even \"greedy\" policy optimization under the learned reward is robust to overestimation, and requires no KL regularization. This approach trains the proxy reward via a minimax objective so that it is a provable lower bound on the true reward for all \"best-of-n\" policies, with sublinear regret guarantees.\n\n## Uncertainty Quantification Approaches\n\nThe Probabilistic Uncertain Reward Model (PURM) generalizes scalar reward outputs to Gaussian distributions, quantifies Bhattacharyya coefficient overlaps for reward uncertainty, and penalizes learning in regions of high uncertainty to prevent overoptimization. Additionally, reward ensembles, where multiple models are trained and their predictions are aggregated pessimistically, can better mitigate reward hacking and lead to improved performance.\n\n## Step-Level Reward Hacking Defense\n\nOne approach penalizes out-of-distribution responses by subtracting per-response uncertainty estimates from the scores assigned by the reward model, and then selects the response with the highest pessimistic score.\n\n## Root Causes and Broader Context\n\nThe reward hacking problem occurs because the proxy reward model is not always accurate, and there could exist responses that are not favored by human preference but the learned proxy reward model overestimates them and gives them high rewards."
    ],
    "durationSeconds": 7.704127951000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7d590b01-be39-416a-82a5-58f534d8673b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-19T18:53:38.709Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K3LcHpghS4BPiQvNkfHtxn`</summary>

```json
{
  "query": "CoRL 2026 conference robot learning submission topics call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6063fb50-9159-40a7-9637-2e52c29c3783",
  "isSidechain": false,
  "requestId": "req_011CbCS8GZmE8nPZBvVdTfv8",
  "type": "assistant",
  "uuid": "470a112a-0f98-4a47-98c5-e06cf0d5333f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017CcfThnpk9HmPihuxcYfwL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1314,
      "cache_read_input_tokens": 26401,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1314,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 26401,
          "cache_creation_input_tokens": 1314,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1314
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

_source line 37 · 2026-05-19T18:53:46.400Z_

<details><summary>↩ Tool result · `toolu_01K3LcHpghS4BPiQvNkfHtxn`</summary>

```text
Web search results for query: "CoRL 2026 conference robot learning submission topics call for papers"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"}]

Based on the search results, here's information about CoRL 2026's call for papers and submission topics:

## Submission Topics

CoRL welcomes papers in areas such as learning representations for robotic perception and control, learning robot foundation models or general-purpose knowledge systems for robotics, imitation learning for robotics, reinforcement learning for control of physical robots, and video models and latent world models for robot learning. Additionally, CoRL covers topics including sim-to-real transfer, robot perception through learning, learned manipulation and locomotion, and learning-based planning.

## Submission Requirements

Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. All submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments.

## Key Deadlines

The paper submission deadline is May 29, 2026, and CoRL 2026 will be held at the JW Marriott Austin in Austin, TX from November 9–12, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "470a112a-0f98-4a47-98c5-e06cf0d5333f",
  "isSidechain": false,
  "promptId": "d551cef2-18fb-4f70-a90b-9c3e21e7f021",
  "type": "user",
  "uuid": "967717ab-a20e-475f-ad5f-c9983bd37f3c",
  "toolUseResult": {
    "query": "CoRL 2026 conference robot learning submission topics call for papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SJJmvtnHyVahJFf5dVdtpn",
        "content": [
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf"
          },
          {
            "title": "CoRL 2026 - Call for Workshops",
            "url": "https://www.corl.org/contributions/call-for-workshops"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          }
        ]
      },
      "Based on the search results, here's information about CoRL 2026's call for papers and submission topics:\n\n## Submission Topics\n\nCoRL welcomes papers in areas such as learning representations for robotic perception and control, learning robot foundation models or general-purpose knowledge systems for robotics, imitation learning for robotics, reinforcement learning for control of physical robots, and video models and latent world models for robot learning. Additionally, CoRL covers topics including sim-to-real transfer, robot perception through learning, learned manipulation and locomotion, and learning-based planning.\n\n## Submission Requirements\n\nSubmissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. All submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments.\n\n## Key Deadlines\n\nThe paper submission deadline is May 29, 2026, and CoRL 2026 will be held at the JW Marriott Austin in Austin, TX from November 9–12, 2026."
    ],
    "durationSeconds": 7.686864655000012,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "470a112a-0f98-4a47-98c5-e06cf0d5333f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-19T18:54:35.652Z_

<details><summary>Logged reasoning block</summary>

```text
This is very important! CoRL 2026 is the Conference on Robot Learning. The topics are specifically about robotics: robot perception, robot control, manipulation, locomotion, sim-to-real transfer, etc. This proposal is about PRM calibration and reward hacking for LLM mathematical reasoning - it has NOTHING to do with robotics.

This is a fundamental venue mismatch. The proposal would almost certainly be desk-rejected at CoRL because it doesn't address any robotics problem. Let me note this in my evaluation.

Wait, but the system prompt says to evaluate for "CoRL 2026 主会的中稿潜力" and the rubric mentions "NLP/CL 领域". 

There's a clear contradiction here - the system prompt explicitly specifies CoRL 2026, but the evaluation rubric references NLP/Computational Linguistics impact, which doesn't align with a robotics conference. I should flag this discrepancy prominently since submitting an LLM reasoning paper to CoRL would be a critical mismatch, though it's possible the user intended a different venue entirely.

Now let me examine the core idea itself: the claim is that PRM calibration quality directly causes resistance to reward hacking, and that a calibration-gated step-level pessimism approach can exploit this relationship. The key question is whether the full framework with causal isolation and CGSP meaningfully improves over a simpler baseline - just applying temperature scaling to PRMs and testing if it mitigates reward hacking.

There are other obvious alternatives too: ensemble methods with pessimistic aggregation are already known to reduce reward hacking, so I need to understand how CGSP compares. The CGSP formula itself - using a lower confidence bound weighted by calibration quality - is fairly standard from bandit and offline RL work, so the novelty really hinges on applying it at the step level with calibration weighting.

The central assumptions here are shaky: calibration quality being causally linked to hackability is the core hypothesis but unproven, post-hoc calibration methods might not actually achieve enough improvement to demonstrate an effect, and computing Hessians at scale for step-level analysis is computationally expensive.

Looking at related work, several papers already tackle pieces of this: CRA does causal analysis of reward hacking using sparse autoencoders, PURM extends to probabilistic uncertainty, and Caution already defends against pessimistic reward hacking. The novelty is mainly in causally isolating calibration from representation changes, applying it step-by-step, and using calibration as a gate for adaptive pessimism - but that's moderate novelty at best. Plus there's a venue problem: this reads like a general ML paper on reward robustness, not robotics work, so CoRL would likely desk-reject it.

The core insight that better calibration makes rewards harder to hack is somewhat intuitive - most people would expect more accurate models to be more robust. The causal isolation experiment is the most novel contribution, and connecting the PRM calibration and hackability literatures is real work, but the question is whether that connection is surprising enough or just confirms what we'd naturally assume.

For CoRL specifically, this is a complete scope mismatch - the conference focuses on robot learning, manipulation, and physical systems, while this work is about LLM math reasoning and RLHF reward hacking. It would get desk-rejected immediately. For more appropriate venues like NeurIPS or ICML, I'd estimate around 25-35% acceptance probability.

The core issue is that while the causal isolation methodology and step-level analysis provide some novelty, the connection between PRM calibration and robustness feels somewhat intuitive, and related work like CRA already explores causal PRM analysis. The significance is real given the importance of the problem, but the contribution feels incremental.

For a better-fit venue like NeurIPS or ICML, I'd estimate 25-35% acceptance probability, but at CoRL it drops below 5% since this is fundamentally an NLP paper with no robotics component—the mention of RL algorithms like GRPO and PPO doesn't change that the application domain is purely math reasoning on MATH-500 and AIME benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "967717ab-a20e-475f-ad5f-c9983bd37f3c",
  "isSidechain": false,
  "requestId": "req_011CbCS936BDXAP8eGcXLddX",
  "type": "assistant",
  "uuid": "f49d6e2b-500e-4a1a-9845-c918831e0e90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGNARXzNGLcqx4yNrMLLUa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 27715,
      "output_tokens": 6643,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6643,
          "cache_read_input_tokens": 27715,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
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

_source line 39 · 2026-05-19T18:56:18.604Z_

现在我有了足够的调研信息来进行评估。让我整理分析。

---

```
【阶段】: Triage
```

## ⚠️ 致命问题：严重的投稿venue不匹配

**在进入正式评估之前，必须首先指出一个致命问题：CoRL（Conference on Robot Learning）是一个机器人学习会议**，其征稿范围明确包括：robot perception、robot control、manipulation、locomotion、sim-to-real transfer、robot foundation models 等。本 proposal 研究的是 LLM 数学推理中的 PRM 校准与 reward hacking 防御（评测数据集为 MATH-500 和 AIME），与机器人学习**零关联**。提交至 CoRL 几乎必然被 desk reject。

**如果投稿目标确实是 CoRL，中稿概率接近 0%，无需进一步评估。**

以下评估假设 proposal 将投稿至**合适的 venue（如 NeurIPS、ICML、ICLR 等 ML/NLP 顶会）**，仅评估 idea 本身的质量。

---

```
【领域调研】:
```

- **[Know What You Don't Know: Uncertainty Calibration of PRMs](https://arxiv.org/abs/2506.09338)** (NeurIPS 2025): 首次系统性研究 PRM 校准问题，发现 PRM 在难题上系统性高估成功概率，提出 quantile regression 校准方法。是 Thread 1 (PRM Calibration) 的奠基工作。本 proposal 的 Component A 直接建立在此基础上。

- **[Distributional PRMs via Conditional Optimal Transport](https://arxiv.org/abs/2605.06785)** (May 2026 preprint): 用条件最优传输获得校准的单调分位数函数，改善 BoN 在 MATH-500 和 AIME 上的表现。**从未测试鲁棒性/抗攻击能力**——这正是本 proposal 声称要填补的空白。

- **[Reward Under Attack: Analyzing Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)** (March 2026): 证明 PRM 是灾难性可攻击的——梯度攻击使 PRM 奖励膨胀 4 倍，RL 训练达到近乎完美的 PRM 奖励但实际准确率 <4%，43% 的奖励增益来自风格捷径。**未提出任何基于校准的防御**。本 proposal 的 Thread 2 基础。

- **[Gradient Regularization Prevents Reward Hacking](https://arxiv.org/abs/2602.18037)** (Feb 2026, Ackermann et al.): 建立了奖励表面平坦度与准确度保持之间的理论联系，提出梯度正则化偏向平坦区域。**仅在 outcome-level 单标量奖励模型上工作**，未涉及 step-level PRM。本 proposal 声称要将此扩展到 step-level Hessian 分析。

- **[APRM: Adversarial Training for PRMs](https://arxiv.org/abs/2511.22888)** (Nov 2025): 对抗训练 PRM，+3.4pp 鲁棒性改善。是 proposal 的 baseline 之一。

- **[From Curiosity to Caution (Caution)](https://arxiv.org/abs/2604.04648)** (April 2026): 使用 prediction error 作为悲观度代理进行 BoN 防御。**使用未校准的不确定性代理，非校准概率**。是 proposal 的 baseline 之一。

- **[Causal Reward Adjustment (CRA)](https://arxiv.org/abs/2508.04216)** (2025): ⚠️ **proposal 未引用此论文**。CRA 用稀疏自编码器识别 PRM 内部的混淆特征，通过 backdoor adjustment 进行因果校正以缓解 reward hacking。虽然机制不同（SAE vs. 校准），但同样是**因果视角下的 PRM reward hacking 防御**，直接威胁 proposal 的 "first causally rigorous study" 声明。

- **[Probabilistic Uncertain Reward Model (PURM)](https://arxiv.org/abs/2503.22480)** (March 2025): 将标量奖励推广为高斯分布，用不确定性惩罚防止过优化。概念上与 CGSP 的 LCB 思路类似，但在 outcome-level。

- **[Learning a Pessimistic Reward Model in RLHF](https://arxiv.org/abs/2505.20556)** (May 2025): 通过 minimax 目标训练悲观代理奖励作为真实奖励的下界。理论上与 CGSP 的悲观主义方向相似。

- **调研总结**: PRM 校准和 PRM 可攻击性确实是两个相对独立的研究线程，但"桥接"的空间正在被多个方向的工作侵蚀。CRA (2508.04216) 已经从因果视角处理 PRM reward hacking；PURM 和 Pessimistic RM 已经在做不确定性驱动的悲观防御。本 proposal 的独特角色——"用校准质量作为因果变量"——仍有真实的 delta，但并非如 proposal 所声称的那样是一片完全未被触及的空白。

---

```
【Trivial Alternative 检验】:
```

**存在显著的 trivial alternative 威胁。**

核心问题：如果 "更好的校准 → 更强的抗攻击能力"，那最简单的 trivial baseline 就是——**直接对 PRM 做 temperature scaling（一个参数的 post-hoc 校准），然后测试抗攻击能力是否改善**。这实际上就是 proposal 自己 Component B1 的一部分。

如果 temperature scaling 就能显著降低 hackability，那么：
1. 整个 48-configuration 相关性研究的增量价值被大幅削弱（一个参数就够了）
2. CGSP 的复杂公式（μ_t − α·σ_t/√c_t）相对于 "简单校准 + 标准 LCB" 的增量价值需要严格论证
3. 因果隔离实验变得不那么必要——如果 post-hoc calibration 就有效，因果关系已经隐含地被建立了

**增量价值的真实所在**：如果只有 calibration 改善有效（而 CKA-matched representation change 无效），且 CGSP 的 adaptive pessimism 明显优于 static pessimism，那 proposal 的贡献才能站住脚。但这取决于实验结果，idea 层面上这个风险是真实的。

另一个 trivial alternative：**ensemble disagreement**（已有工作如 Coste et al.）已经是一种不确定性驱动的悲观方法。CGSP 相比 ensemble-min 的增量需要仔细论证——proposal 声称 ensemble 是 "uncalibrated"，但 ensemble disagreement 本身就是一种合理的不确定性度量，不需要显式校准。

---

```
【前提假设检验】:
```

核心 claim 的逻辑链条：

**校准质量高 → 奖励信号更准确 → 梯度攻击/RL优化更难利用 → hackability 降低**

这条链中有两个关键的未验证假设：

1. **"校准 = 准确"的等式假设**: 校准（calibration）衡量的是 "预测概率与真实频率的匹配度"，但一个完美校准的模型仍然可能有 sharp but exploitable 的奖励表面。校准改善的是概率输出的可靠性，但未必改变模型在对抗性输入上的决策边界。一个 well-calibrated 但在特定 adversarial direction 上仍然脆弱的 PRM 是完全可能的。**Proposal 隐含假设校准改善等同于鲁棒性改善，这个等式没有理论保证。**

2. **Post-hoc calibration "provably preserves representations" 的过度声明**: Temperature scaling 确实不改变 logits 的排序，但它改变了梯度的大小（因为 softmax 的温度影响梯度 landscape）。在梯度攻击场景下，temperature scaling 改变了 loss surface 的曲率，这可能影响攻击效果——但这不是 "calibration" 的功劳，而是 "gradient scaling" 的副作用。**因果隔离实验可能测到的不是"校准的因果效应"，而是"温度缩放改变梯度 landscape"的效应。**

3. **Step-level flatness compounding 假设**: Proposal 假设 step-level 的平坦度会以有意义的方式沿轨迹组合，影响 outcome-level hackability。但 T 个 step 的 Hessian 如何 "组合" 是一个非平凡的数学问题，proposal 没有给出任何理论框架说明这种组合如何工作。

---

```
【3 维度打分】:
```

### 1. Novelty: 中 (偏弱)

**理由**：

- **正面**: 将 PRM 校准线程与 PRM 可攻击性线程显式桥接，这个研究问题的定位是真实的——目前确实没有论文直接测试 "校准质量是否因果地决定抗攻击能力"。因果隔离实验设计（post-hoc vs. fine-tuning vs. matched representation change control）在方法论上有新意。

- **负面**:
  - **CRA (arXiv:2508.04216)** 已经从因果视角（用 backdoor adjustment）处理 PRM reward hacking 防御，且 proposal **未引用**此工作。"First causally rigorous study" 的声明可能被审稿人质疑。
  - CGSP 的核心公式 r̃_t = μ_t − α·σ_t/√c_t 本质上是 **LCB (Lower Confidence Bound) 的标准形式**，加上 calibration quality 的加权。这在 bandit/offline RL 文献中是常见思路。创新性主要在于 "应用场景"（step-level PRM + RL training），而非算法本身。
  - **PURM (arXiv:2503.22480)** 和 **Pessimistic RM (arXiv:2505.20556)** 已经在做不确定性驱动的悲观奖励建模。CGSP 的差异化（step-level + calibration-gated）是增量的，不是范式级的。
  - 核心发现如果是 positive（"better calibrated PRMs are harder to hack"），多数审稿人的反应可能是 **"I would have guessed this"** 而非 "surprising"。

### 2. Significance: 中

**理由**：

- **正面**: PRM 是 LLM 推理的核心组件，reward hacking 是 RLHF/RLVR 的核心问题。如果能建立校准→鲁棒性的因果链，对实践有直接指导意义（"先校准再用 PRM 做 RL"）。
  
- **负面**: 
  - 实际影响可能有限——如果结论是 "校准有帮助"，practitioners 已经有动机去做校准（因为校准本身就改善 BoN 性能，如 Distributional PRM 所示）。这个工作可能只是为已有实践提供了因果层面的解释，而非开辟新实践。
  - CGSP 的实用性取决于其相对 simpler baselines（如 temperature scaling + ensemble-min）的增量收益大小。如果增量很小，方法的复杂度不值得。
  - 研究问题虽然重要，但 "桥接两个线程" 的贡献类型在顶会中通常被视为 solid but not exciting。

### 3. Related Work: 强 (偏中)

**理由**：

- **正面**: 对两条主线（PRM Calibration 和 PRM Hackability）的覆盖非常详尽，差异化定位清晰。对 Ackermann et al. 的区分论述（outcome-level vs. step-level）有说服力。对 Caution、InferenceTimePessimism、URM 等相邻工作的区分也到位。

- **负面**: 
  - **遗漏了 CRA (arXiv:2508.04216)**——这是一个从因果视角处理 PRM reward hacking 的直接竞争工作，未引用是严重疏忽。
  - **遗漏了 PURM (arXiv:2503.22480)**——概率化不确定性奖励建模，概念上与 CGSP 高度相关。
  - **遗漏了 Pessimistic RM (arXiv:2505.20556)**——悲观奖励建模的理论工作。
  - 这些遗漏可能导致审稿人认为 proposal 的 novelty 声明过于强烈。

---

```
【概率估计】: 20% - 32%，中位 25%
```

（注：此概率基于投稿至合适 venue 如 NeurIPS/ICML/ICLR。**若投稿 CoRL，概率为 ~0%，因 scope 完全不匹配。**）

```
【估计理由】:
```

Idea 的研究问题定位是真实的——PRM 校准与可攻击性之间的因果关系确实未被直接研究。但核心贡献受三个因素限制：

1. **Novelty 上界受限**（最主要制约因素）：核心发现若 positive（"校准好→更难攻击"），审稿人反应大概率是 "makes sense, I would have guessed this"。CRA 已经从因果视角切入 PRM reward hacking，PURM/Pessimistic RM 已经在做不确定性悲观防御。CGSP 的公式是标准 LCB。整体 novelty 是增量级别的组合创新，而非范式级别的新洞察。

2. **Trivial alternative 威胁真实**：temperature scaling 一个参数就可能解释大部分效果，且这个 trivial baseline 是 proposal 自己实验的一部分——如果它效果就很好，paper 的 story 会很尴尬。

3. **因果隔离方法论有漏洞**：post-hoc calibration 改变梯度 landscape 的副作用可能混淆因果推断，使 "calibration per se causes robustness" 的声明站不住脚。

这些因素将 idea 定位在 "方向正确、有真实 delta、但核心发现不 surprising" 的区间（25-35% 的下半部分）。

```
【主要风险】:
```

1. **"I would have guessed this" 风险**: 如果核心实验结论是 "better calibrated PRMs are more robust"，审稿人可能认为这是一个 trivially expected result，缺乏 surprising insight。这是最大的 idea 层面风险。

2. **因果声明被攻击的风险**: 审稿人可能指出 post-hoc calibration（尤其是 temperature scaling）改变梯度 landscape 是其降低 hackability 的真正机制（而非"校准"本身），从而瓦解 "calibration causally determines hackability" 的核心 claim。同时 CRA 的存在削弱 "first causal study" 的声明。

---

Sources:
- [Know What You Don't Know: Uncertainty Calibration of PRMs](https://arxiv.org/abs/2506.09338)
- [Distributional PRMs via Conditional Optimal Transport](https://arxiv.org/abs/2605.06785)
- [Reward Under Attack: Analyzing Robustness and Hackability of PRMs](https://arxiv.org/abs/2603.06621)
- [Gradient Regularization Prevents Reward Hacking](https://arxiv.org/abs/2602.18037)
- [APRM: Adversarial Training for PRMs](https://arxiv.org/abs/2511.22888)
- [From Curiosity to Caution](https://arxiv.org/abs/2604.04648)
- [Causal Reward Adjustment (CRA)](https://arxiv.org/abs/2508.04216)
- [Probabilistic Uncertain Reward Model (PURM)](https://arxiv.org/abs/2503.22480)
- [Learning a Pessimistic Reward Model in RLHF](https://arxiv.org/abs/2505.20556)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f49d6e2b-500e-4a1a-9845-c918831e0e90",
  "isSidechain": false,
  "requestId": "req_011CbCS936BDXAP8eGcXLddX",
  "type": "assistant",
  "uuid": "853f0e8e-82eb-4919-9e70-19b7a18d120c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGNARXzNGLcqx4yNrMLLUa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 27715,
      "output_tokens": 6643,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6643,
          "cache_read_input_tokens": 27715,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
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

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "853f0e8e-82eb-4919-9e70-19b7a18d120c",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking proposal",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "853f0e8e-82eb-4919-9e70-19b7a18d120c",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM calibration and reward hacking proposal",
  "sessionId": "ae4450f1-56bb-4a89-8ce0-2088fffebc56"
}
```

---
