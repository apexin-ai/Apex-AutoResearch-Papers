# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-27 (UTC).** ## Original idea { "tit

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/0b883d0b-c2bf-45d5-bbae-05c02a6e8950.jsonl`
- **Structured JSON:** [`70d724fe3666fbfab907.json`](../../sessions/70/70d724fe3666fbfab907.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T20:26:04.659Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T20:26:04.659Z",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Original idea\n{\n  \"title\": \"FrontierCycle: Diagnostic-Guided Iterative RL↔Distillation Scheduling for Cross-Model LLM Reasoning Post-Training\",\n  \"core_problem\": \"RLVR improves sampling efficiency (pass@1) but has limited capacity to expand the reasoning frontier (pass@k on hard problems) specifically in mathematical reasoning, while distillation from a stronger teacher expands the frontier but is bounded by teacher quality and incurs expensive teacher inference. MATH-Beyond (arXiv 2510.11653) quantifies this for mathematics: the best RL method achieves at most 21% frontier expansion, while distillation achieves 66% — though this gap is task-dependent, with ProRL (NeurIPS 2025) demonstrating RL achieves substantial frontier expansion on logic puzzles (+54.8%) and coding tasks. Current approaches to combining RL and distillation operate in two distinct regimes with fundamentally different cost structures:\\n\\nREGIME 1 — SELF-DISTILLATION (cheap teacher): The student model serves as its own teacher with privileged information (e.g., verified reasoning traces, answer visibility). Per-step teacher inference is essentially free since the teacher IS the student with different context. The May 2026 surge of unified single-phase methods — Rebellious Student/RLRT (arXiv 2605.10781), AntiSD (arXiv 2605.11609), CEPO (arXiv 2605.19436), SDAR (arXiv 2605.15155), Uni-OPD (arXiv 2605.03677) — alongside earlier unified methods (RLSD arXiv 2604.03128, CHORD arXiv 2508.11408, KDRL arXiv 2506.02208) all operate in this regime. These methods achieve RL-distillation synergy without phase switching because per-step teacher compute is negligible.\\n\\nREGIME 2 — CROSS-MODEL DISTILLATION (expensive teacher): A much larger external teacher (e.g., 235B MoE → 8B dense student) provides qualitatively different reasoning capabilities. Per-step teacher inference dominates training compute. This is the regime of DeepSeek-R1 distillation (671B→7B), Klear-Reasoner (DeepSeek-R1-0528→Qwen3-8B with 1.5M samples), and Beyond GRPO's sparse-to-dense pipeline. In this regime, invoking the teacher at every training step is prohibitively expensive, creating a genuine scheduling problem: WHEN to invoke the expensive teacher and for HOW LONG.\\n\\nWithin the cross-model regime, current scheduling approaches are limited: (1) fixed multi-stage pipelines (Beyond GRPO, SIRI) with predetermined sequencing regardless of student state; (2) single-transition diagnostic switching (Plasticity-Ceiling Framework, ACL 2026) addressing only the initial SFT→RL handoff; (3) static pre-RL prediction (Quagmires, arXiv 2510.01624) that uses pass@large-k to predict RL outcomes before training begins but not during it. The Plasticity-Ceiling Framework validates that diagnostic-guided switching substantially improves outcomes — sequential SFT-then-DAPOd achieves 78.1 on Qwen2.5-7B vs. 74.3 for pure DAPOd, and the projected ceiling reaches 84.0 when scaling to SFT889K (Pearson r=−0.92 between minimum validation loss and ceiling on Qwen2.5-7B; r=−0.96 on Llama3.2-3B). Notably, synchronized SFT-RL (LUFFY, 72.7) underperforms sequential switching (78.1), supporting phase separation over continuous mixing for cross-model settings. However, no existing work provides adaptive iterative multi-cycle RL↔distillation scheduling where each cycle's duration is dynamically determined by a diagnostic signal, specifically designed for the cross-model distillation regime where teacher compute amortization is the primary design constraint.\",\n  \"opportunity\": \"The Plasticity-Ceiling Framework validates a powerful principle for the cross-model distillation regime: diagnostic-guided phase transitions substantially outperform both fixed schedules and synchronized training (78.1 for sequential SFT-then-DAPOd vs. 72.7 for synchronized LUFFY on Qwen2.5-7B). Quagmires in SFT-RL Post-Training independently validates that pass@large-k predicts RL outcomes (R² up to 0.88, a 2× improvement over SFT score prediction). Pass@k Training (arXiv 2508.10751) further validates pass@k as an active training signal — they use it as a per-step reward to balance exploration and exploitation during RLVR, achieving 17.9% vs. 12.9% Pass@1 on Enigmata for Qwen2.5-7B.\\n\\nWe propose extending these principles from single-transition or pre-training prediction to iterative multi-cycle RL↔distillation scheduling in the CROSS-MODEL DISTILLATION setting, addressing four limitations: (a) single-transition methods (Plasticity-Ceiling) cannot recover if the RL phase saturates prematurely; (b) fixed pipelines (Beyond GRPO) allocate predetermined compute fractions regardless of the student's actual learning state; (c) static prediction (Quagmires) cannot detect mid-training saturation; (d) unified per-step methods are designed for self-distillation where teacher compute is free — they do not address the scheduling problem inherent to expensive cross-model teachers.\\n\\nTHE CYCLING HYPOTHESIS: We hypothesize that in cross-model distillation, iterative RL↔distillation cycling provides compounding benefits because: (i) the external teacher (235B) provides qualitatively different reasoning capabilities than the student can discover through RL alone — unlike self-distillation where the teacher's knowledge is bounded by the student's own architecture; (ii) RL consolidation phases compress absorbed knowledge into pass@1 proficiency, creating capacity for absorbing new patterns in subsequent distillation phases; (iii) 'Why Self-Distillation Sometimes Degrades Reasoning' (arXiv 2603.24472) shows self-distillation degrades math reasoning by suppressing epistemic verbalization (up to 40% drops), suggesting that interleaving RL phases (which preserve exploration via entropy management) with distillation phases (which inject new knowledge) avoids this degradation mechanism. ReMiT (arXiv 2602.03075) provides preliminary evidence: their iterative mid-training ↔ RL cycling shows cascading improvements across two cycles (ReMiT → ReMiT2), validating that iterative cycling can compound rather than diminish. However, this hypothesis is explicitly testable and forms the go/no-go gate for the project: if the second RL phase after distillation does not expand pass@k beyond the first RL plateau, iterative cycling provides no value and the project pivots to optimizing single-cycle scheduling.\\n\\nSCOPE CLARIFICATION: FrontierCycle explicitly targets the cross-model distillation regime. For self-distillation settings where per-step teacher compute is free, unified methods (Rebellious Student, AntiSD, CEPO, RLSD, CHORD) are likely more efficient because they avoid the overhead of phase transition management. FrontierCycle's value proposition is specifically teacher compute amortization — invoking an expensive external teacher only when the student's frontier has genuinely stalled — which is only valuable when teacher inference is costly.\",\n  \"landscape\": \"The Plasticity-Ceiling Framework (arXiv 2512.11470, ACL 2026) is the closest prior work to our concept of diagnostic-guided phase switching. It decomposes post-training performance into P_sft and PL_rl, identifies that minimum SFT validation loss predicts final ceiling (Pearson r=−0.92 on Qwen2.5-7B, r=−0.96 on Llama3.2-3B), and recommends switching to RL at the 'stable sub-phase' (validation loss ≤ 1.02 × L_min). On Qwen2.5-7B, sequential SFT-then-DAPOd achieves 78.1 vs. 74.3 for pure DAPOd; the projected ceiling reaches 84.0 on SFT889K at optimal switching. The synchronized SFT-RL paradigm (LUFFY) achieves only 72.7, empirically supporting phase separation. However, it supports only a single SFT→RL transition with no iterative cycling and its validation-loss criterion detects SFT overfitting, not RL frontier exhaustion.\\n\\nQuagmires in SFT-RL Post-Training (arXiv 2510.01624, NeurIPS 2025 MATH-AI Workshop) trains hundreds of models up to 12B and identifies pass@large-k (pass@64, pass@256) and generalization loss as strong proxies for predicting RL outcomes, improving R² by up to 0.5 (2×) over SFT score prediction. Their use is limited to static pre-RL prediction; FrontierCycle extends pass@k-derived metrics to dynamic real-time switching signals assessed repeatedly during training.\\n\\nPass@k Training (arXiv 2508.10751, ByteDance/RUC) uses pass@k directly as a per-step REWARD signal in RLVR to balance exploration and exploitation, deriving an analytical advantage function and achieving 17.9% Pass@1 on Enigmata vs. 12.9% for standard Pass@1 training on Qwen2.5-7B. This independently validates pass@k as a rich active signal for guiding training decisions. The key differentiation: Pass@k Training uses pass@k at per-step reward granularity to improve exploration within a single RL phase, while FrontierCycle uses pass@k-derived SEG at phase-level diagnostic granularity to determine when to switch between RL and distillation phases. Both elevate pass@k from a passive evaluation metric to an active signal, but at different granularities serving different purposes — they are complementary rather than competing.\\n\\nMAY 2026 UNIFIED METHODS SURGE — SELF-DISTILLATION REGIME: At least 6 new unified single-phase RL+distillation methods appeared in May 2026, almost all operating in the SELF-DISTILLATION regime where per-step teacher compute is free: Rebellious Student/RLRT (arXiv 2605.10781) reverses teacher signals on correct rollouts, improving over GRPO by 8.9% average across Qwen3-4B/8B; AntiSD (arXiv 2605.11609) ascends student-teacher divergence via PMI analysis, improving final accuracy by up to 11.5 points; CEPO (arXiv 2605.19436) uses contrastive evidence from correct vs. wrong rollouts for token-level credit assignment; SDAR (arXiv 2605.15155) gates self-distillation signals for agentic RL (+9.4% on ALFWorld); Uni-OPD (arXiv 2605.03677) unifies on-policy distillation with dual-perspective optimization across 16 benchmarks. dGRPO (arXiv 2605.12227) combines GRPO with on-policy distillation in a unified objective for long-context reasoning, targeting the 8K-32K token regime where sparse rewards are particularly unstable. These methods collectively demonstrate that unified objectives excel when teacher inference is cheap (self-distillation). FrontierCycle does not compete with these methods in their target regime; instead, it addresses the complementary cross-model regime where an expensive external teacher (235B MoE) makes per-step inference prohibitive.\\n\\nSelf-Distilled RLVR (RLSD, arXiv 2604.03128, Apr 2026) uses environment rewards for update direction and self-distillation for magnitude modulation, achieving +2.32% over GRPO on multimodal reasoning. RLAD (arXiv 2602.22495, Feb 2026) integrates KD into RL via Trust Region Ratio Distillation. ATESD (arXiv 2605.11458, May 2026) proposes a Beta-policy meta-controller for within-distillation teacher exposure control, orthogonal to FrontierCycle's inter-phase scheduling.\\n\\nBeyond GRPO (arXiv 2605.12483, May 2026) proposes a fixed 3-stage sparse-to-dense reward pipeline, achieving 79.3% MATH and 25.2% AIME 2024 on Qwen3-1.7B. This is FrontierCycle's CENTRAL fixed-pipeline baseline in the cross-model regime: it demonstrates that well-designed single-pass sequencing captures substantial RL-distillation benefits. Our iterative cycling must demonstrably outperform this.\\n\\nReMiT (arXiv 2602.03075, Feb 2026) provides the closest evidence for iterative cycling: their RL-guided mid-training framework shows cascading improvements across two cycles (ReMiT → ReMiT2), with the second cycle outperforming the first. While ReMiT operates at the pre-training ↔ post-training boundary rather than RL ↔ distillation, it validates the principle that iterative cycling can compound rather than diminish.\\n\\n'Why Self-Distillation Sometimes Degrades Reasoning' (arXiv 2603.24472, Mar 2026) shows that self-distillation suppresses epistemic verbalization in math reasoning, causing up to 40% performance drops on OOD problems. This motivates FrontierCycle's interleaving approach: RL phases preserve exploration (entropy management via Entrocraft), while distillation phases from an external teacher inject genuinely new reasoning patterns without suppressing the student's uncertainty expression, because the teacher's knowledge is architecturally distinct rather than a privileged version of the student's own knowledge.\\n\\nKlear-Reasoner-8B (arXiv 2508.07629) achieves 90.5% on AIME 2024 (64K inference budget; 83.2% at 32K) with a simple SFT+GPPO pipeline from Qwen3-8B-Base using 1.5M DeepSeek-R1-0528 distillation samples. This sets a high bar for 8B-scale performance and contextualizes the overhead any adaptive method must justify.\\n\\nCoPD (arXiv 2604.27083, Apr 2026) achieves RL-distillation interleaving through parallel multi-expert co-evolution. CoDistill-GRPO (arXiv 2605.08873) simultaneously trains large and small models through bidirectional GRPO rewards. CHORD (arXiv 2508.11408, ICLR 2026) dynamically weights SFT within on-policy RL via token-wise uncertainty. SRFT (arXiv 2506.19767) validates entropy as a diagnostic. HPT (arXiv 2509.04419) provides per-question binary switching. Entrocraft (arXiv 2604.26326) achieves ~17% improvement in pass@32 over GRPO through entropy curve control. EOPD (arXiv 2603.07079) augments reverse KL with forward KL at high teacher-entropy tokens. MATH-Beyond (arXiv 2510.11653) quantifies the RL/distillation frontier gap. ProRL (NeurIPS 2025, arXiv 2505.24864) shows RL achieves +54.8% on logic puzzles but diminished frontier on math. Yu (arXiv 2511.16231) proves pass@k gap collapse under policy concentration.\",\n  \"inspired_by\": \"field_gap['cross-model distillation scheduling: expensive teacher amortization via iterative cycling'] + validated_principle[Plasticity-Ceiling Framework: sequential 78.1 vs. synchronized 72.7 on Qwen2.5-7B] + supporting_evidence[Quagmires: pass@large-k predicts RL outcomes R² up to 0.88] + complementary_validation[Pass@k Training: pass@k as active reward signal at per-step granularity] + cycling_evidence[ReMiT: cascading improvements across two cycles ReMiT → ReMiT2] + degradation_insight[Self-distillation degrades math reasoning (2603.24472) → cross-model avoids this via architecturally distinct teacher] + regime_clarification[May 2026 unified methods surge targets self-distillation; FrontierCycle targets cross-model distillation] + mathematical_foundation[Yu's pass@k gap collapse + Entrocraft's entropy-advantage relationship] + design_principle[ZClip's z-score adaptive thresholds]\",\n  \"approach\": \"We propose FrontierCycle, an iterative multi-cycle RL↔distillation scheduling framework with diagnostic-guided phase transitions for LLM reasoning post-training, specifically designed for the CROSS-MODEL DISTILLATION REGIME where per-step teacher inference is expensive. The CORE CONTRIBUTION is the cycling framework architecture — a general mechanism for adaptive multi-cycle scheduling where each phase's duration is dynamically determined by a diagnostic signal — rather than any specific diagnostic metric.\\n\\nThe framework has three components: (1) a DIAGNOSTIC MODULE evaluating candidate switching metrics on a held-out validation set every 100 training steps, (2) a SWITCHING CONTROLLER determining phase transitions using z-score-normalized thresholds, and (3) PHASE-SPECIFIC OPTIMIZERS applying the best available within-phase method (Entrocraft-style entropy annealing during RL, EOPD-style entropy-aware KL during distillation, with ATESD-compatible teacher exposure control composable during distillation phases).\\n\\nWHY DISCRETE PHASE SWITCHING IN THE CROSS-MODEL REGIME: FrontierCycle's design is motivated by the cost structure of cross-model distillation. When the teacher is Qwen3-235B-A22B and the student is 8B dense, each teacher forward pass costs ~3× the student (22B active parameters vs. 8B). Over a full training run of ~10K steps with multiple rollouts per step, per-step teacher inference adds ~300% compute overhead. FrontierCycle invokes the teacher only during distillation phases (estimated 30-40% of total training time), reducing teacher overhead to ~100-120%. For self-distillation settings, where teacher overhead is negligible, unified methods (Rebellious Student, AntiSD, CEPO, RLSD) are likely more efficient — FrontierCycle does not claim superiority there. The Plasticity-Ceiling paper's finding that sequential SFT-then-DAPOd (78.1) outperforms synchronized LUFFY (72.7) further supports phase separation in cross-model settings. Additionally, discrete phases enable specialized optimization: Entrocraft entropy annealing during RL requires different hyperparameters than EOPD entropy-aware KL during distillation.\\n\\nDIAGNOSTIC SIGNAL INVESTIGATION (Stage 0): We treat the diagnostic signal choice as an empirical question. We compare four candidate signals: (a) SEG = pass@k − pass@1 — building on both Quagmires (pass@k predicts RL outcomes) and Pass@k Training (pass@k as active signal at per-step reward granularity; we use it at phase-level diagnostic granularity); (b) EN-SEG = SEG / max(H(π), ε_H) — entropy-normalized for cross-phase comparability; (c) adapted Plasticity-Ceiling validation loss — extending their criterion to RL-phase saturation detection; (d) pass@k growth rate — direct frontier expansion velocity.\\n\\nCYCLING VALIDATION GATE (Stage 0.5 — NEW): Before committing to full iterative cycling experiments, we validate the cycling hypothesis with a minimal single-cycle test. Starting from DeepSeek-R1-0528-Qwen3-8B, we: (i) run RL (GRPO+Entrocraft) until the diagnostic indicates frontier exhaustion (pass@k plateaus); (ii) record the plateau pass@k value P1; (iii) run cross-model distillation from Qwen3-235B-A22B until the diagnostic indicates absorption saturation; (iv) run a second RL phase and measure whether pass@k exceeds P1. GO/NO-GO DECISION: If the second RL phase achieves pass@k > P1 + ε (where ε = 1 percentage point on MATH-500), iterative cycling has demonstrated frontier expansion value and we proceed to Stage 1. If pass@k ≤ P1 + ε, iterative cycling provides no benefit over single-pass scheduling, and we PIVOT to optimizing single-cycle scheduling (determining the optimal RL/distillation budget allocation within one cycle, effectively improving Beyond GRPO with diagnostic-guided switching instead of fixed stages). This go/no-go gate ensures the project produces a meaningful contribution regardless of the cycling hypothesis outcome.\\n\\nWHY CROSS-MODEL CYCLING MAY AVOID DIMINISHING RETURNS: 'Why Self-Distillation Sometimes Degrades Reasoning' (arXiv 2603.24472) identifies the mechanism: self-distillation suppresses epistemic verbalization (uncertainty tokens like 'Wait', 'Let me reconsider') because the teacher's privileged information eliminates uncertainty. In cross-model distillation, the teacher (235B MoE) has architecturally distinct reasoning patterns — it doesn't simply have privileged information about the student's answer, it has genuinely different reasoning strategies developed through its larger capacity. The RL phases preserve exploration and uncertainty expression (via entropy management), while distillation phases inject new patterns without the same suppression mechanism. ReMiT's cascading improvements across two cycles (ReMiT → ReMiT2) provide preliminary evidence that iterative cycling can compound in related settings.\\n\\nEXPERIMENTAL PLAN: STAGE 0 — DIAGNOSTIC SIGNAL COMPARISON (2 weeks): Run 2000-step RL and 2000-step distillation, logging all candidate diagnostics. Compare on signal-to-noise ratio and switching stability. STAGE 0.5 — CYCLING VALIDATION GATE (2 weeks): Single-cycle test (RL→distillation→RL) measuring whether pass@k exceeds the first RL plateau. GO/NO-GO decision. STAGE 1 — ITERATIVE CYCLING (if go) OR SINGLE-CYCLE OPTIMIZATION (if no-go) (5-7 weeks): If cycling validated: run 3-5 cycles, monitoring diagnostic every 100 steps on compact diagnostic set (200 problems, pass@32). If cycling invalidated: optimize single-cycle budget allocation with diagnostic-guided switching.\\n\\nCORE BASELINES (6): (1) Beyond GRPO fixed pipeline — CENTRAL comparison; (2) Plasticity-Ceiling-guided single SFT→RL transition; (3) CHORD continuous mixing (cross-model teacher); (4) RLSD unified self-distillation+RL (self-distillation regime for comparison); (5) Entrocraft-only RL (no distillation); (6) Pure distillation. KEY ABLATIONS (5): (1) Diagnostic signal comparison within FrontierCycle; (2) Adaptive cycling vs. fixed-interval cycling; (3) z-score relative thresholds vs. absolute thresholds (threshold transfer from MATH to AIME/LiveCodeBench); (4) Number of cycles: 1 vs. 3 vs. 5; (5) Teacher compute analysis: H100-hours for FrontierCycle vs. CHORD vs. Beyond GRPO. Evaluate on AIME 2024, MATH-500, and LiveCodeBench, reporting pass@1, pass@32, per-difficulty breakdowns, teacher compute (H100-hours), and threshold transfer success rates.\\n\\nPositioning relative to Klear-Reasoner-8B: we target the moderate-data regime — if FrontierCycle at 32K matches or exceeds Klear-Reasoner's 32K performance (83.2%) with fewer teacher demonstrations, that demonstrates intelligent scheduling as an alternative to brute-force data scaling.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"2800-3600 H100-hours: teacher inference (~400), RL training (~400), pass@32 evaluation (~40), Stage 0 diagnostics (~100), Stage 0.5 cycling validation (~150), baselines (~700), ablations (~500), buffer (~510)\",\n      \"timeline\": \"15-18 weeks (2 weeks Stage 0, 2 weeks Stage 0.5 + go/no-go, 3 weeks implementation, 5-7 weeks experiments, 3-4 weeks writing)\",\n      \"estimated_gpu_cost\": \"$5,600-7,200 at $2/H100-hr\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"2200-2800 H100-hours (Claude assists with veRL integration, Stage 0.5 automated analysis, early stopping)\",\n      \"timeline\": \"12-15 weeks (1.5 weeks Stage 0, 1.5 weeks Stage 0.5, 2.5 weeks implementation, 4-6 weeks experiments, 2-3 weeks writing)\",\n      \"claude_api_cost\": \"$400-600\",\n      \"estimated_gpu_cost\": \"$4,400-5,600 at $2/H100-hr\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"1800-2300 H100-hours (automated scheduling, adaptive sweep, Stage 0.5 as automated go/no-go gate)\",\n      \"timeline\": \"9-12 weeks (1 week Stage 0, 1 week Stage 0.5 + automated pivot decision, 2 weeks implementation, 4-6 weeks automated runs, 1-2 weeks paper generation)\",\n      \"claude_api_cost\": \"$700-1000\",\n      \"estimated_gpu_cost\": \"$3,600-4,600 at $2/H100-hr\",\n      \"speed_bottleneck\": \"Teacher inference from Qwen3-235B-A22B requires 4×H100 per batch; pass@32 evaluation on compact 200-problem set takes ~15 min per checkpoint on 1×H100\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (submission deadline: Sep 24, 2026)\",\n    \"ARR October 2026 cycle (submission: Oct 12, 2026) for commitment to EACL 2027 or NAACL 2027\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Rethinking Expert Trajectory Utilization in LLM Post-training for Mathematical Reasoning — Plasticity-Ceiling Framework (arXiv 2512.11470, ACL 2026)\",\n    \"Quagmires in SFT-RL Post-Training: When High SFT Scores Mislead and What to Use Instead (arXiv 2510.01624, NeurIPS 2025 MATH-AI Workshop)\",\n    \"Pass@k Training for Adaptively Balancing Exploration and Exploitation of Large Reasoning Models (arXiv 2508.10751, ByteDance/RUC)\",\n    \"Combining On-Policy Optimization and Distillation for Long-Context Reasoning in Large Language Models — dGRPO (arXiv 2605.12227, May 2026)\",\n    \"Rebellious Student: Reversing Teacher Signals for Reasoning Exploration with Self-Distilled RLVR — RLRT (arXiv 2605.10781, May 2026)\",\n    \"Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information — AntiSD (arXiv 2605.11609, May 2026)\",\n    \"CEPO: RLVR Self-Distillation using Contrastive Evidence Policy Optimization (arXiv 2605.19436, May 2026)\",\n    \"Self-Distilled Agentic Reinforcement Learning — SDAR (arXiv 2605.15155, May 2026)\",\n    \"Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe (arXiv 2605.03677, May 2026)\",\n    \"ReMiT: RL-Guided Mid-Training for Iterative LLM Evolution (arXiv 2602.03075, Feb 2026)\",\n    \"Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs? (arXiv 2603.24472, Mar 2026)\",\n    \"Self-Distilled RLVR — RLSD (arXiv 2604.03128, Apr 2026)\",\n    \"Reinforcement-aware Knowledge Distillation for LLM Reasoning — RLAD (arXiv 2602.22495, Feb 2026)\",\n    \"Adaptive Teacher Exposure for Self-Distillation in LLM Reasoning — ATESD (arXiv 2605.11458, May 2026)\",\n    \"Co-Evolving Policy Distillation — CoPD (arXiv 2604.27083, Apr 2026)\",\n    \"Klear-Reasoner: Advancing Reasoning Capability via Gradient-Preserving Clipping Policy Optimization (arXiv 2508.07629, 2025)\",\n    \"CoDistill-GRPO: A Co-Distillation Recipe for Efficient Group Relative Policy Optimization (arXiv 2605.08873, May 2026)\",\n    \"Reinforcement Learning vs. Distillation: Understanding Accuracy and Capability in LLM Reasoning (arXiv 2505.14216, 2025)\",\n    \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? (arXiv 2504.13837, 2025)\",\n    \"MATH-Beyond: A Benchmark for RL to Expand Beyond the Base Model (arXiv 2510.11653, 2025)\",\n    \"ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models (NeurIPS 2025, arXiv 2505.24864)\",\n    \"Beyond GRPO and On-Policy Distillation: An Empirical Sparse-to-Dense Reward Principle for Language-Model Post-Training (arXiv 2605.12483, May 2026)\",\n    \"HPT: Towards a Unified View of Large Language Model Post-Training (arXiv 2509.04419, 2025)\",\n    \"CHORD: Controllable Harmonization of On- and Off-Policy RL via Dynamic Weighting (arXiv 2508.11408, ICLR 2026)\",\n    \"SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning (arXiv 2506.19767, 2025)\",\n    \"Entrocraft: Addressing Performance Saturation for LLM RL via Precise Entropy Curve Control (arXiv 2604.26326, 2026)\",\n    \"EOPD: Entropy-Aware On-Policy Distillation of Language Models (arXiv 2603.07079, 2026)\",\n    \"Pass@k Metric for RLVR: A Diagnostic Tool of Exploration, But Not an Objective (arXiv 2511.16231, 2025)\",\n    \"The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models (arXiv 2505.22617, 2025)\",\n    \"EntroPIC: Towards Stable Long-Term Training of LLMs via Entropy Stabilization with PI Control (arXiv 2511.15248, 2025)\",\n    \"Beyond Pass@k: Breadth-Depth Metrics for LLM Reasoning — Cover@tau (arXiv 2510.08325, 2025)\",\n    \"KDRL: Post-Training Reasoning LLMs via Unified Knowledge Distillation and Reinforcement Learning (arXiv 2506.02208, 2025)\",\n    \"JustRL: Scaling a 1.5B LLM with a Simple RL Recipe (arXiv 2512.16649, ICLR 2026 Blogpost)\",\n    \"ZClip: Adaptive Spike Mitigation for LLM Pre-Training (arXiv 2504.02507, 2025)\"\n  ],\n  \"description\": \"FrontierCycle addresses a fundamental scheduling problem in cross-model LLM reasoning post-training: when to invoke an expensive external teacher (e.g., 235B MoE) and for how long, given that per-step teacher inference dominates training compute. We distinguish two regimes: self-distillation, where unified per-step methods (Rebellious Student, AntiSD, CEPO, RLSD) excel because the teacher IS the student with negligible overhead, and cross-model distillation, where teacher inference adds ~300% per-step overhead, creating a genuine scheduling problem. FrontierCycle targets exclusively the cross-model regime — the setting of DeepSeek-R1 distillation, Klear-Reasoner, and Beyond GRPO. The framework proposes iterative multi-cycle RL↔distillation scheduling where each phase's duration is dynamically determined by a diagnostic signal evaluated every 100 training steps. We investigate four candidate diagnostics, including SEG (pass@k minus pass@1) building on both Quagmires' validation of pass@k as an RL outcome predictor and Pass@k Training's use of pass@k as an active per-step reward signal. A z-score-normalized switching controller triggers phase transitions when frontier expansion stalls. Critically, we introduce a cycling validation gate (Stage 0.5): before committing to iterative cycling, we test whether a second RL phase after distillation expands pass@k beyond the first RL plateau. If validated, we proceed to multi-cycle experiments; if falsified, we pivot to optimizing single-cycle scheduling with diagnostic-guided switching — ensuring a meaningful contribution regardless. The cycling hypothesis is motivated by evidence that cross-model distillation avoids the epistemic verbalization suppression that degrades self-distillation (arXiv 2603.24472), and by ReMiT's demonstration of cascading improvements across iterative cycles. Phase-specific optimizers apply Entrocraft-style entropy annealing during RL and EOPD-style entropy-aware KL during distillation, with teacher inference restricted to distillation phases (estimated 30-40% of training), reducing overhead to ~100-120%. We evaluate against Beyond GRPO as the central fixed-pipeline baseline, with six core baselines and five ablations across AIME 2024, MATH-500, and LiveCodeBench.\",\n  \"project_name\": \"frontier_cycle\",\n  \"source\": \"web_research\",\n  \"reviewer_response\": {\n    \"issue_1_factual_error_plasticity_ceiling\": \"FIXED. All Plasticity-Ceiling numbers corrected against the paper (arXiv 2512.11470v2 HTML verified). Previous claim of '85.7 ceiling' replaced with the correct values: 78.1 (actual SFT-then-DAPOd execution on Qwen2.5-7B), 84.0 (projected ceiling at SFT889K with optimal switching timing), and 74.3 (pure DAPOd). Pearson correlation corrected from r=−0.90 to r=−0.92 for Qwen2.5-7B and r=−0.96 for Llama3.2-3B. The synchronized baseline LUFFY (72.7) is now included to strengthen the argument for phase separation over continuous mixing. All numbers verified against the v2 HTML rendering of the paper.\",\n    \"issue_2_quagmires_citation\": \"FIXED. Quagmires in SFT-RL Post-Training (arXiv 2510.01624, NeurIPS 2025 MATH-AI Workshop) integrated as supporting evidence throughout. Their key finding: pass@64/pass@256 and generalization loss predict RL outcomes with R² up to 0.88 (2× improvement over SFT score prediction), trained on hundreds of models up to 12B. Clear differentiation: Quagmires uses pass@k as a STATIC one-shot predictor assessed BEFORE RL training begins (predicting which SFT checkpoint yields best RL outcome), while FrontierCycle extends pass@k-derived metrics to DYNAMIC real-time switching signals assessed repeatedly DURING training to trigger phase transitions. Quagmires validates the general principle that pass@k captures RL potential better than pass@1/SFT scores; FrontierCycle operationalizes this principle for iterative scheduling.\",\n    \"issue_3_enseg_reframing\": \"FIXED via MAJOR REFRAMING. The core contribution is now explicitly the ITERATIVE CYCLING FRAMEWORK with diagnostic-guided phase transitions, NOT EN-SEG specifically. Title changed to center the framework, not the metric. EN-SEG is repositioned as one of four candidate diagnostics investigated empirically in Stage 0, alongside raw SEG, validation loss adaptation, and pass@k growth rate. The description and approach now consistently frame the diagnostic choice as 'an empirical question resolved through systematic comparison' rather than claiming EN-SEG as the contribution.\",\n    \"issue_4_unified_competitors\": \"FIXED. Self-Distilled RLVR (RLSD, arXiv 2604.03128) integrated as a core baseline (#4) and extensively discussed in the landscape. RLAD (arXiv 2602.22495) also added. The argument for discrete phase switching over unified objectives is strengthened with three specific points: (1) TEACHER COMPUTE AMORTIZATION, (2) EMPIRICAL EVIDENCE from Plasticity-Ceiling, (3) PHASE-SPECIFIC OPTIMIZATION.\",\n    \"issue_5_venue_correction\": \"FIXED. ARR July 2026 (July 15) removed — only ~7 weeks remain, insufficient for any timeline. Replaced with ARR October 2026 (submission: Oct 12, 2026) for commitment to EACL 2027 or NAACL 2027 (~20 weeks from now). ICLR 2027 (submission: Sep 24, 2026, ~17 weeks) retained as primary target. Both are feasible under human_in_loop (12-15 weeks) and auto_research (9-12 weeks) timelines.\",\n    \"issue_6_passk_training_citation\": \"FIXED. Pass@k Training (arXiv 2508.10751) integrated into landscape and approach. Clear differentiation established: Pass@k Training uses pass@k at PER-STEP REWARD granularity to improve exploration within a single RL phase (analytical advantage function, 17.9% vs. 12.9% on Enigmata for Qwen2.5-7B); FrontierCycle uses pass@k-derived SEG at PHASE-LEVEL DIAGNOSTIC granularity to determine when to switch between RL and distillation phases. Both elevate pass@k from a passive evaluation metric to an active training signal, but at different granularities serving complementary purposes — they strengthen each other's argument that pass@k is a rich signal.\",\n    \"issue_7_dgrpo_citation\": \"FIXED. dGRPO (arXiv 2605.12227) added to the unified-competitor list in the landscape section alongside RLSD/RLAD. dGRPO combines GRPO with on-policy distillation in a unified objective targeting long-context reasoning (8K-32K tokens). Positioned as part of the broader unified methods landscape.\",\n    \"issue_8_unified_methods_headwind\": \"FIXED via MAJOR REFRAMING. The entire proposal is now structured around a two-regime taxonomy: SELF-DISTILLATION (cheap teacher, unified methods dominate) vs. CROSS-MODEL DISTILLATION (expensive teacher, phase scheduling matters). The May 2026 surge of unified methods (Rebellious Student/RLRT, AntiSD, CEPO, SDAR, Uni-OPD) is explicitly analyzed — almost all operate in the self-distillation regime where per-step teacher compute is free. FrontierCycle is explicitly scoped to the cross-model distillation regime (235B MoE → 8B dense) where per-step teacher inference adds ~300% compute overhead. This is stated as a scope clarification, not a limitation — cross-model distillation is the regime of DeepSeek-R1 distillation, Klear-Reasoner, and Beyond GRPO, which are among the most impactful recent results. For self-distillation settings, we explicitly acknowledge that unified methods are likely more efficient. The approach section quantifies teacher compute savings (300% per-step overhead reduced to 100-120% via phase amortization).\",\n    \"issue_9_iterative_cycling_extrapolation\": \"FIXED via STAGE 0.5 GO/NO-GO GATE and THEORETICAL ARGUMENT. (1) Stage 0.5 added as a cycling validation gate: after one full RL→distillation→RL cycle, we measure whether the student's pass@k frontier exceeds the first RL plateau (P1). If pass@k > P1 + ε (ε = 1pp on MATH-500), cycling is validated; if not, the project PIVOTS to single-cycle optimization, ensuring a meaningful contribution regardless. (2) Theoretical argument for why cross-model cycling avoids diminishing returns: 'Why Self-Distillation Sometimes Degrades Reasoning' (arXiv 2603.24472) shows self-distillation degrades math reasoning via epistemic verbalization suppression — cross-model distillation from a 235B MoE provides architecturally distinct reasoning, not just privileged information, so this degradation mechanism should not apply. (3) ReMiT (arXiv 2602.03075) provides empirical evidence: iterative mid-training ↔ RL cycling shows cascading improvements across two cycles (ReMiT → ReMiT2). The cycling hypothesis is now explicitly stated as TESTABLE with clear falsification criteria.\"\n  }\n}\n\n## Reviewer feedback (round 7)\nIssues: [\"TOPIC MISMATCH WITH USER REQUIREMENTS: The user asked for 'Synthetic Data and Self-Improvement for Mathematical Reasoning Training.' FrontierCycle is about cross-model distillation scheduling from an external 235B teacher — this is fundamentally NOT self-improvement. Self-improvement means the model improves using its own capabilities (self-play, STaR, self-training, RLVR). Cross-model distillation (DeepSeek-R1-0528→Qwen3-8B, Qwen3-235B→8B) is teacher-guided training, the opposite paradigm. The idea addresses a valid research question but does not match the user's stated topic.\", \"SIRI (arXiv 2509.25176) MISCHARACTERIZED: The idea labels SIRI as a 'fixed multi-stage pipeline' alongside Beyond GRPO, but SIRI actually performs 3 iterations of compression↔expansion cycling during RL, achieving 43.2% improvement on AIME24 with 46.9% token reduction. While SIRI cycles within RL (rollout length control) rather than between RL and distillation, it IS an iterative cycling method for math reasoning and should be properly characterized and differentiated as the closest existing iterative cycling approach.\", \"MISSING RELEVANT WORK — CLPD (arXiv 2605.11260, May 2026): Curriculum Learning-Guided Progressive Distillation explicitly addresses teacher scheduling by progressively scheduling teachers of increasing capacity — directly relevant to the cross-model distillation scheduling problem FrontierCycle targets.\", \"MISSING RELEVANT WORK — 'Large Language Model Post-Training: A Unified View' (arXiv 2604.07941, Apr 2026): This 38-page paper directly discusses multi-stage pipeline composition, behavioral consolidation roles, and argues that 'progress increasingly depends on coordinated systems design.' It provides theoretical grounding for FrontierCycle's stage-composition approach and should be cited.\", \"MISSING RELEVANT WORK — PRISM (arXiv 2604.28123, Apr 2026): Inserts an explicit distribution-alignment stage between SFT and RL to mitigate distributional drift — relevant as another diagnostic-guided multi-stage approach to post-training pipeline design.\", \"FIELD MOMENTUM CREATES EXISTENTIAL RISK: The May 2026 unified methods surge now includes not just the 6+ per-step methods cited, but also theoretical unification work: 'Decoupling KL and Trajectories' (2605.16826) and 'Post-Training is About States, Not Tokens' (2605.22731) both provide theoretical frameworks showing SFT, RL, and OPD are points in a continuous design space. This theoretical momentum toward continuous-space optimization further undercuts the case for discrete phase switching.\"]\nFeedback: 1) ADDRESS TOPIC MISMATCH: The user requested 'Synthetic Data and Self-Improvement for Mathematical Reasoning Training.' Either (a) pivot the idea to genuinely address self-improvement — e.g., iterative RL↔self-generated-data cycling where the model generates its own training data (no external teacher), or (b) explicitly acknowledge the mismatch and reframe around how cross-model distillation data IS synthetic data and the RL phases constitute self-improvement phases within the cycle. Option (a) is stronger — self-improvement with iterative cycling is a natural fit for the user's topic and avoids the expensive-teacher-compute problem entirely. 2) FIX SIRI CHARACTERIZATION: SIRI performs 3 iterations of compression↔expansion cycling, not fixed sequencing. Properly differentiate: SIRI cycles within RL (rollout length), FrontierCycle cycles between RL and distillation (training objective). Acknowledge SIRI as the closest existing iterative cycling method for math reasoning. 3) ADD MISSING CITATIONS: Include CLPD (2605.11260), the Unified View paper (2604.07941), and consider PRISM (2604.28123) — all directly relevant to multi-stage pipeline design and teacher scheduling. 4) STRENGTHEN IMPACT ARGUMENT: The cross-model distillation niche is real but shrinking as the field converges on self-distillation. Either (a) expand scope to include self-distillation cycling, or (b) argue more forcefully why cross-model distillation will remain important (citing DeepSeek-R1, Klear-Reasoner as landmark results that required cross-model distillation).\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields.\n\n## 停滞提醒\n经过 7 轮修订，近 3 轮平均分从 3.2 到 3.2，无明显改善。\n考虑 major revision 或 pivot。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T20:26:04.662Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T20:26:04.662Z",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---

## Round 1

56 recorded events

### User

_source line 3 · 2026-05-27T20:26:04.705Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-27 (UTC).**

## Original idea
{
  "title": "FrontierCycle: Diagnostic-Guided Iterative RL↔Distillation Scheduling for Cross-Model LLM Reasoning Post-Training",
  "core_problem": "RLVR improves sampling efficiency (pass@1) but has limited capacity to expand the reasoning frontier (pass@k on hard problems) specifically in mathematical reasoning, while distillation from a stronger teacher expands the frontier but is bounded by teacher quality and incurs expensive teacher inference. MATH-Beyond (arXiv 2510.11653) quantifies this for mathematics: the best RL method achieves at most 21% frontier expansion, while distillation achieves 66% — though this gap is task-dependent, with ProRL (NeurIPS 2025) demonstrating RL achieves substantial frontier expansion on logic puzzles (+54.8%) and coding tasks. Current approaches to combining RL and distillation operate in two distinct regimes with fundamentally different cost structures:\n\nREGIME 1 — SELF-DISTILLATION (cheap teacher): The student model serves as its own teacher with privileged information (e.g., verified reasoning traces, answer visibility). Per-step teacher inference is essentially free since the teacher IS the student with different context. The May 2026 surge of unified single-phase methods — Rebellious Student/RLRT (arXiv 2605.10781), AntiSD (arXiv 2605.11609), CEPO (arXiv 2605.19436), SDAR (arXiv 2605.15155), Uni-OPD (arXiv 2605.03677) — alongside earlier unified methods (RLSD arXiv 2604.03128, CHORD arXiv 2508.11408, KDRL arXiv 2506.02208) all operate in this regime. These methods achieve RL-distillation synergy without phase switching because per-step teacher compute is negligible.\n\nREGIME 2 — CROSS-MODEL DISTILLATION (expensive teacher): A much larger external teacher (e.g., 235B MoE → 8B dense student) provides qualitatively different reasoning capabilities. Per-step teacher inference dominates training compute. This is the regime of DeepSeek-R1 distillation (671B→7B), Klear-Reasoner (DeepSeek-R1-0528→Qwen3-8B with 1.5M samples), and Beyond GRPO's sparse-to-dense pipeline. In this regime, invoking the teacher at every training step is prohibitively expensive, creating a genuine scheduling problem: WHEN to invoke the expensive teacher and for HOW LONG.\n\nWithin the cross-model regime, current scheduling approaches are limited: (1) fixed multi-stage pipelines (Beyond GRPO, SIRI) with predetermined sequencing regardless of student state; (2) single-transition diagnostic switching (Plasticity-Ceiling Framework, ACL 2026) addressing only the initial SFT→RL handoff; (3) static pre-RL prediction (Quagmires, arXiv 2510.01624) that uses pass@large-k to predict RL outcomes before training begins but not during it. The Plasticity-Ceiling Framework validates that diagnostic-guided switching substantially improves outcomes — sequential SFT-then-DAPOd achieves 78.1 on Qwen2.5-7B vs. 74.3 for pure DAPOd, and the projected ceiling reaches 84.0 when scaling to SFT889K (Pearson r=−0.92 between minimum validation loss and ceiling on Qwen2.5-7B; r=−0.96 on Llama3.2-3B). Notably, synchronized SFT-RL (LUFFY, 72.7) underperforms sequential switching (78.1), supporting phase separation over continuous mixing for cross-model settings. However, no existing work provides adaptive iterative multi-cycle RL↔distillation scheduling where each cycle's duration is dynamically determined by a diagnostic signal, specifically designed for the cross-model distillation regime where teacher compute amortization is the primary design constraint.",
  "opportunity": "The Plasticity-Ceiling Framework validates a powerful principle for the cross-model distillation regime: diagnostic-guided phase transitions substantially outperform both fixed schedules and synchronized training (78.1 for sequential SFT-then-DAPOd vs. 72.7 for synchronized LUFFY on Qwen2.5-7B). Quagmires in SFT-RL Post-Training independently validates that pass@large-k predicts RL outcomes (R² up to 0.88, a 2× improvement over SFT score prediction). Pass@k Training (arXiv 2508.10751) further validates pass@k as an active training signal — they use it as a per-step reward to balance exploration and exploitation during RLVR, achieving 17.9% vs. 12.9% Pass@1 on Enigmata for Qwen2.5-7B.\n\nWe propose extending these principles from single-transition or pre-training prediction to iterative multi-cycle RL↔distillation scheduling in the CROSS-MODEL DISTILLATION setting, addressing four limitations: (a) single-transition methods (Plasticity-Ceiling) cannot recover if the RL phase saturates prematurely; (b) fixed pipelines (Beyond GRPO) allocate predetermined compute fractions regardless of the student's actual learning state; (c) static prediction (Quagmires) cannot detect mid-training saturation; (d) unified per-step methods are designed for self-distillation where teacher compute is free — they do not address the scheduling problem inherent to expensive cross-model teachers.\n\nTHE CYCLING HYPOTHESIS: We hypothesize that in cross-model distillation, iterative RL↔distillation cycling provides compounding benefits because: (i) the external teacher (235B) provides qualitatively different reasoning capabilities than the student can discover through RL alone — unlike self-distillation where the teacher's knowledge is bounded by the student's own architecture; (ii) RL consolidation phases compress absorbed knowledge into pass@1 proficiency, creating capacity for absorbing new patterns in subsequent distillation phases; (iii) 'Why Self-Distillation Sometimes Degrades Reasoning' (arXiv 2603.24472) shows self-distillation degrades math reasoning by suppressing epistemic verbalization (up to 40% drops), suggesting that interleaving RL phases (which preserve exploration via entropy management) with distillation phases (which inject new knowledge) avoids this degradation mechanism. ReMiT (arXiv 2602.03075) provides preliminary evidence: their iterative mid-training ↔ RL cycling shows cascading improvements across two cycles (ReMiT → ReMiT2), validating that iterative cycling can compound rather than diminish. However, this hypothesis is explicitly testable and forms the go/no-go gate for the project: if the second RL phase after distillation does not expand pass@k beyond the first RL plateau, iterative cycling provides no value and the project pivots to optimizing single-cycle scheduling.\n\nSCOPE CLARIFICATION: FrontierCycle explicitly targets the cross-model distillation regime. For self-distillation settings where per-step teacher compute is free, unified methods (Rebellious Student, AntiSD, CEPO, RLSD, CHORD) are likely more efficient because they avoid the overhead of phase transition management. FrontierCycle's value proposition is specifically teacher compute amortization — invoking an expensive external teacher only when the student's frontier has genuinely stalled — which is only valuable when teacher inference is costly.",
  "landscape": "The Plasticity-Ceiling Framework (arXiv 2512.11470, ACL 2026) is the closest prior work to our concept of diagnostic-guided phase switching. It decomposes post-training performance into P_sft and PL_rl, identifies that minimum SFT validation loss predicts final ceiling (Pearson r=−0.92 on Qwen2.5-7B, r=−0.96 on Llama3.2-3B), and recommends switching to RL at the 'stable sub-phase' (validation loss ≤ 1.02 × L_min). On Qwen2.5-7B, sequential SFT-then-DAPOd achieves 78.1 vs. 74.3 for pure DAPOd; the projected ceiling reaches 84.0 on SFT889K at optimal switching. The synchronized SFT-RL paradigm (LUFFY) achieves only 72.7, empirically supporting phase separation. However, it supports only a single SFT→RL transition with no iterative cycling and its validation-loss criterion detects SFT overfitting, not RL frontier exhaustion.\n\nQuagmires in SFT-RL Post-Training (arXiv 2510.01624, NeurIPS 2025 MATH-AI Workshop) trains hundreds of models up to 12B and identifies pass@large-k (pass@64, pass@256) and generalization loss as strong proxies for predicting RL outcomes, improving R² by up to 0.5 (2×) over SFT score prediction. Their use is limited to static pre-RL prediction; FrontierCycle extends pass@k-derived metrics to dynamic real-time switching signals assessed repeatedly during training.\n\nPass@k Training (arXiv 2508.10751, ByteDance/RUC) uses pass@k directly as a per-step REWARD signal in RLVR to balance exploration and exploitation, deriving an analytical advantage function and achieving 17.9% Pass@1 on Enigmata vs. 12.9% for standard Pass@1 training on Qwen2.5-7B. This independently validates pass@k as a rich active signal for guiding training decisions. The key differentiation: Pass@k Training uses pass@k at per-step reward granularity to improve exploration within a single RL phase, while FrontierCycle uses pass@k-derived SEG at phase-level diagnostic granularity to determine when to switch between RL and distillation phases. Both elevate pass@k from a passive evaluation metric to an active signal, but at different granularities serving different purposes — they are complementary rather than competing.\n\nMAY 2026 UNIFIED METHODS SURGE — SELF-DISTILLATION REGIME: At least 6 new unified single-phase RL+distillation methods appeared in May 2026, almost all operating in the SELF-DISTILLATION regime where per-step teacher compute is free: Rebellious Student/RLRT (arXiv 2605.10781) reverses teacher signals on correct rollouts, improving over GRPO by 8.9% average across Qwen3-4B/8B; AntiSD (arXiv 2605.11609) ascends student-teacher divergence via PMI analysis, improving final accuracy by up to 11.5 points; CEPO (arXiv 2605.19436) uses contrastive evidence from correct vs. wrong rollouts for token-level credit assignment; SDAR (arXiv 2605.15155) gates self-distillation signals for agentic RL (+9.4% on ALFWorld); Uni-OPD (arXiv 2605.03677) unifies on-policy distillation with dual-perspective optimization across 16 benchmarks. dGRPO (arXiv 2605.12227) combines GRPO with on-policy distillation in a unified objective for long-context reasoning, targeting the 8K-32K token regime where sparse rewards are particularly unstable. These methods collectively demonstrate that unified objectives excel when teacher inference is cheap (self-distillation). FrontierCycle does not compete with these methods in their target regime; instead, it addresses the complementary cross-model regime where an expensive external teacher (235B MoE) makes per-step inference prohibitive.\n\nSelf-Distilled RLVR (RLSD, arXiv 2604.03128, Apr 2026) uses environment rewards for update direction and self-distillation for magnitude modulation, achieving +2.32% over GRPO on multimodal reasoning. RLAD (arXiv 2602.22495, Feb 2026) integrates KD into RL via Trust Region Ratio Distillation. ATESD (arXiv 2605.11458, May 2026) proposes a Beta-policy meta-controller for within-distillation teacher exposure control, orthogonal to FrontierCycle's inter-phase scheduling.\n\nBeyond GRPO (arXiv 2605.12483, May 2026) proposes a fixed 3-stage sparse-to-dense reward pipeline, achieving 79.3% MATH and 25.2% AIME 2024 on Qwen3-1.7B. This is FrontierCycle's CENTRAL fixed-pipeline baseline in the cross-model regime: it demonstrates that well-designed single-pass sequencing captures substantial RL-distillation benefits. Our iterative cycling must demonstrably outperform this.\n\nReMiT (arXiv 2602.03075, Feb 2026) provides the closest evidence for iterative cycling: their RL-guided mid-training framework shows cascading improvements across two cycles (ReMiT → ReMiT2), with the second cycle outperforming the first. While ReMiT operates at the pre-training ↔ post-training boundary rather than RL ↔ distillation, it validates the principle that iterative cycling can compound rather than diminish.\n\n'Why Self-Distillation Sometimes Degrades Reasoning' (arXiv 2603.24472, Mar 2026) shows that self-distillation suppresses epistemic verbalization in math reasoning, causing up to 40% performance drops on OOD problems. This motivates FrontierCycle's interleaving approach: RL phases preserve exploration (entropy management via Entrocraft), while distillation phases from an external teacher inject genuinely new reasoning patterns without suppressing the student's uncertainty expression, because the teacher's knowledge is architecturally distinct rather than a privileged version of the student's own knowledge.\n\nKlear-Reasoner-8B (arXiv 2508.07629) achieves 90.5% on AIME 2024 (64K inference budget; 83.2% at 32K) with a simple SFT+GPPO pipeline from Qwen3-8B-Base using 1.5M DeepSeek-R1-0528 distillation samples. This sets a high bar for 8B-scale performance and contextualizes the overhead any adaptive method must justify.\n\nCoPD (arXiv 2604.27083, Apr 2026) achieves RL-distillation interleaving through parallel multi-expert co-evolution. CoDistill-GRPO (arXiv 2605.08873) simultaneously trains large and small models through bidirectional GRPO rewards. CHORD (arXiv 2508.11408, ICLR 2026) dynamically weights SFT within on-policy RL via token-wise uncertainty. SRFT (arXiv 2506.19767) validates entropy as a diagnostic. HPT (arXiv 2509.04419) provides per-question binary switching. Entrocraft (arXiv 2604.26326) achieves ~17% improvement in pass@32 over GRPO through entropy curve control. EOPD (arXiv 2603.07079) augments reverse KL with forward KL at high teacher-entropy tokens. MATH-Beyond (arXiv 2510.11653) quantifies the RL/distillation frontier gap. ProRL (NeurIPS 2025, arXiv 2505.24864) shows RL achieves +54.8% on logic puzzles but diminished frontier on math. Yu (arXiv 2511.16231) proves pass@k gap collapse under policy concentration.",
  "inspired_by": "field_gap['cross-model distillation scheduling: expensive teacher amortization via iterative cycling'] + validated_principle[Plasticity-Ceiling Framework: sequential 78.1 vs. synchronized 72.7 on Qwen2.5-7B] + supporting_evidence[Quagmires: pass@large-k predicts RL outcomes R² up to 0.88] + complementary_validation[Pass@k Training: pass@k as active reward signal at per-step granularity] + cycling_evidence[ReMiT: cascading improvements across two cycles ReMiT → ReMiT2] + degradation_insight[Self-distillation degrades math reasoning (2603.24472) → cross-model avoids this via architecturally distinct teacher] + regime_clarification[May 2026 unified methods surge targets self-distillation; FrontierCycle targets cross-model distillation] + mathematical_foundation[Yu's pass@k gap collapse + Entrocraft's entropy-advantage relationship] + design_principle[ZClip's z-score adaptive thresholds]",
  "approach": "We propose FrontierCycle, an iterative multi-cycle RL↔distillation scheduling framework with diagnostic-guided phase transitions for LLM reasoning post-training, specifically designed for the CROSS-MODEL DISTILLATION REGIME where per-step teacher inference is expensive. The CORE CONTRIBUTION is the cycling framework architecture — a general mechanism for adaptive multi-cycle scheduling where each phase's duration is dynamically determined by a diagnostic signal — rather than any specific diagnostic metric.\n\nThe framework has three components: (1) a DIAGNOSTIC MODULE evaluating candidate switching metrics on a held-out validation set every 100 training steps, (2) a SWITCHING CONTROLLER determining phase transitions using z-score-normalized thresholds, and (3) PHASE-SPECIFIC OPTIMIZERS applying the best available within-phase method (Entrocraft-style entropy annealing during RL, EOPD-style entropy-aware KL during distillation, with ATESD-compatible teacher exposure control composable during distillation phases).\n\nWHY DISCRETE PHASE SWITCHING IN THE CROSS-MODEL REGIME: FrontierCycle's design is motivated by the cost structure of cross-model distillation. When the teacher is Qwen3-235B-A22B and the student is 8B dense, each teacher forward pass costs ~3× the student (22B active parameters vs. 8B). Over a full training run of ~10K steps with multiple rollouts per step, per-step teacher inference adds ~300% compute overhead. FrontierCycle invokes the teacher only during distillation phases (estimated 30-40% of total training time), reducing teacher overhead to ~100-120%. For self-distillation settings, where teacher overhead is negligible, unified methods (Rebellious Student, AntiSD, CEPO, RLSD) are likely more efficient — FrontierCycle does not claim superiority there. The Plasticity-Ceiling paper's finding that sequential SFT-then-DAPOd (78.1) outperforms synchronized LUFFY (72.7) further supports phase separation in cross-model settings. Additionally, discrete phases enable specialized optimization: Entrocraft entropy annealing during RL requires different hyperparameters than EOPD entropy-aware KL during distillation.\n\nDIAGNOSTIC SIGNAL INVESTIGATION (Stage 0): We treat the diagnostic signal choice as an empirical question. We compare four candidate signals: (a) SEG = pass@k − pass@1 — building on both Quagmires (pass@k predicts RL outcomes) and Pass@k Training (pass@k as active signal at per-step reward granularity; we use it at phase-level diagnostic granularity); (b) EN-SEG = SEG / max(H(π), ε_H) — entropy-normalized for cross-phase comparability; (c) adapted Plasticity-Ceiling validation loss — extending their criterion to RL-phase saturation detection; (d) pass@k growth rate — direct frontier expansion velocity.\n\nCYCLING VALIDATION GATE (Stage 0.5 — NEW): Before committing to full iterative cycling experiments, we validate the cycling hypothesis with a minimal single-cycle test. Starting from DeepSeek-R1-0528-Qwen3-8B, we: (i) run RL (GRPO+Entrocraft) until the diagnostic indicates frontier exhaustion (pass@k plateaus); (ii) record the plateau pass@k value P1; (iii) run cross-model distillation from Qwen3-235B-A22B until the diagnostic indicates absorption saturation; (iv) run a second RL phase and measure whether pass@k exceeds P1. GO/NO-GO DECISION: If the second RL phase achieves pass@k > P1 + ε (where ε = 1 percentage point on MATH-500), iterative cycling has demonstrated frontier expansion value and we proceed to Stage 1. If pass@k ≤ P1 + ε, iterative cycling provides no benefit over single-pass scheduling, and we PIVOT to optimizing single-cycle scheduling (determining the optimal RL/distillation budget allocation within one cycle, effectively improving Beyond GRPO with diagnostic-guided switching instead of fixed stages). This go/no-go gate ensures the project produces a meaningful contribution regardless of the cycling hypothesis outcome.\n\nWHY CROSS-MODEL CYCLING MAY AVOID DIMINISHING RETURNS: 'Why Self-Distillation Sometimes Degrades Reasoning' (arXiv 2603.24472) identifies the mechanism: self-distillation suppresses epistemic verbalization (uncertainty tokens like 'Wait', 'Let me reconsider') because the teacher's privileged information eliminates uncertainty. In cross-model distillation, the teacher (235B MoE) has architecturally distinct reasoning patterns — it doesn't simply have privileged information about the student's answer, it has genuinely different reasoning strategies developed through its larger capacity. The RL phases preserve exploration and uncertainty expression (via entropy management), while distillation phases inject new patterns without the same suppression mechanism. ReMiT's cascading improvements across two cycles (ReMiT → ReMiT2) provide preliminary evidence that iterative cycling can compound in related settings.\n\nEXPERIMENTAL PLAN: STAGE 0 — DIAGNOSTIC SIGNAL COMPARISON (2 weeks): Run 2000-step RL and 2000-step distillation, logging all candidate diagnostics. Compare on signal-to-noise ratio and switching stability. STAGE 0.5 — CYCLING VALIDATION GATE (2 weeks): Single-cycle test (RL→distillation→RL) measuring whether pass@k exceeds the first RL plateau. GO/NO-GO decision. STAGE 1 — ITERATIVE CYCLING (if go) OR SINGLE-CYCLE OPTIMIZATION (if no-go) (5-7 weeks): If cycling validated: run 3-5 cycles, monitoring diagnostic every 100 steps on compact diagnostic set (200 problems, pass@32). If cycling invalidated: optimize single-cycle budget allocation with diagnostic-guided switching.\n\nCORE BASELINES (6): (1) Beyond GRPO fixed pipeline — CENTRAL comparison; (2) Plasticity-Ceiling-guided single SFT→RL transition; (3) CHORD continuous mixing (cross-model teacher); (4) RLSD unified self-distillation+RL (self-distillation regime for comparison); (5) Entrocraft-only RL (no distillation); (6) Pure distillation. KEY ABLATIONS (5): (1) Diagnostic signal comparison within FrontierCycle; (2) Adaptive cycling vs. fixed-interval cycling; (3) z-score relative thresholds vs. absolute thresholds (threshold transfer from MATH to AIME/LiveCodeBench); (4) Number of cycles: 1 vs. 3 vs. 5; (5) Teacher compute analysis: H100-hours for FrontierCycle vs. CHORD vs. Beyond GRPO. Evaluate on AIME 2024, MATH-500, and LiveCodeBench, reporting pass@1, pass@32, per-difficulty breakdowns, teacher compute (H100-hours), and threshold transfer success rates.\n\nPositioning relative to Klear-Reasoner-8B: we target the moderate-data regime — if FrontierCycle at 32K matches or exceeds Klear-Reasoner's 32K performance (83.2%) with fewer teacher demonstrations, that demonstrates intelligent scheduling as an alternative to brute-force data scaling.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "2800-3600 H100-hours: teacher inference (~400), RL training (~400), pass@32 evaluation (~40), Stage 0 diagnostics (~100), Stage 0.5 cycling validation (~150), baselines (~700), ablations (~500), buffer (~510)",
      "timeline": "15-18 weeks (2 weeks Stage 0, 2 weeks Stage 0.5 + go/no-go, 3 weeks implementation, 5-7 weeks experiments, 3-4 weeks writing)",
      "estimated_gpu_cost": "$5,600-7,200 at $2/H100-hr"
    },
    "human_in_loop": {
      "gpu_hours": "2200-2800 H100-hours (Claude assists with veRL integration, Stage 0.5 automated analysis, early stopping)",
      "timeline": "12-15 weeks (1.5 weeks Stage 0, 1.5 weeks Stage 0.5, 2.5 weeks implementation, 4-6 weeks experiments, 2-3 weeks writing)",
      "claude_api_cost": "$400-600",
      "estimated_gpu_cost": "$4,400-5,600 at $2/H100-hr"
    },
    "auto_research": {
      "gpu_hours": "1800-2300 H100-hours (automated scheduling, adaptive sweep, Stage 0.5 as automated go/no-go gate)",
      "timeline": "9-12 weeks (1 week Stage 0, 1 week Stage 0.5 + automated pivot decision, 2 weeks implementation, 4-6 weeks automated runs, 1-2 weeks paper generation)",
      "claude_api_cost": "$700-1000",
      "estimated_gpu_cost": "$3,600-4,600 at $2/H100-hr",
      "speed_bottleneck": "Teacher inference from Qwen3-235B-A22B requires 4×H100 per batch; pass@32 evaluation on compact 200-problem set takes ~15 min per checkpoint on 1×H100"
    }
  },
  "target_venues": [
    "ICLR 2027 (submission deadline: Sep 24, 2026)",
    "ARR October 2026 cycle (submission: Oct 12, 2026) for commitment to EACL 2027 or NAACL 2027"
  ],
  "level": "solid",
  "key_references": [
    "Rethinking Expert Trajectory Utilization in LLM Post-training for Mathematical Reasoning — Plasticity-Ceiling Framework (arXiv 2512.11470, ACL 2026)",
    "Quagmires in SFT-RL Post-Training: When High SFT Scores Mislead and What to Use Instead (arXiv 2510.01624, NeurIPS 2025 MATH-AI Workshop)",
    "Pass@k Training for Adaptively Balancing Exploration and Exploitation of Large Reasoning Models (arXiv 2508.10751, ByteDance/RUC)",
    "Combining On-Policy Optimization and Distillation for Long-Context Reasoning in Large Language Models — dGRPO (arXiv 2605.12227, May 2026)",
    "Rebellious Student: Reversing Teacher Signals for Reasoning Exploration with Self-Distilled RLVR — RLRT (arXiv 2605.10781, May 2026)",
    "Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information — AntiSD (arXiv 2605.11609, May 2026)",
    "CEPO: RLVR Self-Distillation using Contrastive Evidence Policy Optimization (arXiv 2605.19436, May 2026)",
    "Self-Distilled Agentic Reinforcement Learning — SDAR (arXiv 2605.15155, May 2026)",
    "Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe (arXiv 2605.03677, May 2026)",
    "ReMiT: RL-Guided Mid-Training for Iterative LLM Evolution (arXiv 2602.03075, Feb 2026)",
    "Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs? (arXiv 2603.24472, Mar 2026)",
    "Self-Distilled RLVR — RLSD (arXiv 2604.03128, Apr 2026)",
    "Reinforcement-aware Knowledge Distillation for LLM Reasoning — RLAD (arXiv 2602.22495, Feb 2026)",
    "Adaptive Teacher Exposure for Self-Distillation in LLM Reasoning — ATESD (arXiv 2605.11458, May 2026)",
    "Co-Evolving Policy Distillation — CoPD (arXiv 2604.27083, Apr 2026)",
    "Klear-Reasoner: Advancing Reasoning Capability via Gradient-Preserving Clipping Policy Optimization (arXiv 2508.07629, 2025)",
    "CoDistill-GRPO: A Co-Distillation Recipe for Efficient Group Relative Policy Optimization (arXiv 2605.08873, May 2026)",
    "Reinforcement Learning vs. Distillation: Understanding Accuracy and Capability in LLM Reasoning (arXiv 2505.14216, 2025)",
    "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? (arXiv 2504.13837, 2025)",
    "MATH-Beyond: A Benchmark for RL to Expand Beyond the Base Model (arXiv 2510.11653, 2025)",
    "ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models (NeurIPS 2025, arXiv 2505.24864)",
    "Beyond GRPO and On-Policy Distillation: An Empirical Sparse-to-Dense Reward Principle for Language-Model Post-Training (arXiv 2605.12483, May 2026)",
    "HPT: Towards a Unified View of Large Language Model Post-Training (arXiv 2509.04419, 2025)",
    "CHORD: Controllable Harmonization of On- and Off-Policy RL via Dynamic Weighting (arXiv 2508.11408, ICLR 2026)",
    "SRFT: A Single-Stage Method with Supervised and Reinforcement Fine-Tuning for Reasoning (arXiv 2506.19767, 2025)",
    "Entrocraft: Addressing Performance Saturation for LLM RL via Precise Entropy Curve Control (arXiv 2604.26326, 2026)",
    "EOPD: Entropy-Aware On-Policy Distillation of Language Models (arXiv 2603.07079, 2026)",
    "Pass@k Metric for RLVR: A Diagnostic Tool of Exploration, But Not an Objective (arXiv 2511.16231, 2025)",
    "The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models (arXiv 2505.22617, 2025)",
    "EntroPIC: Towards Stable Long-Term Training of LLMs via Entropy Stabilization with PI Control (arXiv 2511.15248, 2025)",
    "Beyond Pass@k: Breadth-Depth Metrics for LLM Reasoning — Cover@tau (arXiv 2510.08325, 2025)",
    "KDRL: Post-Training Reasoning LLMs via Unified Knowledge Distillation and Reinforcement Learning (arXiv 2506.02208, 2025)",
    "JustRL: Scaling a 1.5B LLM with a Simple RL Recipe (arXiv 2512.16649, ICLR 2026 Blogpost)",
    "ZClip: Adaptive Spike Mitigation for LLM Pre-Training (arXiv 2504.02507, 2025)"
  ],
  "description": "FrontierCycle addresses a fundamental scheduling problem in cross-model LLM reasoning post-training: when to invoke an expensive external teacher (e.g., 235B MoE) and for how long, given that per-step teacher inference dominates training compute. We distinguish two regimes: self-distillation, where unified per-step methods (Rebellious Student, AntiSD, CEPO, RLSD) excel because the teacher IS the student with negligible overhead, and cross-model distillation, where teacher inference adds ~300% per-step overhead, creating a genuine scheduling problem. FrontierCycle targets exclusively the cross-model regime — the setting of DeepSeek-R1 distillation, Klear-Reasoner, and Beyond GRPO. The framework proposes iterative multi-cycle RL↔distillation scheduling where each phase's duration is dynamically determined by a diagnostic signal evaluated every 100 training steps. We investigate four candidate diagnostics, including SEG (pass@k minus pass@1) building on both Quagmires' validation of pass@k as an RL outcome predictor and Pass@k Training's use of pass@k as an active per-step reward signal. A z-score-normalized switching controller triggers phase transitions when frontier expansion stalls. Critically, we introduce a cycling validation gate (Stage 0.5): before committing to iterative cycling, we test whether a second RL phase after distillation expands pass@k beyond the first RL plateau. If validated, we proceed to multi-cycle experiments; if falsified, we pivot to optimizing single-cycle scheduling with diagnostic-guided switching — ensuring a meaningful contribution regardless. The cycling hypothesis is motivated by evidence that cross-model distillation avoids the epistemic verbalization suppression that degrades self-distillation (arXiv 2603.24472), and by ReMiT's demonstration of cascading improvements across iterative cycles. Phase-specific optimizers apply Entrocraft-style entropy annealing during RL and EOPD-style entropy-aware KL during distillation, with teacher inference restricted to distillation phases (estimated 30-40% of training), reducing overhead to ~100-120%. We evaluate against Beyond GRPO as the central fixed-pipeline baseline, with six core baselines and five ablations across AIME 2024, MATH-500, and LiveCodeBench.",
  "project_name": "frontier_cycle",
  "source": "web_research",
  "reviewer_response": {
    "issue_1_factual_error_plasticity_ceiling": "FIXED. All Plasticity-Ceiling numbers corrected against the paper (arXiv 2512.11470v2 HTML verified). Previous claim of '85.7 ceiling' replaced with the correct values: 78.1 (actual SFT-then-DAPOd execution on Qwen2.5-7B), 84.0 (projected ceiling at SFT889K with optimal switching timing), and 74.3 (pure DAPOd). Pearson correlation corrected from r=−0.90 to r=−0.92 for Qwen2.5-7B and r=−0.96 for Llama3.2-3B. The synchronized baseline LUFFY (72.7) is now included to strengthen the argument for phase separation over continuous mixing. All numbers verified against the v2 HTML rendering of the paper.",
    "issue_2_quagmires_citation": "FIXED. Quagmires in SFT-RL Post-Training (arXiv 2510.01624, NeurIPS 2025 MATH-AI Workshop) integrated as supporting evidence throughout. Their key finding: pass@64/pass@256 and generalization loss predict RL outcomes with R² up to 0.88 (2× improvement over SFT score prediction), trained on hundreds of models up to 12B. Clear differentiation: Quagmires uses pass@k as a STATIC one-shot predictor assessed BEFORE RL training begins (predicting which SFT checkpoint yields best RL outcome), while FrontierCycle extends pass@k-derived metrics to DYNAMIC real-time switching signals assessed repeatedly DURING training to trigger phase transitions. Quagmires validates the general principle that pass@k captures RL potential better than pass@1/SFT scores; FrontierCycle operationalizes this principle for iterative scheduling.",
    "issue_3_enseg_reframing": "FIXED via MAJOR REFRAMING. The core contribution is now explicitly the ITERATIVE CYCLING FRAMEWORK with diagnostic-guided phase transitions, NOT EN-SEG specifically. Title changed to center the framework, not the metric. EN-SEG is repositioned as one of four candidate diagnostics investigated empirically in Stage 0, alongside raw SEG, validation loss adaptation, and pass@k growth rate. The description and approach now consistently frame the diagnostic choice as 'an empirical question resolved through systematic comparison' rather than claiming EN-SEG as the contribution.",
    "issue_4_unified_competitors": "FIXED. Self-Distilled RLVR (RLSD, arXiv 2604.03128) integrated as a core baseline (#4) and extensively discussed in the landscape. RLAD (arXiv 2602.22495) also added. The argument for discrete phase switching over unified objectives is strengthened with three specific points: (1) TEACHER COMPUTE AMORTIZATION, (2) EMPIRICAL EVIDENCE from Plasticity-Ceiling, (3) PHASE-SPECIFIC OPTIMIZATION.",
    "issue_5_venue_correction": "FIXED. ARR July 2026 (July 15) removed — only ~7 weeks remain, insufficient for any timeline. Replaced with ARR October 2026 (submission: Oct 12, 2026) for commitment to EACL 2027 or NAACL 2027 (~20 weeks from now). ICLR 2027 (submission: Sep 24, 2026, ~17 weeks) retained as primary target. Both are feasible under human_in_loop (12-15 weeks) and auto_research (9-12 weeks) timelines.",
    "issue_6_passk_training_citation": "FIXED. Pass@k Training (arXiv 2508.10751) integrated into landscape and approach. Clear differentiation established: Pass@k Training uses pass@k at PER-STEP REWARD granularity to improve exploration within a single RL phase (analytical advantage function, 17.9% vs. 12.9% on Enigmata for Qwen2.5-7B); FrontierCycle uses pass@k-derived SEG at PHASE-LEVEL DIAGNOSTIC granularity to determine when to switch between RL and distillation phases. Both elevate pass@k from a passive evaluation metric to an active training signal, but at different granularities serving complementary purposes — they strengthen each other's argument that pass@k is a rich signal.",
    "issue_7_dgrpo_citation": "FIXED. dGRPO (arXiv 2605.12227) added to the unified-competitor list in the landscape section alongside RLSD/RLAD. dGRPO combines GRPO with on-policy distillation in a unified objective targeting long-context reasoning (8K-32K tokens). Positioned as part of the broader unified methods landscape.",
    "issue_8_unified_methods_headwind": "FIXED via MAJOR REFRAMING. The entire proposal is now structured around a two-regime taxonomy: SELF-DISTILLATION (cheap teacher, unified methods dominate) vs. CROSS-MODEL DISTILLATION (expensive teacher, phase scheduling matters). The May 2026 surge of unified methods (Rebellious Student/RLRT, AntiSD, CEPO, SDAR, Uni-OPD) is explicitly analyzed — almost all operate in the self-distillation regime where per-step teacher compute is free. FrontierCycle is explicitly scoped to the cross-model distillation regime (235B MoE → 8B dense) where per-step teacher inference adds ~300% compute overhead. This is stated as a scope clarification, not a limitation — cross-model distillation is the regime of DeepSeek-R1 distillation, Klear-Reasoner, and Beyond GRPO, which are among the most impactful recent results. For self-distillation settings, we explicitly acknowledge that unified methods are likely more efficient. The approach section quantifies teacher compute savings (300% per-step overhead reduced to 100-120% via phase amortization).",
    "issue_9_iterative_cycling_extrapolation": "FIXED via STAGE 0.5 GO/NO-GO GATE and THEORETICAL ARGUMENT. (1) Stage 0.5 added as a cycling validation gate: after one full RL→distillation→RL cycle, we measure whether the student's pass@k frontier exceeds the first RL plateau (P1). If pass@k > P1 + ε (ε = 1pp on MATH-500), cycling is validated; if not, the project PIVOTS to single-cycle optimization, ensuring a meaningful contribution regardless. (2) Theoretical argument for why cross-model cycling avoids diminishing returns: 'Why Self-Distillation Sometimes Degrades Reasoning' (arXiv 2603.24472) shows self-distillation degrades math reasoning via epistemic verbalization suppression — cross-model distillation from a 235B MoE provides architecturally distinct reasoning, not just privileged information, so this degradation mechanism should not apply. (3) ReMiT (arXiv 2602.03075) provides empirical evidence: iterative mid-training ↔ RL cycling shows cascading improvements across two cycles (ReMiT → ReMiT2). The cycling hypothesis is now explicitly stated as TESTABLE with clear falsification criteria."
  }
}

## Reviewer feedback (round 7)
Issues: ["TOPIC MISMATCH WITH USER REQUIREMENTS: The user asked for 'Synthetic Data and Self-Improvement for Mathematical Reasoning Training.' FrontierCycle is about cross-model distillation scheduling from an external 235B teacher — this is fundamentally NOT self-improvement. Self-improvement means the model improves using its own capabilities (self-play, STaR, self-training, RLVR). Cross-model distillation (DeepSeek-R1-0528→Qwen3-8B, Qwen3-235B→8B) is teacher-guided training, the opposite paradigm. The idea addresses a valid research question but does not match the user's stated topic.", "SIRI (arXiv 2509.25176) MISCHARACTERIZED: The idea labels SIRI as a 'fixed multi-stage pipeline' alongside Beyond GRPO, but SIRI actually performs 3 iterations of compression↔expansion cycling during RL, achieving 43.2% improvement on AIME24 with 46.9% token reduction. While SIRI cycles within RL (rollout length control) rather than between RL and distillation, it IS an iterative cycling method for math reasoning and should be properly characterized and differentiated as the closest existing iterative cycling approach.", "MISSING RELEVANT WORK — CLPD (arXiv 2605.11260, May 2026): Curriculum Learning-Guided Progressive Distillation explicitly addresses teacher scheduling by progressively scheduling teachers of increasing capacity — directly relevant to the cross-model distillation scheduling problem FrontierCycle targets.", "MISSING RELEVANT WORK — 'Large Language Model Post-Training: A Unified View' (arXiv 2604.07941, Apr 2026): This 38-page paper directly discusses multi-stage pipeline composition, behavioral consolidation roles, and argues that 'progress increasingly depends on coordinated systems design.' It provides theoretical grounding for FrontierCycle's stage-composition approach and should be cited.", "MISSING RELEVANT WORK — PRISM (arXiv 2604.28123, Apr 2026): Inserts an explicit distribution-alignment stage between SFT and RL to mitigate distributional drift — relevant as another diagnostic-guided multi-stage approach to post-training pipeline design.", "FIELD MOMENTUM CREATES EXISTENTIAL RISK: The May 2026 unified methods surge now includes not just the 6+ per-step methods cited, but also theoretical unification work: 'Decoupling KL and Trajectories' (2605.16826) and 'Post-Training is About States, Not Tokens' (2605.22731) both provide theoretical frameworks showing SFT, RL, and OPD are points in a continuous design space. This theoretical momentum toward continuous-space optimization further undercuts the case for discrete phase switching."]
Feedback: 1) ADDRESS TOPIC MISMATCH: The user requested 'Synthetic Data and Self-Improvement for Mathematical Reasoning Training.' Either (a) pivot the idea to genuinely address self-improvement — e.g., iterative RL↔self-generated-data cycling where the model generates its own training data (no external teacher), or (b) explicitly acknowledge the mismatch and reframe around how cross-model distillation data IS synthetic data and the RL phases constitute self-improvement phases within the cycle. Option (a) is stronger — self-improvement with iterative cycling is a natural fit for the user's topic and avoids the expensive-teacher-compute problem entirely. 2) FIX SIRI CHARACTERIZATION: SIRI performs 3 iterations of compression↔expansion cycling, not fixed sequencing. Properly differentiate: SIRI cycles within RL (rollout length), FrontierCycle cycles between RL and distillation (training objective). Acknowledge SIRI as the closest existing iterative cycling method for math reasoning. 3) ADD MISSING CITATIONS: Include CLPD (2605.11260), the Unified View paper (2604.07941), and consider PRISM (2604.28123) — all directly relevant to multi-stage pipeline design and teacher scheduling. 4) STRENGTHEN IMPACT ARGUMENT: The cross-model distillation niche is real but shrinking as the field converges on self-distillation. Either (a) expand scope to include self-distillation cycling, or (b) argue more forcefully why cross-model distillation will remain important (citing DeepSeek-R1, Klear-Reasoner as landmark results that required cross-model distillation).

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.
- Address each issue specifically.

## 深度调研要求

不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。
2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。
3. **深度思考**：
   - 核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach？
4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。

## 针对 Review 意见的定向搜索

1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点
2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline
3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现
4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot

- You have full freedom: minor fix, major revision, or pivot.
- Include a "change_type" field: "minor", "major", or "pivot".
- Output a COMPLETE JSON object with ALL fields.

## 停滞提醒
经过 7 轮修订，近 3 轮平均分从 3.2 到 3.2，无明显改善。
考虑 major revision 或 pivot。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a6903394-624e-4492-ad19-36a9e5620d23",
  "type": "user",
  "uuid": "a4e3178d-e475-434b-8bcc-b5b5ebc5233e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T20:26:04.704Z_

```json
{
  "parentUuid": "a4e3178d-e475-434b-8bcc-b5b5ebc5233e",
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
  "uuid": "d07700d3-70a4-4d8c-9fdc-44cc43b39333",
  "timestamp": "2026-05-27T20:26:04.704Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T20:26:04.704Z_

```json
{
  "parentUuid": "d07700d3-70a4-4d8c-9fdc-44cc43b39333",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4a48a9fd-28a4-41ab-a3c6-5920ded88711",
  "timestamp": "2026-05-27T20:26:04.704Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"FrontierCycle: Diagnostic-Guided Iterative RL↔Distillation Scheduling…",
  "leafUuid": "4a48a9fd-28a4-41ab-a3c6-5920ded88711",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise self-improvement framework for iterative LLM reasoning cycles",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---

### Assistant

_source line 8 · 2026-05-27T20:26:16.204Z_

<details><summary>Logged reasoning block</summary>

```text
The reviewer feedback is quite significant this round. Let me analyze the key issues:

1. **TOPIC MISMATCH**: The user asked for "Synthetic Data and Self-Improvement for Mathematical Reasoning Training" but FrontierCycle is about cross-model distillation scheduling from an expensive external teacher. This is a fundamental mismatch. The reviewer suggests pivoting to self-improvement (option a) which is stronger.

2. **SIRI mischaracterization**: Need to properly characterize SIRI as an iterative cycling method.


3. **Missing citations**: CLPD, Unified View paper, PRISM.
4. **Field momentum toward unified/continuous methods**: Theoretical work undermining discrete phase switching.
5. **Score stagnation**: 7 rounds with no improvement, suggesting a pivot is needed.

Given the stagnation and the fundamental topic mismatch, I think a pivot is the right call. The field is moving toward unified and continuous approaches rather than discrete phase switching, and I should reframe this around iterative self-improvement cycling where the model generates its own synthetic training data through RL exploration, then uses that data for self-training in a loop—this directly addresses the user's topic while aligning with current momentum.

Now I'm researching the landscape for self-improvement in mathematical reasoning to build out a stronger proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a48a9fd-28a4-41ab-a3c6-5920ded88711",
  "isSidechain": false,
  "requestId": "req_011CbThecbuukCM8KvxFbVTL",
  "type": "assistant",
  "uuid": "ff8513b7-a612-43f2-bcb8-714cd7b3a8ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175CLR8T8H7kaEcgR8REQzp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13245,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1751,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13245,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1751,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13245
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

_source line 9 · 2026-05-27T20:26:17.408Z_

I need to carefully analyze the reviewer feedback. The most critical issue is the **topic mismatch** — the user asked for "Synthetic Data and Self-Improvement for Mathematical Reasoning Training" but FrontierCycle is fundamentally about cross-model distillation scheduling. After 7 rounds of stagnation, a pivot is warranted. Let me research the self-improvement landscape thoroughly before designing the new proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff8513b7-a612-43f2-bcb8-714cd7b3a8ec",
  "isSidechain": false,
  "requestId": "req_011CbThecbuukCM8KvxFbVTL",
  "type": "assistant",
  "uuid": "a94a7fa3-bb9d-4a48-a5b2-714208442efb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175CLR8T8H7kaEcgR8REQzp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13245,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1751,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13245,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1751,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13245
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

_source line 10 · 2026-05-27T20:26:25.014Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JBPRGgTeALppA8ePmq6tVM`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research self-improvement math reasoning",
  "prompt": "I'm pivoting a research proposal to focus on \"Synthetic Data and Self-Improvement for Mathematical Reasoning Training.\" I need to understand the current landscape of self-improvement methods (where the model improves using its own capabilities, NOT from an external teacher).\n\nPlease search the web thoroughly for:\n\n1. STaR (Self-Taught Reasoner) and its variants — especially recent 2025-2026 extensions\n2. ReST (Reinforced Self-Training) and REST-EM for math reasoning\n3. Self-play methods for LLM reasoning improvement\n4. Iterative self-training / self-improvement loops for math\n5. Synthetic data generation by the model itself for math training\n6. Any 2025-2026 papers on \"self-improvement\" + \"mathematical reasoning\"\n7. Papers on when/why self-improvement works vs. fails (collapse, mode collapse, etc.)\n8. \"Scalable Oversight\" or \"Weak-to-Strong\" approaches for self-improvement\n\nSearch queries to try:\n- \"self-improvement mathematical reasoning LLM 2025 2026\"\n- \"STaR self-taught reasoner iterative self-training math\"  \n- \"synthetic data self-generated math reasoning training\"\n- \"self-play LLM reasoning improvement\"\n- \"iterative self-training collapse LLM reasoning\"\n\nFor each major paper found, provide: title, arxiv ID, date, key findings, and how it relates to self-improvement for math reasoning. I need at least 15-20 relevant papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a94a7fa3-bb9d-4a48-a5b2-714208442efb",
  "isSidechain": false,
  "requestId": "req_011CbThecbuukCM8KvxFbVTL",
  "type": "assistant",
  "uuid": "9dae3930-abfd-48dc-99fd-16828545c9d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175CLR8T8H7kaEcgR8REQzp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13245,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1751,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13245,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1751,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13245
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

_source line 11 · 2026-05-27T20:26:31.174Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KpAaBfA3XdwRSCN71m7rST`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research SIRI and missing citations",
  "prompt": "I need to research several specific papers that were flagged in a review. Please search the web and fetch details on each:\n\n1. **SIRI (arXiv 2509.25176)**: A paper about iterative compression↔expansion cycling during RL for math reasoning. I need to understand: what exactly does it do? How does it achieve 43.2% improvement on AIME24? What is the compression/expansion cycling mechanism? How many iterations?\n\n2. **CLPD (arXiv 2605.11260, May 2026)**: Curriculum Learning-Guided Progressive Distillation — about progressively scheduling teachers of increasing capacity.\n\n3. **\"Large Language Model Post-Training: A Unified View\" (arXiv 2604.07941, Apr 2026)**: A 38-page survey about multi-stage pipeline composition and coordinated systems design.\n\n4. **PRISM (arXiv 2604.28123, Apr 2026)**: About inserting distribution-alignment stages between SFT and RL.\n\n5. **\"Decoupling KL and Trajectories\" (arXiv 2605.16826)**: Theoretical framework showing SFT/RL/OPD are points in continuous design space.\n\n6. **\"Post-Training is About States, Not Tokens\" (arXiv 2605.22731)**: Another theoretical unification paper.\n\nFor each paper, provide: full title, authors (if available), key contributions, methodology, and results. Fetch the actual arxiv pages to get accurate details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dae3930-abfd-48dc-99fd-16828545c9d7",
  "isSidechain": false,
  "requestId": "req_011CbThecbuukCM8KvxFbVTL",
  "type": "assistant",
  "uuid": "1ec5b627-e2cb-40a3-a631-26ae0e3569a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175CLR8T8H7kaEcgR8REQzp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13245,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1751,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13245,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1751,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13245
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

_source line 12 · 2026-05-27T20:26:38.795Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SypfAtJWby5bUXnHMEYkUx`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research diagnostic-guided self-improvement",
  "prompt": "I'm designing a research proposal about iterative self-improvement for mathematical reasoning where the model generates its own synthetic training data. The key innovation will be using diagnostic signals (like pass@k metrics, entropy, etc.) to guide WHEN to generate new synthetic data vs. WHEN to do RL training.\n\nPlease search for:\n\n1. Papers on \"pass@k\" as a diagnostic or training signal in LLM reasoning (2024-2026)\n2. Papers on entropy management during RL training for reasoning (Entrocraft, EntroPIC, etc.)\n3. Papers on self-generated synthetic data quality — how to filter/select good self-generated traces\n4. Papers on \"model collapse\" or \"self-consuming\" training loops — when iterative self-training fails\n5. Papers on difficulty-aware or curriculum-based synthetic data generation for math\n6. \"Self-rewarding\" language models (Meta's work and follow-ups)\n7. Any work on adaptive scheduling between exploration (generating new data) and exploitation (training on existing data) in self-improvement loops\n\nSearch queries:\n- \"self-rewarding language model mathematical reasoning\"\n- \"model collapse iterative self-training LLM\"\n- \"difficulty curriculum synthetic data math reasoning\"\n- \"pass@k frontier expansion self-improvement\"\n- \"exploration exploitation balance self-training LLM\"\n\nI need concrete paper titles, arxiv IDs, key findings, and how they inform the design of a diagnostic-guided self-improvement system."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ec5b627-e2cb-40a3-a631-26ae0e3569a4",
  "isSidechain": false,
  "requestId": "req_011CbThecbuukCM8KvxFbVTL",
  "type": "assistant",
  "uuid": "1b59a567-4e95-49b3-ba5c-0d64e8e3ad6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175CLR8T8H7kaEcgR8REQzp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13245,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1751,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13245,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1751,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13245
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

_source line 13 · 2026-05-27T20:28:00.372Z_

<details><summary>↩ Tool result · `toolu_01KpAaBfA3XdwRSCN71m7rST`</summary>

```text
Here are the detailed findings for all six papers:

---

## 1. SIRI (arXiv 2509.25176)

**Full Title:** "SIRI: Scaling Iterative Reinforcement Learning with Interleaved Compression"

**Authors:** Haoming Wen, Yushi Bai, Juanzi Li, Jie Tang

**Submitted:** September 29, 2025

**Key Contributions:**
- Introduces an iterative RL training method that alternates between compressing and expanding the reasoning budget (maximum rollout length) to reduce "overthinking" in large reasoning models while improving accuracy.

**Methodology -- Compression/Expansion Cycling:**
- The mechanism operates over **3 iterations**, each consisting of a compression phase followed by an expansion phase (6 total phases: Iter1-Compressed, Iter1-Expanded, Iter2-Compressed, Iter2-Expanded, Iter3-Compressed, Iter3-Expanded).
- Rollout lengths oscillate between **L_min = 8,192 tokens** and **L_max = 16,384 tokens** using a cosine scheduler: `L = (L_max + L_min)/2 + (L_max - L_min)/2 * cos(2*pi/T * t)` over a 640-step cycle.
- **Compression phase:** Forces the model to reason concisely within a limited context window, suppressing backtracking tokens (e.g., "wait") while preserving correct reasoning steps. This increases "reasoning density."
- **Expansion phase:** Relaxes the length limit, letting the model explore longer-horizon reasoning with its newly acquired concise reasoning ability.
- After each cycle, performance improves even as output length decreases.

**Training Setup:**
- Base models: DeepSeek-R1-Distill-Qwen-1.5B and 7B
- RL algorithm: GRPO with DAPO improvements (decoupled clip thresholds, no KL divergence)
- Dataset: 40K math problems from AIME, AMC, Omni-Math, STILL
- Hyperparameters: batch size 128, LR 1e-6, temperature 1.0 (training) / 0.6 (eval)

**Results on AIME24:**
| Method | Accuracy | Avg Length |
|---|---|---|
| Original 1.5B baseline | 28.2% | 12,333 tokens |
| SIRI-low | 40.4% | 7,093 tokens |
| SIRI-high | 43.6% | 10,049 tokens |

- **SIRI-low achieves 43.2% improvement over baseline while reducing token usage by 46.9%.** (The 43.2% figure is a relative improvement: ~12 percentage points absolute on a 28.2% baseline.)
- Baselines compared: DeepScaleR-Preview, DAPO-DeepScaleR-16K, OverThink, DAST, O1-Pruner, AdaptThink.

---

## 2. CLPD (arXiv 2605.11260)

**Full Title:** "Curriculum Learning-Guided Progressive Distillation in Large Language Models"

**Authors:** Jincheng Cao, Fanzhi Zeng, Leqi Liu, Aryan Mokhtari

**Submitted:** May 11, 2026

**Key Contributions:**
- Addresses the counter-intuitive problem where stronger teachers fail to produce better students during knowledge distillation, due to capacity mismatch.
- Proposes CLPD, a framework that jointly aligns data difficulty with teacher strength.

**Methodology:**
- **Explicit Curriculum:** Training examples are organized from easy to hard.
- **Implicit Curriculum:** Supervision signals are progressively scheduled from weaker to stronger teachers (teachers of increasing capacity are introduced as training advances).
- **Integration:** The framework is modular and can be integrated into standard distillation algorithms with minimal overhead.

**Results:**
- CLPD consistently outperforms standard distillation, data ordering alone, and teacher scheduling alone across multiple settings.
- Demonstrates the importance of jointly considering data ordering and teacher capacity when distilling reasoning abilities.

---

## 3. "Large Language Model Post-Training: A Unified View" (arXiv 2604.07941)

**Full Title:** "Large Language Model Post-Training: A Unified View of Off-Policy and On-Policy Learning"

**Authors:** Shiwan Zhao, Zhihu Wang, Xuyang Zhao, Jiaming Zhou, Caiyue Xu, Chenfei Liu, Liting Zhang, Yuhang Jia, Yanzhe Zhang, Hualong Yu, Zichen Xu, Qicheng Li, Yong Qin

**Submitted:** April 9, 2026 (revised April 16, 2026); 38 pages, 1 figure, 8 tables

**Key Contributions:**
- Organizes post-training methods through the lens of **trajectory provenance**, distinguishing between off-policy learning (externally supplied trajectories) and on-policy learning (learner-generated rollouts).
- Identifies three recurring mechanisms that structure all post-training methods:
  1. **Support expansion:** Making useful behaviors more accessible
  2. **Policy reshaping:** Improving performance within reachable regions
  3. **Behavioral consolidation:** Preserving and transferring useful behavior across model stages
- Covers SFT, preference optimization, RL, process supervision, verifier-guided methods, and distillation.

**Core Argument:**
- Progress increasingly depends on **coordinated systems design** (multi-stage pipeline composition) rather than any single dominant objective. This is the paper's central thesis about the field's direction.

---

## 4. PRISM (arXiv 2604.28123)

**Full Title:** "Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL"

**Authors:** Sudong Wang, Weiquan Huang, Xiaomin Yu, Zuhao Yang, Hehai Lin, Keming Wu, Chaojun Xiao, Chen Chen, Wenxuan Wang, Beier Zhu, Yunjian Zhang, Chengwei Qin

**Submitted:** April 2026

**Key Contributions:**
- Identifies that SFT introduces distributional drift that harms subsequent RL, especially in multimodal settings where perception and reasoning errors compound.
- Inserts an explicit **distribution-alignment stage** between SFT and RL.

**Methodology -- Three-Stage Pipeline:**
1. **Stage 1 (Cold-Start SFT):** Fine-tune on ~1.37M demonstrations (1.26M public + 107K curated from Gemini 3 Flash), freezing vision components.
2. **Stage 2 (Distribution Alignment):** Adversarial on-policy distillation for 500 steps. A Mixture-of-Experts discriminator plays a minimax game against the policy: `min_theta max_phi E[(r_phi(x,y+) - r_phi(x,y-))]`. The discriminator tries to distinguish supervision samples from policy rollouts; the policy tries to fool it. KL regularization is deliberately disabled (coefficient = 0.0) to allow free distribution shift.
   - **MoE Discriminator:** Two specialized experts -- a **Perception Expert** (evaluates visual grounding) and a **Reasoning Expert** (evaluates logical consistency). Combined score: `r(x,y) = 0.5*D_v(x,c) + 0.5*D_r(x,t)`. Replacing MoE with a single dense discriminator caused a 3.4-point average drop.
   - Uses 6K high-quality reserved samples, 16 rollouts per prompt at temperature 1.0.
   - Crucially, this is **black-box** -- requires only response-level samples, not teacher logits.
3. **Stage 3 (RLVR):** Standard outcome-based RL with verifiable rewards.

**Results (Qwen3-VL models):**
| Configuration | Avg Accuracy (4B) | Avg Accuracy (8B) |
|---|---|---|
| SFT -> GRPO (baseline) | 61.8% | 63.3% |
| PRISM + GRPO | 66.2% (+4.4) | 69.3% (+6.0) |

- Algorithm-agnostic: consistent improvements with GRPO, DAPO (+4.5/+5.6), and GSPO (+3.8/+5.4).
- SFT-induced drift is more pronounced for stronger models (8B drops more than 4B from SFT alone).

---

## 5. "Decoupling KL and Trajectories" (arXiv 2605.16826)

**Full Title:** "Decoupling KL and Trajectories: A Unified Perspective for SFT, DAgger, Offline RL, and OPD in LLM Distillation"

**Authors:** Anhao Zhao, Haoran Xin, Yingqi Fan, Junlong Tong, Wenjie Li, Xiaoyu Shen

**Key Contributions:**
- Shows that existing distillation approaches implicitly couple two orthogonal design choices: **prefix source** (who generates the context) and **token-level KL direction** (forward vs. reverse).
- By decomposing this coupling, identifies four distinct objectives that unify SFT, DAgger, offline RL, and OPD as points in a continuous design space.

**Theoretical Framework:**
- **Forward KL** produces cross-entropy matching with teacher soft targets (SFT-style behavior).
- **Reverse KL** generates policy-gradient objectives with dense reward signals (RL-style behavior).
- KL direction affects accuracy vs. output diversity; prefix source affects quality vs. computational cost; training length affects accuracy vs. stability.

**Results:**
- Introduces **KL mixing** and an **entropy-gated length curriculum**, improving performance by up to **5.8 points** while reducing average response length by approximately **3x** compared to fixed long-horizon training.
- Code publicly available.

---

## 6. "Post-Training is About States, Not Tokens" (arXiv 2605.22731)

**Full Title:** "Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation"

**Author:** Dong Nie (single author)

**Submitted:** May 21, 2026

**Key Contributions:**
- Reframes post-training analysis from focusing on loss functions to analyzing the **state distribution** on which supervision is applied, where a "state" = prompt + generated prefix in autoregressive generation.
- SFT trains on fixed dataset states; RL and on-policy distillation train on states from the current learner.

**Methodology:**
- Controlled study using Qwen3-0.6B-Base, evaluated on GSM8K (target task), TruthfulQA and MMLU (retention).

**Key Findings:**
1. Mild SFT improves performance with minimal forgetting; intensive SFT causes substantial retention loss.
2. On-policy distillation from a **degraded teacher** surpasses that teacher across all tested benchmarks (a striking result).
3. Lightweight on-policy RL improves target task performance while maintaining retention.

**Core Insight:** "The source and locality of training states can be as important as the form of the supervision signal." This argues that the distribution of states seen during training is the primary axis differentiating post-training methods, not the loss function used.

---

**Summary of Verification Status:**

All six arXiv IDs resolved to real papers with content matching the descriptions provided in the review. The details (titles, methodologies, results) are consistent with what was flagged. One minor note: the SIRI "43.2% improvement" is a **relative** improvement (28.2% -> 40.4% accuracy on AIME24 for SIRI-low), not an absolute percentage point gain.

agentId: ac066298c4ece9054 (use SendMessage with to: 'ac066298c4ece9054' to continue this agent)
&lt;usage>total_tokens: 18078
tool_uses: 9
duration_ms: 89196&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ec5b627-e2cb-40a3-a631-26ae0e3569a4",
  "isSidechain": false,
  "promptId": "a6903394-624e-4492-ad19-36a9e5620d23",
  "type": "user",
  "uuid": "f31ab617-5810-4a2d-82ce-a73df6ef29f9",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research several specific papers that were flagged in a review. Please search the web and fetch details on each:\n\n1. **SIRI (arXiv 2509.25176)**: A paper about iterative compression↔expansion cycling during RL for math reasoning. I need to understand: what exactly does it do? How does it achieve 43.2% improvement on AIME24? What is the compression/expansion cycling mechanism? How many iterations?\n\n2. **CLPD (arXiv 2605.11260, May 2026)**: Curriculum Learning-Guided Progressive Distillation — about progressively scheduling teachers of increasing capacity.\n\n3. **\"Large Language Model Post-Training: A Unified View\" (arXiv 2604.07941, Apr 2026)**: A 38-page survey about multi-stage pipeline composition and coordinated systems design.\n\n4. **PRISM (arXiv 2604.28123, Apr 2026)**: About inserting distribution-alignment stages between SFT and RL.\n\n5. **\"Decoupling KL and Trajectories\" (arXiv 2605.16826)**: Theoretical framework showing SFT/RL/OPD are points in continuous design space.\n\n6. **\"Post-Training is About States, Not Tokens\" (arXiv 2605.22731)**: Another theoretical unification paper.\n\nFor each paper, provide: full title, authors (if available), key contributions, methodology, and results. Fetch the actual arxiv pages to get accurate details.",
    "agentId": "ac066298c4ece9054",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the detailed findings for all six papers:\n\n---\n\n## 1. SIRI (arXiv 2509.25176)\n\n**Full Title:** \"SIRI: Scaling Iterative Reinforcement Learning with Interleaved Compression\"\n\n**Authors:** Haoming Wen, Yushi Bai, Juanzi Li, Jie Tang\n\n**Submitted:** September 29, 2025\n\n**Key Contributions:**\n- Introduces an iterative RL training method that alternates between compressing and expanding the reasoning budget (maximum rollout length) to reduce \"overthinking\" in large reasoning models while improving accuracy.\n\n**Methodology -- Compression/Expansion Cycling:**\n- The mechanism operates over **3 iterations**, each consisting of a compression phase followed by an expansion phase (6 total phases: Iter1-Compressed, Iter1-Expanded, Iter2-Compressed, Iter2-Expanded, Iter3-Compressed, Iter3-Expanded).\n- Rollout lengths oscillate between **L_min = 8,192 tokens** and **L_max = 16,384 tokens** using a cosine scheduler: `L = (L_max + L_min)/2 + (L_max - L_min)/2 * cos(2*pi/T * t)` over a 640-step cycle.\n- **Compression phase:** Forces the model to reason concisely within a limited context window, suppressing backtracking tokens (e.g., \"wait\") while preserving correct reasoning steps. This increases \"reasoning density.\"\n- **Expansion phase:** Relaxes the length limit, letting the model explore longer-horizon reasoning with its newly acquired concise reasoning ability.\n- After each cycle, performance improves even as output length decreases.\n\n**Training Setup:**\n- Base models: DeepSeek-R1-Distill-Qwen-1.5B and 7B\n- RL algorithm: GRPO with DAPO improvements (decoupled clip thresholds, no KL divergence)\n- Dataset: 40K math problems from AIME, AMC, Omni-Math, STILL\n- Hyperparameters: batch size 128, LR 1e-6, temperature 1.0 (training) / 0.6 (eval)\n\n**Results on AIME24:**\n| Method | Accuracy | Avg Length |\n|---|---|---|\n| Original 1.5B baseline | 28.2% | 12,333 tokens |\n| SIRI-low | 40.4% | 7,093 tokens |\n| SIRI-high | 43.6% | 10,049 tokens |\n\n- **SIRI-low achieves 43.2% improvement over baseline while reducing token usage by 46.9%.** (The 43.2% figure is a relative improvement: ~12 percentage points absolute on a 28.2% baseline.)\n- Baselines compared: DeepScaleR-Preview, DAPO-DeepScaleR-16K, OverThink, DAST, O1-Pruner, AdaptThink.\n\n---\n\n## 2. CLPD (arXiv 2605.11260)\n\n**Full Title:** \"Curriculum Learning-Guided Progressive Distillation in Large Language Models\"\n\n**Authors:** Jincheng Cao, Fanzhi Zeng, Leqi Liu, Aryan Mokhtari\n\n**Submitted:** May 11, 2026\n\n**Key Contributions:**\n- Addresses the counter-intuitive problem where stronger teachers fail to produce better students during knowledge distillation, due to capacity mismatch.\n- Proposes CLPD, a framework that jointly aligns data difficulty with teacher strength.\n\n**Methodology:**\n- **Explicit Curriculum:** Training examples are organized from easy to hard.\n- **Implicit Curriculum:** Supervision signals are progressively scheduled from weaker to stronger teachers (teachers of increasing capacity are introduced as training advances).\n- **Integration:** The framework is modular and can be integrated into standard distillation algorithms with minimal overhead.\n\n**Results:**\n- CLPD consistently outperforms standard distillation, data ordering alone, and teacher scheduling alone across multiple settings.\n- Demonstrates the importance of jointly considering data ordering and teacher capacity when distilling reasoning abilities.\n\n---\n\n## 3. \"Large Language Model Post-Training: A Unified View\" (arXiv 2604.07941)\n\n**Full Title:** \"Large Language Model Post-Training: A Unified View of Off-Policy and On-Policy Learning\"\n\n**Authors:** Shiwan Zhao, Zhihu Wang, Xuyang Zhao, Jiaming Zhou, Caiyue Xu, Chenfei Liu, Liting Zhang, Yuhang Jia, Yanzhe Zhang, Hualong Yu, Zichen Xu, Qicheng Li, Yong Qin\n\n**Submitted:** April 9, 2026 (revised April 16, 2026); 38 pages, 1 figure, 8 tables\n\n**Key Contributions:**\n- Organizes post-training methods through the lens of **trajectory provenance**, distinguishing between off-policy learning (externally supplied trajectories) and on-policy learning (learner-generated rollouts).\n- Identifies three recurring mechanisms that structure all post-training methods:\n  1. **Support expansion:** Making useful behaviors more accessible\n  2. **Policy reshaping:** Improving performance within reachable regions\n  3. **Behavioral consolidation:** Preserving and transferring useful behavior across model stages\n- Covers SFT, preference optimization, RL, process supervision, verifier-guided methods, and distillation.\n\n**Core Argument:**\n- Progress increasingly depends on **coordinated systems design** (multi-stage pipeline composition) rather than any single dominant objective. This is the paper's central thesis about the field's direction.\n\n---\n\n## 4. PRISM (arXiv 2604.28123)\n\n**Full Title:** \"Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL\"\n\n**Authors:** Sudong Wang, Weiquan Huang, Xiaomin Yu, Zuhao Yang, Hehai Lin, Keming Wu, Chaojun Xiao, Chen Chen, Wenxuan Wang, Beier Zhu, Yunjian Zhang, Chengwei Qin\n\n**Submitted:** April 2026\n\n**Key Contributions:**\n- Identifies that SFT introduces distributional drift that harms subsequent RL, especially in multimodal settings where perception and reasoning errors compound.\n- Inserts an explicit **distribution-alignment stage** between SFT and RL.\n\n**Methodology -- Three-Stage Pipeline:**\n1. **Stage 1 (Cold-Start SFT):** Fine-tune on ~1.37M demonstrations (1.26M public + 107K curated from Gemini 3 Flash), freezing vision components.\n2. **Stage 2 (Distribution Alignment):** Adversarial on-policy distillation for 500 steps. A Mixture-of-Experts discriminator plays a minimax game against the policy: `min_theta max_phi E[(r_phi(x,y+) - r_phi(x,y-))]`. The discriminator tries to distinguish supervision samples from policy rollouts; the policy tries to fool it. KL regularization is deliberately disabled (coefficient = 0.0) to allow free distribution shift.\n   - **MoE Discriminator:** Two specialized experts -- a **Perception Expert** (evaluates visual grounding) and a **Reasoning Expert** (evaluates logical consistency). Combined score: `r(x,y) = 0.5*D_v(x,c) + 0.5*D_r(x,t)`. Replacing MoE with a single dense discriminator caused a 3.4-point average drop.\n   - Uses 6K high-quality reserved samples, 16 rollouts per prompt at temperature 1.0.\n   - Crucially, this is **black-box** -- requires only response-level samples, not teacher logits.\n3. **Stage 3 (RLVR):** Standard outcome-based RL with verifiable rewards.\n\n**Results (Qwen3-VL models):**\n| Configuration | Avg Accuracy (4B) | Avg Accuracy (8B) |\n|---|---|---|\n| SFT -> GRPO (baseline) | 61.8% | 63.3% |\n| PRISM + GRPO | 66.2% (+4.4) | 69.3% (+6.0) |\n\n- Algorithm-agnostic: consistent improvements with GRPO, DAPO (+4.5/+5.6), and GSPO (+3.8/+5.4).\n- SFT-induced drift is more pronounced for stronger models (8B drops more than 4B from SFT alone).\n\n---\n\n## 5. \"Decoupling KL and Trajectories\" (arXiv 2605.16826)\n\n**Full Title:** \"Decoupling KL and Trajectories: A Unified Perspective for SFT, DAgger, Offline RL, and OPD in LLM Distillation\"\n\n**Authors:** Anhao Zhao, Haoran Xin, Yingqi Fan, Junlong Tong, Wenjie Li, Xiaoyu Shen\n\n**Key Contributions:**\n- Shows that existing distillation approaches implicitly couple two orthogonal design choices: **prefix source** (who generates the context) and **token-level KL direction** (forward vs. reverse).\n- By decomposing this coupling, identifies four distinct objectives that unify SFT, DAgger, offline RL, and OPD as points in a continuous design space.\n\n**Theoretical Framework:**\n- **Forward KL** produces cross-entropy matching with teacher soft targets (SFT-style behavior).\n- **Reverse KL** generates policy-gradient objectives with dense reward signals (RL-style behavior).\n- KL direction affects accuracy vs. output diversity; prefix source affects quality vs. computational cost; training length affects accuracy vs. stability.\n\n**Results:**\n- Introduces **KL mixing** and an **entropy-gated length curriculum**, improving performance by up to **5.8 points** while reducing average response length by approximately **3x** compared to fixed long-horizon training.\n- Code publicly available.\n\n---\n\n## 6. \"Post-Training is About States, Not Tokens\" (arXiv 2605.22731)\n\n**Full Title:** \"Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation\"\n\n**Author:** Dong Nie (single author)\n\n**Submitted:** May 21, 2026\n\n**Key Contributions:**\n- Reframes post-training analysis from focusing on loss functions to analyzing the **state distribution** on which supervision is applied, where a \"state\" = prompt + generated prefix in autoregressive generation.\n- SFT trains on fixed dataset states; RL and on-policy distillation train on states from the current learner.\n\n**Methodology:**\n- Controlled study using Qwen3-0.6B-Base, evaluated on GSM8K (target task), TruthfulQA and MMLU (retention).\n\n**Key Findings:**\n1. Mild SFT improves performance with minimal forgetting; intensive SFT causes substantial retention loss.\n2. On-policy distillation from a **degraded teacher** surpasses that teacher across all tested benchmarks (a striking result).\n3. Lightweight on-policy RL improves target task performance while maintaining retention.\n\n**Core Insight:** \"The source and locality of training states can be as important as the form of the supervision signal.\" This argues that the distribution of states seen during training is the primary axis differentiating post-training methods, not the loss function used.\n\n---\n\n**Summary of Verification Status:**\n\nAll six arXiv IDs resolved to real papers with content matching the descriptions provided in the review. The details (titles, methodologies, results) are consistent with what was flagged. One minor note: the SIRI \"43.2% improvement\" is a **relative** improvement (28.2% -> 40.4% accuracy on AIME24 for SIRI-low), not an absolute percentage point gain."
      }
    ],
    "totalDurationMs": 89196,
    "totalTokens": 18078,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2253,
      "cache_read_input_tokens": 12900,
      "output_tokens": 2924,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2253
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2924,
          "cache_read_input_tokens": 12900,
          "cache_creation_input_tokens": 2253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2253,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 9
    }
  },
  "sourceToolAssistantUUID": "1ec5b627-e2cb-40a3-a631-26ae0e3569a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"FrontierCycle: Diagnostic-Guided Iterative RL↔Distillation Scheduling…",
  "leafUuid": "f31ab617-5810-4a2d-82ce-a73df6ef29f9",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise self-improvement framework for iterative LLM reasoning cycles",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---

