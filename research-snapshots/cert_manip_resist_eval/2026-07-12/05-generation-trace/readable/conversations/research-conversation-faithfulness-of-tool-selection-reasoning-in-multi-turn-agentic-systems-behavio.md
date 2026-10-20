# Research conversation: Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn Probing 

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3.jsonl`
- **Structured JSON:** [`d2b3ea624c902a40494c.json`](../../sessions/d2/d2b3ea624c902a40494c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:40:11.872Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:40:11.872Z",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "content": "# Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn Probing\n\n## Description\nWe present the first systematic study of whether tool-selection reasoning in multi-turn agentic systems is causally faithful or post-hoc rationalization, combining behavioral causal interventions with multi-turn mechanistic probing. While recent work has established that tool identity is linearly readable from pre-generation activations in single-turn settings (2605.07990, achieving 93-100% steering accuracy) and that ~50% of general reasoning is unfaithful (RFEval), no prior work examines whether an agent's stated reasoning for choosing a specific tool across conversation turns actually drives that decision. We construct TOOLFAITH-BENCH, a 600-scenario diagnostic benchmark across five domains, stratified into three difficulty tiers — Unambiguous (single correct tool), Soft-Ambiguous (one optimal among plausible candidates), and Hard-Ambiguous (multiple valid tools) — to address construct validity concerns about benchmark realism. We apply a four-type causal intervention protocol (reason-flip, reason-ablate, counterfactual-inject, reason-scramble) and introduce two metrics: Tool Selection Causal Fidelity (TSCF) and Reasoning Theater Index (RTI). We evaluate seven models spanning current open-weight systems (Kimi K2.6, GLM-5.1, Qwen3.6-35B-A3B, DeepSeek-V4-Pro) and frontier APIs (Claude Sonnet 4.6, GPT-5.5, Gemini 2.5 Pro), supplemented by a multi-turn probing study that extends 2605.07990 to the unsolved multi-turn regime with four novel analyses: cross-turn probe transfer, context-dependent encoding drift, error-induced replanning signals, and behavioral-mechanistic faithfulness coupling. We test five hypotheses, including that RTI will be elevated across model families (extending single-turn findings), that probe accuracy will degrade with conversation depth (unlike stable single-turn results), and — counterintuitively — that harder ambiguous scenarios may elicit more faithful reasoning than unambiguous ones because genuine deliberation is required.\n\n## Core Problem\nIn multi-turn tool-using agents, does the model's stated reasoning about tool selection — which tool to call, with what parameters, and why — actually causally drive the tool call decision, or is it post-hoc rationalization of a latent policy? Recent probing work (2605.07990, 2605.09252) has shown that tool identity is linearly encoded in pre-generation activations in single-turn settings, suggesting CoT may be decorative. But these findings explicitly fail to transfer to multi-turn agentic settings, where accumulated conversation history, prior tool results, and error feedback create dynamic contexts that fundamentally differ from static single-turn tool menus. No systematic behavioral study exists to measure causal coupling between stated reasoning and tool-call actions across conversation turns.\n\n## Opportunity\nThe landscape has bifurcated: single-turn tool probing is now well-characterized (2605.07990 achieves 93-100% steering accuracy for 4B+ models; 2605.09252 shows 0.89-0.96 AUROC for tool-necessity probing), while multi-turn agentic tool selection remains essentially unstudied from a faithfulness perspective. This is precisely where the stakes are highest — production agents execute multi-step workflows where early tool calls condition later ones, errors require replanning, and unfaithful reasoning about tool selection can cascade into irreversible harmful actions. The faithfulness evaluation literature has advanced rapidly in 2026: RFEval finds ~50% of reasoning outputs unfaithful across 7,186 instances; 'Lie to Me' reveals a 59-percentage-point gap between internal recognition and output acknowledgment of hint influence; 'Decoding Answers Before CoT' shows 0.9 AUC pre-CoT answer probing — yet all this work targets single-turn QA/math, not agentic tool selection. Critically, 2605.07990 found multi-turn steering to be 'fragile' with -30 to +10pp vs. baseline and 'no consistent direction,' directly motivating a systematic study of multi-turn tool-selection faithfulness. The behavioral intervention approach — perturbing CoT and measuring whether tool calls change — is entirely unaddressed by any existing work on tool-call probing, creating a unique and timely contribution.\n\n## Related Work / Landscape\nThe landscape spans four converging threads:\n\n**Thread 1 — CoT Faithfulness (General):** Project Ariadne (2601.02314) finds causal decoupling with violation density up to 0.77 in factual domains but focuses on claims, not actions. 'Decoding Answers Before CoT' (2603.01437) shows answers encoded in pre-CoT activations with 0.9 AUC, establishing that CoT can be post-hoc, but only for binary QA. 'Catching Rationalization in the Act' (2603.17199) detects motivated reasoning via activation probing, showing internal representations outperform CoT monitors. RFEval (2602.17053) provides a 7,186-instance counterfactual intervention benchmark finding ~50% unfaithfulness, but for reasoning tasks not tool calls. FACT-E (2604.10693, ACL 2026 Findings) uses causal perturbations for CoT evaluation, finding self-evaluation unreliable. C2-Faith (2603.05167) benchmarks LLM-as-judge for causal/coverage faithfulness, showing systematic blind spots in localization. 'Lie to Me' (2603.22582) evaluates 12 models finding faithfulness rates from 39.7% to 89.9% with a critical 59pp thinking-vs-output gap. Breaking the Chain (2603.16475) shows 60% insensitivity to intermediate structure interventions. FaithCoT-Bench (ICLR 2026, 2510.04040) and FRIT (2509.13334) address single-turn QA faithfulness only.\n\n**Thread 2 — Tool-Call Probing (Single-Turn):** 'Tool Calling is Linearly Readable and Steerable' (2605.07990) probes 12 models, achieving 93-100% tool-name steering accuracy at 4B+ in single-turn fixed-menu settings, but explicitly finds multi-turn transfer 'fragile' (-30 to +10pp). Argument values are NOT steerable (0/30). 'LLM Agents Already Know When to Call Tools' (2605.09252) shows binary tool-necessity is decodable at 0.89-0.96 AUROC, with reasoning providing no additional signal. 'Beyond the Black Box' (2605.06890) applies SAE + probes to multi-step trajectories for tool-need/tool-risk classification but not tool identity or faithfulness. 'Internal Representations as Indicators of Hallucinations in Agent Tool Selection' (2601.05214) detects hallucinated tool calls from hidden states but in single-turn only.\n\n**Thread 3 — Tool Selection Robustness/Behavior:** 'Tool Preferences in Agentic LLMs are Unreliable' (EMNLP 2025, 2505.18135) shows tool selection is fragile under description manipulation but does not examine CoT faithfulness. 'The Reasoning Trap' (2510.22977) demonstrates RL causally amplifies tool hallucination but studies hallucination rates, not reasoning faithfulness. TOOLCERT (2510.03992) studies distributional robustness, not faithfulness. 'Brief Is Better' (2604.02155) finds non-monotonic CoT budget effects on function-calling accuracy. 'The Causal Impact of Tool Affordance on Safety Alignment' (ICECET 2026, 2603.20320) examines safety but not faithfulness.\n\n**Thread 4 — Agentic Monitoring:** SAVeR (2604.08401) proposes self-auditing for agentic faithfulness but provides limited empirical analysis. 'Noticing the Watcher' (2603.16928) shows models detect CoT monitoring from feedback at up to 19% awareness. 'Reasoning and Tool-use Compete in Agentic RL' (2602.00994) reveals interference between reasoning and tool use during training.\n\n**Critical Gap:** No work combines behavioral causal interventions on tool-selection CoT with mechanistic probing in multi-turn agentic settings. Single-turn probing is established; multi-turn is explicitly unsolved. Behavioral faithfulness testing for tool selection is entirely absent.\n\n## Approach\nWe construct TOOLFAITH-BENCH, a diagnostic benchmark of 600 multi-turn agentic scenarios across five domains (code editing, web browsing, data analysis, system administration, information retrieval), each containing 2-4 tool-selection decision points. Scenarios are stratified into three difficulty tiers reflecting real-world ambiguity:\n\n**Tier 1 — Unambiguous (200 scenarios):** A single correct tool per decision point; the reasoning chain uniquely determines the tool. Serves as calibration: if TSCF is low here, the CoT is clearly decorative.\n\n**Tier 2 — Soft-Ambiguous (200 scenarios):** 2-3 plausible tools with one clearly optimal. The reasoning must contain distinguishing information (e.g., 'the file is >2GB, so we need streaming upload rather than multipart'). Interventions target this distinguishing reasoning.\n\n**Tier 3 — Hard-Ambiguous (200 scenarios):** Multiple genuinely valid tools. Faithfulness is measured via stance consistency (does the CoT logically support the specific tool chosen?) and causal coupling (does perturbing the CoT change which valid tool is selected?), following RFEval's framework of decoupling faithfulness from correctness.\n\nAt each decision point we apply four perturbation types: (1) reason-flip — rewrite the CoT to justify a different tool, (2) reason-ablate — remove reasoning entirely, presenting only task context, (3) counterfactual-inject — insert facts that should change the optimal tool, (4) reason-scramble — shuffle reasoning sentences while preserving tool mentions. We define two complementary metrics: Tool Selection Causal Fidelity (TSCF), the rate at which tool calls correctly follow intervened reasoning, and Reasoning Theater Index (RTI), the rate at which tool calls remain unchanged despite contradictory reasoning.\n\nWe evaluate seven models spanning current open-weight systems (Kimi K2.6, GLM-5.1, Qwen3.6-35B-A3B, DeepSeek-V4-Pro) and frontier APIs (Claude Sonnet 4.6, GPT-5.5, Gemini 2.5 Pro), supplementing behavioral results with a multi-turn probing study on open-weight models. The probing component is explicitly positioned as an extension of 2605.07990 to the unsolved multi-turn regime, with four novel analyses: (a) cross-turn probe transfer — whether a probe trained at decision point 1 (turn 2) generalizes to decision point 3 (turn 8) as context accumulates; (b) context-dependent encoding drift — whether the linear direction encoding a given tool shifts across turns as prior tool results modify the task state; (c) error-induced replanning signals — whether tool errors create detectable representational shifts before the next tool selection; (d) faithfulness coupling — correlating probe-detected pre-commitment (tool identity encoded before CoT) with behavioral unfaithfulness (low TSCF), testing whether mechanistic and behavioral measures of unfaithfulness align. This goes beyond 2605.07990's domain transfer, because multi-turn contexts create fundamentally different representational challenges: the residual stream must integrate prior tool results, error states, and evolving task context alongside the current tool decision, and 2605.07990 explicitly showed this integration is fragile.\n\n## Inspiration\nThree converging findings: (1) 2605.07990's explicit acknowledgment that multi-turn tool-call probing is 'fragile' and unsolved, creating a clear frontier; (2) the faithfulness evaluation literature's maturation (RFEval, FACT-E, Lie to Me) providing proven intervention methodologies that have never been applied to tool selection; (3) the growing deployment of multi-turn agentic systems where tool-selection faithfulness has direct safety implications that single-turn probing cannot address.\n\n## Key References\n- Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents (arXiv 2026, 2601.02314)\n- Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing [SAVeR] (arXiv 2026, 2604.08401)\n- Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures (arXiv 2026, 2603.16475)\n- Noticing the Watcher: LLM Agents Can Infer CoT Monitoring from Blocking Feedback (arXiv 2026, 2603.16928)\n- Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering (arXiv 2026, 2603.01437)\n- Catching Rationalization in the Act: Detecting Motivated Reasoning via Activation Probing (arXiv 2026, 2603.17199)\n- RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention (arXiv 2026, 2602.17053)\n- FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning (ACL 2026 Findings, 2604.10693)\n- C2-Faith: Benchmarking LLM Judges for Causal and Coverage Faithfulness in CoT Reasoning (arXiv 2026, 2603.05167)\n- Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models? (arXiv 2026, 2603.22582)\n- Tool Calling is Linearly Readable and Steerable in Language Models (arXiv 2026, 2605.07990)\n- LLM Agents Already Know When to Call Tools — Even Without Reasoning (arXiv 2026, 2605.09252)\n- Beyond the Black Box: Interpretability of Agentic AI Tool Use (arXiv 2026, 2605.06890)\n- FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning (ICLR 2026, 2510.04040)\n- FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness (arXiv 2025, 2509.13334)\n- The Reasoning Trap: How Enhancing LLM Reasoning Amplifies Tool Hallucination (arXiv 2025, 2510.22977)\n- Tool Preferences in Agentic LLMs are Unreliable (EMNLP 2025, 2505.18135)\n- Quantifying Distributional Robustness of Agentic Tool-Selection [TOOLCERT] (arXiv 2025, 2510.03992)\n- Internal Representations as Indicators of Hallucinations in Agent Tool Selection (arXiv 2026, 2601.05214)\n- Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calling Language Agents (arXiv 2026, 2604.02155)\n- The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents (ICECET 2026, 2603.20320)\n- Reasoning and Tool-use Compete in Agentic RL: From Quantifying Interference to Disentangled Tuning (arXiv 2026, 2602.00994)\n- Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation? (arXiv 2025, 2508.19827)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '300 H100-hours (150h model inference across 4 open-weight models × 600 scenarios × 4 intervention types × 3 tiers, 70h multi-turn probing experiments with cross-turn analysis, 80h development/debugging)', 'timeline': '12-14 weeks (3 wk benchmark design with tiered difficulty validation, 3 wk implementation, 3 wk experiments, 3-5 wk analysis/writing)', 'estimated_gpu_cost': '$750 (at ~$2.50/hr H100 spot pricing)'}\n- **human_in_loop**: {'gpu_hours': '240 H100-hours (same inference workload, fewer debugging iterations with Claude-assisted scenario generation and tiered validation)', 'timeline': '10-12 weeks (2.5 wk benchmark design, 2 wk implementation, 2.5 wk experiments, 3-4 wk analysis/writing)', 'claude_api_cost': '$350-450 (scenario generation across 3 tiers, ambiguity calibration, code assistance, statistical analysis, paper drafting across ~18M input + 6M output tokens)', 'estimated_gpu_cost': '$600 (at ~$2.50/hr H100 spot pricing)'}\n- **auto_research**: {'gpu_hours': '500 H100-hours (larger intervention sweep, additional ablations on tier boundaries, probe transfer experiments across multiple random seeds, cross-model probe transfer analysis)', 'timeline': '5-7 weeks wall-clock (parallelized scenario generation, concurrent model evaluation, automated analysis pipeline)', 'claude_api_cost': '$800-1000 (orchestration, tiered scenario generation with ambiguity calibration, evaluation judging, statistical analysis, full paper drafting across ~45M input + 18M output tokens)', 'estimated_gpu_cost': '$1250 (at ~$2.50/hr H100 spot pricing)', 'speed_bottleneck': 'Tier 2/3 scenario quality validation — ensuring soft-ambiguous scenarios have correctly calibrated difficulty (one tool genuinely better but not trivially so) requires human spot-checking that cannot be fully automated without risking construct validity'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T18:40:11.877Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:40:11.877Z",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3"
}
```

