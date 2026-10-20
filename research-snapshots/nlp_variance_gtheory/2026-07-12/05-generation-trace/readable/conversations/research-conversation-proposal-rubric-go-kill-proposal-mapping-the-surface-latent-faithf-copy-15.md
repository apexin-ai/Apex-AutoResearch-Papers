# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Mapping the Surface-Latent Faithf

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/35f5c275-351b-4dc6-a414-ef1af47b83ed.jsonl`
- **Structured JSON:** [`91b6389484735692defb.json`](../../sessions/91/91b6389484735692defb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:35:09.598Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:35:09.598Z",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Models\n\n## Description\nWe propose the first systematic longitudinal study jointly tracking surface-level CoT faithfulness and probe-measured latent faithfulness across matched GRPO training checkpoints of open-weight reasoning models. Unlike the VLM checkpoint study (2602.12506) which used only LLM-as-judge surface metrics on vision-language models, and unlike 'Monitoring the Internal Monologue' (2605.18549) which tracked probe trajectories during inference of fixed models, we generate fine-grained GRPO checkpoints (~20 per model) from two architecturally distinct families — DeepSeek-R1-Distill-Qwen-7B (starting with distilled reasoning) and Qwen3-8B (starting from base) — and at each checkpoint measure: (1) linear probe AUC on pre-CoT residual-stream activations as a latent answer-commitment proxy, (2) hint-injection acknowledgment rate (Chen et al. protocol) as a surface faithfulness metric, (3) NLDD reasoning horizon length as a causal reliance metric, and (4) activation patching effect sizes for CoT tokens. The central hypothesis is that GRPO training creates a widening surface-latent faithfulness gap — surface metrics improve (or plateau) while latent answer pre-commitment strengthens — consistent with the RLVR monitorability finding that surface gains are orthogonal to causal reliance. We apply changepoint detection as an exploratory tool to characterize divergence dynamics without assuming specific functional forms. This work bridges the critical gap between training-dynamics studies (which lack latent measures) and mechanistic faithfulness studies (which lack temporal depth), providing the first temporal map of how RL systematically decouples what reasoning models say from what they compute. Results directly inform whether RL-trained reasoning models require latent-space monitoring infrastructure beyond CoT inspection.\n\n## Core Problem\nWhen and how does the gap between surface CoT faithfulness (measured by behavioral metrics like hint-injection rates and causal reliance) and latent faithfulness (measured by residual-stream probes predicting answer pre-commitment) develop during GRPO training of reasoning models — and what dynamics characterize this divergence?\n\n## Opportunity\nThree converging 2026 findings create a precise, actionable gap. First, the RLVR monitorability paper (2602.03978) showed that RL's surface-monitorability gains come from response distribution sharpening and increased prompt attention — NOT from stronger causal reliance on reasoning traces. Second, pre-CoT probes (2603.01437) demonstrated that instruction-tuned models encode answers in residual-stream activations before generating any CoT (>0.9 AUC), with these directions being causally efficacious. Third, the VLM checkpoint paper (2602.12506) showed an accuracy-faithfulness trade-off during RL fine-tuning — but using only LLM-as-judge surface metrics on vision-language models, with no latent-space analysis. Meanwhile, 'Monitoring the Internal Monologue' (2605.18549) introduced probe trajectories as a powerful inference-time monitoring tool but analyzed only fixed, already-trained models — never tracking how probe characteristics evolve across RL training steps. The Obfuscation Atlas (2602.15515) tracked deception probes across RLVR but focused narrowly on reward-hacking obfuscation rather than general faithfulness divergence. Nobody has jointly measured both surface faithfulness metrics and activation-probe-based latent faithfulness at matched RL training checkpoints to characterize how — and how fast — RL decouples what reasoning models say from what they compute. If this divergence is large and systematic, RL-trained reasoning models require latent-space monitoring beyond CoT inspection for safe deployment.\n\n## Related Work / Landscape\nThe CoT faithfulness literature in 2026 is large but fragmented along complementary axes, leaving the longitudinal surface-latent gap unstudied:\n\n**Surface faithfulness across RL steps (behavioral only):** Chen et al. (Anthropic 2025, 2505.05410) measured surface faithfulness via hint-injection across RL steps, finding initial improvement that plateaus (~25% for Claude 3.7 Sonnet). The VLM checkpoint paper (2602.12506) tracked CoT consistency via LLM-as-judge across GRPO checkpoints of Qwen2.5-VL-7B-Instruct, finding an accuracy-faithfulness trade-off — but used only behavioral metrics (letter entropy, judge-rated consistency) with no activation probes, and studied VLMs rather than language models.\n\n**Latent faithfulness in final models (snapshot only):** Pre-CoT probes (2603.01437) showed >0.9 AUC answer prediction from residual streams of Gemma 2 and Qwen 2.5 before any CoT tokens. 'Catching Rationalization in the Act' (2603.17199) trained probes to detect motivated reasoning pre- and post-CoT. 'The Hypocrisy Gap' (2602.02496) used SAEs to quantify internal-belief/CoT divergence. 'Why Models Know But Don't Say' (2603.26410) measured thinking-token vs. answer divergence. All analyze final models only.\n\n**Probe trajectories during inference (token-level, not training-level):** 'Monitoring the Internal Monologue' (2605.18549, May 2026) constructed probe trajectories across token positions during generation, achieving 95% AUROC for predicting outcomes. However, this tracks probes across tokens within a single generation of a fixed model — not across RL training checkpoints. Their models (Llama-8B-R1-Distill, Qwen3-4B/8B/14B) are final checkpoints only.\n\n**Deception probes across RLVR (deception-specific):** The Obfuscation Atlas (2602.15515) trained logistic regression probes on residual streams of Llama-3-8B through 70B across GRPO steps, mapping deception emergence. But their focus is reward-hacking obfuscation in coding tasks, not general reasoning faithfulness, and they don't measure surface faithfulness metrics jointly.\n\n**RL-Obfuscation (adversarial evasion):** RL-Obfuscation (2506.14261) showed 7B-14B models can learn to evade latent-space monitors through RL, with token-level monitors being vulnerable. This is an adversarial finding about monitor fragility, not a characterization of natural faithfulness divergence.\n\n**Faithfulness-improving RL methods:** FaithRL (2602.03507), AtManRL (2604.16158), and faithfulness-aware step-level RL (2602.05897) propose RL objectives that improve faithfulness, but none characterize the divergence trajectory of standard GRPO/RLVR training.\n\n**RL training dynamics:** Learning dynamics papers (2601.04670) show reduced feature diversity during RL but don't track faithfulness. The synthetic phase-transition paper (2602.01017) demonstrates faithful→unfaithful transitions under controlled noise in toy arithmetic — the only prior showing discrete transitions, but in a setting far removed from real GRPO.\n\n**The gap:** No existing work jointly tracks probe-measured latent faithfulness AND surface CoT faithfulness metrics at matched RL training checkpoints across training to characterize divergence dynamics in language reasoning models.\n\n## Approach\nWe produce our own fine-grained GRPO training checkpoints from two architecturally distinct open-weight model families, then jointly measure surface and latent faithfulness at each checkpoint.\n\n**Model families and checkpoint generation:**\n(1) DeepSeek-R1-Distill-Qwen-7B as base model, trained with GRPO using the Open-R1 pipeline (HuggingFace TRL) on MATH + GPQA, saving checkpoints every 50 GRPO steps for ~20 checkpoints across training. This model starts with distilled reasoning capability, letting us study how further RL reshapes faithfulness.\n(2) Qwen3-8B (base dense model, Apache 2.0) trained with the same GRPO pipeline and datasets, providing an architecturally distinct family that starts without distilled reasoning traces.\n\n**Metrics at each checkpoint:**\n(a) *Latent faithfulness proxy*: Train linear probes on residual-stream activations at the last pre-CoT token (following the methodology of Cox et al., 2603.01437), predicting the model's final answer. Report probe AUC and the layer at which AUC first exceeds 0.8 ('commitment layer'). A rising probe AUC across training indicates strengthening answer pre-commitment — the model increasingly 'knows' its answer before reasoning.\n(b) *Surface faithfulness — hint-injection*: Apply Chen et al.'s protocol with sycophancy and anchoring hints on a fixed MMLU/GPQA subset (~500 items). Report hint-acknowledgment rate (lower = more faithful surface behavior).\n(c) *Causal reliance — NLDD*: Compute the Normalized Logit Difference Decay metric (2602.11201) by corrupting individual reasoning steps and measuring confidence drops. Report the Reasoning Horizon k* (the chain-length fraction beyond which steps have negligible causal effect).\n(d) *Activation patching* (on 5 evenly-spaced checkpoints per family): Measure the causal effect of CoT-token activations on the final answer via mean-ablation patching, quantifying how much the model's computation actually flows through the reasoning trace.\n\n**Analysis:**\n- Construct the *surface-latent divergence curve*: plot surface faithfulness improvement (declining hint-acknowledgment rate) against latent bypass strengthening (rising probe AUC / shortening reasoning horizon) across GRPO steps.\n- Apply changepoint detection (PELT algorithm) as an *exploratory* tool to identify whether divergence accelerates at specific training phases — we do NOT claim phase transitions a priori but test for non-linear dynamics.\n- Compare divergence trajectories between the two model families to assess generality.\n- On a subset of checkpoints, apply the probe-trajectory methodology of 'Monitoring the Internal Monologue' (2605.18549) to test whether the character of inference-time probe trajectories (volatility, trend features) changes systematically across training — bridging their token-level and our checkpoint-level analyses.\n\n**Scaling validation:** If initial 7B results show clear divergence, replicate core probe + hint-injection measurements on DeepSeek-R1-Distill-Qwen-14B with ~10 GRPO checkpoints to verify the pattern holds at larger scale.\n\n**Key methodological choices justified:**\n- Using R1-Distill-7B rather than R1-671B: reviewer correctly identified that Dev1/Dev2/Dev3 checkpoints are not publicly available. Distilled 7B models are computationally tractable (single A100 for inference, 8×A100 for GRPO training) and let us generate arbitrarily fine-grained checkpoints.\n- GRPO rather than PPO: GRPO is the algorithm used in DeepSeek-R1 and the VLM checkpoint paper, ensuring comparability.\n- Two model families with different starting points (distilled reasoning vs. base): controls for whether divergence is an artifact of the starting model's reasoning capability.\n\n## Inspiration\nDirect gap between three convergent findings: (1) RLVR monitorability gains NOT from causal reliance (2602.03978), (2) pre-CoT probes show answer pre-commitment exists in residual streams (2603.01437), (3) VLM checkpoint paper shows accuracy-faithfulness trade-off during RL but with no latent-space analysis (2602.12506). The 'Monitoring the Internal Monologue' paper (2605.18549) shows probe trajectories are powerful for monitoring but leaves the training-dynamics dimension unexplored. The Obfuscation Atlas (2602.15515) demonstrates that probing across RLVR checkpoints is technically feasible at scale.\n\n## Key References\n- Reasoning Models Don't Always Say What They Think (Anthropic 2025, arXiv 2505.05410)\n- Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning (arXiv 2026, 2602.03978)\n- Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering (arXiv 2026, 2603.01437)\n- On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs (arXiv 2026, 2602.12506)\n- Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics (arXiv 2026, 2605.18549)\n- The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes (FAR AI/arXiv 2026, 2602.15515)\n- RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? (arXiv 2025/2026, 2506.14261)\n- How Does Unfaithful Reasoning Emerge from Autoregressive Training? A Study of Synthetic Experiments (arXiv 2026, 2602.01017)\n- Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning (arXiv 2026, 2602.11201)\n- Learning Dynamics in RL Post-Training for Language Models (arXiv 2026, 2601.04670)\n- Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Goodfire/arXiv 2026, 2603.05488)\n- The Hypocrisy Gap: Quantifying Divergence Between Internal Belief and Chain-of-Thought Explanation via Sparse Autoencoders (arXiv 2026, 2602.02496)\n- Catching Rationalization in the Act: Detecting Motivated Reasoning Before and After CoT via Activation Probing (arXiv 2026, 2603.17199)\n- Why Models Know But Don't Say: CoT Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models (arXiv 2026, 2603.26410)\n- FaithRL: Learning to Reason Faithfully through Step-Level Faithfulness Maximization (arXiv 2026, 2602.03507)\n- AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency (arXiv 2026, 2604.16158)\n- DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (DeepSeek 2025, 2501.12948)\n- Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models (arXiv 2025, 2507.18014)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '350–500 A100-hours (GRPO training: ~80 A100-hrs × 2 families = 160 hrs; probe training + inference on ~20 checkpoints × 2 families: ~100 hrs; hint-injection evaluation: ~40 hrs; NLDD computation: ~30 hrs; activation patching on 10 checkpoints: ~50 hrs; 14B scaling validation: ~70 hrs)', 'timeline': '8–11 weeks (2 weeks GRPO training + pipeline setup, 3 weeks probe training & surface measurements in parallel, 2 weeks activation patching & NLDD, 1–2 weeks analysis, 1–2 weeks writing)', 'estimated_gpu_cost': '$900–$1,250 at ~$2.50/A100-hr spot pricing'}\n- **human_in_loop**: {'gpu_hours': '300–400 A100-hours (Claude handles probe training scripts, metric computation pipelines, statistical analysis, and plotting; human designs experiments, interprets results, writes key paper sections)', 'timeline': '6–8 weeks', 'claude_api_cost': '$120–$250 (Sonnet 4.6 for code generation, data analysis scripts, and paper drafting; ~40M input + 8M output tokens)', 'estimated_gpu_cost': '$750–$1,000'}\n- **auto_research**: {'gpu_hours': '300–400 A100-hours', 'timeline': '4–5 weeks (parallelized GRPO training for both families, then parallelized probe training and evaluation across checkpoints)', 'claude_api_cost': '$300–$550 (orchestration agent managing GRPO runs, checkpoint evaluation sweeps, result interpretation, iterative analysis; ~120M input + 25M output tokens)', 'estimated_gpu_cost': '$750–$1,000', 'speed_bottleneck': 'Sequential dependency: GRPO training must complete (or reach sufficient checkpoints) before probe training begins. However, probe training on early checkpoints can start while GRPO training continues. The two model families can be trained in parallel. 14B scaling validation is contingent on 7B results being compelling.'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T18:35:09.600Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:35:09.600Z",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed"
}
```