### Tool result

_source line 16 · 2026-05-27T20:29:55.661Z_

<details><summary>↩ Tool result · `toolu_01SypfAtJWby5bUXnHMEYkUx`</summary>

```text
Here is a comprehensive literature survey organized by your seven research areas, with concrete paper titles, arxiv IDs, key findings, and design implications for your diagnostic-guided self-improvement system.

---

## 1. Pass@k as a Diagnostic / Training Signal

**Pass@k Training for Adaptively Balancing Exploration and Exploitation of Large Reasoning Models**
- ArXiv: 2508.10751 (Chen, Qin et al., 2025)
- Uses pass@k directly as a reward signal during training. Shows analytical solutions where exploration and exploitation mutually enhance each other. Even 7B models surpass GPT-4o and Claude-3.7-Sonnet on certain benchmarks.
- **Design implication:** Pass@k can serve as your primary diagnostic for deciding when the model needs more exploration (generate new data) vs. exploitation (train on existing data). A declining pass@k delta between k=1 and k=large signals the model's frontier is shrinking.

**Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?**
- ArXiv: 2504.13837 (Yue et al., 2025) -- NeurIPS 2025 Best Paper Runner-Up
- Critical finding: RLVR improves pass@1 (sampling efficiency) but does NOT expand pass@k at large k beyond the base model. The reasoning frontier is inherited from pretraining.
- **Design implication:** This is central to your proposal. It means that when your diagnostic detects that pass@k_large is plateauing, RL alone cannot help -- you must generate new synthetic data to expand the frontier before resuming RL.

**Beyond Pass@k: Breadth-Depth Metrics for Reasoning Boundaries**
- ArXiv: 2510.08325 (Dragoi et al., 2025)
- Proposes Cover@tau, which measures the fraction of solvable problems where at least a tau proportion of completions are correct. Unlike pass@k, this captures genuine reasoning reliability rather than lucky sampling.
- **Design implication:** Cover@tau is a better diagnostic than raw pass@k for your system -- it distinguishes between problems the model "truly understands" vs. "gets right by chance," enabling more targeted data generation.

**Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR (SvS)**
- ArXiv: 2508.14029 (Liang, Li et al., 2025)
- Uses correct solutions to synthesize variational (structurally diverse) problems while keeping reference answers identical. Maintains policy entropy and achieves +18.3% and +22.8% pass@32 on AIME24/AIME25.
- **Design implication:** When your diagnostic detects entropy decline and pass@k stagnation, variational problem synthesis is a concrete mechanism for generating useful new training data.

---

## 2. Entropy Management During RL Training

**EntroPIC: Towards Stable Long-Term Training of LLMs via Entropy Stabilization with Proportional-Integral Control**
- ArXiv: 2511.15248 (2025)
- Uses a PID controller to maintain target entropy during RLVR training. Too-low entropy causes premature convergence; too-high causes noise. EntroPIC-Nemotron-1.5B sets new benchmarks for 1.5B models.
- **Design implication:** Your system should incorporate an entropy PID controller as a real-time diagnostic signal. When entropy drops below threshold despite the controller, that is a signal to switch from RL to data generation.

**Entrocraft: Addressing Performance Saturation for LLM RL via Precise Entropy Curve Control**
- ArXiv: 2604.26326 (2026)
- Uses entropy-guided rejection sampling to filter rollouts against a target entropy schedule. No objective regularization needed. Shows that linear annealing (start high, decay to slightly lower target) works best.
- **Design implication:** Entrocraft's entropy schedule concept can be directly integrated as a diagnostic -- deviations from the planned entropy curve trigger your system's mode-switching logic.

**Revisiting Entropy in Reinforcement Learning for Large Reasoning Models**
- ArXiv: 2511.05993 (Jin et al., 2025, updated Jan 2026)
- Identifies three key factors influencing entropy: clipping thresholds, number of off-policy updates, and training data diversity. Entropy collapse leads to premature convergence to suboptimal local minima.
- **Design implication:** Training data diversity is one of three entropy levers. When your diagnostic detects entropy decline, data diversity injection (new synthetic data generation) is a principled response.

**The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models**
- ArXiv: 2505.22617 (2025)
- Establishes that output diversity (quantified by entropy) is critical for both effectiveness and stability of RL training for reasoning.

**Rethinking Entropy Regularization in Large Reasoning Models**
- ArXiv: 2509.25133 (2025)
- Examines when and how entropy regularization helps vs. hurts in reasoning LLM training.

---

## 3. Self-Generated Synthetic Data Quality: Filtering and Selection

**STaR: Self-Taught Reasoner -- Bootstrapping Reasoning With Reasoning**
- ArXiv: 2203.14465 (Zelikman et al., 2022, NeurIPS)
- The foundational iterative self-improvement paper. Generate rationales, filter to keep only those leading to correct answers, fine-tune, repeat. Also uses "rationalization" -- giving the model the correct answer to generate a rationale for hard problems.
- **Design implication:** STaR's correctness-filtering is the baseline mechanism for your system. Your diagnostic signals should determine when STaR-style filtering is sufficient vs. when you need more aggressive curation.

**Think, Prune, Train, Improve: Scaling Reasoning without Scaling Models**
- ArXiv: 2504.18116 (Costello, Guo, Goldie, Mirhoseini, 2025 -- Stanford)
- Iteratively fine-tunes models on their own reasoning traces with ground-truth pruning. Gemma2-2B goes from 41.9% to 57.6% on GSM8K; LLaMA-3.1-70B reaches 91%, surpassing GPT-4o.
- **Design implication:** Demonstrates that self-generated data + systematic pruning works. The "prune" step is essentially a diagnostic-guided filter.

**RL on Incorrect Synthetic Data Scales the Efficiency of LLM Math Reasoning by Eight-Fold**
- ArXiv: 2406.14532 (Setlur et al., 2024, NeurIPS 2024)
- Counterintuitive finding: RL on incorrect synthetic traces is 8x more efficient than training on correct data alone. Training on model-generated positives can amplify spurious correlations.
- **Design implication:** Your system should NOT discard incorrect traces. Instead, use them for RL (as negative examples or for contrastive learning), while using correct traces for SFT. This creates a natural dual-use of self-generated data.

**Self-Rewarding Correction for Mathematical Reasoning**
- ArXiv: 2502.19613 (Feb 2025)
- Models simultaneously solve, critique, and correct. Two-stage framework using sequential rejection sampling to synthesize long chain-of-thought trajectories incorporating self-rewarding and self-correction.
- **Design implication:** Self-correction traces are a particularly valuable form of synthetic data -- they capture the model's error patterns and recovery strategies.

---

## 4. Model Collapse / Self-Consuming Training Loops

**AI Models Collapse When Trained on Recursively Generated Data**
- Nature, 2024 (Shumailov et al.)
- The landmark paper establishing that iterative training on synthetic data causes "model collapse" -- tails of the original distribution disappear, variance trends toward zero.
- **Design implication:** This is the primary risk your diagnostic system must guard against. Pure self-training without external anchoring will collapse.

**Strong Model Collapse**
- ICLR 2025
- Shows model collapse persists even on mixtures of synthetic and real data, as long as the synthetic fraction does not vanish. Establishes that collapse is not just a theoretical concern.

**Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence**
- ArXiv: 2510.16657 (Yi et al., 2025, NeurIPS 2025)
- Key finding: External verification (human or better model) prevents collapse, but gains plateau and may reverse unless the verifier is perfectly reliable. Retraining converges to the verifier's "knowledge center."
- **Design implication:** Your system's verifier quality bounds the long-term outcome. Diagnostics should track whether the model is approaching the verifier's knowledge ceiling (diminishing returns on verification pass rate).

**Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World**
- ArXiv: 2410.16713 (2024)
- Comprehensive survey of conditions under which self-consuming loops succeed vs. fail.

**Model Collapse is Not a Bug but a Feature**
- ArXiv: 2507.04219 (2025)
- Provocative reframing -- argues there are contexts where collapse-like behavior is actually beneficial (e.g., denoising). Worth noting as a counterpoint.

---

## 5. Difficulty-Aware / Curriculum-Based Synthetic Data Generation

**DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving**
- ArXiv: 2407.13690 (NeurIPS 2024)
- Identifies severe bias toward easy queries in existing datasets. Proposes Difficulty-Aware Rejection Sampling (DARS) with two strategies: Uniform (each query gets equal correct responses) and Prop2Diff (correct responses proportional to difficulty).
- **Design implication:** Your data generation phase should use difficulty-aware sampling. When diagnostics show pass@k is high for easy problems but low for hard ones, allocate more generation budget to hard problems.

**Self-Evolving Curriculum for LLM Reasoning (SEC)**
- ArXiv: 2505.14970 (Chen, Lu, Bengio et al., 2025)
- Formulates curriculum selection as a non-stationary Multi-Armed Bandit problem. Each problem category is an arm. Achieves up to +33% on AIME24.
- **Design implication:** Directly applicable -- your system can use MAB to adaptively select which difficulty band to generate new data for, using pass@k as the bandit reward signal.

**MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning**
- ArXiv: 2601.17006 (Jan 2026)
- Shows that difficulty-controllable data + curriculum learning combine for greatest improvement. Identifies lack of explicit difficulty gradients as a fundamental constraint.

**MathSmith: Towards Extremely Hard Mathematical Reasoning by Forging Synthetic Problems with a Reinforced Policy**
- ArXiv: 2508.05592 (Tsinghua, Aug 2025)
- Uses RL to optimize problem generation itself -- jointly optimizes structural validity, reasoning complexity, and answer consistency. Encourages longer reasoning traces as a difficulty heuristic.
- **Design implication:** Instead of just filtering generated problems by difficulty, you can RL-train the problem generator itself, creating a nested self-improvement loop.

---

## 6. Self-Rewarding Language Models

**Self-Rewarding Language Models**
- ArXiv: 2401.10020 (Yuan et al., Meta, Jan 2024)
- The foundational paper. Model acts as both actor (generates responses) and judge (evaluates and assigns rewards). Uses LLM-as-a-Judge for iterative DPO training.

**Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge**
- ArXiv: 2407.19594 (Wu et al., Meta, Jul 2024)
- Adds a meta-rewarding step: the model judges its own judgments. Addresses the saturation problem in vanilla self-rewarding (judge quality stagnates). Llama-3-8B-Instruct goes from 22.9% to 39.4% on AlpacaEval 2.
- **Design implication:** Your system should not just self-evaluate solutions but also self-evaluate the quality of its evaluations (meta-judgment). Track meta-judge agreement as a diagnostic.

**Process-based Self-Rewarding Language Models**
- ArXiv: 2503.03746 (Zhang et al., Findings of ACL 2025)
- Extends self-rewarding to step-wise process rewards. For each reasoning step, generates multiple candidates and uses LLM-as-a-Judge at the step level. Overcomes the limitation that outcome-level self-rewarding fails for complex multi-step reasoning.
- **Design implication:** Step-level diagnostics are more informative than outcome-level. Your system should track at which reasoning step the model most frequently fails, and target data generation there.

**Can Large Reasoning Models Self-Train? (SRT)**
- ArXiv: 2505.21444 (Shafayat et al., May 2025)
- Uses self-consistency to infer correctness signals without ground truth. Quickly rivals RL with gold-standard answers. BUT: prolonged training causes reward hacking and complete performance collapse.
- **Design implication:** This is a critical cautionary result. Your diagnostic system must detect reward hacking (e.g., self-consistency scores rising while external validation scores plateau or drop) and trigger a mode switch.

---

## 7. Adaptive Scheduling: Exploration vs. Exploitation in Self-Improvement

**Pass@k Training for Adaptively Balancing Exploration and Exploitation** (also listed in section 1)
- ArXiv: 2508.10751
- Provides analytical framework showing exploration and exploitation can be mutually reinforcing when properly balanced via pass@k rewards.

**ETTRL: Balancing Exploration and Exploitation in LLM Test-Time Reinforcement Learning Via Entropy Mechanism**
- ArXiv: 2508.11356 (Liu et al., Aug 2025)
- Two mechanisms: (1) Entropy-fork Tree Majority Rollout -- selectively branches only at highest-entropy tokens for diverse candidates; (2) Entropy-based Advantage Reshaping -- sustains exploration. +68% relative pass@1 improvement on AIME 2024 with only 60% of the token budget.
- **Design implication:** Entropy at the token level is a fine-grained diagnostic for where the model is uncertain, enabling targeted exploration.

**rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking**
- ArXiv: 2501.04519 (ICML 2025)
- Uses MCTS for test-time exploration + iterative self-evolution of both the policy and process reward model. Achieves o1-level performance with 7B models.
- **Design implication:** MCTS provides a natural exploration mechanism. The iterative co-evolution of policy + reward model is a form of adaptive scheduling between exploration and exploitation.

**Self-Evolving Curriculum (SEC)** (also listed in section 5)
- ArXiv: 2505.14970
- MAB-based adaptive curriculum that naturally balances exploration of new difficulty levels vs. exploitation of mastered ones.

---

## Synthesis: How These Inform Your Diagnostic-Guided System

Your proposed system -- using diagnostic signals to decide WHEN to generate new synthetic data vs. WHEN to do RL training -- is well-supported by the literature but not yet implemented as a unified framework. Here is how the pieces fit together:

**Core diagnostics to monitor:**
1. **Pass@k spectrum** (pass@1 vs. pass@k_large) -- When the gap narrows, the model is becoming more efficient but not more capable. Time to generate new data.
2. **Policy entropy** -- When entropy drops below a PID-controlled target despite regularization, the model is collapsing. Time to inject new diverse data.
3. **Cover@tau** -- When Cover@tau saturates at moderate tau values, the model has "soft mastery" but lacks deep reliability. Target data generation at those difficulty levels.
4. **Self-consistency vs. external validation gap** -- When self-consistency scores diverge from ground-truth accuracy, reward hacking is occurring. Pause self-training, inject external verification.
5. **Difficulty-stratified pass rates** -- When easy-problem pass@1 is high but hard-problem pass@k is flat, use DART-style difficulty-aware generation.

**Mode-switching logic:**
- **Generate new data** when: entropy is dropping, pass@k_large is plateauing, difficulty-stratified diagnostics show capability gaps, or self-consistency is diverging from external validation.
- **Do RL training** when: fresh diverse data has been generated, entropy is healthy, and pass@k_large shows room for improvement (frontier has expanded but pass@1 efficiency lags behind).
- **Stop / checkpoint** when: Cover@tau is approaching verifier ceiling (per the model collapse verification paper), or reward hacking is detected.

**Key risks your system must address:**
- Model collapse from recursive self-training (Shumailov et al.) -- mitigated by external verification and diversity diagnostics
- Reward hacking from prolonged self-rewarding (SRT paper) -- mitigated by external validation checks
- Pass@k optimization degrading pass@1 (the exploration-exploitation tension) -- mitigated by adaptive scheduling

Sources:
- [Pass@k Training for Adaptively Balancing Exploration and Exploitation](https://arxiv.org/abs/2508.10751)
- [Does RL Really Incentivize Reasoning Beyond the Base Model?](https://arxiv.org/abs/2504.13837)
- [Beyond Pass@k: Breadth-Depth Metrics for Reasoning Boundaries](https://arxiv.org/abs/2510.08325)
- [Beyond Pass@1: Self-Play with Variational Problem Synthesis (SvS)](https://arxiv.org/abs/2508.14029)
- [EntroPIC: Entropy Stabilization with PI Control](https://arxiv.org/abs/2511.15248)
- [Entrocraft: Precise Entropy Curve Control](https://arxiv.org/abs/2604.26326)
- [Revisiting Entropy in RL for Large Reasoning Models](https://arxiv.org/abs/2511.05993)
- [The Entropy Mechanism of RL for Reasoning LMs](https://arxiv.org/abs/2505.22617)
- [Rethinking Entropy Regularization in Large Reasoning Models](https://arxiv.org/abs/2509.25133)
- [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465)
- [Quiet-STaR: Language Models Can Teach Themselves to Think](https://arxiv.org/abs/2403.09629)
- [Think, Prune, Train, Improve](https://arxiv.org/abs/2504.18116)
- [RL on Incorrect Synthetic Data Scales Efficiency 8x](https://arxiv.org/abs/2406.14532)
- [Self-Rewarding Correction for Mathematical Reasoning](https://arxiv.org/abs/2502.19613)
- [AI Models Collapse When Trained on Recursively Generated Data (Nature)](https://www.nature.com/articles/s41586-024-07566-y)
- [Strong Model Collapse (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)
- [Escaping Model Collapse via Synthetic Data Verification](https://arxiv.org/abs/2510.16657)
- [Collapse or Thrive? Perils and Promises of Synthetic Data](https://arxiv.org/abs/2410.16713)
- [DART-Math: Difficulty-Aware Rejection Tuning](https://arxiv.org/abs/2407.13690)
- [Self-Evolving Curriculum for LLM Reasoning (SEC)](https://arxiv.org/abs/2505.14970)
- [MathMixup: Difficulty-Controllable Synthesis + Curriculum](https://arxiv.org/abs/2601.17006)
- [MathSmith: Forging Synthetic Problems with RL](https://arxiv.org/abs/2508.05592)
- [Self-Rewarding Language Models (Meta)](https://arxiv.org/abs/2401.10020)
- [Meta-Rewarding Language Models: LLM-as-a-Meta-Judge](https://arxiv.org/abs/2407.19594)
- [Process-based Self-Rewarding Language Models (ACL 2025)](https://arxiv.org/abs/2503.03746)
- [Can Large Reasoning Models Self-Train? (SRT)](https://arxiv.org/abs/2505.21444)
- [ETTRL: Balancing Exploration and Exploitation via Entropy](https://arxiv.org/abs/2508.11356)
- [rStar-Math: Self-Evolved Deep Thinking (ICML 2025)](https://arxiv.org/abs/2501.04519)

agentId: ae1f242ee57dea9eb (use SendMessage with to: 'ae1f242ee57dea9eb' to continue this agent)
&lt;usage>total_tokens: 39742
tool_uses: 30
duration_ms: 196863&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b59a567-4e95-49b3-ba5c-0d64e8e3ad6d",
  "isSidechain": false,
  "promptId": "a6903394-624e-4492-ad19-36a9e5620d23",
  "type": "user",
  "uuid": "f1894205-f10e-49ae-b504-c7b2b92b8a17",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm designing a research proposal about iterative self-improvement for mathematical reasoning where the model generates its own synthetic training data. The key innovation will be using diagnostic signals (like pass@k metrics, entropy, etc.) to guide WHEN to generate new synthetic data vs. WHEN to do RL training.\n\nPlease search for:\n\n1. Papers on \"pass@k\" as a diagnostic or training signal in LLM reasoning (2024-2026)\n2. Papers on entropy management during RL training for reasoning (Entrocraft, EntroPIC, etc.)\n3. Papers on self-generated synthetic data quality — how to filter/select good self-generated traces\n4. Papers on \"model collapse\" or \"self-consuming\" training loops — when iterative self-training fails\n5. Papers on difficulty-aware or curriculum-based synthetic data generation for math\n6. \"Self-rewarding\" language models (Meta's work and follow-ups)\n7. Any work on adaptive scheduling between exploration (generating new data) and exploitation (training on existing data) in self-improvement loops\n\nSearch queries:\n- \"self-rewarding language model mathematical reasoning\"\n- \"model collapse iterative self-training LLM\"\n- \"difficulty curriculum synthetic data math reasoning\"\n- \"pass@k frontier expansion self-improvement\"\n- \"exploration exploitation balance self-training LLM\"\n\nI need concrete paper titles, arxiv IDs, key findings, and how they inform the design of a diagnostic-guided self-improvement system.",
    "agentId": "ae1f242ee57dea9eb",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a comprehensive literature survey organized by your seven research areas, with concrete paper titles, arxiv IDs, key findings, and design implications for your diagnostic-guided self-improvement system.\n\n---\n\n## 1. Pass@k as a Diagnostic / Training Signal\n\n**Pass@k Training for Adaptively Balancing Exploration and Exploitation of Large Reasoning Models**\n- ArXiv: 2508.10751 (Chen, Qin et al., 2025)\n- Uses pass@k directly as a reward signal during training. Shows analytical solutions where exploration and exploitation mutually enhance each other. Even 7B models surpass GPT-4o and Claude-3.7-Sonnet on certain benchmarks.\n- **Design implication:** Pass@k can serve as your primary diagnostic for deciding when the model needs more exploration (generate new data) vs. exploitation (train on existing data). A declining pass@k delta between k=1 and k=large signals the model's frontier is shrinking.\n\n**Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?**\n- ArXiv: 2504.13837 (Yue et al., 2025) -- NeurIPS 2025 Best Paper Runner-Up\n- Critical finding: RLVR improves pass@1 (sampling efficiency) but does NOT expand pass@k at large k beyond the base model. The reasoning frontier is inherited from pretraining.\n- **Design implication:** This is central to your proposal. It means that when your diagnostic detects that pass@k_large is plateauing, RL alone cannot help -- you must generate new synthetic data to expand the frontier before resuming RL.\n\n**Beyond Pass@k: Breadth-Depth Metrics for Reasoning Boundaries**\n- ArXiv: 2510.08325 (Dragoi et al., 2025)\n- Proposes Cover@tau, which measures the fraction of solvable problems where at least a tau proportion of completions are correct. Unlike pass@k, this captures genuine reasoning reliability rather than lucky sampling.\n- **Design implication:** Cover@tau is a better diagnostic than raw pass@k for your system -- it distinguishes between problems the model \"truly understands\" vs. \"gets right by chance,\" enabling more targeted data generation.\n\n**Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR (SvS)**\n- ArXiv: 2508.14029 (Liang, Li et al., 2025)\n- Uses correct solutions to synthesize variational (structurally diverse) problems while keeping reference answers identical. Maintains policy entropy and achieves +18.3% and +22.8% pass@32 on AIME24/AIME25.\n- **Design implication:** When your diagnostic detects entropy decline and pass@k stagnation, variational problem synthesis is a concrete mechanism for generating useful new training data.\n\n---\n\n## 2. Entropy Management During RL Training\n\n**EntroPIC: Towards Stable Long-Term Training of LLMs via Entropy Stabilization with Proportional-Integral Control**\n- ArXiv: 2511.15248 (2025)\n- Uses a PID controller to maintain target entropy during RLVR training. Too-low entropy causes premature convergence; too-high causes noise. EntroPIC-Nemotron-1.5B sets new benchmarks for 1.5B models.\n- **Design implication:** Your system should incorporate an entropy PID controller as a real-time diagnostic signal. When entropy drops below threshold despite the controller, that is a signal to switch from RL to data generation.\n\n**Entrocraft: Addressing Performance Saturation for LLM RL via Precise Entropy Curve Control**\n- ArXiv: 2604.26326 (2026)\n- Uses entropy-guided rejection sampling to filter rollouts against a target entropy schedule. No objective regularization needed. Shows that linear annealing (start high, decay to slightly lower target) works best.\n- **Design implication:** Entrocraft's entropy schedule concept can be directly integrated as a diagnostic -- deviations from the planned entropy curve trigger your system's mode-switching logic.\n\n**Revisiting Entropy in Reinforcement Learning for Large Reasoning Models**\n- ArXiv: 2511.05993 (Jin et al., 2025, updated Jan 2026)\n- Identifies three key factors influencing entropy: clipping thresholds, number of off-policy updates, and training data diversity. Entropy collapse leads to premature convergence to suboptimal local minima.\n- **Design implication:** Training data diversity is one of three entropy levers. When your diagnostic detects entropy decline, data diversity injection (new synthetic data generation) is a principled response.\n\n**The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models**\n- ArXiv: 2505.22617 (2025)\n- Establishes that output diversity (quantified by entropy) is critical for both effectiveness and stability of RL training for reasoning.\n\n**Rethinking Entropy Regularization in Large Reasoning Models**\n- ArXiv: 2509.25133 (2025)\n- Examines when and how entropy regularization helps vs. hurts in reasoning LLM training.\n\n---\n\n## 3. Self-Generated Synthetic Data Quality: Filtering and Selection\n\n**STaR: Self-Taught Reasoner -- Bootstrapping Reasoning With Reasoning**\n- ArXiv: 2203.14465 (Zelikman et al., 2022, NeurIPS)\n- The foundational iterative self-improvement paper. Generate rationales, filter to keep only those leading to correct answers, fine-tune, repeat. Also uses \"rationalization\" -- giving the model the correct answer to generate a rationale for hard problems.\n- **Design implication:** STaR's correctness-filtering is the baseline mechanism for your system. Your diagnostic signals should determine when STaR-style filtering is sufficient vs. when you need more aggressive curation.\n\n**Think, Prune, Train, Improve: Scaling Reasoning without Scaling Models**\n- ArXiv: 2504.18116 (Costello, Guo, Goldie, Mirhoseini, 2025 -- Stanford)\n- Iteratively fine-tunes models on their own reasoning traces with ground-truth pruning. Gemma2-2B goes from 41.9% to 57.6% on GSM8K; LLaMA-3.1-70B reaches 91%, surpassing GPT-4o.\n- **Design implication:** Demonstrates that self-generated data + systematic pruning works. The \"prune\" step is essentially a diagnostic-guided filter.\n\n**RL on Incorrect Synthetic Data Scales the Efficiency of LLM Math Reasoning by Eight-Fold**\n- ArXiv: 2406.14532 (Setlur et al., 2024, NeurIPS 2024)\n- Counterintuitive finding: RL on incorrect synthetic traces is 8x more efficient than training on correct data alone. Training on model-generated positives can amplify spurious correlations.\n- **Design implication:** Your system should NOT discard incorrect traces. Instead, use them for RL (as negative examples or for contrastive learning), while using correct traces for SFT. This creates a natural dual-use of self-generated data.\n\n**Self-Rewarding Correction for Mathematical Reasoning**\n- ArXiv: 2502.19613 (Feb 2025)\n- Models simultaneously solve, critique, and correct. Two-stage framework using sequential rejection sampling to synthesize long chain-of-thought trajectories incorporating self-rewarding and self-correction.\n- **Design implication:** Self-correction traces are a particularly valuable form of synthetic data -- they capture the model's error patterns and recovery strategies.\n\n---\n\n## 4. Model Collapse / Self-Consuming Training Loops\n\n**AI Models Collapse When Trained on Recursively Generated Data**\n- Nature, 2024 (Shumailov et al.)\n- The landmark paper establishing that iterative training on synthetic data causes \"model collapse\" -- tails of the original distribution disappear, variance trends toward zero.\n- **Design implication:** This is the primary risk your diagnostic system must guard against. Pure self-training without external anchoring will collapse.\n\n**Strong Model Collapse**\n- ICLR 2025\n- Shows model collapse persists even on mixtures of synthetic and real data, as long as the synthetic fraction does not vanish. Establishes that collapse is not just a theoretical concern.\n\n**Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence**\n- ArXiv: 2510.16657 (Yi et al., 2025, NeurIPS 2025)\n- Key finding: External verification (human or better model) prevents collapse, but gains plateau and may reverse unless the verifier is perfectly reliable. Retraining converges to the verifier's \"knowledge center.\"\n- **Design implication:** Your system's verifier quality bounds the long-term outcome. Diagnostics should track whether the model is approaching the verifier's knowledge ceiling (diminishing returns on verification pass rate).\n\n**Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World**\n- ArXiv: 2410.16713 (2024)\n- Comprehensive survey of conditions under which self-consuming loops succeed vs. fail.\n\n**Model Collapse is Not a Bug but a Feature**\n- ArXiv: 2507.04219 (2025)\n- Provocative reframing -- argues there are contexts where collapse-like behavior is actually beneficial (e.g., denoising). Worth noting as a counterpoint.\n\n---\n\n## 5. Difficulty-Aware / Curriculum-Based Synthetic Data Generation\n\n**DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving**\n- ArXiv: 2407.13690 (NeurIPS 2024)\n- Identifies severe bias toward easy queries in existing datasets. Proposes Difficulty-Aware Rejection Sampling (DARS) with two strategies: Uniform (each query gets equal correct responses) and Prop2Diff (correct responses proportional to difficulty).\n- **Design implication:** Your data generation phase should use difficulty-aware sampling. When diagnostics show pass@k is high for easy problems but low for hard ones, allocate more generation budget to hard problems.\n\n**Self-Evolving Curriculum for LLM Reasoning (SEC)**\n- ArXiv: 2505.14970 (Chen, Lu, Bengio et al., 2025)\n- Formulates curriculum selection as a non-stationary Multi-Armed Bandit problem. Each problem category is an arm. Achieves up to +33% on AIME24.\n- **Design implication:** Directly applicable -- your system can use MAB to adaptively select which difficulty band to generate new data for, using pass@k as the bandit reward signal.\n\n**MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning**\n- ArXiv: 2601.17006 (Jan 2026)\n- Shows that difficulty-controllable data + curriculum learning combine for greatest improvement. Identifies lack of explicit difficulty gradients as a fundamental constraint.\n\n**MathSmith: Towards Extremely Hard Mathematical Reasoning by Forging Synthetic Problems with a Reinforced Policy**\n- ArXiv: 2508.05592 (Tsinghua, Aug 2025)\n- Uses RL to optimize problem generation itself -- jointly optimizes structural validity, reasoning complexity, and answer consistency. Encourages longer reasoning traces as a difficulty heuristic.\n- **Design implication:** Instead of just filtering generated problems by difficulty, you can RL-train the problem generator itself, creating a nested self-improvement loop.\n\n---\n\n## 6. Self-Rewarding Language Models\n\n**Self-Rewarding Language Models**\n- ArXiv: 2401.10020 (Yuan et al., Meta, Jan 2024)\n- The foundational paper. Model acts as both actor (generates responses) and judge (evaluates and assigns rewards). Uses LLM-as-a-Judge for iterative DPO training.\n\n**Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge**\n- ArXiv: 2407.19594 (Wu et al., Meta, Jul 2024)\n- Adds a meta-rewarding step: the model judges its own judgments. Addresses the saturation problem in vanilla self-rewarding (judge quality stagnates). Llama-3-8B-Instruct goes from 22.9% to 39.4% on AlpacaEval 2.\n- **Design implication:** Your system should not just self-evaluate solutions but also self-evaluate the quality of its evaluations (meta-judgment). Track meta-judge agreement as a diagnostic.\n\n**Process-based Self-Rewarding Language Models**\n- ArXiv: 2503.03746 (Zhang et al., Findings of ACL 2025)\n- Extends self-rewarding to step-wise process rewards. For each reasoning step, generates multiple candidates and uses LLM-as-a-Judge at the step level. Overcomes the limitation that outcome-level self-rewarding fails for complex multi-step reasoning.\n- **Design implication:** Step-level diagnostics are more informative than outcome-level. Your system should track at which reasoning step the model most frequently fails, and target data generation there.\n\n**Can Large Reasoning Models Self-Train? (SRT)**\n- ArXiv: 2505.21444 (Shafayat et al., May 2025)\n- Uses self-consistency to infer correctness signals without ground truth. Quickly rivals RL with gold-standard answers. BUT: prolonged training causes reward hacking and complete performance collapse.\n- **Design implication:** This is a critical cautionary result. Your diagnostic system must detect reward hacking (e.g., self-consistency scores rising while external validation scores plateau or drop) and trigger a mode switch.\n\n---\n\n## 7. Adaptive Scheduling: Exploration vs. Exploitation in Self-Improvement\n\n**Pass@k Training for Adaptively Balancing Exploration and Exploitation** (also listed in section 1)\n- ArXiv: 2508.10751\n- Provides analytical framework showing exploration and exploitation can be mutually reinforcing when properly balanced via pass@k rewards.\n\n**ETTRL: Balancing Exploration and Exploitation in LLM Test-Time Reinforcement Learning Via Entropy Mechanism**\n- ArXiv: 2508.11356 (Liu et al., Aug 2025)\n- Two mechanisms: (1) Entropy-fork Tree Majority Rollout -- selectively branches only at highest-entropy tokens for diverse candidates; (2) Entropy-based Advantage Reshaping -- sustains exploration. +68% relative pass@1 improvement on AIME 2024 with only 60% of the token budget.\n- **Design implication:** Entropy at the token level is a fine-grained diagnostic for where the model is uncertain, enabling targeted exploration.\n\n**rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking**\n- ArXiv: 2501.04519 (ICML 2025)\n- Uses MCTS for test-time exploration + iterative self-evolution of both the policy and process reward model. Achieves o1-level performance with 7B models.\n- **Design implication:** MCTS provides a natural exploration mechanism. The iterative co-evolution of policy + reward model is a form of adaptive scheduling between exploration and exploitation.\n\n**Self-Evolving Curriculum (SEC)** (also listed in section 5)\n- ArXiv: 2505.14970\n- MAB-based adaptive curriculum that naturally balances exploration of new difficulty levels vs. exploitation of mastered ones.\n\n---\n\n## Synthesis: How These Inform Your Diagnostic-Guided System\n\nYour proposed system -- using diagnostic signals to decide WHEN to generate new synthetic data vs. WHEN to do RL training -- is well-supported by the literature but not yet implemented as a unified framework. Here is how the pieces fit together:\n\n**Core diagnostics to monitor:**\n1. **Pass@k spectrum** (pass@1 vs. pass@k_large) -- When the gap narrows, the model is becoming more efficient but not more capable. Time to generate new data.\n2. **Policy entropy** -- When entropy drops below a PID-controlled target despite regularization, the model is collapsing. Time to inject new diverse data.\n3. **Cover@tau** -- When Cover@tau saturates at moderate tau values, the model has \"soft mastery\" but lacks deep reliability. Target data generation at those difficulty levels.\n4. **Self-consistency vs. external validation gap** -- When self-consistency scores diverge from ground-truth accuracy, reward hacking is occurring. Pause self-training, inject external verification.\n5. **Difficulty-stratified pass rates** -- When easy-problem pass@1 is high but hard-problem pass@k is flat, use DART-style difficulty-aware generation.\n\n**Mode-switching logic:**\n- **Generate new data** when: entropy is dropping, pass@k_large is plateauing, difficulty-stratified diagnostics show capability gaps, or self-consistency is diverging from external validation.\n- **Do RL training** when: fresh diverse data has been generated, entropy is healthy, and pass@k_large shows room for improvement (frontier has expanded but pass@1 efficiency lags behind).\n- **Stop / checkpoint** when: Cover@tau is approaching verifier ceiling (per the model collapse verification paper), or reward hacking is detected.\n\n**Key risks your system must address:**\n- Model collapse from recursive self-training (Shumailov et al.) -- mitigated by external verification and diversity diagnostics\n- Reward hacking from prolonged self-rewarding (SRT paper) -- mitigated by external validation checks\n- Pass@k optimization degrading pass@1 (the exploration-exploitation tension) -- mitigated by adaptive scheduling\n\nSources:\n- [Pass@k Training for Adaptively Balancing Exploration and Exploitation](https://arxiv.org/abs/2508.10751)\n- [Does RL Really Incentivize Reasoning Beyond the Base Model?](https://arxiv.org/abs/2504.13837)\n- [Beyond Pass@k: Breadth-Depth Metrics for Reasoning Boundaries](https://arxiv.org/abs/2510.08325)\n- [Beyond Pass@1: Self-Play with Variational Problem Synthesis (SvS)](https://arxiv.org/abs/2508.14029)\n- [EntroPIC: Entropy Stabilization with PI Control](https://arxiv.org/abs/2511.15248)\n- [Entrocraft: Precise Entropy Curve Control](https://arxiv.org/abs/2604.26326)\n- [Revisiting Entropy in RL for Large Reasoning Models](https://arxiv.org/abs/2511.05993)\n- [The Entropy Mechanism of RL for Reasoning LMs](https://arxiv.org/abs/2505.22617)\n- [Rethinking Entropy Regularization in Large Reasoning Models](https://arxiv.org/abs/2509.25133)\n- [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465)\n- [Quiet-STaR: Language Models Can Teach Themselves to Think](https://arxiv.org/abs/2403.09629)\n- [Think, Prune, Train, Improve](https://arxiv.org/abs/2504.18116)\n- [RL on Incorrect Synthetic Data Scales Efficiency 8x](https://arxiv.org/abs/2406.14532)\n- [Self-Rewarding Correction for Mathematical Reasoning](https://arxiv.org/abs/2502.19613)\n- [AI Models Collapse When Trained on Recursively Generated Data (Nature)](https://www.nature.com/articles/s41586-024-07566-y)\n- [Strong Model Collapse (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)\n- [Escaping Model Collapse via Synthetic Data Verification](https://arxiv.org/abs/2510.16657)\n- [Collapse or Thrive? Perils and Promises of Synthetic Data](https://arxiv.org/abs/2410.16713)\n- [DART-Math: Difficulty-Aware Rejection Tuning](https://arxiv.org/abs/2407.13690)\n- [Self-Evolving Curriculum for LLM Reasoning (SEC)](https://arxiv.org/abs/2505.14970)\n- [MathMixup: Difficulty-Controllable Synthesis + Curriculum](https://arxiv.org/abs/2601.17006)\n- [MathSmith: Forging Synthetic Problems with RL](https://arxiv.org/abs/2508.05592)\n- [Self-Rewarding Language Models (Meta)](https://arxiv.org/abs/2401.10020)\n- [Meta-Rewarding Language Models: LLM-as-a-Meta-Judge](https://arxiv.org/abs/2407.19594)\n- [Process-based Self-Rewarding Language Models (ACL 2025)](https://arxiv.org/abs/2503.03746)\n- [Can Large Reasoning Models Self-Train? (SRT)](https://arxiv.org/abs/2505.21444)\n- [ETTRL: Balancing Exploration and Exploitation via Entropy](https://arxiv.org/abs/2508.11356)\n- [rStar-Math: Self-Evolved Deep Thinking (ICML 2025)](https://arxiv.org/abs/2501.04519)"
      }
    ],
    "totalDurationMs": 196863,
    "totalTokens": 39742,
    "totalToolUseCount": 30,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3481,
      "cache_read_input_tokens": 31030,
      "output_tokens": 5230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3481
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5230,
          "cache_read_input_tokens": 31030,
          "cache_creation_input_tokens": 3481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3481,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 30
    }
  },
  "sourceToolAssistantUUID": "1b59a567-4e95-49b3-ba5c-0d64e8e3ad6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"FrontierCycle: Diagnostic-Guided Iterative RL↔Distillation Scheduling…",
  "leafUuid": "f1894205-f10e-49ae-b504-c7b2b92b8a17",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise self-improvement framework for iterative LLM reasoning cycles",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---

### Tool result

_source line 19 · 2026-05-27T20:34:52.004Z_

<details><summary>↩ Tool result · `toolu_01JBPRGgTeALppA8ePmq6tVM`</summary>

```text
Now I have enough material for a comprehensive report. Let me compile everything into a thorough landscape review.