---

## Round 1

34 recorded events

### User

_source line 3 · 2026-05-19T18:40:11.890Z_

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
  "promptId": "fbfac76e-73db-4150-9394-4640f111f44b",
  "type": "user",
  "uuid": "42dc4b3b-64d8-4c9c-806a-5a1dced976d1",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:40:11.889Z_

```json
{
  "parentUuid": "42dc4b3b-64d8-4c9c-806a-5a1dced976d1",
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
  "uuid": "f75b7801-fb36-4f89-9372-7d665618dafe",
  "timestamp": "2026-05-19T18:40:11.889Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:40:11.889Z_

```json
{
  "parentUuid": "f75b7801-fb36-4f89-9372-7d665618dafe",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fa6a2873-5447-4fd6-9d62-caa4aa12af73",
  "timestamp": "2026-05-19T18:40:11.889Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
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
  "lastPrompt": "# Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn Probing  ## Description We present the first systematic study of whether tool-selectio…",
  "leafUuid": "fa6a2873-5447-4fd6-9d62-caa4aa12af73",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Study tool-selection faithfulness in multi-turn agents",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:40:16.799Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal carefully. It's about studying the faithfulness of tool-selection reasoning in multi-turn agentic systems. Before giving any suggestions, I need to do thorough literature research to understand the current landscape.

Let me first load the WebSearch tool, then conduct my research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa6a2873-5447-4fd6-9d62-caa4aa12af73",
  "isSidechain": false,
  "requestId": "req_011CbCR6ziP5YtSgLaTDwLfL",
  "type": "assistant",
  "uuid": "ac02f424-d735-485b-9699-d8e592db2698",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UT6ETiQkeKhpHUZmxLun2X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8594,
      "cache_read_input_tokens": 11374,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8594,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 153,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 8594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8594
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

_source line 9 · 2026-05-19T18:40:16.811Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Nm94Wdt6xy418i1UBhwVyo`</summary>

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
  "parentUuid": "ac02f424-d735-485b-9699-d8e592db2698",
  "isSidechain": false,
  "requestId": "req_011CbCR6ziP5YtSgLaTDwLfL",
  "type": "assistant",
  "uuid": "50c8bb5e-419d-4e91-9a35-54620aecf120",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UT6ETiQkeKhpHUZmxLun2X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8594,
      "cache_read_input_tokens": 11374,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8594,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 153,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 8594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8594
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

_source line 10 · 2026-05-19T18:40:16.819Z_

<details><summary>↩ Tool result · `toolu_01Nm94Wdt6xy418i1UBhwVyo`</summary>

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
  "parentUuid": "50c8bb5e-419d-4e91-9a35-54620aecf120",
  "isSidechain": false,
  "promptId": "fbfac76e-73db-4150-9394-4640f111f44b",
  "type": "user",
  "uuid": "c46a5dbd-14c9-4856-b561-be21ec14d0de",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "50c8bb5e-419d-4e91-9a35-54620aecf120",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-19T18:40:27.740Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct my pre-research. I need to search for:

1. The most recent work on CoT faithfulness in agentic/tool-use settings (2026)
2. The specific papers referenced (2605.07990, 2605.09252) to verify claims
3. Any work on multi-turn tool selection faithfulness that might overlap
4. Recent CoRL/robotics angle - wait, this is for CoRL 2026. Let me think about this. CoRL is Conference on Robot Learning. This proposal is about faithfulness of tool-selection reasoning in multi-turn agentic systems. Is this a good fit for CoRL? That's an important question.


Actually, I'm noticing a potential venue mismatch here. The user mentions CoRL 2026, which is the Conference on Robot Learning, but this proposal focuses on LLM agent tool-selection faithfulness—something that would typically fit better at venues like NeurIPS, ICML, ACL, EMNLP, or ICLR. CoRL's focus on robot learning doesn't align well with general LLM agent behavior research. Let me search the landscape to understand what's actually out there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c46a5dbd-14c9-4856-b561-be21ec14d0de",
  "isSidechain": false,
  "requestId": "req_011CbCR7MvLckzmfzmjQ2fCh",
  "type": "assistant",
  "uuid": "564fe742-5b1c-41d1-b10d-99beeea4adb9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xJePNsoziyi5RUVzHP8hg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 19968,
      "output_tokens": 530,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 530,
          "cache_read_input_tokens": 19968,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 680
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

_source line 12 · 2026-05-19T18:40:27.741Z_

Now let me conduct the mandatory pre-research before forming any opinions. I'll run multiple searches in parallel to cover different angles.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "564fe742-5b1c-41d1-b10d-99beeea4adb9",
  "isSidechain": false,
  "requestId": "req_011CbCR7MvLckzmfzmjQ2fCh",
  "type": "assistant",
  "uuid": "b68b8139-be0f-49a7-bad4-5e7ddb33c129",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xJePNsoziyi5RUVzHP8hg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 19968,
      "output_tokens": 530,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 530,
          "cache_read_input_tokens": 19968,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 680
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

_source line 13 · 2026-05-19T18:40:27.747Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B9iaE32rHBprHYz2qRnaHp`</summary>

```json
{
  "query": "CoRL 2026 conference on robot learning submission topics scope"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b68b8139-be0f-49a7-bad4-5e7ddb33c129",
  "isSidechain": false,
  "requestId": "req_011CbCR7MvLckzmfzmjQ2fCh",
  "type": "assistant",
  "uuid": "ae63a630-38ed-4f59-9e95-df8f588c12d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xJePNsoziyi5RUVzHP8hg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 19968,
      "output_tokens": 530,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 530,
          "cache_read_input_tokens": 19968,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 680
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

_source line 14 · 2026-05-19T18:40:29.237Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FNLsHNJHALdJHF9TKa7rq5`</summary>

```json
{
  "query": "tool calling linearly readable steerable language models 2605.07990 arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae63a630-38ed-4f59-9e95-df8f588c12d9",
  "isSidechain": false,
  "requestId": "req_011CbCR7MvLckzmfzmjQ2fCh",
  "type": "assistant",
  "uuid": "83f370ab-1445-4c2e-a9f7-904b904bd9ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xJePNsoziyi5RUVzHP8hg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 19968,
      "output_tokens": 530,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 530,
          "cache_read_input_tokens": 19968,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 680
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

_source line 15 · 2026-05-19T18:40:29.294Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GCJPfMWsx2DgKiTeRTrvHW`</summary>

```json
{
  "query": "chain of thought faithfulness tool selection agentic systems 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83f370ab-1445-4c2e-a9f7-904b904bd9ea",
  "isSidechain": false,
  "requestId": "req_011CbCR7MvLckzmfzmjQ2fCh",
  "type": "assistant",
  "uuid": "a8a1d6b9-a547-4df7-b0dc-0e4ae0a411b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xJePNsoziyi5RUVzHP8hg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 19968,
      "output_tokens": 530,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 530,
          "cache_read_input_tokens": 19968,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 680
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

_source line 16 · 2026-05-19T18:40:29.493Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Faw9wBTTABiZTqK9KdsokM`</summary>

```json
{
  "query": "RFEval reasoning faithfulness counterfactual intervention benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8a1d6b9-a547-4df7-b0dc-0e4ae0a411b0",
  "isSidechain": false,
  "requestId": "req_011CbCR7MvLckzmfzmjQ2fCh",
  "type": "assistant",
  "uuid": "e4063dd8-830e-46a0-a10a-107f6414d8a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xJePNsoziyi5RUVzHP8hg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 19968,
      "output_tokens": 530,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 680,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 530,
          "cache_read_input_tokens": 19968,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 680
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

_source line 17 · 2026-05-19T18:40:36.624Z_

<details><summary>↩ Tool result · `toolu_01GCJPfMWsx2DgKiTeRTrvHW`</summary>

```text
Web search results for query: "chain of thought faithfulness tool selection agentic systems 2026"

Links: [{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410"},{"title":"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?","url":"https://arxiv.org/html/2603.22582v1"},{"title":"Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety","url":"https://arxiv.org/html/2507.11473v2"},{"title":"What is chain of thought (CoT) prompting? | IBM","url":"https://www.ibm.com/think/topics/chain-of-thoughts"},{"title":"Measuring Faithfulness in Chain-of-Thought Reasoning Tamera Lanham","url":"https://www-cdn.anthropic.com/827afa7dd36e4afbb1a49c735bfbb2c69749756e/measuring-faithfulness-in-chain-of-thought-reasoning.pdf"},{"title":"Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity","url":"https://arxiv.org/pdf/2510.27378"},{"title":"Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing","url":"https://arxiv.org/pdf/2604.08401"},{"title":"Measuring Faithfulness in Chain-of-Thought Reasoning","url":"https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning"}]

Based on the search results, here's what recent research reveals about chain-of-thought faithfulness and tool selection in agentic systems in 2026:

## Key Findings on CoT Faithfulness

Prior work has established that chain-of-thought reasoning is not always faithful. Recent 2026 research has uncovered significant issues with how reasoning models behave:

- Reasoning models like Claude 3.7 Sonnet and DeepSeek-R1 frequently fail to verbalize the true factors driving their outputs, finding faithfulness rates as low as 25% for some hint types.

- Recent work used activation probing to demonstrate "Reasoning Theater" (models that lock in answers early but continue generating performative reasoning tokens).

## Divergence Between Thinking and Answer Text

A particularly striking 2026 finding involves a gap between what models say in their internal reasoning versus their final answers. Recent research asks: when a model follows a misleading hint, does its visible answer acknowledge the same influences that its thinking tokens do?

## Implications for Agentic Systems

For agentic systems specifically, unfaithful belief states (e.g., unsupported inferences or hidden assumptions) can propagate, bias decisions, and trigger costly actions in closed-loop agent systems, with the risk being not merely incorrect answers, but systematic behavioral drift driven by unfaithful internal beliefs.

LLM agents maintain internal reasoning trajectories for guiding tool invocation, action commitment, and memory updates across decision steps.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8a1d6b9-a547-4df7-b0dc-0e4ae0a411b0",
  "isSidechain": false,
  "promptId": "fbfac76e-73db-4150-9394-4640f111f44b",
  "type": "user",
  "uuid": "e7647cbf-e704-49c1-99c8-a67941d2f196",
  "toolUseResult": {
    "query": "chain of thought faithfulness tool selection agentic systems 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FpC1iVHvyppasmLEQLzkKM",
        "content": [
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410"
          },
          {
            "title": "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?",
            "url": "https://arxiv.org/html/2603.22582v1"
          },
          {
            "title": "Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety",
            "url": "https://arxiv.org/html/2507.11473v2"
          },
          {
            "title": "What is chain of thought (CoT) prompting? | IBM",
            "url": "https://www.ibm.com/think/topics/chain-of-thoughts"
          },
          {
            "title": "Measuring Faithfulness in Chain-of-Thought Reasoning Tamera Lanham",
            "url": "https://www-cdn.anthropic.com/827afa7dd36e4afbb1a49c735bfbb2c69749756e/measuring-faithfulness-in-chain-of-thought-reasoning.pdf"
          },
          {
            "title": "Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity",
            "url": "https://arxiv.org/pdf/2510.27378"
          },
          {
            "title": "Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing",
            "url": "https://arxiv.org/pdf/2604.08401"
          },
          {
            "title": "Measuring Faithfulness in Chain-of-Thought Reasoning",
            "url": "https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning"
          }
        ]
      },
      "Based on the search results, here's what recent research reveals about chain-of-thought faithfulness and tool selection in agentic systems in 2026:\n\n## Key Findings on CoT Faithfulness\n\nPrior work has established that chain-of-thought reasoning is not always faithful. Recent 2026 research has uncovered significant issues with how reasoning models behave:\n\n- Reasoning models like Claude 3.7 Sonnet and DeepSeek-R1 frequently fail to verbalize the true factors driving their outputs, finding faithfulness rates as low as 25% for some hint types.\n\n- Recent work used activation probing to demonstrate \"Reasoning Theater\" (models that lock in answers early but continue generating performative reasoning tokens).\n\n## Divergence Between Thinking and Answer Text\n\nA particularly striking 2026 finding involves a gap between what models say in their internal reasoning versus their final answers. Recent research asks: when a model follows a misleading hint, does its visible answer acknowledge the same influences that its thinking tokens do?\n\n## Implications for Agentic Systems\n\nFor agentic systems specifically, unfaithful belief states (e.g., unsupported inferences or hidden assumptions) can propagate, bias decisions, and trigger costly actions in closed-loop agent systems, with the risk being not merely incorrect answers, but systematic behavioral drift driven by unfaithful internal beliefs.\n\nLLM agents maintain internal reasoning trajectories for guiding tool invocation, action commitment, and memory updates across decision steps."
    ],
    "durationSeconds": 7.3271834490000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a8a1d6b9-a547-4df7-b0dc-0e4ae0a411b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T18:40:37.972Z_

<details><summary>↩ Tool result · `toolu_01Faw9wBTTABiZTqK9KdsokM`</summary>

```text
Web search results for query: "RFEval reasoning faithfulness counterfactual intervention benchmark 2026"

Links: [{"title":"[2602.17053v1] RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/abs/2602.17053v1"},{"title":"[2602.17053] RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/abs/2602.17053"},{"title":"RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=2Gc8aj0afg"},{"title":"Title","url":"https://aidaslab.github.io/RFEval/"},{"title":"RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/pdf/2602.17053"},{"title":"RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models","url":"https://arxiv.org/html/2602.17053"},{"title":"Published as a conference paper at ICLR 2026 RFEVAL:","url":"https://openreview.net/pdf/ec385220f6a93f742a238ef1bcc1ffe77437f953.pdf"}]

Based on the search results, here's what I found about RFEval:

## Overview
RFEval is a benchmark of 7,186 instances across seven tasks that probes faithfulness via controlled, output-level counterfactual interventions.

## Key Findings
Large Reasoning Models (LRMs) often produce rationales that sound plausible but fail to reflect their true decision process, and when evaluating twelve open-source LRMs, unfaithfulness was found in 49.7% of outputs, predominantly from stance inconsistency.

## Framework
The paper introduces a formal framework for reasoning faithfulness, defined by two testable conditions: stance consistency (a coherent stance linking reasoning to answer) and causal influence (the stated reasoning causally drives the answer under output-level interventions), explicitly decoupled from accuracy.

## Important Findings
Failures are concentrated in brittle, convergent domains such as math and code, and correlate more with post-training regimes than with scale. Additionally, accuracy is neither a sufficient nor a reliable proxy for faithfulness.

The paper was published at ICLR 2026 and has resources available at https://aidaslab.github.io/RFEval/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4063dd8-830e-46a0-a10a-107f6414d8a4",
  "isSidechain": false,
  "promptId": "fbfac76e-73db-4150-9394-4640f111f44b",
  "type": "user",
  "uuid": "40bf24a7-dcc2-4b2b-9fad-880e1c6ee62f",
  "toolUseResult": {
    "query": "RFEval reasoning faithfulness counterfactual intervention benchmark 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EKHRUfNDBHfv3t4YM8NKYE",
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
            "title": "Title",
            "url": "https://aidaslab.github.io/RFEval/"
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
            "title": "Published as a conference paper at ICLR 2026 RFEVAL:",
            "url": "https://openreview.net/pdf/ec385220f6a93f742a238ef1bcc1ffe77437f953.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about RFEval:\n\n## Overview\nRFEval is a benchmark of 7,186 instances across seven tasks that probes faithfulness via controlled, output-level counterfactual interventions.\n\n## Key Findings\nLarge Reasoning Models (LRMs) often produce rationales that sound plausible but fail to reflect their true decision process, and when evaluating twelve open-source LRMs, unfaithfulness was found in 49.7% of outputs, predominantly from stance inconsistency.\n\n## Framework\nThe paper introduces a formal framework for reasoning faithfulness, defined by two testable conditions: stance consistency (a coherent stance linking reasoning to answer) and causal influence (the stated reasoning causally drives the answer under output-level interventions), explicitly decoupled from accuracy.\n\n## Important Findings\nFailures are concentrated in brittle, convergent domains such as math and code, and correlate more with post-training regimes than with scale. Additionally, accuracy is neither a sufficient nor a reliable proxy for faithfulness.\n\nThe paper was published at ICLR 2026 and has resources available at https://aidaslab.github.io/RFEval/."
    ],
    "durationSeconds": 8.475957288999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e4063dd8-830e-46a0-a10a-107f6414d8a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T18:40:39.482Z_

<details><summary>↩ Tool result · `toolu_01FNLsHNJHALdJHF9TKa7rq5`</summary>

```text
Web search results for query: "tool calling linearly readable steerable language models 2605.07990 arxiv 2026"

Links: [{"title":"[2605.07990] Tool Calling is Linearly Readable and Steerable in Language Models","url":"https://arxiv.org/abs/2605.07990"},{"title":"[2605.07990v1] Tool Calling is Linearly Readable and Steerable in Language Models","url":"https://arxiv.org/abs/2605.07990v1"},{"title":"Tool Calling is Linearly Readable and Steerable in Language Models","url":"https://arxiv.org/html/2605.07990"},{"title":"AI Steerability 360: A Toolkit for Steering Large Language Models","url":"https://arxiv.org/pdf/2603.07837"},{"title":"How Does Controllability Emerge In Language Models During Pretraining?","url":"https://arxiv.org/pdf/2508.01892"}]

I found the paper! Here's what the search results show:

The paper probes 12 instruction-tuned models across Gemma 3, Qwen 3, Qwen 2.5, and Llama 3.1 (270M to 27B) and finds the identity of the chosen tool is linearly readable and steerable inside the model.

Adding the mean-difference between two tools' average internal activations switches which tool the model selects at 77-100% accuracy on name-only single-turn prompts (93-100% at 4B+), and the JSON arguments that follow autoregressively match the new tool's schema.

The per-tool means also flag likely errors before they happen: on Gemma 3 12B and 27B, queries where the gap between the top-1 and top-2 tool is smallest produce 14-21x more wrong calls than queries with the largest gap.

The paper was submitted on May 8, 2026, and is authored by researchers from University College London, Holistic AI, and Imperial College London. You can access the full paper at https://arxiv.org/abs/2605.07990.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83f370ab-1445-4c2e-a9f7-904b904bd9ea",
  "isSidechain": false,
  "promptId": "fbfac76e-73db-4150-9394-4640f111f44b",
  "type": "user",
  "uuid": "c7ef791a-9893-4eba-8114-5c7c8a5f1897",
  "toolUseResult": {
    "query": "tool calling linearly readable steerable language models 2605.07990 arxiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015qCtfaaMzz4t1sgpDxLTjL",
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
      "I found the paper! Here's what the search results show:\n\nThe paper probes 12 instruction-tuned models across Gemma 3, Qwen 3, Qwen 2.5, and Llama 3.1 (270M to 27B) and finds the identity of the chosen tool is linearly readable and steerable inside the model.\n\nAdding the mean-difference between two tools' average internal activations switches which tool the model selects at 77-100% accuracy on name-only single-turn prompts (93-100% at 4B+), and the JSON arguments that follow autoregressively match the new tool's schema.\n\nThe per-tool means also flag likely errors before they happen: on Gemma 3 12B and 27B, queries where the gap between the top-1 and top-2 tool is smallest produce 14-21x more wrong calls than queries with the largest gap.\n\nThe paper was submitted on May 8, 2026, and is authored by researchers from University College London, Holistic AI, and Imperial College London. You can access the full paper at https://arxiv.org/abs/2605.07990."
    ],
    "durationSeconds": 10.242248806,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "83f370ab-1445-4c2e-a9f7-904b904bd9ea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T18:40:46.526Z_

<details><summary>↩ Tool result · `toolu_01B9iaE32rHBprHYz2qRnaHp`</summary>

```text
Web search results for query: "CoRL 2026 conference on robot learning submission topics scope"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI","url":"https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"2025 Conference on Robot Learning - CoRL","url":"https://www.corl.org/home"},{"title":"CoRL 2026 - About CoRL","url":"https://www.corl.org/about-corl"},{"title":"System and method for robot learning from human demonstrations with formal logic","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12208521"}]

Based on the search results, here's information about CoRL 2026 conference submission topics and scope:

## Conference Overview

The Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.

## Submission Topics and Scope

The aim of CoRL 2026 is to publish significant original research at the intersection of robotics and machine learning.

CoRL welcomes papers in areas such as learning representations for robotic perception and control, learning robot foundation models or general-purpose knowledge systems for robotics, imitation learning for robotics (by behavioral cloning and/or inverse reinforcement learning), reinforcement learning for control of physical robots, and video models and latent world models for robot learning.

CoRL covers topics including imitation learning, reinforcement learning for robots, sim-to-real transfer, robot perception through learning, learned manipulation and locomotion, and learning-based planning.

## Submission Requirements

Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. Submissions without a robotics focus will be returned without review.

The paper submission deadline is May 29, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae63a630-38ed-4f59-9e95-df8f588c12d9",
  "isSidechain": false,
  "promptId": "fbfac76e-73db-4150-9394-4640f111f44b",
  "type": "user",
  "uuid": "6074f7d7-6da9-454d-bc6f-5f987b06ec35",
  "toolUseResult": {
    "query": "CoRL 2026 conference on robot learning submission topics scope",
    "results": [
      {
        "tool_use_id": "srvtoolu_014DGG5pBUNNWjB9Qs7nNPSr",
        "content": [
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI",
            "url": "https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"
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
            "title": "2025 Conference on Robot Learning - CoRL",
            "url": "https://www.corl.org/home"
          },
          {
            "title": "CoRL 2026 - About CoRL",
            "url": "https://www.corl.org/about-corl"
          },
          {
            "title": "System and method for robot learning from human demonstrations with formal logic",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12208521"
          }
        ]
      },
      "Based on the search results, here's information about CoRL 2026 conference submission topics and scope:\n\n## Conference Overview\n\nThe Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.\n\n## Submission Topics and Scope\n\nThe aim of CoRL 2026 is to publish significant original research at the intersection of robotics and machine learning.\n\nCoRL welcomes papers in areas such as learning representations for robotic perception and control, learning robot foundation models or general-purpose knowledge systems for robotics, imitation learning for robotics (by behavioral cloning and/or inverse reinforcement learning), reinforcement learning for control of physical robots, and video models and latent world models for robot learning.\n\nCoRL covers topics including imitation learning, reinforcement learning for robots, sim-to-real transfer, robot perception through learning, learned manipulation and locomotion, and learning-based planning.\n\n## Submission Requirements\n\nSubmissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. Submissions without a robotics focus will be returned without review.\n\nThe paper submission deadline is May 29, 2026."
    ],
    "durationSeconds": 18.773920775999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ae63a630-38ed-4f59-9e95-df8f588c12d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
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
  "lastPrompt": "# Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn Probing  ## Description We present the first systematic study of whether tool-selectio…",
  "leafUuid": "6074f7d7-6da9-454d-bc6f-5f987b06ec35",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Study tool-selection faithfulness in multi-turn agents",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3"
}
```

---

### Assistant

_source line 23 · 2026-05-19T18:40:53.118Z_

<details><summary>Logged reasoning block</summary>

```text
This is critical. The CoRL 2026 call for papers explicitly states:

"Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. **Submissions without a robotics focus will be returned without review.**"

This proposal has absolutely zero robotics content. It's about faithfulness of tool-selection reasoning in multi-turn agentic systems - this is a pure NLP/AI safety/interpretability topic. 

This is a fundamental venue mismatch that would trigger desk rejection. Let me search more thoroughly to be sure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6074f7d7-6da9-454d-bc6f-5f987b06ec35",
  "isSidechain": false,
  "requestId": "req_011CbCR9Ym1abeqy9syy8xHj",
  "type": "assistant",
  "uuid": "b5d38870-8e38-43a3-85dc-15a21f659729",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMpprdVQ377juoVtWERcbg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2061,
      "cache_creation_input_tokens": 1243,
      "cache_read_input_tokens": 20648,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2061,
          "output_tokens": 299,
          "cache_read_input_tokens": 20648,
          "cache_creation_input_tokens": 1243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1243
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

_source line 24 · 2026-05-19T18:40:53.126Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cf7gpEZC3eBuFvAGd47wP5`</summary>

```json
{
  "query": "multi-turn agentic tool selection faithfulness probing mechanistic interpretability 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5d38870-8e38-43a3-85dc-15a21f659729",
  "isSidechain": false,
  "requestId": "req_011CbCR9Ym1abeqy9syy8xHj",
  "type": "assistant",
  "uuid": "d49936fe-5416-4825-9f15-299bc42e6887",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMpprdVQ377juoVtWERcbg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2061,
      "cache_creation_input_tokens": 1243,
      "cache_read_input_tokens": 20648,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2061,
          "output_tokens": 299,
          "cache_read_input_tokens": 20648,
          "cache_creation_input_tokens": 1243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1243
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

_source line 25 · 2026-05-19T18:40:53.133Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014c3HN66jdFiXGhqJiPWXSX`</summary>

```json
{
  "query": "CoRL 2026 \"without a robotics focus\" desk reject submission scope LLM agents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d49936fe-5416-4825-9f15-299bc42e6887",
  "isSidechain": false,
  "requestId": "req_011CbCR9Ym1abeqy9syy8xHj",
  "type": "assistant",
  "uuid": "018bd5dd-7e87-4453-869d-e4d54ce90065",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMpprdVQ377juoVtWERcbg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2061,
      "cache_creation_input_tokens": 1243,
      "cache_read_input_tokens": 20648,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2061,
          "output_tokens": 299,
          "cache_read_input_tokens": 20648,
          "cache_creation_input_tokens": 1243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1243
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

_source line 26 · 2026-05-19T18:41:00.461Z_

<details><summary>↩ Tool result · `toolu_014c3HN66jdFiXGhqJiPWXSX`</summary>

```text
Web search results for query: "CoRL 2026 "without a robotics focus" desk reject submission scope LLM agents"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI","url":"https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"},{"title":"CoRL 2021 - Submission Instructions","url":"https://2021.corl.org/author-information/submission-instructions"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Demonstration-Free Robotic Control via LLM Agents","url":"https://arxiv.org/pdf/2601.20334"}]

Based on the search results, here's what I found regarding CoRL 2026 and submissions without a robotics focus:

Submissions without a robotics focus will be returned without review at CoRL 2026. This is a key desk-rejection criterion for the conference.

More specifically, submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Additionally, authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.

The search results also indicate that papers that contain citations to references that do not exist will be desk-rejected after review by the Program Committee, which is another relevant desk-rejection policy.

Regarding LLM agents specifically, while the search returned a paper about using LLM agents for robotic control, the CoRL 2026 submission guidelines don't explicitly mention LLM agents or provide special guidance for them. However, they would still need to meet the core requirement of demonstrating relevance to a robotics problem to avoid desk rejection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "018bd5dd-7e87-4453-869d-e4d54ce90065",
  "isSidechain": false,
  "promptId": "fbfac76e-73db-4150-9394-4640f111f44b",
  "type": "user",
  "uuid": "2d40c69d-3571-417f-8e82-d15e17f4d8ee",
  "toolUseResult": {
    "query": "CoRL 2026 \"without a robotics focus\" desk reject submission scope LLM agents",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FQhtzei9742NWTRzTx9H2k",
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
            "title": "Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI",
            "url": "https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"
          },
          {
            "title": "CoRL 2021 - Submission Instructions",
            "url": "https://2021.corl.org/author-information/submission-instructions"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "CoRL 2024 - Instruction for Reviews",
            "url": "https://2024.corl.org/contributions/instruction-for-reviews"
          },
          {
            "title": "Demonstration-Free Robotic Control via LLM Agents",
            "url": "https://arxiv.org/pdf/2601.20334"
          }
        ]
      },
      "Based on the search results, here's what I found regarding CoRL 2026 and submissions without a robotics focus:\n\nSubmissions without a robotics focus will be returned without review at CoRL 2026. This is a key desk-rejection criterion for the conference.\n\nMore specifically, submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Additionally, authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\n\nThe search results also indicate that papers that contain citations to references that do not exist will be desk-rejected after review by the Program Committee, which is another relevant desk-rejection policy.\n\nRegarding LLM agents specifically, while the search returned a paper about using LLM agents for robotic control, the CoRL 2026 submission guidelines don't explicitly mention LLM agents or provide special guidance for them. However, they would still need to meet the core requirement of demonstrating relevance to a robotics problem to avoid desk rejection."
    ],
    "durationSeconds": 7.3252856830000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "018bd5dd-7e87-4453-869d-e4d54ce90065",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T18:41:04.046Z_

