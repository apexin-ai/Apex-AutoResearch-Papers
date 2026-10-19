# paper research

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_paper_research_20260522T132715.jsonl`
- **Structured JSON:** [`59184ec552a1018f9961.json`](../../sessions/59/59184ec552a1018f9961.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-22T13:30:14.413818+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260522T132715",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T13:30:14.414369+00:00_

1	---
2	name: reference-audit
3	description: 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。
4	scope: global
5	tags:
6	- workflow
7	- submission
8	- writing
9	- quality
10	priority: 6
11	version: 2
12	roles:
13	- agent
14	- paper_agent
15	- review_reviewer
16	- worker
17	---
18	
19	# 引用验证与审计（Reference Audit）
20	
21	## 核心原则
22	
23	**写时验证，而非写后检查。** 每添加一条引用，立即验证真实性。AI 生成的引用约 40% 存在错误——绝不信任记忆中的引用信息。
24	
25	## 触发条件
26	
27	- 写论文时添加引用
28	- Review Reviewer 审查论文引用质量
29	- 提交前最终检查
30	- 发现可疑引用（年份不对、作者不存在、找不到原文）
31	
32	## 验证流程
33	
34	### 1. 单条引用验证（写论文时）
35	
36	每次需要引用时：
37	
38	1. **WebSearch 查找**：搜索论文标题 + 第一作者
39	2. **Google Scholar 确认**：`site:scholar.google.com [论文标题] [作者]`
40	3. **核对关键信息**：标题、第一作者、年份（±1 年）、venue
41	4. **获取 BibTeX**：从 Google Scholar 或 DBLP 获取标准格式
42	5. **验证 claim**（如果引用了具体结论）：确认该 claim 确实出现在原文中
43	
44	### 2. 全文引用审计（批量检查）
45	
46	**Step 1：调用 `verify_references(paper_dir)`**
47	
48	这是首选方式。该工具自动完成：
49	- 解析所有 .bib 文件，提取结构化条目
50	- 解析所有 .tex 文件，提取 `\cite{}`/`\citep{}`/`\citet{}` 引用
51	- 交叉检查：找出 orphan（.bib 有但未引用）和 missing（引用了但 .bib 没有）
52	- 调 OpenAlex API 在线验证每条引用是否存在（返回 verified/not_found/mismatch）
53	
54	如果只需快速离线检查，传 `skip_online=True`。
55	
56	**Step 2：人工复核工具报告中的问题条目**
57	
58	重点关注：
59	- `status: not_found` — 可能是幻觉引用，用 WebSearch 二次验证
60	- `status: mismatch` — 年份等信息不一致，检查 preprint vs published 版本
61	- `missing_bib` — 正文引用了但 .bib 中不存在，编译会报错
62	- `orphan_bib` — .bib 中有但正文未引用，清理或补引用
63	
64	**Step 3：语义验证**（优先级排序）
65	1. 首先验证 Introduction 和 Related Work 中的高频引用
66	2. 然后验证 Method 中支撑技术 claim 的引用
67	3. 最后验证其余引用
68	
69	对于 OpenAlex 未找到的条目，用 WebSearch 补充验证（arXiv、DOI、DBLP）。
70	
71	### 3. 验证失败处理
72	
73	**找不到论文时**：
74	1. 检查拼写——标题或作者名是否有误？
75	2. 尝试不同查询组合（WebSearch + Google Scholar + DBLP）
76	3. 标记为 `[CITATION NEEDED]`
77	4. 明确告知——说明哪条引用无法验证
78	
79	**信息不匹配时**：
80	1. 确认是否找对了论文
81	2. 检查版本——preprint vs published 版本
82	3. 用最准确的版本更新信息
83	
84	**绝不做的事**：
85	- 从记忆生成 BibTeX——AI 生成引用 40% 错误率
86	- 跳过验证步骤
87	- 假设论文存在
88	- 对无法验证的引用不做标记
…[truncated 888 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T13:30:14.414547+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260522T132715",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T13:30:14.414764+00:00_

1	meta:
2	  last_updated: '2026-05-21T12:04:50.276Z'
3	  total_papers: 10
4	categories: []
5	papers:
6	  zhao2026when:
7	    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'
8	    authors:
9	    - Zhao, J.
10	    - et al.
11	    year: 2026
12	    venue: arXiv
13	    url: https://arxiv.org/abs/2601.07041
14	    doi: ''
15	    bibtex_key: zhao2026when
16	    category: cross-lingual-conflict
17	    role: direct-competitor
18	    relevance: 'CLEAR benchmark: 10-language cross-lingual conflict evaluation. Behavioral
19	      finding that linguistic similarity governs entity-centric conflict resolution.
20	      Our work provides mechanistic explanation.'
21	    abstract: ''
22	    semantic_scholar_id: ''
23	    verified: true
24	    added_by: director-bootstrap
25	    added_at: '2026-05-21T12:04:50.273Z'
26	  zhao2025steering:
27	    title: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation
28	      Engineering
29	    authors:
30	    - Zhao, Y.
31	    - Devoto, A.
32	    - Hong, G.
33	    - et al.
34	    year: 2025
35	    venue: NAACL 2025 Oral
36	    url: https://arxiv.org/abs/2410.15999
37	    doi: ''
38	    bibtex_key: zhao2025steering
39	    category: sae-steering
40	    role: direct-competitor
41	    relevance: 'SpARE: SAE-based conflict feature selection + steering. Core methodology
42	      we extend to cross-lingual setting. MI-based feature selection, constraint-aware
43	      activation editing.'
44	    abstract: ''
45	    semantic_scholar_id: ''
46	    verified: true
47	    added_by: director-bootstrap
48	    added_at: '2026-05-21T12:04:50.273Z'
49	  boer2026probing:
50	    title: Probing for Knowledge Attribution in Large Language Models
51	    authors:
52	    - Boer, A.
53	    - Brink, I.
54	    - Ulmer, D.
55	    year: 2026
56	    venue: arXiv
57	    url: https://arxiv.org/abs/2602.22787
58	    doi: ''
59	    bibtex_key: boer2026probing
60	    category: probing
61	    role: direct-competitor
62	 
…[truncated 5879 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T13:30:14.414990+00:00_

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
  "session": "worker_paper_research_20260522T132715",
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

_source line 6 · 2026-05-22T13:30:14.415127+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T13:30:14.415258+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ConflictQA dataset Xie et al. knowledge conflict LLM paper",
  "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ConflictQA dataset Xie et al. knowledge conflict LLM paper",
    "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T13:30:14.415379+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "context-parametric knowledge conflict detection resolution LLM 2023 2024 2025",
  "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "tool_args": {
    "query": "context-parametric knowledge conflict detection resolution LLM 2023 2024 2025",
    "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T13:30:14.415497+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "cross-lingual knowledge conflict multilingual LLM 2024 2025 2026",
  "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "tool_args": {
    "query": "cross-lingual knowledge conflict multilingual LLM 2024 2025 2026",
    "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T13:30:14.415649+00:00_

Web search results for query: "ConflictQA dataset Xie et al. knowledge conflict LLM paper"

Links: [{"title":"Accommodate Knowledge Conflicts in Retrieval-augmented LLMs: Towards Robust Response Generation in the Wild","url":"https://arxiv.org/html/2504.12982"},{"title":"Exploring Knowledge Conflicts for Faithful LLM Reasoning: Benchmark and Method","url":"https://arxiv.org/html/2604.11209v1"},{"title":"Accommodate Knowledge Conflicts in Retrieval-augmented LLMs: Towards Reliable Response Generation in the Wild","url":"https://arxiv.org/html/2504.12982v1"},{"title":"When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models","url":"https://arxiv.org/html/2601.07041v1"},{"title":"Analysing the Residual Stream of Language Models Under Knowledge Conflicts","url":"https://arxiv.org/html/2410.16090v2"},{"title":"KCR: RESOLVING LONG-CONTEXT KNOWLEDGE CONFLICTS VIA REASONING IN LLMS","url":"https://www.arxiv.org/pdf/2508.01273"},{"title":"Who’s Who: Large Language Models Meet Knowledge Conflicts in Practice","url":"https://arxiv.org/html/2410.15737v1"},{"title":"ConflictBank: A Benchmark for Evaluating Knowledge Conflicts in Large Language Models","url":"https://arxiv.org/html/2408.12076v1"},{"title":"Knowledge Conflicts for LLMs: A Survey","url":"https://arxiv.org/html/2403.08319v1"},{"title":"Analysing the Residual Stream of Language Models Under Knowledge   Conflicts","url":"https://arxiv.org/pdf/2410.16090"}]

Based on the search results, I found information about the ConflictQA dataset and the Xie et al. work on knowledge conflicts in LLMs:

## Overview

ConflictQA (Xie et al. 2023) is a benchmark for studying knowledge conflicts. The dataset was created to examine how Large Language Models handle conflicts between their internal parametric knowledge and external contextual information.

## Dataset Construction

Xie et al. (2023) analyze conflicts between parametric knowledge and external evidence by introducing LLM-generated coherent counter-memory t
…[truncated 992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T13:30:14.415828+00:00_

Web search results for query: "cross-lingual knowledge conflict multilingual LLM 2024 2025 2026"

Links: [{"title":"When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models","url":"https://arxiv.org/pdf/2601.07041"},{"title":"Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation","url":"https://arxiv.org/html/2605.12515"},{"title":"Crosslingual Capabilities and Knowledge Barriers in Multilingual Large   Language Models","url":"https://arxiv.org/pdf/2406.16135"},{"title":"Mechanistic Understanding and Mitigation of Language Confusion in English-Centric Large Language Models","url":"https://arxiv.org/html/2505.16538v2"},{"title":"1 Cross-linguistic disagreement as a conflict of semantic alignment norms in","url":"https://arxiv.org/pdf/2503.04792"},{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge   Representation Sharing in LLMs","url":"https://arxiv.org/pdf/2408.10646"},{"title":"[2406.16135] Crosslingual Capabilities and Knowledge Barriers in Multilingual Large Language Models","url":"https://arxiv.org/abs/2406.16135"},{"title":"Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language   Models","url":"https://arxiv.org/pdf/2407.01358"},{"title":"Measuring Multilingual LLM Consistency as Simple as ...","url":"https://aclanthology.org/2025.ijcnlp-long.185.pdf"}]

I found several relevant research papers on cross-lingual knowledge conflict in multilingual LLMs from 2024-2026. Here's what the search revealed:

## Key Research Areas

Knowledge conflict occurs when a model's internally stored belief contradicts information presented in context, and how LLMs react to and resolve such conflicts is central to system robustness and faithfulness.

Despite the increasing multilingual nature of real-world systems, existing studies remain largely English-centric, leaving the mechanisms underlying Cross-Lingual Knowledge Conflict (CLKC) largely unexplored.

## Main Cha
…[truncated 1013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T13:30:14.416039+00:00_

Web search results for query: "context-parametric knowledge conflict detection resolution LLM 2023 2024 2025"

Links: [{"title":"Taming Knowledge Conflicts in Language Models","url":"https://arxiv.org/pdf/2503.10996"},{"title":"PROBING LATENT KNOWLEDGE CONFLICT FOR FAITHFUL RETRIEVAL-AUGMENTED GENERATION","url":"https://arxiv.org/pdf/2510.12460"},{"title":"Resolving Knowledge Conflicts in Large Language Models","url":"https://arxiv.org/html/2310.00935v3"},{"title":"Knowledge Conflicts for LLMs: A Survey","url":"https://arxiv.org/html/2403.08319v2"},{"title":"Analysing the Residual Stream of Language Models Under Knowledge   Conflicts","url":"https://arxiv.org/pdf/2410.16090"},{"title":"Task Matters: Knowledge Requirements Shape LLM Responses to Context–Memory Conflict","url":"https://arxiv.org/html/2506.06485"},{"title":"Context Copying Modulation: The Role of Entropy Neurons in Managing Parametric and Contextual Knowledge Conflicts","url":"https://arxiv.org/pdf/2509.10663"},{"title":"Understanding the Interplay between LLMs’ Utilisation of Parametric and Contextual Knowledge: A keynote at ECIR 2025","url":"https://arxiv.org/html/2603.09654v1"},{"title":"Steering Knowledge Selection Behaviours in LLMs via SAE-Based   Representation Engineering","url":"https://arxiv.org/pdf/2410.15999"}]

I've found several highly relevant research papers on this topic. Here's what the search revealed:

## Context-Parametric Knowledge Conflicts in LLMs

Context-parametric conflicts occur when LLMs exhibit ambiguity when contextual knowledge contradicts their parametric knowledge. This is a critical issue in modern LLM applications.

### Overview of the Problem

These conflicts are particularly prevalent in real-world applications, especially in context-heavy LLM systems like retrieval-augmented generation (RAG), LLM agents, and tool-augmented LLMs. Such contextual knowledge can include information that conflicts with the parametric knowledge of the model, which may result in undesire
…[truncated 1159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T13:30:14.416218+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xie Jian \"Adaptive Chameleon or Stubborn Sloth\" ConflictQA arxiv 2023",
  "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xie Jian \"Adaptive Chameleon or Stubborn Sloth\" ConflictQA arxiv 2023",
    "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-22T13:30:14.416385+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Knowledge Conflicts for LLMs: A Survey\" Xu et al. 2024 arxiv",
  "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Knowledge Conflicts for LLMs: A Survey\" Xu et al. 2024 arxiv",
    "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T13:30:14.416570+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Beneath the Surface of Consistency\" cross-lingual knowledge representation sharing LLMs arxiv 2024",
  "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Beneath the Surface of Consistency\" cross-lingual knowledge representation sharing LLMs arxiv 2024",
    "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T13:30:14.416731+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models\" 2024 arxiv",
  "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models\" 2024 arxiv",
    "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-22T13:30:14.416934+00:00_

Web search results for query: "Xie Jian "Adaptive Chameleon or Stubborn Sloth" ConflictQA arxiv 2023"

Links: [{"title":"[2305.13300] Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts","url":"https://arxiv.org/abs/2305.13300"},{"title":"[PDF] Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Adaptive-Chameleon-or-Stubborn-Sloth:-Revealing-the-Xie-Zhang/10f829a80a7ee0cdb16307f04e206133d75f81da"},{"title":"Computation and Language May 2023","url":"http://arxiv.org/list/cs.CL/2023-05?skip=1025&show=2000"},{"title":"Chameleon: Adaptive Fault Tolerance for Distributed Training via...","url":"https://arxiv.org/abs/2508.21613"},{"title":"An inductive bias for slowly changing features in human reinforcement learning","url":"https://www.biorxiv.org/content/10.1101/2024.01.24.576910.full.pdf"},{"title":"To mask, or not to mask, Alice and Bob’s dating dilemma","url":"https://www.medrxiv.org/content/10.1101/2022.04.14.22273886.full.pdf"},{"title":"Chameleon: Adaptive Code Optimization for Expedited Deep Neural Network   Compilation","url":"https://arxiv.org/pdf/2001.08743"},{"title":"[2411.17741] Chameleon: Adaptive Caching and Scheduling for Many-Adapter LLM Inference Environments","url":"https://arxiv.org/abs/2411.17741"},{"title":"Stochastic Chameleons: Irrelevant Context Hallucinations Reveal Class-Based (Mis)Generalization in LLMs","url":"https://arxiv.org/html/2505.22630v2"}]

I found the paper you're looking for! Here are the key details:

**Title:** "Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts"

**Authors:** Jian Xie, Kai Zhang, Jiangjie Chen, Renze Lou, and Yu Su

**Publication:** International Conference on Learning Representations, 2023

**ArXiv ID:** 2305.13300

**Overview:** The paper presents the first comprehensive and 
…[truncated 638 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T13:30:14.417156+00:00_

Web search results for query: ""Knowledge Conflicts for LLMs: A Survey" Xu et al. 2024 arxiv"

Links: [{"title":"Taming Knowledge Conflicts in Language Models","url":"https://arxiv.org/html/2503.10996v1"},{"title":"Knowledge Conflicts for LLMs: A Survey - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.486/"},{"title":"Assessing and Mitigating Medical Knowledge Drift and Conflicts in Large Language Models","url":"https://arxiv.org/html/2505.07968"},{"title":"Benchmarking Multimodal Knowledge Conflict for Large Multimodal Models","url":"https://arxiv.org/html/2505.19509v1"},{"title":"What External Knowledge is Preferred by LLMs? Characterizing and Exploring Chain of Evidence in Imperfect Context","url":"https://arxiv.org/html/2412.12632v1"},{"title":"[2403.08319] Knowledge Conflicts for LLMs: A Survey","url":"https://arxiv.org/abs/2403.08319"},{"title":"[2403.08319v2] Knowledge Conflicts for LLMs: A Survey","url":"https://arxiv.org/abs/2403.08319v2"},{"title":"Knowledge Conflicts for LLMs: A Survey","url":"https://arxiv.org/html/2403.08319v2"}]

I found the paper! The paper "Knowledge Conflicts for LLMs: A Survey" by Xu et al. was published in the Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP 2024).

The survey provides an in-depth analysis of knowledge conflicts for large language models, highlighting the complex challenges they encounter when blending contextual and parametric knowledge. The focus is on three categories of knowledge conflicts: context-memory, inter-context, and intra-memory conflict. These conflicts can significantly impact the trustworthiness and performance of LLMs, especially in real-world applications where noise and misinformation are common.

Additionally, the paper is available on arXiv as preprint arXiv:2403.08319.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T13:30:14.417323+00:00_

Web search results for query: ""Beneath the Surface of Consistency" cross-lingual knowledge representation sharing LLMs arxiv 2024"

Links: [{"title":"[PDF] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/54a2e0dad730c1a955c66f3568a3fa0dca400225"},{"title":"[2408.10646v1] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/abs/2408.10646v1"},{"title":"[2408.10646] Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/abs/2408.10646"},{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs","url":"https://arxiv.org/html/2408.10646v1"},{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge","url":"https://arxiv.org/pdf/2408.10646"},{"title":"Computation and Language Aug 2024","url":"https://arxiv.org/list/cs.CL/2024-08?skip=540&show=2000"},{"title":"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.475/"}]

I found the paper! Here's what I discovered:

## Paper Details

**"Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs"** is authored by Maxim Ifergan, Leshem Choshen, Roee Aharoni, Idan Szpektor, and Omri Abend, published on ArXiv on August 20, 2024 (arxiv ID: 2408.10646).

## Key Findings

The research explores an important distinction in how LLMs handle factual knowledge across languages:

- High consistency does not necessarily imply shared representation, particularly for languages with different scripts. Moreover, script similarity is a dominant factor in representation sharing.

- The work explores multilingual factual knowledge through two aspects: the
…[truncated 492 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T13:30:14.417477+00:00_

Web search results for query: ""Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models" 2024 arxiv"

Links: [{"title":"[2407.01358] Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://arxiv.org/abs/2407.01358"},{"title":"Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language   Models","url":"https://arxiv.org/pdf/2407.01358"},{"title":"Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://arxiv.org/html/2407.01358v1"},{"title":"Understanding Cross-Lingual Inconsistency in Large ...","url":"https://arxiv.org/pdf/2505.13141"},{"title":"ECLeKTic: a Novel Challenge Set for Evaluation of Cross-Lingual Knowledge Transfer","url":"https://arxiv.org/html/2502.21228v1"}]

Perfect! I found the paper you're looking for. Here are the results:

**Paper Found:** "Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models" by Xiaolin Xing and 5 other authors

**arXiv Link:** https://arxiv.org/abs/2407.01358

**Publication Date:** July 1, 2024

**Summary:** This paper investigates cross-lingual inconsistencies observed in Large Language Models such as ChatGPT, Llama, and Baichuan, which often exhibit significant inconsistencies when processing the same concepts across different languages.

The study proposes an innovative evaluation method for Cross-lingual Semantic Consistency (xSC) using the LaBSE model, and introduces metrics for Cross-lingual Accuracy Consistency (xAC) and Cross-lingual Timeliness Consistency (xTC) to comprehensively assess the models' performance regarding semantic, accuracy, and timeliness inconsistencies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T13:30:14.417651+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2305.13300 \"Adaptive Chameleon or Stubborn Sloth\" venue ICLR EMNLP publication",
  "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2305.13300 \"Adaptive Chameleon or Stubborn Sloth\" venue ICLR EMNLP publication",
    "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org', 'openreview.net']"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-22T13:30:14.417780+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Knowledge Conflicts for LLMs: A Survey\" authors Rongwu Xu Zehan Qi 2024",
  "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Knowledge Conflicts for LLMs: A Survey\" authors Rongwu Xu Zehan Qi 2024",
    "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T13:30:14.417944+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Taming Knowledge Conflicts in Language Models\" 2025 arxiv authors venue",
  "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Taming Knowledge Conflicts in Language Models\" 2025 arxiv authors venue",
    "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T13:30:14.418097+00:00_

Web search results for query: "arxiv 2305.13300 "Adaptive Chameleon or Stubborn Sloth" venue ICLR EMNLP publication"

Links: [{"title":"[2305.13300] Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts","url":"https://arxiv.org/abs/2305.13300"},{"title":"arXiv:2305.13300v4 [cs.CL] 27 Feb 2024","url":"https://arxiv.org/pdf/2305.13300"},{"title":"Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts. | Semantic Scholar","url":"https://www.semanticscholar.org/search?q=Adaptive+Chameleon+or+Stubborn+Sloth:+Revealing+the+Behavior+of+Large+Language+Models+in+Knowledge+Conflicts."},{"title":"Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts | OpenReview","url":"https://openreview.net/forum?id=auKAUJZMO6"},{"title":"[PDF] Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Adaptive-Chameleon-or-Stubborn-Sloth:-Revealing-the-Xie-Zhang/10f829a80a7ee0cdb16307f04e206133d75f81da"},{"title":"Adaptive Chameleon or Stubborn Sloth:","url":"https://openreview.net/pdf?id=auKAUJZMO6"},{"title":"Chameleon: A Data-Efficient Generalist for Dense Visual Prediction in the Wild","url":"https://arxiv.org/html/2404.18459v1"}]

Based on the search results, I found the information about arxiv 2305.13300:

The paper "Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts" was published as a conference paper at ICLR 2024.

The paper was authored by Jian Xie and 4 other authors (including Kai Zhang, Jiangjie Chen, Renze Lou, and Yu Su, based on the citation information found). The paper presents the first comprehensive and controlled investigation into the behavior of LLMs when encountering knowledge conflicts, investigating how receptive LLMs are to external
…[truncated 183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-22T13:30:14.418268+00:00_

Web search results for query: ""Knowledge Conflicts for LLMs: A Survey" authors Rongwu Xu Zehan Qi 2024"

Links: [{"title":"[2403.08319] Knowledge Conflicts for LLMs: A Survey","url":"https://arxiv.org/abs/2403.08319"},{"title":"[2403.08319v2] Knowledge Conflicts for LLMs: A Survey","url":"https://arxiv.org/abs/2403.08319v2"},{"title":"[PDF] Knowledge Conflicts for LLMs: A Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ab8e6df5001dbb9b48445220099425aff536b3e8"},{"title":"Knowledge Conflicts for LLMs: A Survey - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.486/"},{"title":"Knowledge Conflicts for LLMs: A Survey","url":"https://arxiv.org/html/2403.08319v2"},{"title":"arXiv:2404.16032v1 [cs.LG] 24 Apr 2024","url":"https://arxiv.org/pdf/2404.16032v1"},{"title":"What External Knowledge is Preferred by LLMs? Characterizing and Exploring Chain of Evidence in Imperfect Context","url":"https://arxiv.org/html/2412.12632v1"},{"title":"ConflictBank: A Benchmark for Evaluating Knowledge Conflicts in Large Language Models","url":"https://arxiv.org/html/2408.12076v1"},{"title":"Benchmarking Multimodal Knowledge Conflict for Large Multimodal Models","url":"https://arxiv.org/html/2505.19509v1"}]

I found the paper you're looking for! Here are the details:

**Title:** Knowledge Conflicts for LLMs: A Survey

**Authors:** Rongwu Xu, Zehan Qi, Zhijiang Guo, Cunxiang Wang, Hongru Wang, Yue Zhang, Wei Xu

**Publication Details:** Published in Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 8541–8565, Miami, Florida, USA

**Submission Timeline:** Submitted on 13 Mar 2024 (v1), last revised 22 Jun 2024 (v2)

**Overview:** This survey provides an in-depth analysis of knowledge conflicts for large language models (LLMs), highlighting the complex challenges they encounter when blending contextual and parametric knowledge.

**Focus Areas:** The survey focuses on three categories of knowledge conflicts: cont
…[truncated 400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T13:30:14.418436+00:00_

Web search results for query: ""Taming Knowledge Conflicts in Language Models" 2025 arxiv authors venue"

Links: [{"title":"Taming Knowledge Conflicts in Language Models","url":"https://arxiv.org/pdf/2503.10996"},{"title":"Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models","url":"https://arxiv.org/html/2601.09445v1"},{"title":"[2503.10996] Taming Knowledge Conflicts in Language Models","url":"https://arxiv.org/abs/2503.10996"},{"title":"LLM Microscope: What Model Internals Reveal About Answer Correctness and Context Utilization","url":"https://arxiv.org/html/2510.04013v1"},{"title":"Task Matters: Knowledge Requirements Shape LLM Responses to Context–Memory Conflict","url":"https://arxiv.org/html/2506.06485v3"},{"title":"Machine Learning Mar 2025","url":"https://arxiv.org/list/cs.LG/2025-03?skip=2800&show=250"},{"title":"COMPASS: Context-Modulated PID Attention Steering ...","url":"https://arxiv.org/pdf/2511.14776"}]

Based on the search results, here is the information about the paper "Taming Knowledge Conflicts in Language Models":

**Authors:** Gaotang Li, Yuzhong Chen, and Hanghang Tong

**Venue:** Forty-second International Conference on Machine Learning, ICML 2025, Vancouver, BC, Canada, July 13-19, 2025

**ArXiv ID:** arXiv:2503.10996, 2025

**Presentation Type:** ICML 2025 (Spotlight)


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T13:30:14.418614+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2407.01358 Xiaolin Xing cross-lingual inconsistency LLM authors venue published",
  "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2407.01358 Xiaolin Xing cross-lingual inconsistency LLM authors venue published",
    "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T13:30:14.418756+00:00_

Web search results for query: "arxiv 2407.01358 Xiaolin Xing cross-lingual inconsistency LLM authors venue published"

Links: [{"title":"[2407.01358] Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://arxiv.org/abs/2407.01358"},{"title":"Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models","url":"https://arxiv.org/html/2407.01358v1"},{"title":"Align, Generate, Learn: A Novel Closed-Loop Framework for Cross-Lingual   In-Context Learning","url":"https://arxiv.org/pdf/2412.08955"},{"title":"Cross-Lingual Pitfalls: Automatic Probing Cross-Lingual Weakness of Multilingual Large Language Models","url":"https://arxiv.org/pdf/2505.18673"},{"title":"Toward Cross-Lingual Definition Generation for Language Learners","url":"https://arxiv.org/pdf/2010.05533"},{"title":"On cross-lingual retrieval with multilingual text encoders","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9090691/"},{"title":"Prompt-Tuning Can Be Much Better Than Fine-Tuning on Cross-lingual   Understanding With Multilingual Language Models","url":"https://arxiv.org/pdf/2210.12360"}]

Based on the search results, here is the information about arxiv paper 2407.01358:

**Title:** Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models

**Authors:** Xiaolin Xing, Zhiwei He, Haoyu Xu, Xing Wang, Rui Wang, and Yu Hong from Soochow University, Shanghai Jiao Tong University, and Tencent AI Lab

**Published:** Submitted on July 1, 2024

**Venue:** arXiv (Computer Science category)

**Focus:** The paper investigates cross-lingual inconsistencies in Large Language Models (LLMs), such as ChatGPT, Llama, and Baichuan, which often exhibit significant inconsistencies when processing the same concepts across different languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T13:30:14.418934+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2406.16135 \"Crosslingual Capabilities and Knowledge Barriers\" authors venue EMNLP ACL published",
  "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2406.16135 \"Crosslingual Capabilities and Knowledge Barriers\" authors venue EMNLP ACL published",
    "allowed_domains": "['arxiv.org', 'aclanthology.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T13:30:14.419091+00:00_

Web search results for query: "arxiv 2406.16135 "Crosslingual Capabilities and Knowledge Barriers" authors venue EMNLP ACL published"

Links: [{"title":"[2406.16135] Crosslingual Capabilities and Knowledge Barriers in Multilingual Large Language Models","url":"https://arxiv.org/abs/2406.16135"},{"title":"Computer Science Jun 2024","url":"https://arxiv.org/list/cs/2024-06?skip=7725&show=2000"},{"title":"1 Cross-linguistic disagreement as a conflict of semantic alignment norms in","url":"https://arxiv.org/pdf/2503.04792"},{"title":"Machine Learning Jun 2024","url":"https://web3.arxiv.org/list/cs.LG/2024-06?skip=3320&show=5"},{"title":"AdaCoT: Rethinking Cross-Lingual Factual Reasoning through Adaptive Chain-of-Thought","url":"https://arxiv.org/html/2501.16154v1"},{"title":"Tracing Multilingual Factual Knowledge Acquisition in Pretraining","url":"https://arxiv.org/html/2505.14824"},{"title":"AdaMCoT: Rethinking Cross-Lingual Factual Reasoning through Adaptive Multilingual Chain-of-Thought","url":"https://arxiv.org/html/2501.16154v3"},{"title":"Language Models’ Factuality Depends on the Language of Inquiry","url":"https://arxiv.org/html/2502.17955v1"}]

Based on the search results, here's what I found about arxiv paper 2406.16135:

## Paper Information

**Title:** Crosslingual Capabilities and Knowledge Barriers in Multilingual Large Language Models

**Authors:** Lynn Chua, Badih Ghazi, Yangsibo Huang, Pritish Kamath, Ravi Kumar, Pasin Manurangsi, Amer Sinha, Chulin Xie, Chiyuan Zhang

**Subject Areas:** Computation and Language (cs.CL); Machine Learning (cs.LG)

## Paper Summary

The paper observes that while multilingual large language models show promising surface-level crosslingual abilities on machine translation and embedding space analyses, they struggle with deeper crosslingual knowledge transfer, revealing a crosslingual knowledge barrier in both general (MMLU benchmark) and domain-specific (Harry Potter quiz and TOFU benchmark) contexts.

The researchers propo
…[truncated 463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T13:30:14.419296+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml, datetime\n\npath = 'literature_map.yaml'\nwith open(path) as f:\n    data = yaml.safe_load(f)\n\nnow = '2026-05-22T14:00:00Z'\n\n# === Cluster 1: Knowledge Conflict Detection ===\n\n# 1. ConflictQA original paper (MUST CITE)\ndata['papers']['xie2024adaptive'] = {\n    'title': 'Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts',\n    'authors': ['Xie, J.', 'Zhang, K.', 'Chen, J.', 'Lou, R.', 'Su, Y.'],\n    'year': 2024,\n    'venue': 'ICLR 2024',\n    'url': 'https://arxiv.org/abs/2305.13300',\n    'doi': '',\n    'bibtex_key': 'xie2024adaptive',\n    'category': 'knowledge-conflict',\n    'role': 'foundation',\n    'relevance': 'Introduces ConflictQA benchmark (PopQA + StrategyQA based) for studying LLM behavior under context-parametric knowledge conflicts. Our primary evaluation dataset.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\n# 2. Knowledge Conflicts Survey\ndata['papers']['xu2024knowledge'] = {\n    'title': 'Knowledge Conflicts for LLMs: A Survey',\n    'authors': ['Xu, R.', 'Qi, Z.', 'Guo, Z.', 'Wang, C.', 'Wang, H.', 'Zhang, Y.', 'Xu, W.'],\n    'year': 2024,\n    'venue': 'EMNLP 2024',\n    'url': 'https://arxiv.org/abs/2403.08319',\n    'doi': '',\n    'bibtex_key': 'xu2024knowledge',\n    'category': 'knowledge-conflict',\n    'role': 'foundation',\n    'relevance': 'Comprehensive survey of context-memory, inter-context, and intra-memory knowledge conflicts in LLMs. Defines the taxonomy our work builds on.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\n# 3. Taming Knowledge Conflicts\ndata['papers']['li2025taming'] = {\n    'title': 'Taming Knowledge Conflicts in Language Models',\n    'authors': ['Li, G.', 'Chen, Y.', 'Tong, H.'],\n    'year': 2025,\n    'venue': 'ICML 2025 (Spotlight)',\n    'url': 'https://arxiv.org/abs/2503.10996',\n    'doi': '',\n    'bibtex_key': 'li2025taming',\n    'category': 'knowledge-conflict',\n    'role': 'direct-competitor',\n    'relevance': 'Proposes conflict resolution framework for LLMs. Provides resolution baselines our mechanistic approach complements.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\n# === Cluster 2: Cross-lingual Conflict ===\n\n# 4. Beneath the Surface of Consistency\ndata['papers']['ifergan2024beneath'] = {\n    'title': 'Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs',\n    'authors': ['Ifergan, M.', 'Choshen, L.', 'Aharoni, R.', 'Szpektor, I.', 'Abend, O.'],\n    'year': 2024,\n    'venue': 'Findings of NAACL 2025',\n    'url': 'https://arxiv.org/abs/2408.10646',\n    'doi': '',\n    'bibtex_key': 'ifergan2024beneath',\n    'category': 'cross-lingual-conflict',\n    'role': 'foundation',\n    'relevance': 'Shows cross-lingual answer consistency does not imply shared representation; script similarity dominates sharing. Directly motivates our probing approach to test whether conflict signals share representations across languages.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\n# 5. Evaluating Knowledge-based Cross-lingual Inconsistency\ndata['papers']['xing2024evaluating'] = {\n    'title': 'Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models',\n    'authors': ['Xing, X.', 'He, Z.', 'Xu, H.', 'Wang, X.', 'Wang, R.', 'Hong, Y.'],\n    'year': 2024,\n    'venue': 'arXiv',\n    'url': 'https://arxiv.org/abs/2407.01358',\n    'doi': '',\n    'bibtex_key': 'xing2024evaluating',\n    'category': 'cross-lingual-conflict',\n    'role': 'peripheral',\n    'relevance': 'Proposes cross-lingual semantic/accuracy/timeliness consistency metrics (xSC, xAC, xTC) for evaluating multilingual LLM inconsistency. Provides evaluation methodology relevant to our cross-lingual conflict measurement.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\n# Update meta\ndata['meta']['total_papers'] = len(data['papers'])\ndata['meta']['last_updated'] = now\n\nwith open(path, 'w') as f:\n    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)\n\nprint(f'Done. Total papers: {data[\\\"meta\\\"][\\\"total_papers\\\"]}')\nfor k in ['xie2024adaptive', 'xu2024knowledge', 'li2025taming', 'ifergan2024beneath', 'xing2024evaluating']:\n    print(f'  + {k}: {data[\\\"papers\\\"][k][\\\"title'][:60]}...')\n\"\n",
  "description": "Update literature_map.yaml with 5 new papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260522T132715",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml, datetime\n\npath = 'literature_map.yaml'\nwith open(path) as f:\n    data = yaml.safe_load(f)\n\nnow = '2026-05-22T14:00:00Z'\n\n# === Cluster 1: Knowledge Conflict Detection ===\n\n# 1. ConflictQA original paper (MUST CITE)\ndata['papers']['xie2024adaptive'] = {\n    'title': 'Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts',\n    'authors': ['Xie, J.', 'Zhang, K.', 'Chen, J.', 'Lou, R.', 'Su, Y.'],\n    'year': 2024,\n    'venue': 'ICLR 2024',\n    'url': 'https://arxiv.org/abs/2305.13300',\n    'doi': '',\n    'bibtex_key': 'xie2024adaptive',\n    'category': 'knowledge-conflict',\n    'role': 'foundation',\n    'relevance': 'Introduces ConflictQA benchmark (PopQA + StrategyQA based) for studying LLM behavior under context-parametric knowledge conflicts. Our primary evaluation dataset.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\n# 2. Knowledge Conflicts Survey\ndata['papers']['xu2024knowledge'] = {\n    'title': 'Knowledge Conflicts for LLMs: A Survey',\n    'authors': ['Xu, R.', 'Qi, Z.', 'Guo, Z.', 'Wang, C.', 'Wang, H.', 'Zhang, Y.', 'Xu, W.'],\n    'year': 2024,\n    'venue': 'EMNLP 2024',\n    'url': 'https://arxiv.org/abs/2403.08319',\n    'doi': '',\n    'bibtex_key': 'xu2024knowledge',\n    'category': 'knowledge-conflict',\n    'role': 'foundation',\n    'relevance': 'Comprehensive survey of context-memory, inter-context, and intra-memory knowledge conflicts in LLMs. Defines the taxonomy our work builds on.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\n# 3. Taming Knowledge Conflicts\ndata['papers']['li2025taming'] = {\n    'title': 'Taming Knowledge Conflicts in Language Models',\n    'authors': ['Li, G.', 'Chen, Y.', 'Tong, H.'],\n    'year': 2025,\n    'venue': 'ICML 2025 (Spotlight)',\n    'url': 'https://arxiv.org/abs/2503.10996',\n    'doi': '',\n    'bibtex_key': 'li2025taming',\n    'category': 'knowledge-conflict',\n    'role': 'direct-competitor',\n    'relevance': 'Proposes conflict resolution framework for LLMs. Provides resolution baselines our mechanistic approach complements.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\n# === Cluster 2: Cross-lingual Conflict ===\n\n# 4. Beneath the Surface of Consistency\ndata['papers']['ifergan2024beneath'] = {\n    'title': 'Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs',\n    'authors': ['Ifergan, M.', 'Choshen, L.', 'Aharoni, R.', 'Szpektor, I.', 'Abend, O.'],\n    'year': 2024,\n    'venue': 'Findings of NAACL 2025',\n    'url': 'https://arxiv.org/abs/2408.10646',\n    'doi': '',\n    'bibtex_key': 'ifergan2024beneath',\n    'category': 'cross-lingual-conflict',\n    'role': 'foundation',\n    'relevance': 'Shows cross-lingual answer consistency does not imply shared representation; script similarity dominates sharing. Directly motivates our probing approach to test whether conflict signals share representations across languages.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\n# 5. Evaluating Knowledge-based Cross-lingual Inconsistency\ndata['papers']['xing2024evaluating'] = {\n    'title': 'Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models',\n    'authors': ['Xing, X.', 'He, Z.', 'Xu, H.', 'Wang, X.', 'Wang, R.', 'Hong, Y.'],\n    'year': 2024,\n    'venue': 'arXiv',\n    'url': 'https://arxiv.org/abs/2407.01358',\n    'doi': '',\n    'bibtex_key': 'xing2024evaluating',\n    'category': 'cross-lingual-conflict',\n    'role': 'peripheral',\n    'relevance': 'Proposes cross-lingual semantic/accuracy/timeliness consistency metrics (xSC, xAC, xTC) for evaluating multilingual LLM inconsistency. Provides evaluation methodology relevant to our cross-lingual conflict measurement.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\n# Update meta\ndata['meta']['total_papers'] = len(data['papers'])\ndata['meta']['last_updated'] = now\n\nwith open(path, 'w') as f:\n    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)\n\nprint(f'Done. Total papers: {data[\\\"meta\\\"][\\\"total_papers\\\"]}')\nfor k in ['xie2024adaptive', 'xu2024knowledge', 'li2025taming', 'ifergan2024beneath', 'xing2024evaluating']:\n    print(f'  + {k}: {data[\\\"papers\\\"][k][\\\"title'][:60]}...')\n\"\n",
    "description": "Update literature_map.yaml with 5 new papers"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T13:30:14.419462+00:00_

Exit code 1
  File "&lt;string>", line 108
    print(f'  + {k}: {data["papers"][k]["title'][:60]}...')
                                        ^
SyntaxError: unterminated string literal (detected at line 108)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T13:30:14.419593+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\n\npath = 'literature_map.yaml'\nwith open(path) as f:\n    data = yaml.safe_load(f)\n\nnow = '2026-05-22T14:00:00Z'\n\ndata['papers']['xie2024adaptive'] = {\n    'title': 'Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts',\n    'authors': ['Xie, J.', 'Zhang, K.', 'Chen, J.', 'Lou, R.', 'Su, Y.'],\n    'year': 2024,\n    'venue': 'ICLR 2024',\n    'url': 'https://arxiv.org/abs/2305.13300',\n    'doi': '',\n    'bibtex_key': 'xie2024adaptive',\n    'category': 'knowledge-conflict',\n    'role': 'foundation',\n    'relevance': 'Introduces ConflictQA benchmark (PopQA + StrategyQA based) for studying LLM behavior under context-parametric knowledge conflicts. Our primary evaluation dataset.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\ndata['papers']['xu2024knowledge'] = {\n    'title': 'Knowledge Conflicts for LLMs: A Survey',\n    'authors': ['Xu, R.', 'Qi, Z.', 'Guo, Z.', 'Wang, C.', 'Wang, H.', 'Zhang, Y.', 'Xu, W.'],\n    'year': 2024,\n    'venue': 'EMNLP 2024',\n    'url': 'https://arxiv.org/abs/2403.08319',\n    'doi': '',\n    'bibtex_key': 'xu2024knowledge',\n    'category': 'knowledge-conflict',\n    'role': 'foundation',\n    'relevance': 'Comprehensive survey of context-memory, inter-context, and intra-memory knowledge conflicts in LLMs. Defines the taxonomy our work builds on.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\ndata['papers']['li2025taming'] = {\n    'title': 'Taming Knowledge Conflicts in Language Models',\n    'authors': ['Li, G.', 'Chen, Y.', 'Tong, H.'],\n    'year': 2025,\n    'venue': 'ICML 2025 (Spotlight)',\n    'url': 'https://arxiv.org/abs/2503.10996',\n    'doi': '',\n    'bibtex_key': 'li2025taming',\n    'category': 'knowledge-conflict',\n    'role': 'direct-competitor',\n    'relevance': 'Proposes conflict resolution framework for LLMs. Provides resolution baselines our mechanistic approach complements.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\ndata['papers']['ifergan2024beneath'] = {\n    'title': 'Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs',\n    'authors': ['Ifergan, M.', 'Choshen, L.', 'Aharoni, R.', 'Szpektor, I.', 'Abend, O.'],\n    'year': 2024,\n    'venue': 'Findings of NAACL 2025',\n    'url': 'https://arxiv.org/abs/2408.10646',\n    'doi': '',\n    'bibtex_key': 'ifergan2024beneath',\n    'category': 'cross-lingual-conflict',\n    'role': 'foundation',\n    'relevance': 'Shows cross-lingual answer consistency does not imply shared representation; script similarity dominates sharing. Directly motivates our probing approach to test whether conflict signals share representations across languages.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\ndata['papers']['xing2024evaluating'] = {\n    'title': 'Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models',\n    'authors': ['Xing, X.', 'He, Z.', 'Xu, H.', 'Wang, X.', 'Wang, R.', 'Hong, Y.'],\n    'year': 2024,\n    'venue': 'arXiv',\n    'url': 'https://arxiv.org/abs/2407.01358',\n    'doi': '',\n    'bibtex_key': 'xing2024evaluating',\n    'category': 'cross-lingual-conflict',\n    'role': 'peripheral',\n    'relevance': 'Proposes cross-lingual semantic/accuracy/timeliness consistency metrics (xSC, xAC, xTC) for evaluating multilingual LLM inconsistency. Provides evaluation methodology relevant to our cross-lingual conflict measurement.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\ndata['meta']['total_papers'] = len(data['papers'])\ndata['meta']['last_updated'] = now\n\nwith open(path, 'w') as f:\n    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)\n\ntotal = data['meta']['total_papers']\nnew_keys = ['xie2024adaptive', 'xu2024knowledge', 'li2025taming', 'ifergan2024beneath', 'xing2024evaluating']\nprint(f'Total papers: {total}')\nfor k in new_keys:\n    t = data['papers'][k]['title'][:65]\n    print(f'  + {k}: {t}...')\n\"\n",
  "description": "Update literature_map.yaml with 5 new papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260522T132715",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml\n\npath = 'literature_map.yaml'\nwith open(path) as f:\n    data = yaml.safe_load(f)\n\nnow = '2026-05-22T14:00:00Z'\n\ndata['papers']['xie2024adaptive'] = {\n    'title': 'Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts',\n    'authors': ['Xie, J.', 'Zhang, K.', 'Chen, J.', 'Lou, R.', 'Su, Y.'],\n    'year': 2024,\n    'venue': 'ICLR 2024',\n    'url': 'https://arxiv.org/abs/2305.13300',\n    'doi': '',\n    'bibtex_key': 'xie2024adaptive',\n    'category': 'knowledge-conflict',\n    'role': 'foundation',\n    'relevance': 'Introduces ConflictQA benchmark (PopQA + StrategyQA based) for studying LLM behavior under context-parametric knowledge conflicts. Our primary evaluation dataset.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\ndata['papers']['xu2024knowledge'] = {\n    'title': 'Knowledge Conflicts for LLMs: A Survey',\n    'authors': ['Xu, R.', 'Qi, Z.', 'Guo, Z.', 'Wang, C.', 'Wang, H.', 'Zhang, Y.', 'Xu, W.'],\n    'year': 2024,\n    'venue': 'EMNLP 2024',\n    'url': 'https://arxiv.org/abs/2403.08319',\n    'doi': '',\n    'bibtex_key': 'xu2024knowledge',\n    'category': 'knowledge-conflict',\n    'role': 'foundation',\n    'relevance': 'Comprehensive survey of context-memory, inter-context, and intra-memory knowledge conflicts in LLMs. Defines the taxonomy our work builds on.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\ndata['papers']['li2025taming'] = {\n    'title': 'Taming Knowledge Conflicts in Language Models',\n    'authors': ['Li, G.', 'Chen, Y.', 'Tong, H.'],\n    'year': 2025,\n    'venue': 'ICML 2025 (Spotlight)',\n    'url': 'https://arxiv.org/abs/2503.10996',\n    'doi': '',\n    'bibtex_key': 'li2025taming',\n    'category': 'knowledge-conflict',\n    'role': 'direct-competitor',\n    'relevance': 'Proposes conflict resolution framework for LLMs. Provides resolution baselines our mechanistic approach complements.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\ndata['papers']['ifergan2024beneath'] = {\n    'title': 'Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in LLMs',\n    'authors': ['Ifergan, M.', 'Choshen, L.', 'Aharoni, R.', 'Szpektor, I.', 'Abend, O.'],\n    'year': 2024,\n    'venue': 'Findings of NAACL 2025',\n    'url': 'https://arxiv.org/abs/2408.10646',\n    'doi': '',\n    'bibtex_key': 'ifergan2024beneath',\n    'category': 'cross-lingual-conflict',\n    'role': 'foundation',\n    'relevance': 'Shows cross-lingual answer consistency does not imply shared representation; script similarity dominates sharing. Directly motivates our probing approach to test whether conflict signals share representations across languages.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\ndata['papers']['xing2024evaluating'] = {\n    'title': 'Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models',\n    'authors': ['Xing, X.', 'He, Z.', 'Xu, H.', 'Wang, X.', 'Wang, R.', 'Hong, Y.'],\n    'year': 2024,\n    'venue': 'arXiv',\n    'url': 'https://arxiv.org/abs/2407.01358',\n    'doi': '',\n    'bibtex_key': 'xing2024evaluating',\n    'category': 'cross-lingual-conflict',\n    'role': 'peripheral',\n    'relevance': 'Proposes cross-lingual semantic/accuracy/timeliness consistency metrics (xSC, xAC, xTC) for evaluating multilingual LLM inconsistency. Provides evaluation methodology relevant to our cross-lingual conflict measurement.',\n    'verified': True,\n    'added_by': 'paper-agent-lit-search',\n    'added_at': now\n}\n\ndata['meta']['total_papers'] = len(data['papers'])\ndata['meta']['last_updated'] = now\n\nwith open(path, 'w') as f:\n    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)\n\ntotal = data['meta']['total_papers']\nnew_keys = ['xie2024adaptive', 'xu2024knowledge', 'li2025taming', 'ifergan2024beneath', 'xing2024evaluating']\nprint(f'Total papers: {total}')\nfor k in new_keys:\n    t = data['papers'][k]['title'][:65]\n    print(f'  + {k}: {t}...')\n\"\n",
    "description": "Update literature_map.yaml with 5 new papers"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T13:30:14.419750+00:00_

Total papers: 15
  + xie2024adaptive: Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of L...
  + xu2024knowledge: Knowledge Conflicts for LLMs: A Survey...
  + li2025taming: Taming Knowledge Conflicts in Language Models...
  + ifergan2024beneath: Beneath the Surface of Consistency: Exploring Cross-lingual Knowl...
  + xing2024evaluating: Evaluating Knowledge-based Cross-lingual Inconsistency in Large L...

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260522T132715",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-22T13:30:14.419924+00:00_

已追加 5 篇论文到 `literature_map.yaml`（10 → 15 篇）。

**Cluster 1: Knowledge Conflict Detection (+3)**

| bibtex_key | 论文 | Venue | 角色 |
|---|---|---|---|
| `xie2024adaptive` | Adaptive Chameleon or Stubborn Sloth (ConflictQA) | ICLR 2024 | foundation — 我们使用的数据集原始论文 |
| `xu2024knowledge` | Knowledge Conflicts for LLMs: A Survey | EMNLP 2024 | foundation — 定义 context-memory/inter-context/intra-memory 分类体系 |
| `li2025taming` | Taming Knowledge Conflicts in Language Models | ICML 2025 Spotlight | direct-competitor — 冲突解决框架，我们的机制方法与之互补 |

**Cluster 2: Cross-lingual Conflict (+2)**

| bibtex_key | 论文 | Venue | 角色 |
|---|---|---|---|
| `ifergan2024beneath` | Beneath the Surface of Consistency | NAACL 2025 Findings | foundation — 跨语言一致性 ≠ 共享表征，脚本相似性主导，直接支撑我们的 probing 动机 |
| `xing2024evaluating` | Evaluating Knowledge-based Cross-lingual Inconsistency | arXiv 2024 | peripheral — 提出 xSC/xAC/xTC 跨语言一致性度量 |

所有 URL 均为真实 arXiv 链接，已验证存在。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_20260522T132715"
}
```

</details>

---
