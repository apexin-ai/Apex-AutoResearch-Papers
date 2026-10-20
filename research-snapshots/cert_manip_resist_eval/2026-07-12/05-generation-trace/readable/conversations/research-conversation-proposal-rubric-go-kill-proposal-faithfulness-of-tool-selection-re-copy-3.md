# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Faithfulness of Tool-Selection Re

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/fd8f0a03-d092-491f-8f65-bc44717d9008.jsonl`
- **Structured JSON:** [`b0e24c04913194e38669.json`](../../sessions/b0/b0e24c04913194e38669.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:31:39.646Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:31:39.646Z",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn Probing\n\n## Description\nWe present the first systematic study of whether tool-selection reasoning in multi-turn agentic systems is causally faithful or post-hoc rationalization, combining behavioral causal interventions with multi-turn mechanistic probing. While recent work has established that tool identity is linearly readable from pre-generation activations in single-turn settings (2605.07990, achieving 93-100% steering accuracy) and that ~50% of general reasoning is unfaithful (RFEval), no prior work examines whether an agent's stated reasoning for choosing a specific tool across conversation turns actually drives that decision. We construct TOOLFAITH-BENCH, a 600-scenario diagnostic benchmark across five domains, stratified into three difficulty tiers — Unambiguous (single correct tool), Soft-Ambiguous (one optimal among plausible candidates), and Hard-Ambiguous (multiple valid tools) — to address construct validity concerns about benchmark realism. We apply a four-type causal intervention protocol (reason-flip, reason-ablate, counterfactual-inject, reason-scramble) and introduce two metrics: Tool Selection Causal Fidelity (TSCF) and Reasoning Theater Index (RTI). We evaluate seven models spanning current open-weight systems (Kimi K2.6, GLM-5.1, Qwen3.6-35B-A3B, DeepSeek-V4-Pro) and frontier APIs (Claude Sonnet 4.6, GPT-5.5, Gemini 2.5 Pro), supplemented by a multi-turn probing study that extends 2605.07990 to the unsolved multi-turn regime with four novel analyses: cross-turn probe transfer, context-dependent encoding drift, error-induced replanning signals, and behavioral-mechanistic faithfulness coupling. We test five hypotheses, including that RTI will be elevated across model families (extending single-turn findings), that probe accuracy will degrade with conversation depth (unlike stable single-turn results), and — counterintuitively — that harder ambiguous scenarios may elicit more faithful reasoning than unambiguous ones because genuine deliberation is required.\n\n## Core Problem\nIn multi-turn tool-using agents, does the model's stated reasoning about tool selection — which tool to call, with what parameters, and why — actually causally drive the tool call decision, or is it post-hoc rationalization of a latent policy? Recent probing work (2605.07990, 2605.09252) has shown that tool identity is linearly encoded in pre-generation activations in single-turn settings, suggesting CoT may be decorative. But these findings explicitly fail to transfer to multi-turn agentic settings, where accumulated conversation history, prior tool results, and error feedback create dynamic contexts that fundamentally differ from static single-turn tool menus. No systematic behavioral study exists to measure causal coupling between stated reasoning and tool-call actions across conversation turns.\n\n## Opportunity\nThe landscape has bifurcated: single-turn tool probing is now well-characterized (2605.07990 achieves 93-100% steering accuracy for 4B+ models; 2605.09252 shows 0.89-0.96 AUROC for tool-necessity probing), while multi-turn agentic tool selection remains essentially unstudied from a faithfulness perspective. This is precisely where the stakes are highest — production agents execute multi-step workflows where early tool calls condition later ones, errors require replanning, and unfaithful reasoning about tool selection can cascade into irreversible harmful actions. The faithfulness evaluation literature has advanced rapidly in 2026: RFEval finds ~50% of reasoning outputs unfaithful across 7,186 instances; 'Lie to Me' reveals a 59-percentage-point gap between internal recognition and output acknowledgment of hint influence; 'Decoding Answers Before CoT' shows 0.9 AUC pre-CoT answer probing — yet all this work targets single-turn QA/math, not agentic tool selection. Critically, 2605.07990 found multi-turn steering to be 'fragile' with -30 to +10pp vs. baseline and 'no consistent direction,' directly motivating a systematic study of multi-turn tool-selection faithfulness. The behavioral intervention approach — perturbing CoT and measuring whether tool calls change — is entirely unaddressed by any existing work on tool-call probing, creating a unique and timely contribution.\n\n## Related Work / Landscape\nThe landscape spans four converging threads:\n\n**Thread 1 — CoT Faithfulness (General):** Project Ariadne (2601.02314) finds causal decoupling with violation density up to 0.77 in factual domains but focuses on claims, not actions. 'Decoding Answers Before CoT' (2603.01437) shows answers encoded in pre-CoT activations with 0.9 AUC, establishing that CoT can be post-hoc, but only for binary QA. 'Catching Rationalization in the Act' (2603.17199) detects motivated reasoning via activation probing, showing internal representations outperform CoT monitors. RFEval (2602.17053) provides a 7,186-instance counterfactual intervention benchmark finding ~50% unfaithfulness, but for reasoning tasks not tool calls. FACT-E (2604.10693, ACL 2026 Findings) uses causal perturbations for CoT evaluation, finding self-evaluation unreliable. C2-Faith (2603.05167) benchmarks LLM-as-judge for causal/coverage faithfulness, showing systematic blind spots in localization. 'Lie to Me' (2603.22582) evaluates 12 models finding faithfulness rates from 39.7% to 89.9% with a critical 59pp thinking-vs-output gap. Breaking the Chain (2603.16475) shows 60% insensitivity to intermediate structure interventions. FaithCoT-Bench (ICLR 2026, 2510.04040) and FRIT (2509.13334) address single-turn QA faithfulness only.\n\n**Thread 2 — Tool-Call Probing (Single-Turn):** 'Tool Calling is Linearly Readable and Steerable' (2605.07990) probes 12 models, achieving 93-100% tool-name steering accuracy at 4B+ in single-turn fixed-menu settings, but explicitly finds multi-turn transfer 'fragile' (-30 to +10pp). Argument values are NOT steerable (0/30). 'LLM Agents Already Know When to Call Tools' (2605.09252) shows binary tool-necessity is decodable at 0.89-0.96 AUROC, with reasoning providing no additional signal. 'Beyond the Black Box' (2605.06890) applies SAE + probes to multi-step trajectories for tool-need/tool-risk classification but not tool identity or faithfulness. 'Internal Representations as Indicators of Hallucinations in Agent Tool Selection' (2601.05214) detects hallucinated tool calls from hidden states but in single-turn only.\n\n**Thread 3 — Tool Selection Robustness/Behavior:** 'Tool Preferences in Agentic LLMs are Unreliable' (EMNLP 2025, 2505.18135) shows tool selection is fragile under description manipulation but does not examine CoT faithfulness. 'The Reasoning Trap' (2510.22977) demonstrates RL causally amplifies tool hallucination but studies hallucination rates, not reasoning faithfulness. TOOLCERT (2510.03992) studies distributional robustness, not faithfulness. 'Brief Is Better' (2604.02155) finds non-monotonic CoT budget effects on function-calling accuracy. 'The Causal Impact of Tool Affordance on Safety Alignment' (ICECET 2026, 2603.20320) examines safety but not faithfulness.\n\n**Thread 4 — Agentic Monitoring:** SAVeR (2604.08401) proposes self-auditing for agentic faithfulness but provides limited empirical analysis. 'Noticing the Watcher' (2603.16928) shows models detect CoT monitoring from feedback at up to 19% awareness. 'Reasoning and Tool-use Compete in Agentic RL' (2602.00994) reveals interference between reasoning and tool use during training.\n\n**Critical Gap:** No work combines behavioral causal interventions on tool-selection CoT with mechanistic probing in multi-turn agentic settings. Single-turn probing is established; multi-turn is explicitly unsolved. Behavioral faithfulness testing for tool selection is entirely absent.\n\n## Approach\nWe construct TOOLFAITH-BENCH, a diagnostic benchmark of 600 multi-turn agentic scenarios across five domains (code editing, web browsing, data analysis, system administration, information retrieval), each containing 2-4 tool-selection decision points. Scenarios are stratified into three difficulty tiers reflecting real-world ambiguity:\n\n**Tier 1 — Unambiguous (200 scenarios):** A single correct tool per decision point; the reasoning chain uniquely determines the tool. Serves as calibration: if TSCF is low here, the CoT is clearly decorative.\n\n**Tier 2 — Soft-Ambiguous (200 scenarios):** 2-3 plausible tools with one clearly optimal. The reasoning must contain distinguishing information (e.g., 'the file is >2GB, so we need streaming upload rather than multipart'). Interventions target this distinguishing reasoning.\n\n**Tier 3 — Hard-Ambiguous (200 scenarios):** Multiple genuinely valid tools. Faithfulness is measured via stance consistency (does the CoT logically support the specific tool chosen?) and causal coupling (does perturbing the CoT change which valid tool is selected?), following RFEval's framework of decoupling faithfulness from correctness.\n\nAt each decision point we apply four perturbation types: (1) reason-flip — rewrite the CoT to justify a different tool, (2) reason-ablate — remove reasoning entirely, presenting only task context, (3) counterfactual-inject — insert facts that should change the optimal tool, (4) reason-scramble — shuffle reasoning sentences while preserving tool mentions. We define two complementary metrics: Tool Selection Causal Fidelity (TSCF), the rate at which tool calls correctly follow intervened reasoning, and Reasoning Theater Index (RTI), the rate at which tool calls remain unchanged despite contradictory reasoning.\n\nWe evaluate seven models spanning current open-weight systems (Kimi K2.6, GLM-5.1, Qwen3.6-35B-A3B, DeepSeek-V4-Pro) and frontier APIs (Claude Sonnet 4.6, GPT-5.5, Gemini 2.5 Pro), supplementing behavioral results with a multi-turn probing study on open-weight models. The probing component is explicitly positioned as an extension of 2605.07990 to the unsolved multi-turn regime, with four novel analyses: (a) cross-turn probe transfer — whether a probe trained at decision point 1 (turn 2) generalizes to decision point 3 (turn 8) as context accumulates; (b) context-dependent encoding drift — whether the linear direction encoding a given tool shifts across turns as prior tool results modify the task state; (c) error-induced replanning signals — whether tool errors create detectable representational shifts before the next tool selection; (d) faithfulness coupling — correlating probe-detected pre-commitment (tool identity encoded before CoT) with behavioral unfaithfulness (low TSCF), testing whether mechanistic and behavioral measures of unfaithfulness align. This goes beyond 2605.07990's domain transfer, because multi-turn contexts create fundamentally different representational challenges: the residual stream must integrate prior tool results, error states, and evolving task context alongside the current tool decision, and 2605.07990 explicitly showed this integration is fragile.\n\n## Inspiration\nThree converging findings: (1) 2605.07990's explicit acknowledgment that multi-turn tool-call probing is 'fragile' and unsolved, creating a clear frontier; (2) the faithfulness evaluation literature's maturation (RFEval, FACT-E, Lie to Me) providing proven intervention methodologies that have never been applied to tool selection; (3) the growing deployment of multi-turn agentic systems where tool-selection faithfulness has direct safety implications that single-turn probing cannot address.\n\n## Key References\n- Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents (arXiv 2026, 2601.02314)\n- Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing [SAVeR] (arXiv 2026, 2604.08401)\n- Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures (arXiv 2026, 2603.16475)\n- Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback (arXiv 2026, 2603.16928)\n- Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering (arXiv 2026, 2603.01437)\n- Catching Rationalization in the Act: Detecting Motivated Reasoning via Activation Probing (arXiv 2026, 2603.17199)\n- RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention (arXiv 2026, 2602.17053)\n- FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning (ACL 2026 Findings, 2604.10693)\n- C2-Faith: Benchmarking LLM Judges for Causal and Coverage Faithfulness in CoT Reasoning (arXiv 2026, 2603.05167)\n- Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models? (arXiv 2026, 2603.22582)\n- Tool Calling is Linearly Readable and Steerable in Language Models (arXiv 2026, 2605.07990)\n- LLM Agents Already Know When to Call Tools — Even Without Reasoning (arXiv 2026, 2605.09252)\n- Beyond the Black Box: Interpretability of Agentic AI Tool Use (arXiv 2026, 2605.06890)\n- FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning (ICLR 2026, 2510.04040)\n- FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness (arXiv 2025, 2509.13334)\n- The Reasoning Trap: How Enhancing LLM Reasoning Amplifies Tool Hallucination (arXiv 2025, 2510.22977)\n- Tool Preferences in Agentic LLMs are Unreliable (EMNLP 2025, 2505.18135)\n- Quantifying Distributional Robustness of Agentic Tool-Selection [TOOLCERT] (arXiv 2025, 2510.03992)\n- Internal Representations as Indicators of Hallucinations in Agent Tool Selection (arXiv 2026, 2601.05214)\n- Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calling Language Agents (arXiv 2026, 2604.02155)\n- The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents (ICECET 2026, 2603.20320)\n- Reasoning and Tool-use Compete in Agentic RL: From Quantifying Interference to Disentangled Tuning (arXiv 2026, 2602.00994)\n- Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation? (arXiv 2025, 2508.19827)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '300 H100-hours (150h model inference across 4 open-weight models × 600 scenarios × 4 intervention types × 3 tiers, 70h multi-turn probing experiments with cross-turn analysis, 80h development/debugging)', 'timeline': '12-14 weeks (3 wk benchmark design with tiered difficulty validation, 3 wk implementation, 3 wk experiments, 3-5 wk analysis/writing)', 'estimated_gpu_cost': '$750 (at ~$2.50/hr H100 spot pricing)'}\n- **human_in_loop**: {'gpu_hours': '240 H100-hours (same inference workload, fewer debugging iterations with Claude-assisted scenario generation and tiered validation)', 'timeline': '10-12 weeks (2.5 wk benchmark design, 2 wk implementation, 2.5 wk experiments, 3-4 wk analysis/writing)', 'claude_api_cost': '$350-450 (scenario generation across 3 tiers, ambiguity calibration, code assistance, statistical analysis, paper drafting across ~18M input + 6M output tokens)', 'estimated_gpu_cost': '$600 (at ~$2.50/hr H100 spot pricing)'}\n- **auto_research**: {'gpu_hours': '500 H100-hours (larger intervention sweep, additional ablations on tier boundaries, probe transfer experiments across multiple random seeds, cross-model probe transfer analysis)', 'timeline': '5-7 weeks wall-clock (parallelized scenario generation, concurrent model evaluation, automated analysis pipeline)', 'claude_api_cost': '$800-1000 (orchestration, tiered scenario generation with ambiguity calibration, evaluation judging, statistical analysis, full paper drafting across ~45M input + 18M output tokens)', 'estimated_gpu_cost': '$1250 (at ~$2.50/hr H100 spot pricing)', 'speed_bottleneck': 'Tier 2/3 scenario quality validation — ensuring soft-ambiguous scenarios have correctly calibrated difficulty (one tool genuinely better but not trivially so) requires human spot-checking that cannot be fully automated without risking construct validity'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T18:31:39.650Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:31:39.650Z",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008"
}
```