<details><summary>↩ Tool result · `toolu_01Cf7gpEZC3eBuFvAGd47wP5`</summary>

```text
Web search results for query: "multi-turn agentic tool selection faithfulness probing mechanistic interpretability 2026"

Links: [{"title":"Beyond the Black Box: Interpretability of Agentic AI Tool Use","url":"https://arxiv.org/html/2605.06890"},{"title":"Multi-Turn LLM Evaluation in 2026: What You Need to Know - Confident AI","url":"https://www.confident-ai.com/blog/multi-turn-llm-evaluation-in-2026"},{"title":"From Explainability to Control: The 2026 Executive View of AI Interpretability and Explainability","url":"https://www.ust.com/en/insights/ai-interpretability-explainability-2026-executive-view"},{"title":"Quantifying Distributional Robustness of Agentic Tool-Selection","url":"https://arxiv.org/pdf/2510.03992"},{"title":"GitHub - VoltAgent/awesome-ai-agent-papers: A curated collection of AI agent research papers released in 2026, covering agent engineering, memory, evaluation, workflows, and autonomous systems. · GitHub","url":"https://github.com/VoltAgent/awesome-ai-agent-papers"},{"title":"GitHub - namezhenzhang/CM2-RLCR-Tool-Agent: Official Implementation of Papar CM2 · GitHub","url":"https://github.com/namezhenzhang/CM2-RLCR-Tool-Agent"},{"title":"[2602.12268] CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use","url":"https://arxiv.org/abs/2602.12268"},{"title":"MULTI-TURN RL OF LLM AGENTS","url":"https://openreview.net/pdf?id=ayVIbNrYiC"},{"title":"Towards Trustworthy Multi-Turn LLM Agents via Behavioral Guidance","url":"https://arxiv.org/pdf/2512.11421"}]

I found several relevant results for your query. Here's what the search returned:

## Key Findings

**Recent Research on Agentic AI Interpretability:**

Research is converting multi-step agent trajectories into per-step decision rows containing cumulative context, binary labels indicating whether a tool is required, and three-level risk labels for tool actions.

**Tool Selection and Faithfulness:**

Recent work on tool-selection hallucinations shows that hidden states can contain useful signals for tool-call errors that aren't visible from outputs alone. A 2026 paper introduces a "Determinism-Faithfulness Assurance Harness" for measuring trajectory determinism and evidence-conditioned faithfulness in tool-using LLM agents.

**Mechanistic Interpretability Approaches:**

For frontier models with material safety exposure, mechanistic interpretability work may be justified as part of risk-tier-based controls for agent systems. An internal monitoring framework reads model activations immediately before each action to estimate whether the model is preparing to delegate to a tool and whether that action is appropriate.

**Multi-Turn Agent Evaluation:**

For multi-turn AI agents, task completion measures whether the agent accomplished its goal across all tool calls, reasoning steps, and user interactions. CM2 is a reinforcement learning framework designed to solve challenges of training agents for complex, open-ended tool-use scenarios.

The search results show active 2026 research at the intersection of these topics, particularly focusing on interpretability and faithfulness verification in agentic systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d49936fe-5416-4825-9f15-299bc42e6887",
  "isSidechain": false,
  "promptId": "fbfac76e-73db-4150-9394-4640f111f44b",
  "type": "user",
  "uuid": "fcea334e-e7bf-4cfb-8f88-3b8acbbb6aed",
  "toolUseResult": {
    "query": "multi-turn agentic tool selection faithfulness probing mechanistic interpretability 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GKUkm79wL9kN6QeoWhapF5",
        "content": [
          {
            "title": "Beyond the Black Box: Interpretability of Agentic AI Tool Use",
            "url": "https://arxiv.org/html/2605.06890"
          },
          {
            "title": "Multi-Turn LLM Evaluation in 2026: What You Need to Know - Confident AI",
            "url": "https://www.confident-ai.com/blog/multi-turn-llm-evaluation-in-2026"
          },
          {
            "title": "From Explainability to Control: The 2026 Executive View of AI Interpretability and Explainability",
            "url": "https://www.ust.com/en/insights/ai-interpretability-explainability-2026-executive-view"
          },
          {
            "title": "Quantifying Distributional Robustness of Agentic Tool-Selection",
            "url": "https://arxiv.org/pdf/2510.03992"
          },
          {
            "title": "GitHub - VoltAgent/awesome-ai-agent-papers: A curated collection of AI agent research papers released in 2026, covering agent engineering, memory, evaluation, workflows, and autonomous systems. · GitHub",
            "url": "https://github.com/VoltAgent/awesome-ai-agent-papers"
          },
          {
            "title": "GitHub - namezhenzhang/CM2-RLCR-Tool-Agent: Official Implementation of Papar CM2 · GitHub",
            "url": "https://github.com/namezhenzhang/CM2-RLCR-Tool-Agent"
          },
          {
            "title": "[2602.12268] CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use",
            "url": "https://arxiv.org/abs/2602.12268"
          },
          {
            "title": "MULTI-TURN RL OF LLM AGENTS",
            "url": "https://openreview.net/pdf?id=ayVIbNrYiC"
          },
          {
            "title": "Towards Trustworthy Multi-Turn LLM Agents via Behavioral Guidance",
            "url": "https://arxiv.org/pdf/2512.11421"
          }
        ]
      },
      "I found several relevant results for your query. Here's what the search returned:\n\n## Key Findings\n\n**Recent Research on Agentic AI Interpretability:**\n\nResearch is converting multi-step agent trajectories into per-step decision rows containing cumulative context, binary labels indicating whether a tool is required, and three-level risk labels for tool actions.\n\n**Tool Selection and Faithfulness:**\n\nRecent work on tool-selection hallucinations shows that hidden states can contain useful signals for tool-call errors that aren't visible from outputs alone. A 2026 paper introduces a \"Determinism-Faithfulness Assurance Harness\" for measuring trajectory determinism and evidence-conditioned faithfulness in tool-using LLM agents.\n\n**Mechanistic Interpretability Approaches:**\n\nFor frontier models with material safety exposure, mechanistic interpretability work may be justified as part of risk-tier-based controls for agent systems. An internal monitoring framework reads model activations immediately before each action to estimate whether the model is preparing to delegate to a tool and whether that action is appropriate.\n\n**Multi-Turn Agent Evaluation:**\n\nFor multi-turn AI agents, task completion measures whether the agent accomplished its goal across all tool calls, reasoning steps, and user interactions. CM2 is a reinforcement learning framework designed to solve challenges of training agents for complex, open-ended tool-use scenarios.\n\nThe search results show active 2026 research at the intersection of these topics, particularly focusing on interpretability and faithfulness verification in agentic systems."
    ],
    "durationSeconds": 10.916206502000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d49936fe-5416-4825-9f15-299bc42e6887",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-19T18:41:07.990Z_

<details><summary>Logged reasoning block</summary>

```text
This is a fatal problem. Let me now search for a couple more things to be thorough in my analysis:

1. Whether there's any angle where this could fit CoRL
2. The "Beyond the Black Box" paper (2605.06890) that studies interpretability of agentic AI tool use
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcea334e-e7bf-4cfb-8f88-3b8acbbb6aed",
  "isSidechain": false,
  "requestId": "req_011CbCRAqdnjRyU4fQKBP3Ft",
  "type": "assistant",
  "uuid": "1ff3aada-795f-4542-b2a8-ceb10cfa1684",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVP12GhUtCrw6VqKfg2vJV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 581,
      "cache_creation_input_tokens": 3231,
      "cache_read_input_tokens": 21891,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3231,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 581,
          "output_tokens": 158,
          "cache_read_input_tokens": 21891,
          "cache_creation_input_tokens": 3231,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3231
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

_source line 29 · 2026-05-19T18:41:08.102Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rpo84xuZoWamKkyV2RHpnB`</summary>

```json
{
  "query": "\"beyond the black box\" interpretability agentic AI tool use 2605.06890 arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ff3aada-795f-4542-b2a8-ceb10cfa1684",
  "isSidechain": false,
  "requestId": "req_011CbCRAqdnjRyU4fQKBP3Ft",
  "type": "assistant",
  "uuid": "a3076269-49cb-4c7c-b922-877f44c2fee7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PVP12GhUtCrw6VqKfg2vJV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 581,
      "cache_creation_input_tokens": 3231,
      "cache_read_input_tokens": 21891,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3231,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 581,
          "output_tokens": 158,
          "cache_read_input_tokens": 21891,
          "cache_creation_input_tokens": 3231,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3231
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

_source line 30 · 2026-05-19T18:41:14.501Z_

<details><summary>↩ Tool result · `toolu_01Rpo84xuZoWamKkyV2RHpnB`</summary>

```text
Web search results for query: ""beyond the black box" interpretability agentic AI tool use 2605.06890 arxiv 2026"

Links: [{"title":"[2605.06890] Beyond the Black Box: Interpretability of Agentic AI Tool Use","url":"https://arxiv.org/abs/2605.06890"},{"title":"Beyond the Black Box: Interpretability of Agentic AI Tool Use","url":"https://arxiv.org/html/2605.06890"},{"title":"Beyond Black-Box Benchmarking: Observability, Analytics, and Optimization of Agentic Systems","url":"https://arxiv.org/html/2503.06745v1"},{"title":"Beyond the Black Box: A Cognitive Architecture for Explainable and Aligned AI","url":"https://arxiv.org/html/2512.03072"},{"title":"TripleTree: A Versatile Interpretable Representation of Black Box Agents   and their Environments","url":"https://arxiv.org/pdf/2009.04743"},{"title":"Discovering User-Interpretable Capabilities of Black-Box Planning Agents","url":"https://arxiv.org/pdf/2107.13668"}]

I found the paper you're looking for! Here's what the search revealed:

"Beyond the Black Box: Interpretability of Agentic AI Tool Use" is an arXiv paper (2605.06890) submitted on May 7, 2026, by authors Hariom Tatsat and Ariye Shater.

**Overview:**

The paper addresses how AI agents are promising for high-stakes enterprise workflows, but dependable deployment remains limited because tool-use failures are difficult to diagnose and control. Agents may skip required tool calls, invoke tools unnecessarily, or take actions whose consequence becomes visible only after execution.

**Key Approach:**

The researchers introduce a mechanistic-interpretability toolkit built on Sparse Autoencoders (SAEs) and linear probes that reads model states before each action and infers both whether a tool is needed and how consequential the next tool action is likely to be.

The paper addresses an important gap in AI observability, particularly for long-horizon tasks where tool-use mistakes early on can have cascading negative effects downstream.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3076269-49cb-4c7c-b922-877f44c2fee7",
  "isSidechain": false,
  "promptId": "fbfac76e-73db-4150-9394-4640f111f44b",
  "type": "user",
  "uuid": "62002690-dd44-409d-a9af-0048902c1aad",
  "toolUseResult": {
    "query": "\"beyond the black box\" interpretability agentic AI tool use 2605.06890 arxiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SRptgqsvaSoknpAaCK8YPG",
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
            "title": "Discovering User-Interpretable Capabilities of Black-Box Planning Agents",
            "url": "https://arxiv.org/pdf/2107.13668"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search revealed:\n\n\"Beyond the Black Box: Interpretability of Agentic AI Tool Use\" is an arXiv paper (2605.06890) submitted on May 7, 2026, by authors Hariom Tatsat and Ariye Shater.\n\n**Overview:**\n\nThe paper addresses how AI agents are promising for high-stakes enterprise workflows, but dependable deployment remains limited because tool-use failures are difficult to diagnose and control. Agents may skip required tool calls, invoke tools unnecessarily, or take actions whose consequence becomes visible only after execution.\n\n**Key Approach:**\n\nThe researchers introduce a mechanistic-interpretability toolkit built on Sparse Autoencoders (SAEs) and linear probes that reads model states before each action and infers both whether a tool is needed and how consequential the next tool action is likely to be.\n\nThe paper addresses an important gap in AI observability, particularly for long-horizon tasks where tool-use mistakes early on can have cascading negative effects downstream."
    ],
    "durationSeconds": 6.395100636000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a3076269-49cb-4c7c-b922-877f44c2fee7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-19T18:41:35.950Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to provide my assessment. Let me synthesize:

## FATAL ISSUE: Venue Mismatch

The most critical finding is that **CoRL 2026 explicitly states: "Submissions without a robotics focus will be returned without review."** This proposal has absolutely zero robotics content. It's about faithfulness of tool-selection reasoning in multi-turn LLM agentic systems — a pure NLP/AI safety/interpretability topic. The five domains mentioned are "code editing, web browsing, data analysis, system administration, information retrieval" — none of which are robotics.


This would be desk-rejected at CoRL without review. The right venues are NeurIPS, ICML, ICLR, or ACL/EMNLP depending on the framing, with AAAI as another option, plus relevant workshops at these conferences.

Beyond the venue mismatch, the core idea has real merit: there's a clear gap between single-turn tool probing (well-studied) and multi-turn scenarios (explicitly identified as unsolved in the prior work), and the combination of behavioral analysis with mechanistic investigation looks promising.

But the scope is concerning—it's essentially two papers at once, and I'm wondering if the mechanistic probing part is actually necessary or if a simpler counterfactual comparison of tool distributions before and after chain-of-thought reasoning would suffice, since that intervention framework is already established. The positioning as an extension of the prior work on multi-turn probing also feels a bit thin given what that work already covers.

The real issue though is the venue mismatch—this is fundamentally a direction problem that no amount of refinement can solve, since it risks a desk rejection for being out of scope. I need to flag this as the primary blocker while still exploring whether the core idea has merit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62002690-dd44-409d-a9af-0048902c1aad",
  "isSidechain": false,
  "requestId": "req_011CbCRBcLs3DxNh4xCUi92c",
  "type": "assistant",
  "uuid": "d0f19043-4e21-4c28-800d-699780b555a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AB1q235vgPvVmZV6KhtYN3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1292,
      "cache_read_input_tokens": 25122,
      "output_tokens": 4810,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1292,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4810,
          "cache_read_input_tokens": 25122,
          "cache_creation_input_tokens": 1292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1292
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

_source line 32 · 2026-05-19T18:43:03.954Z_

I now have sufficient information to provide my assessment. Let me compile my findings.

---

【状态】: 有发掘空间

**⚠️ 但首先必须标注一个致命问题：投稿目标会议与论文内容完全不匹配。**

---

【前置调研发现】

- **[Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990) (arXiv 2026):** 本 proposal 最核心的前置工作。对 12 个模型做 single-turn tool probing，4B+ 模型 steering accuracy 达 93-100%，但明确指出 multi-turn 迁移"fragile"（-30 to +10pp）。本 proposal 正确定位在这个 gap 上。
- **[RFEval](https://arxiv.org/abs/2602.17053) (ICLR 2026):** 7,186 instance 的 counterfactual intervention benchmark，发现 ~50% unfaithfulness。提供了 stance consistency + causal influence 的形式化框架。本 proposal 的 intervention protocol 借鉴了此方法论，但迁移到 tool selection 领域。
- **[Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890) (arXiv 2026):** SAE + linear probe 用于 multi-step trajectory 中的 tool-need/tool-risk classification。**高度相关但被 proposal 低估**——该工作已经在多步 trajectory 上做了 probe，虽然不是 tool identity 或 faithfulness，但覆盖面比 proposal 描述的更广。
- **[Lie to Me](https://arxiv.org/abs/2603.22582) (arXiv 2026):** 12 模型评测发现 thinking token 与 output 之间存在 59pp faithfulness gap。核心 insight 是"internal recognition ≠ output acknowledgment"。
- **[CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers):** 明确要求"submissions should focus on a core robotics problem"，"submissions without a robotics focus will be returned without review"。鼓励 real-robot experiments 或 sim-to-real evidence。
- **调研总结:** CoT faithfulness 研究在 2026 年进入了快速成熟期，单轮已有成熟框架（RFEval 的 counterfactual intervention, 2605.07990 的 linear probing），多轮 tool selection 确实是一个被明确标识但尚未系统研究的 gap。但 CoRL 的 scope 严格限定于机器人学习，与本 proposal 的内容领域完全不重叠。

---

【致命问题：投稿目标会议错误——必须在一切发掘之前解决】

- **维度:** 前提假设质疑（研究方向与投稿目标的匹配性）
- **内容:** CoRL 2026 明确声明 **"Submissions without a robotics focus will be returned without review"**。本 proposal 研究的是 LLM agent 在代码编辑、网页浏览、数据分析、系统管理、信息检索五个领域中的 tool-selection faithfulness——没有任何一个领域涉及机器人学习。Benchmark 设计中无 robot manipulation、locomotion、perception、planning、sim-to-real 任何元素。**这不是 borderline case，而是会被直接 desk reject 的完全不匹配。**
- **价值:** 这是一切其他优化建议的前提。如果目标会议选错，idea 本身质量再高也无法中稿。
- **补救方向:**
  - **方案 A（推荐）：** 转投匹配的会议——NeurIPS 2026（有 Safety/Interpretability track，deadline 通常 5-6 月）、EMNLP 2026、AAAI 2027。本 proposal 的内容与这些会议高度匹配。
  - **方案 B（不推荐，成本极高）：** 将整个 proposal 重新定位为 robot learning 问题——例如研究 embodied agent 在 manipulation task 中的 tool-selection faithfulness（机械臂选择 grasp vs. push vs. reposition 的推理忠实性），需要重建 benchmark、重新设计 domain、引入 real-robot 或 sim 实验，基本等于重写一篇新论文。
- **调研依据:** CoRL 2026 官方 Call for Papers（https://www.corl.org/contributions/call-for-papers）。

---

**以下发掘建议基于"已转投至匹配会议（如 NeurIPS 2026）"的前提：**

---

【发掘点 1】
- **维度:** trivial alternative 威胁
- **内容:** 本 proposal 的核心 behavioral intervention protocol（reason-flip, reason-ablate, counterfactual-inject, reason-scramble）本质上是将 RFEval 的 counterfactual intervention 框架从 QA/math reasoning 迁移到 tool selection。审稿人会问：**这个迁移本身有多 non-trivial？** RFEval 已经提供了成熟的 stance consistency + causal influence 框架，将干预对象从"reasoning about an answer"换成"reasoning about a tool call"是否属于 straightforward domain transfer？如果是，那核心贡献就缩窄为"在新 domain 上复现了 RFEval 的发现"。**Proposal 需要清晰 argue 为什么 tool selection 的 faithfulness 问题在结构上不同于 QA faithfulness**——例如：tool call 有 structured output（JSON schema），而非 free-form answer；tool call 有 downstream effect（执行结果反馈到下一轮），创造了 QA 不存在的 temporal dependency；multi-turn 的 context accumulation 改变了 intervention 的 semantics（你 flip 的 reasoning 可能与先前 turn 的 tool result 矛盾，创造 incoherence）。这些结构性差异应该被提升为核心 novelty claim 的一部分，而不仅仅是"我们把 X 用在了新领域 Y"。
- **价值:** 直接提升 Novelty 维度——从"domain transfer"升级为"结构性新问题需要新方法论适配"。
- **调研依据:** RFEval (2602.17053) 的框架已非常成熟且被 ICLR 2026 接收，审稿人必然会追问差异化。

【发掘点 2】
- **维度:** 核心 claim 强化
- **内容:** Proposal 提出的最有趣的假设是 **"harder ambiguous scenarios may elicit more faithful reasoning than unambiguous ones"**——这是一个 counterintuitive prediction，如果被验证，是非常强的 contribution。但当前 proposal 对这个假设的理论动机阐述不足（仅一句"because genuine deliberation is required"）。建议将这个假设提升为论文的 **central narrative**：构建一个"deliberation threshold"的理论模型——当 tool choice 是 trivial 时，模型走 System 1 fast path（直接从 latent policy 选择），CoT 变成 post-hoc rationalization；当 tool choice genuinely ambiguous 时，模型被迫走 System 2 deliberation path，CoT 成为真正的计算介质。这个 framing 将 tool-selection faithfulness 从一个 benchmark paper 提升为一个有 explanatory power 的 framework paper。具体地，三个 tier（Unambiguous/Soft/Hard）不再只是 benchmark stratification，而是对应理论预测的三个 regime。
- **价值:** 提升 Significance 维度——从"我们测量了 faithfulness"升级为"我们发现并解释了 faithfulness 随 task difficulty 的非单调变化规律"。
- **调研依据:** "Brief Is Better" (2604.02155) 已经发现 CoT budget 对 function-calling 有 non-monotonic 效果，暗示了 deliberation dynamics 的复杂性。"Decoding Answers Before CoT" (2603.01437) 的 0.9 AUC pre-CoT probing 支持"System 1 fast path"假说（答案在 CoT 之前已编码）。

【发掘点 3】
- **维度:** related work 差异化
- **内容:** Proposal 对 **"Beyond the Black Box" (2605.06890)** 的定位可能低估了其威胁性。当前 proposal 将其描述为"applies SAE + probes to multi-step trajectories for tool-need/tool-risk classification but not tool identity or faithfulness"。但该工作已经在 multi-step agentic trajectory 上建立了 probing 基础设施——如果他们的后续工作简单扩展到 tool identity probing（技术上直接可行），本 proposal 的 mechanistic probing 部分的 novelty 就会大幅缩水。**建议：(1)** 明确 acknowledge 2605.06890 的 coverage 而非 downplay 它；**(2)** 将 proposal 的 mechanistic 贡献聚焦在 behavioral-mechanistic coupling 上（即发掘点 2 中"behavioral intervention 结果与 probe 结果的相关性分析"），这是 2605.06890 完全没有触及的维度——它只做了 probing，没有做 behavioral intervention，更没有做两者的 coupling analysis。
- **价值:** 提升 Related Work 差异化——预防审稿人认为 mechanistic probing 部分是 incremental extension of 2605.06890。
- **调研依据:** 2605.06890 已在 multi-step trajectory 上部署了 SAE + linear probe，与本 proposal 的 probing component 有直接技术重叠。

【发掘点 4】
- **维度:** significance 提升
- **内容:** 当前 proposal 的 significance 叙事主要停留在"unfaithful tool selection can cascade into harmful actions"这一 safety motivation。但这个 motivation 偏 abstract——审稿人会问"so what, this is true for any unfaithful reasoning"。建议引入一个更锐利的 significance angle：**multi-turn tool selection 是目前 AI agent 可观测推理与不可观测行为之间 alignment gap 最大的场景**。具体论证：(1) 与 QA 不同，tool call 是 action（有不可逆的 real-world effect）；(2) 与 single-turn 不同，multi-turn 中 early unfaithfulness 通过 tool result 反馈 compound（一个基于错误理由选择的 API call 的结果会 condition 所有后续推理）；(3) 当前的 agent monitoring 方案（如 SAVeR）假设 CoT 是 faithful 的，如果这个假设不成立，整个 monitoring paradigm 需要重新审视。第 (3) 点特别有力，因为它将本工作定位为对一个正在被广泛部署的 safety mechanism 的 validity check。
- **价值:** 提升 Significance 维度——从 general safety motivation 升级为对当前 agent monitoring paradigm 的 foundational challenge。
- **调研依据:** SAVeR (2604.08401) 和 "Noticing the Watcher" (2603.16928) 都在构建基于 CoT 的 agent monitoring，隐含假设了 CoT 的 faithfulness。

【发掘点 5】
- **维度:** novelty 锐化
- **内容:** Proposal 目前试图同时做两件大事：(1) behavioral causal intervention benchmark (TOOLFAITH-BENCH + TSCF/RTI metrics)，(2) multi-turn mechanistic probing (cross-turn probe transfer, encoding drift, replanning signals, behavioral-mechanistic coupling)。对于一篇会议论文来说，这两件事的结合既是优势也是风险。优势是 uniqueness（无人做过两者的 coupling）；**风险是审稿人认为每一半都不够深**——behavioral 部分看起来像 RFEval 的 domain transfer，mechanistic 部分看起来像 2605.07990 的 multi-turn extension。建议做出取舍：**将 behavioral-mechanistic coupling analysis 提升为论文的核心独特贡献**，而将 pure behavioral benchmark 和 pure probing 各自 condense 为 supporting components。核心 research question 应该是："当 probe 在 CoT 生成之前就检测到了 tool identity 的 pre-commitment（mechanistic unfaithfulness），behavioral intervention 是否也会显示 low TSCF（behavioral unfaithfulness）？" 如果两种独立的 unfaithfulness measure 高度相关，这是一个非常强的发现（convergent validity）；如果不相关，这同样是一个重要发现（暗示存在多种不同的 unfaithfulness mechanism）。
- **价值:** 同时提升 Novelty 和 Significance——将论文从"两个方向的分别推进"重新定位为"两个方向的 convergence/divergence 分析"，这是任何单独做 behavioral 或 mechanistic 的工作都无法提供的。
- **调研依据:** 基于领域整体趋势判断——behavioral intervention (RFEval 路线) 和 mechanistic probing (2605.07990 路线) 目前是两个平行发展的 community，无人做过两者的 systematic coupling analysis。

---

Sources:
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990)
- [RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention](https://arxiv.org/abs/2602.17053)
- [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890)
- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?](https://arxiv.org/abs/2603.22582)
- [Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing (SAVeR)](https://arxiv.org/abs/2604.08401)
- [CoRL 2026 About Page](https://www.corl.org/about-corl)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0f19043-4e21-4c28-800d-699780b555a9",
  "isSidechain": false,
  "requestId": "req_011CbCRBcLs3DxNh4xCUi92c",
  "type": "assistant",
  "uuid": "2dfffaac-035f-46e0-801f-389c7faf96c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AB1q235vgPvVmZV6KhtYN3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1292,
      "cache_read_input_tokens": 25122,
      "output_tokens": 4810,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1292,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4810,
          "cache_read_input_tokens": 25122,
          "cache_creation_input_tokens": 1292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1292
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
  "lastPrompt": "# Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn Probing  ## Description We present the first systematic study of whether tool-selectio…",
  "leafUuid": "2dfffaac-035f-46e0-801f-389c7faf96c2",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Study tool-selection faithfulness in multi-turn agents",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Faithfulness of Tool-Selection Reasoning in Multi-Turn Agentic Systems: Behavioral Interventions and Multi-Turn Probing  ## Description We present the first systematic study of whether tool-selectio…",
  "leafUuid": "2dfffaac-035f-46e0-801f-389c7faf96c2",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Study tool-selection faithfulness in multi-turn agents",
  "sessionId": "c8fb3812-7ae9-4c8a-be2e-3ae325cb7fc3"
}
```

---
