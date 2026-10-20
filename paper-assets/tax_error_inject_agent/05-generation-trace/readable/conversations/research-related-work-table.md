# research related work table

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_research_related-work-table_20260514T101016.jsonl`
- **Structured JSON:** [`2a3a53c9df94aaef1a8e.json`](../../sessions/2a/2a3a53c9df94aaef1a8e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-14T10:12:17.932430+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T10:12:17.932715+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T10:12:17.932893+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PALADIN tool error injection agent training recovery LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PALADIN tool error injection agent training recovery LLM 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T10:12:17.933051+00:00_

Web search results for query: "PALADIN tool error injection agent training recovery LLM 2024 2025"

Links: [{"title":"[2509.25238] PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases","url":"https://arxiv.org/abs/2509.25238"},{"title":"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases","url":"https://arxiv.org/html/2509.25238"},{"title":"[PDF] PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases | Semantic Scholar","url":"https://www.semanticscholar.org/paper/PALADIN:-Self-Correcting-Language-Model-Agents-to-Vuddanti-Shah/9ae73fb066a4d577bce84c42ec285a05f0b24c46"},{"title":"PALADIN: Self-Correcting Language Model Agents to Cure ...","url":"https://arxiv.org/pdf/2509.25238"},{"title":"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases","url":"https://openreview.net/attachment?id=NVTtoO297p&name=pdf"},{"title":"Prompt Injection Attacks in Large Language Models and AI Agent Systems: A Comprehensive Review of Vulnerabilities, Attack Vectors, and Defense Mechanisms","url":"https://www.mdpi.com/2078-2489/17/1/54"},{"title":"PALADIN: SELF-CORRECTING LANGUAGE MODEL","url":"https://openreview.net/pdf/d1e40c6dda824612ff79e2cdcc4b91ffe0ac75ad.pdf"},{"title":"(PDF) PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases","url":"https://www.researchgate.net/publication/396048240_PALADIN_Self-Correcting_Language_Model_Agents_to_Cure_Tool-Failure_Cases"},{"title":"From prompt injections to protocol exploits: Threats in LLM-powered AI agents workflows - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2405959525001997"},{"title":"Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via Model Context Protocol | OpenReview","url":"https://openreview.net/forum?id=UVgbFuXPaO"}]

Based on the web search results, here's what I found about PALADIN:

## PALADIN: Self-Correcting Language Model Agents

PALADIN is a generalizable framework for equipping
…[truncated 1467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T10:12:17.933196+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Agent-R MCTS self-reflection web agent training 2024 2025 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Agent-R MCTS self-reflection web agent training 2024 2025 paper"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T10:12:17.933316+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AgentRefine trajectory refinement LLM agent training paper 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AgentRefine trajectory refinement LLM agent training paper 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T10:12:17.933433+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Reflexion verbal reinforcement learning agent Shinn 2023 paper method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Reflexion verbal reinforcement learning agent Shinn 2023 paper method"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T10:12:17.933586+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Trial and Error\" exploration agent learning LLM paper 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Trial and Error\" exploration agent learning LLM paper 2023 2024"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T10:12:17.933772+00:00_

Web search results for query: "Reflexion verbal reinforcement learning agent Shinn 2023 paper method"

Links: [{"title":"[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366"},{"title":"NeurIPS Poster Reflexion: language agents with verbal reinforcement learning","url":"https://neurips.cc/virtual/2023/poster/70114"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub","url":"https://github.com/noahshinn/reflexion"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn","url":"https://arxiv.org/pdf/2303.11366"},{"title":"[PDF] Reflexion: language agents with verbal reinforcement learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Reflexion:-language-agents-with-verbal-learning-Shinn-Cassano/0671fd553dd670a4e820553a974bc48040ba0819"},{"title":"Reflexion: language agents with verbal reinforcement learning | OpenReview","url":"https://openreview.net/forum?id=vAElhFcKW6"},{"title":"(PDF) Reflexion: Language Agents with Verbal Reinforcement Learning (2023) | Noah Shinn | 443 Citations","url":"https://scispace.com/papers/reflexion-language-agents-with-verbal-reinforcement-learning-242t789l"},{"title":"Noah Shinn","url":"https://scholar.google.com/citations?user=zTfIpA4AAAAJ&hl=en"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/html/2303.11366"},{"title":"Reflexion: language agents with verbal reinforcement learning [Quick Review]","url":"https://liner.com/review/reflexion-language-agents-with-verbal-reinforcement-learning"}]

Based on the search results, here's an overview of the Reflexion paper by Shinn et al. (2023):

## Paper Overview

Reflexion is a novel framework to reinforce language agents through linguistic feedback, where agents verbally reflect on task feedback signals and then maintain their own reflective text in an episodic
…[truncated 1299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T10:12:17.933945+00:00_

Web search results for query: "AgentRefine trajectory refinement LLM agent training paper 2024 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025 AGENTREFINE:","url":"https://arxiv.org/pdf/2501.01702"},{"title":"[2501.01702] AgentRefine: Enhancing Agent Generalization through Refinement Tuning","url":"https://arxiv.org/abs/2501.01702"},{"title":"[2501.01702v2] AgentRefine: Enhancing Agent Generalization through Refinement Tuning","url":"https://arxiv.org/abs/2501.01702v2"},{"title":"AgentRefine: Enhancing Agent Generalization through Refinement Tuning | OpenReview","url":"https://openreview.net/forum?id=FDimWzmcWn"},{"title":"[2601.22758] AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement","url":"https://arxiv.org/abs/2601.22758"},{"title":"Watch Every Step! LLM Agent Learning via Iterative ...","url":"https://aclanthology.org/2024.emnlp-main.93.pdf"},{"title":"Improving the Efficiency of LLM Agent Systems through Trajectory Reduction","url":"https://arxiv.org/html/2509.23586v1"},{"title":"GitHub - luo-junyu/Awesome-Agent-Papers: [Up-to-date] Large Language Model Agent: A Survey on Methodology, Applications and Challenges · GitHub","url":"https://github.com/luo-junyu/awesome-agent-papers"},{"title":"Paper page - Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training","url":"https://huggingface.co/papers/2501.11425"},{"title":"GitHub - AGI-Edgerunners/LLM-Agents-Papers: A repo lists papers related to LLM based agent · GitHub","url":"https://github.com/AGI-Edgerunners/LLM-Agents-Papers"}]

I found information about the AgentRefine paper. Here are the key findings:

## AgentRefine Paper Overview

AgentRefine is a framework for agent-tuning published as a conference paper at ICLR 2025. 

### Core Concept

The core idea is to enable the model to learn to correct its mistakes via observation in the trajectory. The framework includes an agent synthesis approach that prompts a strong LLM to refin
…[truncated 1111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T10:12:17.934126+00:00_

Web search results for query: ""Trial and Error" exploration agent learning LLM paper 2023 2024"

Links: [{"title":"Trial and Error: Exploration-Based Trajectory Optimization of LLM Agents - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.409/"},{"title":"GitHub - Yifan-Song793/ETO: Trial and Error: Exploration-Based Trajectory Optimization of LLM Agents (ACL 2024 Main Conference) · GitHub","url":"https://github.com/Yifan-Song793/ETO"},{"title":"[2403.02502] Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents","url":"https://arxiv.org/abs/2403.02502"},{"title":"Trial and Error: Exploration-Based Trajectory Optimization of LLM Agents | OpenReview","url":"https://openreview.net/forum?id=jyG14i5vQ5"},{"title":"Trial and Error: Exploration-Based Trajectory Optimization of LLM Agents | Request PDF","url":"https://www.researchgate.net/publication/384216231_Trial_and_Error_Exploration-Based_Trajectory_Optimization_of_LLM_Agents"},{"title":"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2403.02502v2"},{"title":"Exploration-Based Trajectory Optimization for LLM Agents 3⃣","url":"https://aclanthology.org/2024.acl-long.409.pdf"},{"title":"[Quick Review] Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents","url":"https://liner.com/review/trial-and-error-explorationbased-trajectory-optimization-for-llm-agents"},{"title":"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/trial-error-exploration-based-trajectory-optimization-llm"},{"title":"Can We Rely on LLM Agents to Draft Long-Horizon Plans? Let’s Take TravelPlanner as an Example","url":"https://arxiv.org/html/2408.06318"}]

I found excellent results for your search! Here's what I discovered:

## "Trial and Error: Exploration-Based Trajectory Optimization of LLM Agents"

This paper was published b
…[truncated 1627 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T10:12:17.934302+00:00_

Web search results for query: "Agent-R MCTS self-reflection web agent training 2024 2025 paper"

Links: [{"title":"[2410.02052] ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning","url":"https://arxiv.org/abs/2410.02052"},{"title":"[2501.11425] Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training","url":"https://arxiv.org/abs/2501.11425"},{"title":"ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning | OpenReview","url":"https://openreview.net/forum?id=GBIUbwW9D8"},{"title":"Paper page - Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training","url":"https://huggingface.co/papers/2501.11425"},{"title":"Agent-R\\xspace: Training Language Model Agents to Reflect via Iterative Self-Training","url":"https://arxiv.org/html/2501.11425v1"},{"title":"ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/exact-teaching-ai-agents-to-explore-with-reflective-mcts-and-exploratory-learning/"},{"title":"ICLR Poster ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning","url":"https://iclr.cc/virtual/2025/poster/30295"},{"title":"Teaching AI Agents to Search with Reflective-MCTS and Exploratory Learning","url":"https://arxiv.org/html/2410.02052v2"},{"title":"(PDF) Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training","url":"https://www.researchgate.net/publication/388232063_Agent-R_Training_Language_Model_Agents_to_Reflect_via_Iterative_Self-Training"},{"title":"GitHub - ByteDance-Seed/Agent-R: Resources for our paper: \"Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training\" · GitHub","url":"https://github.com/ByteDance-Seed/Agent-R"}]

Based on the search results, I found two highly relevant papers from 2024-2025 that match your query:

## Agent-R: Training Language Model Agents to R
…[truncated 1740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T10:12:17.934496+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Agent-R ByteDance iterative self-training MCTS web agent WebArena environment details 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Agent-R ByteDance iterative self-training MCTS web agent WebArena environment details 2025"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T10:12:17.934630+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AgentRefine ICLR 2025 refinement tuning agent generalization training method SFT details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AgentRefine ICLR 2025 refinement tuning agent generalization training method SFT details"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T10:12:17.934748+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ReAct reasoning acting Yao 2022 agent baseline method details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ReAct reasoning acting Yao 2022 agent baseline method details"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T10:12:17.934901+00:00_

Web search results for query: "Agent-R ByteDance iterative self-training MCTS web agent WebArena environment details 2025"

Links: [{"title":"GitHub - ByteDance-Seed/Agent-R: Resources for our paper: \"Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training\" · GitHub","url":"https://github.com/ByteDance-Seed/Agent-R"},{"title":"Agent-R\\xspace: Training Language Model Agents to Reflect via Iterative Self-Training","url":"https://arxiv.org/html/2501.11425v1"},{"title":"Agent-R/README.md at main · ByteDance-Seed/Agent-R","url":"https://github.com/ByteDance-Seed/Agent-R/blob/main/README.md"},{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2505.16421v1"},{"title":"[2505.16421] WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/abs/2505.16421"},{"title":"Paper page - Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training","url":"https://huggingface.co/papers/2501.11425"},{"title":"ByteDance releases Agent R - by Dhruv Diddi - So Essentially","url":"https://soessentially.substack.com/p/bytedance-releases-agent-r"},{"title":"[2501.11425] Agent-R: Training Language Model Agents to Reflect via Iterative Self-Training","url":"https://arxiv.org/abs/2501.11425"},{"title":"WebSynthesis: World-Model-Guided MCTS for Efficient WebUI-Trajectory Synthesis","url":"https://arxiv.org/html/2507.04370v1"},{"title":"WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=oVKEAFjEqv"}]

Based on the search results, here's information about Agent-R and related web agent research:

## Agent-R Overview

Agent-R is an iterative self-training framework that enables language agents to reflect on the fly. By leveraging Monte Carlo Tree Search (MCTS), Agent-R dynamically constructs training samples that recover correct trajectories from
…[truncated 1370 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T10:12:17.935068+00:00_

Web search results for query: "AgentRefine ICLR 2025 refinement tuning agent generalization training method SFT details"

Links: [{"title":"Published as a conference paper at ICLR 2025 AGENTREFINE:","url":"https://arxiv.org/pdf/2501.01702"},{"title":"GitHub - Fu-Dayuan/AgentRefine: (ICLR 2025) AgentRefine: Enhancing Agent Generalization through Refinement Tuning","url":"https://github.com/Fu-Dayuan/AgentRefine"},{"title":"AgentRefine: Enhancing Agent Generalization through Refinement Tuning | OpenReview","url":"https://openreview.net/forum?id=FDimWzmcWn"},{"title":"[2501.01702] AgentRefine: Enhancing Agent Generalization through Refinement Tuning","url":"https://arxiv.org/abs/2501.01702"},{"title":"[2501.01702v2] AgentRefine: Enhancing Agent Generalization through Refinement Tuning","url":"https://arxiv.org/abs/2501.01702v2"},{"title":"AgentRefine: Enhancing Agent Generalization through Refinement Tuning","url":"https://agentrefine.github.io/"},{"title":"Paper page - AgentRefine: Enhancing Agent Generalization through Refinement Tuning","url":"https://huggingface.co/papers/2501.01702"},{"title":"Fu-Dayuan ( Fu Dayuan) · GitHub","url":"https://github.com/Fu-Dayuan"},{"title":"AgentRefine: Enhancing Agent Generalization through Refinement Tuning","url":"https://www.catalyzex.com/paper/agentrefine-enhancing-agent-generalization"},{"title":"AgentRefine: Enhancing Agent Generalization through Refinement Tuning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/agentrefine-enhancing-agent-generalization-through-refinement-tuning"}]

Based on the search results, here's comprehensive information about AgentRefine from ICLR 2025:

## Overview

AgentRefine was published as a conference paper at ICLR 2025, authored by researchers from Beijing University of Posts and Telecommunications and Meituan. The paper focuses on improving the agent generalization capabilities of LLMs via instruction tuning.

## Core Problem and Solution

The paper observes that exi
…[truncated 1857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T10:12:17.935235+00:00_

Web search results for query: "ReAct reasoning acting Yao 2022 agent baseline method details"

Links: [{"title":"[2210.03629] ReAct: Synergizing Reasoning and Acting in Language Models","url":"https://arxiv.org/abs/2210.03629"},{"title":"ReAct: Synergizing Reasoning and Acting in Language Models","url":"https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/"},{"title":"ReAct: Synergizing Reasoning and Acting in Language Models","url":"https://react-lm.github.io/"},{"title":"ReAct Prompting | Prompt Engineering Guide&lt;!-- -->","url":"https://www.promptingguide.ai/techniques/react"},{"title":"ReAct: Synergizing Reasoning and Acting in Language ...","url":"https://arxiv.org/pdf/2210.03629"},{"title":"ReAct: Combining Reasoning and Acting in Language Models for Smarter AI | by Lawrence Knight | Medium","url":"https://medium.com/@LawrencewleKnight/react-combining-reasoning-and-acting-in-language-models-for-smarter-ai-66d844c1b499"},{"title":"The ReAct Framework: Synergizing Reasoning and Acting","url":"https://apxml.com/courses/agentic-llm-memory-architectures/chapter-2-advanced-agent-architectures-reasoning/react-framework-reasoning-acting"},{"title":"Synergizing reasoning and acting in language models","url":"https://openreview.net/pdf?id=WE_vluYUL-X"},{"title":"ReAct: Synergising Reasoning and Acting in Language Models | cbarkinozer | Medium","url":"https://cbarkinozer.medium.com/react-synergising-reasoning-and-acting-in-language-models-79e09526ffbe"},{"title":"ReAct Prompting Guide: Reasoning Plus Acting for AI Agents (2026) | SurePrompts","url":"https://sureprompts.com/blog/react-prompting-guide"}]

Based on the search results, here are the key details about ReAct (Reasoning + Acting) from the Yao 2022 paper:

## Core Method

ReAct explores the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing reasoning traces to help the model induce, track, and update action plans as well as h
…[truncated 1599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T10:12:17.935405+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "mkdir -p /root/autodl-tmp/tax_error_inject_agent/docs",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "mkdir -p /root/autodl-tmp/tax_error_inject_agent/docs",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T10:12:17.935545+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T10:12:17.935686+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat << 'DOCEOF' > /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md\n# TaxEI vs. Related Methods: Differentiation & Positioning\n\n> **Date**: 2026-05-14\n> **Sources**: arXiv, ACL Anthology, OpenReview, NeurIPS proceedings\n> **Purpose**: Systematic comparison of TaxEI (Taxonomy-guided Error Injection) against representative agent robustness and training methods.\n\n---\n\n## 1. Comparison Table\n\n| Dimension | **TaxEI** (Ours) | **PALADIN** | **Agent-R** | **AgentRefine** | **ReAct** | **Reflexion** | **Trial-and-Error (ETO)** |\n|---|---|---|---|---|---|---|---|\n| **Error Types** | Planning errors (step-order swap, sub-goal deletion) + Context errors (context truncation, observation masking) | Tool errors (API timeout, exception, inconsistent output) | Execution errors (wrong actions in interactive environments) | Execution errors (wrong actions during trajectory generation) | None (no explicit error modeling) | Execution errors (task failure signals) | Execution errors (failed trajectory outcomes) |\n| **Injection Method** | Synthetic injection via taxonomy-defined operators (P1, P2, C1, C4) | Synthetic injection via tool failure simulation (ToolScan taxonomy) | Natural failure from model exploration + MCTS tree search | LLM-generated errors during synthetic trajectory creation | None | Natural failure from trial episodes | Natural failure from agent exploration |\n| **Recovery Signal** | Environment-grounded recovery: corrupted trajectory re-executed in environment, recovery generated from real environment feedback | Expert demonstration recovery + failure exemplar retrieval bank (55+ exemplars) | MCTS-guided trajectory splicing: erroneous path reconnected to correct branch at first divergence point | LLM self-refinement conditioned on environment observation feedback | N/A (no recovery mechanism) | Verbal self-reflection stored in episodic memory buffer | Contrastive failure-success trajectory pairs |\n| **Training Framework** | SFT (LoRA on Qwen3-8B); injection→corruption→recovery triplet data | SFT (LoRA); 50K+ recovery-annotated trajectories | Iterative self-training (SFT on MCTS-constructed revision trajectories) | SFT on synthesized refinement trajectories | Prompt-only (in-context learning, no training) | Prompt-only (verbal memory, no weight updates) | DPO / contrastive learning on trajectory preference pairs |\n| **Environment** | Embodied text (ALFWorld) | Tool-use (ToolBench) | Interactive text (WebShop, ScienceWorld, TextCraft) | Diverse synthesized environments (held-in + held-out generalization) | QA, fact verification, embodied (ALFWorld), web (WebShop) | QA (HotpotQA), coding (HumanEval), embodied (ALFWorld) | Interactive (WebShop, ScienceWorld, ALFWorld) |\n| **Requires Taxonomy** | Yes — error taxonomy defines injection operators and coverage | Yes — ToolScan taxonomy for failure categorization and exemplar retrieval | No | No | No | No | No |\n| **Error Detection** | Explicit — injection point is known; recovery conditioned on corrupted state | Explicit — execution-time error detection + exemplar matching | Implicit — MCTS value function identifies first divergence step in failed trajectory | Implicit — environment observation signals error | None | Implicit — binary task success/failure signal | Implicit — task outcome (success/failure) |\n\n---\n\n## 2. Method Summaries\n\n### PALADIN (arXiv 2509.25238)\n\nPALADIN addresses tool-level failures in LLM agents — API timeouts, exceptions, and inconsistent outputs — by training on 50K+ recovery-annotated trajectories constructed via systematic tool failure injection. At inference, it detects execution-time errors, retrieves the most similar failure exemplar from a curated bank aligned with the ToolScan taxonomy, and executes corresponding recovery actions. Key result: significant improvement in agent robustness on ToolBench tasks where standard agents fail catastrophically.\n\n### Agent-R (arXiv 2501.11425)\n\nAgent-R from ByteDance introduces an iterative self-training framework using MCTS to construct recovery training data. Unlike methods that train on full correct/incorrect trajectories, Agent-R identifies the exact first-error step in a failed trajectory and splices it with the correct branch from MCTS exploration, enabling fine-grained self-correction learning. Evaluated on WebShop, ScienceWorld, and TextCraft, it consistently outperforms SFT and reflection baselines by providing real-time recovery capability.\n\n### AgentRefine (ICLR 2025)\n\nAgentRefine tackles the generalization problem of agent-tuned LLMs — models that perform well on training environments but fail on held-out tasks. It synthesizes diverse agent environments and tasks via LLM, generates trajectories containing natural errors, and trains the model to refine errors conditioned on environment feedback. The refinement tuning approach leads to 13.3% improvement over Agent-FLAN on ScienceWorld and matches GPT-4o performance on some tasks, with notably better robustness under perturbation.\n\n### ReAct (ICLR 2023, Yao et al.)\n\nReAct interleaves reasoning traces and actions in a thought→action→observation loop, enabling LLM agents to decompose tasks, track progress, and handle exceptions through explicit chain-of-thought. As a prompting-only method with no training or error-specific mechanism, it serves as the standard baseline for interactive agent tasks. On ALFWorld and WebShop, it outperforms pure imitation and RL methods by 34% and 10% absolute success rate respectively with only 1-2 in-context examples.\n\n### Reflexion (NeurIPS 2023, Shinn et al.)\n\nReflexion replaces gradient-based learning with verbal self-reflection: after a failed episode, the agent generates a natural language reflection, stores it in an episodic memory buffer, and uses accumulated reflections to improve subsequent attempts. This requires no weight updates and works across diverse tasks (QA, coding, embodied). The limitation is that reflection quality depends entirely on the LLM's introspective ability, and there is no structured error categorization or targeted recovery training.\n\n### Trial-and-Error / ETO (ACL 2024, Song et al.)\n\nETO (Exploration-based Trajectory Optimization) lets agents learn from exploration failures through contrastive trajectory pairs. During exploration, the agent collects both successful and failed trajectories; during training, it uses DPO-style contrastive learning on failure-success trajectory preference pairs. On WebShop and ScienceWorld, ETO achieves 8% and 9.5% average reward increases over SFT behavioral cloning. The key insight is that failure trajectories carry valuable learning signals when properly contrasted with successes.\n\n---\n\n## 3. TaxEI Differentiation\n\n### Taxonomy-Guided Systematic Injection\n\nTaxEI's distinguishing feature is that error injection is neither random nor opportunistic — it is guided by a structured error taxonomy that categorizes agent failures into planning errors and context errors, each with specific injection operators (P1: step-order swap, P2: sub-goal deletion, C1: context truncation, C4: observation masking). This taxonomy-guided approach ensures (1) comprehensive coverage of error types relevant to embodied agents, (2) controllable difficulty via operator selection and injection density, and (3) reproducibility — every injected error has a clear categorical label. In contrast, PALADIN's taxonomy covers tool-level failures only, and other methods (Agent-R, ETO, Reflexion) rely on naturally occurring errors without systematic categorization.\n\n### Planning and Context Errors Beyond Tool Failures\n\nWhile PALADIN demonstrated the effectiveness of injection-based recovery training for tool errors, TaxEI extends this paradigm to higher-level failure modes: planning errors that disrupt the logical structure of action sequences, and context errors that corrupt the agent's situational awareness. These error types are particularly prevalent in embodied environments like ALFWorld where agents must maintain coherent multi-step plans and track environmental state over extended interactions. Tool errors, by contrast, are relatively surface-level — the agent knows *what* to do but the tool fails. Planning and context errors are more fundamental — the agent's reasoning itself is corrupted.\n\n### Environment-Grounded Recovery with Structured Training Signal\n\nTaxEI generates recovery training data through a three-stage pipeline: (1) inject taxonomy-defined errors into successful trajectories, (2) execute corrupted trajectories in the actual environment to observe realistic consequences, (3) generate recovery actions grounded in real environment feedback. This distinguishes TaxEI from methods that rely on LLM self-reflection (Reflexion, AgentRefine) or outcome-level contrastive signals (ETO). The recovery signal is neither hallucinated nor heuristic — it reflects how an agent should actually recover given the true environmental state after corruption. Combined with SFT training (without requiring RL infrastructure), this produces a practical and scalable training pipeline.\nDOCEOF\necho \"DONE: $(wc -l < /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md) lines\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat << 'DOCEOF' > /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md\n# TaxEI vs. Related Methods: Differentiation & Positioning\n\n> **Date**: 2026-05-14\n> **Sources**: arXiv, ACL Anthology, OpenReview, NeurIPS proceedings\n> **Purpose**: Systematic comparison of TaxEI (Taxonomy-guided Error Injection) against representative agent robustness and training methods.\n\n---\n\n## 1. Comparison Table\n\n| Dimension | **TaxEI** (Ours) | **PALADIN** | **Agent-R** | **AgentRefine** | **ReAct** | **Reflexion** | **Trial-and-Error (ETO)** |\n|---|---|---|---|---|---|---|---|\n| **Error Types** | Planning errors (step-order swap, sub-goal deletion) + Context errors (context truncation, observation masking) | Tool errors (API timeout, exception, inconsistent output) | Execution errors (wrong actions in interactive environments) | Execution errors (wrong actions during trajectory generation) | None (no explicit error modeling) | Execution errors (task failure signals) | Execution errors (failed trajectory outcomes) |\n| **Injection Method** | Synthetic injection via taxonomy-defined operators (P1, P2, C1, C4) | Synthetic injection via tool failure simulation (ToolScan taxonomy) | Natural failure from model exploration + MCTS tree search | LLM-generated errors during synthetic trajectory creation | None | Natural failure from trial episodes | Natural failure from agent exploration |\n| **Recovery Signal** | Environment-grounded recovery: corrupted trajectory re-executed in environment, recovery generated from real environment feedback | Expert demonstration recovery + failure exemplar retrieval bank (55+ exemplars) | MCTS-guided trajectory splicing: erroneous path reconnected to correct branch at first divergence point | LLM self-refinement conditioned on environment observation feedback | N/A (no recovery mechanism) | Verbal self-reflection stored in episodic memory buffer | Contrastive failure-success trajectory pairs |\n| **Training Framework** | SFT (LoRA on Qwen3-8B); injection→corruption→recovery triplet data | SFT (LoRA); 50K+ recovery-annotated trajectories | Iterative self-training (SFT on MCTS-constructed revision trajectories) | SFT on synthesized refinement trajectories | Prompt-only (in-context learning, no training) | Prompt-only (verbal memory, no weight updates) | DPO / contrastive learning on trajectory preference pairs |\n| **Environment** | Embodied text (ALFWorld) | Tool-use (ToolBench) | Interactive text (WebShop, ScienceWorld, TextCraft) | Diverse synthesized environments (held-in + held-out generalization) | QA, fact verification, embodied (ALFWorld), web (WebShop) | QA (HotpotQA), coding (HumanEval), embodied (ALFWorld) | Interactive (WebShop, ScienceWorld, ALFWorld) |\n| **Requires Taxonomy** | Yes — error taxonomy defines injection operators and coverage | Yes — ToolScan taxonomy for failure categorization and exemplar retrieval | No | No | No | No | No |\n| **Error Detection** | Explicit — injection point is known; recovery conditioned on corrupted state | Explicit — execution-time error detection + exemplar matching | Implicit — MCTS value function identifies first divergence step in failed trajectory | Implicit — environment observation signals error | None | Implicit — binary task success/failure signal | Implicit — task outcome (success/failure) |\n\n---\n\n## 2. Method Summaries\n\n### PALADIN (arXiv 2509.25238)\n\nPALADIN addresses tool-level failures in LLM agents — API timeouts, exceptions, and inconsistent outputs — by training on 50K+ recovery-annotated trajectories constructed via systematic tool failure injection. At inference, it detects execution-time errors, retrieves the most similar failure exemplar from a curated bank aligned with the ToolScan taxonomy, and executes corresponding recovery actions. Key result: significant improvement in agent robustness on ToolBench tasks where standard agents fail catastrophically.\n\n### Agent-R (arXiv 2501.11425)\n\nAgent-R from ByteDance introduces an iterative self-training framework using MCTS to construct recovery training data. Unlike methods that train on full correct/incorrect trajectories, Agent-R identifies the exact first-error step in a failed trajectory and splices it with the correct branch from MCTS exploration, enabling fine-grained self-correction learning. Evaluated on WebShop, ScienceWorld, and TextCraft, it consistently outperforms SFT and reflection baselines by providing real-time recovery capability.\n\n### AgentRefine (ICLR 2025)\n\nAgentRefine tackles the generalization problem of agent-tuned LLMs — models that perform well on training environments but fail on held-out tasks. It synthesizes diverse agent environments and tasks via LLM, generates trajectories containing natural errors, and trains the model to refine errors conditioned on environment feedback. The refinement tuning approach leads to 13.3% improvement over Agent-FLAN on ScienceWorld and matches GPT-4o performance on some tasks, with notably better robustness under perturbation.\n\n### ReAct (ICLR 2023, Yao et al.)\n\nReAct interleaves reasoning traces and actions in a thought→action→observation loop, enabling LLM agents to decompose tasks, track progress, and handle exceptions through explicit chain-of-thought. As a prompting-only method with no training or error-specific mechanism, it serves as the standard baseline for interactive agent tasks. On ALFWorld and WebShop, it outperforms pure imitation and RL methods by 34% and 10% absolute success rate respectively with only 1-2 in-context examples.\n\n### Reflexion (NeurIPS 2023, Shinn et al.)\n\nReflexion replaces gradient-based learning with verbal self-reflection: after a failed episode, the agent generates a natural language reflection, stores it in an episodic memory buffer, and uses accumulated reflections to improve subsequent attempts. This requires no weight updates and works across diverse tasks (QA, coding, embodied). The limitation is that reflection quality depends entirely on the LLM's introspective ability, and there is no structured error categorization or targeted recovery training.\n\n### Trial-and-Error / ETO (ACL 2024, Song et al.)\n\nETO (Exploration-based Trajectory Optimization) lets agents learn from exploration failures through contrastive trajectory pairs. During exploration, the agent collects both successful and failed trajectories; during training, it uses DPO-style contrastive learning on failure-success trajectory preference pairs. On WebShop and ScienceWorld, ETO achieves 8% and 9.5% average reward increases over SFT behavioral cloning. The key insight is that failure trajectories carry valuable learning signals when properly contrasted with successes.\n\n---\n\n## 3. TaxEI Differentiation\n\n### Taxonomy-Guided Systematic Injection\n\nTaxEI's distinguishing feature is that error injection is neither random nor opportunistic — it is guided by a structured error taxonomy that categorizes agent failures into planning errors and context errors, each with specific injection operators (P1: step-order swap, P2: sub-goal deletion, C1: context truncation, C4: observation masking). This taxonomy-guided approach ensures (1) comprehensive coverage of error types relevant to embodied agents, (2) controllable difficulty via operator selection and injection density, and (3) reproducibility — every injected error has a clear categorical label. In contrast, PALADIN's taxonomy covers tool-level failures only, and other methods (Agent-R, ETO, Reflexion) rely on naturally occurring errors without systematic categorization.\n\n### Planning and Context Errors Beyond Tool Failures\n\nWhile PALADIN demonstrated the effectiveness of injection-based recovery training for tool errors, TaxEI extends this paradigm to higher-level failure modes: planning errors that disrupt the logical structure of action sequences, and context errors that corrupt the agent's situational awareness. These error types are particularly prevalent in embodied environments like ALFWorld where agents must maintain coherent multi-step plans and track environmental state over extended interactions. Tool errors, by contrast, are relatively surface-level — the agent knows *what* to do but the tool fails. Planning and context errors are more fundamental — the agent's reasoning itself is corrupted.\n\n### Environment-Grounded Recovery with Structured Training Signal\n\nTaxEI generates recovery training data through a three-stage pipeline: (1) inject taxonomy-defined errors into successful trajectories, (2) execute corrupted trajectories in the actual environment to observe realistic consequences, (3) generate recovery actions grounded in real environment feedback. This distinguishes TaxEI from methods that rely on LLM self-reflection (Reflexion, AgentRefine) or outcome-level contrastive signals (ETO). The recovery signal is neither hallucinated nor heuristic — it reflects how an agent should actually recover given the true environmental state after corruption. Combined with SFT training (without requiring RL infrastructure), this produces a practical and scalable training pipeline.\nDOCEOF\necho \"DONE: $(wc -l < /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md) lines\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T10:12:17.935895+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"DONE: 63 lines\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-table_20260514T101016",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T10:12:17.936045+00:00_

文件已写入 `/root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md`（63 行）。

核心对比结论：
- **PALADIN** 只覆盖 tool error，TaxEI 将注入式训练扩展到 planning + context error
- **Agent-R / ETO** 依赖自然产生的错误，TaxEI 用 taxonomy 系统化控制注入
- **Reflexion / AgentRefine** 的 recovery 信号来自 LLM 自省，TaxEI 的 recovery 来自真实环境反馈
- **ReAct** 是纯 prompt baseline，无 error training

所有信息已通过 WebSearch 交叉验证，无 [TBD] 标注。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_related-work-table_20260514T101016"
}
```

</details>

---
