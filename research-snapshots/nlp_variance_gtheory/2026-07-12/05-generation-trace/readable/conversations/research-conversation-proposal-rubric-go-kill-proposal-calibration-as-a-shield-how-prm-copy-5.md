# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Calibration as a Shield: How PRM 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/1bbdce7f-bb04-43de-8813-913beef450af.jsonl`
- **Structured JSON:** [`3a5291658bdc71512ca0.json`](../../sessions/3a/3a5291658bdc71512ca0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:41:13.724Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:41:13.724Z",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense\n\n## Description\nWe present the first causally rigorous study connecting PRM calibration quality to adversarial exploitability, and propose Calibration-Gated Step-Level Pessimism (CGSP), a novel defense that transforms calibrated uncertainty into adaptive reward hacking resistance during RL training. Our work bridges two mature but isolated research threads (PRM calibration and PRM hackability) through four contributions. First, an expanded correlation study across 48 configurations (8 PRMs × 6 calibration methods) provides sufficient statistical power (n=48, detecting r≥0.29 at p<0.05) to establish whether calibration quality predicts hackability metrics under gradient attacks, RL-induced hacking (GRPO on AIME), and BoN overoptimization (MATH-500), stratified by problem difficulty. Second, causal isolation experiments separate calibration's true effect from representation change artifacts: we compare post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) that provably preserve model representations against fine-tuning-based methods, with CKA verification and matched-representation-change controls. Third, step-level Hessian spectral analysis goes beyond Ackermann et al.'s outcome-level gradient norm analysis (which applies only to single-scalar reward models) to reveal how calibration affects the multi-reward compositional geometry of PRMs — analyzing how step-level flatness compounds across trajectories. Fourth, CGSP replaces raw PRM rewards during RL training with r̃_t = μ_t − α·σ_t/√c_t, where calibrated uncertainty σ_t and calibration quality c_t adaptively modulate pessimism per-step — trusted when calibration is tight, pessimistic when uncertainty is high — with a Calibration Drift Detector that monitors ECE on current-policy rollouts to flag distribution-shift-induced reward hacking in real time. CGSP differs from existing defenses (Caution uses prediction error, PET uses global pessimism, ensemble methods are uncalibrated) by being step-level, calibration-grounded, and adaptive. We evaluate CGSP against 5 baselines (uncalibrated GRPO, APRM, Caution, ensemble-min, gradient regularization) on MATH-500 and AIME, measuring both reward-accuracy alignment and downstream task accuracy.\n\n## Core Problem\nPRM calibration research and PRM hackability research are entirely separate threads with zero cross-citation — but the deeper problem is that we lack both (a) causal evidence for whether calibration actually determines hackability (vs. being merely correlated), and (b) a principled, step-level defense mechanism that leverages calibrated uncertainty to prevent reward hacking during RL training. Existing ad-hoc defenses (adversarial training, gradient regularization, pessimistic BoN) operate at the outcome level without exploiting the unique step-level structure of PRMs.\n\n## Opportunity\nThree recent developments create a uniquely favorable moment. First, Distributional PRMs (arXiv:2605.06785, May 2026) achieve calibrated step-level uncertainty via conditional optimal transport but never test robustness. Second, Tiwari et al. (arXiv:2603.06621, March 2026) demonstrate that PRMs are catastrophically hackable — near-perfect PRM rewards with <4% actual accuracy — but propose no calibration-based defense. Third, the causal isolation toolkit is mature: post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) modify only the output mapping without changing model representations, enabling controlled experiments that separate calibration effects from representation effects. No existing paper bridges these threads. Ackermann et al.'s gradient regularization work (arXiv:2602.18037) operates exclusively on outcome-level reward models with single-scalar rewards, never touching step-level PRM geometry. The CoT Entropy paper (arXiv:2502.11250) named this connection as future work 16 months ago with no follow-up. The window for a definitive, causally rigorous study is open but narrowing.\n\n## Landscape\nTwo parallel research threads have developed with zero cross-citation. Thread 1 (PRM Calibration): Park et al. (arXiv:2506.09338, NeurIPS 2025) demonstrate PRMs systematically overestimate success probabilities on hard problems, proposing quantile regression calibration. Distributional PRMs (arXiv:2605.06785, May 2026) use conditional optimal transport for calibrated monotone quantile functions, improving BoN on MATH-500 and AIME. Neither paper tests robustness. Thread 2 (PRM Hackability): Tiwari et al. (arXiv:2603.06621) show gradient attacks inflate PRM rewards 4× and RL achieves near-perfect PRM rewards with <4% accuracy, with 43% of reward gains from stylistic shortcuts. APRM (arXiv:2511.22888) uses adversarial training for +3.4pp robustness. Thread 3 (Adjacent but distinct): Ackermann et al. (arXiv:2602.18037) prove reward surface flatness correlates with accuracy retention for outcome-level RMs, but work exclusively with single-scalar rewards, analyze only gradient norms (no Hessian spectra), and never consider step-level reward models. Their theoretical framework (Propositions 3.3-3.4) assumes a single reward function R(s,a) over complete responses — inapplicable to step-level PRM geometry where T coupled reward surfaces {R_1,...,R_T} interact compositionally. InferenceTimePessimism (arXiv:2506.19248) and Caution (arXiv:2604.04648) apply pessimism for BoN but use uncalibrated uncertainty proxies (prediction error, hedging), not calibrated probabilities. URM (arXiv:2410.00847) decomposes uncertainty into aleatoric/epistemic for outcome-level RMs but not PRMs. Bayesian reward models (arXiv:2402.13210) use Laplace approximation on LoRA weights. Conformal prediction has been applied to RLHF feedback alignment (arXiv:2601.17329) but never to PRM defense. No paper establishes a causal link between calibration quality and hackability, and no paper proposes using calibrated step-level PRM uncertainty as a defense during RL training.\n\n## Approach\nThe study has four components: (A) Expanded Correlation Study, (B) Causal Isolation Experiments, (C) Step-Level Mechanistic Analysis, and (D) Calibration-Gated Step-Level Pessimism (CGSP) defense.\n\n**Component A — Expanded Correlation Study (n≥24 configurations):** Apply 6 calibration methods across 2 tiers to 8 open-source PRMs. Tier 1 (post-hoc, representation-preserving): temperature scaling, Platt scaling, isotonic regression. Tier 2 (model-modifying): quantile regression fine-tuning, conditional optimal transport, Venn-Abers predictors. The 8 PRMs span discriminative (Qwen2.5-Math-PRM-7B, Qwen2.5-Math-PRM-72B, Skywork-o1-Open-PRM-7B, RLHFlow-Llama3.1-8B-PRM, Math-Shepherd-7B, OpenR-Math-psa-7B), generative (GenPRM-7B), and implicit (EurusPRM-Stage2) architectures. Each of the 48 PRM×calibration configurations is subjected to three attack tiers: (i) gradient-based reward inflation following Tiwari et al., (ii) RL-induced reward hacking via GRPO on AIME, and (iii) BoN overoptimization at N∈{1,4,16,64,256} on MATH-500. Compute rank correlations (Spearman ρ, Kendall τ) between calibration metrics (ECE, Brier score, quantile coverage, reliability diagram sharpness) and hackability metrics (reward-accuracy divergence, attack success rate, BoN degradation onset N*). Stratify analysis by problem difficulty (MATH levels 1-5, AMC vs. AIME) to test whether calibration is more protective on hard problems where PRMs are known to be overconfident.\n\n**Component B — Causal Isolation Experiments:** This is the methodological core addressing the reviewer's causation concern. Design: (B1) Post-hoc calibration control: Apply temperature scaling, Platt scaling, and isotonic regression — which provably modify only the output mapping, not internal representations — and measure hackability change. If hackability decreases under post-hoc calibration alone, this establishes that calibration per se (not representation change) causally affects hackability. (B2) Representation change verification: For fine-tuning-based calibration methods (quantile regression, COT), measure representation change at every transformer layer using Centered Kernel Alignment (CKA) between the base PRM and calibrated PRM. (B3) Matched representation change control: Fine-tune PRMs on an auxiliary task (e.g., next-token prediction on math text) that produces CKA-matched representation changes but does NOT improve calibration. If only calibration-improving fine-tuning reduces hackability (not the CKA-matched control), the causal role of calibration is confirmed. (B4) Conformal prediction as the cleanest test: Apply split-conformal prediction to PRM step scores, providing distribution-free coverage guarantees with zero model modification. Test whether conformal-calibrated PRMs resist hacking better than uncalibrated ones.\n\n**Component C — Step-Level Mechanistic Analysis (differentiating from Ackermann et al.):** Unlike Ackermann et al., who analyze only outcome-level gradient norms and max-perturbation sharpness, we perform Hessian spectral analysis at the step level — computing top-k eigenvalues and spectral density of the step-level reward Hessian ∂²R_t/∂h² (where h is the hidden representation at step t). Key questions: (i) Do calibrated PRMs have flatter step-level reward surfaces (lower top Hessian eigenvalue)? (ii) Does flatness vary by step position (early reasoning steps vs. final answer steps)? (iii) Do hackable reward peaks correspond to isolated large Hessian eigenvalues (sharp directions) that gradient attacks exploit? This extends Ackermann et al.'s framework from single-reward geometry to multi-reward compositional geometry: we analyze how step-level flatness/sharpness compounds across a T-step trajectory to determine outcome-level hackability.\n\n**Component D — Calibration-Gated Step-Level Pessimism (CGSP) Defense:** This transforms the paper from measurement to method. CGSP operates during RL training (GRPO/PPO) by replacing raw PRM step rewards with calibration-modulated rewards: r̃_t = μ_t − α · σ_t / √(c_t), where μ_t is the calibrated step reward mean, σ_t is the calibrated uncertainty (from quantile width or conformal interval), c_t is a calibration quality score (inverse ECE computed on a rolling buffer), and α is a pessimism strength hyperparameter. When calibration is high (small σ_t, high c_t), the reward is trusted; when calibration is low (large σ_t, low c_t), pessimism dominates. This differs from existing pessimism (Caution uses prediction error, PET uses global pessimistic fine-tuning, InferenceTimePessimism uses hedging) because CGSP is (i) step-level, (ii) grounded in calibrated probabilities rather than heuristic proxies, and (iii) adaptive — the pessimism automatically strengthens in distribution-shift regions where the PRM becomes miscalibrated. Additionally, we implement a Calibration Drift Detector: during RL training, periodically measure ECE on current-policy rollouts vs. the initial SFT-distribution calibration. When drift exceeds a threshold, flag those trajectory types as potentially hacked and apply reward clipping. This converts calibration from a static property into a dynamic training signal.\n\nBaseline comparisons for CGSP: (i) uncalibrated PRM + GRPO, (ii) APRM adversarial training, (iii) Caution/prediction-error pessimism, (iv) ensemble minimum (following Coste et al.), (v) KL-regularized GRPO, (vi) gradient regularization (Ackermann et al.).\n\nCodebase starting points: young-j-park/prm-calibration for calibration fitting, Tiwari et al.'s PRM-BiasBench for adversarial evaluation, vwxyzjn/open_instruct for GRPO training infrastructure.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '4200 H100-hrs (calibration fitting: 200, rollout generation: 600, gradient attacks: 1000, GRPO RL training: 1600 [including CGSP defense training], BoN evaluation: 400, Hessian spectral analysis: 200, causal isolation controls: 200)', 'timeline': '12-14 weeks', 'estimated_gpu_cost': '$10,500 at ~$2.50/H100-hr'}, 'human_in_loop': {'gpu_hours': '3600 H100-hrs (fewer failed iterations with AI-assisted debugging)', 'timeline': '10-12 weeks', 'claude_api_cost': '$400-700 (code generation, experiment analysis, paper drafting)', 'estimated_gpu_cost': '$9,000 at ~$2.50/H100-hr'}, 'auto_research': {'gpu_hours': '5200 H100-hrs (broader sweeps over α pessimism parameter, calibration drift thresholds, and ablations across all 48 configurations)', 'timeline': '7-9 weeks', 'claude_api_cost': '$1,500-2,000 (automated experiment orchestration, iterative analysis, full draft writing)', 'estimated_gpu_cost': '$13,000 at ~$2.50/H100-hr', 'speed_bottleneck': 'GRPO RL training wall-clock time (~18hrs per PRM×calibration×defense configuration on 4×H100); Hessian spectral analysis requires Lanczos iterations per step per problem; 72B PRM requires 4×H100 for inference'}}\n\n## Inspired By\nField guide gap: PRM overconfidence on OOD problems (Section 5.3 'when more compute hurts'); Untried combination: distributional PRM calibration + PRM hackability analysis; Pattern: connecting two mature but isolated research threads; Reviewer insight: pure measurement is insufficient — the key contribution should be a causal mechanism and a defense method; Methodological insight: post-hoc calibration methods that preserve representations enable clean causal isolation experiments impossible with fine-tuning-based calibration alone\n\n## Target Venues\n- ICLR 2027 (abstract Sep 19, paper Sep 24, 2026)\n- AAAI 2027 (abstract Jul 21, paper Jul 28, 2026)\n- AISTATS 2027 (paper Oct 10, 2026)\n\n## Key References\n- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (arXiv:2506.09338, NeurIPS 2025)\n- Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport (arXiv:2605.06785, May 2026)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv:2603.06621, March 2026)\n- Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards (arXiv:2602.18037, Feb 2026)\n- Adversarial Training for Process Reward Models (arXiv:2511.22888, Nov 2025)\n- From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism (arXiv:2604.04648, April 2026)\n- Inference-Time Reward Hacking in Large Language Models (arXiv:2506.19248, NeurIPS 2025 Spotlight)\n- Uncertainty-Aware Step-wise Verification with Generative Reward Models (arXiv:2502.11250, ICLR 2025 Workshop)\n- Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242, April 2026)\n- Uncertainty-Aware Reward Model (arXiv:2410.00847)\n- Helping or Herding? Reward Model Ensembles Mitigate but Do Not Eliminate Overoptimization (arXiv:2312.09244)\n- Bayesian Reward Models for LLM Alignment (arXiv:2402.13210)\n- Conformal Feedback Alignment for RLHF (arXiv:2601.17329)\n- Taming Overconfidence in LLMs: Reward Calibration in RLHF (arXiv:2410.09724)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (arXiv:2501.03124)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T05:41:13.728Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:41:13.728Z",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af"
}
```

---

## Round 1

39 recorded events

### User

_source line 3 · 2026-05-20T05:41:13.745Z_

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
  "promptId": "889f415c-d586-430e-ba7e-2def0b61d52e",
  "type": "user",
  "uuid": "64bdf082-4423-4254-b261-f8d1531eb1f3",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:41:13.744Z_

```json
{
  "parentUuid": "64bdf082-4423-4254-b261-f8d1531eb1f3",
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
  "uuid": "d7d51a26-3311-4e43-b9ca-2f4163fa6df4",
  "timestamp": "2026-05-20T05:41:13.744Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:41:13.744Z_

```json
{
  "parentUuid": "d7d51a26-3311-4e43-b9ca-2f4163fa6df4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c220dd44-9f90-4eef-9106-10e4189f15ae",
  "timestamp": "2026-05-20T05:41:13.744Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
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
  "leafUuid": "c220dd44-9f90-4eef-9106-10e4189f15ae",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration's causal role in reward hacking resistance",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:41:18.597Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for EMNLP 2026. Let me first do the required web searches to understand the current landscape before making any assessments.

Let me search for:
1. PRM calibration recent work
2. PRM hackability/reward hacking recent work
3. The specific papers referenced in the proposal
4. Any work bridging calibration and hackability
5. CGSP or similar defense mechanisms

Let me start with the web searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c220dd44-9f90-4eef-9106-10e4189f15ae",
  "isSidechain": false,
  "requestId": "req_011CbDHWeK2r2b249hoBXyuZ",
  "type": "assistant",
  "uuid": "d3128721-ae9b-4902-89d3-cc7d52e41308",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4P7TN7Wnm4MoY3qhcpcqy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5654,
      "cache_read_input_tokens": 14333,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 224,
          "cache_read_input_tokens": 14333,
          "cache_creation_input_tokens": 5654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5654
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

_source line 9 · 2026-05-20T05:41:19.383Z_

I need to do thorough web research before evaluating this proposal. Let me search for the key topics and referenced papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3128721-ae9b-4902-89d3-cc7d52e41308",
  "isSidechain": false,
  "requestId": "req_011CbDHWeK2r2b249hoBXyuZ",
  "type": "assistant",
  "uuid": "bfcfb9dd-2d98-4267-8d6b-2b9e46dffbf3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4P7TN7Wnm4MoY3qhcpcqy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5654,
      "cache_read_input_tokens": 14333,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 224,
          "cache_read_input_tokens": 14333,
          "cache_creation_input_tokens": 5654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5654
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

_source line 10 · 2026-05-20T05:41:19.550Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01P9SKAHxqYg7b5KNNfAd3ot`</summary>

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
  "parentUuid": "bfcfb9dd-2d98-4267-8d6b-2b9e46dffbf3",
  "isSidechain": false,
  "requestId": "req_011CbDHWeK2r2b249hoBXyuZ",
  "type": "assistant",
  "uuid": "a40b1e0f-2245-4abd-b8bd-835e7cc77fa1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4P7TN7Wnm4MoY3qhcpcqy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5654,
      "cache_read_input_tokens": 14333,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 224,
          "cache_read_input_tokens": 14333,
          "cache_creation_input_tokens": 5654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5654
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

_source line 11 · 2026-05-20T05:41:19.556Z_

<details><summary>↩ Tool result · `toolu_01P9SKAHxqYg7b5KNNfAd3ot`</summary>

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
  "parentUuid": "a40b1e0f-2245-4abd-b8bd-835e7cc77fa1",
  "isSidechain": false,
  "promptId": "889f415c-d586-430e-ba7e-2def0b61d52e",
  "type": "user",
  "uuid": "288508ff-77e1-483e-8758-6404c9e0a78d",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "a40b1e0f-2245-4abd-b8bd-835e7cc77fa1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T05:41:21.740Z_

Now let me run multiple searches in parallel to cover the key areas of this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "288508ff-77e1-483e-8758-6404c9e0a78d",
  "isSidechain": false,
  "requestId": "req_011CbDHX5B1K227y8ghRy47z",
  "type": "assistant",
  "uuid": "7664ac41-9e77-490a-a292-227c4eeca031",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4t2YqjdzbcLSVE42GJTRq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 19987,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 19987,
          "cache_creation_input_tokens": 750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 750
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

_source line 13 · 2026-05-20T05:41:22.278Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CMvuLKMgCjtLtsk14quHQh`</summary>

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
  "parentUuid": "7664ac41-9e77-490a-a292-227c4eeca031",
  "isSidechain": false,
  "requestId": "req_011CbDHX5B1K227y8ghRy47z",
  "type": "assistant",
  "uuid": "395da886-3276-4f4a-9246-67a06faacb44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4t2YqjdzbcLSVE42GJTRq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 19987,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 19987,
          "cache_creation_input_tokens": 750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 750
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

_source line 14 · 2026-05-20T05:41:28.654Z_

<details><summary>↩ Tool result · `toolu_01CMvuLKMgCjtLtsk14quHQh`</summary>

```text
Web search results for query: "PRM calibration process reward model calibration 2025 2026"

Links: [{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models | OpenReview","url":"https://openreview.net/forum?id=hzMkfIrdDT"},{"title":"[2506.09338] Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/abs/2506.09338"},{"title":"NeurIPS Poster Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://neurips.cc/virtual/2025/poster/116598"},{"title":"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/html/2605.06785"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models for NeurIPS 2025 - IBM Research","url":"https://research.ibm.com/publications/know-what-you-dont-know-uncertainty-calibration-of-process-reward-models"},{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/pdf/2506.09338"},{"title":"Process Reward Models (PRMs): Calibration & Scaling","url":"https://www.emergentmind.com/topics/process-reward-models-prms"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+(PRMs)"}]

Based on the search results, here's what I found about PRM calibration in 2025-2026:

## Key Research on Process Reward Model (PRM) Calibration

Process reward models (PRMs) play a central role in guiding inference-time scaling algorithms for large language models (LLMs), however even state-of-the-art PRMs can be poorly calibrated.

### The Calibration Problem

PRMs tend to overestimate the success probability that a partial reasoning step will lead to a correct final answer, particularly when smaller LLMs are used to complete the reasoning trajectory.

### Quantile Regression Calibration Approach

A quantile-regression calibration has been introduced that aligns outputs with success probabilities. This calibration unlocks instance-adaptive inference-time scaling.

### Instance-Adaptive Scaling (IAS) Framework

A calibrated approach introduces an instance-adaptive scaling (IAS) framework that dynamically adjusts the inference budget based on the estimated likelihood that a partial reasoning trajectory will yield a correct final answer, adapting to each instance and reasoning step when using calibrated PRMs.

### Recent Advancements

Recent work has proposed using conditional optimal transport for calibrating PRMs, estimating a monotonic conditional quantile function over success probabilities estimated by the PRM.

### Practical Impact

Experiments on mathematical reasoning benchmarks show that PRM calibration achieves small calibration error, calibration is crucial for enabling effective instance-adaptive scaling, and the proposed strategy reduces inference costs while maintaining final answer accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "395da886-3276-4f4a-9246-67a06faacb44",
  "isSidechain": false,
  "promptId": "889f415c-d586-430e-ba7e-2def0b61d52e",
  "type": "user",
  "uuid": "8e86551f-b467-4092-8e7d-91b665f69b1e",
  "toolUseResult": {
    "query": "PRM calibration process reward model calibration 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T9zhgLKJhFin7EREw3QFYC",
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
      "Based on the search results, here's what I found about PRM calibration in 2025-2026:\n\n## Key Research on Process Reward Model (PRM) Calibration\n\nProcess reward models (PRMs) play a central role in guiding inference-time scaling algorithms for large language models (LLMs), however even state-of-the-art PRMs can be poorly calibrated.\n\n### The Calibration Problem\n\nPRMs tend to overestimate the success probability that a partial reasoning step will lead to a correct final answer, particularly when smaller LLMs are used to complete the reasoning trajectory.\n\n### Quantile Regression Calibration Approach\n\nA quantile-regression calibration has been introduced that aligns outputs with success probabilities. This calibration unlocks instance-adaptive inference-time scaling.\n\n### Instance-Adaptive Scaling (IAS) Framework\n\nA calibrated approach introduces an instance-adaptive scaling (IAS) framework that dynamically adjusts the inference budget based on the estimated likelihood that a partial reasoning trajectory will yield a correct final answer, adapting to each instance and reasoning step when using calibrated PRMs.\n\n### Recent Advancements\n\nRecent work has proposed using conditional optimal transport for calibrating PRMs, estimating a monotonic conditional quantile function over success probabilities estimated by the PRM.\n\n### Practical Impact\n\nExperiments on mathematical reasoning benchmarks show that PRM calibration achieves small calibration error, calibration is crucial for enabling effective instance-adaptive scaling, and the proposed strategy reduces inference costs while maintaining final answer accuracy."
    ],
    "durationSeconds": 6.37142729,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "395da886-3276-4f4a-9246-67a06faacb44",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T05:41:32.712Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CTuMbeM6feywXn2FJeu5wt`</summary>

```json
{
  "query": "PRM hackability reward hacking process reward model attack robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e86551f-b467-4092-8e7d-91b665f69b1e",
  "isSidechain": false,
  "requestId": "req_011CbDHXmas4na8pdS5VGV8b",
  "type": "assistant",
  "uuid": "de7fe492-b79b-4ac6-9ba1-a963118d9d19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcDaoB827sDTyTmWqG6H13",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 20737,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 855,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 20737,
          "cache_creation_input_tokens": 855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 855
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

_source line 16 · 2026-05-20T05:41:38.800Z_

<details><summary>↩ Tool result · `toolu_01CTuMbeM6feywXn2FJeu5wt`</summary>

```text
Web search results for query: "PRM hackability reward hacking process reward model attack robustness 2025 2026"

Links: [{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"1 Introduction","url":"https://arxiv.org/html/2603.06621"},{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"},{"title":"Reward Under Attack: Evaluating the Sensitivity of Process Reward Models","url":"https://openreview.net/pdf?id=Hw24VOppus"},{"title":"Reward Models and Learning Strategies","url":"https://aclanthology.org/2025.findings-emnlp.970.pdf"},{"title":"Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking | Request PDF","url":"https://www.researchgate.net/publication/400369344_Adversarial_Reward_Auditing_for_Active_Detection_and_Mitigation_of_Reward_Hacking"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=reward+hacking"}]

Based on the search results, here's what I found about PRM hackability, reward hacking, and process reward model robustness in 2025-2026:

## Key Research on PRM Robustness

Process Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure.

### Hackability and Robustness Findings

A major 2026 study titled "Reward Under Attack" provides comprehensive analysis of PRM vulnerabilities:

**Static Perturbation Analysis:** High invariance to surface-level style changes shows reward changes less than 0.1, yet inconsistent detection of logically-corrupted reasoning, with different models failing on different attack types.

**Adversarial Optimization:** Gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks.

**RL-Induced Reward Hacking:** Policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.

### Core Problem

Current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.

### Underlying Issues

PRMs often rely on shallow consistency cues rather than causal reasoning structures, and existing analyses are complemented with controlled perturbations, adversarial optimization, and closed-loop RL evaluation to systematically quantify exploitability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de7fe492-b79b-4ac6-9ba1-a963118d9d19",
  "isSidechain": false,
  "promptId": "889f415c-d586-430e-ba7e-2def0b61d52e",
  "type": "user",
  "uuid": "a336f993-8e4f-4dbb-a9ef-0dc1494b5c02",
  "toolUseResult": {
    "query": "PRM hackability reward hacking process reward model attack robustness 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CQpvtdnR9ECuuc77yn5JzT",
        "content": [
          {
            "title": "GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub",
            "url": "https://github.com/xhwang22/Awesome-Reward-Hacking"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2603.06621"
          },
          {
            "title": "[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/abs/2603.06621"
          },
          {
            "title": "Reward Under Attack: Evaluating the Sensitivity of Process Reward Models",
            "url": "https://openreview.net/pdf?id=Hw24VOppus"
          },
          {
            "title": "Reward Models and Learning Strategies",
            "url": "https://aclanthology.org/2025.findings-emnlp.970.pdf"
          },
          {
            "title": "Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking | Request PDF",
            "url": "https://www.researchgate.net/publication/400369344_Adversarial_Reward_Auditing_for_Active_Detection_and_Mitigation_of_Reward_Hacking"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=reward+hacking"
          }
        ]
      },
      "Based on the search results, here's what I found about PRM hackability, reward hacking, and process reward model robustness in 2025-2026:\n\n## Key Research on PRM Robustness\n\nProcess Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure.\n\n### Hackability and Robustness Findings\n\nA major 2026 study titled \"Reward Under Attack\" provides comprehensive analysis of PRM vulnerabilities:\n\n**Static Perturbation Analysis:** High invariance to surface-level style changes shows reward changes less than 0.1, yet inconsistent detection of logically-corrupted reasoning, with different models failing on different attack types.\n\n**Adversarial Optimization:** Gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks.\n\n**RL-Induced Reward Hacking:** Policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.\n\n### Core Problem\n\nCurrent PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.\n\n### Underlying Issues\n\nPRMs often rely on shallow consistency cues rather than causal reasoning structures, and existing analyses are complemented with controlled perturbations, adversarial optimization, and closed-loop RL evaluation to systematically quantify exploitability."
    ],
    "durationSeconds": 6.083815965999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "de7fe492-b79b-4ac6-9ba1-a963118d9d19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T05:41:41.470Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0193XsvztHK3ZxjrkQhAU58C`</summary>

```json
{
  "query": "calibration reward hacking connection causal link reward model calibration robustness 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a336f993-8e4f-4dbb-a9ef-0dc1494b5c02",
  "isSidechain": false,
  "requestId": "req_011CbDHYVDQ85nQHHXPKt4cA",
  "type": "assistant",
  "uuid": "a3794c23-2aeb-41b7-a3c3-6b56ed921257",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NTRyUEJKfKMkdBSdk45kNL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 21592,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 21592,
          "cache_creation_input_tokens": 872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 872
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

_source line 18 · 2026-05-20T05:41:48.873Z_

<details><summary>↩ Tool result · `toolu_0193XsvztHK3ZxjrkQhAU58C`</summary>

```text
Web search results for query: "calibration reward hacking connection causal link reward model calibration robustness 2026"

Links: [{"title":"Robust Reward Modeling via Causal Rubrics | OpenReview","url":"https://openreview.net/forum?id=oP99JQiDYp"},{"title":"Robust Reward Modeling for Large Language Models via Causal Decomposition","url":"https://arxiv.org/html/2604.13833"},{"title":"Robust Reward Modeling via Causal Rubrics","url":"https://www.researchgate.net/publication/392918827_Robust_Reward_Modeling_via_Causal_Rubrics"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"arXiv:2506.16507v1 [cs.LG] 19 Jun 2025 2025-6-23","url":"https://arxiv.org/pdf/2506.16507"},{"title":"RRM: Robust Reward Model Training Mitigates Reward Hacking | OpenReview","url":"https://openreview.net/forum?id=88AS5MQnmC"},{"title":"Causal Rewards for Large Language Model Alignment","url":"https://arxiv.org/pdf/2501.09620"},{"title":"Avoiding Reward Hacking","url":"https://www.emergentmind.com/topics/avoiding-reward-hacking"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"}]

Based on the search results, here's what I found about the connection between calibration, reward hacking, and causal links in reward model calibration robustness:

## Key Findings

Prior work has sought to address reward hacking by reinforcing the causal link between prompt intent and reward model predictions, but has lacked a principled framework to quantify the extent to which a response aligns with the prompt.

Several 2026 research efforts explore this connection directly:

**CROME Framework:** CROME (Causally Robust Reward Modeling) is a novel framework designed to mitigate reward hacking, as reward models often suffer from reward hacking by latching on to superficial attributes like response length or formatting, mistaking these for true causal drivers of quality.

**CARP Framework:** CARP introduces the Semantic Alignment Score (SAS) to measure how well a response reflects latent prompt intentions.

**General Connection:** The quality, calibration, and robustness of the reward model are paramount, as flaws in the reward model directly impact the alignment outcome. Additionally, reward models fail to effectively distinguish between contextual signals and irrelevant artifacts, and addressing this requires introducing a causal framework that learns preferences independent of these artifacts.

The 2026 research landscape shows clear recognition that establishing proper causal links in reward models is essential for both preventing reward hacking and maintaining calibration robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3794c23-2aeb-41b7-a3c3-6b56ed921257",
  "isSidechain": false,
  "promptId": "889f415c-d586-430e-ba7e-2def0b61d52e",
  "type": "user",
  "uuid": "91c22b23-967c-4a74-9f91-fadc805fb063",
  "toolUseResult": {
    "query": "calibration reward hacking connection causal link reward model calibration robustness 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Pd3ctPgVfhNoUdxUvo5Yhp",
        "content": [
          {
            "title": "Robust Reward Modeling via Causal Rubrics | OpenReview",
            "url": "https://openreview.net/forum?id=oP99JQiDYp"
          },
          {
            "title": "Robust Reward Modeling for Large Language Models via Causal Decomposition",
            "url": "https://arxiv.org/html/2604.13833"
          },
          {
            "title": "Robust Reward Modeling via Causal Rubrics",
            "url": "https://www.researchgate.net/publication/392918827_Robust_Reward_Modeling_via_Causal_Rubrics"
          },
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://arxiv.org/pdf/2601.21350"
          },
          {
            "title": "arXiv:2506.16507v1 [cs.LG] 19 Jun 2025 2025-6-23",
            "url": "https://arxiv.org/pdf/2506.16507"
          },
          {
            "title": "RRM: Robust Reward Model Training Mitigates Reward Hacking | OpenReview",
            "url": "https://openreview.net/forum?id=88AS5MQnmC"
          },
          {
            "title": "Causal Rewards for Large Language Model Alignment",
            "url": "https://arxiv.org/pdf/2501.09620"
          },
          {
            "title": "Avoiding Reward Hacking",
            "url": "https://www.emergentmind.com/topics/avoiding-reward-hacking"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/pdf/2604.02986"
          }
        ]
      },
      "Based on the search results, here's what I found about the connection between calibration, reward hacking, and causal links in reward model calibration robustness:\n\n## Key Findings\n\nPrior work has sought to address reward hacking by reinforcing the causal link between prompt intent and reward model predictions, but has lacked a principled framework to quantify the extent to which a response aligns with the prompt.\n\nSeveral 2026 research efforts explore this connection directly:\n\n**CROME Framework:** CROME (Causally Robust Reward Modeling) is a novel framework designed to mitigate reward hacking, as reward models often suffer from reward hacking by latching on to superficial attributes like response length or formatting, mistaking these for true causal drivers of quality.\n\n**CARP Framework:** CARP introduces the Semantic Alignment Score (SAS) to measure how well a response reflects latent prompt intentions.\n\n**General Connection:** The quality, calibration, and robustness of the reward model are paramount, as flaws in the reward model directly impact the alignment outcome. Additionally, reward models fail to effectively distinguish between contextual signals and irrelevant artifacts, and addressing this requires introducing a causal framework that learns preferences independent of these artifacts.\n\nThe 2026 research landscape shows clear recognition that establishing proper causal links in reward models is essential for both preventing reward hacking and maintaining calibration robustness."
    ],
    "durationSeconds": 7.399234801000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a3794c23-2aeb-41b7-a3c3-6b56ed921257",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T05:41:52.049Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rg8aE9XmbLCufqAhjMDYak`</summary>

```json
{
  "query": "gradient regularization reward hacking Ackermann 2026 arxiv 2602.18037 reward surface flatness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91c22b23-967c-4a74-9f91-fadc805fb063",
  "isSidechain": false,
  "requestId": "req_011CbDHZEHzrxEFbmjtrCCpA",
  "type": "assistant",
  "uuid": "e2def5e3-4b1e-44ba-9d09-9382c58f96f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CVDatQVmKUVfSokaCMx6di",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 22464,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 22464,
          "cache_creation_input_tokens": 835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 835
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

_source line 20 · 2026-05-20T05:41:58.542Z_

<details><summary>↩ Tool result · `toolu_01Rg8aE9XmbLCufqAhjMDYak`</summary>

```text
Web search results for query: "gradient regularization reward hacking Ackermann 2026 arxiv 2602.18037 reward surface flatness"

Links: [{"title":"[2602.18037] Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards","url":"https://arxiv.org/abs/2602.18037"},{"title":"Detecting and Suppressing Reward Hacking with Gradient Fingerprints","url":"https://arxiv.org/html/2604.16242v1"},{"title":"Gradient Regularization Prevents Reward Hacking in ...","url":"https://arxiv.org/pdf/2602.18037"},{"title":"Correlated Proxies: A New Definition and Improved Mitigation for Reward   Hacking","url":"https://arxiv.org/pdf/2403.03185"},{"title":"Projected Gradient Ascent for Efficient Reward-Guided Updates with One-Step Generative Models","url":"https://arxiv.org/html/2602.08646v1"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"}]

I found the paper you're searching for. Here are the key findings from arxiv 2602.18037:

**Title and Authors:**
The paper addresses Reinforcement Learning from Human Feedback (RLHF) or Verifiable Rewards (RLVR) as key steps in post-training of modern Language Models, authored by J. Ackermann and colleagues.

**Main Problem:**
The paper addresses reward hacking, where the policy may exploit inaccuracies of the reward and learn an unintended behavior.

**Key Contribution:**
The authors derive a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence. Gradient regularization (GR) can then be used to bias training to flatter regions and thereby maintain reward model accuracy.

**Empirical Validation:**
The authors confirm their results by showing that the gradient norm and reward accuracy are empirically correlated in RLHF.

**Results:**
GR performs better than a KL penalty across a diverse set of RL experiments with LMs, and the approach uses an efficient finite-difference estimate for explicit gradient regularization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2def5e3-4b1e-44ba-9d09-9382c58f96f3",
  "isSidechain": false,
  "promptId": "889f415c-d586-430e-ba7e-2def0b61d52e",
  "type": "user",
  "uuid": "3e9b94cd-eb2b-4aba-9eb4-9b65dbb0135e",
  "toolUseResult": {
    "query": "gradient regularization reward hacking Ackermann 2026 arxiv 2602.18037 reward surface flatness",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KAEzSDP9CuSfVfHYSXKjWZ",
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
            "title": "Correlated Proxies: A New Definition and Improved Mitigation for Reward   Hacking",
            "url": "https://arxiv.org/pdf/2403.03185"
          },
          {
            "title": "Projected Gradient Ascent for Efficient Reward-Guided Updates with One-Step Generative Models",
            "url": "https://arxiv.org/html/2602.08646v1"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/pdf/2604.02986"
          }
        ]
      },
      "I found the paper you're searching for. Here are the key findings from arxiv 2602.18037:\n\n**Title and Authors:**\nThe paper addresses Reinforcement Learning from Human Feedback (RLHF) or Verifiable Rewards (RLVR) as key steps in post-training of modern Language Models, authored by J. Ackermann and colleagues.\n\n**Main Problem:**\nThe paper addresses reward hacking, where the policy may exploit inaccuracies of the reward and learn an unintended behavior.\n\n**Key Contribution:**\nThe authors derive a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence. Gradient regularization (GR) can then be used to bias training to flatter regions and thereby maintain reward model accuracy.\n\n**Empirical Validation:**\nThe authors confirm their results by showing that the gradient norm and reward accuracy are empirically correlated in RLHF.\n\n**Results:**\nGR performs better than a KL penalty across a diverse set of RL experiments with LMs, and the approach uses an efficient finite-difference estimate for explicit gradient regularization."
    ],
    "durationSeconds": 6.488959875000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e2def5e3-4b1e-44ba-9d09-9382c58f96f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
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
  "leafUuid": "3e9b94cd-eb2b-4aba-9eb4-9b65dbb0135e",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration's causal role in reward hacking resistance",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af"
}
```

---

### Tool call

_source line 23 · 2026-05-20T05:42:01.947Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JSW7xLKRMqDZfphDvug2Wy`</summary>

```json
{
  "query": "\"step-level pessimism\" OR \"calibration-gated\" reward model defense RL training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e9b94cd-eb2b-4aba-9eb4-9b65dbb0135e",
  "isSidechain": false,
  "requestId": "req_011CbDHZweet6CX8LHb1W4yC",
  "type": "assistant",
  "uuid": "207ba7de-208d-42af-b3e8-b0014f3a2106",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQZ54N35HJ36KSHyk5dp4n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 23299,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 23299,
          "cache_creation_input_tokens": 672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 672
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

_source line 24 · 2026-05-20T05:42:09.333Z_

<details><summary>↩ Tool result · `toolu_01JSW7xLKRMqDZfphDvug2Wy`</summary>

```text
Web search results for query: ""step-level pessimism" OR "calibration-gated" reward model defense RL training 2025 2026"

Links: [{"title":"arXiv:2505.19196v1 [cs.CV] 25 May 2025 Step-level Reward for Free in RL-based","url":"https://arxiv.org/pdf/2505.19196"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/pdf/2604.04648"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"Taming Overconfidence in LLMs: Reward Calibration in RLHF","url":"https://arxiv.org/pdf/2410.09724"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.18533"}]

Based on the search results, I found several relevant papers related to your query:

1. **"Learning a Pessimistic Reward Model in RLHF"** (arXiv:2505.20556): This work demonstrates the feasibility of learning a pessimistic reward model against reward hacking, where agents can greedily search for policies with high pessimistic rewards without suffering from reward hacking.

2. **"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism"** (arXiv:2604.04648): This paper applies pessimism at the reward level by penalizing out-of-distribution responses through subtracting per-response uncertainty estimates from reward scores.

3. **Step-level Pessimism in RL-based Training**: Recent research identifies early-step bias in step-level reward labeling, where step-level value estimates can be overly pessimistic, leading to premature discarding of potentially correct reasoning paths during search.

4. **Reward Calibration**: Studies on reward calibration in RLHF show methods like PPO-M and PPO-C that reduce Expected Calibration Error while maintaining comparable accuracy.

5. **Post-Training Techniques (2025-2026)**: The field has shifted toward verifiable rewards for reasoning tasks, with DeepSeek-R1 demonstrating that pure RL with verifiable rewards can produce emergent reasoning capabilities without human-labeled reasoning traces.

These recent papers address defense mechanisms against reward hacking and optimization issues in RL-based training for language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "207ba7de-208d-42af-b3e8-b0014f3a2106",
  "isSidechain": false,
  "promptId": "889f415c-d586-430e-ba7e-2def0b61d52e",
  "type": "user",
  "uuid": "dd868dd1-cbc6-426a-9c7a-accd2e75d4d6",
  "toolUseResult": {
    "query": "\"step-level pessimism\" OR \"calibration-gated\" reward model defense RL training 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012uHjWaD8bfSE3eThSa22yD",
        "content": [
          {
            "title": "arXiv:2505.19196v1 [cs.CV] 25 May 2025 Step-level Reward for Free in RL-based",
            "url": "https://arxiv.org/pdf/2505.19196"
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
            "title": "Post-Training in 2026: GRPO, DAPO, RLVR & Beyond",
            "url": "https://llm-stats.com/blog/research/post-training-techniques-2026"
          },
          {
            "title": "Taming Overconfidence in LLMs: Reward Calibration in RLHF",
            "url": "https://arxiv.org/pdf/2410.09724"
          },
          {
            "title": "Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation",
            "url": "https://arxiv.org/html/2602.09305v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2601.18533"
          }
        ]
      },
      "Based on the search results, I found several relevant papers related to your query:\n\n1. **\"Learning a Pessimistic Reward Model in RLHF\"** (arXiv:2505.20556): This work demonstrates the feasibility of learning a pessimistic reward model against reward hacking, where agents can greedily search for policies with high pessimistic rewards without suffering from reward hacking.\n\n2. **\"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism\"** (arXiv:2604.04648): This paper applies pessimism at the reward level by penalizing out-of-distribution responses through subtracting per-response uncertainty estimates from reward scores.\n\n3. **Step-level Pessimism in RL-based Training**: Recent research identifies early-step bias in step-level reward labeling, where step-level value estimates can be overly pessimistic, leading to premature discarding of potentially correct reasoning paths during search.\n\n4. **Reward Calibration**: Studies on reward calibration in RLHF show methods like PPO-M and PPO-C that reduce Expected Calibration Error while maintaining comparable accuracy.\n\n5. **Post-Training Techniques (2025-2026)**: The field has shifted toward verifiable rewards for reasoning tasks, with DeepSeek-R1 demonstrating that pure RL with verifiable rewards can produce emergent reasoning capabilities without human-labeled reasoning traces.\n\nThese recent papers address defense mechanisms against reward hacking and optimization issues in RL-based training for language models."
    ],
    "durationSeconds": 7.381900409999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "207ba7de-208d-42af-b3e8-b0014f3a2106",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T05:42:12.141Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V1XqZctBe2pVvCap7S5JK1`</summary>

```json
{
  "query": "distributional process reward model arxiv 2605.06785 conditional optimal transport calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd868dd1-cbc6-426a-9c7a-accd2e75d4d6",
  "isSidechain": false,
  "requestId": "req_011CbDHakh8FHaFoAiL1vPex",
  "type": "assistant",
  "uuid": "08ac25a4-236a-46c7-a808-4283f7501225",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TkqYQWr7ekcPbn3Z3YsAvi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 23971,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 835,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 23971,
          "cache_creation_input_tokens": 835,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 835
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

_source line 26 · 2026-05-20T05:42:19.472Z_

<details><summary>↩ Tool result · `toolu_01V1XqZctBe2pVvCap7S5JK1`</summary>

```text
Web search results for query: "distributional process reward model arxiv 2605.06785 conditional optimal transport calibration"

Links: [{"title":"[2605.06785] Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/abs/2605.06785"},{"title":"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/html/2605.06785"},{"title":"Quantile Regression for Distributional Reward Models in RLHF","url":"https://arxiv.org/pdf/2409.10164"},{"title":"Entropy-Regularized Process Reward Model","url":"https://arxiv.org/pdf/2412.11006"},{"title":"GRPO is Secretly a Process Reward Model","url":"https://arxiv.org/pdf/2509.21154"}]

Based on the search results, I found the paper you're looking for:

The paper "Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport" (arxiv 2605.06785) addresses the problem that inference-time scaling methods rely on Process Reward Models (PRMs), which are often poorly calibrated and overestimate success probabilities.

The authors propose the first use of conditional optimal transport for calibrating PRMs, modifying conditional OT (CondOT) map learning to estimate a monotonic conditional quantile function over success probabilities estimated by the PRM, conditioned on PRM hidden states.

This approach yields structurally valid quantile estimates and enables efficient extraction of confidence bounds at arbitrary levels, which are integrated into the instance-adaptive scaling (IAS) framework.

The evaluation is conducted on mathematical reasoning benchmarks spanning moderate-difficulty problems (MATH-500) and harder out-of-distribution problems (AIME), and for PRMs with reliable ranking signals, the method substantially improves calibration over both uncalibrated PRMs and quantile regression.

The paper was submitted on May 7, 2026, with authors Rachel Ma, Dylan Hadfield-Menell, and Kristjan Greenewald.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08ac25a4-236a-46c7-a808-4283f7501225",
  "isSidechain": false,
  "promptId": "889f415c-d586-430e-ba7e-2def0b61d52e",
  "type": "user",
  "uuid": "94e9b0cd-19be-422b-9f47-f3dd7630d56b",
  "toolUseResult": {
    "query": "distributional process reward model arxiv 2605.06785 conditional optimal transport calibration",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Mcnyu1qqvJ6J2KR8QKddBz",
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
            "title": "Quantile Regression for Distributional Reward Models in RLHF",
            "url": "https://arxiv.org/pdf/2409.10164"
          },
          {
            "title": "Entropy-Regularized Process Reward Model",
            "url": "https://arxiv.org/pdf/2412.11006"
          },
          {
            "title": "GRPO is Secretly a Process Reward Model",
            "url": "https://arxiv.org/pdf/2509.21154"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper \"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport\" (arxiv 2605.06785) addresses the problem that inference-time scaling methods rely on Process Reward Models (PRMs), which are often poorly calibrated and overestimate success probabilities.\n\nThe authors propose the first use of conditional optimal transport for calibrating PRMs, modifying conditional OT (CondOT) map learning to estimate a monotonic conditional quantile function over success probabilities estimated by the PRM, conditioned on PRM hidden states.\n\nThis approach yields structurally valid quantile estimates and enables efficient extraction of confidence bounds at arbitrary levels, which are integrated into the instance-adaptive scaling (IAS) framework.\n\nThe evaluation is conducted on mathematical reasoning benchmarks spanning moderate-difficulty problems (MATH-500) and harder out-of-distribution problems (AIME), and for PRMs with reliable ranking signals, the method substantially improves calibration over both uncalibrated PRMs and quantile regression.\n\nThe paper was submitted on May 7, 2026, with authors Rachel Ma, Dylan Hadfield-Menell, and Kristjan Greenewald."
    ],
    "durationSeconds": 7.327451180000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "08ac25a4-236a-46c7-a808-4283f7501225",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T05:42:21.849Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0187e9EMUFSDL8djmYxY9gwx`</summary>

```json
{
  "query": "pessimistic reward model ensemble uncertainty reward hacking defense RLHF 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94e9b0cd-19be-422b-9f47-f3dd7630d56b",
  "isSidechain": false,
  "requestId": "req_011CbDHbV6nPSQJPnCuF1Xy6",
  "type": "assistant",
  "uuid": "c840acf8-3817-4eea-8b19-647273075b64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQiGrwXoKKx5LhX4gHK6w4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 613,
      "cache_read_input_tokens": 24806,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 613,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 24806,
          "cache_creation_input_tokens": 613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 613
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

_source line 28 · 2026-05-20T05:42:29.169Z_

<details><summary>↩ Tool result · `toolu_0187e9EMUFSDL8djmYxY9gwx`</summary>

```text
Web search results for query: "pessimistic reward model ensemble uncertainty reward hacking defense RLHF 2025 2026"

Links: [{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/html/2604.02986"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/pdf/2602.10623"},{"title":"Reward Hacking Defense Rubric","url":"https://www.emergentmind.com/topics/reward-hacking-defense-rubric"},{"title":"Pessimistic Reward Tuning (PET) in RLHF","url":"https://www.emergentmind.com/topics/pessimistic-reward-tuning-pet"},{"title":"Pessimistic Reward Modeling in RLHF against Reward Hacking","url":"https://openreview.net/pdf?id=HWOAZUPA0C"},{"title":"[2505.20556] Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/abs/2505.20556"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"}]

Based on the search results, here's what I found on pessimistic reward model ensemble uncertainty and reward hacking defense in RLHF for 2025-2026:

## Key Research Areas

**Pessimistic Reward Tuning (PET):**
Pessimistic Reward Tuning (PET) is a suite of algorithmic and theoretical techniques for robustifying reinforcement learning from human feedback (RLHF) against overoptimization, reward hacking, and distributional shift. When optimizing a policy on a pessimistic reward model fine-tuned through PET, reward hacking can be prevented without relying on any regularization.

**Ensemble-Based Methods:**
Ensemble-based methods mitigate reward hacking by optimizing a policy conservatively with respect to multiple RMs, with multiple RMs trained and conservative objectives such as worst-case and uncertainty-weighted optimization (UWO) studied. However, ensembles still exploit spurious features when all members agree on them.

**Uncertainty Quantification Approaches:**
The Probabilistic Uncertain Reward Model (PURM) generalizes scalar reward outputs to Gaussian distributions, quantifies Bhattacharyya coefficient overlaps for reward uncertainty, and penalizes learning in regions of high uncertainty to prevent overoptimization.

**Bayesian Approaches:**
Bayesian Non-negative Reward Modeling (BNRM) substantially mitigates reward over-optimization, improves robustness under distribution shifts, and yields more interpretable reward decompositions.

**Adversarial Training:**
RL-driven adversarial example generation is used to surface OOD, low-quality but high-scoring samples that are then added to the RM training set, which demonstrably increases downstream RLHF robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c840acf8-3817-4eea-8b19-647273075b64",
  "isSidechain": false,
  "promptId": "889f415c-d586-430e-ba7e-2def0b61d52e",
  "type": "user",
  "uuid": "db670594-b727-4f4f-ab45-789d02b60bcf",
  "toolUseResult": {
    "query": "pessimistic reward model ensemble uncertainty reward hacking defense RLHF 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014Uj69PXiyxVhx3GLPkRWvB",
        "content": [
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/html/2604.02986"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/pdf/2602.10623"
          },
          {
            "title": "Reward Hacking Defense Rubric",
            "url": "https://www.emergentmind.com/topics/reward-hacking-defense-rubric"
          },
          {
            "title": "Pessimistic Reward Tuning (PET) in RLHF",
            "url": "https://www.emergentmind.com/topics/pessimistic-reward-tuning-pet"
          },
          {
            "title": "Pessimistic Reward Modeling in RLHF against Reward Hacking",
            "url": "https://openreview.net/pdf?id=HWOAZUPA0C"
          },
          {
            "title": "[2505.20556] Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/abs/2505.20556"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/pdf/2505.20556"
          }
        ]
      },
      "Based on the search results, here's what I found on pessimistic reward model ensemble uncertainty and reward hacking defense in RLHF for 2025-2026:\n\n## Key Research Areas\n\n**Pessimistic Reward Tuning (PET):**\nPessimistic Reward Tuning (PET) is a suite of algorithmic and theoretical techniques for robustifying reinforcement learning from human feedback (RLHF) against overoptimization, reward hacking, and distributional shift. When optimizing a policy on a pessimistic reward model fine-tuned through PET, reward hacking can be prevented without relying on any regularization.\n\n**Ensemble-Based Methods:**\nEnsemble-based methods mitigate reward hacking by optimizing a policy conservatively with respect to multiple RMs, with multiple RMs trained and conservative objectives such as worst-case and uncertainty-weighted optimization (UWO) studied. However, ensembles still exploit spurious features when all members agree on them.\n\n**Uncertainty Quantification Approaches:**\nThe Probabilistic Uncertain Reward Model (PURM) generalizes scalar reward outputs to Gaussian distributions, quantifies Bhattacharyya coefficient overlaps for reward uncertainty, and penalizes learning in regions of high uncertainty to prevent overoptimization.\n\n**Bayesian Approaches:**\nBayesian Non-negative Reward Modeling (BNRM) substantially mitigates reward over-optimization, improves robustness under distribution shifts, and yields more interpretable reward decompositions.\n\n**Adversarial Training:**\nRL-driven adversarial example generation is used to surface OOD, low-quality but high-scoring samples that are then added to the RM training set, which demonstrably increases downstream RLHF robustness."
    ],
    "durationSeconds": 7.315263602999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c840acf8-3817-4eea-8b19-647273075b64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T05:42:29.173Z_

```json
{
  "parentUuid": "db670594-b727-4f4f-ab45-789d02b60bcf",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1ff4893f-0983-46a1-94fd-7a3f1624f859",
  "timestamp": "2026-05-20T05:42:29.173Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-20T05:42:31.639Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013pKB8vyoDb6XnER87vqt21`</summary>

```json
{
  "query": "adversarial process reward model APRM arxiv 2511.22888 robustness training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ff4893f-0983-46a1-94fd-7a3f1624f859",
  "isSidechain": false,
  "requestId": "req_011CbDHcCbt3StFzfX9wWeVh",
  "type": "assistant",
  "uuid": "bf2ee1a5-4c80-4528-8f0a-5c3f899355eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DXUQkYfsEQXRiZ9gdmjDJr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 25419,
      "output_tokens": 73,
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
          "output_tokens": 73,
          "cache_read_input_tokens": 25419,
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

_source line 31 · 2026-05-20T05:42:38.891Z_

<details><summary>↩ Tool result · `toolu_013pKB8vyoDb6XnER87vqt21`</summary>

```text
Web search results for query: "adversarial process reward model APRM arxiv 2511.22888 robustness training"

Links: [{"title":"[2511.22888] Adversarial Training for Process Reward Models","url":"https://arxiv.org/abs/2511.22888"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/html/2511.22888"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/pdf/2511.22888"},{"title":"Adversarially Trained Reward Models","url":"https://www.emergentmind.com/topics/adversarially-trained-reward-models"},{"title":"Adversarial Training of Reward Models","url":"https://arxiv.org/pdf/2504.06141"},{"title":"[2504.06141] Adversarial Training of Reward Models","url":"https://arxiv.org/abs/2504.06141"},{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"}]

Based on the search results, here's what I found about the APRM (Adversarial Process Reward Model) paper:

## Overview

Process Reward Models (PRMs) enhance reasoning ability of LLMs by providing step-level supervision. However, their widespread adoption is limited due to expensive manual step-level annotation and poor generalization of static training data to novel errors.

## APRM Approach

Adversarially Trained PRMs (APRM) use a Generator that learns to produce reasoning errors to deceive a PRM, while the PRM concurrently learns to detect them. This interaction yields progressively harder negatives for the PRM, improving its robustness and generalization to novel errors without requiring manual step-level labels.

## Training Framework

The PRM training is formulated as a two-player, general-sum, non-cooperative game. This competitive interaction creates an adaptive curriculum, directly addressing the limitations of static or passively generated training data.

## Results

Averaged across diverse mathematical reasoning benchmarks, APRM improves solver accuracy by +3.4 percentage points over the strongest PRM baseline, and achieves gains of +5.3 pp on out-of-distribution tasks.

The paper was submitted on November 28, 2025, by Gurusha Juneja, Deepak Nathani, and William Yang Wang from UC Santa Barbara.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf2ee1a5-4c80-4528-8f0a-5c3f899355eb",
  "isSidechain": false,
  "promptId": "889f415c-d586-430e-ba7e-2def0b61d52e",
  "type": "user",
  "uuid": "434f477d-ddc1-43df-8bcd-59a9a4eba037",
  "toolUseResult": {
    "query": "adversarial process reward model APRM arxiv 2511.22888 robustness training",
    "results": [
      {
        "tool_use_id": "srvtoolu_0132HhKYqXJdwwmUdk5uBNWq",
        "content": [
          {
            "title": "[2511.22888] Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/abs/2511.22888"
          },
          {
            "title": "Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/html/2511.22888"
          },
          {
            "title": "Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/pdf/2511.22888"
          },
          {
            "title": "Adversarially Trained Reward Models",
            "url": "https://www.emergentmind.com/topics/adversarially-trained-reward-models"
          },
          {
            "title": "Adversarial Training of Reward Models",
            "url": "https://arxiv.org/pdf/2504.06141"
          },
          {
            "title": "[2504.06141] Adversarial Training of Reward Models",
            "url": "https://arxiv.org/abs/2504.06141"
          },
          {
            "title": "[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/abs/2603.06621"
          }
        ]
      },
      "Based on the search results, here's what I found about the APRM (Adversarial Process Reward Model) paper:\n\n## Overview\n\nProcess Reward Models (PRMs) enhance reasoning ability of LLMs by providing step-level supervision. However, their widespread adoption is limited due to expensive manual step-level annotation and poor generalization of static training data to novel errors.\n\n## APRM Approach\n\nAdversarially Trained PRMs (APRM) use a Generator that learns to produce reasoning errors to deceive a PRM, while the PRM concurrently learns to detect them. This interaction yields progressively harder negatives for the PRM, improving its robustness and generalization to novel errors without requiring manual step-level labels.\n\n## Training Framework\n\nThe PRM training is formulated as a two-player, general-sum, non-cooperative game. This competitive interaction creates an adaptive curriculum, directly addressing the limitations of static or passively generated training data.\n\n## Results\n\nAveraged across diverse mathematical reasoning benchmarks, APRM improves solver accuracy by +3.4 percentage points over the strongest PRM baseline, and achieves gains of +5.3 pp on out-of-distribution tasks.\n\nThe paper was submitted on November 28, 2025, by Gurusha Juneja, Deepak Nathani, and William Yang Wang from UC Santa Barbara."
    ],
    "durationSeconds": 7.248664617000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bf2ee1a5-4c80-4528-8f0a-5c3f899355eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T05:42:41.517Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JtNNCmiE9arb4t8pCZ9xVB`</summary>

```json
{
  "query": "\"calibration\" AND \"reward hacking\" OR \"overoptimization\" process reward model causal 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "434f477d-ddc1-43df-8bcd-59a9a4eba037",
  "isSidechain": false,
  "requestId": "req_011CbDHcv9hWCfM7RE3m63Nw",
  "type": "assistant",
  "uuid": "5e94d5af-682e-472e-b3ce-56e46d0f0686",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019FohLc4T36ybZeDNb5756k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 26368,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 26368,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
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

_source line 33 · 2026-05-20T05:42:54.571Z_

<details><summary>↩ Tool result · `toolu_01JtNNCmiE9arb4t8pCZ9xVB`</summary>

```text
Web search results for query: ""calibration" AND "reward hacking" OR "overoptimization" process reward model causal 2026"

Links: [{"title":"Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment","url":"https://arxiv.org/html/2501.09620v1"},{"title":"Reward Model Overoptimization: Root Causes and Mitigations","url":"https://www.reinforced.info/p/reward-model-overoptimization"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms | OpenReview","url":"https://openreview.net/forum?id=pf4OuJyn4Q"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/pdf/2602.10623"},{"title":"Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate   Reward Hacking","url":"https://arxiv.org/pdf/2312.09244"}]

Based on the search results, I found several relevant papers and resources about calibration, reward hacking, and overoptimization in process reward models with causal approaches:

## Key Findings:

**Causal Approaches to Reward Hacking:**
A novel causal reward modeling approach integrates causal inference to mitigate spurious correlations, with counterfactual invariance ensuring reward predictions remain consistent when irrelevant variables are altered.

**Reward Overoptimization and Hacking:**
A combination of reward hacking and distribution shift inevitably leads to overoptimization. Reward over-optimization occurs where the performance as measured by the learned proxy reward model increases, but the true model quality plateaus or even deteriorates.

**Calibration Methods:**
To mitigate positional bias, multiple evidence calibration asks evaluator models to provide evaluation evidence and output scores, while balanced position calibration aggregates results across various response orders to get the final score.

**Recent Causal Work (2026):**
Research traces underlying causal mechanisms distinguishing feature-level exploitation from representation-level exploitation, concluding with a bridge to how these localized shortcuts set the stage for emergent strategic misalignment. Additionally, factored causal representation learning demonstrates improved downstream RLHF performance and validates effectiveness in mitigating reward hacking behaviors like length and sycophantic bias.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e94d5af-682e-472e-b3ce-56e46d0f0686",
  "isSidechain": false,
  "promptId": "889f415c-d586-430e-ba7e-2def0b61d52e",
  "type": "user",
  "uuid": "3b8a7de2-7b8b-46d9-9bcf-fb0f46c0fd98",
  "toolUseResult": {
    "query": "\"calibration\" AND \"reward hacking\" OR \"overoptimization\" process reward model causal 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VU4YYU784ChtanTvYt1P5R",
        "content": [
          {
            "title": "Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment",
            "url": "https://arxiv.org/html/2501.09620v1"
          },
          {
            "title": "Reward Model Overoptimization: Root Causes and Mitigations",
            "url": "https://www.reinforced.info/p/reward-model-overoptimization"
          },
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          },
          {
            "title": "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/html/2604.13602v1"
          },
          {
            "title": "Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms | OpenReview",
            "url": "https://openreview.net/forum?id=pf4OuJyn4Q"
          },
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://arxiv.org/pdf/2601.21350"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/pdf/2602.10623"
          },
          {
            "title": "Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate   Reward Hacking",
            "url": "https://arxiv.org/pdf/2312.09244"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and resources about calibration, reward hacking, and overoptimization in process reward models with causal approaches:\n\n## Key Findings:\n\n**Causal Approaches to Reward Hacking:**\nA novel causal reward modeling approach integrates causal inference to mitigate spurious correlations, with counterfactual invariance ensuring reward predictions remain consistent when irrelevant variables are altered.\n\n**Reward Overoptimization and Hacking:**\nA combination of reward hacking and distribution shift inevitably leads to overoptimization. Reward over-optimization occurs where the performance as measured by the learned proxy reward model increases, but the true model quality plateaus or even deteriorates.\n\n**Calibration Methods:**\nTo mitigate positional bias, multiple evidence calibration asks evaluator models to provide evaluation evidence and output scores, while balanced position calibration aggregates results across various response orders to get the final score.\n\n**Recent Causal Work (2026):**\nResearch traces underlying causal mechanisms distinguishing feature-level exploitation from representation-level exploitation, concluding with a bridge to how these localized shortcuts set the stage for emergent strategic misalignment. Additionally, factored causal representation learning demonstrates improved downstream RLHF performance and validates effectiveness in mitigating reward hacking behaviors like length and sycophantic bias."
    ],
    "durationSeconds": 13.049593197000009,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5e94d5af-682e-472e-b3ce-56e46d0f0686",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "3b8a7de2-7b8b-46d9-9bcf-fb0f46c0fd98",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration's causal role in reward hacking resistance",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af"
}
```

---

### Assistant

_source line 36 · 2026-05-20T05:44:16.250Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to do a thorough evaluation. Let me synthesize my findings and evaluate this proposal.

Let me analyze the proposal carefully:

## Key Claims of the Proposal:

1. **Bridging two isolated threads**: PRM calibration and PRM hackability research have zero cross-citation
2. **Causal link**: Calibration quality causally determines hackability
3. **CGSP defense**: A novel step-level defense using calibrated uncertainty
4. **Hessian spectral analysis**: Extending beyond gradient norm analysis to step-level geometry

## Detailed Analysis:


The claim about two disconnected research threads appears valid—the calibration work doesn't address adversarial robustness, while the hackability research doesn't explore calibration-based defenses, and the distributional work provides uncertainty estimates without testing against attacks. Nobody has formally connected these areas yet.

The intuition that well-calibrated confidence should resist hacking seems reasonable—if a model's confidence genuinely reflects correctness probability, adversarial outputs producing wrong answers should get lower scores, making manipulation harder. But the proposal actually sidesteps the trivial alternative threat by testing temperature scaling directly in their experiments, which either validates the core hypothesis or reveals that simple post-hoc calibration isn't sufficient.

The real subtlety is that temperature scaling only rescales logits without changing response rankings, so gradient-based attacks would still find the same high-reward peaks—the attack surface doesn't actually shrink. This suggests that calibration alone might not be the mechanism driving robustness, or that something deeper than post-hoc rescaling is needed. still assign the same relative ordering to adversarial vs. genuine responses.

Wait, this is actually a serious problem for the proposal's core hypothesis. If post-hoc calibration preserves rankings (which it does by design for monotonic transformations like temperature scaling, Platt scaling), then the same adversarial inputs that fool the original model would still get the highest scores from the calibrated model. The absolute scores would change, but the gradient landscape for attacks wouldn't fundamentally change.

Hmm, but the proposal addresses this by looking at BoN overoptimization where the absolute value matters (not just ranking), and the CGSP formula uses σ_t (uncertainty) which could change behavior.

Let me think about this more carefully: temperature scaling, isotonic regression, and Platt scaling are all monotonic transformations that preserve rankings, so they shouldn't actually make a PRM more robust to gradient attacks since the attack direction remains unchanged. For BoN overoptimization, calibration does affect the absolute threshold for stopping, but that's really just better decision-making about when to stop scaling N rather than genuine robustness of the PRM itself.

This cuts to the heart of the issue—the proposal's cleanest experiments might actually produce negative results for gradient attacks and undermine the core hypothesis, unless "hackability" is defined to include something like reward-accuracy divergence.

Actually, I'm reconsidering: the CGSP defense mechanism is more sophisticated than just using calibrated scores. It uses calibrated uncertainty (σ_t) to apply pessimism where the model is uncertain and trust where it's confident and well-calibrated. The formula r̃_t = μ_t − α·σ_t/√c_t is essentially a Lower Confidence Bound approach, which is well-established in bandit algorithms.

But when I look at related work, this is fundamentally just pessimistic RL with uncertainty estimation applied to PRMs. Papers like Caution, PET, and PURM already explore pessimism with prediction error or Bayesian uncertainty. The claimed novelties—step-level application, calibration-grounded uncertainty, and adaptive drift detection—don't seem as novel as they appear. Step-level defenses are standard for PRM-based approaches, using calibrated versus raw uncertainty might not be meaningfully different, and drift detection through ECE monitoring on current rollouts is relatively straightforward.

The research question itself matters though. Understanding whether calibration determines PRM hackability would be genuinely useful, and the 48-configuration correlation study could map out the landscape regardless of the answer. If calibration does improve robustness, that's a cheap fix compared to adversarial training. If not, it's still a valuable negative result. The related work section is thorough and correctly positions the gap, though I should check if there are recent papers I'm missing.

I'm noticing a potential issue with the core argument: post-hoc calibration preserves the model's underlying representations and rankings, which is what gradient attacks actually target. So the causal isolation experiments might actually show that calibration doesn't reduce hackability for gradient-based attacks, which would contradict the paper's main narrative. And CGSP itself is really just a specific application of lower confidence bounds from the bandit literature—the novelty is more in the engineering than in the fundamental contribution.

The large-scale configuration study could be expensive without being particularly surprising if calibration is just a proxy for overall model quality, meaning the correlation with robustness might be explained by a confound rather than a causal mechanism. The Hessian spectral analysis is technically sound but computationally costly and might not translate into actionable insights about calibration.

Looking at the strengths and weaknesses: the research tackles an important gap between calibration and robustness with solid experimental design and good literature positioning, and the correlation study will generate useful data regardless of outcome. But the core hypothesis risks being undermined by the experiments themselves.

The real question is whether a positive result—that calibration predicts hackability—would actually surprise reviewers. Intuitively, better-calibrated models being harder to exploit seems expected. A negative result would be more interesting, suggesting calibration's focus on absolute scores doesn't capture the exploitable geometry of the reward landscape. The proposal has substance but lacks the surprising factor, landing somewhere in the 25-35% range. The comprehensive methodology and causal isolation approach add credibility, though the overall scope might work better as two separate papers.

Factoring in the polished presentation, genuine gap-bridging, and rigorous empirical methodology—which exceeds typical NLP standards—I'm settling around 28% for EMNLP. The core insight that calibration improves robustness is somewhat intuitive, but the execution and practical applicability push it slightly higher. I should also verify that temperature scaling truly preserves ranking order, since that's central to the post-hoc calibration argument.

Actually, isotonic regression can shift rankings since it's piecewise constant, and conformal prediction intervals vary by instance, so the CGSP formula using those interval widths could genuinely produce different orderings than raw scores. For BoN attacks, calibration affects how aggressively you can scale with additional samples—overconfident models might over-optimize while calibrated ones provide more reliable guidance. So the post-hoc calibration story is more nuanced than I initially thought, with results likely depending on the specific attack type. The core claim about calibration improving robustness remains somewhat expected, though the mechanistic understanding through Hessian analysis might offer the real novelty.

The obvious trivial alternatives are ensemble-min (already a baseline) and just applying temperature scaling before RL training. If CGSP doesn't substantially beat these simpler approaches, the elaborate calibration machinery doesn't add much. The proposal does include these baselines, but the critical question is whether CGSP actually outperforms them meaningfully. The underlying assumption that calibration quality measured by standard metrics like ECE or Brier score directly translates to robustness gains hasn't been validated yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b8a7de2-7b8b-46d9-9bcf-fb0f46c0fd98",
  "isSidechain": false,
  "requestId": "req_011CbDHe5DSFk8rijoc7zBG3",
  "type": "assistant",
  "uuid": "7e4ffc69-9d83-44ea-b211-01870c0eba64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqRT8m5gquDzT91yUB8A9T",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 27067,
      "output_tokens": 7835,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 818,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7835,
          "cache_read_input_tokens": 27067,
          "cache_creation_input_tokens": 818,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 818
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

_source line 37 · 2026-05-20T05:45:49.690Z_

Now I have sufficient research to evaluate this proposal. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. **Park et al. "Know What You Don't Know: Uncertainty Calibration of PRMs"** (arXiv:2506.09338, NeurIPS 2025):
   - 与本 proposal 的关系：Thread 1 核心论文。证明 PRM 系统性地对难题过度估计成功概率，提出 quantile regression calibration。关键缺陷——从未测试校准后的 PRM 在对抗攻击下的鲁棒性。
   - Proposal 准确引用了该工作，描述基本准确。

2. **Ma et al. "Distributional Process Reward Models"** (arXiv:2605.06785, May 2026):
   - 与本 proposal 的关系：最新的 PRM 校准工作，用 conditional optimal transport 实现 calibrated monotone quantile functions。在 MATH-500 和 AIME 上改进 BoN。同样从未测试鲁棒性。
   - Proposal 准确引用该工作。该论文发表于 2026 年 5 月，非常新。

3. **Tiwari et al. "Reward Under Attack"** (arXiv:2603.06621, March 2026):
   - 与本 proposal 的关系：Thread 2 核心论文。证明 PRM 灾难性可破解——gradient attacks 将奖励膨胀 4x，RL 训练可达到近完美 PRM 奖励但实际准确率 <4%，43% 的奖励增益来自风格快捷方式。未提出校准相关防御。
   - Proposal 准确引用并描述了该工作的核心发现。

4. **Ackermann et al. "Gradient Regularization Prevents Reward Hacking"** (arXiv:2602.18037, Feb 2026):
   - 与本 proposal 的关系：建立奖励模型准确性与 flatness 的理论联系，但仅针对 outcome-level RM。Proposal 正确指出该工作仅处理单标量奖励，不涉及 step-level PRM 几何。
   - Proposal 对 Ackermann 的局限性描述准确——确实仅使用 gradient norm，未做 Hessian spectral analysis。

5. **"From Curiosity to Caution"** (arXiv:2604.04648, April 2026):
   - BoN 层面的悲观主义防御，使用 prediction error 作为不确定性代理（未校准）。
   - Proposal 正确区分了自己与该工作的差异——CGSP 使用校准概率而非启发式代理。

6. **"Learning a Pessimistic Reward Model in RLHF"** (arXiv:2505.20556, May 2025):
   - 2025 年的悲观奖励模型方法。通过 pessimistic fine-tuning 防止 reward hacking。
   - Proposal 未引用此论文，但其 PET baseline 覆盖了类似方向。

7. **APRM "Adversarial Training for PRMs"** (arXiv:2511.22888, Nov 2025):
   - 对抗训练方法。Generator 学习产生推理错误欺骗 PRM，PRM 同时学习检测。平均 +3.4pp。
   - Proposal 将其列为 baseline，描述准确。

8. **"Robust Reward Modeling via Causal Rubrics"** (2026, OpenReview) 和 **"Robust Reward Modeling via Causal Decomposition"** (arXiv:2604.13833):
   - 因果推理用于奖励模型鲁棒性的新兴方向。与 proposal 的"因果隔离"实验有概念重叠，但未专注于 PRM 校准。
   - **Proposal 未引用这些工作**，是一个 related work 缺口。

- **调研总结**: PRM 校准和 PRM 可攻击性确实是两条基本独立的研究线。近期（2025-2026）悲观主义防御（Caution、PET、pessimistic RM）和不确定性感知方法（URM、PURM、Bayesian RM）正在快速涌现，但尚无工作正式建立校准质量与可攻击性的因果联系。Proposal 识别的 gap 是真实的，但该领域在快速趋同——多个小组正从不同角度逼近类似结论。窗口期确实存在但正在缩小。

---

【Trivial Alternative 检验】:

**最直接的 trivial alternative**: 对 PRM 做简单的 temperature scaling（一个标量参数的后校准），然后在 RL 训练中使用校准后的分数。这是成本最低的干预。

**关键问题**: Temperature scaling、Platt scaling、isotonic regression 等 post-hoc 方法是**保序变换**（monotonic transformation）——它们不改变 PRM 对不同 response 的排序，只改变绝对分数值。Gradient-based attacks 利用的是 reward landscape 的结构（梯度方向），而不是绝对分数值。因此：

- **对 gradient attacks**: post-hoc calibration 理论上不应改变攻击表面（attack surface），因为排序和梯度方向不变。这意味着 proposal Component B1 的"最干净测试"很可能产生 **negative 结果**——post-hoc calibration alone 不减少 gradient attack hackability。
- **对 BoN overoptimization**: 校准影响 scaling 决策（何时停止增加 N），但这不是 PRM 本身的鲁棒性，而是决策层面的改进。
- **对 RL-induced hacking**: 校准后的绝对分数变化可能改变 GRPO 的优化动态，但核心 reward landscape 几何未变。

**增量价值**: CGSP 的真正增量不是来自"校准本身提高鲁棒性"，而是来自"使用校准后的不确定性估计（σ_t）进行自适应悲观"。但这本质上是 LCB（Lower Confidence Bound）方法在 step-level PRM 上的应用——这在 bandit/RL 文献中已是标准技术。与 ensemble-min 或 Caution 的 prediction-error pessimism 相比，CGSP 的优势取决于校准不确定性估计是否比这些 heuristic 代理更好，这并非显而易见。

**结论**: Trivial alternative 威胁中等偏高。如果实验发现 simple temperature scaling + standard pessimism 已经获得 CGSP 大部分收益，那 CGSP 的价值就大打折扣。

---

【前提假设检验】:

核心 claim 的逻辑链：**"PRM 校准质量好 → PRM 更难被 hack"**

**未经验证的假设 1**: 校准质量是可攻击性的**独立预测因子**，而非模型整体质量的 proxy。
- 更好的模型可能同时更 well-calibrated 和更 robust（模型质量是 confound）
- Proposal 的 Component B3（matched representation change control）试图解决这个问题，但这需要找到一个"改变表征但不改善校准"的任务，这本身是一个困难的实验设计问题
- 如果校准仅仅是"好模型"的 symptom 而非 cause，核心 claim 就变成了"好模型更难 hack"——这是 trivial 的

**未经验证的假设 2**: Post-hoc 校准改变了 reward landscape 的可攻击几何。
- 如上分析，monotonic post-hoc 校准保持排序不变，理论上不应改变 gradient attack 的攻击面
- 这与 proposal 声称的"calibration per se causally affects hackability"存在张力
- 如果 Component B1 产生 negative 结果，proposal 的核心叙事需要重大调整

**未经验证的假设 3**: Step-level flatness 与 outcome-level hackability 之间存在 compounding 关系。
- Proposal 假设 step-level Hessian spectral 分析能揭示"step-level flatness 如何跨 trajectory compound"
- 但 T 个 step-level reward 的 compositional geometry 可能非常复杂，flatness 在每步的含义可能不同（early reasoning vs. final answer steps），简单的 compounding 模型可能不成立

**未经验证的假设 4**: Calibration Drift Detector 能实时区分 distribution shift 和正常 policy 改进。
- RL 训练中 policy 自然会偏离 SFT 分布，ECE drift 可能反映正常学习而非 reward hacking
- 需要一个 threshold 来区分，但这个 threshold 的设定本身就是一个未解决的问题

---

【3 维度打分】:

**1. Novelty: 中 (偏弱)**

理由：
- **真实 novelty**: 将 PRM 校准与可攻击性正式联系起来的思路确实无人做过。调研确认两条研究线确实缺乏交叉引用。
- **但 novelty 的深度有限**: 核心假说"校准好的模型更难 hack"在直觉上是预期中的（"expected, not surprising"）。审稿人的反应更可能是"I would have guessed this"而非"surprising"。
- **CGSP 本质上是 LCB**: r̃_t = μ_t − α·σ_t/√c_t 是 bandit/RL 中 well-known 的 pessimistic/conservative 估计。应用到 step-level PRM 是增量而非突破。Caution (arXiv:2604.04648) 已经做了 reward-level pessimism，PURM 做了 uncertainty-penalized rewards——CGSP 的 novelty delta 不大。
- **Hessian spectral 分析是扩展而非创新**: 将 Ackermann et al. 从 outcome-level 扩展到 step-level 是自然延伸，方法论本身（Lanczos iteration for Hessian spectra）是标准技术。
- **最相关竞争**: "Learning a Pessimistic Reward Model in RLHF" (arXiv:2505.20556) 和 "Robust Reward Modeling via Causal Decomposition" (arXiv:2604.13833) 都在向类似方向推进——因果鲁棒 + 悲观主义。

**2. Significance: 中**

理由：
- **问题本身重要**: PRM 的可攻击性是 reasoning LLM 可靠性的核心问题。理解校准与鲁棒性的关系有实际价值。
- **48-configuration 相关性研究** 即使假说被否定也有 mapping 价值——为领域提供系统性 benchmark。
- **但实际影响取决于效果大小**: 如果 CGSP 仅比 ensemble-min 好 1-2pp，实际影响有限。
- **方法论贡献（因果隔离）有推广价值**: 使用 post-hoc calibration 做 representation-preserving 控制实验的方法论可以被其他工作借鉴。
- **但如果 Component B1 negative result（我认为很可能）**: 那故事需要重讲——"calibration per se does NOT determine hackability, but calibrated uncertainty enables better defense"——这是一个不同的、较弱的 claim。

**3. Related Work: 强 (偏中)**

理由：
- **覆盖度高**: Proposal 识别并正确描述了两条核心研究线及其交叉点的所有关键论文（Park et al., Distributional PRM, Tiwari et al., Ackermann et al., APRM, Caution, URM, Bayesian RM, Conformal RLHF）。
- **差异化定位清晰**: 与 Ackermann et al. 的区分（outcome-level vs. step-level）、与 Caution 的区分（prediction error vs. calibrated probability）、与 ensemble 方法的区分（uncalibrated vs. calibrated）都表述清楚。
- **缺口**: 未覆盖 "Robust Reward Modeling via Causal Rubrics" (OpenReview 2026) 和 "Robust Reward Modeling via Causal Decomposition" (arXiv:2604.13833)——这些同样使用因果框架处理奖励模型鲁棒性问题，是直接相关的工作。也未引用 "Learning a Pessimistic Reward Model in RLHF" (arXiv:2505.20556)，该工作在悲观 RM 方向上有直接竞争关系。

---

【概率估计】: [22% - 32%] 中位 26%

【估计理由】:
- **核心限制因素是 Novelty 深度**。该 proposal 连接了一个真实 gap，方法论设计精良，但核心发现如果 positive（"校准好的 PRM 更难 hack"），审稿人的反应大概率是 "I would have guessed this"——这将其锚定在 25-35% 区间的下半段。
- **存在非平凡的 trivial alternative 威胁**: Post-hoc calibration 保序性意味着 gradient attacks 的攻击面理论上不变，CGSP 的核心优势本质上是 LCB（标准技术）。
- **前提假设 2 的张力**: Post-hoc calibration 不改变 reward landscape 几何，这与 proposal 声称 "calibration per se causally affects hackability" 可能矛盾。如果 Component B1 产生 negative 结果，核心叙事需要调整，可能导致 story 不够连贯。
- **Related work 覆盖是加分项**，但 related work 好只能保底不能拉高上限。
- **上界被 Novelty 限制**: 即使所有实验结果完美，核心 insight 的"惊喜度"不足以突破 35%。

【主要风险】:
1. **因果隔离实验可能自我否定核心假说**: Post-hoc calibration（保序变换）理论上不改变 gradient attack 攻击面，Component B1 很可能显示 "calibration alone does NOT reduce hackability"，这将迫使 paper 重新定位为 "calibrated uncertainty enables better defense"——一个更弱的 claim，削弱整体叙事的力度。
2. **"Calibration → robustness" 可能是 confounded 结论**: 模型质量同时影响校准和鲁棒性。即使 48-config 相关性显著，也可能被审稿人以 "correlation driven by model quality confounder" 为由质疑，因果隔离实验的设计质量直接决定这个论点能否成立。
```

Sources:
- [Know What You Don't Know: Uncertainty Calibration of PRMs (NeurIPS 2025)](https://arxiv.org/abs/2506.09338)
- [Distributional Process Reward Models (May 2026)](https://arxiv.org/abs/2605.06785)
- [Reward Under Attack: Analyzing PRM Robustness (March 2026)](https://arxiv.org/abs/2603.06621)
- [Gradient Regularization Prevents Reward Hacking (Feb 2026)](https://arxiv.org/abs/2602.18037)
- [Adversarial Training for Process Reward Models (Nov 2025)](https://arxiv.org/abs/2511.22888)
- [From Curiosity to Caution: Pessimism for BoN (April 2026)](https://arxiv.org/abs/2604.04648)
- [Learning a Pessimistic Reward Model in RLHF (May 2025)](https://arxiv.org/abs/2505.20556)
- [Robust Reward Modeling via Causal Decomposition (April 2026)](https://arxiv.org/abs/2604.13833)
- [Robust Reward Modeling via Causal Rubrics (OpenReview 2026)](https://openreview.net/forum?id=oP99JQiDYp)
- [Reward Hacking: Mechanisms and Emergent Misalignment (2026)](https://arxiv.org/html/2604.13602v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e4ffc69-9d83-44ea-b211-01870c0eba64",
  "isSidechain": false,
  "requestId": "req_011CbDHe5DSFk8rijoc7zBG3",
  "type": "assistant",
  "uuid": "b9321438-e385-48f0-a769-606926b39c2a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqRT8m5gquDzT91yUB8A9T",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 27067,
      "output_tokens": 7835,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 818,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7835,
          "cache_read_input_tokens": 27067,
          "cache_creation_input_tokens": 818,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 818
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

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "b9321438-e385-48f0-a769-606926b39c2a",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration's causal role in reward hacking resistance",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "b9321438-e385-48f0-a769-606926b39c2a",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration's causal role in reward hacking resistance",
  "sessionId": "1bbdce7f-bb04-43de-8813-913beef450af"
}
```

---
