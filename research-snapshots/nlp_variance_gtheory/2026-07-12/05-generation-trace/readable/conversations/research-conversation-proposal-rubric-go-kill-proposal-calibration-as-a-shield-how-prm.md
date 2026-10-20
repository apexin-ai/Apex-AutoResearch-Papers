# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Calibration as a Shield: How PRM 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/ecb60731-02e7-46e4-8411-219f7ddb854c.jsonl`
- **Structured JSON:** [`bf1787cbaf1051665362.json`](../../sessions/bf/bf1787cbaf1051665362.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:41:13.711Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:41:13.711Z",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense\n\n## Description\nWe present the first causally rigorous study connecting PRM calibration quality to adversarial exploitability, and propose Calibration-Gated Step-Level Pessimism (CGSP), a novel defense that transforms calibrated uncertainty into adaptive reward hacking resistance during RL training. Our work bridges two mature but isolated research threads (PRM calibration and PRM hackability) through four contributions. First, an expanded correlation study across 48 configurations (8 PRMs × 6 calibration methods) provides sufficient statistical power (n=48, detecting r≥0.29 at p<0.05) to establish whether calibration quality predicts hackability metrics under gradient attacks, RL-induced hacking (GRPO on AIME), and BoN overoptimization (MATH-500), stratified by problem difficulty. Second, causal isolation experiments separate calibration's true effect from representation change artifacts: we compare post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) that provably preserve model representations against fine-tuning-based methods, with CKA verification and matched-representation-change controls. Third, step-level Hessian spectral analysis goes beyond Ackermann et al.'s outcome-level gradient norm analysis (which applies only to single-scalar reward models) to reveal how calibration affects the multi-reward compositional geometry of PRMs — analyzing how step-level flatness compounds across trajectories. Fourth, CGSP replaces raw PRM rewards during RL training with r̃_t = μ_t − α·σ_t/√c_t, where calibrated uncertainty σ_t and calibration quality c_t adaptively modulate pessimism per-step — trusted when calibration is tight, pessimistic when uncertainty is high — with a Calibration Drift Detector that monitors ECE on current-policy rollouts to flag distribution-shift-induced reward hacking in real time. CGSP differs from existing defenses (Caution uses prediction error, PET uses global pessimism, ensemble methods are uncalibrated) by being step-level, calibration-grounded, and adaptive. We evaluate CGSP against 5 baselines (uncalibrated GRPO, APRM, Caution, ensemble-min, gradient regularization) on MATH-500 and AIME, measuring both reward-accuracy alignment and downstream task accuracy.\n\n## Core Problem\nPRM calibration research and PRM hackability research are entirely separate threads with zero cross-citation — but the deeper problem is that we lack both (a) causal evidence for whether calibration actually determines hackability (vs. being merely correlated), and (b) a principled, step-level defense mechanism that leverages calibrated uncertainty to prevent reward hacking during RL training. Existing ad-hoc defenses (adversarial training, gradient regularization, pessimistic BoN) operate at the outcome level without exploiting the unique step-level structure of PRMs.\n\n## Opportunity\nThree recent developments create a uniquely favorable moment. First, Distributional PRMs (arXiv:2605.06785, May 2026) achieve calibrated step-level uncertainty via conditional optimal transport but never test robustness. Second, Tiwari et al. (arXiv:2603.06621, March 2026) demonstrate that PRMs are catastrophically hackable — near-perfect PRM rewards with <4% actual accuracy — but propose no calibration-based defense. Third, the causal isolation toolkit is mature: post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) modify only the output mapping without changing model representations, enabling controlled experiments that separate calibration effects from representation effects. No existing paper bridges these threads. Ackermann et al.'s gradient regularization work (arXiv:2602.18037) operates exclusively on outcome-level reward models with single-scalar rewards, never touching step-level PRM geometry. The CoT Entropy paper (arXiv:2502.11250) named this connection as future work 16 months ago with no follow-up. The window for a definitive, causally rigorous study is open but narrowing.\n\n## Landscape\nTwo parallel research threads have developed with zero cross-citation. Thread 1 (PRM Calibration): Park et al. (arXiv:2506.09338, NeurIPS 2025) demonstrate PRMs systematically overestimate success probabilities on hard problems, proposing quantile regression calibration. Distributional PRMs (arXiv:2605.06785, May 2026) use conditional optimal transport for calibrated monotone quantile functions, improving BoN on MATH-500 and AIME. Neither paper tests robustness. Thread 2 (PRM Hackability): Tiwari et al. (arXiv:2603.06621) show gradient attacks inflate PRM rewards 4× and RL achieves near-perfect PRM rewards with <4% accuracy, with 43% of reward gains from stylistic shortcuts. APRM (arXiv:2511.22888) uses adversarial training for +3.4pp robustness. Thread 3 (Adjacent but distinct): Ackermann et al. (arXiv:2602.18037) prove reward surface flatness correlates with accuracy retention for outcome-level RMs, but work exclusively with single-scalar rewards, analyze only gradient norms (no Hessian spectra), and never consider step-level reward models. Their theoretical framework (Propositions 3.3-3.4) assumes a single reward function R(s,a) over complete responses — inapplicable to step-level PRM geometry where T coupled reward surfaces {R_1,...,R_T} interact compositionally. InferenceTimePessimism (arXiv:2506.19248) and Caution (arXiv:2604.04648) apply pessimism for BoN but use uncalibrated uncertainty proxies (prediction error, hedging), not calibrated probabilities. URM (arXiv:2410.00847) decomposes uncertainty into aleatoric/epistemic for outcome-level RMs but not PRMs. Bayesian reward models (arXiv:2402.13210) use Laplace approximation on LoRA weights. Conformal prediction has been applied to RLHF feedback alignment (arXiv:2601.17329) but never to PRM defense. No paper establishes a causal link between calibration quality and hackability, and no paper proposes using calibrated step-level PRM uncertainty as a defense during RL training.\n\n## Approach\nThe study has four components: (A) Expanded Correlation Study, (B) Causal Isolation Experiments, (C) Step-Level Mechanistic Analysis, and (D) Calibration-Gated Step-Level Pessimism (CGSP) defense.\n\n**Component A — Expanded Correlation Study (n≥24 configurations):** Apply 6 calibration methods across 2 tiers to 8 open-source PRMs. Tier 1 (post-hoc, representation-preserving): temperature scaling, Platt scaling, isotonic regression. Tier 2 (model-modifying): quantile regression fine-tuning, conditional optimal transport, Venn-Abers predictors. The 8 PRMs span discriminative (Qwen2.5-Math-PRM-7B, Qwen2.5-Math-PRM-72B, Skywork-o1-Open-PRM-7B, RLHFlow-Llama3.1-8B-PRM, Math-Shepherd-7B, OpenR-Math-psa-7B), generative (GenPRM-7B), and implicit (EurusPRM-Stage2) architectures. Each of the 48 PRM×calibration configurations is subjected to three attack tiers: (i) gradient-based reward inflation following Tiwari et al., (ii) RL-induced reward hacking via GRPO on AIME, and (iii) BoN overoptimization at N∈{1,4,16,64,256} on MATH-500. Compute rank correlations (Spearman ρ, Kendall τ) between calibration metrics (ECE, Brier score, quantile coverage, reliability diagram sharpness) and hackability metrics (reward-accuracy divergence, attack success rate, BoN degradation onset N*). Stratify analysis by problem difficulty (MATH levels 1-5, AMC vs. AIME) to test whether calibration is more protective on hard problems where PRMs are known to be overconfident.\n\n**Component B — Causal Isolation Experiments:** This is the methodological core addressing the reviewer's causation concern. Design: (B1) Post-hoc calibration control: Apply temperature scaling, Platt scaling, and isotonic regression — which provably modify only the output mapping, not internal representations — and measure hackability change. If hackability decreases under post-hoc calibration alone, this establishes that calibration per se (not representation change) causally affects hackability. (B2) Representation change verification: For fine-tuning-based calibration methods (quantile regression, COT), measure representation change at every transformer layer using Centered Kernel Alignment (CKA) between the base PRM and calibrated PRM. (B3) Matched representation change control: Fine-tune PRMs on an auxiliary task (e.g., next-token prediction on math text) that produces CKA-matched representation changes but does NOT improve calibration. If only calibration-improving fine-tuning reduces hackability (not the CKA-matched control), the causal role of calibration is confirmed. (B4) Conformal prediction as the cleanest test: Apply split-conformal prediction to PRM step scores, providing distribution-free coverage guarantees with zero model modification. Test whether conformal-calibrated PRMs resist hacking better than uncalibrated ones.\n\n**Component C — Step-Level Mechanistic Analysis (differentiating from Ackermann et al.):** Unlike Ackermann et al., who analyze only outcome-level gradient norms and max-perturbation sharpness, we perform Hessian spectral analysis at the step level — computing top-k eigenvalues and spectral density of the step-level reward Hessian ∂²R_t/∂h² (where h is the hidden representation at step t). Key questions: (i) Do calibrated PRMs have flatter step-level reward surfaces (lower top Hessian eigenvalue)? (ii) Does flatness vary by step position (early reasoning steps vs. final answer steps)? (iii) Do hackable reward peaks correspond to isolated large Hessian eigenvalues (sharp directions) that gradient attacks exploit? This extends Ackermann et al.'s framework from single-reward geometry to multi-reward compositional geometry: we analyze how step-level flatness/sharpness compounds across a T-step trajectory to determine outcome-level hackability.\n\n**Component D — Calibration-Gated Step-Level Pessimism (CGSP) Defense:** This transforms the paper from measurement to method. CGSP operates during RL training (GRPO/PPO) by replacing raw PRM step rewards with calibration-modulated rewards: r̃_t = μ_t − α · σ_t / √(c_t), where μ_t is the calibrated step reward mean, σ_t is the calibrated uncertainty (from quantile width or conformal interval), c_t is a calibration quality score (inverse ECE computed on a rolling buffer), and α is a pessimism strength hyperparameter. When calibration is high (small σ_t, high c_t), the reward is trusted; when calibration is low (large σ_t, low c_t), pessimism dominates. This differs from existing pessimism (Caution uses prediction error, PET uses global pessimistic fine-tuning, InferenceTimePessimism uses hedging) because CGSP is (i) step-level, (ii) grounded in calibrated probabilities rather than heuristic proxies, and (iii) adaptive — the pessimism automatically strengthens in distribution-shift regions where the PRM becomes miscalibrated. Additionally, we implement a Calibration Drift Detector: during RL training, periodically measure ECE on current-policy rollouts vs. the initial SFT-distribution calibration. When drift exceeds a threshold, flag those trajectory types as potentially hacked and apply reward clipping. This converts calibration from a static property into a dynamic training signal.\n\nBaseline comparisons for CGSP: (i) uncalibrated PRM + GRPO, (ii) APRM adversarial training, (iii) Caution/prediction-error pessimism, (iv) ensemble minimum (following Coste et al.), (v) KL-regularized GRPO, (vi) gradient regularization (Ackermann et al.).\n\nCodebase starting points: young-j-park/prm-calibration for calibration fitting, Tiwari et al.'s PRM-BiasBench for adversarial evaluation, vwxyzjn/open_instruct for GRPO training infrastructure.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '4200 H100-hrs (calibration fitting: 200, rollout generation: 600, gradient attacks: 1000, GRPO RL training: 1600 [including CGSP defense training], BoN evaluation: 400, Hessian spectral analysis: 200, causal isolation controls: 200)', 'timeline': '12-14 weeks', 'estimated_gpu_cost': '$10,500 at ~$2.50/H100-hr'}, 'human_in_loop': {'gpu_hours': '3600 H100-hrs (fewer failed iterations with AI-assisted debugging)', 'timeline': '10-12 weeks', 'claude_api_cost': '$400-700 (code generation, experiment analysis, paper drafting)', 'estimated_gpu_cost': '$9,000 at ~$2.50/H100-hr'}, 'auto_research': {'gpu_hours': '5200 H100-hrs (broader sweeps over α pessimism parameter, calibration drift thresholds, and ablations across all 48 configurations)', 'timeline': '7-9 weeks', 'claude_api_cost': '$1,500-2,000 (automated experiment orchestration, iterative analysis, full draft writing)', 'estimated_gpu_cost': '$13,000 at ~$2.50/H100-hr', 'speed_bottleneck': 'GRPO RL training wall-clock time (~18hrs per PRM×calibration×defense configuration on 4×H100); Hessian spectral analysis requires Lanczos iterations per step per problem; 72B PRM requires 4×H100 for inference'}}\n\n## Inspired By\nField guide gap: PRM overconfidence on OOD problems (Section 5.3 'when more compute hurts'); Untried combination: distributional PRM calibration + PRM hackability analysis; Pattern: connecting two mature but isolated research threads; Reviewer insight: pure measurement is insufficient — the key contribution should be a causal mechanism and a defense method; Methodological insight: post-hoc calibration methods that preserve representations enable clean causal isolation experiments impossible with fine-tuning-based calibration alone\n\n## Target Venues\n- ICLR 2027 (abstract Sep 19, paper Sep 24, 2026)\n- AAAI 2027 (abstract Jul 21, paper Jul 28, 2026)\n- AISTATS 2027 (paper Oct 10, 2026)\n\n## Key References\n- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (arXiv:2506.09338, NeurIPS 2025)\n- Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport (arXiv:2605.06785, May 2026)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv:2603.06621, March 2026)\n- Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards (arXiv:2602.18037, Feb 2026)\n- Adversarial Training for Process Reward Models (arXiv:2511.22888, Nov 2025)\n- From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism (arXiv:2604.04648, April 2026)\n- Inference-Time Reward Hacking in Large Language Models (arXiv:2506.19248, NeurIPS 2025 Spotlight)\n- Uncertainty-Aware Step-wise Verification with Generative Reward Models (arXiv:2502.11250, ICLR 2025 Workshop)\n- Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242, April 2026)\n- Uncertainty-Aware Reward Model (arXiv:2410.00847)\n- Helping or Herding? Reward Model Ensembles Mitigate but Do Not Eliminate Overoptimization (arXiv:2312.09244)\n- Bayesian Reward Models for LLM Alignment (arXiv:2402.13210)\n- Conformal Feedback Alignment for RLHF (arXiv:2601.17329)\n- Taming Overconfidence in LLMs: Reward Calibration in RLHF (arXiv:2410.09724)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (arXiv:2501.03124)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T05:41:13.715Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:41:13.715Z",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-20T05:41:13.788Z_

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
  "promptId": "af403a09-8d24-4670-ac94-635b17ecc710",
  "type": "user",
  "uuid": "f8663fc5-173f-4153-8f51-d514ee8756f8",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:41:13.786Z_

```json
{
  "parentUuid": "f8663fc5-173f-4153-8f51-d514ee8756f8",
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
  "uuid": "ec370621-150f-4541-a513-fe531c99e0c3",
  "timestamp": "2026-05-20T05:41:13.786Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:41:13.786Z_

```json
{
  "parentUuid": "ec370621-150f-4541-a513-fe531c99e0c3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cf0e6b0e-502f-4c7f-9ed6-68a3e9fead3d",
  "timestamp": "2026-05-20T05:41:13.786Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
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
  "leafUuid": "cf0e6b0e-502f-4c7f-9ed6-68a3e9fead3d",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration quality and reward hacking resistance analysis",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:41:20.906Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal. Before I can give a proper assessment, I need to do thorough literature research to understand the current landscape and validate the novelty claims. Let me start by searching for the key papers and topics mentioned in this proposal.

The proposal is about:
1. Establishing a causal link between PRM (Process Reward Model) calibration quality and adversarial exploitability/hackability
2. Proposing CGSP (Calibration-Gated Step-Level Pessimism) as a defense mechanism
3. Bridging two research threads: PRM calibration and PRM hackability


4. Now I'm looking into the existing literature on these topics to understand what's already been established and where the gaps are.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf0e6b0e-502f-4c7f-9ed6-68a3e9fead3d",
  "isSidechain": false,
  "requestId": "req_011CbDHWenK545zRBa2L7TYX",
  "type": "assistant",
  "uuid": "3e43e964-5960-4b80-bfca-b1e1ce1e29f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2jPMeaqiDYietgtt1GJBR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5654,
      "cache_read_input_tokens": 14333,
      "output_tokens": 269,
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
          "output_tokens": 269,
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

_source line 9 · 2026-05-20T05:41:21.052Z_

I need to conduct thorough literature research before evaluating this proposal. Let me search for the key papers and the current state of the field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e43e964-5960-4b80-bfca-b1e1ce1e29f0",
  "isSidechain": false,
  "requestId": "req_011CbDHWenK545zRBa2L7TYX",
  "type": "assistant",
  "uuid": "6ce7cf55-1696-4c93-bef4-4240cbe66d70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2jPMeaqiDYietgtt1GJBR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5654,
      "cache_read_input_tokens": 14333,
      "output_tokens": 269,
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
          "output_tokens": 269,
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

_source line 10 · 2026-05-20T05:41:21.117Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Kq8WzW3JETn3HTLwDW3hu1`</summary>

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
  "parentUuid": "6ce7cf55-1696-4c93-bef4-4240cbe66d70",
  "isSidechain": false,
  "requestId": "req_011CbDHWenK545zRBa2L7TYX",
  "type": "assistant",
  "uuid": "853e14b0-b4a7-4179-83fd-56a31daecd1d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J2jPMeaqiDYietgtt1GJBR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5654,
      "cache_read_input_tokens": 14333,
      "output_tokens": 269,
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
          "output_tokens": 269,
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

_source line 11 · 2026-05-20T05:41:21.123Z_

<details><summary>↩ Tool result · `toolu_01Kq8WzW3JETn3HTLwDW3hu1`</summary>

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
  "parentUuid": "853e14b0-b4a7-4179-83fd-56a31daecd1d",
  "isSidechain": false,
  "promptId": "af403a09-8d24-4670-ac94-635b17ecc710",
  "type": "user",
  "uuid": "755cc8a8-94fe-4826-8f2a-e9b88dd83fee",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "853e14b0-b4a7-4179-83fd-56a31daecd1d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T05:41:23.457Z_

Now let me conduct the literature searches in parallel to understand the current landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "755cc8a8-94fe-4826-8f2a-e9b88dd83fee",
  "isSidechain": false,
  "requestId": "req_011CbDHXCRpdaKhc8s8KidD7",
  "type": "assistant",
  "uuid": "59ebc5d2-4ab5-4c07-80fb-f05308db43cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjTMKRitNHYhZ84YWZLAKn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 19987,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 88,
          "cache_read_input_tokens": 19987,
          "cache_creation_input_tokens": 796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 796
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

_source line 13 · 2026-05-20T05:41:23.959Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q4ktzsR4Ygo7yGPffS1hNK`</summary>

```json
{
  "query": "PRM process reward model hackability robustness adversarial attack 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59ebc5d2-4ab5-4c07-80fb-f05308db43cf",
  "isSidechain": false,
  "requestId": "req_011CbDHXCRpdaKhc8s8KidD7",
  "type": "assistant",
  "uuid": "fc41cbc7-fb66-46dd-a061-84b5183472bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjTMKRitNHYhZ84YWZLAKn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 19987,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 88,
          "cache_read_input_tokens": 19987,
          "cache_creation_input_tokens": 796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 796
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

_source line 14 · 2026-05-20T05:41:31.682Z_

<details><summary>↩ Tool result · `toolu_01Q4ktzsR4Ygo7yGPffS1hNK`</summary>

```text
Web search results for query: "PRM process reward model hackability robustness adversarial attack 2025 2026"

Links: [{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"1 Introduction","url":"https://arxiv.org/html/2603.06621"},{"title":"Adversarial Training for Process Reward Models | OpenReview","url":"https://openreview.net/forum?id=7DXEF4xHt3"},{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"},{"title":"[2511.22888] Adversarial Training for Process Reward Models","url":"https://arxiv.org/abs/2511.22888"},{"title":"Adversarial Training of Reward Models","url":"https://arxiv.org/pdf/2504.06141"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/pdf/2511.22888"},{"title":"PRM-Free Security Alignment of Large Models via Red Teaming and Adversarial Training","url":"https://arxiv.org/pdf/2507.14202"}]

Here are the search results for PRM process reward model hackability, robustness, and adversarial attacks in 2025-2026:

## Key Findings

**Robustness Vulnerabilities:**

Process Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure. Static perturbation analysis uncovers a fluency-logic dissociation: high invariance to surface-level style changes, yet inconsistent detection of logically-corrupted reasoning, with different models failing on different attack types.

**Adversarial Attack Findings:**

Adversarial optimization demonstrates that gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks. Most critically, policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.

**Fundamental Issue:**

Current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.

## Defense Approaches

Recent work has explored adversarial training to improve robustness. Adversarially Trained PRMs (APRM) use a Generator to produce reasoning errors to deceive a PRM while the PRM learns to detect them, improving its robustness and generalization to novel errors. APRM improves solver accuracy by +3.4 percentage points over the strongest PRM baseline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc41cbc7-fb66-46dd-a061-84b5183472bf",
  "isSidechain": false,
  "promptId": "af403a09-8d24-4670-ac94-635b17ecc710",
  "type": "user",
  "uuid": "c31e07fe-cf96-48d0-a48f-a51745c56151",
  "toolUseResult": {
    "query": "PRM process reward model hackability robustness adversarial attack 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018xizhroT51Z2efrk2xVmcM",
        "content": [
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2603.06621"
          },
          {
            "title": "Adversarial Training for Process Reward Models | OpenReview",
            "url": "https://openreview.net/forum?id=7DXEF4xHt3"
          },
          {
            "title": "[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/abs/2603.06621"
          },
          {
            "title": "[2511.22888] Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/abs/2511.22888"
          },
          {
            "title": "Adversarial Training of Reward Models",
            "url": "https://arxiv.org/pdf/2504.06141"
          },
          {
            "title": "Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/pdf/2511.22888"
          },
          {
            "title": "PRM-Free Security Alignment of Large Models via Red Teaming and Adversarial Training",
            "url": "https://arxiv.org/pdf/2507.14202"
          }
        ]
      },
      "Here are the search results for PRM process reward model hackability, robustness, and adversarial attacks in 2025-2026:\n\n## Key Findings\n\n**Robustness Vulnerabilities:**\n\nProcess Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure. Static perturbation analysis uncovers a fluency-logic dissociation: high invariance to surface-level style changes, yet inconsistent detection of logically-corrupted reasoning, with different models failing on different attack types.\n\n**Adversarial Attack Findings:**\n\nAdversarial optimization demonstrates that gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks. Most critically, policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.\n\n**Fundamental Issue:**\n\nCurrent PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.\n\n## Defense Approaches\n\nRecent work has explored adversarial training to improve robustness. Adversarially Trained PRMs (APRM) use a Generator to produce reasoning errors to deceive a PRM while the PRM learns to detect them, improving its robustness and generalization to novel errors. APRM improves solver accuracy by +3.4 percentage points over the strongest PRM baseline."
    ],
    "durationSeconds": 7.716482666,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fc41cbc7-fb66-46dd-a061-84b5183472bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T05:41:34.196Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019UHwirR7btpa4m7pja7c2c`</summary>

```json
{
  "query": "PRM calibration process reward model uncertainty calibration 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c31e07fe-cf96-48d0-a48f-a51745c56151",
  "isSidechain": false,
  "requestId": "req_011CbDHXxs2UaqFa47CcY142",
  "type": "assistant",
  "uuid": "74e8e4c2-7eeb-4a1f-8736-52bad82cebf8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5zLtneG9rbdg9LRQ5KfBt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 802,
      "cache_read_input_tokens": 20783,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 20783,
          "cache_creation_input_tokens": 802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 802
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

_source line 16 · 2026-05-20T05:41:42.692Z_

<details><summary>↩ Tool result · `toolu_019UHwirR7btpa4m7pja7c2c`</summary>

```text
Web search results for query: "PRM calibration process reward model uncertainty calibration 2025 2026"

Links: [{"title":"[2506.09338] Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/abs/2506.09338"},{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models | OpenReview","url":"https://openreview.net/forum?id=hzMkfIrdDT"},{"title":"NeurIPS Poster Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://neurips.cc/virtual/2025/poster/116598"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/html/2506.09338v1"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models","url":"https://openreview.net/pdf?id=hzMkfIrdDT"},{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/pdf/2506.09338"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models for NeurIPS 2025 - IBM Research","url":"https://research.ibm.com/publications/know-what-you-dont-know-uncertainty-calibration-of-process-reward-models"},{"title":"Process Reward Models (PRMs): Calibration & Scaling","url":"https://www.emergentmind.com/topics/process-reward-models-prms"}]

Based on the search results, here's what I found on PRM (Process Reward Model) calibration and uncertainty calibration:

## Key Research: "Know What You Don't Know"

Process reward models (PRMs) play a central role in guiding inference-time scaling algorithms for large language models (LLMs), but even state-of-the-art PRMs can be poorly calibrated, specifically tending to overestimate the success probability that a partial reasoning step will lead to a correct final answer, particularly when smaller LLMs are used.

## Calibration Approach

The research introduces a quantile-regression calibration that aligns PRM outputs with success probabilities. Standard calibration techniques, such as temperature scaling, are inadequate for calibrating PRMs.

## Practical Application: Instance-Adaptive Scaling (IAS)

The calibrated success estimates and their confidence bounds enable an instance-adaptive scaling framework that dynamically adjusts the inference budget based on the estimated likelihood that a partial reasoning trajectory will yield a correct final answer, adapting to each instance and reasoning step.

## Results

The PRM calibration method achieves small calibration error outperforming baseline methods, calibration is crucial for enabling effective adaptive scaling, and the proposed IAS strategy reduces inference costs while maintaining final answer accuracy.

This research was presented at NeurIPS 2025 and represents recent developments in making PRMs more reliable and efficient for LLM inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74e8e4c2-7eeb-4a1f-8736-52bad82cebf8",
  "isSidechain": false,
  "promptId": "af403a09-8d24-4670-ac94-635b17ecc710",
  "type": "user",
  "uuid": "90dbe4be-8441-462d-91c6-dd75b83b9ad1",
  "toolUseResult": {
    "query": "PRM calibration process reward model uncertainty calibration 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BGq5A234mozYqegKh923Nz",
        "content": [
          {
            "title": "[2506.09338] Know What You Don't Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://arxiv.org/abs/2506.09338"
          },
          {
            "title": "Know What You Don't Know: Uncertainty Calibration of Process Reward Models | OpenReview",
            "url": "https://openreview.net/forum?id=hzMkfIrdDT"
          },
          {
            "title": "NeurIPS Poster Know What You Don't Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://neurips.cc/virtual/2025/poster/116598"
          },
          {
            "title": "Know What You Don’t Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://arxiv.org/html/2506.09338v1"
          },
          {
            "title": "Know What You Don’t Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://openreview.net/pdf?id=hzMkfIrdDT"
          },
          {
            "title": "Know What You Don't Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://arxiv.org/pdf/2506.09338"
          },
          {
            "title": "Know What You Don’t Know: Uncertainty Calibration of Process Reward Models for NeurIPS 2025 - IBM Research",
            "url": "https://research.ibm.com/publications/know-what-you-dont-know-uncertainty-calibration-of-process-reward-models"
          },
          {
            "title": "Process Reward Models (PRMs): Calibration & Scaling",
            "url": "https://www.emergentmind.com/topics/process-reward-models-prms"
          }
        ]
      },
      "Based on the search results, here's what I found on PRM (Process Reward Model) calibration and uncertainty calibration:\n\n## Key Research: \"Know What You Don't Know\"\n\nProcess reward models (PRMs) play a central role in guiding inference-time scaling algorithms for large language models (LLMs), but even state-of-the-art PRMs can be poorly calibrated, specifically tending to overestimate the success probability that a partial reasoning step will lead to a correct final answer, particularly when smaller LLMs are used.\n\n## Calibration Approach\n\nThe research introduces a quantile-regression calibration that aligns PRM outputs with success probabilities. Standard calibration techniques, such as temperature scaling, are inadequate for calibrating PRMs.\n\n## Practical Application: Instance-Adaptive Scaling (IAS)\n\nThe calibrated success estimates and their confidence bounds enable an instance-adaptive scaling framework that dynamically adjusts the inference budget based on the estimated likelihood that a partial reasoning trajectory will yield a correct final answer, adapting to each instance and reasoning step.\n\n## Results\n\nThe PRM calibration method achieves small calibration error outperforming baseline methods, calibration is crucial for enabling effective adaptive scaling, and the proposed IAS strategy reduces inference costs while maintaining final answer accuracy.\n\nThis research was presented at NeurIPS 2025 and represents recent developments in making PRMs more reliable and efficient for LLM inference."
    ],
    "durationSeconds": 8.491933302999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "74e8e4c2-7eeb-4a1f-8736-52bad82cebf8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T05:41:44.602Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UVdspo4SXXUVS3XjhDhwG7`</summary>

```json
{
  "query": "distributional process reward model calibrated optimal transport arXiv 2605.06785"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90dbe4be-8441-462d-91c6-dd75b83b9ad1",
  "isSidechain": false,
  "requestId": "req_011CbDHYmuVSTdoQBZZQ2VjC",
  "type": "assistant",
  "uuid": "30f7b866-f75d-4dcf-b104-1af1466fbe8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GaoXCHh4UbGWLpWstuukAG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 817,
      "cache_read_input_tokens": 21585,
      "output_tokens": 69,
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
          "output_tokens": 69,
          "cache_read_input_tokens": 21585,
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

_source line 18 · 2026-05-20T05:42:04.402Z_

<details><summary>↩ Tool result · `toolu_01UVdspo4SXXUVS3XjhDhwG7`</summary>

```text
Web search results for query: "distributional process reward model calibrated optimal transport arXiv 2605.06785"

Links: [{"title":"[2605.06785] Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/abs/2605.06785"},{"title":"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/html/2605.06785"},{"title":"APLOT: Robust Reward Modeling via Adaptive Preference Learning with Optimal Transport","url":"https://arxiv.org/pdf/2510.10963"},{"title":"Distributional Preference Alignment of LLMs via Optimal Transport","url":"https://arxiv.org/pdf/2406.05882"},{"title":"Optimal Transport Model Distributional Robustness Van-Anh Nguyen1 Trung Le1","url":"https://arxiv.org/pdf/2306.04178"},{"title":"[2306.04178] Optimal Transport Model Distributional Robustness","url":"https://arxiv.org/abs/2306.04178"},{"title":"[2406.05882] Distributional Preference Alignment of LLMs via Optimal Transport","url":"https://arxiv.org/abs/2406.05882"}]

Based on the search results, here's what I found about arXiv paper 2605.06785:

## Paper Overview

The paper addresses the issue that Process Reward Models (PRMs) used in inference-time scaling methods are often poorly calibrated and overestimate success probabilities.

## Main Contribution

The authors propose what appears to be the first use of conditional optimal transport for calibrating PRMs, modifying conditional OT (CondOT) map learning to estimate a monotonic conditional quantile function over success probabilities estimated by the PRM, conditioned on PRM hidden states.

## Key Features

This approach yields structurally valid quantile estimates and enables efficient extraction of confidence bounds at arbitrary levels, which they integrate into the instance-adaptive scaling (IAS) framework.

## Evaluation

The method is evaluated on mathematical reasoning benchmarks spanning moderate-difficulty problems (MATH-500) and harder out-of-distribution problems (AIME), with results showing substantial improvements in calibration over both uncalibrated PRMs and quantile regression for PRMs with reliable ranking signals.

**Authors:** Rachel Ma, Dylan Hadfield-Menell, and Kristjan Greenewald  
**Submission Date:** May 7, 2026


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30f7b866-f75d-4dcf-b104-1af1466fbe8e",
  "isSidechain": false,
  "promptId": "af403a09-8d24-4670-ac94-635b17ecc710",
  "type": "user",
  "uuid": "74adf9db-b872-4590-8bd6-961e61a55da6",
  "toolUseResult": {
    "query": "distributional process reward model calibrated optimal transport arXiv 2605.06785",
    "results": [
      {
        "tool_use_id": "srvtoolu_013XfqnrnAgLEGyvyGkqCMLz",
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
            "title": "APLOT: Robust Reward Modeling via Adaptive Preference Learning with Optimal Transport",
            "url": "https://arxiv.org/pdf/2510.10963"
          },
          {
            "title": "Distributional Preference Alignment of LLMs via Optimal Transport",
            "url": "https://arxiv.org/pdf/2406.05882"
          },
          {
            "title": "Optimal Transport Model Distributional Robustness Van-Anh Nguyen1 Trung Le1",
            "url": "https://arxiv.org/pdf/2306.04178"
          },
          {
            "title": "[2306.04178] Optimal Transport Model Distributional Robustness",
            "url": "https://arxiv.org/abs/2306.04178"
          },
          {
            "title": "[2406.05882] Distributional Preference Alignment of LLMs via Optimal Transport",
            "url": "https://arxiv.org/abs/2406.05882"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2605.06785:\n\n## Paper Overview\n\nThe paper addresses the issue that Process Reward Models (PRMs) used in inference-time scaling methods are often poorly calibrated and overestimate success probabilities.\n\n## Main Contribution\n\nThe authors propose what appears to be the first use of conditional optimal transport for calibrating PRMs, modifying conditional OT (CondOT) map learning to estimate a monotonic conditional quantile function over success probabilities estimated by the PRM, conditioned on PRM hidden states.\n\n## Key Features\n\nThis approach yields structurally valid quantile estimates and enables efficient extraction of confidence bounds at arbitrary levels, which they integrate into the instance-adaptive scaling (IAS) framework.\n\n## Evaluation\n\nThe method is evaluated on mathematical reasoning benchmarks spanning moderate-difficulty problems (MATH-500) and harder out-of-distribution problems (AIME), with results showing substantial improvements in calibration over both uncalibrated PRMs and quantile regression for PRMs with reliable ranking signals.\n\n**Authors:** Rachel Ma, Dylan Hadfield-Menell, and Kristjan Greenewald  \n**Submission Date:** May 7, 2026"
    ],
    "durationSeconds": 19.795894578,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "30f7b866-f75d-4dcf-b104-1af1466fbe8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T05:42:06.503Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WErwb8kQ7LVsK2S8W8Ey1E`</summary>

```json
{
  "query": "reward hacking defense pessimism RL training calibration uncertainty 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74adf9db-b872-4590-8bd6-961e61a55da6",
  "isSidechain": false,
  "requestId": "req_011CbDHaNhnWrBDfY6YiDcm2",
  "type": "assistant",
  "uuid": "d4c20ba0-e771-4327-bd48-ec4ad53802af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Tz4E9rPzKzwtMKg1Qo6sS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 22402,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 708,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 22402,
          "cache_creation_input_tokens": 708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 708
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

_source line 20 · 2026-05-20T05:42:13.086Z_

<details><summary>↩ Tool result · `toolu_01WErwb8kQ7LVsK2S8W8Ey1E`</summary>

```text
Web search results for query: "reward hacking defense pessimism RL training calibration uncertainty 2025 2026"

Links: [{"title":"Reward Hacking Defense Rubric","url":"https://www.emergentmind.com/topics/reward-hacking-defense-rubric"},{"title":"Reinforcement Learning from Human Feedback (RLHF) Explained","url":"https://intuitionlabs.ai/pdfs/reinforcement-learning-from-human-feedback-rlhf-explained.pdf"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/pdf/2604.04648"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf"},{"title":"Reinforcement Learning with Missing Context to Mitigate Reward Hacking from Training Only on Golden Answers | OpenReview","url":"https://openreview.net/forum?id=eOqnXPOl4S"},{"title":"Natural emergent misalignment from reward hacking in production RL","url":"https://arxiv.org/html/2511.18397v1"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"NATURAL EMERGENT MISALIGNMENT FROM REWARD HACKING IN PRODUCTION RL","url":"https://assets.anthropic.com/m/74342f2c96095771/original/Natural-emergent-misalignment-from-reward-hacking-paper.pdf"}]

I found relevant research on reward hacking defense with pessimism, calibration, and uncertainty approaches from 2025-2026. Here's a summary of the key findings:

## Recent Defenses Against Reward Hacking

Pessimistic reward modeling (Xu et al., May 2025) embeds pessimism so that even "greedy" policy optimization under the learned reward is robust to overestimation, and requires no KL regularization.

The Probabilistic Uncertain Reward Model (PURM) generalizes scalar reward outputs to Gaussian distributions, quantifies uncertainty, and penalizes learning in regions of high uncertainty to prevent overoptimization.

## RL Training Approaches

One approach penalizes out-of-distribution responses by subtracting per-response uncertainty estimates from reward scores, measuring uncertainty by training a student model to predict a fixed target on in-distribution data.

## Practical Challenges

Defending against reward hacking through continuous retraining, intensive counterfactual data generation, and specification monitoring raise computational demands.

Recent 2025-2026 research has made significant progress on mitigating reward hacking.

The search results show an active research area with multiple complementary approaches combining pessimism, uncertainty quantification, and calibration techniques to address reward hacking in RL training systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4c20ba0-e771-4327-bd48-ec4ad53802af",
  "isSidechain": false,
  "promptId": "af403a09-8d24-4670-ac94-635b17ecc710",
  "type": "user",
  "uuid": "e48d538b-2bdc-4b50-9609-201d03e8ab6f",
  "toolUseResult": {
    "query": "reward hacking defense pessimism RL training calibration uncertainty 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XiqqBBABNAZrcqQrex9pgG",
        "content": [
          {
            "title": "Reward Hacking Defense Rubric",
            "url": "https://www.emergentmind.com/topics/reward-hacking-defense-rubric"
          },
          {
            "title": "Reinforcement Learning from Human Feedback (RLHF) Explained",
            "url": "https://intuitionlabs.ai/pdfs/reinforcement-learning-from-human-feedback-rlhf-explained.pdf"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism",
            "url": "https://arxiv.org/pdf/2604.04648"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf"
          },
          {
            "title": "Reinforcement Learning with Missing Context to Mitigate Reward Hacking from Training Only on Golden Answers | OpenReview",
            "url": "https://openreview.net/forum?id=eOqnXPOl4S"
          },
          {
            "title": "Natural emergent misalignment from reward hacking in production RL",
            "url": "https://arxiv.org/html/2511.18397v1"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/pdf/2505.20556"
          },
          {
            "title": "NATURAL EMERGENT MISALIGNMENT FROM REWARD HACKING IN PRODUCTION RL",
            "url": "https://assets.anthropic.com/m/74342f2c96095771/original/Natural-emergent-misalignment-from-reward-hacking-paper.pdf"
          }
        ]
      },
      "I found relevant research on reward hacking defense with pessimism, calibration, and uncertainty approaches from 2025-2026. Here's a summary of the key findings:\n\n## Recent Defenses Against Reward Hacking\n\nPessimistic reward modeling (Xu et al., May 2025) embeds pessimism so that even \"greedy\" policy optimization under the learned reward is robust to overestimation, and requires no KL regularization.\n\nThe Probabilistic Uncertain Reward Model (PURM) generalizes scalar reward outputs to Gaussian distributions, quantifies uncertainty, and penalizes learning in regions of high uncertainty to prevent overoptimization.\n\n## RL Training Approaches\n\nOne approach penalizes out-of-distribution responses by subtracting per-response uncertainty estimates from reward scores, measuring uncertainty by training a student model to predict a fixed target on in-distribution data.\n\n## Practical Challenges\n\nDefending against reward hacking through continuous retraining, intensive counterfactual data generation, and specification monitoring raise computational demands.\n\nRecent 2025-2026 research has made significant progress on mitigating reward hacking.\n\nThe search results show an active research area with multiple complementary approaches combining pessimism, uncertainty quantification, and calibration techniques to address reward hacking in RL training systems."
    ],
    "durationSeconds": 6.577339066999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d4c20ba0-e771-4327-bd48-ec4ad53802af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
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
  "leafUuid": "e48d538b-2bdc-4b50-9609-201d03e8ab6f",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration quality and reward hacking resistance analysis",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c"
}
```

---

### Tool call

_source line 23 · 2026-05-20T05:42:15.556Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J7KHgfWAhjEJV7rKm9ryDY`</summary>

```json
{
  "query": "gradient regularization reward hacking Ackermann arXiv 2602.18037 Hessian reward surface flatness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e48d538b-2bdc-4b50-9609-201d03e8ab6f",
  "isSidechain": false,
  "requestId": "req_011CbDHb1sC1Mhaqn7MZkcEU",
  "type": "assistant",
  "uuid": "9aa1e937-2948-4ede-ad5b-9c69988946a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcidoYnChtW7Zvnntphs65",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 23110,
      "output_tokens": 79,
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
          "output_tokens": 79,
          "cache_read_input_tokens": 23110,
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

_source line 24 · 2026-05-20T05:42:22.594Z_

<details><summary>↩ Tool result · `toolu_01J7KHgfWAhjEJV7rKm9ryDY`</summary>

```text
Web search results for query: "gradient regularization reward hacking Ackermann arXiv 2602.18037 Hessian reward surface flatness"

Links: [{"title":"[2602.18037] Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards","url":"https://arxiv.org/abs/2602.18037"},{"title":"Gradient Regularization Prevents Reward Hacking in ...","url":"https://arxiv.org/pdf/2602.18037"},{"title":"[2604.16242] Detecting and Suppressing Reward Hacking with Gradient Fingerprints","url":"https://arxiv.org/abs/2604.16242"},{"title":"Reward Sharpness-Aware Fine-Tuning for Diffusion Models","url":"https://arxiv.org/pdf/2603.21175"},{"title":"Noise Stability Optimization for Finding Flat Minima: A Hessian-based   Regularization Approach","url":"https://arxiv.org/pdf/2306.08553"},{"title":"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking","url":"https://arxiv.org/pdf/2501.19358"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"}]

Based on the search results, I found the paper you're looking for:

"Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards" is a paper by Johannes Ackermann and 3 other authors.

The paper's key contributions include:

1. **Theoretical Framework**: The authors derive a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence, showing that gradient regularization (GR) can be used to bias training to flatter regions and thereby maintain reward model accuracy.

2. **Empirical Validation**: The gradient norm and reward accuracy are empirically correlated in RLHF.

3. **Practical Improvements**: The authors propose to use explicit GR with an efficient finite-difference estimate, and empirically GR performs better than a KL penalty across a diverse set of RL experiments with LMs.

4. **Applications**: GR achieves a higher GPT-judged win-rate in RLHF, avoids overly focusing on the format in rule-based math rewards, and prevents hacking the judge in LLM-as-a-Judge math tasks.

The paper was posted on arXiv on February 20, 2026 (arXiv:2602.18037).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9aa1e937-2948-4ede-ad5b-9c69988946a1",
  "isSidechain": false,
  "promptId": "af403a09-8d24-4670-ac94-635b17ecc710",
  "type": "user",
  "uuid": "a6e9ec11-5f87-457a-b6b3-fa06f3157206",
  "toolUseResult": {
    "query": "gradient regularization reward hacking Ackermann arXiv 2602.18037 Hessian reward surface flatness",
    "results": [
      {
        "tool_use_id": "srvtoolu_012ZPoZfDFN5UQUEris1uYfU",
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
            "title": "[2604.16242] Detecting and Suppressing Reward Hacking with Gradient Fingerprints",
            "url": "https://arxiv.org/abs/2604.16242"
          },
          {
            "title": "Reward Sharpness-Aware Fine-Tuning for Diffusion Models",
            "url": "https://arxiv.org/pdf/2603.21175"
          },
          {
            "title": "Noise Stability Optimization for Finding Flat Minima: A Hessian-based   Regularization Approach",
            "url": "https://arxiv.org/pdf/2306.08553"
          },
          {
            "title": "The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking",
            "url": "https://arxiv.org/pdf/2501.19358"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/pdf/2604.02986"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards\" is a paper by Johannes Ackermann and 3 other authors.\n\nThe paper's key contributions include:\n\n1. **Theoretical Framework**: The authors derive a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence, showing that gradient regularization (GR) can be used to bias training to flatter regions and thereby maintain reward model accuracy.\n\n2. **Empirical Validation**: The gradient norm and reward accuracy are empirically correlated in RLHF.\n\n3. **Practical Improvements**: The authors propose to use explicit GR with an efficient finite-difference estimate, and empirically GR performs better than a KL penalty across a diverse set of RL experiments with LMs.\n\n4. **Applications**: GR achieves a higher GPT-judged win-rate in RLHF, avoids overly focusing on the format in rule-based math rewards, and prevents hacking the judge in LLM-as-a-Judge math tasks.\n\nThe paper was posted on arXiv on February 20, 2026 (arXiv:2602.18037)."
    ],
    "durationSeconds": 7.034763373000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9aa1e937-2948-4ede-ad5b-9c69988946a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T05:42:26.220Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013F4udNtpxQAoAVqjnvQ2Uz`</summary>

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
  "parentUuid": "a6e9ec11-5f87-457a-b6b3-fa06f3157206",
  "isSidechain": false,
  "requestId": "req_011CbDHbiWSFu9NMnyXN7Rkq",
  "type": "assistant",
  "uuid": "ca62bb2a-1cfb-425a-bf12-d2b013c47e97",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JThpUu6QFLeeNR7McYywP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 23943,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 23943,
          "cache_creation_input_tokens": 764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 764
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

_source line 26 · 2026-05-20T05:42:32.640Z_

<details><summary>↩ Tool result · `toolu_013F4udNtpxQAoAVqjnvQ2Uz`</summary>

```text
Web search results for query: ""calibration" "reward hacking" causal link process reward model step-level defense 2026"

Links: [{"title":"Avoiding Reward Hacking","url":"https://www.emergentmind.com/topics/avoiding-reward-hacking"},{"title":"Beyond Outcome Verification: Verifiable Process Reward Models for","url":"https://www.arxiv.org/pdf/2601.17223"},{"title":"GitHub - JLZhong23/awesome-reward-models · GitHub","url":"https://github.com/JLZhong23/awesome-reward-models"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"Reward Hacking Defense Rubric","url":"https://www.emergentmind.com/topics/reward-hacking-defense-rubric"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/pdf/2509.26578"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/pdf/2508.04216"}]

Based on the search results, here's what I found regarding calibration, reward hacking, causal links, process reward models, and step-level defenses in 2026:

## Key Research Areas

**Causal Approaches to Reward Hacking:**
Causal Reward Adjustment leverages sparse autoencoders and structural causal models to identify and correct for reward-hacking confounders, applying backdoor adjustment to debias the reward model. More specifically, this method trains sparse autoencoders on the PRM's internal activations to recover interpretable features, then corrects confounding by using backdoor adjustment.

**Process Reward Models and Step-Level Defenses:**
Verifiable step-level rewards would eliminate the aforementioned problems associated with neural process rewards. Process reward models provide finer-grained rewards at the level of individual reasoning steps or even tokens. Additionally, conditional reward modeling explicitly conditions each step reward on the previous reasoning steps and aligns it with the final outcome.

**Multi-Step Defenses:**
Myopic Optimization with Non-myopic Approval (MONA) ensures agents optimize only step-wise rewards plus approval, blocking multi-step hacks by eliminating foresight about reward returns.

**Robustness Results:**
Conditional reward modeling is more robust to reward hacking and delivers stable downstream improvements without relying on verifiable rewards derived from ground truth.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca62bb2a-1cfb-425a-bf12-d2b013c47e97",
  "isSidechain": false,
  "promptId": "af403a09-8d24-4670-ac94-635b17ecc710",
  "type": "user",
  "uuid": "14bc3721-93f4-441c-a21f-5faacbed23e4",
  "toolUseResult": {
    "query": "\"calibration\" \"reward hacking\" causal link process reward model step-level defense 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015ja9cFgusaVvACS8GeZ9WL",
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
      "Based on the search results, here's what I found regarding calibration, reward hacking, causal links, process reward models, and step-level defenses in 2026:\n\n## Key Research Areas\n\n**Causal Approaches to Reward Hacking:**\nCausal Reward Adjustment leverages sparse autoencoders and structural causal models to identify and correct for reward-hacking confounders, applying backdoor adjustment to debias the reward model. More specifically, this method trains sparse autoencoders on the PRM's internal activations to recover interpretable features, then corrects confounding by using backdoor adjustment.\n\n**Process Reward Models and Step-Level Defenses:**\nVerifiable step-level rewards would eliminate the aforementioned problems associated with neural process rewards. Process reward models provide finer-grained rewards at the level of individual reasoning steps or even tokens. Additionally, conditional reward modeling explicitly conditions each step reward on the previous reasoning steps and aligns it with the final outcome.\n\n**Multi-Step Defenses:**\nMyopic Optimization with Non-myopic Approval (MONA) ensures agents optimize only step-wise rewards plus approval, blocking multi-step hacks by eliminating foresight about reward returns.\n\n**Robustness Results:**\nConditional reward modeling is more robust to reward hacking and delivers stable downstream improvements without relying on verifiable rewards derived from ground truth."
    ],
    "durationSeconds": 6.414345895000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ca62bb2a-1cfb-425a-bf12-d2b013c47e97",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T05:42:35.966Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F2s83uw9YkvmZcVqGHG1c1`</summary>

```json
{
  "query": "pessimistic reward model uncertainty step level RL LLM reasoning \"Caution\" \"inference time pessimism\" 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14bc3721-93f4-441c-a21f-5faacbed23e4",
  "isSidechain": false,
  "requestId": "req_011CbDHcTVL1tLPbnFY4crXo",
  "type": "assistant",
  "uuid": "e315c902-e079-422c-8f8a-d40516e462e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ugexq7v3v8BDazEGxvB2Vi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 24707,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 24707,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
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

_source line 28 · 2026-05-20T05:42:42.990Z_

<details><summary>↩ Tool result · `toolu_01F2s83uw9YkvmZcVqGHG1c1`</summary>

```text
Web search results for query: "pessimistic reward model uncertainty step level RL LLM reasoning "Caution" "inference time pessimism" 2025 2026"

Links: [{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM ...","url":"https://openreview.net/pdf?id=TDfrN1TbGH"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/pdf/2604.04648"},{"title":"Improving reasoning at inference time via uncertainty minimisation","url":"https://arxiv.org/pdf/2603.07159"},{"title":"On Designing Effective RL Reward at Training Time for LLM Reasoning","url":"https://arxiv.org/pdf/2410.15115"},{"title":"Beyond Correctness: Confidence-Aware Reward Modeling for Enhancing Large Language Model Reasoning","url":"https://arxiv.org/pdf/2511.07483"},{"title":"Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping for Deeper Reasoning","url":"https://arxiv.org/pdf/2510.10649"}]

Based on the search results, I found several highly relevant papers from 2025-2026 addressing your query:

## Key Findings:

**1. Step-Level Pessimism in LLM Reasoning (February 2026)**

Early-step bias causes labels for initial steps to be less accurate due to higher uncertainty, leading to step-level value estimates that can be overly pessimistic, resulting in the premature discarding of potentially correct reasoning paths during search at inference time.

**2. Caution-Based Pessimism Approach (2026)**

A paper titled "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism" directly addresses inference-time pessimism. The approach penalizes out-of-distribution responses by subtracting per-response uncertainty estimates from the scores assigned by the reward model, then selecting the response with the highest pessimistic score.

**3. Pessimistic Reward Models in RLHF (2025)**

There is also work on "Learning a Pessimistic Reward Model in RLHF" that discusses pessimism approaches in policy optimization.

**4. Uncertainty-Aware Inference-Time Scaling (2025)**

Recent work has focused on inference-time scaling, allocating additional computation during generation rather than training.

The search results reveal an active research area exploring how pessimism at different levels (step-level, distribution-level, and response-level) can improve LLM reasoning during inference while mitigating issues like reward hacking and over-optimistic evaluations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e315c902-e079-422c-8f8a-d40516e462e3",
  "isSidechain": false,
  "promptId": "af403a09-8d24-4670-ac94-635b17ecc710",
  "type": "user",
  "uuid": "38a4012d-c365-43b3-81a6-0ac3c8085ab8",
  "toolUseResult": {
    "query": "pessimistic reward model uncertainty step level RL LLM reasoning \"Caution\" \"inference time pessimism\" 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015Z3dWH3e8fFctMKnRSmHQz",
        "content": [
          {
            "title": "Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation",
            "url": "https://arxiv.org/html/2602.09305v1"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/pdf/2505.20556"
          },
          {
            "title": "Reward Modeling for Reinforcement Learning-Based LLM ...",
            "url": "https://openreview.net/pdf?id=TDfrN1TbGH"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism",
            "url": "https://arxiv.org/pdf/2604.04648"
          },
          {
            "title": "Improving reasoning at inference time via uncertainty minimisation",
            "url": "https://arxiv.org/pdf/2603.07159"
          },
          {
            "title": "On Designing Effective RL Reward at Training Time for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2410.15115"
          },
          {
            "title": "Beyond Correctness: Confidence-Aware Reward Modeling for Enhancing Large Language Model Reasoning",
            "url": "https://arxiv.org/pdf/2511.07483"
          },
          {
            "title": "Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping for Deeper Reasoning",
            "url": "https://arxiv.org/pdf/2510.10649"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers from 2025-2026 addressing your query:\n\n## Key Findings:\n\n**1. Step-Level Pessimism in LLM Reasoning (February 2026)**\n\nEarly-step bias causes labels for initial steps to be less accurate due to higher uncertainty, leading to step-level value estimates that can be overly pessimistic, resulting in the premature discarding of potentially correct reasoning paths during search at inference time.\n\n**2. Caution-Based Pessimism Approach (2026)**\n\nA paper titled \"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism\" directly addresses inference-time pessimism. The approach penalizes out-of-distribution responses by subtracting per-response uncertainty estimates from the scores assigned by the reward model, then selecting the response with the highest pessimistic score.\n\n**3. Pessimistic Reward Models in RLHF (2025)**\n\nThere is also work on \"Learning a Pessimistic Reward Model in RLHF\" that discusses pessimism approaches in policy optimization.\n\n**4. Uncertainty-Aware Inference-Time Scaling (2025)**\n\nRecent work has focused on inference-time scaling, allocating additional computation during generation rather than training.\n\nThe search results reveal an active research area exploring how pessimism at different levels (step-level, distribution-level, and response-level) can improve LLM reasoning during inference while mitigating issues like reward hacking and over-optimistic evaluations."
    ],
    "durationSeconds": 7.020778917999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e315c902-e079-422c-8f8a-d40516e462e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T05:42:42.993Z_

```json
{
  "parentUuid": "38a4012d-c365-43b3-81a6-0ac3c8085ab8",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1df7f310-98c2-4c7c-8a1b-1fbb089165e0",
  "timestamp": "2026-05-20T05:42:42.993Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-20T05:42:49.193Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Un85BcVga5bnVK6QGXt5BZ`</summary>

```json
{
  "query": "causal reward adjustment sparse autoencoder PRM backdoor correction reward hacking arXiv 2508.04216"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1df7f310-98c2-4c7c-8a1b-1fbb089165e0",
  "isSidechain": false,
  "requestId": "req_011CbDHdDh9FTn59kgq3Nkhz",
  "type": "assistant",
  "uuid": "d79cbf49-ecef-4843-8c0a-ddef394bd81f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxqcjmYndCRbjyWgFTSzny",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 959,
      "cache_read_input_tokens": 25436,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 25436,
          "cache_creation_input_tokens": 959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 959
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

_source line 31 · 2026-05-20T05:42:54.772Z_

<details><summary>↩ Tool result · `toolu_01Un85BcVga5bnVK6QGXt5BZ`</summary>

```text
Web search results for query: "causal reward adjustment sparse autoencoder PRM backdoor correction reward hacking arXiv 2508.04216"

Links: [{"title":"[2508.04216] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/abs/2508.04216"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/html/2508.04216v1"},{"title":"[PDF] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Causal-Reward-Adjustment:-Mitigating-Reward-Hacking-Song-Song/d98cf088a2ca29326352d4499c11d32b25e75bfa"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in ...","url":"https://arxiv.org/pdf/2508.04216"},{"title":"IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/pdf/2602.19416"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment","url":"https://arxiv.org/pdf/2501.09620"}]

Based on the search results, I found the paper you were looking for. Here's what the research is about:

The paper addresses external reasoning systems that combine language models with process reward models (PRMs) to select high-quality reasoning paths for complex tasks such as mathematical problem solving, but these systems are prone to reward hacking, where high-scoring but logically incorrect paths are assigned high scores by the PRMs, leading to incorrect answers.

From a causal inference perspective, the authors attribute this phenomenon primarily to the presence of confounding semantic features.

To address this, they propose Causal Reward Adjustment (CRA), a method that mitigates reward hacking by estimating the true reward of a reasoning path. CRA trains sparse autoencoders on the PRM's internal activations to recover interpretable features, then corrects confounding by using backdoor adjustment.

Experiments on math solving datasets demonstrate that CRA mitigates reward hacking and improves final accuracy, without modifying the policy model or retraining PRM.

The paper (arXiv 2508.04216) was published on August 6, 2025, and is currently under review.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d79cbf49-ecef-4843-8c0a-ddef394bd81f",
  "isSidechain": false,
  "promptId": "af403a09-8d24-4670-ac94-635b17ecc710",
  "type": "user",
  "uuid": "dd42e830-2c11-4f04-bd8a-564cb1362e78",
  "toolUseResult": {
    "query": "causal reward adjustment sparse autoencoder PRM backdoor correction reward hacking arXiv 2508.04216",
    "results": [
      {
        "tool_use_id": "srvtoolu_013tc9NSedYvFKJKdTV3Ledv",
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
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in ...",
            "url": "https://arxiv.org/pdf/2508.04216"
          },
          {
            "title": "IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking",
            "url": "https://arxiv.org/pdf/2602.19416"
          },
          {
            "title": "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/html/2604.13602v1"
          },
          {
            "title": "Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment",
            "url": "https://arxiv.org/pdf/2501.09620"
          }
        ]
      },
      "Based on the search results, I found the paper you were looking for. Here's what the research is about:\n\nThe paper addresses external reasoning systems that combine language models with process reward models (PRMs) to select high-quality reasoning paths for complex tasks such as mathematical problem solving, but these systems are prone to reward hacking, where high-scoring but logically incorrect paths are assigned high scores by the PRMs, leading to incorrect answers.\n\nFrom a causal inference perspective, the authors attribute this phenomenon primarily to the presence of confounding semantic features.\n\nTo address this, they propose Causal Reward Adjustment (CRA), a method that mitigates reward hacking by estimating the true reward of a reasoning path. CRA trains sparse autoencoders on the PRM's internal activations to recover interpretable features, then corrects confounding by using backdoor adjustment.\n\nExperiments on math solving datasets demonstrate that CRA mitigates reward hacking and improves final accuracy, without modifying the policy model or retraining PRM.\n\nThe paper (arXiv 2508.04216) was published on August 6, 2025, and is currently under review."
    ],
    "durationSeconds": 5.574573290999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d79cbf49-ecef-4843-8c0a-ddef394bd81f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-20T05:42:57.365Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture of the landscape. Let me also check one more thing - whether anyone has already bridged the calibration-hackability connection that this proposal claims is novel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd42e830-2c11-4f04-bd8a-564cb1362e78",
  "isSidechain": false,
  "requestId": "req_011CbDHe64nG8zfXy9ALJgAm",
  "type": "assistant",
  "uuid": "24a0ddde-0694-41a4-ae1c-19f07d578470",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVL86hGDA8rtSEaXiW7Gef",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 787,
      "cache_read_input_tokens": 26395,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 787,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 26395,
          "cache_creation_input_tokens": 787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 787
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

_source line 33 · 2026-05-20T05:42:58.340Z_

Let me do one more targeted search to check if anyone has already connected calibration to hackability directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24a0ddde-0694-41a4-ae1c-19f07d578470",
  "isSidechain": false,
  "requestId": "req_011CbDHe64nG8zfXy9ALJgAm",
  "type": "assistant",
  "uuid": "18642794-4b86-4b15-9c8c-0cdb5f3567fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVL86hGDA8rtSEaXiW7Gef",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 787,
      "cache_read_input_tokens": 26395,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 787,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 26395,
          "cache_creation_input_tokens": 787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 787
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

_source line 34 · 2026-05-20T05:42:58.949Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SKGQoZU2W4GnKZTvTXZDkd`</summary>

```json
{
  "query": "\"calibration quality\" determines \"reward hacking\" resistance PRM causal 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18642794-4b86-4b15-9c8c-0cdb5f3567fc",
  "isSidechain": false,
  "requestId": "req_011CbDHe64nG8zfXy9ALJgAm",
  "type": "assistant",
  "uuid": "482a4110-0e7d-484f-9f0e-3e98aba78122",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVL86hGDA8rtSEaXiW7Gef",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 787,
      "cache_read_input_tokens": 26395,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 787,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 26395,
          "cache_creation_input_tokens": 787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 787
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "482a4110-0e7d-484f-9f0e-3e98aba78122",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration quality and reward hacking resistance analysis",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c"
}
```

---

### Tool result

_source line 37 · 2026-05-20T05:43:05.696Z_

<details><summary>↩ Tool result · `toolu_01SKGQoZU2W4GnKZTvTXZDkd`</summary>

```text
Web search results for query: ""calibration quality" determines "reward hacking" resistance PRM causal 2026"

Links: [{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+(PRMs)"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/html/2508.04216v1"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM ...","url":"https://openreview.net/pdf?id=TDfrN1TbGH"},{"title":"[2508.04216] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/abs/2508.04216"},{"title":"CHARM: Calibrating Reward Models With Chatbot Arena Scores","url":"https://arxiv.org/pdf/2504.10045"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in ...","url":"https://arxiv.org/pdf/2508.04216"}]

Based on the search results, I found relevant information about the relationship between calibration quality and reward hacking resistance in Process Reward Models (PRMs) with a causal perspective:

Recent research on Process Reward Models shows that calibration is crucial for enabling effective scaling, and identifies reward hacking as a key issue with PRMs that limits their successful application in reinforcement fine-tuning. The main cause of PRM-induced reward hacking is the canonical summation-form credit assignment in reinforcement learning, which induces language models to hack steps with high rewards.

From a causal perspective, the phenomenon is attributed primarily to the presence of confounding semantic features, and approaches like Causal Reward Adjustment (CRA) mitigate reward hacking by estimating the true reward of a reasoning path.

Additionally, one approach trains a PRM that grounds step-wise judgments in interpretable principles rather than ad-hoc heuristics, with reward being calibrated to unify the scales of sparse outcome and dense process rewards before advantage estimation.

The search results demonstrate that calibration quality is indeed an important factor in addressing reward hacking resistance in PRMs, particularly when combined with causal inference methods to correct for confounding factors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "482a4110-0e7d-484f-9f0e-3e98aba78122",
  "isSidechain": false,
  "promptId": "af403a09-8d24-4670-ac94-635b17ecc710",
  "type": "user",
  "uuid": "8fd474eb-e30f-405b-9696-582e67c48964",
  "toolUseResult": {
    "query": "\"calibration quality\" determines \"reward hacking\" resistance PRM causal 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016DV9H8gYhGyGkaFXCzrdQd",
        "content": [
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Process+Reward+Models+(PRMs)"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/html/2508.04216v1"
          },
          {
            "title": "Reward Modeling for Reinforcement Learning-Based LLM ...",
            "url": "https://openreview.net/pdf?id=TDfrN1TbGH"
          },
          {
            "title": "[2508.04216] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/abs/2508.04216"
          },
          {
            "title": "CHARM: Calibrating Reward Models With Chatbot Arena Scores",
            "url": "https://arxiv.org/pdf/2504.10045"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/pdf/2604.02986"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in ...",
            "url": "https://arxiv.org/pdf/2508.04216"
          }
        ]
      },
      "Based on the search results, I found relevant information about the relationship between calibration quality and reward hacking resistance in Process Reward Models (PRMs) with a causal perspective:\n\nRecent research on Process Reward Models shows that calibration is crucial for enabling effective scaling, and identifies reward hacking as a key issue with PRMs that limits their successful application in reinforcement fine-tuning. The main cause of PRM-induced reward hacking is the canonical summation-form credit assignment in reinforcement learning, which induces language models to hack steps with high rewards.\n\nFrom a causal perspective, the phenomenon is attributed primarily to the presence of confounding semantic features, and approaches like Causal Reward Adjustment (CRA) mitigate reward hacking by estimating the true reward of a reasoning path.\n\nAdditionally, one approach trains a PRM that grounds step-wise judgments in interpretable principles rather than ad-hoc heuristics, with reward being calibrated to unify the scales of sparse outcome and dense process rewards before advantage estimation.\n\nThe search results demonstrate that calibration quality is indeed an important factor in addressing reward hacking resistance in PRMs, particularly when combined with causal inference methods to correct for confounding factors."
    ],
    "durationSeconds": 6.742044989000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "482a4110-0e7d-484f-9f0e-3e98aba78122",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T05:43:08.136Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018BdXbdanv8oHesRVMGQZP5`</summary>

```json
{
  "query": "pessimistic reward RLHF step-level uncertainty-penalized reward RL training LLM 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fd474eb-e30f-405b-9696-582e67c48964",
  "isSidechain": false,
  "requestId": "req_011CbDHetnAACat6cJ4doDyr",
  "type": "assistant",
  "uuid": "9e44f87e-bb30-493f-8fe8-7ddb68f94906",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XPWB111uHP1bCsFUwVmRU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 824,
      "cache_read_input_tokens": 27182,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 824,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 27182,
          "cache_creation_input_tokens": 824,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 824
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

_source line 39 · 2026-05-20T05:43:14.725Z_

<details><summary>↩ Tool result · `toolu_018BdXbdanv8oHesRVMGQZP5`</summary>

```text
Web search results for query: "pessimistic reward RLHF step-level uncertainty-penalized reward RL training LLM 2025 2026 arXiv"

Links: [{"title":"Uncertainty-Penalized Direct Preference Optimization","url":"https://arxiv.org/html/2410.20187"},{"title":"Reward-Robust RLHF in LLMs","url":"https://arxiv.org/pdf/2409.15360"},{"title":"Uncertainty-Penalized Reinforcement Learning from Human Feedback with Diverse Reward LoRA Ensembles","url":"https://arxiv.org/html/2401.00243"},{"title":"Learning from Failures: Understanding LLM Alignment through Failure-Aware Inverse RL","url":"https://arxiv.org/html/2510.06092v1"},{"title":"Uncertainty-Penalized Reinforcement Learning from Human Feedback with   Diverse Reward LoRA Ensembles","url":"https://arxiv.org/pdf/2401.00243"},{"title":"Uncertainty Quantification for Large Language Model Reward Learning under Heterogeneous Human Feedback","url":"https://arxiv.org/html/2512.03208"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"[2505.20556] Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/abs/2505.20556"}]

I found several relevant research papers on pessimistic reward models, uncertainty-penalized RLHF, and step-level reward training for LLMs from recent arxiv submissions in 2025-2026:

## Key Findings:

**Pessimistic Reward Models in RLHF:**
A recent paper titled "Learning a Pessimistic Reward Model in RLHF" (arXiv 2505.20556, May 2025) demonstrates that one can learn high-quality policies on pessimistic rewards without using any regularization, tested on the TL;DR summarization dataset.

**Uncertainty-Penalized Approaches:**
One notable work introduces uncertainty penalization schemes for Direct Preference Optimization (DPO) inspired by pessimistic offline RL to address DPO's overfitting problem. Another paper proposes uncertainty-penalized RLHF (UP-RLHF), which incorporates uncertainty regularization during RL-finetuning.

**Recent Work on Pessimistic Policies (2025):**
PET (Xu et al., 2025) trains pessimistic reward models to mitigate reward hacking. Recent works on pessimistic policies for RLHF leverage finite-sample lower bounds, with some approaches using asymptotic lower bounds derived from distributional guarantees.

**Step-Level and Uncertainty Quantification:**
Uncertainty quantification methods have been proposed to assess the reliability of reward models to avoid over-optimization.

These papers represent the cutting edge of research addressing reward hacking and overoptimization in LLM alignment through pessimistic and uncertainty-aware approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e44f87e-bb30-493f-8fe8-7ddb68f94906",
  "isSidechain": false,
  "promptId": "af403a09-8d24-4670-ac94-635b17ecc710",
  "type": "user",
  "uuid": "7e538dbe-fd1e-4c18-8fcd-aea5fb65785e",
  "toolUseResult": {
    "query": "pessimistic reward RLHF step-level uncertainty-penalized reward RL training LLM 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_013qRCieyFBYsXad29yc8sDi",
        "content": [
          {
            "title": "Uncertainty-Penalized Direct Preference Optimization",
            "url": "https://arxiv.org/html/2410.20187"
          },
          {
            "title": "Reward-Robust RLHF in LLMs",
            "url": "https://arxiv.org/pdf/2409.15360"
          },
          {
            "title": "Uncertainty-Penalized Reinforcement Learning from Human Feedback with Diverse Reward LoRA Ensembles",
            "url": "https://arxiv.org/html/2401.00243"
          },
          {
            "title": "Learning from Failures: Understanding LLM Alignment through Failure-Aware Inverse RL",
            "url": "https://arxiv.org/html/2510.06092v1"
          },
          {
            "title": "Uncertainty-Penalized Reinforcement Learning from Human Feedback with   Diverse Reward LoRA Ensembles",
            "url": "https://arxiv.org/pdf/2401.00243"
          },
          {
            "title": "Uncertainty Quantification for Large Language Model Reward Learning under Heterogeneous Human Feedback",
            "url": "https://arxiv.org/html/2512.03208"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/pdf/2505.20556"
          },
          {
            "title": "[2505.20556] Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/abs/2505.20556"
          }
        ]
      },
      "I found several relevant research papers on pessimistic reward models, uncertainty-penalized RLHF, and step-level reward training for LLMs from recent arxiv submissions in 2025-2026:\n\n## Key Findings:\n\n**Pessimistic Reward Models in RLHF:**\nA recent paper titled \"Learning a Pessimistic Reward Model in RLHF\" (arXiv 2505.20556, May 2025) demonstrates that one can learn high-quality policies on pessimistic rewards without using any regularization, tested on the TL;DR summarization dataset.\n\n**Uncertainty-Penalized Approaches:**\nOne notable work introduces uncertainty penalization schemes for Direct Preference Optimization (DPO) inspired by pessimistic offline RL to address DPO's overfitting problem. Another paper proposes uncertainty-penalized RLHF (UP-RLHF), which incorporates uncertainty regularization during RL-finetuning.\n\n**Recent Work on Pessimistic Policies (2025):**\nPET (Xu et al., 2025) trains pessimistic reward models to mitigate reward hacking. Recent works on pessimistic policies for RLHF leverage finite-sample lower bounds, with some approaches using asymptotic lower bounds derived from distributional guarantees.\n\n**Step-Level and Uncertainty Quantification:**\nUncertainty quantification methods have been proposed to assess the reliability of reward models to avoid over-optimization.\n\nThese papers represent the cutting edge of research addressing reward hacking and overoptimization in LLM alignment through pessimistic and uncertainty-aware approaches."
    ],
    "durationSeconds": 6.5850645640000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9e44f87e-bb30-493f-8fe8-7ddb68f94906",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-20T05:44:30.674Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of the landscape. Let me synthesize my findings and evaluate this proposal.

## Summary of Key Findings from Research

### Thread 1: PRM Calibration
- **Park et al. (arXiv:2506.09338, NeurIPS 2025)**: PRMs systematically overestimate success probabilities, proposes quantile regression calibration. ✅ Exists
- **Distributional PRMs (arXiv:2605.06785, May 2026)**: Uses conditional optimal transport for calibrated predictions. ✅ Exists, very recent


### Thread 2: PRM Hackability
- **Tiwari et al. (arXiv:2603.06621, March 2026)**: PRMs are catastrophically hackable — near-perfect PRM rewards with <4% actual accuracy. ✅ Exists
- **APRM (arXiv:2511.22888)**: Adversarial training for PRM robustness, +3.4pp improvement. ✅ Exists

### Thread 3: Reward Hacking Defenses
- **Ackermann et al. (arXiv:2602.18037)**: Gradient regularization, connects reward surface flatness to accuracy retention. ✅ Exists
- **Caution (arXiv:2604.04648)**: Pessimism for BoN, uses prediction error. ✅ Exists
- **Causal Reward Adjustment (arXiv:2508.04216)**: Uses sparse autoencoders and causal inference on PRM activations. ✅ Exists
- **PET / Pessimistic Reward Model (arXiv:2505.20556)**: Learns pessimistic reward model. ✅ Exists
- **Uncertainty-Penalized RLHF**: Multiple papers on using uncertainty as penalty in RLHF. ✅ Exists

### Key Assessment

I'm now checking the core claim about whether PRM calibration and hackability operate in completely separate research threads with no cross-citation. My searches suggest there's limited explicit connection between these areas, but I haven't yet found a paper that directly bridges them.

That said, the Causal Reward Adjustment work does tackle reward hacking through a causal lens, though it focuses on confounding features rather than calibration quality specifically. And the broader literature on uncertainty and pessimism for mitigating reward hacking is well-established across multiple papers. The specific contribution of this proposal would be combining step-level analysis with calibrated probabilities rather than heuristic proxies, and making the approach adaptive based on how well-calibrated the PRM actually is.

Now I'm checking whether a simpler alternative could work just as well—for instance, whether just applying post-hoc calibration like temperature scaling to existing PRMs would achieve similar results without the full causal framework.

The CGSP formula itself is essentially a pessimistic reward adjusted by calibration-weighted uncertainty, which is a fairly natural extension of existing pessimistic methods to the step level. The real question is whether ensemble disagreement at the step level alone could match what CGSP achieves, since that wouldn't require the calibration infrastructure at all. If it does, then CGSP's incremental value becomes questionable.

I should also verify the core logical chain here—that poorly calibrated PRMs actually lead to increased hackability, and that better calibration genuinely reduces it.  The critical untested assumption is whether calibration actually improves resistance to hacking. It's plausible, but there's a real possibility that post-hoc calibration methods like temperature scaling only rescale the output logits without changing the underlying reward landscape that gradient attacks exploit. The exploitable features in the representation space might remain unchanged, or the causal direction could be flipped entirely—maybe more robust PRMs just happen to be better calibrated, rather than calibration being what makes them robust.

This is actually a crucial insight: if gradient attacks operate in input space and post-hoc calibration only modifies the output mapping, then calibration might have no effect on hackability at all. Temperature scaling changes gradient magnitudes but doesn't alter the relative ranking of inputs, so an adversarial attack would still find the same problematic inputs—just with different absolute reward values. The "causal isolation" experiment could reveal that post-hoc calibration provides no defense against gradient-based attacks, which would fundamentally undermine the thesis.

But thinking through this more carefully, the picture gets more complex. Temperature scaling does modify the gradient flow (∂p/∂z), which could affect how easily gradient attacks succeed. For best-of-N style overoptimization, calibration changes which samples get selected. For RL training, it directly modifies the reward signal. So the effect depends heavily on the attack type, and the proposal's experimental design does account for this by testing different attack vectors.

Looking at the novelty claims, the expanded correlation study is primarily measurement work. The causal isolation experiments using post-hoc calibration versus fine-tuning with CKA controls is the most methodologically novel piece—that's a clever experimental design. The step-level Hessian spectral analysis extends prior work incrementally. CGSP itself combines calibrated uncertainty with step-level pessimism and a drift detector, which is relatively straightforward but gains novelty from the calibration connection.

What stands out is that nobody's really bridged calibration and hackability before—that's genuinely novel territory. CGSP as a method is an incremental refinement of existing pessimistic approaches, but the causal isolation methodology is well-executed. The research question itself matters: whether calibration affects robustness would either guide the community toward calibration as a defense or reveal it doesn't help, both outcomes being informative. If CGSP proves effective, it could offer a practical defense mechanism.

The strengths are solid—genuinely connecting two research threads with no prior precedent, strong causal isolation design, practical applicability, comprehensive experiments across multiple attack types, and well-timed positioning. But there are real risks: the core claim might not hold, especially against gradient attacks; the CGSP formula is fairly simple and incremental; post-hoc calibration might yield null results if it doesn't alter the underlying geometry; the paper's scope across four components could feel scattered; and if the central claim doesn't pan out, the whole contribution weakens significantly.

The biggest vulnerability is that the causal study could show calibration has minimal impact on hackability, or that any effect comes entirely from representation shifts rather than calibration itself—which would undermine CGSP's foundation. Even a negative result would be informative, but those are harder to get published. Looking at the probability, the novelty of bridging these areas is medium-to-strong despite CGSP being somewhat incremental, and the significance is solid given the practical implications and important research question. The related work coverage is comprehensive. For the target venues listed—ICLR, AAAI, and AISTATS 2027—I'd estimate this sits somewhere in the 30-40% acceptance range, though the exact odds depend heavily on whether the core empirical claim holds up.

Stepping back from venue considerations and focusing purely on idea quality, the work does bridge two distinct research threads with a solid causal methodology, but CGSP itself feels incremental and the core hypothesis carries real risk. The proposal tries to pack quite a bit together. I'm settling on around 28-38%, with a midpoint near 33%—the idea has genuine merit, but it's not at that surprising level where researchers would be shocked by the results. If calibration does help with hackability, most would find it intuitive rather than unexpected. The CGSP formula itself is a natural pessimistic lower confidence bound construction that most ML researchers would recognize as a straightforward approach.

But I should dig deeper into what would actually move a reviewer. The central question is whether the causal link between calibration and hackability resistance would strike reviewers as novel or just plausible. Most would likely say "yeah, better-calibrated models should be more robust"—which suggests the conceptual contribution is limited, even if the causal isolation methodology is technically sound. There's also a real concern that simpler alternatives, like using ensemble disagreement at the step level without any calibration infrastructure, might achieve similar defensive effects, which would undermine the necessity of the elaborate machinery being proposed.

I'm landing on 25-35%, midpoint around 30%—solid execution and good measurement work, but the core idea isn't surprising enough to push it higher. first paper to bridge PRM calibration and hackability — important contribution"
- "The causal isolation experiments are well-designed and add methodological rigor"
- "CGSP is a practical, principled defense"

**Negative reviewer:**
- "The core hypothesis (calibration → robustness) is intuitive and not surprising"
- "CGSP is essentially LCB (lower confidence bound) applied to step rewards — well-known in the pessimistic RL literature"
- "The paper tries to do too much — four components feel like four separate papers glued together"
- "If post-hoc calibration doesn't change the reward landscape topology, the causal isolation experiments may show null results"

I think the balance is:
- Novelty: Medium — the bridge is novel, but the methods are incremental
- Significance: Medium to Medium-Strong — important question
- Related Work: Strong — thorough

Probability: 27

I'm noticing some gaps in the related work coverage though. There's a causal perspective paper on reward hacking in PRMs using sparse autoencoders that occupies similar conceptual ground, and a pessimistic reward modeling paper in RLHF that's quite relevant — neither gets mentioned in the proposal. These omissions weaken the positioning. Let me finalize my assessment with these considerations in mind.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e538dbe-fd1e-4c18-8fcd-aea5fb65785e",
  "isSidechain": false,
  "requestId": "req_011CbDHfZPNBxfbpHQ1nF3qY",
  "type": "assistant",
  "uuid": "de6c349a-5bb6-403c-82b5-7c0ee71f9e28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MQf7izTJtfJcC1hReRdHw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 28006,
      "output_tokens": 6911,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6911,
          "cache_read_input_tokens": 28006,
          "cache_creation_input_tokens": 860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 860
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

_source line 41 · 2026-05-20T05:45:51.180Z_

Now I have sufficient research to make an informed assessment. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:

1. **Tiwari et al. "Reward Under Attack" (arXiv:2603.06621, March 2026)**: 直接竞争论文。证明 PRMs 在梯度攻击下 reward 可膨胀 4×，RL 训练下实现 >0.9 PRM reward 但 <4% 真实准确率，43% reward 增益来自 stylistic shortcuts。提出了 PRM-BiasBench 但**未提出基于 calibration 的防御**。本 proposal 的攻击端实验设计直接基于此工作。

2. **Park et al. "Know What You Don't Know" (arXiv:2506.09338, NeurIPS 2025)**: PRM calibration 的奠基工作。证明 PRMs 系统性高估 success probability（尤其在难题上），提出 quantile regression calibration + Instance-Adaptive Scaling (IAS)。**未测试 robustness**——本 proposal 正好填补这个空白。

3. **Distributional PRMs (arXiv:2605.06785, May 2026)**: 用 conditional optimal transport 实现 calibrated monotone quantile function，在 MATH-500/AIME 上改善 BoN。同样**未测试 robustness**。极其新鲜（3 周前），进一步确认 calibration 线程活跃但与 hackability 线程隔离。

4. **Ackermann et al. "Gradient Regularization" (arXiv:2602.18037, Feb 2026)**: 证明 reward surface flatness 与 accuracy retention 相关，提出 gradient regularization 防御。但**仅限 outcome-level single-scalar RM**，从未处理 step-level PRM geometry。proposal 正确识别了这一局限。

5. **APRM "Adversarial Training for PRMs" (arXiv:2511.22888, Nov 2025)**: 通过对抗训练提升 PRM 鲁棒性 +3.4pp。是防御端的直接 baseline，但**不涉及 calibration**。

6. **"From Curiosity to Caution" (arXiv:2604.04648, April 2026)**: 使用 prediction error 作为 pessimism proxy 在 BoN 中防御 reward hacking。**Outcome-level、非 calibrated**——proposal 的 CGSP 直接对标此工作。

7. **Causal Reward Adjustment (arXiv:2508.04216, Aug 2025)**: 用 sparse autoencoders + structural causal model 对 PRM activations 做 backdoor adjustment 来纠正 reward hacking。虽然也取 causal 视角，但关注的是 confounding features 而非 calibration quality。**proposal 未引用此工作——这是一个 related work 缺口**。

8. **"Learning a Pessimistic Reward Model in RLHF" (arXiv:2505.20556, May 2025)**: 学习 pessimistic reward 函数直接用于 policy optimization，无需 KL regularization。**proposal 也未引用此工作，是另一个 related work 缺口**。

9. **Uncertainty-Penalized RLHF (arXiv:2401.00243, 2024)**: 使用 ensemble LoRA 的 disagreement 作为 uncertainty penalty。公式形式与 CGSP 类似（r - β·uncertainty），但不是 step-level 也不是 calibration-grounded。

- **调研总结**: PRM calibration（Park 2025, Distributional PRM 2026）和 PRM hackability（Tiwari 2026, APRM 2025）确实是两个高度活跃但几乎完全隔离的研究线程——我的搜索未发现直接连接两者的论文。Causal Reward Adjustment（2508.04216）是最接近的竞争者，但它用 SAE+causal graph 而非 calibration quality 作为切入点。pessimistic reward 领域已有大量 outcome-level 工作，但 step-level + calibration-grounded 的组合确属空白。proposal 对两个主线程的 gap identification 是准确的，但遗漏了 CRA 和 pessimistic RM 两项重要相关工作。

【Trivial Alternative 检验】:

存在两个值得认真考虑的 trivial alternative：

(1) **Ensemble step-level disagreement 作为 pessimism proxy**：不需要任何 calibration 基础设施，直接用 K 个 PRM 的 step-level disagreement（std）作为 σ_t 替代物，公式变为 r̃_t = μ_t − α·σ_t（ensemble 版），成本更低且无需 calibration fitting 的 200 H100-hrs。如果 ensemble disagreement 在防御效果上与 CGSP 可比，则 calibration 的"精细化"增量价值有限。

(2) **直接对 PRM 做 temperature scaling + BoN/RL**：不需要 CGSP 的复杂公式，仅用 post-hoc calibration 调整 PRM 输出，然后正常使用。如果这就能减少 reward hacking，则不需要 CGSP 的 per-step pessimism 机制。

**增量价值分析**：CGSP 相对于 trivial alternatives 的增量在于 (i) calibration quality c_t 的 per-step 自适应性——在 PRM 本身 well-calibrated 的区域不过度 pessimistic，(ii) Calibration Drift Detector 提供 real-time 分布偏移检测。这些增量是真实的但不算大。proposal 需要在实验中直接对比这些 trivial alternatives（特别是 ensemble disagreement 基线），否则审稿人会质疑。

【前提假设检验】:

核心逻辑链：**calibration quality → reward surface geometry change → hackability resistance**

关键未验证假设：

(1) **Post-hoc calibration 是否真的改变 reward landscape 的可利用性？** Temperature scaling 和 Platt scaling 只修改 logit→probability 的映射，不改变 representation space 中 reward peaks 的位置。对于在 representation/input space 中操作的 gradient attacks，post-hoc calibration 改变的是梯度幅度（∂p/∂z 变了），但不改变 reward surface 的拓扑结构。这意味着 Component B（causal isolation）的核心实验可能得到**零效应**——post-hoc calibration 对 gradient attack hackability 可能没有显著影响。这不是致命问题（negative result 也有价值），但如果 positive result 不出现，整个 causal thesis 的核心会被动摇。

(2) **Calibration quality 和 hackability resistance 之间的因果方向**。可能存在 confound：更"好"的 PRM（representation 更好）恰好同时表现出 better calibration 和 better robustness，但 calibration 不是 cause。proposal 的 matched representation change control (B3) 试图解决这个问题，但 CKA-matched auxiliary task 是否真能控制所有 confounding representation changes 是另一个未验证假设。

(3) **Step-level flatness compounding 假设**。proposal 假设 step-level Hessian flatness 会 compound across trajectory 影响 outcome-level hackability。这在数学上不一定成立——多个 flat step rewards 的组合不一定产生 flat outcome reward surface（非线性组合可以创造 sharp peaks）。

【3 维度打分】:

1. **Novelty: 中** — 
   Bridge 的 identification 是准确的且有真实 novelty：根据调研，PRM calibration（Park NeurIPS'25, Distributional PRM May'26）和 PRM hackability（Tiwari Mar'26）确实是两个零交叉引用的研究线程，没有现有论文建立 calibration→hackability 的因果联系。这是一个真实的 gap。然而：(a) CGSP 的公式 r̃_t = μ_t − α·σ_t/√c_t 本质上是 pessimistic RL 中经典的 LCB（Lower Confidence Bound）构造的 step-level 版本，技术上是 incremental extension，不是方法论创新；(b) 将 pessimism + uncertainty 用于 reward hacking defense 已有大量先例（Caution arXiv:2604.04648, PET arXiv:2505.20556, UP-RLHF arXiv:2401.00243），CGSP 的贡献在于 calibration-grounded 这一特征，增量真实但不大；(c) Causal Reward Adjustment（arXiv:2508.04216）已经从 causal 视角分析 PRM reward hacking，虽然切入点不同（confounding features vs. calibration），但占据了相似的 conceptual space。

2. **Significance: 中偏强** — 
   研究问题具有实际重要性：PRM 正在成为 LLM reasoning pipeline 的核心组件（test-time compute, RL training signals），理解其 calibration 与 robustness 的关系对整个领域有指导意义。如果 positive result 成立（calibration causally improves robustness），这将给出一条简单、可操作的建议（"calibrate your PRMs"）。CGSP 如果有效，是可以直接部署的实用工具。然而，核心发现如果 positive，审稿人更可能说 "this is intuitive — of course better calibrated models are harder to hack" 而非 "this is surprising"。calibration 改善 robustness 是多数研究者的先验直觉——proposal 验证了这个直觉但没有挑战它。

3. **Related Work: 中** — 
   对两个主线程（PRM calibration 和 PRM hackability）的覆盖全面且准确：Park et al., Distributional PRM, Tiwari et al., APRM, Ackermann et al. 等关键论文都已正确引用和描述。差异化定位清晰（vs. Ackermann 的 outcome-level 局限、vs. Caution 的 uncalibrated proxy、vs. ensemble methods 的 non-calibrated nature）。但存在两个重要遗漏：(a) Causal Reward Adjustment (arXiv:2508.04216) 同样从 causal 视角分析 PRM reward hacking，是最直接的 conceptual competitor，完全未被引用；(b) Pessimistic Reward Model (arXiv:2505.20556) 学习 pessimistic reward 无需 KL regularization，与 CGSP 的 pessimism 设计直接相关。这些遗漏会被审稿人发现。

【概率估计】: [25% - 35%] 中位 30%

【估计理由】: 
Novelty 维度是主要的概率约束因素。Gap identification（bridging calibration and hackability）是真实的且有 novelty delta，但 CGSP 作为方法贡献是 LCB 的 step-level calibration-weighted 变体，技术上 incremental。核心假设（calibration causally determines hackability）如果得到 positive 验证，审稿人的反应更可能是 "makes sense" 而非 "surprising"——这将 idea 锚定在 25-35% 区间（有实质内核、方向正确、novelty delta 真实，但核心发现 not surprising）。Significance 有一定上推力（实际可操作性强），但被 trivial alternative 威胁（ensemble disagreement 可能达到类似防御效果而不需 calibration 基础设施）部分抵消。Related work 的两处重要遗漏（CRA、Pessimistic RM）进一步压制上界。

【主要风险】:
1. **核心因果假设可能不成立或效应微弱**：Post-hoc calibration 不改变 reward surface 拓扑，对 gradient-based attacks 可能无显著防御效果。如果 Component B 的 causal isolation 实验显示 null effect，整个论文的 thesis 将失去支撑——而 negative result papers 在顶会的接收难度显著更高。
2. **Trivial alternative 威胁**：如果 ensemble step-level disagreement（无需 calibration）作为 pessimism proxy 在防御效果上与 CGSP 可比，则 CGSP 的 calibration-grounded 增量价值将被严重质疑。审稿人会问："why not just use ensemble disagreement instead of this elaborate calibration machinery?"
```

Sources:
- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)
- [Know What You Don't Know: Uncertainty Calibration of Process Reward Models](https://arxiv.org/abs/2506.09338)
- [Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport](https://arxiv.org/abs/2605.06785)
- [Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards](https://arxiv.org/abs/2602.18037)
- [Adversarial Training for Process Reward Models](https://arxiv.org/abs/2511.22888)
- [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/pdf/2604.04648)
- [Causal Reward Adjustment: Mitigating Reward Hacking via Backdoor Correction](https://arxiv.org/abs/2508.04216)
- [Learning a Pessimistic Reward Model in RLHF](https://arxiv.org/abs/2505.20556)
- [Uncertainty-Penalized RLHF with Diverse Reward LoRA Ensembles](https://arxiv.org/abs/2401.00243)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de6c349a-5bb6-403c-82b5-7c0ee71f9e28",
  "isSidechain": false,
  "requestId": "req_011CbDHfZPNBxfbpHQ1nF3qY",
  "type": "assistant",
  "uuid": "e1cd4db5-d8a4-46d0-9b67-cdaf449592e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014MQf7izTJtfJcC1hReRdHw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 28006,
      "output_tokens": 6911,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6911,
          "cache_read_input_tokens": 28006,
          "cache_creation_input_tokens": 860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 860
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "e1cd4db5-d8a4-46d0-9b67-cdaf449592e9",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration quality and reward hacking resistance analysis",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-L…",
  "leafUuid": "e1cd4db5-d8a4-46d0-9b67-cdaf449592e9",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration quality and reward hacking resistance analysis",
  "sessionId": "ecb60731-02e7-46e4-8411-219f7ddb854c"
}
```

---