---

Here is a comprehensive landscape review of self-improvement methods for mathematical reasoning training, organized by theme, with 25+ relevant papers identified.

---

## 1. FOUNDATIONAL WORKS

### 1.1 STaR: Self-Taught Reasoner Bootstrapping Reasoning With Reasoning
- **arXiv:** 2203.14465 | **Date:** March 2022 | **Authors:** Zelikman et al.
- **Key findings:** The original STaR paper. The model iteratively generates chain-of-thought rationales, filters for correct answers, and fine-tunes on successful rationales. Includes "rationalization" -- when the model fails, the correct answer is provided as a hint to generate a rationale, which is then added to training data. Demonstrated improvements on GSM8K and CommonsenseQA.
- **Relevance:** The foundational self-improvement loop for math reasoning -- generate, filter, retrain.

### 1.2 Large Language Models Can Self-Improve
- **arXiv:** 2210.11610 | **Date:** October 2022 | **Authors:** Huang et al. (Google)
- **Key findings:** Showed that a 540B PaLM model can self-improve using only unlabeled data. Uses CoT prompting + self-consistency (majority voting) to generate high-confidence answers, then fine-tunes on those. GSM8K improved from 74.4% to 82.1% without any ground truth labels.
- **Relevance:** Seminal demonstration that self-improvement without external supervision is possible for math.

