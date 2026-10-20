# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Calibration as a Shield: How PRM 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/e8828fd2-61a1-4417-b87e-354620af4528.jsonl`
- **Structured JSON:** [`a384d098cb44a22cb59a.json`](../../sessions/a3/a384d098cb44a22cb59a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:45:50.885Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:45:50.885Z",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Calibration as a Shield: How PRM Calibration Quality Causally Determines Reward Hacking Resistance, and a Step-Level Defense\n\n## Description\nWe present the first causally rigorous study connecting PRM calibration quality to adversarial exploitability, and propose Calibration-Gated Step-Level Pessimism (CGSP), a novel defense that transforms calibrated uncertainty into adaptive reward hacking resistance during RL training. Our work bridges two mature but isolated research threads (PRM calibration and PRM hackability) through four contributions. First, an expanded correlation study across 48 configurations (8 PRMs × 6 calibration methods) provides sufficient statistical power (n=48, detecting r≥0.29 at p<0.05) to establish whether calibration quality predicts hackability metrics under gradient attacks, RL-induced hacking (GRPO on AIME), and BoN overoptimization (MATH-500), stratified by problem difficulty. Second, causal isolation experiments separate calibration's true effect from representation change artifacts: we compare post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) that provably preserve model representations against fine-tuning-based methods, with CKA verification and matched-representation-change controls. Third, step-level Hessian spectral analysis goes beyond Ackermann et al.'s outcome-level gradient norm analysis (which applies only to single-scalar reward models) to reveal how calibration affects the multi-reward compositional geometry of PRMs — analyzing how step-level flatness compounds across trajectories. Fourth, CGSP replaces raw PRM rewards during RL training with r̃_t = μ_t − α·σ_t/√c_t, where calibrated uncertainty σ_t and calibration quality c_t adaptively modulate pessimism per-step — trusted when calibration is tight, pessimistic when uncertainty is high — with a Calibration Drift Detector that monitors ECE on current-policy rollouts to flag distribution-shift-induced reward hacking in real time. CGSP differs from existing defenses (Caution uses prediction error, PET uses global pessimism, ensemble methods are uncalibrated) by being step-level, calibration-grounded, and adaptive. We evaluate CGSP against 5 baselines (uncalibrated GRPO, APRM, Caution, ensemble-min, gradient regularization) on MATH-500 and AIME, measuring both reward-accuracy alignment and downstream task accuracy.\n\n## Core Problem\nPRM calibration research and PRM hackability research are entirely separate threads with zero cross-citation — but the deeper problem is that we lack both (a) causal evidence for whether calibration actually determines hackability (vs. being merely correlated), and (b) a principled, step-level defense mechanism that leverages calibrated uncertainty to prevent reward hacking during RL training. Existing ad-hoc defenses (adversarial training, gradient regularization, pessimistic BoN) operate at the outcome level without exploiting the unique step-level structure of PRMs.\n\n## Opportunity\nThree recent developments create a uniquely favorable moment. First, Distributional PRMs (arXiv:2605.06785, May 2026) achieve calibrated step-level uncertainty via conditional optimal transport but never test robustness. Second, Tiwari et al. (arXiv:2603.06621, March 2026) demonstrate that PRMs are catastrophically hackable — near-perfect PRM rewards with <4% actual accuracy — but propose no calibration-based defense. Third, the causal isolation toolkit is mature: post-hoc calibration methods (temperature scaling, Platt scaling, isotonic regression, conformal prediction) modify only the output mapping without changing model representations, enabling controlled experiments that separate calibration effects from representation effects. No existing paper bridges these threads. Ackermann et al.'s gradient regularization work (arXiv:2602.18037) operates exclusively on outcome-level reward models with single-scalar rewards, never touching step-level PRM geometry. The CoT Entropy paper (arXiv:2502.11250) named this connection as future work 16 months ago with no follow-up. The window for a definitive, causally rigorous study is open but narrowing.\n\n## Landscape\nTwo parallel research threads have developed with zero cross-citation. Thread 1 (PRM Calibration): Park et al. (arXiv:2506.09338, NeurIPS 2025) demonstrate PRMs systematically overestimate success probabilities on hard problems, proposing quantile regression calibration. Distributional PRMs (arXiv:2605.06785, May 2026) use conditional optimal transport for calibrated monotone quantile functions, improving BoN on MATH-500 and AIME. Neither paper tests robustness. Thread 2 (PRM Hackability): Tiwari et al. (arXiv:2603.06621) show gradient attacks inflate PRM rewards 4× and RL achieves near-perfect PRM rewards with <4% accuracy, with 43% of reward gains from stylistic shortcuts. APRM (arXiv:2511.22888) uses adversarial training for +3.4pp robustness. Thread 3 (Adjacent but distinct): Ackermann et al. (arXiv:2602.18037) prove reward surface flatness correlates with accuracy retention for outcome-level RMs, but work exclusively with single-scalar rewards, analyze only gradient norms (no Hessian spectra), and never consider step-level reward models. Their theoretical framework (Propositions 3.3-3.4) assumes a single reward function R(s,a) over complete responses — inapplicable to step-level PRM geometry where T coupled reward surfaces {R_1,...,R_T} interact compositionally. InferenceTimePessimism (arXiv:2506.19248) and Caution (arXiv:2604.04648) apply pessimism for BoN but use uncalibrated uncertainty proxies (prediction error, hedging), not calibrated probabilities. URM (arXiv:2410.00847) decomposes uncertainty into aleatoric/epistemic for outcome-level RMs but not PRMs. Bayesian reward models (arXiv:2402.13210) use Laplace approximation on LoRA weights. Conformal prediction has been applied to RLHF feedback alignment (arXiv:2601.17329) but never to PRM defense. No paper establishes a causal link between calibration quality and hackability, and no paper proposes using calibrated step-level PRM uncertainty as a defense during RL training.\n\n## Approach\nThe study has four components: (A) Expanded Correlation Study, (B) Causal Isolation Experiments, (C) Step-Level Mechanistic Analysis, and (D) Calibration-Gated Step-Level Pessimism (CGSP) defense.\n\n**Component A — Expanded Correlation Study (n≥24 configurations):** Apply 6 calibration methods across 2 tiers to 8 open-source PRMs. Tier 1 (post-hoc, representation-preserving): temperature scaling, Platt scaling, isotonic regression. Tier 2 (model-modifying): quantile regression fine-tuning, conditional optimal transport, Venn-Abers predictors. The 8 PRMs span discriminative (Qwen2.5-Math-PRM-7B, Qwen2.5-Math-PRM-72B, Skywork-o1-Open-PRM-7B, RLHFlow-Llama3.1-8B-PRM, Math-Shepherd-7B, OpenR-Math-psa-7B), generative (GenPRM-7B), and implicit (EurusPRM-Stage2) architectures. Each of the 48 PRM×calibration configurations is subjected to three attack tiers: (i) gradient-based reward inflation following Tiwari et al., (ii) RL-induced reward hacking via GRPO on AIME, and (iii) BoN overoptimization at N∈{1,4,16,64,256} on MATH-500. Compute rank correlations (Spearman ρ, Kendall τ) between calibration metrics (ECE, Brier score, quantile coverage, reliability diagram sharpness) and hackability metrics (reward-accuracy divergence, attack success rate, BoN degradation onset N*). Stratify analysis by problem difficulty (MATH levels 1-5, AMC vs. AIME) to test whether calibration is more protective on hard problems where PRMs are known to be overconfident.\n\n**Component B — Causal Isolation Experiments:** This is the methodological core addressing the reviewer's causation concern. Design: (B1) Post-hoc calibration control: Apply temperature scaling, Platt scaling, and isotonic regression — which provably modify only the output mapping, not internal representations — and measure hackability change. If hackability decreases under post-hoc calibration alone, this establishes that calibration per se (not representation change) causally affects hackability. (B2) Representation change verification: For fine-tuning-based calibration methods (quantile regression, COT), measure representation change at every transformer layer using Centered Kernel Alignment (CKA) between the base PRM and calibrated PRM. (B3) Matched representation change control: Fine-tune PRMs on an auxiliary task (e.g., next-token prediction on math text) that produces CKA-matched representation changes but does NOT improve calibration. If only calibration-improving fine-tuning reduces hackability (not the CKA-matched control), the causal role of calibration is confirmed. (B4) Conformal prediction as the cleanest test: Apply split-conformal prediction to PRM step scores, providing distribution-free coverage guarantees with zero model modification. Test whether conformal-calibrated PRMs resist hacking better than uncalibrated ones.\n\n**Component C — Step-Level Mechanistic Analysis (differentiating from Ackermann et al.):** Unlike Ackermann et al., who analyze only outcome-level gradient norms and max-perturbation sharpness, we perform Hessian spectral analysis at the step level — computing top-k eigenvalues and spectral density of the step-level reward Hessian ∂²R_t/∂h² (where h is the hidden representation at step t). Key questions: (i) Do calibrated PRMs have flatter step-level reward surfaces (lower top Hessian eigenvalue)? (ii) Does flatness vary by step position (early reasoning steps vs. final answer steps)? (iii) Do hackable reward peaks correspond to isolated large Hessian eigenvalues (sharp directions) that gradient attacks exploit? This extends Ackermann et al.'s framework from single-reward geometry to multi-reward compositional geometry: we analyze how step-level flatness/sharpness compounds across a T-step trajectory to determine outcome-level hackability.\n\n**Component D — Calibration-Gated Step-Level Pessimism (CGSP) Defense:** This transforms the paper from measurement to method. CGSP operates during RL training (GRPO/PPO) by replacing raw PRM step rewards with calibration-modulated rewards: r̃_t = μ_t − α · σ_t / √(c_t), where μ_t is the calibrated step reward mean, σ_t is the calibrated uncertainty (from quantile width or conformal interval), c_t is a calibration quality score (inverse ECE computed on a rolling buffer), and α is a pessimism strength hyperparameter. When calibration is high (small σ_t, high c_t), the reward is trusted; when calibration is low (large σ_t, low c_t), pessimism dominates. This differs from existing pessimism (Caution uses prediction error, PET uses global pessimistic fine-tuning, InferenceTimePessimism uses hedging) because CGSP is (i) step-level, (ii) grounded in calibrated probabilities rather than heuristic proxies, and (iii) adaptive — the pessimism automatically strengthens in distribution-shift regions where the PRM becomes miscalibrated. Additionally, we implement a Calibration Drift Detector: during RL training, periodically measure ECE on current-policy rollouts vs. the initial SFT-distribution calibration. When drift exceeds a threshold, flag those trajectory types as potentially hacked and apply reward clipping. This converts calibration from a static property into a dynamic training signal.\n\nBaseline comparisons for CGSP: (i) uncalibrated PRM + GRPO, (ii) APRM adversarial training, (iii) Caution/prediction-error pessimism, (iv) ensemble minimum (following Coste et al.), (v) KL-regularized GRPO, (vi) gradient regularization (Ackermann et al.).\n\nCodebase starting points: young-j-park/prm-calibration for calibration fitting, Tiwari et al.'s PRM-BiasBench for adversarial evaluation, vwxyzjn/open_instruct for GRPO training infrastructure.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '4200 H100-hrs (calibration fitting: 200, rollout generation: 600, gradient attacks: 1000, GRPO RL training: 1600 [including CGSP defense training], BoN evaluation: 400, Hessian spectral analysis: 200, causal isolation controls: 200)', 'timeline': '12-14 weeks', 'estimated_gpu_cost': '$10,500 at ~$2.50/H100-hr'}, 'human_in_loop': {'gpu_hours': '3600 H100-hrs (fewer failed iterations with AI-assisted debugging)', 'timeline': '10-12 weeks', 'claude_api_cost': '$400-700 (code generation, experiment analysis, paper drafting)', 'estimated_gpu_cost': '$9,000 at ~$2.50/H100-hr'}, 'auto_research': {'gpu_hours': '5200 H100-hrs (broader sweeps over α pessimism parameter, calibration drift thresholds, and ablations across all 48 configurations)', 'timeline': '7-9 weeks', 'claude_api_cost': '$1,500-2,000 (automated experiment orchestration, iterative analysis, full draft writing)', 'estimated_gpu_cost': '$13,000 at ~$2.50/H100-hr', 'speed_bottleneck': 'GRPO RL training wall-clock time (~18hrs per PRM×calibration×defense configuration on 4×H100); Hessian spectral analysis requires Lanczos iterations per step per problem; 72B PRM requires 4×H100 for inference'}}\n\n## Inspired By\nField guide gap: PRM overconfidence on OOD problems (Section 5.3 'when more compute hurts'); Untried combination: distributional PRM calibration + PRM hackability analysis; Pattern: connecting two mature but isolated research threads; Reviewer insight: pure measurement is insufficient — the key contribution should be a causal mechanism and a defense method; Methodological insight: post-hoc calibration methods that preserve representations enable clean causal isolation experiments impossible with fine-tuning-based calibration alone\n\n## Target Venues\n- ICLR 2027 (abstract Sep 19, paper Sep 24, 2026)\n- AAAI 2027 (abstract Jul 21, paper Jul 28, 2026)\n- AISTATS 2027 (paper Oct 10, 2026)\n\n## Key References\n- Know What You Don't Know: Uncertainty Calibration of Process Reward Models (arXiv:2506.09338, NeurIPS 2025)\n- Distributional Process Reward Models: Calibrated Prediction via Conditional Optimal Transport (arXiv:2605.06785, May 2026)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv:2603.06621, March 2026)\n- Gradient Regularization Prevents Reward Hacking in RLHF and Verifiable Rewards (arXiv:2602.18037, Feb 2026)\n- Adversarial Training for Process Reward Models (arXiv:2511.22888, Nov 2025)\n- From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism (arXiv:2604.04648, April 2026)\n- Inference-Time Reward Hacking in Large Language Models (arXiv:2506.19248, NeurIPS 2025 Spotlight)\n- Uncertainty-Aware Step-wise Verification with Generative Reward Models (arXiv:2502.11250, ICLR 2025 Workshop)\n- Detecting and Suppressing Reward Hacking with Gradient Fingerprints (arXiv:2604.16242, April 2026)\n- Uncertainty-Aware Reward Model (arXiv:2410.00847)\n- Helping or Herding? Reward Model Ensembles Mitigate but Do Not Eliminate Overoptimization (arXiv:2312.09244)\n- Bayesian Reward Models for LLM Alignment (arXiv:2402.13210)\n- Conformal Feedback Alignment for RLHF (arXiv:2601.17329)\n- Taming Overconfidence in LLMs: Reward Calibration in RLHF (arXiv:2410.09724)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (arXiv:2501.03124)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T05:45:50.889Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:45:50.889Z",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528"
}
```

---

## Round 1

37 recorded events

### User

_source line 3 · 2026-05-20T05:45:50.939Z_

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
  "promptId": "22a781c4-29a2-4eb1-939b-fe0caec12b40",
  "type": "user",
  "uuid": "b5b2c8e5-3dfc-4e3a-9a8e-6dd1f57ac64f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:45:50.938Z_

```json
{
  "parentUuid": "b5b2c8e5-3dfc-4e3a-9a8e-6dd1f57ac64f",
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
  "uuid": "cd14bbc9-22f2-425f-a656-e20a6f11f658",
  "timestamp": "2026-05-20T05:45:50.938Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:45:50.938Z_

```json
{
  "parentUuid": "cd14bbc9-22f2-425f-a656-e20a6f11f658",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d0154494-b80f-4db4-bc1f-a3e44ed08522",
  "timestamp": "2026-05-20T05:45:50.938Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
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
  "leafUuid": "d0154494-b80f-4db4-bc1f-a3e44ed08522",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration quality and reward hacking resistance",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:45:54.663Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal. Before I can give a proper evaluation, I need to do thorough research on the current state of the field. Let me search for the key papers and topics mentioned in this proposal.

Let me start by searching for the key papers and topics:
1. PRM calibration and hackability
2. The specific papers referenced
3. Any existing work bridging these two areas
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0154494-b80f-4db4-bc1f-a3e44ed08522",
  "isSidechain": false,
  "requestId": "req_011CbDHs5KkL9oQ3A9jMG54F",
  "type": "assistant",
  "uuid": "cc6b159d-1afd-4acb-a6c1-f87560617b84",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Qxm9LMuLBNH5RXnKpHxwT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19987,
      "output_tokens": 202,
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
          "output_tokens": 202,
          "cache_read_input_tokens": 19987,
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

_source line 9 · 2026-05-20T05:45:55.655Z_

I need to do thorough field research before evaluating this proposal. Let me search for the key papers and topics mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc6b159d-1afd-4acb-a6c1-f87560617b84",
  "isSidechain": false,
  "requestId": "req_011CbDHs5KkL9oQ3A9jMG54F",
  "type": "assistant",
  "uuid": "72913902-22c7-4448-8b48-57860c0d92b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Qxm9LMuLBNH5RXnKpHxwT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19987,
      "output_tokens": 202,
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
          "output_tokens": 202,
          "cache_read_input_tokens": 19987,
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

_source line 10 · 2026-05-20T05:45:55.937Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EBKTsKRbHsHJ1Ck3i8yA17`</summary>

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
  "parentUuid": "72913902-22c7-4448-8b48-57860c0d92b8",
  "isSidechain": false,
  "requestId": "req_011CbDHs5KkL9oQ3A9jMG54F",
  "type": "assistant",
  "uuid": "b202db92-7889-47e7-95bf-1391fb01017d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Qxm9LMuLBNH5RXnKpHxwT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19987,
      "output_tokens": 202,
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
          "output_tokens": 202,
          "cache_read_input_tokens": 19987,
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

_source line 11 · 2026-05-20T05:45:55.945Z_

<details><summary>↩ Tool result · `toolu_01EBKTsKRbHsHJ1Ck3i8yA17`</summary>

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
  "parentUuid": "b202db92-7889-47e7-95bf-1391fb01017d",
  "isSidechain": false,
  "promptId": "22a781c4-29a2-4eb1-939b-fe0caec12b40",
  "type": "user",
  "uuid": "b6364afc-73fb-4738-aa3e-b21d9c0bcf7d",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "b202db92-7889-47e7-95bf-1391fb01017d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T05:46:06.639Z_

Now let me conduct the field research. I'll run multiple searches in parallel to cover the key areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6364afc-73fb-4738-aa3e-b21d9c0bcf7d",
  "isSidechain": false,
  "requestId": "req_011CbDHsSvmH2pBhJWMoPjkV",
  "type": "assistant",
  "uuid": "3c1c0244-b710-439d-8815-0c9839f2960d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6yeZkUz989daX1uBJN7ym",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 19987,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 19987,
          "cache_creation_input_tokens": 727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 727
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

_source line 13 · 2026-05-20T05:46:07.382Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W7jKEdWU3ePXPWeuidQkkP`</summary>

```json
{
  "query": "PRM process reward model hackability adversarial robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c1c0244-b710-439d-8815-0c9839f2960d",
  "isSidechain": false,
  "requestId": "req_011CbDHsSvmH2pBhJWMoPjkV",
  "type": "assistant",
  "uuid": "b43a5983-9f87-495c-a570-af03460642a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H6yeZkUz989daX1uBJN7ym",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 19987,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 19987,
          "cache_creation_input_tokens": 727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 727
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

_source line 14 · 2026-05-20T05:46:16.076Z_

<details><summary>↩ Tool result · `toolu_01W7jKEdWU3ePXPWeuidQkkP`</summary>

```text
Web search results for query: "PRM process reward model hackability adversarial robustness 2025 2026"

Links: [{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"Adversarial Training for Process Reward Models | OpenReview","url":"https://openreview.net/forum?id=7DXEF4xHt3"},{"title":"1 Introduction","url":"https://arxiv.org/html/2603.06621"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"[2511.22888] Adversarial Training for Process Reward Models","url":"https://arxiv.org/abs/2511.22888"},{"title":"Adversarial Training of Reward Models","url":"https://arxiv.org/pdf/2504.06141"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/pdf/2511.22888"}]

Based on the search results, here are the key findings on PRM (Process Reward Model) hackability and adversarial robustness from 2025-2026:

## Key Vulnerabilities

Adversarial optimization demonstrates that gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks. Policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.

Current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.

## Reward Hacking Issues

Policies learn to exploit the Reward Model's biases, such as favoring longer chains, specific formatting, or confident phrasing, rather than improving genuine logic, resulting in "reward hacking" that produces high rewards for vacuous reasoning.

## Solutions Under Development

Research has proposed adversarial training approaches to improve robustness. Adversarially Trained PRMs (APRM) use a Generator that learns to produce reasoning errors to deceive a PRM, while the PRM concurrently learns to detect them, improving robustness and generalization to novel errors. APRM improves solver accuracy by +3.4 percentage points over the strongest PRM baseline.

A promising direction is to introduce heterogeneous supervision, where PRMs are guided by an "adversarial council" of diverse models with different architectures, scales, or training corpora that are encouraged to search for weaknesses.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b43a5983-9f87-495c-a570-af03460642a3",
  "isSidechain": false,
  "promptId": "22a781c4-29a2-4eb1-939b-fe0caec12b40",
  "type": "user",
  "uuid": "5d7f8a98-eafd-44aa-9bff-eaca97faa47a",
  "toolUseResult": {
    "query": "PRM process reward model hackability adversarial robustness 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V9Ww57Q69mt6Xp75JAcLuw",
        "content": [
          {
            "title": "[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/abs/2603.06621"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "Adversarial Training for Process Reward Models | OpenReview",
            "url": "https://openreview.net/forum?id=7DXEF4xHt3"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2603.06621"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
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
          }
        ]
      },
      "Based on the search results, here are the key findings on PRM (Process Reward Model) hackability and adversarial robustness from 2025-2026:\n\n## Key Vulnerabilities\n\nAdversarial optimization demonstrates that gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks. Policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.\n\nCurrent PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.\n\n## Reward Hacking Issues\n\nPolicies learn to exploit the Reward Model's biases, such as favoring longer chains, specific formatting, or confident phrasing, rather than improving genuine logic, resulting in \"reward hacking\" that produces high rewards for vacuous reasoning.\n\n## Solutions Under Development\n\nResearch has proposed adversarial training approaches to improve robustness. Adversarially Trained PRMs (APRM) use a Generator that learns to produce reasoning errors to deceive a PRM, while the PRM concurrently learns to detect them, improving robustness and generalization to novel errors. APRM improves solver accuracy by +3.4 percentage points over the strongest PRM baseline.\n\nA promising direction is to introduce heterogeneous supervision, where PRMs are guided by an \"adversarial council\" of diverse models with different architectures, scales, or training corpora that are encouraged to search for weaknesses."
    ],
    "durationSeconds": 8.688371278999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b43a5983-9f87-495c-a570-af03460642a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T05:46:18.672Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BRH87Btmqri2QYjVr7giQW`</summary>

```json
{
  "query": "PRM calibration process reward model calibration uncertainty quantile 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d7f8a98-eafd-44aa-9bff-eaca97faa47a",
  "isSidechain": false,
  "requestId": "req_011CbDHtvisWM85mBacUZSjb",
  "type": "assistant",
  "uuid": "e3eeb7cf-5b93-4ed6-93f2-630755eb12d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CjBk2G7B6QhA1qkEAnmxCd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 809,
      "cache_read_input_tokens": 20714,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 20714,
          "cache_creation_input_tokens": 809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 809
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

_source line 16 · 2026-05-20T05:46:25.384Z_

<details><summary>↩ Tool result · `toolu_01BRH87Btmqri2QYjVr7giQW`</summary>

```text
Web search results for query: "PRM calibration process reward model calibration uncertainty quantile 2025 2026"

Links: [{"title":"NeurIPS Poster Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://neurips.cc/virtual/2025/poster/116598"},{"title":"Process Reward Models (PRMs): Calibration & Scaling","url":"https://www.emergentmind.com/topics/process-reward-models-prms"},{"title":"[2506.09338] Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/abs/2506.09338"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models for NeurIPS 2025 - IBM Research","url":"https://research.ibm.com/publications/know-what-you-dont-know-uncertainty-calibration-of-process-reward-models"},{"title":"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/html/2605.06785"},{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models | OpenReview","url":"https://openreview.net/forum?id=hzMkfIrdDT"},{"title":"Know What You Don't Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/pdf/2506.09338"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models","url":"https://arxiv.org/html/2506.09338v1"},{"title":"Know What You Don’t Know: Uncertainty Calibration of Process Reward Models","url":"https://openreview.net/pdf?id=hzMkfIrdDT"}]

Based on the web search results, here's what I found regarding PRM calibration, process reward models, and uncertainty quantification:

## Key Findings

Process reward models (PRMs) play a central role in guiding inference-time scaling algorithms for large language models (LLMs). However, even state-of-the-art PRMs can be poorly calibrated, and they tend to overestimate the success probability that a partial reasoning step will lead to a correct final answer, particularly when smaller LLMs are used to complete the reasoning trajectory.

## Calibration Approach

A calibration approach is performed via quantile regression that adjusts PRM outputs to better align with true success probabilities. The quantile regression based scheme reduces the calibration error of PRM scores.

## Uncertainty Quantification

Calibrated PRMs now provide actionable, instance-specific success probabilities and confidence bounds, moving beyond relative solution ranking to genuinely trustworthy supervision. By predicting a lower quantile of the posterior distribution (e.g., the 10th percentile), the method ensures that for at least 90% of test cases, the estimate is below or equal to the true success probability.

## Applications

Calibration unlocks instance-adaptive inference-time scaling. This represents recent research from 2025-2026 published at venues like NeurIPS 2025 and on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3eeb7cf-5b93-4ed6-93f2-630755eb12d6",
  "isSidechain": false,
  "promptId": "22a781c4-29a2-4eb1-939b-fe0caec12b40",
  "type": "user",
  "uuid": "09b603d8-8856-4ca0-bc90-740657e0c689",
  "toolUseResult": {
    "query": "PRM calibration process reward model calibration uncertainty quantile 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019PLxkvo1iuE93XX67PyFZt",
        "content": [
          {
            "title": "NeurIPS Poster Know What You Don't Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://neurips.cc/virtual/2025/poster/116598"
          },
          {
            "title": "Process Reward Models (PRMs): Calibration & Scaling",
            "url": "https://www.emergentmind.com/topics/process-reward-models-prms"
          },
          {
            "title": "[2506.09338] Know What You Don't Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://arxiv.org/abs/2506.09338"
          },
          {
            "title": "Know What You Don’t Know: Uncertainty Calibration of Process Reward Models for NeurIPS 2025 - IBM Research",
            "url": "https://research.ibm.com/publications/know-what-you-dont-know-uncertainty-calibration-of-process-reward-models"
          },
          {
            "title": "Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport",
            "url": "https://arxiv.org/html/2605.06785"
          },
          {
            "title": "Know What You Don't Know: Uncertainty Calibration of Process Reward Models | OpenReview",
            "url": "https://openreview.net/forum?id=hzMkfIrdDT"
          },
          {
            "title": "Know What You Don't Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://arxiv.org/pdf/2506.09338"
          },
          {
            "title": "Know What You Don’t Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://arxiv.org/html/2506.09338v1"
          },
          {
            "title": "Know What You Don’t Know: Uncertainty Calibration of Process Reward Models",
            "url": "https://openreview.net/pdf?id=hzMkfIrdDT"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding PRM calibration, process reward models, and uncertainty quantification:\n\n## Key Findings\n\nProcess reward models (PRMs) play a central role in guiding inference-time scaling algorithms for large language models (LLMs). However, even state-of-the-art PRMs can be poorly calibrated, and they tend to overestimate the success probability that a partial reasoning step will lead to a correct final answer, particularly when smaller LLMs are used to complete the reasoning trajectory.\n\n## Calibration Approach\n\nA calibration approach is performed via quantile regression that adjusts PRM outputs to better align with true success probabilities. The quantile regression based scheme reduces the calibration error of PRM scores.\n\n## Uncertainty Quantification\n\nCalibrated PRMs now provide actionable, instance-specific success probabilities and confidence bounds, moving beyond relative solution ranking to genuinely trustworthy supervision. By predicting a lower quantile of the posterior distribution (e.g., the 10th percentile), the method ensures that for at least 90% of test cases, the estimate is below or equal to the true success probability.\n\n## Applications\n\nCalibration unlocks instance-adaptive inference-time scaling. This represents recent research from 2025-2026 published at venues like NeurIPS 2025 and on arXiv."
    ],
    "durationSeconds": 6.708261637000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e3eeb7cf-5b93-4ed6-93f2-630755eb12d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T05:46:27.295Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011mQZBGJ7naHD522JM4F8Pe`</summary>

```json
{
  "query": "reward hacking defense pessimism RLHF reward model 2025 2026 step-level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09b603d8-8856-4ca0-bc90-740657e0c689",
  "isSidechain": false,
  "requestId": "req_011CbDHucUnkfwerTNM2czaL",
  "type": "assistant",
  "uuid": "bae42e39-bb5c-499f-af75-6c1644c4ac76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkN13y6MiayhnJ41wf9msu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 854,
      "cache_read_input_tokens": 21523,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 21523,
          "cache_creation_input_tokens": 854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 854
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

_source line 18 · 2026-05-20T05:46:34.625Z_

<details><summary>↩ Tool result · `toolu_011mQZBGJ7naHD522JM4F8Pe`</summary>

```text
Web search results for query: "reward hacking defense pessimism RLHF reward model 2025 2026 step-level"

Links: [{"title":"Pessimistic Reward Modeling in RLHF against Reward Hacking | OpenReview","url":"https://openreview.net/forum?id=mKPpS6n3cZ"},{"title":"Learning a Pessimistic Reward Model in RLHF","url":"https://arxiv.org/pdf/2505.20556"},{"title":"Pessimistic Reward Modeling in RLHF against Reward Hacking","url":"https://openreview.net/pdf?id=HWOAZUPA0C"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/html/2604.02986"},{"title":"Reward Hacking Defense Rubric","url":"https://www.emergentmind.com/topics/reward-hacking-defense-rubric"},{"title":"[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/abs/2502.18770"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/pdf/2602.10623"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/html/2502.18770v3"}]

Based on the search results, I found several recent papers and research on reward hacking defense and pessimistic RLHF approaches from 2025-2026:

## Key Research Areas

**Pessimistic Reward Modeling:**
A novel pessimistic reward fine-tuning method called PET was proposed (submitted to ICLR 2026) to learn a pessimistic reward model robust against reward hacking in offline RLHF. To avoid reward hacking, the idea of 'pessimism' is necessary for the learning agent—the agent must be pessimistic when evaluating the policy's performance, expecting cases where true performance is less than performance evaluated based on the proxy reward.

**Reward Hacking Challenges:**
Reward hacking, also known as reward over-optimization, is a critical problem in standard RLHF training that can decrease learning efficiency. Reward hacking arises when the policy distribution drifts outside the region where the proxy reward model is reliable.

**Recent Defense Approaches (2025-2026):**
- Uncertainty Quantification methods like the Probabilistic Uncertain Reward Model (PURM) generalize scalar reward outputs to Gaussian distributions and penalize learning in regions of high uncertainty
- Adversarial training uses RL-driven adversarial example generation to surface low-quality but high-scoring samples, immunizing the reward model against exploit modes
- Key design principles include: the RL reward should be bounded, and should benefit from rapid initial growth followed by gradual convergence


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bae42e39-bb5c-499f-af75-6c1644c4ac76",
  "isSidechain": false,
  "promptId": "22a781c4-29a2-4eb1-939b-fe0caec12b40",
  "type": "user",
  "uuid": "8b18ae7a-e3a6-4ef0-b4f0-5a6e827ecea8",
  "toolUseResult": {
    "query": "reward hacking defense pessimism RLHF reward model 2025 2026 step-level",
    "results": [
      {
        "tool_use_id": "srvtoolu_018idRTnbb17G4YkH1Y4r8gP",
        "content": [
          {
            "title": "Pessimistic Reward Modeling in RLHF against Reward Hacking | OpenReview",
            "url": "https://openreview.net/forum?id=mKPpS6n3cZ"
          },
          {
            "title": "Learning a Pessimistic Reward Model in RLHF",
            "url": "https://arxiv.org/pdf/2505.20556"
          },
          {
            "title": "Pessimistic Reward Modeling in RLHF against Reward Hacking",
            "url": "https://openreview.net/pdf?id=HWOAZUPA0C"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/html/2604.02986"
          },
          {
            "title": "Reward Hacking Defense Rubric",
            "url": "https://www.emergentmind.com/topics/reward-hacking-defense-rubric"
          },
          {
            "title": "[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/abs/2502.18770"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/pdf/2602.10623"
          },
          {
            "title": "Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/html/2502.18770v3"
          }
        ]
      },
      "Based on the search results, I found several recent papers and research on reward hacking defense and pessimistic RLHF approaches from 2025-2026:\n\n## Key Research Areas\n\n**Pessimistic Reward Modeling:**\nA novel pessimistic reward fine-tuning method called PET was proposed (submitted to ICLR 2026) to learn a pessimistic reward model robust against reward hacking in offline RLHF. To avoid reward hacking, the idea of 'pessimism' is necessary for the learning agent—the agent must be pessimistic when evaluating the policy's performance, expecting cases where true performance is less than performance evaluated based on the proxy reward.\n\n**Reward Hacking Challenges:**\nReward hacking, also known as reward over-optimization, is a critical problem in standard RLHF training that can decrease learning efficiency. Reward hacking arises when the policy distribution drifts outside the region where the proxy reward model is reliable.\n\n**Recent Defense Approaches (2025-2026):**\n- Uncertainty Quantification methods like the Probabilistic Uncertain Reward Model (PURM) generalize scalar reward outputs to Gaussian distributions and penalize learning in regions of high uncertainty\n- Adversarial training uses RL-driven adversarial example generation to surface low-quality but high-scoring samples, immunizing the reward model against exploit modes\n- Key design principles include: the RL reward should be bounded, and should benefit from rapid initial growth followed by gradual convergence"
    ],
    "durationSeconds": 7.324511490999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bae42e39-bb5c-499f-af75-6c1644c4ac76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T05:46:39.259Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017H3XnfHtc6WzYepgpDuu3n`</summary>

```json
{
  "query": "calibration reward model hackability causal connection linking calibration robustness 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b18ae7a-e3a6-4ef0-b4f0-5a6e827ecea8",
  "isSidechain": false,
  "requestId": "req_011CbDHvJFx4CDxuQ9HjrU9y",
  "type": "assistant",
  "uuid": "6c9cd1e6-e76e-49e3-8931-8e79f6d1f704",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015D47f2hZTfPtLQZfy3U7ca",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 22377,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 842,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 22377,
          "cache_creation_input_tokens": 842,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 842
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

_source line 20 · 2026-05-20T05:46:46.998Z_

<details><summary>↩ Tool result · `toolu_017H3XnfHtc6WzYepgpDuu3n`</summary>

```text
Web search results for query: "calibration reward model hackability causal connection linking calibration robustness 2026"

Links: [{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"},{"title":"arXiv:2506.16507v1 [cs.LG] 19 Jun 2025 2025-6-23","url":"https://arxiv.org/pdf/2506.16507"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/pdf/2603.06621"}]

Based on the web search results, I found several recent papers from 2026 addressing topics related to calibration, reward model robustness, and causal connections:

## Key Findings:

**Causal Approaches to Robust Reward Modeling:**
A recent approach decomposes the model's contextual embedding into causal factors sufficient for reward prediction and noncausal factors capturing reward-irrelevant attributes, with the reward head constrained to depend only on the causal component.

**Causal Robustness (Crome):**
One recent work addresses the challenge of reward hacking in the context of aligning LLMs via RLHF through causally robust reward modeling. A combination of well-designed augmentation strategies, including causal upgradations and degradations, produces the most robust and generalizable reward models.

**Process Reward Model Hackability:**
Adversarial optimization demonstrates that gradient-based attacks inflate rewards on invalid trajectories, with policies trained on reasoning problems achieving near-perfect PRM rewards while ground-truth accuracy remains low, with 43% of reward gains attributable to stylistic shortcuts.

**Calibration Methods:**
Multiple evidence calibration asks evaluator models to provide evaluation evidence/explanations and can be robustified by sampling multiple evidence explanations.

These papers from 2026 suggest active research into connecting causal understanding with reward model robustness to mitigate hackability issues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c9cd1e6-e76e-49e3-8931-8e79f6d1f704",
  "isSidechain": false,
  "promptId": "22a781c4-29a2-4eb1-939b-fe0caec12b40",
  "type": "user",
  "uuid": "b53fa6a0-b7d3-4f22-904d-1e6ea33f59c0",
  "toolUseResult": {
    "query": "calibration reward model hackability causal connection linking calibration robustness 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NUXNkGght4XahxWH3sTi4D",
        "content": [
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          },
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://arxiv.org/pdf/2601.21350"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/pdf/2604.02986"
          },
          {
            "title": "arXiv:2506.16507v1 [cs.LG] 19 Jun 2025 2025-6-23",
            "url": "https://arxiv.org/pdf/2506.16507"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/pdf/2603.06621"
          }
        ]
      },
      "Based on the web search results, I found several recent papers from 2026 addressing topics related to calibration, reward model robustness, and causal connections:\n\n## Key Findings:\n\n**Causal Approaches to Robust Reward Modeling:**\nA recent approach decomposes the model's contextual embedding into causal factors sufficient for reward prediction and noncausal factors capturing reward-irrelevant attributes, with the reward head constrained to depend only on the causal component.\n\n**Causal Robustness (Crome):**\nOne recent work addresses the challenge of reward hacking in the context of aligning LLMs via RLHF through causally robust reward modeling. A combination of well-designed augmentation strategies, including causal upgradations and degradations, produces the most robust and generalizable reward models.\n\n**Process Reward Model Hackability:**\nAdversarial optimization demonstrates that gradient-based attacks inflate rewards on invalid trajectories, with policies trained on reasoning problems achieving near-perfect PRM rewards while ground-truth accuracy remains low, with 43% of reward gains attributable to stylistic shortcuts.\n\n**Calibration Methods:**\nMultiple evidence calibration asks evaluator models to provide evaluation evidence/explanations and can be robustified by sampling multiple evidence explanations.\n\nThese papers from 2026 suggest active research into connecting causal understanding with reward model robustness to mitigate hackability issues."
    ],
    "durationSeconds": 7.734558061999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6c9cd1e6-e76e-49e3-8931-8e79f6d1f704",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
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
  "leafUuid": "b53fa6a0-b7d3-4f22-904d-1e6ea33f59c0",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration quality and reward hacking resistance",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528"
}
```

---

### Tool call

_source line 23 · 2026-05-20T05:46:49.602Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016LgUoipMMY4VwGncs9eQwD`</summary>

```json
{
  "query": "gradient regularization reward hacking Ackermann 2602.18037 Hessian reward surface flatness 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b53fa6a0-b7d3-4f22-904d-1e6ea33f59c0",
  "isSidechain": false,
  "requestId": "req_011CbDHwCvkZdrq7EnxPruA2",
  "type": "assistant",
  "uuid": "08eb35cc-b67c-4858-86c8-fe4f5c06231b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NHF2wn9NTb7uJqRn8Lsnn6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 23219,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 23219,
          "cache_creation_input_tokens": 678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 678
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

_source line 24 · 2026-05-20T05:46:55.921Z_

<details><summary>↩ Tool result · `toolu_016LgUoipMMY4VwGncs9eQwD`</summary>

```text
Web search results for query: "gradient regularization reward hacking Ackermann 2602.18037 Hessian reward surface flatness 2026"

Links: [{"title":"[2602.18037] Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards","url":"https://arxiv.org/abs/2602.18037"},{"title":"Gradient Regularization Prevents Reward Hacking in ...","url":"https://arxiv.org/pdf/2602.18037"},{"title":"[2604.16242] Detecting and Suppressing Reward Hacking with Gradient Fingerprints","url":"https://arxiv.org/abs/2604.16242"},{"title":"Reward Sharpness-Aware Fine-Tuning for Diffusion Models","url":"https://arxiv.org/pdf/2603.21175"},{"title":"Hessian Regularization Scheme","url":"https://www.emergentmind.com/topics/hessian-regularization-scheme"},{"title":"Noise Stability Optimization for Finding Flat Minima: A Hessian-based   Regularization Approach","url":"https://arxiv.org/pdf/2306.08553"}]

I found the paper you're looking for! Here are the key findings:

The work derives a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence, and proposes that gradient regularization (GR) can be used to bias training to flatter regions and thereby maintain reward model accuracy.

The paper addresses reward hacking, where the policy may exploit inaccuracies of the reward and learn an unintended behavior. Rather than the traditional approach, the authors propose to train the LM in a way that biases policy updates towards regions in which the reward is more accurate.

Empirically, GR performs better than a KL penalty across a diverse set of RL experiments with LMs, achieving a higher GPT-judged win-rate in RLHF, avoiding overly focusing on the format in rule-based math rewards, and preventing hacking the judge in LLM-as-a-Judge math tasks.

The paper was published on February 20, 2026, by Johannes Ackermann and colleagues on arXiv (paper ID: 2602.18037).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08eb35cc-b67c-4858-86c8-fe4f5c06231b",
  "isSidechain": false,
  "promptId": "22a781c4-29a2-4eb1-939b-fe0caec12b40",
  "type": "user",
  "uuid": "4bfcba45-b959-4356-933b-c1391add7f76",
  "toolUseResult": {
    "query": "gradient regularization reward hacking Ackermann 2602.18037 Hessian reward surface flatness 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LkYbfN2urXM54E3fRwX7VR",
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
            "title": "Hessian Regularization Scheme",
            "url": "https://www.emergentmind.com/topics/hessian-regularization-scheme"
          },
          {
            "title": "Noise Stability Optimization for Finding Flat Minima: A Hessian-based   Regularization Approach",
            "url": "https://arxiv.org/pdf/2306.08553"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key findings:\n\nThe work derives a theoretical connection between the accuracy of a reward model and the flatness of an optimum at convergence, and proposes that gradient regularization (GR) can be used to bias training to flatter regions and thereby maintain reward model accuracy.\n\nThe paper addresses reward hacking, where the policy may exploit inaccuracies of the reward and learn an unintended behavior. Rather than the traditional approach, the authors propose to train the LM in a way that biases policy updates towards regions in which the reward is more accurate.\n\nEmpirically, GR performs better than a KL penalty across a diverse set of RL experiments with LMs, achieving a higher GPT-judged win-rate in RLHF, avoiding overly focusing on the format in rule-based math rewards, and preventing hacking the judge in LLM-as-a-Judge math tasks.\n\nThe paper was published on February 20, 2026, by Johannes Ackermann and colleagues on arXiv (paper ID: 2602.18037)."
    ],
    "durationSeconds": 6.31501121299999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "08eb35cc-b67c-4858-86c8-fe4f5c06231b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T05:47:06.676Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015mW1sDiyYrX9K3hzmKUQVB`</summary>

```json
{
  "query": "\"distributional process reward model\" arXiv 2605.06785 conditional optimal transport calibrated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bfcba45-b959-4356-933b-c1391add7f76",
  "isSidechain": false,
  "requestId": "req_011CbDHwsT1cvfhPad1yiX3k",
  "type": "assistant",
  "uuid": "ad26dec1-6322-4559-90c1-4442d0d837f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQMNrKUSMThxP887zPxiXZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 23897,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 659,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 23897,
          "cache_creation_input_tokens": 659,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 659
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

_source line 26 · 2026-05-20T05:47:13.118Z_

<details><summary>↩ Tool result · `toolu_015mW1sDiyYrX9K3hzmKUQVB`</summary>

```text
Web search results for query: ""distributional process reward model" arXiv 2605.06785 conditional optimal transport calibrated"

Links: [{"title":"[2605.06785] Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/abs/2605.06785"},{"title":"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/html/2605.06785"},{"title":"APLOT: Robust Reward Modeling via Adaptive Preference Learning with Optimal Transport","url":"https://arxiv.org/pdf/2510.10963"},{"title":"Consistent Optimal Transport with Empirical Conditional Measures","url":"https://arxiv.org/pdf/2305.15901"},{"title":"1. Introduction","url":"https://arxiv.org/html/2505.21098v2"},{"title":"Conditional Risk Minimization with Side Information: A Tractable, Universal Optimal Transport Framework","url":"https://arxiv.org/pdf/2509.23128"},{"title":"Distributional Preference Alignment of LLMs via Optimal Transport","url":"https://arxiv.org/pdf/2406.05882"}]

I found the paper! Here's the information about arXiv paper 2605.06785:

**Title:** Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport

**Key Contribution:** The paper proposes the first use of conditional optimal transport for calibrating PRMs, modifying conditional OT map learning to estimate a monotonic conditional quantile function over success probabilities estimated by the PRM, conditioned on PRM hidden states.

**Problem Being Addressed:** Inference-time scaling methods rely on Process Reward Models (PRMs), which are often poorly calibrated and overestimate success probabilities.

**Method Benefits:** This yields structurally valid quantile estimates and enables efficient extraction of confidence bounds at arbitrary levels, which is integrated into the instance-adaptive scaling framework.

**Evaluation:** The method is evaluated on mathematical reasoning benchmarks spanning moderate-difficulty problems (MATH-500) and harder out-of-distribution problems (AIME), with substantial improvements in calibration over both uncalibrated PRMs and quantile regression for PRMs with reliable ranking signals.

The paper was posted on arXiv on May 7, 2026, and is authored by researchers from MIT CSAIL and IBM Research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad26dec1-6322-4559-90c1-4442d0d837f6",
  "isSidechain": false,
  "promptId": "22a781c4-29a2-4eb1-939b-fe0caec12b40",
  "type": "user",
  "uuid": "f87525db-6340-4b20-be42-d3a7b7513f88",
  "toolUseResult": {
    "query": "\"distributional process reward model\" arXiv 2605.06785 conditional optimal transport calibrated",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KJR9gidy1NTiEwxpMDRVGV",
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
            "title": "Consistent Optimal Transport with Empirical Conditional Measures",
            "url": "https://arxiv.org/pdf/2305.15901"
          },
          {
            "title": "1. Introduction",
            "url": "https://arxiv.org/html/2505.21098v2"
          },
          {
            "title": "Conditional Risk Minimization with Side Information: A Tractable, Universal Optimal Transport Framework",
            "url": "https://arxiv.org/pdf/2509.23128"
          },
          {
            "title": "Distributional Preference Alignment of LLMs via Optimal Transport",
            "url": "https://arxiv.org/pdf/2406.05882"
          }
        ]
      },
      "I found the paper! Here's the information about arXiv paper 2605.06785:\n\n**Title:** Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport\n\n**Key Contribution:** The paper proposes the first use of conditional optimal transport for calibrating PRMs, modifying conditional OT map learning to estimate a monotonic conditional quantile function over success probabilities estimated by the PRM, conditioned on PRM hidden states.\n\n**Problem Being Addressed:** Inference-time scaling methods rely on Process Reward Models (PRMs), which are often poorly calibrated and overestimate success probabilities.\n\n**Method Benefits:** This yields structurally valid quantile estimates and enables efficient extraction of confidence bounds at arbitrary levels, which is integrated into the instance-adaptive scaling framework.\n\n**Evaluation:** The method is evaluated on mathematical reasoning benchmarks spanning moderate-difficulty problems (MATH-500) and harder out-of-distribution problems (AIME), with substantial improvements in calibration over both uncalibrated PRMs and quantile regression for PRMs with reliable ranking signals.\n\nThe paper was posted on arXiv on May 7, 2026, and is authored by researchers from MIT CSAIL and IBM Research."
    ],
    "durationSeconds": 6.437736530000009,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ad26dec1-6322-4559-90c1-4442d0d837f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T05:47:17.953Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MYQAk6ojRmxBSLU6iHPxx7`</summary>

```json
{
  "query": "\"Caution\" reward hacking pessimism best-of-N 2604.04648 inference time pessimism 2506.19248"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f87525db-6340-4b20-be42-d3a7b7513f88",
  "isSidechain": false,
  "requestId": "req_011CbDHy8bN1DyzWQLWXbkQL",
  "type": "assistant",
  "uuid": "32cd4c91-a8ee-4c9d-bc38-c796b2810a18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XQZbtszDJimD7M7JnELtR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 688,
      "cache_read_input_tokens": 24556,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 688,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 24556,
          "cache_creation_input_tokens": 688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 688
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

_source line 28 · 2026-05-20T05:47:25.675Z_

<details><summary>↩ Tool result · `toolu_01MYQAk6ojRmxBSLU6iHPxx7`</summary>

```text
Web search results for query: ""Caution" reward hacking pessimism best-of-N 2604.04648 inference time pessimism 2506.19248"

Links: [{"title":"[2604.04648] From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/abs/2604.04648"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism","url":"https://arxiv.org/pdf/2604.04648"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-𝑁 with Pessimism","url":"https://arxiv.org/html/2604.04648"},{"title":"[2506.19248] Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/abs/2506.19248"},{"title":"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-$N$ with Pessimism | OpenReview","url":"https://openreview.net/forum?id=EZn2TmBBfF"},{"title":"Best-of-Tails: Bridging Optimism and Pessimism in Inference-Time Alignment","url":"https://arxiv.org/pdf/2603.06797"}]

Based on the search results, I found both papers referenced in your query:

## Paper 2604.04648: "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism"

This paper explores inference-time compute scaling for language models. A popular approach called Best-of-N (BoN) sampling generates N candidate responses, scores them according to a reward model, and selects the highest-scoring response. However, this approach is vulnerable to reward hacking, where performance degrades as N increases due to selection of responses that exploit imperfections in the reward model instead of genuinely improving generation quality.

The paper explores the principle of pessimism in RL, which uses lower confidence bounds on value estimates to avoid out-of-distribution actions with uncertain reward estimates. Their approach, termed "caution," can be seen as the reverse of curiosity: where curiosity rewards prediction error as a signal of novelty, caution penalizes prediction error as a signal of distributional uncertainty. Practically, caution trains an error model on typical responses and uses its prediction error to lower reward estimates for atypical ones.

## Paper 2506.19248: "Inference-Time Reward Hacking in Large Language Models"

This paper characterizes reward hacking in inference-time alignment, where overoptimizing for a misspecified reward can subvert intended alignment goals and reduce overall performance. The authors demonstrate when and how this phenomenon can be mitigated by hedging on the proxy reward. The work studies this phenomenon under Best-of-n (BoN) and Soft Best-of-n (SBoN), and introduces Best-of-Poisson (BoP) that provides an efficient, near-exact approximation of the optimal reward-KL divergence policy at inference time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32cd4c91-a8ee-4c9d-bc38-c796b2810a18",
  "isSidechain": false,
  "promptId": "22a781c4-29a2-4eb1-939b-fe0caec12b40",
  "type": "user",
  "uuid": "edda0904-c715-43bd-9d49-2d17520d1f0e",
  "toolUseResult": {
    "query": "\"Caution\" reward hacking pessimism best-of-N 2604.04648 inference time pessimism 2506.19248",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LcUtXTNdSCwRQau2yVcSMr",
        "content": [
          {
            "title": "[2604.04648] From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism",
            "url": "https://arxiv.org/abs/2604.04648"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism",
            "url": "https://arxiv.org/pdf/2604.04648"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-𝑁 with Pessimism",
            "url": "https://arxiv.org/html/2604.04648"
          },
          {
            "title": "[2506.19248] Inference-Time Reward Hacking in Large Language Models",
            "url": "https://arxiv.org/abs/2506.19248"
          },
          {
            "title": "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-$N$ with Pessimism | OpenReview",
            "url": "https://openreview.net/forum?id=EZn2TmBBfF"
          },
          {
            "title": "Best-of-Tails: Bridging Optimism and Pessimism in Inference-Time Alignment",
            "url": "https://arxiv.org/pdf/2603.06797"
          }
        ]
      },
      "Based on the search results, I found both papers referenced in your query:\n\n## Paper 2604.04648: \"From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism\"\n\nThis paper explores inference-time compute scaling for language models. A popular approach called Best-of-N (BoN) sampling generates N candidate responses, scores them according to a reward model, and selects the highest-scoring response. However, this approach is vulnerable to reward hacking, where performance degrades as N increases due to selection of responses that exploit imperfections in the reward model instead of genuinely improving generation quality.\n\nThe paper explores the principle of pessimism in RL, which uses lower confidence bounds on value estimates to avoid out-of-distribution actions with uncertain reward estimates. Their approach, termed \"caution,\" can be seen as the reverse of curiosity: where curiosity rewards prediction error as a signal of novelty, caution penalizes prediction error as a signal of distributional uncertainty. Practically, caution trains an error model on typical responses and uses its prediction error to lower reward estimates for atypical ones.\n\n## Paper 2506.19248: \"Inference-Time Reward Hacking in Large Language Models\"\n\nThis paper characterizes reward hacking in inference-time alignment, where overoptimizing for a misspecified reward can subvert intended alignment goals and reduce overall performance. The authors demonstrate when and how this phenomenon can be mitigated by hedging on the proxy reward. The work studies this phenomenon under Best-of-n (BoN) and Soft Best-of-n (SBoN), and introduces Best-of-Poisson (BoP) that provides an efficient, near-exact approximation of the optimal reward-KL divergence policy at inference time."
    ],
    "durationSeconds": 7.7148855360000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "32cd4c91-a8ee-4c9d-bc38-c796b2810a18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T05:47:25.685Z_

```json
{
  "parentUuid": "edda0904-c715-43bd-9d49-2d17520d1f0e",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "55b47dee-81da-4682-a547-b92f268dd069",
  "timestamp": "2026-05-20T05:47:25.685Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-20T05:47:28.017Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ZiwztnjW9y7ZZTpVB69Fv`</summary>

```json
{
  "query": "calibration link to adversarial robustness reward model exploit uncertainty calibration prevents hacking"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55b47dee-81da-4682-a547-b92f268dd069",
  "isSidechain": false,
  "requestId": "req_011CbDHz4Mu7ybXr5anq75gf",
  "type": "assistant",
  "uuid": "559515f9-9f6d-4ea9-bf96-6aba2b79e664",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019fiA2AjXMavZXZef3UrnYj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 980,
      "cache_read_input_tokens": 25244,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 980,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 25244,
          "cache_creation_input_tokens": 980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 980
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

_source line 31 · 2026-05-20T05:47:35.342Z_

<details><summary>↩ Tool result · `toolu_015ZiwztnjW9y7ZZTpVB69Fv`</summary>

```text
Web search results for query: "calibration link to adversarial robustness reward model exploit uncertainty calibration prevents hacking"

Links: [{"title":"Towards Certification of Uncertainty Calibration under Adversarial Attacks","url":"https://arxiv.org/html/2405.13922v1"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/html/2604.02986"},{"title":"Improving Calibration through the Relationship with Adversarial Robustness","url":"https://proceedings.neurips.cc/paper_files/paper/2021/file/78421a2e0e1168e5cd1b7a8d23773ce6-Paper.pdf"},{"title":"Adversarial Training of Reward Models","url":"https://arxiv.org/html/2504.06141"},{"title":"Uncertainty-Aware Reward Discounting for Mitigating Reward Hacking","url":"https://arxiv.org/html/2604.26360"},{"title":"Integrating confidence calibration and adversarial robustness via adversarial calibration entropy - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0020025524004456"},{"title":"Reward Hacking Defense Rubric","url":"https://www.emergentmind.com/topics/reward-hacking-defense-rubric"}]

Based on the search results, here are the key findings connecting calibration, adversarial robustness, reward models, and exploitation prevention:

## Calibration and Adversarial Robustness Connection

Adversarial robustness can be used as a means to improve model trustworthiness by limiting adversarial attacks and also improving calibration and stability on unexpected data. Additionally, confidence and adversarial robustness can exhibit a uniform trend, and adversarial calibration entropy can be used to simultaneously improve a model's adversarial robustness and confidence calibration performance.

## Uncertainty Calibration Preventing Reward Hacking

High uncertainty reduces effective reward through a reciprocal discounting mechanism, steering agents away from unreliable regions, which is critical for alignment under reward misspecification. 

Regarding specific defenses against reward model exploitation, the Probabilistic Uncertain Reward Model (PURM) generalizes scalar reward outputs to Gaussian distributions and penalizes learning in regions of high uncertainty to prevent overoptimization.

## Reward Model Exploit Mitigation

Adversarial training frameworks automatically identify adversarial examples that receive high rewards but are out-of-distribution and low quality, and leverage reinforcement learning to generate examples that expose vulnerabilities in reward models.

The research suggests that uncertainty calibration plays a crucial defensive role by reducing the model's confidence in unreliable regions, thereby preventing policies from exploiting poorly calibrated reward signals.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "559515f9-9f6d-4ea9-bf96-6aba2b79e664",
  "isSidechain": false,
  "promptId": "22a781c4-29a2-4eb1-939b-fe0caec12b40",
  "type": "user",
  "uuid": "b55356a3-b6da-4759-9965-fb07180bdb54",
  "toolUseResult": {
    "query": "calibration link to adversarial robustness reward model exploit uncertainty calibration prevents hacking",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JncP3PTHHH4DcsFJMNJagH",
        "content": [
          {
            "title": "Towards Certification of Uncertainty Calibration under Adversarial Attacks",
            "url": "https://arxiv.org/html/2405.13922v1"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/html/2604.02986"
          },
          {
            "title": "Improving Calibration through the Relationship with Adversarial Robustness",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2021/file/78421a2e0e1168e5cd1b7a8d23773ce6-Paper.pdf"
          },
          {
            "title": "Adversarial Training of Reward Models",
            "url": "https://arxiv.org/html/2504.06141"
          },
          {
            "title": "Uncertainty-Aware Reward Discounting for Mitigating Reward Hacking",
            "url": "https://arxiv.org/html/2604.26360"
          },
          {
            "title": "Integrating confidence calibration and adversarial robustness via adversarial calibration entropy - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0020025524004456"
          },
          {
            "title": "Reward Hacking Defense Rubric",
            "url": "https://www.emergentmind.com/topics/reward-hacking-defense-rubric"
          }
        ]
      },
      "Based on the search results, here are the key findings connecting calibration, adversarial robustness, reward models, and exploitation prevention:\n\n## Calibration and Adversarial Robustness Connection\n\nAdversarial robustness can be used as a means to improve model trustworthiness by limiting adversarial attacks and also improving calibration and stability on unexpected data. Additionally, confidence and adversarial robustness can exhibit a uniform trend, and adversarial calibration entropy can be used to simultaneously improve a model's adversarial robustness and confidence calibration performance.\n\n## Uncertainty Calibration Preventing Reward Hacking\n\nHigh uncertainty reduces effective reward through a reciprocal discounting mechanism, steering agents away from unreliable regions, which is critical for alignment under reward misspecification. \n\nRegarding specific defenses against reward model exploitation, the Probabilistic Uncertain Reward Model (PURM) generalizes scalar reward outputs to Gaussian distributions and penalizes learning in regions of high uncertainty to prevent overoptimization.\n\n## Reward Model Exploit Mitigation\n\nAdversarial training frameworks automatically identify adversarial examples that receive high rewards but are out-of-distribution and low quality, and leverage reinforcement learning to generate examples that expose vulnerabilities in reward models.\n\nThe research suggests that uncertainty calibration plays a crucial defensive role by reducing the model's confidence in unreliable regions, thereby preventing policies from exploiting poorly calibrated reward signals."
    ],
    "durationSeconds": 7.320559448,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "559515f9-9f6d-4ea9-bf96-6aba2b79e664",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T05:47:37.799Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019txDdEbXSXmwKCur93sek9`</summary>

```json
{
  "query": "\"uncertainty-aware reward\" discount step-level PRM defense RL training 2604.26360"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b55356a3-b6da-4759-9965-fb07180bdb54",
  "isSidechain": false,
  "requestId": "req_011CbDHzmbNQjsd7YAWNP1LL",
  "type": "assistant",
  "uuid": "a6fefabf-5acd-4fc8-ad2f-712edca0728c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KN7eKmhacTBDj7QtUNiDEN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 778,
      "cache_read_input_tokens": 26224,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 26224,
          "cache_creation_input_tokens": 778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 778
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

_source line 33 · 2026-05-20T05:47:44.294Z_

<details><summary>↩ Tool result · `toolu_019txDdEbXSXmwKCur93sek9`</summary>

```text
Web search results for query: ""uncertainty-aware reward" discount step-level PRM defense RL training 2604.26360"

Links: [{"title":"[2604.26360] Uncertainty-Aware Reward Discounting for Mitigating Reward Hacking","url":"https://arxiv.org/abs/2604.26360"},{"title":"Uncertainty-Aware Reward Discounting for Mitigating Reward Hacking","url":"https://arxiv.org/html/2604.26360"},{"title":"Adaptive Discount Factor for Deep Reinforcement Learning in Continuing Tasks with Uncertainty","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9570626/"},{"title":"UNCERTAINTY-AWARE STEP-WISE VERIFICATION","url":"https://openreview.net/pdf?id=6YICujbAtG"},{"title":"Preprint SPARK: STEPWISE PROCESS-AWARE REWARDS FOR","url":"https://arxiv.org/pdf/2512.03244"},{"title":"Probabilistic Uncertain Reward Model","url":"https://arxiv.org/pdf/2503.22480"},{"title":"Agentic Reinforcement Learning with Implicit Step Rewards","url":"https://arxiv.org/html/2509.19199v3"},{"title":"Reducing Reward Dependence in RL Through Adaptive Confidence Discounting","url":"https://arxiv.org/html/2502.21181v1"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/pdf/2603.06621"}]

Based on the search results, I found the paper you're looking for. Here's what the research is about:

The paper introduces a dual-source uncertainty-aware reward framework that explicitly models both epistemic uncertainty in value estimation and uncertainty in human preferences. Model uncertainty is captured via ensemble disagreement over value predictions, while preference uncertainty is derived from variability in reward annotations.

The research addresses the problem that RL systems typically optimize scalar reward functions assuming precise evaluation, but real-world objectives—especially those derived from human preferences—are often uncertain, context-dependent, and internally inconsistent, which can lead to alignment failures such as reward hacking, over-optimization, and overconfident behavior.

The framework combines these uncertainty signals through a confidence-adjusted Reliability Filter that adaptively modulates action selection, encouraging a balance between exploitation and caution.

The paper (arXiv:2604.26360) was published in April 2026 and appears to be addressing a critical problem in reinforcement learning where reward models can be exploited or manipulated during training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6fefabf-5acd-4fc8-ad2f-712edca0728c",
  "isSidechain": false,
  "promptId": "22a781c4-29a2-4eb1-939b-fe0caec12b40",
  "type": "user",
  "uuid": "50e4d4c0-73ff-4287-8f00-f1f3258e3a8c",
  "toolUseResult": {
    "query": "\"uncertainty-aware reward\" discount step-level PRM defense RL training 2604.26360",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LSNcuB4sNygwJMTJR3cPGQ",
        "content": [
          {
            "title": "[2604.26360] Uncertainty-Aware Reward Discounting for Mitigating Reward Hacking",
            "url": "https://arxiv.org/abs/2604.26360"
          },
          {
            "title": "Uncertainty-Aware Reward Discounting for Mitigating Reward Hacking",
            "url": "https://arxiv.org/html/2604.26360"
          },
          {
            "title": "Adaptive Discount Factor for Deep Reinforcement Learning in Continuing Tasks with Uncertainty",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9570626/"
          },
          {
            "title": "UNCERTAINTY-AWARE STEP-WISE VERIFICATION",
            "url": "https://openreview.net/pdf?id=6YICujbAtG"
          },
          {
            "title": "Preprint SPARK: STEPWISE PROCESS-AWARE REWARDS FOR",
            "url": "https://arxiv.org/pdf/2512.03244"
          },
          {
            "title": "Probabilistic Uncertain Reward Model",
            "url": "https://arxiv.org/pdf/2503.22480"
          },
          {
            "title": "Agentic Reinforcement Learning with Implicit Step Rewards",
            "url": "https://arxiv.org/html/2509.19199v3"
          },
          {
            "title": "Reducing Reward Dependence in RL Through Adaptive Confidence Discounting",
            "url": "https://arxiv.org/html/2502.21181v1"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/pdf/2603.06621"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what the research is about:\n\nThe paper introduces a dual-source uncertainty-aware reward framework that explicitly models both epistemic uncertainty in value estimation and uncertainty in human preferences. Model uncertainty is captured via ensemble disagreement over value predictions, while preference uncertainty is derived from variability in reward annotations.\n\nThe research addresses the problem that RL systems typically optimize scalar reward functions assuming precise evaluation, but real-world objectives—especially those derived from human preferences—are often uncertain, context-dependent, and internally inconsistent, which can lead to alignment failures such as reward hacking, over-optimization, and overconfident behavior.\n\nThe framework combines these uncertainty signals through a confidence-adjusted Reliability Filter that adaptively modulates action selection, encouraging a balance between exploitation and caution.\n\nThe paper (arXiv:2604.26360) was published in April 2026 and appears to be addressing a critical problem in reinforcement learning where reward models can be exploited or manipulated during training."
    ],
    "durationSeconds": 6.492186968999987,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a6fefabf-5acd-4fc8-ad2f-712edca0728c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
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
  "leafUuid": "50e4d4c0-73ff-4287-8f00-f1f3258e3a8c",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration quality and reward hacking resistance",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528"
}
```

---

### Assistant

_source line 36 · 2026-05-20T05:48:33.099Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough research to make a thorough evaluation. Let me synthesize what I've found:

Key findings from my research:

1. **PRM Hackability (Tiwari et al., 2603.06621)**: Confirmed - PRMs are catastrophically hackable, with near-perfect PRM rewards but <4% accuracy. This is a real, well-documented problem.

2. **PRM Calibration (Park et al., 2506.09338, NeurIPS 2025; Distributional PRMs, 2605.06785)**: Confirmed - PRMs are poorly calibrated, especially on hard problems. Calibration methods exist but haven't been tested for robustness.


3. **Ackermann et al. (2602.18037)**: Confirmed - Gradient regularization addresses reward hacking at the outcome level, which aligns with their specific focus.

4. **Caution (2604.04648)**: Confirmed - Leverages prediction error as an uncertainty signal for pessimistic best-of-N selection, though it's not calibration-based.

5. **Inference-Time Pessimism (2506.19248)**: Confirmed - Uses hedging strategies for best-of-N, also not calibration-based.

6. **Uncertainty-Aware Reward Discounting (2604.26360)**: Still examining this approach...

7. **PURM (Probabilistic Uncertain Reward Model)**: Generalizes rewards to Gaussian distributions and penalizes high-uncertainty regions, which is conceptually aligned with the proposal's approach but isn't cited.

8. **PET (Pessimistic Reward Fine-Tuning)**: Need to verify this more thoroughly.

The core insight here is that calibrated uncertainty in reward models could directly mitigate reward hacking, and it's striking how the literature on PRM calibration and PRM vulnerability operate in isolation with minimal cross-referencing. The proposal's strength lies in connecting these two threads and proposing that calibration quality is the causal mechanism for robustness.

The causal isolation strategy using post-hoc versus fine-tuning-based calibration is clever, and extending Hessian analysis to the step level beyond prior outcome-level work adds genuine novelty. CGSP itself is a concrete, implementable defense.

However, there's a significant concern: uncertainty-aware reward discounting from that earlier paper already accomplishes something very similar to CGSP by using uncertainty to modulate rewards during training. The question is whether the calibration-specific aspect is truly critical, or if simpler uncalibrated uncertainty like ensemble disagreement could work just as well. The proposal does test ensemble-min as a baseline, which is good, but this fundamental question about whether calibration is essential versus just having any uncertainty signal remains unresolved.

There's also a risk that the core finding—that fixing calibration reduces hackability—is somewhat tautological: if a PRM overestimates success on bad solutions, then correcting that overestimation naturally eliminates false positive high-reward regions to exploit. The real scientific question is whether calibrated uncertainty provides robustness *beyond* just correcting mean predictions, or whether the uncertainty estimates themselves add independent value. Additionally, the proposal tries to cover too much ground—correlation analysis across 48 configurations, causal isolation methodology, Hessian analysis, and a novel defense mechanism—which risks making each component feel superficial rather than deeply explored.

I'm also noticing a significant gap: the proposal doesn't reference 2604.26360 on uncertainty-aware reward discounting, which is conceptually very similar to CGSP. That's a notable omission in the related work.

Looking at the overall assessment, the novelty is medium—bridging calibration and hackability is an interesting observation, but it may be near-tautological, and CGSP itself is closely related to existing uncertainty-aware approaches. The significance is there since PRM reward hacking is an important problem, and establishing the causal link could guide future design, though the practical impact of CGSP remains to be fully demonstrated.

Given the solid methodology but moderate insight ceiling, I'm settling around 30% as my probability estimate—the core idea is sound and timely, but it's not revolutionary enough to push higher. and no one has bridged them
2. The causal isolation methodology is rigorous
3. It has a concrete defense (CGSP)
4. The experimental plan is comprehensive

But the weaknesses:
1. The core insight might be "obviously true" → reviewers say "I would have guessed this"
2. CGSP is incrementally different from existing uncertainty-based defenses
3. Missing key related work
4. Overly ambitious scope

I think 25-35% is right, with midpoint around 28-30%.

Actually, let me reconsider more carefully. The proposal has a genuine methodological contribution in the causal isolation experiments. The idea of using post-hoc calibration as a way to isolate the causal effect of calibration on hackability is genuinely clever. This is not trivial.

However, the CGSP defense is indeed closely related to existing work on uncertainty-aware reward discounting—the step-level aspect and calibration-grounding are real differentiators, but they're incremental. I should also consider that if the causal study finds calibration doesn't actually determine hackability, that would be more interesting than the proposal suggests. Overall, the work has real substance and explores a genuinely unexplored bridge, but the ceiling on what we might discover is limited by the near-tautology concern, and CGSP doesn't sufficiently differentiate itself from prior work. I'll estimate 25-33%, with a midpoint around 28%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50e4d4c0-73ff-4287-8f00-f1f3258e3a8c",
  "isSidechain": false,
  "requestId": "req_011CbDJ1RtE5PxGTFTx8tQNc",
  "type": "assistant",
  "uuid": "2136153a-333e-4082-9c6a-0d9ce2cd1fde",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZYBsWE6RPYfFj1xurJg9b",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 27002,
      "output_tokens": 5699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 728,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5699,
          "cache_read_input_tokens": 27002,
          "cache_creation_input_tokens": 728,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 728
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

_source line 37 · 2026-05-20T05:49:54.704Z_

Now I have sufficient research to make a thorough assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. **Tiwari et al. "Reward Under Attack" (arXiv:2603.06621, Mar 2026)**:
   直接相关——系统性展示 PRM 的脆弱性：梯度攻击可将 PRM reward 膨胀 4×，GRPO 训练后 PRM reward 接近满分但真实准确率 <4%，43% 的 reward gain 来自风格捷径。该论文只做了诊断，未提出基于 calibration 的防御。Proposal 的 Thread 2 直接引用此工作，描述准确。

2. **Park et al. "Know What You Don't Know" (arXiv:2506.09338, NeurIPS 2025)**:
   直接相关——发现 PRM 系统性高估困难题的成功概率，提出基于 quantile regression 的 calibration。仅用于 inference-time scaling，未测试鲁棒性。Proposal 引用准确。

3. **Distributional PRMs (arXiv:2605.06785, May 2026)**:
   直接相关——用 conditional optimal transport 实现 calibrated monotone quantile function。在 MATH-500 和 AIME 上改善 BoN。同样未测试对抗鲁棒性。Proposal 引用准确，确认 May 2026 发布。

4. **Ackermann et al. "Gradient Regularization Prevents Reward Hacking" (arXiv:2602.18037, Feb 2026)**:
   密切相关——建立了 reward surface flatness 与准确率保持之间的理论联系，提出梯度正则化。确认工作在 outcome level，使用单标量 reward，仅分析 gradient norms。Proposal 关于其局限性的描述准确。

5. **"From Curiosity to Caution" (arXiv:2604.04648, Apr 2026)**:
   相关——用 prediction error 作为 uncertainty proxy 实现 pessimistic BoN，非 calibration-based。Proposal 描述准确。

6. **"Inference-Time Reward Hacking" (arXiv:2506.19248, NeurIPS 2025 Spotlight)**:
   相关——用 hedging 方法缓解 BoN 中的 reward hacking。非 calibration-based。Proposal 描述准确。

7. **⚠️ "Uncertainty-Aware Reward Discounting" (arXiv:2604.26360, Apr 2026)** ← **Proposal 未引用的重要相关工作**:
   高度相关——提出 dual-source uncertainty-aware reward framework，显式建模 epistemic uncertainty 和 preference uncertainty，通过 confidence-adjusted Reliability Filter 自适应调节 action selection。这与 CGSP 的 r̃_t = μ_t − α·σ_t/√c_t 思路高度重合：都用 uncertainty 来 discount reward 以防 hacking。关键差异是 CGSP 强调 step-level + calibration-grounded，但概念重叠显著。

8. **APRM "Adversarial Training for PRMs" (arXiv:2511.22888, Nov 2025)**:
   相关——对抗训练提升 PRM 鲁棒性 +3.4pp。非 calibration 路线。Proposal 引用准确。

9. **PURM (Probabilistic Uncertain Reward Model, arXiv:2503.22480)**:
   相关但 Proposal 未引用——将标量 reward 泛化为 Gaussian 分布，在高不确定区域施加惩罚。与 CGSP 的 uncertainty-based pessimism 有概念重叠。

- **调研总结**: PRM calibration 和 PRM hackability 确实是两个独立发展的研究线程（零交叉引用可以确认）。同时，uncertainty-aware reward discounting 已成为 2026 年的活跃方向（2604.26360, PURM），但现有工作集中在 outcome level 且不使用 calibrated uncertainty。Proposal 处于一个真实的交叉空白，但该空白正在被从 uncertainty 方向逐渐填补。


【Trivial Alternative 检验】:

存在两个 trivial alternative 威胁：

(1) **简单 ensemble disagreement 替代 calibrated uncertainty**: 已有工作（Coste et al. ensemble-min, URM 等）直接用 ensemble 分歧作为 uncertainty proxy 来实现 pessimism，无需 calibration。Proposal 虽列出 ensemble-min 作 baseline，但如果 ensemble-min 效果相当，则 calibration-grounding 的增量价值存疑。Proposal 需要证明 calibrated uncertainty 在 CGSP 中的表现显著优于 uncalibrated ensemble uncertainty。

(2) **"Calibration 减少 hackability"可能是近似重言式**: 如果 PRM 对错误解法过度自信（高估 success probability），calibration 修正这种过度自信，则 reward hacking 减少是直接推论——不是因为"calibration 带来了某种特殊防御"，而是因为"calibration 纠正了错误的高分"。如果是这样，增量贡献就只是把一个直觉形式化了。Proposal 的 causal isolation 实验可以部分回应这个问题（如果 post-hoc calibration 修正了 mean prediction 但 hackability 下降幅度超过 mean correction 能解释的部分，则说明 calibration 的价值不止于修正均值），但 proposal 目前没有明确设计这个对照。


【前提假设检验】:

Proposal 的核心逻辑链：calibration quality ↑ → uncertainty estimates become reliable → uncertainty-based pessimism can prevent hacking → CGSP works

未经验证的关键假设：

(1) **"Post-hoc calibration 足以显著降低 hackability"**: Post-hoc 方法（temperature scaling 等）只修改 output mapping，对 gradient attack 的影响路径不清楚。梯度攻击直接操纵 input space 以最大化 reward，temperature scaling 仅改变 logit-to-probability 映射——攻击者可以适应新的映射。Proposal 假设 calibration 使 reward surface 变"平坦"，但 post-hoc calibration 对 Hessian spectrum 的影响尚无理论支撑。

(2) **"Calibration quality 在 RL training 过程中可以实时维护"**: CGSP 依赖 rolling buffer 上计算的 calibration quality score c_t。但 RL 训练导致 policy distribution shift，calibration（在 SFT distribution 上拟合）会快速退化。虽然 Proposal 设计了 Calibration Drift Detector，但这是一个后验监测而非前瞻保证——如果 drift 太快，CGSP 可能退化为简单的 reward clipping。

(3) **"Step-level Hessian analysis 在计算上可行且信息量充足"**: 对大型 PRM（7B-72B 参数）在每个 step 上计算 Hessian 的 top-k eigenvalues 计算成本极高。即使使用 Lanczos 方法，48 个配置 × 多个问题 × 多个 step 的规模可能不可行。且 Hessian 分析的因果解释力有限——相关不等于因果。


【3 维度打分】:

1. **Novelty: 中** —
   - (+) 桥接 calibration 和 hackability 两个零交叉引用的研究线程确实是一个真实且未被占据的空白位置。目前没有找到任何论文建立 calibration → hackability 的因果链接。
   - (+) Causal isolation 方法论（利用 post-hoc calibration 的 representation-preserving 特性来分离因果效应）在方法论上是巧妙的。
   - (−) CGSP 的核心公式 r̃_t = μ_t − α·σ_t/√c_t 与 2604.26360 的 uncertainty-aware reward discounting、PURM 的 Gaussian-based pessimism 在概念上高度重合。step-level 和 calibration-grounded 是差异点，但属于增量创新而非范式转变。
   - (−) "better calibrated → harder to hack" 可能是一个 reviewer 会认为"I would have guessed this"的发现。核心 insight 的惊喜度有限。

2. **Significance: 中偏强** —
   - (+) PRM reward hacking 是一个重要且时效性强的问题，影响所有使用 PRM 进行 RL 训练的系统。
   - (+) 如果因果链接被确认，对 PRM 设计有直接指导意义：PRM 开发者应优先保证 calibration quality。
   - (+) CGSP 如果有效，可直接集成到现有 GRPO/PPO 训练流程。
   - (−) 如果核心发现是近似重言式的（calibration 修正 overestimation → 自然减少 hacking），对领域的认知推进有限。
   - (−) Step-level Hessian analysis 的可推广性存疑——在不同架构/规模上结论是否一致？

3. **Related Work: 中偏弱** —
   - (+) 对 PRM calibration 线和 PRM hackability 线的覆盖比较充分，引用的核心论文均真实存在且描述准确。
   - (+) 与 Ackermann et al. 的差异化定位清晰合理。
   - (−) **遗漏了 2604.26360 (Uncertainty-Aware Reward Discounting)**，这是与 CGSP 最直接竞争的工作，概念重叠显著。此遗漏会被审稿人直接指出。
   - (−) **遗漏了 PURM (arXiv:2503.22480)**，同样用 uncertainty/分布化方法对 reward 做 pessimistic adjustment。
   - (−) 未讨论 PET (Pessimistic Reward Fine-Tuning) 的具体方法论——仅一笔带过"uses global pessimism"。
   - (−) Proposal 声称"零交叉引用"，但未提供检索证据。如果审稿人发现相关 workshop paper 或 concurrent work，这个 claim 会被削弱。


【概率估计】: [22% - 32%] 中位 27%

【估计理由】:
Novelty 是限制上界的主要维度。虽然 bridging two threads 的定位是真实的空白，但 (a) 核心发现（calibration → robustness）的 surprise value 有限——审稿人大概率会说"I would have guessed this"；(b) CGSP 作为方法贡献与 2604.26360 和 PURM 的概念重叠使 novelty claim 被削弱。Significance 是支撑下界的维度——问题确实重要、时效性强，即使 insight 不够 surprising，系统性的 causal study + 48 配置的 empirical evidence 本身也有贡献。Related work 的遗漏（2604.26360）是一个可修复但目前存在的风险。整体看，这是一个 "solid but not surprising" 类型的 idea，方法论严谨但 insight ceiling 受限于近似重言式的威胁。中位 27% 反映了"idea 方向正确、有真实 novelty delta，但核心发现审稿人可能觉得 expected"的定位。

【主要风险】:
1. **Near-tautology 风险**: "Better calibrated PRM → less hackable" 可能被审稿人认为是 trivially expected 的结论。如果 causal study 只是确认了这个直觉而没有 unexpected 发现（如 calibration 在某些 regime 反而增加 vulnerability、或 post-hoc calibration 的效果量远超/远低于预期），论文的 intellectual contribution 会受质疑。
2. **CGSP novelty 被竞争工作稀释**: 2604.26360 (Uncertainty-Aware Reward Discounting) 和 PURM 已经在做 uncertainty-based reward pessimism for anti-hacking。CGSP 的 step-level + calibration-grounded 差异化可能不足以说服审稿人这是一个本质不同的方法。
```

Sources:
- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)
- [Know What You Don't Know: Uncertainty Calibration of Process Reward Models](https://arxiv.org/abs/2506.09338)
- [Distributional Process Reward Models](https://arxiv.org/abs/2605.06785)
- [Gradient Regularization Prevents Reward Hacking in RLHF](https://arxiv.org/abs/2602.18037)
- [From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism](https://arxiv.org/abs/2604.04648)
- [Inference-Time Reward Hacking in Large Language Models](https://arxiv.org/abs/2506.19248)
- [Uncertainty-Aware Reward Discounting for Mitigating Reward Hacking](https://arxiv.org/abs/2604.26360)
- [Adversarial Training for Process Reward Models](https://arxiv.org/abs/2511.22888)
- [Probabilistic Uncertain Reward Model (PURM)](https://arxiv.org/pdf/2503.22480)
- [Pessimistic Reward Modeling in RLHF against Reward Hacking](https://openreview.net/forum?id=mKPpS6n3cZ)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2136153a-333e-4082-9c6a-0d9ce2cd1fde",
  "isSidechain": false,
  "requestId": "req_011CbDJ1RtE5PxGTFTx8tQNc",
  "type": "assistant",
  "uuid": "a2b897bf-f304-4165-b984-44d42ca35fa3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZYBsWE6RPYfFj1xurJg9b",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 27002,
      "output_tokens": 5699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 728,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5699,
          "cache_read_input_tokens": 27002,
          "cache_creation_input_tokens": 728,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 728
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
  "leafUuid": "a2b897bf-f304-4165-b984-44d42ca35fa3",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "PRM calibration quality and reward hacking resistance",
  "sessionId": "e8828fd2-61a1-4417-b87e-354620af4528"
}
```

---
