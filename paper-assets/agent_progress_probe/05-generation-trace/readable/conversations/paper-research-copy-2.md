# paper research

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_paper_research_20260514T202752.jsonl`
- **Structured JSON:** [`a97d4200170e8cbe0ea9.json`](../../sessions/a9/a97d4200170e8cbe0ea9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-14T20:29:41.418296+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T202752",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T20:29:41.418768+00:00_

1	# Literature Map for Agent Progress Probe (EMNLP 2026 ARR)
2	# Generated: 2026-05-14
3	# Paper: Structural Signal Analysis for Progress Stagnation Detection in LLM Agents
4	#
5	# D039 Pivot: Empirical analysis paper. Central finding: stagnation signals are
6	# fundamentally structural (30 features → 0.995 in-domain, 0.967 cross-agent F1),
7	# decisively surpassing NL embeddings (0.906/0.751) and LLM-as-judge (+24.3pp).
8	# TLM is a well-motivated negative finding (3 implementations all fail to beat MV).
9	
10	papers:
11	
12	  # ============================================================
13	  # CATEGORY: direct-competitor
14	  # ============================================================
15	
16	  - id: "xi2025agentprm"
17	    title: "AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress"
18	    authors: "Zhiheng Xi, Chenyang Liao, Guanyu Li, Yajie Yang, Wenxiang Chen, Zhihao Zhang, Binghai Wang, Senjie Jin, Yuhao Zhou, Jian Guan, Wei Wu, Tao Ji, Tao Gui, Qi Zhang, Xuanjing Huang"
19	    venue: "arXiv preprint"
20	    year: 2025
21	    arxiv: "2511.08325"
22	    category: "direct-competitor"
23	    role: "主要竞争者：step-level PRM for agent guidance"
24	    key_finding: "用 promise（长期潜力）和 progress（即时进展）两个维度评估 agent 每步决策，实现 8x 计算效率提升"
25	    our_differentiation: "我们是 window-level monitoring（不是 step-level guidance），不需要 outcome labels，目标是 stagnation detection 不是 reward shaping"
26	
27	  - id: "choudhury2025prm"
28	    title: "Process Reward Models for LLM Agents: Practical Framework and Directions"
29	    authors: "Sanjiban Choudhury"
30	    venue: "arXiv preprint"
31	    year: 2025
32	    arxiv: "2502.10325"
33	    category: "direct-competitor"
34	    role: "PRM 框架综述 + InversePRM 方法"
35	    key_finding: "提出 AgentPRM（Monte Carlo rollout actor-critic）和 InversePRM（从 demonstrations 学习 process reward），3B 模型超越 GPT-4o"
36	    our_differentiation: "InversePRM 仍需 demonstration trajectories，我们用 programmatic LFs 替代人工标注；我们关注 monitoring 而非 training signal"

…[truncated 20053 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T202752",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T20:29:41.418987+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T202752",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T20:29:41.419133+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T202752",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T20:29:41.419311+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "WebArena benchmark agent evaluation arxiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T202752",
  "tool": "WebSearch",
  "tool_args": {
    "query": "WebArena benchmark agent evaluation arxiv 2024"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T20:29:41.419436+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MINT benchmark multi-turn interaction agent evaluation arxiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T202752",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MINT benchmark multi-turn interaction agent evaluation arxiv 2024"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T20:29:41.419555+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "agent trajectory anomaly detection loop detection 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T202752",
  "tool": "WebSearch",
  "tool_args": {
    "query": "agent trajectory anomaly detection loop detection 2025 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T20:29:41.419722+00:00_

Web search results for query: "WebArena benchmark agent evaluation arxiv 2024"

Links: [{"title":"[2307.13854] WebArena: A Realistic Web Environment for Building Autonomous Agents","url":"https://arxiv.org/abs/2307.13854"},{"title":"ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents","url":"https://arxiv.org/html/2410.06703v5"},{"title":"Published as a conference paper at ICLR 2024","url":"https://arxiv.org/pdf/2307.13854"},{"title":"WebArena Benchmark: Evaluating Web Agents","url":"https://www.emergentmind.com/topics/webarena-benchmark"},{"title":"WebArena Benchmark and the State of Agentic AI | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/webarena-benchmark-and-the-state-of-agentic-ai-c22697e8e192"},{"title":"WebArena: A Realistic Web Environment for Building Autonomous Agents - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230713854Z/abstract"},{"title":"GitHub - web-arena-x/visualwebarena: VisualWebArena is a benchmark for multimodal agents. · GitHub","url":"https://github.com/web-arena-x/visualwebarena"},{"title":"WebArena: A Realistic Web Environment for Building Autonomous Agents","url":"https://arxiv.org/html/2307.13854v4"},{"title":"WebArena-x","url":"https://webarena.dev/"},{"title":"BrowserArena: Evaluating LLM Agents on Real-World Web Navigation Tasks","url":"https://arxiv.org/html/2510.02418v2"}]

I've found comprehensive information about the WebArena benchmark for agent evaluation. Here are the key findings:

## Overview

WebArena is an environment for language-guided agents that is highly realistic and reproducible, focusing on agents that perform tasks on the web and creating an environment with fully functional websites from four common domains: e-commerce, social forum discussions, collaborative software development, and content management.

## Benchmark Details

The benchmark includes 812 long-horizon web-based tasks, with each task described as a high-level natural language in
…[truncated 1029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T202752",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T20:29:41.419908+00:00_

Web search results for query: "agent trajectory anomaly detection loop detection 2025 arxiv"

Links: [{"title":"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents","url":"https://arxiv.org/html/2602.06443"},{"title":"Trajectory Guard - A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI","url":"https://arxiv.org/html/2601.00516"},{"title":"Unsupervised Anomaly Detection in Multi-Agent Trajectory Prediction via Transformer-Based Models","url":"https://arxiv.org/html/2601.20367"},{"title":"Graph Enhanced Trajectory Anomaly Detection Jonathan Kabala Mbuya","url":"https://arxiv.org/pdf/2509.18386"},{"title":"Graph Enhanced Trajectory Anomaly Detection","url":"https://arxiv.org/html/2509.18386v1"},{"title":"[2601.20367] Unsupervised Anomaly Detection in Multi-Agent Trajectory Prediction via Transformer-Based Models","url":"https://arxiv.org/abs/2601.20367"},{"title":"[2509.18386] Graph Enhanced Trajectory Anomaly Detection","url":"https://arxiv.org/abs/2509.18386"},{"title":"Detecting Silent Failures in Multi-Agentic AI Trajectories","url":"https://arxiv.org/html/2511.04032"},{"title":"Context-Aware Trajectory Anomaly Detection","url":"https://arxiv.org/pdf/2410.19136"},{"title":"[2602.06443] TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents","url":"https://arxiv.org/abs/2602.06443"}]

Based on the search results, I found several recent 2025 arxiv papers on agent trajectory anomaly detection that include loop detection:

## Key Papers Found:

1. **TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents** (February 2026, arxiv 2602.06443)
   
   TrajAD is a specialized auditing framework for detecting and localizing anomalies by modeling the global context of execution traces to achieve precise step-level localization of errors. Notably, the framework is designed to detect logical errors inherent to the sequence, such as infinite loops or redundant actions. This capability enables efficient error recovery th
…[truncated 1051 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T202752",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T20:29:41.420089+00:00_

Web search results for query: "MINT benchmark multi-turn interaction agent evaluation arxiv 2024"

Links: [{"title":"GitHub - xingyaoww/mint-bench: Official Repo for ICLR 2024 paper MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback by Xingyao Wang*, Zihan Wang*, Jiateng Liu, Yangyi Chen, Lifan Yuan, Hao Peng and Heng Ji. · GitHub","url":"https://github.com/xingyaoww/mint-bench"},{"title":"[2309.10691] MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback","url":"https://arxiv.org/abs/2309.10691"},{"title":"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback","url":"https://xwang.dev/mint-bench/"},{"title":"mint: evaluating llms in multi-turn inter","url":"https://zihanwang314.github.io/pdf/mint.pdf"},{"title":"AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents Chang Ma∗♠","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf"},{"title":"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback | OpenReview","url":"https://openreview.net/forum?id=jp3gWrMuIZ"},{"title":"Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions","url":"https://arxiv.org/html/2507.05257v3"},{"title":"\\scalerel*X MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback","url":"https://arxiv.org/html/2309.10691v1"},{"title":"Published as a conference paper at ICLR 2024 MINTREC2.0: A LARGE-SCALE","url":"https://arxiv.org/pdf/2403.10943"},{"title":"[PDF] MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MINT:-Evaluating-LLMs-in-Multi-turn-Interaction-and-Wang-Wang/12b233752c7097ea6525622bed238ae2d2193c5a"}]

I found relevant information about the MINT benchmark. Here's what the search revealed:

## MINT: Evaluating LLMs in Multi-turn Interaction with
…[truncated 1375 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T202752",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T20:29:41.420341+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2307.13854 WebArena authors Shunyu Zhou ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T202752",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2307.13854 WebArena authors Shunyu Zhou ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T20:29:41.420478+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2602.06443 TrajAD trajectory anomaly detection LLM agents authors 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T202752",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2602.06443 TrajAD trajectory anomaly detection LLM agents authors 2026"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T20:29:41.420628+00:00_

Web search results for query: "arxiv 2307.13854 WebArena authors Shunyu Zhou ICLR 2024"

Links: [{"title":"[2307.13854] WebArena: A Realistic Web Environment for Building Autonomous Agents","url":"https://arxiv.org/abs/2307.13854"},{"title":"Published as a conference paper at ICLR 2024","url":"https://arxiv.org/pdf/2307.13854"},{"title":"[PDF] WebArena: A Realistic Web Environment for Building Autonomous Agents | Semantic Scholar","url":"https://www.semanticscholar.org/paper/WebArena:-A-Realistic-Web-Environment-for-Building-Zhou-Xu/e41482f4ee984f17382f6cdd900df094d928be06"},{"title":"GitHub - web-arena-x/webarena: Code repo for \"WebArena: A Realistic Web Environment for Building Autonomous Agents\" · GitHub","url":"https://github.com/web-arena-x/webarena"},{"title":"WebArena: A Realistic Web Environment for Building Autonomous Agents","url":"https://arxiv.org/html/2307.13854.pdf"},{"title":"WebArena: A Realistic Web Environment for Building Autonomous Agents - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230713854Z/abstract"},{"title":"(PDF) WebArena: A Realistic Web Environment for Building Autonomous Agents","url":"https://www.researchgate.net/publication/372654539_WebArena_A_Realistic_Web_Environment_for_Building_Autonomous_Agents"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2411.02337"},{"title":"Learning representations of learning representations","url":"https://arxiv.org/html/2404.08403v1"},{"title":"Computer Science Mar 2024","url":"https://arxiv.org/list/cs/2024-03?skip=8100&show=2000"}]

Based on the search results, I can provide you with information about the WebArena paper:

## WebArena Paper Details

The authors of the WebArena paper (arXiv 2307.13854) are Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, and Graham Neubig.

The paper was published as a conference paper at ICLR 2024.

## Paper Summary

The paper 
…[truncated 714 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T202752",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T20:29:41.420852+00:00_

Web search results for query: "arxiv 2602.06443 TrajAD trajectory anomaly detection LLM agents authors 2026"

Links: [{"title":"[2602.06443] TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents","url":"https://arxiv.org/abs/2602.06443"},{"title":"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents","url":"https://arxiv.org/html/2602.06443"},{"title":"Graph Enhanced Trajectory Anomaly Detection","url":"https://arxiv.org/html/2509.18386v1"},{"title":"Trajectory Anomaly Detection with By-Design Complementary Detectors Shurui Cao∗","url":"https://www.andrew.cmu.edu/user/lakoglu/pubs/25-sdm-TrajAD.pdf"},{"title":"[2509.18386] Graph Enhanced Trajectory Anomaly Detection","url":"https://arxiv.org/abs/2509.18386"},{"title":"Trajectory Anomaly Detection with Language Models","url":"https://arxiv.org/html/2409.15366v1"},{"title":"Context-Aware Trajectory Anomaly Detection","url":"https://arxiv.org/html/2410.19136v1"},{"title":"[2409.15366] Trajectory Anomaly Detection with Language Models","url":"https://arxiv.org/abs/2409.15366"},{"title":"Unsupervised Anomaly Detection in Multi-Agent Trajectory Prediction via Transformer-Based Models","url":"https://arxiv.org/html/2601.20367"},{"title":"[2303.05000] Learning Representation for Anomaly Detection of Vehicle Trajectories","url":"https://arxiv.org/abs/2303.05000"}]

Based on the search results, I found the paper you're looking for. Here's the information about arxiv 2602.06443:

## TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents

**Authors:** Yibing Liu, Chong Zhang, Zhongyi Han, Hansong Liu, Yong Wang, Yang Yu, Xiaoyan Wang, and Yilong Yin

**Paper ID:** arxiv 2602.06443  
**Submitted:** February 6, 2026

### Overview

The paper addresses runtime trajectory anomaly detection, a critical capability for enabling trustworthy LLM agents. The goal is not merely detection, but precise error localization, which is essential for enabling efficient rollback-and-retry.

### Key Contributions

- Tra
…[truncated 615 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T202752",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T20:29:41.421056+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
  "old_string": "  - id: \"wang2025openhands\"\n    title: \"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\"\n    authors: \"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    arxiv: \"2407.16741\"\n    category: \"evaluation\"\n    role: \"Agent 平台——主要数据来源\"\n    key_finding: \"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\"\n    our_differentiation: \"OpenHands trajectories 是我们的主要实验数据来源\"\n\n  # ============================================================\n  # CATEGORY: background\n  # ============================================================",
  "new_string": "  - id: \"wang2025openhands\"\n    title: \"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\"\n    authors: \"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    arxiv: \"2407.16741\"\n    category: \"evaluation\"\n    role: \"Agent 平台——主要数据来源\"\n    key_finding: \"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\"\n    our_differentiation: \"OpenHands trajectories 是我们的主要实验数据来源\"\n\n  - id: \"zhou2024webarena\"\n    title: \"WebArena: A Realistic Web Environment for Building Autonomous Agents\"\n    authors: \"Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2307.13854\"\n    category: \"evaluation\"\n    verified: true\n    role: \"Web agent 评测基准——long-horizon 任务评估\"\n    key_finding: \"812 个真实网站上的 long-horizon 任务，GPT-4 agent 仅 14.41% 成功率 vs 人类 78.24%，揭示 agent 在复杂任务上的巨大差距\"\n    our_differentiation: \"WebArena 的 long-horizon 任务正是 stagnation 高发场景；我们的 monitor 可作为此类任务的早期终止/干预信号\"\n\n  - id: \"wang2024mint\"\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Xingyao Wang, Zihan Wang, Jiateng Liu, Yangyi Chen, Lifan Yuan, Hao Peng, Heng Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2309.10691\"\n    category: \"evaluation\"\n    verified: true\n    role: \"Multi-turn agent 评测基准——tool use + feedback 交互评估\"\n    key_finding: \"评估 LLM 在多轮交互中使用工具和接收自然语言反馈的能力，每轮 tool use 提升 1-8%，NL feedback 提升 2-17%\"\n    our_differentiation: \"MINT 量化了 multi-turn 交互中的性能变化，我们的 stagnation detection 关注多轮交互中进展停滞的检测；MINT 的 multi-turn 设定与我们的 window-level 分析天然对齐\"\n\n  # ============================================================\n  # CATEGORY: background\n  # ============================================================"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T202752",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
    "old_string": "  - id: \"wang2025openhands\"\n    title: \"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\"\n    authors: \"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    arxiv: \"2407.16741\"\n    category: \"evaluation\"\n    role: \"Agent 平台——主要数据来源\"\n    key_finding: \"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\"\n    our_differentiation: \"OpenHands trajectories 是我们的主要实验数据来源\"\n\n  # ============================================================\n  # CATEGORY: background\n  # ============================================================",
    "new_string": "  - id: \"wang2025openhands\"\n    title: \"OpenHands: An Open Platform for AI Software Developers as Generalist Agents\"\n    authors: \"Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    arxiv: \"2407.16741\"\n    category: \"evaluation\"\n    role: \"Agent 平台——主要数据来源\"\n    key_finding: \"开源 agent 平台，sandbox 执行环境，15+ benchmarks 评测\"\n    our_differentiation: \"OpenHands trajectories 是我们的主要实验数据来源\"\n\n  - id: \"zhou2024webarena\"\n    title: \"WebArena: A Realistic Web Environment for Building Autonomous Agents\"\n    authors: \"Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2307.13854\"\n    category: \"evaluation\"\n    verified: true\n    role: \"Web agent 评测基准——long-horizon 任务评估\"\n    key_finding: \"812 个真实网站上的 long-horizon 任务，GPT-4 agent 仅 14.41% 成功率 vs 人类 78.24%，揭示 agent 在复杂任务上的巨大差距\"\n    our_differentiation: \"WebArena 的 long-horizon 任务正是 stagnation 高发场景；我们的 monitor 可作为此类任务的早期终止/干预信号\"\n\n  - id: \"wang2024mint\"\n    title: \"MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback\"\n    authors: \"Xingyao Wang, Zihan Wang, Jiateng Liu, Yangyi Chen, Lifan Yuan, Hao Peng, Heng Ji\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2309.10691\"\n    category: \"evaluation\"\n    verified: true\n    role: \"Multi-turn agent 评测基准——tool use + feedback 交互评估\"\n    key_finding: \"评估 LLM 在多轮交互中使用工具和接收自然语言反馈的能力，每轮 tool use 提升 1-8%，NL feedback 提升 2-17%\"\n    our_differentiation: \"MINT 量化了 multi-turn 交互中的性能变化，我们的 stagnation detection 关注多轮交互中进展停滞的检测；MINT 的 multi-turn 设定与我们的 window-level 分析天然对齐\"\n\n  # ============================================================\n  # CATEGORY: background\n  # ============================================================"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T20:29:41.421304+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T202752",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T20:29:41.421461+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
  "old_string": "  - id: \"kamoi2024selfcorrection\"\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    venue: \"TACL 2024\"\n    year: 2024\n    arxiv: \"2406.01297\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\"\n    key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"\n    our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 empirical analysis 表明 structural features 即可提供高精度外部 stagnation 信号，无需复杂的语义理解\"\n\n  # ============================================================\n  # CATEGORY: technique\n  # ============================================================",
  "new_string": "  - id: \"kamoi2024selfcorrection\"\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    venue: \"TACL 2024\"\n    year: 2024\n    arxiv: \"2406.01297\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\"\n    key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"\n    our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 empirical analysis 表明 structural features 即可提供高精度外部 stagnation 信号，无需复杂的语义理解\"\n\n  - id: \"liu2026trajad\"\n    title: \"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents\"\n    authors: \"Yibing Liu, Chong Zhang, Zhongyi Han, Hansong Liu, Yong Wang, Yang Yu, Xiaoyan Wang, Yilong Yin\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2602.06443\"\n    category: \"background\"\n    verified: true\n    role: \"Agent trajectory 异常检测——stagnation detection 的直接前驱\"\n    key_finding: \"TrajAD 通过 fine-grained process supervision 训练 verifier 检测 agent trajectory 中的异常（task failure, process inefficiency, unwarranted continuation），通用 LLM zero-shot 表现差\"\n    our_differentiation: \"TrajAD 需要训练专用 verifier + 合成数据（perturb-and-complete），我们用 30 个 structural features 无需训练即达 0.995 F1；他们覆盖多种异常类型，我们专注 stagnation pattern 的深度分析\"\n\n  # ============================================================\n  # CATEGORY: technique\n  # ============================================================"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T202752",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
    "old_string": "  - id: \"kamoi2024selfcorrection\"\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    venue: \"TACL 2024\"\n    year: 2024\n    arxiv: \"2406.01297\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\"\n    key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"\n    our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 empirical analysis 表明 structural features 即可提供高精度外部 stagnation 信号，无需复杂的语义理解\"\n\n  # ============================================================\n  # CATEGORY: technique\n  # ============================================================",
    "new_string": "  - id: \"kamoi2024selfcorrection\"\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    venue: \"TACL 2024\"\n    year: 2024\n    arxiv: \"2406.01297\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\"\n    key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"\n    our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 empirical analysis 表明 structural features 即可提供高精度外部 stagnation 信号，无需复杂的语义理解\"\n\n  - id: \"liu2026trajad\"\n    title: \"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents\"\n    authors: \"Yibing Liu, Chong Zhang, Zhongyi Han, Hansong Liu, Yong Wang, Yang Yu, Xiaoyan Wang, Yilong Yin\"\n    venue: \"arXiv preprint\"\n    year: 2026\n    arxiv: \"2602.06443\"\n    category: \"background\"\n    verified: true\n    role: \"Agent trajectory 异常检测——stagnation detection 的直接前驱\"\n    key_finding: \"TrajAD 通过 fine-grained process supervision 训练 verifier 检测 agent trajectory 中的异常（task failure, process inefficiency, unwarranted continuation），通用 LLM zero-shot 表现差\"\n    our_differentiation: \"TrajAD 需要训练专用 verifier + 合成数据（perturb-and-complete），我们用 30 个 structural features 无需训练即达 0.995 F1；他们覆盖多种异常类型，我们专注 stagnation pattern 的深度分析\"\n\n  # ============================================================\n  # CATEGORY: technique\n  # ============================================================"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T20:29:41.421721+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T202752",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-14T20:29:41.421891+00:00_

已添加 3 篇论文：

- **evaluation**: `zhou2024webarena` (WebArena, ICLR 2024, arxiv 2307.13854), `wang2024mint` (MINT, ICLR 2024, arxiv 2309.10691)
- **background**: `liu2026trajad` (TrajAD, arXiv 2026, arxiv 2602.06443)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_20260514T202752"
}
```

</details>

---