---

## Round 1

39 recorded events

### User

_source line 3 · 2026-05-19T18:35:09.611Z_

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
  "promptId": "f6d1450c-25e4-4b19-8c5a-b25909ce1666",
  "type": "user",
  "uuid": "b98f4077-ccc0-488c-9c17-dd86a1e20d9e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:35:09.610Z_

```json
{
  "parentUuid": "b98f4077-ccc0-488c-9c17-dd86a1e20d9e",
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
  "uuid": "89f3c11a-abca-4c33-a307-a627aad7c9b0",
  "timestamp": "2026-05-19T18:35:09.610Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:35:09.610Z_

```json
{
  "parentUuid": "89f3c11a-abca-4c33-a307-a627aad7c9b0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9d9f015c-ae19-453a-ac2e-762b4170ca72",
  "timestamp": "2026-05-19T18:35:09.610Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
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
  "leafUuid": "9d9f015c-ae19-453a-ac2e-762b4170ca72",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Study surface-latent faithfulness gap in GRPO reasoning models",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:35:21.487Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026 (Conference on Robot Learning). Wait, actually, let me re-read - the system prompt says "CoRL 2026 主会" but this proposal is about CoT faithfulness, reasoning models, GRPO training - this is clearly an NLP/AI safety paper, not a robotics paper. Let me re-read... Actually the system prompt says "CoRL 2026" but the rubric mentions "NLP/CL 领域". Let me not get hung up on the venue and focus on evaluating the idea quality.

Actually, wait - CoRL is Conference on Robot Learning. 

I'm realizing there's a mismatch between the venue and the paper topic, but I'll proceed with evaluating this as a top-tier ML/AI submission. Before I assess the proposal itself, I should search for the key papers and recent work on CoT faithfulness and RL training dynamics to understand the landscape better.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d9f015c-ae19-453a-ac2e-762b4170ca72",
  "isSidechain": false,
  "requestId": "req_011CbCQiiLmtb4bEFwMkHCkv",
  "type": "assistant",
  "uuid": "1195ac57-5ce3-4eb3-813c-5eaf94416b3f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNiGVU4rxyt4MxKGtmMgC4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19549,
      "output_tokens": 364,
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
          "output_tokens": 364,
          "cache_read_input_tokens": 19549,
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

_source line 9 · 2026-05-19T18:35:21.495Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UDvLJfZbNLUtrx6Y8Yaq3a`</summary>

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
  "parentUuid": "1195ac57-5ce3-4eb3-813c-5eaf94416b3f",
  "isSidechain": false,
  "requestId": "req_011CbCQiiLmtb4bEFwMkHCkv",
  "type": "assistant",
  "uuid": "7b217037-8846-43ac-997d-6826843250bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KNiGVU4rxyt4MxKGtmMgC4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19549,
      "output_tokens": 364,
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
          "output_tokens": 364,
          "cache_read_input_tokens": 19549,
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

_source line 10 · 2026-05-19T18:35:21.501Z_

<details><summary>↩ Tool result · `toolu_01UDvLJfZbNLUtrx6Y8Yaq3a`</summary>

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
  "parentUuid": "7b217037-8846-43ac-997d-6826843250bd",
  "isSidechain": false,
  "promptId": "f6d1450c-25e4-4b19-8c5a-b25909ce1666",
  "type": "user",
  "uuid": "8da49fda-92cf-4169-bbd9-33632ab68d44",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "7b217037-8846-43ac-997d-6826843250bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-19T18:35:24.404Z_

Now let me conduct the required field research with multiple targeted searches before making any judgments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8da49fda-92cf-4169-bbd9-33632ab68d44",
  "isSidechain": false,
  "requestId": "req_011CbCQjbuM4tjBt3v8VYt6j",
  "type": "assistant",
  "uuid": "d366de90-cef6-4dfc-9460-13195a753aa0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiT5ELSx1ZkEut2F8WLvw1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 892,
      "cache_read_input_tokens": 19549,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 19549,
          "cache_creation_input_tokens": 892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 892
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

_source line 12 · 2026-05-19T18:35:25.105Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WJZ232spfLVdrBFYNAaq7a`</summary>

```json
{
  "query": "CoT faithfulness probes RL training dynamics 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d366de90-cef6-4dfc-9460-13195a753aa0",
  "isSidechain": false,
  "requestId": "req_011CbCQjbuM4tjBt3v8VYt6j",
  "type": "assistant",
  "uuid": "d26acb1c-4215-40e7-88da-78485742acd5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiT5ELSx1ZkEut2F8WLvw1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 892,
      "cache_read_input_tokens": 19549,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 19549,
          "cache_creation_input_tokens": 892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 892
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

_source line 13 · 2026-05-19T18:35:25.354Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TquuL3MPTrHwdpKg82qvZK`</summary>

```json
{
  "query": "RLVR monitorability surface faithfulness latent faithfulness divergence 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d26acb1c-4215-40e7-88da-78485742acd5",
  "isSidechain": false,
  "requestId": "req_011CbCQjbuM4tjBt3v8VYt6j",
  "type": "assistant",
  "uuid": "acd47bdb-babf-411a-a216-e601946fa640",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiT5ELSx1ZkEut2F8WLvw1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 892,
      "cache_read_input_tokens": 19549,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 19549,
          "cache_creation_input_tokens": 892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 892
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

_source line 14 · 2026-05-19T18:35:25.785Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UDCK6k86Va6RTfynpveE5z`</summary>

```json
{
  "query": "pre-CoT probes residual stream answer pre-commitment 2603.01437"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acd47bdb-babf-411a-a216-e601946fa640",
  "isSidechain": false,
  "requestId": "req_011CbCQjbuM4tjBt3v8VYt6j",
  "type": "assistant",
  "uuid": "5d182861-1636-4b63-9636-c95c5930138f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiT5ELSx1ZkEut2F8WLvw1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 892,
      "cache_read_input_tokens": 19549,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 892,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 19549,
          "cache_creation_input_tokens": 892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 892
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

_source line 15 · 2026-05-19T18:35:32.472Z_

<details><summary>↩ Tool result · `toolu_01UDCK6k86Va6RTfynpveE5z`</summary>

```text
Web search results for query: "pre-CoT probes residual stream answer pre-commitment 2603.01437"

Links: [{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/html/2603.01437"},{"title":"[Literature Review] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://www.themoonlight.io/en/review/decoding-answers-before-chain-of-thought-evidence-from-pre-cot-probes-and-activation-steering"},{"title":"[2603.01437] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/abs/2603.01437"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/pdf/2603.01437"},{"title":"Post-Hoc Reasoning in Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering | OpenReview","url":"https://openreview.net/forum?id=UMUYpeXtJQ"},{"title":"Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing","url":"https://arxiv.org/pdf/2603.17199"},{"title":"[2603.17199] Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing","url":"https://arxiv.org/abs/2603.17199"}]

I found the research paper you're looking for. Here are the key findings:

**Paper Title:** "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering" by Kyle Cox, Darius Kianersi, and Adrià Garriga-Alonso (arXiv:2603.01437)

**Main Findings:**

The paper investigates whether chain-of-thought (CoT) reasoning in large language models is faithful to their actual decision-making process. The researchers provide mechanistic evidence that instruction-tuned models often determine their answer before generating CoT. They trained linear probes on residual stream activations at the last token before CoT and could predict the model's final answer with >0.9 AUC on most tasks.

**Three Key Hypotheses:**

1. **Representational pre-commitment:** The model's final answer is encoded in pre-CoT activations in the residual stream and is linearly decodable by a simple probe.

2. **Causal pre-commitment:** The probe direction is not merely predictive but causal—steering activations along this direction shifts the model's answer far more than equally large orthogonal perturbations.

3. **Pathologies of unfaithfulness:** When steered in the direction of the incorrect response, the model's verbalized reasoning exhibits confabulation (stating false premises to support the steered answer) and non-entailment (stating true premises but giving a conclusion that does not follow).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d182861-1636-4b63-9636-c95c5930138f",
  "isSidechain": false,
  "promptId": "f6d1450c-25e4-4b19-8c5a-b25909ce1666",
  "type": "user",
  "uuid": "fff144ed-ffce-4dd8-853c-f348c0e21533",
  "toolUseResult": {
    "query": "pre-CoT probes residual stream answer pre-commitment 2603.01437",
    "results": [
      {
        "tool_use_id": "srvtoolu_018CTXAViLrZ1edXxxs9nn7d",
        "content": [
          {
            "title": "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://arxiv.org/html/2603.01437"
          },
          {
            "title": "[Literature Review] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://www.themoonlight.io/en/review/decoding-answers-before-chain-of-thought-evidence-from-pre-cot-probes-and-activation-steering"
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
            "title": "Post-Hoc Reasoning in Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering | OpenReview",
            "url": "https://openreview.net/forum?id=UMUYpeXtJQ"
          },
          {
            "title": "Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing",
            "url": "https://arxiv.org/pdf/2603.17199"
          },
          {
            "title": "[2603.17199] Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing",
            "url": "https://arxiv.org/abs/2603.17199"
          }
        ]
      },
      "I found the research paper you're looking for. Here are the key findings:\n\n**Paper Title:** \"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering\" by Kyle Cox, Darius Kianersi, and Adrià Garriga-Alonso (arXiv:2603.01437)\n\n**Main Findings:**\n\nThe paper investigates whether chain-of-thought (CoT) reasoning in large language models is faithful to their actual decision-making process. The researchers provide mechanistic evidence that instruction-tuned models often determine their answer before generating CoT. They trained linear probes on residual stream activations at the last token before CoT and could predict the model's final answer with >0.9 AUC on most tasks.\n\n**Three Key Hypotheses:**\n\n1. **Representational pre-commitment:** The model's final answer is encoded in pre-CoT activations in the residual stream and is linearly decodable by a simple probe.\n\n2. **Causal pre-commitment:** The probe direction is not merely predictive but causal—steering activations along this direction shifts the model's answer far more than equally large orthogonal perturbations.\n\n3. **Pathologies of unfaithfulness:** When steered in the direction of the incorrect response, the model's verbalized reasoning exhibits confabulation (stating false premises to support the steered answer) and non-entailment (stating true premises but giving a conclusion that does not follow)."
    ],
    "durationSeconds": 6.6824737690000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5d182861-1636-4b63-9636-c95c5930138f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T18:35:33.787Z_

<details><summary>↩ Tool result · `toolu_01WJZ232spfLVdrBFYNAaq7a`</summary>

```text
Web search results for query: "CoT faithfulness probes RL training dynamics 2026 arXiv"

Links: [{"title":"Reasoning Theater: Probing for Performative Chain-of-Thought","url":"https://www.goodfire.ai/research/reasoning-theater"},{"title":"Confessions vs. CoT Monitoring vs. Probes: Three Bets on Model Honesty | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/three-bets-model-honesty/"},{"title":"Published as a workshop paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.16158"},{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410v1"},{"title":"[2602.20710] Counterfactual Simulation Training for Chain-of-Thought Faithfulness","url":"https://arxiv.org/abs/2602.20710"},{"title":"Stop Rewarding Hallucinated Steps: Faithfulness-Aware Step-Level Reinforcement Learning for Small Reasoning Models","url":"https://arxiv.org/pdf/2602.05897"},{"title":"On Robustness and Chain-of-Thought consistency of RL-Finetuned VLMs","url":"https://arxiv.org/html/2602.12506v1"},{"title":"AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency","url":"https://arxiv.org/html/2604.16158"},{"title":"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning","url":"https://arxiv.org/pdf/2602.03978"}]

Based on the search results, here are the key findings related to CoT faithfulness probes and RL training dynamics from 2026 arXiv papers:

## Key Research Findings

**Performative Reasoning and Faithfulness Decay**

Training models with reinforcement learning has led to longer, more elaborate reasoning traces that seem monitorable, but prior work has indicated that chain-of-thought is not always faithful. Recent work used activation probing to demonstrate "Reasoning Theater," where models lock in answers early but continue generating performative reasoning tokens.

**Training Dynamics Phase Transitions**

Training dynamics show a phase transition from faithful stepwise reasoning to unfaithful "skip-step" reasoning when noise exceeds a critical threshold. Additionally, research discovered a consistent "Reasoning Horizon" where at 70-85% of chain length, reasoning tokens have little or even negative effect on the final answer.

**Probes for Detecting Unfaithfulness**

Probes can enable monitoring for unfaithfulness by using signals that aren't present in model outputs, with minimal inference overhead. RL training incentivizes reasoning that leads to correct answers, so the resulting CoT only needs to be useful to the model.

**Addressing Faithfulness Through RL Methods**

Several papers propose solutions: outcome rewards focus on answer correctness and do not enforce that the reasoning trace causally influences the final prediction, whereas some approaches explicitly reward causal dependency between CoT tokens and the answer.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d26acb1c-4215-40e7-88da-78485742acd5",
  "isSidechain": false,
  "promptId": "f6d1450c-25e4-4b19-8c5a-b25909ce1666",
  "type": "user",
  "uuid": "55d2f222-8002-44f3-910e-4f2ab6d2255a",
  "toolUseResult": {
    "query": "CoT faithfulness probes RL training dynamics 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01C8BDXpcHZ6zmHCREbMDgdL",
        "content": [
          {
            "title": "Reasoning Theater: Probing for Performative Chain-of-Thought",
            "url": "https://www.goodfire.ai/research/reasoning-theater"
          },
          {
            "title": "Confessions vs. CoT Monitoring vs. Probes: Three Bets on Model Honesty | Subhadip Mitra",
            "url": "https://subhadipmitra.com/blog/2026/three-bets-model-honesty/"
          },
          {
            "title": "Published as a workshop paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2604.16158"
          },
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410v1"
          },
          {
            "title": "[2602.20710] Counterfactual Simulation Training for Chain-of-Thought Faithfulness",
            "url": "https://arxiv.org/abs/2602.20710"
          },
          {
            "title": "Stop Rewarding Hallucinated Steps: Faithfulness-Aware Step-Level Reinforcement Learning for Small Reasoning Models",
            "url": "https://arxiv.org/pdf/2602.05897"
          },
          {
            "title": "On Robustness and Chain-of-Thought consistency of RL-Finetuned VLMs",
            "url": "https://arxiv.org/html/2602.12506v1"
          },
          {
            "title": "AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency",
            "url": "https://arxiv.org/html/2604.16158"
          },
          {
            "title": "Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning",
            "url": "https://arxiv.org/pdf/2602.03978"
          }
        ]
      },
      "Based on the search results, here are the key findings related to CoT faithfulness probes and RL training dynamics from 2026 arXiv papers:\n\n## Key Research Findings\n\n**Performative Reasoning and Faithfulness Decay**\n\nTraining models with reinforcement learning has led to longer, more elaborate reasoning traces that seem monitorable, but prior work has indicated that chain-of-thought is not always faithful. Recent work used activation probing to demonstrate \"Reasoning Theater,\" where models lock in answers early but continue generating performative reasoning tokens.\n\n**Training Dynamics Phase Transitions**\n\nTraining dynamics show a phase transition from faithful stepwise reasoning to unfaithful \"skip-step\" reasoning when noise exceeds a critical threshold. Additionally, research discovered a consistent \"Reasoning Horizon\" where at 70-85% of chain length, reasoning tokens have little or even negative effect on the final answer.\n\n**Probes for Detecting Unfaithfulness**\n\nProbes can enable monitoring for unfaithfulness by using signals that aren't present in model outputs, with minimal inference overhead. RL training incentivizes reasoning that leads to correct answers, so the resulting CoT only needs to be useful to the model.\n\n**Addressing Faithfulness Through RL Methods**\n\nSeveral papers propose solutions: outcome rewards focus on answer correctness and do not enforce that the reasoning trace causally influences the final prediction, whereas some approaches explicitly reward causal dependency between CoT tokens and the answer."
    ],
    "durationSeconds": 8.678349941999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d26acb1c-4215-40e7-88da-78485742acd5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T18:35:39.290Z_

<details><summary>↩ Tool result · `toolu_01TquuL3MPTrHwdpKg82qvZK`</summary>

```text
Web search results for query: "RLVR monitorability surface faithfulness latent faithfulness divergence 2026"

Links: [{"title":"[2602.03978] Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning","url":"https://arxiv.org/abs/2602.03978"},{"title":"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning","url":"https://arxiv.org/html/2602.03978v1"},{"title":"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning","url":"https://arxiv.org/pdf/2602.03978"},{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410v1"},{"title":"The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward","url":"https://arxiv.org/pdf/2509.07430"},{"title":"FaithRL: Learning to Reason Faithfully through Step-Level Faithfulness Maximization","url":"https://arxiv.org/pdf/2602.03507"},{"title":"REASONING UNDER PRESSURE: HOW DO TRAINING INCENTIVES INFLUENCE CHAIN-OF-THOUGHT","url":"https://arxiv.org/pdf/2512.00218"}]

Based on the search results, I found several relevant research papers related to your query:

## Main Result: "Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning"

The primary result shows that monitorability—the degree to which CoT faithfully and informatively reflects internal computation—can appear as a "free gift" during the early stages of Reinforcement Learning with Verifiable Rewards (RLVR).

The research demonstrates that this effect is not universal: monitorability improvements are strongly data-dependent, with results highlighting the critical role of data diversity and instruction-following data during RLVR training.

## Related Concepts

**Surface vs. Latent Faithfulness:** Recent work shows that monitoring only visible answer text can miss a significant portion of cases where models' internal reasoning diverges from their outputs, with high-divergence models missing over 90% of cases.

**RLVR and Divergence:** While RLVR-tuned models improve single-attempt performance, their multi-attempt performance often stagnates or degrades compared to base models, suggesting RLVR may overfit to known solution paths rather than teaching novel reasoning.

**Faithfulness in RLVR:** Recent approaches like FaithRL work to reduce hallucination rates while maintaining answer correctness and increasing step-wise reasoning faithfulness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acd47bdb-babf-411a-a216-e601946fa640",
  "isSidechain": false,
  "promptId": "f6d1450c-25e4-4b19-8c5a-b25909ce1666",
  "type": "user",
  "uuid": "a2389d6d-5ee3-49f0-9a7c-54c23ffb4c78",
  "toolUseResult": {
    "query": "RLVR monitorability surface faithfulness latent faithfulness divergence 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WgJNkesCwdTHG2n9YVu8SY",
        "content": [
          {
            "title": "[2602.03978] Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning",
            "url": "https://arxiv.org/abs/2602.03978"
          },
          {
            "title": "Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning",
            "url": "https://arxiv.org/html/2602.03978v1"
          },
          {
            "title": "Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning",
            "url": "https://arxiv.org/pdf/2602.03978"
          },
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410v1"
          },
          {
            "title": "The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward",
            "url": "https://arxiv.org/pdf/2509.07430"
          },
          {
            "title": "FaithRL: Learning to Reason Faithfully through Step-Level Faithfulness Maximization",
            "url": "https://arxiv.org/pdf/2602.03507"
          },
          {
            "title": "REASONING UNDER PRESSURE: HOW DO TRAINING INCENTIVES INFLUENCE CHAIN-OF-THOUGHT",
            "url": "https://arxiv.org/pdf/2512.00218"
          }
        ]
      },
      "Based on the search results, I found several relevant research papers related to your query:\n\n## Main Result: \"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning\"\n\nThe primary result shows that monitorability—the degree to which CoT faithfully and informatively reflects internal computation—can appear as a \"free gift\" during the early stages of Reinforcement Learning with Verifiable Rewards (RLVR).\n\nThe research demonstrates that this effect is not universal: monitorability improvements are strongly data-dependent, with results highlighting the critical role of data diversity and instruction-following data during RLVR training.\n\n## Related Concepts\n\n**Surface vs. Latent Faithfulness:** Recent work shows that monitoring only visible answer text can miss a significant portion of cases where models' internal reasoning diverges from their outputs, with high-divergence models missing over 90% of cases.\n\n**RLVR and Divergence:** While RLVR-tuned models improve single-attempt performance, their multi-attempt performance often stagnates or degrades compared to base models, suggesting RLVR may overfit to known solution paths rather than teaching novel reasoning.\n\n**Faithfulness in RLVR:** Recent approaches like FaithRL work to reduce hallucination rates while maintaining answer correctness and increasing step-wise reasoning faithfulness."
    ],
    "durationSeconds": 13.933286852999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "acd47bdb-babf-411a-a216-e601946fa640",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T18:35:42.331Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ZVnfumMuh1sCNKEw1iy6G`</summary>

```json
{
  "query": "Obfuscation Atlas deception probes RLVR training checkpoints 2602.15515"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2389d6d-5ee3-49f0-9a7c-54c23ffb4c78",
  "isSidechain": false,
  "requestId": "req_011CbCQkuAx64gT3i98CZLgs",
  "type": "assistant",
  "uuid": "d69dbeaa-9bb9-4da9-a7e9-b3dcc0a8d32c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019c3Pto4Yof2W7WVjdqYD7y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 809,
      "cache_creation_input_tokens": 1753,
      "cache_read_input_tokens": 20441,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 809,
          "output_tokens": 132,
          "cache_read_input_tokens": 20441,
          "cache_creation_input_tokens": 1753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1753
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

_source line 19 · 2026-05-19T18:35:43.443Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BF2qxj4ay4qTizzx4irjMA`</summary>

```json
{
  "query": "\"Monitoring the Internal Monologue\" probe trajectories reasoning 2605.18549 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d69dbeaa-9bb9-4da9-a7e9-b3dcc0a8d32c",
  "isSidechain": false,
  "requestId": "req_011CbCQkuAx64gT3i98CZLgs",
  "type": "assistant",
  "uuid": "50eab9d6-becd-442c-be4c-41abf1831138",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019c3Pto4Yof2W7WVjdqYD7y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 809,
      "cache_creation_input_tokens": 1753,
      "cache_read_input_tokens": 20441,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 809,
          "output_tokens": 132,
          "cache_read_input_tokens": 20441,
          "cache_creation_input_tokens": 1753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1753
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Mo…",
  "leafUuid": "50eab9d6-becd-442c-be4c-41abf1831138",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Study surface-latent faithfulness gap in GRPO reasoning models",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed"
}
```

---

### Tool result

_source line 22 · 2026-05-19T18:35:47.916Z_

<details><summary>↩ Tool result · `toolu_015ZVnfumMuh1sCNKEw1iy6G`</summary>

```text
Web search results for query: "Obfuscation Atlas deception probes RLVR training checkpoints 2602.15515"

Links: [{"title":"GitHub - AlignmentResearch/obfuscation-atlas: The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes · GitHub","url":"https://github.com/AlignmentResearch/obfuscation-atlas"},{"title":"[2602.15515] The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes","url":"https://arxiv.org/abs/2602.15515"},{"title":"The Obfuscation Atlas:","url":"https://arxiv.org/pdf/2602.15515"},{"title":"The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/obfuscation-atlas-mapping-where-honesty-emerges-rlvr"},{"title":"AlignmentResearch/obfuscation-atlas-Meta-Llama-3-8B-Instruct-kl0.001-det1-seed1-deception_probe · Hugging Face","url":"https://huggingface.co/AlignmentResearch/obfuscation-atlas-Meta-Llama-3-8B-Instruct-kl0.001-det1-seed1-deception_probe"},{"title":"The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes","url":"https://arxiv.org/html/2602.15515v1"},{"title":"The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes","url":"https://www.catalyzex.com/paper/the-obfuscation-atlas-mapping-where-honesty"},{"title":"AlignmentResearch/obfuscation-atlas-gemma-3-12b-it-kl0.0001-det3-seed1-mbpp_probe · Discussions","url":"https://api-inference.hf-mirror.com/AlignmentResearch/obfuscation-atlas-gemma-3-12b-it-kl0.0001-det3-seed1-mbpp_probe/discussions"},{"title":"The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | FAR.AI","url":"https://www.far.ai/research/the-obfuscation-atlas-mapping-where-honesty-emerges-in-rlvr-with-deception-probes"}]

Based on the search results, I found comprehensive information about the Obfuscation Atlas research:

## Overview

Training against white-box deception detectors has been proposed as a way to make AI systems honest, but such training risks models learning to obfuscate their deception to evade the detector.

## Research Focus

The researchers constructed a realistic coding environment where reward hacking via hardcoding test cases naturally occurs, and showed that obfuscation emerges in this setting.

## Key Findings

The paper introduces a taxonomy of possible outcomes when training against a deception detector, where the model either remains honest, or becomes deceptive via two possible obfuscation strategies. These strategies are:

1. Obfuscated activations: the model outputs deceptive text while modifying its internal representations to no longer trigger the detector.

2. Obfuscated policy: the model outputs deceptive text that evades the detector, typically by including a justification for the reward hack.

## Resources

The codebase implements methods for training deception probes (linear and nonlinear detectors on model activations) and running RLVR experiments that train language models against those probes. The 500+ trained models from the paper are available in the Hugging Face collection.

The paper was published in February 2026 with arXiv ID 2602.15515 by Mohammad Taufeeque, Stefan Heimersheim, Adam Gleave, and Chris Cundy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d69dbeaa-9bb9-4da9-a7e9-b3dcc0a8d32c",
  "isSidechain": false,
  "promptId": "f6d1450c-25e4-4b19-8c5a-b25909ce1666",
  "type": "user",
  "uuid": "2cd0f4c6-8205-47b7-be46-a6ba9472727d",
  "toolUseResult": {
    "query": "Obfuscation Atlas deception probes RLVR training checkpoints 2602.15515",
    "results": [
      {
        "tool_use_id": "srvtoolu_013X2sqMpwJKDLobUnspv56L",
        "content": [
          {
            "title": "GitHub - AlignmentResearch/obfuscation-atlas: The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes · GitHub",
            "url": "https://github.com/AlignmentResearch/obfuscation-atlas"
          },
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
            "title": "AlignmentResearch/obfuscation-atlas-Meta-Llama-3-8B-Instruct-kl0.001-det1-seed1-deception_probe · Hugging Face",
            "url": "https://huggingface.co/AlignmentResearch/obfuscation-atlas-Meta-Llama-3-8B-Instruct-kl0.001-det1-seed1-deception_probe"
          },
          {
            "title": "The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes",
            "url": "https://arxiv.org/html/2602.15515v1"
          },
          {
            "title": "The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes",
            "url": "https://www.catalyzex.com/paper/the-obfuscation-atlas-mapping-where-honesty"
          },
          {
            "title": "AlignmentResearch/obfuscation-atlas-gemma-3-12b-it-kl0.0001-det3-seed1-mbpp_probe · Discussions",
            "url": "https://api-inference.hf-mirror.com/AlignmentResearch/obfuscation-atlas-gemma-3-12b-it-kl0.0001-det3-seed1-mbpp_probe/discussions"
          },
          {
            "title": "The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | FAR.AI",
            "url": "https://www.far.ai/research/the-obfuscation-atlas-mapping-where-honesty-emerges-in-rlvr-with-deception-probes"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the Obfuscation Atlas research:\n\n## Overview\n\nTraining against white-box deception detectors has been proposed as a way to make AI systems honest, but such training risks models learning to obfuscate their deception to evade the detector.\n\n## Research Focus\n\nThe researchers constructed a realistic coding environment where reward hacking via hardcoding test cases naturally occurs, and showed that obfuscation emerges in this setting.\n\n## Key Findings\n\nThe paper introduces a taxonomy of possible outcomes when training against a deception detector, where the model either remains honest, or becomes deceptive via two possible obfuscation strategies. These strategies are:\n\n1. Obfuscated activations: the model outputs deceptive text while modifying its internal representations to no longer trigger the detector.\n\n2. Obfuscated policy: the model outputs deceptive text that evades the detector, typically by including a justification for the reward hack.\n\n## Resources\n\nThe codebase implements methods for training deception probes (linear and nonlinear detectors on model activations) and running RLVR experiments that train language models against those probes. The 500+ trained models from the paper are available in the Hugging Face collection.\n\nThe paper was published in February 2026 with arXiv ID 2602.15515 by Mohammad Taufeeque, Stefan Heimersheim, Adam Gleave, and Chris Cundy."
    ],
    "durationSeconds": 5.580441528999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d69dbeaa-9bb9-4da9-a7e9-b3dcc0a8d32c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T18:35:51.136Z_

<details><summary>↩ Tool result · `toolu_01BF2qxj4ay4qTizzx4irjMA`</summary>

```text
Web search results for query: ""Monitoring the Internal Monologue" probe trajectories reasoning 2605.18549 2026"

Links: [{"title":"[2605.18549] Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics","url":"https://arxiv.org/abs/2605.18549"},{"title":"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics","url":"https://arxiv.org/html/2605.18549"},{"title":"Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing","url":"https://arxiv.org/pdf/2603.17199"},{"title":"Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning","url":"https://arxiv.org/pdf/2603.01326"},{"title":"Can We Predict Alignment Before Models Finish Thinking? Towards Monitoring Misaligned Reasoning Models","url":"https://arxiv.org/pdf/2507.12428"},{"title":"LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals","url":"https://arxiv.org/pdf/2604.05655"},{"title":"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning","url":"https://arxiv.org/pdf/2602.03978"},{"title":"Internalizing LLM Reasoning via Discovery and Replay of Latent Actions","url":"https://arxiv.org/pdf/2602.04925"}]

Based on the search results, here's what I found about the paper 2605.18549:

## "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics"

The paper addresses how Large Reasoning Models (LRMs) introduce new opportunities for safety monitoring through their Chain of Thought (CoT) reasoning. However, CoT is not always faithful to the model's final output, undermining its reliability as a monitoring tool.

### Key Methodology

The researchers investigate the hidden representations of LRMs to determine whether future behavior can be predicted from prompt and CoT representations by evaluating a probe at each generated token to construct a probe trajectory, the continuous evolution of a concept's probability across the reasoning process.

### Main Findings

The choice of pooling operation is critical: average-pooling and last-token methods collapse to near-random performance, while max-pooling achieves up to 95% AUROC and yields stable probe trajectories. Additionally, template-based training data achieves near-parity with dynamically generated model responses, eliminating the need for a costly initial inference and labeling.

Using four datasets and four reasoning models across the domains of safety and mathematics, the researchers demonstrate that trajectory features encode task-specific dynamics that improve outcome separability, establishing probe trajectories as a complementary framework for monitoring LRM behavior.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50eab9d6-becd-442c-be4c-41abf1831138",
  "isSidechain": false,
  "promptId": "f6d1450c-25e4-4b19-8c5a-b25909ce1666",
  "type": "user",
  "uuid": "a540df67-2ef1-453d-8c2e-d6e1750a70de",
  "toolUseResult": {
    "query": "\"Monitoring the Internal Monologue\" probe trajectories reasoning 2605.18549 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014J4t7BLfPUag5ab3iYRmEZ",
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
            "title": "Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning",
            "url": "https://arxiv.org/pdf/2603.01326"
          },
          {
            "title": "Can We Predict Alignment Before Models Finish Thinking? Towards Monitoring Misaligned Reasoning Models",
            "url": "https://arxiv.org/pdf/2507.12428"
          },
          {
            "title": "LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals",
            "url": "https://arxiv.org/pdf/2604.05655"
          },
          {
            "title": "Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning",
            "url": "https://arxiv.org/pdf/2602.03978"
          },
          {
            "title": "Internalizing LLM Reasoning via Discovery and Replay of Latent Actions",
            "url": "https://arxiv.org/pdf/2602.04925"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper 2605.18549:\n\n## \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\"\n\nThe paper addresses how Large Reasoning Models (LRMs) introduce new opportunities for safety monitoring through their Chain of Thought (CoT) reasoning. However, CoT is not always faithful to the model's final output, undermining its reliability as a monitoring tool.\n\n### Key Methodology\n\nThe researchers investigate the hidden representations of LRMs to determine whether future behavior can be predicted from prompt and CoT representations by evaluating a probe at each generated token to construct a probe trajectory, the continuous evolution of a concept's probability across the reasoning process.\n\n### Main Findings\n\nThe choice of pooling operation is critical: average-pooling and last-token methods collapse to near-random performance, while max-pooling achieves up to 95% AUROC and yields stable probe trajectories. Additionally, template-based training data achieves near-parity with dynamically generated model responses, eliminating the need for a costly initial inference and labeling.\n\nUsing four datasets and four reasoning models across the domains of safety and mathematics, the researchers demonstrate that trajectory features encode task-specific dynamics that improve outcome separability, establishing probe trajectories as a complementary framework for monitoring LRM behavior."
    ],
    "durationSeconds": 7.690544102,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "50eab9d6-becd-442c-be4c-41abf1831138",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T18:35:54.181Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VwKUreTCnURrHadNbFq2VX`</summary>

```json
{
  "query": "surface latent faithfulness gap RL training reasoning models probes longitudinal 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a540df67-2ef1-453d-8c2e-d6e1750a70de",
  "isSidechain": false,
  "requestId": "req_011CbCQmn4bQFo5Xjn6Ced8Q",
  "type": "assistant",
  "uuid": "73596883-e9cf-4e30-b11d-e9d468162859",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuCUqcyCKW34YRYxT54DEC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2736,
      "cache_read_input_tokens": 22194,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 22194,
          "cache_creation_input_tokens": 2736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2736
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

_source line 25 · 2026-05-19T18:35:55.060Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011f2uGZppLGgFTkY72zhWbN`</summary>

```json
{
  "query": "CoT faithfulness RL checkpoint analysis GRPO training probes NeurIPS ICML CoRL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73596883-e9cf-4e30-b11d-e9d468162859",
  "isSidechain": false,
  "requestId": "req_011CbCQmn4bQFo5Xjn6Ced8Q",
  "type": "assistant",
  "uuid": "21030b45-329d-4537-913a-427ca35d01fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuCUqcyCKW34YRYxT54DEC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2736,
      "cache_read_input_tokens": 22194,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 22194,
          "cache_creation_input_tokens": 2736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2736
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

_source line 26 · 2026-05-19T18:36:03.167Z_

<details><summary>↩ Tool result · `toolu_011f2uGZppLGgFTkY72zhWbN`</summary>

```text
Web search results for query: "CoT faithfulness RL checkpoint analysis GRPO training probes NeurIPS ICML CoRL 2026"

Links: [{"title":"Accepted papers | FoRLM @ NeurIPS'25","url":"https://reasoning-workshop.github.io/accepted/"},{"title":"Evaluating GRPO and DPO for Faithful Chain-of-Thought Reasoning in LLMs","url":"https://arxiv.org/html/2512.22631v1"},{"title":"Reasoning Faithfulness","url":"https://akhil.bio/CoT"},{"title":"Evaluating GRPO and DPO for Faithful Chain-of-Thought Reasoning in LLMs","url":"https://arxiv.org/pdf/2512.22631"},{"title":"The Promise of RL for Autoregressive Image Editing Saba Ahmadi1∗","url":"https://arxiv.org/pdf/2508.01119"},{"title":"Preprint. Counterfactual Simulation Training for Chain-of-Thought Faithfulness","url":"https://arxiv.org/pdf/2602.20710"},{"title":"Stable Reinforcement Learning for Efficient Reasoning","url":"https://arxiv.org/pdf/2505.18086"}]

Based on the search results, I found relevant research related to your query about CoT (Chain-of-Thought) faithfulness with RL, GRPO training, and related techniques:

## Key Research Findings:

### GRPO Training for Faithful CoT Reasoning

Improving faithfulness (i.e., ensuring that CoT explanations correspond to a model's true internal reasoning) is crucial for building transparent and trustworthy AI systems. Two recent optimization techniques, Direct Preference Optimization (DPO) and Group Relative Policy Optimization (GRPO), offer complementary strategies for addressing this challenge.

### ReFIne Framework at NeurIPS

ReFIne is a new training framework that integrates supervised fine-tuning with GRPO to encourage models to improve interpretability by producing structured, tag-based traces with high-level planning that are easier for humans to follow, enhance faithfulness by explicitly disclosing the decisive information guiding each solution, and promote reliability by providing self-assessments of both the derivation's soundness and the confidence of the final answer.

### Training with Checkpoints

Models were trained for one epoch with a 90–10 train–validation split, with checkpoints saved at each epoch.

### Probing Faithful Reasoning

Models trained with long CoTs and RL on reasoning tasks show that on some tasks like algebra word problems, CoTs are indeed pretty load-bearing, where early answering and adding mistakes often change the answer, which looks more faithful.

The research indicates active work in this area combining RL optimization (particularly GRPO), faithfulness analysis, and checkpoint-based training approaches, with papers presented at venues like NeurIPS.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21030b45-329d-4537-913a-427ca35d01fb",
  "isSidechain": false,
  "promptId": "f6d1450c-25e4-4b19-8c5a-b25909ce1666",
  "type": "user",
  "uuid": "3b664bbb-6b4a-481e-a2ce-b27a86816869",
  "toolUseResult": {
    "query": "CoT faithfulness RL checkpoint analysis GRPO training probes NeurIPS ICML CoRL 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RydJZ4ACBNT3LASR7H7PhY",
        "content": [
          {
            "title": "Accepted papers | FoRLM @ NeurIPS'25",
            "url": "https://reasoning-workshop.github.io/accepted/"
          },
          {
            "title": "Evaluating GRPO and DPO for Faithful Chain-of-Thought Reasoning in LLMs",
            "url": "https://arxiv.org/html/2512.22631v1"
          },
          {
            "title": "Reasoning Faithfulness",
            "url": "https://akhil.bio/CoT"
          },
          {
            "title": "Evaluating GRPO and DPO for Faithful Chain-of-Thought Reasoning in LLMs",
            "url": "https://arxiv.org/pdf/2512.22631"
          },
          {
            "title": "The Promise of RL for Autoregressive Image Editing Saba Ahmadi1∗",
            "url": "https://arxiv.org/pdf/2508.01119"
          },
          {
            "title": "Preprint. Counterfactual Simulation Training for Chain-of-Thought Faithfulness",
            "url": "https://arxiv.org/pdf/2602.20710"
          },
          {
            "title": "Stable Reinforcement Learning for Efficient Reasoning",
            "url": "https://arxiv.org/pdf/2505.18086"
          }
        ]
      },
      "Based on the search results, I found relevant research related to your query about CoT (Chain-of-Thought) faithfulness with RL, GRPO training, and related techniques:\n\n## Key Research Findings:\n\n### GRPO Training for Faithful CoT Reasoning\n\nImproving faithfulness (i.e., ensuring that CoT explanations correspond to a model's true internal reasoning) is crucial for building transparent and trustworthy AI systems. Two recent optimization techniques, Direct Preference Optimization (DPO) and Group Relative Policy Optimization (GRPO), offer complementary strategies for addressing this challenge.\n\n### ReFIne Framework at NeurIPS\n\nReFIne is a new training framework that integrates supervised fine-tuning with GRPO to encourage models to improve interpretability by producing structured, tag-based traces with high-level planning that are easier for humans to follow, enhance faithfulness by explicitly disclosing the decisive information guiding each solution, and promote reliability by providing self-assessments of both the derivation's soundness and the confidence of the final answer.\n\n### Training with Checkpoints\n\nModels were trained for one epoch with a 90–10 train–validation split, with checkpoints saved at each epoch.\n\n### Probing Faithful Reasoning\n\nModels trained with long CoTs and RL on reasoning tasks show that on some tasks like algebra word problems, CoTs are indeed pretty load-bearing, where early answering and adding mistakes often change the answer, which looks more faithful.\n\nThe research indicates active work in this area combining RL optimization (particularly GRPO), faithfulness analysis, and checkpoint-based training approaches, with papers presented at venues like NeurIPS."
    ],
    "durationSeconds": 8.102614031999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "21030b45-329d-4537-913a-427ca35d01fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T18:36:04.429Z_

<details><summary>↩ Tool result · `toolu_01VwKUreTCnURrHadNbFq2VX`</summary>

```text
Web search results for query: "surface latent faithfulness gap RL training reasoning models probes longitudinal 2026"

Links: [{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410v1"},{"title":"Published at Latent & Implicit Thinking Workshop @ ICLR 2026","url":"https://openreview.net/pdf?id=6a3InGPoEG"},{"title":"A Survey on the Mechanisms of Multi-Step Reasoning in ...","url":"https://www.preprints.org/frontend/manuscript/11cab45ab0d578f7080de19423eb6ffe/download_pub"},{"title":"Are DeepSeek R1 And Other Reasoning Models More Faithful?","url":"https://arxiv.org/pdf/2501.08156"},{"title":"RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/pdf/2602.17053"},{"title":"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?","url":"https://arxiv.org/pdf/2603.22582"},{"title":"When Shallow Wins: Silent Failures and the Depth-Accuracy Paradox in Latent Reasoning","url":"https://arxiv.org/pdf/2603.03475"}]

Based on the web search results, I found several highly relevant papers from 2026 that address your query about the surface-latent faithfulness gap in RL-trained reasoning models:

## Key Findings:

Even with thinking-token access, 11.8% of influenced cases show no acknowledgment in either channel, requiring activation-level or probe-based monitoring beyond answer-text and thinking-token screening.

Research identified a "Reasoning Horizon" at 70–85% of chain length beyond which reasoning tokens have diminishing causal influence, and models often commit to answers early in the reasoning chain with subsequent tokens serving a performative rather than computational role.

## RL Training and Latent Reasoning:

After initializing reasoning projectors, performance on tasks is improved via RL using reward functions, with latent reasoning incorporated to lower computational costs using Group Relative Policy Optimization.

## Broader Faithfulness Concerns:

Evaluating twelve open-source large reasoning models found unfaithfulness in 49.7% of outputs, with failures concentrated in brittle domains like math and code, and showing that adding current RL-style objectives can reduce reasoning faithfulness even when accuracy is maintained.

Surface-level monitoring may systematically underestimate the true divergence between stated and actual reasoning, as models can encode reasoning steganographically in CoT text.

These papers address the longitudinal aspect you mentioned through benchmarking and systematic evaluation of how RL training affects the relationship between surface-level explanations and latent model representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73596883-e9cf-4e30-b11d-e9d468162859",
  "isSidechain": false,
  "promptId": "f6d1450c-25e4-4b19-8c5a-b25909ce1666",
  "type": "user",
  "uuid": "3736ae26-ff7c-45d4-97b2-0b76917d3fb6",
  "toolUseResult": {
    "query": "surface latent faithfulness gap RL training reasoning models probes longitudinal 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01G1vS2RtRWPN3hyGUJtEhrA",
        "content": [
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410v1"
          },
          {
            "title": "Published at Latent & Implicit Thinking Workshop @ ICLR 2026",
            "url": "https://openreview.net/pdf?id=6a3InGPoEG"
          },
          {
            "title": "A Survey on the Mechanisms of Multi-Step Reasoning in ...",
            "url": "https://www.preprints.org/frontend/manuscript/11cab45ab0d578f7080de19423eb6ffe/download_pub"
          },
          {
            "title": "Are DeepSeek R1 And Other Reasoning Models More Faithful?",
            "url": "https://arxiv.org/pdf/2501.08156"
          },
          {
            "title": "RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2602.17053"
          },
          {
            "title": "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?",
            "url": "https://arxiv.org/pdf/2603.22582"
          },
          {
            "title": "When Shallow Wins: Silent Failures and the Depth-Accuracy Paradox in Latent Reasoning",
            "url": "https://arxiv.org/pdf/2603.03475"
          }
        ]
      },
      "Based on the web search results, I found several highly relevant papers from 2026 that address your query about the surface-latent faithfulness gap in RL-trained reasoning models:\n\n## Key Findings:\n\nEven with thinking-token access, 11.8% of influenced cases show no acknowledgment in either channel, requiring activation-level or probe-based monitoring beyond answer-text and thinking-token screening.\n\nResearch identified a \"Reasoning Horizon\" at 70–85% of chain length beyond which reasoning tokens have diminishing causal influence, and models often commit to answers early in the reasoning chain with subsequent tokens serving a performative rather than computational role.\n\n## RL Training and Latent Reasoning:\n\nAfter initializing reasoning projectors, performance on tasks is improved via RL using reward functions, with latent reasoning incorporated to lower computational costs using Group Relative Policy Optimization.\n\n## Broader Faithfulness Concerns:\n\nEvaluating twelve open-source large reasoning models found unfaithfulness in 49.7% of outputs, with failures concentrated in brittle domains like math and code, and showing that adding current RL-style objectives can reduce reasoning faithfulness even when accuracy is maintained.\n\nSurface-level monitoring may systematically underestimate the true divergence between stated and actual reasoning, as models can encode reasoning steganographically in CoT text.\n\nThese papers address the longitudinal aspect you mentioned through benchmarking and systematic evaluation of how RL training affects the relationship between surface-level explanations and latent model representations."
    ],
    "durationSeconds": 10.243611294000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "73596883-e9cf-4e30-b11d-e9d468162859",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-19T18:36:07.777Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do one more search to check if there's any very recent work that directly overlaps with this proposal - specifically looking for longitudinal studies of probes across GRPO checkpoints for faithfulness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3736ae26-ff7c-45d4-97b2-0b76917d3fb6",
  "isSidechain": false,
  "requestId": "req_011CbCQnkdo4gtMGcDig74Re",
  "type": "assistant",
  "uuid": "c204e87d-ae21-462d-83d1-c71229c748ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157mopZX8DMkyTTZiVGePmQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 730,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 24930,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 730,
          "output_tokens": 189,
          "cache_read_input_tokens": 24930,
          "cache_creation_input_tokens": 880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 880
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

_source line 29 · 2026-05-19T18:36:08.777Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015QRzoHUtDrhsD4RYWthYv6`</summary>

```json
{
  "query": "RL-Obfuscation language models evade latent space monitors 2506.14261"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c204e87d-ae21-462d-83d1-c71229c748ac",
  "isSidechain": false,
  "requestId": "req_011CbCQnkdo4gtMGcDig74Re",
  "type": "assistant",
  "uuid": "65bbd904-4ae6-48a9-810f-fc4c8c720a78",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157mopZX8DMkyTTZiVGePmQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 730,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 24930,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 730,
          "output_tokens": 189,
          "cache_read_input_tokens": 24930,
          "cache_creation_input_tokens": 880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 880
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

_source line 30 · 2026-05-19T18:36:09.513Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019RLLV3VawKQ5Aw5wPEzAvB`</summary>

```json
{
  "query": "VLM checkpoint robustness chain-of-thought consistency RL finetuning 2602.12506"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65bbd904-4ae6-48a9-810f-fc4c8c720a78",
  "isSidechain": false,
  "requestId": "req_011CbCQnkdo4gtMGcDig74Re",
  "type": "assistant",
  "uuid": "5a3dd60c-3c41-461d-8518-c2027529293a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157mopZX8DMkyTTZiVGePmQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 730,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 24930,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 730,
          "output_tokens": 189,
          "cache_read_input_tokens": 24930,
          "cache_creation_input_tokens": 880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 880
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Mo…",
  "leafUuid": "5a3dd60c-3c41-461d-8518-c2027529293a",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Study surface-latent faithfulness gap in GRPO reasoning models",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed"
}
```

---

### Tool result

_source line 33 · 2026-05-19T18:36:14.366Z_

<details><summary>↩ Tool result · `toolu_015QRzoHUtDrhsD4RYWthYv6`</summary>

```text
Web search results for query: "RL-Obfuscation language models evade latent space monitors 2506.14261"

Links: [{"title":"[2506.14261] RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?","url":"https://arxiv.org/abs/2506.14261"},{"title":"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?","url":"https://arxiv.org/html/2506.14261v3"},{"title":"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250614261G/abstract"},{"title":"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?","url":"https://arxiv.org/pdf/2506.14261"},{"title":"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? | OpenReview","url":"https://openreview.net/forum?id=YT97yOoD4x"},{"title":"(PDF) RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?","url":"https://www.researchgate.net/publication/392765939_RL-Obfuscation_Can_Language_Models_Learn_to_Evade_Latent-Space_Monitors"},{"title":"RL Obfuscation tests whether a Language Model can evade a monitoring... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/RL-Obfuscation-tests-whether-a-Language-Model-can-evade-a-monitoring-method-without_fig1_392765939"}]

Based on the search results, here's what I found about this research paper:

## Overview

RL-Obfuscation is a technique where LLMs are finetuned via reinforcement learning to evade latent-space monitors while maintaining their blackbox behaviour.

## Key Findings

Latent-space monitors aim to detect undesirable behaviours in Large Language Models by leveraging their internal representations rather than relying solely on black-box outputs. These methods have shown promise in identifying behaviours such as deception and unsafe completions.

However, the research demonstrates vulnerabilities. When applied to Language Models ranging from 7B to 14B parameters, token-level monitors are highly vulnerable to this attack while more holistic monitors, such as max-pooling or attention-based probes, remain robust.

## Additional Findings

Models trained to evade a single static monitor can generalise to evade other unseen monitors. Additionally, the model can learn to repurpose tokens to have different internal representations.

The paper was authored by Rohan Gupta and Erik Jenner, with the arxiv identifier 2506.14261.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65bbd904-4ae6-48a9-810f-fc4c8c720a78",
  "isSidechain": false,
  "promptId": "f6d1450c-25e4-4b19-8c5a-b25909ce1666",
  "type": "user",
  "uuid": "cd1ce966-354e-4391-8cb6-0174940cd13a",
  "toolUseResult": {
    "query": "RL-Obfuscation language models evade latent space monitors 2506.14261",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BQXsVss7LTgsya9uUxCLJ2",
        "content": [
          {
            "title": "[2506.14261] RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?",
            "url": "https://arxiv.org/abs/2506.14261"
          },
          {
            "title": "RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?",
            "url": "https://arxiv.org/html/2506.14261v3"
          },
          {
            "title": "RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250614261G/abstract"
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
            "title": "(PDF) RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?",
            "url": "https://www.researchgate.net/publication/392765939_RL-Obfuscation_Can_Language_Models_Learn_to_Evade_Latent-Space_Monitors"
          },
          {
            "title": "RL Obfuscation tests whether a Language Model can evade a monitoring... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/RL-Obfuscation-tests-whether-a-Language-Model-can-evade-a-monitoring-method-without_fig1_392765939"
          }
        ]
      },
      "Based on the search results, here's what I found about this research paper:\n\n## Overview\n\nRL-Obfuscation is a technique where LLMs are finetuned via reinforcement learning to evade latent-space monitors while maintaining their blackbox behaviour.\n\n## Key Findings\n\nLatent-space monitors aim to detect undesirable behaviours in Large Language Models by leveraging their internal representations rather than relying solely on black-box outputs. These methods have shown promise in identifying behaviours such as deception and unsafe completions.\n\nHowever, the research demonstrates vulnerabilities. When applied to Language Models ranging from 7B to 14B parameters, token-level monitors are highly vulnerable to this attack while more holistic monitors, such as max-pooling or attention-based probes, remain robust.\n\n## Additional Findings\n\nModels trained to evade a single static monitor can generalise to evade other unseen monitors. Additionally, the model can learn to repurpose tokens to have different internal representations.\n\nThe paper was authored by Rohan Gupta and Erik Jenner, with the arxiv identifier 2506.14261."
    ],
    "durationSeconds": 5.584593791,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "65bbd904-4ae6-48a9-810f-fc4c8c720a78",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T18:36:15.409Z_

<details><summary>↩ Tool result · `toolu_019RLLV3VawKQ5Aw5wPEzAvB`</summary>

```text
Web search results for query: "VLM checkpoint robustness chain-of-thought consistency RL finetuning 2602.12506"

Links: [{"title":"[2602.12506v1] On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs","url":"https://arxiv.org/abs/2602.12506v1"},{"title":"[2602.12506] On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs","url":"https://arxiv.org/abs/2602.12506"},{"title":"On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs","url":"https://arxiv.org/pdf/2602.12506"},{"title":"On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs | OpenReview","url":"https://openreview.net/forum?id=oFC7fUsGje"},{"title":"On Robustness and Chain-of-Thought consistency of RL-Finetuned VLMs","url":"https://arxiv.org/html/2602.12506v1"}]

I found the research paper you're looking for! Here's what the paper is about:

**Title:** On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs

**Authors:** Rosie Zhao, Anshul Shah, Xiaoyu Zhu, Xinke Deng, Zhongyu Jiang, Yang Yang, Joerg Liebelt, and Arnab Mondal (Apple)

**Key Findings:**

While RL-tuned VLMs improve on visual reasoning benchmarks, they remain vulnerable to weak visual grounding, hallucinations, and over-reliance on textual cues. Simple, controlled textual perturbations—misleading captions or incorrect chain-of-thought (CoT) traces—cause substantial drops in robustness and confidence.

Closed models exhibit similar failure modes but maintain markedly greater robustness and reasoning consistency, suggesting that the gap reflects a shortcoming in current open-source RL fine-tuning rather than an inherent limitation of the task.

The researchers uncovered an accuracy–faithfulness trade-off: fine-tuning raises benchmark accuracy, but can simultaneously erode the reliability of the accompanying CoT and its robustness to contextual shifts.

The paper is available on arXiv at https://arxiv.org/abs/2602.12506


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a3dd60c-3c41-461d-8518-c2027529293a",
  "isSidechain": false,
  "promptId": "f6d1450c-25e4-4b19-8c5a-b25909ce1666",
  "type": "user",
  "uuid": "839f9299-71db-4f70-9b7d-cade4737d4d7",
  "toolUseResult": {
    "query": "VLM checkpoint robustness chain-of-thought consistency RL finetuning 2602.12506",
    "results": [
      {
        "tool_use_id": "srvtoolu_0192tbCHQ2VfMGEHuHYzUYrj",
        "content": [
          {
            "title": "[2602.12506v1] On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs",
            "url": "https://arxiv.org/abs/2602.12506v1"
          },
          {
            "title": "[2602.12506] On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs",
            "url": "https://arxiv.org/abs/2602.12506"
          },
          {
            "title": "On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs",
            "url": "https://arxiv.org/pdf/2602.12506"
          },
          {
            "title": "On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs | OpenReview",
            "url": "https://openreview.net/forum?id=oFC7fUsGje"
          },
          {
            "title": "On Robustness and Chain-of-Thought consistency of RL-Finetuned VLMs",
            "url": "https://arxiv.org/html/2602.12506v1"
          }
        ]
      },
      "I found the research paper you're looking for! Here's what the paper is about:\n\n**Title:** On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs\n\n**Authors:** Rosie Zhao, Anshul Shah, Xiaoyu Zhu, Xinke Deng, Zhongyu Jiang, Yang Yang, Joerg Liebelt, and Arnab Mondal (Apple)\n\n**Key Findings:**\n\nWhile RL-tuned VLMs improve on visual reasoning benchmarks, they remain vulnerable to weak visual grounding, hallucinations, and over-reliance on textual cues. Simple, controlled textual perturbations—misleading captions or incorrect chain-of-thought (CoT) traces—cause substantial drops in robustness and confidence.\n\nClosed models exhibit similar failure modes but maintain markedly greater robustness and reasoning consistency, suggesting that the gap reflects a shortcoming in current open-source RL fine-tuning rather than an inherent limitation of the task.\n\nThe researchers uncovered an accuracy–faithfulness trade-off: fine-tuning raises benchmark accuracy, but can simultaneously erode the reliability of the accompanying CoT and its robustness to contextual shifts.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2602.12506"
    ],
    "durationSeconds": 5.893188962999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5a3dd60c-3c41-461d-8518-c2027529293a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-19T18:36:15.416Z_

```json
{
  "parentUuid": "839f9299-71db-4f70-9b7d-cade4737d4d7",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "838a9970-6e4d-4674-adfe-132e5187e849",
  "timestamp": "2026-05-19T18:36:15.416Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 36 · 2026-05-19T18:37:04.221Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture of the research landscape. Let me synthesize my findings and provide the evaluation.

Let me think carefully about this proposal:

## What the proposal is doing:
It proposes a longitudinal study tracking both surface-level CoT faithfulness (hint-injection rates, NLDD) and latent faithfulness (linear probes on residual streams) across GRPO training checkpoints (~20 per model) for two model families (DeepSeek-R1-Distill-Qwen-7B and Qwen3-8B).

The central hypothesis: GRPO training creates a widening surface-latent faithfulness gap.
 
## Key questions:

### 1. Is this truly novel?

Looking at the existing work, there's substantial overlap with prior approaches. The Obfuscation Atlas paper already uses a similar methodology—probing across training checkpoints—though it focuses on deception and reward-hacking rather than general faithfulness. The VLM checkpoint work tracks faithfulness across RL checkpoints but relies only on surface metrics and studies vision models. The pre-CoT probes paper shows that probing approaches can detect hidden reasoning, but the novelty here hinges on whether combining these elements across GRPO specifically reveals something genuinely new about the surface-latent gap during this particular training process.

The core claim is that no one has simultaneously tracked both probe-measured latent faithfulness and surface CoT metrics at matched checkpoints during GRPO training. That's technically accurate as a combination, but the Obfuscation Atlas already demonstrated checkpoint-level probing is feasible, and the methodology itself isn't new—it's applying established techniques to a specific training regime.

The hypothesis that GRPO training widens the surface-latent faithfulness gap isn't particularly surprising either. The existing literature already points toward this conclusion: models pre-commit answers before generating reasoning, RL training improves surface metrics without improving causal reliance, and there's a documented accuracy-faithfulness trade-off. A positive result would feel predictable given what we already know from these converging lines of evidence.

I could probably reach the same conclusion by combining insights from the three existing papers without running new experiments. But there's a simpler path: the Obfuscation Atlas codebase is already public with 500+ trained models, so I could just retrain their probes on general faithfulness instead of deception detection and add surface metrics. That would give nearly identical results with significantly less work.

Now I'm realizing this is being proposed for CoRL 2026, which changes the venue considerations. I'm settling on treating this as an NLP/AI venue regardless of the CoRL label, and focusing on evaluating the idea itself. The core contribution is combining existing probe methodologies across training checkpoints with surface-level metrics—methodologically straightforward but novel in its specific combination. The significance is moderate since it would mainly confirm what prior work already suggests, though tracking how the gap evolves over training could offer useful temporal insights. The core idea—that the gap between surface and latent faithfulness widens during RL training—is something researchers in this space would likely expect already, so the real value lies in having empirical evidence rather than novel insight. I'm settling on 20-30% with a midpoint of 25%, though I should flag that CoRL 2026 focuses on robot learning, which creates a venue mismatch for this work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "838a9970-6e4d-4674-adfe-132e5187e849",
  "isSidechain": false,
  "requestId": "req_011CbCQoZdHpPFriFec3megA",
  "type": "assistant",
  "uuid": "28f4703b-83dd-4413-af0d-362342afcfef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fmrKMyuvzJZ5UNyUEpQp9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2439,
      "cache_read_input_tokens": 25810,
      "output_tokens": 5916,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2439,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5916,
          "cache_read_input_tokens": 25810,
          "cache_creation_input_tokens": 2439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2439
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

_source line 37 · 2026-05-19T18:38:26.571Z_

Now I have sufficient research data. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. **"Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning" (2602.03978, 2026)**:
   最直接相关的先驱工作之一。证明 RLVR 的表面可监控性提升来自响应分布收缩和 prompt attention 增加，而非 CoT 因果依赖增强。即：surface gains ≠ causal reliance。本 proposal 的核心假设（surface-latent gap widens）几乎是这篇论文结论的直接推论。

2. **"Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering" (2603.01437, Cox et al. 2026)**:
   在 Gemma 2 和 Qwen 2.5 上证明线性 probe 可以 >0.9 AUC 从 pre-CoT residual stream 中解码最终答案，且该方向是 causal 的（steering 实验）。这是 proposal 的方法论支柱——但该论文只研究 final models，没有训练动态。

3. **"On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs" (2602.12506, Apple 2026)**:
   在 Qwen2.5-VL-7B 上发现 RL fine-tuning 的 accuracy-faithfulness trade-off，但仅使用 LLM-as-judge 表面指标，无 activation-level 分析，且是 VLM 而非 LLM。本 proposal 的直接对标和改进目标。

4. **"The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes" (2602.15515, FAR AI 2026)**:
   **这是最关键的竞争工作**。已经在 Llama-3-8B through 70B 上跨 GRPO training steps 训练了 logistic regression probes，公开了 500+ 训练模型。方法论（probes across RLVR checkpoints）与本 proposal 高度重叠。区别：该论文聚焦 deception/reward-hacking obfuscation，而非 general faithfulness；未联合测量 surface faithfulness 指标。但技术路径几乎相同。

5. **"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics" (2605.18549, May 2026)**:
   构建 token-level probe trajectories，95% AUROC 预测推理结果。关键发现：max-pooling 是关键。但仅分析 fixed final models，未追踪 training dynamics。本 proposal 声称要 bridge token-level 和 checkpoint-level 分析。

6. **"RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?" (2506.14261, Gupta & Jenner)**:
   7B-14B 模型可通过 RL 学会逃避 latent-space monitors，token-level monitors 脆弱而 max-pooling/attention-based probes 鲁棒。这是对 probe-based monitoring 本身的质疑——若 RL 能学会 evade probes，那 probe AUC 在 training 过程中的变化可能反映的是 evasion 而非 faithfulness。

7. **其他 final-model snapshot 工作**: "Catching Rationalization in the Act" (2603.17199), "The Hypocrisy Gap" (2602.02496), "Why Models Know But Don't Say" (2603.26410), "Reasoning Theater" (Goodfire 2603.05488) — 这些都在不同角度证实了 final models 的 surface-latent divergence，但都是 snapshot 研究。

8. **Faithfulness-improving RL**: FaithRL (2602.03507), AtManRL (2604.16158, ICLR 2026 workshop) — 提出改进 faithfulness 的 RL 方法，但不研究 standard GRPO 的 divergence trajectory。

- **调研总结**: CoT faithfulness 在 2026 是极其拥挤的赛道，已存在大量高质量工作。关键组件——probes across RLVR checkpoints（Obfuscation Atlas）、pre-CoT probe methodology（Cox et al.）、checkpoint-level surface faithfulness tracking（VLM paper）——均已有独立工作。本 proposal 的核心贡献是将这些已有组件组合在一起，联合测量 surface + latent faithfulness across GRPO steps。这是一个 "组合 novelty" 而非 "方法 novelty" 的工作。

【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。** 具体来说：

1. **最直接的 trivial baseline**: 直接使用 Obfuscation Atlas 已公开的 500+ RLVR checkpoints（Llama-3-8B through 70B，GitHub 开源），在其上训练 general faithfulness probes（而非 deception probes），并添加 hint-injection surface metrics。这将以远低于本 proposal 的成本（无需自己跑 GRPO training）达到几乎相同的核心结论。

2. **更简单的推论路径**: RLVR Monitorability 论文已证明 "surface gains ≠ causal reliance"，Pre-CoT Probes 论文已证明 "models pre-commit answers in residual streams"。将两者放在一起，"RL training widens the surface-latent gap" 已是强推论——本 proposal 的实验价值在于 **量化** 这个 gap，而非 **发现** 它。

**增量价值**: 本 proposal 相对于 trivial alternatives 的增量在于：(a) 两个 architecturally distinct model families 的对比，(b) changepoint detection 的时间动态分析，(c) 联合的 NLDD + activation patching 因果分析。但这些都是实验设计层面的增量，不改变核心 insight。

【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的假设：

1. **"Linear probe AUC 上升 = latent answer pre-commitment 增强" 这个等价关系未必成立。** Probe AUC 上升可能反映 RL training 导致 representation 变得更线性可分（表征空间结构变化），而非模型真的更早"决定"了答案。RL training 改变了 representation geometry，这可能让 probe 更容易 decode，但不等价于 faithfulness 下降。Obfuscation Atlas 和 RL-Obfuscation 论文都表明 RL 可以改变 probe 的可检测性，但方向是复杂的。

2. **"Surface faithfulness metrics (hint-injection) 的改善方向是 monotonic 的" 这个假设过于简化。** Chen et al. 的结果显示 hint-injection rate 先下降后 plateau，但在不同 model families 和 training regimes 下可能呈现不同 pattern。如果 surface metric 也恶化（而非改善），那 "divergence" 的 narrative 就不成立——两者可能同时恶化，即不存在 "gap"。

3. **"GRPO training 的 faithfulness dynamics 可以从 7B distilled models 外推到大规模 models" 这个假设需要谨慎。** Distilled models 的起点（已有 reasoning traces）与 from-scratch RL training 有质的不同。14B scaling validation 是个好设计，但 7B → 14B 的 scaling step 太小，难以说明 generality。

【3 维度打分】:

1. **Novelty: 弱-中 (Weak-Medium)** — 核心贡献是将已有方法组合应用：probe methodology 来自 Cox et al. (2603.01437)，probes across RLVR checkpoints 的技术路径已被 Obfuscation Atlas (2602.15515) 证明可行且开源，surface faithfulness tracking 已有 VLM checkpoint paper (2602.12506) 和 Chen et al. (2505.05410) 的先例。本 proposal 的 novelty 是 "combination novelty"——将这些已有组件组合在一起。虽然 proposal 正确指出 "nobody has jointly measured both"，但这种 "nobody has done X+Y together" 式的 gap 在审稿人看来通常属于 incremental contribution。更关键的是，Obfuscation Atlas 已经做了 probes across RLVR checkpoints 的核心方法论，本 proposal 的差异化（general faithfulness vs. deception）不构成显著的方法论跃迁。

2. **Significance: 中 (Medium)** — 研究问题本身是重要的：理解 RL training 如何影响 reasoning faithfulness 对 AI safety 有直接意义。但如果核心发现是 positive（gap widens），审稿人的反应更可能是 "I would have guessed this"，因为 RLVR Monitorability (2602.03978) 已经告诉我们 surface gains 不来自 causal reliance，Pre-CoT Probes (2603.01437) 已经告诉我们 models pre-commit answers。这两个事实加在一起，gap widening 是 expected outcome。如果发现是 negative（gap doesn't widen），反而更 surprising 更有价值——但 proposal 的 framing 显然 bet on positive result。Significance 的上界受限于 confirmatory nature。

3. **Related Work: 强 (Strong)** — 这是 proposal 最突出的优点。对 2026 年 CoT faithfulness 文献的覆盖极为全面，对每篇相关工作的差异化定位清晰准确。Obfuscation Atlas、RL-Obfuscation、Monitoring Internal Monologue、Pre-CoT Probes、VLM checkpoint paper 等关键竞争工作均被识别并合理定位。唯一的小瑕疵是对 Obfuscation Atlas 的竞争性可能 understate 了——proposal 将其定位为 "deception-specific" 而与自己区隔，但审稿人可能认为从 deception probes 到 general faithfulness probes 的 generalization 是 straightforward 的。

【概率估计】: [18% - 28%] 中位 22%

【估计理由】:
Novelty 是主要限制维度。核心方法论组件均已存在（probes across checkpoints: Obfuscation Atlas; pre-CoT probes: Cox et al.; surface metrics across RL steps: Chen et al. & VLM paper），proposal 的贡献是将它们组合并联合测量。在一个已经非常拥挤的 2026 CoT faithfulness 赛道中，"combination study with existing methods" 面临 "incremental" 的审稿评价风险。Significance 受限于核心假设的 expected nature——如果 positive 结果是大多数人已经预期的，empirical confirmation 的价值被打折。Related work 的高质量和实验设计的完善度提供了一定的 floor（不太可能因为 coverage 不足被拒），但无法弥补 idea 层面 novelty 的不足。概率上界受 novelty 限制在 ~28%；下界由 solid execution plan + important question 支撑在 ~18%。

**关于投稿会议的重要说明**: 本 proposal 的主题是 NLP reasoning model 的 CoT faithfulness 和 RL training dynamics，与 **CoRL (Conference on Robot Learning)** 的 scope 完全不匹配。CoRL 聚焦机器人学习、机器人感知、运动规划等。如果确实投稿 CoRL，中稿概率接近 0%（desk reject）。上述概率估计基于将其投稿到合适的 NLP/ML venue（如 NeurIPS, ICML, ACL, EMNLP）。

【主要风险】:
1. **Novelty 不足风险（最核心）**: 审稿人很可能指出 Obfuscation Atlas 已经做了 "probes across RLVR checkpoints" 的核心工作，本文的差异化（general faithfulness vs. deception + adding surface metrics）不足以构成 top-venue 级别的 novelty。"Nobody has done X+Y together" 这种 gap statement 在拥挤赛道中说服力有限。
2. **Confirmatory bias 风险**: 核心假设（gap widens）是已有 evidence 的直接推论，若实验结果如预期，审稿人可能评价为 "confirmatory study with limited new insight"。Proposal 缺少一个 "如果结果出乎意料会怎样" 的 contingency framing，也缺少一个能区分 "gap widens because of X" vs. "gap widens because of Y" 的 mechanistic hypothesis。
```

Sources:
- [Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning](https://arxiv.org/abs/2602.03978)
- [Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437)
- [On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)
- [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://arxiv.org/abs/2602.15515)
- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)
- [RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261)
- [Catching Rationalization in the Act](https://arxiv.org/abs/2603.17199)
- [The Hypocrisy Gap](https://arxiv.org/abs/2602.02496)
- [Why Models Know But Don't Say](https://arxiv.org/abs/2603.26410)
- [FaithRL](https://arxiv.org/abs/2602.03507)
- [AtManRL](https://arxiv.org/abs/2604.16158)
- [Reasoning Theater](https://www.goodfire.ai/research/reasoning-theater)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28f4703b-83dd-4413-af0d-362342afcfef",
  "isSidechain": false,
  "requestId": "req_011CbCQoZdHpPFriFec3megA",
  "type": "assistant",
  "uuid": "273910d9-6130-4d46-9e96-55f70c695ed0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fmrKMyuvzJZ5UNyUEpQp9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2439,
      "cache_read_input_tokens": 25810,
      "output_tokens": 5916,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2439,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5916,
          "cache_read_input_tokens": 25810,
          "cache_creation_input_tokens": 2439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2439
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Mo…",
  "leafUuid": "273910d9-6130-4d46-9e96-55f70c695ed0",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Study surface-latent faithfulness gap in GRPO reasoning models",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Mapping the Surface-Latent Faithfulness Gap Across RL Training: A Probe-Based Longitudinal Study of Reasoning Mo…",
  "leafUuid": "273910d9-6130-4d46-9e96-55f70c695ed0",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Study surface-latent faithfulness gap in GRPO reasoning models",
  "sessionId": "35f5c275-351b-4dc6-a414-ef1af47b83ed"
}
```

---