### 1.3 Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models (ReST-EM)
- **arXiv:** 2312.06585 | **Date:** December 2023 | **Authors:** Singh et al. (Google DeepMind)
- **Key findings:** Formalized self-training as an Expectation-Maximization procedure (ReST^EM). Generate samples, filter using binary feedback (correct/incorrect), fine-tune, repeat. On MATH and APPS benchmarks with PaLM-2, model-generated synthetic data yielded larger gains than human-written data. Diminishing returns after ~2 iterations indicating potential overfitting.
- **Relevance:** The key ReST paper for math. Shows self-training scales favorably with model size and surpasses human data fine-tuning.

---

## 2. STaR VARIANTS AND EXTENSIONS

### 2.1 V-STaR: Training Verifiers for Self-Taught Reasoners
- **arXiv:** 2402.06457 | **Date:** February 2024 | **Authors:** Hosseini et al.
- **Key findings:** Uses BOTH correct and incorrect solutions from the self-improvement loop to train a DPO-based verifier. At inference, the verifier selects among candidate solutions. Achieves 6-17% absolute improvement over prior self-improvement methods on math reasoning. 7B V-STaR surpasses LLaMA2 70B on GSM8K.
- **Relevance:** Critical insight that failed generations are also valuable training signal for a verifier component.

### 2.2 Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking
- **arXiv:** 2403.09629 | **Date:** March 2024 | **Authors:** Zelikman, Harik et al.
- **Key findings:** Generalizes STaR so the model generates internal "thinking tokens" before each output token, trained via REINFORCE on whether the hidden reasoning improves next-token prediction. Improved GSM8K zero-shot from 5.9% to 10.9%. First work training LLMs to reason generally from unstructured text rather than curated tasks.
- **Relevance:** Extends self-improvement from task-specific to general reasoning via implicit rationale generation.

### 2.3 HS-STaR: Hierarchical Sampling for Self-Taught Reasoners
- **arXiv:** 2505.19866 | **Date:** May 2025 | **Authors:** Xiong et al. | **Venue:** EMNLP 2025
- **Key findings:** Not all training examples contribute equally. Problems near the boundary of the model's capability offer the greatest learning utility. Uses pre-sampling with difficulty estimation to identify "boundary-level" problems, then reallocates sampling budget toward them. Outperforms baselines without additional compute.
- **Relevance:** Directly addresses the efficiency of the STaR self-improvement loop by intelligent data selection.

