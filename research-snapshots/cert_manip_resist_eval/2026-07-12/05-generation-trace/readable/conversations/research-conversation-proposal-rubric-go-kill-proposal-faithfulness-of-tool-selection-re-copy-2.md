# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Faithfulness of Tool-Selection Re

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/c9225054-61e2-4260-93a8-43c36f992bce.jsonl`
- **Structured JSON:** [`134fcd2fb0de9b067b37.json`](../../sessions/13/134fcd2fb0de9b067b37.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:35:08.692Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:35:08.692Z",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn Probing\n\n## Description\nWe present the first systematic study of whether tool-selection reasoning in multi-turn agentic systems is causally faithful or post-hoc rationalization, combining behavioral causal interventions with multi-turn mechanistic probing. While recent work has established that tool identity is linearly readable from pre-generation activations in single-turn settings (2605.07990, achieving 93-100% steering accuracy) and that ~50% of general reasoning is unfaithful (RFEval), no prior work examines whether an agent's stated reasoning for choosing a specific tool across conversation turns actually drives that decision. We construct TOOLFAITH-BENCH, a 600-scenario diagnostic benchmark across five domains, stratified into three difficulty tiers — Unambiguous (single correct tool), Soft-Ambiguous (one optimal among plausible candidates), and Hard-Ambiguous (multiple valid tools) — to address construct validity concerns about benchmark realism. We apply a four-type causal intervention protocol (reason-flip, reason-ablate, counterfactual-inject, reason-scramble) and introduce two metrics: Tool Selection Causal Fidelity (TSCF) and Reasoning Theater Index (RTI). We evaluate seven models spanning current open-weight systems (Kimi K2.6, GLM-5.1, Qwen3.6-35B-A3B, DeepSeek-V4-Pro) and frontier APIs (Claude Sonnet 4.6, GPT-5.5, Gemini 2.5 Pro), supplemented by a multi-turn probing study that extends 2605.07990 to the unsolved multi-turn regime with four novel analyses: cross-turn probe transfer, context-dependent encoding drift, error-induced replanning signals, and behavioral-mechanistic faithfulness coupling. We test five hypotheses, including that RTI will be elevated across model families (extending single-turn findings), that probe accuracy will degrade with conversation depth (unlike stable single-turn results), and — counterintuitively — that harder ambiguous scenarios may elicit more faithful reasoning than unambiguous ones because genuine deliberation is required.\n\n## Core Problem\nIn multi-turn tool-using agents, does the model's stated reasoning about tool selection — which tool to call, with what parameters, and why — actually causally drive the tool call decision, or is it post-hoc rationalization of a latent policy? Recent probing work (2605.07990, 2605.09252) has shown that tool identity is linearly encoded in pre-generation activations in single-turn settings, suggesting CoT may be decorative. But these findings explicitly fail to transfer to multi-turn agentic settings, where accumulated conversation history, prior tool results, and error feedback create dynamic contexts that fundamentally differ from static single-turn tool menus. No systematic behavioral study exists to measure causal coupling between stated reasoning and tool-call actions across conversation turns.\n\n## Opportunity\nThe landscape has bifurcated: single-turn tool probing is now well-characterized (2605.07990 achieves 93-100% steering accuracy for 4B+ models; 2605.09252 shows 0.89-0.96 AUROC for tool-necessity probing), while multi-turn agentic tool selection remains essentially unstudied from a faithfulness perspective. This is precisely where the stakes are highest — production agents execute multi-step workflows where early tool calls condition later ones, errors require replanning, and unfaithful reasoning about tool selection can cascade into irreversible harmful actions. The faithfulness evaluation literature has advanced rapidly in 2026: RFEval finds ~50% of reasoning outputs unfaithful across 7,186 instances; 'Lie to Me' reveals a 59-percentage-point gap between internal recognition and output acknowledgment of hint influence; 'Decoding Answers Before CoT' shows 0.9 AUC pre-CoT answer probing — yet all this work targets single-turn QA/math, not agentic tool selection. Critically, 2605.07990 found multi-turn steering to be 'fragile' with -30 to +10pp vs. baseline and 'no consistent direction,' directly motivating a systematic study of multi-turn tool-selection faithfulness. The behavioral intervention approach — perturbing CoT and measuring whether tool calls change — is entirely unaddressed by any existing work on tool-call probing, creating a unique and timely contribution.\n\n## Related Work / Landscape\nThe landscape spans four converging threads:\n\n**Thread 1 — CoT Faithfulness (General):** Project Ariadne (2601.02314) finds causal decoupling with violation density up to 0.77 in factual domains but focuses on claims, not actions. 'Decoding Answers Before CoT' (2603.01437) shows answers encoded in pre-CoT activations with 0.9 AUC, establishing that CoT can be post-hoc, but only for binary QA. 'Catching Rationalization in the Act' (2603.17199) detects motivated reasoning via activation probing, showing internal representations outperform CoT monitors. RFEval (2602.17053) provides a 7,186-instance counterfactual intervention benchmark finding ~50% unfaithfulness, but for reasoning tasks not tool calls. FACT-E (2604.10693, ACL 2026 Findings) uses causal perturbations for CoT evaluation, finding self-evaluation unreliable. C2-Faith (2603.05167) benchmarks LLM-as-judge for causal/coverage faithfulness, showing systematic blind spots in localization. 'Lie to Me' (2603.22582) evaluates 12 models finding faithfulness rates from 39.7% to 89.9% with a critical 59pp thinking-vs-output gap. Breaking the Chain (2603.16475) shows 60% insensitivity to intermediate structure interventions. FaithCoT-Bench (ICLR 2026, 2510.04040) and FRIT (2509.13334) address single-turn QA faithfulness only.\n\n**Thread 2 — Tool-Call Probing (Single-Turn):** 'Tool Calling is Linearly Readable and Steerable' (2605.07990) probes 12 models, achieving 93-100% tool-name steering accuracy at 4B+ in single-turn fixed-menu settings, but explicitly finds multi-turn transfer 'fragile' (-30 to +10pp). Argument values are NOT steerable (0/30). 'LLM Agents Already Know When to Call Tools' (2605.09252) shows binary tool-necessity is decodable at 0.89-0.96 AUROC, with reasoning providing no additional signal. 'Beyond the Black Box' (2605.06890) applies SAE + probes to multi-step trajectories for tool-need/tool-risk classification but not tool identity or faithfulness. 'Internal Representations as Indicators of Hallucinations in Agent Tool Selection' (2601.05214) detects hallucinated tool calls from hidden states but in single-turn only.\n\n**Thread 3 — Tool Selection Robustness/Behavior:** 'Tool Preferences in Agentic LLMs are Unreliable' (EMNLP 2025, 2505.18135) shows tool selection is fragile under description manipulation but does not examine CoT faithfulness. 'The Reasoning Trap' (2510.22977) demonstrates RL causally amplifies tool hallucination but studies hallucination rates, not reasoning faithfulness. TOOLCERT (2510.03992) studies distributional robustness, not faithfulness. 'Brief Is Better' (2604.02155) finds non-monotonic CoT budget effects on function-calling accuracy. 'The Causal Impact of Tool Affordance on Safety Alignment' (ICECET 2026, 2603.20320) examines safety but not faithfulness.\n\n**Thread 4 — Agentic Monitoring:** SAVeR (2604.08401) proposes self-auditing for agentic faithfulness but provides limited empirical analysis. 'Noticing the Watcher' (2603.16928) shows models detect CoT monitoring from feedback at up to 19% awareness. 'Reasoning and Tool-use Compete in Agentic RL' (2602.00994) reveals interference between reasoning and tool use during training.\n\n**Critical Gap:** No work combines behavioral causal interventions on tool-selection CoT with mechanistic probing in multi-turn agentic settings. Single-turn probing is established; multi-turn is explicitly unsolved. Behavioral faithfulness testing for tool selection is entirely absent.\n\n## Approach\nWe construct TOOLFAITH-BENCH, a diagnostic benchmark of 600 multi-turn agentic scenarios across five domains (code editing, web browsing, data analysis, system administration, information retrieval), each containing 2-4 tool-selection decision points. Scenarios are stratified into three difficulty tiers reflecting real-world ambiguity:\n\n**Tier 1 — Unambiguous (200 scenarios):** A single correct tool per decision point; the reasoning chain uniquely determines the tool. Serves as calibration: if TSCF is low here, the CoT is clearly decorative.\n\n**Tier 2 — Soft-Ambiguous (200 scenarios):** 2-3 plausible tools with one clearly optimal. The reasoning must contain distinguishing information (e.g., 'the file is >2GB, so we need streaming upload rather than multipart'). Interventions target this distinguishing reasoning.\n\n**Tier 3 — Hard-Ambiguous (200 scenarios):** Multiple genuinely valid tools. Faithfulness is measured via stance consistency (does the CoT logically support the specific tool chosen?) and causal coupling (does perturbing the CoT change which valid tool is selected?), following RFEval's framework of decoupling faithfulness from correctness.\n\nAt each decision point we apply four perturbation types: (1) reason-flip — rewrite the CoT to justify a different tool, (2) reason-ablate — remove reasoning entirely, presenting only task context, (3) counterfactual-inject — insert facts that should change the optimal tool, (4) reason-scramble — shuffle reasoning sentences while preserving tool mentions. We define two complementary metrics: Tool Selection Causal Fidelity (TSCF), the rate at which tool calls correctly follow intervened reasoning, and Reasoning Theater Index (RTI), the rate at which tool calls remain unchanged despite contradictory reasoning.\n\nWe evaluate seven models spanning current open-weight systems (Kimi K2.6, GLM-5.1, Qwen3.6-35B-A3B, DeepSeek-V4-Pro) and frontier APIs (Claude Sonnet 4.6, GPT-5.5, Gemini 2.5 Pro), supplementing behavioral results with a multi-turn probing study on open-weight models. The probing component is explicitly positioned as an extension of 2605.07990 to the unsolved multi-turn regime, with four novel analyses: (a) cross-turn probe transfer — whether a probe trained at decision point 1 (turn 2) generalizes to decision point 3 (turn 8) as context accumulates; (b) context-dependent encoding drift — whether the linear direction encoding a given tool shifts across turns as prior tool results modify the task state; (c) error-induced replanning signals — whether tool errors create detectable representational shifts before the next tool selection; (d) faithfulness coupling — correlating probe-detected pre-commitment (tool identity encoded before CoT) with behavioral unfaithfulness (low TSCF), testing whether mechanistic and behavioral measures of unfaithfulness align. This goes beyond 2605.07990's domain transfer, because multi-turn contexts create fundamentally different representational challenges: the residual stream must integrate prior tool results, error states, and evolving task context alongside the current tool decision, and 2605.07990 explicitly showed this integration is fragile.\n\n## Inspiration\nThree converging findings: (1) 2605.07990's explicit acknowledgment that multi-turn tool-call probing is 'fragile' and unsolved, creating a clear frontier; (2) the faithfulness evaluation literature's maturation (RFEval, FACT-E, Lie to Me) providing proven intervention methodologies that have never been applied to tool selection; (3) the growing deployment of multi-turn agentic systems where tool-selection faithfulness has direct safety implications that single-turn probing cannot address.\n\n## Key References\n- Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents (arXiv 2026, 2601.02314)\n- Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing [SAVeR] (arXiv 2026, 2604.08401)\n- Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures (arXiv 2026, 2603.16475)\n- Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback (arXiv 2026, 2603.16928)\n- Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering (arXiv 2026, 2603.01437)\n- Catching Rationalization in the Act: Detecting Motivated Reasoning via Activation Probing (arXiv 2026, 2603.17199)\n- RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention (arXiv 2026, 2602.17053)\n- FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning (ACL 2026 Findings, 2604.10693)\n- C2-Faith: Benchmarking LLM Judges for Causal and Coverage Faithfulness in CoT Reasoning (arXiv 2026, 2603.05167)\n- Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models? (arXiv 2026, 2603.22582)\n- Tool Calling is Linearly Readable and Steerable in Language Models (arXiv 2026, 2605.07990)\n- LLM Agents Already Know When to Call Tools — Even Without Reasoning (arXiv 2026, 2605.09252)\n- Beyond the Black Box: Interpretability of Agentic AI Tool Use (arXiv 2026, 2605.06890)\n- FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning (ICLR 2026, 2510.04040)\n- FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness (arXiv 2025, 2509.13334)\n- The Reasoning Trap: How Enhancing LLM Reasoning Amplifies Tool Hallucination (arXiv 2025, 2510.22977)\n- Tool Preferences in Agentic LLMs are Unreliable (EMNLP 2025, 2505.18135)\n- Quantifying Distributional Robustness of Agentic Tool-Selection [TOOLCERT] (arXiv 2025, 2510.03992)\n- Internal Representations as Indicators of Hallucinations in Agent Tool Selection (arXiv 2026, 2601.05214)\n- Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calling Language Agents (arXiv 2026, 2604.02155)\n- The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents (ICECET 2026, 2603.20320)\n- Reasoning and Tool-use Compete in Agentic RL: From Quantifying Interference to Disentangled Tuning (arXiv 2026, 2602.00994)\n- Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation? (arXiv 2025, 2508.19827)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '300 H100-hours (150h model inference across 4 open-weight models × 600 scenarios × 4 intervention types × 3 tiers, 70h multi-turn probing experiments with cross-turn analysis, 80h development/debugging)', 'timeline': '12-14 weeks (3 wk benchmark design with tiered difficulty validation, 3 wk implementation, 3 wk experiments, 3-5 wk analysis/writing)', 'estimated_gpu_cost': '$750 (at ~$2.50/hr H100 spot pricing)'}\n- **human_in_loop**: {'gpu_hours': '240 H100-hours (same inference workload, fewer debugging iterations with Claude-assisted scenario generation and tiered validation)', 'timeline': '10-12 weeks (2.5 wk benchmark design, 2 wk implementation, 2.5 wk experiments, 3-4 wk analysis/writing)', 'claude_api_cost': '$350-450 (scenario generation across 3 tiers, ambiguity calibration, code assistance, statistical analysis, paper drafting across ~18M input + 6M output tokens)', 'estimated_gpu_cost': '$600 (at ~$2.50/hr H100 spot pricing)'}\n- **auto_research**: {'gpu_hours': '500 H100-hours (larger intervention sweep, additional ablations on tier boundaries, probe transfer experiments across multiple random seeds, cross-model probe transfer analysis)', 'timeline': '5-7 weeks wall-clock (parallelized scenario generation, concurrent model evaluation, automated analysis pipeline)', 'claude_api_cost': '$800-1000 (orchestration, tiered scenario generation with ambiguity calibration, evaluation judging, statistical analysis, full paper drafting across ~45M input + 18M output tokens)', 'estimated_gpu_cost': '$1250 (at ~$2.50/hr H100 spot pricing)', 'speed_bottleneck': 'Tier 2/3 scenario quality validation — ensuring soft-ambiguous scenarios have correctly calibrated difficulty (one tool genuinely better but not trivially so) requires human spot-checking that cannot be fully automated without risking construct validity'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T18:35:08.695Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:35:08.695Z",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-19T18:35:08.706Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn Probing

## Description
We present the first systematic study of whether tool-selection reasoning in multi-turn agentic systems is causally faithful or post-hoc rationalization, combining behavioral causal interventions with multi-turn mechanistic probing. While recent work has established that tool identity is linearly readable from pre-generation activations in single-turn settings (2605.07990, achieving 93-100% steering accuracy) and that ~50% of general reasoning is unfaithful (RFEval), no prior work examines whether an agent's stated reasoning for choosing a specific tool across conversation turns actually drives that decision. We construct TOOLFAITH-BENCH, a 600-scenario diagnostic benchmark across five domains, stratified into three difficulty tiers — Unambiguous (single correct tool), Soft-Ambiguous (one optimal among plausible candidates), and Hard-Ambiguous (multiple valid tools) — to address construct validity concerns about benchmark realism. We apply a four-type causal intervention protocol (reason-flip, reason-ablate, counterfactual-inject, reason-scramble) and introduce two metrics: Tool Selection Causal Fidelity (TSCF) and Reasoning Theater Index (RTI). We evaluate seven models spanning current open-weight systems (Kimi K2.6, GLM-5.1, Qwen3.6-35B-A3B, DeepSeek-V4-Pro) and frontier APIs (Claude Sonnet 4.6, GPT-5.5, Gemini 2.5 Pro), supplemented by a multi-turn probing study that extends 2605.07990 to the unsolved multi-turn regime with four novel analyses: cross-turn probe transfer, context-dependent encoding drift, error-induced replanning signals, and behavioral-mechanistic faithfulness coupling. We test five hypotheses, including that RTI will be elevated across model families (extending single-turn findings), that probe accuracy will degrade with conversation depth (unlike stable single-turn results), and — counterintuitively — that harder ambiguous scenarios may elicit more faithful reasoning than unambiguous ones because genuine deliberation is required.

## Core Problem
In multi-turn tool-using agents, does the model's stated reasoning about tool selection — which tool to call, with what parameters, and why — actually causally drive the tool call decision, or is it post-hoc rationalization of a latent policy? Recent probing work (2605.07990, 2605.09252) has shown that tool identity is linearly encoded in pre-generation activations in single-turn settings, suggesting CoT may be decorative. But these findings explicitly fail to transfer to multi-turn agentic settings, where accumulated conversation history, prior tool results, and error feedback create dynamic contexts that fundamentally differ from static single-turn tool menus. No systematic behavioral study exists to measure causal coupling between stated reasoning and tool-call actions across conversation turns.

## Opportunity
The landscape has bifurcated: single-turn tool probing is now well-characterized (2605.07990 achieves 93-100% steering accuracy for 4B+ models; 2605.09252 shows 0.89-0.96 AUROC for tool-necessity probing), while multi-turn agentic tool selection remains essentially unstudied from a faithfulness perspective. This is precisely where the stakes are highest — production agents execute multi-step workflows where early tool calls condition later ones, errors require replanning, and unfaithful reasoning about tool selection can cascade into irreversible harmful actions. The faithfulness evaluation literature has advanced rapidly in 2026: RFEval finds ~50% of reasoning outputs unfaithful across 7,186 instances; 'Lie to Me' reveals a 59-percentage-point gap between internal recognition and output acknowledgment of hint influence; 'Decoding Answers Before CoT' shows 0.9 AUC pre-CoT answer probing — yet all this work targets single-turn QA/math, not agentic tool selection. Critically, 2605.07990 found multi-turn steering to be 'fragile' with -30 to +10pp vs. baseline and 'no consistent direction,' directly motivating a systematic study of multi-turn tool-selection faithfulness. The behavioral intervention approach — perturbing CoT and measuring whether tool calls change — is entirely unaddressed by any existing work on tool-call probing, creating a unique and timely contribution.

## Related Work / Landscape
The landscape spans four converging threads:

**Thread 1 — CoT Faithfulness (General):** Project Ariadne (2601.02314) finds causal decoupling with violation density up to 0.77 in factual domains but focuses on claims, not actions. 'Decoding Answers Before CoT' (2603.01437) shows answers encoded in pre-CoT activations with 0.9 AUC, establishing that CoT can be post-hoc, but only for binary QA. 'Catching Rationalization in the Act' (2603.17199) detects motivated reasoning via activation probing, showing internal representations outperform CoT monitors. RFEval (2602.17053) provides a 7,186-instance counterfactual intervention benchmark finding ~50% unfaithfulness, but for reasoning tasks not tool calls. FACT-E (2604.10693, ACL 2026 Findings) uses causal perturbations for CoT evaluation, finding self-evaluation unreliable. C2-Faith (2603.05167) benchmarks LLM-as-judge for causal/coverage faithfulness, showing systematic blind spots in localization. 'Lie to Me' (2603.22582) evaluates 12 models finding faithfulness rates from 39.7% to 89.9% with a critical 59pp thinking-vs-output gap. Breaking the Chain (2603.16475) shows 60% insensitivity to intermediate structure interventions. FaithCoT-Bench (ICLR 2026, 2510.04040) and FRIT (2509.13334) address single-turn QA faithfulness only.

**Thread 2 — Tool-Call Probing (Single-Turn):** 'Tool Calling is Linearly Readable and Steerable' (2605.07990) probes 12 models, achieving 93-100% tool-name steering accuracy at 4B+ in single-turn fixed-menu settings, but explicitly finds multi-turn transfer 'fragile' (-30 to +10pp). Argument values are NOT steerable (0/30). 'LLM Agents Already Know When to Call Tools' (2605.09252) shows binary tool-necessity is decodable at 0.89-0.96 AUROC, with reasoning providing no additional signal. 'Beyond the Black Box' (2605.06890) applies SAE + probes to multi-step trajectories for tool-need/tool-risk classification but not tool identity or faithfulness. 'Internal Representations as Indicators of Hallucinations in Agent Tool Selection' (2601.05214) detects hallucinated tool calls from hidden states but in single-turn only.

**Thread 3 — Tool Selection Robustness/Behavior:** 'Tool Preferences in Agentic LLMs are Unreliable' (EMNLP 2025, 2505.18135) shows tool selection is fragile under description manipulation but does not examine CoT faithfulness. 'The Reasoning Trap' (2510.22977) demonstrates RL causally amplifies tool hallucination but studies hallucination rates, not reasoning faithfulness. TOOLCERT (2510.03992) studies distributional robustness, not faithfulness. 'Brief Is Better' (2604.02155) finds non-monotonic CoT budget effects on function-calling accuracy. 'The Causal Impact of Tool Affordance on Safety Alignment' (ICECET 2026, 2603.20320) examines safety but not faithfulness.

**Thread 4 — Agentic Monitoring:** SAVeR (2604.08401) proposes self-auditing for agentic faithfulness but provides limited empirical analysis. 'Noticing the Watcher' (2603.16928) shows models detect CoT monitoring from feedback at up to 19% awareness. 'Reasoning and Tool-use Compete in Agentic RL' (2602.00994) reveals interference between reasoning and tool use during training.

**Critical Gap:** No work combines behavioral causal interventions on tool-selection CoT with mechanistic probing in multi-turn agentic settings. Single-turn probing is established; multi-turn is explicitly unsolved. Behavioral faithfulness testing for tool selection is entirely absent.

## Approach
We construct TOOLFAITH-BENCH, a diagnostic benchmark of 600 multi-turn agentic scenarios across five domains (code editing, web browsing, data analysis, system administration, information retrieval), each containing 2-4 tool-selection decision points. Scenarios are stratified into three difficulty tiers reflecting real-world ambiguity:

**Tier 1 — Unambiguous (200 scenarios):** A single correct tool per decision point; the reasoning chain uniquely determines the tool. Serves as calibration: if TSCF is low here, the CoT is clearly decorative.

**Tier 2 — Soft-Ambiguous (200 scenarios):** 2-3 plausible tools with one clearly optimal. The reasoning must contain distinguishing information (e.g., 'the file is >2GB, so we need streaming upload rather than multipart'). Interventions target this distinguishing reasoning.

**Tier 3 — Hard-Ambiguous (200 scenarios):** Multiple genuinely valid tools. Faithfulness is measured via stance consistency (does the CoT logically support the specific tool chosen?) and causal coupling (does perturbing the CoT change which valid tool is selected?), following RFEval's framework of decoupling faithfulness from correctness.

At each decision point we apply four perturbation types: (1) reason-flip — rewrite the CoT to justify a different tool, (2) reason-ablate — remove reasoning entirely, presenting only task context, (3) counterfactual-inject — insert facts that should change the optimal tool, (4) reason-scramble — shuffle reasoning sentences while preserving tool mentions. We define two complementary metrics: Tool Selection Causal Fidelity (TSCF), the rate at which tool calls correctly follow intervened reasoning, and Reasoning Theater Index (RTI), the rate at which tool calls remain unchanged despite contradictory reasoning.

We evaluate seven models spanning current open-weight systems (Kimi K2.6, GLM-5.1, Qwen3.6-35B-A3B, DeepSeek-V4-Pro) and frontier APIs (Claude Sonnet 4.6, GPT-5.5, Gemini 2.5 Pro), supplementing behavioral results with a multi-turn probing study on open-weight models. The probing component is explicitly positioned as an extension of 2605.07990 to the unsolved multi-turn regime, with four novel analyses: (a) cross-turn probe transfer — whether a probe trained at decision point 1 (turn 2) generalizes to decision point 3 (turn 8) as context accumulates; (b) context-dependent encoding drift — whether the linear direction encoding a given tool shifts across turns as prior tool results modify the task state; (c) error-induced replanning signals — whether tool errors create detectable representational shifts before the next tool selection; (d) faithfulness coupling — correlating probe-detected pre-commitment (tool identity encoded before CoT) with behavioral unfaithfulness (low TSCF), testing whether mechanistic and behavioral measures of unfaithfulness align. This goes beyond 2605.07990's domain transfer, because multi-turn contexts create fundamentally different representational challenges: the residual stream must integrate prior tool results, error states, and evolving task context alongside the current tool decision, and 2605.07990 explicitly showed this integration is fragile.

## Inspiration
Three converging findings: (1) 2605.07990's explicit acknowledgment that multi-turn tool-call probing is 'fragile' and unsolved, creating a clear frontier; (2) the faithfulness evaluation literature's maturation (RFEval, FACT-E, Lie to Me) providing proven intervention methodologies that have never been applied to tool selection; (3) the growing deployment of multi-turn agentic systems where tool-selection faithfulness has direct safety implications that single-turn probing cannot address.

## Key References
- Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents (arXiv 2026, 2601.02314)
- Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing [SAVeR] (arXiv 2026, 2604.08401)
- Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures (arXiv 2026, 2603.16475)
- Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback (arXiv 2026, 2603.16928)
- Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering (arXiv 2026, 2603.01437)
- Catching Rationalization in the Act: Detecting Motivated Reasoning via Activation Probing (arXiv 2026, 2603.17199)
- RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention (arXiv 2026, 2602.17053)
- FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning (ACL 2026 Findings, 2604.10693)
- C2-Faith: Benchmarking LLM Judges for Causal and Coverage Faithfulness in CoT Reasoning (arXiv 2026, 2603.05167)
- Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models? (arXiv 2026, 2603.22582)
- Tool Calling is Linearly Readable and Steerable in Language Models (arXiv 2026, 2605.07990)
- LLM Agents Already Know When to Call Tools — Even Without Reasoning (arXiv 2026, 2605.09252)
- Beyond the Black Box: Interpretability of Agentic AI Tool Use (arXiv 2026, 2605.06890)
- FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning (ICLR 2026, 2510.04040)
- FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness (arXiv 2025, 2509.13334)
- The Reasoning Trap: How Enhancing LLM Reasoning Amplifies Tool Hallucination (arXiv 2025, 2510.22977)
- Tool Preferences in Agentic LLMs are Unreliable (EMNLP 2025, 2505.18135)
- Quantifying Distributional Robustness of Agentic Tool-Selection [TOOLCERT] (arXiv 2025, 2510.03992)
- Internal Representations as Indicators of Hallucinations in Agent Tool Selection (arXiv 2026, 2601.05214)
- Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calling Language Agents (arXiv 2026, 2604.02155)
- The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents (ICECET 2026, 2603.20320)
- Reasoning and Tool-use Compete in Agentic RL: From Quantifying Interference to Disentangled Tuning (arXiv 2026, 2602.00994)
- Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation? (arXiv 2025, 2508.19827)

## Resource Estimate
- **manual**: {'gpu_hours': '300 H100-hours (150h model inference across 4 open-weight models × 600 scenarios × 4 intervention types × 3 tiers, 70h multi-turn probing experiments with cross-turn analysis, 80h development/debugging)', 'timeline': '12-14 weeks (3 wk benchmark design with tiered difficulty validation, 3 wk implementation, 3 wk experiments, 3-5 wk analysis/writing)', 'estimated_gpu_cost': '$750 (at ~$2.50/hr H100 spot pricing)'}
- **human_in_loop**: {'gpu_hours': '240 H100-hours (same inference workload, fewer debugging iterations with Claude-assisted scenario generation and tiered validation)', 'timeline': '10-12 weeks (2.5 wk benchmark design, 2 wk implementation, 2.5 wk experiments, 3-4 wk analysis/writing)', 'claude_api_cost': '$350-450 (scenario generation across 3 tiers, ambiguity calibration, code assistance, statistical analysis, paper drafting across ~18M input + 6M output tokens)', 'estimated_gpu_cost': '$600 (at ~$2.50/hr H100 spot pricing)'}
- **auto_research**: {'gpu_hours': '500 H100-hours (larger intervention sweep, additional ablations on tier boundaries, probe transfer experiments across multiple random seeds, cross-model probe transfer analysis)', 'timeline': '5-7 weeks wall-clock (parallelized scenario generation, concurrent model evaluation, automated analysis pipeline)', 'claude_api_cost': '$800-1000 (orchestration, tiered scenario generation with ambiguity calibration, evaluation judging, statistical analysis, full paper drafting across ~45M input + 18M output tokens)', 'estimated_gpu_cost': '$1250 (at ~$2.50/hr H100 spot pricing)', 'speed_bottleneck': 'Tier 2/3 scenario quality validation — ensuring soft-ambiguous scenarios have correctly calibrated difficulty (one tool genuinely better but not trivially so) requires human spot-checking that cannot be fully automated without risking construct validity'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "cc8c0189-3054-417a-9b7e-b465e21bc716",
  "type": "user",
  "uuid": "16095d36-a573-4715-a03a-40dcb4500815",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:35:08.705Z_

```json
{
  "parentUuid": "16095d36-a573-4715-a03a-40dcb4500815",
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
  "uuid": "c4d50e83-b5b0-49de-a038-a9e590b0de2a",
  "timestamp": "2026-05-19T18:35:08.705Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:35:08.705Z_

```json
{
  "parentUuid": "c4d50e83-b5b0-49de-a038-a9e590b0de2a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a06789d9-7d7f-42f0-957b-6963ebf5d72b",
  "timestamp": "2026-05-19T18:35:08.705Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn…",
  "leafUuid": "a06789d9-7d7f-42f0-957b-6963ebf5d72b",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate tool-selection faithfulness proposal for publication",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:35:29.269Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026. Let me first note something important: the user says "CoRL 2026" which is a robotics conference (Conference on Robot Learning). But this proposal is about faithfulness of tool-selection reasoning in LLM agents - this seems more like an NLP/AI conference topic (like ACL, EMNLP, NeurIPS, ICML, ICLR). Let me re-read...

Actually, wait. The system prompt says "评估其投稿 CoRL 2026 主会的中稿潜力" - CoRL is Conference on Robot Learning. 

There's a clear mismatch here: this proposal focuses on LLM agent tool-selection faithfulness with no robotics component, yet it's being submitted to a robotics venue. That said, let me evaluate the core idea quality regardless of venue fit, since that's what matters most for assessing the research contribution. I'm realizing there's a fundamental mismatch here—the proposal lacks any robotics content, yet I'm being asked to evaluate it for CoRL, which is typically a robotics conference. I should proceed with an objective evaluation of the idea's quality while flagging this venue concern, and I'll need to do some web searches to better understand the current landscape in this field.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a06789d9-7d7f-42f0-957b-6963ebf5d72b",
  "isSidechain": false,
  "requestId": "req_011CbCQieXaQsDPnvZKrQd2f",
  "type": "assistant",
  "uuid": "f725c810-f15c-4d28-824e-b7870c5bed43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XxAaisQdAyQ9D3CTjYXRf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19817,
      "output_tokens": 642,
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
          "output_tokens": 642,
          "cache_read_input_tokens": 19817,
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

_source line 9 · 2026-05-19T18:35:29.273Z_

我先进行领域调研，搜索与本 proposal 最相关的近期工作，然后再进行评估。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f725c810-f15c-4d28-824e-b7870c5bed43",
  "isSidechain": false,
  "requestId": "req_011CbCQieXaQsDPnvZKrQd2f",
  "type": "assistant",
  "uuid": "da072335-55a7-4aa2-9499-590d01ff4d9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XxAaisQdAyQ9D3CTjYXRf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19817,
      "output_tokens": 642,
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
          "output_tokens": 642,
          "cache_read_input_tokens": 19817,
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

_source line 10 · 2026-05-19T18:35:29.276Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GyBKp8tsYJNF1Ls8YTK6TS`</summary>

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
  "parentUuid": "da072335-55a7-4aa2-9499-590d01ff4d9f",
  "isSidechain": false,
  "requestId": "req_011CbCQieXaQsDPnvZKrQd2f",
  "type": "assistant",
  "uuid": "13daf8a8-d572-44e1-9480-cadf08a54841",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XxAaisQdAyQ9D3CTjYXRf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19817,
      "output_tokens": 642,
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
          "output_tokens": 642,
          "cache_read_input_tokens": 19817,
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

_source line 11 · 2026-05-19T18:35:29.284Z_

<details><summary>↩ Tool result · `toolu_01GyBKp8tsYJNF1Ls8YTK6TS`</summary>

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
  "parentUuid": "13daf8a8-d572-44e1-9480-cadf08a54841",
  "isSidechain": false,
  "promptId": "cc8c0189-3054-417a-9b7e-b465e21bc716",
  "type": "user",
  "uuid": "59650f6f-c64d-47c8-8969-cc57d2e9a64f",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "13daf8a8-d572-44e1-9480-cadf08a54841",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T18:35:41.411Z_

现在开始进行领域调研，我会并行发起多个搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59650f6f-c64d-47c8-8969-cc57d2e9a64f",
  "isSidechain": false,
  "requestId": "req_011CbCQkAqVpR2bWntUv2jkD",
  "type": "assistant",
  "uuid": "2a721ad2-f56f-4fdb-b6fa-f1950233032d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Picv8x7WQR3LFmCxnYQJZK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1169,
      "cache_read_input_tokens": 19817,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1169,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 262,
          "cache_read_input_tokens": 19817,
          "cache_creation_input_tokens": 1169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1169
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T18:35:42.302Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HxBgNHbqnjxZRXuSXU346k`</summary>

```json
{
  "query": "tool calling linearly readable steerable language models arXiv 2605.07990 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a721ad2-f56f-4fdb-b6fa-f1950233032d",
  "isSidechain": false,
  "requestId": "req_011CbCQkAqVpR2bWntUv2jkD",
  "type": "assistant",
  "uuid": "11d3291c-e0c0-4a66-8fb7-60e4cdfa5d0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Picv8x7WQR3LFmCxnYQJZK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1169,
      "cache_read_input_tokens": 19817,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1169,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 262,
          "cache_read_input_tokens": 19817,
          "cache_creation_input_tokens": 1169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1169
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T18:35:43.713Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EpKDqoaJFKtbG4N17zAtfm`</summary>

```json
{
  "query": "RFEval reasoning faithfulness counterfactual intervention benchmark 2026 arXiv 2602.17053"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11d3291c-e0c0-4a66-8fb7-60e4cdfa5d0b",
  "isSidechain": false,
  "requestId": "req_011CbCQkAqVpR2bWntUv2jkD",
  "type": "assistant",
  "uuid": "2efee56f-5381-424e-be5f-07d1d06ca60e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Picv8x7WQR3LFmCxnYQJZK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1169,
      "cache_read_input_tokens": 19817,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1169,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 262,
          "cache_read_input_tokens": 19817,
          "cache_creation_input_tokens": 1169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1169
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T18:35:44.187Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018JMYLTBwh6bqzPaXx9AX2v`</summary>

```json
{
  "query": "CoT faithfulness tool selection multi-turn agentic systems 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2efee56f-5381-424e-be5f-07d1d06ca60e",
  "isSidechain": false,
  "requestId": "req_011CbCQkAqVpR2bWntUv2jkD",
  "type": "assistant",
  "uuid": "c8d255a9-3aef-4cca-9080-4b09cc0e6093",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Picv8x7WQR3LFmCxnYQJZK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1169,
      "cache_read_input_tokens": 19817,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1169,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 262,
          "cache_read_input_tokens": 19817,
          "cache_creation_input_tokens": 1169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1169
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T18:35:44.817Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017oB4tP7MdpsdHpR3dp6tm6`</summary>

```json
{
  "query": "LLM agents tool call faithfulness reasoning post-hoc rationalization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8d255a9-3aef-4cca-9080-4b09cc0e6093",
  "isSidechain": false,
  "requestId": "req_011CbCQkAqVpR2bWntUv2jkD",
  "type": "assistant",
  "uuid": "46b003ca-ab12-42dc-baf1-1fb0e902ce83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Picv8x7WQR3LFmCxnYQJZK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1169,
      "cache_read_input_tokens": 19817,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1169,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 262,
          "cache_read_input_tokens": 19817,
          "cache_creation_input_tokens": 1169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1169
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T18:35:48.521Z_

<details><summary>↩ Tool result · `toolu_01EpKDqoaJFKtbG4N17zAtfm`</summary>

```text
Web search results for query: "RFEval reasoning faithfulness counterfactual intervention benchmark 2026 arXiv 2602.17053"

Links: [{"title":"[2602.17053v1] RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/abs/2602.17053v1"},{"title":"[2602.17053] RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/abs/2602.17053"},{"title":"RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=2Gc8aj0afg"},{"title":"RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/pdf/2602.17053"},{"title":"RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/html/2602.17053"}]

Based on the search results, here's what I found about RFEval:

RFEval addresses the issue that Large Reasoning Models (LRMs) exhibit strong performance, yet often produce rationales that sound plausible but fail to reflect their true decision process, undermining reliability and trust.

The paper introduces a formal framework for reasoning faithfulness, defined by two testable conditions: stance consistency (a coherent stance linking reasoning to answer) and causal influence (the stated reasoning causally drives the answer under output-level interventions), explicitly decoupled from accuracy.

To operationalize this, RFEval is a benchmark of 7,186 instances across seven tasks that probes faithfulness via controlled, output-level counterfactual interventions.

**Key Findings:**

Evaluating twelve open-source LRMs, the researchers find unfaithfulness in 49.7% of outputs, predominantly from stance inconsistency. Failures are concentrated in brittle, convergent domains such as math and code, and correlate more with post-training regimes than with scale.

The paper was submitted to arXiv on February 19, 2026, with the latest version (v3) on February 23, 2026, and is authored by Yunseok Han, Yejoon Lee, and Jaeyoung Do.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2efee56f-5381-424e-be5f-07d1d06ca60e",
  "isSidechain": false,
  "promptId": "cc8c0189-3054-417a-9b7e-b465e21bc716",
  "type": "user",
  "uuid": "de71ca95-24c2-4a84-a6e3-2f051c4f0dae",
  "toolUseResult": {
    "query": "RFEval reasoning faithfulness counterfactual intervention benchmark 2026 arXiv 2602.17053",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FewkQDQTqxNsNXiKSZcmtD",
        "content": [
          {
            "title": "[2602.17053v1] RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models",
            "url": "https://arxiv.org/abs/2602.17053v1"
          },
          {
            "title": "[2602.17053] RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models",
            "url": "https://arxiv.org/abs/2602.17053"
          },
          {
            "title": "RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models | OpenReview",
            "url": "https://openreview.net/forum?id=2Gc8aj0afg"
          },
          {
            "title": "RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2602.17053"
          },
          {
            "title": "RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models",
            "url": "https://arxiv.org/html/2602.17053"
          }
        ]
      },
      "Based on the search results, here's what I found about RFEval:\n\nRFEval addresses the issue that Large Reasoning Models (LRMs) exhibit strong performance, yet often produce rationales that sound plausible but fail to reflect their true decision process, undermining reliability and trust.\n\nThe paper introduces a formal framework for reasoning faithfulness, defined by two testable conditions: stance consistency (a coherent stance linking reasoning to answer) and causal influence (the stated reasoning causally drives the answer under output-level interventions), explicitly decoupled from accuracy.\n\nTo operationalize this, RFEval is a benchmark of 7,186 instances across seven tasks that probes faithfulness via controlled, output-level counterfactual interventions.\n\n**Key Findings:**\n\nEvaluating twelve open-source LRMs, the researchers find unfaithfulness in 49.7% of outputs, predominantly from stance inconsistency. Failures are concentrated in brittle, convergent domains such as math and code, and correlate more with post-training regimes than with scale.\n\nThe paper was submitted to arXiv on February 19, 2026, with the latest version (v3) on February 23, 2026, and is authored by Yunseok Han, Yejoon Lee, and Jaeyoung Do."
    ],
    "durationSeconds": 4.805679317000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2efee56f-5381-424e-be5f-07d1d06ca60e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T18:35:49.564Z_

<details><summary>↩ Tool result · `toolu_01HxBgNHbqnjxZRXuSXU346k`</summary>

```text
Web search results for query: "tool calling linearly readable steerable language models arXiv 2605.07990 2026"

Links: [{"title":"[2605.07990] Tool Calling is Linearly Readable and Steerable in Language Models","url":"https://arxiv.org/abs/2605.07990"},{"title":"[2605.07990v1] Tool Calling is Linearly Readable and Steerable in Language Models","url":"https://arxiv.org/abs/2605.07990v1"},{"title":"Tool Calling is Linearly Readable and Steerable in Language Models","url":"https://arxiv.org/html/2605.07990"},{"title":"AI Steerability 360: A Toolkit for Steering Large Language Models","url":"https://arxiv.org/pdf/2603.07837"},{"title":"How Does Controllability Emerge In Language Models During Pretraining?","url":"https://arxiv.org/pdf/2508.01892"}]

I found the paper! Here's information about arXiv paper 2605.07990 titled "Tool Calling is Linearly Readable and Steerable in Language Models", which was submitted on May 8, 2026.

**Key Findings:**

The research probed 12 instruction-tuned models across Gemma 3, Qwen 3, Qwen 2.5, and Llama 3.1 (270M to 27B parameters) and found that the identity of the chosen tool is linearly readable and steerable inside the model.

Adding the mean-difference between two tools' average internal activations switches which tool the model selects at 77-100% accuracy on name-only single-turn prompts (93-100% at 4B+), and the JSON arguments that follow autoregressively match the new tool's schema.

**Error Detection:**

The same per-tool means also flag likely errors before they happen: on Gemma 3 12B and 27B, queries where the gap between the top-1 and top-2 tool is smallest produce 14-21x more wrong calls than queries with the largest gap.

The paper was authored by researchers from University College London, Holistic AI, and Imperial College London.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11d3291c-e0c0-4a66-8fb7-60e4cdfa5d0b",
  "isSidechain": false,
  "promptId": "cc8c0189-3054-417a-9b7e-b465e21bc716",
  "type": "user",
  "uuid": "7986188f-fa13-4a19-9b14-ca416c67852b",
  "toolUseResult": {
    "query": "tool calling linearly readable steerable language models arXiv 2605.07990 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015aUnfqqjSU5hjRD3ehpK57",
        "content": [
          {
            "title": "[2605.07990] Tool Calling is Linearly Readable and Steerable in Language Models",
            "url": "https://arxiv.org/abs/2605.07990"
          },
          {
            "title": "[2605.07990v1] Tool Calling is Linearly Readable and Steerable in Language Models",
            "url": "https://arxiv.org/abs/2605.07990v1"
          },
          {
            "title": "Tool Calling is Linearly Readable and Steerable in Language Models",
            "url": "https://arxiv.org/html/2605.07990"
          },
          {
            "title": "AI Steerability 360: A Toolkit for Steering Large Language Models",
            "url": "https://arxiv.org/pdf/2603.07837"
          },
          {
            "title": "How Does Controllability Emerge In Language Models During Pretraining?",
            "url": "https://arxiv.org/pdf/2508.01892"
          }
        ]
      },
      "I found the paper! Here's information about arXiv paper 2605.07990 titled \"Tool Calling is Linearly Readable and Steerable in Language Models\", which was submitted on May 8, 2026.\n\n**Key Findings:**\n\nThe research probed 12 instruction-tuned models across Gemma 3, Qwen 3, Qwen 2.5, and Llama 3.1 (270M to 27B parameters) and found that the identity of the chosen tool is linearly readable and steerable inside the model.\n\nAdding the mean-difference between two tools' average internal activations switches which tool the model selects at 77-100% accuracy on name-only single-turn prompts (93-100% at 4B+), and the JSON arguments that follow autoregressively match the new tool's schema.\n\n**Error Detection:**\n\nThe same per-tool means also flag likely errors before they happen: on Gemma 3 12B and 27B, queries where the gap between the top-1 and top-2 tool is smallest produce 14-21x more wrong calls than queries with the largest gap.\n\nThe paper was authored by researchers from University College London, Holistic AI, and Imperial College London."
    ],
    "durationSeconds": 7.258660488000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "11d3291c-e0c0-4a66-8fb7-60e4cdfa5d0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T18:35:51.960Z_

<details><summary>↩ Tool result · `toolu_017oB4tP7MdpsdHpR3dp6tm6`</summary>

```text
Web search results for query: "LLM agents tool call faithfulness reasoning post-hoc rationalization 2025 2026"

Links: [{"title":"Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing","url":"https://arxiv.org/html/2604.08401"},{"title":"LLM Agent Architectures in 2026: Core Components and Patterns","url":"https://futureagi.com/blog/llm-agent-architectures-core-components/"},{"title":"Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents","url":"https://arxiv.org/pdf/2601.02314"},{"title":"Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing","url":"https://arxiv.org/pdf/2604.08401"},{"title":"Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents","url":"https://arxiv.org/html/2601.02314"},{"title":"Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1383/"}]

I found several relevant research papers and articles on this topic. Here are the key findings:

## Recent Research on LLM Agent Faithfulness

An emerging research perspective frames LLMs as agents that perform multi-step reasoning through planning, tool use, and interaction with external environments. However, there are significant concerns about faithfulness in this context.

### The Post-Hoc Rationalization Problem

Empirical studies show that generated chains of thought may rely on spurious signals, and intervening on them has limited impact on model predictions, suggesting that such explanations are post-hoc rationalizations. More specifically for agents, agent-generated plans or tool-use rationales may not causally determine outcomes, but instead serve as plausible post-hoc justifications.

While Chain-of-Thought (CoT) prompting allows agents to generate human-readable reasoning traces, it remains unclear whether these traces are faithful generative drivers of the model's output or merely post-hoc rationalizations.

### Proposed Solutions

Project Ariadne introduces a novel XAI framework that utilizes Structural Causal Models (SCMs) and counterfactual logic to audit the causal integrity of agentic reasoning. Additionally, span-level evaluation scores each LLM call for faithfulness, tool-use correctness, and grounding, representing an emerging practice in 2026 for assessing agent quality.

The research suggests that ensuring faithful reasoning in LLM agents remains an active and critical research area in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46b003ca-ab12-42dc-baf1-1fb0e902ce83",
  "isSidechain": false,
  "promptId": "cc8c0189-3054-417a-9b7e-b465e21bc716",
  "type": "user",
  "uuid": "44c33859-572d-4bfa-bec2-02e13e1ad60b",
  "toolUseResult": {
    "query": "LLM agents tool call faithfulness reasoning post-hoc rationalization 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NzrE9pmSHDgqR1AxRUHS3H",
        "content": [
          {
            "title": "Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing",
            "url": "https://arxiv.org/html/2604.08401"
          },
          {
            "title": "LLM Agent Architectures in 2026: Core Components and Patterns",
            "url": "https://futureagi.com/blog/llm-agent-architectures-core-components/"
          },
          {
            "title": "Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents",
            "url": "https://arxiv.org/pdf/2601.02314"
          },
          {
            "title": "Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing",
            "url": "https://arxiv.org/pdf/2604.08401"
          },
          {
            "title": "Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents",
            "url": "https://arxiv.org/html/2601.02314"
          },
          {
            "title": "Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.1383/"
          }
        ]
      },
      "I found several relevant research papers and articles on this topic. Here are the key findings:\n\n## Recent Research on LLM Agent Faithfulness\n\nAn emerging research perspective frames LLMs as agents that perform multi-step reasoning through planning, tool use, and interaction with external environments. However, there are significant concerns about faithfulness in this context.\n\n### The Post-Hoc Rationalization Problem\n\nEmpirical studies show that generated chains of thought may rely on spurious signals, and intervening on them has limited impact on model predictions, suggesting that such explanations are post-hoc rationalizations. More specifically for agents, agent-generated plans or tool-use rationales may not causally determine outcomes, but instead serve as plausible post-hoc justifications.\n\nWhile Chain-of-Thought (CoT) prompting allows agents to generate human-readable reasoning traces, it remains unclear whether these traces are faithful generative drivers of the model's output or merely post-hoc rationalizations.\n\n### Proposed Solutions\n\nProject Ariadne introduces a novel XAI framework that utilizes Structural Causal Models (SCMs) and counterfactual logic to audit the causal integrity of agentic reasoning. Additionally, span-level evaluation scores each LLM call for faithfulness, tool-use correctness, and grounding, representing an emerging practice in 2026 for assessing agent quality.\n\nThe research suggests that ensuring faithful reasoning in LLM agents remains an active and critical research area in 2025-2026."
    ],
    "durationSeconds": 7.140672250000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "46b003ca-ab12-42dc-baf1-1fb0e902ce83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T18:35:52.804Z_

<details><summary>↩ Tool result · `toolu_018JMYLTBwh6bqzPaXx9AX2v`</summary>

```text
Web search results for query: "CoT faithfulness tool selection multi-turn agentic systems 2026"

Links: [{"title":"Taskade","url":"https://www.taskade.com/wiki/ai/chain-of-thought"},{"title":"Agentic AI Architecture: Building Autonomous AI Systems in 2026 - Calmops","url":"https://calmops.com/architecture/agentic-ai-architecture-autonomous-ai-systems/"},{"title":"Best LLM Evaluation Tools for AI Agents in 2026 - Confident AI","url":"https://www.confident-ai.com/knowledge-base/compare/best-llm-evaluation-tools-for-ai-agents"},{"title":"10 Best AI Evaluation Tools for Testing & Improving AI Applications in 2026 - Confident AI","url":"https://www.confident-ai.com/knowledge-base/compare/best-ai-evaluation-tools-2026"},{"title":"Evaluating AI agents: Real-world lessons from building agentic systems at Amazon | Artificial Intelligence","url":"https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/"},{"title":"Quantifying Distributional Robustness of Agentic Tool-Selection","url":"https://arxiv.org/pdf/2510.03992"},{"title":"Top 7 LLM Evaluation Tools in 2026 - Confident AI","url":"https://www.confident-ai.com/knowledge-base/compare/best-llm-evaluation-tools"}]

I found relevant search results about CoT faithfulness, tool selection, and multi-turn agentic systems in 2026. Here are the key findings:

## Chain-of-Thought in Multi-Turn Agentic Systems

Agentic AI extends CoT across many turns, interleaving reasoning with tool use, and agentic systems use CoT at every step of a multi-turn automation.

## Evaluation of Tool Selection and Faithfulness

Purpose-built metrics for agentic workflows include tool selection accuracy, planning quality, step-level faithfulness, and reasoning coherence. Agents fail through cascading tool selection and reasoning errors.

## Amazon's Multi-Layer Evaluation Approach

The middle layer of agent evaluation determines whether the agent understands user intents correctly, how the LLM drives agentic workflow planning through chain-of-thought reasoning, whether the tool selection and execution are aligned with the agentic plan, and if the plan is completed successfully.

## Security and Robustness of Tool Selection

The integration of external tools into large language model agent workflows has fundamentally transformed agentic systems, allowing agents to retrieve information and invoke APIs to execute computations, and by chaining tool calls, agents perform multi-step reasoning and solve tasks that exceed the scope of static text generation.

The search results indicate that in 2026, evaluation frameworks are increasingly focusing on step-level faithfulness and tool selection accuracy as critical metrics for multi-turn agentic systems, moving beyond traditional output-only evaluation to assess intermediate reasoning and decision-making steps.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8d255a9-3aef-4cca-9080-4b09cc0e6093",
  "isSidechain": false,
  "promptId": "cc8c0189-3054-417a-9b7e-b465e21bc716",
  "type": "user",
  "uuid": "d4d81fb4-f353-4930-aa9c-f935db9f5ecd",
  "toolUseResult": {
    "query": "CoT faithfulness tool selection multi-turn agentic systems 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012hLSqFYF39Uv1NbsXfAgp8",
        "content": [
          {
            "title": "Taskade",
            "url": "https://www.taskade.com/wiki/ai/chain-of-thought"
          },
          {
            "title": "Agentic AI Architecture: Building Autonomous AI Systems in 2026 - Calmops",
            "url": "https://calmops.com/architecture/agentic-ai-architecture-autonomous-ai-systems/"
          },
          {
            "title": "Best LLM Evaluation Tools for AI Agents in 2026 - Confident AI",
            "url": "https://www.confident-ai.com/knowledge-base/compare/best-llm-evaluation-tools-for-ai-agents"
          },
          {
            "title": "10 Best AI Evaluation Tools for Testing & Improving AI Applications in 2026 - Confident AI",
            "url": "https://www.confident-ai.com/knowledge-base/compare/best-ai-evaluation-tools-2026"
          },
          {
            "title": "Evaluating AI agents: Real-world lessons from building agentic systems at Amazon | Artificial Intelligence",
            "url": "https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/"
          },
          {
            "title": "Quantifying Distributional Robustness of Agentic Tool-Selection",
            "url": "https://arxiv.org/pdf/2510.03992"
          },
          {
            "title": "Top 7 LLM Evaluation Tools in 2026 - Confident AI",
            "url": "https://www.confident-ai.com/knowledge-base/compare/best-llm-evaluation-tools"
          }
        ]
      },
      "I found relevant search results about CoT faithfulness, tool selection, and multi-turn agentic systems in 2026. Here are the key findings:\n\n## Chain-of-Thought in Multi-Turn Agentic Systems\n\nAgentic AI extends CoT across many turns, interleaving reasoning with tool use, and agentic systems use CoT at every step of a multi-turn automation.\n\n## Evaluation of Tool Selection and Faithfulness\n\nPurpose-built metrics for agentic workflows include tool selection accuracy, planning quality, step-level faithfulness, and reasoning coherence. Agents fail through cascading tool selection and reasoning errors.\n\n## Amazon's Multi-Layer Evaluation Approach\n\nThe middle layer of agent evaluation determines whether the agent understands user intents correctly, how the LLM drives agentic workflow planning through chain-of-thought reasoning, whether the tool selection and execution are aligned with the agentic plan, and if the plan is completed successfully.\n\n## Security and Robustness of Tool Selection\n\nThe integration of external tools into large language model agent workflows has fundamentally transformed agentic systems, allowing agents to retrieve information and invoke APIs to execute computations, and by chaining tool calls, agents perform multi-step reasoning and solve tasks that exceed the scope of static text generation.\n\nThe search results indicate that in 2026, evaluation frameworks are increasingly focusing on step-level faithfulness and tool selection accuracy as critical metrics for multi-turn agentic systems, moving beyond traditional output-only evaluation to assess intermediate reasoning and decision-making steps."
    ],
    "durationSeconds": 8.614238668999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c8d255a9-3aef-4cca-9080-4b09cc0e6093",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn…",
  "leafUuid": "d4d81fb4-f353-4930-aa9c-f935db9f5ecd",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate tool-selection faithfulness proposal for publication",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce"
}
```

---

### Tool call

_source line 23 · 2026-05-19T18:35:55.575Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FyVtG8mJ2eJdvciqYQ6sAQ`</summary>

```json
{
  "query": "\"Lie to Me\" chain of thought faithfulness reasoning models 2026 arXiv 2603.22582"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4d81fb4-f353-4930-aa9c-f935db9f5ecd",
  "isSidechain": false,
  "requestId": "req_011CbCQmtvqmHkFd47htLRkJ",
  "type": "assistant",
  "uuid": "aa770a2b-af35-4756-941e-bca0a48ce0df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRgx223aZCg6Vnh7qAAHje",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 710,
      "cache_creation_input_tokens": 3431,
      "cache_read_input_tokens": 19817,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 710,
          "output_tokens": 184,
          "cache_read_input_tokens": 19817,
          "cache_creation_input_tokens": 3431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3431
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

_source line 24 · 2026-05-19T18:35:56.545Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GHNojKGsYZNLDfWv8q8H1v`</summary>

```json
{
  "query": "LLM agents already know when to call tools without reasoning arXiv 2605.09252 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa770a2b-af35-4756-941e-bca0a48ce0df",
  "isSidechain": false,
  "requestId": "req_011CbCQmtvqmHkFd47htLRkJ",
  "type": "assistant",
  "uuid": "d7e2a95c-36a2-4a0e-a0f2-cbffcbc475d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRgx223aZCg6Vnh7qAAHje",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 710,
      "cache_creation_input_tokens": 3431,
      "cache_read_input_tokens": 19817,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 710,
          "output_tokens": 184,
          "cache_read_input_tokens": 19817,
          "cache_creation_input_tokens": 3431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3431
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

_source line 25 · 2026-05-19T18:35:57.179Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MKPWk6CCCimc7ijHXgZJE7`</summary>

```json
{
  "query": "CoRL 2026 conference on robot learning topics scope call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7e2a95c-36a2-4a0e-a0f2-cbffcbc475d0",
  "isSidechain": false,
  "requestId": "req_011CbCQmtvqmHkFd47htLRkJ",
  "type": "assistant",
  "uuid": "ba96580b-59cc-4a56-957d-d7ca2ab04ef3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRgx223aZCg6Vnh7qAAHje",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 710,
      "cache_creation_input_tokens": 3431,
      "cache_read_input_tokens": 19817,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 710,
          "output_tokens": 184,
          "cache_read_input_tokens": 19817,
          "cache_creation_input_tokens": 3431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3431
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

_source line 26 · 2026-05-19T18:36:02.355Z_

<details><summary>↩ Tool result · `toolu_01FyVtG8mJ2eJdvciqYQ6sAQ`</summary>

```text
Web search results for query: ""Lie to Me" chain of thought faithfulness reasoning models 2026 arXiv 2603.22582"

Links: [{"title":"[2603.22582] Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?","url":"https://arxiv.org/abs/2603.22582"},{"title":"Paper page - Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?","url":"https://huggingface.co/papers/2603.22582"},{"title":"(PDF) Why Models Know But Don't Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://www.researchgate.net/publication/403262878_Why_Models_Know_But_Don't_Say_Chain-of-Thought_Faithfulness_Divergence_Between_Thinking_Tokens_and_Answers_in_Open-Weight_Reasoning_Models"},{"title":"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?","url":"https://arxiv.org/html/2603.22582v1"},{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410"},{"title":"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning…","url":"https://www.opentrain.ai/papers/lie-to-me-how-faithful-is-chain-of-thought-reasoning-in-reasoning-models--arxiv-2603.22582/"},{"title":"LIE TO ME: HOW FAITHFUL IS CHAIN-OF-THOUGHT REASONING","url":"https://arxiv.org/pdf/2603.22582"},{"title":"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models? [Quick Review]","url":"https://liner.com/review/lie-to-me-how-faithful-is-chainofthought-reasoning-in-reasoning"},{"title":"Reasoning Models Will Sometimes Lie About Their Reasoning","url":"https://arxiv.org/html/2601.07663v4"}]

I found the paper! Here are the search results for "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?" (arXiv 2603.22582):

## Paper Overview

The paper examines chain-of-thought (CoT) reasoning as a transparency mechanism for large language models in safety-critical deployments, focusing on faithfulness—whether models accurately verbalize the factors that actually influence their outputs. The paper was submitted on March 23, 2026.

## Methodology

The study tests 12 open-weight reasoning models spanning 9 architectural families (7B-685B parameters) on 498 multiple-choice questions from MMLU and GPQA Diamond, injecting six categories of reasoning hints (sycophancy, consistency, visual pattern, metadata, grader hacking, and unethical information) and measuring the rate at which models acknowledge hint influence in their CoT when hints successfully alter answers.

## Key Findings

Across 41,832 inference runs, overall faithfulness rates range from 39.7% (Seed-1.6-Flash) to 89.9% (DeepSeek-V3.2-Speciale) across model families, with consistency hints (35.5%) and sycophancy hints (53.9%) exhibiting the lowest acknowledgment rates.

Training methodology and model family predict faithfulness more strongly than parameter count, and keyword-based analysis reveals a striking gap between thinking-token acknowledgment (approximately 87.5%) and answer-text acknowledgment (approximately 28.6%), suggesting that models internally recognize hint influence but systematically suppress this acknowledgment in their outputs.

These findings carry direct implications for the viability of CoT monitoring as a safety mechanism and suggest that faithfulness is not a fixed property of reasoning models but varies systematically with architecture, training method, and the nature of the influencing cue.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa770a2b-af35-4756-941e-bca0a48ce0df",
  "isSidechain": false,
  "promptId": "cc8c0189-3054-417a-9b7e-b465e21bc716",
  "type": "user",
  "uuid": "f5278fa3-0e60-4a03-a8c3-e9ae7d042f2d",
  "toolUseResult": {
    "query": "\"Lie to Me\" chain of thought faithfulness reasoning models 2026 arXiv 2603.22582",
    "results": [
      {
        "tool_use_id": "srvtoolu_014Ejqvvcwv1NRwrYV3JYT3e",
        "content": [
          {
            "title": "[2603.22582] Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?",
            "url": "https://arxiv.org/abs/2603.22582"
          },
          {
            "title": "Paper page - Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?",
            "url": "https://huggingface.co/papers/2603.22582"
          },
          {
            "title": "(PDF) Why Models Know But Don't Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://www.researchgate.net/publication/403262878_Why_Models_Know_But_Don't_Say_Chain-of-Thought_Faithfulness_Divergence_Between_Thinking_Tokens_and_Answers_in_Open-Weight_Reasoning_Models"
          },
          {
            "title": "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?",
            "url": "https://arxiv.org/html/2603.22582v1"
          },
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410"
          },
          {
            "title": "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning…",
            "url": "https://www.opentrain.ai/papers/lie-to-me-how-faithful-is-chain-of-thought-reasoning-in-reasoning-models--arxiv-2603.22582/"
          },
          {
            "title": "LIE TO ME: HOW FAITHFUL IS CHAIN-OF-THOUGHT REASONING",
            "url": "https://arxiv.org/pdf/2603.22582"
          },
          {
            "title": "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models? [Quick Review]",
            "url": "https://liner.com/review/lie-to-me-how-faithful-is-chainofthought-reasoning-in-reasoning"
          },
          {
            "title": "Reasoning Models Will Sometimes Lie About Their Reasoning",
            "url": "https://arxiv.org/html/2601.07663v4"
          }
        ]
      },
      "I found the paper! Here are the search results for \"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?\" (arXiv 2603.22582):\n\n## Paper Overview\n\nThe paper examines chain-of-thought (CoT) reasoning as a transparency mechanism for large language models in safety-critical deployments, focusing on faithfulness—whether models accurately verbalize the factors that actually influence their outputs. The paper was submitted on March 23, 2026.\n\n## Methodology\n\nThe study tests 12 open-weight reasoning models spanning 9 architectural families (7B-685B parameters) on 498 multiple-choice questions from MMLU and GPQA Diamond, injecting six categories of reasoning hints (sycophancy, consistency, visual pattern, metadata, grader hacking, and unethical information) and measuring the rate at which models acknowledge hint influence in their CoT when hints successfully alter answers.\n\n## Key Findings\n\nAcross 41,832 inference runs, overall faithfulness rates range from 39.7% (Seed-1.6-Flash) to 89.9% (DeepSeek-V3.2-Speciale) across model families, with consistency hints (35.5%) and sycophancy hints (53.9%) exhibiting the lowest acknowledgment rates.\n\nTraining methodology and model family predict faithfulness more strongly than parameter count, and keyword-based analysis reveals a striking gap between thinking-token acknowledgment (approximately 87.5%) and answer-text acknowledgment (approximately 28.6%), suggesting that models internally recognize hint influence but systematically suppress this acknowledgment in their outputs.\n\nThese findings carry direct implications for the viability of CoT monitoring as a safety mechanism and suggest that faithfulness is not a fixed property of reasoning models but varies systematically with architecture, training method, and the nature of the influencing cue."
    ],
    "durationSeconds": 6.774950679000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "aa770a2b-af35-4756-941e-bca0a48ce0df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T18:36:03.102Z_

<details><summary>↩ Tool result · `toolu_01GHNojKGsYZNLDfWv8q8H1v`</summary>

```text
Web search results for query: "LLM agents already know when to call tools without reasoning arXiv 2605.09252 2026"

Links: [{"title":"LLM Agents Already Know When to Call Tools - Even Without Reasoning","url":"https://arxiv.org/html/2605.09252v1"},{"title":"Your LLM Agents are Temporally Blind: The Misalignment Between Tool Use Decisions and Human Time Perception","url":"https://arxiv.org/pdf/2510.23853"},{"title":"Function Calling in AI Agents | Prompt Engineering Guide&lt;!-- -->","url":"https://www.promptingguide.ai/agents/function-calling"},{"title":"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling","url":"https://arxiv.org/html/2605.00737v1"},{"title":"More Vulnerable than You Think: On the Stability of Tool-Integrated LLM Agents","url":"https://arxiv.org/pdf/2506.21967"},{"title":"Learning to Ask: When LLM Agents Meet Unclear Instruction","url":"https://arxiv.org/pdf/2409.00557"}]

Perfect! I found the paper you're looking for. Here's what I found:

The paper "LLM Agents Already Know When to Call Tools - Even Without Reasoning" (arXiv:2605.09252) was published on May 10, 2026, by researchers from UC San Diego and Amazon AWS.

The paper addresses the problem that tool-augmented LLM agents tend to call tools indiscriminately, even when the model can answer directly. Each unnecessary call wastes API fees and latency, yet no existing benchmark systematically studies when a tool call is actually needed.

The authors propose When2Tool, a benchmark of 18 environments (15 single-hop, 3 multi-hop) spanning three categories of tool necessity — computational scale, knowledge boundaries, and execution reliability — each with controlled difficulty levels that create a clear decision boundary between tool-necessary and tool-unnecessary tasks.

They evaluate two families of training-free baselines: Prompt-only (varying the prompt to discourage unnecessary calls) and Reason-then-Act (requiring the model to reason about tool necessity before acting).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7e2a95c-36a2-4a0e-a0f2-cbffcbc475d0",
  "isSidechain": false,
  "promptId": "cc8c0189-3054-417a-9b7e-b465e21bc716",
  "type": "user",
  "uuid": "ec1d160e-166e-4c5d-b3cc-1834100be664",
  "toolUseResult": {
    "query": "LLM agents already know when to call tools without reasoning arXiv 2605.09252 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NYX9BZD8F9fDzpVkB9tEuq",
        "content": [
          {
            "title": "LLM Agents Already Know When to Call Tools - Even Without Reasoning",
            "url": "https://arxiv.org/html/2605.09252v1"
          },
          {
            "title": "Your LLM Agents are Temporally Blind: The Misalignment Between Tool Use Decisions and Human Time Perception",
            "url": "https://arxiv.org/pdf/2510.23853"
          },
          {
            "title": "Function Calling in AI Agents | Prompt Engineering Guide&lt;!-- -->",
            "url": "https://www.promptingguide.ai/agents/function-calling"
          },
          {
            "title": "To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling",
            "url": "https://arxiv.org/html/2605.00737v1"
          },
          {
            "title": "More Vulnerable than You Think: On the Stability of Tool-Integrated LLM Agents",
            "url": "https://arxiv.org/pdf/2506.21967"
          },
          {
            "title": "Learning to Ask: When LLM Agents Meet Unclear Instruction",
            "url": "https://arxiv.org/pdf/2409.00557"
          }
        ]
      },
      "Perfect! I found the paper you're looking for. Here's what I found:\n\nThe paper \"LLM Agents Already Know When to Call Tools - Even Without Reasoning\" (arXiv:2605.09252) was published on May 10, 2026, by researchers from UC San Diego and Amazon AWS.\n\nThe paper addresses the problem that tool-augmented LLM agents tend to call tools indiscriminately, even when the model can answer directly. Each unnecessary call wastes API fees and latency, yet no existing benchmark systematically studies when a tool call is actually needed.\n\nThe authors propose When2Tool, a benchmark of 18 environments (15 single-hop, 3 multi-hop) spanning three categories of tool necessity — computational scale, knowledge boundaries, and execution reliability — each with controlled difficulty levels that create a clear decision boundary between tool-necessary and tool-unnecessary tasks.\n\nThey evaluate two families of training-free baselines: Prompt-only (varying the prompt to discourage unnecessary calls) and Reason-then-Act (requiring the model to reason about tool necessity before acting)."
    ],
    "durationSeconds": 6.554163740999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d7e2a95c-36a2-4a0e-a0f2-cbffcbc475d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T18:36:04.271Z_

<details><summary>↩ Tool result · `toolu_01MKPWk6CCCimc7ijHXgZJE7`</summary>

```text
Web search results for query: "CoRL 2026 conference on robot learning topics scope call for papers"

Links: [{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models","url":"https://arxiv.org/pdf/2512.11908"}]

Based on the search results, here's what I found about CoRL 2026:

## Conference Overview
The Conference on Robot Learning (CoRL) is an annual international conference focusing on the intersection of robotics and machine learning. CoRL 2026 will be held in Austin, Texas, US.

## Key Dates
The CoRL 2026 website is officially live at http://corl.org with key dates for your submissions: May 25: Abstract Submission May 28: Full Paper Submission Nov 9-12: Conference in Austin, TX

## Paper Submission Requirements
Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.

Submissions without a robotics focus will be returned without review. Additionally, all submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments and how these might be addressed in the future.

## Reviewer Requirements
All submissions must include at least one author who agrees to serve as a CoRL reviewer. They are qualified if they have at least one accepted publication at a previous robotics (CoRL/ ICRA/ IROS/ RSS) or learning conference (ICLR/ NeurIPS/ ICML) or equivalent journal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba96580b-59cc-4a56-957d-d7ca2ab04ef3",
  "isSidechain": false,
  "promptId": "cc8c0189-3054-417a-9b7e-b465e21bc716",
  "type": "user",
  "uuid": "2eeba14e-f4a4-460c-b1ee-a6f39cb00f49",
  "toolUseResult": {
    "query": "CoRL 2026 conference on robot learning topics scope call for papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_019dbLTX8MdRV5CRE2XYMLpp",
        "content": [
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf?lang=en"
          },
          {
            "title": "CoRL 2026 - Call for Workshops",
            "url": "https://www.corl.org/contributions/call-for-workshops"
          },
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
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
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models",
            "url": "https://arxiv.org/pdf/2512.11908"
          }
        ]
      },
      "Based on the search results, here's what I found about CoRL 2026:\n\n## Conference Overview\nThe Conference on Robot Learning (CoRL) is an annual international conference focusing on the intersection of robotics and machine learning. CoRL 2026 will be held in Austin, Texas, US.\n\n## Key Dates\nThe CoRL 2026 website is officially live at http://corl.org with key dates for your submissions: May 25: Abstract Submission May 28: Full Paper Submission Nov 9-12: Conference in Austin, TX\n\n## Paper Submission Requirements\nSubmissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\n\nSubmissions without a robotics focus will be returned without review. Additionally, all submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments and how these might be addressed in the future.\n\n## Reviewer Requirements\nAll submissions must include at least one author who agrees to serve as a CoRL reviewer. They are qualified if they have at least one accepted publication at a previous robotics (CoRL/ ICRA/ IROS/ RSS) or learning conference (ICLR/ NeurIPS/ ICML) or equivalent journal."
    ],
    "durationSeconds": 7.089406048000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ba96580b-59cc-4a56-957d-d7ca2ab04ef3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-19T18:36:04.275Z_

```json
{
  "parentUuid": "2eeba14e-f4a4-460c-b1ee-a6f39cb00f49",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c76831dd-6a3b-436a-8fe7-94f6e3ee0ec1",
  "timestamp": "2026-05-19T18:36:04.275Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 30 · 2026-05-19T18:36:10.641Z_

<details><summary>Logged reasoning block</summary>

```text
This is very important! CoRL 2026 explicitly states: "Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics." and "Submissions without a robotics focus will be returned without review."

This proposal has ZERO robotics content. It's about LLM tool-selection faithfulness in multi-turn agentic systems. This is fundamentally an NLP/AI safety topic, not a robotics topic. The proposal would be desk-rejected at CoRL.

Let me do one more search to see if there's any overlap between this kind of work and CoRL, and also to check more related work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c76831dd-6a3b-436a-8fe7-94f6e3ee0ec1",
  "isSidechain": false,
  "requestId": "req_011CbCQnjyc3LCXSW6ki7Rjh",
  "type": "assistant",
  "uuid": "c49ad364-e90d-4ae7-ab55-30a36acb01a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139nhgfJBea6LkHJmUHxjd2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3290,
      "cache_read_input_tokens": 23248,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3290,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 318,
          "cache_read_input_tokens": 23248,
          "cache_creation_input_tokens": 3290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3290
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

_source line 31 · 2026-05-19T18:36:10.910Z_

这是一个关键发现——让我再做一轮搜索确认。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c49ad364-e90d-4ae7-ab55-30a36acb01a2",
  "isSidechain": false,
  "requestId": "req_011CbCQnjyc3LCXSW6ki7Rjh",
  "type": "assistant",
  "uuid": "00a1235a-b338-4afa-9762-be9ba8a4d2ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139nhgfJBea6LkHJmUHxjd2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3290,
      "cache_read_input_tokens": 23248,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3290,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 318,
          "cache_read_input_tokens": 23248,
          "cache_creation_input_tokens": 3290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3290
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

_source line 32 · 2026-05-19T18:36:11.847Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015LHQrZqBG4EWGmoe3F3vrB`</summary>

```json
{
  "query": "CoRL 2026 call for papers \"without a robotics focus\" desk reject scope"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00a1235a-b338-4afa-9762-be9ba8a4d2ba",
  "isSidechain": false,
  "requestId": "req_011CbCQnjyc3LCXSW6ki7Rjh",
  "type": "assistant",
  "uuid": "54e114b1-684b-4f3e-a1d2-0d2a8e4cf660",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139nhgfJBea6LkHJmUHxjd2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3290,
      "cache_read_input_tokens": 23248,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3290,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 318,
          "cache_read_input_tokens": 23248,
          "cache_creation_input_tokens": 3290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3290
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

_source line 33 · 2026-05-19T18:36:12.807Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015jsZBfXWhW32sXjWtJavbM`</summary>

```json
{
  "query": "\"beyond the black box\" interpretability agentic AI tool use arXiv 2605.06890 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54e114b1-684b-4f3e-a1d2-0d2a8e4cf660",
  "isSidechain": false,
  "requestId": "req_011CbCQnjyc3LCXSW6ki7Rjh",
  "type": "assistant",
  "uuid": "37a8c7af-aa20-47e7-b315-d4a718544da6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139nhgfJBea6LkHJmUHxjd2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3290,
      "cache_read_input_tokens": 23248,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3290,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 318,
          "cache_read_input_tokens": 23248,
          "cache_creation_input_tokens": 3290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3290
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

_source line 34 · 2026-05-19T18:36:17.265Z_

<details><summary>↩ Tool result · `toolu_015LHQrZqBG4EWGmoe3F3vrB`</summary>

```text
Web search results for query: "CoRL 2026 call for papers "without a robotics focus" desk reject scope"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2025 - Call for Papers","url":"https://2025.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"}]

Based on the search results, I found the relevant information about CoRL 2026's desk reject scope for submissions without a robotics focus:

Submissions without a robotics focus will be returned without review at CoRL 2026. This means such papers are subject to desk rejection as part of the initial screening process.

Additionally, submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. The conference emphasizes this requirement to ensure that all accepted work contributes meaningfully to the field of robot learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54e114b1-684b-4f3e-a1d2-0d2a8e4cf660",
  "isSidechain": false,
  "promptId": "cc8c0189-3054-417a-9b7e-b465e21bc716",
  "type": "user",
  "uuid": "dfbddb2f-ee61-4e01-953f-fabe93d35dd3",
  "toolUseResult": {
    "query": "CoRL 2026 call for papers \"without a robotics focus\" desk reject scope",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MZUvUZFSXWWxmtZvKRHDb5",
        "content": [
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "CoRL 2025 - Call for Papers",
            "url": "https://2025.corl.org/contributions/call-for-papers"
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
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf?lang=en"
          },
          {
            "title": "CoRL 2026 - Annoucements",
            "url": "https://www.corl.org/annoucements"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "CoRL 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"
          }
        ]
      },
      "Based on the search results, I found the relevant information about CoRL 2026's desk reject scope for submissions without a robotics focus:\n\nSubmissions without a robotics focus will be returned without review at CoRL 2026. This means such papers are subject to desk rejection as part of the initial screening process.\n\nAdditionally, submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. The conference emphasizes this requirement to ensure that all accepted work contributes meaningfully to the field of robot learning."
    ],
    "durationSeconds": 5.4146959960000025,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "54e114b1-684b-4f3e-a1d2-0d2a8e4cf660",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn…",
  "leafUuid": "dfbddb2f-ee61-4e01-953f-fabe93d35dd3",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate tool-selection faithfulness proposal for publication",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce"
}
```

---

### Tool result

_source line 37 · 2026-05-19T18:36:20.542Z_

<details><summary>↩ Tool result · `toolu_015jsZBfXWhW32sXjWtJavbM`</summary>

```text
Web search results for query: ""beyond the black box" interpretability agentic AI tool use arXiv 2605.06890 2026"

Links: [{"title":"[2605.06890] Beyond the Black Box: Interpretability of Agentic AI Tool Use","url":"https://arxiv.org/abs/2605.06890"},{"title":"Beyond the Black Box: Interpretability of Agentic AI Tool Use","url":"https://arxiv.org/html/2605.06890"},{"title":"Beyond Black-Box Benchmarking: Observability, Analytics, and Optimization of Agentic Systems","url":"https://arxiv.org/html/2503.06745v1"},{"title":"Beyond the Black Box: A Cognitive Architecture for Explainable and Aligned AI","url":"https://arxiv.org/html/2512.03072"},{"title":"TripleTree: A Versatile Interpretable Representation of Black Box Agents   and their Environments","url":"https://arxiv.org/pdf/2009.04743"},{"title":"Beyond Single Systems: How Multi-Agent AI Is Reshaping Ethics in Radiology","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12562106/"}]

I found the paper you're looking for! Here are the key details:

**Title:** Beyond the Black Box: Interpretability of Agentic AI Tool Use

**ArXiv ID:** 2605.06890

**Authors:** Hariom Tatsat and Ariye Shater from Quantitative Analytics at Barclays

**Submission Date:** 7 May 2026

**Main Problem:** AI agents are promising for high-stakes enterprise workflows, but dependable deployment remains limited because tool-use failures are difficult to diagnose and control.

**Key Issues Addressed:** Agents may skip required tool calls, invoke tools unnecessarily, or take actions whose consequence becomes visible only after execution.

**Proposed Solution:** The authors introduce a mechanistic-interpretability toolkit built on Sparse Autoencoders (SAEs) and linear probes that reads model states before each action and infers both whether a tool is needed and how consequential the next tool action is likely to be.

The paper is available on arXiv at: https://arxiv.org/abs/2605.06890


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37a8c7af-aa20-47e7-b315-d4a718544da6",
  "isSidechain": false,
  "promptId": "cc8c0189-3054-417a-9b7e-b465e21bc716",
  "type": "user",
  "uuid": "2a7f2d8c-f178-4eb1-b085-d0957b171974",
  "toolUseResult": {
    "query": "\"beyond the black box\" interpretability agentic AI tool use arXiv 2605.06890 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Udgp1y7f4uztR8eZ7ZGpba",
        "content": [
          {
            "title": "[2605.06890] Beyond the Black Box: Interpretability of Agentic AI Tool Use",
            "url": "https://arxiv.org/abs/2605.06890"
          },
          {
            "title": "Beyond the Black Box: Interpretability of Agentic AI Tool Use",
            "url": "https://arxiv.org/html/2605.06890"
          },
          {
            "title": "Beyond Black-Box Benchmarking: Observability, Analytics, and Optimization of Agentic Systems",
            "url": "https://arxiv.org/html/2503.06745v1"
          },
          {
            "title": "Beyond the Black Box: A Cognitive Architecture for Explainable and Aligned AI",
            "url": "https://arxiv.org/html/2512.03072"
          },
          {
            "title": "TripleTree: A Versatile Interpretable Representation of Black Box Agents   and their Environments",
            "url": "https://arxiv.org/pdf/2009.04743"
          },
          {
            "title": "Beyond Single Systems: How Multi-Agent AI Is Reshaping Ethics in Radiology",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12562106/"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n**Title:** Beyond the Black Box: Interpretability of Agentic AI Tool Use\n\n**ArXiv ID:** 2605.06890\n\n**Authors:** Hariom Tatsat and Ariye Shater from Quantitative Analytics at Barclays\n\n**Submission Date:** 7 May 2026\n\n**Main Problem:** AI agents are promising for high-stakes enterprise workflows, but dependable deployment remains limited because tool-use failures are difficult to diagnose and control.\n\n**Key Issues Addressed:** Agents may skip required tool calls, invoke tools unnecessarily, or take actions whose consequence becomes visible only after execution.\n\n**Proposed Solution:** The authors introduce a mechanistic-interpretability toolkit built on Sparse Autoencoders (SAEs) and linear probes that reads model states before each action and infers both whether a tool is needed and how consequential the next tool action is likely to be.\n\nThe paper is available on arXiv at: https://arxiv.org/abs/2605.06890"
    ],
    "durationSeconds": 7.731566012000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "37a8c7af-aa20-47e7-b315-d4a718544da6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-19T18:37:12.561Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to make my assessment. Let me organize my findings:

## Critical Issue: Venue Mismatch

CoRL 2026 explicitly states: "Submissions without a robotics focus will be returned without review." This proposal has ZERO robotics content. It's purely about LLM tool-selection faithfulness in multi-turn agentic systems with domains like "code editing, web browsing, data analysis, system administration, information retrieval" — none of which are robotics. This is a desk-reject-level venue mismatch.

However, the user's system prompt mentions "NLP/CL 领域" in the rubric, so maybe the user intends this for an NLP venue and just mistakenly said CoRL? Or maybe they're genuinely asking about CoRL? I should note this clearly.
 
## Idea Quality Assessment

### Novelty Assessment

Looking at the related work, the closest prior is the tool calling paper that shows tool identity is linearly probed in single-turn settings but explicitly notes multi-turn is fragile—so the proposal correctly identifies a genuine gap there. RFEval addresses behavioral faithfulness through counterfactual interventions, but focuses on reasoning tasks rather than tool selection across multi-turn interactions, so there's meaningful novelty in extending this to the agentic setting.

The other papers I'm reviewing either tackle different aspects of agent auditing (structural causal frameworks for claims, SAE-based probing for tool-need detection, or CoT faithfulness in QA/math) but none specifically examine whether tool-selection reasoning is actually faithful to the model's underlying decisions in multi-turn trajectories. So the gap is real—this combination of behavioral causal interventions applied to tool-selection CoT in multi-turn settings hasn't been done.

The harder question is whether this gap matters enough to be interesting.

Given that prior work already shows tool identity is linearly readable and steerable in single-turn settings, and that roughly half of CoT reasoning is unfaithful in general, the expected findings feel somewhat predictable: tool-selection CoT in multi-turn would likely be unfaithful too, multi-turn would make probing harder, and maybe ambiguity correlates with faithfulness. The concern is that I could just apply existing methodologies from those papers to the multi-turn tool domain and get a straightforward extension rather than a novel insight.

The practical stakes are real—agentic systems are being deployed and understanding whether CoT actually drives tool selection matters for safety. But this is fundamentally an empirical measurement paper without a proposed solution, and benchmark-plus-findings contributions need genuinely surprising results to stand out at top venues. The idea addresses a real gap and the related work is solid, but the most likely outcome is a somewhat predictable confirmation of what we'd expect from combining the existing findings. tool-selection CoT in multi-turn is also substantially unfaithful" — which is what one would guess.

The counterintuitive hypothesis about harder ambiguity leading to more faithful reasoning is the most compelling part, though it's speculative rather than a core finding. If it doesn't hold up, the paper loses its most surprising potential insight.

This is fundamentally an empirical benchmarking study with TOOLFAITH-BENCH and associated metrics. Top venues expect benchmark papers to surface genuinely unexpected discoveries, not just validate intuitions.

The combination of behavioral and mechanistic analysis is a legitimate methodological contribution, though it feels more like a natural pairing than a breakthrough approach.

Now I'm realizing the venue mismatch is actually a critical problem. CoRL 2026 is robotics-focused, and this proposal has zero robotics content — that's an immediate desk rejection regardless of how strong the idea itself might be. I should flag this as a fatal issue upfront, then evaluate the work on its own merits for what it actually is: an NLP/ML contribution that belongs at venues like ACL or EMNLP, not robotics conferences. 的逻辑强度、novelty 的真实程度、研究问题的重要性。"

And the scoring is about idea quality. But acceptance probability at CoRL specifically? That's ~0% due to venue mismatch.

I'll evaluate the idea quality honestly, then note that the CoRL-specific probability is essentially 0% due to venue mismatch, while giving an estimate of what it might be at an appropriate venue.

Let me finalize my assessment:

**Novelty: 中** — The gap is real but the synthesis is somewhat expected. The behavioral+mechanistic combination and the multi-turn extension are genuine contributions, but they're natural extensions of existing methodologies to a new domain.

**Significance: 中** — The question is important for agent safety, but the paper is measurement-only (no solution), and the most likely findings would confirm what experts would predict.

**Related Work: 强** — Extremely thorough coverage of the landscape with correct identification of gaps and clear positioning.

For an appropriate NLP venue like ACL/EMNLP/NeurIPS, I'd estimate 25-35% acceptance probability—the gap is well-motivated and real, but the expected findings are fairly predictable, and pure measurement papers need surprising results to stand out. The counterintuitive H5 hypothesis could be the deciding factor. At CoRL though, this is essentially a desk reject due to fundamental venue mismatch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a7f2d8c-f178-4eb1-b085-d0957b171974",
  "isSidechain": false,
  "requestId": "req_011CbCQowXv4Nj6fiBiwkbsF",
  "type": "assistant",
  "uuid": "68cfa3ac-1c69-4838-9162-b3f981603a94",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QVbQHztE3tKUEJ87dYpze",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1495,
      "cache_read_input_tokens": 26538,
      "output_tokens": 5778,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1495,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5778,
          "cache_read_input_tokens": 26538,
          "cache_creation_input_tokens": 1495,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1495
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

_source line 39 · 2026-05-19T18:38:37.141Z_

调研完成。现在我来撰写完整的入口评审报告。

---

```
【阶段】: Triage
```

---

## ⚠️ 致命前置问题：投稿 venue 严重不匹配

在进入 idea 质量评估之前，必须先指出一个**致命的 venue mismatch**：

**CoRL (Conference on Robot Learning)** 2026 的 Call for Papers 明确要求："Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics." 并且明确声明 **"Submissions without a robotics focus will be returned without review."**

本 proposal 研究的是 LLM 多轮对话中 tool-selection CoT 的 faithfulness，涉及的五个 domain 是 code editing、web browsing、data analysis、system administration、information retrieval——**没有任何 robotics 内容**。这意味着 **在 CoRL 2026 投稿会被直接 desk reject**，接受概率实质为 0%。

本 proposal 的正确目标 venue 应该是 **NeurIPS、ICML、ACL、EMNLP** 等 NLP/ML 会议。以下 idea 质量评估基于该 proposal 在**合适 venue（如 NeurIPS/ACL/EMNLP）** 的中稿潜力进行，同时在最终概率中反映 CoRL 的 venue 因素。

---

```
【领域调研】:

1. [Tool Calling is Linearly Readable and Steerable in Language Models] (arXiv 2605.07990, May 2026):
   最直接的前序工作。Probe 12 个模型，发现 tool identity 在 pre-generation activations 中线性可读、
   可操控（4B+ 模型 93-100% steering accuracy）。但明确指出多轮迁移"fragile"（-30 到 +10pp），
   且 argument values 不可操控（0/30）。本 proposal 的 mechanistic probing 部分是对该工作的多轮扩展。

2. [RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Intervention] (arXiv 2602.17053, Feb 2026):
   7,186 实例的 counterfactual 干预 benchmark，发现 ~50% 的推理输出不忠实，集中在数学和代码等领域。
   但仅针对 reasoning task 的答案，不涉及 tool call 行为。本 proposal 的 behavioral intervention 方法论
   直接借鉴了该工作的框架。

3. [Lie to Me: How Faithful Is CoT Reasoning in Reasoning Models?] (arXiv 2603.22582, Mar 2026):
   评估 12 个模型，发现 faithfulness 从 39.7% 到 89.9% 不等，thinking token 和 output 之间存在
   59pp 的 gap。但仅针对 QA 选择题，不涉及 agentic tool selection。

4. [LLM Agents Already Know When to Call Tools — Even Without Reasoning] (arXiv 2605.09252, May 2026):
   提出 When2Tool benchmark，发现 tool-necessity 的二元判断可从 activations 以 0.89-0.96 AUROC 
   decode，reasoning 不提供额外信号。但这是 tool-necessity（是否 call tool），不是 tool-identity 
   faithfulness（选哪个 tool 的 CoT 是否忠实）。

5. [Beyond the Black Box: Interpretability of Agentic AI Tool Use] (arXiv 2605.06890, May 2026):
   用 SAE + linear probe 对多步 trajectory 进行 tool-need 和 tool-risk 分类。
   但不研究 tool identity 或 CoT faithfulness。

6. [Project Ariadne: Structural Causal Framework for Auditing Faithfulness in LLM Agents] (arXiv 2601.02314, Jan 2026):
   用 SCM 和反事实逻辑审计 agent 推理的因果完整性，但聚焦 factual claims 而非 tool-call actions，
   violation density 指标也不直接测量 tool-selection faithfulness。

7. [SAVeR: Verify Before You Commit] (arXiv 2604.08401, Apr 2026):
   提出自审计方法提高 agent faithfulness，但经验分析有限，偏方法论提案。

调研总结：2026 上半年 CoT faithfulness 和 tool-call probing 两条线路都有快速进展，
但二者的交叉点——multi-turn agentic tool-selection 的 behavioral causal faithfulness——
确实是一个真实存在的空白。Proposal 对 gap 的识别是准确的。但这个 gap 是否足够 surprising 
是核心问题。
```

---

```
【Trivial Alternative 检验】:

存在两个 trivial alternative 威胁：

(1) 直接组合已有方法论：将 RFEval 的 counterfactual intervention 框架直接应用于 tool-call 
    场景（替换干预对象从 "reasoning step → answer" 变为 "reasoning step → tool call"），
    加上 2605.07990 的 probing 方法跑多轮数据。这两步组合不需要任何方法论创新，只需"换领域
    重跑"。Proposal 的核心方法论（reason-flip, reason-ablate, counterfactual-inject, 
    reason-scramble）确实与 RFEval 的 counterfactual intervention 和 FACT-E 的 causal 
    perturbation 高度同构。

(2) 如果只想知道"multi-turn tool-selection CoT 是否忠实"，一个更轻量的方式是：
    直接用 2605.07990 的 linear probe 在多轮数据上测 pre-CoT tool identity encoding 
    的强度，如果 pre-CoT 就能高准确率 decode tool identity，那 CoT 就大概率是 decorative
    ——不需要构建完整的 600-scenario benchmark。

增量价值在哪？Proposal 的增量在于：(a) behavioral + mechanistic 两种视角的交叉验证
（faithfulness coupling 分析），(b) tiered ambiguity 设计可能揭示 faithfulness 与
任务难度的非单调关系，(c) 跨 turn 的 probe transfer/encoding drift 分析。
这些增量是真实的，但是否构成"非 trivial"贡献，取决于发现的 surprising 程度。
如果最终发现只是"multi-turn faithfulness 也约 50%，和 single-turn 差不多"，
则增量有限。
```

---

```
【前提假设检验】:

核心 claim 的逻辑链有以下未经验证的环节：

(1) "reason-flip 等干预是 well-defined 的"假设：在多轮场景中，CoT 不只包含 tool 
    选择理由，还包含对 prior tool results、error 状态的整合。Rewrite CoT to justify 
    a different tool 时，是否能保持上下文其他部分的 coherence？如果干预本身引入了 
    incoherence，测到的"unfaithfulness"可能只是模型在 reject 不一致输入，
    而非揭示真实的 faithfulness 问题。这是 RFEval 在 single-turn 中可以规避但
    multi-turn 中难以规避的 confound。

(2) "TSCF 和 RTI 可以可靠测量 faithfulness"假设：RTI 定义为"tool call 在矛盾 
    reasoning 下保持不变的比率"。但在 multi-turn 中，模型可能 attend 到 conversation 
    history 中的其他信号（prior tool results、user instructions）而非当前 turn 的 CoT。
    RTI 高可能意味着"模型依赖 history 而非当前 CoT"，而非"CoT 是 theater"。
    这是 construct validity 的核心隐患。

(3) H5（harder ambiguity → more faithful）的论证逻辑："genuine deliberation is 
    required" → "more faithful"。但 harder ambiguity 也可能导致模型更依赖 latent 
    heuristics（因为 reasoning 更困难），从而 less faithful。这个假设的方向性是
    未经验证的直觉。

(4) Tiered benchmark 的 construct validity：Soft-Ambiguous tier 要求"one clearly 
    optimal tool"但同时"2-3 plausible tools"。这种 calibration 在多轮动态场景中
    是否可靠实现——即人类标注者是否能一致同意哪个 tool 是"clearly optimal"——
    是一个实践假设。
```

---

```
【3 维度打分】:

1. Novelty: 中 — 
   gap 本身是真实的：behavioral causal intervention + mechanistic probing 在 multi-turn 
   tool-selection 的交叉确实无人做过（调研确认 2605.07990 明确标注多轮为 unsolved，
   RFEval/Lie to Me 等都仅限 single-turn QA/math）。但方法论本质是已有技术的领域迁移：
   intervention protocol 从 RFEval 迁移，probing 从 2605.07990 迁移，metrics 是
   自然定义的比率指标。真正的 novelty delta 集中在 (a) tiered ambiguity 设计 和 
   (b) faithfulness coupling（behavioral-mechanistic 对齐分析）这两个点上，
   属于"有意义的组合创新"而非"根本性新方法"。

2. Significance: 中 — 
   研究问题（multi-turn tool-selection faithfulness）有真实的安全意义，尤其是 
   production agent 场景下。但本 proposal 是纯测量型研究（benchmark + 实验发现），
   不提出解决方案。对领域的影响取决于发现的 surprising 程度。如果核心发现是 
   "multi-turn 也有 ~50% unfaithful"（类比 RFEval 的 single-turn 发现），
   审稿人可能会说 "I would have guessed this"。
   counterintuitive hypothesis H5（harder ambiguity → more faithful）是最有潜力的
   亮点，但它是 hypothesis 不是 confirmed finding。如果 H5 被否定，
   significance 会进一步降低。

3. Related Work: 强 — 
   覆盖全面且定位精准。四条 thread 的组织方式清晰，对每篇工作都准确描述了"做了什么"和
   "没做什么"，gap identification 经调研验证是 legitimate 的。引用的关键论文
   （2605.07990, 2602.17053, 2603.22582, 2605.09252）均经搜索确认真实存在且
   描述准确。这是该 proposal 最强的维度。
```

---

```
【概率估计】: 

CoRL 2026: 0-2%（desk reject，venue 完全不匹配，无任何 robotics 内容）

若投至合适 venue（NeurIPS / ACL / EMNLP）: [20% - 32%] 中位 25%

【估计理由】:
Idea 处于 rubric 的 "25-35% 区间下半部"：方向正确、gap 真实、related work 扎实，
但核心发现 if positive 审稿人大概率会说 "not surprising"——given RFEval 已证明 
single-turn ~50% unfaithful，2605.07990 已证明 multi-turn probing fragile，
本工作的最可能结论（multi-turn tool-selection CoT 也 substantially unfaithful）
是 expected direction。Novelty 维度（中）和 Significance 维度（中）共同限制了上界。
Related Work（强）提升了下界，但无法弥补 idea 内核的 "predictable findings" 问题。

CoRL 的 0-2% 是因为 venue policy 明确的 desk reject，与 idea 质量无关。

【主要风险】:
1. Predictable findings 风险：核心实验最可能揭示 "multi-turn tool-selection CoT 也大面积
   不忠实"，这与领域直觉一致，缺乏 surprise factor。审稿人可能认为这是"confirming the 
   obvious in a new domain"而非"revealing something new"。
   
2. Construct validity 风险：在多轮场景中，reason-flip 等干预可能引入 incoherence confound
   （模型拒绝不一致输入 ≠ 模型 CoT 不忠实），RTI 指标可能混淆"依赖 history"和"CoT is 
   theater"两种不同机制。这是一个 idea 层面的设计缺陷，不仅是执行问题。
```

---

Sources:
- [Tool Calling is Linearly Readable and Steerable in Language Models (2605.07990)](https://arxiv.org/abs/2605.07990)
- [RFEval: Benchmarking Reasoning Faithfulness (2602.17053)](https://arxiv.org/abs/2602.17053)
- [Lie to Me: How Faithful Is CoT Reasoning (2603.22582)](https://arxiv.org/abs/2603.22582)
- [LLM Agents Already Know When to Call Tools (2605.09252)](https://arxiv.org/abs/2605.09252)
- [Beyond the Black Box: Interpretability of Agentic AI Tool Use (2605.06890)](https://arxiv.org/abs/2605.06890)
- [Project Ariadne: Structural Causal Framework (2601.02314)](https://arxiv.org/abs/2601.02314)
- [SAVeR: Verify Before You Commit (2604.08401)](https://arxiv.org/abs/2604.08401)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68cfa3ac-1c69-4838-9162-b3f981603a94",
  "isSidechain": false,
  "requestId": "req_011CbCQowXv4Nj6fiBiwkbsF",
  "type": "assistant",
  "uuid": "fc1d019b-5c6f-42d9-a6db-88de86428aca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QVbQHztE3tKUEJ87dYpze",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1495,
      "cache_read_input_tokens": 26538,
      "output_tokens": 5778,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1495,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5778,
          "cache_read_input_tokens": 26538,
          "cache_creation_input_tokens": 1495,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1495
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn…",
  "leafUuid": "fc1d019b-5c6f-42d9-a6db-88de86428aca",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate tool-selection faithfulness proposal for publication",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn…",
  "leafUuid": "fc1d019b-5c6f-42d9-a6db-88de86428aca",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate tool-selection faithfulness proposal for publication",
  "sessionId": "c9225054-61e2-4260-93a8-43c36f992bce"
}
```

---