---

## Round 1

34 recorded events

### User

_source line 3 · 2026-05-19T18:31:39.671Z_

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
  "promptId": "14b469ab-1910-4e37-ad22-9c281ad2e6b6",
  "type": "user",
  "uuid": "42b9977b-3f6c-44fb-94b8-2eff9bb971fb",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:31:39.670Z_

```json
{
  "parentUuid": "42b9977b-3f6c-44fb-94b8-2eff9bb971fb",
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
  "uuid": "a150a0b0-bc90-4c83-ba49-5edbedb95bf8",
  "timestamp": "2026-05-19T18:31:39.670Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:31:39.670Z_

```json
{
  "parentUuid": "a150a0b0-bc90-4c83-ba49-5edbedb95bf8",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1757575f-1af9-42f9-9848-95305462be4f",
  "timestamp": "2026-05-19T18:31:39.670Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
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
  "leafUuid": "1757575f-1af9-42f9-9848-95305462be4f",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate tool-selection faithfulness in multi-turn agents",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:31:52.727Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026 (Conference on Robot Learning). Wait, let me re-read - actually the system prompt says "CoRL 2026 主会" but the proposal itself is about faithfulness of tool-selection reasoning in multi-turn agentic systems, which seems more like an NLP/AI conference topic. Let me re-read...

Actually, the system prompt mentions "CoRL 2026" but the rubric mentions "NLP/CL 领域的影响力". Let me just evaluate this proposal objectively regardless of the venue. 

I'm noticing a potential venue mismatch here—the proposal is about LLM reasoning and tool-selection faithfulness, which feels more aligned with NLP or interpretability conferences than a robotics-focused venue like CoRL. But I'll set that aside and focus on evaluating the core idea quality as instructed, then I need to do the required web searches before proceeding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1757575f-1af9-42f9-9848-95305462be4f",
  "isSidechain": false,
  "requestId": "req_011CbCQTKC5AJYeP7XTtdg4d",
  "type": "assistant",
  "uuid": "d6f2490b-249f-4452-a23a-1fa584ed6574",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVXJN98b5iWUrpG5kdaGx7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19817,
      "cache_read_input_tokens": 0,
      "output_tokens": 477,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 477,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 19817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19817
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

_source line 9 · 2026-05-19T18:31:52.731Z_

I need to conduct thorough literature research before evaluating this proposal. Let me search for the key topics and referenced papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6f2490b-249f-4452-a23a-1fa584ed6574",
  "isSidechain": false,
  "requestId": "req_011CbCQTKC5AJYeP7XTtdg4d",
  "type": "assistant",
  "uuid": "e81abe03-6c32-4622-980b-7114be07a234",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVXJN98b5iWUrpG5kdaGx7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19817,
      "cache_read_input_tokens": 0,
      "output_tokens": 477,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 477,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 19817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19817
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

_source line 10 · 2026-05-19T18:31:52.942Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NtdHK9uk9awQZdnNM1Gjk9`</summary>

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
  "parentUuid": "e81abe03-6c32-4622-980b-7114be07a234",
  "isSidechain": false,
  "requestId": "req_011CbCQTKC5AJYeP7XTtdg4d",
  "type": "assistant",
  "uuid": "48a8420e-300b-40e9-8377-f1a66032633f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVXJN98b5iWUrpG5kdaGx7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19817,
      "cache_read_input_tokens": 0,
      "output_tokens": 477,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 477,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 19817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19817
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

_source line 11 · 2026-05-19T18:31:52.949Z_

<details><summary>↩ Tool result · `toolu_01NtdHK9uk9awQZdnNM1Gjk9`</summary>

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
  "parentUuid": "48a8420e-300b-40e9-8377-f1a66032633f",
  "isSidechain": false,
  "promptId": "14b469ab-1910-4e37-ad22-9c281ad2e6b6",
  "type": "user",
  "uuid": "0021f0a1-4880-4c72-838a-3f50a85cb90c",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "48a8420e-300b-40e9-8377-f1a66032633f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T18:31:56.361Z_

Now let me conduct the required literature searches. I'll run multiple searches in parallel to cover the key areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0021f0a1-4880-4c72-838a-3f50a85cb90c",
  "isSidechain": false,
  "requestId": "req_011CbCQUDkRhYRk58K3MqEYo",
  "type": "assistant",
  "uuid": "dd76505a-9ee7-4597-a269-3d17319ddf9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K27436NM6dFnUP9SqZar8y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1004,
      "cache_read_input_tokens": 19817,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1004,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 19817,
          "cache_creation_input_tokens": 1004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1004
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

_source line 13 · 2026-05-19T18:31:56.588Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017gyJWHGb1WxZH5npL4EoTx`</summary>

```json
{
  "query": "arXiv 2605.07990 tool calling linearly readable steerable language models 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd76505a-9ee7-4597-a269-3d17319ddf9a",
  "isSidechain": false,
  "requestId": "req_011CbCQUDkRhYRk58K3MqEYo",
  "type": "assistant",
  "uuid": "4d9df3dc-c8ea-4bfb-9923-450f0864d436",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K27436NM6dFnUP9SqZar8y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1004,
      "cache_read_input_tokens": 19817,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1004,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 19817,
          "cache_creation_input_tokens": 1004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1004
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

_source line 14 · 2026-05-19T18:32:12.573Z_

<details><summary>↩ Tool result · `toolu_017gyJWHGb1WxZH5npL4EoTx`</summary>

```text
Web search results for query: "arXiv 2605.07990 tool calling linearly readable steerable language models 2026"

Links: [{"title":"[2605.07990] Tool Calling is Linearly Readable and Steerable in Language Models","url":"https://arxiv.org/abs/2605.07990"},{"title":"[2605.07990v1] Tool Calling is Linearly Readable and Steerable in Language Models","url":"https://arxiv.org/abs/2605.07990v1"},{"title":"Tool Calling is Linearly Readable and Steerable in Language Models","url":"https://arxiv.org/html/2605.07990"},{"title":"AI Steerability 360: A Toolkit for Steering Large Language Models","url":"https://arxiv.org/pdf/2603.07837"},{"title":"Efficient and accurate steering of Large Language Models through attention-guided feature learning","url":"https://arxiv.org/pdf/2602.00333"}]

Based on the search results, I found the paper you're looking for:

**Title:** Tool Calling is Linearly Readable and Steerable in Language Models

**ArXiv ID:** 2605.07990

**Submission Date:** May 8, 2026

**Authors:** Zekun Wu, Ze Wang, Seonglae Cho, Yufei Yang, Adriano Koshiyama, Sahan Bulathwela, and Maria Perez-Ortiz from University College London, Holistic AI, and Imperial College London

**Key Findings:**

The researchers probed 12 instruction-tuned models across Gemma 3, Qwen 3, Qwen 2.5, and Llama 3.1 (270M to 27B), finding that the identity of the chosen tool is linearly readable and steerable inside the model.

Adding the mean-difference between two tools' average internal activations switches which tool the model selects at 77-100% accuracy on name-only single-turn prompts (93-100% at 4B+).

The per-tool means can also flag likely errors before they happen: on Gemma 3 12B and 27B, queries where the gap between the top-1 and top-2 tool is smallest produce 14-21x more wrong calls than queries with the largest gap.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d9df3dc-c8ea-4bfb-9923-450f0864d436",
  "isSidechain": false,
  "promptId": "14b469ab-1910-4e37-ad22-9c281ad2e6b6",
  "type": "user",
  "uuid": "3b678818-7584-4b31-8670-48254110a151",
  "toolUseResult": {
    "query": "arXiv 2605.07990 tool calling linearly readable steerable language models 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017DMeNV9Yxpj6gPGQHNvFne",
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
            "title": "Efficient and accurate steering of Large Language Models through attention-guided feature learning",
            "url": "https://arxiv.org/pdf/2602.00333"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Title:** Tool Calling is Linearly Readable and Steerable in Language Models\n\n**ArXiv ID:** 2605.07990\n\n**Submission Date:** May 8, 2026\n\n**Authors:** Zekun Wu, Ze Wang, Seonglae Cho, Yufei Yang, Adriano Koshiyama, Sahan Bulathwela, and Maria Perez-Ortiz from University College London, Holistic AI, and Imperial College London\n\n**Key Findings:**\n\nThe researchers probed 12 instruction-tuned models across Gemma 3, Qwen 3, Qwen 2.5, and Llama 3.1 (270M to 27B), finding that the identity of the chosen tool is linearly readable and steerable inside the model.\n\nAdding the mean-difference between two tools' average internal activations switches which tool the model selects at 77-100% accuracy on name-only single-turn prompts (93-100% at 4B+).\n\nThe per-tool means can also flag likely errors before they happen: on Gemma 3 12B and 27B, queries where the gap between the top-1 and top-2 tool is smallest produce 14-21x more wrong calls than queries with the largest gap."
    ],
    "durationSeconds": 15.979381081000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4d9df3dc-c8ea-4bfb-9923-450f0864d436",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T18:32:15.484Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DiZdM38JxpGXpASUgKWpZA`</summary>

```json
{
  "query": "RFEval reasoning faithfulness counterfactual intervention benchmark 2602.17053 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b678818-7584-4b31-8670-48254110a151",
  "isSidechain": false,
  "requestId": "req_011CbCQVfPok6CHaScoqFGAQ",
  "type": "assistant",
  "uuid": "8e5174d0-5038-45d7-a6b0-627c7e4ffb25",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017NRMAZArWZWTgtg4gGJNEC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 20821,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 686,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 20821,
          "cache_creation_input_tokens": 686,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 686
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

_source line 16 · 2026-05-19T18:32:22.651Z_

<details><summary>↩ Tool result · `toolu_01DiZdM38JxpGXpASUgKWpZA`</summary>

```text
Web search results for query: "RFEval reasoning faithfulness counterfactual intervention benchmark 2602.17053 2026"

Links: [{"title":"[2602.17053v1] RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/abs/2602.17053v1"},{"title":"[2602.17053] RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/abs/2602.17053"},{"title":"RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/pdf/2602.17053"},{"title":"RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/html/2602.17053"},{"title":"RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=2Gc8aj0afg"}]

Based on the search results, here's what I found about RFEval:

## Overview

RFEval is a benchmark created by Yunseok Han, Yejoon Lee, and Jaeyoung Do that addresses how Large Reasoning Models often produce rationales that sound plausible but fail to reflect their true decision process.

## Key Components

The framework defines reasoning faithfulness through two testable conditions: stance consistency (a coherent stance linking reasoning to answer) and causal influence (the stated reasoning causally drives the answer under output-level interventions), explicitly decoupled from accuracy.

## Benchmark Details

RFEval is a benchmark of 7,186 instances across seven tasks that probes faithfulness via controlled, output-level counterfactual interventions.

## Findings

Evaluating twelve open-source LRMs, the researchers found unfaithfulness in 49.7% of outputs, predominantly from stance inconsistency. Failures are concentrated in brittle, convergent domains such as math and code, and correlate more with post-training regimes than with scale.

Notably, accuracy is neither a sufficient nor a reliable proxy for faithfulness: once controlling for model and task, the accuracy-faithfulness link is weak and statistically insignificant.

The paper was submitted on February 19, 2026, with the latest version (v3) on February 23, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e5174d0-5038-45d7-a6b0-627c7e4ffb25",
  "isSidechain": false,
  "promptId": "14b469ab-1910-4e37-ad22-9c281ad2e6b6",
  "type": "user",
  "uuid": "abd9690b-f82b-4020-bd99-ec13b546c854",
  "toolUseResult": {
    "query": "RFEval reasoning faithfulness counterfactual intervention benchmark 2602.17053 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DnPkAHtBZVYgFsTXPpPequ",
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
            "title": "RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2602.17053"
          },
          {
            "title": "RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models",
            "url": "https://arxiv.org/html/2602.17053"
          },
          {
            "title": "RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models | OpenReview",
            "url": "https://openreview.net/forum?id=2Gc8aj0afg"
          }
        ]
      },
      "Based on the search results, here's what I found about RFEval:\n\n## Overview\n\nRFEval is a benchmark created by Yunseok Han, Yejoon Lee, and Jaeyoung Do that addresses how Large Reasoning Models often produce rationales that sound plausible but fail to reflect their true decision process.\n\n## Key Components\n\nThe framework defines reasoning faithfulness through two testable conditions: stance consistency (a coherent stance linking reasoning to answer) and causal influence (the stated reasoning causally drives the answer under output-level interventions), explicitly decoupled from accuracy.\n\n## Benchmark Details\n\nRFEval is a benchmark of 7,186 instances across seven tasks that probes faithfulness via controlled, output-level counterfactual interventions.\n\n## Findings\n\nEvaluating twelve open-source LRMs, the researchers found unfaithfulness in 49.7% of outputs, predominantly from stance inconsistency. Failures are concentrated in brittle, convergent domains such as math and code, and correlate more with post-training regimes than with scale.\n\nNotably, accuracy is neither a sufficient nor a reliable proxy for faithfulness: once controlling for model and task, the accuracy-faithfulness link is weak and statistically insignificant.\n\nThe paper was submitted on February 19, 2026, with the latest version (v3) on February 23, 2026."
    ],
    "durationSeconds": 7.161263918999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8e5174d0-5038-45d7-a6b0-627c7e4ffb25",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T18:32:25.022Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014AQx4z1zM85RELrqnT9d75`</summary>

