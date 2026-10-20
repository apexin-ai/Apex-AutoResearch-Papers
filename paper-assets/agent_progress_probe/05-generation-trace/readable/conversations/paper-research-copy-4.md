# paper research

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_paper_research_20260514T200749.jsonl`
- **Structured JSON:** [`7dba2b2d8e815b626f39.json`](../../sessions/7d/7dba2b2d8e815b626f39.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-14T20:09:21.720561+00:00_

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
  "session": "worker_paper_research_20260514T200749",
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

_source line 2 · 2026-05-14T20:09:21.720908+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T200749",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T20:09:21.721078+00:00_

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
  "session": "worker_paper_research_20260514T200749",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T20:09:21.721355+00:00_

1	# Literature Map for Agent Progress Probe (EMNLP 2026 ARR)
2	# Generated: 2026-05-14
3	# Paper: Temporal Label Model for Progress Stagnation Detection in LLM Agents
4	#
5	# Novelty check result: "temporal label model" as a general-purpose extension
6	# of data programming to sequential data appears NOVEL. Closest works are
7	# Safranchik AAAI 2020 (NER-specific linked HMM) and Sala NeurIPS 2019
8	# (multi-resolution WS, not temporal transitions).
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
37	
38	  - id: "li2026toolprmbench"
39	    title: "ToolPRM
…[truncated 17985 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T200749",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T20:09:21.721533+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM agent self-correction limitations failure 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T200749",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM agent self-correction limitations failure 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T20:09:21.721680+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"self-reflection\" LLM agent fails limitations external verification 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T200749",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"self-reflection\" LLM agent fails limitations external verification 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T20:09:21.721866+00:00_

Web search results for query: ""self-reflection" LLM agent fails limitations external verification 2024 2025"

Links: [{"title":"Large Language Models Cannot Self-Correct Reasoning Yet | OpenReview","url":"https://openreview.net/forum?id=IkmD3fKBPQ"},{"title":"Self-Reflection in LLM Agents: Effects on Problem-Solving Performance","url":"https://arxiv.org/pdf/2405.06682"},{"title":"[2310.01798] Large Language Models Cannot Self-Correct Reasoning Yet","url":"https://arxiv.org/abs/2310.01798"},{"title":"Reflect, Retry, Reward: Self-Improving LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2505.24726v1"},{"title":"Better Ways to Build Self-Improving AI Agents – Yohei Nakajima","url":"https://yoheinakajima.com/better-ways-to-build-self-improving-ai-agents/"},{"title":"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs","url":"https://arxiv.org/html/2510.16062v1"},{"title":"Self-reflection enhances large language models towards substantial academic response | npj Artificial Intelligence","url":"https://www.nature.com/articles/s44387-025-00045-3"},{"title":"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs","url":"https://arxiv.org/html/2512.20845"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"Large Language Models Can Self-Correct with Key Condition Verification - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.714/"}]

I've found substantial research on this topic. Here are the key findings:

## LLM Self-Reflection Limitations and the Need for External Verification

### Core Finding: Self-Correction Without External Feedback Fails

LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction. This has been wel
…[truncated 1535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T200749",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T20:09:21.722061+00:00_

Web search results for query: "LLM agent self-correction limitations failure 2024 2025"

Links: [{"title":"Large Language Models Cannot Self-Correct Reasoning Yet | OpenReview","url":"https://openreview.net/forum?id=IkmD3fKBPQ"},{"title":"[2310.01798] Large Language Models Cannot Self-Correct Reasoning Yet","url":"https://arxiv.org/abs/2310.01798"},{"title":"Limits of Self-Correction in LLMs: An Information-Theoretic Analysis of Correlated Errors[v2] | Preprints.org","url":"https://www.preprints.org/manuscript/202601.0892"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes"},{"title":"Experience-based Knowledge Correction for Robust Planning in Minecraft","url":"https://arxiv.org/html/2505.24157v2"},{"title":"Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=7K1kXowjK1"},{"title":"Large Language Models Can Self-Correct with Key Condition Verification - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.714/"},{"title":"NeurIPS Poster Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs","url":"https://neurips.cc/virtual/2025/poster/121806"},{"title":"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs","url":"https://arxiv.org/html/2510.16062v1"},{"title":"WHERE LLM AGENTS FAIL AND HOW THEY CAN LEARN FROM FAILURES","url":"https://arxiv.org/pdf/2509.25370"}]

Based on the search results, here's a comprehensive overview of LLM agent self-correction limitations and failures from recent research (2024-2025):

## Key Limitations and Failures

### Intrinsic Self-Correction Challenges

LLMs struggle to self-correct their responses without external feedback, and at times, 
…[truncated 1930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T200749",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T20:09:21.722233+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2310.01798",
  "prompt": "Extract: title, authors, venue/conference, year, arxiv ID, key findings about self-correction limitations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T200749",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2310.01798",
    "prompt": "Extract: title, authors, venue/conference, year, arxiv ID, key findings about self-correction limitations"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T20:09:21.722357+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2405.06682",
  "prompt": "Extract: title, authors, venue/conference, year, arxiv ID, key findings about self-reflection limitations in agents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T200749",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2405.06682",
    "prompt": "Extract: title, authors, venue/conference, year, arxiv ID, key findings about self-reflection limitations in agents"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T20:09:21.722487+00:00_

# Research Paper Summary

**Title:** Self-Reflection in LLM Agents: Effects on Problem-Solving Performance

**Authors:** Matthew Renze, Erhan Guven

**Venue/Conference:** 2nd International Conference on Foundation and Large Language Models (FLLM 2024)

**Year:** 2024

**arXiv ID:** 2405.06682

## Key Findings

The research demonstrated that "LLM agents are able to significantly improve their problem-solving performance through self-reflection (p < 0.001)." The study evaluated nine popular LLMs using multiple-choice questions, then employed eight distinct self-reflection approaches on incorrect responses.

**Important Note on Limitations:** The provided abstract does not explicitly detail limitations of self-reflection in agents. The paper focuses on positive outcomes—showing statistically significant performance improvements—and mentions comparing different reflection types, but the full limitations discussion appears to be contained within the complete paper rather than the abstract provided.

The researchers made all code and data publicly available on GitHub to support reproducibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T200749",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T20:09:21.722624+00:00_

# Paper Summary

**Title:** Large Language Models Cannot Self-Correct Reasoning Yet

**Authors:** Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou

**Venue/Conference:** ICLR 2024

**Year:** 2023 (submitted October 3, 2023; revised March 14, 2024)

**arXiv ID:** 2310.01798

## Key Findings on Self-Correction Limitations

The research reveals that "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction." 

The study focuses on *intrinsic self-correction*—where models attempt to correct themselves based solely on their own capabilities rather than receiving external guidance. The central conclusion is that this approach has significant limitations for reasoning tasks. Rather than improving accuracy, self-correction attempts can paradoxically worsen results, highlighting that current large language models lack the capacity for effective autonomous error detection and correction in logical reasoning contexts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T200749",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T20:09:21.722818+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes",
  "prompt": "Extract: title, all authors, venue, year, arxiv ID if available, key findings about when self-correction works vs fails"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T200749",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes",
    "prompt": "Extract: title, all authors, venue, year, arxiv ID if available, key findings about when self-correction works vs fails"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T20:09:21.722942+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv \"When Can LLMs Actually Correct Their Own Mistakes\" survey self-correction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T200749",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv \"When Can LLMs Actually Correct Their Own Mistakes\" survey self-correction"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T20:09:21.723054+00:00_

Request failed with status code 403

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T200749",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T20:09:21.723202+00:00_

Web search results for query: "arxiv "When Can LLMs Actually Correct Their Own Mistakes" survey self-correction"

Links: [{"title":"[2406.01297] When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://arxiv.org/abs/2406.01297"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://arxiv.org/html/2406.01297v1"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes"},{"title":"[2406.01297v3] When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://arxiv.org/abs/2406.01297v3"},{"title":"[2406.01297v2] When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://arxiv.org/abs/2406.01297v2"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A ...","url":"https://aclanthology.org/2024.tacl-1.78.pdf"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | alphaXiv","url":"https://www.alphaxiv.org/abs/2406.01297"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs - ACL Anthology","url":"https://aclanthology.org/2024.tacl-1.78/"},{"title":"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs","url":"https://arxiv.org/html/2510.16062"}]

I found the paper you're looking for! Here are the key results:

## Paper S
…[truncated 1495 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T200749",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T20:09:21.723344+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.01297",
  "prompt": "Extract: exact title, all authors, arxiv ID, venue/conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T200749",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2406.01297",
    "prompt": "Extract: exact title, all authors, arxiv ID, venue/conference"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T20:09:21.723461+00:00_

# Paper Information

**Title:** "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs"

**Authors:** 
- Ryo Kamoi
- Yusen Zhang
- Nan Zhang
- Jiawei Han
- Rui Zhang

**arXiv ID:** 2406.01297

**Venue:** Transactions of the Association for Computational Linguistics (TACL 2024)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T200749",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T20:09:21.723631+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
  "old_string": "  - id: \"pipis2025reasoningloop\"\n    title: \"Wait, Wait, Wait... Why Do Reasoning Models Loop?\"\n    authors: \"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.12895\"\n    category: \"background\"\n    role: \"Reasoning model looping 分析\"\n    key_finding: \"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\"\n    our_differentiation: \"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\"\n\n  # ============================================================\n  # CATEGORY: technique",
  "new_string": "  - id: \"pipis2025reasoningloop\"\n    title: \"Wait, Wait, Wait... Why Do Reasoning Models Loop?\"\n    authors: \"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.12895\"\n    category: \"background\"\n    role: \"Reasoning model looping 分析\"\n    key_finding: \"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\"\n    our_differentiation: \"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\"\n\n  - id: \"huang2024selfcorrect\"\n    title: \"Large Language Models Cannot Self-Correct Reasoning Yet\"\n    authors: \"Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2310.01798\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 失败的关键证据——支持 external monitoring 必要性\"\n    key_finding: \"LLM 在无外部反馈时无法自我纠错推理错误，intrinsic self-correction 甚至导致性能下降\"\n    our_differentiation: \"直接支持我们的核心论点：agent 不能可靠地自我检测 stagnation，需要外部 monitor（即我们的 TLM）\"\n\n  - id: \"kamoi2024selfcorrection\"\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    venue: \"TACL 2024\"\n    year: 2024\n    arxiv: \"2406.01297\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\"\n    key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"\n    our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 TLM 正是提供这种外部 stagnation 信号的轻量方案\"\n\n  # ============================================================\n  # CATEGORY: technique"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T200749",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
    "old_string": "  - id: \"pipis2025reasoningloop\"\n    title: \"Wait, Wait, Wait... Why Do Reasoning Models Loop?\"\n    authors: \"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.12895\"\n    category: \"background\"\n    role: \"Reasoning model looping 分析\"\n    key_finding: \"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\"\n    our_differentiation: \"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\"\n\n  # ============================================================\n  # CATEGORY: technique",
    "new_string": "  - id: \"pipis2025reasoningloop\"\n    title: \"Wait, Wait, Wait... Why Do Reasoning Models Loop?\"\n    authors: \"Charilaos Pipis, Shivam Garg, Vasilis Kontonis, Vaishnavi Shrivastava, Akshay Krishnamurthy, Dimitris Papailiopoulos\"\n    venue: \"arXiv preprint\"\n    year: 2025\n    arxiv: \"2512.12895\"\n    category: \"background\"\n    role: \"Reasoning model looping 分析\"\n    key_finding: \"Looping 是 risk-aversion 的表现：模型选择简单循环动作而非推进；用 30-gram 重复检测\"\n    our_differentiation: \"他们分析 reasoning model 内部循环的原因，我们检测 agent trajectory 级别的 stagnation；n-gram 是我们 LFs 之一\"\n\n  - id: \"huang2024selfcorrect\"\n    title: \"Large Language Models Cannot Self-Correct Reasoning Yet\"\n    authors: \"Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    arxiv: \"2310.01798\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 失败的关键证据——支持 external monitoring 必要性\"\n    key_finding: \"LLM 在无外部反馈时无法自我纠错推理错误，intrinsic self-correction 甚至导致性能下降\"\n    our_differentiation: \"直接支持我们的核心论点：agent 不能可靠地自我检测 stagnation，需要外部 monitor（即我们的 TLM）\"\n\n  - id: \"kamoi2024selfcorrection\"\n    title: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\"\n    authors: \"Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang\"\n    venue: \"TACL 2024\"\n    year: 2024\n    arxiv: \"2406.01297\"\n    category: \"background\"\n    verified: true\n    role: \"Self-correction 条件的系统性综述——外部反馈是成功的必要条件\"\n    key_finding: \"无外部反馈的 prompted self-correction 均未成功；self-correction 仅在有可靠外部反馈或大规模微调时有效\"\n    our_differentiation: \"综述证实 self-correction 需要外部信号，我们的 TLM 正是提供这种外部 stagnation 信号的轻量方案\"\n\n  # ============================================================\n  # CATEGORY: technique"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T20:09:21.723896+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T200749",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-14T20:09:21.724061+00:00_

已添加 2 篇论文到 `background` 类别末尾：

1. **huang2024selfcorrect** — "Large Language Models Cannot Self-Correct Reasoning Yet" (ICLR 2024, `2310.01798`)  
   核心证据：LLM 无外部反馈时 intrinsic self-correction 失败甚至降低性能。

2. **kamoi2024selfcorrection** — "When Can LLMs Actually Correct Their Own Mistakes?" (TACL 2024, `2406.01297`)  
   系统性综述确认：prompted self-correction 无一成功，self-correction 仅在有可靠外部反馈时有效。

两篇都直接支持我们的 "external monitoring > self-reflection" 论点——agent 不能可靠自检 stagnation，需要外部 monitor（即 TLM）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_20260514T200749"
}
```

</details>

---