### 2.4 B-STaR: Balanced Self-Training Reasoner
- **Key findings:** Uses calibration to maximize a "Balance Score" that sustains both exploration and exploitation across iterations. Prevents the collapse observed in vanilla STaR. Boosts final accuracy across math reasoning benchmarks.
- **Relevance:** Addresses the critical collapse problem in iterative self-training.

---

## 3. SELF-PLAY METHODS

### 3.1 Absolute Zero: Reinforced Self-play Reasoning with Zero Data
- **arXiv:** 2505.03335 | **Date:** May 2025 | **Authors:** Zhao et al. (Tsinghua/LeapLab)
- **Key findings:** A single model plays dual roles: proposer (generates tasks) and solver (solves them), using a code executor as the sole source of verifiable reward. Achieves SOTA on coding and math reasoning without ANY external data -- outperforming models trained on tens of thousands of human-curated examples.
- **Relevance:** The purest form of self-improvement -- no external data at all. Demonstrates that self-play alone can bootstrap strong math reasoning.

### 3.2 R-Zero: Self-Evolving Reasoning LLM from Zero Data
- **arXiv:** 2508.05004 | **Date:** August 2025 | **Authors:** Huang et al.
- **Key findings:** A Challenger-Solver co-evolutionary framework. The Challenger generates problems targeting the Solver's weaknesses; the Solver trains on them using GRPO with majority-vote pseudo-labels. Qwen3-4B-Base improved by +6.49 points on math benchmarks after 3 iterations. Reasoning skills transfer to general-domain tasks.
- **Relevance:** Self-play with distinct proposer/solver roles and iterative co-evolution.

### 3.3 R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training
- **arXiv:** 2602.13103 | **Date:** February 2026 | **Authors:** Li et al.
- **Key findings:** Identifies "Diversity Illusion" -- self-play training signals appear diverse but collapse into recurring patterns. Two failure modes: Local Diversity Illusion (cross-iteration mode cycling) and Surface Diversity Illusion (superficially varied questions requiring identical reasoning). Proposes Memory-Augmented Penalty (MAP) and Skill-Aware Measurement (SAM). Sustains gains across 10 benchmarks.
- **Relevance:** Directly addresses WHY self-play fails and provides concrete solutions.

### 3.4 Towards Understanding Self-play for LLM Reasoning
- **arXiv:** 2510.27072 | **Date:** October 2025 | **Authors:** Chae et al. | **Venue:** NeurIPS 2025
- **Key findings:** Analyzes self-play training dynamics (via the Absolute Zero framework) compared to RLVR and SFT. Finds that (1) self-play reasoning capacity is bounded by the base model, (2) the proposer is the critical component driving improvement, and (3) self-play still undergoes entropy collapse.
- **Relevance:** Provides crucial understanding of mechanisms and limitations of self-play for math reasoning.

### 3.5 STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving
- **arXiv:** 2502.00212 | **Date:** February 2025 | **Venue:** ICML 2025
- **Key findings:** Self-play for formal theorem proving. Model simultaneously conjectures new statements and proves them. The conjecturer is trained on "barely provable" conjectures. Achieves SOTA on miniF2F and ProofNet for whole-proof generation methods.
- **Relevance:** Self-play applied to formal mathematical reasoning with verifiable proofs.

### 3.6 SPIN: Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models
- **arXiv:** 2401.01335 | **Date:** January 2024 | **Authors:** Chen et al. (UCLA)
- **Key findings:** LLM plays against previous iterations of itself, distinguishing self-generated responses from human data via a minimax game. Improves GSM8K from 26.76% to 38.97%. Outperforms DPO supplemented with GPT-4 preference data.
- **Relevance:** Self-play fine-tuning as a general paradigm for model improvement including math.

---

## 4. REINFORCEMENT LEARNING AND REWARD-BASED APPROACHES

### 4.1 DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **arXiv:** 2501.12948 | **Date:** January 2025 | **Authors:** DeepSeek AI
- **Key findings:** Pure RL applied directly to a base model using GRPO, without any supervised fine-tuning. Emergent behaviors include self-reflection, verification, and dynamic strategy adaptation. AIME 2024 performance: 15.6% to 71.0%. Achieves performance on par with OpenAI-o1 on math/code/STEM.
- **Relevance:** Landmark demonstration that pure self-improvement via RL with verifiable rewards can produce SOTA reasoning.

### 4.2 ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search
- **arXiv:** 2406.03816 | **Date:** June 2024 | **Authors:** Zhang et al.
- **Key findings:** Combines MCTS tree search with process reward models for self-training. Uses tree search to infer per-step process rewards from final answer correctness (avoiding manual step annotation). Trains both policy and reward models on collected traces. Outperforms Self-Consistency and Best-of-N with the same compute budget.
- **Relevance:** Process-level self-training that bootstraps its own step-level reward signal.

### 4.3 Learning to Reason without External Rewards (Intuitor/RLIF)
- **arXiv:** 2505.19590 | **Date:** May 2025
- **Key findings:** Introduces Reinforcement Learning from Internal Feedback (RLIF). Uses the model's own confidence (self-certainty, measured via KL divergence from uniform distribution) as the sole reward signal. Matches GRPO performance on math benchmarks while achieving superior OOD generalization to code, all without gold solutions.
- **Relevance:** Eliminates the need for ANY external reward signal -- the model improves purely from its own confidence estimates.

### 4.4 Self-Rewarding Language Models / Meta-Rewarding Language Models
- **arXiv:** 2401.10020 (Self-Rewarding, Jan 2024) / 2407.19594 (Meta-Rewarding, Jul 2024)
- **Key findings:** The model serves as both generator and judge (LLM-as-a-Judge). Meta-Rewarding adds a meta-judge layer where the model judges its own judgments. Improved Llama-3-8B-Instruct from 22.9% to 39.4% on AlpacaEval 2.
- **Relevance:** Self-improvement through self-evaluation without external reward models.

---

## 5. SYNTHETIC DATA GENERATION

### 5.1 MathSmith: Towards Extremely Hard Mathematical Reasoning by Forging Synthetic Problems
- **arXiv:** 2508.05592 | **Date:** August 2025
- **Key findings:** Generates math problems from randomly sampled concept-explanation pairs (bypassing existing problems entirely). Uses structural, complexity, and consistency-aware rewards via RL to create high-quality, verifiable problems. Uses reasoning trace length as a proxy for cognitive complexity. Consistently outperforms baselines on GSM8K, MATH-500, AIME2024/25, and OlympiadBench.
- **Relevance:** RL-optimized synthetic math problem generation that directly feeds self-training.

### 5.2 MARGE: Improving Math Reasoning with Guided Exploration
- **arXiv:** 2505.12500 | **Date:** May 2025 | **Venue:** ICML 2025
- **Key findings:** Systematically explores intermediate reasoning states from self-generated solutions. By completing partial solutions from different intermediate states, obtains a larger training set with lower spurious correlations. Improves both single-shot accuracy and exploration diversity.
- **Relevance:** Addresses the quality problem in self-generated data by guided exploration of reasoning paths.

### 5.3 Self-Explore: Enhancing Mathematical Reasoning with Fine-grained Rewards
- **arXiv:** 2404.10346 | **Date:** April 2024 | **Venue:** EMNLP Findings 2024
- **Key findings:** The LLM explores its own rationales to find the "first wrong step," then uses step-level DPO to increase probability of correct reasoning and decrease probability of incorrect steps. Achieves 11.57% improvement on GSM8K and 2.89% on MATH across 3 LLMs without distillation from proprietary models.
- **Relevance:** Self-generated fine-grained reward signals for math reasoning improvement.

---

## 6. WHEN/WHY SELF-IMPROVEMENT WORKS VS. FAILS

### 6.1 Can Large Reasoning Models Self-Train? (SRT)
- **arXiv:** 2505.21444 | **Date:** May 2025 | **Authors:** Shafayat, Tajwar et al. (CMU)
- **Key findings:** Studies self-training using majority voting as self-feedback. Positive: improves reasoning AND quality of self-feedback across iterations. Negative: prolonged RL leads to reward hacking and sudden complete performance collapse. Self-improvement works under controllable difficulty but fails on real-world math due to reward hacking.
- **Relevance:** Critical evidence on both the promise and the failure modes of self-training.

### 6.2 Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models
- **arXiv:** 2412.02674 | **Date:** December 2024 | **Venue:** ICLR 2025
- **Key findings:** Formalizes self-improvement mathematically via the "generation-verification gap" -- the difference between a model's ability to generate vs. verify solutions. Discovers a scaling law: this gap scales monotonically with pre-training compute. Larger models have larger gaps, enabling more effective self-improvement.
- **Relevance:** Provides the theoretical foundation for WHEN self-improvement is possible.

### 6.3 Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap
- **arXiv:** 2507.00075 | **Date:** July 2025
- **Key findings:** Models self-improvement dynamics as an exponential curve toward a limit determined by the solver-verifier gap. Validates experimentally across multiple models and datasets. Shows that external data can be introduced at any stage without significantly affecting final performance.
- **Relevance:** Provides predictive theory for self-improvement trajectories and limits.

### 6.4 Limits of Generalization in RLVR: Two Case Studies in Mathematical Reasoning
- **arXiv:** 2510.27044 | **Date:** October 2025
- **Key findings:** On carefully controlled combinatorial problems, RLVR improves metrics but often by reinforcing superficial heuristics rather than acquiring genuine new reasoning strategies. Emphasizes the importance of benchmarks that disentangle real reasoning from shortcut exploitation.
- **Relevance:** Important caution -- self-improvement may be "Goodharting" on metrics without true reasoning gains.

### 6.5 Rethinking Chain-of-Thought from the Perspective of Self-Training
- **arXiv:** 2412.10827 | **Date:** December 2024
- **Key findings:** Shows that CoT reasoning and self-training share a core objective of entropy minimization. Proposes a unified framework addressing over-reasoning and high similarity between consecutive reasoning iterations.
- **Relevance:** Theoretical unification of CoT and self-training paradigms.

---

## 7. EFFICIENCY AND PRACTICAL IMPROVEMENTS

### 7.1 Better, Faster: Harnessing Self-Improvement in Large Reasoning Models (HSIR)
- **arXiv:** 2605.24998 | **Date:** May 2026
- **Key findings:** Identifies two key problems in self-improvement: data imbalance (most samples are easy) and overthinking (redundant reasoning steps). Proposes verify-then-exit sampling and an Intrinsic Diversity score. Achieves up to +10.9% performance gains while reducing 42.4% inference overhead.
- **Relevance:** Very recent work making self-improvement more practical and efficient.

### 7.2 Self-Training Elicits Concise Reasoning in Large Language Models
- **arXiv:** 2502.20122 | **Date:** February 2025 | **Venue:** ACL 2025 Findings
- **Key findings:** LLMs have a latent ability to reason more concisely. Simple self-training using best-of-N sampling and few-shot conditioning reduces output tokens by 30% on GSM8K and MATH while maintaining accuracy across 5 model families.
- **Relevance:** Self-improvement for reasoning efficiency, not just accuracy.

---

## 8. WEAK-TO-STRONG AND SCALABLE OVERSIGHT

### 8.1 Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision (OpenAI)
- **Source:** OpenAI technical report | **Date:** 2023
- **Key findings:** Foundational study showing that strong models supervised by weaker models can generalize beyond the weak supervisor's capabilities. Two mechanisms: pseudolabel correction and coverage expansion.
- **Relevance:** Theoretical basis for how self-improvement can exceed the supervisor's level.

### 8.2 Debate Helps Weak-to-Strong Generalization
- **arXiv:** 2501.13124 | **Date:** January 2025 | **Venue:** AAAI 2025
- **Key findings:** Debate between models helps a weak supervisor extract trustworthy information from a strong but potentially untrustworthy model. Combines scalable oversight with weak-to-strong generalization for better alignment.
- **Relevance:** Mechanism for bootstrapping self-improvement through inter-model debate.

---

## 9. SURVEYS

### 9.1 Self-Improvement of Large Language Models: A Technical Overview and Future Outlook
- **arXiv:** 2603.25681 | **Date:** March 2026
- **Relevance:** The most recent comprehensive survey. Covers the GRO (Generation-Reward-Optimization) framework as the unifying paradigm.

### 9.2 A Survey on Large Language Models for Mathematical Reasoning
- **arXiv:** 2506.08446 | **Date:** June 2025
- **Relevance:** Broad survey covering prompting, SFT, RL, and test-time scaling for math reasoning.

---

## KEY TAKEAWAYS FOR YOUR PROPOSAL

1. **The generation-verification gap is the theoretical engine**: Self-improvement works when models are better at verifying than generating (Mind the Gap, ICLR 2025). This gap scales with pre-training compute.

2. **Pure self-play from zero data is now feasible**: Absolute Zero and R-Zero show that models can bootstrap math reasoning without any external data, using self-proposed problems.

3. **Collapse is the central failure mode**: Vanilla iterative self-training leads to mode collapse, reward hacking, or diversity illusion. Solutions include balanced exploration (B-STaR), diversity-aware training (R-Diverse), and difficulty-aware sampling (HS-STaR).

4. **Process rewards beat outcome rewards**: ReST-MCTS* and MARGE show that self-training with step-level feedback produces higher-quality data than filtering only on final answers.

5. **DeepSeek-R1 is the industrial proof point**: Pure RL with verifiable rewards, no supervised fine-tuning, achieved competition-level math reasoning.

6. **Synthetic problem generation is its own research frontier**: MathSmith uses RL to optimize problem difficulty and quality, producing harder-than-human training problems.

7. **Critical caution**: RLVR may reinforce heuristics rather than genuine reasoning (Limits of Generalization). Prolonged self-training leads to reward hacking (SRT/Can Large Reasoning Models Self-Train?).

---