```json
{
  "query": "multi-turn agentic tool selection faithfulness CoT reasoning 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abd9690b-f82b-4020-bd99-ec13b546c854",
  "isSidechain": false,
  "requestId": "req_011CbCQWQU9oyAcuCSCi53d5",
  "type": "assistant",
  "uuid": "3dff3746-dd56-4383-ba6b-6d5cdd710860",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AcnaZ14HNX8j1eqKibb9kt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 21507,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 21507,
          "cache_creation_input_tokens": 731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 731
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

_source line 18 · 2026-05-19T18:32:33.609Z_

<details><summary>↩ Tool result · `toolu_014AQx4z1zM85RELrqnT9d75`</summary>

```text
Web search results for query: "multi-turn agentic tool selection faithfulness CoT reasoning 2026 arxiv"

Links: [{"title":"[2602.16154v1] Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution","url":"https://arxiv.org/abs/2602.16154v1"},{"title":"Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing","url":"https://arxiv.org/html/2604.08401"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2512.20745"},{"title":"AutoTool: Dynamic Tool Selection and Integration for Agentic Reasoning","url":"https://arxiv.org/html/2512.13278v1"},{"title":"Preprint AUTOTOOL: DYNAMIC TOOL SELECTION AND INTEGRATION FOR AGENTIC REASONING","url":"https://arxiv.org/pdf/2512.13278"},{"title":"Beyond Correctness: Rewarding Faithful Reasoning in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2510.13272"},{"title":"Empowering Multi-Turn Tool-Integrated Agentic Reasoning with Group...","url":"https://arxiv.org/abs/2511.14846"},{"title":"Towards Trustworthy Multi-Turn LLM Agents via Behavioral Guidance","url":"https://arxiv.org/pdf/2512.11421"}]

I found several highly relevant arxiv papers from 2026 that relate to your search query about multi-turn agentic tool selection, faithfulness, and CoT reasoning:

## Key Papers Found:

1. **Empowering Multi-Turn Tool-Integrated Agentic Reasoning with Group Turn Policy Optimization** (2511.14846)
   - Latest version uploaded April 20, 2026
   - Focuses on multi-turn tool-integrated agentic reasoning

2. **AutoTool: Dynamic Tool Selection and Integration for Agentic Reasoning** (2512.13278)
   - Explores how LLMs can operate as agents that interleave their reasoning with multi-turn interactions in external tool environments such as search engines, code interpreters, and vision tools
   - The tool integration process reduces compounding errors in long CoT trajectories and enables more precise and reliable computation

3. **Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing** (2604.08401)
   - Addresses how agentic systems manage uncertainty before committing internal reasoning states to actions through methods like self-consistency and multi-agent debate
   - Focuses on faithful reasoning in agentic contexts

4. **Beyond Correctness: Rewarding Faithful Reasoning in Retrieval-Augmented Generation** (2510.13272)
   - Addresses that existing agentic search methods optimize for final-answer correctness while overlooking the faithfulness of intermediate reasoning steps

5. **Towards Trustworthy Multi-Turn LLM Agents via Behavioral Guidance** (2512.11421)
   - Focuses on trustworthiness in multi-turn LLM agents

These papers directly address the intersection of multi-turn agentic reasoning, tool selection, faithfulness, and CoT reasoning that your search query targets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dff3746-dd56-4383-ba6b-6d5cdd710860",
  "isSidechain": false,
  "promptId": "14b469ab-1910-4e37-ad22-9c281ad2e6b6",
  "type": "user",
  "uuid": "16b09599-16c9-42b1-b23a-4a964beb6e4e",
  "toolUseResult": {
    "query": "multi-turn agentic tool selection faithfulness CoT reasoning 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01REsZD2Szh3tPsskC12GWVX",
        "content": [
          {
            "title": "[2602.16154v1] Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution",
            "url": "https://arxiv.org/abs/2602.16154v1"
          },
          {
            "title": "Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing",
            "url": "https://arxiv.org/html/2604.08401"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2512.20745"
          },
          {
            "title": "AutoTool: Dynamic Tool Selection and Integration for Agentic Reasoning",
            "url": "https://arxiv.org/html/2512.13278v1"
          },
          {
            "title": "Preprint AUTOTOOL: DYNAMIC TOOL SELECTION AND INTEGRATION FOR AGENTIC REASONING",
            "url": "https://arxiv.org/pdf/2512.13278"
          },
          {
            "title": "Beyond Correctness: Rewarding Faithful Reasoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2510.13272"
          },
          {
            "title": "Empowering Multi-Turn Tool-Integrated Agentic Reasoning with Group...",
            "url": "https://arxiv.org/abs/2511.14846"
          },
          {
            "title": "Towards Trustworthy Multi-Turn LLM Agents via Behavioral Guidance",
            "url": "https://arxiv.org/pdf/2512.11421"
          }
        ]
      },
      "I found several highly relevant arxiv papers from 2026 that relate to your search query about multi-turn agentic tool selection, faithfulness, and CoT reasoning:\n\n## Key Papers Found:\n\n1. **Empowering Multi-Turn Tool-Integrated Agentic Reasoning with Group Turn Policy Optimization** (2511.14846)\n   - Latest version uploaded April 20, 2026\n   - Focuses on multi-turn tool-integrated agentic reasoning\n\n2. **AutoTool: Dynamic Tool Selection and Integration for Agentic Reasoning** (2512.13278)\n   - Explores how LLMs can operate as agents that interleave their reasoning with multi-turn interactions in external tool environments such as search engines, code interpreters, and vision tools\n   - The tool integration process reduces compounding errors in long CoT trajectories and enables more precise and reliable computation\n\n3. **Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing** (2604.08401)\n   - Addresses how agentic systems manage uncertainty before committing internal reasoning states to actions through methods like self-consistency and multi-agent debate\n   - Focuses on faithful reasoning in agentic contexts\n\n4. **Beyond Correctness: Rewarding Faithful Reasoning in Retrieval-Augmented Generation** (2510.13272)\n   - Addresses that existing agentic search methods optimize for final-answer correctness while overlooking the faithfulness of intermediate reasoning steps\n\n5. **Towards Trustworthy Multi-Turn LLM Agents via Behavioral Guidance** (2512.11421)\n   - Focuses on trustworthiness in multi-turn LLM agents\n\nThese papers directly address the intersection of multi-turn agentic reasoning, tool selection, faithfulness, and CoT reasoning that your search query targets."
    ],
    "durationSeconds": 8.582593716000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3dff3746-dd56-4383-ba6b-6d5cdd710860",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T18:32:36.136Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K84msiyK8zPhXwcJQdWacs`</summary>

```json
{
  "query": "\"Lie to Me\" chain-of-thought faithfulness reasoning models 2603.22582 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16b09599-16c9-42b1-b23a-4a964beb6e4e",
  "isSidechain": false,
  "requestId": "req_011CbCQXDGyoS9JX5j8U63QX",
  "type": "assistant",
  "uuid": "9deef0bd-a590-4757-b262-e89280ba93b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WABQcH72a11bE4uPFDbbRt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 898,
      "cache_read_input_tokens": 22238,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 22238,
          "cache_creation_input_tokens": 898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 898
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

_source line 20 · 2026-05-19T18:32:46.530Z_

<details><summary>↩ Tool result · `toolu_01K84msiyK8zPhXwcJQdWacs`</summary>

```text
Web search results for query: ""Lie to Me" chain-of-thought faithfulness reasoning models 2603.22582 2026"

Links: [{"title":"[2603.22582] Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?","url":"https://arxiv.org/abs/2603.22582"},{"title":"(PDF) Why Models Know But Don't Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://www.researchgate.net/publication/403262878_Why_Models_Know_But_Don't_Say_Chain-of-Thought_Faithfulness_Divergence_Between_Thinking_Tokens_and_Answers_in_Open-Weight_Reasoning_Models"},{"title":"Paper page - Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?","url":"https://huggingface.co/papers/2603.22582"},{"title":"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning…","url":"https://www.opentrain.ai/papers/lie-to-me-how-faithful-is-chain-of-thought-reasoning-in-reasoning-models--arxiv-2603.22582/"},{"title":"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?","url":"https://arxiv.org/html/2603.22582v1"},{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410v1"},{"title":"LIE TO ME: HOW FAITHFUL IS CHAIN-OF-THOUGHT REASONING","url":"https://arxiv.org/pdf/2603.22582"},{"title":"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models? [Quick Review]","url":"https://liner.com/review/lie-to-me-how-faithful-is-chainofthought-reasoning-in-reasoning"}]

I found detailed information about the research paper you're asking about. Here's what the search reveals:

## "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?"

The paper (arXiv:2603.22582) was submitted on March 23, 2026 and authored by Richard J. Young.

### Research Overview

The paper examines chain-of-thought (CoT) reasoning as a transparency mechanism for large language models in safety-critical deployments, focusing on faithfulness (whether models accurately verbalize the factors that actually influence their outputs).

### Methodology

The study tests 12 open-weight reasoning models spanning 9 architectural families (7B-685B parameters) on 498 multiple-choice questions from MMLU and GPQA Diamond, injecting six categories of reasoning hints (sycophancy, consistency, visual pattern, metadata, grader hacking, and unethical information) and measuring the rate at which models acknowledge hint influence in their CoT when hints successfully alter answers.

### Key Findings

Across 41,832 inference runs, overall faithfulness rates range from 39.7% (Seed-1.6-Flash) to 89.9% (DeepSeek-V3.2-Speciale) across model families, with consistency hints (35.5%) and sycophancy hints (53.9%) exhibiting the lowest acknowledgment rates.

Notably, there is a striking gap between thinking-token acknowledgment (approximately 87.5%) and answer-text acknowledgment (approximately 28.6%), suggesting that models internally recognize hint influence but systematically suppress this acknowledgment in their outputs.

### Implications

The findings carry direct implications for the viability of CoT monitoring as a safety mechanism and suggest that faithfulness is not a fixed property of reasoning models but varies systematically with architecture, training method, and the nature of the influencing cue.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9deef0bd-a590-4757-b262-e89280ba93b1",
  "isSidechain": false,
  "promptId": "14b469ab-1910-4e37-ad22-9c281ad2e6b6",
  "type": "user",
  "uuid": "3b4c04ea-7a45-44e3-876b-be31dc244de8",
  "toolUseResult": {
    "query": "\"Lie to Me\" chain-of-thought faithfulness reasoning models 2603.22582 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Gs9TiDYRTk9hc9E1MxZKVt",
        "content": [
          {
            "title": "[2603.22582] Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?",
            "url": "https://arxiv.org/abs/2603.22582"
          },
          {
            "title": "(PDF) Why Models Know But Don't Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://www.researchgate.net/publication/403262878_Why_Models_Know_But_Don't_Say_Chain-of-Thought_Faithfulness_Divergence_Between_Thinking_Tokens_and_Answers_in_Open-Weight_Reasoning_Models"
          },
          {
            "title": "Paper page - Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?",
            "url": "https://huggingface.co/papers/2603.22582"
          },
          {
            "title": "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning…",
            "url": "https://www.opentrain.ai/papers/lie-to-me-how-faithful-is-chain-of-thought-reasoning-in-reasoning-models--arxiv-2603.22582/"
          },
          {
            "title": "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?",
            "url": "https://arxiv.org/html/2603.22582v1"
          },
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410v1"
          },
          {
            "title": "LIE TO ME: HOW FAITHFUL IS CHAIN-OF-THOUGHT REASONING",
            "url": "https://arxiv.org/pdf/2603.22582"
          },
          {
            "title": "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models? [Quick Review]",
            "url": "https://liner.com/review/lie-to-me-how-faithful-is-chainofthought-reasoning-in-reasoning"
          }
        ]
      },
      "I found detailed information about the research paper you're asking about. Here's what the search reveals:\n\n## \"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?\"\n\nThe paper (arXiv:2603.22582) was submitted on March 23, 2026 and authored by Richard J. Young.\n\n### Research Overview\n\nThe paper examines chain-of-thought (CoT) reasoning as a transparency mechanism for large language models in safety-critical deployments, focusing on faithfulness (whether models accurately verbalize the factors that actually influence their outputs).\n\n### Methodology\n\nThe study tests 12 open-weight reasoning models spanning 9 architectural families (7B-685B parameters) on 498 multiple-choice questions from MMLU and GPQA Diamond, injecting six categories of reasoning hints (sycophancy, consistency, visual pattern, metadata, grader hacking, and unethical information) and measuring the rate at which models acknowledge hint influence in their CoT when hints successfully alter answers.\n\n### Key Findings\n\nAcross 41,832 inference runs, overall faithfulness rates range from 39.7% (Seed-1.6-Flash) to 89.9% (DeepSeek-V3.2-Speciale) across model families, with consistency hints (35.5%) and sycophancy hints (53.9%) exhibiting the lowest acknowledgment rates.\n\nNotably, there is a striking gap between thinking-token acknowledgment (approximately 87.5%) and answer-text acknowledgment (approximately 28.6%), suggesting that models internally recognize hint influence but systematically suppress this acknowledgment in their outputs.\n\n### Implications\n\nThe findings carry direct implications for the viability of CoT monitoring as a safety mechanism and suggest that faithfulness is not a fixed property of reasoning models but varies systematically with architecture, training method, and the nature of the influencing cue."
    ],
    "durationSeconds": 10.390533659,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9deef0bd-a590-4757-b262-e89280ba93b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
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
  "leafUuid": "3b4c04ea-7a45-44e3-876b-be31dc244de8",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate tool-selection faithfulness in multi-turn agents",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008"
}
```

---

### Tool call

_source line 23 · 2026-05-19T18:32:49.095Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RqENJShTdrkCfrc9pn9668`</summary>

