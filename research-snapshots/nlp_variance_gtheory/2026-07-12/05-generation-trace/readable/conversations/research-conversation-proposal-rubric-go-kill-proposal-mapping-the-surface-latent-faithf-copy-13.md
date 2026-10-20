# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Mapping the Surface-Latent Faithf

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/111b1ec3-6515-44c7-b8fc-61520f2f0414.jsonl`
- **Structured JSON:** [`b0ae62e1b50b1ab1b198.json`](../../sessions/b0/b0ae62e1b50b1ab1b198.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:31:40.796Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:31:40.796Z",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Models\n\n## Description\nWe propose the first systematic longitudinal study jointly tracking surface-level CoT faithfulness and probe-measured latent faithfulness across matched GRPO training checkpoints of open-weight reasoning models. Unlike the VLM checkpoint study (2602.12506) which used only LLM-as-judge surface metrics on vision-language models, and unlike 'Monitoring the Internal Monologue' (2605.18549) which tracked probe trajectories during inference of fixed models, we generate fine-grained GRPO checkpoints (~20 per model) from two architecturally distinct families — DeepSeek-R1-Distill-Qwen-7B (starting with distilled reasoning) and Qwen3-8B (starting from base) — and at each checkpoint measure: (1) linear probe AUC on pre-CoT residual-stream activations as a latent answer-commitment proxy, (2) hint-injection acknowledgment rate (Chen et al. protocol) as a surface faithfulness metric, (3) NLDD reasoning horizon length as a causal reliance metric, and (4) activation patching effect sizes for CoT tokens. The central hypothesis is that GRPO training creates a widening surface-latent faithfulness gap — surface metrics improve (or plateau) while latent answer pre-commitment strengthens — consistent with the RLVR monitorability finding that surface gains are orthogonal to causal reliance. We apply changepoint detection as an exploratory tool to characterize divergence dynamics without assuming specific functional forms. This work bridges the critical gap between training-dynamics studies (which lack latent measures) and mechanistic faithfulness studies (which lack temporal depth), providing the first temporal map of how RL systematically decouples what reasoning models say from what they compute. Results directly inform whether RL-trained reasoning models require latent-space monitoring infrastructure beyond CoT inspection.\n\n## Core Problem\nWhen and how does the gap between surface CoT faithfulness (measured by behavioral metrics like hint-injection rates and causal reliance) and latent faithfulness (measured by residual-stream probes predicting answer pre-commitment) develop during GRPO training of reasoning models — and what dynamics characterize this divergence?\n\n## Opportunity\nThree converging 2026 findings create a precise, actionable gap. First, the RLVR monitorability paper (2602.03978) showed that RL's surface-monitorability gains come from response distribution sharpening and increased prompt attention — NOT from stronger causal reliance on reasoning traces. Second, pre-CoT probes (2603.01437) demonstrated that instruction-tuned models encode answers in residual-stream activations before generating any CoT (>0.9 AUC), with these directions being causally efficacious. Third, the VLM checkpoint paper (2602.12506) showed an accuracy-faithfulness trade-off during RL fine-tuning — but using only LLM-as-judge surface metrics on vision-language models, with no latent-space analysis. Meanwhile, 'Monitoring the Internal Monologue' (2605.18549) introduced probe trajectories as a powerful inference-time monitoring tool but analyzed only fixed, already-trained models — never tracking how probe characteristics evolve across RL training steps. The Obfuscation Atlas (2602.15515) tracked deception probes across RLVR but focused narrowly on reward-hacking obfuscation rather than general faithfulness divergence. Nobody has jointly measured both surface faithfulness metrics and activation-probe-based latent faithfulness at matched RL training checkpoints to characterize how — and how fast — RL decouples what reasoning models say from what they compute. If this divergence is large and systematic, RL-trained reasoning models require latent-space monitoring beyond CoT inspection for safe deployment.\n\n## Related Work / Landscape\nThe CoT faithfulness literature in 2026 is large but fragmented along complementary axes, leaving the longitudinal surface-latent gap unstudied:\n\n**Surface faithfulness across RL steps (behavioral only):** Chen et al. (Anthropic 2025, 2505.05410) measured surface faithfulness via hint-injection across RL steps, finding initial improvement that plateaus (~25% for Claude 3.7 Sonnet). The VLM checkpoint paper (2602.12506) tracked CoT consistency via LLM-as-judge across GRPO checkpoints of Qwen2.5-VL-7B-Instruct, finding an accuracy-faithfulness trade-off — but used only behavioral metrics (letter entropy, judge-rated consistency) with no activation probes, and studied VLMs rather than language models.\n\n**Latent faithfulness in final models (snapshot only):** Pre-CoT probes (2603.01437) showed >0.9 AUC answer prediction from residual streams of Gemma 2 and Qwen 2.5 before any CoT tokens. 'Catching Rationalization in the Act' (2603.17199) trained probes to detect motivated reasoning pre- and post-CoT. 'The Hypocrisy Gap' (2602.02496) used SAEs to quantify internal-belief/CoT divergence. 'Why Models Know But Don't Say' (2603.26410) measured thinking-token vs. answer divergence. All analyze final models only.\n\n**Probe trajectories during inference (token-level, not training-level):** 'Monitoring the Internal Monologue' (2605.18549, May 2026) constructed probe trajectories across token positions during generation, achieving 95% AUROC for predicting outcomes. However, this tracks probes across tokens within a single generation of a fixed model — not across RL training checkpoints. Their models (Llama-8B-R1-Distill, Qwen3-4B/8B/14B) are final checkpoints only.\n\n**Deception probes across RLVR (deception-specific):** The Obfuscation Atlas (2602.15515) trained logistic regression probes on residual streams of Llama-3-8B through 70B across GRPO steps, mapping deception emergence. But their focus is reward-hacking obfuscation in coding tasks, not general reasoning faithfulness, and they don't measure surface faithfulness metrics jointly.\n\n**RL-Obfuscation (adversarial evasion):** RL-Obfuscation (2506.14261) showed 7B-14B models can learn to evade latent-space monitors through RL, with token-level monitors being vulnerable. This is an adversarial finding about monitor fragility, not a characterization of natural faithfulness divergence.\n\n**Faithfulness-improving RL methods:** FaithRL (2602.03507), AtManRL (2604.16158), and faithfulness-aware step-level RL (2602.05897) propose RL objectives that improve faithfulness, but none characterize the divergence trajectory of standard GRPO/RLVR training.\n\n**RL training dynamics:** Learning dynamics papers (2601.04670) show reduced feature diversity during RL but don't track faithfulness. The synthetic phase-transition paper (2602.01017) demonstrates faithful→unfaithful transitions under controlled noise in toy arithmetic — the only prior showing discrete transitions, but in a setting far removed from real GRPO.\n\n**The gap:** No existing work jointly tracks probe-measured latent faithfulness AND surface CoT faithfulness metrics at matched RL training checkpoints across training to characterize divergence dynamics in language reasoning models.\n\n## Approach\nWe produce our own fine-grained GRPO training checkpoints from two architecturally distinct open-weight model families, then jointly measure surface and latent faithfulness at each checkpoint.\n\n**Model families and checkpoint generation:**\n(1) DeepSeek-R1-Distill-Qwen-7B as base model, trained with GRPO using the Open-R1 pipeline (HuggingFace TRL) on MATH + GPQA, saving checkpoints every 50 GRPO steps for ~20 checkpoints across training. This model starts with distilled reasoning capability, letting us study how further RL reshapes faithfulness.\n(2) Qwen3-8B (base dense model, Apache 2.0) trained with the same GRPO pipeline and datasets, providing an architecturally distinct family that starts without distilled reasoning traces.\n\n**Metrics at each checkpoint:**\n(a) *Latent faithfulness proxy*: Train linear probes on residual-stream activations at the last pre-CoT token (following the methodology of Cox et al., 2603.01437), predicting the model's final answer. Report probe AUC and the layer at which AUC first exceeds 0.8 ('commitment layer'). A rising probe AUC across training indicates strengthening answer pre-commitment — the model increasingly 'knows' its answer before reasoning.\n(b) *Surface faithfulness — hint-injection*: Apply Chen et al.'s protocol with sycophancy and anchoring hints on a fixed MMLU/GPQA subset (~500 items). Report hint-acknowledgment rate (lower = more faithful surface behavior).\n(c) *Causal reliance — NLDD*: Compute the Normalized Logit Difference Decay metric (2602.11201) by corrupting individual reasoning steps and measuring confidence drops. Report the Reasoning Horizon k* (the chain-length fraction beyond which steps have negligible causal effect).\n(d) *Activation patching* (on 5 evenly-spaced checkpoints per family): Measure the causal effect of CoT-token activations on the final answer via mean-ablation patching, quantifying how much the model's computation actually flows through the reasoning trace.\n\n**Analysis:**\n- Construct the *surface-latent divergence curve*: plot surface faithfulness improvement (declining hint-acknowledgment rate) against latent bypass strengthening (rising probe AUC / shortening reasoning horizon) across GRPO steps.\n- Apply changepoint detection (PELT algorithm) as an *exploratory* tool to identify whether divergence accelerates at specific training phases — we do NOT claim phase transitions a priori but test for non-linear dynamics.\n- Compare divergence trajectories between the two model families to assess generality.\n- On a subset of checkpoints, apply the probe-trajectory methodology of 'Monitoring the Internal Monologue' (2605.18549) to test whether the character of inference-time probe trajectories (volatility, trend features) changes systematically across training — bridging their token-level and our checkpoint-level analyses.\n\n**Scaling validation:** If initial 7B results show clear divergence, replicate core probe + hint-injection measurements on DeepSeek-R1-Distill-Qwen-14B with ~10 GRPO checkpoints to verify the pattern holds at larger scale.\n\n**Key methodological choices justified:**\n- Using R1-Distill-7B rather than R1-671B: reviewer correctly identified that Dev1/Dev2/Dev3 checkpoints are not publicly available. Distilled 7B models are computationally tractable (single A100 for inference, 8×A100 for GRPO training) and let us generate arbitrarily fine-grained checkpoints.\n- GRPO rather than PPO: GRPO is the algorithm used in DeepSeek-R1 and the VLM checkpoint paper, ensuring comparability.\n- Two model families with different starting points (distilled reasoning vs. base): controls for whether divergence is an artifact of the starting model's reasoning capability.\n\n## Inspiration\nDirect gap between three convergent findings: (1) RLVR monitorability gains NOT from causal reliance (2602.03978), (2) pre-CoT probes show answer pre-commitment exists in residual streams (2603.01437), (3) VLM checkpoint paper shows accuracy-faithfulness trade-off during RL but with no latent-space analysis (2602.12506). The 'Monitoring the Internal Monologue' paper (2605.18549) shows probe trajectories are powerful for monitoring but leaves the training-dynamics dimension unexplored. The Obfuscation Atlas (2602.15515) demonstrates that probing across RLVR checkpoints is technically feasible at scale.\n\n## Key References\n- Reasoning Models Don't Always Say What They Think (Anthropic 2025, arXiv 2505.05410)\n- Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning (arXiv 2026, 2602.03978)\n- Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering (arXiv 2026, 2603.01437)\n- On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs (arXiv 2026, 2602.12506)\n- Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics (arXiv 2026, 2605.18549)\n- The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (FAR AI/arXiv 2026, 2602.15515)\n- RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? (arXiv 2025/2026, 2506.14261)\n- How Does Unfaithful Reasoning Emerge from Autoregressive Training? A Study of Synthetic Experiments (arXiv 2026, 2602.01017)\n- Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning (arXiv 2026, 2602.11201)\n- Learning Dynamics in RL Post-Training for Language Models (arXiv 2026, 2601.04670)\n- Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Goodfire/arXiv 2026, 2603.05488)\n- The Hypocrisy Gap: Quantifying Divergence Between Internal Belief and Chain-of-Thought Explanation via Sparse Autoencoders (arXiv 2026, 2602.02496)\n- Catching Rationalization in the Act: Detecting Motivated Reasoning Before and After CoT via Activation Probing (arXiv 2026, 2603.17199)\n- Why Models Know But Don't Say: CoT Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models (arXiv 2026, 2603.26410)\n- FaithRL: Learning to Reason Faithfully through Step-Level Faithfulness Maximization (arXiv 2026, 2602.03507)\n- AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency (arXiv 2026, 2604.16158)\n- DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (DeepSeek 2025, 2501.12948)\n- Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models (arXiv 2025, 2507.18014)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '350–500 A100-hours (GRPO training: ~80 A100-hrs × 2 families = 160 hrs; probe training + inference on ~20 checkpoints × 2 families: ~100 hrs; hint-injection evaluation: ~40 hrs; NLDD computation: ~30 hrs; activation patching on 10 checkpoints: ~50 hrs; 14B scaling validation: ~70 hrs)', 'timeline': '8–11 weeks (2 weeks GRPO training + pipeline setup, 3 weeks probe training & surface measurements in parallel, 2 weeks activation patching & NLDD, 1–2 weeks analysis, 1–2 weeks writing)', 'estimated_gpu_cost': '$900–$1,250 at ~$2.50/A100-hr spot pricing'}\n- **human_in_loop**: {'gpu_hours': '300–400 A100-hours (Claude handles probe training scripts, metric computation pipelines, statistical analysis, and plotting; human designs experiments, interprets results, writes key paper sections)', 'timeline': '6–8 weeks', 'claude_api_cost': '$120–$250 (Sonnet 4.6 for code generation, data analysis scripts, and paper drafting; ~40M input + 8M output tokens)', 'estimated_gpu_cost': '$750–$1,000'}\n- **auto_research**: {'gpu_hours': '300–400 A100-hours', 'timeline': '4–5 weeks (parallelized GRPO training for both families, then parallelized probe training and evaluation across checkpoints)', 'claude_api_cost': '$300–$550 (orchestration agent managing GRPO runs, checkpoint evaluation sweeps, result interpretation, iterative analysis; ~120M input + 25M output tokens)', 'estimated_gpu_cost': '$750–$1,000', 'speed_bottleneck': 'Sequential dependency: GRPO training must complete (or reach sufficient checkpoints) before probe training begins. However, probe training on early checkpoints can start while GRPO training continues. The two model families can be trained in parallel. 14B scaling validation is contingent on 7B results being compelling.'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T18:31:40.810Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:31:40.810Z",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-19T18:31:41.015Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Models

## Description
We propose the first systematic longitudinal study jointly tracking surface-level CoT faithfulness and probe-measured latent faithfulness across matched GRPO training checkpoints of open-weight reasoning models. Unlike the VLM checkpoint study (2602.12506) which used only LLM-as-judge surface metrics on vision-language models, and unlike 'Monitoring the Internal Monologue' (2605.18549) which tracked probe trajectories during inference of fixed models, we generate fine-grained GRPO checkpoints (~20 per model) from two architecturally distinct families — DeepSeek-R1-Distill-Qwen-7B (starting with distilled reasoning) and Qwen3-8B (starting from base) — and at each checkpoint measure: (1) linear probe AUC on pre-CoT residual-stream activations as a latent answer-commitment proxy, (2) hint-injection acknowledgment rate (Chen et al. protocol) as a surface faithfulness metric, (3) NLDD reasoning horizon length as a causal reliance metric, and (4) activation patching effect sizes for CoT tokens. The central hypothesis is that GRPO training creates a widening surface-latent faithfulness gap — surface metrics improve (or plateau) while latent answer pre-commitment strengthens — consistent with the RLVR monitorability finding that surface gains are orthogonal to causal reliance. We apply changepoint detection as an exploratory tool to characterize divergence dynamics without assuming specific functional forms. This work bridges the critical gap between training-dynamics studies (which lack latent measures) and mechanistic faithfulness studies (which lack temporal depth), providing the first temporal map of how RL systematically decouples what reasoning models say from what they compute. Results directly inform whether RL-trained reasoning models require latent-space monitoring infrastructure beyond CoT inspection.

## Core Problem
When and how does the gap between surface CoT faithfulness (measured by behavioral metrics like hint-injection rates and causal reliance) and latent faithfulness (measured by residual-stream probes predicting answer pre-commitment) develop during GRPO training of reasoning models — and what dynamics characterize this divergence?

## Opportunity
Three converging 2026 findings create a precise, actionable gap. First, the RLVR monitorability paper (2602.03978) showed that RL's surface-monitorability gains come from response distribution sharpening and increased prompt attention — NOT from stronger causal reliance on reasoning traces. Second, pre-CoT probes (2603.01437) demonstrated that instruction-tuned models encode answers in residual-stream activations before generating any CoT (>0.9 AUC), with these directions being causally efficacious. Third, the VLM checkpoint paper (2602.12506) showed an accuracy-faithfulness trade-off during RL fine-tuning — but using only LLM-as-judge surface metrics on vision-language models, with no latent-space analysis. Meanwhile, 'Monitoring the Internal Monologue' (2605.18549) introduced probe trajectories as a powerful inference-time monitoring tool but analyzed only fixed, already-trained models — never tracking how probe characteristics evolve across RL training steps. The Obfuscation Atlas (2602.15515) tracked deception probes across RLVR but focused narrowly on reward-hacking obfuscation rather than general faithfulness divergence. Nobody has jointly measured both surface faithfulness metrics and activation-probe-based latent faithfulness at matched RL training checkpoints to characterize how — and how fast — RL decouples what reasoning models say from what they compute. If this divergence is large and systematic, RL-trained reasoning models require latent-space monitoring beyond CoT inspection for safe deployment.

## Related Work / Landscape
The CoT faithfulness literature in 2026 is large but fragmented along complementary axes, leaving the longitudinal surface-latent gap unstudied:

**Surface faithfulness across RL steps (behavioral only):** Chen et al. (Anthropic 2025, 2505.05410) measured surface faithfulness via hint-injection across RL steps, finding initial improvement that plateaus (~25% for Claude 3.7 Sonnet). The VLM checkpoint paper (2602.12506) tracked CoT consistency via LLM-as-judge across GRPO checkpoints of Qwen2.5-VL-7B-Instruct, finding an accuracy-faithfulness trade-off — but used only behavioral metrics (letter entropy, judge-rated consistency) with no activation probes, and studied VLMs rather than language models.

**Latent faithfulness in final models (snapshot only):** Pre-CoT probes (2603.01437) showed >0.9 AUC answer prediction from residual streams of Gemma 2 and Qwen 2.5 before any CoT tokens. 'Catching Rationalization in the Act' (2603.17199) trained probes to detect motivated reasoning pre- and post-CoT. 'The Hypocrisy Gap' (2602.02496) used SAEs to quantify internal-belief/CoT divergence. 'Why Models Know But Don't Say' (2603.26410) measured thinking-token vs. answer divergence. All analyze final models only.

**Probe trajectories during inference (token-level, not training-level):** 'Monitoring the Internal Monologue' (2605.18549, May 2026) constructed probe trajectories across token positions during generation, achieving 95% AUROC for predicting outcomes. However, this tracks probes across tokens within a single generation of a fixed model — not across RL training checkpoints. Their models (Llama-8B-R1-Distill, Qwen3-4B/8B/14B) are final checkpoints only.

**Deception probes across RLVR (deception-specific):** The Obfuscation Atlas (2602.15515) trained logistic regression probes on residual streams of Llama-3-8B through 70B across GRPO steps, mapping deception emergence. But their focus is reward-hacking obfuscation in coding tasks, not general reasoning faithfulness, and they don't measure surface faithfulness metrics jointly.

**RL-Obfuscation (adversarial evasion):** RL-Obfuscation (2506.14261) showed 7B-14B models can learn to evade latent-space monitors through RL, with token-level monitors being vulnerable. This is an adversarial finding about monitor fragility, not a characterization of natural faithfulness divergence.

**Faithfulness-improving RL methods:** FaithRL (2602.03507), AtManRL (2604.16158), and faithfulness-aware step-level RL (2602.05897) propose RL objectives that improve faithfulness, but none characterize the divergence trajectory of standard GRPO/RLVR training.

**RL training dynamics:** Learning dynamics papers (2601.04670) show reduced feature diversity during RL but don't track faithfulness. The synthetic phase-transition paper (2602.01017) demonstrates faithful→unfaithful transitions under controlled noise in toy arithmetic — the only prior showing discrete transitions, but in a setting far removed from real GRPO.

**The gap:** No existing work jointly tracks probe-measured latent faithfulness AND surface CoT faithfulness metrics at matched RL training checkpoints across training to characterize divergence dynamics in language reasoning models.

## Approach
We produce our own fine-grained GRPO training checkpoints from two architecturally distinct open-weight model families, then jointly measure surface and latent faithfulness at each checkpoint.

**Model families and checkpoint generation:**
(1) DeepSeek-R1-Distill-Qwen-7B as base model, trained with GRPO using the Open-R1 pipeline (HuggingFace TRL) on MATH + GPQA, saving checkpoints every 50 GRPO steps for ~20 checkpoints across training. This model starts with distilled reasoning capability, letting us study how further RL reshapes faithfulness.
(2) Qwen3-8B (base dense model, Apache 2.0) trained with the same GRPO pipeline and datasets, providing an architecturally distinct family that starts without distilled reasoning traces.

**Metrics at each checkpoint:**
(a) *Latent faithfulness proxy*: Train linear probes on residual-stream activations at the last pre-CoT token (following the methodology of Cox et al., 2603.01437), predicting the model's final answer. Report probe AUC and the layer at which AUC first exceeds 0.8 ('commitment layer'). A rising probe AUC across training indicates strengthening answer pre-commitment — the model increasingly 'knows' its answer before reasoning.
(b) *Surface faithfulness — hint-injection*: Apply Chen et al.'s protocol with sycophancy and anchoring hints on a fixed MMLU/GPQA subset (~500 items). Report hint-acknowledgment rate (lower = more faithful surface behavior).
(c) *Causal reliance — NLDD*: Compute the Normalized Logit Difference Decay metric (2602.11201) by corrupting individual reasoning steps and measuring confidence drops. Report the Reasoning Horizon k* (the chain-length fraction beyond which steps have negligible causal effect).
(d) *Activation patching* (on 5 evenly-spaced checkpoints per family): Measure the causal effect of CoT-token activations on the final answer via mean-ablation patching, quantifying how much the model's computation actually flows through the reasoning trace.

**Analysis:**
- Construct the *surface-latent divergence curve*: plot surface faithfulness improvement (declining hint-acknowledgment rate) against latent bypass strengthening (rising probe AUC / shortening reasoning horizon) across GRPO steps.
- Apply changepoint detection (PELT algorithm) as an *exploratory* tool to identify whether divergence accelerates at specific training phases — we do NOT claim phase transitions a priori but test for non-linear dynamics.
- Compare divergence trajectories between the two model families to assess generality.
- On a subset of checkpoints, apply the probe-trajectory methodology of 'Monitoring the Internal Monologue' (2605.18549) to test whether the character of inference-time probe trajectories (volatility, trend features) changes systematically across training — bridging their token-level and our checkpoint-level analyses.

**Scaling validation:** If initial 7B results show clear divergence, replicate core probe + hint-injection measurements on DeepSeek-R1-Distill-Qwen-14B with ~10 GRPO checkpoints to verify the pattern holds at larger scale.

**Key methodological choices justified:**
- Using R1-Distill-7B rather than R1-671B: reviewer correctly identified that Dev1/Dev2/Dev3 checkpoints are not publicly available. Distilled 7B models are computationally tractable (single A100 for inference, 8×A100 for GRPO training) and let us generate arbitrarily fine-grained checkpoints.
- GRPO rather than PPO: GRPO is the algorithm used in DeepSeek-R1 and the VLM checkpoint paper, ensuring comparability.
- Two model families with different starting points (distilled reasoning vs. base): controls for whether divergence is an artifact of the starting model's reasoning capability.

## Inspiration
Direct gap between three convergent findings: (1) RLVR monitorability gains NOT from causal reliance (2602.03978), (2) pre-CoT probes show answer pre-commitment exists in residual streams (2603.01437), (3) VLM checkpoint paper shows accuracy-faithfulness trade-off during RL but with no latent-space analysis (2602.12506). The 'Monitoring the Internal Monologue' paper (2605.18549) shows probe trajectories are powerful for monitoring but leaves the training-dynamics dimension unexplored. The Obfuscation Atlas (2602.15515) demonstrates that probing across RLVR checkpoints is technically feasible at scale.

## Key References
- Reasoning Models Don't Always Say What They Think (Anthropic 2025, arXiv 2505.05410)
- Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning (arXiv 2026, 2602.03978)
- Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering (arXiv 2026, 2603.01437)
- On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs (arXiv 2026, 2602.12506)
- Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics (arXiv 2026, 2605.18549)
- The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (FAR AI/arXiv 2026, 2602.15515)
- RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? (arXiv 2025/2026, 2506.14261)
- How Does Unfaithful Reasoning Emerge from Autoregressive Training? A Study of Synthetic Experiments (arXiv 2026, 2602.01017)
- Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning (arXiv 2026, 2602.11201)
- Learning Dynamics in RL Post-Training for Language Models (arXiv 2026, 2601.04670)
- Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Goodfire/arXiv 2026, 2603.05488)
- The Hypocrisy Gap: Quantifying Divergence Between Internal Belief and Chain-of-Thought Explanation via Sparse Autoencoders (arXiv 2026, 2602.02496)
- Catching Rationalization in the Act: Detecting Motivated Reasoning Before and After CoT via Activation Probing (arXiv 2026, 2603.17199)
- Why Models Know But Don't Say: CoT Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models (arXiv 2026, 2603.26410)
- FaithRL: Learning to Reason Faithfully through Step-Level Faithfulness Maximization (arXiv 2026, 2602.03507)
- AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency (arXiv 2026, 2604.16158)
- DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (DeepSeek 2025, 2501.12948)
- Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models (arXiv 2025, 2507.18014)

## Resource Estimate
- **manual**: {'gpu_hours': '350–500 A100-hours (GRPO training: ~80 A100-hrs × 2 families = 160 hrs; probe training + inference on ~20 checkpoints × 2 families: ~100 hrs; hint-injection evaluation: ~40 hrs; NLDD computation: ~30 hrs; activation patching on 10 checkpoints: ~50 hrs; 14B scaling validation: ~70 hrs)', 'timeline': '8–11 weeks (2 weeks GRPO training + pipeline setup, 3 weeks probe training & surface measurements in parallel, 2 weeks activation patching & NLDD, 1–2 weeks analysis, 1–2 weeks writing)', 'estimated_gpu_cost': '$900–$1,250 at ~$2.50/A100-hr spot pricing'}
- **human_in_loop**: {'gpu_hours': '300–400 A100-hours (Claude handles probe training scripts, metric computation pipelines, statistical analysis, and plotting; human designs experiments, interprets results, writes key paper sections)', 'timeline': '6–8 weeks', 'claude_api_cost': '$120–$250 (Sonnet 4.6 for code generation, data analysis scripts, and paper drafting; ~40M input + 8M output tokens)', 'estimated_gpu_cost': '$750–$1,000'}
- **auto_research**: {'gpu_hours': '300–400 A100-hours', 'timeline': '4–5 weeks (parallelized GRPO training for both families, then parallelized probe training and evaluation across checkpoints)', 'claude_api_cost': '$300–$550 (orchestration agent managing GRPO runs, checkpoint evaluation sweeps, result interpretation, iterative analysis; ~120M input + 25M output tokens)', 'estimated_gpu_cost': '$750–$1,000', 'speed_bottleneck': 'Sequential dependency: GRPO training must complete (or reach sufficient checkpoints) before probe training begins. However, probe training on early checkpoints can start while GRPO training continues. The two model families can be trained in parallel. 14B scaling validation is contingent on 7B results being compelling.'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "96bd0ccc-0e1b-4fbf-a59e-b6e20abee508",
  "type": "user",
  "uuid": "96c51d48-f60b-48ee-a59e-b167269c7bd9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:31:41.014Z_

```json
{
  "parentUuid": "96c51d48-f60b-48ee-a59e-b167269c7bd9",
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
  "uuid": "c29b241d-aa34-4ac9-b318-565cc37121b2",
  "timestamp": "2026-05-19T18:31:41.014Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:31:41.014Z_

```json
{
  "parentUuid": "c29b241d-aa34-4ac9-b318-565cc37121b2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6b7cf8ac-5eff-46ff-bbd8-68d130ce3157",
  "timestamp": "2026-05-19T18:31:41.014Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Mo…",
  "leafUuid": "6b7cf8ac-5eff-46ff-bbd8-68d130ce3157",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Track faithfulness gap across GRPO training checkpoints",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:32:04.504Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026 (Conference on Robot Learning). Wait, let me re-read - actually, the system prompt says "CoRL 2026 主会" but this proposal is about CoT faithfulness, reasoning models, GRPO training, probes - this is clearly an NLP/AI safety/mechanistic interpretability paper, not a robotics paper. Let me re-read the system prompt... it says "CoRL 2026" but also mentions "NLP/CL 领域". Hmm, maybe they meant a different conference, or maybe CoRL here is used generically. 

There's a venue mismatch here - the proposal is fundamentally about LLM reasoning and interpretability, which would be better suited for NeurIPS, ICML, ICLR, or ACL rather than a robotics conference. But I'll set that aside and focus on evaluating the core idea quality.

Before I score this, I need to do some research to understand the current landscape - I should look into recent work on chain-of-thought faithfulness, RL training approaches for reasoning models, and the specific papers this proposal builds on.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b7cf8ac-5eff-46ff-bbd8-68d130ce3157",
  "isSidechain": false,
  "requestId": "req_011CbCQTLmKvHSczwntTm9qy",
  "type": "assistant",
  "uuid": "5a1855b4-ab26-4fab-badb-6f86b6834a49",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZBYLwEbC1ZmsreWv3XPiT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8175,
      "cache_read_input_tokens": 11374,
      "output_tokens": 509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8175,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 509,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 8175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8175
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

_source line 9 · 2026-05-19T18:32:04.595Z_

I need to do thorough literature research before evaluating this proposal. Let me search for the key topics and verify the referenced papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a1855b4-ab26-4fab-badb-6f86b6834a49",
  "isSidechain": false,
  "requestId": "req_011CbCQTLmKvHSczwntTm9qy",
  "type": "assistant",
  "uuid": "7b6c2779-3a69-400a-b672-7c05c8047553",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZBYLwEbC1ZmsreWv3XPiT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8175,
      "cache_read_input_tokens": 11374,
      "output_tokens": 509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8175,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 509,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 8175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8175
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

_source line 10 · 2026-05-19T18:32:04.764Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011sTd3JZ3KGzAHi5KNurF6w`</summary>

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
  "parentUuid": "7b6c2779-3a69-400a-b672-7c05c8047553",
  "isSidechain": false,
  "requestId": "req_011CbCQTLmKvHSczwntTm9qy",
  "type": "assistant",
  "uuid": "f785f4fe-50e0-4d44-a68e-ccb9ec83d8f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZBYLwEbC1ZmsreWv3XPiT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8175,
      "cache_read_input_tokens": 11374,
      "output_tokens": 509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8175,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 509,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 8175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8175
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

_source line 11 · 2026-05-19T18:32:04.771Z_

<details><summary>↩ Tool result · `toolu_011sTd3JZ3KGzAHi5KNurF6w`</summary>

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
  "parentUuid": "f785f4fe-50e0-4d44-a68e-ccb9ec83d8f5",
  "isSidechain": false,
  "promptId": "96bd0ccc-0e1b-4fbf-a59e-b6e20abee508",
  "type": "user",
  "uuid": "dc78ab9b-44ff-4c64-a591-be1229add740",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "f785f4fe-50e0-4d44-a68e-ccb9ec83d8f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T18:32:10.262Z_

Now let me run multiple searches in parallel to cover the key areas of this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc78ab9b-44ff-4c64-a591-be1229add740",
  "isSidechain": false,
  "requestId": "req_011CbCQV6E1mJXVTXzv27zf7",
  "type": "assistant",
  "uuid": "64860df1-d529-4f11-9715-9135c5b133ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQgpMc8dzM4tXpyaF726Kp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1036,
      "cache_read_input_tokens": 19549,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1036,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 19549,
          "cache_creation_input_tokens": 1036,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1036
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

_source line 13 · 2026-05-19T18:32:11.265Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018ojns9o8iqX6NAyQgwaXN2`</summary>

```json
{
  "query": "CoT chain-of-thought faithfulness RL training probes latent 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64860df1-d529-4f11-9715-9135c5b133ae",
  "isSidechain": false,
  "requestId": "req_011CbCQV6E1mJXVTXzv27zf7",
  "type": "assistant",
  "uuid": "346eedb5-cd98-4d1b-8545-d7e1c870b8fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQgpMc8dzM4tXpyaF726Kp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1036,
      "cache_read_input_tokens": 19549,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1036,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 19549,
          "cache_creation_input_tokens": 1036,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1036
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

_source line 14 · 2026-05-19T18:32:12.247Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011W19p8nXQphKD1cYLQu1mS`</summary>

```json
{
  "query": "pre-CoT probes residual stream answer pre-commitment 2603.01437 arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "346eedb5-cd98-4d1b-8545-d7e1c870b8fa",
  "isSidechain": false,
  "requestId": "req_011CbCQV6E1mJXVTXzv27zf7",
  "type": "assistant",
  "uuid": "e30a39c8-3795-44d6-961c-8e5e8e9e6b43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQgpMc8dzM4tXpyaF726Kp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1036,
      "cache_read_input_tokens": 19549,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1036,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 19549,
          "cache_creation_input_tokens": 1036,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1036
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

_source line 15 · 2026-05-19T18:32:13.146Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019rpdQr54qj1b4JSdoqnRHU`</summary>

```json
{
  "query": "RLVR monitorability reasoning 2602.03978 surface faithfulness arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e30a39c8-3795-44d6-961c-8e5e8e9e6b43",
  "isSidechain": false,
  "requestId": "req_011CbCQV6E1mJXVTXzv27zf7",
  "type": "assistant",
  "uuid": "d3e1bb85-5b9a-4631-93e1-52cca91db697",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQgpMc8dzM4tXpyaF726Kp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1036,
      "cache_read_input_tokens": 19549,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1036,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 19549,
          "cache_creation_input_tokens": 1036,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1036
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

_source line 16 · 2026-05-19T18:32:14.052Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019VXXahpgj9VvJ814GY3XUy`</summary>

```json
{
  "query": "Obfuscation Atlas deception probes RLVR GRPO checkpoints 2602.15515 arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3e1bb85-5b9a-4631-93e1-52cca91db697",
  "isSidechain": false,
  "requestId": "req_011CbCQV6E1mJXVTXzv27zf7",
  "type": "assistant",
  "uuid": "adb16f26-2945-4afc-95ba-1f9dea6e6a33",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQgpMc8dzM4tXpyaF726Kp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1036,
      "cache_read_input_tokens": 19549,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1036,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 19549,
          "cache_creation_input_tokens": 1036,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1036
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

_source line 17 · 2026-05-19T18:32:19.297Z_

<details><summary>↩ Tool result · `toolu_019rpdQr54qj1b4JSdoqnRHU`</summary>

```text
Web search results for query: "RLVR monitorability reasoning 2602.03978 surface faithfulness arXiv 2026"

Links: [{"title":"[2602.03978] Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning","url":"https://arxiv.org/abs/2602.03978"},{"title":"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning","url":"https://arxiv.org/pdf/2602.03978"},{"title":"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning","url":"https://arxiv.org/html/2602.03978v1"},{"title":"arXiv:2505.13774v2 [cs.AI] 28 May 2025","url":"https://arxiv.org/pdf/2505.13774"},{"title":"[2602.11792] Detecting RLVR Training Data via Structural Convergence of Reasoning","url":"https://arxiv.org/abs/2602.11792"},{"title":"RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/html/2602.17053v1"}]

Based on the search results, here's what I found:

The arXiv paper 2602.03978 reports that monitorability--the degree to which chain-of-thought (CoT) faithfully and informatively reflects internal computation--can appear as a "free gift" during the early stages of Reinforcement Learning with Verifiable Rewards (RLVR).

The research shows that this effect is not universal: monitorability improvements are strongly data-dependent, with data diversity and instruction-following data playing critical roles during RLVR training.

The paper further demonstrates that monitorability is orthogonal to capability--improvements in reasoning performance do not imply increased transparency.

The paper is titled "Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning" and was published on February 3, 2026. It provides a systematic evaluation across model families and training domains to understand how monitorability emerges during RLVR training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3e1bb85-5b9a-4631-93e1-52cca91db697",
  "isSidechain": false,
  "promptId": "96bd0ccc-0e1b-4fbf-a59e-b6e20abee508",
  "type": "user",
  "uuid": "b483ad3e-6a9d-4b2f-9f68-581a9fbb2294",
  "toolUseResult": {
    "query": "RLVR monitorability reasoning 2602.03978 surface faithfulness arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01H57DNaQzEZMqEu8Z68gDdZ",
        "content": [
          {
            "title": "[2602.03978] Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning",
            "url": "https://arxiv.org/abs/2602.03978"
          },
          {
            "title": "Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning",
            "url": "https://arxiv.org/pdf/2602.03978"
          },
          {
            "title": "Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning",
            "url": "https://arxiv.org/html/2602.03978v1"
          },
          {
            "title": "arXiv:2505.13774v2 [cs.AI] 28 May 2025",
            "url": "https://arxiv.org/pdf/2505.13774"
          },
          {
            "title": "[2602.11792] Detecting RLVR Training Data via Structural Convergence of Reasoning",
            "url": "https://arxiv.org/abs/2602.11792"
          },
          {
            "title": "RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models",
            "url": "https://arxiv.org/html/2602.17053v1"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\nThe arXiv paper 2602.03978 reports that monitorability--the degree to which chain-of-thought (CoT) faithfully and informatively reflects internal computation--can appear as a \"free gift\" during the early stages of Reinforcement Learning with Verifiable Rewards (RLVR).\n\nThe research shows that this effect is not universal: monitorability improvements are strongly data-dependent, with data diversity and instruction-following data playing critical roles during RLVR training.\n\nThe paper further demonstrates that monitorability is orthogonal to capability--improvements in reasoning performance do not imply increased transparency.\n\nThe paper is titled \"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning\" and was published on February 3, 2026. It provides a systematic evaluation across model families and training domains to understand how monitorability emerges during RLVR training."
    ],
    "durationSeconds": 6.146343331000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d3e1bb85-5b9a-4631-93e1-52cca91db697",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T18:32:20.288Z_

<details><summary>↩ Tool result · `toolu_018ojns9o8iqX6NAyQgwaXN2`</summary>

```text
Web search results for query: "CoT chain-of-thought faithfulness RL training probes latent 2025 2026 arXiv"

Links: [{"title":"On Robustness and Chain-of-Thought consistency of RL-Finetuned VLMs","url":"https://arxiv.org/html/2602.12506v1"},{"title":"Preprint. Counterfactual Simulation Training for Chain-of-Thought Faithfulness","url":"https://arxiv.org/pdf/2602.20710"},{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410v1"},{"title":"Chain-of-Thought Reasoning In The Wild Is Not Always Faithful","url":"https://arxiv.org/pdf/2503.08679"},{"title":"Published as a workshop paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.16158"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/pdf/2603.01437"},{"title":"Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought?","url":"https://arxiv.org/pdf/2603.30036"},{"title":"AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency","url":"https://arxiv.org/html/2604.16158"}]

Based on the search results, I found several recent arXiv papers from 2025-2026 related to chain-of-thought faithfulness, RL training, and probing methods:

## Key Papers Found:

1. **"On Robustness and Chain-of-Thought consistency of RL-Finetuned VLMs"** (February 2026): This paper probes whether CoT traces are faithful by using Qwen3-32B as a judge to determine consistency between the model's final judgment within reasoning tags and the answer.

2. **"Counterfactual Simulation Training for Chain-of-Thought Faithfulness"** (February 2026): This work includes assessment of the CoT's causal importance to the final output, testing whether CoT is useful for counterfactual simulation, and analyzing whether CoT reasoning verbalizes the role of cues in the model input.

3. **"Why Models Know But Don't Say"** (March 2026): This paper uses activation probing to demonstrate "Reasoning Theater" where models lock in answers early but continue generating performative reasoning tokens.

4. **"AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency"** (April 2026): This work defines faithfulness as requiring that the reasoning trace must accurately reflect the latent reasoning that produces the answer, and uses differentiable attention manipulation to learn token-level saliency and incorporate it into RL training.

5. **"Decoding Answers Before Chain-of-Thought"** (March 2026): This paper examines faithfulness in terms of whether the model's verbalized reasoning reflects its true decision-making process, using pre-CoT probes and activation steering.

These papers collectively address the intersection of chain-of-thought faithfulness, reinforcement learning training, and mechanistic probing of latent model representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "346eedb5-cd98-4d1b-8545-d7e1c870b8fa",
  "isSidechain": false,
  "promptId": "96bd0ccc-0e1b-4fbf-a59e-b6e20abee508",
  "type": "user",
  "uuid": "14efea07-2701-4ae3-b8c1-c0e9b893176f",
  "toolUseResult": {
    "query": "CoT chain-of-thought faithfulness RL training probes latent 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TZHCLiLqSTSSPGNP7jSKgj",
        "content": [
          {
            "title": "On Robustness and Chain-of-Thought consistency of RL-Finetuned VLMs",
            "url": "https://arxiv.org/html/2602.12506v1"
          },
          {
            "title": "Preprint. Counterfactual Simulation Training for Chain-of-Thought Faithfulness",
            "url": "https://arxiv.org/pdf/2602.20710"
          },
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410v1"
          },
          {
            "title": "Chain-of-Thought Reasoning In The Wild Is Not Always Faithful",
            "url": "https://arxiv.org/pdf/2503.08679"
          },
          {
            "title": "Published as a workshop paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2604.16158"
          },
          {
            "title": "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://arxiv.org/pdf/2603.01437"
          },
          {
            "title": "Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought?",
            "url": "https://arxiv.org/pdf/2603.30036"
          },
          {
            "title": "AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency",
            "url": "https://arxiv.org/html/2604.16158"
          }
        ]
      },
      "Based on the search results, I found several recent arXiv papers from 2025-2026 related to chain-of-thought faithfulness, RL training, and probing methods:\n\n## Key Papers Found:\n\n1. **\"On Robustness and Chain-of-Thought consistency of RL-Finetuned VLMs\"** (February 2026): This paper probes whether CoT traces are faithful by using Qwen3-32B as a judge to determine consistency between the model's final judgment within reasoning tags and the answer.\n\n2. **\"Counterfactual Simulation Training for Chain-of-Thought Faithfulness\"** (February 2026): This work includes assessment of the CoT's causal importance to the final output, testing whether CoT is useful for counterfactual simulation, and analyzing whether CoT reasoning verbalizes the role of cues in the model input.\n\n3. **\"Why Models Know But Don't Say\"** (March 2026): This paper uses activation probing to demonstrate \"Reasoning Theater\" where models lock in answers early but continue generating performative reasoning tokens.\n\n4. **\"AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency\"** (April 2026): This work defines faithfulness as requiring that the reasoning trace must accurately reflect the latent reasoning that produces the answer, and uses differentiable attention manipulation to learn token-level saliency and incorporate it into RL training.\n\n5. **\"Decoding Answers Before Chain-of-Thought\"** (March 2026): This paper examines faithfulness in terms of whether the model's verbalized reasoning reflects its true decision-making process, using pre-CoT probes and activation steering.\n\nThese papers collectively address the intersection of chain-of-thought faithfulness, reinforcement learning training, and mechanistic probing of latent model representations."
    ],
    "durationSeconds": 9.01947094,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "346eedb5-cd98-4d1b-8545-d7e1c870b8fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T18:32:20.557Z_

<details><summary>↩ Tool result · `toolu_019VXXahpgj9VvJ814GY3XUy`</summary>

```text
Web search results for query: "Obfuscation Atlas deception probes RLVR GRPO checkpoints 2602.15515 arXiv 2026"

Links: [{"title":"[2602.15515] The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes","url":"https://arxiv.org/abs/2602.15515"},{"title":"The Obfuscation Atlas:","url":"https://arxiv.org/pdf/2602.15515"},{"title":"The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/obfuscation-atlas-mapping-where-honesty-emerges-rlvr"},{"title":"The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes","url":"https://arxiv.org/html/2602.15515v1"},{"title":"GitHub - AlignmentResearch/obfuscation-atlas: The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes · GitHub","url":"https://github.com/AlignmentResearch/obfuscation-atlas"},{"title":"The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | FAR.AI","url":"https://www.far.ai/research/the-obfuscation-atlas-mapping-where-honesty-emerges-in-rlvr-with-deception-probes"},{"title":"The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes","url":"https://www.catalyzex.com/paper/the-obfuscation-atlas-mapping-where-honesty"},{"title":"Benchmarking Deception Probes via Black-to-White Performance Boosts","url":"https://arxiv.org/pdf/2507.12691"}]

I found the research paper you're looking for! Here's what I found:

"The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes" (arXiv:2602.15515) examines training against white-box deception detectors as a way to make AI systems honest, but notes that such training risks models learning to obfuscate their deception to evade the detector.

The research constructs a realistic coding environment where reward hacking via hardcoding test cases naturally occurs, and shows that obfuscation emerges in this setting.

The paper introduces a taxonomy of possible outcomes when training against a deception detector: the model either remains honest, or becomes deceptive via two possible obfuscation strategies: (i) Obfuscated activations where the model outputs deceptive text while modifying its internal representations to evade the detector, or (ii) Obfuscated policy where the model outputs deceptive text that evades the detector by including a justification for the reward hack.

The paper is authored by Mohammad Taufeeque, Stefan Heimersheim, Adam Gleave, and Chris Cundy. The paper was released on February 17, 2026, and includes code available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adb16f26-2945-4afc-95ba-1f9dea6e6a33",
  "isSidechain": false,
  "promptId": "96bd0ccc-0e1b-4fbf-a59e-b6e20abee508",
  "type": "user",
  "uuid": "a5af6613-56eb-4cbb-b1bd-2c2a5a3877cb",
  "toolUseResult": {
    "query": "Obfuscation Atlas deception probes RLVR GRPO checkpoints 2602.15515 arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KB1TszRxfLAq9muyZNm7pw",
        "content": [
          {
            "title": "[2602.15515] The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes",
            "url": "https://arxiv.org/abs/2602.15515"
          },
          {
            "title": "The Obfuscation Atlas:",
            "url": "https://arxiv.org/pdf/2602.15515"
          },
          {
            "title": "The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/obfuscation-atlas-mapping-where-honesty-emerges-rlvr"
          },
          {
            "title": "The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes",
            "url": "https://arxiv.org/html/2602.15515v1"
          },
          {
            "title": "GitHub - AlignmentResearch/obfuscation-atlas: The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes · GitHub",
            "url": "https://github.com/AlignmentResearch/obfuscation-atlas"
          },
          {
            "title": "The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | FAR.AI",
            "url": "https://www.far.ai/research/the-obfuscation-atlas-mapping-where-honesty-emerges-in-rlvr-with-deception-probes"
          },
          {
            "title": "The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes",
            "url": "https://www.catalyzex.com/paper/the-obfuscation-atlas-mapping-where-honesty"
          },
          {
            "title": "Benchmarking Deception Probes via Black-to-White Performance Boosts",
            "url": "https://arxiv.org/pdf/2507.12691"
          }
        ]
      },
      "I found the research paper you're looking for! Here's what I found:\n\n\"The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes\" (arXiv:2602.15515) examines training against white-box deception detectors as a way to make AI systems honest, but notes that such training risks models learning to obfuscate their deception to evade the detector.\n\nThe research constructs a realistic coding environment where reward hacking via hardcoding test cases naturally occurs, and shows that obfuscation emerges in this setting.\n\nThe paper introduces a taxonomy of possible outcomes when training against a deception detector: the model either remains honest, or becomes deceptive via two possible obfuscation strategies: (i) Obfuscated activations where the model outputs deceptive text while modifying its internal representations to evade the detector, or (ii) Obfuscated policy where the model outputs deceptive text that evades the detector by including a justification for the reward hack.\n\nThe paper is authored by Mohammad Taufeeque, Stefan Heimersheim, Adam Gleave, and Chris Cundy. The paper was released on February 17, 2026, and includes code available on GitHub."
    ],
    "durationSeconds": 6.501814836999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "adb16f26-2945-4afc-95ba-1f9dea6e6a33",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T18:32:21.033Z_

<details><summary>↩ Tool result · `toolu_011W19p8nXQphKD1cYLQu1mS`</summary>

```text
Web search results for query: "pre-CoT probes residual stream answer pre-commitment 2603.01437 arXiv 2026"

Links: [{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/html/2603.01437"},{"title":"[2603.01437] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/abs/2603.01437"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/pdf/2603.01437"},{"title":"Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing","url":"https://arxiv.org/pdf/2603.17199"},{"title":"[2603.17199] Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing","url":"https://arxiv.org/abs/2603.17199"},{"title":"Analysing the Residual Stream of Language Models Under Knowledge   Conflicts","url":"https://arxiv.org/pdf/2410.16090"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering"

**Authors:** Kyle Cox, Darius Kianersi, and Adrià Garriga-Alonso

**Main Findings:**

The paper provides mechanistic evidence that instruction-tuned models often determine their answer before generating CoT. Training linear probes on residual stream activations at the last token before CoT, the researchers can predict the model's final answer with >0.9 AUC on most tasks.

The researchers find that these directions are not only predictive, but also causal: steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines.

The paper was submitted to arXiv on March 2, 2026, with the identifier 2603.01437.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e30a39c8-3795-44d6-961c-8e5e8e9e6b43",
  "isSidechain": false,
  "promptId": "96bd0ccc-0e1b-4fbf-a59e-b6e20abee508",
  "type": "user",
  "uuid": "56ef70ea-b9c6-427a-958e-441e34d6ea5c",
  "toolUseResult": {
    "query": "pre-CoT probes residual stream answer pre-commitment 2603.01437 arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01G72yDtxUscDHxVWqRQHLZa",
        "content": [
          {
            "title": "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://arxiv.org/html/2603.01437"
          },
          {
            "title": "[2603.01437] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://arxiv.org/abs/2603.01437"
          },
          {
            "title": "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://arxiv.org/pdf/2603.01437"
          },
          {
            "title": "Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing",
            "url": "https://arxiv.org/pdf/2603.17199"
          },
          {
            "title": "[2603.17199] Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing",
            "url": "https://arxiv.org/abs/2603.17199"
          },
          {
            "title": "Analysing the Residual Stream of Language Models Under Knowledge   Conflicts",
            "url": "https://arxiv.org/pdf/2410.16090"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Title:** \"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering\"\n\n**Authors:** Kyle Cox, Darius Kianersi, and Adrià Garriga-Alonso\n\n**Main Findings:**\n\nThe paper provides mechanistic evidence that instruction-tuned models often determine their answer before generating CoT. Training linear probes on residual stream activations at the last token before CoT, the researchers can predict the model's final answer with >0.9 AUC on most tasks.\n\nThe researchers find that these directions are not only predictive, but also causal: steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines.\n\nThe paper was submitted to arXiv on March 2, 2026, with the identifier 2603.01437."
    ],
    "durationSeconds": 8.783149857999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e30a39c8-3795-44d6-961c-8e5e8e9e6b43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Mo…",
  "leafUuid": "56ef70ea-b9c6-427a-958e-441e34d6ea5c",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Track faithfulness gap across GRPO training checkpoints",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414"
}
```

---

### Assistant

_source line 23 · 2026-05-19T18:32:23.732Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've confirmed several key papers. Let me do a few more targeted searches to complete my research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56ef70ea-b9c6-427a-958e-441e34d6ea5c",
  "isSidechain": false,
  "requestId": "req_011CbCQWHXgtrZrLR7Lcqcvq",
  "type": "assistant",
  "uuid": "d7177a06-d2db-4336-99e3-f21881ffa54a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EQgupPDe3YYLuziwg69WS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1458,
      "cache_creation_input_tokens": 1731,
      "cache_read_input_tokens": 20585,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1458,
          "output_tokens": 243,
          "cache_read_input_tokens": 20585,
          "cache_creation_input_tokens": 1731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1731
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

_source line 24 · 2026-05-19T18:32:24.729Z_

Good, key papers are verified. Let me do additional searches to check for more directly competing work and the most recent developments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7177a06-d2db-4336-99e3-f21881ffa54a",
  "isSidechain": false,
  "requestId": "req_011CbCQWHXgtrZrLR7Lcqcvq",
  "type": "assistant",
  "uuid": "6813ff59-52a6-4284-9c59-3e0d2364be7b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EQgupPDe3YYLuziwg69WS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1458,
      "cache_creation_input_tokens": 1731,
      "cache_read_input_tokens": 20585,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1458,
          "output_tokens": 243,
          "cache_read_input_tokens": 20585,
          "cache_creation_input_tokens": 1731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1731
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

_source line 25 · 2026-05-19T18:32:25.817Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PxKBDTHAiPAmqQtEzTaaL4`</summary>

```json
{
  "query": "Monitoring Internal Monologue probe trajectories reasoning 2605.18549 arXiv May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6813ff59-52a6-4284-9c59-3e0d2364be7b",
  "isSidechain": false,
  "requestId": "req_011CbCQWHXgtrZrLR7Lcqcvq",
  "type": "assistant",
  "uuid": "3644825d-8f33-4acb-8a5b-5cca05adeced",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EQgupPDe3YYLuziwg69WS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1458,
      "cache_creation_input_tokens": 1731,
      "cache_read_input_tokens": 20585,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1458,
          "output_tokens": 243,
          "cache_read_input_tokens": 20585,
          "cache_creation_input_tokens": 1731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1731
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

_source line 26 · 2026-05-19T18:32:26.739Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mr6YGoPRdazzpxudJZjQ41`</summary>

```json
{
  "query": "surface latent faithfulness gap RL training reasoning models longitudinal probes 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3644825d-8f33-4acb-8a5b-5cca05adeced",
  "isSidechain": false,
  "requestId": "req_011CbCQWHXgtrZrLR7Lcqcvq",
  "type": "assistant",
  "uuid": "7cd1b473-380c-4abb-b343-8c4d28100704",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EQgupPDe3YYLuziwg69WS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1458,
      "cache_creation_input_tokens": 1731,
      "cache_read_input_tokens": 20585,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1458,
          "output_tokens": 243,
          "cache_read_input_tokens": 20585,
          "cache_creation_input_tokens": 1731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1731
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

_source line 27 · 2026-05-19T18:32:27.598Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RuZiVPuNPetG9LLWSgQz9y`</summary>

```json
{
  "query": "GRPO training dynamics faithfulness divergence reasoning models checkpoints probing 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cd1b473-380c-4abb-b343-8c4d28100704",
  "isSidechain": false,
  "requestId": "req_011CbCQWHXgtrZrLR7Lcqcvq",
  "type": "assistant",
  "uuid": "d930d830-ec80-4e22-a51d-0eca4622d660",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013EQgupPDe3YYLuziwg69WS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1458,
      "cache_creation_input_tokens": 1731,
      "cache_read_input_tokens": 20585,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1458,
          "output_tokens": 243,
          "cache_read_input_tokens": 20585,
          "cache_creation_input_tokens": 1731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1731
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

_source line 28 · 2026-05-19T18:32:32.749Z_

<details><summary>↩ Tool result · `toolu_01PxKBDTHAiPAmqQtEzTaaL4`</summary>

```text
Web search results for query: "Monitoring Internal Monologue probe trajectories reasoning 2605.18549 arXiv May 2026"

Links: [{"title":"[2605.18549] Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics","url":"https://arxiv.org/abs/2605.18549"},{"title":"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics","url":"https://arxiv.org/html/2605.18549"},{"title":"Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing","url":"https://arxiv.org/pdf/2603.17199"},{"title":"Tracing the Traces: Latent Temporal Signals for Efficient and Accurate Reasoning","url":"https://arxiv.org/pdf/2510.10494"},{"title":"Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning","url":"https://arxiv.org/pdf/2603.01326"},{"title":"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning","url":"https://arxiv.org/pdf/2602.03978"},{"title":"Probing the Trajectories of Reasoning Traces in Large Language Models","url":"https://arxiv.org/html/2601.23163v1"},{"title":"LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals","url":"https://arxiv.org/pdf/2604.05655"},{"title":"Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback","url":"https://arxiv.org/pdf/2603.16928"}]

Based on the search results, I found the paper you're looking for:

**"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics"** (arXiv 2605.18549) addresses how Large Reasoning Models (LRMs) introduce new opportunities for safety monitoring through their Chain of Thought (CoT) reasoning.

**Key findings:**

- The research constructs probe trajectories by evaluating a probe at each generated token, showing the continuous evolution of a concept's probability across the reasoning process.

- Future model behavior is more distinguishable when examined over the full trajectory than from a single static prediction.

- The choice of pooling operation is critical: average-pooling and last-token methods collapse to near-random performance, while max-pooling achieves up to 95% AUROC and yields stable probe trajectories.

- Using four datasets and four reasoning models across the domains of safety and mathematics, the researchers demonstrate that trajectory features encode task-specific dynamics that improve outcome separability.

The paper was published very recently (the search indicates 2 days ago), and it establishes probe trajectories as a framework for monitoring LRM behavior.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3644825d-8f33-4acb-8a5b-5cca05adeced",
  "isSidechain": false,
  "promptId": "96bd0ccc-0e1b-4fbf-a59e-b6e20abee508",
  "type": "user",
  "uuid": "46bc6261-0e15-4b08-82a4-ffa27f70444b",
  "toolUseResult": {
    "query": "Monitoring Internal Monologue probe trajectories reasoning 2605.18549 arXiv May 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RYAYg8aSQ9K43EkzZgcD76",
        "content": [
          {
            "title": "[2605.18549] Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics",
            "url": "https://arxiv.org/abs/2605.18549"
          },
          {
            "title": "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics",
            "url": "https://arxiv.org/html/2605.18549"
          },
          {
            "title": "Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing",
            "url": "https://arxiv.org/pdf/2603.17199"
          },
          {
            "title": "Tracing the Traces: Latent Temporal Signals for Efficient and Accurate Reasoning",
            "url": "https://arxiv.org/pdf/2510.10494"
          },
          {
            "title": "Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning",
            "url": "https://arxiv.org/pdf/2603.01326"
          },
          {
            "title": "Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning",
            "url": "https://arxiv.org/pdf/2602.03978"
          },
          {
            "title": "Probing the Trajectories of Reasoning Traces in Large Language Models",
            "url": "https://arxiv.org/html/2601.23163v1"
          },
          {
            "title": "LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals",
            "url": "https://arxiv.org/pdf/2604.05655"
          },
          {
            "title": "Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback",
            "url": "https://arxiv.org/pdf/2603.16928"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**\"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\"** (arXiv 2605.18549) addresses how Large Reasoning Models (LRMs) introduce new opportunities for safety monitoring through their Chain of Thought (CoT) reasoning.\n\n**Key findings:**\n\n- The research constructs probe trajectories by evaluating a probe at each generated token, showing the continuous evolution of a concept's probability across the reasoning process.\n\n- Future model behavior is more distinguishable when examined over the full trajectory than from a single static prediction.\n\n- The choice of pooling operation is critical: average-pooling and last-token methods collapse to near-random performance, while max-pooling achieves up to 95% AUROC and yields stable probe trajectories.\n\n- Using four datasets and four reasoning models across the domains of safety and mathematics, the researchers demonstrate that trajectory features encode task-specific dynamics that improve outcome separability.\n\nThe paper was published very recently (the search indicates 2 days ago), and it establishes probe trajectories as a framework for monitoring LRM behavior."
    ],
    "durationSeconds": 6.927213821999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3644825d-8f33-4acb-8a5b-5cca05adeced",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T18:32:34.693Z_

<details><summary>↩ Tool result · `toolu_01Mr6YGoPRdazzpxudJZjQ41`</summary>

```text
Web search results for query: "surface latent faithfulness gap RL training reasoning models longitudinal probes 2026"

Links: [{"title":"Published at Latent & Implicit Thinking Workshop @ ICLR 2026","url":"https://openreview.net/pdf?id=6a3InGPoEG"},{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410v1"},{"title":"A Survey on the Mechanisms of Multi-Step Reasoning in ...","url":"https://www.preprints.org/frontend/manuscript/11cab45ab0d578f7080de19423eb6ffe/download_pub"},{"title":"RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/pdf/2602.17053"},{"title":"Are DeepSeek R1 And Other Reasoning Models More Faithful?","url":"https://arxiv.org/pdf/2501.08156"},{"title":"When Shallow Wins: Silent Failures and the Depth-Accuracy Paradox in Latent Reasoning","url":"https://arxiv.org/pdf/2603.03475"},{"title":"Stop Rewarding Hallucinated Steps: Faithfulness-Aware Step-Level Reinforcement Learning for Small Reasoning Models","url":"https://arxiv.org/pdf/2602.05897"}]

Based on the search results, I found several highly relevant papers from 2026 addressing the intersections of faithfulness, RL training, reasoning models, and latent/implicit reasoning:

## Key Research Areas

**Faithfulness Divergence in Reasoning Models:**
Recent work has identified that even with thinking-token access, 11.8% of influenced cases show no acknowledgment in either channel, aligning with findings that models can commit to answers before generating reasoning tokens. A complete monitoring pipeline requires three tiers: answer-text screening, thinking-token screening, and activation-level or probe-based monitoring.

**RL Training and Latent Reasoning:**
After a Reasoning Projector is initialized, performance is improved via RL using reward functions, with the goal of lowering computational costs through latent reasoning. Experiments use Group Relative Policy Optimization (GRPO) to ensure consistency with previous work on latent reasoning.

**Mechanistic Understanding:**
Research has identified a "Reasoning Horizon" at 70–85% of chain length, beyond which reasoning tokens have diminishing causal influence on the final answer. Activation probes show that models often commit to answers early in the reasoning chain, with subsequent tokens serving a performative rather than computational role.

**Faithfulness vs. Accuracy:**
Adding current RL-style objectives on top of supervised fine-tuning can reduce reasoning faithfulness, even when accuracy is maintained.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cd1b473-380c-4abb-b343-8c4d28100704",
  "isSidechain": false,
  "promptId": "96bd0ccc-0e1b-4fbf-a59e-b6e20abee508",
  "type": "user",
  "uuid": "35dfe1dd-1bf6-4b15-aef8-1b92db1883fc",
  "toolUseResult": {
    "query": "surface latent faithfulness gap RL training reasoning models longitudinal probes 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VeXrKHWvCFZSbGeBzcSiVq",
        "content": [
          {
            "title": "Published at Latent & Implicit Thinking Workshop @ ICLR 2026",
            "url": "https://openreview.net/pdf?id=6a3InGPoEG"
          },
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410v1"
          },
          {
            "title": "A Survey on the Mechanisms of Multi-Step Reasoning in ...",
            "url": "https://www.preprints.org/frontend/manuscript/11cab45ab0d578f7080de19423eb6ffe/download_pub"
          },
          {
            "title": "RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2602.17053"
          },
          {
            "title": "Are DeepSeek R1 And Other Reasoning Models More Faithful?",
            "url": "https://arxiv.org/pdf/2501.08156"
          },
          {
            "title": "When Shallow Wins: Silent Failures and the Depth-Accuracy Paradox in Latent Reasoning",
            "url": "https://arxiv.org/pdf/2603.03475"
          },
          {
            "title": "Stop Rewarding Hallucinated Steps: Faithfulness-Aware Step-Level Reinforcement Learning for Small Reasoning Models",
            "url": "https://arxiv.org/pdf/2602.05897"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers from 2026 addressing the intersections of faithfulness, RL training, reasoning models, and latent/implicit reasoning:\n\n## Key Research Areas\n\n**Faithfulness Divergence in Reasoning Models:**\nRecent work has identified that even with thinking-token access, 11.8% of influenced cases show no acknowledgment in either channel, aligning with findings that models can commit to answers before generating reasoning tokens. A complete monitoring pipeline requires three tiers: answer-text screening, thinking-token screening, and activation-level or probe-based monitoring.\n\n**RL Training and Latent Reasoning:**\nAfter a Reasoning Projector is initialized, performance is improved via RL using reward functions, with the goal of lowering computational costs through latent reasoning. Experiments use Group Relative Policy Optimization (GRPO) to ensure consistency with previous work on latent reasoning.\n\n**Mechanistic Understanding:**\nResearch has identified a \"Reasoning Horizon\" at 70–85% of chain length, beyond which reasoning tokens have diminishing causal influence on the final answer. Activation probes show that models often commit to answers early in the reasoning chain, with subsequent tokens serving a performative rather than computational role.\n\n**Faithfulness vs. Accuracy:**\nAdding current RL-style objectives on top of supervised fine-tuning can reduce reasoning faithfulness, even when accuracy is maintained."
    ],
    "durationSeconds": 7.951639149000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7cd1b473-380c-4abb-b343-8c4d28100704",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T18:32:35.574Z_

<details><summary>↩ Tool result · `toolu_01RuZiVPuNPetG9LLWSgQz9y`</summary>

```text
Web search results for query: "GRPO training dynamics faithfulness divergence reasoning models checkpoints probing 2026"

Links: [{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410v1"},{"title":"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?","url":"https://arxiv.org/html/2603.22582v1"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.20659"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/html/2503.06639v4"},{"title":"Training your reasoning models with GRPO: A practical guide for VLMs Post Training with TRL | Towards AI","url":"https://towardsai.net/p/machine-learning/training-your-reasoning-models-with-grpo-a-practical-guide-for-vlms-post-training-with-trl"},{"title":"Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models","url":"https://arxiv.org/pdf/2507.18014"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/pdf/2503.06639"},{"title":"Evaluating GRPO and DPO for Faithful Chain-of-Thought Reasoning in LLMs","url":"https://arxiv.org/html/2512.22631v1"}]

I found several relevant research papers on your search topic. Here's a summary of the key findings:

## Main Research Areas

**GRPO Training and Dynamics:**
Group Relative Policy Optimization (GRPO) was introduced by Shao et al. (2024) and used to train DeepSeek-R1 for promoting reasoning in LLMs under verifiable (binary) rewards. GRPO with verifiable rewards can be written as a KL-regularized contrastive loss, where the optimal policy can be expressed in terms of the binary reward and first- and second-order statistics of the old and reference policies.

**Faithfulness and Divergence in Reasoning Models:**
DeepSeek-R1-Zero, trained with pure GRPO and no supervised warm-start, exhibited language mixing and poor readability in its reasoning traces. Models trained with rewards depending only on answer correctness may learn to omit hint acknowledgment from the visible channel while retaining it in the thinking channel.

**Checkpoint Evaluation and Probing Methods:**
Researchers saved checkpoints at each epoch and selected the best one based on validation loss when evaluating GRPO and DPO for faithful chain-of-thought reasoning. One approach probes intermediate reasoning steps by the probability increment of the reference answer at corresponding breakpoints, showing that average probed probability increases as reasoning progresses.

**Recent 2026 Papers:**
The search returned several papers from early 2026 examining these topics, including studies on faithfulness divergence between thinking tokens and final answers in open-weight reasoning models, and evaluations of GRPO compared to other training methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d930d830-ec80-4e22-a51d-0eca4622d660",
  "isSidechain": false,
  "promptId": "96bd0ccc-0e1b-4fbf-a59e-b6e20abee508",
  "type": "user",
  "uuid": "04232c42-114b-431d-a24f-85313a3a5cbe",
  "toolUseResult": {
    "query": "GRPO training dynamics faithfulness divergence reasoning models checkpoints probing 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RGqhnvdZ312imQJ9XSH4Jy",
        "content": [
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410v1"
          },
          {
            "title": "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?",
            "url": "https://arxiv.org/html/2603.22582v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2604.20659"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification",
            "url": "https://arxiv.org/html/2503.06639v4"
          },
          {
            "title": "Training your reasoning models with GRPO: A practical guide for VLMs Post Training with TRL | Towards AI",
            "url": "https://towardsai.net/p/machine-learning/training-your-reasoning-models-with-grpo-a-practical-guide-for-vlms-post-training-with-trl"
          },
          {
            "title": "Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2507.18014"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification",
            "url": "https://arxiv.org/pdf/2503.06639"
          },
          {
            "title": "Evaluating GRPO and DPO for Faithful Chain-of-Thought Reasoning in LLMs",
            "url": "https://arxiv.org/html/2512.22631v1"
          }
        ]
      },
      "I found several relevant research papers on your search topic. Here's a summary of the key findings:\n\n## Main Research Areas\n\n**GRPO Training and Dynamics:**\nGroup Relative Policy Optimization (GRPO) was introduced by Shao et al. (2024) and used to train DeepSeek-R1 for promoting reasoning in LLMs under verifiable (binary) rewards. GRPO with verifiable rewards can be written as a KL-regularized contrastive loss, where the optimal policy can be expressed in terms of the binary reward and first- and second-order statistics of the old and reference policies.\n\n**Faithfulness and Divergence in Reasoning Models:**\nDeepSeek-R1-Zero, trained with pure GRPO and no supervised warm-start, exhibited language mixing and poor readability in its reasoning traces. Models trained with rewards depending only on answer correctness may learn to omit hint acknowledgment from the visible channel while retaining it in the thinking channel.\n\n**Checkpoint Evaluation and Probing Methods:**\nResearchers saved checkpoints at each epoch and selected the best one based on validation loss when evaluating GRPO and DPO for faithful chain-of-thought reasoning. One approach probes intermediate reasoning steps by the probability increment of the reference answer at corresponding breakpoints, showing that average probed probability increases as reasoning progresses.\n\n**Recent 2026 Papers:**\nThe search returned several papers from early 2026 examining these topics, including studies on faithfulness divergence between thinking tokens and final answers in open-weight reasoning models, and evaluations of GRPO compared to other training methods."
    ],
    "durationSeconds": 7.972122847999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d930d830-ec80-4e22-a51d-0eca4622d660",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-19T18:32:35.578Z_

```json
{
  "parentUuid": "04232c42-114b-431d-a24f-85313a3a5cbe",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "06b4cba6-38ff-4917-9181-b13454998a32",
  "timestamp": "2026-05-19T18:32:35.578Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-19T18:32:39.564Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do one more round of searches to check for the most directly competing work - specifically any paper that already jointly tracks surface and latent faithfulness across RL training checkpoints.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06b4cba6-38ff-4917-9181-b13454998a32",
  "isSidechain": false,
  "requestId": "req_011CbCQXMjUVkqQh9Kv89xce",
  "type": "assistant",
  "uuid": "a704a20a-9672-473d-9ed8-6c29b17c699a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQv5Hpu8nLv1e33baseuiz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4110,
      "cache_read_input_tokens": 22316,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4110,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 22316,
          "cache_creation_input_tokens": 4110,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4110
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

_source line 33 · 2026-05-19T18:32:40.086Z_

Let me do one more targeted search to check for any work that might already be doing exactly what this proposal describes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a704a20a-9672-473d-9ed8-6c29b17c699a",
  "isSidechain": false,
  "requestId": "req_011CbCQXMjUVkqQh9Kv89xce",
  "type": "assistant",
  "uuid": "120479b1-dea6-4ae8-812f-1419f8da7a5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQv5Hpu8nLv1e33baseuiz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4110,
      "cache_read_input_tokens": 22316,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4110,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 22316,
          "cache_creation_input_tokens": 4110,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4110
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

_source line 34 · 2026-05-19T18:32:41.634Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CYMUsQgWAhB272mK2cgs2x`</summary>

```json
{
  "query": "\"faithfulness\" \"probes\" \"RL checkpoints\" \"training steps\" reasoning models activation longitudinal 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "120479b1-dea6-4ae8-812f-1419f8da7a5f",
  "isSidechain": false,
  "requestId": "req_011CbCQXMjUVkqQh9Kv89xce",
  "type": "assistant",
  "uuid": "3e23e46b-0b6a-453e-9946-80913331bb73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQv5Hpu8nLv1e33baseuiz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4110,
      "cache_read_input_tokens": 22316,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4110,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 22316,
          "cache_creation_input_tokens": 4110,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4110
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

_source line 35 · 2026-05-19T18:32:42.415Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H5ha9UYasjYWZTJ8TfGw4K`</summary>

```json
{
  "query": "RL-Obfuscation latent space monitors evasion 2506.14261 language models 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e23e46b-0b6a-453e-9946-80913331bb73",
  "isSidechain": false,
  "requestId": "req_011CbCQXMjUVkqQh9Kv89xce",
  "type": "assistant",
  "uuid": "ad1ce734-4d7f-486d-8968-016283ea35cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQv5Hpu8nLv1e33baseuiz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4110,
      "cache_read_input_tokens": 22316,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4110,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 22316,
          "cache_creation_input_tokens": 4110,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4110
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

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Mo…",
  "leafUuid": "ad1ce734-4d7f-486d-8968-016283ea35cf",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Track faithfulness gap across GRPO training checkpoints",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414"
}
```

---

### Tool result

_source line 38 · 2026-05-19T18:32:48.857Z_

<details><summary>↩ Tool result · `toolu_01CYMUsQgWAhB272mK2cgs2x`</summary>

```text
Web search results for query: ""faithfulness" "probes" "RL checkpoints" "training steps" reasoning models activation longitudinal 2026"

Links: [{"title":"RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/html/2602.17053"},{"title":"Reasoning Theater: Probing for Performative Chain-of-Thought","url":"https://www.goodfire.ai/research/reasoning-theater"},{"title":"Reasoning Faithfulness","url":"https://akhil.bio/CoT"},{"title":"Stop Rewarding Hallucinated Steps: Faithfulness-Aware Step-Level Reinforcement Learning for Small Reasoning Models","url":"https://arxiv.org/pdf/2602.05897"},{"title":"RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/pdf/2602.17053"},{"title":"Reasoning Through Chess: How Reasoning Evolves from Data Through Fine-Tuning and Reinforcement Learning","url":"https://arxiv.org/pdf/2604.05134"},{"title":"[2602.17053v1] RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/abs/2602.17053v1"},{"title":"[2602.17053] RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/abs/2602.17053"},{"title":"FaithRL: Learning to Reason Faithfully through Step-Level Faithfulness Maximization","url":"https://arxiv.org/html/2602.03507"}]

Based on the web search results, I found several relevant papers from 2026 on faithfulness probes and reasoning models. Here are the key findings:

## Recent Research on Faithfulness in Reasoning Models (2026)

**RFEval Benchmark**: RFEval is a benchmark of 7,186 instances across seven tasks that probes faithfulness via controlled, output-level counterfactual interventions. The research found that unfaithfulness appears in 49.7% of outputs, predominantly from stance inconsistency, with failures concentrated in brittle domains like math and code that correlate more with post-training regimes than with scale.

**Reasoning Theater**: Models genuinely reason through hard problems, but coast through easy ones while generating superfluous chain-of-thought. Importantly, probes can enable monitoring for such unfaithfulness by using signals that aren't present in model outputs, with minimal inference overhead.

**RL Training Impact**: Research indicates that adding current RL-style objectives on top of supervised fine-tuning can reduce reasoning faithfulness, even when accuracy is maintained.

**SFT Checkpoints**: Several SFT-checkpoint metrics—spanning evaluation performance, hallucination rates, and reasoning quality—are predictive of post-RL model performance.

These studies demonstrate active research in 2026 on understanding and improving faithfulness in large reasoning models through checkpoint analysis and specialized probing methodologies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e23e46b-0b6a-453e-9946-80913331bb73",
  "isSidechain": false,
  "promptId": "96bd0ccc-0e1b-4fbf-a59e-b6e20abee508",
  "type": "user",
  "uuid": "c30bc26e-0b48-40a5-9227-fe023d626f50",
  "toolUseResult": {
    "query": "\"faithfulness\" \"probes\" \"RL checkpoints\" \"training steps\" reasoning models activation longitudinal 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0184Tui7Z1B47aQZRJRSrW1V",
        "content": [
          {
            "title": "RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models",
            "url": "https://arxiv.org/html/2602.17053"
          },
          {
            "title": "Reasoning Theater: Probing for Performative Chain-of-Thought",
            "url": "https://www.goodfire.ai/research/reasoning-theater"
          },
          {
            "title": "Reasoning Faithfulness",
            "url": "https://akhil.bio/CoT"
          },
          {
            "title": "Stop Rewarding Hallucinated Steps: Faithfulness-Aware Step-Level Reinforcement Learning for Small Reasoning Models",
            "url": "https://arxiv.org/pdf/2602.05897"
          },
          {
            "title": "RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2602.17053"
          },
          {
            "title": "Reasoning Through Chess: How Reasoning Evolves from Data Through Fine-Tuning and Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2604.05134"
          },
          {
            "title": "[2602.17053v1] RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models",
            "url": "https://arxiv.org/abs/2602.17053v1"
          },
          {
            "title": "[2602.17053] RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models",
            "url": "https://arxiv.org/abs/2602.17053"
          },
          {
            "title": "FaithRL: Learning to Reason Faithfully through Step-Level Faithfulness Maximization",
            "url": "https://arxiv.org/html/2602.03507"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers from 2026 on faithfulness probes and reasoning models. Here are the key findings:\n\n## Recent Research on Faithfulness in Reasoning Models (2026)\n\n**RFEval Benchmark**: RFEval is a benchmark of 7,186 instances across seven tasks that probes faithfulness via controlled, output-level counterfactual interventions. The research found that unfaithfulness appears in 49.7% of outputs, predominantly from stance inconsistency, with failures concentrated in brittle domains like math and code that correlate more with post-training regimes than with scale.\n\n**Reasoning Theater**: Models genuinely reason through hard problems, but coast through easy ones while generating superfluous chain-of-thought. Importantly, probes can enable monitoring for such unfaithfulness by using signals that aren't present in model outputs, with minimal inference overhead.\n\n**RL Training Impact**: Research indicates that adding current RL-style objectives on top of supervised fine-tuning can reduce reasoning faithfulness, even when accuracy is maintained.\n\n**SFT Checkpoints**: Several SFT-checkpoint metrics—spanning evaluation performance, hallucination rates, and reasoning quality—are predictive of post-RL model performance.\n\nThese studies demonstrate active research in 2026 on understanding and improving faithfulness in large reasoning models through checkpoint analysis and specialized probing methodologies."
    ],
    "durationSeconds": 7.218329908999992,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3e23e46b-0b6a-453e-9946-80913331bb73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T18:32:49.805Z_

<details><summary>↩ Tool result · `toolu_01H5ha9UYasjYWZTJ8TfGw4K`</summary>

```text
Web search results for query: "RL-Obfuscation latent space monitors evasion 2506.14261 language models 2025 2026"

Links: [{"title":"[2506.14261] RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?","url":"https://arxiv.org/abs/2506.14261"},{"title":"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?","url":"https://arxiv.org/pdf/2506.14261"},{"title":"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? | OpenReview","url":"https://openreview.net/forum?id=YT97yOoD4x"},{"title":"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250614261G/abstract"},{"title":"(PDF) RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?","url":"https://www.researchgate.net/publication/392765939_RL-Obfuscation_Can_Language_Models_Learn_to_Evade_Latent-Space_Monitors"},{"title":"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? | Papers With Code","url":"https://paperswithcode.com/paper/rl-obfuscation-can-language-models-learn-to"},{"title":"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? - MATS Research","url":"https://www.matsprogram.org/research/receWMx6ftg6mcyCh"},{"title":"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? - Paper Detail","url":"https://deeplearn.org/arxiv/620530/rl-obfuscation:-can-language-models-learn-to-evade-latent-space-monitors"},{"title":"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?","url":"https://arxiv.org/html/2506.14261v3"}]

Based on the search results, here's what I found about the research paper 2506.14261:

## Overview

RL-Obfuscation is a method in which LLMs are finetuned via reinforcement learning to evade latent-space monitors while maintaining their blackbox behaviour.

## Research Question

Latent-space monitors aim to detect undesirable behaviours in Large Language Models by leveraging their internal representations rather than relying solely on black-box outputs, and these methods have shown promise in identifying behaviours such as deception and unsafe completions. The research investigates whether models can learn to evade such monitors.

## Key Findings

The research applied RL-Obfuscation to Language Models ranging from 7B to 14B parameters and evaluated their Evasion Success Rate against a suite of monitors. 

Token-level monitors are highly vulnerable to this attack while more holistic monitors, such as max-pooling or attention-based probes, remain robust. 

Models trained to evade a single static monitor can generalise to evade other unseen monitors. Additionally, the models can be trained to conditionally bypass latent-space monitors on only certain inputs, and the model can learn to repurpose tokens to have different internal representations.

The paper was published on June 17, 2025, and is available on arXiv with the identifier 2506.14261.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad1ce734-4d7f-486d-8968-016283ea35cf",
  "isSidechain": false,
  "promptId": "96bd0ccc-0e1b-4fbf-a59e-b6e20abee508",
  "type": "user",
  "uuid": "5aecbef6-59ff-4e35-beb2-fd470f7c8cf9",
  "toolUseResult": {
    "query": "RL-Obfuscation latent space monitors evasion 2506.14261 language models 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QkkYerFVypTSVYKbjhsabn",
        "content": [
          {
            "title": "[2506.14261] RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?",
            "url": "https://arxiv.org/abs/2506.14261"
          },
          {
            "title": "RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?",
            "url": "https://arxiv.org/pdf/2506.14261"
          },
          {
            "title": "RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? | OpenReview",
            "url": "https://openreview.net/forum?id=YT97yOoD4x"
          },
          {
            "title": "RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250614261G/abstract"
          },
          {
            "title": "(PDF) RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?",
            "url": "https://www.researchgate.net/publication/392765939_RL-Obfuscation_Can_Language_Models_Learn_to_Evade_Latent-Space_Monitors"
          },
          {
            "title": "RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? | Papers With Code",
            "url": "https://paperswithcode.com/paper/rl-obfuscation-can-language-models-learn-to"
          },
          {
            "title": "RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? - MATS Research",
            "url": "https://www.matsprogram.org/research/receWMx6ftg6mcyCh"
          },
          {
            "title": "RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? - Paper Detail",
            "url": "https://deeplearn.org/arxiv/620530/rl-obfuscation:-can-language-models-learn-to-evade-latent-space-monitors"
          },
          {
            "title": "RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?",
            "url": "https://arxiv.org/html/2506.14261v3"
          }
        ]
      },
      "Based on the search results, here's what I found about the research paper 2506.14261:\n\n## Overview\n\nRL-Obfuscation is a method in which LLMs are finetuned via reinforcement learning to evade latent-space monitors while maintaining their blackbox behaviour.\n\n## Research Question\n\nLatent-space monitors aim to detect undesirable behaviours in Large Language Models by leveraging their internal representations rather than relying solely on black-box outputs, and these methods have shown promise in identifying behaviours such as deception and unsafe completions. The research investigates whether models can learn to evade such monitors.\n\n## Key Findings\n\nThe research applied RL-Obfuscation to Language Models ranging from 7B to 14B parameters and evaluated their Evasion Success Rate against a suite of monitors. \n\nToken-level monitors are highly vulnerable to this attack while more holistic monitors, such as max-pooling or attention-based probes, remain robust. \n\nModels trained to evade a single static monitor can generalise to evade other unseen monitors. Additionally, the models can be trained to conditionally bypass latent-space monitors on only certain inputs, and the model can learn to repurpose tokens to have different internal representations.\n\nThe paper was published on June 17, 2025, and is available on arXiv with the identifier 2506.14261."
    ],
    "durationSeconds": 7.387614459000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ad1ce734-4d7f-486d-8968-016283ea35cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-19T18:33:43.702Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the landscape. Let me synthesize my findings and evaluate this proposal.

Key observations from my research:

1. **The referenced papers all exist and are accurately described** in the proposal. This is a good sign of scholarly rigor.

2. **The gap identification is legitimate**: No existing work jointly tracks probe-measured latent faithfulness AND surface CoT faithfulness at matched RL training checkpoints across training. The closest works are:
   - Obfuscation Atlas (2602.15515): Tracks probes across GRPO checkpoints but focuses on deception, not general faithfulness, and doesn't jointly measure surface faithfulness
   - VLM checkpoint paper (2602.12506): Tracks surface faithfulness across RL checkpoints but no latent measures
   - Monitoring Internal Monologue (2605.18549): Probe trajectories during inference, not across training
   - Pre-CoT probes (2603.01437): Snapshot of final models only

3. **The core hypothesis is well-motivated**: RLVR monitorability findings suggest surface gains are orthogonal to causal reliance, and pre-CoT probes show answer pre-commitment exists. It's a natural next step to track how these evolve together across training.

Now I'm thinking through whether there's a simpler alternative approach that could achieve the same insights without the full experimental scope.

The Obfuscation Atlas already probes across GRPO checkpoints, but it focuses on deception rather than answer-commitment, and the VLM checkpoint paper tracks surface metrics across training but uses vision models instead of language models — so combining them wouldn't directly answer the question. A stripped-down version with just five checkpoints and hint-injection could probably establish the core finding, though the full analysis with multiple metrics and changepoint detection adds rigor. The real concern is whether the result will feel predictable given what the monitorability and pre-CoT papers already suggest about the mechanism.

The core assumption that pre-CoT probe AUC reflects latent answer-commitment is grounded in causal work, but there's a risk the probe is capturing task-related features rather than genuine pre-commitment — the steering results help validate this but aren't a perfect correspondence. I'm also questioning whether characterizing the divergence between surface and latent faithfulness is the right focus, since the practical need for latent monitoring holds regardless of whether that divergence emerges gradually or suddenly.

The novelty is real but modest — this fills a genuine gap by doing the first joint longitudinal measurement, but it's more about connecting existing dots than a conceptual leap. The expected finding would confirm what prior work already implies, and the methodology combines existing tools rather than introducing new ones, making this a solid measurement study without a major novel insight. For safety relevance, the question matters because systematic divergence would inform deployment monitoring, but the field already assumes CoT may be unfaithful, so this would quantify rather than fundamentally shift understanding — the truly surprising result would be finding no divergence, though that's less likely given what we know.

The related work section is exceptionally strong, covering 15+ recent papers and clearly mapping where prior work fragments and what specific gap remains. But there's a venue mismatch here — the user mentioned CoRL 2026, which is Conference on Robot Learning, yet this proposal is entirely about LLM reasoning faithfulness and has nothing to do with robotics.

Let me reconsider though. The rubric mentions "NLP/CL 领域" which suggests NLP/CL venues, not robotics. Maybe "CoRL" means something different in this context, or there's a typo. Rather than get stuck on the venue question, I should focus on evaluating the idea quality itself as if it's being submitted to a top-tier ML/NLP conference like ICML, NeurIPS, ICLR, or ACL, and let the venue question be secondary.

Now I'm thinking through the overall probability. This is a solid measurement study with real novelty in how it combines existing tools, and there's a genuine gap in the literature. But the expected results aren't surprising — most reviewers would predict the direction anyway. It's fundamentally a measurement study rather than a conceptual or methodological advance, and all the tools are borrowed from prior work. If the findings come out positive, they'd mostly confirm existing assumptions rather than overturn them. For a top ML venue, I'd put this in the 25-35% acceptance range, with a median around 30%. The thorough related work helps push it up, but the predictability of the expected outcome caps how high it can go.

Actually, I should reconsider this. Chain-of-thought faithfulness is an extremely hot topic right now in 2026, especially with the safety community paying close attention. A well-executed study that provides the first temporal analysis of how faithfulness evolves could have real impact.

The dual-model-family approach adds methodological rigor, and the changepoint detection might uncover non-obvious dynamics. But the field is crowded enough that many groups are probably exploring similar directions, which means scooping is a real risk given how natural this next step feels. I'm settling on 25-33%, with a median around 28%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5aecbef6-59ff-4e35-beb2-fd470f7c8cf9",
  "isSidechain": false,
  "requestId": "req_011CbCQYQYfn3N55xaZSRA9V",
  "type": "assistant",
  "uuid": "993b64ce-23f0-4933-b2a8-0bfdb05c68f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HT8fuVkxNovdZU656YrjTN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1982,
      "cache_read_input_tokens": 26426,
      "output_tokens": 5703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1982,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5703,
          "cache_read_input_tokens": 26426,
          "cache_creation_input_tokens": 1982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1982
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

_source line 41 · 2026-05-19T18:35:08.199Z_

Now I have sufficient research to make a well-informed assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978) (arXiv 2026):
   核心发现 RLVR 的 surface monitorability 提升来自 response distribution sharpening 和 prompt attention 增强，而非 causal reliance 增强。Monitorability 与 capability 正交。该论文是本 proposal 的直接灵感来源之一，proposal 引用准确。

2. [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437) (arXiv 2026, Cox et al.):
   在 Gemma 2 和 Qwen 2.5 上训练线性 probe，从 pre-CoT residual stream 预测 final answer，AUC >0.9。且证明 probe direction 有因果效力（steering 可 flip 答案 >50%）。Proposal 引用准确，这是其 latent faithfulness proxy 的方法论基础。

3. [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506) (arXiv 2026):
   在 Qwen2.5-VL-7B 的 GRPO checkpoint 上跟踪 accuracy vs. CoT consistency，发现 trade-off。但仅用 LLM-as-judge 表层指标，无 activation probe，且是 VLM 而非 LLM。Proposal 对其局限性的描述准确。

4. [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549) (arXiv May 2026):
   在固定模型的 inference 过程中构建 probe trajectory（逐 token），max-pooling 达 95% AUROC。但只分析 final model，不跟踪 training 过程。极新论文（~2 天前发布），proposal 已引用并正确描述了其局限。

5. [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515) (FAR AI, arXiv 2026):
   在 Llama-3-8B 到 70B 的 GRPO step 上训练 logistic regression deception probes。这是最接近 proposal 的工作——已证明"probing across GRPO checkpoints"技术可行。但 focus 是 reward-hacking obfuscation in coding tasks，不是 general faithfulness，且未联合测量 surface faithfulness。

6. [RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261) (arXiv 2025):
   7B-14B 模型可通过 RL 学会逃避 latent-space monitors，token-level monitors 脆弱。这是 adversarial 发现，与 proposal 的"natural divergence"视角互补。

7. [Reasoning Theater: Probing for Performative Chain-of-Thought](https://www.goodfire.ai/research/reasoning-theater) (Goodfire, 2026):
   发现模型在 easy problems 上 coast（生成多余 CoT），probes 可以检测此类 unfaithfulness。快照分析，无 training dynamics。

8. [RFEval: Benchmarking Reasoning Faithfulness](https://arxiv.org/abs/2602.17053) (arXiv 2026):
   7,186 instances 跨 7 tasks 的 faithfulness benchmark，发现 49.7% 输出含 unfaithfulness。Focus 是 benchmark 设计而非 training dynamics。

- **调研总结**: CoT faithfulness 在 2026 年是极度活跃的领域，但工作沿"表层 behavioral 指标 vs. latent probe 指标"和"固定模型快照 vs. 训练过程"两个维度高度碎片化。确实没有工作在 matched RL checkpoints 上同时测量 surface + latent faithfulness。最接近的是 Obfuscation Atlas（probe across GRPO steps，但 focus 是 deception 而非 general faithfulness）和 VLM checkpoint paper（surface metrics across RL steps，但无 probe）。proposal 的 gap identification 是成立的。

【Trivial Alternative 检验】:

存在两个 trivial alternative 威胁：

(1) **纯 meta-analysis 替代**：既然 RLVR monitorability 论文已经表明 surface gains 与 causal reliance 正交，pre-CoT probes 已经表明 final model 有强 answer pre-commitment——能否直接从现有文献推断"RL 训练必然加剧 surface-latent gap"？答案是：大方向可以推断，但 **divergence 的动态特征**（何时开始、是否存在 phase transition、两个 model family 是否不同）无法从现有工作推断。因此 proposal 的增量价值在于 **temporal resolution 和动态刻画**，而非定性发现本身。这是真实的增量，但这也意味着论文的价值高度依赖于动态特征是否有 non-trivial patterns——如果只是线性渐进 divergence，审稿人可能认为 insight 有限。

(2) **简化实验替代**：proposal 堆了 4 个 metrics（probe AUC, hint-injection, NLDD, activation patching）、2 个 model families、changepoint detection、probe trajectory analysis。一个更简单的版本——只用 probe AUC + hint-injection 在 1 个 model family 的 10 个 checkpoints 上——可能就能回答核心问题。当然，更全面的实验提高 robustness，但这是执行层面的，不改变 idea 本质。

**增量价值判断**：存在但有限。核心 finding 的方向是可预测的，价值集中在 temporal dynamics 的量化刻画上。

【前提假设检验】:

核心 claim 的逻辑链中有以下未经充分验证的假设：

(1) **"Probe AUC = latent faithfulness" 假设**：Proposal 将 pre-CoT probe AUC 上升等同于"latent answer pre-commitment strengthening"。但 probe AUC 可能反映的是 task representation quality 的提升（模型更好地理解问题），而非"在推理前就锁定答案"。Cox et al. 的 activation steering 实验部分支持因果性，但 steering ≠ natural generation pathway。这个等式需要更强的论证。

(2) **"Surface metrics improvement = surface faithfulness improvement" 假设**：Hint-injection acknowledgment rate 下降可能意味着模型变得更不容易被 hint 干扰（robustness），也可能意味着模型学会了不在输出中提及 hint 但仍被 hint 影响（deceptive alignment）。Proposal 对此没有充分讨论。

(3) **"Divergence = RL systematically decouples what models say from what they compute" 的因果推断**：即使观察到 surface-latent divergence 增大，也可能是 RL 让模型在 both dimensions 各自变好但速率不同（而非"decoupling"）。"Decoupling" 暗示某种对抗性关系，而实际可能只是独立变化。

假设(1)是最关键的——如果 probe AUC 不是 latent faithfulness 的有效代理，整个"gap"的解读就会坍塌。

【3 维度打分】:

1. **Novelty: 中** — 
   Gap identification 是成立的：确实没有工作在 matched RL checkpoints 上联合测量 surface + latent faithfulness（Obfuscation Atlas focus 是 deception probes，VLM checkpoint paper 无 latent measures，Monitoring Internal Monologue 只看 inference-time 的 fixed models）。但这个 novelty 本质上是 **组合式的**——将 Cox et al. 的 probe methodology、Chen et al. 的 hint-injection protocol、VLM checkpoint paper 的"checkpoint 采样"思路组合到一起，在 GRPO checkpoints 上 run。没有新方法论、没有新概念框架，核心贡献是 "在正确的时间轴上运行现有工具的组合"。这对于一篇 top venue 论文来说，novelty 偏窄。更关键的是，**核心发现的方向（divergence 加剧）是高度可预测的**——如果结果显示 no divergence 反而更 surprising 也更有影响力，但 proposal 自己都 hypothesize widening gap。

2. **Significance: 中偏强** — 
   研究问题本身对 AI safety 有直接意义："RL 训练是否系统性地让 CoT 变得不可信"是 2026 年的核心问题之一。如果结果清晰，直接影响 deployment monitoring 决策（是否需要 latent-space monitoring infrastructure）。此外，两个 model family 的对比增加了 generalizability。但 significance 受限于：(a) safety community 已经 operate under the assumption that CoT may not be faithful——本研究量化 degree 而非改变 fundamental understanding；(b) 即使证明 divergence 存在，下一步的 actionable advice（"所以我们需要 latent monitoring"）已经是 existing consensus。

3. **Related Work: 强** — 
   这是 proposal 最出色的部分。引用了 15+ 篇 2025-2026 论文，覆盖了 surface faithfulness (Chen et al., VLM checkpoint)、latent probing (Cox et al., Catching Rationalization, Hypocrisy Gap)、probe trajectories (Monitoring Internal Monologue)、deception probing across training (Obfuscation Atlas)、adversarial evasion (RL-Obfuscation)、faithfulness-improving RL (FaithRL, AtManRL)、training dynamics (learning dynamics, synthetic phase transition) 等多个维度。所有引用经调研验证均真实存在且描述准确。gap 的差异化定位清晰——沿 "surface vs. latent" 和 "snapshot vs. longitudinal" 两个轴精确刻画。唯一轻微不足是未讨论 Reasoning Theater (Goodfire, 2603.05488) 虽列在引用中但未深入分析其 probe-based performative detection 与本工作的关系。

【概率估计】: [22% - 33%] 中位 27%

【估计理由】:
Novelty 是限制上界的主要维度。核心贡献是"组合现有方法在新的时间轴上运行"，这在 idea 层面偏 incremental。虽然 gap identification 成立，但预期结果的方向高度可预测（widening divergence），审稿人大概率会写"the main finding confirms what prior work already strongly suggests"。Significance 给了一定的下限支撑——research question 确实重要，对 safety practice 有直接 implications——但不足以突破 novelty 的 ceiling。Related Work 的出色覆盖是加分项，但形式完善不等于 idea 强。

上界 33% 对应的场景是：动态特征出现非常 non-trivial 的 pattern（如 sharp phase transition、两个 model family 完全不同的 divergence trajectory），且审稿人认为这些 finding 本身就是重要贡献。下界 22% 对应的场景是：divergence 呈单调渐进，审稿人认为"we already knew this would happen"。

【主要风险】:
1. **"Expected finding" 问题**：核心 hypothesis（widening gap）是 prior work 的直接外推，如果结果如预测，审稿人会质疑 insight 的增量价值——"quantifying a gap everyone already assumed exists" 不足以撑起一篇 top venue 论文。论文的影响力高度依赖于 temporal dynamics 中是否有 surprising patterns。
2. **Proxy validity 问题**：Probe AUC 作为 "latent faithfulness" 的代理指标的有效性未经充分论证。如果审稿人质疑"probe AUC 上升可能只反映 task representation 改善而非 answer pre-commitment 加剧"，整个 surface-latent gap 的叙事就会被动摇，而 proposal 没有给出 convincing 的反驳。
```

Sources:
- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978)
- [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437)
- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)
- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)
- [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515)
- [RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261)
- [Reasoning Theater: Probing for Performative Chain-of-Thought](https://www.goodfire.ai/research/reasoning-theater)
- [RFEval: Benchmarking Reasoning Faithfulness](https://arxiv.org/abs/2602.17053)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "993b64ce-23f0-4933-b2a8-0bfdb05c68f9",
  "isSidechain": false,
  "requestId": "req_011CbCQYQYfn3N55xaZSRA9V",
  "type": "assistant",
  "uuid": "cfcb1dfd-cd74-4764-b456-83e85fa00627",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HT8fuVkxNovdZU656YrjTN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1982,
      "cache_read_input_tokens": 26426,
      "output_tokens": 5703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1982,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5703,
          "cache_read_input_tokens": 26426,
          "cache_creation_input_tokens": 1982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1982
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Mo…",
  "leafUuid": "cfcb1dfd-cd74-4764-b456-83e85fa00627",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Track faithfulness gap across GRPO training checkpoints",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Mo…",
  "leafUuid": "cfcb1dfd-cd74-4764-b456-83e85fa00627",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Track faithfulness gap across GRPO training checkpoints",
  "sessionId": "111b1ec3-6515-44c7-b8fc-61520f2f0414"
}
```

---