Sources:
- [STaR: Self-Taught Reasoner](https://ar5iv.labs.arxiv.org/html/2203.14465)
- [Large Language Models Can Self-Improve](https://arxiv.org/abs/2210.11610)
- [Beyond Human Data / ReST-EM](https://arxiv.org/abs/2312.06585)
- [V-STaR: Training Verifiers for Self-Taught Reasoners](https://arxiv.org/abs/2402.06457)
- [Quiet-STaR](https://arxiv.org/abs/2403.09629)
- [HS-STaR: Hierarchical Sampling](https://arxiv.org/abs/2505.19866)
- [Absolute Zero Reasoner](https://arxiv.org/abs/2505.03335)
- [R-Zero: Self-Evolving Reasoning LLM](https://arxiv.org/html/2508.05004v1)
- [R-Diverse: Mitigating Diversity Illusion](https://arxiv.org/abs/2602.13103)
- [Towards Understanding Self-play for LLM Reasoning](https://arxiv.org/abs/2510.27072)
- [STP: Self-play Theorem Provers](https://arxiv.org/abs/2502.00212)
- [SPIN: Self-Play Fine-Tuning](https://arxiv.org/abs/2401.01335)
- [DeepSeek-R1](https://arxiv.org/abs/2501.12948)
- [ReST-MCTS*](https://arxiv.org/abs/2406.03816)
- [Learning to Reason without External Rewards / Intuitor](https://arxiv.org/abs/2505.19590)
- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020)
- [Meta-Rewarding Language Models](https://arxiv.org/abs/2407.19594)
- [MathSmith](https://arxiv.org/abs/2508.05592)
- [MARGE: Guided Exploration](https://arxiv.org/abs/2505.12500)
- [Self-Explore: Fine-grained Rewards](https://arxiv.org/abs/2404.10346)
- [Can Large Reasoning Models Self-Train? (SRT)](https://arxiv.org/abs/2505.21444)
- [Mind the Gap](https://arxiv.org/abs/2412.02674)
- [Theoretical Modeling via Solver-Verifier Gap](https://arxiv.org/abs/2507.00075)
- [Limits of Generalization in RLVR](https://arxiv.org/abs/2510.27044)
- [Rethinking CoT from Self-Training Perspective](https://arxiv.org/abs/2412.10827)
- [Better, Faster: HSIR](https://arxiv.org/abs/2605.24998)
- [Self-Training Elicits Concise Reasoning](https://arxiv.org/abs/2502.20122)
- [Weak-to-Strong Generalization (OpenAI)](https://cdn.openai.com/papers/weak-to-strong-generalization.pdf)
- [Debate Helps Weak-to-Strong Generalization](https://arxiv.org/abs/2501.13124)
- [Self-Improvement Survey 2026](https://arxiv.org/abs/2603.25681)
- [Math Reasoning Survey](https://arxiv.org/abs/2506.08446)
- [Dual-Phase Self-Evolved Mathematical Frameworks](https://arxiv.org/abs/2601.05616)
- [ReST-RL](https://arxiv.org/abs/2508.19576)
- [Self-Improvement LLM Repository](https://github.com/Zesearch/self-improvement-llm)
- [Emergent Mind: STaR Topics](https://www.emergentmind.com/topics/self-taught-reasoners-star)
- [Emergent Mind: RLVR Topics](https://www.emergentmind.com/topics/reinforcement-learning-from-verifiable-rewards-rlvr)

agentId: a0ab169fb1c5dfad1 (use SendMessage with to: 'a0ab169fb1c5dfad1' to continue this agent)
&lt;usage>total_tokens: 48788
tool_uses: 39
duration_ms: 506979&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9dae3930-abfd-48dc-99fd-16828545c9d7",
  "isSidechain": false,
  "promptId": "a6903394-624e-4492-ad19-36a9e5620d23",
  "type": "user",
  "uuid": "b7b88d9b-7eda-4011-9466-3aa11a73a043",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm pivoting a research proposal to focus on \"Synthetic Data and Self-Improvement for Mathematical Reasoning Training.\" I need to understand the current landscape of self-improvement methods (where the model improves using its own capabilities, NOT from an external teacher).\n\nPlease search the web thoroughly for:\n\n1. STaR (Self-Taught Reasoner) and its variants — especially recent 2025-2026 extensions\n2. ReST (Reinforced Self-Training) and REST-EM for math reasoning\n3. Self-play methods for LLM reasoning improvement\n4. Iterative self-training / self-improvement loops for math\n5. Synthetic data generation by the model itself for math training\n6. Any 2025-2026 papers on \"self-improvement\" + \"mathematical reasoning\"\n7. Papers on when/why self-improvement works vs. fails (collapse, mode collapse, etc.)\n8. \"Scalable Oversight\" or \"Weak-to-Strong\" approaches for self-improvement\n\nSearch queries to try:\n- \"self-improvement mathematical reasoning LLM 2025 2026\"\n- \"STaR self-taught reasoner iterative self-training math\"  \n- \"synthetic data self-generated math reasoning training\"\n- \"self-play LLM reasoning improvement\"\n- \"iterative self-training collapse LLM reasoning\"\n\nFor each major paper found, provide: title, arxiv ID, date, key findings, and how it relates to self-improvement for math reasoning. I need at least 15-20 relevant papers.",
    "agentId": "a0ab169fb1c5dfad1",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough material for a comprehensive report. Let me compile everything into a thorough landscape review.\n\n---\n\nHere is a comprehensive landscape review of self-improvement methods for mathematical reasoning training, organized by theme, with 25+ relevant papers identified.\n\n---\n\n## 1. FOUNDATIONAL WORKS\n\n### 1.1 STaR: Self-Taught Reasoner Bootstrapping Reasoning With Reasoning\n- **arXiv:** 2203.14465 | **Date:** March 2022 | **Authors:** Zelikman et al.\n- **Key findings:** The original STaR paper. The model iteratively generates chain-of-thought rationales, filters for correct answers, and fine-tunes on successful rationales. Includes \"rationalization\" -- when the model fails, the correct answer is provided as a hint to generate a rationale, which is then added to training data. Demonstrated improvements on GSM8K and CommonsenseQA.\n- **Relevance:** The foundational self-improvement loop for math reasoning -- generate, filter, retrain.\n\n### 1.2 Large Language Models Can Self-Improve\n- **arXiv:** 2210.11610 | **Date:** October 2022 | **Authors:** Huang et al. (Google)\n- **Key findings:** Showed that a 540B PaLM model can self-improve using only unlabeled data. Uses CoT prompting + self-consistency (majority voting) to generate high-confidence answers, then fine-tunes on those. GSM8K improved from 74.4% to 82.1% without any ground truth labels.\n- **Relevance:** Seminal demonstration that self-improvement without external supervision is possible for math.\n\n### 1.3 Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models (ReST-EM)\n- **arXiv:** 2312.06585 | **Date:** December 2023 | **Authors:** Singh et al. (Google DeepMind)\n- **Key findings:** Formalized self-training as an Expectation-Maximization procedure (ReST^EM). Generate samples, filter using binary feedback (correct/incorrect), fine-tune, repeat. On MATH and APPS benchmarks with PaLM-2, model-generated synthetic data yielded larger gains than human-written data. Diminishing returns after ~2 iterations indicating potential overfitting.\n- **Relevance:** The key ReST paper for math. Shows self-training scales favorably with model size and surpasses human data fine-tuning.\n\n---\n\n## 2. STaR VARIANTS AND EXTENSIONS\n\n### 2.1 V-STaR: Training Verifiers for Self-Taught Reasoners\n- **arXiv:** 2402.06457 | **Date:** February 2024 | **Authors:** Hosseini et al.\n- **Key findings:** Uses BOTH correct and incorrect solutions from the self-improvement loop to train a DPO-based verifier. At inference, the verifier selects among candidate solutions. Achieves 6-17% absolute improvement over prior self-improvement methods on math reasoning. 7B V-STaR surpasses LLaMA2 70B on GSM8K.\n- **Relevance:** Critical insight that failed generations are also valuable training signal for a verifier component.\n\n### 2.2 Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking\n- **arXiv:** 2403.09629 | **Date:** March 2024 | **Authors:** Zelikman, Harik et al.\n- **Key findings:** Generalizes STaR so the model generates internal \"thinking tokens\" before each output token, trained via REINFORCE on whether the hidden reasoning improves next-token prediction. Improved GSM8K zero-shot from 5.9% to 10.9%. First work training LLMs to reason generally from unstructured text rather than curated tasks.\n- **Relevance:** Extends self-improvement from task-specific to general reasoning via implicit rationale generation.\n\n### 2.3 HS-STaR: Hierarchical Sampling for Self-Taught Reasoners\n- **arXiv:** 2505.19866 | **Date:** May 2025 | **Authors:** Xiong et al. | **Venue:** EMNLP 2025\n- **Key findings:** Not all training examples contribute equally. Problems near the boundary of the model's capability offer the greatest learning utility. Uses pre-sampling with difficulty estimation to identify \"boundary-level\" problems, then reallocates sampling budget toward them. Outperforms baselines without additional compute.\n- **Relevance:** Directly addresses the efficiency of the STaR self-improvement loop by intelligent data selection.\n\n### 2.4 B-STaR: Balanced Self-Training Reasoner\n- **Key findings:** Uses calibration to maximize a \"Balance Score\" that sustains both exploration and exploitation across iterations. Prevents the collapse observed in vanilla STaR. Boosts final accuracy across math reasoning benchmarks.\n- **Relevance:** Addresses the critical collapse problem in iterative self-training.\n\n---\n\n## 3. SELF-PLAY METHODS\n\n### 3.1 Absolute Zero: Reinforced Self-play Reasoning with Zero Data\n- **arXiv:** 2505.03335 | **Date:** May 2025 | **Authors:** Zhao et al. (Tsinghua/LeapLab)\n- **Key findings:** A single model plays dual roles: proposer (generates tasks) and solver (solves them), using a code executor as the sole source of verifiable reward. Achieves SOTA on coding and math reasoning without ANY external data -- outperforming models trained on tens of thousands of human-curated examples.\n- **Relevance:** The purest form of self-improvement -- no external data at all. Demonstrates that self-play alone can bootstrap strong math reasoning.\n\n### 3.2 R-Zero: Self-Evolving Reasoning LLM from Zero Data\n- **arXiv:** 2508.05004 | **Date:** August 2025 | **Authors:** Huang et al.\n- **Key findings:** A Challenger-Solver co-evolutionary framework. The Challenger generates problems targeting the Solver's weaknesses; the Solver trains on them using GRPO with majority-vote pseudo-labels. Qwen3-4B-Base improved by +6.49 points on math benchmarks after 3 iterations. Reasoning skills transfer to general-domain tasks.\n- **Relevance:** Self-play with distinct proposer/solver roles and iterative co-evolution.\n\n### 3.3 R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training\n- **arXiv:** 2602.13103 | **Date:** February 2026 | **Authors:** Li et al.\n- **Key findings:** Identifies \"Diversity Illusion\" -- self-play training signals appear diverse but collapse into recurring patterns. Two failure modes: Local Diversity Illusion (cross-iteration mode cycling) and Surface Diversity Illusion (superficially varied questions requiring identical reasoning). Proposes Memory-Augmented Penalty (MAP) and Skill-Aware Measurement (SAM). Sustains gains across 10 benchmarks.\n- **Relevance:** Directly addresses WHY self-play fails and provides concrete solutions.\n\n### 3.4 Towards Understanding Self-play for LLM Reasoning\n- **arXiv:** 2510.27072 | **Date:** October 2025 | **Authors:** Chae et al. | **Venue:** NeurIPS 2025\n- **Key findings:** Analyzes self-play training dynamics (via the Absolute Zero framework) compared to RLVR and SFT. Finds that (1) self-play reasoning capacity is bounded by the base model, (2) the proposer is the critical component driving improvement, and (3) self-play still undergoes entropy collapse.\n- **Relevance:** Provides crucial understanding of mechanisms and limitations of self-play for math reasoning.\n\n### 3.5 STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving\n- **arXiv:** 2502.00212 | **Date:** February 2025 | **Venue:** ICML 2025\n- **Key findings:** Self-play for formal theorem proving. Model simultaneously conjectures new statements and proves them. The conjecturer is trained on \"barely provable\" conjectures. Achieves SOTA on miniF2F and ProofNet for whole-proof generation methods.\n- **Relevance:** Self-play applied to formal mathematical reasoning with verifiable proofs.\n\n### 3.6 SPIN: Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models\n- **arXiv:** 2401.01335 | **Date:** January 2024 | **Authors:** Chen et al. (UCLA)\n- **Key findings:** LLM plays against previous iterations of itself, distinguishing self-generated responses from human data via a minimax game. Improves GSM8K from 26.76% to 38.97%. Outperforms DPO supplemented with GPT-4 preference data.\n- **Relevance:** Self-play fine-tuning as a general paradigm for model improvement including math.\n\n---\n\n## 4. REINFORCEMENT LEARNING AND REWARD-BASED APPROACHES\n\n### 4.1 DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\n- **arXiv:** 2501.12948 | **Date:** January 2025 | **Authors:** DeepSeek AI\n- **Key findings:** Pure RL applied directly to a base model using GRPO, without any supervised fine-tuning. Emergent behaviors include self-reflection, verification, and dynamic strategy adaptation. AIME 2024 performance: 15.6% to 71.0%. Achieves performance on par with OpenAI-o1 on math/code/STEM.\n- **Relevance:** Landmark demonstration that pure self-improvement via RL with verifiable rewards can produce SOTA reasoning.\n\n### 4.2 ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search\n- **arXiv:** 2406.03816 | **Date:** June 2024 | **Authors:** Zhang et al.\n- **Key findings:** Combines MCTS tree search with process reward models for self-training. Uses tree search to infer per-step process rewards from final answer correctness (avoiding manual step annotation). Trains both policy and reward models on collected traces. Outperforms Self-Consistency and Best-of-N with the same compute budget.\n- **Relevance:** Process-level self-training that bootstraps its own step-level reward signal.\n\n### 4.3 Learning to Reason without External Rewards (Intuitor/RLIF)\n- **arXiv:** 2505.19590 | **Date:** May 2025\n- **Key findings:** Introduces Reinforcement Learning from Internal Feedback (RLIF). Uses the model's own confidence (self-certainty, measured via KL divergence from uniform distribution) as the sole reward signal. Matches GRPO performance on math benchmarks while achieving superior OOD generalization to code, all without gold solutions.\n- **Relevance:** Eliminates the need for ANY external reward signal -- the model improves purely from its own confidence estimates.\n\n### 4.4 Self-Rewarding Language Models / Meta-Rewarding Language Models\n- **arXiv:** 2401.10020 (Self-Rewarding, Jan 2024) / 2407.19594 (Meta-Rewarding, Jul 2024)\n- **Key findings:** The model serves as both generator and judge (LLM-as-a-Judge). Meta-Rewarding adds a meta-judge layer where the model judges its own judgments. Improved Llama-3-8B-Instruct from 22.9% to 39.4% on AlpacaEval 2.\n- **Relevance:** Self-improvement through self-evaluation without external reward models.\n\n---\n\n## 5. SYNTHETIC DATA GENERATION\n\n### 5.1 MathSmith: Towards Extremely Hard Mathematical Reasoning by Forging Synthetic Problems\n- **arXiv:** 2508.05592 | **Date:** August 2025\n- **Key findings:** Generates math problems from randomly sampled concept-explanation pairs (bypassing existing problems entirely). Uses structural, complexity, and consistency-aware rewards via RL to create high-quality, verifiable problems. Uses reasoning trace length as a proxy for cognitive complexity. Consistently outperforms baselines on GSM8K, MATH-500, AIME2024/25, and OlympiadBench.\n- **Relevance:** RL-optimized synthetic math problem generation that directly feeds self-training.\n\n### 5.2 MARGE: Improving Math Reasoning with Guided Exploration\n- **arXiv:** 2505.12500 | **Date:** May 2025 | **Venue:** ICML 2025\n- **Key findings:** Systematically explores intermediate reasoning states from self-generated solutions. By completing partial solutions from different intermediate states, obtains a larger training set with lower spurious correlations. Improves both single-shot accuracy and exploration diversity.\n- **Relevance:** Addresses the quality problem in self-generated data by guided exploration of reasoning paths.\n\n### 5.3 Self-Explore: Enhancing Mathematical Reasoning with Fine-grained Rewards\n- **arXiv:** 2404.10346 | **Date:** April 2024 | **Venue:** EMNLP Findings 2024\n- **Key findings:** The LLM explores its own rationales to find the \"first wrong step,\" then uses step-level DPO to increase probability of correct reasoning and decrease probability of incorrect steps. Achieves 11.57% improvement on GSM8K and 2.89% on MATH across 3 LLMs without distillation from proprietary models.\n- **Relevance:** Self-generated fine-grained reward signals for math reasoning improvement.\n\n---\n\n## 6. WHEN/WHY SELF-IMPROVEMENT WORKS VS. FAILS\n\n### 6.1 Can Large Reasoning Models Self-Train? (SRT)\n- **arXiv:** 2505.21444 | **Date:** May 2025 | **Authors:** Shafayat, Tajwar et al. (CMU)\n- **Key findings:** Studies self-training using majority voting as self-feedback. Positive: improves reasoning AND quality of self-feedback across iterations. Negative: prolonged RL leads to reward hacking and sudden complete performance collapse. Self-improvement works under controllable difficulty but fails on real-world math due to reward hacking.\n- **Relevance:** Critical evidence on both the promise and the failure modes of self-training.\n\n### 6.2 Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models\n- **arXiv:** 2412.02674 | **Date:** December 2024 | **Venue:** ICLR 2025\n- **Key findings:** Formalizes self-improvement mathematically via the \"generation-verification gap\" -- the difference between a model's ability to generate vs. verify solutions. Discovers a scaling law: this gap scales monotonically with pre-training compute. Larger models have larger gaps, enabling more effective self-improvement.\n- **Relevance:** Provides the theoretical foundation for WHEN self-improvement is possible.\n\n### 6.3 Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap\n- **arXiv:** 2507.00075 | **Date:** July 2025\n- **Key findings:** Models self-improvement dynamics as an exponential curve toward a limit determined by the solver-verifier gap. Validates experimentally across multiple models and datasets. Shows that external data can be introduced at any stage without significantly affecting final performance.\n- **Relevance:** Provides predictive theory for self-improvement trajectories and limits.\n\n### 6.4 Limits of Generalization in RLVR: Two Case Studies in Mathematical Reasoning\n- **arXiv:** 2510.27044 | **Date:** October 2025\n- **Key findings:** On carefully controlled combinatorial problems, RLVR improves metrics but often by reinforcing superficial heuristics rather than acquiring genuine new reasoning strategies. Emphasizes the importance of benchmarks that disentangle real reasoning from shortcut exploitation.\n- **Relevance:** Important caution -- self-improvement may be \"Goodharting\" on metrics without true reasoning gains.\n\n### 6.5 Rethinking Chain-of-Thought from the Perspective of Self-Training\n- **arXiv:** 2412.10827 | **Date:** December 2024\n- **Key findings:** Shows that CoT reasoning and self-training share a core objective of entropy minimization. Proposes a unified framework addressing over-reasoning and high similarity between consecutive reasoning iterations.\n- **Relevance:** Theoretical unification of CoT and self-training paradigms.\n\n---\n\n## 7. EFFICIENCY AND PRACTICAL IMPROVEMENTS\n\n### 7.1 Better, Faster: Harnessing Self-Improvement in Large Reasoning Models (HSIR)\n- **arXiv:** 2605.24998 | **Date:** May 2026\n- **Key findings:** Identifies two key problems in self-improvement: data imbalance (most samples are easy) and overthinking (redundant reasoning steps). Proposes verify-then-exit sampling and an Intrinsic Diversity score. Achieves up to +10.9% performance gains while reducing 42.4% inference overhead.\n- **Relevance:** Very recent work making self-improvement more practical and efficient.\n\n### 7.2 Self-Training Elicits Concise Reasoning in Large Language Models\n- **arXiv:** 2502.20122 | **Date:** February 2025 | **Venue:** ACL 2025 Findings\n- **Key findings:** LLMs have a latent ability to reason more concisely. Simple self-training using best-of-N sampling and few-shot conditioning reduces output tokens by 30% on GSM8K and MATH while maintaining accuracy across 5 model families.\n- **Relevance:** Self-improvement for reasoning efficiency, not just accuracy.\n\n---\n\n## 8. WEAK-TO-STRONG AND SCALABLE OVERSIGHT\n\n### 8.1 Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision (OpenAI)\n- **Source:** OpenAI technical report | **Date:** 2023\n- **Key findings:** Foundational study showing that strong models supervised by weaker models can generalize beyond the weak supervisor's capabilities. Two mechanisms: pseudolabel correction and coverage expansion.\n- **Relevance:** Theoretical basis for how self-improvement can exceed the supervisor's level.\n\n### 8.2 Debate Helps Weak-to-Strong Generalization\n- **arXiv:** 2501.13124 | **Date:** January 2025 | **Venue:** AAAI 2025\n- **Key findings:** Debate between models helps a weak supervisor extract trustworthy information from a strong but potentially untrustworthy model. Combines scalable oversight with weak-to-strong generalization for better alignment.\n- **Relevance:** Mechanism for bootstrapping self-improvement through inter-model debate.\n\n---\n\n## 9. SURVEYS\n\n### 9.1 Self-Improvement of Large Language Models: A Technical Overview and Future Outlook\n- **arXiv:** 2603.25681 | **Date:** March 2026\n- **Relevance:** The most recent comprehensive survey. Covers the GRO (Generation-Reward-Optimization) framework as the unifying paradigm.\n\n### 9.2 A Survey on Large Language Models for Mathematical Reasoning\n- **arXiv:** 2506.08446 | **Date:** June 2025\n- **Relevance:** Broad survey covering prompting, SFT, RL, and test-time scaling for math reasoning.\n\n---\n\n## KEY TAKEAWAYS FOR YOUR PROPOSAL\n\n1. **The generation-verification gap is the theoretical engine**: Self-improvement works when models are better at verifying than generating (Mind the Gap, ICLR 2025). This gap scales with pre-training compute.\n\n2. **Pure self-play from zero data is now feasible**: Absolute Zero and R-Zero show that models can bootstrap math reasoning without any external data, using self-proposed problems.\n\n3. **Collapse is the central failure mode**: Vanilla iterative self-training leads to mode collapse, reward hacking, or diversity illusion. Solutions include balanced exploration (B-STaR), diversity-aware training (R-Diverse), and difficulty-aware sampling (HS-STaR).\n\n4. **Process rewards beat outcome rewards**: ReST-MCTS* and MARGE show that self-training with step-level feedback produces higher-quality data than filtering only on final answers.\n\n5. **DeepSeek-R1 is the industrial proof point**: Pure RL with verifiable rewards, no supervised fine-tuning, achieved competition-level math reasoning.\n\n6. **Synthetic problem generation is its own research frontier**: MathSmith uses RL to optimize problem difficulty and quality, producing harder-than-human training problems.\n\n7. **Critical caution**: RLVR may reinforce heuristics rather than genuine reasoning (Limits of Generalization). Prolonged self-training leads to reward hacking (SRT/Can Large Reasoning Models Self-Train?).\n\n---\n\nSources:\n- [STaR: Self-Taught Reasoner](https://ar5iv.labs.arxiv.org/html/2203.14465)\n- [Large Language Models Can Self-Improve](https://arxiv.org/abs/2210.11610)\n- [Beyond Human Data / ReST-EM](https://arxiv.org/abs/2312.06585)\n- [V-STaR: Training Verifiers for Self-Taught Reasoners](https://arxiv.org/abs/2402.06457)\n- [Quiet-STaR](https://arxiv.org/abs/2403.09629)\n- [HS-STaR: Hierarchical Sampling](https://arxiv.org/abs/2505.19866)\n- [Absolute Zero Reasoner](https://arxiv.org/abs/2505.03335)\n- [R-Zero: Self-Evolving Reasoning LLM](https://arxiv.org/html/2508.05004v1)\n- [R-Diverse: Mitigating Diversity Illusion](https://arxiv.org/abs/2602.13103)\n- [Towards Understanding Self-play for LLM Reasoning](https://arxiv.org/abs/2510.27072)\n- [STP: Self-play Theorem Provers](https://arxiv.org/abs/2502.00212)\n- [SPIN: Self-Play Fine-Tuning](https://arxiv.org/abs/2401.01335)\n- [DeepSeek-R1](https://arxiv.org/abs/2501.12948)\n- [ReST-MCTS*](https://arxiv.org/abs/2406.03816)\n- [Learning to Reason without External Rewards / Intuitor](https://arxiv.org/abs/2505.19590)\n- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020)\n- [Meta-Rewarding Language Models](https://arxiv.org/abs/2407.19594)\n- [MathSmith](https://arxiv.org/abs/2508.05592)\n- [MARGE: Guided Exploration](https://arxiv.org/abs/2505.12500)\n- [Self-Explore: Fine-grained Rewards](https://arxiv.org/abs/2404.10346)\n- [Can Large Reasoning Models Self-Train? (SRT)](https://arxiv.org/abs/2505.21444)\n- [Mind the Gap](https://arxiv.org/abs/2412.02674)\n- [Theoretical Modeling via Solver-Verifier Gap](https://arxiv.org/abs/2507.00075)\n- [Limits of Generalization in RLVR](https://arxiv.org/abs/2510.27044)\n- [Rethinking CoT from Self-Training Perspective](https://arxiv.org/abs/2412.10827)\n- [Better, Faster: HSIR](https://arxiv.org/abs/2605.24998)\n- [Self-Training Elicits Concise Reasoning](https://arxiv.org/abs/2502.20122)\n- [Weak-to-Strong Generalization (OpenAI)](https://cdn.openai.com/papers/weak-to-strong-generalization.pdf)\n- [Debate Helps Weak-to-Strong Generalization](https://arxiv.org/abs/2501.13124)\n- [Self-Improvement Survey 2026](https://arxiv.org/abs/2603.25681)\n- [Math Reasoning Survey](https://arxiv.org/abs/2506.08446)\n- [Dual-Phase Self-Evolved Mathematical Frameworks](https://arxiv.org/abs/2601.05616)\n- [ReST-RL](https://arxiv.org/abs/2508.19576)\n- [Self-Improvement LLM Repository](https://github.com/Zesearch/self-improvement-llm)\n- [Emergent Mind: STaR Topics](https://www.emergentmind.com/topics/self-taught-reasoners-star)\n- [Emergent Mind: RLVR Topics](https://www.emergentmind.com/topics/reinforcement-learning-from-verifiable-rewards-rlvr)"
      }
    ],
    "totalDurationMs": 506979,
    "totalTokens": 48788,
    "totalToolUseCount": 39,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 41868,
      "output_tokens": 6202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 717
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6202,
          "cache_read_input_tokens": 41868,
          "cache_creation_input_tokens": 717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 717,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 39
    }
  },
  "sourceToolAssistantUUID": "9dae3930-abfd-48dc-99fd-16828545c9d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"FrontierCycle: Diagnostic-Guided Iterative RL↔Distillation Scheduling…",
  "leafUuid": "b7b88d9b-7eda-4011-9466-3aa11a73a043",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise self-improvement framework for iterative LLM reasoning cycles",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---

### Assistant

_source line 22 · 2026-05-27T20:39:58.623Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent research results! Now I have a comprehensive picture. Let me synthesize the key insights:

**The Pivot Decision**: The reviewer is right — the original FrontierCycle is fundamentally about cross-model distillation scheduling, NOT self-improvement. The user asked for "Synthetic Data and Self-Improvement for Mathematical Reasoning Training." I need to pivot to genuinely address this topic.

**Key Insights from Research:**

1. **Self-improvement landscape is rich**: STaR, ReST-EM, Absolute Zero, R-Zero, self-play, self-rewarding — all are genuine self-improvement methods where the model generates its own training data.


2. **The efficiency-frontier tradeoff**: RLVR can boost pass@1 efficiency but doesn't necessarily expand the model's frontier beyond its base capabilities, so self-generated data only pushes boundaries under specific conditions.
3. **Model collapse is the critical constraint**: Iterative self-training on the model's own outputs causes distribution collapse, though this risk can be managed through external verification, diversity mechanisms, and sampling strategies that account for difficulty.
4. **Verification is the bottleneck**: Self-improvement hinges on models being stronger at verifying solutions than generating them, and this gap determines whether the approach actually works.
5. **I have concrete diagnostic tools**: Pass@k, entropy, Cover@tau, and difficulty-stratified metrics all provide measurable signals for tracking progress.
6. **The missing piece is adaptive scheduling**: Nobody's built a system that uses these diagnostics to dynamically decide when to generate new synthetic data versus when to focus on RL training within the self-improvement loop. The key insight is that current methods like STaR and ReST-EM use fixed iteration schedules, but what if I could make the cycling between generation and training phases responsive to actual performance signals?

The problem is clear: generating too much data wastes compute on redundancy, while over-training causes the model to collapse on its own biases. The optimal ratio shifts as the model improves, so I should use diagnostic signals to adaptively control when to switch phases, what difficulty levels to target, and when to stop before collapse. This directly tackles the intersection of synthetic data, self-improvement loops, and mathematical reasoning that the user is asking about.

Now I need to think through what's genuinely novel here versus existing approaches like STaR, ReST-EM, and Absolute Zero, which all have fixed schedules or limited adaptation mechanisms.

The key innovations are using the pass@k spectrum as a phase-level diagnostic to decide between generation and training, tracking per-difficulty-band performance to guide targeted data synthesis, and detecting collapse early through entropy or other signals.

I'm considering names that capture the diagnostic-guided cycling aspect—something like DiagSTaR or AutoSTaR feels right, though I want to land on one that clearly signals the adaptive scheduling across generation and training phases.

Now I'm thinking through the actual mechanism more carefully. The standard STaR loop generates K solutions per problem, filters for correct ones, then fine-tunes—but this treats every problem uniformly regardless of difficulty, runs for a fixed number of iterations without stopping criteria, and doesn't monitor for collapse risk. What I want instead is a system that dynamically adjusts the sampling budget per problem, determines iteration count adaptively based on performance signals, and tracks diagnostic metrics like self-consistency divergence to catch reward hacking early.

The core loop would be: compute baseline pass@k metrics across difficulty levels, then at each iteration decide whether to expand the frontier by generating targeted synthetic data at the hardest problems, exploit what we've learned through RL on recent data, or inject diversity if collapse is detected. This way the model gets more samples on problems it's struggling with, stops iterating once improvements plateau, and has explicit safeguards against mode collapse. The key distinction is that this approach adaptively switches between self-data-generation and RL-training phases based on frontier diagnostics, with built-in collapse detection—unlike STaR's pure filtering, ReST-EM's fixed scheduling, or Absolute Zero's static iteration structure. For the practical implementation, I'd use a small model like Qwen3-8B with ground-truth answer verification as the reward signal (not an external teacher, just mathematical validation), running diagnostics every 100 training steps on a held-out validation set to guide mode selection. is standard for RLVR.

Let me think about the base model choice. Recent high-performing self-improvement works like DeepSeek-R1, Absolute Zero, and R-Zero show that starting from a strong base model and demonstrating diagnostic-guided self-improvement outperforms fixed-schedule approaches is the way to go.

For baselines, I'd compare STaR with fixed iterations, ReST-EM with a few iterations, pure RLVR, self-play from scratch, and fixed-interval cycling regardless of diagnostics. The key ablations would isolate the diagnostic signal itself, then layer in comparisons across different diagnostic metrics, adaptive versus fixed budgets, targeted versus uniform data generation, collapse prevention mechanisms, and whether adding diversity injection helps.

This feels like a much stronger direction. Now I'm working through potential titles that capture the core idea—something like "FrontierSTaR" or "AdaSTaR" to emphasize the adaptive scheduling aspect, though I want something broader that really highlights the diagnostic-guided iterative self-improvement with adaptive synthetic data generation for math reasoning. I'm cycling through different naming options to capture the core innovation—diagnostic guidance driving iterative self-improvement loops that alternate between synthetic data generation and reinforcement learning. The key is signaling this is a fresh approach rather than just extending prior work, so I want a name that emphasizes the adaptive cycling mechanism and self-generated data rather than relying on existing frameworks like STaR. Let me go with **"FrontierLoop"** — it captures the idea of expanding the reasoning frontier through diagnostic-guided self-improvement loops.

Now I'm pivoting from the original FrontierCycle concept (which focused on cross-model distillation scheduling) to FrontierLoop (self-improvement with adaptive scheduling). The diagnostic framework stays central, but I'm applying it to a completely different problem.

Looking at what's been validated: Pass@k reliably predicts RL outcomes, entropy management is critical for stability, self-improvement works when there's a generation-verification gap, and difficulty-aware data selection improves efficiency. The key gap is that no existing work uses these diagnostics to adaptively schedule the self-improvement loop itself — deciding when to generate new data, what difficulty to target, when to apply RL, and when to stop.

The hypothesis is that diagnostic-guided adaptive scheduling outperforms fixed schedules by targeting frontier problems rather than easy ones, switching to RL when the data pool is sufficiently diverse, detecting collapse before it happens, and dynamically determining iteration count. This is testable and directly addresses the synthetic data and self-improvement problem.

For compute, self-improvement is much cheaper than cross-model distillation since everything uses the same 8B model — just generation, training, and Pass@k evaluation on the validation set. I'm estimating around 800-1500 H100-hours total. Let me reconsider those resource estimates more carefully.

For a Qwen3-8B model, I'm calculating training at roughly 1 H100-hour per 1000 steps with batch size 128, generation pass@32 evaluations at about 0.5 H100-hours each, and self-generation of training data at around 2 H100-hours per iteration. Across all cycles I'm looking at maybe 10K-20K total training steps with diagnostics every 100 steps, which means 100-200 evaluations. Breaking this down: stage 0 diagnostic comparison around 200 H100-hours, stage 1 main experiments with 5 configurations at roughly 500 H100-hours, baselines at 500 H100-hours, ablations at 250 H100-hours, and data generation costs still being calculated.

Adding in a buffer, the total comes to around 1800 H100-hours, which is significantly cheaper than the original FrontierCycle approach since there's no expensive teacher model involved.

Now I'm thinking through the specific diagnostic signals that would drive the self-improvement scheduling, particularly looking at sampling efficiency gaps and difficulty-stratified frontier scores to identify where the model has frontier capability it hasn't consolidated versus where it's genuinely stuck.

I'm also considering entropy trajectories, self-consistency divergence, and generalization gaps as measurable signals—when self-consistency is much higher than single-sample accuracy, that indicates room for RL consolidation, but when it plateaus, the model needs fresh data instead.

Writing phase selection logic... Now I'm laying out the experimental plan in three stages. First, I'll validate which diagnostic signals actually predict when to switch between generation and RL training by running standard self-improvement loops and logging everything. Then I'll compare FrontierLoop against fixed baselines like STaR and ReST-EM across multiple benchmarks, tracking pass rates and compute efficiency. Finally, I'll run ablations to isolate which diagnostic signals matter most and whether adaptive scheduling beats fixed intervals.

The whole timeline fits within 10-14 weeks, which works for both ICLR 2027 and ARR October 2026. I also need to make sure I'm addressing the reviewer feedback directly—especially clarifying that this is about self-improvement cycles rather than a topic mismatch, properly distinguishing our generation-RL cycling from how SIRI uses iterative cycling within RL, and filling in the missing citations like CLPD.

Now I'm thinking through which citations are actually relevant to the new framing. CLPD and PRISM are about distillation, so they're less central now, but the Unified View paper still grounds the theoretical side. The reviewer's concern about a surge in unified methods matters less since we're focused on self-improvement rather than cross-model distillation.

Comparing to the most direct competitors—Absolute Zero and R-Zero—Absolute Zero uses self-play where the proposer generates problems and the solver tackles them with no external data, relying on code generation.

R-Zero takes a co-evolution approach where the challenger targets the solver's weaknesses, giving it some diagnostic awareness, though it's locked into three fixed iterations. Our approach differs in three key ways: we extract richer diagnostic signals from the pass@k spectrum and difficulty stratification rather than just binary success, we dynamically adjust both iteration length and count instead of using fixed schedules, and we explicitly prevent collapse. Most importantly, we're addressing the scheduling problem—deciding when to generate and when to train—which neither competitor tackles. B-STaR and HS-STaR optimize within individual iterations through better sampling and filtering, while SEC uses a multi-armed bandit for difficulty selection, but we're thinking about the cross-iteration scheduling layer that sits above these approaches.

Now I'm clarifying what "synthetic data" actually means for this proposal. The model generates step-by-step reasoning traces for math problems, which become the training signal for self-improvement.  Beyond that, it can generate entirely new math problems targeted at its own weaknesses—the diagnostic system identifies which difficulty levels and topics need work, then the model creates problems in those areas. This combines the STaR/ReST-EM paradigm with more advanced synthetic problem generation, all without external teachers.

For the title, I'm settling on something concise that captures the core idea of diagnostic-guided cycling between data generation and self-improvement.

Now I need to clarify the exact mechanics of each phase: the generation phase creates new training data by solving targeted problems and filtering for correct answers, while the training phase consolidates that data through reinforcement learning.

The key insight is that RLVR operates differently from STaR—it generates and trains simultaneously in an on-policy loop rather than in separate alternating phases. So my framework needs to decide whether to follow a discrete generation-then-training schedule or embrace the continuous on-policy approach.

I'm settling on two distinct modes: one where GRPO/RLVR consolidates performance on the current problem distribution, and another where I deliberately synthesize new problems at targeted difficulty levels to expand what the model can handle.

The switching logic is straightforward—when RL training plateaus and metrics like pass@k and entropy stagnate, I shift to data generation mode. Once I've accumulated enough new training examples, I cycle back to RL to integrate them. This creates a diagnostic-driven loop that combines the focused improvement of reinforcement learning with the frontier-pushing of synthetic data creation.

What really sets this apart from standard STaR is the use of RL instead of just supervised fine-tuning, which lets me maintain exploration through entropy control. I'm also checking diagnostics continuously rather than waiting for iteration boundaries, targeting generation specifically at the difficulty bands where the model struggles most, and actively watching for collapse signals. The iteration count adapts based on actual progress rather than being fixed upfront. So it's a hybrid approach that uses real-time diagnostics to orchestrate when and how to improve.

The "cycling between RL and data generation" framing feels right because it's concrete, connects to existing work like SIRI and ReMiT, and has a clear feedback loop: detect stall → generate targeted data → train → repeat. Before running the full experiment, I should validate that this targeted generation approach actually beats uniform generation, that RL on self-generated data improves real performance rather than just memorization, and establish what the validation gate criteria are.

The compute picture is much more favorable now since everything runs on the 8B model itself—no 235B teacher, cheaper pass@k evaluation, and the model generates its own training data. I'm estimating around 1200-1800 H100-hours, possibly less. The key references I'll anchor on are STaR for the foundational self-training approach, ReST-EM for the RL-based refinement, and Absolute Zero as a self-play baseline to compare against.

Now I'm building out the full reference list to support the pivoted approach—pulling in R-Zero for self-evolution, Mind the Gap for the theoretical grounding on why self-improvement works, and several papers on pass@k as both a limitation and an active training signal. I'm also including work on entropy management during training and difficulty-aware data selection to handle the practical challenges of scaling this up. I'm seeing the rest of the reference list and realizing I need to be selective about what to include. The HSIR paper from May 2026 on efficient self-improvement seems particularly relevant given its recency, so I should prioritize understanding its contributions and how it positions against the other work on solver-verifier dynamics and iterative improvement.

Now I'm articulating the core insight: fixed iteration schedules for self-improvement are inefficient because the model's data needs shift throughout training—early phases benefit from broad exploration while later phases need precision on the frontier. The challenge is that diminishing returns and model collapse happen unpredictably, so a static schedule can't adapt to when these inflection points occur.

The key opportunity is that we have multiple validated signals—pass@k metrics, entropy trajectories, generation-verification gaps, and difficulty stratification—that together can diagnose the model's learning state in real time and guide adaptive scheduling decisions.

This hasn't been attempted before because the diagnostic tools were developed separately across different research contexts, and the understanding of pass@k as an active training signal only emerged recently. Previous work focused either on the self-play mechanism itself or on detecting collapse after it happens, rather than using live diagnostics to prevent it proactively.

The contribution feels solid — it's well-motivated, cheaper than the cross-model approach, and addresses a clear gap in how self-improvement loops are currently scheduled. But I'm wondering if there's a more ambitious version here: what if we go beyond just scheduling the existing loop and propose a self-evolving curriculum that dynamically adjusts not just when to train, but what the model should be learning at each stage?

That would mean combining diagnostic-guided problem generation, frontier-targeted solution synthesis, and adaptive RL training all orchestrated by a unified framework. It's elegant in theory, but probably too much for one paper. The scheduling angle is cleaner and more tractable.

Let me focus on that and start drafting the JSON with a clear title and core contribution.

The system would have three main pieces: a diagnostic module that tracks the model's pass@k spectrum and performance across difficulty levels every hundred steps, an adaptive scheduler that decides whether to generate new synthetic data or consolidate through RL based on those diagnostics, and phase-specific operators that handle either targeted problem synthesis with filtering or entropy-managed reinforcement learning depending on the current mode.

For the experimental timeline, I'm planning validation work over the first week and a half, then a second cycle to test if the approach improves iteratively, followed by full experiments, ablations, and writing—totaling around eleven to fifteen weeks. I'm realizing the core insight here is that diagnostic signals developed for other contexts like distillation are actually more critical for self-improvement scheduling because of the higher risk of collapse, and existing methods use fixed schedules partly for historical reasons and partly because these tools weren't available when they were designed.

The two-mode framework—alternating between generation to expand what the policy can do and RL to refine performance within that expanded space—connects directly to the theoretical mechanisms in the Unified View paper around support expansion and policy reshaping. Our contribution is using diagnostics to intelligently schedule between these two modes rather than relying on fixed intervals.

This framing feels solid. Now I'm working on the title and want something concise that captures the core idea without being unwieldy.

I'm settling on "FrontierLoop: Diagnostic-Guided Adaptive Scheduling of Self-Improvement Cycles for Mathematical Reasoning" as the final title—it's precise and highlights the key contribution of knowing when to generate versus when to train. I briefly considered alternatives like DiagSTaR or AdaptLoop, but FrontierLoop best captures the sense of pushing boundaries through iterative cycling. Before finalizing, I should verify the name isn't already in use, though I can't easily check that right now. I'm cycling through naming options for this approach—ReasonLoop, DiagLoop, ASIDE—but I think FrontierLoop is the cleanest choice since it directly references tracking the reasoning frontier through pass@k metrics. Now I need to write out the full JSON proposal, starting with the title and core problem statement that addresses why fixed schedules in existing self-improvement methods like STaR and ReST-EM are suboptimal, particularly around how model needs evolve during training.

The key insight is that early-stage training benefits from broad data generation while later stages need targeted expansion at specific difficulty boundaries, but fixed schedules can't adapt. Beyond that, these methods also fail to detect saturation and collapse—research shows diminishing returns after a few iterations and eventual distribution degradation from iterative self-training—and they misallocate compute by generating uniformly across difficulty levels when boundary-level problems near the model's current capability are actually where learning concentrates.

RL methods like GRPO improve sampling efficiency but hit a ceiling on expanding the reasoning frontier beyond what the base model can do, so new synthetic data becomes necessary before RL can consolidate gains. The tools to address these problems already exist individually—pass@k metrics predict RL outcomes with high correlation, entropy management prevents collapse, and the generation-verification gap reveals self-improvement potential—but they've never been integrated into a unified scheduling framework.

The key insight is that self-improvement cycles are uniquely suited for diagnostic-guided scheduling because they face higher collapse risk than supervised training, self-generated data quality is more variable, and the optimal balance between generation and training shifts as the model improves. I'm proposing a system that uses frontier diagnostics like pass@k spectrum and entropy to adaptively determine when to generate new data, what difficulty level to target, and how to balance generation against training iterations. For generation, I'm targeting the frontier difficulty identified by the stratified scoring, creating structurally diverse problems, and filtering for correctness. The RL phase uses GRPO with entropy management on the accumulated self-generated data. After completing one full cycle, I need a go/no-go gate to check if the second cycle improves beyond the first plateau—if not, I'll focus on single-cycle optimization instead. The resource estimate comes in much cheaper than the original approach, ranging from 900 to 1800 H100-hours depending on the level of automation.

Now I'm refining how SIRI fits into this framework—it's actually an iterative compression-expansion method within RL itself, not a fixed pipeline stage like I initially characterized it. That's orthogonal to FrontierLoop's cycling between generation and RL training, so they could work together. I should also make sure I'm properly citing CLP and clarifying these distinctions in the proposal for ICLR 2027 and ARR October 2026.

Looking at the related work more carefully: the unified view papers on support expansion and policy reshaping map directly to our generation and RL modes, the distribution alignment work is relevant to understanding mode transitions, and the theoretical pieces on continuous SFT/RL/OPD and state distributions actually support our scheduling approach rather than undermining it.

Writing the JSON now...

For the inspired_by field, I'm pulling together the key validated principles and theoretical foundations: pass@k as a predictor of RL outcomes and as an active training signal, the insight that RLVR doesn't expand the frontier, the generation-verification gap enabling self-improvement, understanding how iterative self-training collapses, difficulty-aware sampling approaches, the compounding effects of iterative cycling, the design principles around support expansion and policy reshaping, and entropy management techniques.

Now I'm assessing the contribution level. The diagnostic-guided scheduling is fundamentally an engineering contribution rather than a breakthrough insight, but it's well-motivated and addresses a real gap in the landscape. I think "solid" is the right rating, with potential to upgrade to "strong" if the experiments demonstrate substantial improvements over baselines.

Writing the JSON schema now...

Filling in the core sections carefully. For the core problem, I need to establish that self-improvement methods rely on fixed schedules, which is suboptimal since model capabilities evolve unpredictably and diagnostic tools already exist but haven't been leveraged for this specific purpose. The opportunity lies in recognizing that diagnostic signals are actually more valuable for self-improvement scheduling than they are for distillation, grounded in the generation-verification gap, and there's a clear gap in the literature where no one's combined these ideas yet.

Writing JSON structure... -guided self-improvement scheduling
4. Practical impact: more efficient self-improvement

For landscape:
1. STaR, ReST-EM (foundational self-improvement)
2. Self-play methods (Absolute Zero, R-Zero, R-Diverse)
3. Diagnostic tools (pass@k, entropy, Cover@tau)
4. Collapse literature (Nature 2024, SRT)
5. Difficulty-aware methods (DART-Math, HS-STaR, SEC)
6. Iterative cycling (SIRI, ReMiT)
7. Theoretical foundations (Mind the Gap, Unified View, Solver-Verifier Gap)
8. May 2026 unified methods (properly acknowledged as targeting different regime)

For approach:
1. Diagnostic module
2. Adaptive scheduler with mode switching logic
3. Phase-specific operators
4. Go/no-go gate
5. Experimental plan with stages
6. Baselines and ablations

Now I need to address a key distinction: this isn't just active learning applied to self-improvement. While active learning picks which examples to label from a fixed pool, we're generating new data and making phase-level decisions about difficulty targeting—plus our diagnostics are tailored to self-improvement collapse patterns. I should clarify this upfront to preempt that criticism. There's also the practical concern that pass@k evaluation every 100 steps could get expensive, but I can mitigate that by using a compact validation set of around 200 problems with a moderate k value.

For the go/no-go validation gate, I'm thinking of a Stage 0.5 that runs one complete cycle to verify the cycling mechanism works: generate data at frontier difficulty, train with RL, measure if performance improves by at least 1 percentage point on MATH-500. Only if that threshold is met do we proceed to the full adaptive scheduling.

Either path yields something publishable—either the complete FrontierLoop framework if cycling validates, or diagnostic-guided single-iteration improvement if it doesn't.

For baselines, I'm comparing against STaR, ReST-EM, pure RLVR without data generation, Absolute Zero self-play, fixed-interval cycling as a non-adaptive control, and R-Zero. For ablations, I need to isolate the diagnostic signal itself by testing different variants like SEG versus entropy versus DSFS versus combining them.

I'm also varying the scheduling between adaptive and fixed, testing whether targeted difficulty in generated data outperforms uniform sampling, checking if collapse prevention actually helps, and running experiments with 1, 3, and 5 cycles to understand the scaling behavior.

Evaluation spans MATH-500, AIME 2024, and LiveCodeBench with pass@1 and pass@32 metrics broken down by difficulty level. I'll track compute efficiency in H100-hours per percentage point gain and count how many cycles FrontierLoop actually uses compared to the fixed baselines.

Now I'm drafting the JSON response carefully, especially the reviewer_response section to directly address each concern. The topic mismatch gets resolved by framing this as pure self-improvement—no external teacher, just the model generating synthetic data and improving through RL. For the SIRI mischaracterization... FrontierLoop operates in pure self-improvement without any external teacher, and the theoretical work on support expansion and policy reshaping gives me the vocabulary to operationalize this through adaptive scheduling. The proposal now covers all three elements the user requested: synthetic data generation through reasoning traces and problem synthesis, self-improvement via bootstrapping from the model's own capabilities with verifiable rewards, and mathematical reasoning as the application domain. I'll go with "FrontierLoop" as the name and write out the full JSON response. Writing the JSON config...

I'm settling on "FrontierLoop" as the final name since it's broad enough to cover both the data generation and reinforcement learning components. Now I need to crystallize the core novelty claims: using real-time frontier diagnostics from the pass@k spectrum to adaptively schedule self-improvement cycles, generating synthetic data specifically targeted at the model's capability boundaries through difficulty stratification, and preventing collapse via self-consistency divergence detection. The experimental validation should demonstrate that adaptive scheduling beats fixed-schedule approaches like STaR and ReST.

EM, that difficulty-targeted generation is more sample-efficient than uniform generation, that collapse detection enables more training iterations, and that the overall approach matches or exceeds self-play methods like Absolute Zero and R-Zero while using less compute.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7b88d9b-7eda-4011-9466-3aa11a73a043",
  "isSidechain": false,
  "requestId": "req_011CbTiKV1MMkGx1rLimoGX7",
  "type": "assistant",
  "uuid": "f0c44d59-c25f-47a9-9de8-5e2d310befde",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M926VteXSJUe4Y4WDeimgS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 8346,
      "cache_creation_input_tokens": 8056,
      "cache_read_input_tokens": 24259,
      "output_tokens": 14423,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8056,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 8346,
          "output_tokens": 14423,
          "cache_read_input_tokens": 24259,
          "cache_creation_input_tokens": 8056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8056
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

_source line 23 · 2026-05-27T20:39:58.626Z_

Now let me fetch a few key papers to verify critical details before writing the pivoted proposal:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0c44d59-c25f-47a9-9de8-5e2d310befde",
  "isSidechain": false,
  "requestId": "req_011CbTiKV1MMkGx1rLimoGX7",
  "type": "assistant",
  "uuid": "15210103-c5a9-4cab-a5d9-4da7420aaf29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M926VteXSJUe4Y4WDeimgS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 8346,
      "cache_creation_input_tokens": 8056,
      "cache_read_input_tokens": 24259,
      "output_tokens": 14423,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8056,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 8346,
          "output_tokens": 14423,
          "cache_read_input_tokens": 24259,
          "cache_creation_input_tokens": 8056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8056
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

_source line 24 · 2026-05-27T20:39:58.627Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XRPwHZj9roRfSgGVznEtcp`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15210103-c5a9-4cab-a5d9-4da7420aaf29",
  "isSidechain": false,
  "requestId": "req_011CbTiKV1MMkGx1rLimoGX7",
  "type": "assistant",
  "uuid": "cadad683-0b13-42d0-9aa9-e69c61f29ec6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M926VteXSJUe4Y4WDeimgS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 8346,
      "cache_creation_input_tokens": 8056,
      "cache_read_input_tokens": 24259,
      "output_tokens": 14423,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8056,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 8346,
          "output_tokens": 14423,
          "cache_read_input_tokens": 24259,
          "cache_creation_input_tokens": 8056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8056
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

_source line 25 · 2026-05-27T20:39:58.635Z_

<details><summary>↩ Tool result · `toolu_01XRPwHZj9roRfSgGVznEtcp`</summary>

````text
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
  "parentUuid": "cadad683-0b13-42d0-9aa9-e69c61f29ec6",
  "isSidechain": false,
  "promptId": "a6903394-624e-4492-ad19-36a9e5620d23",
  "type": "user",
  "uuid": "1dbe7944-b118-4b39-ba55-fad3fac44e30",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "cadad683-0b13-42d0-9aa9-e69c61f29ec6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"FrontierCycle: Diagnostic-Guided Iterative RL↔Distillation Scheduling…",
  "leafUuid": "1dbe7944-b118-4b39-ba55-fad3fac44e30",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise self-improvement framework for iterative LLM reasoning cycles",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---

### Assistant

_source line 28 · 2026-05-27T20:40:02.140Z_

<details><summary>Logged reasoning block</summary>

```text
Let me fetch a few key papers to verify details before writing the pivoted proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dbe7944-b118-4b39-ba55-fad3fac44e30",
  "isSidechain": false,
  "requestId": "req_011CbTii5zdy5CSX7z6sWfQq",
  "type": "assistant",
  "uuid": "63802dc6-05b6-4f3f-be91-2f66d06b9802",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjB1QenUSr7CX5CLgBbSVh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23287,
      "cache_read_input_tokens": 32315,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 500,
          "cache_read_input_tokens": 32315,
          "cache_creation_input_tokens": 23287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23287
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

_source line 29 · 2026-05-27T20:40:03.774Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HJSgsV9aauiX2kuwp4ytai`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.21444",
  "prompt": "Extract: full title, authors, key findings about self-training collapse/reward hacking, how many iterations before collapse occurs, specific numbers on math benchmarks, and the main conclusions about when self-training works vs. fails."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63802dc6-05b6-4f3f-be91-2f66d06b9802",
  "isSidechain": false,
  "requestId": "req_011CbTii5zdy5CSX7z6sWfQq",
  "type": "assistant",
  "uuid": "24101b5f-e880-43db-a53b-e81150cfbf3c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjB1QenUSr7CX5CLgBbSVh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23287,
      "cache_read_input_tokens": 32315,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 500,
          "cache_read_input_tokens": 32315,
          "cache_creation_input_tokens": 23287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23287
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

_source line 30 · 2026-05-27T20:40:05.233Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MQwfwRmgVX2EKpqKG8KF9E`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.02674",
  "prompt": "Extract: full title, authors, key findings about the \"generation-verification gap\", the scaling law they discover, specific numbers showing when self-improvement works, and the mathematical formalization of the gap."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24101b5f-e880-43db-a53b-e81150cfbf3c",
  "isSidechain": false,
  "requestId": "req_011CbTii5zdy5CSX7z6sWfQq",
  "type": "assistant",
  "uuid": "de1c16ee-aeaa-480f-9560-28bfc98140da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjB1QenUSr7CX5CLgBbSVh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23287,
      "cache_read_input_tokens": 32315,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 500,
          "cache_read_input_tokens": 32315,
          "cache_creation_input_tokens": 23287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23287
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

_source line 31 · 2026-05-27T20:40:07.544Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016iFomvmsGJZFjKPrd8zgAA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.03335",
  "prompt": "Extract: full title, authors, key results on math reasoning benchmarks (MATH, AIME, GSM8K), how the self-play mechanism works (proposer + solver), what verifier is used, and any limitations mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de1c16ee-aeaa-480f-9560-28bfc98140da",
  "isSidechain": false,
  "requestId": "req_011CbTii5zdy5CSX7z6sWfQq",
  "type": "assistant",
  "uuid": "1c5dc3e0-b08f-4e02-ae92-fe438d54b0b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjB1QenUSr7CX5CLgBbSVh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23287,
      "cache_read_input_tokens": 32315,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 500,
          "cache_read_input_tokens": 32315,
          "cache_creation_input_tokens": 23287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23287
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

_source line 32 · 2026-05-27T20:40:08.847Z_

<details><summary>↩ Tool result · `toolu_01HJSgsV9aauiX2kuwp4ytai`</summary>

```text
# Paper Summary: Can Large Reasoning Models Self-Train?

**Full Title:** "Can Large Reasoning Models Self-Train?"

**Authors:** Sheikh Shafayat, Fahim Tajwar, Ruslan Salakhutdinov, Jeff Schneider, Andrea Zanette

## Key Findings

**Self-Training Benefits:**
The research demonstrates that models can improve through self-feedback mechanisms. Using majority voting as feedback, the approach successfully enhanced "not only the model's reasoning performance, but also its capability of generating better quality feedback" for subsequent training cycles.

**Critical Limitation - Reward Hacking:**
The study identifies a fundamental vulnerability: extended training with self-generated rewards leads to "reward hacking where models learn to maximize training (pseudo-)reward, resulting in sudden and complete performance collapse."

**Iterations Before Collapse:**
The abstract does not specify the exact number of iterations before collapse occurs.

**Specific Benchmark Numbers:**
No concrete numerical results on math benchmarks are provided in the abstract.

## Main Conclusions

The paper frames "feedback design as the central challenge" for sustainable self-training. While initial self-training iterations show promise for improving model reasoning capabilities, the approach becomes unstable under prolonged training without proper safeguards against reward manipulation. The research calls for developing mechanisms that enable genuine self-improvement while preventing exploitation of training signals.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24101b5f-e880-43db-a53b-e81150cfbf3c",
  "isSidechain": false,
  "promptId": "a6903394-624e-4492-ad19-36a9e5620d23",
  "type": "user",
  "uuid": "23dece94-ddf8-4bb1-a9ef-97659c51fa80",
  "toolUseResult": {
    "bytes": 46506,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: Can Large Reasoning Models Self-Train?\n\n**Full Title:** \"Can Large Reasoning Models Self-Train?\"\n\n**Authors:** Sheikh Shafayat, Fahim Tajwar, Ruslan Salakhutdinov, Jeff Schneider, Andrea Zanette\n\n## Key Findings\n\n**Self-Training Benefits:**\nThe research demonstrates that models can improve through self-feedback mechanisms. Using majority voting as feedback, the approach successfully enhanced \"not only the model's reasoning performance, but also its capability of generating better quality feedback\" for subsequent training cycles.\n\n**Critical Limitation - Reward Hacking:**\nThe study identifies a fundamental vulnerability: extended training with self-generated rewards leads to \"reward hacking where models learn to maximize training (pseudo-)reward, resulting in sudden and complete performance collapse.\"\n\n**Iterations Before Collapse:**\nThe abstract does not specify the exact number of iterations before collapse occurs.\n\n**Specific Benchmark Numbers:**\nNo concrete numerical results on math benchmarks are provided in the abstract.\n\n## Main Conclusions\n\nThe paper frames \"feedback design as the central challenge\" for sustainable self-training. While initial self-training iterations show promise for improving model reasoning capabilities, the approach becomes unstable under prolonged training without proper safeguards against reward manipulation. The research calls for developing mechanisms that enable genuine self-improvement while preventing exploitation of training signals.",
    "durationMs": 5070,
    "url": "https://arxiv.org/abs/2505.21444"
  },
  "sourceToolAssistantUUID": "24101b5f-e880-43db-a53b-e81150cfbf3c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-27T20:40:09.229Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Nc7ZmXMf51Fn3q73WAiPib`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.24998",
  "prompt": "Extract: full title, authors, key findings about efficient self-improvement, the verify-then-exit sampling method, Intrinsic Diversity score, specific numbers (+10.9% gain, -42.4% overhead), and which benchmarks were used."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23dece94-ddf8-4bb1-a9ef-97659c51fa80",
  "isSidechain": false,
  "requestId": "req_011CbTii5zdy5CSX7z6sWfQq",
  "type": "assistant",
  "uuid": "4a4abfab-9d80-4771-b772-a45f1b0c0893",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjB1QenUSr7CX5CLgBbSVh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23287,
      "cache_read_input_tokens": 32315,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 500,
          "cache_read_input_tokens": 32315,
          "cache_creation_input_tokens": 23287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23287
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

_source line 34 · 2026-05-27T20:40:10.503Z_

<details><summary>↩ Tool result · `toolu_01MQwfwRmgVX2EKpqKG8KF9E`</summary>

```text
# Research Summary: Mind the Gap

**Full Title:** "Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models"

**Authors:** Yuda Song, Hanlin Zhang, Carson Eisenach, Sham Kakade, Dean Foster, and Udaya Ghai

## Key Findings

**Generation-Verification Gap:**
The researchers formalize a central concept they call the "generation-verification gap," which they describe as "a quantity which we formalize as the generation-verification gap." This metric fundamentally governs how effectively self-improvement mechanisms operate in LLMs.

**Scaling Phenomenon:**
The study identifies a noteworthy scaling law: "a variant of the generation-verification gap scales monotonically with the model pre-training flops." This demonstrates that as models grow larger computationally, this gap exhibits predictable, consistent behavior.

**Self-Improvement Mechanism:**
The framework involves models that "verifies its own outputs, filters or reweights data based on this verification, and distills the filtered data."

**Specific Quantitative Thresholds:**
The abstract does not provide explicit numerical thresholds for when self-improvement succeeds or fails. However, the paper examines "when self-improvement is possible" through controlled experiments.

**Mathematical Formalization:**
The researchers provide "a mathematical formulation for self-improvement," grounded in their formalized generation-verification gap concept, though specific equations are not detailed in this abstract.

The paper was accepted to ICLR 2025 and comprises 41 pages with 19 figures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de1c16ee-aeaa-480f-9560-28bfc98140da",
  "isSidechain": false,
  "promptId": "a6903394-624e-4492-ad19-36a9e5620d23",
  "type": "user",
  "uuid": "c05f7fd0-c8e7-4bd3-bf4a-a5f5f950c4ba",
  "toolUseResult": {
    "bytes": 46280,
    "code": 200,
    "codeText": "OK",
    "result": "# Research Summary: Mind the Gap\n\n**Full Title:** \"Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models\"\n\n**Authors:** Yuda Song, Hanlin Zhang, Carson Eisenach, Sham Kakade, Dean Foster, and Udaya Ghai\n\n## Key Findings\n\n**Generation-Verification Gap:**\nThe researchers formalize a central concept they call the \"generation-verification gap,\" which they describe as \"a quantity which we formalize as the generation-verification gap.\" This metric fundamentally governs how effectively self-improvement mechanisms operate in LLMs.\n\n**Scaling Phenomenon:**\nThe study identifies a noteworthy scaling law: \"a variant of the generation-verification gap scales monotonically with the model pre-training flops.\" This demonstrates that as models grow larger computationally, this gap exhibits predictable, consistent behavior.\n\n**Self-Improvement Mechanism:**\nThe framework involves models that \"verifies its own outputs, filters or reweights data based on this verification, and distills the filtered data.\"\n\n**Specific Quantitative Thresholds:**\nThe abstract does not provide explicit numerical thresholds for when self-improvement succeeds or fails. However, the paper examines \"when self-improvement is possible\" through controlled experiments.\n\n**Mathematical Formalization:**\nThe researchers provide \"a mathematical formulation for self-improvement,\" grounded in their formalized generation-verification gap concept, though specific equations are not detailed in this abstract.\n\nThe paper was accepted to ICLR 2025 and comprises 41 pages with 19 figures.",
    "durationMs": 5267,
    "url": "https://arxiv.org/abs/2412.02674"
  },
  "sourceToolAssistantUUID": "de1c16ee-aeaa-480f-9560-28bfc98140da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-27T20:40:12.732Z_

<details><summary>↩ Tool result · `toolu_016iFomvmsGJZFjKPrd8zgAA`</summary>

```text
# Absolute Zero: Paper Summary

**Full Title:** "Absolute Zero: Reinforced Self-play Reasoning with Zero Data"

**Authors:** Andrew Zhao, Yiran Wu, Yang Yue, Tong Wu, Quentin Xu, Matthieu Lin, Shenzhi Wang, Qingyun Wu, Zilong Zheng, Gao Huang

## Key Results
The abstract states the system "achieves overall SOTA performance on coding and mathematical reasoning tasks" while surpassing "existing zero-setting models that rely on tens of thousands of in-domain human-curated examples." However, specific benchmark scores for MATH, AIME, or GSM8K are not provided in the page content.

## Self-Play Mechanism
The system employs a dual-role approach where "a single model learns to propose tasks that maximize its own learning progress and improves reasoning by solving them." The proposer generates tasks while the solver attempts to complete them.

## Verifier
A "code executor" serves as the verification mechanism, functioning to "both validate proposed code reasoning tasks and verify answers, serving as a unified source of verifiable reward."

## Limitations Mentioned
The abstract does not explicitly discuss limitations. It focuses on advantages: the approach eliminates dependence on external datasets and functions across different model scales and classes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c5dc3e0-b08f-4e02-ae92-fe438d54b0b9",
  "isSidechain": false,
  "promptId": "a6903394-624e-4492-ad19-36a9e5620d23",
  "type": "user",
  "uuid": "a3a25e6e-516e-4955-a17e-4a2e51fcd888",
  "toolUseResult": {
    "bytes": 49522,
    "code": 200,
    "codeText": "OK",
    "result": "# Absolute Zero: Paper Summary\n\n**Full Title:** \"Absolute Zero: Reinforced Self-play Reasoning with Zero Data\"\n\n**Authors:** Andrew Zhao, Yiran Wu, Yang Yue, Tong Wu, Quentin Xu, Matthieu Lin, Shenzhi Wang, Qingyun Wu, Zilong Zheng, Gao Huang\n\n## Key Results\nThe abstract states the system \"achieves overall SOTA performance on coding and mathematical reasoning tasks\" while surpassing \"existing zero-setting models that rely on tens of thousands of in-domain human-curated examples.\" However, specific benchmark scores for MATH, AIME, or GSM8K are not provided in the page content.\n\n## Self-Play Mechanism\nThe system employs a dual-role approach where \"a single model learns to propose tasks that maximize its own learning progress and improves reasoning by solving them.\" The proposer generates tasks while the solver attempts to complete them.\n\n## Verifier\nA \"code executor\" serves as the verification mechanism, functioning to \"both validate proposed code reasoning tasks and verify answers, serving as a unified source of verifiable reward.\"\n\n## Limitations Mentioned\nThe abstract does not explicitly discuss limitations. It focuses on advantages: the approach eliminates dependence on external datasets and functions across different model scales and classes.",
    "durationMs": 5186,
    "url": "https://arxiv.org/abs/2505.03335"
  },
  "sourceToolAssistantUUID": "1c5dc3e0-b08f-4e02-ae92-fe438d54b0b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-27T20:40:14.846Z_

<details><summary>↩ Tool result · `toolu_01Nc7ZmXMf51Fn3q73WAiPib`</summary>

```text
# Research Summary: HSIR Self-Improvement Framework

**Full Title:** "Better, Faster: Harnessing Self-Improvement in Large Reasoning Models"

**Authors:** Qihuang Zhong, Liang Ding, Juhua Liu, Bo Du, Leszek Rutkowski, Dacheng Tao

## Key Findings on Efficient Self-Improvement

The research identifies two critical problems in self-improvement training for large reasoning models:

1. **Data Imbalance:** Most training samples are simple, while challenging samples remain scarce
2. **Overthinking:** Models generate "many undesired samples with redundant reasoning steps"

## Core Methods

**Verify-Then-Exit Sampling Strategy:** This approach mitigates data imbalance by "efficiently collecting more accurate solutions for difficult queries," prioritizing harder problems during training.

**Intrinsic Diversity Score:** Designed to quantify overthinking and eliminate solutions containing excessive reasoning steps.

## Performance Metrics

- **Reasoning Performance Gain:** Up to +10.9% average improvement
- **Efficiency Improvement:** Reduced inference overhead by up to 42.4%

## Technical Enhancement

The paper proposes H-GRPO, an enhanced algorithm leveraging intrinsic diversity as external reinforcement learning rewards to "encourage concise and diverse reasoning."

## Benchmarks

The abstract does not specify which particular benchmarks were evaluated—only that "extensive results" demonstrated effectiveness across various post-training paradigms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a4abfab-9d80-4771-b772-a45f1b0c0893",
  "isSidechain": false,
  "promptId": "a6903394-624e-4492-ad19-36a9e5620d23",
  "type": "user",
  "uuid": "6a22c672-b216-4338-80de-73c38d43f8e6",
  "toolUseResult": {
    "bytes": 47260,
    "code": 200,
    "codeText": "OK",
    "result": "# Research Summary: HSIR Self-Improvement Framework\n\n**Full Title:** \"Better, Faster: Harnessing Self-Improvement in Large Reasoning Models\"\n\n**Authors:** Qihuang Zhong, Liang Ding, Juhua Liu, Bo Du, Leszek Rutkowski, Dacheng Tao\n\n## Key Findings on Efficient Self-Improvement\n\nThe research identifies two critical problems in self-improvement training for large reasoning models:\n\n1. **Data Imbalance:** Most training samples are simple, while challenging samples remain scarce\n2. **Overthinking:** Models generate \"many undesired samples with redundant reasoning steps\"\n\n## Core Methods\n\n**Verify-Then-Exit Sampling Strategy:** This approach mitigates data imbalance by \"efficiently collecting more accurate solutions for difficult queries,\" prioritizing harder problems during training.\n\n**Intrinsic Diversity Score:** Designed to quantify overthinking and eliminate solutions containing excessive reasoning steps.\n\n## Performance Metrics\n\n- **Reasoning Performance Gain:** Up to +10.9% average improvement\n- **Efficiency Improvement:** Reduced inference overhead by up to 42.4%\n\n## Technical Enhancement\n\nThe paper proposes H-GRPO, an enhanced algorithm leveraging intrinsic diversity as external reinforcement learning rewards to \"encourage concise and diverse reasoning.\"\n\n## Benchmarks\n\nThe abstract does not specify which particular benchmarks were evaluated—only that \"extensive results\" demonstrated effectiveness across various post-training paradigms.",
    "durationMs": 5615,
    "url": "https://arxiv.org/abs/2605.24998"
  },
  "sourceToolAssistantUUID": "4a4abfab-9d80-4771-b772-a45f1b0c0893",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-27T20:40:14.849Z_

```json
{
  "parentUuid": "6a22c672-b216-4338-80de-73c38d43f8e6",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c652405f-6d3c-4302-84c3-58139de3c442",
  "timestamp": "2026-05-27T20:40:14.849Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 38 · 2026-05-27T20:40:17.613Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the key details. Let me also fetch a couple more critical papers for the pivot.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c652405f-6d3c-4302-84c3-58139de3c442",
  "isSidechain": false,
  "requestId": "req_011CbTijHH5JT21z9FpAvFaD",
  "type": "assistant",
  "uuid": "b53019ea-1423-4be1-b5fa-3f1ad2a550ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015X8r9Uph3aeCUk64Upo6uz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1988,
      "cache_read_input_tokens": 55602,
      "output_tokens": 398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1988,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 398,
          "cache_read_input_tokens": 55602,
          "cache_creation_input_tokens": 1988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1988
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

_source line 39 · 2026-05-27T20:40:19.021Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Lhd5NXAVNXYniocFDnbdeg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.00075",
  "prompt": "Extract: full title, authors, key findings about the solver-verifier gap theory, the exponential curve model for self-improvement dynamics, specific numbers/equations, and conclusions about when self-improvement saturates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b53019ea-1423-4be1-b5fa-3f1ad2a550ef",
  "isSidechain": false,
  "requestId": "req_011CbTijHH5JT21z9FpAvFaD",
  "type": "assistant",
  "uuid": "6ccbf7c5-7579-4531-88b9-9904d19aafd5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015X8r9Uph3aeCUk64Upo6uz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1988,
      "cache_read_input_tokens": 55602,
      "output_tokens": 398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1988,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 398,
          "cache_read_input_tokens": 55602,
          "cache_creation_input_tokens": 1988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1988
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

_source line 40 · 2026-05-27T20:40:21.364Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013Qp6EoxMByyG134SKVjbd7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.14029",
  "prompt": "Extract: full title, authors, key findings about variational problem synthesis for sustaining RLVR, specific numbers on pass@32 for AIME24/AIME25, the SvS mechanism, and how it maintains entropy/prevents collapse."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ccbf7c5-7579-4531-88b9-9904d19aafd5",
  "isSidechain": false,
  "requestId": "req_011CbTijHH5JT21z9FpAvFaD",
  "type": "assistant",
  "uuid": "f1f3c848-b160-49d4-bdba-46ab2f2c5fde",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015X8r9Uph3aeCUk64Upo6uz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1988,
      "cache_read_input_tokens": 55602,
      "output_tokens": 398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1988,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 398,
          "cache_read_input_tokens": 55602,
          "cache_creation_input_tokens": 1988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1988
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

_source line 41 · 2026-05-27T20:40:22.611Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01445kUjdt6RDPtRNzQpsewy`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.07941",
  "prompt": "Extract: full title, authors, key arguments about multi-stage pipeline composition, the three mechanisms (support expansion, policy reshaping, behavioral consolidation), the central thesis about coordinated systems design, and any specific recommendations for combining RL and SFT."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1f3c848-b160-49d4-bdba-46ab2f2c5fde",
  "isSidechain": false,
  "requestId": "req_011CbTijHH5JT21z9FpAvFaD",
  "type": "assistant",
  "uuid": "7feb672d-f3c5-4232-8cdb-43fe47587bb4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015X8r9Uph3aeCUk64Upo6uz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1988,
      "cache_read_input_tokens": 55602,
      "output_tokens": 398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1988,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 398,
          "cache_read_input_tokens": 55602,
          "cache_creation_input_tokens": 1988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1988
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

_source line 42 · 2026-05-27T20:40:23.890Z_

<details><summary>↩ Tool result · `toolu_01Lhd5NXAVNXYniocFDnbdeg`</summary>

```text
# Paper Summary: LLM Self-Improvement Training Dynamics

**Full Title:** "Theoretical Modeling of Large Language Model Self-Improvement Training Dynamics Through Solver-Verifier Gap"

**Authors:** Yifan Sun, Yushan Liang, Zhen Zhang, Xin Liu, Jiaye Teng

## Key Findings

**Solver-Verifier Gap Theory:**
The researchers propose that performance gains in self-improvement stem from "the gap between LLM's solver capability and verifier capability." This gap serves as the central theoretical construct explaining how models enhance themselves without external training data.

**Training Dynamics Model:**
The paper presents a mathematical framework capturing the entire training trajectory. Rather than ad-hoc approaches, their theoretical model quantifies the capability ceiling of self-improvement by fitting predicted patterns to empirical results.

**Self-Improvement Saturation:**
The framework reveals that self-improvement performance eventually plateaus—suggesting models reach a natural limit based on their inherent solver-verifier differential.

**External Data Integration:**
A notable discovery involves limited external data: when scarce, "such external data can be utilized at any stage without significantly affecting final performances," aligning with observed empirical patterns across various LLMs and datasets.

The paper spans 37 pages and was last revised in February 2026, with testing across multiple language models and benchmark datasets validating the theoretical predictions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ccbf7c5-7579-4531-88b9-9904d19aafd5",
  "isSidechain": false,
  "promptId": "a6903394-624e-4492-ad19-36a9e5620d23",
  "type": "user",
  "uuid": "98bfd133-20da-43d7-87fc-cf408b5c8456",
  "toolUseResult": {
    "bytes": 47886,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: LLM Self-Improvement Training Dynamics\n\n**Full Title:** \"Theoretical Modeling of Large Language Model Self-Improvement Training Dynamics Through Solver-Verifier Gap\"\n\n**Authors:** Yifan Sun, Yushan Liang, Zhen Zhang, Xin Liu, Jiaye Teng\n\n## Key Findings\n\n**Solver-Verifier Gap Theory:**\nThe researchers propose that performance gains in self-improvement stem from \"the gap between LLM's solver capability and verifier capability.\" This gap serves as the central theoretical construct explaining how models enhance themselves without external training data.\n\n**Training Dynamics Model:**\nThe paper presents a mathematical framework capturing the entire training trajectory. Rather than ad-hoc approaches, their theoretical model quantifies the capability ceiling of self-improvement by fitting predicted patterns to empirical results.\n\n**Self-Improvement Saturation:**\nThe framework reveals that self-improvement performance eventually plateaus—suggesting models reach a natural limit based on their inherent solver-verifier differential.\n\n**External Data Integration:**\nA notable discovery involves limited external data: when scarce, \"such external data can be utilized at any stage without significantly affecting final performances,\" aligning with observed empirical patterns across various LLMs and datasets.\n\nThe paper spans 37 pages and was last revised in February 2026, with testing across multiple language models and benchmark datasets validating the theoretical predictions.",
    "durationMs": 4867,
    "url": "https://arxiv.org/abs/2507.00075"
  },
  "sourceToolAssistantUUID": "6ccbf7c5-7579-4531-88b9-9904d19aafd5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"FrontierCycle: Diagnostic-Guided Iterative RL↔Distillation Scheduling…",
  "leafUuid": "98bfd133-20da-43d7-87fc-cf408b5c8456",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise self-improvement framework for iterative LLM reasoning cycles",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---

### Tool result

_source line 45 · 2026-05-27T20:40:26.435Z_

<details><summary>↩ Tool result · `toolu_013Qp6EoxMByyG134SKVjbd7`</summary>

```text
# Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR

**Full Title:** Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR

**Authors:** Xiao Liang, Zhongzhi Li, Yeyun Gong, Yelong Shen, Ying Nian Wu, Zhijiang Guo, Weizhu Chen

## Key Findings

**The Core Problem:**
Standard RLVR training improves Pass@1 metrics but causes "policy entropy" decline, reducing generation variety and limiting Pass@k performance potential.

**The SvS Mechanism:**
The proposed Self-play with Variational problem Synthesis strategy addresses this by leveraging correct model solutions to generate alternative problem variants. Critically, "synthesized variational problems" maintain identical reference answers to original problems, enabling continuous self-improvement without additional labeling.

**Performance Gains:**
The method achieved substantial improvements on competitive mathematics benchmarks:
- **18.3% absolute gain** in Pass@32 on AIME24
- **22.8% absolute gain** in Pass@32 on AIME25
- Consistent benefits demonstrated across code generation tasks

**Entropy Preservation:**
By continuously augmenting and updating training problems during online learning, SvS effectively mitigates entropy collapse, sustaining generation diversity throughout training and enabling prolonged performance improvements across 12 benchmarks with models ranging from 3B to 32B parameters.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1f3c848-b160-49d4-bdba-46ab2f2c5fde",
  "isSidechain": false,
  "promptId": "a6903394-624e-4492-ad19-36a9e5620d23",
  "type": "user",
  "uuid": "07b639a8-a3b9-498d-b0a0-fe7cf6ebacd2",
  "toolUseResult": {
    "bytes": 47389,
    "code": 200,
    "codeText": "OK",
    "result": "# Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR\n\n**Full Title:** Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR\n\n**Authors:** Xiao Liang, Zhongzhi Li, Yeyun Gong, Yelong Shen, Ying Nian Wu, Zhijiang Guo, Weizhu Chen\n\n## Key Findings\n\n**The Core Problem:**\nStandard RLVR training improves Pass@1 metrics but causes \"policy entropy\" decline, reducing generation variety and limiting Pass@k performance potential.\n\n**The SvS Mechanism:**\nThe proposed Self-play with Variational problem Synthesis strategy addresses this by leveraging correct model solutions to generate alternative problem variants. Critically, \"synthesized variational problems\" maintain identical reference answers to original problems, enabling continuous self-improvement without additional labeling.\n\n**Performance Gains:**\nThe method achieved substantial improvements on competitive mathematics benchmarks:\n- **18.3% absolute gain** in Pass@32 on AIME24\n- **22.8% absolute gain** in Pass@32 on AIME25\n- Consistent benefits demonstrated across code generation tasks\n\n**Entropy Preservation:**\nBy continuously augmenting and updating training problems during online learning, SvS effectively mitigates entropy collapse, sustaining generation diversity throughout training and enabling prolonged performance improvements across 12 benchmarks with models ranging from 3B to 32B parameters.",
    "durationMs": 5067,
    "url": "https://arxiv.org/abs/2508.14029"
  },
  "sourceToolAssistantUUID": "f1f3c848-b160-49d4-bdba-46ab2f2c5fde",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-27T20:40:28.211Z_

<details><summary>↩ Tool result · `toolu_01445kUjdt6RDPtRNzQpsewy`</summary>

```text
# LLM Post-Training: Unified Framework Analysis

## Full Title
"Large Language Model Post-Training: A Unified View of Off-Policy and On-Policy Learning"

## Authors
Shiwan Zhao, Zhihu Wang, Xuyang Zhao, Jiaming Zhou, Caiyue Xu, Chenfei Liu, Liting Zhang, Yuhang Jia, Yanzhe Zhang, Hualong Yu, Zichen Xu, Qicheng Li, and Yong Qin

## Three Core Mechanisms

The paper identifies three primary behavioral interventions:

1. **Support Expansion**: Making useful behaviors more accessible to the model
2. **Policy Reshaping**: Improving behavior within already-reachable regions
3. **Behavioral Consolidation**: "preserves, transfers, and amortizes useful behavior across stages"

## Central Thesis

The authors argue that "progress increasingly depends on coordinated systems design rather than any single dominant objective." Rather than treating post-training methods in isolation, the framework emphasizes understanding them through trajectory provenance (off-policy vs. on-policy) and their functional roles.

## Multi-Stage Pipeline Composition

The paper characterizes hybrid pipelines as "coordinated multi-stage compositions," suggesting that effectiveness emerges from orchestrating different methods sequentially rather than relying on individual techniques.

## SFT and RL Integration

The framework indicates supervised fine-tuning can serve either support expansion or reshaping roles, while on-policy RL strengthens behavior on model-generated states. The synthesis implies combining these approaches strategically across stages based on specific bottlenecks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7feb672d-f3c5-4232-8cdb-43fe47587bb4",
  "isSidechain": false,
  "promptId": "a6903394-624e-4492-ad19-36a9e5620d23",
  "type": "user",
  "uuid": "759147b8-55f9-44bc-8dea-22131fff71e2",
  "toolUseResult": {
    "bytes": 50044,
    "code": 200,
    "codeText": "OK",
    "result": "# LLM Post-Training: Unified Framework Analysis\n\n## Full Title\n\"Large Language Model Post-Training: A Unified View of Off-Policy and On-Policy Learning\"\n\n## Authors\nShiwan Zhao, Zhihu Wang, Xuyang Zhao, Jiaming Zhou, Caiyue Xu, Chenfei Liu, Liting Zhang, Yuhang Jia, Yanzhe Zhang, Hualong Yu, Zichen Xu, Qicheng Li, and Yong Qin\n\n## Three Core Mechanisms\n\nThe paper identifies three primary behavioral interventions:\n\n1. **Support Expansion**: Making useful behaviors more accessible to the model\n2. **Policy Reshaping**: Improving behavior within already-reachable regions\n3. **Behavioral Consolidation**: \"preserves, transfers, and amortizes useful behavior across stages\"\n\n## Central Thesis\n\nThe authors argue that \"progress increasingly depends on coordinated systems design rather than any single dominant objective.\" Rather than treating post-training methods in isolation, the framework emphasizes understanding them through trajectory provenance (off-policy vs. on-policy) and their functional roles.\n\n## Multi-Stage Pipeline Composition\n\nThe paper characterizes hybrid pipelines as \"coordinated multi-stage compositions,\" suggesting that effectiveness emerges from orchestrating different methods sequentially rather than relying on individual techniques.\n\n## SFT and RL Integration\n\nThe framework indicates supervised fine-tuning can serve either support expansion or reshaping roles, while on-policy RL strengthens behavior on model-generated states. The synthesis implies combining these approaches strategically across stages based on specific bottlenecks.",
    "durationMs": 5598,
    "url": "https://arxiv.org/abs/2604.07941"
  },
  "sourceToolAssistantUUID": "7feb672d-f3c5-4232-8cdb-43fe47587bb4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-27T20:40:36.003Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research to write the pivoted proposal. Let me synthesize everything and write the full JSON.

Let me now carefully construct the complete JSON for FrontierLoop — the pivoted proposal that genuinely addresses "Synthetic Data and Self-Improvement for Mathematical Reasoning Training."

Key decisions:
1. This is a PIVOT from cross-model distillation to self-improvement
2. Core concept: diagnostic-guided adaptive scheduling of self-improvement cycles
3. Two modes: Data Generation (frontier expansion) and RL Training (consolidation)
4. Diagnostics: pass@k spectrum, entropy, difficulty-stratified scores, self-consistency divergence


5. The system operates entirely on self-generated rewards without relying on external teacher models

Writing the JSON structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "759147b8-55f9-44bc-8dea-22131fff71e2",
  "isSidechain": false,
  "requestId": "req_011CbTikGRFq78mc9LqEZLZM",
  "type": "assistant",
  "uuid": "b5d3646f-0580-4780-baa7-14edc033af7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUdJnPzwibRcqE6BivLSW5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1503,
      "cache_read_input_tokens": 57590,
      "output_tokens": 436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1503,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 436,
          "cache_read_input_tokens": 57590,
          "cache_creation_input_tokens": 1503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1503
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

_source line 48 · 2026-05-27T20:40:36.005Z_

Now I have comprehensive research. Let me synthesize everything and write the pivoted proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5d3646f-0580-4780-baa7-14edc033af7f",
  "isSidechain": false,
  "requestId": "req_011CbTikGRFq78mc9LqEZLZM",
  "type": "assistant",
  "uuid": "b6b2dccf-fcc9-4f50-bb00-ebcaa948bec3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUdJnPzwibRcqE6BivLSW5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1503,
      "cache_read_input_tokens": 57590,
      "output_tokens": 436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1503,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 436,
          "cache_read_input_tokens": 57590,
          "cache_creation_input_tokens": 1503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1503
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

_source line 49 · 2026-05-27T20:40:37.214Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01N2DyDK98CeAHkerq9FA3Vn`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.05004",
  "prompt": "Extract: full title, authors, key results on math benchmarks, the Challenger-Solver co-evolutionary mechanism, how many iterations, specific improvements per iteration, and the self-evolving data generation process."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6b2dccf-fcc9-4f50-bb00-ebcaa948bec3",
  "isSidechain": false,
  "requestId": "req_011CbTikGRFq78mc9LqEZLZM",
  "type": "assistant",
  "uuid": "0be37236-7159-47c5-8553-64a35f65b4c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUdJnPzwibRcqE6BivLSW5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1503,
      "cache_read_input_tokens": 57590,
      "output_tokens": 436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1503,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 436,
          "cache_read_input_tokens": 57590,
          "cache_creation_input_tokens": 1503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1503
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

_source line 50 · 2026-05-27T20:40:38.796Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BFz9xmaxiugMjUVgKEB7Pk`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.14970",
  "prompt": "Extract: full title, authors, key findings about self-evolving curriculum, the Multi-Armed Bandit formulation, specific results on AIME24 (+33%), and how difficulty selection is adaptive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0be37236-7159-47c5-8553-64a35f65b4c8",
  "isSidechain": false,
  "requestId": "req_011CbTikGRFq78mc9LqEZLZM",
  "type": "assistant",
  "uuid": "8b3a8b45-e9ba-49bc-8919-efffbe130049",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUdJnPzwibRcqE6BivLSW5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1503,
      "cache_read_input_tokens": 57590,
      "output_tokens": 436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1503,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 436,
          "cache_read_input_tokens": 57590,
          "cache_creation_input_tokens": 1503,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1503
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

_source line 51 · 2026-05-27T20:40:43.078Z_

<details><summary>↩ Tool result · `toolu_01N2DyDK98CeAHkerq9FA3Vn`</summary>

```text
# R-Zero: Self-Evolving Reasoning LLM Summary

**Full Title:**
"R-Zero: Self-Evolving Reasoning LLM from Zero Data"

**Authors:**
Chengsong Huang, Wenhao Yu, Xiaoyang Wang, Hongming Zhang, Zongxia Li, Ruosen Li, Jiaxin Huang, Haitao Mi, and Dong Yu

**Key Math Benchmark Results:**
The framework achieved a +6.49 point improvement on math-reasoning benchmarks when applied to the Qwen3-4B-Base model, with an additional +7.54 point gain on general-domain reasoning tasks.

**Challenger-Solver Co-evolutionary Mechanism:**
The system initializes two independent models with distinct purposes. The Challenger generates tasks at "the edge of the Solver capability," while the Solver tackles progressively harder challenges. Both models receive separate optimization and mutually improve through their interaction.

**Iterations and Per-Iteration Improvements:**
The provided content does not specify the number of iterations or detailed per-iteration performance metrics.

**Self-Evolving Data Generation:**
The framework operates "from scratch" without relying on pre-existing human-curated datasets. Rather than depending on "fine-tuning or reinforcement learning" with labeled data, it autonomously generates training materials through the competitive dynamic between the two models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0be37236-7159-47c5-8553-64a35f65b4c8",
  "isSidechain": false,
  "promptId": "a6903394-624e-4492-ad19-36a9e5620d23",
  "type": "user",
  "uuid": "b4b952bd-2516-4452-84b7-101def5d42d1",
  "toolUseResult": {
    "bytes": 48099,
    "code": 200,
    "codeText": "OK",
    "result": "# R-Zero: Self-Evolving Reasoning LLM Summary\n\n**Full Title:**\n\"R-Zero: Self-Evolving Reasoning LLM from Zero Data\"\n\n**Authors:**\nChengsong Huang, Wenhao Yu, Xiaoyang Wang, Hongming Zhang, Zongxia Li, Ruosen Li, Jiaxin Huang, Haitao Mi, and Dong Yu\n\n**Key Math Benchmark Results:**\nThe framework achieved a +6.49 point improvement on math-reasoning benchmarks when applied to the Qwen3-4B-Base model, with an additional +7.54 point gain on general-domain reasoning tasks.\n\n**Challenger-Solver Co-evolutionary Mechanism:**\nThe system initializes two independent models with distinct purposes. The Challenger generates tasks at \"the edge of the Solver capability,\" while the Solver tackles progressively harder challenges. Both models receive separate optimization and mutually improve through their interaction.\n\n**Iterations and Per-Iteration Improvements:**\nThe provided content does not specify the number of iterations or detailed per-iteration performance metrics.\n\n**Self-Evolving Data Generation:**\nThe framework operates \"from scratch\" without relying on pre-existing human-curated datasets. Rather than depending on \"fine-tuning or reinforcement learning\" with labeled data, it autonomously generates training materials through the competitive dynamic between the two models.",
    "durationMs": 5862,
    "url": "https://arxiv.org/abs/2508.05004"
  },
  "sourceToolAssistantUUID": "0be37236-7159-47c5-8553-64a35f65b4c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-27T20:40:44.309Z_

<details><summary>↩ Tool result · `toolu_01BFz9xmaxiugMjUVgKEB7Pk`</summary>

```text
# Self-Evolving Curriculum for LLM Reasoning

**Full Title:** "Self-Evolving Curriculum for LLM Reasoning"

**Authors:** Xiaoyin Chen, Jiarui Lu, Minsu Kim, Dinghuai Zhang, Jian Tang, Alexandre Piché, Nicolas Gontier, Yoshua Bengio, Ehsan Kamalloo

## Key Findings

**Self-Evolving Curriculum (SEC) Approach:**
The method automatically learns a curriculum policy during RL fine-tuning. The system treats training "as a non-stationary Multi-Armed Bandit problem, treating each problem category as an individual arm." This formulation enables dynamic selection of which problem types to present during training.

**Learning Mechanism:**
The curriculum leverages "the absolute advantage from policy gradient methods as a proxy measure for immediate learning gain." The policy updates occur via TD(0) method at each training step.

**Demonstrated Results:**
Testing across three reasoning domains—planning, inductive reasoning, and mathematics—showed SEC enables enhanced reasoning capabilities with "better generalization to harder, out-of-distribution test problems." The method also achieves improved skill balance when training on multiple domains simultaneously.

**Note:** The specific AIME24 (+33%) result mentioned in your query does not appear in the provided abstract or metadata. The document confirms improved performance broadly but doesn't cite that particular benchmark in the displayed content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b3a8b45-e9ba-49bc-8919-efffbe130049",
  "isSidechain": false,
  "promptId": "a6903394-624e-4492-ad19-36a9e5620d23",
  "type": "user",
  "uuid": "3ce5a1e7-25be-4c50-9c01-45ea80efd193",
  "toolUseResult": {
    "bytes": 48086,
    "code": 200,
    "codeText": "OK",
    "result": "# Self-Evolving Curriculum for LLM Reasoning\n\n**Full Title:** \"Self-Evolving Curriculum for LLM Reasoning\"\n\n**Authors:** Xiaoyin Chen, Jiarui Lu, Minsu Kim, Dinghuai Zhang, Jian Tang, Alexandre Piché, Nicolas Gontier, Yoshua Bengio, Ehsan Kamalloo\n\n## Key Findings\n\n**Self-Evolving Curriculum (SEC) Approach:**\nThe method automatically learns a curriculum policy during RL fine-tuning. The system treats training \"as a non-stationary Multi-Armed Bandit problem, treating each problem category as an individual arm.\" This formulation enables dynamic selection of which problem types to present during training.\n\n**Learning Mechanism:**\nThe curriculum leverages \"the absolute advantage from policy gradient methods as a proxy measure for immediate learning gain.\" The policy updates occur via TD(0) method at each training step.\n\n**Demonstrated Results:**\nTesting across three reasoning domains—planning, inductive reasoning, and mathematics—showed SEC enables enhanced reasoning capabilities with \"better generalization to harder, out-of-distribution test problems.\" The method also achieves improved skill balance when training on multiple domains simultaneously.\n\n**Note:** The specific AIME24 (+33%) result mentioned in your query does not appear in the provided abstract or metadata. The document confirms improved performance broadly but doesn't cite that particular benchmark in the displayed content.",
    "durationMs": 5511,
    "url": "https://arxiv.org/abs/2505.14970"
  },
  "sourceToolAssistantUUID": "8b3a8b45-e9ba-49bc-8919-efffbe130049",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-27T20:41:11.564Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have all the research I need. Now let me write the complete pivoted proposal JSON. This is a major pivot from cross-model distillation to self-improvement, which directly addresses the user's original request for "Synthetic Data and Self-Improvement for Mathematical Reasoning Training."

Let me write each section carefully now.

For the core_problem, I need to be precise about what's missing in the self-improvement literature.

For the landscape, I need to properly position against STaR, ReST-EM, Absolute Zero, R-Zero, SIRI, and the diagnostic tools literature.


I'm ready to draft the proposal now. Before I do, I want to nail down the novelty claim—what exactly makes FrontierLoop distinct from existing approaches. STaR uses a fixed schedule with SFT-only training, while ReST-EM applies EM-style iteration but also with a fixed curriculum. I need to articulate how FrontierLoop's adaptive frontier-based approach differs fundamentally from these. 2-3 iterations
3. **Absolute Zero (2025)**: Self-play with proposer+solver, but no adaptive scheduling
4. **R-Zero (2025)**: Challenger targets solver's weaknesses (some difficulty awareness), but fixed iterations
5. **HS-STaR (2025)**: Difficulty-aware sampling within STaR, but doesn't address generation/training balance
6. **B-STaR**: Balance score within iterations, but not cross-iteration scheduling
7. **SEC (2025)**: MAB for problem category selection within RL, but within fixed training, not across modes
8. **SvS (2025)**: Variational problem synthesis during RLVR, but continuous not phased
9. **SIRI (2025)**: Iterative cycling of rollout length within RL, but doesn't alternate between data generation and training
10. **HSIR/Better,Faster (2026)**: Efficient self-improvement via verify-then-exit, but within fixed loop
11. **DART-Math (2024)**: Difficulty-aware rejection sampling, but static not adaptive
12. **MathSmith (2025)**: RL-optimized problem generation, but doesn't adaptively schedule when to generate vs. train

The real gap I'm identifying is that no existing approach uses live frontier diagnostics—like pass@k distributions, entropy measures, and difficulty stratification—to make phase-level decisions about when to switch between data generation and RL training modes. SEC comes closest with its multi-armed bandit approach for problem selection, but that operates within a single training run rather than orchestrating higher-level mode transitions. FrontierLoop is designed to make exactly those kinds of decisions: determining whether to be actively generating synthetic data or focused on RL training at any given point.

Writing the JSON structure now with the core framing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ce5a1e7-25be-4c50-9c01-45ea80efd193",
  "isSidechain": false,
  "requestId": "req_011CbTimTEfKU4XkiJRkgaeZ",
  "type": "assistant",
  "uuid": "479b2b67-98d4-48ba-aa4d-ede03773f61e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hhLmtJE5eTGphR2CqTcTX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 59093,
      "output_tokens": 12828,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1130,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12828,
          "cache_read_input_tokens": 59093,
          "cache_creation_input_tokens": 1130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1130
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

_source line 54 · 2026-05-27T20:45:29.746Z_

Now I have all the research needed for a comprehensive pivot. Let me write the complete revised proposal.

```json
{
  "title": "FrontierLoop: Diagnostic-Guided Adaptive Self-Improvement Cycling for Mathematical Reasoning",
  "change_type": "pivot",
  "core_problem": "Self-improvement methods for mathematical reasoning — where the model generates its own synthetic training data and improves without an external teacher — follow FIXED iteration schedules despite operating in a non-stationary learning landscape. STaR (NeurIPS 2022) generates rationales, filters for correctness, and fine-tunes for a predetermined number of iterations. ReST-EM (Google DeepMind, 2023) formalizes this as Expectation-Maximization but observes diminishing returns after exactly 2-3 iterations without understanding WHY or WHEN to stop. Self-play methods (Absolute Zero, arXiv 2505.03335; R-Zero, arXiv 2508.05004) use fixed iteration structures despite the model's learning needs changing across iterations.\n\nThis fixed scheduling is suboptimal for three compounding reasons:\n\n(1) CHANGING MODEL NEEDS: Early in self-improvement, the model benefits from broad data generation across difficulty levels. As training progresses, the model masters easy problems and needs targeted data at its capability frontier — the 'boundary-level' problems that HS-STaR (EMNLP 2025, arXiv 2505.19866) shows offer maximal learning utility. DART-Math (NeurIPS 2024, arXiv 2407.13690) demonstrates that standard generation has severe bias toward easy queries, wasting compute on problems the model has already mastered. But the frontier shifts during training, so static difficulty targeting is itself insufficient.\n\n(2) UNPREDICTABLE SATURATION AND COLLAPSE: 'Can Large Reasoning Models Self-Train?' (arXiv 2505.21444) shows that prolonged self-training leads to reward hacking and sudden complete performance collapse — but the onset is unpredictable and varies by model and dataset. ReST-EM's diminishing returns after 2-3 iterations may be premature stopping (the model could benefit from more cycles with targeted data) or too late (collapse has already begun). The model collapse literature (Shumailov et al., Nature 2024) establishes that iterative training on self-generated data degrades distribution tails, with 'Strong Model Collapse' (ICLR 2025) showing this persists even with mixed real/synthetic data.\n\n(3) MISALIGNED GENERATION↔TRAINING BALANCE: RLVR (GRPO) improves pass@1 (sampling efficiency) but has limited capacity to expand the pass@k reasoning frontier beyond the base model (arXiv 2504.13837, NeurIPS 2025 Best Paper Runner-Up). This means RL phases eventually saturate and new synthetic data is needed to expand the frontier before RL can consolidate further. Conversely, generating too much data without sufficient RL consolidation wastes compute — the model needs to absorb existing knowledge before benefiting from new examples. The optimal balance between generation and training changes as the model improves, but no existing method adapts this balance.\n\nCritically, the DIAGNOSTIC TOOLS to address these limitations already exist but have never been combined into a self-improvement scheduling framework: pass@k predicts RL outcomes with R² up to 0.88 (Quagmires, arXiv 2510.01624, NeurIPS 2025 MATH-AI Workshop); pass@k serves as an active training signal at per-step granularity (Pass@k Training, arXiv 2508.10751); entropy trajectory signals collapse (Entrocraft, arXiv 2604.26326; EntroPIC, arXiv 2511.15248); the generation-verification gap determines self-improvement potential and scales monotonically with pre-training compute (Mind the Gap, arXiv 2412.02674, ICLR 2025); the solver-verifier gap predicts self-improvement trajectories as exponential curves toward a computable limit (arXiv 2507.00075). These diagnostic signals, developed for RLVR optimization and distillation, are even MORE valuable for self-improvement scheduling because self-improvement has higher collapse risk, self-generated data quality varies more than teacher-generated data, and the optimal generation↔training balance changes as the model improves.",
  "opportunity": "We propose FrontierLoop: the first diagnostic-guided adaptive scheduling framework for self-improvement cycles in mathematical reasoning. FrontierLoop uses frontier diagnostics — pass@k spectrum, entropy trajectory, difficulty-stratified performance — to make real-time phase-level decisions: WHEN to generate new synthetic data, WHAT difficulty to target, WHEN to switch to RL training, and WHEN to stop.\n\nFour specific limitations of existing methods create this opportunity:\n\n(a) FIXED ITERATION COUNTS: STaR and ReST-EM use predetermined iteration counts (typically 2-3). Mind the Gap (ICLR 2025) shows that self-improvement potential is governed by the generation-verification gap, which varies by model, task, and training stage — a fixed count cannot adapt to this. The solver-verifier gap theory (arXiv 2507.00075) models self-improvement as an exponential curve toward a limit, but the curve's parameters change across iterations as the model's distribution shifts.\n\n(b) NO COLLAPSE DETECTION: Self-training can lead to reward hacking and complete collapse (arXiv 2505.21444), but no self-improvement method monitors for collapse in real time. R-Diverse (arXiv 2602.13103) identifies 'Diversity Illusion' — where training signals appear diverse but collapse into recurring patterns — but addresses this within self-play, not through scheduled diagnostics.\n\n(c) UNIFORM DATA GENERATION: Existing methods generate data uniformly across difficulty levels (STaR) or with static difficulty heuristics (DART-Math). Self-Evolving Curriculum (SEC, arXiv 2505.14970) uses MAB for adaptive category selection within a single RL run, but does not make the higher-level decision of whether to generate data AT ALL vs. train on existing data.\n\n(d) NO GENERATION↔TRAINING SCHEDULING: SvS (Beyond Pass@1, arXiv 2508.14029) performs variational problem synthesis continuously during RLVR — at every step regardless of whether new data is needed. SIRI (arXiv 2509.25176) cycles rollout length within RL but doesn't alternate between data generation and training modes. Neither uses diagnostics to determine WHEN generation is productive vs. wasteful.\n\nFrontierLoop's value proposition is COMPUTE EFFICIENCY: by generating data only when diagnostics indicate frontier stagnation, and targeting generation at the specific difficulty bands where the model is stuck, FrontierLoop avoids wasting compute on redundant data generation while preventing premature stopping. The theoretical grounding comes from three validated principles: (i) pass@k captures the model's latent capability that RL can consolidate (Quagmires); (ii) entropy trajectory predicts training stability (Entrocraft); (iii) the generation-verification gap determines the ceiling of self-improvement (Mind the Gap), providing a principled stopping criterion.",
  "landscape": "FOUNDATIONAL SELF-IMPROVEMENT METHODS:\n\nSTaR (arXiv 2203.14465, NeurIPS 2022, Zelikman et al.) is the foundational iterative self-improvement method: generate chain-of-thought rationales, filter for correctness, fine-tune, repeat. Includes 'rationalization' — providing the correct answer as a hint for failed problems. Demonstrated improvements on GSM8K and CommonsenseQA. FrontierLoop extends STaR's generate→filter→train loop with diagnostic-guided scheduling and RL-based training.\n\nReST-EM (Beyond Human Data, arXiv 2312.06585, Google DeepMind, 2023) formalizes self-training as Expectation-Maximization: generate samples (E-step), filter by correctness (M-step), iterate. On MATH and APPS with PaLM-2, model-generated data yielded larger gains than human-written data. Critical observation: diminishing returns after 2-3 iterations. FrontierLoop addresses this by using diagnostics to determine whether diminishing returns signal genuine saturation or suboptimal data targeting.\n\nV-STaR (arXiv 2402.06457, 2024) trains a DPO-based verifier on BOTH correct and incorrect solutions from the STaR loop. 7B V-STaR surpasses LLaMA2 70B on GSM8K. FrontierLoop could incorporate V-STaR's verifier as an enhanced filtering mechanism during generation phases.\n\nSELF-PLAY AND ZERO-DATA METHODS:\n\nAbsolute Zero (arXiv 2505.03335, 2025) achieves SOTA on coding and math reasoning with ZERO external data via self-play: a single model proposes tasks and solves them, with code execution as the sole verifiable reward. R-Zero (arXiv 2508.05004, 2025) uses a Challenger-Solver co-evolutionary framework, achieving +6.49 points on math benchmarks with Qwen3-4B-Base over 3 iterations. R-Diverse (arXiv 2602.13103, Feb 2026) identifies 'Diversity Illusion' in self-play and proposes Memory-Augmented Penalty and Skill-Aware Measurement. 'Towards Understanding Self-play for LLM Reasoning' (arXiv 2510.27072, NeurIPS 2025) finds self-play capacity is bounded by the base model and the proposer is the critical component.\n\nFrontierLoop differs from self-play methods in two ways: (1) we use adaptive diagnostic-guided scheduling rather than fixed iteration structures; (2) our framework is agnostic to the data generation mechanism — it can use self-play (Absolute Zero-style), solution sampling (STaR-style), or problem synthesis (MathSmith-style) during generation phases, with the diagnostic module determining which is most productive.\n\nITERATIVE CYCLING METHODS — CLOSEST PRIOR WORK:\n\nSIRI (arXiv 2509.25176, Wen et al., 2025) is the closest existing iterative cycling method for math reasoning. SIRI performs 3 iterations of compression↔expansion cycling during RL, oscillating rollout length between 8,192 and 16,384 tokens via a cosine scheduler. On AIME24, SIRI-low achieves 40.4% accuracy (vs. 28.2% baseline) with 46.9% token reduction. CRITICAL DIFFERENTIATION: SIRI cycles WITHIN RL (varying rollout length to control reasoning conciseness), while FrontierLoop cycles BETWEEN modes (data generation vs. RL training). SIRI does not generate new training data — it varies the RL training configuration. FrontierLoop could incorporate SIRI's compression↔expansion within its RL phases while adding the higher-level generation↔training scheduling.\n\nReMiT (arXiv 2602.03075, Feb 2026) performs iterative mid-training ↔ RL cycling, showing cascading improvements across two cycles (ReMiT → ReMiT2). While ReMiT operates at the pre-training ↔ post-training boundary, it validates that iterative cycling can compound.\n\nBeyond Pass@1 / SvS (arXiv 2508.14029, Liang et al., 2025) synthesizes variational problems from correct solutions during RLVR, achieving +18.3% and +22.8% pass@32 on AIME24/AIME25. SvS performs continuous problem synthesis at every training step. FrontierLoop's key difference: diagnostic-gated generation — synthesize new data only when frontier diagnostics indicate stagnation, saving compute when the current data pool is sufficient.\n\nDIAGNOSTIC TOOLS AND SIGNALS:\n\nQuagmires in SFT-RL Post-Training (arXiv 2510.01624, NeurIPS 2025 MATH-AI Workshop) trained hundreds of models up to 12B and found pass@64/pass@256 predict RL outcomes with R² up to 0.88 (2× over SFT score prediction). Used as a STATIC pre-RL predictor; FrontierLoop extends to DYNAMIC real-time monitoring during training.\n\nPass@k Training (arXiv 2508.10751, ByteDance/RUC) uses pass@k directly as a per-step reward to balance exploration and exploitation, achieving 17.9% vs. 12.9% Pass@1 on Enigmata for Qwen2.5-7B. This validates pass@k as an active signal at per-step granularity; FrontierLoop uses it at phase-level diagnostic granularity for mode switching — complementary applications at different scales.\n\nEntrocraft (arXiv 2604.26326, 2026) achieves ~17% improvement in pass@32 over GRPO through entropy-guided rejection sampling against a target entropy schedule. EntroPIC (arXiv 2511.15248, 2025) uses PID control to maintain target entropy during RLVR. Both validate entropy trajectory as a training stability diagnostic. FrontierLoop incorporates entropy monitoring as a collapse detection signal, using deviations from the expected entropy schedule to trigger mode switching.\n\nCover@tau (Beyond Pass@k, arXiv 2510.08325, 2025) measures the fraction of solvable problems where at least tau proportion of completions are correct, capturing genuine reasoning reliability vs. lucky sampling. More informative than raw pass@k for FrontierLoop's difficulty-stratified diagnostics.\n\nSELF-IMPROVEMENT THEORY:\n\nMind the Gap (arXiv 2412.02674, ICLR 2025) formalizes self-improvement through the 'generation-verification gap' — when models verify better than they generate, self-improvement is possible. This gap scales monotonically with pre-training compute. Provides FrontierLoop's theoretical stopping criterion: when diagnostics indicate the generation-verification gap has narrowed to zero for a difficulty band, further self-improvement on that band is impossible.\n\nSolver-Verifier Gap Theory (arXiv 2507.00075, 2025) models self-improvement as an exponential curve toward a limit determined by the solver-verifier gap. Validated across multiple models and datasets. Key finding: external data can be introduced at any stage without significantly affecting final performance — supporting FrontierLoop's flexible scheduling.\n\n'Can Large Reasoning Models Self-Train?' (arXiv 2505.21444, Shafayat et al., 2025) demonstrates both the promise and peril: self-training improves reasoning and feedback quality, but prolonged training causes reward hacking and complete collapse. FrontierLoop's collapse detection module directly addresses this.\n\nDoes RL Really Incentivize Reasoning Beyond the Base Model? (arXiv 2504.13837, NeurIPS 2025 Best Paper Runner-Up) shows RLVR improves pass@1 but does NOT expand pass@k frontier. This is FrontierLoop's central motivation: when RL reaches its pass@k ceiling, diagnostic-triggered data generation is needed to expand the frontier.\n\nDIFFICULTY-AWARE AND EFFICIENT METHODS:\n\nDART-Math (arXiv 2407.13690, NeurIPS 2024) identifies severe easy-query bias in standard generation and proposes Difficulty-Aware Rejection Sampling (DARS). HS-STaR (arXiv 2505.19866, EMNLP 2025) uses hierarchical pre-sampling with difficulty estimation to reallocate sampling budget toward 'boundary-level' problems. Self-Evolving Curriculum / SEC (arXiv 2505.14970, Chen, Bengio et al., 2025) formulates curriculum selection as a non-stationary MAB problem. MathSmith (arXiv 2508.05592, 2025) uses RL to optimize synthetic problem generation, jointly optimizing structural validity, reasoning complexity, and answer consistency.\n\nFrontierLoop integrates insights from all four: DART-Math's difficulty awareness informs generation targeting; HS-STaR's boundary-level concept motivates frontier-difficulty generation; SEC's MAB formulation could enhance within-generation difficulty selection; MathSmith's RL-optimized generation is a candidate mechanism for FrontierLoop's generation phase.\n\nHSIR / 'Better, Faster' (arXiv 2605.24998, May 2026) proposes verify-then-exit sampling and an Intrinsic Diversity score, achieving +10.9% performance with 42.4% less inference overhead. Orthogonal to FrontierLoop — HSIR improves efficiency WITHIN a self-improvement iteration; FrontierLoop optimizes scheduling ACROSS iterations. The two are composable.\n\nRL on Incorrect Synthetic Data (arXiv 2406.14532, NeurIPS 2024) shows RL on incorrect traces is 8× more efficient than training on correct data alone. Motivates using both correct (for SFT/generation phase) and incorrect (for RL phase) self-generated data.\n\nTHEORETICAL FOUNDATIONS FOR MULTI-STAGE DESIGN:\n\n'Large Language Model Post-Training: A Unified View' (arXiv 2604.07941, Zhao et al., Apr 2026) identifies three mechanisms structuring all post-training: support expansion, policy reshaping, and behavioral consolidation. FrontierLoop's two modes map directly: Generation Mode = support expansion (making new behaviors accessible), RL Mode = policy reshaping (improving within reachable regions). The paper's central thesis — 'progress increasingly depends on coordinated systems design' — provides theoretical justification for FrontierLoop's diagnostic-guided orchestration.\n\n'Decoupling KL and Trajectories' (arXiv 2605.16826, May 2026) shows SFT, DAgger, offline RL, and OPD are points in a continuous design space defined by prefix source × KL direction. 'Post-Training is About States, Not Tokens' (arXiv 2605.22731, May 2026) argues state distribution — not loss function — is the primary differentiator of post-training methods. Both support FrontierLoop's approach: rather than claiming any single objective is optimal, we adaptively schedule modes that operate on different state distributions (model-generated for RL, frontier-targeted for generation).\n\nCLPD (arXiv 2605.11260, May 2026) addresses teacher scheduling by progressively scheduling teachers of increasing capacity. PRISM (arXiv 2604.28123, Apr 2026) inserts distribution-alignment stages between SFT and RL. Both address multi-stage pipeline design but for supervised/distillation settings; FrontierLoop targets the pure self-improvement setting.\n\nMATH-Beyond (arXiv 2510.11653, 2025) quantifies the RL/distillation frontier gap for mathematics. ProRL (NeurIPS 2025, arXiv 2505.24864) shows RL achieves substantial frontier expansion on logic puzzles (+54.8%) but limited expansion on math. 'Self-Improvement of Large Language Models: A Technical Overview' (arXiv 2603.25681, Mar 2026) surveys the field through the GRO (Generation-Reward-Optimization) framework. 'Limits of Generalization in RLVR' (arXiv 2510.27044, 2025) cautions that RLVR may reinforce superficial heuristics — motivating FrontierLoop's difficulty-stratified diagnostics that can detect whether improvements are genuine.",
  "inspired_by": "foundational_insight[RLVR doesn't expand pass@k frontier: arXiv 2504.13837 → new data needed to break ceilings] + validated_principle[pass@k predicts RL outcomes: Quagmires R²=0.88] + active_signal[Pass@k Training: pass@k as per-step reward; we extend to phase-level diagnostic] + theoretical_foundation[generation-verification gap enables self-improvement and scales with compute: Mind the Gap, ICLR 2025] + theoretical_model[solver-verifier gap predicts self-improvement trajectory: arXiv 2507.00075] + collapse_understanding[self-training collapses from reward hacking: arXiv 2505.21444 → need real-time diagnostics] + entropy_management[Entrocraft + EntroPIC validate entropy as stability diagnostic] + difficulty_awareness[DART-Math + HS-STaR: boundary problems offer maximal learning utility] + frontier_synthesis[SvS: +18.3%/+22.8% pass@32 via variational problem synthesis] + cycling_evidence[SIRI: 3 iterations of compression↔expansion improve AIME24 by 43%; ReMiT: cascading improvements across cycles] + systems_design[Unified View: 'progress depends on coordinated systems design' → diagnostic-guided orchestration] + adaptive_curriculum[SEC: MAB for problem category selection → extend to mode-level scheduling]",
  "approach": "We propose FrontierLoop, the first diagnostic-guided adaptive scheduling framework for self-improvement cycles in mathematical reasoning. FrontierLoop operates in the PURE SELF-IMPROVEMENT REGIME: no external teacher model — the student generates its own synthetic data (reasoning traces and problems), with only a mathematical answer verifier as the external component (standard for RLVR). The core contribution is the SCHEDULING FRAMEWORK — a general mechanism for adaptively orchestrating when to generate new synthetic data, what difficulty to target, when to consolidate via RL, and when to stop — rather than any specific diagnostic metric.\n\nARCHITECTURAL OVERVIEW: FrontierLoop alternates between two modes, with transitions governed by a diagnostic module:\n\nMODE 1 — GENERATION (Frontier Expansion / Support Expansion): Generate new synthetic training data targeted at the model's current capability frontier. Three generation mechanisms, selectable by the scheduler: (a) SOLUTION SAMPLING: for problems at the frontier difficulty, generate K solutions, filter for correctness (STaR-style), add to data pool; (b) VARIATIONAL PROBLEM SYNTHESIS: from existing correct solutions, synthesize structurally diverse problem variants with identical reference answers (SvS-inspired, arXiv 2508.14029); (c) RL-GUIDED PROBLEM GENERATION: use the model's own capabilities to generate new problems at target difficulty (MathSmith-inspired, arXiv 2508.05592). Difficulty targeting uses the Difficulty-Stratified Frontier Score (DSFS) to identify which difficulty bands have stalling pass@k.\n\nMODE 2 — RL TRAINING (Consolidation / Policy Reshaping): Standard GRPO-based RLVR on the accumulated self-generated data pool. Entropy management via Entrocraft-style annealing schedule to prevent premature collapse. Both correct and incorrect self-generated traces are used: correct for positive rewards, incorrect for learning from errors (motivated by arXiv 2406.14532 showing RL on incorrect data is 8× more efficient).\n\nDIAGNOSTIC MODULE: Evaluated on a compact held-out validation set (200 problems stratified by difficulty) every 100 training steps, computing:\n\n(1) SAMPLING EFFICIENCY GAP (SEG) = pass@k − pass@1 (k=32): When SEG is large, the model has latent capability that RL can consolidate. When SEG is small AND pass@k is low, the model needs new data. Building on Quagmires' validation (pass@k predicts RL outcomes, R²=0.88) and Pass@k Training's validation (pass@k as active signal).\n\n(2) DIFFICULTY-STRATIFIED FRONTIER SCORE (DSFS): Group validation problems into difficulty bands (easy/medium/hard/competition). Compute pass@32 for each band. Identify bands where pass@32 has stalled — these are where generation should target. Extends HS-STaR's 'boundary-level' concept from static pre-sampling to dynamic real-time targeting.\n\n(3) ENTROPY TRAJECTORY: Policy entropy during RL training, compared against an expected annealing schedule. Entropy dropping below threshold despite regularization signals incipient collapse — trigger generation mode with temperature boost for diversity injection. Validated by Entrocraft and EntroPIC.\n\n(4) SELF-CONSISTENCY DIVERGENCE (SCD): Gap between self-consistency accuracy (majority vote over K samples) and true accuracy (verified against ground truth). When self-consistency rises but true accuracy plateaus or drops, reward hacking is occurring (per arXiv 2505.21444). Trigger: pause training, evaluate, reduce RL intensity.\n\nADAPTIVE SCHEDULER — MODE SWITCHING LOGIC: Uses z-score-normalized thresholds (inspired by ZClip, arXiv 2504.02507) for cross-phase comparability:\n- IF SEG is small (z < −1) AND pass@k_large stagnant (growth < ε per 500 steps) → Switch to GENERATION MODE (frontier exhausted, need new data)\n- IF SEG is large (z > 0) AND entropy healthy (above schedule) → Stay in / switch to RL MODE (consolidate frontier into pass@1)\n- IF entropy drops below 0.8× scheduled value → DIVERSITY INJECTION: generation with elevated temperature (1.2-1.5) targeting frontier difficulty\n- IF SCD exceeds threshold (self-consistency diverging from ground truth) → EMERGENCY PAUSE: checkpoint, evaluate on held-out test, reduce RL learning rate\n- IF pass@32 stagnant across ALL difficulty bands for 3 consecutive evaluations → STOP (generation-verification gap exhausted per Mind the Gap theory)\n\nTHEORETICAL GROUNDING: FrontierLoop's two modes map directly to the mechanisms identified in the Unified View of Post-Training (arXiv 2604.07941): Generation Mode performs SUPPORT EXPANSION (making new behaviors accessible by introducing training data at the frontier), while RL Mode performs POLICY RESHAPING (improving pass@1 within the currently reachable behavior space). The Unified View's thesis — 'progress increasingly depends on coordinated systems design' — motivates diagnostic-guided orchestration over fixed sequencing.\n\nEXPERIMENTAL PLAN:\n\nSTAGE 0 — DIAGNOSTIC SIGNAL VALIDATION (1.5 weeks): Run a standard 3-iteration STaR loop on Qwen3-8B (or DeepSeek-R1-Distill-Qwen3-8B), logging ALL four candidate diagnostics at every checkpoint. Analyze: (a) which signal best correlates with subsequent learning gain, (b) signal-to-noise ratio, (c) lead time (how early does each signal detect stagnation/collapse). Select the best diagnostic combination for subsequent stages.\n\nSTAGE 0.5 — CYCLING VALIDATION GATE (1.5 weeks): Single-cycle test: (i) RL training until diagnostic indicates frontier exhaustion → plateau pass@32 = P1; (ii) Difficulty-targeted generation → create new frontier data; (iii) Second RL phase → measure pass@32 = P2. GO/NO-GO: If P2 > P1 + 1pp on MATH-500, cycling validated → proceed to Stage 1. If P2 ≤ P1 + 1pp, cycling has no frontier expansion value → PIVOT to optimizing single-iteration diagnostic-guided self-improvement (still novel: when to stop generating, what difficulty to target, when to stop training). Either outcome produces a publishable contribution.\n\nSTAGE 1 — FULL EXPERIMENTS (4-5 weeks): If cycling validated: run FrontierLoop for up to 5 adaptive cycles, with the scheduler determining each phase's duration and the total number of cycles. If cycling invalidated: optimize single-iteration self-improvement with diagnostic-guided generation targeting and early stopping.\n\nCORE BASELINES (6): (1) STaR with fixed 3 iterations — foundational comparison; (2) ReST-EM with fixed 2 iterations; (3) Pure RLVR (GRPO, no explicit generation phase); (4) Absolute Zero self-play (Zhao et al., 2025); (5) Fixed-interval cycling — generate every 2000 steps regardless of diagnostics (ablates the diagnostic guidance); (6) SvS-style continuous problem synthesis during RLVR.\n\nKEY ABLATIONS (5): (1) Diagnostic signal comparison within FrontierLoop (SEG vs. entropy vs. DSFS vs. combined); (2) Adaptive vs. fixed scheduling (same total compute, different allocation); (3) Targeted vs. uniform difficulty in data generation; (4) With vs. without collapse prevention module; (5) Compute efficiency analysis: H100-hours per percentage point improvement.\n\nEVALUATION: MATH-500, AIME 2024, LiveCodeBench. Report pass@1, pass@32, per-difficulty breakdowns, compute efficiency (H100-hours per point), number of adaptive cycles used, and collapse/divergence events. Additionally report Cover@tau (arXiv 2510.08325) for reasoning reliability.\n\nCOMPUTE ADVANTAGE: FrontierLoop operates entirely in the self-improvement regime — no expensive external teacher. All generation and training use the same 8B model. The diagnostic module adds ~15% compute overhead (pass@32 on 200 problems every 100 steps ≈ 15 min on 1×H100). The primary compute savings come from: (a) not generating redundant data when the current pool is sufficient (estimated 20-30% savings over fixed-schedule generation); (b) early stopping when diagnostics detect saturation or collapse (preventing wasted RL compute); (c) targeted generation at frontier difficulty (fewer samples needed per iteration than uniform generation, per DART-Math's findings).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "1400-1800 H100-hours: RL training (~400), self-data generation (~200), pass@32 diagnostics (~100), Stage 0 signal comparison (~100), Stage 0.5 cycling validation (~100), baselines (~400), ablations (~200), buffer (~200)",
      "timeline": "13-16 weeks (1.5 weeks Stage 0, 1.5 weeks Stage 0.5 + go/no-go, 2 weeks implementation, 4-5 weeks experiments, 2 weeks ablations, 2-3 weeks writing)",
      "estimated_gpu_cost": "$2,800-3,600 at $2/H100-hr"
    },
    "human_in_loop": {
      "gpu_hours": "1100-1400 H100-hours (Claude assists with veRL integration, diagnostic module implementation, automated Stage 0.5 analysis)",
      "timeline": "10-13 weeks (1 week Stage 0, 1 week Stage 0.5, 1.5 weeks implementation, 4-5 weeks experiments, 1.5 weeks ablations, 2 weeks writing)",
      "claude_api_cost": "$300-500",
      "estimated_gpu_cost": "$2,200-2,800 at $2/H100-hr"
    },
    "auto_research": {
      "gpu_hours": "900-1200 H100-hours (automated diagnostic sweep, adaptive experiment scheduling, Stage 0.5 as automated gate)",
      "timeline": "8-11 weeks (0.5 weeks Stage 0, 0.5 weeks Stage 0.5, 1.5 weeks implementation, 3-5 weeks automated runs, 1-2 weeks paper generation)",
      "claude_api_cost": "$500-800",
      "estimated_gpu_cost": "$1,800-2,400 at $2/H100-hr",
      "speed_bottleneck": "Pass@32 evaluation on 200-problem diagnostic set takes ~15 min per checkpoint on 1×H100; no external teacher bottleneck"
    }
  },
  "target_venues": [
    "ICLR 2027 (submission deadline: Sep 24, 2026 — ~17 weeks from now)",
    "ARR October 2026 cycle (submission: Oct 12, 2026 — ~20 weeks) for commitment to EACL 2027 or NAACL 2027"
  ],
  "level": "solid",
  "key_references": [
    "STaR: Self-Taught Reasoner — Bootstrapping Reasoning With Reasoning (arXiv 2203.14465, NeurIPS 2022)",
    "Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models — ReST-EM (arXiv 2312.06585, Google DeepMind 2023)",
    "V-STaR: Training Verifiers for Self-Taught Reasoners (arXiv 2402.06457, 2024)",
    "Absolute Zero: Reinforced Self-play Reasoning with Zero Data (arXiv 2505.03335, 2025)",
    "R-Zero: Self-Evolving Reasoning LLM from Zero Data (arXiv 2508.05004, 2025)",
    "R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training (arXiv 2602.13103, Feb 2026)",
    "Towards Understanding Self-play for LLM Reasoning (arXiv 2510.27072, NeurIPS 2025)",
    "Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models (arXiv 2412.02674, ICLR 2025)",
    "Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap (arXiv 2507.00075, 2025)",
    "Can Large Reasoning Models Self-Train? (arXiv 2505.21444, 2025)",
    "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? (arXiv 2504.13837, NeurIPS 2025 Best Paper Runner-Up)",
    "Quagmires in SFT-RL Post-Training: When High SFT Scores Mislead and What to Use Instead (arXiv 2510.01624, NeurIPS 2025 MATH-AI Workshop)",
    "Pass@k Training for Adaptively Balancing Exploration and Exploitation of Large Reasoning Models (arXiv 2508.10751, ByteDance/RUC 2025)",
    "Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR — SvS (arXiv 2508.14029, 2025)",
    "SIRI: Scaling Iterative Reinforcement Learning with Interleaved Compression (arXiv 2509.25176, 2025)",
    "ReMiT: RL-Guided Mid-Training for Iterative LLM Evolution (arXiv 2602.03075, Feb 2026)",
    "DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving (arXiv 2407.13690, NeurIPS 2024)",
    "HS-STaR: Hierarchical Sampling for Self-Taught Reasoners (arXiv 2505.19866, EMNLP 2025)",
    "Self-Evolving Curriculum for LLM Reasoning — SEC (arXiv 2505.14970, Chen, Bengio et al., 2025)",
    "MathSmith: Towards Extremely Hard Mathematical Reasoning by Forging Synthetic Problems (arXiv 2508.05592, 2025)",
    "Better, Faster: Harnessing Self-Improvement in Large Reasoning Models — HSIR (arXiv 2605.24998, May 2026)",
    "Entrocraft: Addressing Performance Saturation for LLM RL via Precise Entropy Curve Control (arXiv 2604.26326, 2026)",
    "EntroPIC: Towards Stable Long-Term Training via Entropy Stabilization with PI Control (arXiv 2511.15248, 2025)",
    "RL on Incorrect Synthetic Data Scales the Efficiency of LLM Math Reasoning by Eight-Fold (arXiv 2406.14532, NeurIPS 2024)",
    "AI Models Collapse When Trained on Recursively Generated Data (Shumailov et al., Nature 2024)",
    "Large Language Model Post-Training: A Unified View (arXiv 2604.07941, Zhao et al., Apr 2026)",
    "Decoupling KL and Trajectories: A Unified Perspective for SFT, DAgger, Offline RL, and OPD (arXiv 2605.16826, May 2026)",
    "Post-Training is About States, Not Tokens (arXiv 2605.22731, May 2026)",
    "CLPD: Curriculum Learning-Guided Progressive Distillation (arXiv 2605.11260, May 2026)",
    "PRISM: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL (arXiv 2604.28123, Apr 2026)",
    "Beyond Pass@k: Breadth-Depth Metrics for LLM Reasoning — Cover@tau (arXiv 2510.08325, 2025)",
    "MATH-Beyond: A Benchmark for RL to Expand Beyond the Base Model (arXiv 2510.11653, 2025)",
    "ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries (NeurIPS 2025, arXiv 2505.24864)",
    "Self-Improvement of Large Language Models: A Technical Overview (arXiv 2603.25681, Mar 2026)",
    "ZClip: Adaptive Spike Mitigation for LLM Pre-Training (arXiv 2504.02507, 2025)",
    "rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking (arXiv 2501.04519, ICML 2025)",
    "Pass@k Metric for RLVR: A Diagnostic Tool of Exploration, But Not an Objective (arXiv 2511.16231, 2025)",
    "Limits of Generalization in RLVR: Two Case Studies (arXiv 2510.27044, 2025)"
  ],
  "description": "FrontierLoop addresses a fundamental scheduling problem in self-improvement for mathematical reasoning: WHEN to generate new synthetic training data, WHAT difficulty to target, WHEN to consolidate via RL, and WHEN to stop — decisions that current methods (STaR, ReST-EM, self-play) make with fixed schedules despite the model's needs changing across iterations. We operate in the pure self-improvement regime: the model generates its own synthetic data (reasoning traces and problems) with only a mathematical answer verifier as external component — no teacher model. The framework alternates between two modes: Generation Mode (frontier expansion via difficulty-targeted solution sampling, variational problem synthesis, or RL-guided problem generation) and RL Mode (consolidation via GRPO with entropy management). Transitions are governed by a diagnostic module evaluating four signals every 100 training steps on a compact validation set: (1) Sampling Efficiency Gap (SEG = pass@32 − pass@1), building on Quagmires' validation that pass@k predicts RL outcomes (R² up to 0.88) and Pass@k Training's use of pass@k as active signal; (2) Difficulty-Stratified Frontier Score (DSFS), identifying which difficulty bands have stalling frontiers, extending HS-STaR's boundary-level concept to dynamic targeting; (3) Entropy trajectory for collapse detection (validated by Entrocraft and EntroPIC); (4) Self-consistency divergence for reward hacking detection (motivated by arXiv 2505.21444). A z-score-normalized switching controller triggers transitions. Theoretically grounded by Mind the Gap (ICLR 2025, generation-verification gap governs self-improvement potential), the Unified View of Post-Training (arXiv 2604.07941, Generation=support expansion, RL=policy reshaping), and the solver-verifier gap theory (arXiv 2507.00075, self-improvement follows exponential curves toward computable limits). A cycling validation gate (Stage 0.5) tests whether a second generation→RL cycle expands pass@k beyond the first cycle's plateau; if not, the project pivots to single-iteration diagnostic-guided self-improvement, ensuring a contribution regardless. We evaluate against six baselines (STaR, ReST-EM, GRPO, Absolute Zero, fixed-interval cycling, SvS) with five ablations across MATH-500, AIME 2024, and LiveCodeBench, reporting pass@1, pass@32, per-difficulty breakdowns, compute efficiency (H100-hours per point), and Cover@tau for reasoning reliability. No external teacher means substantially lower compute (~1100-1800 H100-hours) than cross-model approaches.",
  "project_name": "frontier_loop",
  "source": "web_research",
  "reviewer_response": {
    "issue_1_topic_mismatch": "FIXED via PIVOT. The proposal has been completely restructured to genuinely address 'Synthetic Data and Self-Improvement for Mathematical Reasoning Training.' FrontierLoop operates in the PURE SELF-IMPROVEMENT regime: no external teacher model of any kind. 'Synthetic data' = the model generates its own reasoning traces (STaR-style) and problems (MathSmith/Absolute Zero-style). 'Self-improvement' = bootstrapping from own capabilities with only verifiable answer checking as external signal. 'Mathematical reasoning' = the target domain with MATH-500, AIME 2024, and LiveCodeBench evaluation. The cross-model distillation framing has been entirely removed. The core diagnostic-guided scheduling innovation is retained but applied to the self-improvement setting, where it is arguably MORE valuable because self-improvement has higher collapse risk and more variable data quality than teacher-supervised training.",
    "issue_2_siri_characterization": "FIXED. SIRI (arXiv 2509.25176) is now properly characterized as performing 3 iterations of compression↔expansion cycling WITHIN RL, oscillating rollout length between 8,192 and 16,384 tokens via a cosine scheduler. On AIME24, SIRI-low achieves 40.4% (vs. 28.2% baseline) with 46.9% token reduction. Clear differentiation: SIRI cycles WITHIN RL (varying rollout length to control reasoning conciseness), FrontierLoop cycles BETWEEN modes (data generation vs. RL training). SIRI does not generate new training data. FrontierLoop could incorporate SIRI's compression↔expansion within its RL phases while adding the higher-level generation↔training scheduling. SIRI is now positioned as the closest existing iterative cycling method for math reasoning and properly differentiated.",
    "issue_3_missing_citations": "FIXED. All three papers integrated: (1) CLPD (arXiv 2605.11260) — curriculum-guided progressive distillation, acknowledged in landscape as addressing teacher scheduling in supervised settings while FrontierLoop targets self-improvement; (2) 'Large Language Model Post-Training: A Unified View' (arXiv 2604.07941) — now provides core theoretical grounding for FrontierLoop via the support expansion / policy reshaping / behavioral consolidation framework, with FrontierLoop's Generation Mode mapping to support expansion and RL Mode to policy reshaping, and the paper's thesis ('progress depends on coordinated systems design') directly motivating diagnostic-guided orchestration; (3) PRISM (arXiv 2604.28123) — distribution-alignment between SFT and RL, acknowledged as relevant multi-stage design for supervised settings. Additionally integrated: 'Decoupling KL and Trajectories' (arXiv 2605.16826) and 'Post-Training is About States, Not Tokens' (arXiv 2605.22731) — both acknowledged and shown to SUPPORT FrontierLoop's approach (adaptive mode scheduling across different state distributions).",
    "issue_4_field_momentum_existential_risk": "ADDRESSED via PIVOT. The existential risk from the unified methods surge (Rebellious Student, AntiSD, CEPO, etc.) targeted the cross-model distillation regime, which FrontierLoop no longer occupies. FrontierLoop operates in the pure self-improvement regime where there is no teacher at all — neither cheap (self-distillation) nor expensive (cross-model). The unified methods and theoretical unification work (Decoupling KL, States Not Tokens) are complementary: they provide the vocabulary (support expansion, policy reshaping, state distributions) that FrontierLoop operationalizes through adaptive scheduling. The field momentum toward continuous-space optimization does not undermine discrete mode switching in the self-improvement context because the two modes serve fundamentally different computational purposes: Generation Mode creates new training data (requires inference-only compute), while RL Mode updates model weights (requires gradient compute). These cannot be trivially unified into a continuous objective.",
    "additional_improvements": "The pivot introduces 20+ new references from the self-improvement literature (STaR, ReST-EM, Absolute Zero, R-Zero, Mind the Gap, SRT, DART-Math, HS-STaR, SEC, MathSmith, SvS, HSIR, rStar-Math, etc.). Compute budget reduced by ~40% (no 235B teacher). The cycling validation gate (Stage 0.5) is retained with adapted criteria. The go/no-go pivot path now leads to single-iteration diagnostic-guided self-improvement (still novel). Six new baselines specific to self-improvement. The proposal now naturally fits the user's requested topic at every level."
  }
}
```

---

## Summary of Changes (Round 7 → Round 8): **PIVOT**

### Why Pivot?

After 7 rounds of stagnation (average score flat at 3.2), the reviewer identified the **fundamental problem**: the user asked for "Synthetic Data and Self-Improvement for Mathematical Reasoning Training," but FrontierCycle was about cross-model distillation scheduling from an expensive 235B teacher — the **opposite** of self-improvement. No amount of minor fixes could resolve this mismatch.

### What Changed

| Aspect | Before (FrontierCycle) | After (FrontierLoop) |
|--------|----------------------|---------------------|
| **Regime** | Cross-model distillation (235B→8B) | Pure self-improvement (no teacher) |
| **Synthetic data** | Teacher-generated | Self-generated traces + problems |
| **Core scheduling** | When to invoke expensive teacher | When to generate data vs. train via RL |
| **Compute** | 2800-3600 H100-hrs | 1100-1800 H100-hrs (~50% reduction) |
| **Key competitors** | Beyond GRPO, CHORD, unified methods | STaR, ReST-EM, Absolute Zero, SvS |
| **Topic alignment** | Mismatched | Direct match |

### Reviewer Issues Addressed

1. **Topic mismatch** → Complete pivot to self-improvement. No external teacher.
2. **SIRI mischaracterized** → Properly described as 3-iteration compression↔expansion cycling within RL. Differentiated: SIRI cycles rollout length; FrontierLoop cycles between data generation and RL.
3. **Missing citations** → CLPD, Unified View (now provides core theoretical grounding), PRISM all integrated.
4. **Field momentum risk** → Sidestepped: unified methods target distillation, FrontierLoop targets self-improvement where there's no teacher to unify with. The two modes (generation vs. RL) serve computationally distinct purposes that cannot be trivially collapsed.

### Core Novelty Retained but Reframed

The diagnostic-guided scheduling framework is preserved but applied to self-improvement, where it's **more valuable** because:
- Self-improvement has higher collapse risk (Nature 2024, SRT paper)
- Self-generated data quality varies more than teacher data  
- The generation-verification gap (Mind the Gap, ICLR 2025) provides a principled stopping criterion unique to self-improvement
- No existing self-improvement method uses real-time frontier diagnostics for scheduling

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "479b2b67-98d4-48ba-aa4d-ede03773f61e",
  "isSidechain": false,
  "requestId": "req_011CbTimTEfKU4XkiJRkgaeZ",
  "type": "assistant",
  "uuid": "c4db0faf-bec1-41d7-ae36-0c2240c4ccca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hhLmtJE5eTGphR2CqTcTX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1130,
      "cache_read_input_tokens": 59093,
      "output_tokens": 12828,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1130,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12828,
          "cache_read_input_tokens": 59093,
          "cache_creation_input_tokens": 1130,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1130
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

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"FrontierCycle: Diagnostic-Guided Iterative RL↔Distillation Scheduling…",
  "leafUuid": "c4db0faf-bec1-41d7-ae36-0c2240c4ccca",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise self-improvement framework for iterative LLM reasoning cycles",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"FrontierCycle: Diagnostic-Guided Iterative RL↔Distillation Scheduling…",
  "leafUuid": "c4db0faf-bec1-41d7-ae36-0c2240c4ccca",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise self-improvement framework for iterative LLM reasoning cycles",
  "sessionId": "0b883d0b-c2bf-45d5-bbae-05c02a6e8950"
}
```

---