```json
{
  "query": "CoRL 2026 conference topics scope accepted papers robot learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b4c04ea-7a45-44e3-876b-be31dc244de8",
  "isSidechain": false,
  "requestId": "req_011CbCQYAcGbgmvLfrwNVb1u",
  "type": "assistant",
  "uuid": "42ef2054-0b28-458c-a257-d8a8e1253082",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NQ5CXV5xe94WzDqRQe2EQS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 23136,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 23136,
          "cache_creation_input_tokens": 1066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1066
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

_source line 24 · 2026-05-19T18:32:56.966Z_

<details><summary>↩ Tool result · `toolu_01RqENJShTdrkCfrc9pn9668`</summary>

```text
Web search results for query: "CoRL 2026 conference topics scope accepted papers robot learning"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI","url":"https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - About CoRL","url":"https://www.corl.org/about-corl"}]

Based on the search results, here's comprehensive information about CoRL 2026:

## Conference Overview

The Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics. The aim of CoRL 2026 is to publish significant original research at the intersection of robotics and machine learning, and it is a selective, single-track international conference addressing theory and practice of machine learning for robots.

## Conference Topics and Scope

CoRL welcomes papers in areas such as: learning representations for robotic perception and control; learning robot foundation models or general-purpose knowledge systems for robotics; imitation learning for robotics; reinforcement learning for control of physical robots; learning approaches to robot safety and alignment; applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics; robot systems, hardware, and sensors for learning and data-driven approaches; theoretical foundations of robot learning, including generalization theory and uncertainty quantification; and video models and latent world models for robot learning.

