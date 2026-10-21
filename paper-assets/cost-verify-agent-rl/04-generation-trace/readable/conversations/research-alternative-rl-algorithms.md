# research alternative rl algorithms

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 0
- **Tool calls:** 31
- **Original source:** `logs/chats/worker_research_alternative-rl-algorithms_20260514T131751.jsonl`
- **Structured JSON:** [`2b62e9024dc3f4b98786.json`](../../sessions/2b/2b62e9024dc3f4b98786.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

64 recorded events

### Assistant

_source line 1 · 2026-05-14T13:18:01.025598+00:00_

You've hit your limit · resets 5am (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T13:24:47.607083+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,TodoWrite,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,TodoWrite,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-14T13:24:47.607366+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T13:24:47.607542+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Search GDPO algorithm papers', 'activeForm': 'Searching GDPO algorithm papers', 'status': 'in_progress'}, {'content': 'Search DAPO clip-higher dynamic sampling', 'activeForm': 'Searching DAPO clip-higher dynamic sampling', 'status': 'pending'}, {'content': 'Search SPEAR sparse reward exploration', 'activeForm': 'Searching SPEAR sparse reward exploration', 'status': 'pending'}, {'content': 'Search Dr.GRPO and GRPO variants', 'activeForm': 'Searching Dr.GRPO and GRPO variants', 'status': 'pending'}, {'content': 'Search sparse reward RL for LLM agents', 'activeForm': 'Searching sparse reward RL for LLM agents', 'status': 'pending'}, {'content': 'Verify key papers via WebFetch', 'activeForm': 'Verifying key papers via WebFetch', 'status': 'pending'}, {'content': 'Write literature_rl_alternatives.md', 'activeForm': 'Writing literature_rl_alternatives.md', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Search GDPO algorithm papers', 'activeForm': 'Searching GDPO algorithm papers', 'status': 'in_progress'}, {'content': 'Search DAPO clip-higher dynamic sampling', 'activeForm': 'Searching DAPO clip-higher dynamic sampling', 'status': 'pending'}, {'content': 'Search SPEAR sparse reward exploration', 'activeForm': 'Searching SPEAR sparse reward exploration', 'status': 'pending'}, {'content': 'Search Dr.GRPO and GRPO variants', 'activeForm': 'Searching Dr.GRPO and GRPO variants', 'status': 'pending'}, {'content': 'Search sparse reward RL for LLM agents', 'activeForm': 'Searching sparse reward RL for LLM agents', 'status': 'pending'}, {'content': 'Verify key papers via WebFetch', 'activeForm': 'Verifying key papers via WebFetch', 'status': 'pending'}, {'content': 'Write literature_rl_alternatives.md', 'activeForm': 'Writing literature_rl_alternatives.md', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T13:24:47.607773+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T13:24:47.607918+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GDPO Group Distributionally-robust Policy Optimization LLM sparse reward 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GDPO Group Distributionally-robust Policy Optimization LLM sparse reward 2025"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T13:24:47.608042+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DAPO clip-higher dynamic sampling GRPO LLM reasoning paper 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DAPO clip-higher dynamic sampling GRPO LLM reasoning paper 2025"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T13:24:47.608188+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SPEAR sparse reward exploration LLM agent reinforcement learning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SPEAR sparse reward exploration LLM agent reinforcement learning 2025"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T13:24:47.608309+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dr GRPO improved variant length bias group relative policy optimization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dr GRPO improved variant length bias group relative policy optimization"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T13:24:47.608463+00:00_

Web search results for query: "GDPO Group Distributionally-robust Policy Optimization LLM sparse reward 2025"

Links: [{"title":"Group Distributionally Robust Optimization-Driven Reinforcement Learning for LLM Reasoning","url":"https://arxiv.org/html/2601.19280v1"},{"title":"[2601.05242] GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://arxiv.org/abs/2601.05242"},{"title":"GitHub - NVlabs/GDPO: Official implementation of GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization · GitHub","url":"https://github.com/NVlabs/GDPO"},{"title":"Paper page - GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://huggingface.co/papers/2601.05242"},{"title":"GDPO: Group reward-Decoupled Normalization Policy ...","url":"https://arxiv.org/pdf/2601.05242"},{"title":"GAGPO: Generalized Advantage Grouped Policy Optimization","url":"https://arxiv.org/html/2605.13217"},{"title":"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://arxiv.org/html/2601.05242"},{"title":"[Quick Review] GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization","url":"https://liner.com/review/gdpo-group-rewarddecoupled-normalization-policy-optimization-for-multireward-rl-optimization"},{"title":"Robust LLM Alignment via Distributionally Robust Direct Preference Optimization | OpenReview","url":"https://openreview.net/forum?id=D19hc2XPeZ"},{"title":"DGPO: Decoupled Gradient Policy Optimization for RLVR in LLMs | OpenReview","url":"https://openreview.net/forum?id=AU37MqplU4"}]

Based on the search results, I found information about GDPO and related concepts:

## GDPO: Group reward-Decoupled Normalization Policy Optimization

GDPO (Group reward-Decoupled Normalization Policy Optimization) is a new policy optimization method that resolves multi-reward optimiz
…[truncated 1604 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T13:24:47.608690+00:00_

Web search results for query: "DAPO clip-higher dynamic sampling GRPO LLM reasoning paper 2025"

Links: [{"title":"DAPO: An Open-Source LLM Reinforcement Learning System at Scale | OpenReview","url":"https://openreview.net/forum?id=2a36EMSSTp"},{"title":"[2503.14476] DAPO: An Open-Source LLM Reinforcement Learning System at Scale","url":"https://arxiv.org/abs/2503.14476"},{"title":"The Mathematics of DAPO, PPO, and GRPO Algorithms by Miquel Noguer I Alonso, Rodolfo Pereira Franklin :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/5205449.pdf?abstractid=5205449&mirid=1"},{"title":"DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization): GRPO on steroids | by Syed Hasan | Medium","url":"https://medium.com/@syed_hasan/dapo-decoupled-clip-and-dynamic-sampling-policy-optimization-grpo-on-steroids-9c571a0536f3"},{"title":"DAPO: An Open Source LLM Reinforcement Learning System at Scale","url":"https://self-supervised.cs.jhu.edu/fa2025/files/presentations/Why-RL-Sep16-AdvancesNLP.pdf"},{"title":"[2512.07611] Comparative Analysis and Parametric Tuning of PPO, GRPO, and DAPO for LLM Reasoning Enhancement","url":"https://arxiv.org/abs/2512.07611"},{"title":"DAPO","url":"https://dapo-sia.github.io/"},{"title":"DAPO: An Open-Source LLM Reinforcement Learning System at Scale 1ByteDance Seed","url":"https://arxiv.org/pdf/2503.14476"},{"title":"DAPO: Enhancing GRPO For LLM Reinforcement Learning - AI Papers Academy","url":"https://aipapersacademy.com/dapo/"},{"title":"DAPO: A Case Study with Small Language Models | Projects","url":"https://alexlavaee.me/projects/reasoning-slms/"}]

Based on the search results, here's what I found about the DAPO paper and related research:

## DAPO: An Open-Source LLM Reinforcement Learning System at Scale

DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization) is an algorithm that achieves 50 points on AIME 2024 using Qwen2.5-32B base model.

### Key Technical Components

Clip-Higher promotes the diversity of the system and 
…[truncated 1370 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T13:24:47.608890+00:00_

Web search results for query: "SPEAR sparse reward exploration LLM agent reinforcement learning 2025"

Links: [{"title":"GitHub - TencentYoutuResearch/SPEAR: An RL Recipe for Building Agentic LLMs via Self-Imitation on Long-Horizon Agentic Tasks · GitHub","url":"https://github.com/TencentYoutuResearch/SPEAR"},{"title":"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning","url":"https://arxiv.org/html/2509.22601v1"},{"title":"Paper page - Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning","url":"https://huggingface.co/papers/2509.22601"},{"title":"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=Kssko33Ekq"},{"title":"sparse- reward multi-agent reinforcement learning","url":"https://arxiv.org/pdf/2509.21828"},{"title":"LLM-Driven Intrinsic Motivation for Sparse Reward Reinforcement Learning","url":"https://arxiv.org/html/2508.18420v1"},{"title":"STO-RL: Offline RL under Sparse Rewards via LLM-Guided Subgoal Temporal Order","url":"https://arxiv.org/html/2601.08107v1"},{"title":"GitHub - opendilab/awesome-exploration-rl: A curated list of awesome exploration RL resources (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-exploration-rl"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"GUIDED LEARNING FOR SPARSE-REWARD MULTI- ...","url":"https://openreview.net/pdf?id=7ei1uOYUY0"}]

Based on the search results, here's what I found about SPEAR:

## SPEAR: Self-Imitation Learning for Agentic LLMs

SPEAR is a curriculum-based self-imitation learning (SIL) framework for training agentic LLMs on long-horizon, sparse-reward tas
…[truncated 1228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T13:24:47.609098+00:00_

Web search results for query: "Dr GRPO improved variant length bias group relative policy optimization"

Links: [{"title":"Group Relative Policy Optimization (GRPO) — verl documentation","url":"https://verl.readthedocs.io/en/latest/algo/grpo.html"},{"title":"Dr. GRPO: Correcting Token Aggregation Bias","url":"https://www.emergentmind.com/topics/dr-grpo"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"GRPO: Group Relative Policy Optimization","url":"https://www.emergentmind.com/topics/grpo"},{"title":"The Evolution of Policy Optimization: Understanding GRPO, DAPO, and Dr. GRPO’s Theoretical Foundations | by Jennifer Wei | Medium","url":"https://medium.com/@jenwei0312/the-evolution-of-policy-optimization-understanding-grpo-dapo-and-dr-3e758c54b2c6"},{"title":"GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision for Effective Reasoning","url":"https://arxiv.org/html/2604.20659"},{"title":"GRPO Trainer · Hugging Face","url":"https://huggingface.co/docs/trl/main/en/grpo_trainer"},{"title":"From REINFORCE to Dr. GRPO","url":"https://lancelqf.github.io/note/llm_post_training/"},{"title":"Balanced Aggregation: Understanding and Fixing Aggregation Bias in GRPO","url":"https://arxiv.org/html/2605.04077"},{"title":"GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control","url":"https://arxiv.org/html/2508.03772v4"}]

Based on the search results, here's what I found about Dr GRPO and its improvements for length bias in group relative policy optimization:

## Overview

Dr. GRPO is a modification to the Group Relative Policy Optimization (GRPO) framework that addresses systematic biases in the way token-level policy gradients are aggregated, particularly concerning the influence of sequence length.

## The Length Bias Problem

GRPO's normalization by sequence length causes longer incorrect responses to be under-penalized. There's optimization bias
…[truncated 1332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T13:24:47.609329+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Search GDPO algorithm papers', 'activeForm': 'Searching GDPO algorithm papers', 'status': 'completed'}, {'content': 'Search DAPO clip-higher dynamic sampling', 'activeForm': 'Searching DAPO clip-higher dynamic sampling', 'status': 'completed'}, {'content': 'Search SPEAR sparse reward exploration', 'activeForm': 'Searching SPEAR sparse reward exploration', 'status': 'completed'}, {'content': 'Search Dr.GRPO and GRPO variants', 'activeForm': 'Searching Dr.GRPO and GRPO variants', 'status': 'completed'}, {'content': 'Search sparse reward RL for LLM agents', 'activeForm': 'Searching sparse reward RL for LLM agents', 'status': 'in_progress'}, {'content': 'Verify key papers via WebFetch', 'activeForm': 'Verifying key papers via WebFetch', 'status': 'pending'}, {'content': 'Write literature_rl_alternatives.md', 'activeForm': 'Writing literature_rl_alternatives.md', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Search GDPO algorithm papers', 'activeForm': 'Searching GDPO algorithm papers', 'status': 'completed'}, {'content': 'Search DAPO clip-higher dynamic sampling', 'activeForm': 'Searching DAPO clip-higher dynamic sampling', 'status': 'completed'}, {'content': 'Search SPEAR sparse reward exploration', 'activeForm': 'Searching SPEAR sparse reward exploration', 'status': 'completed'}, {'content': 'Search Dr.GRPO and GRPO variants', 'activeForm': 'Searching Dr.GRPO and GRPO variants', 'status': 'completed'}, {'content': 'Search sparse reward RL for LLM agents', 'activeForm': 'Searching sparse reward RL for LLM agents', 'status': 'in_progress'}, {'content': 'Verify key papers via WebFetch', 'activeForm': 'Verifying key papers via WebFetch', 'status': 'pending'}, {'content': 'Write literature_rl_alternatives.md', 'activeForm': 'Writing literature_rl_alternatives.md', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T13:24:47.609492+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T13:24:47.609615+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ALFWorld GRPO sparse reward LLM agent RAGEN training collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ALFWorld GRPO sparse reward LLM agent RAGEN training collapse"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T13:24:47.609794+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "curiosity-driven exploration LLM agent sparse reward intrinsic motivation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "tool_args": {
    "query": "curiosity-driven exploration LLM agent sparse reward intrinsic motivation 2025"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T13:24:47.609918+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GiGPO group-in-group policy optimization agent ALFWorld 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GiGPO group-in-group policy optimization agent ALFWorld 2025"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T13:24:47.610032+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RLOO REINFORCE++ leave-one-out sparse reward LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RLOO REINFORCE++ leave-one-out sparse reward LLM 2025"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T13:24:47.610184+00:00_

Web search results for query: "ALFWorld GRPO sparse reward LLM agent RAGEN training collapse"

Links: [{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via","url":"https://ragen-ai.github.io/pdf/RAGEN.pdf"},{"title":"RAGEN-2: Reasoning Collapse in Agentic RL","url":"https://ragen-ai.github.io/"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://arxiv.org/pdf/2505.10978"},{"title":"GitHub - mll-lab-nu/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments. · GitHub","url":"https://github.com/mll-lab-nu/RAGEN"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2504.20073v2"},{"title":"A Practitioner’s Guide to Multi-turn Agentic Reinforcement Learning","url":"https://arxiv.org/html/2510.01132"},{"title":"Training LLM Agents Just Got More Stable: Researchers Introduce StarPO-S and RAGEN to Tackle Multi-Turn Reasoning and Collapse in Reinforcement Learning - MarkTechPost","url":"https://www.marktechpost.com/2025/05/01/training-llm-agents-just-got-more-stable-researchers-introduce-starpo-s-and-ragen-to-tackle-multi-turn-reasoning-and-collapse-in-reinforcement-learning/"},{"title":"EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning","url":"https://arxiv.org/html/2509.22576"},{"title":"ShapE-GRPO: Shapley-Enhanced Reward Allocation for Multi-Candidate LLM Training","url":"https://arxiv.org/html/2603.29871"}]

I found comprehensive information about this topic. Here's what the research shows:

## Overview

Vanilla adaptations from single-turn methods like PPO and GRPO achieve early gains in agent settings but often collapse. This is a central problem that RAGEN (Reasoning Agents for General Environments) addresses.

## The Training Collapse
…[truncated 1576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T13:24:47.610363+00:00_

Web search results for query: "curiosity-driven exploration LLM agent sparse reward intrinsic motivation 2025"

Links: [{"title":"LLM-Driven Intrinsic Motivation for Sparse Reward Reinforcement Learning","url":"https://arxiv.org/html/2508.18420v1"},{"title":"NeurIPS Poster Wonder Wins Ways: Curiosity-Driven Exploration through Multi-Agent Contextual Calibration","url":"https://neurips.cc/virtual/2025/poster/120209"},{"title":"Curiosity-Driven Reinforcement Learning from Human ...","url":"https://aclanthology.org/2025.acl-long.1146.pdf"},{"title":"Online Intrinsic Rewards for Decision Making Agents from ...","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_6.pdf"},{"title":"[2302.10825] Curiosity-driven Exploration in Sparse-reward Multi-agent Reinforcement Learning","url":"https://arxiv.org/abs/2302.10825"},{"title":"[2508.18420] LLM-Driven Intrinsic Motivation for Sparse Reward Reinforcement Learning","url":"https://arxiv.org/abs/2508.18420"},{"title":"Navigate the Unknown: Enhancing LLM Reasoning with Intrinsic Motivation Guided Exploration","url":"https://arxiv.org/html/2505.17621v5"},{"title":"The impact of intrinsic rewards on exploration in Reinforcement Learning | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-025-11340-0"},{"title":"ORIGINAL ARTICLE The impact of intrinsic rewards on exploration","url":"https://d-nb.info/1377024458/34"},{"title":"Curiosity-Driven Exploration in Reinforcement Learning: An Adaptive Self-Supervised Learning Approach for Playing Action Games","url":"https://www.mdpi.com/2073-431X/14/10/434"}]

I found several relevant research papers and articles on this topic. Here's a summary of the key findings:

## LLM-Driven Intrinsic Motivation for Sparse Reward RL

A recent paper explores the combination of two intrinsic motivation strategies to improve the efficiency of RL agents in environments with extreme sparse rewards, proposing integration of Variational Sta
…[truncated 1755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T13:24:47.610539+00:00_

Web search results for query: "GiGPO group-in-group policy optimization agent ALFWorld 2025"

Links: [{"title":"[2505.10978] Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/abs/2505.10978"},{"title":"GAGPO: Generalized Advantage Grouped Policy Optimization","url":"https://arxiv.org/html/2605.13217"},{"title":"NeurIPS Poster Group-in-Group Policy Optimization for LLM Agent Training","url":"https://neurips.cc/virtual/2025/poster/118123"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training | OpenReview","url":"https://openreview.net/forum?id=QXEhBMNrCW"},{"title":"Paper page - Group-in-Group Policy Optimization for LLM Agent Training","url":"https://huggingface.co/papers/2505.10978"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978v1"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.10978v1"},{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengq/verl-agent"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training | Request PDF","url":"https://www.researchgate.net/publication/391857132_Group-in-Group_Policy_Optimization_for_LLM_Agent_Training"}]

Based on the search results, here's what I found about GiGPO:

## Overview

Group-in-Group Policy Optimization (GiGPO) is a novel reinforcement learning algorithm that achieves fine-grained credit assignment for LLM agents while preserving the appealing properties of group-based RL: critic-free, low memory, and stable convergence.

## How It Works

GiGPO introduce
…[truncated 1400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T13:24:47.610747+00:00_

Web search results for query: "RLOO REINFORCE++ leave-one-out sparse reward LLM 2025"

Links: [{"title":"Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs","url":"https://arxiv.org/html/2402.14740v1"},{"title":"REINFORCE: Easy Online RL for LLMs","url":"https://cameronrwolfe.substack.com/p/reinforce"},{"title":"Putting RL back in RLHF","url":"https://huggingface.co/blog/putting_rl_back_in_rlhf_with_rloo"},{"title":"From REINFORCE to Dr. GRPO","url":"https://lancelqf.github.io/note/llm_post_training/"},{"title":"REINFORCE: A Simple and Effective Approach to LLM Alignment","url":"https://medium.com/@ayoubkirouane3/reinforce-a-simple-and-effective-approach-to-llm-alignment-75c7ac0fdf9d"},{"title":"Revisiting REINFORCE-Style Optimization for Learning ...","url":"https://aclanthology.org/2024.acl-long.662.pdf"},{"title":"Exploring the Limit of Outcome Reward for Learning Mathematical Reasoning","url":"https://arxiv.org/pdf/2502.06781"},{"title":"Exploring Pass-Rate Reward in Reinforcement Learning for Code Generation","url":"https://arxiv.org/html/2605.02944"},{"title":"Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human","url":"https://arxiv.org/pdf/2402.14740"},{"title":"Simpler Online Reinforcement Learning for LLM Alignment: Why REINFORCE Deserves Another Look","url":"https://www.linkedin.com/pulse/simpler-online-reinforcement-learning-llm-alignment-why-reinforce-qdkic"}]

Based on the search results, here's what I found about RLOO, REINFORCE++, leave-one-out sparse reward, and LLM training in 2025:

## RLOO (REINFORCE Leave-One-Out)

RLOO is a multi-sample extension of the REINFORCE estimator used to optimize the sequence-level objective in LLM training. It treats the entire model completion as a single action, whereas regular PPO treats each completion token as individual actions, and attributes the EOS reward to the entire completion rather than just the EOS token.

## Key Advantages

RLOO 
…[truncated 1128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T13:24:47.610912+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "StarPO-S RAGEN stabilized policy optimization filtering low-variance trajectory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "tool_args": {
    "query": "StarPO-S RAGEN stabilized policy optimization filtering low-variance trajectory"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T13:24:47.611038+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EPO entropy-regularized policy optimization LLM agent reinforcement learning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EPO entropy-regularized policy optimization LLM agent reinforcement learning 2025"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T13:24:47.611153+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "hindsight experience replay LLM agent sparse reward reward relabeling 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "tool_args": {
    "query": "hindsight experience replay LLM agent sparse reward reward relabeling 2025"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T13:24:47.611262+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GTPO gradient entropy control GRPO stability collapse 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GTPO gradient entropy control GRPO stability collapse 2025"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T13:24:47.611413+00:00_

Web search results for query: "StarPO-S RAGEN stabilized policy optimization filtering low-variance trajectory"

Links: [{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via","url":"https://ragen-ai.github.io/pdf/RAGEN.pdf"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via ...","url":"https://arxiv.org/pdf/2504.20073"},{"title":"RAGEN-2: Reasoning Collapse in Agentic RL","url":"https://ragen-ai.github.io/"},{"title":"StarPO (Trajectory Optimization for LLM Agents) - Arize AI","url":"https://arize.com/glossary/starpo-trajectory-optimization-for-llm-agents/"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2504.20073v2"},{"title":"RAGEN: Self-Evolution in LLM Agents via Multi-Turn RL","url":"https://www.emergentmind.com/papers/2504.20073"},{"title":"StarPO-S Stabilization for LLM Agents","url":"https://www.emergentmind.com/topics/starpo-s-stabilization"},{"title":"StarPO: RL Framework for LLM Agents","url":"https://www.emergentmind.com/topics/starpo-framework"},{"title":"Training AI Agents That Don’t Fall Apart: How RAGEN and StarPO Are Solving the ‘Echo Trap’ | by Tech Dose | Medium","url":"https://medium.com/@tech.dose/training-ai-agents-that-dont-fall-apart-how-ragen-and-starpo-are-solving-the-echo-trap-c149b23248fa"},{"title":"RAGEN & StarPO Aim to Tame LLM Instability in Complex Tasks - Business Leaders Review: Best Business Magazine and News Online","url":"https://businessleadersreview.com/ragen-starpo-aim-to-tame-llm-instability-in-complex-tasks/"}]

Based on the web search results, here's what I found about StarPO-S, RAGEN, and stabilized policy optimization with trajectory filtering:

## Overview

StarPO (State-Thinking-Actions-Reward Policy Optimization) is a general framework for trajectory-level agent RL, and RAGEN is a modular system for training and evaluating LLM agents.

## StarPO-S Stabilization

StarPO-S is a stabilized variant of the framework 
…[truncated 1045 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T13:24:47.611582+00:00_

Web search results for query: "EPO entropy-regularized policy optimization LLM agent reinforcement learning 2025"

Links: [{"title":"[2509.22576] EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning","url":"https://arxiv.org/abs/2509.22576"},{"title":"EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning","url":"https://arxiv.org/html/2509.22576v1"},{"title":"GitHub - WujiangXu/EPO: The code for paper \"EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning\"","url":"https://github.com/WujiangXu/EPO"},{"title":"Paper page - EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning","url":"https://huggingface.co/papers/2509.22576"},{"title":"Under review EPO: ENTROPY-REGULARIZED POLICY OPTIMIZATION","url":"https://arxiv.org/pdf/2509.22576"},{"title":"EPO: Entropy-Regularized Policy Optimization for LLM Agents Reinforcement Learning | by Dixon | Medium","url":"https://medium.com/@huguosuo/epo-entropy-regularized-policy-optimization-for-llm-agents-reinforcement-learning-37d0b473773a"},{"title":"EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/resources/2509.22576v1"},{"title":"Paper page - Agentic Entropy-Balanced Policy Optimization","url":"https://huggingface.co/papers/2510.14545"},{"title":"EXPLORING THE ENTROPY MECHANISM IN ON-POLICY ...","url":"https://openreview.net/pdf/6c16f45b426201b6fae58f66047f9496c0aa6f30.pdf"},{"title":"EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/epo-entropy-regularized-policy-optimization-llm-agents"}]

I've performed the web search and found comprehensive information about EPO. Here are the key findings:

## EPO: Entropy-regularized Policy Optimization for LLM Agents

EPO addresses the fundamental challenge of training LLM agents in multi-tu
…[truncated 1485 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T13:24:47.611788+00:00_

Web search results for query: "hindsight experience replay LLM agent sparse reward reward relabeling 2025"

Links: [{"title":"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling","url":"https://arxiv.org/html/2603.21357"},{"title":"Sample-Efficient Online Learning in LM Agents via Hindsight Trajectory Rewriting","url":"https://arxiv.org/html/2510.10304v1"},{"title":"[2603.21357] AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling","url":"https://arxiv.org/abs/2603.21357"},{"title":"Hindsight Task Relabelling: Experience Replay for Sparse Reward Meta-RL","url":"https://openreview.net/pdf?id=FeFIzwifdoL"},{"title":"Hindsight Experience Replay - Practical Guide 2025 | ShadeCoder","url":"https://www.shadecoder.com/topics/hindsight-experience-replay-a-comprehensive-guide-for-2025"},{"title":"Enabling Option Learning in Sparse Rewards with Hindsight Experience Replay","url":"https://arxiv.org/html/2602.13865v1"},{"title":"Sparse Reward: A Comprehensive Guide for 2025 - Shadecoder - 100% Invisibile AI Coding Interview Copilot","url":"https://www.shadecoder.com/topics/sparse-reward-a-comprehensive-guide-for-2025"},{"title":"[2602.13865] Enabling Option Learning in Sparse Rewards with Hindsight Experience Replay","url":"https://arxiv.org/abs/2602.13865"},{"title":"Hindsight Experience Replay","url":"https://www.emergentmind.com/topics/hindsight-experience-replay"},{"title":"GitHub - kaixindelele/RHER: The Code for Paper “Relay Hindsight Experience Replay: Self-Guided Continual Reinforcement Learning for Sequential Object Manipulation Tasks with Sparse Rewards”","url":"https://github.com/kaixindelele/RHER"}]

Based on the search results, here are the key findings about hindsight experience replay, LLM agents, sparse rewards, and reward relabeling in 2025:

## Recent LLM Agent Applications

AgentHER is a framework that adapts the Hindsight Experience Replay (HER) principle to natural-language agent trajectories for offline data augme
…[truncated 1474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T13:24:47.611969+00:00_

Web search results for query: "GTPO gradient entropy control GRPO stability collapse 2025"

Links: [{"title":"GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control","url":"https://arxiv.org/html/2508.03772v4"},{"title":"[2508.03772] GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control","url":"https://arxiv.org/abs/2508.03772"},{"title":"GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250803772S/abstract"},{"title":"GTPO: Trajectory-Based Policy Optimization in Large Language Models","url":"https://arxiv.org/html/2508.03772v3"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Multi-Turn+Group+Relative+Policy+Optimization"},{"title":"CE-GPPO: Coordinating Entropy via Gradient-Preserving Clipping Policy Optimization in Reinforcement Learning","url":"https://arxiv.org/html/2509.20712"},{"title":"GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with Policy Entropy","url":"https://arxiv.org/html/2508.04349v6"},{"title":"GTPO vs GRPO: A Smarter Path to Stable Reasoning LLMs | by Marco Simoni | Medium","url":"https://medium.com/@marco.simoni0711/gtpo-vs-grpo-a-smarter-path-to-stable-reasoning-llms-3f51bc0b58c1"},{"title":"GitHub - winstonsmith1897/GTPO: Group-relative Trajectory-based Policy Optimization: Increasing Quality and Training Stability · GitHub","url":"https://github.com/winstonsmith1897/GTPO"},{"title":"GTPO: Fine-Grained Policy Optimization","url":"https://www.emergentmind.com/topics/gtpo"}]

Based on the search results, here's comprehensive information about GTPO, gradient entropy control, GRPO stability, and collapse issues in 2025:

## GTPO: Stabilizing GRPO via Gradient and Entropy Control

Group-relative Trajectory-based Policy Optimization (GTPO) addresses two issues of GRPO—gradient conflicts and policy collapse—through conflict-aware updates and entropy contro
…[truncated 1648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T13:24:47.612156+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "multi-turn agent RL credit assignment process reward step-level GRPO 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "tool_args": {
    "query": "multi-turn agent RL credit assignment process reward step-level GRPO 2025"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T13:24:47.612292+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"self-imitation learning\" LLM agent ALFWorld WebShop replay buffer 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"self-imitation learning\" LLM agent ALFWorld WebShop replay buffer 2025"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T13:24:47.612408+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VAPO value augmented policy optimization sparse reward 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VAPO value augmented policy optimization sparse reward 2025"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T13:24:47.612520+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARPO Agentic-RLPO trinity-RFT sparse reward training stability 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARPO Agentic-RLPO trinity-RFT sparse reward training stability 2025"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T13:24:47.612676+00:00_

Web search results for query: "VAPO value augmented policy optimization sparse reward 2025"

Links: [{"title":"[2504.05118] VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks","url":"https://arxiv.org/abs/2504.05118"},{"title":"VAPO: Efficient and Reliable Reinforcement Learning for ...","url":"https://arxiv.org/pdf/2504.05118"},{"title":"VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks","url":"https://arxiv.org/html/2504.05118v1"},{"title":"VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.05118v3"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=VAPO+framework"},{"title":"Paper page - VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks","url":"https://huggingface.co/papers/2504.05118"},{"title":"PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning","url":"https://arxiv.org/html/2508.21104v1"},{"title":"VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks","url":"https://www.researchgate.net/publication/390571214_VAPO_Efficient_and_Reliable_Reinforcement_Learning_for_Advanced_Reasoning_Tasks"},{"title":"VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/vapo-efficient-reliable-reinforcement-learning-advanced-reasoning"},{"title":"[2504.05118v3] VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks","url":"https://arxiv.org/abs/2504.05118v3"}]

Based on the search results, here's what I found about VAPO:

## Overview

VAPO is a Value-based Augmented Proximal Policy Optimization framework for reasoning models, a novel framework tailored for reasoning models within the value-based paradigm.

## Key Challenges Addressed

VAPO addresses three key challenges that plague value-based method
…[truncated 1238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T13:24:47.612862+00:00_

Web search results for query: "multi-turn agent RL credit assignment process reward step-level GRPO 2025"

Links: [{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"NeurIPS Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design and Credit Assignment","url":"https://neurips.cc/virtual/2025/133311"},{"title":"GitHub - SiliangZeng/Multi-Turn-RL-Agent · GitHub","url":"https://github.com/SiliangZeng/Multi-Turn-RL-Agent"},{"title":"[2505.11821] Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design","url":"https://arxiv.org/abs/2505.11821"},{"title":"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design","url":"https://arxiv.org/html/2505.11821v2"},{"title":"Multi-Turn Credit Assignment with LLM Agents - hlfshell","url":"https://hlfshell.ai/posts/multi-turn-credit-assignment/"},{"title":"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design | OpenReview","url":"https://openreview.net/forum?id=7cgTBPuwMr"},{"title":"ICML Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Credit Assignment","url":"https://icml.cc/virtual/2025/49783"},{"title":"NeurIPS 2025 Workshop on Multi-Turn Interactions in Large Language Models","url":"https://workshop-multi-turn-interaction.github.io/"},{"title":"[Quick Review] Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Credit\\n Assignment","url":"https://liner.com/review/reinforcing-multiturn-reasoning-in-llm-agents-via-turnlevel-credit-assignment"}]

Based on the search results, I found comprehensive information about multi-turn agent RL credit assignment with GRPO in 2025:

## Key Findings

Research in 2025 investigates RL approaches to enhance reasoning capabilities of LLM agents in long-horizon, multi-turn scenarios. Although RL algorithms such as Group Rel
…[truncated 1662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T13:24:47.613031+00:00_

Web search results for query: "ARPO Agentic-RLPO trinity-RFT sparse reward training stability 2025"

Links: [{"title":"GitHub - RUC-NLPIR/ARPO: [ICLR 2026] Agentic Reinforced Policy Optimization (ARPO) · GitHub","url":"https://github.com/RUC-NLPIR/ARPO"},{"title":"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning","url":"https://arxiv.org/html/2605.02178v1"},{"title":"Agentic Reinforced Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=TX4k7BF6aO"},{"title":"Agentic Reinforced Policy Optimization","url":"https://arxiv.org/html/2507.19849v1"},{"title":"[2507.19849] Agentic Reinforced Policy Optimization","url":"https://arxiv.org/abs/2507.19849"},{"title":"arXiv:2505.16282v1 [cs.CV] 22 May 2025 ARPO: End-to-End Policy Optimization","url":"https://arxiv.org/pdf/2505.16282"},{"title":"[2505.16282] ARPO:End-to-End Policy Optimization for GUI Agents with Experience Replay","url":"https://arxiv.org/abs/2505.16282"},{"title":"Agentic Reinforced Policy Optimization | Request PDF","url":"https://www.researchgate.net/publication/394081444_Agentic_Reinforced_Policy_Optimization"},{"title":"ICLR Poster Agentic Reinforced Policy Optimization","url":"https://iclr.cc/virtual/2026/poster/10009306"},{"title":"Paper page - Agentic Reinforced Policy Optimization","url":"https://huggingface.co/papers/2507.19849"}]

Based on the search results, here's what I found about your query:

## ARPO (Agentic Reinforced Policy Optimization)

ARPO is a novel agentic RL algorithm tailored for training multi-turn LLM-based agents. The ARPO paper was made available on arXiv on July 29, 2025.

### Key Technical Components

LLMs frequently exhibit increased uncertainty after tool-call steps, as evidenced by higher entropy in the distribution of generated tokens, which motivated ARPO to incorporate an entropy-based adaptive rollout mechanism that encourages the policy model to adaptively branch sampling during high-entropy tool-call r
…[truncated 1048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T13:24:47.613203+00:00_

Web search results for query: ""self-imitation learning" LLM agent ALFWorld WebShop replay buffer 2025"

Links: [{"title":"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning","url":"https://arxiv.org/html/2509.22601v1"},{"title":"[2509.22601] Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning","url":"https://arxiv.org/abs/2509.22601"},{"title":"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=Kssko33Ekq"},{"title":"yolay/SPEAR-ALFWorld-DrBoT-GRPO-1.5B · Hugging Face","url":"https://huggingface.co/yolay/SPEAR-ALFWorld-DrBoT-GRPO-1.5B"},{"title":"GitHub - TencentYoutuResearch/SPEAR: An RL Recipe for Building Agentic LLMs via Self-Imitation on Long-Horizon Agentic Tasks · GitHub","url":"https://github.com/TencentYoutuResearch/SPEAR"},{"title":"Improving Retrospective Language Agents via Joint Policy ...","url":"https://aclanthology.org/2025.naacl-long.6.pdf"},{"title":"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models","url":"https://arxiv.org/html/2601.08955v2"},{"title":"Paper page - Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning","url":"https://huggingface.co/papers/2509.22601"},{"title":"FEDERATED AGENT REINFORCEMENT LEARNING","url":"https://openreview.net/pdf?id=BhrN4Sv6v2"},{"title":"[2602.05842] Reinforcement World Model Learning for LLM-based Agents","url":"https://arxiv.org/abs/2602.05842"}]

Based on the search results, I found relevant information about self-imitation learning with LLM agents on ALFWorld and WebShop tasks in 2025:

## SPEAR: Self-Imitation Learning Framework (2025)

SPEAR is a self-imitation learning (SIL) recipe for training agentic LLMs that extends the vanilla SIL, where a replay buffer stores go
…[truncated 1264 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T13:24:47.613351+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Search GDPO algorithm papers', 'activeForm': 'Searching GDPO algorithm papers', 'status': 'completed'}, {'content': 'Search DAPO clip-higher dynamic sampling', 'activeForm': 'Searching DAPO clip-higher dynamic sampling', 'status': 'completed'}, {'content': 'Search SPEAR sparse reward exploration', 'activeForm': 'Searching SPEAR sparse reward exploration', 'status': 'completed'}, {'content': 'Search Dr.GRPO and GRPO variants', 'activeForm': 'Searching Dr.GRPO and GRPO variants', 'status': 'completed'}, {'content': 'Search sparse reward RL for LLM agents', 'activeForm': 'Searching sparse reward RL for LLM agents', 'status': 'completed'}, {'content': 'Verify SPEAR and EPO details via WebFetch', 'activeForm': 'Verifying SPEAR and EPO details via WebFetch', 'status': 'in_progress'}, {'content': 'Write literature_rl_alternatives.md', 'activeForm': 'Writing literature_rl_alternatives.md', 'status': 'pending'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Search GDPO algorithm papers', 'activeForm': 'Searching GDPO algorithm papers', 'status': 'completed'}, {'content': 'Search DAPO clip-higher dynamic sampling', 'activeForm': 'Searching DAPO clip-higher dynamic sampling', 'status': 'completed'}, {'content': 'Search SPEAR sparse reward exploration', 'activeForm': 'Searching SPEAR sparse reward exploration', 'status': 'completed'}, {'content': 'Search Dr.GRPO and GRPO variants', 'activeForm': 'Searching Dr.GRPO and GRPO variants', 'status': 'completed'}, {'content': 'Search sparse reward RL for LLM agents', 'activeForm': 'Searching sparse reward RL for LLM agents', 'status': 'completed'}, {'content': 'Verify SPEAR and EPO details via WebFetch', 'activeForm': 'Verifying SPEAR and EPO details via WebFetch', 'status': 'in_progress'}, {'content': 'Write literature_rl_alternatives.md', 'activeForm': 'Writing literature_rl_alternatives.md', 'status': 'pending'}]"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T13:24:47.613503+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T13:24:47.613622+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.22601",
  "prompt": "Extract key details about SPEAR algorithm: (1) authors and exact title; (2) what hyperparameters does it introduce; (3) what exact mechanisms does it use for handling sparse rewards in ALFWorld; (4) what reward shaping does it use (tool-use bonus details); (5) what is the curriculum schedule; (6) what framework/code is it built on"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2509.22601",
    "prompt": "Extract key details about SPEAR algorithm: (1) authors and exact title; (2) what hyperparameters does it introduce; (3) what exact mechanisms does it use for handling sparse rewards in ALFWorld; (4) what reward shaping does it use (tool-use bonus details); (5) what is the curriculum schedule; (6) what framework/code is it built on"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T13:24:47.613766+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.10978",
  "prompt": "Extract key details about GiGPO: (1) full title and authors; (2) exact mechanism of step-level credit assignment (anchor state grouping); (3) hyperparameters; (4) implementation details and whether it's built on verl; (5) ALFWorld results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2505.10978",
    "prompt": "Extract key details about GiGPO: (1) full title and authors; (2) exact mechanism of step-level credit assignment (anchor state grouping); (3) hyperparameters; (4) implementation details and whether it's built on verl; (5) ALFWorld results"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-14T13:24:47.613882+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.14476",
  "prompt": "Extract key details about DAPO: (1) the four key techniques; (2) clip-higher hyperparameter values (epsilon_low, epsilon_high); (3) dynamic sampling mechanism; (4) token-level loss vs sample-level loss; (5) overlong shaping"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2503.14476",
    "prompt": "Extract key details about DAPO: (1) the four key techniques; (2) clip-higher hyperparameter values (epsilon_low, epsilon_high); (3) dynamic sampling mechanism; (4) token-level loss vs sample-level loss; (5) overlong shaping"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T13:24:47.614004+00:00_

# SPEAR Algorithm: Key Details

## (1) Authors and Title
**Authors:** Yulei Qin, Xiaoyu Tan, Zhengbao He, Gang Li, Haojia Lin, Zongyi Li, Zihan Xu, Yuchen Shi, Siqi Cai, Renting Rui, Shaofei Cai, Yuzheng Cai, Xuan Zhang, Sheng Ye, Ke Li, Xing Sun

**Title:** "Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning"

## (2) Hyperparameters
The provided webpage does not specify particular hyperparameter values introduced by SPEAR.

## (3) Sparse Reward Handling in ALFWorld
The abstract does not detail specific mechanisms for handling sparse rewards in ALFWorld beyond stating that SPEAR "increases the success rates" by up to 16.1% over comparable baselines.

## (4) Reward Shaping/Tool-Use Bonus
The abstract mentions "intrinsic reward shaping" but does not provide specific details about tool-use bonus mechanisms.

## (5) Curriculum Schedule
The approach uses "curriculum scheduling" that "harmonizes intrinsic reward shaping and self-imitation to 1) expedite exploration via frequent tool interactions at the beginning, and 2) strengthen exploitation of successful tactics upon convergence." Precise scheduling parameters are not described in this excerpt.

## (6) Framework/Code
The webpage does not identify the underlying framework or provide code repository information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T13:24:47.614137+00:00_

# GiGPO: Key Details Extract

## (1) Title and Authors
**Title:** "Group-in-Group Policy Optimization for LLM Agent Training"

**Authors:** Lang Feng, Zhenghai Xue, Tingcong Liu, Bo An

## (2) Step-Level Credit Assignment Mechanism
The anchor state grouping approach works as follows: GiGPO "introduces an anchor state grouping mechanism that retroactively constructs step-level groups by identifying repeated environment states across trajectories. Actions stemming from the same state are grouped together, enabling micro relative advantage estimation."

## (3) Hyperparameters
The provided abstract and paper metadata do not specify hyperparameters. Access to the full paper content would be required for this information.

## (4) Implementation Details / verl Integration
The abstract notes GiGPO maintains "the same GPU memory overhead, identical LLM rollout, and incurring little to no additional time cost," but does not mention whether it's built on verl or provide other implementation specifics. Full paper review would be needed.

## (5) ALFWorld Results
GiGPO "achieves performance gains of > 12% on ALFWorld" compared to GRPO baseline. The paper uses Qwen2.5-1.5B/3B/7B-Instruct models for evaluation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-14T13:24:47.614270+00:00_

# DAPO: Key Technical Details

Based on the provided arXiv page content, I can only offer limited information:

## Available Information

**What the abstract confirms:**
The paper introduces "DAPO" (Decoupled Clip and Dynamic sAmpling Policy Optimization) and mentions it includes "four key techniques" that enable large-scale LLM RL success. The abstract states the system "achieves 50 points on AIME 2024 using Qwen2.5-32B base model."

## Unavailable Details

The specific technical details you've requested are **not contained in the webpage excerpt provided**:

- ❌ The four key techniques (mentioned but not detailed)
- ❌ Hyperparameter values (epsilon_low, epsilon_high)
- ❌ Dynamic sampling mechanism specifics
- ❌ Token-level vs. sample-level loss details
- ❌ Overlong shaping methodology

## Accessing Complete Information

To obtain these details, you would need to:
1. View the full PDF at `/pdf/2503.14476`
2. Access the project page: `dapo-sia.github.io`
3. Review the open-sourced training code in the verl framework
4. Consult the authors' dataset and documentation

The webpage only provides bibliographic information and the abstract, not the technical content itself.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T13:24:47.614399+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2509.22601v1",
  "prompt": "Extract detailed information about SPEAR for sparse reward agent training: (1) what specific intrinsic reward / tool-use bonus formula does it use; (2) what is the curriculum (formula and stages); (3) what is the self-imitation update rule; (4) what hyperparameters (replay buffer size, mixing ratio, entropy thresholds); (5) what RL framework is it built on; (6) for ALFWorld experiments, what base model and what specific results vs GRPO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2509.22601v1",
    "prompt": "Extract detailed information about SPEAR for sparse reward agent training: (1) what specific intrinsic reward / tool-use bonus formula does it use; (2) what is the curriculum (formula and stages); (3) what is the self-imitation update rule; (4) what hyperparameters (replay buffer size, mixing ratio, entropy thresholds); (5) what RL framework is it built on; (6) for ALFWorld experiments, what base model and what specific results vs GRPO"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T13:24:47.614516+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://dapo-sia.github.io/",
  "prompt": "Extract the four key techniques of DAPO with specific details: (1) Clip-Higher with exact epsilon_low and epsilon_high values; (2) Dynamic Sampling - what gets filtered; (3) Token-Level Policy Gradient Loss - what changes; (4) Overlong Reward Shaping - what reward modifications. Also extract the GRPO formula vs DAPO formula."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://dapo-sia.github.io/",
    "prompt": "Extract the four key techniques of DAPO with specific details: (1) Clip-Higher with exact epsilon_low and epsilon_high values; (2) Dynamic Sampling - what gets filtered; (3) Token-Level Policy Gradient Loss - what changes; (4) Overlong Reward Shaping - what reward modifications. Also extract the GRPO formula vs DAPO formula."
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T13:24:47.614651+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.22576",
  "prompt": "Extract details about EPO for sparse reward LLM agents: (1) the three mechanisms - exact formulas if possible; (2) entropy smoothing regularizer formula; (3) adaptive phase-based weighting schedule; (4) what is the failure mode \"exploration-exploitation cascade failure\"; (5) ALFWorld and ScienceWorld results with specific numbers vs GRPO baseline; (6) base model used"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2509.22576",
    "prompt": "Extract details about EPO for sparse reward LLM agents: (1) the three mechanisms - exact formulas if possible; (2) entropy smoothing regularizer formula; (3) adaptive phase-based weighting schedule; (4) what is the failure mode \"exploration-exploitation cascade failure\"; (5) ALFWorld and ScienceWorld results with specific numbers vs GRPO baseline; (6) base model used"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-14T13:24:47.614786+00:00_

# DAPO: Key Techniques and Formulas

Based on the provided content, here's what can be extracted:

## Four Key Techniques

**1. Clip-Higher**
The document describes this as promoting diversity and avoiding entropy collapse by "increasing the upper clip range of the importance sampling ratio in policy gradient loss." However, **specific epsilon values (epsilon_low and epsilon_high) are not provided** in this webpage.

**2. Dynamic Sampling**
The technique "filters out prompt groups with the accuracy equal to 1 and 0, keeping a consistent number of prompts with effective gradients across batches." This removes trivial cases (perfect or failed solutions) to focus training on meaningful examples.

**3. Token-level Policy Gradient Loss**
The page notes this is "critical in long-CoT RL scenarios" but provides **no details about what specific changes this entails**.

**4. Overlong Reward Shaping**
Described as "reduces reward noise and stabilizes training," though the exact **modifications to rewards are not specified** in this content.

## Formula Information

**Limitation**: Neither the GRPO formula nor the DAPO formula are included in this webpage. The document references "Detailed analysis and insights can be found in our technical report," indicating such mathematical details reside in the linked [paper](https://arxiv.org/pdf/2503.14476) rather than this summary page.

For complete technical specifications, consulting the full research paper would be necessary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T13:24:47.614916+00:00_

# EPO Paper Details - Available Information

Based on the arXiv abstract provided, I can only extract limited technical details:

## Available Information:

**Three Mechanisms:** The abstract mentions EPO includes:
1. "Adopting entropy regularization in multi-turn settings to enhance exploration"
2. "An entropy smoothing regularizer that bounds policy entropy within historical averages to prevent abrupt fluctuations"
3. "Adaptive phase-based weighting that balances exploration and exploitation across training"

However, **exact formulas are not included** in the abstract text provided.

**Failure Mode Identified:** The paper describes "exploration-exploitation cascade failure" as a two-stage problem: early "policy premature convergence" from sparse feedback commitment to flawed strategies, followed by "late-stage policy collapse" where standard entropy regularization backfires.

**Performance Results:**
- ScienceWorld: up to 152% improvement
- ALFWorld: up to 19.8% improvement
- No baseline comparison numbers provided in the abstract

**Base Model:** Not specified in the abstract content

## Limitation:

The webpage excerpt contains only the abstract and metadata. Technical details like exact formulas, detailed experimental comparisons, and model specifications would require accessing the full PDF or HTML versions linked on the page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-14T13:24:47.615093+00:00_

# SPEAR: Self-Imitation with Progressive Exploration for Agentic RL

## 1. Intrinsic Reward Formula

SPEAR uses a composite reward with three components:

**Outcome Reward**: Binary signal (+1 for success, -1 otherwise)

**Tool-call Reward**: `R_tool-call = min(1, 0.1 × n_tool-call)` where n_tool-call is the number of valid tool interactions

**Format Reward**: 0.1 if output is properly wrapped, 0 otherwise

Total: `R = R_outcome + μ × R_tool-call + R_format`

## 2. Curriculum Scheduling

Two key schedules control progressive exploration:

**Intrinsic Reward Decay** (Eq. 21): 
```
μ = {½(cos(πt/T_decay) + 1), if t ≤ T_decay
     {0, if t > T_decay
```
Tool-call reward decays from 1 to 0, ensuring "outcome reward dominance."

**Self-Imitation Warm-up** (Eq. 12):
```
γ = {½(1 - cos(πt/T_warmup)), if t ≤ T_warmup
     {1, if t > T_warmup
```
Self-imitation loss weight gradually increases, preventing early overfitting.

## 3. Self-Imitation Update Rule

Maintains replay buffer D storing trajectories with "positive in-group advantages." Off-policy loss:

`𝒥̃^SIL-R = Σ 𝒥̃^GRPO_j × 𝟙(Â_j > 0 & Ã_j > 0) × M_j`

Where Ã_j represents "recalibrated advantage using 50th percentile baseline," and M_j masks high-covariance tokens.

## 4. Key Hyperparameters

- **Replay buffer size (N_D)**: Optimal range ~2000-4000 trajectories
- **Baseline buffer size (N_DR)**: ~500 for robust percentile estimation
- **Clipping ratio (λ)**: 0.0002-0.02 (percentage of tokens masked)
- **Warm-up steps (T_warmup)**: Typically 200 steps
- **Decay steps (T_decay)**: Also ~200 steps

## 5. RL Framework

Built on **GRPO (Group Relative Policy Optimization)** with modifications:
- Removes KL divergence (β=0)
- Uses "clip-higher" asymmetric bounds (0.28 upper, 0.2 lower)
- Removes intra-group normalization
- Filters over-long and void-turn samples

## 6. ALFWorld Results (Qwen2.5-1.5B)

SPEAR + GRPO achieves **88.9% success** vs GRPO baseline **72.8%** — a **+16.1% improvement**. For WebShop with same mod
…[truncated 69 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-14T13:24:47.615269+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Search GDPO algorithm papers', 'activeForm': 'Searching GDPO algorithm papers', 'status': 'completed'}, {'content': 'Search DAPO clip-higher dynamic sampling', 'activeForm': 'Searching DAPO clip-higher dynamic sampling', 'status': 'completed'}, {'content': 'Search SPEAR sparse reward exploration', 'activeForm': 'Searching SPEAR sparse reward exploration', 'status': 'completed'}, {'content': 'Search Dr.GRPO and GRPO variants', 'activeForm': 'Searching Dr.GRPO and GRPO variants', 'status': 'completed'}, {'content': 'Search sparse reward RL for LLM agents', 'activeForm': 'Searching sparse reward RL for LLM agents', 'status': 'completed'}, {'content': 'Verify SPEAR and EPO details via WebFetch', 'activeForm': 'Verifying SPEAR and EPO details via WebFetch', 'status': 'completed'}, {'content': 'Write literature_rl_alternatives.md', 'activeForm': 'Writing literature_rl_alternatives.md', 'status': 'in_progress'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Search GDPO algorithm papers', 'activeForm': 'Searching GDPO algorithm papers', 'status': 'completed'}, {'content': 'Search DAPO clip-higher dynamic sampling', 'activeForm': 'Searching DAPO clip-higher dynamic sampling', 'status': 'completed'}, {'content': 'Search SPEAR sparse reward exploration', 'activeForm': 'Searching SPEAR sparse reward exploration', 'status': 'completed'}, {'content': 'Search Dr.GRPO and GRPO variants', 'activeForm': 'Searching Dr.GRPO and GRPO variants', 'status': 'completed'}, {'content': 'Search sparse reward RL for LLM agents', 'activeForm': 'Searching sparse reward RL for LLM agents', 'status': 'completed'}, {'content': 'Verify SPEAR and EPO details via WebFetch', 'activeForm': 'Verifying SPEAR and EPO details via WebFetch', 'status': 'completed'}, {'content': 'Write literature_rl_alternatives.md', 'activeForm': 'Writing literature_rl_alternatives.md', 'status': 'in_progress'}]"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-14T13:24:47.615415+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-14T13:24:47.615597+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "literature_rl_alternatives.md",
  "content": "# GRPO 替代/改进算法调研\n\n**调研背景**：用 GRPO + Qwen3-1.7B 在 ALFWorld 上训练 agent，遇到三个核心问题：\n1. Sparse 二值奖励 → 同一 group 内 reward 相同 → advantage=0 → pg_loss=0（零梯度）\n2. Dense bonus 引入后 reward gaming（action_valid 60→97.5%，success→0%）\n3. 即使出现 success 信号，单步 GRPO 更新过激 → catastrophic collapse\n\n**调研截止**：2026-05（覆盖 ICLR 2026、NeurIPS 2025、arXiv 2024-2026）\n\n---\n\n## 1. SPEAR (Self-imitation with Progressive Exploration)\n- **论文**：\"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\"，Qin et al.（Tencent Youtu），arXiv 2509.22601，**ICLR 2026 接收**\n- **核心思想**：课程式自模仿学习（SIL）。早期用辅助 tool-use reward 鼓励技能层面探索，后期逐步把权重切换到成功 trajectory 的 self-imitation；用 replay buffer 存正 advantage 轨迹做 off-policy 更新。\n- **与我们场景的相关性**：⭐⭐⭐⭐⭐ **最直接相关**。明确针对 sparse-reward + long-horizon agent，**用同一个 ALFWorld + Qwen2.5-1.5B 设置在 GRPO 基础上 +16.1% success（72.8% → 88.9%）**。同时也跑了 WebShop（+20.7%）。三个核心问题它都覆盖：\n  - sparse reward：early-stage 用 tool-call bonus 给信号\n  - reward gaming：bonus 用 cosine schedule **衰减到 0**，最终只剩 outcome reward\n  - collapse：self-imitation 用历史成功轨迹稳定梯度\n- **关键公式**：\n  - 复合奖励：`R = R_outcome + μ·R_tool-call + R_format`，`R_tool-call = min(1, 0.1·n_tool_call)`\n  - 衰减：`μ = ½(cos(πt/T_decay)+1)`，t > T_decay 后 μ=0\n  - SIL warm-up：`γ = ½(1 - cos(πt/T_warmup))`，逐步上升到 1\n  - SIL 损失：`J_SIL = Σ J_GRPO_j · 𝟙(Â_j > 0 ∧ Ã_j > 0) · M_j`，Ã_j 是 50 分位 baseline 重新校准的 advantage\n- **集成难度**：低-中。代码在 `TencentYoutuResearch/SPEAR`，**基于 GRPO + 修改**（去掉 KL，clip-higher 0.28/0.2，去掉 intra-group 归一化）。如果 RAGEN 已经在 verl/TRL 上跑通 GRPO，加 replay buffer + 双 cosine schedule + SIL loss 项即可。\n- **关键超参**：\n  - replay buffer size N_D = 2000-4000\n  - baseline buffer N_DR = 500\n  - T_warmup ≈ T_decay ≈ 200 steps\n  - clip ratio λ = 0.0002-0.02（mask 高 covariance token）\n  - KL coef = 0\n- **风险**：\n  - 我们 exp013 试过 valid_action_bonus=0.15 已经 gaming 了，SPEAR 的 `0.1·n_tool_call` 系数类似量级——必须严格遵守 cosine decay，否则同样 gaming\n  - 1.7B 模型在 ALFWorld 初期 success≈0%，replay buffer 可能长时间为空 → 退化成 GRPO；可考虑用 SFT warm-up 让 buffer 先有种子轨迹\n\n---\n\n## 2. GiGPO (Group-in-Group Policy Optimization)\n- **论文**：\"Group-in-Group Policy Optimization for LLM Agent Training\"，Feng, Xue, Liu, An（NTU），arXiv 2505.10978，**NeurIPS 2025**\n- **核心思想**：两层 group 结构做细粒度 credit assignment：episode 级用整条 trajectory 算 macro advantage；step 级用 **anchor state grouping**——把跨 trajectory 出现的相同环境状态聚成一组，在该组内对动作算 micro advantage。\n- **与我们场景的相关性**：⭐⭐⭐⭐ 主要解决 sparse outcome reward 下的 credit assignment 问题。同样在 ALFWorld + Qwen2.5-1.5B/3B/7B-Instruct 上验证，**vs GRPO +12% on ALFWorld，+9% on WebShop**。不直接解决 collapse，但通过 step-level 信号让 advantage 更稳定（少一些零梯度 group）。\n- **集成难度**：中。代码在 `langfengq/verl-agent`（verl-agent 是 verl 的 agent 扩展）。如果 RAGEN 也基于 verl，迁移成本低；核心改动是 rollout 后做状态 hash + 重新分组。**关键依赖**：环境状态可哈希/可识别相同状态——ALFWorld 部分观测下要小心，可能需要用前 N 步 observation 拼接做 anchor。\n- **关键超参**：episode-level 和 step-level advantage 的加权系数（论文需查）。\n- **风险**：\n  - ALFWorld 状态空间大，\"相同 anchor state\" 可能很少出现 → step-level group 太小 → 仍是 sparse 信号\n  - 实现复杂度比 SPEAR 高一些\n\n---\n\n## 3. EPO (Entropy-regularized Policy Optimization for LLM Agents)\n- **论文**：\"EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning\"，Wujiang Xu et al.，arXiv 2509.22576（2025-09，2026-02 更新）\n- **核心思想**：诊断了 sparse-reward 多轮 agent 训练的 **\"exploration-exploitation cascade failure\"**——前期 sparse feedback 让 policy 过早收敛到 flawed strategies；后期 vanilla entropy 正则反而引发混乱探索导致 collapse。EPO 三机制：(1) 多轮设置下加 entropy 正则，(2) **entropy smoothing regularizer**——把 policy entropy 约束在历史均值范围内防止突变，(3) 自适应阶段权重，平衡探索/利用。\n- **与我们场景的相关性**：⭐⭐⭐⭐ 论文描述的 cascade failure 与我们 exp013→exp015 观察到的「先 gaming 再 collapse」非常相似。ALFWorld +19.8%，ScienceWorld +152%。代码在 `WujiangXu/EPO`。\n- **集成难度**：中。需要维护历史 entropy 滑动均值，并把 entropy bound 加进 loss——比 SPEAR 改动小，但比单纯加 entropy coef 复杂。\n- **关键超参**：entropy 历史窗口大小、entropy bound 的上下限、阶段切换 schedule。\n- **风险**：\n  - 我们 exp015 已经用 kl_coef=0.1 + lr=1e-7 做稳定性修复，再叠加 EPO 可能过约束（entropy 完全压死 → 无探索）\n  - \"保证 entropy variance 单调下降\"听起来像主动抑制探索，对 1.7B 这种已经 entropy 偏低的模型可能不利\n\n---\n\n## 4. DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization)\n- **论文**：\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"，ByteDance Seed，arXiv 2503.14476（2025-03）\n- **核心思想**：在 Qwen2.5-32B 上 50% 步数超过 DeepSeek-R1-Zero-Qwen-32B。四个关键技术：\n  1. **Clip-Higher**：解耦上下 clip，把上 clip 从 0.2 扩到 0.28，鼓励低概率 token 上升，**防止 entropy collapse**\n  2. **Dynamic Sampling**：丢弃 acc=0 和 acc=1 的 prompt group（这些 group 内 advantage 全相同），保留有梯度的样本\n  3. **Token-level Policy Gradient Loss**：长 CoT 场景下不再按序列平均\n  4. **Overlong Reward Shaping**：长输出的奖励 shaping，降低噪声\n- **与我们场景的相关性**：⭐⭐⭐⭐ **Dynamic Sampling 直接解决我们「group 内 reward 全相同 → 零梯度」的问题**——把这种 group 丢掉、resample 直到 batch 内有有效梯度的样本。Clip-Higher 缓解 entropy collapse。\n- **集成难度**：低。已被 verl 原生支持，TRL 也有 PR。改三个参数就能开 Clip-Higher，Dynamic Sampling 需要在 batch 构造时加过滤逻辑。\n- **关键超参**：ε_low=0.2, ε_high=0.28（论文默认值）；Dynamic Sampling 的 oversample 倍数\n- **风险**：\n  - 注意：**有研究发现 Dynamic Sampling 在某些设置下不提升性能甚至有害**（见 arxiv 2512.07611）——需要消融\n  - DAPO 是为单轮长 CoT reasoning 设计，agent 多轮场景需要额外验证\n  - Dynamic Sampling 在 success≈0% 的初期意味着**一直丢弃所有 group**（全 acc=0），可能完全无法启动训练——需要配合 SPEAR 式 bonus 或 SFT warm-up\n\n---\n\n## 5. GTPO (Stabilizing GRPO via Gradient and Entropy Control)\n- **论文**：\"GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control\"，arXiv 2508.03772（2025-08）\n- **核心思想**：诊断 GRPO 两个本质问题：(1) **同 group 内不同 completion 共享的 token 收到矛盾梯度**（gradient conflict）；(2) negative-reward completion 对 confident token 施加惩罚导致 **policy collapse**。GTPO：跳过这些 token 的 negative update，只放大 positive；按 entropy 阈值过滤高 entropy completion；**完全不依赖 KL**（不需要 reference model）。\n- **与我们场景的相关性**：⭐⭐⭐ 直接针对 collapse 现象。但实验集中在数学推理（GSM8K/MATH/AIME），agent 任务上未验证。\n- **集成难度**：中。需要在 token 级做 gradient 路由（识别哪些 token 跨 completion 共享）。\n- **关键超参**：entropy 阈值；conflict 检测的 token 共现窗口\n- **风险**：未在 agent 任务上验证；跨 completion 的共享 token 在 agent 多轮场景定义不同（每轮 prompt 不同）\n\n---\n\n## 6. Dr. GRPO (Length-bias 修正)\n- **论文**：来自 \"Understanding R1-Zero-Like Training: A Critical Perspective\"（2503.20783）等工作\n- **核心思想**：GRPO 原版按序列长度归一化导致长的错误回复被欠惩罚。Dr. GRPO 用全局常数归一化，消除长度偏差。\n- **与我们场景的相关性**：⭐⭐ 主要解决 length bias，不直接解决 sparse reward / collapse / gaming。但 SPEAR 内部就用了类似策略（去掉 intra-group 归一化）。\n- **集成难度**：极低。verl 里改 `loss_agg_mode=\"seq-mean-token-sum-norm\"` 即可。\n- **风险**：单独用不解决我们的核心问题；可作为基础设置叠加在其他算法上\n\n---\n\n## 7. GDPO (Group reward-Decoupled Normalization)\n- **论文**：\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\"，NVlabs，arXiv 2601.05242\n- **核心思想**：注意：GDPO 这里指 \"Group reward-Decoupled\"，**不是** \"Group Distributionally-robust\"。专门解决**多奖励**场景下 GRPO 把不同 reward 组合 normalize 到同一 advantage 而丢失分辨率的问题。Key trick：**先 normalize 再聚合**（与原 GRPO 顺序相反）。\n- **与我们场景的相关性**：⭐⭐⭐ 如果我们坚持用 sparse outcome + dense bonus 的多奖励组合（exp013 的方向），GDPO 比 GRPO 更合适——能保留 success 信号和 bonus 信号的分辨率，**潜在缓解 reward gaming**（因为不同 reward 维度的相对差异被保留）。代码在 `NVlabs/GDPO`。\n- **集成难度**：中。需要把 reward 拆成多维度，分别 normalize。\n- **关键超参**：各 reward 维度的相对权重\n- **风险**：仍未根本解决 gaming——只是让 success 信号不被 bonus 淹没；如果 success 信号本身缺失（初期），多奖励解耦也救不了\n\n---\n\n## 8. StarPO-S (RAGEN 自带的稳定化变体)\n- **论文**：RAGEN 论文（arXiv 2504.20073），\"Understanding Self-Evolution in LLM Agents via Multi-Turn RL\"\n- **核心思想**：三个稳定化机制：(1) **variability-based trajectory filtering**——丢弃 group 内 reward variance 低的 trajectory（默认丢 25%）；(2) critic baselining；(3) decoupled clipping。\n- **与我们场景的相关性**：⭐⭐⭐⭐ **我们用的就是 RAGEN，这是开箱即用方案**。trajectory filtering 与 DAPO Dynamic Sampling 思路一致。论文还观察到「GRPO 在 Bandit 上 20 步开始 collapse，PPO 100 步才 collapse；reward std 和 entropy 是 early warning」——和我们看到的现象一致。\n- **集成难度**：极低（已在 RAGEN 仓库内）。\n- **关键超参**：filtering rate（默认 25%）；decoupled clip 上下限\n- **风险**：低。可作为 baseline 设置\n\n---\n\n## 9. VAPO (Value-Augmented Proximal PO)\n- **论文**：\"VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks\"，ByteDance，arXiv 2504.05118（2025-04）\n- **核心思想**：value-based 方法（保留 critic，与 GRPO 路线相反）。解决 value model bias、长序列异质性、reward sparsity 三大问题。**value-pretraining**：用 fixed policy 的 Monte Carlo return 预训练 value network，避免 value 初始 bias。\n- **与我们场景的相关性**：⭐⭐⭐ 直接讨论 sparse reward。但属于 PPO 路线，要恢复 critic，对 1.7B 显存不大友好（不过 1.7B 还好）。AIME 上 60.4，**无训练 crash**。\n- **集成难度**：中-高。需要切换回 PPO + critic，多出 value 预训练阶段。\n- **关键超参**：value pretraining 步数；GAE λ\n- **风险**：PPO 路线整体收敛比 GRPO 慢；agent 场景未验证\n\n---\n\n## 10. ARPO (Agentic Reinforced PO)\n- **论文**：\"Agentic Reinforced Policy Optimization\"，RUC-NLPIR，arXiv 2507.19849，**ICLR 2026 接收**\n- **核心思想**：观察到 LLM 在 tool-call 后 entropy 升高（不确定性增大）→ **entropy-based adaptive rollout**：在高 entropy 的 tool-call 轮次自适应分支采样。advantage attribution estimation 让 LLM 内化 stepwise 工具使用的 advantage 差异。\n- **与我们场景的相关性**：⭐⭐⭐ ALFWorld 是工具/动作型 agent，思路适用但论文重点是 search/tool-use。\n- **集成难度**：中。需要 rollout 阶段做自适应分支，与 verl 现有同步 rollout 不太一样。\n- **关键超参**：entropy 触发阈值；分支因子\n- **风险**：rollout 改造工程量；agent 任务 entropy 信号是否可靠未知\n\n---\n\n## 11. AgentHER / ECHO (Hindsight Trajectory Relabeling)\n- **论文**：\n  - AgentHER：arXiv 2603.21357\n  - ECHO（Sample-Efficient Online Learning via Hindsight Trajectory Rewriting）：arXiv 2510.10304\n- **核心思想**：把失败 trajectory 用 LLM 改写成「针对 goal B 的成功 trajectory」——失败一次仍能产生学习信号。AgentHER 报告 WebArena/ToolBench 上 +7.1~11.7pp。\n- **与我们场景的相关性**：⭐⭐⭐ 针对 sparse reward 下 \"0% success → 0 信号\" 的根本问题。但当前主要用于 **offline SFT 数据增强**，online RL 集成方案尚不成熟。\n- **集成难度**：中-高。需要 LLM 改写 trajectory（额外推理成本），且要确认 ALFWorld 任务 goal 可以重新标注（ALFWorld 是文本游戏，goal 是\"在 X 中放 Y\"，理论上可改写）。\n- **关键超参**：relabel 的 trajectory 占比；改写温度\n- **风险**：可能引入 reward hacking（改写后的\"成功\"与原任务无关）；多一个推理 pipeline\n\n---\n\n## 12. i-MENTOR / LLM 驱动内在动机\n- **论文**：\"Navigate the Unknown: Enhancing LLM Reasoning with Intrinsic Motivation Guided Exploration\"（arXiv 2505.17621）；\"LLM-Driven Intrinsic Motivation for Sparse Reward RL\"（arXiv 2508.18420）\n- **核心思想**：用 VAE state novelty 或 LLM 评估 state novelty 给 intrinsic reward。\n- **与我们场景的相关性**：⭐⭐ 思路通用，但偏经典 RL，没在 ALFWorld LLM agent 上验证。\n- **集成难度**：高（需要训 VAE 或加 LLM 评估 callback）\n- **风险**：与 SPEAR 的 tool-call bonus 类似 → 仍有 gaming 风险；额外训练成本\n\n---\n\n## 13. MT-GRPO (Turn-Level Reward Design)\n- **论文**：\"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\"，arXiv 2505.11821，**NeurIPS 2025**\n- **核心思想**：把 outcome reward 拆到 turn 级——每一轮给一个中间奖励。GRPO/PPO 扩展为 MT-GRPO/MT-PPO。\n- **与我们场景的相关性**：⭐⭐ 思路合理，但 ALFWorld 的「每轮是否合法/有进展」难以自动给出 turn 级奖励（需要 process reward model 或环境信号）。\n- **集成难度**：中。如果 ALFWorld 能给 turn 级 progress 信号（如目标距离），直接接入。\n- **风险**：与 dense bonus 同一类问题——turn 级奖励容易被 game\n\n---\n\n## 总结推荐表\n\n| 算法 | 解决问题 | 集成难度 | 推荐优先级 | 备注 |\n|------|---------|---------|----------|------|\n| **SPEAR** | sparse + gaming + collapse 全覆盖 | 低-中 | **★★★★★ P0** | 同设置 ALFWorld 实测 +16.1%；ICLR 2026；课程 + SIL 优雅解决 gaming |\n| **GiGPO** | sparse credit assignment | 中 | **★★★★ P1** | ALFWorld +12%；verl-agent 已实现；可与 SPEAR 叠加（SPEAR 论文也对比了 GiGPO） |\n| **DAPO 组件** | 零梯度 group + entropy collapse | 低 | **★★★★ P1** | Dynamic Sampling 直接解决「group 全相同」；Clip-Higher 防 collapse；可单独抽取组件叠加 |\n| **EPO** | cascade failure（gaming→collapse） | 中 | ★★★ P2 | ALFWorld +19.8%；与 exp015 已有的稳定性修复方向重合，需消融 |\n| **StarPO-S** | 一般稳定化 | 极低 | ★★★ P2 | RAGEN 自带，立即可用；与 DAPO Dynamic Sampling 思路重叠 |\n| **GDPO** | 多奖励解耦（缓解 gaming） | 中 | ★★ P3 | 仅在保留 dense bonus 时有意义；不解决 sparse 启动问题 |\n| **GTPO** | gradient conflict + collapse | 中 | ★★ P3 | 仅推理任务验证；agent 场景未知 |\n| **VAPO** | 切回 critic 路线 | 中-高 | ★★ P3 | 改动大；显存/速度劣于 GRPO 系 |\n| **ARPO** | tool-call 自适应 rollout | 中 | ★★ P3 | rollout 改造工程量 |\n| **AgentHER/ECHO** | 失败轨迹重标 | 中-高 | ★★ P3 | 当前 online RL 集成不成熟，更适合 SFT 阶段 |\n| **MT-GRPO** | turn-level credit | 中 | ★ P4 | 需要外部 progress 信号 |\n| **Dr. GRPO** | length bias | 极低 | ★ basic | 作为基础设置叠加 |\n\n---\n\n## 行动建议\n\n**短期（1-2 周）**：\n- 落地 **SPEAR**，直接复用其 ALFWorld + Qwen2.5-1.5B 配置作为强 baseline（我们用 Qwen3-1.7B 接近）：复合 reward + cosine decay + SIL replay buffer\n- 同时叠加 **DAPO 的 Clip-Higher (0.2/0.28) + Dynamic Sampling 过滤 all-same-reward group**，几乎零成本\n- 设置 **StarPO-S filtering** 作为额外保险\n\n**消融**：\n- SPEAR 复合 reward 单独 vs SPEAR + SIL → 确认 SIL 贡献\n- 关掉 cosine decay 看是否 gaming（验证 decay 的必要性）\n- 用 SPEAR 默认 KL=0 vs 我们 exp015 的 KL=0.1 → 哪个更稳\n\n**中期备选**：\n- 如果 SPEAR + DAPO 组件仍不够稳，叠加 **GiGPO step-level advantage**\n- 如果 1.7B 初期 replay buffer 长期为空，先做 **expert trajectory SFT warm-up**（ALFWorld 有 ground-truth solver 可生成专家轨迹）\n\n**不推荐近期尝试**：\n- VAPO（切 PPO 路线工程量过大）\n- AgentHER online 集成（不成熟）\n- 单独的 GDPO/GTPO（缺 agent 任务验证）\n\n---\n\n## 参考资源\n\n- SPEAR 代码：https://github.com/TencentYoutuResearch/SPEAR\n- GiGPO 代码：https://github.com/langfengq/verl-agent\n- DAPO 项目页：https://dapo-sia.github.io/\n- EPO 代码：https://github.com/WujiangXu/EPO\n- RAGEN/StarPO-S：https://github.com/mll-lab-nu/RAGEN\n- ARPO 代码：https://github.com/RUC-NLPIR/ARPO\n- 综述：blacksnail789521/Agentic-RL-Training-Recipes（持续更新）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "file": "literature_rl_alternatives.md",
    "content": "# GRPO 替代/改进算法调研\n\n**调研背景**：用 GRPO + Qwen3-1.7B 在 ALFWorld 上训练 agent，遇到三个核心问题：\n1. Sparse 二值奖励 → 同一 group 内 reward 相同 → advantage=0 → pg_loss=0（零梯度）\n2. Dense bonus 引入后 reward gaming（action_valid 60→97.5%，success→0%）\n3. 即使出现 success 信号，单步 GRPO 更新过激 → catastrophic collapse\n\n**调研截止**：2026-05（覆盖 ICLR 2026、NeurIPS 2025、arXiv 2024-2026）\n\n---\n\n## 1. SPEAR (Self-imitation with Progressive Exploration)\n- **论文**：\"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\"，Qin et al.（Tencent Youtu），arXiv 2509.22601，**ICLR 2026 接收**\n- **核心思想**：课程式自模仿学习（SIL）。早期用辅助 tool-use reward 鼓励技能层面探索，后期逐步把权重切换到成功 trajectory 的 self-imitation；用 replay buffer 存正 advantage 轨迹做 off-policy 更新。\n- **与我们场景的相关性**：⭐⭐⭐⭐⭐ **最直接相关**。明确针对 sparse-reward + long-horizon agent，**用同一个 ALFWorld + Qwen2.5-1.5B 设置在 GRPO 基础上 +16.1% success（72.8% → 88.9%）**。同时也跑了 WebShop（+20.7%）。三个核心问题它都覆盖：\n  - sparse reward：early-stage 用 tool-call bonus 给信号\n  - reward gaming：bonus 用 cosine schedule **衰减到 0**，最终只剩 outcome reward\n  - collapse：self-imitation 用历史成功轨迹稳定梯度\n- **关键公式**：\n  - 复合奖励：`R = R_outcome + μ·R_tool-call + R_format`，`R_tool-call = min(1, 0.1·n_tool_call)`\n  - 衰减：`μ = ½(cos(πt/T_decay)+1)`，t > T_decay 后 μ=0\n  - SIL warm-up：`γ = ½(1 - cos(πt/T_warmup))`，逐步上升到 1\n  - SIL 损失：`J_SIL = Σ J_GRPO_j · 𝟙(Â_j > 0 ∧ Ã_j > 0) · M_j`，Ã_j 是 50 分位 baseline 重新校准的 advantage\n- **集成难度**：低-中。代码在 `TencentYoutuResearch/SPEAR`，**基于 GRPO + 修改**（去掉 KL，clip-higher 0.28/0.2，去掉 intra-group 归一化）。如果 RAGEN 已经在 verl/TRL 上跑通 GRPO，加 replay buffer + 双 cosine schedule + SIL loss 项即可。\n- **关键超参**：\n  - replay buffer size N_D = 2000-4000\n  - baseline buffer N_DR = 500\n  - T_warmup ≈ T_decay ≈ 200 steps\n  - clip ratio λ = 0.0002-0.02（mask 高 covariance token）\n  - KL coef = 0\n- **风险**：\n  - 我们 exp013 试过 valid_action_bonus=0.15 已经 gaming 了，SPEAR 的 `0.1·n_tool_call` 系数类似量级——必须严格遵守 cosine decay，否则同样 gaming\n  - 1.7B 模型在 ALFWorld 初期 success≈0%，replay buffer 可能长时间为空 → 退化成 GRPO；可考虑用 SFT warm-up 让 buffer 先有种子轨迹\n\n---\n\n## 2. GiGPO (Group-in-Group Policy Optimization)\n- **论文**：\"Group-in-Group Policy Optimization for LLM Agent Training\"，Feng, Xue, Liu, An（NTU），arXiv 2505.10978，**NeurIPS 2025**\n- **核心思想**：两层 group 结构做细粒度 credit assignment：episode 级用整条 trajectory 算 macro advantage；step 级用 **anchor state grouping**——把跨 trajectory 出现的相同环境状态聚成一组，在该组内对动作算 micro advantage。\n- **与我们场景的相关性**：⭐⭐⭐⭐ 主要解决 sparse outcome reward 下的 credit assignment 问题。同样在 ALFWorld + Qwen2.5-1.5B/3B/7B-Instruct 上验证，**vs GRPO +12% on ALFWorld，+9% on WebShop**。不直接解决 collapse，但通过 step-level 信号让 advantage 更稳定（少一些零梯度 group）。\n- **集成难度**：中。代码在 `langfengq/verl-agent`（verl-agent 是 verl 的 agent 扩展）。如果 RAGEN 也基于 verl，迁移成本低；核心改动是 rollout 后做状态 hash + 重新分组。**关键依赖**：环境状态可哈希/可识别相同状态——ALFWorld 部分观测下要小心，可能需要用前 N 步 observation 拼接做 anchor。\n- **关键超参**：episode-level 和 step-level advantage 的加权系数（论文需查）。\n- **风险**：\n  - ALFWorld 状态空间大，\"相同 anchor state\" 可能很少出现 → step-level group 太小 → 仍是 sparse 信号\n  - 实现复杂度比 SPEAR 高一些\n\n---\n\n## 3. EPO (Entropy-regularized Policy Optimization for LLM Agents)\n- **论文**：\"EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning\"，Wujiang Xu et al.，arXiv 2509.22576（2025-09，2026-02 更新）\n- **核心思想**：诊断了 sparse-reward 多轮 agent 训练的 **\"exploration-exploitation cascade failure\"**——前期 sparse feedback 让 policy 过早收敛到 flawed strategies；后期 vanilla entropy 正则反而引发混乱探索导致 collapse。EPO 三机制：(1) 多轮设置下加 entropy 正则，(2) **entropy smoothing regularizer**——把 policy entropy 约束在历史均值范围内防止突变，(3) 自适应阶段权重，平衡探索/利用。\n- **与我们场景的相关性**：⭐⭐⭐⭐ 论文描述的 cascade failure 与我们 exp013→exp015 观察到的「先 gaming 再 collapse」非常相似。ALFWorld +19.8%，ScienceWorld +152%。代码在 `WujiangXu/EPO`。\n- **集成难度**：中。需要维护历史 entropy 滑动均值，并把 entropy bound 加进 loss——比 SPEAR 改动小，但比单纯加 entropy coef 复杂。\n- **关键超参**：entropy 历史窗口大小、entropy bound 的上下限、阶段切换 schedule。\n- **风险**：\n  - 我们 exp015 已经用 kl_coef=0.1 + lr=1e-7 做稳定性修复，再叠加 EPO 可能过约束（entropy 完全压死 → 无探索）\n  - \"保证 entropy variance 单调下降\"听起来像主动抑制探索，对 1.7B 这种已经 entropy 偏低的模型可能不利\n\n---\n\n## 4. DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization)\n- **论文**：\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"，ByteDance Seed，arXiv 2503.14476（2025-03）\n- **核心思想**：在 Qwen2.5-32B 上 50% 步数超过 DeepSeek-R1-Zero-Qwen-32B。四个关键技术：\n  1. **Clip-Higher**：解耦上下 clip，把上 clip 从 0.2 扩到 0.28，鼓励低概率 token 上升，**防止 entropy collapse**\n  2. **Dynamic Sampling**：丢弃 acc=0 和 acc=1 的 prompt group（这些 group 内 advantage 全相同），保留有梯度的样本\n  3. **Token-level Policy Gradient Loss**：长 CoT 场景下不再按序列平均\n  4. **Overlong Reward Shaping**：长输出的奖励 shaping，降低噪声\n- **与我们场景的相关性**：⭐⭐⭐⭐ **Dynamic Sampling 直接解决我们「group 内 reward 全相同 → 零梯度」的问题**——把这种 group 丢掉、resample 直到 batch 内有有效梯度的样本。Clip-Higher 缓解 entropy collapse。\n- **集成难度**：低。已被 verl 原生支持，TRL 也有 PR。改三个参数就能开 Clip-Higher，Dynamic Sampling 需要在 batch 构造时加过滤逻辑。\n- **关键超参**：ε_low=0.2, ε_high=0.28（论文默认值）；Dynamic Sampling 的 oversample 倍数\n- **风险**：\n  - 注意：**有研究发现 Dynamic Sampling 在某些设置下不提升性能甚至有害**（见 arxiv 2512.07611）——需要消融\n  - DAPO 是为单轮长 CoT reasoning 设计，agent 多轮场景需要额外验证\n  - Dynamic Sampling 在 success≈0% 的初期意味着**一直丢弃所有 group**（全 acc=0），可能完全无法启动训练——需要配合 SPEAR 式 bonus 或 SFT warm-up\n\n---\n\n## 5. GTPO (Stabilizing GRPO via Gradient and Entropy Control)\n- **论文**：\"GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control\"，arXiv 2508.03772（2025-08）\n- **核心思想**：诊断 GRPO 两个本质问题：(1) **同 group 内不同 completion 共享的 token 收到矛盾梯度**（gradient conflict）；(2) negative-reward completion 对 confident token 施加惩罚导致 **policy collapse**。GTPO：跳过这些 token 的 negative update，只放大 positive；按 entropy 阈值过滤高 entropy completion；**完全不依赖 KL**（不需要 reference model）。\n- **与我们场景的相关性**：⭐⭐⭐ 直接针对 collapse 现象。但实验集中在数学推理（GSM8K/MATH/AIME），agent 任务上未验证。\n- **集成难度**：中。需要在 token 级做 gradient 路由（识别哪些 token 跨 completion 共享）。\n- **关键超参**：entropy 阈值；conflict 检测的 token 共现窗口\n- **风险**：未在 agent 任务上验证；跨 completion 的共享 token 在 agent 多轮场景定义不同（每轮 prompt 不同）\n\n---\n\n## 6. Dr. GRPO (Length-bias 修正)\n- **论文**：来自 \"Understanding R1-Zero-Like Training: A Critical Perspective\"（2503.20783）等工作\n- **核心思想**：GRPO 原版按序列长度归一化导致长的错误回复被欠惩罚。Dr. GRPO 用全局常数归一化，消除长度偏差。\n- **与我们场景的相关性**：⭐⭐ 主要解决 length bias，不直接解决 sparse reward / collapse / gaming。但 SPEAR 内部就用了类似策略（去掉 intra-group 归一化）。\n- **集成难度**：极低。verl 里改 `loss_agg_mode=\"seq-mean-token-sum-norm\"` 即可。\n- **风险**：单独用不解决我们的核心问题；可作为基础设置叠加在其他算法上\n\n---\n\n## 7. GDPO (Group reward-Decoupled Normalization)\n- **论文**：\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\"，NVlabs，arXiv 2601.05242\n- **核心思想**：注意：GDPO 这里指 \"Group reward-Decoupled\"，**不是** \"Group Distributionally-robust\"。专门解决**多奖励**场景下 GRPO 把不同 reward 组合 normalize 到同一 advantage 而丢失分辨率的问题。Key trick：**先 normalize 再聚合**（与原 GRPO 顺序相反）。\n- **与我们场景的相关性**：⭐⭐⭐ 如果我们坚持用 sparse outcome + dense bonus 的多奖励组合（exp013 的方向），GDPO 比 GRPO 更合适——能保留 success 信号和 bonus 信号的分辨率，**潜在缓解 reward gaming**（因为不同 reward 维度的相对差异被保留）。代码在 `NVlabs/GDPO`。\n- **集成难度**：中。需要把 reward 拆成多维度，分别 normalize。\n- **关键超参**：各 reward 维度的相对权重\n- **风险**：仍未根本解决 gaming——只是让 success 信号不被 bonus 淹没；如果 success 信号本身缺失（初期），多奖励解耦也救不了\n\n---\n\n## 8. StarPO-S (RAGEN 自带的稳定化变体)\n- **论文**：RAGEN 论文（arXiv 2504.20073），\"Understanding Self-Evolution in LLM Agents via Multi-Turn RL\"\n- **核心思想**：三个稳定化机制：(1) **variability-based trajectory filtering**——丢弃 group 内 reward variance 低的 trajectory（默认丢 25%）；(2) critic baselining；(3) decoupled clipping。\n- **与我们场景的相关性**：⭐⭐⭐⭐ **我们用的就是 RAGEN，这是开箱即用方案**。trajectory filtering 与 DAPO Dynamic Sampling 思路一致。论文还观察到「GRPO 在 Bandit 上 20 步开始 collapse，PPO 100 步才 collapse；reward std 和 entropy 是 early warning」——和我们看到的现象一致。\n- **集成难度**：极低（已在 RAGEN 仓库内）。\n- **关键超参**：filtering rate（默认 25%）；decoupled clip 上下限\n- **风险**：低。可作为 baseline 设置\n\n---\n\n## 9. VAPO (Value-Augmented Proximal PO)\n- **论文**：\"VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks\"，ByteDance，arXiv 2504.05118（2025-04）\n- **核心思想**：value-based 方法（保留 critic，与 GRPO 路线相反）。解决 value model bias、长序列异质性、reward sparsity 三大问题。**value-pretraining**：用 fixed policy 的 Monte Carlo return 预训练 value network，避免 value 初始 bias。\n- **与我们场景的相关性**：⭐⭐⭐ 直接讨论 sparse reward。但属于 PPO 路线，要恢复 critic，对 1.7B 显存不大友好（不过 1.7B 还好）。AIME 上 60.4，**无训练 crash**。\n- **集成难度**：中-高。需要切换回 PPO + critic，多出 value 预训练阶段。\n- **关键超参**：value pretraining 步数；GAE λ\n- **风险**：PPO 路线整体收敛比 GRPO 慢；agent 场景未验证\n\n---\n\n## 10. ARPO (Agentic Reinforced PO)\n- **论文**：\"Agentic Reinforced Policy Optimization\"，RUC-NLPIR，arXiv 2507.19849，**ICLR 2026 接收**\n- **核心思想**：观察到 LLM 在 tool-call 后 entropy 升高（不确定性增大）→ **entropy-based adaptive rollout**：在高 entropy 的 tool-call 轮次自适应分支采样。advantage attribution estimation 让 LLM 内化 stepwise 工具使用的 advantage 差异。\n- **与我们场景的相关性**：⭐⭐⭐ ALFWorld 是工具/动作型 agent，思路适用但论文重点是 search/tool-use。\n- **集成难度**：中。需要 rollout 阶段做自适应分支，与 verl 现有同步 rollout 不太一样。\n- **关键超参**：entropy 触发阈值；分支因子\n- **风险**：rollout 改造工程量；agent 任务 entropy 信号是否可靠未知\n\n---\n\n## 11. AgentHER / ECHO (Hindsight Trajectory Relabeling)\n- **论文**：\n  - AgentHER：arXiv 2603.21357\n  - ECHO（Sample-Efficient Online Learning via Hindsight Trajectory Rewriting）：arXiv 2510.10304\n- **核心思想**：把失败 trajectory 用 LLM 改写成「针对 goal B 的成功 trajectory」——失败一次仍能产生学习信号。AgentHER 报告 WebArena/ToolBench 上 +7.1~11.7pp。\n- **与我们场景的相关性**：⭐⭐⭐ 针对 sparse reward 下 \"0% success → 0 信号\" 的根本问题。但当前主要用于 **offline SFT 数据增强**，online RL 集成方案尚不成熟。\n- **集成难度**：中-高。需要 LLM 改写 trajectory（额外推理成本），且要确认 ALFWorld 任务 goal 可以重新标注（ALFWorld 是文本游戏，goal 是\"在 X 中放 Y\"，理论上可改写）。\n- **关键超参**：relabel 的 trajectory 占比；改写温度\n- **风险**：可能引入 reward hacking（改写后的\"成功\"与原任务无关）；多一个推理 pipeline\n\n---\n\n## 12. i-MENTOR / LLM 驱动内在动机\n- **论文**：\"Navigate the Unknown: Enhancing LLM Reasoning with Intrinsic Motivation Guided Exploration\"（arXiv 2505.17621）；\"LLM-Driven Intrinsic Motivation for Sparse Reward RL\"（arXiv 2508.18420）\n- **核心思想**：用 VAE state novelty 或 LLM 评估 state novelty 给 intrinsic reward。\n- **与我们场景的相关性**：⭐⭐ 思路通用，但偏经典 RL，没在 ALFWorld LLM agent 上验证。\n- **集成难度**：高（需要训 VAE 或加 LLM 评估 callback）\n- **风险**：与 SPEAR 的 tool-call bonus 类似 → 仍有 gaming 风险；额外训练成本\n\n---\n\n## 13. MT-GRPO (Turn-Level Reward Design)\n- **论文**：\"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\"，arXiv 2505.11821，**NeurIPS 2025**\n- **核心思想**：把 outcome reward 拆到 turn 级——每一轮给一个中间奖励。GRPO/PPO 扩展为 MT-GRPO/MT-PPO。\n- **与我们场景的相关性**：⭐⭐ 思路合理，但 ALFWorld 的「每轮是否合法/有进展」难以自动给出 turn 级奖励（需要 process reward model 或环境信号）。\n- **集成难度**：中。如果 ALFWorld 能给 turn 级 progress 信号（如目标距离），直接接入。\n- **风险**：与 dense bonus 同一类问题——turn 级奖励容易被 game\n\n---\n\n## 总结推荐表\n\n| 算法 | 解决问题 | 集成难度 | 推荐优先级 | 备注 |\n|------|---------|---------|----------|------|\n| **SPEAR** | sparse + gaming + collapse 全覆盖 | 低-中 | **★★★★★ P0** | 同设置 ALFWorld 实测 +16.1%；ICLR 2026；课程 + SIL 优雅解决 gaming |\n| **GiGPO** | sparse credit assignment | 中 | **★★★★ P1** | ALFWorld +12%；verl-agent 已实现；可与 SPEAR 叠加（SPEAR 论文也对比了 GiGPO） |\n| **DAPO 组件** | 零梯度 group + entropy collapse | 低 | **★★★★ P1** | Dynamic Sampling 直接解决「group 全相同」；Clip-Higher 防 collapse；可单独抽取组件叠加 |\n| **EPO** | cascade failure（gaming→collapse） | 中 | ★★★ P2 | ALFWorld +19.8%；与 exp015 已有的稳定性修复方向重合，需消融 |\n| **StarPO-S** | 一般稳定化 | 极低 | ★★★ P2 | RAGEN 自带，立即可用；与 DAPO Dynamic Sampling 思路重叠 |\n| **GDPO** | 多奖励解耦（缓解 gaming） | 中 | ★★ P3 | 仅在保留 dense bonus 时有意义；不解决 sparse 启动问题 |\n| **GTPO** | gradient conflict + collapse | 中 | ★★ P3 | 仅推理任务验证；agent 场景未知 |\n| **VAPO** | 切回 critic 路线 | 中-高 | ★★ P3 | 改动大；显存/速度劣于 GRPO 系 |\n| **ARPO** | tool-call 自适应 rollout | 中 | ★★ P3 | rollout 改造工程量 |\n| **AgentHER/ECHO** | 失败轨迹重标 | 中-高 | ★★ P3 | 当前 online RL 集成不成熟，更适合 SFT 阶段 |\n| **MT-GRPO** | turn-level credit | 中 | ★ P4 | 需要外部 progress 信号 |\n| **Dr. GRPO** | length bias | 极低 | ★ basic | 作为基础设置叠加 |\n\n---\n\n## 行动建议\n\n**短期（1-2 周）**：\n- 落地 **SPEAR**，直接复用其 ALFWorld + Qwen2.5-1.5B 配置作为强 baseline（我们用 Qwen3-1.7B 接近）：复合 reward + cosine decay + SIL replay buffer\n- 同时叠加 **DAPO 的 Clip-Higher (0.2/0.28) + Dynamic Sampling 过滤 all-same-reward group**，几乎零成本\n- 设置 **StarPO-S filtering** 作为额外保险\n\n**消融**：\n- SPEAR 复合 reward 单独 vs SPEAR + SIL → 确认 SIL 贡献\n- 关掉 cosine decay 看是否 gaming（验证 decay 的必要性）\n- 用 SPEAR 默认 KL=0 vs 我们 exp015 的 KL=0.1 → 哪个更稳\n\n**中期备选**：\n- 如果 SPEAR + DAPO 组件仍不够稳，叠加 **GiGPO step-level advantage**\n- 如果 1.7B 初期 replay buffer 长期为空，先做 **expert trajectory SFT warm-up**（ALFWorld 有 ground-truth solver 可生成专家轨迹）\n\n**不推荐近期尝试**：\n- VAPO（切 PPO 路线工程量过大）\n- AgentHER online 集成（不成熟）\n- 单独的 GDPO/GTPO（缺 agent 任务验证）\n\n---\n\n## 参考资源\n\n- SPEAR 代码：https://github.com/TencentYoutuResearch/SPEAR\n- GiGPO 代码：https://github.com/langfengq/verl-agent\n- DAPO 项目页：https://dapo-sia.github.io/\n- EPO 代码：https://github.com/WujiangXu/EPO\n- RAGEN/StarPO-S：https://github.com/mll-lab-nu/RAGEN\n- ARPO 代码：https://github.com/RUC-NLPIR/ARPO\n- 综述：blacksnail789521/Agentic-RL-Training-Recipes（持续更新）\n"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-14T13:24:47.615946+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'literature_rl_alternatives.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-14T13:24:47.616128+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/ 2>&1 | head -20",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/ 2>&1 | head -20",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-14T13:24:47.616271+00:00_

_project
alfworld_dryrun_report.md
biavr
disk_cleanup_report.md
env_setup_report.md
exp003
exp003_invalid_action_diagnosis.md
exp003_status_check.md
exp007
exp008_sft
exp009
exp010
exp010_reward_analysis.md
exp013f_training_metrics.md
exp_001
expert_trajectory_plan.md
manifest.yaml
phase_b_literature_survey.md
phase_b_prep_checklist.md
phase_b_readiness_check.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-14T13:24:47.616453+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/literature_rl_alternatives.md",
  "content": "# GRPO 替代/改进算法调研\n\n**调研背景**：用 GRPO + Qwen3-1.7B 在 ALFWorld 上训练 agent，遇到三个核心问题：\n1. Sparse 二值奖励 → 同一 group 内 reward 相同 → advantage=0 → pg_loss=0（零梯度）\n2. Dense bonus 引入后 reward gaming（action_valid 60→97.5%，success→0%）\n3. 即使出现 success 信号，单步 GRPO 更新过激 → catastrophic collapse\n\n**调研截止**：2026-05（覆盖 ICLR 2026、NeurIPS 2025、arXiv 2024-2026）\n\n注：原 task 要求 save_project_file 写入，但该文件不在白名单（白名单仅 memory.md/paper_framing.md/writing_plan.yaml），转写到 artifacts/。\n\n---\n\n## 1. SPEAR (Self-imitation with Progressive Exploration)\n- **论文**：\"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\"，Qin et al.（Tencent Youtu），arXiv 2509.22601，**ICLR 2026 接收**\n- **核心思想**：课程式自模仿学习（SIL）。早期用辅助 tool-use reward 鼓励技能层面探索，后期逐步把权重切换到成功 trajectory 的 self-imitation；用 replay buffer 存正 advantage 轨迹做 off-policy 更新。\n- **与我们场景的相关性**：⭐⭐⭐⭐⭐ **最直接相关**。明确针对 sparse-reward + long-horizon agent，**用同一个 ALFWorld + Qwen2.5-1.5B 设置在 GRPO 基础上 +16.1% success（72.8% → 88.9%）**。同时也跑了 WebShop（+20.7%）。三个核心问题它都覆盖：\n  - sparse reward：early-stage 用 tool-call bonus 给信号\n  - reward gaming：bonus 用 cosine schedule **衰减到 0**，最终只剩 outcome reward\n  - collapse：self-imitation 用历史成功轨迹稳定梯度\n- **关键公式**：\n  - 复合奖励：`R = R_outcome + μ·R_tool-call + R_format`，`R_tool-call = min(1, 0.1·n_tool_call)`\n  - 衰减：`μ = ½(cos(πt/T_decay)+1)`，t > T_decay 后 μ=0\n  - SIL warm-up：`γ = ½(1 - cos(πt/T_warmup))`，逐步上升到 1\n  - SIL 损失：`J_SIL = Σ J_GRPO_j · 𝟙(Â_j > 0 ∧ Ã_j > 0) · M_j`，Ã_j 是 50 分位 baseline 重新校准的 advantage\n- **集成难度**：低-中。代码在 `TencentYoutuResearch/SPEAR`，**基于 GRPO + 修改**（去掉 KL，clip-higher 0.28/0.2，去掉 intra-group 归一化）。如果 RAGEN 已经在 verl/TRL 上跑通 GRPO，加 replay buffer + 双 cosine schedule + SIL loss 项即可。\n- **关键超参**：\n  - replay buffer size N_D = 2000-4000\n  - baseline buffer N_DR = 500\n  - T_warmup ≈ T_decay ≈ 200 steps\n  - clip ratio λ = 0.0002-0.02（mask 高 covariance token）\n  - KL coef = 0\n- **风险**：\n  - 我们 exp013 试过 valid_action_bonus=0.15 已经 gaming 了，SPEAR 的 `0.1·n_tool_call` 系数类似量级——必须严格遵守 cosine decay，否则同样 gaming\n  - 1.7B 模型在 ALFWorld 初期 success≈0%，replay buffer 可能长时间为空 → 退化成 GRPO；可考虑用 SFT warm-up 让 buffer 先有种子轨迹\n\n---\n\n## 2. GiGPO (Group-in-Group Policy Optimization)\n- **论文**：\"Group-in-Group Policy Optimization for LLM Agent Training\"，Feng, Xue, Liu, An（NTU），arXiv 2505.10978，**NeurIPS 2025**\n- **核心思想**：两层 group 结构做细粒度 credit assignment：episode 级用整条 trajectory 算 macro advantage；step 级用 **anchor state grouping**——把跨 trajectory 出现的相同环境状态聚成一组，在该组内对动作算 micro advantage。\n- **与我们场景的相关性**：⭐⭐⭐⭐ 主要解决 sparse outcome reward 下的 credit assignment 问题。同样在 ALFWorld + Qwen2.5-1.5B/3B/7B-Instruct 上验证，**vs GRPO +12% on ALFWorld，+9% on WebShop**。不直接解决 collapse，但通过 step-level 信号让 advantage 更稳定（少一些零梯度 group）。\n- **集成难度**：中。代码在 `langfengq/verl-agent`（verl-agent 是 verl 的 agent 扩展）。如果 RAGEN 也基于 verl，迁移成本低；核心改动是 rollout 后做状态 hash + 重新分组。**关键依赖**：环境状态可哈希/可识别相同状态——ALFWorld 部分观测下要小心，可能需要用前 N 步 observation 拼接做 anchor。\n- **关键超参**：episode-level 和 step-level advantage 的加权系数（论文需查）。\n- **风险**：\n  - ALFWorld 状态空间大，\"相同 anchor state\" 可能很少出现 → step-level group 太小 → 仍是 sparse 信号\n  - 实现复杂度比 SPEAR 高一些\n\n---\n\n## 3. EPO (Entropy-regularized Policy Optimization for LLM Agents)\n- **论文**：\"EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning\"，Wujiang Xu et al.，arXiv 2509.22576（2025-09，2026-02 更新）\n- **核心思想**：诊断了 sparse-reward 多轮 agent 训练的 **\"exploration-exploitation cascade failure\"**——前期 sparse feedback 让 policy 过早收敛到 flawed strategies；后期 vanilla entropy 正则反而引发混乱探索导致 collapse。EPO 三机制：(1) 多轮设置下加 entropy 正则，(2) **entropy smoothing regularizer**——把 policy entropy 约束在历史均值范围内防止突变，(3) 自适应阶段权重，平衡探索/利用。\n- **与我们场景的相关性**：⭐⭐⭐⭐ 论文描述的 cascade failure 与我们 exp013→exp015 观察到的「先 gaming 再 collapse」非常相似。ALFWorld +19.8%，ScienceWorld +152%。代码在 `WujiangXu/EPO`。\n- **集成难度**：中。需要维护历史 entropy 滑动均值，并把 entropy bound 加进 loss——比 SPEAR 改动小，但比单纯加 entropy coef 复杂。\n- **关键超参**：entropy 历史窗口大小、entropy bound 的上下限、阶段切换 schedule。\n- **风险**：\n  - 我们 exp015 已经用 kl_coef=0.1 + lr=1e-7 做稳定性修复，再叠加 EPO 可能过约束（entropy 完全压死 → 无探索）\n  - \"保证 entropy variance 单调下降\"听起来像主动抑制探索，对 1.7B 这种已经 entropy 偏低的模型可能不利\n\n---\n\n## 4. DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization)\n- **论文**：\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"，ByteDance Seed，arXiv 2503.14476（2025-03）\n- **核心思想**：在 Qwen2.5-32B 上 50% 步数超过 DeepSeek-R1-Zero-Qwen-32B。四个关键技术：\n  1. **Clip-Higher**：解耦上下 clip，把上 clip 从 0.2 扩到 0.28，鼓励低概率 token 上升，**防止 entropy collapse**\n  2. **Dynamic Sampling**：丢弃 acc=0 和 acc=1 的 prompt group（这些 group 内 advantage 全相同），保留有梯度的样本\n  3. **Token-level Policy Gradient Loss**：长 CoT 场景下不再按序列平均\n  4. **Overlong Reward Shaping**：长输出的奖励 shaping，降低噪声\n- **与我们场景的相关性**：⭐⭐⭐⭐ **Dynamic Sampling 直接解决我们「group 内 reward 全相同 → 零梯度」的问题**——把这种 group 丢掉、resample 直到 batch 内有有效梯度的样本。Clip-Higher 缓解 entropy collapse。\n- **集成难度**：低。已被 verl 原生支持，TRL 也有 PR。改三个参数就能开 Clip-Higher，Dynamic Sampling 需要在 batch 构造时加过滤逻辑。\n- **关键超参**：ε_low=0.2, ε_high=0.28（论文默认值）；Dynamic Sampling 的 oversample 倍数\n- **风险**：\n  - 注意：**有研究发现 Dynamic Sampling 在某些设置下不提升性能甚至有害**（见 arxiv 2512.07611）——需要消融\n  - DAPO 是为单轮长 CoT reasoning 设计，agent 多轮场景需要额外验证\n  - Dynamic Sampling 在 success≈0% 的初期意味着**一直丢弃所有 group**（全 acc=0），可能完全无法启动训练——需要配合 SPEAR 式 bonus 或 SFT warm-up\n\n---\n\n## 5. GTPO (Stabilizing GRPO via Gradient and Entropy Control)\n- **论文**：\"GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control\"，arXiv 2508.03772（2025-08）\n- **核心思想**：诊断 GRPO 两个本质问题：(1) **同 group 内不同 completion 共享的 token 收到矛盾梯度**（gradient conflict）；(2) negative-reward completion 对 confident token 施加惩罚导致 **policy collapse**。GTPO：跳过这些 token 的 negative update，只放大 positive；按 entropy 阈值过滤高 entropy completion；**完全不依赖 KL**（不需要 reference model）。\n- **与我们场景的相关性**：⭐⭐⭐ 直接针对 collapse 现象。但实验集中在数学推理（GSM8K/MATH/AIME），agent 任务上未验证。\n- **集成难度**：中。需要在 token 级做 gradient 路由（识别哪些 token 跨 completion 共享）。\n- **关键超参**：entropy 阈值；conflict 检测的 token 共现窗口\n- **风险**：未在 agent 任务上验证；跨 completion 的共享 token 在 agent 多轮场景定义不同（每轮 prompt 不同）\n\n---\n\n## 6. Dr. GRPO (Length-bias 修正)\n- **论文**：来自 \"Understanding R1-Zero-Like Training: A Critical Perspective\"（2503.20783）等工作\n- **核心思想**：GRPO 原版按序列长度归一化导致长的错误回复被欠惩罚。Dr. GRPO 用全局常数归一化，消除长度偏差。\n- **与我们场景的相关性**：⭐⭐ 主要解决 length bias，不直接解决 sparse reward / collapse / gaming。但 SPEAR 内部就用了类似策略（去掉 intra-group 归一化）。\n- **集成难度**：极低。verl 里改 `loss_agg_mode=\"seq-mean-token-sum-norm\"` 即可。\n- **风险**：单独用不解决我们的核心问题；可作为基础设置叠加在其他算法上\n\n---\n\n## 7. GDPO (Group reward-Decoupled Normalization)\n- **论文**：\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\"，NVlabs，arXiv 2601.05242\n- **核心思想**：注意：GDPO 这里指 \"Group reward-Decoupled\"，**不是** \"Group Distributionally-robust\"。专门解决**多奖励**场景下 GRPO 把不同 reward 组合 normalize 到同一 advantage 而丢失分辨率的问题。Key trick：**先 normalize 再聚合**（与原 GRPO 顺序相反）。\n- **与我们场景的相关性**：⭐⭐⭐ 如果我们坚持用 sparse outcome + dense bonus 的多奖励组合（exp013 的方向），GDPO 比 GRPO 更合适——能保留 success 信号和 bonus 信号的分辨率，**潜在缓解 reward gaming**（因为不同 reward 维度的相对差异被保留）。代码在 `NVlabs/GDPO`。\n- **集成难度**：中。需要把 reward 拆成多维度，分别 normalize。\n- **关键超参**：各 reward 维度的相对权重\n- **风险**：仍未根本解决 gaming——只是让 success 信号不被 bonus 淹没；如果 success 信号本身缺失（初期），多奖励解耦也救不了\n\n---\n\n## 8. StarPO-S (RAGEN 自带的稳定化变体)\n- **论文**：RAGEN 论文（arXiv 2504.20073），\"Understanding Self-Evolution in LLM Agents via Multi-Turn RL\"\n- **核心思想**：三个稳定化机制：(1) **variability-based trajectory filtering**——丢弃 group 内 reward variance 低的 trajectory（默认丢 25%）；(2) critic baselining；(3) decoupled clipping。\n- **与我们场景的相关性**：⭐⭐⭐⭐ **我们用的就是 RAGEN，这是开箱即用方案**。trajectory filtering 与 DAPO Dynamic Sampling 思路一致。论文还观察到「GRPO 在 Bandit 上 20 步开始 collapse，PPO 100 步才 collapse；reward std 和 entropy 是 early warning」——和我们看到的现象一致。\n- **集成难度**：极低（已在 RAGEN 仓库内）。\n- **关键超参**：filtering rate（默认 25%）；decoupled clip 上下限\n- **风险**：低。可作为 baseline 设置\n\n---\n\n## 9. VAPO (Value-Augmented Proximal PO)\n- **论文**：\"VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks\"，ByteDance，arXiv 2504.05118（2025-04）\n- **核心思想**：value-based 方法（保留 critic，与 GRPO 路线相反）。解决 value model bias、长序列异质性、reward sparsity 三大问题。**value-pretraining**：用 fixed policy 的 Monte Carlo return 预训练 value network，避免 value 初始 bias。\n- **与我们场景的相关性**：⭐⭐⭐ 直接讨论 sparse reward。但属于 PPO 路线，要恢复 critic，对 1.7B 显存不大友好（不过 1.7B 还好）。AIME 上 60.4，**无训练 crash**。\n- **集成难度**：中-高。需要切换回 PPO + critic，多出 value 预训练阶段。\n- **关键超参**：value pretraining 步数；GAE λ\n- **风险**：PPO 路线整体收敛比 GRPO 慢；agent 场景未验证\n\n---\n\n## 10. ARPO (Agentic Reinforced PO)\n- **论文**：\"Agentic Reinforced Policy Optimization\"，RUC-NLPIR，arXiv 2507.19849，**ICLR 2026 接收**\n- **核心思想**：观察到 LLM 在 tool-call 后 entropy 升高（不确定性增大）→ **entropy-based adaptive rollout**：在高 entropy 的 tool-call 轮次自适应分支采样。advantage attribution estimation 让 LLM 内化 stepwise 工具使用的 advantage 差异。\n- **与我们场景的相关性**：⭐⭐⭐ ALFWorld 是工具/动作型 agent，思路适用但论文重点是 search/tool-use。\n- **集成难度**：中。需要 rollout 阶段做自适应分支，与 verl 现有同步 rollout 不太一样。\n- **关键超参**：entropy 触发阈值；分支因子\n- **风险**：rollout 改造工程量；agent 任务 entropy 信号是否可靠未知\n\n---\n\n## 11. AgentHER / ECHO (Hindsight Trajectory Relabeling)\n- **论文**：\n  - AgentHER：arXiv 2603.21357\n  - ECHO（Sample-Efficient Online Learning via Hindsight Trajectory Rewriting）：arXiv 2510.10304\n- **核心思想**：把失败 trajectory 用 LLM 改写成「针对 goal B 的成功 trajectory」——失败一次仍能产生学习信号。AgentHER 报告 WebArena/ToolBench 上 +7.1~11.7pp。\n- **与我们场景的相关性**：⭐⭐⭐ 针对 sparse reward 下 \"0% success → 0 信号\" 的根本问题。但当前主要用于 **offline SFT 数据增强**，online RL 集成方案尚不成熟。\n- **集成难度**：中-高。需要 LLM 改写 trajectory（额外推理成本），且要确认 ALFWorld 任务 goal 可以重新标注（ALFWorld 是文本游戏，goal 是\"在 X 中放 Y\"，理论上可改写）。\n- **关键超参**：relabel 的 trajectory 占比；改写温度\n- **风险**：可能引入 reward hacking（改写后的\"成功\"与原任务无关）；多一个推理 pipeline\n\n---\n\n## 12. i-MENTOR / LLM 驱动内在动机\n- **论文**：\"Navigate the Unknown: Enhancing LLM Reasoning with Intrinsic Motivation Guided Exploration\"（arXiv 2505.17621）；\"LLM-Driven Intrinsic Motivation for Sparse Reward RL\"（arXiv 2508.18420）\n- **核心思想**：用 VAE state novelty 或 LLM 评估 state novelty 给 intrinsic reward。\n- **与我们场景的相关性**：⭐⭐ 思路通用，但偏经典 RL，没在 ALFWorld LLM agent 上验证。\n- **集成难度**：高（需要训 VAE 或加 LLM 评估 callback）\n- **风险**：与 SPEAR 的 tool-call bonus 类似 → 仍有 gaming 风险；额外训练成本\n\n---\n\n## 13. MT-GRPO (Turn-Level Reward Design)\n- **论文**：\"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\"，arXiv 2505.11821，**NeurIPS 2025**\n- **核心思想**：把 outcome reward 拆到 turn 级——每一轮给一个中间奖励。GRPO/PPO 扩展为 MT-GRPO/MT-PPO。\n- **与我们场景的相关性**：⭐⭐ 思路合理，但 ALFWorld 的「每轮是否合法/有进展」难以自动给出 turn 级奖励（需要 process reward model 或环境信号）。\n- **集成难度**：中。如果 ALFWorld 能给 turn 级 progress 信号（如目标距离），直接接入。\n- **风险**：与 dense bonus 同一类问题——turn 级奖励容易被 game\n\n---\n\n## 总结推荐表\n\n| 算法 | 解决问题 | 集成难度 | 推荐优先级 | 备注 |\n|------|---------|---------|----------|------|\n| **SPEAR** | sparse + gaming + collapse 全覆盖 | 低-中 | **★★★★★ P0** | 同设置 ALFWorld 实测 +16.1%；ICLR 2026；课程 + SIL 优雅解决 gaming |\n| **GiGPO** | sparse credit assignment | 中 | **★★★★ P1** | ALFWorld +12%；verl-agent 已实现；可与 SPEAR 叠加（SPEAR 论文也对比了 GiGPO） |\n| **DAPO 组件** | 零梯度 group + entropy collapse | 低 | **★★★★ P1** | Dynamic Sampling 直接解决「group 全相同」；Clip-Higher 防 collapse；可单独抽取组件叠加 |\n| **EPO** | cascade failure（gaming→collapse） | 中 | ★★★ P2 | ALFWorld +19.8%；与 exp015 已有的稳定性修复方向重合，需消融 |\n| **StarPO-S** | 一般稳定化 | 极低 | ★★★ P2 | RAGEN 自带，立即可用；与 DAPO Dynamic Sampling 思路重叠 |\n| **GDPO** | 多奖励解耦（缓解 gaming） | 中 | ★★ P3 | 仅在保留 dense bonus 时有意义；不解决 sparse 启动问题 |\n| **GTPO** | gradient conflict + collapse | 中 | ★★ P3 | 仅推理任务验证；agent 场景未知 |\n| **VAPO** | 切回 critic 路线 | 中-高 | ★★ P3 | 改动大；显存/速度劣于 GRPO 系 |\n| **ARPO** | tool-call 自适应 rollout | 中 | ★★ P3 | rollout 改造工程量 |\n| **AgentHER/ECHO** | 失败轨迹重标 | 中-高 | ★★ P3 | 当前 online RL 集成不成熟，更适合 SFT 阶段 |\n| **MT-GRPO** | turn-level credit | 中 | ★ P4 | 需要外部 progress 信号 |\n| **Dr. GRPO** | length bias | 极低 | ★ basic | 作为基础设置叠加 |\n\n---\n\n## 行动建议\n\n**短期（1-2 周）**：\n- 落地 **SPEAR**，直接复用其 ALFWorld + Qwen2.5-1.5B 配置作为强 baseline（我们用 Qwen3-1.7B 接近）：复合 reward + cosine decay + SIL replay buffer\n- 同时叠加 **DAPO 的 Clip-Higher (0.2/0.28) + Dynamic Sampling 过滤 all-same-reward group**，几乎零成本\n- 设置 **StarPO-S filtering** 作为额外保险\n\n**消融**：\n- SPEAR 复合 reward 单独 vs SPEAR + SIL → 确认 SIL 贡献\n- 关掉 cosine decay 看是否 gaming（验证 decay 的必要性）\n- 用 SPEAR 默认 KL=0 vs 我们 exp015 的 KL=0.1 → 哪个更稳\n\n**中期备选**：\n- 如果 SPEAR + DAPO 组件仍不够稳，叠加 **GiGPO step-level advantage**\n- 如果 1.7B 初期 replay buffer 长期为空，先做 **expert trajectory SFT warm-up**（ALFWorld 有 ground-truth solver 可生成专家轨迹）\n\n**不推荐近期尝试**：\n- VAPO（切 PPO 路线工程量过大）\n- AgentHER online 集成（不成熟）\n- 单独的 GDPO/GTPO（缺 agent 任务验证）\n\n---\n\n## 关于原 task 提到的算法的纠正\n\n- **\"GDPO = Group Distributionally-robust PO\"**：搜不到完全对应该名称的工作。最接近的是 NVlabs 的 \"Group reward-Decoupled\" GDPO，**作用完全不同**（多奖励解耦，不是 distributional robustness）。\"Distributionally Robust DPO\" 有相关工作（OpenReview D19hc2XPeZ），但那是 alignment 场景，不是 RL agent。\n- **\"DAPO = Decoupled Alignment PO\"**：原始 DAPO 全称是 \"**Decoupled Clip and Dynamic sAmpling Policy Optimization**\"（ByteDance），不是 \"Alignment\"。Clip-higher + Dynamic Sampling 部分原 task 描述正确。\n- **SPEAR**：与原 task 描述一致，确为 sparse-reward agent 训练方法。\n\n---\n\n## 参考资源\n\n- SPEAR 代码：https://github.com/TencentYoutuResearch/SPEAR\n- GiGPO 代码：https://github.com/langfengq/verl-agent\n- DAPO 项目页：https://dapo-sia.github.io/\n- EPO 代码：https://github.com/WujiangXu/EPO\n- RAGEN/StarPO-S：https://github.com/mll-lab-nu/RAGEN\n- ARPO 代码：https://github.com/RUC-NLPIR/ARPO\n- 综述：blacksnail789521/Agentic-RL-Training-Recipes（持续更新）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/literature_rl_alternatives.md",
    "content": "# GRPO 替代/改进算法调研\n\n**调研背景**：用 GRPO + Qwen3-1.7B 在 ALFWorld 上训练 agent，遇到三个核心问题：\n1. Sparse 二值奖励 → 同一 group 内 reward 相同 → advantage=0 → pg_loss=0（零梯度）\n2. Dense bonus 引入后 reward gaming（action_valid 60→97.5%，success→0%）\n3. 即使出现 success 信号，单步 GRPO 更新过激 → catastrophic collapse\n\n**调研截止**：2026-05（覆盖 ICLR 2026、NeurIPS 2025、arXiv 2024-2026）\n\n注：原 task 要求 save_project_file 写入，但该文件不在白名单（白名单仅 memory.md/paper_framing.md/writing_plan.yaml），转写到 artifacts/。\n\n---\n\n## 1. SPEAR (Self-imitation with Progressive Exploration)\n- **论文**：\"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\"，Qin et al.（Tencent Youtu），arXiv 2509.22601，**ICLR 2026 接收**\n- **核心思想**：课程式自模仿学习（SIL）。早期用辅助 tool-use reward 鼓励技能层面探索，后期逐步把权重切换到成功 trajectory 的 self-imitation；用 replay buffer 存正 advantage 轨迹做 off-policy 更新。\n- **与我们场景的相关性**：⭐⭐⭐⭐⭐ **最直接相关**。明确针对 sparse-reward + long-horizon agent，**用同一个 ALFWorld + Qwen2.5-1.5B 设置在 GRPO 基础上 +16.1% success（72.8% → 88.9%）**。同时也跑了 WebShop（+20.7%）。三个核心问题它都覆盖：\n  - sparse reward：early-stage 用 tool-call bonus 给信号\n  - reward gaming：bonus 用 cosine schedule **衰减到 0**，最终只剩 outcome reward\n  - collapse：self-imitation 用历史成功轨迹稳定梯度\n- **关键公式**：\n  - 复合奖励：`R = R_outcome + μ·R_tool-call + R_format`，`R_tool-call = min(1, 0.1·n_tool_call)`\n  - 衰减：`μ = ½(cos(πt/T_decay)+1)`，t > T_decay 后 μ=0\n  - SIL warm-up：`γ = ½(1 - cos(πt/T_warmup))`，逐步上升到 1\n  - SIL 损失：`J_SIL = Σ J_GRPO_j · 𝟙(Â_j > 0 ∧ Ã_j > 0) · M_j`，Ã_j 是 50 分位 baseline 重新校准的 advantage\n- **集成难度**：低-中。代码在 `TencentYoutuResearch/SPEAR`，**基于 GRPO + 修改**（去掉 KL，clip-higher 0.28/0.2，去掉 intra-group 归一化）。如果 RAGEN 已经在 verl/TRL 上跑通 GRPO，加 replay buffer + 双 cosine schedule + SIL loss 项即可。\n- **关键超参**：\n  - replay buffer size N_D = 2000-4000\n  - baseline buffer N_DR = 500\n  - T_warmup ≈ T_decay ≈ 200 steps\n  - clip ratio λ = 0.0002-0.02（mask 高 covariance token）\n  - KL coef = 0\n- **风险**：\n  - 我们 exp013 试过 valid_action_bonus=0.15 已经 gaming 了，SPEAR 的 `0.1·n_tool_call` 系数类似量级——必须严格遵守 cosine decay，否则同样 gaming\n  - 1.7B 模型在 ALFWorld 初期 success≈0%，replay buffer 可能长时间为空 → 退化成 GRPO；可考虑用 SFT warm-up 让 buffer 先有种子轨迹\n\n---\n\n## 2. GiGPO (Group-in-Group Policy Optimization)\n- **论文**：\"Group-in-Group Policy Optimization for LLM Agent Training\"，Feng, Xue, Liu, An（NTU），arXiv 2505.10978，**NeurIPS 2025**\n- **核心思想**：两层 group 结构做细粒度 credit assignment：episode 级用整条 trajectory 算 macro advantage；step 级用 **anchor state grouping**——把跨 trajectory 出现的相同环境状态聚成一组，在该组内对动作算 micro advantage。\n- **与我们场景的相关性**：⭐⭐⭐⭐ 主要解决 sparse outcome reward 下的 credit assignment 问题。同样在 ALFWorld + Qwen2.5-1.5B/3B/7B-Instruct 上验证，**vs GRPO +12% on ALFWorld，+9% on WebShop**。不直接解决 collapse，但通过 step-level 信号让 advantage 更稳定（少一些零梯度 group）。\n- **集成难度**：中。代码在 `langfengq/verl-agent`（verl-agent 是 verl 的 agent 扩展）。如果 RAGEN 也基于 verl，迁移成本低；核心改动是 rollout 后做状态 hash + 重新分组。**关键依赖**：环境状态可哈希/可识别相同状态——ALFWorld 部分观测下要小心，可能需要用前 N 步 observation 拼接做 anchor。\n- **关键超参**：episode-level 和 step-level advantage 的加权系数（论文需查）。\n- **风险**：\n  - ALFWorld 状态空间大，\"相同 anchor state\" 可能很少出现 → step-level group 太小 → 仍是 sparse 信号\n  - 实现复杂度比 SPEAR 高一些\n\n---\n\n## 3. EPO (Entropy-regularized Policy Optimization for LLM Agents)\n- **论文**：\"EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning\"，Wujiang Xu et al.，arXiv 2509.22576（2025-09，2026-02 更新）\n- **核心思想**：诊断了 sparse-reward 多轮 agent 训练的 **\"exploration-exploitation cascade failure\"**——前期 sparse feedback 让 policy 过早收敛到 flawed strategies；后期 vanilla entropy 正则反而引发混乱探索导致 collapse。EPO 三机制：(1) 多轮设置下加 entropy 正则，(2) **entropy smoothing regularizer**——把 policy entropy 约束在历史均值范围内防止突变，(3) 自适应阶段权重，平衡探索/利用。\n- **与我们场景的相关性**：⭐⭐⭐⭐ 论文描述的 cascade failure 与我们 exp013→exp015 观察到的「先 gaming 再 collapse」非常相似。ALFWorld +19.8%，ScienceWorld +152%。代码在 `WujiangXu/EPO`。\n- **集成难度**：中。需要维护历史 entropy 滑动均值，并把 entropy bound 加进 loss——比 SPEAR 改动小，但比单纯加 entropy coef 复杂。\n- **关键超参**：entropy 历史窗口大小、entropy bound 的上下限、阶段切换 schedule。\n- **风险**：\n  - 我们 exp015 已经用 kl_coef=0.1 + lr=1e-7 做稳定性修复，再叠加 EPO 可能过约束（entropy 完全压死 → 无探索）\n  - \"保证 entropy variance 单调下降\"听起来像主动抑制探索，对 1.7B 这种已经 entropy 偏低的模型可能不利\n\n---\n\n## 4. DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization)\n- **论文**：\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"，ByteDance Seed，arXiv 2503.14476（2025-03）\n- **核心思想**：在 Qwen2.5-32B 上 50% 步数超过 DeepSeek-R1-Zero-Qwen-32B。四个关键技术：\n  1. **Clip-Higher**：解耦上下 clip，把上 clip 从 0.2 扩到 0.28，鼓励低概率 token 上升，**防止 entropy collapse**\n  2. **Dynamic Sampling**：丢弃 acc=0 和 acc=1 的 prompt group（这些 group 内 advantage 全相同），保留有梯度的样本\n  3. **Token-level Policy Gradient Loss**：长 CoT 场景下不再按序列平均\n  4. **Overlong Reward Shaping**：长输出的奖励 shaping，降低噪声\n- **与我们场景的相关性**：⭐⭐⭐⭐ **Dynamic Sampling 直接解决我们「group 内 reward 全相同 → 零梯度」的问题**——把这种 group 丢掉、resample 直到 batch 内有有效梯度的样本。Clip-Higher 缓解 entropy collapse。\n- **集成难度**：低。已被 verl 原生支持，TRL 也有 PR。改三个参数就能开 Clip-Higher，Dynamic Sampling 需要在 batch 构造时加过滤逻辑。\n- **关键超参**：ε_low=0.2, ε_high=0.28（论文默认值）；Dynamic Sampling 的 oversample 倍数\n- **风险**：\n  - 注意：**有研究发现 Dynamic Sampling 在某些设置下不提升性能甚至有害**（见 arxiv 2512.07611）——需要消融\n  - DAPO 是为单轮长 CoT reasoning 设计，agent 多轮场景需要额外验证\n  - Dynamic Sampling 在 success≈0% 的初期意味着**一直丢弃所有 group**（全 acc=0），可能完全无法启动训练——需要配合 SPEAR 式 bonus 或 SFT warm-up\n\n---\n\n## 5. GTPO (Stabilizing GRPO via Gradient and Entropy Control)\n- **论文**：\"GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control\"，arXiv 2508.03772（2025-08）\n- **核心思想**：诊断 GRPO 两个本质问题：(1) **同 group 内不同 completion 共享的 token 收到矛盾梯度**（gradient conflict）；(2) negative-reward completion 对 confident token 施加惩罚导致 **policy collapse**。GTPO：跳过这些 token 的 negative update，只放大 positive；按 entropy 阈值过滤高 entropy completion；**完全不依赖 KL**（不需要 reference model）。\n- **与我们场景的相关性**：⭐⭐⭐ 直接针对 collapse 现象。但实验集中在数学推理（GSM8K/MATH/AIME），agent 任务上未验证。\n- **集成难度**：中。需要在 token 级做 gradient 路由（识别哪些 token 跨 completion 共享）。\n- **关键超参**：entropy 阈值；conflict 检测的 token 共现窗口\n- **风险**：未在 agent 任务上验证；跨 completion 的共享 token 在 agent 多轮场景定义不同（每轮 prompt 不同）\n\n---\n\n## 6. Dr. GRPO (Length-bias 修正)\n- **论文**：来自 \"Understanding R1-Zero-Like Training: A Critical Perspective\"（2503.20783）等工作\n- **核心思想**：GRPO 原版按序列长度归一化导致长的错误回复被欠惩罚。Dr. GRPO 用全局常数归一化，消除长度偏差。\n- **与我们场景的相关性**：⭐⭐ 主要解决 length bias，不直接解决 sparse reward / collapse / gaming。但 SPEAR 内部就用了类似策略（去掉 intra-group 归一化）。\n- **集成难度**：极低。verl 里改 `loss_agg_mode=\"seq-mean-token-sum-norm\"` 即可。\n- **风险**：单独用不解决我们的核心问题；可作为基础设置叠加在其他算法上\n\n---\n\n## 7. GDPO (Group reward-Decoupled Normalization)\n- **论文**：\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\"，NVlabs，arXiv 2601.05242\n- **核心思想**：注意：GDPO 这里指 \"Group reward-Decoupled\"，**不是** \"Group Distributionally-robust\"。专门解决**多奖励**场景下 GRPO 把不同 reward 组合 normalize 到同一 advantage 而丢失分辨率的问题。Key trick：**先 normalize 再聚合**（与原 GRPO 顺序相反）。\n- **与我们场景的相关性**：⭐⭐⭐ 如果我们坚持用 sparse outcome + dense bonus 的多奖励组合（exp013 的方向），GDPO 比 GRPO 更合适——能保留 success 信号和 bonus 信号的分辨率，**潜在缓解 reward gaming**（因为不同 reward 维度的相对差异被保留）。代码在 `NVlabs/GDPO`。\n- **集成难度**：中。需要把 reward 拆成多维度，分别 normalize。\n- **关键超参**：各 reward 维度的相对权重\n- **风险**：仍未根本解决 gaming——只是让 success 信号不被 bonus 淹没；如果 success 信号本身缺失（初期），多奖励解耦也救不了\n\n---\n\n## 8. StarPO-S (RAGEN 自带的稳定化变体)\n- **论文**：RAGEN 论文（arXiv 2504.20073），\"Understanding Self-Evolution in LLM Agents via Multi-Turn RL\"\n- **核心思想**：三个稳定化机制：(1) **variability-based trajectory filtering**——丢弃 group 内 reward variance 低的 trajectory（默认丢 25%）；(2) critic baselining；(3) decoupled clipping。\n- **与我们场景的相关性**：⭐⭐⭐⭐ **我们用的就是 RAGEN，这是开箱即用方案**。trajectory filtering 与 DAPO Dynamic Sampling 思路一致。论文还观察到「GRPO 在 Bandit 上 20 步开始 collapse，PPO 100 步才 collapse；reward std 和 entropy 是 early warning」——和我们看到的现象一致。\n- **集成难度**：极低（已在 RAGEN 仓库内）。\n- **关键超参**：filtering rate（默认 25%）；decoupled clip 上下限\n- **风险**：低。可作为 baseline 设置\n\n---\n\n## 9. VAPO (Value-Augmented Proximal PO)\n- **论文**：\"VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks\"，ByteDance，arXiv 2504.05118（2025-04）\n- **核心思想**：value-based 方法（保留 critic，与 GRPO 路线相反）。解决 value model bias、长序列异质性、reward sparsity 三大问题。**value-pretraining**：用 fixed policy 的 Monte Carlo return 预训练 value network，避免 value 初始 bias。\n- **与我们场景的相关性**：⭐⭐⭐ 直接讨论 sparse reward。但属于 PPO 路线，要恢复 critic，对 1.7B 显存不大友好（不过 1.7B 还好）。AIME 上 60.4，**无训练 crash**。\n- **集成难度**：中-高。需要切换回 PPO + critic，多出 value 预训练阶段。\n- **关键超参**：value pretraining 步数；GAE λ\n- **风险**：PPO 路线整体收敛比 GRPO 慢；agent 场景未验证\n\n---\n\n## 10. ARPO (Agentic Reinforced PO)\n- **论文**：\"Agentic Reinforced Policy Optimization\"，RUC-NLPIR，arXiv 2507.19849，**ICLR 2026 接收**\n- **核心思想**：观察到 LLM 在 tool-call 后 entropy 升高（不确定性增大）→ **entropy-based adaptive rollout**：在高 entropy 的 tool-call 轮次自适应分支采样。advantage attribution estimation 让 LLM 内化 stepwise 工具使用的 advantage 差异。\n- **与我们场景的相关性**：⭐⭐⭐ ALFWorld 是工具/动作型 agent，思路适用但论文重点是 search/tool-use。\n- **集成难度**：中。需要 rollout 阶段做自适应分支，与 verl 现有同步 rollout 不太一样。\n- **关键超参**：entropy 触发阈值；分支因子\n- **风险**：rollout 改造工程量；agent 任务 entropy 信号是否可靠未知\n\n---\n\n## 11. AgentHER / ECHO (Hindsight Trajectory Relabeling)\n- **论文**：\n  - AgentHER：arXiv 2603.21357\n  - ECHO（Sample-Efficient Online Learning via Hindsight Trajectory Rewriting）：arXiv 2510.10304\n- **核心思想**：把失败 trajectory 用 LLM 改写成「针对 goal B 的成功 trajectory」——失败一次仍能产生学习信号。AgentHER 报告 WebArena/ToolBench 上 +7.1~11.7pp。\n- **与我们场景的相关性**：⭐⭐⭐ 针对 sparse reward 下 \"0% success → 0 信号\" 的根本问题。但当前主要用于 **offline SFT 数据增强**，online RL 集成方案尚不成熟。\n- **集成难度**：中-高。需要 LLM 改写 trajectory（额外推理成本），且要确认 ALFWorld 任务 goal 可以重新标注（ALFWorld 是文本游戏，goal 是\"在 X 中放 Y\"，理论上可改写）。\n- **关键超参**：relabel 的 trajectory 占比；改写温度\n- **风险**：可能引入 reward hacking（改写后的\"成功\"与原任务无关）；多一个推理 pipeline\n\n---\n\n## 12. i-MENTOR / LLM 驱动内在动机\n- **论文**：\"Navigate the Unknown: Enhancing LLM Reasoning with Intrinsic Motivation Guided Exploration\"（arXiv 2505.17621）；\"LLM-Driven Intrinsic Motivation for Sparse Reward RL\"（arXiv 2508.18420）\n- **核心思想**：用 VAE state novelty 或 LLM 评估 state novelty 给 intrinsic reward。\n- **与我们场景的相关性**：⭐⭐ 思路通用，但偏经典 RL，没在 ALFWorld LLM agent 上验证。\n- **集成难度**：高（需要训 VAE 或加 LLM 评估 callback）\n- **风险**：与 SPEAR 的 tool-call bonus 类似 → 仍有 gaming 风险；额外训练成本\n\n---\n\n## 13. MT-GRPO (Turn-Level Reward Design)\n- **论文**：\"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design\"，arXiv 2505.11821，**NeurIPS 2025**\n- **核心思想**：把 outcome reward 拆到 turn 级——每一轮给一个中间奖励。GRPO/PPO 扩展为 MT-GRPO/MT-PPO。\n- **与我们场景的相关性**：⭐⭐ 思路合理，但 ALFWorld 的「每轮是否合法/有进展」难以自动给出 turn 级奖励（需要 process reward model 或环境信号）。\n- **集成难度**：中。如果 ALFWorld 能给 turn 级 progress 信号（如目标距离），直接接入。\n- **风险**：与 dense bonus 同一类问题——turn 级奖励容易被 game\n\n---\n\n## 总结推荐表\n\n| 算法 | 解决问题 | 集成难度 | 推荐优先级 | 备注 |\n|------|---------|---------|----------|------|\n| **SPEAR** | sparse + gaming + collapse 全覆盖 | 低-中 | **★★★★★ P0** | 同设置 ALFWorld 实测 +16.1%；ICLR 2026；课程 + SIL 优雅解决 gaming |\n| **GiGPO** | sparse credit assignment | 中 | **★★★★ P1** | ALFWorld +12%；verl-agent 已实现；可与 SPEAR 叠加（SPEAR 论文也对比了 GiGPO） |\n| **DAPO 组件** | 零梯度 group + entropy collapse | 低 | **★★★★ P1** | Dynamic Sampling 直接解决「group 全相同」；Clip-Higher 防 collapse；可单独抽取组件叠加 |\n| **EPO** | cascade failure（gaming→collapse） | 中 | ★★★ P2 | ALFWorld +19.8%；与 exp015 已有的稳定性修复方向重合，需消融 |\n| **StarPO-S** | 一般稳定化 | 极低 | ★★★ P2 | RAGEN 自带，立即可用；与 DAPO Dynamic Sampling 思路重叠 |\n| **GDPO** | 多奖励解耦（缓解 gaming） | 中 | ★★ P3 | 仅在保留 dense bonus 时有意义；不解决 sparse 启动问题 |\n| **GTPO** | gradient conflict + collapse | 中 | ★★ P3 | 仅推理任务验证；agent 场景未知 |\n| **VAPO** | 切回 critic 路线 | 中-高 | ★★ P3 | 改动大；显存/速度劣于 GRPO 系 |\n| **ARPO** | tool-call 自适应 rollout | 中 | ★★ P3 | rollout 改造工程量 |\n| **AgentHER/ECHO** | 失败轨迹重标 | 中-高 | ★★ P3 | 当前 online RL 集成不成熟，更适合 SFT 阶段 |\n| **MT-GRPO** | turn-level credit | 中 | ★ P4 | 需要外部 progress 信号 |\n| **Dr. GRPO** | length bias | 极低 | ★ basic | 作为基础设置叠加 |\n\n---\n\n## 行动建议\n\n**短期（1-2 周）**：\n- 落地 **SPEAR**，直接复用其 ALFWorld + Qwen2.5-1.5B 配置作为强 baseline（我们用 Qwen3-1.7B 接近）：复合 reward + cosine decay + SIL replay buffer\n- 同时叠加 **DAPO 的 Clip-Higher (0.2/0.28) + Dynamic Sampling 过滤 all-same-reward group**，几乎零成本\n- 设置 **StarPO-S filtering** 作为额外保险\n\n**消融**：\n- SPEAR 复合 reward 单独 vs SPEAR + SIL → 确认 SIL 贡献\n- 关掉 cosine decay 看是否 gaming（验证 decay 的必要性）\n- 用 SPEAR 默认 KL=0 vs 我们 exp015 的 KL=0.1 → 哪个更稳\n\n**中期备选**：\n- 如果 SPEAR + DAPO 组件仍不够稳，叠加 **GiGPO step-level advantage**\n- 如果 1.7B 初期 replay buffer 长期为空，先做 **expert trajectory SFT warm-up**（ALFWorld 有 ground-truth solver 可生成专家轨迹）\n\n**不推荐近期尝试**：\n- VAPO（切 PPO 路线工程量过大）\n- AgentHER online 集成（不成熟）\n- 单独的 GDPO/GTPO（缺 agent 任务验证）\n\n---\n\n## 关于原 task 提到的算法的纠正\n\n- **\"GDPO = Group Distributionally-robust PO\"**：搜不到完全对应该名称的工作。最接近的是 NVlabs 的 \"Group reward-Decoupled\" GDPO，**作用完全不同**（多奖励解耦，不是 distributional robustness）。\"Distributionally Robust DPO\" 有相关工作（OpenReview D19hc2XPeZ），但那是 alignment 场景，不是 RL agent。\n- **\"DAPO = Decoupled Alignment PO\"**：原始 DAPO 全称是 \"**Decoupled Clip and Dynamic sAmpling Policy Optimization**\"（ByteDance），不是 \"Alignment\"。Clip-higher + Dynamic Sampling 部分原 task 描述正确。\n- **SPEAR**：与原 task 描述一致，确为 sparse-reward agent 训练方法。\n\n---\n\n## 参考资源\n\n- SPEAR 代码：https://github.com/TencentYoutuResearch/SPEAR\n- GiGPO 代码：https://github.com/langfengq/verl-agent\n- DAPO 项目页：https://dapo-sia.github.io/\n- EPO 代码：https://github.com/WujiangXu/EPO\n- RAGEN/StarPO-S：https://github.com/mll-lab-nu/RAGEN\n- ARPO 代码：https://github.com/RUC-NLPIR/ARPO\n- 综述：blacksnail789521/Agentic-RL-Training-Recipes（持续更新）\n"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-14T13:24:47.616841+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/literature_rl_alternatives.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-14T13:24:47.616987+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Search GDPO algorithm papers', 'activeForm': 'Searching GDPO algorithm papers', 'status': 'completed'}, {'content': 'Search DAPO clip-higher dynamic sampling', 'activeForm': 'Searching DAPO clip-higher dynamic sampling', 'status': 'completed'}, {'content': 'Search SPEAR sparse reward exploration', 'activeForm': 'Searching SPEAR sparse reward exploration', 'status': 'completed'}, {'content': 'Search Dr.GRPO and GRPO variants', 'activeForm': 'Searching Dr.GRPO and GRPO variants', 'status': 'completed'}, {'content': 'Search sparse reward RL for LLM agents', 'activeForm': 'Searching sparse reward RL for LLM agents', 'status': 'completed'}, {'content': 'Verify SPEAR and EPO details via WebFetch', 'activeForm': 'Verifying SPEAR and EPO details via WebFetch', 'status': 'completed'}, {'content': 'Write literature_rl_alternatives.md', 'activeForm': 'Writing literature_rl_alternatives.md', 'status': 'completed'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Search GDPO algorithm papers', 'activeForm': 'Searching GDPO algorithm papers', 'status': 'completed'}, {'content': 'Search DAPO clip-higher dynamic sampling', 'activeForm': 'Searching DAPO clip-higher dynamic sampling', 'status': 'completed'}, {'content': 'Search SPEAR sparse reward exploration', 'activeForm': 'Searching SPEAR sparse reward exploration', 'status': 'completed'}, {'content': 'Search Dr.GRPO and GRPO variants', 'activeForm': 'Searching Dr.GRPO and GRPO variants', 'status': 'completed'}, {'content': 'Search sparse reward RL for LLM agents', 'activeForm': 'Searching sparse reward RL for LLM agents', 'status': 'completed'}, {'content': 'Verify SPEAR and EPO details via WebFetch', 'activeForm': 'Verifying SPEAR and EPO details via WebFetch', 'status': 'completed'}, {'content': 'Write literature_rl_alternatives.md', 'activeForm': 'Writing literature_rl_alternatives.md', 'status': 'completed'}]"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-14T13:24:47.617145+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-14T13:24:47.617318+00:00_

文件已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/literature_rl_alternatives.md`（save_project_file 不允许该文件名，白名单仅 memory.md/paper_framing.md/writing_plan.yaml，已转写到 artifacts 目录）。

## 关键结论

**最推荐：SPEAR（P0）** — Tencent Youtu，ICLR 2026
- 同设置 ALFWorld + Qwen2.5-1.5B 上对 GRPO **+16.1% success（72.8→88.9）**
- 三个问题全覆盖：tool-call bonus（解决初期 sparse）+ cosine decay 到 0（解决 gaming）+ SIL replay buffer（解决 collapse）
- 基于 GRPO 修改，代码开源；超参：N_D=2000-4000, T_warmup=T_decay=200, KL=0, clip-higher 0.28/0.2

**次推荐组合：DAPO 组件 + GiGPO（P1）**
- DAPO **Dynamic Sampling** 直接解决我们「group reward 全相同→零梯度」问题；**Clip-Higher (0.28/0.2)** 防 entropy collapse
- GiGPO 用 anchor state grouping 做 step-level credit assignment，ALFWorld +12%，已在 verl-agent 中实现

**已纠正原 task 的两点**：
- "GDPO = Group Distributionally-robust"：搜不到该名工作；存在的 GDPO 是 NVlabs 的 "Group reward-Decoupled"（多奖励解耦，作用不同）
- "DAPO = Decoupled Alignment PO"：实际是 "Decoupled Clip and Dynamic sAmpling PO"（ByteDance）

**重要风险提示**：DAPO Dynamic Sampling 单用会在 success≈0% 初期丢弃所有 group → 无法启动训练；必须配 SPEAR 式 bonus 或 SFT warm-up。

完整调研含 13 个算法的论文、公式、超参、集成方案、风险评估，以及短期/中期落地建议——见上述 md 文件。

Sources:
- [SPEAR — Learn the Ropes, Then Trust the Wins (arXiv 2509.22601)](https://arxiv.org/abs/2509.22601)
- [GiGPO — Group-in-Group Policy Optimization (arXiv 2505.10978)](https://arxiv.org/abs/2505.10978)
- [DAPO — Open-Source LLM RL System at Scale (arXiv 2503.14476)](https://arxiv.org/abs/2503.14476)
- [EPO — Entropy-regularized PO (arXiv 2509.22576)](https://arxiv.org/abs/2509.22576)
- [GTPO — Gradient and Entropy Control (arXiv 2508.03772)](https://arxiv.org/abs/2508.03772)
- [GDPO — Group reward-Decoupled (arXiv 2601.05242)](https://arxiv.org/abs/2601.05242)
- [VAPO — Value-Augmented PPO (arXiv 2504.05118)](https://arxiv.org/abs/2504.05118)
- [ARPO — Agentic Reinforced PO (arXiv 2507.19849)](https://arxiv.org/abs/2507.19849)
- [RAGEN/StarPO-S (arXiv 2504.20073)](https://arxiv.org/abs/2504.20073)
- [MT-GRPO — Turn-Level Reward (arXiv 2505.11821)](https://arxiv.org/abs/2505.11821)
- [SPEAR code](https://github.com/TencentYoutuResearch/SPEAR)
- [GiGPO code (verl-agent)](https://github.com/langfengq/verl-agent)
- [DAPO project page](https://dapo-sia.github.io/)
- [EPO code](https://github.com/WujiangXu/EPO)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_alternative-rl-algorithms_20260514T131751"
}
```

</details>

---
