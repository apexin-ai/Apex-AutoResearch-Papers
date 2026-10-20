# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # How Fragile Is Safety Under Retra

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d.jsonl`
- **Structured JSON:** [`d556ebb852edb5103663.json`](../../sessions/d5/d556ebb852edb5103663.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T21:02:45.692Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T21:02:45.692Z",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# How Fragile Is Safety Under Retraining? A Large-Scale Reproducibility Audit of Post-Training Alignment\n\n## Description\nPreliminary evidence shows that safety alignment is fragile: Larsen (2025) found 18–28% of prompts flip between refusal and compliance across inference seeds, and Fraser et al. (2025) found up to 9-percentage-point variance in harmfulness scores across 5 SFT seeds on small models using LoRA. Yet no study has systematically measured training-time safety reproducibility for the preference optimization methods (DPO, PPO-RLHF, GRPO) that actually power deployed alignment, characterized how fragility scales with model size, disentangled LoRA initialization variance from seed variance, or provided power-justified minimum-seed recommendations for reliable safety claims. We propose the first large-scale training-time safety reproducibility audit of preference-based alignment. Using TRL v1.0's unified training stack with full fine-tuning throughout (eliminating LoRA initialization as a confound), we train DPO, PPO-RLHF, and GRPO on Qwen3-Instruct at 1.7B, 4B, and 8B scales with 20 seeds per configuration using PKU-SafeRLHF-30K safety preference data (~260 total runs including hardware and reward model ablations). The three algorithms cover distinct paradigms: offline preference optimization (DPO), online reward-model-based RL (PPO with Skywork/ArmoRM/FsfairX reward models), and online classifier-based RL (GRPO with WildGuard as safety reward). We evaluate on WildGuard, HarmBench, SORRY-Bench, and four capability benchmarks under a fixed evaluation pipeline. We introduce SCI-T (Safety Consistency Index for Training), extending Larsen's inference-time SSI to training-time: while SSI measures agreement across sampling randomness with fixed weights, SCI-T measures agreement across different training seeds under fixed inference—capturing fundamentally different learned safety boundaries. We decompose variance via ANOVA across seed, algorithm, scale, hardware, and reward model factors, testing the central hypothesis that safety is significantly more fragile than capabilities under retraining. A priori power analysis using Fraser et al.'s empirical variance (σ̂_safety ≈ 3.9pp) and OXRL's capability baseline (σ̂_capability ≈ 0.55pp) confirms 20 seeds provides ≥88% power for detecting safety/capability variance ratios ≥3:1 and ≥82% power for ANOVA interaction effects. The primary deliverable is empirically-grounded minimum-seed lookup tables for AI governance frameworks.\n\n## Core Problem\nWhen the same preference-based alignment algorithm (DPO/PPO-RLHF/GRPO) is rerun with different random seeds, hardware configurations, or reward model instances, how much do safety properties—refusal behavior, harmlessness scores, and instance-level safety decisions—vary compared to general capabilities? Preliminary evidence from SFT (Fraser et al. 2025) and inference-time sampling (Larsen 2025) shows safety decisions are surprisingly inconsistent, but no study has systematically measured training-time safety reproducibility for the preference optimization methods that actually power deployed safety alignment (PPO-RLHF at OpenAI/Anthropic, DPO in open-source pipelines, GRPO at DeepSeek), or characterized how this fragility scales with model size.\n\n## Opportunity\nThree converging lines of evidence create a clear gap. First, Larsen (arXiv:2512.12066) introduced the Safety Stability Index (SSI) showing 18–28% of prompts flip between refusal and compliance across inference seeds and temperatures—but this measures generation-level variance with fixed model weights, not the deeper question of whether retraining produces models with fundamentally different safety boundaries. Second, Fraser et al. (arXiv:2506.17209) demonstrated up to 9-percentage-point variance in harmfulness scores across 5 SFT seeds on Llama-3.2-1B and Mistral-7B using LoRA with 4-bit quantization and SORRY-Bench—establishing that training-time safety variance exists but leaving preference-based alignment (DPO/PPO/GRPO), larger scales, multi-benchmark evaluation, LoRA-vs-full-FT variance confounds, and formal consistency metrics unexplored. Third, OXRL (arXiv:2603.19335) revealed dramatic scale-dependent ranking inversions across post-training algorithms on capability benchmarks using Qwen 2.5 at 0.5B–7B, but evaluated no safety properties. Fourth, SafeDPO (arXiv:2505.20065, ICLR 2026 Oral) demonstrated that safety alignment via DPO on PKU-SafeRLHF-30K can achieve ~97% harmless ratio, establishing both the dataset and method as mature—but reported no cross-seed variance. Meanwhile, TRL v1.0 (March 2026) now provides a unified training stack for DPO, PPO, and GRPO, eliminating infrastructure confounds. We propose to close this gap with the first large-scale, multi-algorithm, multi-scale reproducibility audit of training-time safety alignment, using full fine-tuning throughout to cleanly isolate training-seed variance from LoRA initialization noise.\n\n## Related Work / Landscape\nLarsen (arXiv:2512.12066, Dec 2025) introduced the SSI metric measuring per-prompt refusal agreement across inference configurations (5 seeds × 4 temperatures), finding 18–28% flip rates on BeaverTails across four 7–12B models. Critically, SSI captures generation-level stochasticity (same weights, different sampling), not model-level variance from retraining. Fraser et al. (arXiv:2506.17209, June 2025, LLMSEC) studied SFT seed variance with 5 seeds on Llama-3.2-1B and Mistral-7B using LoRA with 4-bit quantization and AdamW-8bit optimizer, evaluating on SORRY-Bench (440 class-balanced unsafe instructions); they found up to 9pp harmfulness score variance (e.g., 0.73 to 0.82 on Llama-1B fine-tuned on Dolly) and called for 'multiple runs to estimate random variation' but used only SFT, not preference optimization, and did not disentangle LoRA initialization variance from true seed variance. SafeTuneBed (arXiv:2506.00676, May 2025) offers a fine-tuning safety toolkit that averages results over 3 seeds and lists 'refusal consistency' as a metric but never formally defines or operationalizes it. OXRL (arXiv:2603.19335, March 2026) provides a controlled framework for 51 post-training algorithms using Qwen 2.5 Instruct at 0.5B–7B with full FT at ≤3B and LoRA (rank 16, α=32) at 7B, using 3–5 seeds per configuration on GSM8K self-play data—but evaluates only capability benchmarks with no safety evaluation. Notably, OXRL found scale-dependent ranking inversions (SimPO worst at 1.5B, best at 7B) and cross-seed std of ±0.57pp on GSM8K for SGRPO at 1.5B with 5 seeds, establishing a baseline for capability variance. SafeDPO (arXiv:2505.20065, ICLR 2026 Oral) achieves ~97% harmless ratio using DPO on PKU-SafeRLHF-30K but reports no cross-seed variance. The 'LLM-Safety Evaluations Lack Robustness' paper (arXiv:2503.02574, March 2025) demonstrates that evaluation pipeline choices cause up to 28% ASR variance, motivating fixed-evaluation-pipeline designs. SafeGRPO (arXiv:2511.12982, Nov 2025) proposes rule-governed reward construction for GRPO-based safety alignment, demonstrating that safety classifiers can serve as GRPO reward signals—validating our approach to using WildGuard as GRPO's safety reward function. TRL v1.0 (March 2026) provides a unified post-training stack for SFT, DPO, PPO, and GRPO with consistent infrastructure, enabling fair cross-algorithm comparison. PKU-SafeRLHF (arXiv:2406.15513, ACL 2025) provides 30K+ expert comparisons with decoupled safety/helpfulness annotations across 19 harm categories and 3 severity levels—the standard safety preference dataset used by SafeDPO and related work. Open-source reward models (Skywork-Reward-Llama-3.1-8B-v0.2, ArmoRM-Llama3-8B-v0.1, FsfairX-LLaMA3-RM-v0.1) achieve strong RewardBench scores including explicit safety dimensions, enabling controlled reward model ablations for PPO. No published work combines: (a) three distinct alignment paradigms (offline DPO, online PPO-RLHF, online GRPO), (b) multiple model scales with full fine-tuning, (c) ≥20 seeds per configuration with a priori power justification, (d) multiple safety benchmarks with fixed evaluation pipeline, (e) a formal training-time consistency metric, and (f) separated variance decomposition across seed, algorithm, scale, hardware, and reward model factors.\n\n## Approach\nPhase 1 — Infrastructure (3 weeks): Build unified training and evaluation pipeline using TRL v1.0 as the training backbone and OXRL-inspired evaluation infrastructure. Training setup: Configure DPO, PPO-RLHF, and GRPO trainers in TRL v1.0 with full fine-tuning at all scales using DeepSpeed ZeRO-2 for memory management at 8B. We use full fine-tuning throughout (not LoRA) to eliminate LoRA random A/B matrix initialization as a variance source—a confound identified in Fraser et al.'s LoRA-based SFT study where LoRA initialization and seed variance were entangled. This increases compute by ~50% at 8B but produces cleaner variance isolation, which is essential for a paper whose central contribution is variance decomposition. Preference dataset: PKU-SafeRLHF-30K (PKU-Alignment, ACL 2025), selected for three reasons: (i) decoupled safety/helpfulness annotations enable isolating safety-specific preference learning, (ii) it is the standard benchmark used by SafeDPO (ICLR 2026 Oral) enabling direct comparability, (iii) 19 harm categories with 3 severity levels enable fine-grained analysis of which safety dimensions are most fragile. Dataset adaptation per algorithm: DPO receives safety preference pairs directly (safer response as chosen, less safe as rejected); PPO uses the 27K prompts with an external reward model scoring generated responses; GRPO uses the same prompts with WildGuard (7B) as a binary safety classifier reward (safe=1, unsafe=0), following the classifier-as-reward paradigm validated by SafeGRPO (arXiv:2511.12982). Evaluation pipeline: Fix the evaluation pipeline completely (WildGuard as primary safety judge, deterministic decoding at temperature=0, fixed chat template, bf16 quantization) per the robustness findings of arXiv:2503.02574 to isolate training-time variance from evaluation-time variance. Integrate WildGuard (prompt + response classification, 7B Mistral-based), HarmBench (400 harmful behaviors with 7B Mistral classifier), SORRY-Bench (440 category-balanced unsafe instructions), and capability benchmarks (GSM8K, MATH, AlpacaEval 2, MT-Bench).\n\nPhase 2 — Training Runs (6–7 weeks): Algorithm selection rationale: We select DPO, PPO-RLHF, and GRPO to cover three fundamentally distinct alignment paradigms—(i) DPO: offline, reference-model-regularized preference optimization without a reward model, the dominant method in open-source safety alignment; (ii) PPO-RLHF: online, reward-model-based reinforcement learning, the method deployed for safety-critical systems at OpenAI and Anthropic; (iii) GRPO: online, group-relative optimization with classifier-based rewards, the emerging paradigm (DeepSeek-R1) increasingly applied to safety via SafeGRPO. This replaces the originally proposed SimPO, which is architecturally a DPO variant (reference-free but still offline preference optimization)—including both DPO and SimPO would over-represent the offline paradigm while leaving online RL unrepresented, creating an algorithmic coverage gap for the methods that actually power deployed safety alignment. Core runs: Train DPO, PPO, and GRPO on Qwen3-Instruct at three scales (1.7B, 4B, 8B) with 20 random seeds each, holding all hyperparameters fixed per algorithm. Full fine-tuning with DeepSpeed ZeRO-2; 1 H100 for 1.7B/4B DPO/GRPO, 2 H100s for 8B and all PPO runs (policy + reference + reward/value models). Total core: 180 runs (3 × 3 × 20). Hardware ablation: For the 8B DPO configuration, run 20 seeds on A100-80GB vs H100-80GB and 20 seeds with bf16 vs fp16 to isolate hardware/precision effects (40 additional runs, comparing against the 20 core H100/bf16 runs). Reward model ablation: For the 8B PPO configuration, run 20 seeds each with three independently-developed open-source reward models: (RM1) Skywork-Reward-Llama-3.1-8B-v0.2 — Bradley-Terry RM, #1 on RewardBench among 8B models, trained on Skywork's curated preference data; (RM2) ArmoRM-Llama3-8B-v0.1 — multi-objective RM with mixture-of-experts gating across 19 reward dimensions including an explicit safety objective, 89.0 RewardBench overall; (RM3) FsfairX-LLaMA3-RM-v0.1 — Bradley-Terry RM trained on the RLHFlow dataset, different training distribution from Skywork. The core PPO runs use ArmoRM as default (its explicit safety dimension makes it most appropriate for safety alignment); the ablation adds 40 additional runs with Skywork-RM and FsfairX-RM. All three RMs are ~8B parameters, Llama-3-based, publicly available, and independently trained with different objectives, architectures (Bradley-Terry vs MoE-gated multi-objective), and training data—providing genuine variance in the reward signal. Total runs: 180 core + 40 hardware + 40 reward model = 260 runs.\n\nPhase 3 — Evaluation and Analysis (3–4 weeks): For each of 260 checkpoints, evaluate safety (WildGuard refusal rate on WildGuardTest 5K subset, HarmBench ASR with 400 behaviors, SORRY-Bench harmfulness with 440 prompts) and capabilities (GSM8K 1.3K, MATH 5K, AlpacaEval 2 805 prompts, MT-Bench 80 turns). All safety evaluations use deterministic decoding (temperature=0) to ensure SCI-T captures training-time variance only. Introduce the Safety Consistency Index for Training (SCI-T), explicitly extending Larsen's SSI from inference-time to training-time: SCI-T(p) = max_c(n_c) / K where n_c counts training-seed runs in category c ∈ {REFUSE, COMPLY} and K = number of seeds. While SSI measures whether the same model produces consistent safety decisions across sampling randomness, SCI-T measures whether different models (from different training seeds) make consistent safety decisions under fixed inference conditions (temperature=0). This distinction matters because training-time inconsistency implies fundamentally different learned safety boundaries, not mere sampling noise. Compute SCI-T for every prompt × algorithm × scale combination. Apply ANOVA decomposition: Var(safety_metric) = Var(seed) + Var(algorithm) + Var(scale) + Var(hardware) + Var(reward_model) + Var(algorithm×scale) + residual. Test the central hypothesis: safety properties exhibit significantly higher cross-seed variance than capability properties at the same scale, and this differential fragility changes with scale. Additionally analyze which of PKU-SafeRLHF's 19 harm categories show highest SCI-T fragility—identifying 'fragile safety categories' that are most sensitive to training randomness.\n\nPhase 4 — Minimum-Seed Recommendations (2–3 weeks): A priori power justification for 20 seeds: We apply Cédric et al.'s (2018) framework to our own experimental design before running. From Fraser et al.'s empirical data: 5 SFT seeds on Llama-1B produced harmfulness scores ranging 0.73–0.82, yielding σ̂_safety ≈ 3.9pp (range/d₂ for n=5). From OXRL: 5 SGRPO seeds at 1.5B on GSM8K produced ±0.57pp std, yielding σ̂_capability ≈ 0.55pp. For our central F-test (H₀: σ²_safety = σ²_capability vs H₁: σ²_safety > σ²_capability) with df=(19,19): at true variance ratio λ=3 (conservative estimate from Fraser/OXRL data suggesting λ≈50), power ≥ 0.88 at α=0.05. For ANOVA main effects (3 levels, N=180, medium effect f=0.25): power ≈ 0.92. For ANOVA interactions (3×3 design, df=(4,171)): power ≈ 0.82 for medium effects. For variance estimation precision: with n=20 (df=19), the 95% CI for σ² spans a factor of 3.69 (χ²_{0.975,19}/χ²_{0.025,19} = 32.85/8.91), sufficient for categorizing configurations as 'high-fragility' vs 'low-fragility.' Conclusion: 20 seeds per cell provides ≥80% power for all planned analyses, meeting the standard power threshold. Adaptive provision: if Phase 2 pilot (first 5 seeds per cell) reveals smaller effect sizes than estimated, we increase to 25 seeds with ~25% additional compute within budget contingency. Post-hoc deliverable: Using the full empirical variance estimates, derive minimum seed counts needed for P(detecting a true safety difference ≥ δ) ≥ 0.8 at α=0.05 via inverse power analysis. Produce concrete lookup tables: 'To claim safety refusal rate ≥ R% with 95% confidence for algorithm X at scale Y, run ≥ N seeds.' This is the actionable regulatory deliverable targeting EU AI Act verifiable safety requirements and NIST AI RMF reproducibility standards.\n\n## Inspiration\nExtension: Larsen's SSI measures inference-time safety agreement; we extend this concept to training-time agreement across different model weights, a fundamentally harder reproducibility challenge since different weights may encode different safety boundaries. Scale-up: Fraser et al.'s SFT seed study (2 models, 5 seeds, 1 benchmark, LoRA) demonstrated the phenomenon exists; we scale to 3 algorithms × 3 model sizes × 20 seeds × 4 benchmarks with full fine-tuning (eliminating LoRA initialization variance) and formal ANOVA decomposition. Bridge: OXRL's controlled post-training infrastructure + TRL v1.0's unified training stack + PKU-SafeRLHF-30K's decoupled safety preference data + WildGuard/HarmBench classifiers can be composed to create a safety-aware reproducibility audit pipeline that none provides alone. Safety reward signals: SafeGRPO's demonstration that safety classifiers can serve as GRPO reward functions validates our approach to using WildGuard as GRPO's reward signal for safety alignment. Reward model variance: ArmoRM's multi-objective design (with explicit safety dimension), Skywork-Reward's top RewardBench performance, and FsfairX's Bradley-Terry approach provide three independently-trained reward models for PPO ablation, operationalizing RVPO's concern about inter-reward variance. Statistical grounding: Cédric et al.'s power analysis framework for RL seed selection (arXiv:1806.08295) provides the methodology for deriving minimum-seed recommendations—never applied to safety alignment. We apply it a priori to justify our 20-seed design.\n\n## Key References\n- The Instability of Safety: How Random Seeds and Temperature Expose Inconsistent LLM Refusal Behavior (arXiv:2512.12066, Dec 2025) — introduces SSI metric for inference-time refusal consistency; SCI-T extends SSI to training-time\n- Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency (arXiv:2506.17209, June 2025, LLMSEC) — first evidence of training-seed safety variance: 9pp range across 5 SFT seeds on Llama-1B with LoRA/4-bit, SORRY-Bench; establishes σ̂_safety ≈ 3.9pp used in our power analysis\n- SafeTuneBed: A Toolkit for Benchmarking LLM Safety Alignment in Fine-Tuning (arXiv:2506.00676, May 2025) — safety fine-tuning toolkit with 3-seed averaging; mentions 'refusal consistency' without formal definition\n- Do Post-Training Algorithms Actually Differ? A Controlled Study Across Model Scales (arXiv:2603.19335, March 2026) — OXRL framework, Qwen 2.5 at 0.5B–7B, scale-dependent ranking inversions, ±0.57pp GSM8K std providing σ̂_capability baseline for our power analysis\n- LLM-Safety Evaluations Lack Robustness (arXiv:2503.02574, March 2025) — evaluation pipeline variance up to 28%, motivates our fixed-pipeline design\n- PKU-SafeRLHF: Towards Multi-Level Safety Alignment for LLMs with Human Preference (arXiv:2406.15513, ACL 2025) — 30K+ expert comparisons with decoupled safety/helpfulness annotations across 19 harm categories; our primary training dataset\n- SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety (arXiv:2505.20065, ICLR 2026 Oral) — achieves ~97% harmless ratio via DPO on PKU-SafeRLHF-30K; establishes dataset+method maturity but reports no cross-seed variance\n- SafeGRPO: Self-Rewarded Multimodal Safety Alignment via Rule-Governed Policy Optimization (arXiv:2511.12982, Nov 2025) — validates classifier-as-reward paradigm for GRPO safety alignment; motivates our WildGuard-as-reward design\n- TRL v1.0: Post-Training Library Built to Move with the Field (Hugging Face, March 2026) — unified training stack for DPO, PPO, GRPO eliminating infrastructure confounds across algorithms\n- How Many Random Seeds? Statistical Power Analysis in Deep RL Experiments (arXiv:1806.08295, 2018) — methodology for minimum-seed derivation via power analysis; we extend to safety alignment and apply a priori to justify our 20-seed design\n- What Matters For Safety Alignment? (arXiv:2601.03868, Jan 2026) — cross-model safety comparison across 32 models and 13 families\n- WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs (arXiv:2406.18495, 2024) — 7B safety classifier achieving 94.7% F1 on response harmfulness; our primary safety judge and GRPO reward signal\n- Skywork-Reward: Bag of Tricks for Reward Modeling in LLMs (arXiv:2410.18451, 2024) — Skywork-Reward-Llama-3.1-8B-v0.2, #1 8B model on RewardBench; one of three PPO reward models in our ablation\n- Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts (arXiv:2406.12845, 2024) — ArmoRM-Llama3-8B-v0.1, 89.0 RewardBench with explicit safety dimension; default PPO reward model\n- Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping (arXiv 2020) — seed variance methodology for NLP\n- Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning LLMs (IJCNLP-AACL 2025) — macro/micro consistency metrics for LLM fine-tuning\n- RVPO: Risk-Sensitive Alignment via Variance Regularization (arXiv:2605.05750, May 2026) — inter-reward variance penalization in single runs; motivates reward model ablation\n- Improving Safety Alignment via Balanced Direct Preference Optimization (arXiv:2603.22829, March 2026) — safety alignment overfitting in DPO\n- Safety Training Persists Through Helpfulness Optimization in LLM Agents (arXiv:2603.02229, March 2026) — safety-helpfulness Pareto frontier under DPO\n- Reproducibility in Machine-Learning-Based Research: Overview, Barriers, and Drivers (AI Magazine 2025)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '~2,800 H100-hours total: ~1,600 training (260 runs across 3 algorithms × 3 scales × 20+ seeds, all full fine-tuning with DeepSpeed ZeRO-2; PPO runs require 2 H100s for policy+reference+RM) + ~1,200 evaluation (260 checkpoints × 8 benchmarks including WildGuard 7B and HarmBench 7B classifier inference, each checkpoint requiring ~3-4 GPU-hours for generation + classification across all benchmarks)', 'timeline': '17–19 weeks (infrastructure + TRL v1.0 pipeline setup 3w, training runs 6–7w on 8×H100 cluster, evaluation 3–4w, statistical analysis + minimum-seed derivation + paper writing 5–6w)', 'estimated_gpu_cost': '$7,000 at ~$2.50/H100-hr on mid-tier providers'}\n- **human_in_loop**: {'gpu_hours': '~2,800 H100-hours (identical core compute; full FT precludes further memory optimization)', 'timeline': '14–16 weeks (Claude accelerates TRL v1.0 pipeline integration, ANOVA analysis scripts, power analysis code, per-category fragility analysis, and paper drafting)', 'claude_api_cost': '$500–700 (Sonnet 4.6 for code generation, statistical analysis automation, and drafting; ~150M tokens)', 'estimated_gpu_cost': '$7,000'}\n- **auto_research**: {'gpu_hours': '~2,800 H100-hours', 'timeline': '11–14 weeks (parallelized experiment orchestration with automated sweep management, evaluation pipelines, and ANOVA analysis)', 'claude_api_cost': '$1,500–2,200 (experiment orchestration, automated analysis, full paper draft generation; ~600M tokens)', 'estimated_gpu_cost': '$7,000', 'speed_bottleneck': 'GPU cluster queue time for 260 training jobs (PPO runs ~2× longer than DPO/GRPO due to multi-model training); sequential dependency between training completion and safety evaluation; WildGuard 7B + HarmBench 7B classifier inference throughput across 260 checkpoints × ~6K safety evaluation prompts each'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T21:02:45.697Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T21:02:45.697Z",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-19T21:02:45.713Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# How Fragile Is Safety Under Retraining? A Large-Scale Reproducibility Audit of Post-Training Alignment

## Description
Preliminary evidence shows that safety alignment is fragile: Larsen (2025) found 18–28% of prompts flip between refusal and compliance across inference seeds, and Fraser et al. (2025) found up to 9-percentage-point variance in harmfulness scores across 5 SFT seeds on small models using LoRA. Yet no study has systematically measured training-time safety reproducibility for the preference optimization methods (DPO, PPO-RLHF, GRPO) that actually power deployed alignment, characterized how fragility scales with model size, disentangled LoRA initialization variance from seed variance, or provided power-justified minimum-seed recommendations for reliable safety claims. We propose the first large-scale training-time safety reproducibility audit of preference-based alignment. Using TRL v1.0's unified training stack with full fine-tuning throughout (eliminating LoRA initialization as a confound), we train DPO, PPO-RLHF, and GRPO on Qwen3-Instruct at 1.7B, 4B, and 8B scales with 20 seeds per configuration using PKU-SafeRLHF-30K safety preference data (~260 total runs including hardware and reward model ablations). The three algorithms cover distinct paradigms: offline preference optimization (DPO), online reward-model-based RL (PPO with Skywork/ArmoRM/FsfairX reward models), and online classifier-based RL (GRPO with WildGuard as safety reward). We evaluate on WildGuard, HarmBench, SORRY-Bench, and four capability benchmarks under a fixed evaluation pipeline. We introduce SCI-T (Safety Consistency Index for Training), extending Larsen's inference-time SSI to training-time: while SSI measures agreement across sampling randomness with fixed weights, SCI-T measures agreement across different training seeds under fixed inference—capturing fundamentally different learned safety boundaries. We decompose variance via ANOVA across seed, algorithm, scale, hardware, and reward model factors, testing the central hypothesis that safety is significantly more fragile than capabilities under retraining. A priori power analysis using Fraser et al.'s empirical variance (σ̂_safety ≈ 3.9pp) and OXRL's capability baseline (σ̂_capability ≈ 0.55pp) confirms 20 seeds provides ≥88% power for detecting safety/capability variance ratios ≥3:1 and ≥82% power for ANOVA interaction effects. The primary deliverable is empirically-grounded minimum-seed lookup tables for AI governance frameworks.

## Core Problem
When the same preference-based alignment algorithm (DPO/PPO-RLHF/GRPO) is rerun with different random seeds, hardware configurations, or reward model instances, how much do safety properties—refusal behavior, harmlessness scores, and instance-level safety decisions—vary compared to general capabilities? Preliminary evidence from SFT (Fraser et al. 2025) and inference-time sampling (Larsen 2025) shows safety decisions are surprisingly inconsistent, but no study has systematically measured training-time safety reproducibility for the preference optimization methods that actually power deployed safety alignment (PPO-RLHF at OpenAI/Anthropic, DPO in open-source pipelines, GRPO at DeepSeek), or characterized how this fragility scales with model size.

## Opportunity
Three converging lines of evidence create a clear gap. First, Larsen (arXiv:2512.12066) introduced the Safety Stability Index (SSI) showing 18–28% of prompts flip between refusal and compliance across inference seeds and temperatures—but this measures generation-level variance with fixed model weights, not the deeper question of whether retraining produces models with fundamentally different safety boundaries. Second, Fraser et al. (arXiv:2506.17209) demonstrated up to 9-percentage-point variance in harmfulness scores across 5 SFT seeds on Llama-3.2-1B and Mistral-7B using LoRA with 4-bit quantization and SORRY-Bench—establishing that training-time safety variance exists but leaving preference-based alignment (DPO/PPO/GRPO), larger scales, multi-benchmark evaluation, LoRA-vs-full-FT variance confounds, and formal consistency metrics unexplored. Third, OXRL (arXiv:2603.19335) revealed dramatic scale-dependent ranking inversions across post-training algorithms on capability benchmarks using Qwen 2.5 at 0.5B–7B, but evaluated no safety properties. Fourth, SafeDPO (arXiv:2505.20065, ICLR 2026 Oral) demonstrated that safety alignment via DPO on PKU-SafeRLHF-30K can achieve ~97% harmless ratio, establishing both the dataset and method as mature—but reported no cross-seed variance. Meanwhile, TRL v1.0 (March 2026) now provides a unified training stack for DPO, PPO, and GRPO, eliminating infrastructure confounds. We propose to close this gap with the first large-scale, multi-algorithm, multi-scale reproducibility audit of training-time safety alignment, using full fine-tuning throughout to cleanly isolate training-seed variance from LoRA initialization noise.

## Related Work / Landscape
Larsen (arXiv:2512.12066, Dec 2025) introduced the SSI metric measuring per-prompt refusal agreement across inference configurations (5 seeds × 4 temperatures), finding 18–28% flip rates on BeaverTails across four 7–12B models. Critically, SSI captures generation-level stochasticity (same weights, different sampling), not model-level variance from retraining. Fraser et al. (arXiv:2506.17209, June 2025, LLMSEC) studied SFT seed variance with 5 seeds on Llama-3.2-1B and Mistral-7B using LoRA with 4-bit quantization and AdamW-8bit optimizer, evaluating on SORRY-Bench (440 class-balanced unsafe instructions); they found up to 9pp harmfulness score variance (e.g., 0.73 to 0.82 on Llama-1B fine-tuned on Dolly) and called for 'multiple runs to estimate random variation' but used only SFT, not preference optimization, and did not disentangle LoRA initialization variance from true seed variance. SafeTuneBed (arXiv:2506.00676, May 2025) offers a fine-tuning safety toolkit that averages results over 3 seeds and lists 'refusal consistency' as a metric but never formally defines or operationalizes it. OXRL (arXiv:2603.19335, March 2026) provides a controlled framework for 51 post-training algorithms using Qwen 2.5 Instruct at 0.5B–7B with full FT at ≤3B and LoRA (rank 16, α=32) at 7B, using 3–5 seeds per configuration on GSM8K self-play data—but evaluates only capability benchmarks with no safety evaluation. Notably, OXRL found scale-dependent ranking inversions (SimPO worst at 1.5B, best at 7B) and cross-seed std of ±0.57pp on GSM8K for SGRPO at 1.5B with 5 seeds, establishing a baseline for capability variance. SafeDPO (arXiv:2505.20065, ICLR 2026 Oral) achieves ~97% harmless ratio using DPO on PKU-SafeRLHF-30K but reports no cross-seed variance. The 'LLM-Safety Evaluations Lack Robustness' paper (arXiv:2503.02574, March 2025) demonstrates that evaluation pipeline choices cause up to 28% ASR variance, motivating fixed-evaluation-pipeline designs. SafeGRPO (arXiv:2511.12982, Nov 2025) proposes rule-governed reward construction for GRPO-based safety alignment, demonstrating that safety classifiers can serve as GRPO reward signals—validating our approach to using WildGuard as GRPO's safety reward function. TRL v1.0 (March 2026) provides a unified post-training stack for SFT, DPO, PPO, and GRPO with consistent infrastructure, enabling fair cross-algorithm comparison. PKU-SafeRLHF (arXiv:2406.15513, ACL 2025) provides 30K+ expert comparisons with decoupled safety/helpfulness annotations across 19 harm categories and 3 severity levels—the standard safety preference dataset used by SafeDPO and related work. Open-source reward models (Skywork-Reward-Llama-3.1-8B-v0.2, ArmoRM-Llama3-8B-v0.1, FsfairX-LLaMA3-RM-v0.1) achieve strong RewardBench scores including explicit safety dimensions, enabling controlled reward model ablations for PPO. No published work combines: (a) three distinct alignment paradigms (offline DPO, online PPO-RLHF, online GRPO), (b) multiple model scales with full fine-tuning, (c) ≥20 seeds per configuration with a priori power justification, (d) multiple safety benchmarks with fixed evaluation pipeline, (e) a formal training-time consistency metric, and (f) separated variance decomposition across seed, algorithm, scale, hardware, and reward model factors.

## Approach
Phase 1 — Infrastructure (3 weeks): Build unified training and evaluation pipeline using TRL v1.0 as the training backbone and OXRL-inspired evaluation infrastructure. Training setup: Configure DPO, PPO-RLHF, and GRPO trainers in TRL v1.0 with full fine-tuning at all scales using DeepSpeed ZeRO-2 for memory management at 8B. We use full fine-tuning throughout (not LoRA) to eliminate LoRA random A/B matrix initialization as a variance source—a confound identified in Fraser et al.'s LoRA-based SFT study where LoRA initialization and seed variance were entangled. This increases compute by ~50% at 8B but produces cleaner variance isolation, which is essential for a paper whose central contribution is variance decomposition. Preference dataset: PKU-SafeRLHF-30K (PKU-Alignment, ACL 2025), selected for three reasons: (i) decoupled safety/helpfulness annotations enable isolating safety-specific preference learning, (ii) it is the standard benchmark used by SafeDPO (ICLR 2026 Oral) enabling direct comparability, (iii) 19 harm categories with 3 severity levels enable fine-grained analysis of which safety dimensions are most fragile. Dataset adaptation per algorithm: DPO receives safety preference pairs directly (safer response as chosen, less safe as rejected); PPO uses the 27K prompts with an external reward model scoring generated responses; GRPO uses the same prompts with WildGuard (7B) as a binary safety classifier reward (safe=1, unsafe=0), following the classifier-as-reward paradigm validated by SafeGRPO (arXiv:2511.12982). Evaluation pipeline: Fix the evaluation pipeline completely (WildGuard as primary safety judge, deterministic decoding at temperature=0, fixed chat template, bf16 quantization) per the robustness findings of arXiv:2503.02574 to isolate training-time variance from evaluation-time variance. Integrate WildGuard (prompt + response classification, 7B Mistral-based), HarmBench (400 harmful behaviors with 7B Mistral classifier), SORRY-Bench (440 category-balanced unsafe instructions), and capability benchmarks (GSM8K, MATH, AlpacaEval 2, MT-Bench).

Phase 2 — Training Runs (6–7 weeks): Algorithm selection rationale: We select DPO, PPO-RLHF, and GRPO to cover three fundamentally distinct alignment paradigms—(i) DPO: offline, reference-model-regularized preference optimization without a reward model, the dominant method in open-source safety alignment; (ii) PPO-RLHF: online, reward-model-based reinforcement learning, the method deployed for safety-critical systems at OpenAI and Anthropic; (iii) GRPO: online, group-relative optimization with classifier-based rewards, the emerging paradigm (DeepSeek-R1) increasingly applied to safety via SafeGRPO. This replaces the originally proposed SimPO, which is architecturally a DPO variant (reference-free but still offline preference optimization)—including both DPO and SimPO would over-represent the offline paradigm while leaving online RL unrepresented, creating an algorithmic coverage gap for the methods that actually power deployed safety alignment. Core runs: Train DPO, PPO, and GRPO on Qwen3-Instruct at three scales (1.7B, 4B, 8B) with 20 random seeds each, holding all hyperparameters fixed per algorithm. Full fine-tuning with DeepSpeed ZeRO-2; 1 H100 for 1.7B/4B DPO/GRPO, 2 H100s for 8B and all PPO runs (policy + reference + reward/value models). Total core: 180 runs (3 × 3 × 20). Hardware ablation: For the 8B DPO configuration, run 20 seeds on A100-80GB vs H100-80GB and 20 seeds with bf16 vs fp16 to isolate hardware/precision effects (40 additional runs, comparing against the 20 core H100/bf16 runs). Reward model ablation: For the 8B PPO configuration, run 20 seeds each with three independently-developed open-source reward models: (RM1) Skywork-Reward-Llama-3.1-8B-v0.2 — Bradley-Terry RM, #1 on RewardBench among 8B models, trained on Skywork's curated preference data; (RM2) ArmoRM-Llama3-8B-v0.1 — multi-objective RM with mixture-of-experts gating across 19 reward dimensions including an explicit safety objective, 89.0 RewardBench overall; (RM3) FsfairX-LLaMA3-RM-v0.1 — Bradley-Terry RM trained on the RLHFlow dataset, different training distribution from Skywork. The core PPO runs use ArmoRM as default (its explicit safety dimension makes it most appropriate for safety alignment); the ablation adds 40 additional runs with Skywork-RM and FsfairX-RM. All three RMs are ~8B parameters, Llama-3-based, publicly available, and independently trained with different objectives, architectures (Bradley-Terry vs MoE-gated multi-objective), and training data—providing genuine variance in the reward signal. Total runs: 180 core + 40 hardware + 40 reward model = 260 runs.

Phase 3 — Evaluation and Analysis (3–4 weeks): For each of 260 checkpoints, evaluate safety (WildGuard refusal rate on WildGuardTest 5K subset, HarmBench ASR with 400 behaviors, SORRY-Bench harmfulness with 440 prompts) and capabilities (GSM8K 1.3K, MATH 5K, AlpacaEval 2 805 prompts, MT-Bench 80 turns). All safety evaluations use deterministic decoding (temperature=0) to ensure SCI-T captures training-time variance only. Introduce the Safety Consistency Index for Training (SCI-T), explicitly extending Larsen's SSI from inference-time to training-time: SCI-T(p) = max_c(n_c) / K where n_c counts training-seed runs in category c ∈ {REFUSE, COMPLY} and K = number of seeds. While SSI measures whether the same model produces consistent safety decisions across sampling randomness, SCI-T measures whether different models (from different training seeds) make consistent safety decisions under fixed inference conditions (temperature=0). This distinction matters because training-time inconsistency implies fundamentally different learned safety boundaries, not mere sampling noise. Compute SCI-T for every prompt × algorithm × scale combination. Apply ANOVA decomposition: Var(safety_metric) = Var(seed) + Var(algorithm) + Var(scale) + Var(hardware) + Var(reward_model) + Var(algorithm×scale) + residual. Test the central hypothesis: safety properties exhibit significantly higher cross-seed variance than capability properties at the same scale, and this differential fragility changes with scale. Additionally analyze which of PKU-SafeRLHF's 19 harm categories show highest SCI-T fragility—identifying 'fragile safety categories' that are most sensitive to training randomness.

Phase 4 — Minimum-Seed Recommendations (2–3 weeks): A priori power justification for 20 seeds: We apply Cédric et al.'s (2018) framework to our own experimental design before running. From Fraser et al.'s empirical data: 5 SFT seeds on Llama-1B produced harmfulness scores ranging 0.73–0.82, yielding σ̂_safety ≈ 3.9pp (range/d₂ for n=5). From OXRL: 5 SGRPO seeds at 1.5B on GSM8K produced ±0.57pp std, yielding σ̂_capability ≈ 0.55pp. For our central F-test (H₀: σ²_safety = σ²_capability vs H₁: σ²_safety > σ²_capability) with df=(19,19): at true variance ratio λ=3 (conservative estimate from Fraser/OXRL data suggesting λ≈50), power ≥ 0.88 at α=0.05. For ANOVA main effects (3 levels, N=180, medium effect f=0.25): power ≈ 0.92. For ANOVA interactions (3×3 design, df=(4,171)): power ≈ 0.82 for medium effects. For variance estimation precision: with n=20 (df=19), the 95% CI for σ² spans a factor of 3.69 (χ²_{0.975,19}/χ²_{0.025,19} = 32.85/8.91), sufficient for categorizing configurations as 'high-fragility' vs 'low-fragility.' Conclusion: 20 seeds per cell provides ≥80% power for all planned analyses, meeting the standard power threshold. Adaptive provision: if Phase 2 pilot (first 5 seeds per cell) reveals smaller effect sizes than estimated, we increase to 25 seeds with ~25% additional compute within budget contingency. Post-hoc deliverable: Using the full empirical variance estimates, derive minimum seed counts needed for P(detecting a true safety difference ≥ δ) ≥ 0.8 at α=0.05 via inverse power analysis. Produce concrete lookup tables: 'To claim safety refusal rate ≥ R% with 95% confidence for algorithm X at scale Y, run ≥ N seeds.' This is the actionable regulatory deliverable targeting EU AI Act verifiable safety requirements and NIST AI RMF reproducibility standards.

## Inspiration
Extension: Larsen's SSI measures inference-time safety agreement; we extend this concept to training-time agreement across different model weights, a fundamentally harder reproducibility challenge since different weights may encode different safety boundaries. Scale-up: Fraser et al.'s SFT seed study (2 models, 5 seeds, 1 benchmark, LoRA) demonstrated the phenomenon exists; we scale to 3 algorithms × 3 model sizes × 20 seeds × 4 benchmarks with full fine-tuning (eliminating LoRA initialization variance) and formal ANOVA decomposition. Bridge: OXRL's controlled post-training infrastructure + TRL v1.0's unified training stack + PKU-SafeRLHF-30K's decoupled safety preference data + WildGuard/HarmBench classifiers can be composed to create a safety-aware reproducibility audit pipeline that none provides alone. Safety reward signals: SafeGRPO's demonstration that safety classifiers can serve as GRPO reward functions validates our approach to using WildGuard as GRPO's reward signal for safety alignment. Reward model variance: ArmoRM's multi-objective design (with explicit safety dimension), Skywork-Reward's top RewardBench performance, and FsfairX's Bradley-Terry approach provide three independently-trained reward models for PPO ablation, operationalizing RVPO's concern about inter-reward variance. Statistical grounding: Cédric et al.'s power analysis framework for RL seed selection (arXiv:1806.08295) provides the methodology for deriving minimum-seed recommendations—never applied to safety alignment. We apply it a priori to justify our 20-seed design.

## Key References
- The Instability of Safety: How Random Seeds and Temperature Expose Inconsistent LLM Refusal Behavior (arXiv:2512.12066, Dec 2025) — introduces SSI metric for inference-time refusal consistency; SCI-T extends SSI to training-time
- Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency (arXiv:2506.17209, June 2025, LLMSEC) — first evidence of training-seed safety variance: 9pp range across 5 SFT seeds on Llama-1B with LoRA/4-bit, SORRY-Bench; establishes σ̂_safety ≈ 3.9pp used in our power analysis
- SafeTuneBed: A Toolkit for Benchmarking LLM Safety Alignment in Fine-Tuning (arXiv:2506.00676, May 2025) — safety fine-tuning toolkit with 3-seed averaging; mentions 'refusal consistency' without formal definition
- Do Post-Training Algorithms Actually Differ? A Controlled Study Across Model Scales (arXiv:2603.19335, March 2026) — OXRL framework, Qwen 2.5 at 0.5B–7B, scale-dependent ranking inversions, ±0.57pp GSM8K std providing σ̂_capability baseline for our power analysis
- LLM-Safety Evaluations Lack Robustness (arXiv:2503.02574, March 2025) — evaluation pipeline variance up to 28%, motivates our fixed-pipeline design
- PKU-SafeRLHF: Towards Multi-Level Safety Alignment for LLMs with Human Preference (arXiv:2406.15513, ACL 2025) — 30K+ expert comparisons with decoupled safety/helpfulness annotations across 19 harm categories; our primary training dataset
- SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety (arXiv:2505.20065, ICLR 2026 Oral) — achieves ~97% harmless ratio via DPO on PKU-SafeRLHF-30K; establishes dataset+method maturity but reports no cross-seed variance
- SafeGRPO: Self-Rewarded Multimodal Safety Alignment via Rule-Governed Policy Optimization (arXiv:2511.12982, Nov 2025) — validates classifier-as-reward paradigm for GRPO safety alignment; motivates our WildGuard-as-reward design
- TRL v1.0: Post-Training Library Built to Move with the Field (Hugging Face, March 2026) — unified training stack for DPO, PPO, GRPO eliminating infrastructure confounds across algorithms
- How Many Random Seeds? Statistical Power Analysis in Deep RL Experiments (arXiv:1806.08295, 2018) — methodology for minimum-seed derivation via power analysis; we extend to safety alignment and apply a priori to justify our 20-seed design
- What Matters For Safety Alignment? (arXiv:2601.03868, Jan 2026) — cross-model safety comparison across 32 models and 13 families
- WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs (arXiv:2406.18495, 2024) — 7B safety classifier achieving 94.7% F1 on response harmfulness; our primary safety judge and GRPO reward signal
- Skywork-Reward: Bag of Tricks for Reward Modeling in LLMs (arXiv:2410.18451, 2024) — Skywork-Reward-Llama-3.1-8B-v0.2, #1 8B model on RewardBench; one of three PPO reward models in our ablation
- Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts (arXiv:2406.12845, 2024) — ArmoRM-Llama3-8B-v0.1, 89.0 RewardBench with explicit safety dimension; default PPO reward model
- Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping (arXiv 2020) — seed variance methodology for NLP
- Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning LLMs (IJCNLP-AACL 2025) — macro/micro consistency metrics for LLM fine-tuning
- RVPO: Risk-Sensitive Alignment via Variance Regularization (arXiv:2605.05750, May 2026) — inter-reward variance penalization in single runs; motivates reward model ablation
- Improving Safety Alignment via Balanced Direct Preference Optimization (arXiv:2603.22829, March 2026) — safety alignment overfitting in DPO
- Safety Training Persists Through Helpfulness Optimization in LLM Agents (arXiv:2603.02229, March 2026) — safety-helpfulness Pareto frontier under DPO
- Reproducibility in Machine-Learning-Based Research: Overview, Barriers, and Drivers (AI Magazine 2025)

## Resource Estimate
- **manual**: {'gpu_hours': '~2,800 H100-hours total: ~1,600 training (260 runs across 3 algorithms × 3 scales × 20+ seeds, all full fine-tuning with DeepSpeed ZeRO-2; PPO runs require 2 H100s for policy+reference+RM) + ~1,200 evaluation (260 checkpoints × 8 benchmarks including WildGuard 7B and HarmBench 7B classifier inference, each checkpoint requiring ~3-4 GPU-hours for generation + classification across all benchmarks)', 'timeline': '17–19 weeks (infrastructure + TRL v1.0 pipeline setup 3w, training runs 6–7w on 8×H100 cluster, evaluation 3–4w, statistical analysis + minimum-seed derivation + paper writing 5–6w)', 'estimated_gpu_cost': '$7,000 at ~$2.50/H100-hr on mid-tier providers'}
- **human_in_loop**: {'gpu_hours': '~2,800 H100-hours (identical core compute; full FT precludes further memory optimization)', 'timeline': '14–16 weeks (Claude accelerates TRL v1.0 pipeline integration, ANOVA analysis scripts, power analysis code, per-category fragility analysis, and paper drafting)', 'claude_api_cost': '$500–700 (Sonnet 4.6 for code generation, statistical analysis automation, and drafting; ~150M tokens)', 'estimated_gpu_cost': '$7,000'}
- **auto_research**: {'gpu_hours': '~2,800 H100-hours', 'timeline': '11–14 weeks (parallelized experiment orchestration with automated sweep management, evaluation pipelines, and ANOVA analysis)', 'claude_api_cost': '$1,500–2,200 (experiment orchestration, automated analysis, full paper draft generation; ~600M tokens)', 'estimated_gpu_cost': '$7,000', 'speed_bottleneck': 'GPU cluster queue time for 260 training jobs (PPO runs ~2× longer than DPO/GRPO due to multi-model training); sequential dependency between training completion and safety evaluation; WildGuard 7B + HarmBench 7B classifier inference throughput across 260 checkpoints × ~6K safety evaluation prompts each'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ade27768-4a40-4ee6-96c8-ace8104cf60a",
  "type": "user",
  "uuid": "5fa1e293-593c-43fa-8845-204413054af8",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T21:02:45.711Z_

```json
{
  "parentUuid": "5fa1e293-593c-43fa-8845-204413054af8",
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
  "uuid": "42210c3f-c107-465c-bb42-87d8204ca5ce",
  "timestamp": "2026-05-19T21:02:45.711Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T21:02:45.711Z_

```json
{
  "parentUuid": "42210c3f-c107-465c-bb42-87d8204ca5ce",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3ab7a4ad-6d61-4dc0-9962-a61cbb874258",
  "timestamp": "2026-05-19T21:02:45.711Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # How Fragile Is Safety Under Retraining? A Large-Scale Reproducibility Audit of Post-Training Alignment  ## Descr…",
  "leafUuid": "3ab7a4ad-6d61-4dc0-9962-a61cbb874258",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate safety alignment reproducibility proposal",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d"
}
```

---

### Assistant

_source line 8 · 2026-05-19T21:02:58.571Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026. Let me first note that CoRL is the Conference on Robot Learning - but this proposal is about LLM safety alignment reproducibility, which doesn't seem like a robotics paper at all. Let me re-read...

Wait, the user said "CoRL 2026 主会" - Conference on Robot Learning. But this proposal is about safety alignment reproducibility for LLMs. This is a significant mismatch. Let me think about this more carefully.

Actually, let me re-read the system prompt. It says "评估其投稿 CoRL 2026 主会的中稿潜力" - evaluating the acceptance potential for CoRL 2026 main conference. 

There's definitely a venue mismatch here - the proposal is clearly about LLM safety and NLP, not robotics. The rubric even mentions "NLP/CL 领域" which suggests the user might be working from a template meant for a different conference, or perhaps they're testing whether I'll notice the inconsistency. I should proceed with the evaluation as requested but flag this discrepancy since it's relevant to assessing the paper's fit.

Now I need to search for the key papers and understand the current state of the field to properly evaluate the proposal's novelty and significance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ab7a4ad-6d61-4dc0-9962-a61cbb874258",
  "isSidechain": false,
  "requestId": "req_011CbCbyY754LBCxc8Y8oRgo",
  "type": "assistant",
  "uuid": "f13494cb-2cef-4eea-b335-4476fd8622ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RvxTKx33a5kSgfmNGFZL8A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8330,
      "cache_read_input_tokens": 13985,
      "output_tokens": 530,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8330,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 530,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 8330,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8330
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

_source line 9 · 2026-05-19T21:02:58.573Z_

我需要先进行领域调研，然后再打分。让我先搜索相关文献和领域现状。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f13494cb-2cef-4eea-b335-4476fd8622ba",
  "isSidechain": false,
  "requestId": "req_011CbCbyY754LBCxc8Y8oRgo",
  "type": "assistant",
  "uuid": "5dbff3c7-9e79-49bf-b78a-2ac60cc6cbd9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RvxTKx33a5kSgfmNGFZL8A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8330,
      "cache_read_input_tokens": 13985,
      "output_tokens": 530,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8330,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 530,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 8330,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8330
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

_source line 10 · 2026-05-19T21:02:58.636Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Apjd5tZMjkjpUHgzn1M4Qn`</summary>

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
  "parentUuid": "5dbff3c7-9e79-49bf-b78a-2ac60cc6cbd9",
  "isSidechain": false,
  "requestId": "req_011CbCbyY754LBCxc8Y8oRgo",
  "type": "assistant",
  "uuid": "d4458032-12af-4c2e-abc6-86fcda250bf5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RvxTKx33a5kSgfmNGFZL8A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8330,
      "cache_read_input_tokens": 13985,
      "output_tokens": 530,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8330,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 530,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 8330,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8330
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

_source line 11 · 2026-05-19T21:02:58.645Z_

<details><summary>↩ Tool result · `toolu_01Apjd5tZMjkjpUHgzn1M4Qn`</summary>

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
  "parentUuid": "d4458032-12af-4c2e-abc6-86fcda250bf5",
  "isSidechain": false,
  "promptId": "ade27768-4a40-4ee6-96c8-ace8104cf60a",
  "type": "user",
  "uuid": "13936a83-8069-4dd7-bcc7-bc4cb642faae",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "d4458032-12af-4c2e-abc6-86fcda250bf5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T21:03:00.574Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do the web searches to understand the field. I'll search for the key papers and related work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13936a83-8069-4dd7-bcc7-bc4cb642faae",
  "isSidechain": false,
  "requestId": "req_011CbCbzVaJ8nuhFMN2FLDHR",
  "type": "assistant",
  "uuid": "c0e0c1d0-7a12-431c-8ed5-7ca0af953473",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvEQPRKyhUMGhk7Cu5LbjN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1057,
      "cache_read_input_tokens": 22315,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1057,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 22315,
          "cache_creation_input_tokens": 1057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1057
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

_source line 13 · 2026-05-19T21:03:01.195Z_

Let me conduct the required field research with multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0e0c1d0-7a12-431c-8ed5-7ca0af953473",
  "isSidechain": false,
  "requestId": "req_011CbCbzVaJ8nuhFMN2FLDHR",
  "type": "assistant",
  "uuid": "21da750c-2df1-48fa-a642-8d128dee53dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvEQPRKyhUMGhk7Cu5LbjN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1057,
      "cache_read_input_tokens": 22315,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1057,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 22315,
          "cache_creation_input_tokens": 1057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1057
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

_source line 14 · 2026-05-19T21:03:01.571Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018NFxTzy67Hr9Qog4tCK2k8`</summary>

```json
{
  "query": "LLM safety alignment reproducibility training seed variance 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21da750c-2df1-48fa-a642-8d128dee53dc",
  "isSidechain": false,
  "requestId": "req_011CbCbzVaJ8nuhFMN2FLDHR",
  "type": "assistant",
  "uuid": "6d672842-d269-4348-958d-747596aa610c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvEQPRKyhUMGhk7Cu5LbjN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1057,
      "cache_read_input_tokens": 22315,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1057,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 22315,
          "cache_creation_input_tokens": 1057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1057
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

_source line 15 · 2026-05-19T21:03:09.446Z_

<details><summary>↩ Tool result · `toolu_018NFxTzy67Hr9Qog4tCK2k8`</summary>

```text
Web search results for query: "LLM safety alignment reproducibility training seed variance 2025 2026"

Links: [{"title":"How to get consistent and reproducible LLM outputs in 2025 (OpenAI, Gemini, Claude, vLLM...)","url":"https://www.keywordsai.co/blog/llm_consistency_2025"},{"title":"Non-Deterministic LLM Prompts in 2026: A Practical Guide","url":"https://futureagi.com/blog/non-deterministic-llm-prompts-2025/"},{"title":"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models","url":"https://arxiv.org/html/2503.07329v2"},{"title":"Towards Reliable, Uncertainty-Aware Alignment","url":"https://arxiv.org/pdf/2507.15906"},{"title":"What Matters For Safety Alignment?","url":"https://arxiv.org/pdf/2601.03868"},{"title":"[2512.12066] The Instability of Safety: How Random Seeds and Temperature Expose Inconsistent LLM Refusal Behavior","url":"https://arxiv.org/abs/2512.12066"},{"title":"Large Empirical Case Study: Go-Explore adapted for AI Red Team Testing","url":"https://arxiv.org/pdf/2601.00042"},{"title":"Generalization Limits of Reinforcement Learning Alignment","url":"https://arxiv.org/pdf/2604.02652"}]

Here are the key findings from the web search on LLM safety alignment reproducibility and training seed variance in 2025-2026:

## Reproducibility and Seed Variance in LLM Alignment

**General Reproducibility Challenges:**
Non-determinism is not a defect; it is the consequence of probabilistic decoding plus hardware-level non-associativity. In 2026 the working answer is to bound variance with temperature, seed, and version pinning, and to design your evaluation to tolerate semantic equivalence rather than byte-exact match.

**Fine-Tuning Stability:**
Extensive experiments reveal significant variability in both standard and consistency metrics, underscoring the need to consider seed-induced variability in fine-tuning and evaluation. 5–10 seeds are sufficient to estimate variance of LLMs in NLP tasks.

**Safety Alignment Instability:**
A critical 2025 finding addresses safety directly: Testing four instruction-tuned models across 876 harmful prompts in different sampling configurations found that 18-28% of prompts exhibit decision flips--the model refuses in some configurations but complies in others.

Independently trained reward models on the same preference dataset can exhibit substantial disagreement, highlighting the instability of current alignment strategies.

**Security Testing Implications:**
Seed variance exceeds algorithmic parameter effects in Go-Explore security testing of safety-trained LLMs, with averaging across multiple seeds materially reducing variance.

These findings suggest that seed variance is a significant factor affecting both reproducibility and safety alignment reliability in modern LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d672842-d269-4348-958d-747596aa610c",
  "isSidechain": false,
  "promptId": "ade27768-4a40-4ee6-96c8-ace8104cf60a",
  "type": "user",
  "uuid": "db19cbfd-8845-4e60-b373-e45fdf80af23",
  "toolUseResult": {
    "query": "LLM safety alignment reproducibility training seed variance 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JnbbMMhd9XtkRGE5uGCDMf",
        "content": [
          {
            "title": "How to get consistent and reproducible LLM outputs in 2025 (OpenAI, Gemini, Claude, vLLM...)",
            "url": "https://www.keywordsai.co/blog/llm_consistency_2025"
          },
          {
            "title": "Non-Deterministic LLM Prompts in 2026: A Practical Guide",
            "url": "https://futureagi.com/blog/non-deterministic-llm-prompts-2025/"
          },
          {
            "title": "Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models",
            "url": "https://arxiv.org/html/2503.07329v2"
          },
          {
            "title": "Towards Reliable, Uncertainty-Aware Alignment",
            "url": "https://arxiv.org/pdf/2507.15906"
          },
          {
            "title": "What Matters For Safety Alignment?",
            "url": "https://arxiv.org/pdf/2601.03868"
          },
          {
            "title": "[2512.12066] The Instability of Safety: How Random Seeds and Temperature Expose Inconsistent LLM Refusal Behavior",
            "url": "https://arxiv.org/abs/2512.12066"
          },
          {
            "title": "Large Empirical Case Study: Go-Explore adapted for AI Red Team Testing",
            "url": "https://arxiv.org/pdf/2601.00042"
          },
          {
            "title": "Generalization Limits of Reinforcement Learning Alignment",
            "url": "https://arxiv.org/pdf/2604.02652"
          }
        ]
      },
      "Here are the key findings from the web search on LLM safety alignment reproducibility and training seed variance in 2025-2026:\n\n## Reproducibility and Seed Variance in LLM Alignment\n\n**General Reproducibility Challenges:**\nNon-determinism is not a defect; it is the consequence of probabilistic decoding plus hardware-level non-associativity. In 2026 the working answer is to bound variance with temperature, seed, and version pinning, and to design your evaluation to tolerate semantic equivalence rather than byte-exact match.\n\n**Fine-Tuning Stability:**\nExtensive experiments reveal significant variability in both standard and consistency metrics, underscoring the need to consider seed-induced variability in fine-tuning and evaluation. 5–10 seeds are sufficient to estimate variance of LLMs in NLP tasks.\n\n**Safety Alignment Instability:**\nA critical 2025 finding addresses safety directly: Testing four instruction-tuned models across 876 harmful prompts in different sampling configurations found that 18-28% of prompts exhibit decision flips--the model refuses in some configurations but complies in others.\n\nIndependently trained reward models on the same preference dataset can exhibit substantial disagreement, highlighting the instability of current alignment strategies.\n\n**Security Testing Implications:**\nSeed variance exceeds algorithmic parameter effects in Go-Explore security testing of safety-trained LLMs, with averaging across multiple seeds materially reducing variance.\n\nThese findings suggest that seed variance is a significant factor affecting both reproducibility and safety alignment reliability in modern LLMs."
    ],
    "durationSeconds": 7.868541024999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6d672842-d269-4348-958d-747596aa610c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T21:03:11.934Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GyqLJT6NEDncwBecBVtfEV`</summary>

```json
{
  "query": "Fraser et al 2025 \"Fine-Tuning Lowers Safety\" arXiv 2506.17209 seed variance SFT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db19cbfd-8845-4e60-b373-e45fdf80af23",
  "isSidechain": false,
  "requestId": "req_011CbCc1HXXerFsBLUy9Q2ua",
  "type": "assistant",
  "uuid": "43f8e45f-6658-46c4-8b82-21b7e53eb9dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpkvL7Uf96FNiYX4y7gcea",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 23372,
      "output_tokens": 84,
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
          "output_tokens": 84,
          "cache_read_input_tokens": 23372,
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

_source line 17 · 2026-05-19T21:03:20.482Z_

<details><summary>↩ Tool result · `toolu_01GyqLJT6NEDncwBecBVtfEV`</summary>

```text
Web search results for query: "Fraser et al 2025 "Fine-Tuning Lowers Safety" arXiv 2506.17209 seed variance SFT"

Links: [{"title":"[2506.17209] Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency","url":"https://arxiv.org/abs/2506.17209"},{"title":"Fine-Tuning Lowers Safety and Disrupts Evaluation ...","url":"https://arxiv.org/pdf/2506.17209"},{"title":"(PDF) Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency","url":"https://www.researchgate.net/publication/392917561_Fine-Tuning_Lowers_Safety_and_Disrupts_Evaluation_Consistency"},{"title":"MedRiskEval: Medical Risk Evaluation Benchmark of ...","url":"https://aclanthology.org/2026.eacl-industry.39.pdf"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=8700&show=2000"},{"title":"Computation and Language Jun 2025","url":"https://www.arxiv.org/list/cs.CL/2025-06?skip=1325&show=50"},{"title":"Rethinking Jailbreak Detection of Large Vision Language Models with Representational Contrastive Scoring","url":"https://arxiv.org/html/2512.12069v3"},{"title":"The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety","url":"https://arxiv.org/pdf/2602.15799"}]

I found the paper! The paper "Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency" was authored by Kathleen C. Fraser, Hillary Dawkins, Isar Nejadgholi, and Svetlana Kiritchenko from the National Research Council Canada, and was submitted on June 20, 2025.

The paper investigates how robust safety benchmarks are to trivial variations in experimental procedure and the stochastic nature of LLMs, while noting that fine-tuning is known to remove the safety alignment features of models, even when the fine-tuning data does not contain any harmful content.

Regarding the specific aspect you asked about regarding seed variance and SFT: The search results show references to variance due to randomness in fine-tuning procedures, with error bands representing the minimum and maximum harmfulness scores across five similarly fine-tuned models. However, the search results don't provide detailed information specifically about seed variance in supervised fine-tuning (SFT). To get more specific details about those particular findings, you would need to access the full paper PDF directly from arXiv at arxiv.org/pdf/2506.17209.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43f8e45f-6658-46c4-8b82-21b7e53eb9dc",
  "isSidechain": false,
  "promptId": "ade27768-4a40-4ee6-96c8-ace8104cf60a",
  "type": "user",
  "uuid": "f69a8286-de6f-450c-bab6-4c70044105f7",
  "toolUseResult": {
    "query": "Fraser et al 2025 \"Fine-Tuning Lowers Safety\" arXiv 2506.17209 seed variance SFT",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NdUHZeeKnDfq6vaz4xqXQj",
        "content": [
          {
            "title": "[2506.17209] Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency",
            "url": "https://arxiv.org/abs/2506.17209"
          },
          {
            "title": "Fine-Tuning Lowers Safety and Disrupts Evaluation ...",
            "url": "https://arxiv.org/pdf/2506.17209"
          },
          {
            "title": "(PDF) Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency",
            "url": "https://www.researchgate.net/publication/392917561_Fine-Tuning_Lowers_Safety_and_Disrupts_Evaluation_Consistency"
          },
          {
            "title": "MedRiskEval: Medical Risk Evaluation Benchmark of ...",
            "url": "https://aclanthology.org/2026.eacl-industry.39.pdf"
          },
          {
            "title": "Computation and Language 2025",
            "url": "https://arxiv.org/list/cs.CL/2025?skip=8700&show=2000"
          },
          {
            "title": "Computation and Language Jun 2025",
            "url": "https://www.arxiv.org/list/cs.CL/2025-06?skip=1325&show=50"
          },
          {
            "title": "Rethinking Jailbreak Detection of Large Vision Language Models with Representational Contrastive Scoring",
            "url": "https://arxiv.org/html/2512.12069v3"
          },
          {
            "title": "The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety",
            "url": "https://arxiv.org/pdf/2602.15799"
          }
        ]
      },
      "I found the paper! The paper \"Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency\" was authored by Kathleen C. Fraser, Hillary Dawkins, Isar Nejadgholi, and Svetlana Kiritchenko from the National Research Council Canada, and was submitted on June 20, 2025.\n\nThe paper investigates how robust safety benchmarks are to trivial variations in experimental procedure and the stochastic nature of LLMs, while noting that fine-tuning is known to remove the safety alignment features of models, even when the fine-tuning data does not contain any harmful content.\n\nRegarding the specific aspect you asked about regarding seed variance and SFT: The search results show references to variance due to randomness in fine-tuning procedures, with error bands representing the minimum and maximum harmfulness scores across five similarly fine-tuned models. However, the search results don't provide detailed information specifically about seed variance in supervised fine-tuning (SFT). To get more specific details about those particular findings, you would need to access the full paper PDF directly from arXiv at arxiv.org/pdf/2506.17209."
    ],
    "durationSeconds": 8.542737946,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "43f8e45f-6658-46c4-8b82-21b7e53eb9dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T21:03:22.990Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GYZcoo7Nh25D2XZnve83aU`</summary>

```json
{
  "query": "OXRL \"Do Post-Training Algorithms Actually Differ\" arXiv 2603.19335 controlled study model scales 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f69a8286-de6f-450c-bab6-4c70044105f7",
  "isSidechain": false,
  "requestId": "req_011CbCc26azZoKieoKskto2f",
  "type": "assistant",
  "uuid": "69f54d06-b46d-46bb-b1ad-2104105de652",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015F4V1nLx1sdhzXYFziwBM4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 24244,
      "output_tokens": 82,
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
          "output_tokens": 82,
          "cache_read_input_tokens": 24244,
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

_source line 19 · 2026-05-19T21:03:30.261Z_

<details><summary>↩ Tool result · `toolu_01GYZcoo7Nh25D2XZnve83aU`</summary>

```text
Web search results for query: "OXRL "Do Post-Training Algorithms Actually Differ" arXiv 2603.19335 controlled study model scales 2026"

Links: [{"title":"[2603.19335] Do Post-Training Algorithms Actually Differ? A Controlled Study Across Model Scales Uncovers Scale-Dependent Ranking Inversions","url":"https://arxiv.org/abs/2603.19335"},{"title":"Do Post-Training Algorithms Actually Differ? A Controlled Study Across Model Scales Uncovers Scale-Dependent Ranking Inversions","url":"https://arxiv.org/html/2603.19335"},{"title":"Do Post-Training Algorithms Actually Differ? A Controlled ...","url":"https://arxiv.org/pdf/2603.19335"},{"title":"Towards a Unified View of Large Language Model Post-Training","url":"https://arxiv.org/pdf/2509.04419"},{"title":"Understanding Post-Training Structural Changes in Large Language Models","url":"https://arxiv.org/pdf/2509.17866"},{"title":"Can Post-Training Transform LLMs into Causal Reasoners?","url":"https://arxiv.org/pdf/2602.06337"},{"title":"Echo Chamber: RL Post-training Amplifies Behaviors Learned in Pretraining","url":"https://arxiv.org/pdf/2504.07912"},{"title":"Learning Dynamics in RL Post-Training for Language Models","url":"https://arxiv.org/pdf/2601.04670"}]

Based on the search results, I found the paper you're looking for. Here's what it contains:

The paper "Do Post-Training Algorithms Actually Differ?" presents OXRL, a unified framework implementing 51 post-training algorithms with identical infrastructure, enabling the first large-scale apples-to-apples evaluation.

**Study Design:**
The study spans 8 algorithms across 4 model scales (0.5B--7B), 3 evaluation domains, and a 20-variant DPO taxonomy (100 runs at 1.5B, 5 seeds each), totaling approximately 240 training runs on H100 GPUs.

**Key Finding on Scale-Dependent Rankings:**
Algorithm rankings are unstable across scale: at 1.5B, online RL (SGRPO) tops all methods at 58.0% ± 0.57 on GSM8K; by 7B, the worst small-scale method (SimPO) becomes the best (85.8%), a complete ranking inversion driven by model scale rather than LoRA regularization.

**Additional Key Finding:**
Zero of 20 DPO variants beat vanilla DPO.

The paper (arXiv:2603.19335) was submitted on March 19, 2026, and provides important insights about how post-training algorithm performance fundamentally changes across different model scales.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69f54d06-b46d-46bb-b1ad-2104105de652",
  "isSidechain": false,
  "promptId": "ade27768-4a40-4ee6-96c8-ace8104cf60a",
  "type": "user",
  "uuid": "f915bc7d-760d-4bfe-811c-7fa28b4bd8ec",
  "toolUseResult": {
    "query": "OXRL \"Do Post-Training Algorithms Actually Differ\" arXiv 2603.19335 controlled study model scales 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V5euvzmPYQAGn8qoUBMNdr",
        "content": [
          {
            "title": "[2603.19335] Do Post-Training Algorithms Actually Differ? A Controlled Study Across Model Scales Uncovers Scale-Dependent Ranking Inversions",
            "url": "https://arxiv.org/abs/2603.19335"
          },
          {
            "title": "Do Post-Training Algorithms Actually Differ? A Controlled Study Across Model Scales Uncovers Scale-Dependent Ranking Inversions",
            "url": "https://arxiv.org/html/2603.19335"
          },
          {
            "title": "Do Post-Training Algorithms Actually Differ? A Controlled ...",
            "url": "https://arxiv.org/pdf/2603.19335"
          },
          {
            "title": "Towards a Unified View of Large Language Model Post-Training",
            "url": "https://arxiv.org/pdf/2509.04419"
          },
          {
            "title": "Understanding Post-Training Structural Changes in Large Language Models",
            "url": "https://arxiv.org/pdf/2509.17866"
          },
          {
            "title": "Can Post-Training Transform LLMs into Causal Reasoners?",
            "url": "https://arxiv.org/pdf/2602.06337"
          },
          {
            "title": "Echo Chamber: RL Post-training Amplifies Behaviors Learned in Pretraining",
            "url": "https://arxiv.org/pdf/2504.07912"
          },
          {
            "title": "Learning Dynamics in RL Post-Training for Language Models",
            "url": "https://arxiv.org/pdf/2601.04670"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what it contains:\n\nThe paper \"Do Post-Training Algorithms Actually Differ?\" presents OXRL, a unified framework implementing 51 post-training algorithms with identical infrastructure, enabling the first large-scale apples-to-apples evaluation.\n\n**Study Design:**\nThe study spans 8 algorithms across 4 model scales (0.5B--7B), 3 evaluation domains, and a 20-variant DPO taxonomy (100 runs at 1.5B, 5 seeds each), totaling approximately 240 training runs on H100 GPUs.\n\n**Key Finding on Scale-Dependent Rankings:**\nAlgorithm rankings are unstable across scale: at 1.5B, online RL (SGRPO) tops all methods at 58.0% ± 0.57 on GSM8K; by 7B, the worst small-scale method (SimPO) becomes the best (85.8%), a complete ranking inversion driven by model scale rather than LoRA regularization.\n\n**Additional Key Finding:**\nZero of 20 DPO variants beat vanilla DPO.\n\nThe paper (arXiv:2603.19335) was submitted on March 19, 2026, and provides important insights about how post-training algorithm performance fundamentally changes across different model scales."
    ],
    "durationSeconds": 7.266437148999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "69f54d06-b46d-46bb-b1ad-2104105de652",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T21:03:32.752Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D5tG28NRWTBtWKRNb8uaCH`</summary>

```json
{
  "query": "safety alignment reproducibility audit DPO PPO GRPO cross-seed variance benchmark 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f915bc7d-760d-4bfe-811c-7fa28b4bd8ec",
  "isSidechain": false,
  "requestId": "req_011CbCc2pMi3J8npNbqpnXRL",
  "type": "assistant",
  "uuid": "a1c3cbd2-6c02-4653-a777-809ad9b09fea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G62FsAQHzdTV4Nx2zPGWrK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 25028,
      "output_tokens": 75,
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
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 25028,
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

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # How Fragile Is Safety Under Retraining? A Large-Scale Reproducibility Audit of Post-Training Alignment  ## Descr…",
  "leafUuid": "a1c3cbd2-6c02-4653-a777-809ad9b09fea",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate safety alignment reproducibility proposal",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d"
}
```

---

### Tool result

_source line 23 · 2026-05-19T21:03:42.949Z_

<details><summary>↩ Tool result · `toolu_01D5tG28NRWTBtWKRNb8uaCH`</summary>

```text
Web search results for query: "safety alignment reproducibility audit DPO PPO GRPO cross-seed variance benchmark 2025 2026"

Links: [{"title":"It Takes Two: Your GRPO Is Secretly DPO","url":"https://arxiv.org/pdf/2510.00977"},{"title":"Optimizing Safe and Aligned Language Generation: A Multi-Objective GRPO   Approach","url":"https://arxiv.org/pdf/2503.21819"},{"title":"Why Alignment Must Precede Distillation: A Minimal Working Explanation","url":"https://arxiv.org/html/2509.23667"},{"title":"How to align open LLMs in 2025 with DPO & and synthetic data","url":"https://www.philschmid.de/rl-with-llms-in-2025-dpo"},{"title":"Evaluating GRPO and DPO for Faithful Chain-of-Thought Reasoning in LLMs","url":"https://arxiv.org/html/2512.22631v1"},{"title":"Rethinking the Evaluation of Alignment Methods: Insights into Diversity, Generalisation, and Safety","url":"https://arxiv.org/pdf/2509.12936"},{"title":"Balancing Safety and Helpfulness in Healthcare AI Assistants through Iterative Preference Alignment","url":"https://arxiv.org/pdf/2512.04210"},{"title":"Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study","url":"https://arxiv.org/pdf/2404.10719"}]

Based on my search results, here's what I found regarding safety alignment, reproducibility, and benchmarking of DPO, PPO, and GRPO methods:

## Recent Research on Alignment Methods (2025-2026)

Post-training methods like Direct Preference Optimization (DPO), Proximal Policy Optimization (PPO), and Group Preference Optimization (GRPO) have been used to align models with human preferences and improve performance.

## Safety and Multi-Objective Alignment

Aligning large language models (LLMs) with human values and safety constraints is challenging, especially when objectives like helpfulness, truthfulness, and avoidance of harm conflict. Recent work has addressed this through multi-objective approaches: A Group Relative Policy Optimization (GRPO) framework with a multi-label reward regression model can achieve safe and aligned language generation, where the GRPO algorithm optimizes a policy by comparing groups of sampled responses, eliminating the need for a separate value critic and improving training efficiency.

## Comparative Evaluation and Trade-offs

Recent studies evaluate multiple alignment techniques in parallel—PPO, DPO, ORPO, and KTO—using both in-distribution and out-of-distribution test sets, including dedicated safety datasets. Additionally, GRPO achieves higher faithfulness but requires careful tuning and greater computational resources, whereas DPO provides steadier improvements that remain accessible on smaller models.

## Theoretical Connections

Recent work establishes a formal link between GRPO and DPO through a contrastive lens, providing a unified analytical framework for understanding alignment, and attributes the efficacy of GRPO to the construction of contrastive pairs, which serves as a control variate to reduce the variance of the gradient estimator.

The search results indicate active research in this area in 2025-2026, though specific information about cross-seed variance benchmarking or comprehensive reproducibility audits wasn't prominently featured in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1c3cbd2-6c02-4653-a777-809ad9b09fea",
  "isSidechain": false,
  "promptId": "ade27768-4a40-4ee6-96c8-ace8104cf60a",
  "type": "user",
  "uuid": "8fdbda4b-15bc-4130-b972-22ae491541a3",
  "toolUseResult": {
    "query": "safety alignment reproducibility audit DPO PPO GRPO cross-seed variance benchmark 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LwuRSpG3KEZzPcfxfFrUro",
        "content": [
          {
            "title": "It Takes Two: Your GRPO Is Secretly DPO",
            "url": "https://arxiv.org/pdf/2510.00977"
          },
          {
            "title": "Optimizing Safe and Aligned Language Generation: A Multi-Objective GRPO   Approach",
            "url": "https://arxiv.org/pdf/2503.21819"
          },
          {
            "title": "Why Alignment Must Precede Distillation: A Minimal Working Explanation",
            "url": "https://arxiv.org/html/2509.23667"
          },
          {
            "title": "How to align open LLMs in 2025 with DPO & and synthetic data",
            "url": "https://www.philschmid.de/rl-with-llms-in-2025-dpo"
          },
          {
            "title": "Evaluating GRPO and DPO for Faithful Chain-of-Thought Reasoning in LLMs",
            "url": "https://arxiv.org/html/2512.22631v1"
          },
          {
            "title": "Rethinking the Evaluation of Alignment Methods: Insights into Diversity, Generalisation, and Safety",
            "url": "https://arxiv.org/pdf/2509.12936"
          },
          {
            "title": "Balancing Safety and Helpfulness in Healthcare AI Assistants through Iterative Preference Alignment",
            "url": "https://arxiv.org/pdf/2512.04210"
          },
          {
            "title": "Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study",
            "url": "https://arxiv.org/pdf/2404.10719"
          }
        ]
      },
      "Based on my search results, here's what I found regarding safety alignment, reproducibility, and benchmarking of DPO, PPO, and GRPO methods:\n\n## Recent Research on Alignment Methods (2025-2026)\n\nPost-training methods like Direct Preference Optimization (DPO), Proximal Policy Optimization (PPO), and Group Preference Optimization (GRPO) have been used to align models with human preferences and improve performance.\n\n## Safety and Multi-Objective Alignment\n\nAligning large language models (LLMs) with human values and safety constraints is challenging, especially when objectives like helpfulness, truthfulness, and avoidance of harm conflict. Recent work has addressed this through multi-objective approaches: A Group Relative Policy Optimization (GRPO) framework with a multi-label reward regression model can achieve safe and aligned language generation, where the GRPO algorithm optimizes a policy by comparing groups of sampled responses, eliminating the need for a separate value critic and improving training efficiency.\n\n## Comparative Evaluation and Trade-offs\n\nRecent studies evaluate multiple alignment techniques in parallel—PPO, DPO, ORPO, and KTO—using both in-distribution and out-of-distribution test sets, including dedicated safety datasets. Additionally, GRPO achieves higher faithfulness but requires careful tuning and greater computational resources, whereas DPO provides steadier improvements that remain accessible on smaller models.\n\n## Theoretical Connections\n\nRecent work establishes a formal link between GRPO and DPO through a contrastive lens, providing a unified analytical framework for understanding alignment, and attributes the efficacy of GRPO to the construction of contrastive pairs, which serves as a control variate to reduce the variance of the gradient estimator.\n\nThe search results indicate active research in this area in 2025-2026, though specific information about cross-seed variance benchmarking or comprehensive reproducibility audits wasn't prominently featured in these results."
    ],
    "durationSeconds": 10.188626510000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a1c3cbd2-6c02-4653-a777-809ad9b09fea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T21:03:45.034Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CgBj1PrLJ3PWuvDfqrrbDM`</summary>

```json
{
  "query": "CoRL 2026 conference topics scope submission \"robot learning\" accepted papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fdbda4b-15bc-4130-b972-22ae491541a3",
  "isSidechain": false,
  "requestId": "req_011CbCc3kkwJfLjCwU2UcXTK",
  "type": "assistant",
  "uuid": "d7b68f6e-feac-4a4e-8a56-0092826b7d30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uyagJMUm2och42rnMBjHa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 919,
      "cache_read_input_tokens": 25824,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 919,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 25824,
          "cache_creation_input_tokens": 919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 919
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

_source line 25 · 2026-05-19T21:03:50.999Z_

<details><summary>↩ Tool result · `toolu_01CgBj1PrLJ3PWuvDfqrrbDM`</summary>

```text
Web search results for query: "CoRL 2026 conference topics scope submission "robot learning" accepted papers"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - About CoRL","url":"https://www.corl.org/about-corl"},{"title":"Iterative transfer learning for automatic collective motion tuning on multiple robot platforms","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10060795/"},{"title":"Editorial: Advancements in neural learning control for enhanced multi-robot coordination","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12678322/"}]

Based on the search results, I found information about CoRL 2026 conference scope and submission guidelines:

## Conference Scope and Topics

The Conference on Robot Learning (CoRL) is an annual international conference focusing on the intersection of robotics and machine learning. CoRL 2026 will be held in Austin, Texas, US.

## Submission Requirements

The conference covers topics including video models and latent world models for robot learning, with submissions required to focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots, and submissions without a robotics focus will be returned without review.

## Accepted Papers

The accepted papers and reviews will be publicly accessible and de-anonymized after decisions are announced. Accepted papers will appear in the Proceedings of Machine Learning Research. However, the search results did not provide a specific list of already-accepted papers for CoRL 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7b68f6e-feac-4a4e-8a56-0092826b7d30",
  "isSidechain": false,
  "promptId": "ade27768-4a40-4ee6-96c8-ace8104cf60a",
  "type": "user",
  "uuid": "7e78cafa-b762-4bd4-8347-b0a88d811f61",
  "toolUseResult": {
    "query": "CoRL 2026 conference topics scope submission \"robot learning\" accepted papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Nix5RXZzc3k8S8uohSTmSH",
        "content": [
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "CoRL 2026 - Call for Workshops",
            "url": "https://www.corl.org/contributions/call-for-workshops"
          },
          {
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
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
            "title": "CoRL 2026 - About CoRL",
            "url": "https://www.corl.org/about-corl"
          },
          {
            "title": "Iterative transfer learning for automatic collective motion tuning on multiple robot platforms",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10060795/"
          },
          {
            "title": "Editorial: Advancements in neural learning control for enhanced multi-robot coordination",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12678322/"
          }
        ]
      },
      "Based on the search results, I found information about CoRL 2026 conference scope and submission guidelines:\n\n## Conference Scope and Topics\n\nThe Conference on Robot Learning (CoRL) is an annual international conference focusing on the intersection of robotics and machine learning. CoRL 2026 will be held in Austin, Texas, US.\n\n## Submission Requirements\n\nThe conference covers topics including video models and latent world models for robot learning, with submissions required to focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots, and submissions without a robotics focus will be returned without review.\n\n## Accepted Papers\n\nThe accepted papers and reviews will be publicly accessible and de-anonymized after decisions are announced. Accepted papers will appear in the Proceedings of Machine Learning Research. However, the search results did not provide a specific list of already-accepted papers for CoRL 2026."
    ],
    "durationSeconds": 5.9598270060000065,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d7b68f6e-feac-4a4e-8a56-0092826b7d30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T21:04:04.199Z_

<details><summary>Logged reasoning block</summary>

```text
This is extremely important! CoRL 2026 explicitly states that "submissions without a robotics focus will be returned without review." This proposal is about LLM safety alignment reproducibility - it has absolutely nothing to do with robotics. This is a fundamental venue mismatch.

Let me also search for whether this topic would fit NeurIPS, ICML, or other ML venues better.

Actually wait - let me re-read the user's request. They said "CoRL 2026 主会". This is clearly a venue mismatch issue. The proposal is about LLM safety alignment, which would be appropriate for NeurIPS, ICML, ICLR, ACL, EMNLP, AAAI, etc. 

But CoRL explicitly requires a robotics focus, so the acceptance probability there is essentially zero. This venue mismatch is the primary concern I need to flag prominently, though I should still evaluate the idea quality independently and note whether the user may have intended a different venue given the NLP/CL evaluation criteria in their rubric.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e78cafa-b762-4bd4-8347-b0a88d811f61",
  "isSidechain": false,
  "requestId": "req_011CbCc4M8uLgrvoAM3WHRmX",
  "type": "assistant",
  "uuid": "d4346f76-4c8b-4710-85b9-f529b76cc4c5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fzofj1y286fHpchvKvtR1W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 26743,
      "output_tokens": 444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 444,
          "cache_read_input_tokens": 26743,
          "cache_creation_input_tokens": 628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 628
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

_source line 27 · 2026-05-19T21:04:04.212Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RUKHFDqSfjVrUhrAXi3Nx7`</summary>

```json
{
  "query": "SafeDPO arXiv 2505.20065 ICLR 2026 PKU-SafeRLHF safety alignment DPO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4346f76-4c8b-4710-85b9-f529b76cc4c5",
  "isSidechain": false,
  "requestId": "req_011CbCc4M8uLgrvoAM3WHRmX",
  "type": "assistant",
  "uuid": "fa816d84-7d0d-49c6-bd13-b2926dc49c75",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fzofj1y286fHpchvKvtR1W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 26743,
      "output_tokens": 444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 444,
          "cache_read_input_tokens": 26743,
          "cache_creation_input_tokens": 628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 628
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

_source line 28 · 2026-05-19T21:04:13.230Z_

<details><summary>↩ Tool result · `toolu_01RUKHFDqSfjVrUhrAXi3Nx7`</summary>

```text
Web search results for query: "SafeDPO arXiv 2505.20065 ICLR 2026 PKU-SafeRLHF safety alignment DPO"

Links: [{"title":"[2505.20065] SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety","url":"https://arxiv.org/abs/2505.20065"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2505.20065"},{"title":"SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety","url":"https://arxiv.org/html/2505.20065"},{"title":"[2505.20065v1] SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety","url":"https://arxiv.org/abs/2505.20065v1"},{"title":"ICLR 2026 Accepted Papers: Oral Papers, Research Trends & Top Highlights","url":"https://www.bohrium.com/en/blog/research-notes/iclr-2026-accepted-papers-highlights/"},{"title":"Artificial Intelligence May 2025","url":"https://www.arxiv.org/list/cs.AI/2025-05?skip=3675&show=50"}]

Based on the search results, here's what I found about SafeDPO:

SafeDPO is titled "A Simple Approach to Direct Preference Optimization with Enhanced Safety" and was authored by Geon-Hyeong Kim and 6 other authors. It was published as a conference paper at ICLR 2026.

**Key Features:**

SafeDPO eliminates the need for reward models, cost models, and online sampling, relying only on preference data and safety indicators. The algorithm is designed to directly optimize the safety alignment objective in a single stage of policy learning, without requiring relaxation.

**Motivation:**

The work incorporates safety constraints into Reinforcement Learning from Human Feedback (RLHF), addressing how existing methods often rely on auxiliary networks or multi-stage pipelines, thereby increasing complexity.

**Technical Approach:**

The authors revisit the original safety alignment objective and show that, under mild assumptions, it admits a closed-form optimal policy, and further derive a provably equivalent and tractable objective, enabling direct optimization.

**Recognition:**

SafeDPO offers a constrained alternative that balances helpfulness and safety without auxiliary networks, and was accepted as one of the Oral presentations at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa816d84-7d0d-49c6-bd13-b2926dc49c75",
  "isSidechain": false,
  "promptId": "ade27768-4a40-4ee6-96c8-ace8104cf60a",
  "type": "user",
  "uuid": "6a3d0c20-0efc-459e-bf7a-a892652ef3b6",
  "toolUseResult": {
    "query": "SafeDPO arXiv 2505.20065 ICLR 2026 PKU-SafeRLHF safety alignment DPO",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TZhvFnR1erKiCjRURPhDw4",
        "content": [
          {
            "title": "[2505.20065] SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety",
            "url": "https://arxiv.org/abs/2505.20065"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2505.20065"
          },
          {
            "title": "SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety",
            "url": "https://arxiv.org/html/2505.20065"
          },
          {
            "title": "[2505.20065v1] SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety",
            "url": "https://arxiv.org/abs/2505.20065v1"
          },
          {
            "title": "ICLR 2026 Accepted Papers: Oral Papers, Research Trends & Top Highlights",
            "url": "https://www.bohrium.com/en/blog/research-notes/iclr-2026-accepted-papers-highlights/"
          },
          {
            "title": "Artificial Intelligence May 2025",
            "url": "https://www.arxiv.org/list/cs.AI/2025-05?skip=3675&show=50"
          }
        ]
      },
      "Based on the search results, here's what I found about SafeDPO:\n\nSafeDPO is titled \"A Simple Approach to Direct Preference Optimization with Enhanced Safety\" and was authored by Geon-Hyeong Kim and 6 other authors. It was published as a conference paper at ICLR 2026.\n\n**Key Features:**\n\nSafeDPO eliminates the need for reward models, cost models, and online sampling, relying only on preference data and safety indicators. The algorithm is designed to directly optimize the safety alignment objective in a single stage of policy learning, without requiring relaxation.\n\n**Motivation:**\n\nThe work incorporates safety constraints into Reinforcement Learning from Human Feedback (RLHF), addressing how existing methods often rely on auxiliary networks or multi-stage pipelines, thereby increasing complexity.\n\n**Technical Approach:**\n\nThe authors revisit the original safety alignment objective and show that, under mild assumptions, it admits a closed-form optimal policy, and further derive a provably equivalent and tractable objective, enabling direct optimization.\n\n**Recognition:**\n\nSafeDPO offers a constrained alternative that balances helpfulness and safety without auxiliary networks, and was accepted as one of the Oral presentations at ICLR 2026."
    ],
    "durationSeconds": 9.010048243000012,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fa816d84-7d0d-49c6-bd13-b2926dc49c75",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T21:04:16.107Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012VWvGtXbVbWgygaGyhW1Kt`</summary>

```json
{
  "query": "\"training time\" \"safety variance\" OR \"safety fragility\" LLM alignment reproducibility multi-seed 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a3d0c20-0efc-459e-bf7a-a892652ef3b6",
  "isSidechain": false,
  "requestId": "req_011CbCc5zBtBGBKNTcjpxQ7v",
  "type": "assistant",
  "uuid": "0d9fa853-44b2-4f40-a587-9ecf712dd3b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdxqHDArniZsYxRWbeaWKU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1073,
      "cache_read_input_tokens": 27371,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1073,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 27371,
          "cache_creation_input_tokens": 1073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1073
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

_source line 30 · 2026-05-19T21:04:24.977Z_

<details><summary>↩ Tool result · `toolu_012VWvGtXbVbWgygaGyhW1Kt`</summary>

```text
Web search results for query: ""training time" "safety variance" OR "safety fragility" LLM alignment reproducibility multi-seed 2026"

Links: [{"title":"Aligning large language models across the lifecycle: A survey on safety-usability trade-offs from pre-training to post-training - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608026004570"},{"title":"LoX: Low-Rank Extrapolation Robustifies LLM Safety Against Fine-tuning","url":"https://arxiv.org/pdf/2506.15606"},{"title":"TRACEALIGN -- Tracing the Drift: Attributing Alignment Failures to Training-Time Belief Sources in LLMs","url":"https://arxiv.org/pdf/2508.02063"},{"title":"Efficient Switchable Safety Control in LLMs via Magic-Token-Guided Co-Training","url":"https://arxiv.org/pdf/2508.14904"},{"title":"Re-Emergent Misalignment: How Narrow Fine-Tuning Erodes Safety Alignment in LLMs","url":"https://arxiv.org/pdf/2507.03662"},{"title":"Alignment and Safety in Large Language Models: Safety Mechanisms, Training Paradigms, and Emerging Challenges","url":"https://arxiv.org/html/2507.19672v1"}]

I've completed the web search for your query. Here are the results:

The search returned several recent papers (2025-2026) on LLM safety and alignment:

1. **Survey on Safety-Usability Trade-offs** - A comprehensive survey searched literature from January 2019 to December 2025 across major academic databases and repositories, examining how safety and usability trade-offs occur across the LLM lifecycle.

2. **Low-Rank Extrapolation for Safety Robustness** (LoX) - Addresses how safety alignment can be easily broken by simple and inexpensive attacks through fine-tuning or in-context learning.

3. **TRACEALIGN** - Focuses on tracing alignment failures to training-time sources, proposing mechanisms that reduce alignment drift by up to 85% while preserving utility on standard tasks.

4. **Efficient Safety Control via Co-Training** - Introduces a method where co-training induces a distinct Safety Alignment Margin in the output space, with well-separated response distributions that provide empirical evidence for the model's safety robustness.

5. **Re-Emergent Misalignment** - Examines how alignment can degrade when a model is fine-tuned on data that conflicts with prior fine-tuning alignment.

6. **Safety Mechanisms and Training Paradigms** - A comprehensive review of alignment and safety in LLMs, including the CyberSecEval benchmark suite for reproducible safety testing.

These papers all address reproducibility and robustness concerns in LLM safety alignment, though the specific metrics and methodologies vary across studies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d9fa853-44b2-4f40-a587-9ecf712dd3b3",
  "isSidechain": false,
  "promptId": "ade27768-4a40-4ee6-96c8-ace8104cf60a",
  "type": "user",
  "uuid": "276d3744-1fe3-4c07-920e-ffa9f1c5379a",
  "toolUseResult": {
    "query": "\"training time\" \"safety variance\" OR \"safety fragility\" LLM alignment reproducibility multi-seed 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T9gRdzVxCUPvJKR1JFJc46",
        "content": [
          {
            "title": "Aligning large language models across the lifecycle: A survey on safety-usability trade-offs from pre-training to post-training - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0893608026004570"
          },
          {
            "title": "LoX: Low-Rank Extrapolation Robustifies LLM Safety Against Fine-tuning",
            "url": "https://arxiv.org/pdf/2506.15606"
          },
          {
            "title": "TRACEALIGN -- Tracing the Drift: Attributing Alignment Failures to Training-Time Belief Sources in LLMs",
            "url": "https://arxiv.org/pdf/2508.02063"
          },
          {
            "title": "Efficient Switchable Safety Control in LLMs via Magic-Token-Guided Co-Training",
            "url": "https://arxiv.org/pdf/2508.14904"
          },
          {
            "title": "Re-Emergent Misalignment: How Narrow Fine-Tuning Erodes Safety Alignment in LLMs",
            "url": "https://arxiv.org/pdf/2507.03662"
          },
          {
            "title": "Alignment and Safety in Large Language Models: Safety Mechanisms, Training Paradigms, and Emerging Challenges",
            "url": "https://arxiv.org/html/2507.19672v1"
          }
        ]
      },
      "I've completed the web search for your query. Here are the results:\n\nThe search returned several recent papers (2025-2026) on LLM safety and alignment:\n\n1. **Survey on Safety-Usability Trade-offs** - A comprehensive survey searched literature from January 2019 to December 2025 across major academic databases and repositories, examining how safety and usability trade-offs occur across the LLM lifecycle.\n\n2. **Low-Rank Extrapolation for Safety Robustness** (LoX) - Addresses how safety alignment can be easily broken by simple and inexpensive attacks through fine-tuning or in-context learning.\n\n3. **TRACEALIGN** - Focuses on tracing alignment failures to training-time sources, proposing mechanisms that reduce alignment drift by up to 85% while preserving utility on standard tasks.\n\n4. **Efficient Safety Control via Co-Training** - Introduces a method where co-training induces a distinct Safety Alignment Margin in the output space, with well-separated response distributions that provide empirical evidence for the model's safety robustness.\n\n5. **Re-Emergent Misalignment** - Examines how alignment can degrade when a model is fine-tuned on data that conflicts with prior fine-tuning alignment.\n\n6. **Safety Mechanisms and Training Paradigms** - A comprehensive review of alignment and safety in LLMs, including the CyberSecEval benchmark suite for reproducible safety testing.\n\nThese papers all address reproducibility and robustness concerns in LLM safety alignment, though the specific metrics and methodologies vary across studies."
    ],
    "durationSeconds": 8.864529385,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0d9fa853-44b2-4f40-a587-9ecf712dd3b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-19T21:04:24.980Z_

```json
{
  "parentUuid": "276d3744-1fe3-4c07-920e-ffa9f1c5379a",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3d168641-d27d-43b5-a8d4-69a24aabce9a",
  "timestamp": "2026-05-19T21:04:24.980Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-19T21:05:01.288Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to evaluate this proposal. Let me synthesize my findings.

**Critical Issue: Venue Mismatch**
CoRL 2026 explicitly requires a robotics focus. The call for papers says "submissions without a robotics focus will be returned without review." This proposal is about LLM safety alignment reproducibility - it has zero robotics content. This means the acceptance probability at CoRL is essentially 0%, desk-rejected.

But wait - maybe the user made an error about the venue and actually intends NeurIPS, ICML, or another ML venue. I should evaluate the idea quality objectively and note the venue mismatch.
 
Looking at the core contribution: this is essentially a large-scale reproducibility study that trains three alignment methods (DPO, PPO-RLHF, GRPO) across multiple model sizes with 20 seeds each, measures safety variance against capability variance, introduces a new SCI-T metric, and provides lookup tables for minimum seed requirements. The fundamental issue is that this is a straightforward extension of Fraser et al.'s existing work - just applying their methodology to preference optimization methods with more seeds.

The methodology itself is quite simple: run many seeds, measure variance, decompose with ANOVA, and the SCI-T metric is just a ratio of refusal counts. A much leaner version could demonstrate the core finding with just 10 seeds of DPO on a single model size to establish whether safety variance is actually higher than capability variance. The 260-run design adds rigor but the key insight doesn't require that scale.

There's a significant risk here: the entire paper hinges on the assumption that training-seed variance in safety is meaningfully larger than in capabilities. If the data shows they're similar, the central narrative collapses. The dual-outcome design provides some protection against this, but it's still fundamentally a bet on what the empirical results will show.

On novelty, the core contribution is measuring reproducibility of safety alignment across seeds at scale—a well-motivated question, but prior work has already established that seed variance exists in safety SFT, inference-time safety shows instability, and post-training algorithms exhibit seed variance. This proposal scales up and combines those findings rather than introducing something fundamentally new. The SCI-T metric is trivially simple—just the fraction of seeds agreeing on refuse versus comply—so calling it a novel metric feels like a stretch. The minimum-seed lookup tables are genuinely useful, but the underlying methodology relies on standard power analysis.

The significance is real though: the question matters for AI governance and safety evaluation. If safety truly is more fragile than capabilities under retraining, that's a meaningful empirical finding for the field. But it's an empirical result, not a conceptual breakthrough, and the practical value comes mainly from those lookup tables.

The related work is thorough, which ironically highlights how close prior work already is to what's being proposed here. Stepping back, this is a well-executed empirical study addressing a genuine gap, but the core contribution boils down to running more experiments with more seeds across more algorithms—a quantitative scaling rather than a qualitative advance. If safety variance turns out to match capability variance, the paper loses much of its impact. And the finding that safety is fragile under retraining isn't particularly surprising given what we already know. This reads as a solid empirical audit—valuable for the field, but not high-novelty work. For a top venue like NeurIPS or ICML, it'd be borderline. For CoRL specifically, it's a venue mismatch.

I need to flag something important though: there's a contradiction between the system prompt asking me to evaluate for NLP/CL and the user specifying CoRL 2026. CoRL explicitly rejects papers without robotics focus, which means this paper would face a desk reject there regardless of quality. If we're evaluating for an appropriate venue instead, the probability shifts significantly, but at CoRL it's essentially zero.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d168641-d27d-43b5-a8d4-69a24aabce9a",
  "isSidechain": false,
  "requestId": "req_011CbCc6rJPtSi5RWU281C7J",
  "type": "assistant",
  "uuid": "7d7374d6-52ff-458a-8c52-d49006548b3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WiWjkY7MtX3FwdJHPnm1ex",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 911,
      "cache_read_input_tokens": 28444,
      "output_tokens": 5905,
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
          "output_tokens": 5905,
          "cache_read_input_tokens": 28444,
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

### Assistant

_source line 33 · 2026-05-19T21:06:37.338Z_

Now I have sufficient information to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ 致命性前置问题：venue mismatch（投稿目标错误）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

在进入 idea 质量评估之前，必须首先指出：

**本 proposal 与 CoRL 2026 存在根本性的 venue mismatch。** 

CoRL (Conference on Robot Learning) 2026 的 Call for Papers 明确要求：
- 投稿必须聚焦于核心的 robotics problem
- 必须展示所提出的 models/algorithms/datasets/benchmarks 对 robotics 的 relevance
- "Submissions without a robotics focus will be returned without review"（无机器人焦点的投稿将不经审稿直接退回）

本 proposal 的内容是 **LLM 安全对齐的训练时可复现性审计**——完全属于 NLP/AI Safety 领域，与 robot learning 无任何交集。投稿 CoRL 将 100% 被 desk reject。

**如果用户实际目标是 NeurIPS 2026、ICML 2026、ICLR 2027 或 EMNLP 2026 等 NLP/ML 主会，以下 idea 质量评估仍然适用。** 以下评估假设投稿目标是一个接受 LLM safety 话题的 top venue（如 NeurIPS/ICML/ICLR）。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

【领域调研】:

- [Larsen 2025, arXiv:2512.12066] (Dec 2025): 提出 SSI 指标，发现 18–28% 的 prompt 在不同 inference seed/temperature 下在 refusal 和 compliance 之间翻转。本 proposal 的直接前驱，但仅关注 inference-time variance（固定权重），未触及 training-time variance。论文存在且描述准确。

- [Fraser et al. 2025, arXiv:2506.17209] (June 2025, LLMSEC): 首次证明 training-seed variance 影响安全性——5 个 SFT seed 在 Llama-3.2-1B 上产生最高 9pp 的 harmfulness score 变化。使用 LoRA + 4-bit quantization + SORRY-Bench。论文存在且描述准确。**但注意：这是 SFT 而非 preference optimization，且仅 5 seeds、2 models、1 benchmark——proposal 将其作为核心 gap 依据是合理的。**

- [OXRL, arXiv:2603.19335] (March 2026): 51 种 post-training 算法在 Qwen 2.5 (0.5B–7B) 上的 controlled comparison。发现 scale-dependent ranking inversions（SimPO 在 1.5B 最差、7B 最好）。提供了 GSM8K 上 SGRPO 的 cross-seed std ±0.57pp 作为 capability variance baseline。**但 OXRL 未做任何 safety evaluation**——proposal 准确地将此定位为 gap。

- [SafeDPO, arXiv:2505.20065] (ICLR 2026 Oral): DPO + PKU-SafeRLHF-30K 达到 ~97% harmless ratio。确认了数据集和方法的成熟度，但未报告 cross-seed variance。论文存在且描述准确。

- [SafeGRPO, arXiv:2511.12982] (Nov 2025): 验证了 classifier-as-reward 的 GRPO 安全对齐范式。论文存在。

- [SafeTuneBed, arXiv:2506.00676] (May 2025): 安全微调 toolkit，3-seed averaging，提到 refusal consistency 但未正式定义。

- [LLM-Safety Evaluations Lack Robustness, arXiv:2503.02574] (March 2025): evaluation pipeline 选择导致最高 28% ASR variance，动机化了 fixed-pipeline 设计。

- [TRACEALIGN, arXiv:2508.02063] (2025): 追踪对齐失败到训练时信念来源，减少 alignment drift 达 85%，但方法论完全不同（mechanistic interpretation vs empirical audit）。

- 调研总结：**safety alignment 的 fragility 是一个已被多个角度初步验证的现象（inference-time: Larsen; SFT training-time: Fraser; evaluation pipeline: arXiv:2503.02574），但 preference-based alignment (DPO/PPO/GRPO) 的 training-time safety reproducibility 确实没有被系统研究过。** 该 gap 真实存在，但 gap 的 "width" 有限——核心问题方向已被邻近工作大致框定，本 proposal 的贡献本质是 scale-up + 组合 + 方法扩展。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

【Trivial Alternative 检验】:

**存在明显的 trivial alternative 威胁。**

核心问题是"safety 在 retraining 中是否比 capability 更 fragile"。一个成本远低的替代方案是：
1. 仅跑 DPO 一种算法（最成熟的 open-source 方法），在 1-2 个 scale 上，用 10 seeds，对比 safety vs capability variance。这已经足以回答核心问题，compute 成本不到 proposal 的 1/5。
2. 如果发现 safety 确实更 fragile（高概率，因为 Fraser et al. 已在 SFT 上证明了），增量发现不令人惊讶。
3. 260 runs 的大规模设计增加了 **thoroughness**（hardware ablation, reward model ablation, 3 algorithms × 3 scales），但这些都是实验设计层面的完善，不改变核心发现的 novelty。

增量价值在于：(a) 覆盖三种不同范式的 preference optimization 而非仅 SFT；(b) ANOVA 方差分解跨多因素；(c) minimum-seed lookup tables 的实用工具。但这些增量价值更接近 "engineering thoroughness" 而非 "conceptual breakthrough"。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

【前提假设检验】:

核心 claim 逻辑链中有以下未经验证的假设：

1. **"Safety 比 capability 在 training-time 上更 fragile" 几乎是预期结论。** Fraser et al. 在 SFT 上已经显示 9pp safety variance vs 一般认为的 <1pp capability variance。如果 preference optimization 也呈现相同模式，审稿人会说 "I would have guessed this"——safety decisions 本质上是在 decision boundary 附近的二元分类，而 capability（如 GSM8K 准确率）是在整个分布上的聚合指标，前者天然更 noisy。这不需要大规模实验来"发现"，更像是在验证一个已有的 prior。

2. **SCI-T 的学术贡献被高估。** SCI-T(p) = max_c(n_c)/K 本质上就是"K 个 seed 中多数决策的比例"——这是一个 trivially simple metric。Proposal 将其包装为"extending Larsen's SSI to training-time"，但实际上 SSI 也是一个简单的 agreement metric，从 inference-time 到 training-time 的"扩展"不涉及任何方法论创新，仅仅是改变了 variance source（sampling noise → training noise）。

3. **Minimum-seed lookup tables 的假设前提。** 这些 tables 假设 variance 在不同 hyperparameter settings、不同 base models、不同数据集上是稳定的（否则 tables 不可推广）。但 variance 高度依赖于具体配置，一个在 Qwen3 + PKU-SafeRLHF 上得出的 "minimum 15 seeds" 结论对 Llama + 其他数据集是否适用，完全未被论证。

4. **Full fine-tuning 消除 LoRA confound 的论证是合理的**，但也引入了新问题——real-world deployment 中很多人用 LoRA，full FT 的结论对 LoRA practitioners 的实用性受限。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

【3 维度打分】:

1. **Novelty: 弱-中** — 
   核心发现方向（safety 比 capability 更 fragile under retraining）已被 Fraser et al. 在 SFT 上初步证明，Larsen 在 inference-time 上证明。Proposal 的 novelty delta 是"从 SFT 扩展到 DPO/PPO/GRPO + 从 2 models 扩展到 3 scales + 从 5 seeds 扩展到 20 seeds + ANOVA 分解"——这是 **quantitative scaling**，不是 qualitative leap。SCI-T 是一个 trivial metric（max agreement ratio），几乎不贡献方法论 novelty。Minimum-seed tables 是标准 power analysis 的直接应用（Cédric et al. 2018），方法论上无新意。OXRL (arXiv:2603.19335) 已经建立了 controlled post-training comparison 的范式，本 proposal 本质上是将 OXRL 的框架加了 safety 维度。

2. **Significance: 中** — 
   研究问题本身重要——AI governance 需要知道 safety claim 的 reproducibility bound，EU AI Act 和 NIST AI RMF 确实需要这类 empirical evidence。但问题的重要性和 idea 的 contribution 是两回事。如果核心发现是 "safety 确实比 capability 更 fragile"（高概率如此），这不令人惊讶。如果核心发现是 "safety 和 capability 一样 stable"（低概率），那反而更 surprising 和有价值。Proposal 的 dual-outcome 设计部分缓解了这个问题，但主路径的 expected finding 缺乏 surprise value。

3. **Related Work: 强** — 
   Proposal 对 related work 的覆盖异常全面，清晰定位了与 Larsen (inference-time), Fraser et al. (SFT, small-scale), OXRL (capability-only), SafeDPO (no variance), SafeGRPO (method validation), SafeTuneBed (3-seed, no metric) 各自的差异。引用的论文经核实均真实存在，描述准确。差异化定位清晰：no prior work combines (a) preference optimization, (b) multi-scale, (c) 20+ seeds, (d) multi-benchmark, (e) formal metric, (f) ANOVA decomposition——这是事实。但 related work 的完善度本身也暴露了一个问题：prior work 已经非常接近这个 proposal 在做的事情，剩余的 gap 相对狭窄。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

【概率估计】: 

- 如投 CoRL 2026: 0%（desk reject，venue mismatch，无任何 robotics 内容）
- 如投适当 venue（NeurIPS/ICML/ICLR）: [18% - 28%]，中位 22%

【估计理由】:

Idea 处于 rubric 中 "15-25%: idea 方向站得住脚但内核薄弱" 到 "25-35%: idea 有实质内核但 expected finding not surprising" 的边界。

向上拉的因素：
- 研究问题对 AI governance 确实重要（Significance 中等偏上）
- 实验设计严谨（但这是执行层面，不影响 idea 评分）
- Related work 定位清晰，gap 真实存在

向下拉的因素（限制上界的关键维度：**Novelty**）：
- 核心 expected finding（safety > capability fragility）缺乏 surprise value——审稿人大概率会说 "I would have guessed this"
- 贡献本质是 scale-up + combination of existing directions，不是 conceptual innovation
- SCI-T 和 minimum-seed tables 的方法论贡献过于 trivial
- 存在明显的 trivial alternative：小规模实验即可验证核心 hypothesis

Novelty 是限制上界的主要维度。即使实验执行完美，idea 的 ceiling 也在 ~30%。

【主要风险】:

1. **"Confirmatory study" 质疑**：核心发现（safety 比 capability 更 fragile）几乎是 prior work 的直接预期推论——审稿人可能认为这是一个 expensive 但 unsurprising 的 confirmatory study，而非 discovery paper。在 top venue 中，"the answer is what we expected, but now we know for sure" 型论文的接受门槛远高于 "surprising finding" 型论文。

2. **Generalizability 质疑**：所有实验基于 Qwen3-Instruct + PKU-SafeRLHF-30K 这一组合。Minimum-seed lookup tables 的推广性（到不同 base model families, 不同 safety 数据集, 不同 scale ranges）缺乏理论保障——审稿人会质疑 "your tables are for Qwen3 on PKU-SafeRLHF; why should I trust them for my Llama model on my dataset?"
```

---

**补充说明**：本 proposal 在**形式完善度**上极高——power analysis、ANOVA 设计、dual-outcome、多 ablation 等都表明作者具有强实验设计能力。但形式完善度本身不等于 idea 质量。如果将此 proposal 视为一个 "empirical benchmark/audit" 类型的贡献（类似 HELM、AlpacaEval 等 benchmark paper），而非一个 "discovery" paper，投稿 workshop（如 NeurIPS SafeGenAI workshop）或 Datasets & Benchmarks track 可能更匹配其贡献类型。

Sources:
- [The Instability of Safety (Larsen 2025)](https://arxiv.org/abs/2512.12066)
- [Fine-Tuning Lowers Safety and Disrupts Evaluation Consistency (Fraser et al. 2025)](https://arxiv.org/abs/2506.17209)
- [OXRL: Do Post-Training Algorithms Actually Differ? (2026)](https://arxiv.org/abs/2603.19335)
- [SafeDPO (ICLR 2026 Oral)](https://arxiv.org/abs/2505.20065)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 About](https://www.corl.org/about-corl)
- [Assessing Macro and Micro Effects of Random Seeds on Fine-Tuning LLMs](https://arxiv.org/html/2503.07329v2)
- [TRACEALIGN](https://arxiv.org/pdf/2508.02063)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d7374d6-52ff-458a-8c52-d49006548b3b",
  "isSidechain": false,
  "requestId": "req_011CbCc6rJPtSi5RWU281C7J",
  "type": "assistant",
  "uuid": "92cc9833-3be6-4ed2-bd54-f0af84daa722",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WiWjkY7MtX3FwdJHPnm1ex",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 911,
      "cache_read_input_tokens": 28444,
      "output_tokens": 5905,
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
          "output_tokens": 5905,
          "cache_read_input_tokens": 28444,
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

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # How Fragile Is Safety Under Retraining? A Large-Scale Reproducibility Audit of Post-Training Alignment  ## Descr…",
  "leafUuid": "92cc9833-3be6-4ed2-bd54-f0af84daa722",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate safety alignment reproducibility proposal",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # How Fragile Is Safety Under Retraining? A Large-Scale Reproducibility Audit of Post-Training Alignment  ## Descr…",
  "leafUuid": "92cc9833-3be6-4ed2-bd54-f0af84daa722",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate safety alignment reproducibility proposal",
  "sessionId": "f8f6a9d4-f8f1-49ca-85ff-43e6e5d2e97d"
}
```

---