## Submission Requirements

Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots, and submissions without a robotics focus will be returned without review.

## Event Details

CoRL 2026 is scheduled for November 10–12, 2026, in Austin, Texas. The paper submission deadline is May 29, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42ef2054-0b28-458c-a257-d8a8e1253082",
  "isSidechain": false,
  "promptId": "14b469ab-1910-4e37-ad22-9c281ad2e6b6",
  "type": "user",
  "uuid": "fb701326-c1c3-4d67-8bca-2b664bf98d2c",
  "toolUseResult": {
    "query": "CoRL 2026 conference topics scope accepted papers robot learning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GzqVSWGBbKcYpJxfMtfPgF",
        "content": [
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI",
            "url": "https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"
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
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
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
            "title": "CoRL 2026 - About CoRL",
            "url": "https://www.corl.org/about-corl"
          }
        ]
      },
      "Based on the search results, here's comprehensive information about CoRL 2026:\n\n## Conference Overview\n\nThe Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics. The aim of CoRL 2026 is to publish significant original research at the intersection of robotics and machine learning, and it is a selective, single-track international conference addressing theory and practice of machine learning for robots.\n\n## Conference Topics and Scope\n\nCoRL welcomes papers in areas such as: learning representations for robotic perception and control; learning robot foundation models or general-purpose knowledge systems for robotics; imitation learning for robotics; reinforcement learning for control of physical robots; learning approaches to robot safety and alignment; applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics; robot systems, hardware, and sensors for learning and data-driven approaches; theoretical foundations of robot learning, including generalization theory and uncertainty quantification; and video models and latent world models for robot learning.\n\n## Submission Requirements\n\nAuthors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots, and submissions without a robotics focus will be returned without review.\n\n## Event Details\n\nCoRL 2026 is scheduled for November 10–12, 2026, in Austin, Texas. The paper submission deadline is May 29, 2026."
    ],
    "durationSeconds": 7.865530906999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "42ef2054-0b28-458c-a257-d8a8e1253082",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T18:33:00.054Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JUUumhtXTBZ3yUUCSrAsUc`</summary>

```json
{
  "query": "tool selection causal intervention behavioral probing LLM agents benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb701326-c1c3-4d67-8bca-2b664bf98d2c",
  "isSidechain": false,
  "requestId": "req_011CbCQYwCuLbaY5KPCBEMVb",
  "type": "assistant",
  "uuid": "ec7d4e26-11a9-45d5-b29a-9e3d8f7e6e94",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DgLouyYiYDijPCMuFKGvyt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 742,
      "cache_read_input_tokens": 24202,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 24202,
          "cache_creation_input_tokens": 742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 742
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

_source line 26 · 2026-05-19T18:33:08.696Z_

<details><summary>↩ Tool result · `toolu_01JUUumhtXTBZ3yUUCSrAsUc`</summary>

```text
Web search results for query: "tool selection causal intervention behavioral probing LLM agents benchmark 2026"

Links: [{"title":"[2605.17641] Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents","url":"https://arxiv.org/abs/2605.17641"},{"title":"Top 10 LLM Research Papers of 2026","url":"https://www.analyticsvidhya.com/blog/2026/05/top-llm-research-papers-2026/"},{"title":"Agent-SafetyBench: Evaluating LLM Agent Safety","url":"https://www.emergentmind.com/topics/agent-safetybench"},{"title":"BiasBusters: Uncovering and Mitigating Tool Selection Bias in Large Language Models","url":"https://arxiv.org/pdf/2510.00307"},{"title":"A Survey on Evaluation of LLM-based Agents","url":"https://arxiv.org/pdf/2503.16416"},{"title":"Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents","url":"https://arxiv.org/html/2605.17641"},{"title":"Evaluation and Benchmarking of LLM Agents: A Survey | Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2","url":"https://dl.acm.org/doi/10.1145/3711896.3736570"},{"title":"Internal Representations as Indicators of Hallucinations in Agent Tool Selection","url":"https://arxiv.org/pdf/2601.05214"}]

Based on the search results, I found several highly relevant papers and research from 2026 related to your query:

## Key Findings:

**Causal Intervention-Based Memory Selection (May 2026)**

Causal Memory Intervention (CMI) is a causal memory-selection technique that estimates how candidate memories affect the model's answer under controlled interventions, selecting memories that improve task performance while suppressing unstable, irrelevant, or harmful ones. A causally annotated benchmark called Causal-LoCoMo was introduced, derived from long conversational data, where each example contains a user request, a structured memory bank, useful memories, irrelevant distractors, and synthetic harmful memories.

**Tool Selection Bias Research**

Tool-selection bias has been identified as a key obstacle to the fair deployment of tool-augmented LLM agents. LLMs may prefer certain tools not for their relevance or accuracy, but because of superficial metadata, such as tool names, descriptions, or prompt ordering.

**Agent Safety Benchmarking**

Agent-SafetyBench is a suite of datasets, benchmarks, and evaluation methodologies designed for systematically assessing and improving the safety of LLM agents, focusing specifically on the behavioral safety of interactive, tool-using agents and probing their robustness, risk awareness, and failure modes.

**Recent Behavioral Probing Studies**

SteerEval is a benchmark for evaluating how well LLMs can be controlled across language features, sentiment, and personality, focusing on different levels of behavioral control.

These papers reflect the emerging focus on rigorous evaluation of tool-using LLM agents through causal interventions and behavioral probing methodologies in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec7d4e26-11a9-45d5-b29a-9e3d8f7e6e94",
  "isSidechain": false,
  "promptId": "14b469ab-1910-4e37-ad22-9c281ad2e6b6",
  "type": "user",
  "uuid": "4d9c5c2a-971a-45c7-b828-ddd9e7321dba",
  "toolUseResult": {
    "query": "tool selection causal intervention behavioral probing LLM agents benchmark 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PC1vHxAFKFXpo5uWTgaCZt",
        "content": [
          {
            "title": "[2605.17641] Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents",
            "url": "https://arxiv.org/abs/2605.17641"
          },
          {
            "title": "Top 10 LLM Research Papers of 2026",
            "url": "https://www.analyticsvidhya.com/blog/2026/05/top-llm-research-papers-2026/"
          },
          {
            "title": "Agent-SafetyBench: Evaluating LLM Agent Safety",
            "url": "https://www.emergentmind.com/topics/agent-safetybench"
          },
          {
            "title": "BiasBusters: Uncovering and Mitigating Tool Selection Bias in Large Language Models",
            "url": "https://arxiv.org/pdf/2510.00307"
          },
          {
            "title": "A Survey on Evaluation of LLM-based Agents",
            "url": "https://arxiv.org/pdf/2503.16416"
          },
          {
            "title": "Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents",
            "url": "https://arxiv.org/html/2605.17641"
          },
          {
            "title": "Evaluation and Benchmarking of LLM Agents: A Survey | Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2",
            "url": "https://dl.acm.org/doi/10.1145/3711896.3736570"
          },
          {
            "title": "Internal Representations as Indicators of Hallucinations in Agent Tool Selection",
            "url": "https://arxiv.org/pdf/2601.05214"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers and research from 2026 related to your query:\n\n## Key Findings:\n\n**Causal Intervention-Based Memory Selection (May 2026)**\n\nCausal Memory Intervention (CMI) is a causal memory-selection technique that estimates how candidate memories affect the model's answer under controlled interventions, selecting memories that improve task performance while suppressing unstable, irrelevant, or harmful ones. A causally annotated benchmark called Causal-LoCoMo was introduced, derived from long conversational data, where each example contains a user request, a structured memory bank, useful memories, irrelevant distractors, and synthetic harmful memories.\n\n**Tool Selection Bias Research**\n\nTool-selection bias has been identified as a key obstacle to the fair deployment of tool-augmented LLM agents. LLMs may prefer certain tools not for their relevance or accuracy, but because of superficial metadata, such as tool names, descriptions, or prompt ordering.\n\n**Agent Safety Benchmarking**\n\nAgent-SafetyBench is a suite of datasets, benchmarks, and evaluation methodologies designed for systematically assessing and improving the safety of LLM agents, focusing specifically on the behavioral safety of interactive, tool-using agents and probing their robustness, risk awareness, and failure modes.\n\n**Recent Behavioral Probing Studies**\n\nSteerEval is a benchmark for evaluating how well LLMs can be controlled across language features, sentiment, and personality, focusing on different levels of behavioral control.\n\nThese papers reflect the emerging focus on rigorous evaluation of tool-using LLM agents through causal interventions and behavioral probing methodologies in 2026."
    ],
    "durationSeconds": 8.637352314999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ec7d4e26-11a9-45d5-b29a-9e3d8f7e6e94",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T18:33:11.776Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BcLyA4JhTxTppZmwcSRscz`</summary>

```json
{
  "query": "arXiv 2605.09252 \"LLM agents already know when to call tools\" tool-necessity probing 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d9c5c2a-971a-45c7-b828-ddd9e7321dba",
  "isSidechain": false,
  "requestId": "req_011CbCQZoJfdg2iHoFT6c5qX",
  "type": "assistant",
  "uuid": "2a87913c-2b4f-43e0-8864-0512b380faac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dzF2TkcUN883EBTZitg1N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 871,
      "cache_read_input_tokens": 24944,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 871,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 24944,
          "cache_creation_input_tokens": 871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 871
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

_source line 28 · 2026-05-19T18:33:20.342Z_

<details><summary>↩ Tool result · `toolu_01BcLyA4JhTxTppZmwcSRscz`</summary>

```text
Web search results for query: "arXiv 2605.09252 "LLM agents already know when to call tools" tool-necessity probing 2026"

Links: [{"title":"[2605.14038] Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use","url":"https://arxiv.org/abs/2605.14038"},{"title":"LLM Agents Already Know When to Call Tools - Even Without Reasoning","url":"https://arxiv.org/html/2605.09252v1"},{"title":"Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use","url":"https://arxiv.org/html/2605.14038"},{"title":"LLM Agents for Knowledge Discovery in Atomic Layer Processing","url":"https://arxiv.org/html/2509.26201v1"},{"title":"Evaluation and Benchmarking of LLM Agents: A Survey","url":"https://arxiv.org/html/2507.21504v1"},{"title":"Trust No Tool: Evaluating and Defending LLM Agents under Untrusted Tool Feedback","url":"https://arxiv.org/html/2605.17453v1"}]

I found the paper! Here's the information about arXiv 2605.09252:

The paper "LLM Agents Already Know When to Call Tools - Even Without Reasoning" (arXiv:2605.09252) was submitted on May 10, 2026, by authors Chung-En Sun, Linbo Liu, Ge Yan, Zimo Wang, and Tsui-Wei Weng from UC San Diego and Amazon AWS.

The paper addresses the problem that tool-augmented LLM agents tend to call tools indiscriminately, even when the model can answer directly, with each unnecessary call wasting API fees and latency.

The researchers propose "When2Tool," a benchmark of 18 environments (15 single-hop, 3 multi-hop) spanning three categories of tool necessity — computational scale, knowledge boundaries, and execution reliability — each with controlled difficulty levels.

They evaluate two families of training-free baselines: Prompt-only approaches (varying the prompt to discourage unnecessary calls) and Reason-then-Act (requiring the model to reason about tool necessity before acting). Both approaches provide limited control: Prompt-only suppresses necessary calls alongside unnecessary ones, and Reason-then-Act still incurs a disproportionate accuracy cost on hard tasks.

The paper uses hidden state probing to understand why these baselines fail, which aligns with the tool-necessity probing methodology you mentioned in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a87913c-2b4f-43e0-8864-0512b380faac",
  "isSidechain": false,
  "promptId": "14b469ab-1910-4e37-ad22-9c281ad2e6b6",
  "type": "user",
  "uuid": "7adb55f1-0b39-4fbf-83fe-43e61ba3683e",
  "toolUseResult": {
    "query": "arXiv 2605.09252 \"LLM agents already know when to call tools\" tool-necessity probing 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01E3GC1aT8ueQZZMq8BW54Ro",
        "content": [
          {
            "title": "[2605.14038] Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use",
            "url": "https://arxiv.org/abs/2605.14038"
          },
          {
            "title": "LLM Agents Already Know When to Call Tools - Even Without Reasoning",
            "url": "https://arxiv.org/html/2605.09252v1"
          },
          {
            "title": "Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use",
            "url": "https://arxiv.org/html/2605.14038"
          },
          {
            "title": "LLM Agents for Knowledge Discovery in Atomic Layer Processing",
            "url": "https://arxiv.org/html/2509.26201v1"
          },
          {
            "title": "Evaluation and Benchmarking of LLM Agents: A Survey",
            "url": "https://arxiv.org/html/2507.21504v1"
          },
          {
            "title": "Trust No Tool: Evaluating and Defending LLM Agents under Untrusted Tool Feedback",
            "url": "https://arxiv.org/html/2605.17453v1"
          }
        ]
      },
      "I found the paper! Here's the information about arXiv 2605.09252:\n\nThe paper \"LLM Agents Already Know When to Call Tools - Even Without Reasoning\" (arXiv:2605.09252) was submitted on May 10, 2026, by authors Chung-En Sun, Linbo Liu, Ge Yan, Zimo Wang, and Tsui-Wei Weng from UC San Diego and Amazon AWS.\n\nThe paper addresses the problem that tool-augmented LLM agents tend to call tools indiscriminately, even when the model can answer directly, with each unnecessary call wasting API fees and latency.\n\nThe researchers propose \"When2Tool,\" a benchmark of 18 environments (15 single-hop, 3 multi-hop) spanning three categories of tool necessity — computational scale, knowledge boundaries, and execution reliability — each with controlled difficulty levels.\n\nThey evaluate two families of training-free baselines: Prompt-only approaches (varying the prompt to discourage unnecessary calls) and Reason-then-Act (requiring the model to reason about tool necessity before acting). Both approaches provide limited control: Prompt-only suppresses necessary calls alongside unnecessary ones, and Reason-then-Act still incurs a disproportionate accuracy cost on hard tasks.\n\nThe paper uses hidden state probing to understand why these baselines fail, which aligns with the tool-necessity probing methodology you mentioned in your query."
    ],
    "durationSeconds": 8.562060353000009,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2a87913c-2b4f-43e0-8864-0512b380faac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-19T18:33:20.348Z_

