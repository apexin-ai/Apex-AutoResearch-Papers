# paper research

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_research_20260514T204749.jsonl`
- **Structured JSON:** [`d574550b1569229c8a5a.json`](../../sessions/d5/d574550b1569229c8a5a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-14T20:48:34.427043+00:00_

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
  "session": "worker_paper_research_20260514T204749",
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

_source line 2 · 2026-05-14T20:48:34.427371+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T204749",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T20:48:34.427533+00:00_

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
  "session": "worker_paper_research_20260514T204749",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T20:48:34.427857+00:00_

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

…[truncated 22186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T204749",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T20:48:34.428066+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.05672",
  "prompt": "Extract the exact paper title, full author list, and year of publication."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T204749",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2402.05672",
    "prompt": "Extract the exact paper title, full author list, and year of publication."
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T20:48:34.428198+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.03216",
  "prompt": "Extract the exact paper title, full author list, and year of publication."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T204749",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2402.03216",
    "prompt": "Extract the exact paper title, full author list, and year of publication."
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T20:48:34.428322+00:00_

# Paper Details

**Title:** "Multilingual E5 Text Embeddings: A Technical Report"

**Authors:** Liang Wang, Nan Yang, Xiaolong Huang, Linjun Yang, Rangan Majumder, Furu Wei

**Year:** 2024 (submitted February 8, 2024)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T204749",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T20:48:34.428456+00:00_

# Paper Information

**Title:** "M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation"

**Authors:** Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, Zheng Liu

**Year of Publication:** 2024 (submitted February 5, 2024; latest revision December 12, 2025)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T204749",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T20:48:34.428621+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
  "old_string": "    key_finding: \"基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA\"\n\n# ============================================================",
  "new_string": "    key_finding: \"基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA\"\n\n  - id: \"wang2024e5\"\n    title: \"Multilingual E5 Text Embeddings: A Technical Report\"\n    authors: \"Liang Wang, Nan Yang, Xiaolong Huang, Linjun Yang, Rangan Majumder, Furu Wei\"\n    venue: \"arXiv preprint\"\n    year: 2024\n    arxiv: \"2402.05672\"\n    category: \"technique\"\n    verified: true\n    role: \"Encoder ablation 中使用的 embedding model\"\n    key_finding: \"基于 XLM-R 的多语言 text embedding，混合多语言数据训练，跨语言检索和语义相似度任务上性能强劲\"\n\n  - id: \"chen2024bgem3\"\n    title: \"BGE M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation\"\n    authors: \"Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, Zheng Liu\"\n    venue: \"arXiv preprint\"\n    year: 2024\n    arxiv: \"2402.03216\"\n    category: \"technique\"\n    verified: true\n    role: \"Encoder ablation 中使用的 embedding model\"\n    key_finding: \"统一 dense/sparse/multi-vec 三种检索功能于单一模型，通过 self-knowledge distillation 训练，支持 8192 token 长文本和 100+ 语言\"\n\n# ============================================================"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260514T204749",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml",
    "old_string": "    key_finding: \"基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA\"\n\n# ============================================================",
    "new_string": "    key_finding: \"基于 Qwen3 的 embedding 模型（0.6B/4B/8B），多阶段训练，MTEB 多语言 SOTA\"\n\n  - id: \"wang2024e5\"\n    title: \"Multilingual E5 Text Embeddings: A Technical Report\"\n    authors: \"Liang Wang, Nan Yang, Xiaolong Huang, Linjun Yang, Rangan Majumder, Furu Wei\"\n    venue: \"arXiv preprint\"\n    year: 2024\n    arxiv: \"2402.05672\"\n    category: \"technique\"\n    verified: true\n    role: \"Encoder ablation 中使用的 embedding model\"\n    key_finding: \"基于 XLM-R 的多语言 text embedding，混合多语言数据训练，跨语言检索和语义相似度任务上性能强劲\"\n\n  - id: \"chen2024bgem3\"\n    title: \"BGE M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation\"\n    authors: \"Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, Zheng Liu\"\n    venue: \"arXiv preprint\"\n    year: 2024\n    arxiv: \"2402.03216\"\n    category: \"technique\"\n    verified: true\n    role: \"Encoder ablation 中使用的 embedding model\"\n    key_finding: \"统一 dense/sparse/multi-vec 三种检索功能于单一模型，通过 self-knowledge distillation 训练，支持 8192 token 长文本和 100+ 语言\"\n\n# ============================================================"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T20:48:34.428868+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260514T204749",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-14T20:48:34.429038+00:00_

已追加 2 篇论文到 `technique` section 末尾：

- `wang2024e5` — Multilingual E5 Text Embeddings (2402.05672)
- `chen2024bgem3` — BGE M3-Embedding (2402.03216)

两条均 `verified: true`，arxiv ID 已通过 arxiv 页面确认。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_20260514T204749"
}
```

</details>

---
