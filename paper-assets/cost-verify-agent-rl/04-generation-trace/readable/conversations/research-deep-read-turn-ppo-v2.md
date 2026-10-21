# research deep read turn ppo v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 77
- **Recorded user turns:** 0
- **Tool calls:** 38
- **Original source:** `logs/chats/worker_research_deep-read-turn-ppo-v2_20260517T121530.jsonl`
- **Structured JSON:** [`2a01c3f4993c95695fa2.json`](../../sessions/2a/2a01c3f4993c95695fa2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

77 recorded events

### Tool call

_source line 1 · 2026-05-17T12:22:12.574080+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T12:22:12.574433+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T12:22:12.574648+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T12:22:12.574796+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T12:22:12.574920+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "turn-level PPO per-turn credit assignment multi-turn agent reinforcement learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "tool_args": {
    "query": "turn-level PPO per-turn credit assignment multi-turn agent reinforcement learning 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T12:22:12.575042+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GRPO group relative policy optimization multi-step agent training credit assignment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GRPO group relative policy optimization multi-step agent training credit assignment"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T12:22:12.575296+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "step-level reward stepwise optimization language model agent RL sparse reward"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "tool_args": {
    "query": "step-level reward stepwise optimization language model agent RL sparse reward"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T12:22:12.575421+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RAGEN reinforcement learning agent multi-turn credit assignment 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RAGEN reinforcement learning agent multi-turn credit assignment 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T12:22:12.575538+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "temporal credit assignment large language model reinforcement learning multi-step"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "tool_args": {
    "query": "temporal credit assignment large language model reinforcement learning multi-step"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T12:22:12.575716+00:00_

Web search results for query: "turn-level PPO per-turn credit assignment multi-turn agent reinforcement learning 2024 2025"

Links: [{"title":"NeurIPS Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design and Credit Assignment","url":"https://neurips.cc/virtual/2025/133311"},{"title":"[Quick Review] Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Credit\\n Assignment","url":"https://liner.com/review/reinforcing-multiturn-reasoning-in-llm-agents-via-turnlevel-credit-assignment"},{"title":"ICML Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Credit Assignment","url":"https://icml.cc/virtual/2025/49783"},{"title":"Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration","url":"https://arxiv.org/html/2604.02869v1"},{"title":"NeurIPS 2025 Workshop on Multi-Turn Interactions in Large Language Models","url":"https://workshop-multi-turn-interaction.github.io/"},{"title":"Turn-Aware PPO for Multi-Turn RL","url":"https://www.emergentmind.com/topics/turn-aware-ppo-ta-ppo"},{"title":"GitHub - SiliangZeng/Multi-Turn-RL-Agent · GitHub","url":"https://github.com/SiliangZeng/Multi-Turn-RL-Agent"},{"title":"[2505.11821] Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design","url":"https://arxiv.org/abs/2505.11821"},{"title":"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs","url":"https://arxiv.org/html/2512.17008v1"},{"title":"[2512.17008] Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs","url":"https://arxiv.org/abs/2512.17008"}]

I found several highly relevant papers and research on turn-level PPO and per-turn credit assignment in multi-turn agent reinforcement learning from 2024-2025. Here are the key findings:

## Primary Research Papers

A major work introduces fine-grained turn-level credit assignment strategy and extends GRPO and PPO to their multi-turn variants by incorporating 
…[truncated 1566 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T12:22:12.575931+00:00_

Web search results for query: "GRPO group relative policy optimization multi-step agent training credit assignment"

Links: [{"title":"M-GRPO: Multi-Agent Group Relative Policy Optimization","url":"https://www.emergentmind.com/topics/multi-agent-group-relative-policy-optimization-m-grpo"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978v3"},{"title":"[2505.10978] Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/abs/2505.10978"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"},{"title":"Group-Based Relative Policy Optimization","url":"https://www.emergentmind.com/topics/group-based-relative-policy-optimization-grpo"},{"title":"Tree-GRPO: Group Relative Policy Optimization","url":"https://www.emergentmind.com/topics/tree-based-group-relative-policy-optimization-tree-grpo"},{"title":"GRPO: Group Relative Policy Optimization","url":"https://www.emergentmind.com/topics/grpo"},{"title":"What is GRPO? Group Relative Policy Optimization Explained | DataCamp","url":"https://www.datacamp.com/blog/what-is-grpo-group-relative-policy-optimization"},{"title":"GitHub - kechirojp/sb3-grpo: GRPO (Group Relative Policy Optimization) implementation for Stable Baselines3. Drop-in PPO replacement with instant action comparison. Easy pip install, full API compatibility. Used by DeepSeek for LLM training. · GitHub","url":"https://github.com/kechirojp/sb3-grpo"}]

Based on the search results, here's comprehensive information about GRPO and its application to multi-step agent training with credit assignment:

## Group Relative Policy Optimization (GRPO)

Group-based Relative Policy Optimization (GRPO) is a reinforcement learning algorithm rooted in group-wise advantage estimation and policy optim
…[truncated 2331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T12:22:12.576271+00:00_

Web search results for query: "step-level reward stepwise optimization language model agent RL sparse reward"

Links: [{"title":"[2509.19199] Agentic Reinforcement Learning with Implicit Step Rewards","url":"https://arxiv.org/abs/2509.19199"},{"title":"SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution","url":"https://arxiv.org/html/2505.20732v1"},{"title":"R1-VL: Learning to Reason with Multimodal Large Language Models via","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_R1-VL_Learning_to_Reason_with_Multimodal_Large_Language_Models_via_ICCV_2025_paper.pdf"},{"title":"[2411.03817] From Novice to Expert: LLM Agent Policy Optimization via Step-wise Reinforcement Learning","url":"https://arxiv.org/abs/2411.03817"},{"title":"Alleviating Sparse Rewards by Modeling Step-Wise and Long-Term Sampling Effects in Flow-Based GRPO","url":"https://arxiv.org/html/2602.06422"},{"title":"Agentic Reinforcement Learning with Implicit Step Rewards | OpenReview","url":"https://openreview.net/forum?id=ooROvpmxMV"},{"title":"Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs","url":"https://arxiv.org/html/2509.25779v2"},{"title":"STEP-LLM: Fine-Grained LLM Optimization","url":"https://www.emergentmind.com/topics/step-llm"},{"title":"[Literature Review] SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution","url":"https://www.themoonlight.io/en/review/spa-rl-reinforcing-llm-agents-via-stepwise-progress-attribution"},{"title":"Agentic Reinforcement Learning with Implicit Step Rewards","url":"https://arxiv.org/html/2509.19199v3"}]

I found several relevant research papers and resources on step-level reward optimization for language model agents using reinforcement learning with sparse rewards. Here are the key findings:

## Main Research Areas

Sparse and sometimes unverifiable rewards make it extremely challenging to assign credit when training LLM agents that serve as a policy.

### Key Approaches

1. **Implicit Step Rewar
…[truncated 1634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T12:22:12.576469+00:00_

Web search results for query: "RAGEN reinforcement learning agent multi-turn credit assignment 2024 2025"

Links: [{"title":"GitHub - mll-lab-nu/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments. · GitHub","url":"https://github.com/mll-lab-nu/RAGEN"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2504.20073v2"},{"title":"[PDF] RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RAGEN:-Understanding-Self-Evolution-in-LLM-Agents-Wang-Wang/1d03586baa32b3d6ff657a180053821543e11abb"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"Understanding Self-Evolution in LLM Agents via Multi-Turn ...","url":"https://ragen-ai.github.io/pdf/RAGEN.pdf"},{"title":"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models","url":"https://arxiv.org/html/2604.09459v1"},{"title":"GitHub - xxzcc/Awesome-Credit-Assignment-in-LLM-RL · GitHub","url":"https://github.com/xxzcc/Awesome-Credit-Assignment-in-LLM-RL"},{"title":"RAGEN - RL Agent","url":"https://ragen-ai.github.io/"},{"title":"Paper page - Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Credit Assignment","url":"https://huggingface.co/papers/2505.11821"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via ...","url":"https://arxiv.org/pdf/2504.20073"}]

Based on the search results, here's information about RAGEN and its focus on multi-turn credit assignment in reinforcement learning:

## Overview

RAGEN is built around StarPO (State-Thinking-Actions-Reward Policy Optimization), a unified RL framework for training multi-turn, trajectory-level agents
…[truncated 1529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T12:22:12.576691+00:00_

Web search results for query: "temporal credit assignment large language model reinforcement learning multi-step"

Links: [{"title":"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents","url":"https://arxiv.org/html/2602.16165"},{"title":"[2604.09459] From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models","url":"https://arxiv.org/abs/2604.09459"},{"title":"Towards Efficient Multi-Agent and Temporal Credit Assignment in","url":"https://www.ri.cmu.edu/app/uploads/2025/07/cmu_msr_thesis.pdf"},{"title":"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models","url":"https://arxiv.org/html/2604.09459v1"},{"title":"[2602.16165v1] HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents","url":"https://arxiv.org/abs/2602.16165v1"},{"title":"[2312.01072] A Survey of Temporal Credit Assignment in Deep Reinforcement Learning","url":"https://arxiv.org/abs/2312.01072"},{"title":"CALM: Credit Assignment with Language Models","url":"https://arxiv.org/html/2409.12798v1"},{"title":"Towards Efficient Multi-Agent and Temporal Credit Assignment in Reinforcement Learning - Robotics Institute Carnegie Mellon University","url":"https://www.ri.cmu.edu/publications/towards-efficient-multi-agent-and-temporal-credit-assignment-in-reinforcement-learning/"},{"title":"Retrospective In-Context Learning for Temporal Credit ...","url":"https://openreview.net/pdf?id=QAVpe6a3rp"},{"title":"Hindsight Credit Assignment for Long-Horizon LLM Agents","url":"https://arxiv.org/html/2603.08754v1"}]

I've completed the web search for "temporal credit assignment large language model reinforcement learning multi-step". Here are the key findings:

## Main Research Areas

Reinforcement learning for LLMs increasingly relies on sparse, outcome-level rewards, with credit assignment manifesting in two regimes: reasoning RL (where 
…[truncated 1769 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T12:22:12.576914+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.17008",
  "prompt": "Extract: title, authors, year, venue, abstract, core method (how they handle turn-level credit assignment), key experimental results, and any comparison between step-independent vs episode-level approaches. What is their \"Turn-PPO\" method exactly?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2512.17008",
    "prompt": "Extract: title, authors, year, venue, abstract, core method (how they handle turn-level credit assignment), key experimental results, and any comparison between step-independent vs episode-level approaches. What is their \"Turn-PPO\" method exactly?"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T12:22:12.577049+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.11821",
  "prompt": "Extract: title, authors, year, venue, abstract, core method for turn-level credit assignment and reward design, how they extend GRPO and PPO to multi-turn variants, key experimental results, and any discussion of advantage misattribution or sign issues."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2505.11821",
    "prompt": "Extract: title, authors, year, venue, abstract, core method for turn-level credit assignment and reward design, how they extend GRPO and PPO to multi-turn variants, key experimental results, and any discussion of advantage misattribution or sign issues."
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T12:22:12.577173+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.10978",
  "prompt": "Extract: title, authors, year, venue, abstract, core method of GiGPO (Group-in-Group Policy Optimization), how it achieves fine-grained credit assignment while being critic-free, anchor state grouping mechanism, key experimental results on ALFWorld and WebShop."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2505.10978",
    "prompt": "Extract: title, authors, year, venue, abstract, core method of GiGPO (Group-in-Group Policy Optimization), how it achieves fine-grained credit assignment while being critic-free, anchor state grouping mechanism, key experimental results on ALFWorld and WebShop."
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T12:22:12.577293+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.20073",
  "prompt": "Extract: title, authors, year, venue, abstract, the StarPO framework details, how RAGEN handles multi-turn credit assignment, the \"Echo Trap\" finding, key experimental results, and any discussion of step-level vs episode-level reward assignment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2504.20073",
    "prompt": "Extract: title, authors, year, venue, abstract, the StarPO framework details, how RAGEN handles multi-turn credit assignment, the \"Echo Trap\" finding, key experimental results, and any discussion of step-level vs episode-level reward assignment."
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-17T12:22:12.577427+00:00_

# Turn-PPO Paper Analysis

**Title:** Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs

**Authors:** Junbo Li, Peng Zhou, Rui Meng, Meet P. Vadera, Lihong Li, Yang Li

**Year:** 2025 (submitted December 18, 2025; revised January 23, 2026)

**Venue:** EACL 2026

**Abstract Summary:**
The authors address limitations in applying GRPO to multi-turn agent tasks. They investigate "more stable and effective advantage estimation strategies" and propose turn-PPO, which "operates on a turn-level MDP formulation, as opposed to the commonly used token-level MDP."

**Core Method—Turn-PPO:**
Rather than computing advantages at the token level (standard practice), turn-PPO reformulates the problem as a turn-level MDP. This shift in granularity enables better credit assignment across multi-turn interactions where individual token rewards may be sparse or delayed.

**Key Findings:**
- PPO proved "more robust than GRPO" for multi-turn scenarios
- Turn-PPO demonstrated effectiveness on WebShop and Sokoban benchmarks
- Performance gains occurred "both with and without long reasoning components"

**Comparison Note:**
The paper contrasts token-level MDPs (standard approach) against their turn-level alternative, positioning the latter as superior for long-horizon reasoning tasks requiring proper credit assignment across dialogue turns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-17T12:22:12.577569+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.19199",
  "prompt": "Extract: title, authors, year, venue, abstract, core method of implicit step rewards (iStar), how it assigns credit without explicit step labels, the trajectory-based DPO objective, key experimental results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2509.19199",
    "prompt": "Extract: title, authors, year, venue, abstract, core method of implicit step rewards (iStar), how it assigns credit without explicit step labels, the trajectory-based DPO objective, key experimental results."
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T12:22:12.577716+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "WebRL agent reinforcement learning credit assignment multi-turn 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "tool_args": {
    "query": "WebRL agent reinforcement learning credit assignment multi-turn 2024"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T12:22:12.577845+00:00_

# Paper Summary: Turn-Level Reward Design for LLM Agents

**Title:** Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design

**Authors:** Quan Wei, Siliang Zeng, Chenliang Li, William Brown, Oana Frunza, Wei Deng, Anderson Schneider, Yuriy Nevmyvaka, Yang Katie Zhao, Alfredo Garcia, Mingyi Hong

**Year:** 2025 (submitted May 17, 2025; revised October 23, 2025)

**Venue:** arXiv (cs.LG - Machine Learning)

## Abstract Summary
The work addresses limitations of sparse reward signals in reinforcement learning for multi-turn LLM agent reasoning. The authors propose "the first systematic study of turn-level reward design" to enable finer-grained credit assignment across reasoning steps.

## Core Method
The research extends GRPO and PPO algorithms with turn-level rewards incorporating two designs: "verifiable and LLM-as-judge" reward mechanisms. This approach replaces reliance solely on trajectory-level outcomes with intermediate signals at each decision step.

## Key Experimental Results
The methods demonstrate "greater stability, faster convergence, and higher accuracy" compared to baseline approaches. Across question-answering datasets, the approach achieved "highest answer correctness and 100% format correctness."

## Notable Gap
The provided content does not discuss advantage misattribution or sign issues in the reward assignment process.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T12:22:12.577973+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AgentTrek agent training reinforcement learning trajectory optimization 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AgentTrek agent training reinforcement learning trajectory optimization 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-17T12:22:12.578101+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "advantage misattribution sign error reinforcement learning sparse reward multi-step"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "tool_args": {
    "query": "advantage misattribution sign error reinforcement learning sparse reward multi-step"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-17T12:22:12.578248+00:00_

# Group-in-Group Policy Optimization for LLM Agent Training

**Title:** Group-in-Group Policy Optimization for LLM Agent Training

**Authors:** Lang Feng, Zhenghai Xue, Tingcong Liu, Bo An

**Year:** 2025

**Venue:** NeurIPS 2025

## Abstract Summary
The paper addresses limitations in applying group-based reinforcement learning to multi-turn LLM agents. The authors note that "agent-environment interactions unfold over many steps and often yield sparse or delayed rewards, making credit assignment across individual steps significantly more challenging."

## Core Method: GiGPO

GiGPO introduces a hierarchical two-level structure for advantage estimation:

1. **Episode-level (macro):** Computes relative advantages across groups of complete trajectories
2. **Step-level (micro):** Uses an anchor state grouping mechanism to retroactively construct step-level groups by identifying repeated environment states

This approach enables fine-grained per-step credit signals while maintaining the benefits of group-based RL: critic-free operation, low memory requirements, and stable convergence.

## Key Experimental Results

- **ALFWorld:** >12% performance improvement over GRPO
- **WebShop:** >9% performance improvement over GRPO  
- **QA Tasks:** 42.1% (3B model) and 47.2% (7B model)
- **Efficiency:** Maintains identical GPU memory overhead and LLM rollout with minimal additional computational cost

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T12:22:12.578391+00:00_

# Paper Summary: Agentic Reinforcement Learning with Implicit Step Rewards

**Title:** Agentic Reinforcement Learning with Implicit Step Rewards

**Authors:** Xiaoqian Liu, Ke Wang, Yuchuan Wu, Fei Huang, Yongbin Li, Junge Zhang, Jianbin Jiao

**Year:** 2025 (submitted September 23)

**Venue:** arXiv (cs.CL - Computation and Language)

## Abstract Overview
The researchers address a critical challenge in training LLM agents: assigning credit effectively when rewards are sparse. Their work tackles limitations of prior process supervision approaches that suffer from annotation bias and high variance.

## Core Method: iStar (Implicit Step Rewards)

The innovation centers on a strategy that "integrates seamlessly with standard RL algorithms without relying on additional rollouts or explicit step labels." Rather than requiring manual step-level annotations, iStar operates through:

1. **Process Reward Model (PRM):** Optimized alternately with the policy
2. **Trajectory-based DPO Objective:** Generates step rewards implicitly through a direct preference optimization framework
3. **Dual Advantage Integration:** Combines step-level and episode-level advantages in policy updates

## Credit Assignment Without Explicit Labels
The method achieves credit assignment by deriving step-wise rewards from trajectory-level preferences, eliminating dependency on costly human step annotations while maintaining theoretical grounding.

## Key Experimental Results
Testing across WebShop, VisualSokoban, and SOTOPIA benchmarks demonstrated "superior performance over frontier LLMs and strong RL baselines," achieving state-of-the-art results with improved sample efficiency and stability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-17T12:22:12.578526+00:00_

# RAGEN: LLM Agent Self-Evolution via Multi-Turn RL

**Title:** RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning

**Authors:** Zihan Wang, Kangrui Wang, Qineng Wang, Pingyue Zhang, Linjie Li, Zhengyuan Yang, Xing Jin, Kefan Yu, Minh Nhat Nguyen, Licheng Liu, Eli Gottlieb, Yiping Lu, Kyunghyun Cho, Jiajun Wu, Li Fei-Fei, Lijuan Wang, Yejin Choi, Manling Li

**Year:** 2025 (submitted April 24, 2025; revised May 26, 2025)

**Venue:** arXiv (cs.LG - Machine Learning)

## Abstract Summary

The paper addresses challenges in training LLMs as interactive agents through long-horizon decision-making and stochastic environmental feedback. The authors propose StarPO for trajectory-level agent RL and introduce RAGEN, a modular system for training and evaluation.

## StarPO Framework

StarPO represents "State-Thinking-Actions-Reward Policy Optimization," functioning as a general framework for trajectory-level agent reinforcement learning. The stabilized variant, StarPO-S, incorporates trajectory filtering, critic integration, and gradient stabilization mechanisms.

## Key Findings

**The Echo Trap:** The research identifies a recurring instability pattern where "reward variance cliffs and gradient spikes" occur during training, which StarPO-S addresses through stabilization techniques.

**Rollout Shaping:** Effective RL training benefits from diverse initial states, medium-granularity interactions, and frequent sampling.

**Reward Signal Requirements:** Without "fine-grained, reasoning-aware reward signals," agents fail to develop genuine reasoning, instead exhibiting shallow strategies or hallucinated reasoning steps.

## Credit Assignment & Reward Structure

The abstract emphasizes trajectory-level (episode-level) optimization rather than step-level approaches, stressing that multi-turn agent RL requires reasoning-aware signals for proper credit assignment across extended agent interactions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T12:22:12.578713+00:00_

Web search results for query: "AgentTrek agent training reinforcement learning trajectory optimization 2024 2025"

Links: [{"title":"GitHub - xlang-ai/AgentTrek: [ICLR2025 Spotlight] Agent Trajectory Synthesis via Guiding Replay with Web Tutorials · GitHub","url":"https://github.com/xlang-ai/AgentTrek"},{"title":"AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials","url":"https://agenttrek.github.io/"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials | OpenReview","url":"https://openreview.net/forum?id=EEgYUccwsV"},{"title":"WebSynthesis: World-Model-Guided MCTS for Efficient WebUI-Trajectory Synthesis","url":"https://arxiv.org/html/2507.04370v1"},{"title":"AgentTrek: Agent Trajectory synthesis","url":"https://openreview.net/pdf/e95d923ccea15b1bab268aeeb8b3845547e3dafe.pdf"},{"title":"[2412.09605] AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials","url":"https://arxiv.org/abs/2412.09605"},{"title":"[Quick Review] AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials","url":"https://liner.com/review/agenttrek-agent-trajectory-synthesis-via-guiding-replay-with-web-tutorials"},{"title":"Dec 2025 Training One Model to Master Cross-Level","url":"https://arxiv.org/pdf/2512.09706"},{"title":"Paper page - AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials","url":"https://huggingface.co/papers/2412.09605"}]

Based on the search results, I found comprehensive information about AgentTrek:

## Overview

AgentTrek is an ICLR 2025 Spotlight paper on Agent Trajectory Synthesis via Guiding Replay with Web Tutorials.

## What It Does

AgentTrek is a scalable data synthesis pipeline that generates high-quality web agent trajectories by le
…[truncated 1494 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-17T12:22:12.578893+00:00_

Web search results for query: "WebRL agent reinforcement learning credit assignment multi-turn 2024"

Links: [{"title":"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models","url":"https://arxiv.org/html/2604.09459v1"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2505.16421v1"},{"title":"WEBAGENT-R1: Training Web Agents via End-to-End Multi-Turn","url":"https://arxiv.org/pdf/2505.16421"},{"title":"ICML Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Credit Assignment","url":"https://icml.cc/virtual/2025/49783"},{"title":"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Credit Assignment","url":"https://arxiv.org/html/2505.11821v1"},{"title":"NeurIPS A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning","url":"https://neurips.cc/virtual/2025/127960"},{"title":"GitHub - xxzcc/Awesome-Credit-Assignment-in-LLM-RL · GitHub","url":"https://github.com/xxzcc/Awesome-Credit-Assignment-in-LLM-RL"},{"title":"NeurIPS Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design and Credit Assignment","url":"https://neurips.cc/virtual/2025/133311"},{"title":"Multi-Turn Credit Assignment with LLM Agents - hlfshell","url":"https://hlfshell.ai/posts/multi-turn-credit-assignment/"}]

Based on the search results, here's what I found about WebRL agents, reinforcement learning, credit assignment, and multi-turn interactions in 2024:

## Overview of WebRL and Agentic RL

WebRL is part of the second wave of agentic RL that extends reinforcement learning to multi-turn interactive tasks, including LLM agents that browse the web. WebRL trains LLM web agents via self-evolving online curriculum reinforce
…[truncated 1154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T12:22:12.579075+00:00_

Web search results for query: "advantage misattribution sign error reinforcement learning sparse reward multi-step"

Links: [{"title":"sparse- reward multi-agent reinforcement learning","url":"https://arxiv.org/pdf/2509.21828"},{"title":"University of Sheﬃeld Dealing with Sparse Rewards in Reinforcement Learning","url":"https://arxiv.org/pdf/1910.09281"},{"title":"Reinforcement Learning: Dealing with Sparse Reward Environments | by Karam Daaboul | Medium","url":"https://medium.com/@m.k.daaboul/dealing-with-sparse-reward-environments-38c0489c844d"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"Sparse Rewards in Reinforcement Learning - GeeksforGeeks","url":"https://www.geeksforgeeks.org/machine-learning/sparse-rewards-in-reinforcement-learning/"},{"title":"Learning to Generalize from Sparse and Underspeciﬁed Rewards","url":"https://arxiv.org/pdf/1902.07198"},{"title":"Shaping Sparse Rewards in Reinforcement Learning: A Semi-supervised Approach","url":"https://arxiv.org/html/2501.19128v4"},{"title":"Revisiting Sparse Rewards for Goal-Reaching Reinforcement Learning","url":"https://arxiv.org/html/2407.00324v2"},{"title":"Hybrid Reinforcement:When Reward Is Sparse, It’s Better to Be Dense","url":"https://arxiv.org/html/2510.07242v1"},{"title":"(PDF) Reinforcement Learning with Sparse Rewards: Developing Algorithms for Learning in Environments with Infrequent Feedback","url":"https://www.researchgate.net/publication/391371020_Reinforcement_Learning_with_Sparse_Rewards_Developing_Algorithms_for_Learning_in_Environments_with_Infrequent_Feedback"}]

The search has been completed. Here are the results for your query "advantage misattribution sign error reinforcement learning sparse reward multi-step":

The search results cover several related topics in reinforcement learning with sparse rewards and multi-step learning:

**Sparse Reward Challenges:** A common
…[truncated 1597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T12:22:12.579258+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.20732",
  "prompt": "Extract: title, authors, year, venue, abstract, core method of SPA-RL (Stepwise Progress Attribution), how it measures progress toward task completion as intermediate rewards, key experimental results and benchmarks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2505.20732",
    "prompt": "Extract: title, authors, year, venue, abstract, core method of SPA-RL (Stepwise Progress Attribution), how it measures progress toward task completion as intermediate rewards, key experimental results and benchmarks."
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-17T12:22:12.579388+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.08754",
  "prompt": "Extract: title, authors, year, venue, abstract, core method of HCAPO (Hindsight Credit Assignment Policy Optimization), how it refines trajectory-level feedback into step-level advantage signals, key experimental results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2603.08754",
    "prompt": "Extract: title, authors, year, venue, abstract, core method of HCAPO (Hindsight Credit Assignment Policy Optimization), how it refines trajectory-level feedback into step-level advantage signals, key experimental results."
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T12:22:12.579507+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.16165",
  "prompt": "Extract: title, authors, year, venue, abstract, core method of HiPER (Hierarchical Plan-Execute RL), how it separates planning from execution for credit assignment, key experimental results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2602.16165",
    "prompt": "Extract: title, authors, year, venue, abstract, core method of HiPER (Hierarchical Plan-Execute RL), how it separates planning from execution for credit assignment, key experimental results."
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T12:22:12.579650+00:00_

# SPA-RL: Paper Summary

**Title:** SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution

**Authors:** Hanlin Wang, Chak Tou Leong, Jiashuo Wang, Jian Wang, Wenjie Li

**Year:** 2025 (submitted May 27, 2025)

**Venue:** arXiv (cs.CL - Computation and Language)

## Abstract
The paper addresses a critical challenge in reinforcement learning for LLM agents: "delayed rewards: feedback signals are typically available only after the entire task is completed." This makes it difficult to guide earlier actions effectively.

## Core Method
Stepwise Progress Attribution (SPA) is a reward redistribution framework that decomposes final task rewards into individual step contributions. The approach trains a progress estimator that accumulates stepwise contributions across a trajectory to match task completion. During policy optimization, estimated per-step contributions combine with action grounding signals to create fine-grained intermediate rewards.

## Key Experimental Results
Testing on benchmark environments (Webshop, ALFWorld, and VirtualHome) shows:
- Success rate improvement of +2.5% on average
- Grounding accuracy improvement of +1.9% on average
- More effective intermediate rewards for RL training compared to state-of-the-art methods

**Code availability:** [GitHub repository provided](https://github.com/WangHanLinHenry/SPA-RL-Agent)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T12:22:12.579788+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.09459",
  "prompt": "Extract: title, authors, year, abstract. This is a survey paper on credit assignment in LLM RL. Extract: taxonomy of credit assignment methods, key categories (reasoning RL vs agentic RL), how many papers covered, key findings about step-level vs episode-level, any discussion of advantage sign issues or misattribution."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2604.09459",
    "prompt": "Extract: title, authors, year, abstract. This is a survey paper on credit assignment in LLM RL. Extract: taxonomy of credit assignment methods, key categories (reasoning RL vs agentic RL), how many papers covered, key findings about step-level vs episode-level, any discussion of advantage sign issues or misattribution."
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T12:22:12.579920+00:00_

# Paper Summary: Hindsight Credit Assignment for Long-Horizon LLM Agents

**Title:** Hindsight Credit Assignment for Long-Horizon LLM Agents

**Authors:** Hui-Ze Tan, Xiao-Wen Yang, Hao Chen, Jie-Jing Shao, Yi Wen, Yuteng Shen, Weihong Luo, Xiku Du, Lan-Zhe Guo, Yu-Feng Li

**Year:** 2026 (submitted March 7, 2026)

**Venue:** arXiv (Computer Science - Machine Learning category)

## Abstract
The paper addresses a critical challenge in agent training: "credit assignment challenges in long-horizon, multi-step tasks due to sparse rewards." Existing methods like GRPO struggle with inaccurate Q-value estimates and misaligned baselines for intermediate states.

## Core Method: HCAPO
HCAPO (Hindsight Credit Assignment Policy Optimization) operates through two key mechanisms:

1. **Post-hoc Critic Refinement:** The LLM itself functions as "a post-hoc critic to refine step-level Q-values through hindsight reasoning," enabling retrospective analysis of decision quality.

2. **Multi-scale Advantage Mechanism:** HCAPO employs "a multi-scale advantage mechanism" that addresses value baseline inaccuracies at critical decision points, converting overall trajectory rewards into granular step-level signals.

## Key Experimental Results
- **WebShop:** 7.7% success rate improvement over GRPO (Qwen2.5-7B-Instruct)
- **ALFWorld:** 13.8% improvement over GRPO
- Demonstrates enhanced "exploration efficiency, promotes concise decision-making, and ensures scalability"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T12:22:12.580054+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2411.03817",
  "prompt": "Extract: title, authors, year, venue, abstract, core method of StepAgent (step-wise reinforcement learning for LLM agents), how it generates intermediate rewards by comparing expert and agent actions, key experimental results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2411.03817",
    "prompt": "Extract: title, authors, year, venue, abstract, core method of StepAgent (step-wise reinforcement learning for LLM agents), how it generates intermediate rewards by comparing expert and agent actions, key experimental results."
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-17T12:22:12.580369+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.16421",
  "prompt": "Extract: title, authors, year, venue, abstract, core method of WebAgent-R1 for multi-turn web agent RL training, how it handles credit assignment, key experimental results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2505.16421",
    "prompt": "Extract: title, authors, year, venue, abstract, core method of WebAgent-R1 for multi-turn web agent RL training, how it handles credit assignment, key experimental results."
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-17T12:22:12.580538+00:00_

# HiPER: Paper Summary

**Title:** HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents

**Authors:** Jiangweizhi Peng, Yuanxin Liu, Ruida Zhou, Charles Fleming, Zhaoran Wang, Alfredo Garcia, Mingyi Hong

**Year:** 2026 (submitted February 18, 2026)

**Venue:** arXiv (cs.LG - Computer Science, Machine Learning)

## Abstract
The paper addresses training LLMs as interactive agents for extended decision-making tasks with sparse rewards. Traditional flat RL approaches struggle to propagate credit effectively across long action sequences.

## Core Method
HiPER implements a two-level hierarchical architecture. The framework features "a high-level planner that proposes subgoals and a low-level executor that carries them out over multiple action steps." The key innovation is hierarchical advantage estimation (HAE), which "carefully assigns credit at both the planning and execution levels" by aggregating returns for each subgoal and coordinating updates across both tiers.

## Planning vs. Execution Separation
Rather than treating agents as flat policies, HiPER explicitly decomposes decision-making into hierarchical levels. This temporal abstraction enables more effective credit assignment compared to standard approaches that "must propagate credit across the entire trajectory without explicit temporal abstraction."

## Key Results
- ALFWorld: 97.4% success rate (+6.6% improvement)
- WebShop: 83.3% success rate (+8.3% improvement)
- Model: Qwen2.5-7B-Instruct
- Particularly strong performance on long-horizon tasks requiring multiple dependent subtasks

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-17T12:22:12.580712+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "WebRL web agent self-evolving online curriculum reinforcement learning arXiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "tool_args": {
    "query": "WebRL web agent self-evolving online curriculum reinforcement learning arXiv 2024"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-17T12:22:12.580861+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GAE generalized advantage estimation language model agent reinforcement learning multi-turn 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GAE generalized advantage estimation language model agent reinforcement learning multi-turn 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-17T12:22:12.580993+00:00_

# Credit Assignment in RL for LLMs: Survey Summary

**Title:** From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models

**Author:** Chenchen Zhang

**Year:** 2026

**Abstract Summary:** This survey examines the challenge of determining "which actions within a long trajectory caused the outcome" across two distinct settings: reasoning RL (single chain-of-thought, 500-30K+ tokens) and agentic RL (multi-turn interaction, 100K-1M tokens).

## Taxonomy & Coverage

The paper surveys **47 credit assignment methods** organized across two dimensions:

1. **Granularity:** token, segment, step, turn, multi-agent
2. **Methodology:** Monte Carlo, temporal difference, model-based, game-theoretic, information-theoretic

## Key Findings

**Reasoning vs. Agentic Distinction:** The work identifies a fundamental shift in the landscape. "Reasoning CA is maturing around process reward models and critic-free group comparison, while agentic CA is driving genuinely new approaches" including hindsight counterfactual analysis and turn-level MDP reformulations.

**Episode-Level Limitations:** The abstract emphasizes that episode-level rewards become "increasingly uninformative" at longer horizons, highlighting the inadequacy of simple outcome-only signals for complex trajectories.

## Contributions

Beyond the taxonomy, the paper provides:
- Machine-readable paper inventory with baseline families
- Reporting checklist identifying methodological gaps
- Benchmark protocol with task families and method selection decision tree

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-17T12:22:12.581131+00:00_

# StepAgent: LLM Agent Policy Optimization

**Title:** From Novice to Expert: LLM Agent Policy Optimization via Step-wise Reinforcement Learning

**Authors:** Zhirui Deng, Zhicheng Dou, Yutao Zhu, Ji-Rong Wen, Ruibin Xiong, Mang Wang, Weipeng Chen

**Year:** 2024 (submitted November 6, 2024)

**Venue:** arXiv (cs.AI)

## Abstract Summary

The paper addresses a critical limitation in LLM agent training: sparse reward signals. Traditional approaches provide only final outcomes, making policy learning inefficient for multi-step reasoning tasks.

## Core Method: Step-wise Reinforcement Learning

StepAgent introduces granular reward structures by automatically comparing expert and agent behaviors at each step. Rather than waiting for task completion to receive feedback, the system generates intermediate rewards throughout the decision chain, enabling finer-grained policy optimization.

The approach incorporates:
- **Intermediate reward generation** through expert-agent action comparisons
- **Implicit-reward techniques** for agent self-reflection
- **Inverse reinforcement learning** to facilitate policy adjustment

## Theoretical Contribution

The authors provide formal analysis showing that "the action distribution of the agent can converge toward the expert action distribution over multiple training cycles," grounding their empirical approach in theoretical foundations.

## Key Results

Experimental validation across multiple datasets demonstrates that StepAgent outperforms existing baseline methods, validating the effectiveness of step-wise optimization over traditional sparse-reward approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-17T12:22:12.581272+00:00_

# WebAgent-R1: Research Paper Summary

**Title:** WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning

**Authors:** Zhepei Wei, Wenlin Yao, Yao Liu, Weizhi Zhang, Qin Lu, Liang Qiu, Changlong Yu, Puyang Xu, Chao Zhang, Bing Yin, Hyokun Yun, Lihong Li

**Year:** 2025

**Venue:** EMNLP 2025

**Abstract:** The paper addresses training web agents for multi-turn interactions through reinforcement learning. The system "learns directly from online interactions with web environments by asynchronously generating diverse trajectories, entirely guided by binary rewards depending on task success."

---

## Core Method

WebAgent-R1 employs an end-to-end multi-turn RL framework that generates diverse trajectories from actual web environment interactions. The approach uses binary success-based rewards to guide learning, incorporating thinking-based prompting strategies and behavior cloning as a warm-up training stage.

## Credit Assignment

The paper doesn't explicitly detail a sophisticated credit assignment mechanism—it relies on binary reward signals contingent on task completion rather than intermediate step rewards. This suggests credit assignment occurs implicitly through the RL optimization process across the full trajectory.

## Key Experimental Results

- **Qwen-2.5-3B:** Performance improved from 6.1% to 33.9% task success rate
- **Llama-3.1-8B:** Performance improved from 8.5% to 44.8% task success rate
- Results significantly outperformed existing methods and proprietary models including OpenAI o3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-17T12:22:12.581444+00:00_

Web search results for query: "WebRL web agent self-evolving online curriculum reinforcement learning arXiv 2024"

Links: [{"title":"[2411.02337] WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning","url":"https://arxiv.org/abs/2411.02337"},{"title":"WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning","url":"https://arxiv.org/html/2411.02337v1"},{"title":"GitHub - THUDM/WebRL: Building Open LLM Web Agents with Self-Evolving Online Curriculum RL · GitHub","url":"https://github.com/THUDM/WebRL"},{"title":"[2411.02337v1] WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning","url":"https://arxiv.org/abs/2411.02337v1"},{"title":"webrl: training llm web agents via self","url":"https://arxiv.org/pdf/2411.02337"},{"title":"Preprint WEBRL: TRAINING LLM WEB AGENTS VIA SELF-","url":"https://arxiv.org/pdf/2411.02337v1"},{"title":"WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/webrl-training-llm-web-agents-via-self"},{"title":"WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=oVKEAFjEqv"},{"title":"WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning - Paper Detail","url":"https://deeplearn.org/arxiv/554503/webrl:-training-llm-web-agents-via-self-evolving-online-curriculum-reinforcement-learning"},{"title":"[PDF] WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/WebRL:-Training-LLM-Web-Agents-via-Self-Evolving-Qi-Liu/bde841b0dbbf7a15ee69966a828c7fe2cf532ad9"}]

I found detailed information about WebRL. Here's a summary of the search results:

## WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcem
…[truncated 1261 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-17T12:22:12.581644+00:00_

Web search results for query: "GAE generalized advantage estimation language model agent reinforcement learning multi-turn 2024 2025"

Links: [{"title":"VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents","url":"https://vagen-ai.github.io/vagen_paper.pdf"},{"title":"Generalized Advantage Estimation (GAE)","url":"https://apxml.com/courses/advanced-reinforcement-learning/chapter-3-advanced-policy-gradients-actor-critic/generalized-advantage-estimation"},{"title":"GAGPO: Generalized Advantage Grouped Policy Optimization","url":"https://arxiv.org/html/2605.13217"},{"title":"Generalized Advantage Estimation (GAE)","url":"https://www.emergentmind.com/topics/generalized-advantage-estimation-gae"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via ...","url":"https://arxiv.org/pdf/2504.20073"},{"title":"GitHub - bsivanantham/GAE: Reinforcement learning algorithms with Generalized Advantage Estimation · GitHub","url":"https://github.com/bsivanantham/GAE"},{"title":"What are GAEs (Generalized Advantage Estimations) in Reinforcement Learning? | BoxingBytes","url":"https://boxingbytes.github.io/2025/03/20/gae.html"},{"title":"Extended Generalized Advantage Estimation (EGAE)","url":"https://www.emergentmind.com/topics/extended-generalized-advantage-estimation-egae"},{"title":"AgentRM: Enhancing Agent Generalization with Reward ...","url":"https://aclanthology.org/2025.acl-long.945.pdf"},{"title":"Generalized Advantage Estimation (GAE)","url":"https://nn.labml.ai/rl/ppo/gae.html"}]

Based on the web search results, here's what I found about GAE (Generalized Advantage Estimation) in the context of language model agents and reinforcement learning for multi-turn tasks in 2024-2025:

## Key Research Areas

### VAGEN Framework (Multi-Turn Vision-Language Agents)
VAGEN uses Token-Level Generalized Advantage Estimation (GAE), applying a per-token KL penalty at each token index to encourage the current policy to stay close to a frozen reference policy. The fr
…[truncated 1347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-17T12:22:12.581838+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2411.02337",
  "prompt": "Extract: title, authors, year, venue, abstract, core method of WebRL (self-evolving curriculum, outcome-supervised reward model, adaptive RL), how it handles credit assignment with sparse rewards, key experimental results on WebArena."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2411.02337",
    "prompt": "Extract: title, authors, year, venue, abstract, core method of WebRL (self-evolving curriculum, outcome-supervised reward model, adaptive RL), how it handles credit assignment with sparse rewards, key experimental results on WebArena."
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-17T12:22:12.581967+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2605.13217",
  "prompt": "Extract: title, authors, year, abstract, core method of GAGPO (Generalized Advantage Grouped Policy Optimization), how it extends critic-free grouped RL to multi-turn agent training with temporally propagated step-aligned credit assignment, key experimental results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2605.13217",
    "prompt": "Extract: title, authors, year, abstract, core method of GAGPO (Generalized Advantage Grouped Policy Optimization), how it extends critic-free grouped RL to multi-turn agent training with temporally propagated step-aligned credit assignment, key experimental results."
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-17T12:22:12.582242+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2512.17008v1",
  "prompt": "Extract the detailed method section of Turn-PPO: (1) How exactly is the turn-level MDP formulated? (2) How is advantage computed at the turn level vs token level? (3) What specific problems did they identify with GRPO in multi-turn settings? (4) Any discussion of advantage sign issues or misattribution? (5) Detailed experimental results comparing Turn-PPO vs GRPO vs standard PPO. (6) WebShop and Sokoban results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2512.17008v1",
    "prompt": "Extract the detailed method section of Turn-PPO: (1) How exactly is the turn-level MDP formulated? (2) How is advantage computed at the turn level vs token level? (3) What specific problems did they identify with GRPO in multi-turn settings? (4) Any discussion of advantage sign issues or misattribution? (5) Detailed experimental results comparing Turn-PPO vs GRPO vs standard PPO. (6) WebShop and Sokoban results."
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-17T12:22:12.582373+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Planner-R1\" reward shaping agentic RL smaller LLMs arXiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Planner-R1\" reward shaping agentic RL smaller LLMs arXiv 2025"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-17T12:22:12.582518+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VAGEN bi-level GAE turn-aware credit assignment multi-turn VLM agent 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VAGEN bi-level GAE turn-aware credit assignment multi-turn VLM agent 2025"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-17T12:22:12.582755+00:00_

# GAGPO: Generalized Advantage Grouped Policy Optimization

**Title:** GAGPO: Generalized Advantage Grouped Policy Optimization

**Authors:** Siyuan Zhu, Chao Yu, Rongxin Yang, Zongkai Liu, Jinjun Hu, Qiwen Chen, Yibo Zhang

**Year:** 2026 (arXiv:2605.13217v1, posted May 13, 2026)

## Abstract Summary

GAGPO addresses credit assignment challenges in multi-turn language model agent training through reinforcement learning. The method tackles the difficulty of propagating sparse, delayed trajectory-level rewards back to individual intermediate actions without requiring auxiliary value models.

## Core Method

GAGPO introduces three key innovations for step-aligned temporal credit assignment:

1. **Grouped Value Proxy:** Constructs a non-parametric value estimate by "averaging the discounted returns of steps in the same [environmental] group" across sampled rollouts, enabling TD/GAE-style advantage computation without a learned critic.

2. **Temporal Credit Propagation:** Implements recursive advantage estimation using the formula A^t = δt + γλA^(t+1), where temporal-difference residuals propagate delayed outcomes backward through time.

3. **Group-Normalized PPO:** Applies normalization within rollout groups rather than across batches, and uses sequence-level importance ratios for multi-token actions to maintain coherent optimization signals.

## Key Experimental Results

**ALFWorld Performance:**
- Qwen2.5-1.5B: 93.5% success (vs. 88.1% for prior best)
- Qwen2.5-7B: 95.6% success (vs. 88.8% for prior best)

**WebShop Performance:**
- 1.5B model: 88.6 score, 78.1% success rate
- 7B model: 90.3 score, 77.5% success rate

**Learning Efficiency:** GAGPO demonstrates faster early-stage improvement, smoother optimization dynamics with lower gradient variance, and substantially lower advantage signal variance compared to baseline GiGPO.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-17T12:22:12.583010+00:00_

# WebRL Paper Summary

**Title:** WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning

**Authors:** Zehan Qi, Xiao Liu, Iat Long Iong, Hanyu Lai, Xueqiao Sun, Wenyi Zhao, Yu Yang, Xinyue Yang, Jiadai Sun, Shuntian Yao, Tianjie Zhang, Wei Xu, Jie Tang, Yuxiao Dong

**Year:** 2024 (submitted November 4, 2024; published at ICLR 2025)

**Venue:** ICLR 2025

## Abstract Summary

The paper addresses training open-source language models to function as effective web agents. The authors note that "LLMs have shown remarkable potential as autonomous agents, particularly in web-based tasks" but existing approaches rely on expensive proprietary APIs.

## Core WebRL Methods

**Three key components:**

1. **Self-Evolving Curriculum:** Generates new training tasks dynamically from unsuccessful attempts, expanding limited task availability
2. **Outcome-Supervised Reward Model (ORM):** Provides robust reward signals despite sparse feedback in web navigation environments
3. **Adaptive Reinforcement Learning:** Maintains consistent performance improvements while mitigating policy distribution drift during online training

## Handling Sparse Rewards

The outcome-supervised reward model specifically addresses credit assignment challenges by supervising rewards based on task completion outcomes rather than relying on intermediate signals.

## Key Experimental Results (WebArena-Lite)

- Llama-3.1-8B: improved from 4.8% to 42.4% success rate
- GLM-4-9B: improved from 6.1% to 43% success rate
- Both significantly outperformed GPT-4-Turbo (17.6%) and GPT-4o (13.9%)
- Exceeded previous state-of-the-art open-model approach (AutoWebGLM, 18.2%)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-17T12:22:12.583272+00:00_

Web search results for query: ""Planner-R1" reward shaping agentic RL smaller LLMs arXiv 2025"

Links: [{"title":"[2509.25779] Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs","url":"https://arxiv.org/abs/2509.25779"},{"title":"Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs","url":"https://arxiv.org/html/2509.25779v2"},{"title":"PLANNER-R1: REWARD SHAPING ENABLES EFFI- CIENT AGENTIC RL WITH SMALLER LLMS","url":"https://arxiv.org/pdf/2509.25779"},{"title":"Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs | OpenReview","url":"https://openreview.net/forum?id=CmOaD42eAT"},{"title":"Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250925779Z/abstract"},{"title":"Planner-R1: Reward Shaping Enables Efficient Agentic RL ...","url":"https://www.researchgate.net/publication/396048946_Planner-R1_Reward_Shaping_Enables_Efficient_Agentic_RL_with_Smaller_LLMs"},{"title":"PLANNER-R1: REWARD SHAPING ENABLES EFFI","url":"https://openreview.net/pdf/24fff7e9068e6d8af9f07e73abfdcb0d788c3abe.pdf"},{"title":"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey","url":"https://arxiv.org/html/2509.02547v4"},{"title":"Enhancing Agentic RL with Progressive Reward Shaping and...","url":"https://arxiv.org/abs/2512.07478"},{"title":"Enhancing Agentic RL with Progressive Reward Shaping and Value-based Sampling Policy Optimization","url":"https://arxiv.org/html/2512.07478"}]

I found comprehensive information about the Planner-R1 paper. Here's a summary:

## Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs

Planner-R1 achieved a 56.9% final-pass rate with only 180 training queries, a 2.7× improvement over GPT-5's 21.2% baseline and the strongest agentic result on the public leaderboard on the TravelPlanner benchmark.

### Key Findings

A central finding was that smaller models (8B) were highly respons
…[truncated 1063 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-17T12:22:12.583541+00:00_

# Turn-PPO Method Analysis

## (1) Turn-Level MDP Formulation

The turn-MDP redefines the state-action structure fundamentally. Rather than treating individual tokens as actions, the authors define the state as "the full interaction history up to the (h−1)-th round together with the current h-th query," while the action becomes "the LLM's response at round h." This creates uniform representation where every state is complete history plus current query, and every action is a full response.

## (2) Advantage Computation: Turn vs Token Level

**Token-level PPO** computes advantages at each token using the critic's value predictions: γV_{t+1} − V_t for intermediate tokens and r − V_T for final tokens, with clipping performed per token.

**Turn-PPO** operates at turn granularity, computing advantages as γV_{n+1} − V_n for intermediate turns and r − V_N for final turns. Critically, "the entire LLM response for that turn is considered the action, so the computed advantage applies to the whole response." This yields much higher clipping ratios, preventing unstable updates when policy shifts dramatically.

## (3) GRPO Problems in Multi-Turn Settings

The paper identifies two fundamental issues:

1. **Uniform advantage assignment**: GRPO applies "the same advantage uniformly to all tokens across turns," ignoring that different turns "contribute unequally to the final reward."

2. **High variance in advantage estimation**: The "state representation misalignment" occurs because "within a response, the next state is simply the current state with one token appended, whereas across responses, the next state incorporates an entire block of tokens from the environment output." This causes the critic to regress toward averaged values, degrading advantage quality.

## (4) Advantage Sign Issues

The paper doesn't explicitly discuss advantage sign misattribution but emphasizes that token-level MDPs suffer from "state representation misalignment," complicating critic learning through het
…[truncated 1223 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-17T12:22:12.583799+00:00_

Web search results for query: "VAGEN bi-level GAE turn-aware credit assignment multi-turn VLM agent 2025"

Links: [{"title":"VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents","url":"https://vagen-ai.github.io/vagen_paper.pdf"},{"title":"[2510.16907] VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents","url":"https://arxiv.org/abs/2510.16907"},{"title":"VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents | OpenReview","url":"https://openreview.net/forum?id=xpjWEgf8zi"},{"title":"VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents","url":"https://arxiv.org/html/2510.16907v1"},{"title":"VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/vagen-reinforcing-world-model-reasoning-for-multi-turn-vlm-agents/"},{"title":"VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents","url":"https://www.researchgate.net/publication/396715759_VAGEN_Reinforcing_World_Model_Reasoning_for_Multi-Turn_VLM_Agents"},{"title":"VAGEN - VLM Agent Training","url":"https://vagen-ai.github.io/"},{"title":"[2510.16907v1] VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents","url":"https://arxiv.org/abs/2510.16907v1"},{"title":"VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.16907v1"},{"title":"VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents","url":"https://openreview.net/pdf/ed11882b04656406635941c99bb0b5dbf475a088.pdf"}]

Based on the search results, I found comprehensive information about VAGEN. Here's what the research presents:

## VAGEN: Overview

VAGEN is a scalable system for training and analyzing multi-turn VLM agents in diverse visual environments.

## Key Challenge

A key challenge in training Vision-Language Model (VLM) agents, compared to Language Model (LLM) agents, lies in the shift from textual states to c
…[truncated 1251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-17T12:22:12.583998+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.16907",
  "prompt": "Extract: title, authors, year, venue, abstract, detailed description of Bi-Level GAE method (how turn-level advantages are computed first, then propagated to token level), key experimental results and benchmarks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2510.16907",
    "prompt": "Extract: title, authors, year, venue, abstract, detailed description of Bi-Level GAE method (how turn-level advantages are computed first, then propagated to token level), key experimental results and benchmarks."
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-17T12:22:12.584131+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.25779",
  "prompt": "Extract: title, authors, year, venue, abstract, core findings on reward shaping for agentic RL (dense vs sparse rewards, effect on smaller vs larger models), key experimental results on TravelPlanner benchmark."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2509.25779",
    "prompt": "Extract: title, authors, year, venue, abstract, core findings on reward shaping for agentic RL (dense vs sparse rewards, effect on smaller vs larger models), key experimental results on TravelPlanner benchmark."
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-17T12:22:12.584355+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ArCHer hierarchical reinforcement learning language model multi-turn token-level turn-level 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ArCHer hierarchical reinforcement learning language model multi-turn token-level turn-level 2024"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-17T12:22:12.584488+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"practitioner guide\" multi-turn agentic reinforcement learning NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"practitioner guide\" multi-turn agentic reinforcement learning NeurIPS 2025"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-17T12:22:12.584608+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSeek-R1 GRPO reinforcement learning reasoning credit assignment token-level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSeek-R1 GRPO reinforcement learning reasoning credit assignment token-level"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-17T12:22:12.584923+00:00_

# VAGEN: Paper Summary

**Title:** "VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents"

**Authors:** Kangrui Wang, Pingyue Zhang, Zihan Wang, Yaning Gao, Linjie Li, Qineng Wang, Hanyang Chen, Chi Wan, Yiping Lu, Zhengyuan Yang, Lijuan Wang, Ranjay Krishna, Jiajun Wu, Li Fei-Fei, Yejin Choi, and Manling Li

**Year:** 2025 (submitted October 19, 2025)

**Venue:** NeurIPS 2025

## Abstract Summary

The research tackles a critical challenge in training vision-language model agents: moving from text-based to visually-grounded reasoning. The authors propose that "VLM agents construct internal world models through explicit visual state" decomposition, focusing on State Estimation and Transition Modeling as core components.

## Bi-Level GAE Method

The paper introduces Bi-Level General Advantage Estimation (Bi-Level GAE) as a credit assignment mechanism. Rather than providing detailed equations in the source material, the abstract indicates this method enables "turn-aware credit assignment," suggesting advantages are first computed at the turn (interaction step) level before distribution to individual token positions within each turn.

## Key Results

A 3-billion parameter model achieved:
- **0.82 score** across five diverse agent benchmarks
- **3× improvement** over untrained baseline (0.21)
- **Outperformed** GPT-5 (0.75), Gemini 2.5 Pro (0.67), and Claude 4.5 (0.62)

The framework, VAGEN, demonstrates that optimal internal representation varies by task—natural language for semantic tasks, structured formats for precise manipulation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-17T12:22:12.585143+00:00_

# Planner-R1: Paper Summary

**Title:** Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs

**Authors:** Siyu Zhu, Yanbin Jiang, Hejian Sang, Shao Tang, Qingquan Song, Biao He, Rohit Jain, Zhipeng Wang, Alborz Geramifard

**Year:** 2025 (submitted September 30, 2025)

**Venue:** arXiv (cs.AI - Computer Science/Artificial Intelligence)

## Abstract Summary
The research examines agent-based reinforcement learning using language models on the TravelPlanner benchmark, focusing on how reward shaping influences training efficiency across different model sizes.

## Core Findings on Reward Shaping

**Dense vs. Sparse Rewards:**
- Dense process-level reward signals proved significantly more effective than sparse approaches
- "Shaped rewards consistently amplified learning dynamics"

**Effect on Model Sizes:**
- **Smaller models (8B parameters):** Highly responsive to reward shaping, achieving competitive results while being "3.5× more compute-efficient and 1.5× more memory-efficient than 32B models"
- **Larger models (32B+):** More robust under sparse rewards but showed smaller relative gains from shaping and higher variance

## Key TravelPlanner Results
- **56.9% final-pass rate** achieved with only 180 training queries
- Represents a **2.7× improvement** over GPT-5's 21.2% baseline
- Strongest public leaderboard performance for agentic approaches
- Generalization maintained: models performed comparably on out-of-domain tasks

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-17T12:22:12.585327+00:00_

Web search results for query: "ArCHer hierarchical reinforcement learning language model multi-turn token-level turn-level 2024"

Links: [{"title":"[2402.19446] ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL","url":"https://arxiv.org/abs/2402.19446"},{"title":"ICML Poster ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL","url":"https://icml.cc/virtual/2024/poster/33654"},{"title":"ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL","url":"https://proceedings.mlr.press/v235/zhou24t.html"},{"title":"GitHub - YifeiZhou02/ArCHer: Research Code for \"ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL\" · GitHub","url":"https://github.com/YifeiZhou02/ArCHer"},{"title":"ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL","url":"https://yifeizhou02.github.io/archer.io/"},{"title":"training language model agents via hierarchical multi-turn RL","url":"https://dl.acm.org/doi/10.5555/3692070.3694644"},{"title":"[Quick Review] ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL","url":"https://liner.com/review/archer-training-language-model-agents-via-hierarchical-multiturn-rl"},{"title":"ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL","url":"https://arxiv.org/html/2402.19446v1"},{"title":"ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL | Jiayi Pan","url":"https://jiayipan.me/publication/archer/"},{"title":"[2402.19446v1] ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL","url":"https://arxiv.org/abs/2402.19446v1"}]

I found comprehensive information about ArCHer. Here's what the search results reveal:

## ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL

ArCHer is an Actor-Critic Framework with a Hierarchical Structure that combines a high-level off-policy RL algorithm that trains a value function with a low-level RL algorithm that trains a token-by-token policy.

### Core Pro
…[truncated 1336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-17T12:22:12.585514+00:00_

Web search results for query: ""practitioner guide" multi-turn agentic reinforcement learning NeurIPS 2025"

Links: [{"title":"NeurIPS A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning","url":"https://neurips.cc/virtual/2025/127960"},{"title":"A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=yPWJG9wgll"},{"title":"[2510.01132] A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning","url":"https://arxiv.org/abs/2510.01132"},{"title":"(PDF) A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning","url":"https://www.researchgate.net/publication/396094509_A_Practitioner's_Guide_to_Multi-turn_Agentic_Reinforcement_Learning"},{"title":"NeurIPS 2025 Workshop on Multi-Turn Interactions in Large Language Models","url":"https://workshop-multi-turn-interaction.github.io/"},{"title":"A Practitioner’s Guide to Multi-turn Agentic Reinforcement Learning","url":"https://arxiv.org/html/2510.01132v2"},{"title":"A Practitioner’s Guide to Multi-turn Agentic Reinforcement Learning","url":"https://openreview.net/pdf?id=yPWJG9wgll"},{"title":"Paper page - A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning","url":"https://huggingface.co/papers/2510.01132"},{"title":"A Practitioner's Guide to Multi-turn Agentic Reinforcement ...","url":"https://www.facebook.com/groups/DeepNetGroup/posts/2613713835688149/"},{"title":"A Practitioner's Guide to Multi-turn Agentic Reinforcement ...","url":"https://arxiv.org/pdf/2510.01132"}]

I found comprehensive information about this paper. Here are the key details:

## "A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning"

This paper studies how to train large language models (LLMs) as autonomous agents that act over multiple turns in agentic environments. While reinforcement learning has driven strong single-turn reasoning, extending to multi-turn environments introduces new challenges yet to be addressed.

###
…[truncated 1066 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-17T12:22:12.585723+00:00_

Web search results for query: "DeepSeek-R1 GRPO reinforcement learning reasoning credit assignment token-level"

Links: [{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning | Nature","url":"https://www.nature.com/articles/s41586-025-09422-z"},{"title":"[2501.12948] DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/abs/2501.12948"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via","url":"https://arxiv.org/pdf/2501.12948"},{"title":"GRPO Reinforcement Learning Explained (DeepSeekMath Paper) - AI Papers Academy","url":"https://aipapersacademy.com/deepseekmath-grpo/"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2501.12948v1"},{"title":"Beyond Supervised Fine Tuning: How Reinforcement Learning Empowers AI with Minimal Labels","url":"https://fireworks.ai/blog/reinforcement-learning-with-verifiable-reward"},{"title":"Aman's AI Journal • Primers • DeepSeek-R1","url":"https://aman.ai/primers/ai/deepseek-R1/"},{"title":"Inside DeepSeek-R1: A Masterclass in Incentivising Intelligence","url":"https://blog.neosage.io/p/inside-deepseek-r1-a-masterclass"},{"title":"GitHub - FareedKhan-dev/train-deepseek-r1: Building DeepSeek R1 from Scratch · GitHub","url":"https://github.com/FareedKhan-dev/train-deepseek-r1"},{"title":"Understanding the DeepSeek R1 Paper - Hugging Face LLM Course","url":"https://huggingface.co/learn/llm-course/en/chapter12/3"}]

I've completed the web search on DeepSeek-R1 GRPO reinforcement learning reasoning credit assignment token-level. Here are the key findings:

## Core Framework

DeepSeek-R1 uses Group Relative Policy Optimization (GRPO) as its RL framework, building on DeepSeek-V3 Base.

## Token-Level Credit Assignment

Regarding token-level credit assignment specifically, even though there is no ground truth label for each token, and only a reward for the entire re
…[truncated 1177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-17T12:22:12.585910+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.19446",
  "prompt": "Extract: title, authors, year, venue, abstract, core method of ArCHer (hierarchical multi-turn RL with utterance-level value function and token-level policy), how it handles credit assignment between turns and within turns, key experimental results and sample efficiency gains."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2402.19446",
    "prompt": "Extract: title, authors, year, venue, abstract, core method of ArCHer (hierarchical multi-turn RL with utterance-level value function and token-level policy), how it handles credit assignment between turns and within turns, key experimental results and sample efficiency gains."
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-17T12:22:12.586042+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.01132",
  "prompt": "Extract: title, authors, year, venue, abstract, key findings about multi-turn agentic RL formulation, comparison of sparse vs dense per-turn rewards, token-level credit assignment approach, key experimental results on TextWorld and ALFWorld."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2510.01132",
    "prompt": "Extract: title, authors, year, venue, abstract, key findings about multi-turn agentic RL formulation, comparison of sparse vs dense per-turn rewards, token-level credit assignment approach, key experimental results on TextWorld and ALFWorld."
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-17T12:22:12.586342+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.09459",
  "prompt": "Extract the full taxonomy of credit assignment methods from this survey. Specifically: (1) What are the main categories? (2) Which methods handle step-level vs turn-level vs token-level? (3) Any discussion of advantage sign issues or misattribution? (4) What are the key open problems identified? (5) List the most important papers covered in each category."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2604.09459",
    "prompt": "Extract the full taxonomy of credit assignment methods from this survey. Specifically: (1) What are the main categories? (2) Which methods handle step-level vs turn-level vs token-level? (3) Any discussion of advantage sign issues or misattribution? (4) What are the key open problems identified? (5) List the most important papers covered in each category."
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-17T12:22:12.586495+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"reward redistribution\" \"return decomposition\" multi-turn agent reinforcement learning LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"reward redistribution\" \"return decomposition\" multi-turn agent reinforcement learning LLM 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-17T12:22:12.586650+00:00_

# ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL

**Title:** ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL

**Authors:** Yifei Zhou, Andrea Zanette, Jiayi Pan, Sergey Levine, Aviral Kumar

**Year:** 2024 (submitted February 29, 2024)

**Venue:** arXiv (cs.LG - Machine Learning)

## Abstract
The paper addresses multi-turn reinforcement learning for LLM agents. The authors note that "current RL methods for LLMs largely focus on optimizing single-turn rewards," which limits agents' ability to seek information across turns or perform credit assignment.

## Core Method
ArCHer employs a hierarchical RL structure with two parallel algorithms:
- **High-level component:** An off-policy value-based RL algorithm aggregating rewards across utterances
- **Low-level component:** An RL algorithm training token policies within each turn, leveraging the high-level value function

This design enables the framework to "preserve the flexibility of existing single-turn RL methods" while handling multiple turns and delayed rewards.

## Credit Assignment Mechanism
The hierarchical approach addresses credit assignment bidirectionally: the utterance-level value function evaluates decisions across turns, while token-level policies use this value information to optimize within-turn generation.

## Key Results
- **Sample efficiency:** Approximately 100x improvement over existing methods
- **Scalability:** Performance improvements demonstrated up to 7 billion parameter models
- Enhanced efficiency and performance on agent tasks

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-17T12:22:12.586802+00:00_

# A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning

**Title:** A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning

**Authors:** Ruiyi Wang, Prithviraj Ammanabrolu

**Year:** 2025 (submitted October 1, 2025; revised December 6, 2025)

**Venue:** arXiv:2510.01132 (cs.LG)

## Abstract Summary

The paper investigates empirically validated approaches for training large language models as agents through multi-turn RL. The authors state they "address this gap by first breaking down the design space into three inter-related pillars -- environment, reward, and policy."

## Key Findings

**Multi-turn Agentic RL Formulation:**
The research organizes the design space into three components: environment characteristics (state/action space sizes, solution length), reward mechanisms, and policy gradient methods.

**Sparse vs. Dense Per-Turn Rewards:**
The study observes that "dense turn-level rewards accelerate training, performance and stability is highly dependent on the choice of RL algorithm." This indicates a nuanced relationship where reward density alone doesn't guarantee success.

**Experimental Domains:**
Testing occurred across TextWorld and ALFWorld (textual embodied reasoning tasks) and SWE-Gym (software engineering tasks). Findings suggest simple environments within domains can predict generalization to complex variants.

**Policy Comparisons:**
The research explores biased methods (PPO, GRPO) versus unbiased approaches (RLOO), alongside determining optimal SFT-to-RL training ratios within budget constraints.

**Code Availability:** https://github.com/pearls-lab/meow-tea-taro

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-17T12:22:12.586950+00:00_

# Credit Assignment Survey Analysis

Based on the arXiv abstract provided, I can offer limited insights, as the full paper content isn't available—only the metadata and abstract are shown.

## Available Information:

**Main Taxonomy Dimensions:**
The survey organizes methods along two axes:
- Assignment granularity: "token, segment, step, turn, multi-agent"
- Methodology: "Monte Carlo, temporal difference, model-based, game-theoretic, information-theoretic"

**Scope Coverage:**
The paper addresses two regimes:
- **Reasoning RL**: credit distribution across "tokens and steps within a single chain-of-thought generation (500--30K+ tokens)"
- **Agentic RL**: "multi-turn environment interaction" with "horizons of 100+ turns (100K--1M tokens)"

**Key Finding:**
The abstract notes that "reasoning CA is maturing around process reward models and critic-free group comparison, while agentic CA is driving genuinely new approaches -- hindsight counterfactual analysis, privileged asymmetric critics, and turn-level MDP reformulations."

## Limitations:

I cannot definitively address your questions about advantage sign issues, misattribution discussion, specific open problems, or the most important papers in each category without access to the full paper text. The abstract mentions surveying 47 methods but doesn't enumerate them individually.

To obtain this detailed taxonomy, you would need to access the full PDF or HTML version of the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-17T12:22:12.587151+00:00_

Web search results for query: ""reward redistribution" "return decomposition" multi-turn agent reinforcement learning LLM 2025 2026"

Links: [{"title":"sparse- reward multi-agent reinforcement learning","url":"https://arxiv.org/pdf/2509.21828"},{"title":"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design","url":"https://arxiv.org/html/2505.11821v2"},{"title":"[Literature Review] SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution","url":"https://www.themoonlight.io/en/review/spa-rl-reinforcing-llm-agents-via-stepwise-progress-attribution"},{"title":"Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces","url":"https://arxiv.org/html/2605.02801v1"},{"title":"Enhancing Multi-Agent Learning in Real-World Interactive Environments through Process Reward Decomposition | OpenReview","url":"https://openreview.net/forum?id=E2CR6hmV1I"},{"title":"Training Task Reasoning LLM Agents for Multi-turn Task Planning via Single-turn Reinforcement Learning","url":"https://arxiv.org/html/2509.20616"},{"title":"Best Practices for Multi-Turn RL","url":"https://fireworks.ai/blog/best-practices-for-multi-turn-RL"},{"title":"LLM Collaboration with Multi-Agent Reinforcement Learning","url":"https://arxiv.org/pdf/2508.04652"},{"title":"[2505.11821] Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design","url":"https://arxiv.org/abs/2505.11821"},{"title":"Resolving Action Bottleneck: Agentic Reinforcement Learning Informed by Token-Level Energy","url":"https://arxiv.org/html/2605.14558"}]

I found relevant research on this topic. Here's what the web search revealed:

## Key Research Findings (2025-2026)

### Recent Work on Multi-Turn RL and Reward Decomposition

Recent research investigates RL approaches for LLM agents in multi-turn scenarios, with studies noting that algorithms like GRPO and PPO rely on sparse outcome rewards and lack dense intermediate signals. To address this, researchers have conduct
…[truncated 1603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-17T12:22:12.587545+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "memory.md",
  "content": "# Turn-Level PPO / Per-Step Credit Assignment Literature Review\n\n> 调研日期：2026-05-17  \n> 调研范围：2024–2026 年发表的 multi-turn agent RL credit assignment 相关论文\n\n---\n\n## 一、Direct Competitors：Turn-Level Credit Assignment Methods\n\n### 1.1 Turn-PPO (Li et al., 2025)\n\n- **论文**: Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs\n- **作者**: Junbo Li, Peng Zhou, Rui Meng, Meet P. Vadera, Lihong Li, Yang Li\n- **年份/会议**: 2025, EACL 2026\n- **arXiv**: 2512.17008\n\n**核心方法**:\n- 将 MDP 从 token-level 重新定义为 turn-level：state = 到第 h-1 轮的完整交互历史 + 当前 query，action = LLM 在第 h 轮的完整 response\n- Turn-level advantage 计算：γV_{n+1} − V_n（中间 turn），r − V_N（最终 turn）\n- 整个 response 作为一个 action，advantage 应用于完整 response\n\n**对 GRPO 的批判**（与我们的发现高度相关）:\n1. **Uniform advantage assignment**: GRPO 对所有 token 跨 turn 施加相同的 advantage，忽略不同 turn 对最终 reward 的不等贡献\n2. **High variance in advantage estimation**: \"state representation misalignment\" — response 内的 next state 只多一个 token，而跨 response 的 next state 包含整个环境输出块，导致 critic 退化为平均值\n3. **GRPO 在 multi-turn 中频繁崩溃**: Sokoban 两个配置均 crash，WebShop 启用 reasoning 也 crash\n\n**关键实验结果**:\n\n| 环境 | 模型 | GRPO | Token-PPO | Turn-PPO |\n|------|------|------|-----------|----------|\n| WebShop | Qwen2.5-3B | 0.72 | 0.73 | **0.75** |\n| WebShop | Qwen3-1.7B (no think) | 0.78 | 0.77 | **0.80** |\n| WebShop | Qwen3-1.7B (think) | Crash | 0.54 | **0.55** |\n| Sokoban | Qwen2.5-3B | Crash | 1.93 | **2.29** |\n| Sokoban | Qwen2.5-7B | Crash | 2.90 | **3.74** |\n\n**与本项目的关系**: **最直接的竞品**。他们发现的 GRPO 问题（uniform advantage、崩溃）与我们发现的 Advantage Sign Misattribution 高度相关。区别在于：我们更深入地分析了 sign misattribution 的机制（γ 折扣导致早期步骤只保留 ~29% 的终端 return），他们更侧重 turn-level MDP 的形式化方案。\n\n---\n\n### 1.2 MT-GRPO / MT-PPO (Wei et al., 2025)\n\n- **论文**: Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\n- **作者**: Quan Wei, Siliang Zeng, Chenliang Li, William Brown, Oana Frunza, Wei Deng, Anderson Schneider, Yuriy Nevmyvaka, Yang Katie Zhao, Alfredo Garcia, Mingyi Hong\n- **年份/会议**: 2025, ICML 2025\n- **arXiv**: 2505.11821\n\n**核心方法**:\n- 第一个系统性研究 turn-level reward design 的工作\n- 将 GRPO 和 PPO 扩展为 multi-turn 变体（MT-GRPO、MT-PPO）\n- 两种 turn-level reward 设计：(1) Verifiable reward（可验证中间结果）(2) LLM-as-judge reward（用 LLM 评价中间步骤质量）\n- 细粒度 credit assignment strategy\n\n**关键实验结果**:\n- 在 QA 数据集上 MT-PPO 一致性最优，尤其在 multi-hop 任务（HotpotQA）上提升显著\n- 100% format correctness，更高 answer correctness\n- 更快收敛，更高稳定性\n\n**与本项目的关系**: **直接竞品**。与我们的方向完全吻合——同样发现 episode-level sparse reward 不足以训练 multi-turn agent，需要 turn-level 信号。差异在于他们依赖外部 reward 信号（verifiable/LLM-judge），而我们关注的是在纯 outcome reward 下的 credit assignment 机制。\n\n---\n\n### 1.3 GiGPO (Feng et al., 2025)\n\n- **论文**: Group-in-Group Policy Optimization for LLM Agent Training\n- **作者**: Lang Feng, Zhenghai Xue, Tingcong Liu, Bo An\n- **年份/会议**: 2025, NeurIPS 2025\n- **arXiv**: 2505.10978\n\n**核心方法**:\n- 两层结构的 advantage estimation：\n  - **Episode-level (macro)**: 对完整 trajectory 的 group 计算 relative advantage\n  - **Step-level (micro)**: Anchor State Grouping — 在不同 trajectory 中找到重复出现的环境状态，回溯性地构建 step-level group，从而在相同状态下比较不同 action 的优劣\n- 保持 group-based RL 的优点：critic-free、低显存、稳定收敛\n\n**关键实验结果**:\n- ALFWorld: >12% improvement over GRPO\n- WebShop: >9% improvement over GRPO\n- QA: 42.1% (3B), 47.2% (7B)\n- 计算开销与 GRPO 几乎相同\n\n**与本项目的关系**: **方法组件参考**。Anchor State Grouping 是一个巧妙的思路——通过在不同 trajectory 中找到相同环境状态来实现 step-level 比较。但这种方法依赖于环境状态的可重复性，在 cost verification agent 这种任务中状态空间更大更稀疏，直接复用可能受限。但其 \"两层 advantage\" 的思想与我们的分析方向兼容。\n\n---\n\n### 1.4 GAGPO (Zhu et al., 2026)\n\n- **论文**: GAGPO: Generalized Advantage Grouped Policy Optimization\n- **作者**: Siyuan Zhu, Chao Yu, Rongxin Yang, Zongkai Liu, Jinjun Hu, Qiwen Chen, Yibo Zhang\n- **年份**: 2026\n- **arXiv**: 2605.13217\n\n**核心方法**:\n- **Grouped Value Proxy**: 非参数化的 value 估计，通过对同一环境 group 中步骤的 discounted return 取平均来构建 baseline\n- **Temporal Credit Propagation**: 递归 advantage 估计 A^t = δt + γλA^(t+1)，TD 残差向后传播延迟结果\n- **Group-Normalized PPO**: 在 rollout group 内归一化（而非 batch 内），使用 sequence-level importance ratio\n\n**关键实验结果**:\n- ALFWorld: Qwen2.5-1.5B 93.5% (vs. 88.1% prior best), Qwen2.5-7B 95.6% (vs. 88.8%)\n- WebShop: 1.5B 88.6 score / 78.1% SR, 7B 90.3 / 77.5%\n- 比 GiGPO 更低的 advantage signal variance，更快的早期学习\n\n**与本项目的关系**: **方法组件参考**。GAGPO 的 Grouped Value Proxy 本质上是一种无 critic 的 GAE 近似——用同一环境状态的多条 trajectory 来估计 value，再做 TD-style 的 advantage 传播。这与我们在纯 outcome reward 下寻找 credit assignment 方案的方向契合。\n\n---\n\n### 1.5 HCAPO (Tan et al., 2026)\n\n- **论文**: Hindsight Credit Assignment for Long-Horizon LLM Agents\n- **作者**: Hui-Ze Tan, Xiao-Wen Yang, Hao Chen, Jie-Jing Shao, Yi Wen, Yuteng Shen, Weihong Luo, Xiku Du, Lan-Zhe Guo, Yu-Feng Li\n- **年份**: 2026\n- **arXiv**: 2603.08754\n\n**核心方法**:\n- **Post-hoc Critic Refinement**: 用 LLM 自身作为 post-hoc critic，通过 hindsight reasoning 来 refine step-level Q-value\n- **Multi-scale Advantage Mechanism**: 在关键决策点修正 value baseline 不准确性，将 trajectory-level reward 转化为 step-level 信号\n- Value-free RL：不需要单独训练 critic\n\n**关键实验结果**:\n- WebShop: +7.7% over GRPO (Qwen2.5-7B-Instruct)\n- ALFWorld: +13.8% over GRPO\n- 更高 exploration efficiency，更简洁的决策\n\n**与本项目的关系**: **方法组件参考**。Hindsight credit assignment 的思路很有启发性——在看到完整 trajectory 后回溯性地评估每步的质量。但依赖 LLM 自身做 Q-value 估计的可靠性存疑。\n\n---\n\n### 1.6 iStar (Liu et al., 2025)\n\n- **论文**: Agentic Reinforcement Learning with Implicit Step Rewards\n- **作者**: Xiaoqian Liu, Ke Wang, Yuchuan Wu, Fei Huang, Yongbin Li, Junge Zhang, Jianbin Jiao\n- **年份**: 2025\n- **arXiv**: 2509.19199\n\n**核心方法**:\n- 交替优化 implicit Process Reward Model (PRM) 和 policy model\n- 通过 trajectory-based DPO objective 生成 implicit step reward\n- **Dual Advantage Integration**: 组合 step-level 和 episode-level advantage 进行 policy update\n- 不需要额外 rollout 或显式 step label\n\n**关键实验结果**:\n- WebShop, VisualSokoban, SOTOPIA 上超越 frontier LLM 和强 RL baseline\n- 更好的 sample efficiency 和稳定性\n\n**与本项目的关系**: **方法组件参考**。Dual advantage（step + episode）的组合是一个有趣的设计选择。Implicit PRM 的训练方式避免了人工标注 step reward 的成本。\n\n---\n\n### 1.7 SPA-RL (Wang et al., 2025)\n\n- **论文**: SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution\n- **作者**: Hanlin Wang, Chak Tou Leong, Jiashuo Wang, Jian Wang, Wenjie Li\n- **年份**: 2025\n- **arXiv**: 2505.20732\n\n**核心方法**:\n- **Reward redistribution framework**: 将最终任务 reward 分解为各步的贡献\n- **Progress Estimator**: 训练一个进度估计器，使各步贡献的累积和匹配任务完成度\n- 估计的 per-step 贡献 + action grounding 信号 = 细粒度中间 reward\n\n**关键实验结果**:\n- WebShop, ALFWorld, VirtualHome 上平均 +2.5% success rate, +1.9% grounding accuracy\n\n**与本项目的关系**: **方法组件参考**。Progress estimator 的思路类似 potential-based reward shaping。在 cost verification 任务中，可以尝试类似思路估计每步对最终验证成功的\"贡献度\"。\n\n---\n\n## 二、Foundational Frameworks\n\n### 2.1 ArCHer (Zhou et al., 2024)\n\n- **论文**: ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL\n- **作者**: Yifei Zhou, Andrea Zanette, Jiayi Pan, Sergey Levine, Aviral Kumar\n- **年份/会议**: 2024, ICML 2024\n- **arXiv**: 2402.19446\n\n**核心方法**:\n- 开创性的 hierarchical multi-turn RL 框架\n- **High-level**: off-policy TD 学习 utterance-level value function（跨 turn 聚合 reward）\n- **Low-level**: policy gradient 在每个 turn 内优化 token 生成，使用 high-level value function 作为 terminal reward\n- Off-policy 特性允许 sample reuse\n- 避免对每个 token 做 Bellman backup\n\n**关键实验结果**:\n- 比 on-policy 方法约 **100x sample efficiency improvement**\n- 在 7B 模型上验证可扩展性\n\n**与本项目的关系**: **理论基础**。ArCHer 是 turn-level RL for LLMs 的开山之作。其 hierarchical (utterance-level value + token-level policy) 的设计启发了后续所有 Turn-PPO 类工作。但它依赖 off-policy 学习和显式 value function，而我们使用的 GRPO 是 on-policy、critic-free 的。\n\n---\n\n### 2.2 RAGEN / StarPO (Wang et al., 2025)\n\n- **论文**: RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning\n- **作者**: Zihan Wang, Kangrui Wang, Qineng Wang, Pingyue Zhang, et al.\n- **年份**: 2025\n- **arXiv**: 2504.20073\n\n**核心方法**:\n- **StarPO** (State-Thinking-Actions-Reward Policy Optimization): 通用 trajectory-level agent RL 框架\n- 支持 multi-turn rollout, trajectory-level reward assignment, policy update\n- **StarPO-S**: 稳定化变体，加入 trajectory filtering, critic integration, gradient stabilization\n- **SNR-Adaptive Filtering (V2)**: 基于 reward variance 的 rollout 过滤，减少 noisy gradient\n\n**关键发现**:\n- **Echo Trap**: 训练后 agent 收敛到固定短语模板，RL 可能强化了 superficial pattern 而非 general reasoning\n- 没有细粒度的 reasoning-aware reward signal，agent 无法发展真正的推理能力\n- 10 个内置环境（Sokoban, FrozenLake, WebShop, DeepCoder, SearchQA 等）\n\n**与本项目的关系**: **方法组件 + 实验平台**。StarPO 是一个通用框架，其 trajectory-level 设计在精神上与我们的 episode-level GRPO 类似。Echo Trap 现象值得关注——可能与我们观察到的 step-independent 崩塌有关联。\n\n---\n\n### 2.3 VAGEN (Wang et al., 2025)\n\n- **论文**: VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents\n- **作者**: Kangrui Wang, Pingyue Zhang, Zihan Wang, et al.\n- **年份/会议**: 2025, NeurIPS 2025\n- **arXiv**: 2510.16907\n\n**核心方法**:\n- **Bi-Level GAE (Bi-Level Generalized Advantage Estimation)**:\n  - 第一层：turn-level advantage 评估每个 VLM response 的整体有效性\n  - 第二层：将 turn-level signal 传播到 token-level，为每个 token 提供细粒度 advantage\n- World Model 分解：State Estimation (\"当前状态是什么？\") + Transition Modeling (\"下一步会怎样？\")\n\n**关键实验结果**:\n- 3B 模型在 5 个 agent benchmark 上达到 0.82（3x improvement over untrained）\n- 超越 GPT-5 (0.75), Gemini 2.5 Pro (0.67), Claude 4.5 (0.62)\n\n**与本项目的关系**: **方法组件参考**。Bi-Level GAE 的 turn→token 传播机制是一个清晰的两层 credit assignment 设计。虽然 VAGEN 面向 VLM，但其 advantage 传播的数学形式可以直接迁移到 text-only agent RL。\n\n---\n\n### 2.4 HiPER (Peng et al., 2026)\n\n- **论文**: HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents\n- **作者**: Jiangweizhi Peng, Yuanxin Liu, Ruida Zhou, Charles Fleming, Zhaoran Wang, Alfredo Garcia, Mingyi Hong\n- **年份**: 2026\n- **arXiv**: 2602.16165\n\n**核心方法**:\n- **Hierarchical Plan-Execute**: 高层 planner 提出 subgoal，低层 executor 执行多步 action\n- **Hierarchical Advantage Estimation (HAE)**: 在 planning 和 execution 两层分别做 credit assignment\n  - 对每个 subgoal 聚合 return\n  - 在两层之间协调 update\n- 显式 temporal abstraction vs 传统 flat policy\n\n**关键实验结果**:\n- ALFWorld: 97.4% success (+6.6%)\n- WebShop: 83.3% success (+8.3%)\n- 在需要多个依赖子任务的长期任务上尤其强\n\n**与本项目的关系**: **理论参考**。Hierarchical 分解的思路有参考价值，但需要额外定义 subgoal 结构，在 cost verification 任务中 subgoal 的定义不太自然。\n\n---\n\n## 三、Agent RL Frameworks (Episode-Level Reward)\n\n### 3.1 WebRL (Qi et al., 2024)\n\n- **论文**: WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning\n- **作者**: Zehan Qi, Xiao Liu, et al.\n- **年份/会议**: 2024, ICLR 2025\n- **arXiv**: 2411.02337\n\n**核心方法**:\n- Self-evolving curriculum（从失败尝试生成新任务）\n- Outcome-Supervised Reward Model (ORM) 提供 reward signal\n- Adaptive RL 策略防止 policy distribution drift\n- 使用 episode-level reward，不做显式 step-level credit assignment\n\n**关键实验结果**:\n- Llama-3.1-8B: 4.8% → 42.4% on WebArena-Lite\n- GLM-4-9B: 6.1% → 43%\n- 超越 GPT-4-Turbo (17.6%), GPT-4o (13.9%)\n\n**与本项目的关系**: **Baseline 参考**。WebRL 表明在某些任务上 episode-level reward + curriculum 就能取得很好效果。但它没有 explicit credit assignment，在更长 horizon 或更稀疏 reward 的任务上可能受限。\n\n---\n\n### 3.2 WebAgent-R1 (Wei et al., 2025)\n\n- **论文**: WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning\n- **作者**: Zhepei Wei, Wenlin Yao, et al.\n- **年份/会议**: 2025, EMNLP 2025\n- **arXiv**: 2505.16421\n\n**核心方法**:\n- End-to-end multi-turn RL，binary success reward\n- Thinking-based prompting + behavior cloning warm-up\n- Credit assignment 隐式地通过 RL 优化过程实现\n\n**关键实验结果**:\n- Qwen-2.5-3B: 6.1% → 33.9%\n- Llama-3.1-8B: 8.5% → 44.8%\n- 显著超越 OpenAI o3\n\n**与本项目的关系**: **Baseline 参考**。证明 end-to-end binary reward 也能工作，但不清楚其 credit assignment 的隐式机制。\n\n---\n\n### 3.3 StepAgent (Deng et al., 2024)\n\n- **论文**: From Novice to Expert: LLM Agent Policy Optimization via Step-wise Reinforcement Learning\n- **作者**: Zhirui Deng, Zhicheng Dou, Yutao Zhu, et al.\n- **年份**: 2024\n- **arXiv**: 2411.03817\n\n**核心方法**:\n- 通过自动比较 expert 和 agent 在每步的 action 来生成中间 reward\n- Implicit-reward + 自我反思\n- Inverse RL 辅助 policy adjustment\n- 理论证明 agent action 分布可收敛到 expert\n\n**与本项目的关系**: **方法参考**。依赖 expert demonstration 的方式在纯 RL 设定下不适用，但 IRL 思路可参考。\n\n---\n\n### 3.4 Planner-R1 (Zhu et al., 2025)\n\n- **论文**: Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs\n- **作者**: Siyu Zhu, Yanbin Jiang, et al.\n- **年份**: 2025\n- **arXiv**: 2509.25779\n\n**核心方法**:\n- Dense process-level reward shaping\n- 研究 reward density 对不同大小模型的影响\n- Smaller (8B) models 对 reward shaping 高度敏感，dense reward 下可与 32B 竞争\n\n**关键实验结果**:\n- TravelPlanner: 56.9% final-pass (2.7x over GPT-5's 21.2%)\n- 8B 模型在 dense reward 下 3.5x compute-efficient vs 32B\n- Curriculum learning 无显著收益，shaped reward 一致性提升\n\n**与本项目的关系**: **实验参考**。验证了 dense reward 对小模型训练的重要性。在 cost verification 场景下，如何设计 dense intermediate reward 是核心问题。\n\n---\n\n## 四、Surveys & Guides\n\n### 4.1 From Reasoning to Agentic: Credit Assignment in RL for LLMs (Zhang, 2026)\n\n- **论文**: From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models\n- **作者**: Chenchen Zhang\n- **年份**: 2026\n- **arXiv**: 2604.09459\n\n**核心内容**:\n- 覆盖 **47 种 credit assignment 方法**（41 core + 6 adjacent enablers），2024–2026\n- **两维分类法**:\n  - 粒度维度: token / segment / step / turn / multi-agent\n  - 方法维度: Monte Carlo / temporal difference / model-based / game-theoretic / information-theoretic\n- **两种 regime**:\n  - Reasoning RL: 单次 CoT（500–30K+ tokens），credit 在 tokens/steps 间分配\n  - Agentic RL: multi-turn 交互（100K–1M tokens），有 stochastic transition 和 partial observability\n- **关键判断**: Reasoning CA 围绕 PRM 和 critic-free group comparison 成熟，Agentic CA 正在推动新方法——hindsight counterfactual analysis, privileged asymmetric critics, turn-level MDP reformulations\n\n**与本项目的关系**: **理论框架**。这篇 survey 的分类法可以帮助定位我们的工作——我们的 \"Advantage Sign Misattribution\" 发现属于 turn-level + Monte Carlo 的交叉区域。\n\n---\n\n### 4.2 A Practitioner's Guide to Multi-turn Agentic RL (Wang & Ammanabrolu, 2025)\n\n- **论文**: A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning\n- **作者**: Ruiyi Wang, Prithviraj Ammanabrolu\n- **年份/会议**: 2025, NeurIPS 2025 Workshop\n- **arXiv**: 2510.01132\n\n**核心内容**:\n- 三大支柱: Environment, Reward, Policy\n- **Dense vs Sparse per-turn reward**: dense turn-level reward 加速训练，但效果高度依赖 RL 算法选择\n- PPO vs GRPO vs RLOO 对比\n- Simple 环境可预测在 complex 变体上的泛化性\n\n**与本项目的关系**: **实验设计参考**。其关于 sparse vs dense reward 的系统比较提供了实验设计的参考框架。\n\n---\n\n### 4.3 DeepSeek-R1 (DeepSeek, 2025)\n\n- **论文**: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\n- **arXiv**: 2501.12948\n\n**GRPO 在 single-turn 推理中的应用**:\n- Episode-level advantage: 对同一 prompt 的 group 采样 → 组内归一化\n- 所有 advantage estimation 在 sequence level（整个 completion）进行\n- 移除 Value Model 后不再需要 token-level reward\n- Policy ratio 仍在 token-level 计算（用于 gradient update）\n\n**与本项目的关系**: **方法基础**。DeepSeek-R1 确立了 GRPO 的 single-turn 范式，但其 sequence-level advantage 直接应用到 multi-turn 场景时会产生我们发现的 Advantage Sign Misattribution 问题——因为多步交互中，不同步骤的 action 质量可能完全不同，统一的 sequence-level advantage 无法区分。\n\n---\n\n## 五、与本项目的关系总结\n\n### 5.1 核心发现定位\n\n我们发现的 **Advantage Sign Misattribution** 问题——失败 episode 中好的 action 收到无差别的负向 advantage，成功 episode 中差的 action 收到正向 advantage——与以下工作有直接对应关系：\n\n| 论文 | 相关发现 |\n|------|----------|\n| Turn-PPO | \"uniform advantage assignment\" across turns，GRPO 在 multi-turn 中崩溃 |\n| GiGPO | GRPO \"collapses step-level distinctions\" |\n| HCAPO | GRPO 存在 \"inaccurate Q-value estimates and misaligned baselines for intermediate states\" |\n| GAGPO | sparse reward 下 \"impact of any individual action may only manifest much later\" |\n| iStar | \"sparse and sometimes unverifiable rewards make credit assignment extremely challenging\" |\n\n然而，**没有一篇论文明确使用 \"advantage sign misattribution\" 这个术语**，也没有论文量化分析 γ 折扣对 sign 的影响（如我们发现的 ~29% 保留率）。这是我们可以贡献的新 framing。\n\n### 5.2 分类\n\n**Direct Competitors（解决相同问题的方法）**:\n- Turn-PPO：turn-level MDP + turn-level advantage\n- MT-GRPO/MT-PPO：turn-level reward design（verifiable + LLM-judge）\n- GiGPO：anchor state grouping for step-level group comparison\n- GAGPO：grouped value proxy + temporal credit propagation\n- HCAPO：hindsight credit assignment with LLM-as-critic\n\n**Method Components（可借鉴的技术组件）**:\n- iStar: implicit PRM + dual advantage\n- SPA-RL: progress estimator for reward redistribution\n- VAGEN Bi-Level GAE: turn→token advantage propagation\n- ArCHer: utterance-level value function (off-policy)\n- HiPER: hierarchical advantage estimation\n\n**Theoretical Foundation（理论基础）**:\n- DeepSeek-R1 GRPO: 我们方法的出发点\n- Credit Assignment Survey (Zhang 2026): 分类法和开放问题\n- Practitioner's Guide: 实验设计参考\n\n**Baseline Comparison（效果对比参考）**:\n- WebRL: episode-level reward + curriculum\n- WebAgent-R1: binary reward + end-to-end RL\n- Planner-R1: reward shaping effect on model sizes\n\n### 5.3 我们的差异化贡献空间\n\n1. **Advantage Sign Misattribution 的正式定义和量化分析** — 现有工作描述了 \"uniform advantage\" 和 \"credit assignment challenge\"，但没有具体分析 sign 级别的错误及其量化影响\n2. **γ 折扣在 multi-step agent 中的 return 衰减分析** — 早期步骤只保留 ~29% 的终端 return，这个量化结果是新的\n3. **Step-independent vs Episode-level 的受控对比实验** — 直接证明 step-independent 优化的崩塌和 episode-level 的提升（0% vs 28%），这种 clean 的对比是稀缺的\n4. **在 cost verification 特定任务上的分析** — 现有工作集中在 WebShop, ALFWorld, Sokoban 等标准 benchmark，我们的任务场景是差异化的\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "file": "memory.md",
    "content": "# Turn-Level PPO / Per-Step Credit Assignment Literature Review\n\n> 调研日期：2026-05-17  \n> 调研范围：2024–2026 年发表的 multi-turn agent RL credit assignment 相关论文\n\n---\n\n## 一、Direct Competitors：Turn-Level Credit Assignment Methods\n\n### 1.1 Turn-PPO (Li et al., 2025)\n\n- **论文**: Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs\n- **作者**: Junbo Li, Peng Zhou, Rui Meng, Meet P. Vadera, Lihong Li, Yang Li\n- **年份/会议**: 2025, EACL 2026\n- **arXiv**: 2512.17008\n\n**核心方法**:\n- 将 MDP 从 token-level 重新定义为 turn-level：state = 到第 h-1 轮的完整交互历史 + 当前 query，action = LLM 在第 h 轮的完整 response\n- Turn-level advantage 计算：γV_{n+1} − V_n（中间 turn），r − V_N（最终 turn）\n- 整个 response 作为一个 action，advantage 应用于完整 response\n\n**对 GRPO 的批判**（与我们的发现高度相关）:\n1. **Uniform advantage assignment**: GRPO 对所有 token 跨 turn 施加相同的 advantage，忽略不同 turn 对最终 reward 的不等贡献\n2. **High variance in advantage estimation**: \"state representation misalignment\" — response 内的 next state 只多一个 token，而跨 response 的 next state 包含整个环境输出块，导致 critic 退化为平均值\n3. **GRPO 在 multi-turn 中频繁崩溃**: Sokoban 两个配置均 crash，WebShop 启用 reasoning 也 crash\n\n**关键实验结果**:\n\n| 环境 | 模型 | GRPO | Token-PPO | Turn-PPO |\n|------|------|------|-----------|----------|\n| WebShop | Qwen2.5-3B | 0.72 | 0.73 | **0.75** |\n| WebShop | Qwen3-1.7B (no think) | 0.78 | 0.77 | **0.80** |\n| WebShop | Qwen3-1.7B (think) | Crash | 0.54 | **0.55** |\n| Sokoban | Qwen2.5-3B | Crash | 1.93 | **2.29** |\n| Sokoban | Qwen2.5-7B | Crash | 2.90 | **3.74** |\n\n**与本项目的关系**: **最直接的竞品**。他们发现的 GRPO 问题（uniform advantage、崩溃）与我们发现的 Advantage Sign Misattribution 高度相关。区别在于：我们更深入地分析了 sign misattribution 的机制（γ 折扣导致早期步骤只保留 ~29% 的终端 return），他们更侧重 turn-level MDP 的形式化方案。\n\n---\n\n### 1.2 MT-GRPO / MT-PPO (Wei et al., 2025)\n\n- **论文**: Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\n- **作者**: Quan Wei, Siliang Zeng, Chenliang Li, William Brown, Oana Frunza, Wei Deng, Anderson Schneider, Yuriy Nevmyvaka, Yang Katie Zhao, Alfredo Garcia, Mingyi Hong\n- **年份/会议**: 2025, ICML 2025\n- **arXiv**: 2505.11821\n\n**核心方法**:\n- 第一个系统性研究 turn-level reward design 的工作\n- 将 GRPO 和 PPO 扩展为 multi-turn 变体（MT-GRPO、MT-PPO）\n- 两种 turn-level reward 设计：(1) Verifiable reward（可验证中间结果）(2) LLM-as-judge reward（用 LLM 评价中间步骤质量）\n- 细粒度 credit assignment strategy\n\n**关键实验结果**:\n- 在 QA 数据集上 MT-PPO 一致性最优，尤其在 multi-hop 任务（HotpotQA）上提升显著\n- 100% format correctness，更高 answer correctness\n- 更快收敛，更高稳定性\n\n**与本项目的关系**: **直接竞品**。与我们的方向完全吻合——同样发现 episode-level sparse reward 不足以训练 multi-turn agent，需要 turn-level 信号。差异在于他们依赖外部 reward 信号（verifiable/LLM-judge），而我们关注的是在纯 outcome reward 下的 credit assignment 机制。\n\n---\n\n### 1.3 GiGPO (Feng et al., 2025)\n\n- **论文**: Group-in-Group Policy Optimization for LLM Agent Training\n- **作者**: Lang Feng, Zhenghai Xue, Tingcong Liu, Bo An\n- **年份/会议**: 2025, NeurIPS 2025\n- **arXiv**: 2505.10978\n\n**核心方法**:\n- 两层结构的 advantage estimation：\n  - **Episode-level (macro)**: 对完整 trajectory 的 group 计算 relative advantage\n  - **Step-level (micro)**: Anchor State Grouping — 在不同 trajectory 中找到重复出现的环境状态，回溯性地构建 step-level group，从而在相同状态下比较不同 action 的优劣\n- 保持 group-based RL 的优点：critic-free、低显存、稳定收敛\n\n**关键实验结果**:\n- ALFWorld: >12% improvement over GRPO\n- WebShop: >9% improvement over GRPO\n- QA: 42.1% (3B), 47.2% (7B)\n- 计算开销与 GRPO 几乎相同\n\n**与本项目的关系**: **方法组件参考**。Anchor State Grouping 是一个巧妙的思路——通过在不同 trajectory 中找到相同环境状态来实现 step-level 比较。但这种方法依赖于环境状态的可重复性，在 cost verification agent 这种任务中状态空间更大更稀疏，直接复用可能受限。但其 \"两层 advantage\" 的思想与我们的分析方向兼容。\n\n---\n\n### 1.4 GAGPO (Zhu et al., 2026)\n\n- **论文**: GAGPO: Generalized Advantage Grouped Policy Optimization\n- **作者**: Siyuan Zhu, Chao Yu, Rongxin Yang, Zongkai Liu, Jinjun Hu, Qiwen Chen, Yibo Zhang\n- **年份**: 2026\n- **arXiv**: 2605.13217\n\n**核心方法**:\n- **Grouped Value Proxy**: 非参数化的 value 估计，通过对同一环境 group 中步骤的 discounted return 取平均来构建 baseline\n- **Temporal Credit Propagation**: 递归 advantage 估计 A^t = δt + γλA^(t+1)，TD 残差向后传播延迟结果\n- **Group-Normalized PPO**: 在 rollout group 内归一化（而非 batch 内），使用 sequence-level importance ratio\n\n**关键实验结果**:\n- ALFWorld: Qwen2.5-1.5B 93.5% (vs. 88.1% prior best), Qwen2.5-7B 95.6% (vs. 88.8%)\n- WebShop: 1.5B 88.6 score / 78.1% SR, 7B 90.3 / 77.5%\n- 比 GiGPO 更低的 advantage signal variance，更快的早期学习\n\n**与本项目的关系**: **方法组件参考**。GAGPO 的 Grouped Value Proxy 本质上是一种无 critic 的 GAE 近似——用同一环境状态的多条 trajectory 来估计 value，再做 TD-style 的 advantage 传播。这与我们在纯 outcome reward 下寻找 credit assignment 方案的方向契合。\n\n---\n\n### 1.5 HCAPO (Tan et al., 2026)\n\n- **论文**: Hindsight Credit Assignment for Long-Horizon LLM Agents\n- **作者**: Hui-Ze Tan, Xiao-Wen Yang, Hao Chen, Jie-Jing Shao, Yi Wen, Yuteng Shen, Weihong Luo, Xiku Du, Lan-Zhe Guo, Yu-Feng Li\n- **年份**: 2026\n- **arXiv**: 2603.08754\n\n**核心方法**:\n- **Post-hoc Critic Refinement**: 用 LLM 自身作为 post-hoc critic，通过 hindsight reasoning 来 refine step-level Q-value\n- **Multi-scale Advantage Mechanism**: 在关键决策点修正 value baseline 不准确性，将 trajectory-level reward 转化为 step-level 信号\n- Value-free RL：不需要单独训练 critic\n\n**关键实验结果**:\n- WebShop: +7.7% over GRPO (Qwen2.5-7B-Instruct)\n- ALFWorld: +13.8% over GRPO\n- 更高 exploration efficiency，更简洁的决策\n\n**与本项目的关系**: **方法组件参考**。Hindsight credit assignment 的思路很有启发性——在看到完整 trajectory 后回溯性地评估每步的质量。但依赖 LLM 自身做 Q-value 估计的可靠性存疑。\n\n---\n\n### 1.6 iStar (Liu et al., 2025)\n\n- **论文**: Agentic Reinforcement Learning with Implicit Step Rewards\n- **作者**: Xiaoqian Liu, Ke Wang, Yuchuan Wu, Fei Huang, Yongbin Li, Junge Zhang, Jianbin Jiao\n- **年份**: 2025\n- **arXiv**: 2509.19199\n\n**核心方法**:\n- 交替优化 implicit Process Reward Model (PRM) 和 policy model\n- 通过 trajectory-based DPO objective 生成 implicit step reward\n- **Dual Advantage Integration**: 组合 step-level 和 episode-level advantage 进行 policy update\n- 不需要额外 rollout 或显式 step label\n\n**关键实验结果**:\n- WebShop, VisualSokoban, SOTOPIA 上超越 frontier LLM 和强 RL baseline\n- 更好的 sample efficiency 和稳定性\n\n**与本项目的关系**: **方法组件参考**。Dual advantage（step + episode）的组合是一个有趣的设计选择。Implicit PRM 的训练方式避免了人工标注 step reward 的成本。\n\n---\n\n### 1.7 SPA-RL (Wang et al., 2025)\n\n- **论文**: SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution\n- **作者**: Hanlin Wang, Chak Tou Leong, Jiashuo Wang, Jian Wang, Wenjie Li\n- **年份**: 2025\n- **arXiv**: 2505.20732\n\n**核心方法**:\n- **Reward redistribution framework**: 将最终任务 reward 分解为各步的贡献\n- **Progress Estimator**: 训练一个进度估计器，使各步贡献的累积和匹配任务完成度\n- 估计的 per-step 贡献 + action grounding 信号 = 细粒度中间 reward\n\n**关键实验结果**:\n- WebShop, ALFWorld, VirtualHome 上平均 +2.5% success rate, +1.9% grounding accuracy\n\n**与本项目的关系**: **方法组件参考**。Progress estimator 的思路类似 potential-based reward shaping。在 cost verification 任务中，可以尝试类似思路估计每步对最终验证成功的\"贡献度\"。\n\n---\n\n## 二、Foundational Frameworks\n\n### 2.1 ArCHer (Zhou et al., 2024)\n\n- **论文**: ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL\n- **作者**: Yifei Zhou, Andrea Zanette, Jiayi Pan, Sergey Levine, Aviral Kumar\n- **年份/会议**: 2024, ICML 2024\n- **arXiv**: 2402.19446\n\n**核心方法**:\n- 开创性的 hierarchical multi-turn RL 框架\n- **High-level**: off-policy TD 学习 utterance-level value function（跨 turn 聚合 reward）\n- **Low-level**: policy gradient 在每个 turn 内优化 token 生成，使用 high-level value function 作为 terminal reward\n- Off-policy 特性允许 sample reuse\n- 避免对每个 token 做 Bellman backup\n\n**关键实验结果**:\n- 比 on-policy 方法约 **100x sample efficiency improvement**\n- 在 7B 模型上验证可扩展性\n\n**与本项目的关系**: **理论基础**。ArCHer 是 turn-level RL for LLMs 的开山之作。其 hierarchical (utterance-level value + token-level policy) 的设计启发了后续所有 Turn-PPO 类工作。但它依赖 off-policy 学习和显式 value function，而我们使用的 GRPO 是 on-policy、critic-free 的。\n\n---\n\n### 2.2 RAGEN / StarPO (Wang et al., 2025)\n\n- **论文**: RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning\n- **作者**: Zihan Wang, Kangrui Wang, Qineng Wang, Pingyue Zhang, et al.\n- **年份**: 2025\n- **arXiv**: 2504.20073\n\n**核心方法**:\n- **StarPO** (State-Thinking-Actions-Reward Policy Optimization): 通用 trajectory-level agent RL 框架\n- 支持 multi-turn rollout, trajectory-level reward assignment, policy update\n- **StarPO-S**: 稳定化变体，加入 trajectory filtering, critic integration, gradient stabilization\n- **SNR-Adaptive Filtering (V2)**: 基于 reward variance 的 rollout 过滤，减少 noisy gradient\n\n**关键发现**:\n- **Echo Trap**: 训练后 agent 收敛到固定短语模板，RL 可能强化了 superficial pattern 而非 general reasoning\n- 没有细粒度的 reasoning-aware reward signal，agent 无法发展真正的推理能力\n- 10 个内置环境（Sokoban, FrozenLake, WebShop, DeepCoder, SearchQA 等）\n\n**与本项目的关系**: **方法组件 + 实验平台**。StarPO 是一个通用框架，其 trajectory-level 设计在精神上与我们的 episode-level GRPO 类似。Echo Trap 现象值得关注——可能与我们观察到的 step-independent 崩塌有关联。\n\n---\n\n### 2.3 VAGEN (Wang et al., 2025)\n\n- **论文**: VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents\n- **作者**: Kangrui Wang, Pingyue Zhang, Zihan Wang, et al.\n- **年份/会议**: 2025, NeurIPS 2025\n- **arXiv**: 2510.16907\n\n**核心方法**:\n- **Bi-Level GAE (Bi-Level Generalized Advantage Estimation)**:\n  - 第一层：turn-level advantage 评估每个 VLM response 的整体有效性\n  - 第二层：将 turn-level signal 传播到 token-level，为每个 token 提供细粒度 advantage\n- World Model 分解：State Estimation (\"当前状态是什么？\") + Transition Modeling (\"下一步会怎样？\")\n\n**关键实验结果**:\n- 3B 模型在 5 个 agent benchmark 上达到 0.82（3x improvement over untrained）\n- 超越 GPT-5 (0.75), Gemini 2.5 Pro (0.67), Claude 4.5 (0.62)\n\n**与本项目的关系**: **方法组件参考**。Bi-Level GAE 的 turn→token 传播机制是一个清晰的两层 credit assignment 设计。虽然 VAGEN 面向 VLM，但其 advantage 传播的数学形式可以直接迁移到 text-only agent RL。\n\n---\n\n### 2.4 HiPER (Peng et al., 2026)\n\n- **论文**: HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents\n- **作者**: Jiangweizhi Peng, Yuanxin Liu, Ruida Zhou, Charles Fleming, Zhaoran Wang, Alfredo Garcia, Mingyi Hong\n- **年份**: 2026\n- **arXiv**: 2602.16165\n\n**核心方法**:\n- **Hierarchical Plan-Execute**: 高层 planner 提出 subgoal，低层 executor 执行多步 action\n- **Hierarchical Advantage Estimation (HAE)**: 在 planning 和 execution 两层分别做 credit assignment\n  - 对每个 subgoal 聚合 return\n  - 在两层之间协调 update\n- 显式 temporal abstraction vs 传统 flat policy\n\n**关键实验结果**:\n- ALFWorld: 97.4% success (+6.6%)\n- WebShop: 83.3% success (+8.3%)\n- 在需要多个依赖子任务的长期任务上尤其强\n\n**与本项目的关系**: **理论参考**。Hierarchical 分解的思路有参考价值，但需要额外定义 subgoal 结构，在 cost verification 任务中 subgoal 的定义不太自然。\n\n---\n\n## 三、Agent RL Frameworks (Episode-Level Reward)\n\n### 3.1 WebRL (Qi et al., 2024)\n\n- **论文**: WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning\n- **作者**: Zehan Qi, Xiao Liu, et al.\n- **年份/会议**: 2024, ICLR 2025\n- **arXiv**: 2411.02337\n\n**核心方法**:\n- Self-evolving curriculum（从失败尝试生成新任务）\n- Outcome-Supervised Reward Model (ORM) 提供 reward signal\n- Adaptive RL 策略防止 policy distribution drift\n- 使用 episode-level reward，不做显式 step-level credit assignment\n\n**关键实验结果**:\n- Llama-3.1-8B: 4.8% → 42.4% on WebArena-Lite\n- GLM-4-9B: 6.1% → 43%\n- 超越 GPT-4-Turbo (17.6%), GPT-4o (13.9%)\n\n**与本项目的关系**: **Baseline 参考**。WebRL 表明在某些任务上 episode-level reward + curriculum 就能取得很好效果。但它没有 explicit credit assignment，在更长 horizon 或更稀疏 reward 的任务上可能受限。\n\n---\n\n### 3.2 WebAgent-R1 (Wei et al., 2025)\n\n- **论文**: WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning\n- **作者**: Zhepei Wei, Wenlin Yao, et al.\n- **年份/会议**: 2025, EMNLP 2025\n- **arXiv**: 2505.16421\n\n**核心方法**:\n- End-to-end multi-turn RL，binary success reward\n- Thinking-based prompting + behavior cloning warm-up\n- Credit assignment 隐式地通过 RL 优化过程实现\n\n**关键实验结果**:\n- Qwen-2.5-3B: 6.1% → 33.9%\n- Llama-3.1-8B: 8.5% → 44.8%\n- 显著超越 OpenAI o3\n\n**与本项目的关系**: **Baseline 参考**。证明 end-to-end binary reward 也能工作，但不清楚其 credit assignment 的隐式机制。\n\n---\n\n### 3.3 StepAgent (Deng et al., 2024)\n\n- **论文**: From Novice to Expert: LLM Agent Policy Optimization via Step-wise Reinforcement Learning\n- **作者**: Zhirui Deng, Zhicheng Dou, Yutao Zhu, et al.\n- **年份**: 2024\n- **arXiv**: 2411.03817\n\n**核心方法**:\n- 通过自动比较 expert 和 agent 在每步的 action 来生成中间 reward\n- Implicit-reward + 自我反思\n- Inverse RL 辅助 policy adjustment\n- 理论证明 agent action 分布可收敛到 expert\n\n**与本项目的关系**: **方法参考**。依赖 expert demonstration 的方式在纯 RL 设定下不适用，但 IRL 思路可参考。\n\n---\n\n### 3.4 Planner-R1 (Zhu et al., 2025)\n\n- **论文**: Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs\n- **作者**: Siyu Zhu, Yanbin Jiang, et al.\n- **年份**: 2025\n- **arXiv**: 2509.25779\n\n**核心方法**:\n- Dense process-level reward shaping\n- 研究 reward density 对不同大小模型的影响\n- Smaller (8B) models 对 reward shaping 高度敏感，dense reward 下可与 32B 竞争\n\n**关键实验结果**:\n- TravelPlanner: 56.9% final-pass (2.7x over GPT-5's 21.2%)\n- 8B 模型在 dense reward 下 3.5x compute-efficient vs 32B\n- Curriculum learning 无显著收益，shaped reward 一致性提升\n\n**与本项目的关系**: **实验参考**。验证了 dense reward 对小模型训练的重要性。在 cost verification 场景下，如何设计 dense intermediate reward 是核心问题。\n\n---\n\n## 四、Surveys & Guides\n\n### 4.1 From Reasoning to Agentic: Credit Assignment in RL for LLMs (Zhang, 2026)\n\n- **论文**: From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models\n- **作者**: Chenchen Zhang\n- **年份**: 2026\n- **arXiv**: 2604.09459\n\n**核心内容**:\n- 覆盖 **47 种 credit assignment 方法**（41 core + 6 adjacent enablers），2024–2026\n- **两维分类法**:\n  - 粒度维度: token / segment / step / turn / multi-agent\n  - 方法维度: Monte Carlo / temporal difference / model-based / game-theoretic / information-theoretic\n- **两种 regime**:\n  - Reasoning RL: 单次 CoT（500–30K+ tokens），credit 在 tokens/steps 间分配\n  - Agentic RL: multi-turn 交互（100K–1M tokens），有 stochastic transition 和 partial observability\n- **关键判断**: Reasoning CA 围绕 PRM 和 critic-free group comparison 成熟，Agentic CA 正在推动新方法——hindsight counterfactual analysis, privileged asymmetric critics, turn-level MDP reformulations\n\n**与本项目的关系**: **理论框架**。这篇 survey 的分类法可以帮助定位我们的工作——我们的 \"Advantage Sign Misattribution\" 发现属于 turn-level + Monte Carlo 的交叉区域。\n\n---\n\n### 4.2 A Practitioner's Guide to Multi-turn Agentic RL (Wang & Ammanabrolu, 2025)\n\n- **论文**: A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning\n- **作者**: Ruiyi Wang, Prithviraj Ammanabrolu\n- **年份/会议**: 2025, NeurIPS 2025 Workshop\n- **arXiv**: 2510.01132\n\n**核心内容**:\n- 三大支柱: Environment, Reward, Policy\n- **Dense vs Sparse per-turn reward**: dense turn-level reward 加速训练，但效果高度依赖 RL 算法选择\n- PPO vs GRPO vs RLOO 对比\n- Simple 环境可预测在 complex 变体上的泛化性\n\n**与本项目的关系**: **实验设计参考**。其关于 sparse vs dense reward 的系统比较提供了实验设计的参考框架。\n\n---\n\n### 4.3 DeepSeek-R1 (DeepSeek, 2025)\n\n- **论文**: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\n- **arXiv**: 2501.12948\n\n**GRPO 在 single-turn 推理中的应用**:\n- Episode-level advantage: 对同一 prompt 的 group 采样 → 组内归一化\n- 所有 advantage estimation 在 sequence level（整个 completion）进行\n- 移除 Value Model 后不再需要 token-level reward\n- Policy ratio 仍在 token-level 计算（用于 gradient update）\n\n**与本项目的关系**: **方法基础**。DeepSeek-R1 确立了 GRPO 的 single-turn 范式，但其 sequence-level advantage 直接应用到 multi-turn 场景时会产生我们发现的 Advantage Sign Misattribution 问题——因为多步交互中，不同步骤的 action 质量可能完全不同，统一的 sequence-level advantage 无法区分。\n\n---\n\n## 五、与本项目的关系总结\n\n### 5.1 核心发现定位\n\n我们发现的 **Advantage Sign Misattribution** 问题——失败 episode 中好的 action 收到无差别的负向 advantage，成功 episode 中差的 action 收到正向 advantage——与以下工作有直接对应关系：\n\n| 论文 | 相关发现 |\n|------|----------|\n| Turn-PPO | \"uniform advantage assignment\" across turns，GRPO 在 multi-turn 中崩溃 |\n| GiGPO | GRPO \"collapses step-level distinctions\" |\n| HCAPO | GRPO 存在 \"inaccurate Q-value estimates and misaligned baselines for intermediate states\" |\n| GAGPO | sparse reward 下 \"impact of any individual action may only manifest much later\" |\n| iStar | \"sparse and sometimes unverifiable rewards make credit assignment extremely challenging\" |\n\n然而，**没有一篇论文明确使用 \"advantage sign misattribution\" 这个术语**，也没有论文量化分析 γ 折扣对 sign 的影响（如我们发现的 ~29% 保留率）。这是我们可以贡献的新 framing。\n\n### 5.2 分类\n\n**Direct Competitors（解决相同问题的方法）**:\n- Turn-PPO：turn-level MDP + turn-level advantage\n- MT-GRPO/MT-PPO：turn-level reward design（verifiable + LLM-judge）\n- GiGPO：anchor state grouping for step-level group comparison\n- GAGPO：grouped value proxy + temporal credit propagation\n- HCAPO：hindsight credit assignment with LLM-as-critic\n\n**Method Components（可借鉴的技术组件）**:\n- iStar: implicit PRM + dual advantage\n- SPA-RL: progress estimator for reward redistribution\n- VAGEN Bi-Level GAE: turn→token advantage propagation\n- ArCHer: utterance-level value function (off-policy)\n- HiPER: hierarchical advantage estimation\n\n**Theoretical Foundation（理论基础）**:\n- DeepSeek-R1 GRPO: 我们方法的出发点\n- Credit Assignment Survey (Zhang 2026): 分类法和开放问题\n- Practitioner's Guide: 实验设计参考\n\n**Baseline Comparison（效果对比参考）**:\n- WebRL: episode-level reward + curriculum\n- WebAgent-R1: binary reward + end-to-end RL\n- Planner-R1: reward shaping effect on model sizes\n\n### 5.3 我们的差异化贡献空间\n\n1. **Advantage Sign Misattribution 的正式定义和量化分析** — 现有工作描述了 \"uniform advantage\" 和 \"credit assignment challenge\"，但没有具体分析 sign 级别的错误及其量化影响\n2. **γ 折扣在 multi-step agent 中的 return 衰减分析** — 早期步骤只保留 ~29% 的终端 return，这个量化结果是新的\n3. **Step-independent vs Episode-level 的受控对比实验** — 直接证明 step-independent 优化的崩塌和 episode-level 的提升（0% vs 28%），这种 clean 的对比是稀缺的\n4. **在 cost verification 特定任务上的分析** — 现有工作集中在 WebShop, ALFWorld, Sokoban 等标准 benchmark，我们的任务场景是差异化的\n"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-17T12:22:12.588093+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-17T12:22:12.588364+00:00_

文献调研完成，已写入 `memory.md`。覆盖 18 篇论文（2024–2026），结构如下：

**Direct Competitors（5 篇）**:
- **Turn-PPO** (EACL 2026) — turn-level MDP，发现 GRPO 在 multi-turn 中 uniform advantage + 频繁 crash，最相关竞品
- **MT-GRPO/MT-PPO** (ICML 2025) — 第一个系统性 turn-level reward design 研究，verifiable + LLM-judge 两种 reward
- **GiGPO** (NeurIPS 2025) — anchor state grouping 实现 step-level group comparison，critic-free
- **GAGPO** (2026) — grouped value proxy + 递归 GAE，比 GiGPO variance 更低
- **HCAPO** (2026) — hindsight credit assignment，LLM 做 post-hoc critic

**Method Components（5 篇）**: iStar (implicit PRM + dual advantage), SPA-RL (progress estimator), VAGEN (bi-level GAE), ArCHer (ICML 2024, 开山之作), HiPER (hierarchical advantage)

**Frameworks/Baselines（4 篇）**: RAGEN/StarPO, WebRL, WebAgent-R1, Planner-R1

**Surveys（3 篇）**: Credit Assignment Survey (47 methods), Practitioner's Guide, DeepSeek-R1 GRPO

**关键结论**: 没有论文使用 "advantage sign misattribution" 术语，也没有量化 γ 折扣对 sign 的影响（~29% 保留率）。Turn-PPO 描述了相近现象（uniform advantage assignment），但我们的 sign-level 分析和 step-independent vs episode-level 的受控对比（0% vs 28%）是差异化贡献空间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_deep-read-turn-ppo-v2_20260517T121530"
}
```

</details>

---