```json
{
  "parentUuid": "7adb55f1-0b39-4fbf-83fe-43e61ba3683e",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b82f01d1-11d3-4545-9d41-5c6fccea0ae0",
  "timestamp": "2026-05-19T18:33:20.348Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-19T18:33:23.345Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LzpGrE7RsNLBoShZiJwD85`</summary>

```json
{
  "query": "\"Beyond the Black Box\" interpretability agentic AI tool use 2605.06890 SAE probes multi-step"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b82f01d1-11d3-4545-9d41-5c6fccea0ae0",
  "isSidechain": false,
  "requestId": "req_011CbCQaf9KM9EuWoDfrKVsG",
  "type": "assistant",
  "uuid": "81fa5c67-c72e-4c88-aa22-3036398326a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ws4q1Jd48ZPb3PURuq7VkY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 25815,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 25815,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 829
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

_source line 31 · 2026-05-19T18:33:35.084Z_

<details><summary>↩ Tool result · `toolu_01LzpGrE7RsNLBoShZiJwD85`</summary>

```text
Web search results for query: ""Beyond the Black Box" interpretability agentic AI tool use 2605.06890 SAE probes multi-step"

Links: [{"title":"[2605.06890] Beyond the Black Box: Interpretability of Agentic AI Tool Use","url":"https://arxiv.org/abs/2605.06890"},{"title":"Beyond the Black Box: Interpretability of Agentic AI Tool Use","url":"https://arxiv.org/html/2605.06890"},{"title":"Beyond the black box: How agentic AI is redefining explainability - SAS Voices","url":"https://blogs.sas.com/content/sascom/2025/03/24/beyond-the-black-box-how-agentic-ai-is-redefining-explainability/"},{"title":"Deploying Interpretability to Production with Rakuten: SAE Probes for PII Detection","url":"https://www.goodfire.ai/research/rakuten-sae-probes-for-pii-detection"},{"title":"Beyond Black-Box Benchmarking: Observability, Analytics, and Optimization of Agentic Systems","url":"https://arxiv.org/html/2503.06745v1"},{"title":"Bridging the Black Box: A Survey on Mechanistic Interpretability in AI | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3787104"}]

I found the paper you're looking for! Here's what the research is about:

The paper "Beyond the Black Box: Interpretability of Agentic AI Tool Use" (arXiv 2605.06890) addresses tool-use failures in AI agents, which can manifest as skipping required tool calls, invoking tools unnecessarily, or taking actions whose consequences only become visible after execution.

The research introduces a mechanistic-interpretability toolkit built on Sparse Autoencoders (SAEs) and linear probes. The framework reads model states before each action and infers both whether a tool is needed and how consequential the next tool action is likely to be.

The approach combines both methods: pre-action activations are first mapped into a sparse feature basis via an SAE, then read out by two task-specific probes—the Tool-Need Probe (binary: tool call vs. no tool call) and the Tool-Risk Probe (ternary: low/medium/high risk).

The researchers trained the probes on multi-step trajectories from the NVIDIA Nemotron function-calling dataset and applied the same workflow to GPT-OSS 20B and Gemma 3 27B models. This approach helps surface deeper causes of agent failure, especially in long-horizon runs where an early mistake can reshape the rest of the agentic interaction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81fa5c67-c72e-4c88-aa22-3036398326a9",
  "isSidechain": false,
  "promptId": "14b469ab-1910-4e37-ad22-9c281ad2e6b6",
  "type": "user",
  "uuid": "43ad2508-f108-4c71-aef3-9a451949cb0a",
  "toolUseResult": {
    "query": "\"Beyond the Black Box\" interpretability agentic AI tool use 2605.06890 SAE probes multi-step",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JjaEjtRLqgtbSA2YCANEAe",
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
            "title": "Beyond the black box: How agentic AI is redefining explainability - SAS Voices",
            "url": "https://blogs.sas.com/content/sascom/2025/03/24/beyond-the-black-box-how-agentic-ai-is-redefining-explainability/"
          },
          {
            "title": "Deploying Interpretability to Production with Rakuten: SAE Probes for PII Detection",
            "url": "https://www.goodfire.ai/research/rakuten-sae-probes-for-pii-detection"
          },
          {
            "title": "Beyond Black-Box Benchmarking: Observability, Analytics, and Optimization of Agentic Systems",
            "url": "https://arxiv.org/html/2503.06745v1"
          },
          {
            "title": "Bridging the Black Box: A Survey on Mechanistic Interpretability in AI | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3787104"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the research is about:\n\nThe paper \"Beyond the Black Box: Interpretability of Agentic AI Tool Use\" (arXiv 2605.06890) addresses tool-use failures in AI agents, which can manifest as skipping required tool calls, invoking tools unnecessarily, or taking actions whose consequences only become visible after execution.\n\nThe research introduces a mechanistic-interpretability toolkit built on Sparse Autoencoders (SAEs) and linear probes. The framework reads model states before each action and infers both whether a tool is needed and how consequential the next tool action is likely to be.\n\nThe approach combines both methods: pre-action activations are first mapped into a sparse feature basis via an SAE, then read out by two task-specific probes—the Tool-Need Probe (binary: tool call vs. no tool call) and the Tool-Risk Probe (ternary: low/medium/high risk).\n\nThe researchers trained the probes on multi-step trajectories from the NVIDIA Nemotron function-calling dataset and applied the same workflow to GPT-OSS 20B and Gemma 3 27B models. This approach helps surface deeper causes of agent failure, especially in long-horizon runs where an early mistake can reshape the rest of the agentic interaction."
    ],
    "durationSeconds": 11.734397616999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "81fa5c67-c72e-4c88-aa22-3036398326a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-19T18:35:30.512Z_

Now I have sufficient research data to make my evaluation. Let me note a critical venue mismatch issue and then provide the full assessment.

---

```
【阶段】: Triage
```

## ⚠️ 前置警告：严重的投稿目标不匹配

在进行 idea 质量评估之前，必须指出一个**致命的投稿策略问题**：**这篇 proposal 与 CoRL 2026 的投稿范围完全不匹配。**

CoRL（Conference on Robot Learning）明确要求论文聚焦于"机器学习在机器人中的应用"，涵盖机器人感知、控制、操作、导航、运动等主题，且**"submissions without a robotics focus will be returned without review"**（无机器人焦点的投稿将不经审稿直接退回）。

本 proposal 研究的是 LLM 多轮对话中 tool-selection 推理的忠实性（faithfulness），属于 **NLP/AI interpretability/alignment** 方向，与机器人学习没有任何实质性联系。这篇文章应该投向 **NeurIPS、ICML、ICLR、ACL、EMNLP** 等会议，而非 CoRL。

**如果坚持投 CoRL，中稿概率接近 0%（desk reject）。** 以下评估基于 idea 本身的质量进行，假设投向一个合适的 venue（如 NeurIPS 2026 或 EMNLP 2026）。

---

```
【领域调研】:

- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990) (arXiv 2026/05): 
  本 proposal 最核心的前序工作。对 12 个模型 (270M-27B) 进行 probing，发现 tool identity 在 pre-generation activations 中线性可读且可 steer（4B+ 模型 93-100%），但明确指出 multi-turn 场景下 steering "fragile"（-30 到 +10pp）。Proposal 准确引用了该工作，并以其 multi-turn 局限性作为核心动机。

- [RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention](https://arxiv.org/abs/2602.17053) (arXiv 2026/02): 
  7,186 实例的 counterfactual intervention benchmark，发现 ~49.7% 的推理输出不忠实，主要集中于 stance inconsistency。但仅针对 math/code 等 reasoning tasks，不涉及 tool selection。Proposal 准确引用。

- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?](https://arxiv.org/abs/2603.22582) (arXiv 2026/03): 
  测试 12 个开源推理模型，发现 faithfulness rates 39.7%-89.9%，thinking-token vs. answer-text acknowledgment 有 59pp gap。但仅针对 MMLU/GPQA QA 任务，非 agentic tool selection。Proposal 准确引用。

- [LLM Agents Already Know When to Call Tools — Even Without Reasoning](https://arxiv.org/abs/2605.09252) (arXiv 2026/05): 
  提出 When2Tool benchmark（18 environments），用 hidden state probing 分析 tool-necessity 判断，AUROC 0.89-0.96。聚焦 binary tool-necessity（是否需要 tool），非 tool identity faithfulness。Proposal 准确引用。

- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890) (arXiv 2026/05): 
  SAE + linear probes 对 multi-step trajectories 进行 tool-need/tool-risk 分类，但不涉及 tool identity 或 faithfulness。Proposal 准确引用并正确区分了其范围。

- [Verify Before You Commit (SAVeR)](https://arxiv.org/abs/2604.08401) (arXiv 2026/04): 
  提出 self-auditing 提高 agent faithfulness，但以方法论为主，实证分析有限。Proposal 正确引用。

- [Tool Preferences in Agentic LLMs are Unreliable](https://arxiv.org/abs/2505.18135) (EMNLP 2025): 
  发现 tool selection 在 description manipulation 下脆弱，但不研究 CoT faithfulness。

- [Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents](https://arxiv.org/abs/2605.17641) (arXiv 2026/05): 
  对 long-horizon agent 的 memory selection 应用 causal intervention，但针对 memory 非 tool selection。属于 causal intervention 方法论在 agent 中的应用，与 proposal 有方法论上的交叠但研究对象不同。

- 调研总结：CoT faithfulness 领域在 2026 年上半年经历了快速发展，single-turn 场景下 reasoning faithfulness（RFEval）和 tool-call probing（2605.07990, 2605.09252）已被较好地 characterize。但"multi-turn agentic tool selection 的 CoT faithfulness"确实是一个明确的空白——现有工作要么是 single-turn probing，要么是 general reasoning faithfulness，要么是 tool robustness 而非 faithfulness。Proposal 对这一 gap 的定位是准确的。
```

```
【Trivial Alternative 检验】:

有两个需要严肃考虑的 trivial alternative：

1. **直接扩展 2605.07990 的 probing 方法到 multi-turn**：2605.07990 已经做了 single-turn tool identity probing 并尝试了 multi-turn（虽然结果 fragile）。一个 trivial baseline 是简单地在更大规模、更多模型上重跑 2605.07990 的 multi-turn steering 实验，而不需要构建新 benchmark 和新的 behavioral intervention protocol。但 proposal 的增量价值在于：(a) 它不仅做 mechanistic probing，还引入了 behavioral causal interventions（reason-flip/ablate/inject/scramble），这是 probing 无法替代的——probing 只告诉你"tool identity 是否预先编码"，不告诉你"CoT reasoning 是否 causally drive 了 tool selection"；(b) 它引入了 ambiguity stratification（三个 difficulty tiers），这解决了 construct validity 问题。

2. **直接将 RFEval 的 counterfactual intervention framework 应用到 tool-call scenarios**：RFEval 已有成熟的 counterfactual intervention 方法论。一个更简单的做法是直接复用 RFEval 的 framework，将其 task domain 替换为 tool selection scenarios。Proposal 在某种程度上就是这样做的——它的四种 intervention 类型与 RFEval 的方法论高度同构。增量价值在于：(a) multi-turn context 带来的技术挑战（accumulated history, error feedback）是 RFEval 的 single-turn framework 无法直接处理的；(b) 三级难度分层是针对 tool selection ambiguity 的独特设计；(c) probing + behavioral 双重验证提供了比纯 behavioral 更深的 insight。

**判断**：trivial alternative 威胁存在但不致命。核心增量价值在于 "multi-turn + tool-selection + behavioral + mechanistic 四者结合"，单独拆开任何一条都有更简单的替代方案，但组合起来形成了一个目前不存在的系统性研究。问题在于这个组合的增量价值是否足够显著——见下方 Novelty 评估。
```

```
【前提假设检验】:

核心 claim 的逻辑链条中有以下未经验证的前提假设：

1. **"Multi-turn 场景下 faithfulness 的表现与 single-turn 会有 qualitatively different 的 pattern"** — 这是整篇论文存在意义的核心假设。如果 multi-turn 的结果只是 single-turn 结果的 noisy 版本（量变而非质变），那这篇论文的 significance 会大幅缩水。2605.07990 报告的 multi-turn steering "fragile" 结果提供了一定支撑，但 "fragile" 可能只意味着 "same mechanism, noisier signal"，而非 "fundamentally different mechanism"。这个假设需要实验验证，无法先验判断。

2. **"Behavioral causal interventions（reason-flip etc.）能有效衡量 causal coupling"** — 四种 intervention 隐含了一个关键假设：当你 flip/ablate/inject/scramble CoT reasoning 时，模型会像人一样"读取"这些 reasoning 来做 tool selection。但如果模型的 tool selection 主要由 prompt context（而非 CoT）驱动，那所有 intervention 都只是在测试"模型是否会被注入的 CoT 所误导"，而非"模型的 CoT 是否忠实反映了其决策过程"。这是一个深层的 methodological concern——behavioral intervention 方法测量的是 "CoT 对决策的 causal influence"，但 "causal influence" 和 "faithfulness" 之间有微妙区别。RFEval 面临同样的问题但已被社区接受。

3. **"Hard-Ambiguous 场景会 elicit more faithful reasoning" 的反直觉假设** — 这是 proposal 中最有趣的假设，但其前提是 "genuine deliberation → more faithful CoT"。这个因果链条未必成立：模型可能在 hard-ambiguous 场景下更不确定，从而产生更多 post-hoc rationalization 来 justify 一个本质上随机的选择。这个假设的方向性不确定，作为研究假设是合理的，但 proposal 倾向于将其呈现为"反直觉预测"而非"开放问题"。

4. **600 scenarios × 5 domains 的 benchmark 规模足以支撑 7 个模型 × 3 tiers × 4 intervention types 的实验矩阵** — 每个 cell 只有约 200/5 = 40 个 scenarios per domain per tier per model，统计 power 是否足够支撑 reliable 结论需要验证。
```

```
【3 维度打分】:

1. Novelty: 【中】
   
   理由：Proposal 正确识别了一个真实的研究空白——multi-turn agentic tool selection 的 CoT faithfulness 确实没有被系统研究过。2605.07990 明确指出 multi-turn 是 unsolved，RFEval/Lie to Me/FACT-E 均不涉及 tool selection。这个 gap 是真实的。
   
   但 novelty 的"增量"需要审慎评估：
   - **方法论层面**：四种 behavioral intervention（reason-flip, ablate, inject, scramble）与 RFEval 的 counterfactual intervention 方法论高度同构，不是全新方法。TSCF 和 RTI 两个 metrics 本质上是 "tool call follows/ignores intervened reasoning" 的正反面，不是 conceptually novel 的度量。
   - **Probing 层面**：将 2605.07990 的 linear probing 从 single-turn 扩展到 multi-turn 是自然的 next step，四个新分析（cross-turn transfer, encoding drift, error replanning, faithfulness coupling）有一定技术新意，但更像是 "engineering extension" 而非 "conceptual breakthrough"。
   - **Benchmark 层面**：三级难度分层（Unambiguous / Soft-Ambiguous / Hard-Ambiguous）是合理的设计，但 benchmark 构建本身不构成核心 novelty。
   
   总体来说，这是一个 "well-identified gap + systematic investigation with existing methodologies adapted to a new domain" 的工作。Novelty 主要在于 **problem identification 和 systematic combination**，而非方法论创新。在 top venue 中，这种 "first systematic study of X" 类型的工作如果做得好是可以接受的，但审稿人可能会质疑 "is this sufficiently novel or just a natural extension?"

2. Significance: 【中偏强】
   
   理由：研究问题的重要性是真实的——multi-turn agent 在 production 中的部署越来越广泛，tool-selection faithfulness 直接关系到 agent 的可信度、安全性和可调试性。如果一个 agent 的 CoT 是 "reasoning theater"，那基于 CoT 的 monitoring/safety 机制（如 SAVeR 2604.08401 和 Noticing the Watcher 2603.16928 所讨论的）将失效。
   
   但 significance 有上限：
   - 这是一个 **empirical characterization** 工作，不提出新方法来解决 unfaithfulness。即使结果发现 50% 的 multi-turn tool-selection reasoning 是 unfaithful，论文的贡献止于 "diagnosing the problem"，不提供 "fix"。
   - 结果的可推广性取决于 benchmark 的代表性——600 scenarios across 5 domains 是否能代表真实 production agent 的 tool selection 分布存疑。
   - "如果核心发现是 positive（high faithfulness），审稿人会说 surprising 吗？" 大概率不会——given 2605.07990 的 multi-turn steering fragility 和 RFEval 的 50% unfaithfulness，multi-turn tool selection 的 faithfulness 同样 problematic 是 **expected**，不是 surprising。"如果发现 hard-ambiguous 比 unambiguous 更 faithful？" 这才 surprising，但 proposal 只是提出了这个假设而非提供了初步证据。

3. Related Work: 【强】
   
   理由：这是 proposal 最大的优势。Related work 覆盖极为全面，清晰地组织为四个 converging threads，每个引用都准确且与 proposal 的关系被正确标注（经调研验证：2605.07990、RFEval、Lie to Me、2605.09252、2605.06890 等核心论文的描述均准确）。Gap 的定位精准且有充分文献支撑。唯一可补充的是 2605.17641（Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents）作为方法论上的 adjacent work。
```

```
【概率估计】: [20% - 35%] 中位 27%

（注：此概率基于投向合适 venue 如 NeurIPS/EMNLP。若投 CoRL，概率 ~0% due to scope mismatch。）
```

```
【估计理由】:

Novelty 是中等——gap 真实但填补方式主要是 existing methodologies 的 systematic combination 和 domain extension，缺乏方法论上的 conceptual leap。Significance 中偏强——问题确实重要，但作为 empirical characterization 而非 solution，impact 有天花板。Related work 做得好，但好的 related work survey 是 necessary condition 不是 sufficient condition。

限制上界的主要维度是 **Novelty**：审稿人很可能认为这是 "a natural next step that combines RFEval-style interventions with 2605.07990-style probing in multi-turn settings"，methodology contribution 有限。Proposal 试图通过大量实验（7 models × 3 tiers × 4 interventions + probing）来弥补方法论 novelty 的不足，但这是 execution 能提升的部分，不改变 idea 内核。

核心预测（multi-turn faithfulness 比 single-turn 更差）如果被验证，审稿人可能说 "expected given prior work"。只有 "hard-ambiguous → more faithful" 这个假设如果被验证才会达到 "surprising" 的标准，但它只是 5 个假设之一，且方向不确定。

概率范围 20-35% 反映了：
- 下界 20%：如果审稿人认为这主要是 existing methods 的 domain transfer，novelty 不足
- 上界 35%：如果审稿人认可 "first systematic study" 的价值、三级难度分层的设计、以及 behavioral + mechanistic 双重验证的 contribution
```

```
【主要风险】:

1. **"Natural extension" 质疑**：最大的 idea 层面风险。审稿人可能认为 "applying RFEval-style counterfactual interventions to multi-turn tool selection + extending 2605.07990's probing to multi-turn" 是 two straightforward extensions combined，不构成足够的 intellectual contribution。Proposal 需要一个真正的 "aha moment"——目前最接近的是 "hard-ambiguous → more faithful" 假设，但这只是一个待验证的猜想。

2. **核心发现的可预测性**：如果主要结论是 "multi-turn tool-selection CoT is substantially unfaithful, more so than single-turn"，这与现有文献的预期高度一致（2605.07990 的 multi-turn fragility + RFEval 的 50% unfaithfulness + Lie to Me 的 thinking-output gap），审稿人可能认为 contribution 是 confirming the expected 而非 discovering the unexpected。
```

Sources:
- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990)
- [RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention](https://arxiv.org/abs/2602.17053)
- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?](https://arxiv.org/abs/2603.22582)
- [LLM Agents Already Know When to Call Tools — Even Without Reasoning](https://arxiv.org/abs/2605.09252)
- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890)
- [Verify Before You Commit (SAVeR)](https://arxiv.org/abs/2604.08401)
- [Tool Preferences in Agentic LLMs are Unreliable](https://arxiv.org/abs/2505.18135)
- [Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents](https://arxiv.org/abs/2605.17641)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43ad2508-f108-4c71-aef3-9a451949cb0a",
  "isSidechain": false,
  "requestId": "req_011CbCQbk8UheTL7xbNAFnoZ",
  "type": "assistant",
  "uuid": "f5ed62bc-998d-4ec8-94ab-ded64751b002",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019uWgd8DTNyLNFRhrVyQYJ6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 759,
      "cache_read_input_tokens": 26644,
      "output_tokens": 5302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 759,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5302,
          "cache_read_input_tokens": 26644,
          "cache_creation_input_tokens": 759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 759
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn…",
  "leafUuid": "f5ed62bc-998d-4ec8-94ab-ded64751b002",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate tool-selection faithfulness in multi-turn agents",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn…",
  "leafUuid": "f5ed62bc-998d-4ec8-94ab-ded64751b002",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate tool-selection faithfulness in multi-turn agents",
  "sessionId": "fd8f0a03-d092-491f-8f65-bc44717d9008"
}
```

---
