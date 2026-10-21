# paper writing introduction

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_paper_writing_introduction_20260516T090825.log`
- **Structured JSON:** [`a9cda1130cd8b364af72.json`](../../sessions/a9/a9cda1130cd8b364af72.json)

## Before a recorded user message

32 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__bootstrap_provenance",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__overleaf_init",
    "mcp__agent-ml-research__overleaf_pull",
    "mcp__agent-ml-research__overleaf_push",
    "mcp__agent-ml-research__overleaf_status",
    "mcp__agent-ml-research__overleaf_sync",
    "mcp__agent-ml-research__paper_agent_post_to_director",
    "mcp__agent-ml-research__paper_agent_request_review",
    "mcp__agent-ml-research__paper_compile_and_check",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "34a6a3f1-7d9d-4a14-82ea-09d640e858c4",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778931000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "3770675d-61bd-41e0-a609-96e5d05d4e51",
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b"
}
```

---

### Assistant

_source line 4_

Let me first read the existing introduction.tex and the LaTeX writing skill guide.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "c0e2f536-bb94-4c45-baa6-d12179042880",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X31usLgUq2tNqsXPwHGKy6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13298,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13298
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01E9NFZ98sacz5fUe1BKCmH1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "a3b468f6-ac20-48fa-a6b5-05444bbc183e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X31usLgUq2tNqsXPwHGKy6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13298,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13298
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T09:08:35.708Z_

<details><summary>↩ Tool result · `toolu_01E9NFZ98sacz5fUe1BKCmH1`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Large language models trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong performance on mathematical and logical reasoning~\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.
5	Structured pruning---removing entire attention heads or MLP channels---offers a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\citep{llmpruner2023,graspprune2026}.
6	However, structured pruning at moderate sparsity severely degrades reasoning ability, necessitating a post-pruning recovery stage.
7	\citet{selfhealing2025} show that RLVR-based recovery substantially outperforms SFT-based recovery for pruned reasoning models, establishing RLVR as the preferred recovery paradigm.
8	
9	Despite this, current approaches treat pruning and recovery as independent steps: pruning methods optimize for immediate post-pruning accuracy~\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\citep{selfhealing2025,paser2025}.
10	No prior work has studied whether the \emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning---or whether this interaction differs from SFT-based recovery.
11	This gap is consequential because RLVR and SFT impose fundamentally different functional demands on the retained architecture: \citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation.
12	The optimal set of structures to retain should therefore depend on the recovery paradigm.
13	
14	We hypothesize that \emph{functional overlap}---the degree to which a structure's computation is redundant with its within-layer peers---positively predicts RLVR recoverability.
15	If a pruned structure has high overlap with retained structures, RLVR can absorb its function through global policy optimization over the remaining architecture.
16	Conversely, structures with unique, non-redundant computations are difficult to recover once removed.
17	This yields what we term the \textbf{Redundancy Paradox}: the property that makes a structure functionally ``redundant''---high overlap with within-layer peers---is precisely the property that makes it most recoverable under RLVR, because reinforcement learning can redistribute its function through retained structures with similar representations.
18	\rasp{} exploits this by preferentially pruning high-overlap structures whose function can be absorbed, while protecting functionally unique structures whose contribution is irrecoverable once removed.
19	Importance-only pruning is blind to this distinction and may inadvertently remove unique structures critical for recovery.
20	
21	We propose \textbf{Recovery-Aware Structured Pruning (\rasp{})}, a three-stage framework that incorporates recoverability into the pruning decision.
22	In Stage~1, \rasp{} computes for each structure both a gradient-based importance score and a functional overlap score via intra-layer Centered Kernel Alignment (CKA;~\citealp{kornblith2019cka}).
23	In Stage~2, these are combined into a recovery-aware score $S(h) = I(h) \times (1 - F(h))^\alpha$ that protects structures which are both important \emph{and} functionally unique, while allowing removal of important-but-redundant structures whose function RLVR can redistribute.
24	In Stage~3, the pruned model undergoes a brief SFT warmup to restore generation competence, followed by GRPO-based RLVR recovery~\citep{shao2024grpo} to restore reasoning ability.
25	Unlike prior CKA-based pruning that uses inter-layer similarity for depth pruning~\citep{mpruner2024,lachance2024cka}, \rasp{} uses \emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability---a finer granularity optimizing for a fundamentally different objective.
26	
27	We evaluate \rasp{} on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} at 20\% structured sparsity.
28	At matched sparsity, \rasp{}-pruned models retain 29\% GSM8K~\citep{cobbe2021gsm8k} accuracy immediately after pruning, compared to 1\% for importance-only pruning ($N{=}100$, $p{<}0.0001$)---a 28-percentage-point advantage attributable to the recovery-aware scoring criterion.
29	After SFT warmup, importance-only pruning recovers to 64\% versus \rasp{}'s 57\%, consistent with the hypothesis that SFT preferentially benefits structures selected for immediate accuracy.
30	[TBD: GRPO results]
31	
32	Our contributions are:
33	\begin{enumerate}[nosep,leftmargin=*]
34	    \item We identify the \emph{Redundancy Paradox}---that functional redundancy, typically a signal for removal in standard pruning, is the property that enables RLVR recovery---and formalize it through intra-layer CKA-based functional overlap scoring.
35	    \item We propose \rasp{}, a recovery-aware pruning framework that integrates functional overlap into structural pruning decisions, achieving 29\% post-prune GSM8K accuracy versus 1\% for importance-only pruning at matched 20\% sparsity on DeepSeek-R1-Distill-Qwen-7B.
36	    \item [TBD: GRPO recovery results---contribution demonstrating that \rasp{}'s post-prune advantage translates to superior post-RLVR reasoning performance.]
37	    \item We provide evidence that the optimal pruning strategy is conditioned on the recovery paradigm: \rasp{} and importance-only pruning exhibit reversed relative advantages under SFT versus RLVR recovery [TBD: pending GRPO confirmation], supporting the notion of \emph{paradigm-conditioned prunability}.
38	\end{enumerate}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "62297646-3bca-4f3c-b5c2-e91ec7efbc91",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong performance on mathematical and logical reasoning~\\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.\nStructured pruning---removing entire attention heads or MLP channels---offers a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\\citep{llmpruner2023,graspprune2026}.\nHowever, structured pruning at moderate sparsity severely degrades reasoning ability, necessitating a post-pruning recovery stage.\n\\citet{selfhealing2025} show that RLVR-based recovery substantially outperforms SFT-based recovery for pruned reasoning models, establishing RLVR as the preferred recovery paradigm.\n\nDespite this, current approaches treat pruning and recovery as independent steps: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.\nNo prior work has studied whether the \\emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning---or whether this interaction differs from SFT-based recovery.\nThis gap is consequential because RLVR and SFT impose fundamentally different functional demands on the retained architecture: \\citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation.\nThe optimal set of structures to retain should therefore depend on the recovery paradigm.\n\nWe hypothesize that \\emph{functional overlap}---the degree to which a structure's computation is redundant with its within-layer peers---positively predicts RLVR recoverability.\nIf a pruned structure has high overlap with retained structures, RLVR can absorb its function through global policy optimization over the remaining architecture.\nConversely, structures with unique, non-redundant computations are difficult to recover once removed.\nThis yields what we term the \\textbf{Redundancy Paradox}: the property that makes a structure functionally ``redundant''---high overlap with within-layer peers---is precisely the property that makes it most recoverable under RLVR, because reinforcement learning can redistribute its function through retained structures with similar representations.\n\\rasp{} exploits this by preferentially pruning high-overlap structures whose function can be absorbed, while protecting functionally unique structures whose contribution is irrecoverable once removed.\nImportance-only pruning is blind to this distinction and may inadvertently remove unique structures critical for recovery.\n\nWe propose \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework that incorporates recoverability into the pruning decision.\nIn Stage~1, \\rasp{} computes for each structure both a gradient-based importance score and a functional overlap score via intra-layer Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}).\nIn Stage~2, these are combined into a recovery-aware score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important \\emph{and} functionally unique, while allowing removal of important-but-redundant structures whose function RLVR can redistribute.\nIn Stage~3, the pruned model undergoes a brief SFT warmup to restore generation competence, followed by GRPO-based RLVR recovery~\\citep{shao2024grpo} to restore reasoning ability.\nUnlike prior CKA-based pruning that uses inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability---a finer granularity optimizing for a fundamentally different objective.\n\nWe evaluate \\rasp{} on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} at 20\\% structured sparsity.\nAt matched sparsity, \\rasp{}-pruned models retain 29\\% GSM8K~\\citep{cobbe2021gsm8k} accuracy immediately after pruning, compared to 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$)---a 28-percentage-point advantage attributable to the recovery-aware scoring criterion.\nAfter SFT warmup, importance-only pruning recovers to 64\\% versus \\rasp{}'s 57\\%, consistent with the hypothesis that SFT preferentially benefits structures selected for immediate accuracy.\n[TBD: GRPO results]\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify the \\emph{Redundancy Paradox}---that functional redundancy, typically a signal for removal in standard pruning, is the property that enables RLVR recovery---and formalize it through intra-layer CKA-based functional overlap scoring.\n    \\item We propose \\rasp{}, a recovery-aware pruning framework that integrates functional overlap into structural pruning decisions, achieving 29\\% post-prune GSM8K accuracy versus 1\\% for importance-only pruning at matched 20\\% sparsity on DeepSeek-R1-Distill-Qwen-7B.\n    \\item [TBD: GRPO recovery results---contribution demonstrating that \\rasp{}'s post-prune advantage translates to superior post-RLVR reasoning performance.]\n    \\item We provide evidence that the optimal pruning strategy is conditioned on the recovery paradigm: \\rasp{} and importance-only pruning exhibit reversed relative advantages under SFT versus RLVR recovery [TBD: pending GRPO confirmation], supporting the notion of \\emph{paradigm-conditioned prunability}.\n\\end{enumerate}\n",
      "numLines": 39,
      "startLine": 1,
      "totalLines": 39
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01D6qSSYTTKNFXSuNGtGmrR3`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "c9fe0861-1a85-4a06-a56b-5d60ab603c06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X31usLgUq2tNqsXPwHGKy6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13298,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13298
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T09:08:35.778Z_

<details><summary>↩ Tool result · `toolu_01D6qSSYTTKNFXSuNGtGmrR3`</summary>

````text
1	---
2	name: latex-paper
3	description: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。
4	scope: global
5	tags:
6	- latex
7	- paper-writing
8	- academic
9	- citation
10	- submission
11	version: 1
12	roles:
13	- agent
14	- worker
15	---
16	
17	# LaTeX 论文写作全流程
18	
19	ML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。
20	
21	---
22	
23	## 1. 工作模式
24	
25	开始前选择模式：
26	
27	| 模式 | 说明 | 适用 |
28	|------|------|------|
29	| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |
30	| **Improve** | 改写已有章节，强化论证 | 修改稿 |
31	| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |
32	
33	---
34	
35	## 2. Claim-Evidence 方法论
36	
37	**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**
38	
39	### 2.1 一句话贡献
40	
41	在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。
42	
43	### 2.2 Claim-Evidence Map
44	
45	为每个 contribution 建立 claim→evidence 映射表：
46	
47	| Contribution | Claim | Evidence | Table/Figure |
48	|-------------|-------|----------|-------------|
49	| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |
50	| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |
51	| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |
52	
53	**没有直接证据支撑的 claim 必须删除或降级为 discussion。**
54	
55	### 2.3 章节起草顺序
56	
57	```
58	1. Introduction + Experiments（先确定 claim 和 evidence）
59	2. Method（评估问题稳定后再写细节）
60	3. Related Work
61	4. Abstract + Title（核心 claim 定型后最后写）
62	```
63	
64	### 2.4 Quality Gates
65	
66	投稿前必须通过：
67	- [ ] 前两段出现显式 novelty 声明
68	- [ ] 每个 contribution 有可验证的 evidence
69	- [ ] Abstract / Intro / Conclusion 的 claim 一致
70	- [ ] Limitations 真实且技术性诚实
71	- [ ] 审稿人两分钟内能识别 delta
72	
73	---
74	
75	## 3. 引用防幻觉（CRITICAL）
76	
77	**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**
78	
79	### 3.1 黄金法则
80	
81	```
82	IF 无法程序化获取引用:
83	    → 标记 [CITATION NEEDED] 或 \cite{PLACEHOLDER_verify}
84	    → 明确告知用户
85	    → 绝不编造看似合理的引用
86	```
87	
88	### 3.2 五步验证流程
89	
90	```
91	1. SEARCH  → Semantic Scholar API 搜索关键词
92	2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）
93	3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）
94	4. CHECK   → 确认你引用的 claim 确实出自该论文
95	5. ADD     → 加入 .bib 文件
96	```
97	
98	### 3.3 API 速查
99	
100	| API | 用途 | 限制 |
101	|-----|------|------|
102	| **Semantic Scholar** | ML/AI 论文搜索 | 1 RPS (免费) |
103	| **CrossRef** | DOI → BibTeX | 需 mailto 头 |
104	| **arXiv** | 预印本搜索 | 3s 间隔 |
105	
106	```python
107	# DOI → BibTeX（最可靠的方式）
108	import requests
109	def doi_to_bibtex(doi: str) -> str:
110	    r = requests.get(f"https://doi.org/{doi}",
111	                     headers={"Accept": "application/x-bibtex"})
112	    r.raise_for_status()
113	    return r.text
114	
115	# Semantic Scholar 搜索
116	from semanticscholar import SemanticScholar
117	sch = SemanticScholar()
118	results = sch.search_paper("attention mechanism transformers", limit=5)
119	for p in results:
120	    print(f"{p.title} | DOI: {p.externalIds.get('DOI', 'N/A')}")
121	```
122	
123	### 3.4 引用处理规则
124	
125	| 情况 | 处理 |
126	|------|------|
127	| 找到论文 + DOI + BibTeX | 直接用 |
128	| 找到论文，无 DOI | 用 arXiv BibTeX |
129	| 论文存在但无法获取 BibTeX | 标记 placeholder，告知用户 |
130	| 不确定论文是否存在 | 标记 `[CITATION NEEDED]`，告知用户 |
131	| "我觉得有篇关于 X 的论文" | **绝不引用** — 先搜索或标记 |
132	
133	---
134	
135	## 4. 顶会模板速查
136	
137	### 4.1 ML/AI 会议
138	
139	| 会议 | 页数限制 | 主文件 | 样式文件 | 必须项 |
140	|------|---------|--------|---------|--------|
141	| **NeurIPS** | 9 页 | `main.tex` | `neurips.sty` | Paper Checklist |
142	| **ICML** | 8 页 (+1 camera-ready) | `example_paper.tex` | `icml2026.sty` | Broader Impact |
143	| **ICLR** | 9 页 (+1) | `iclr_conference.tex` | `iclr_conference.sty` | LLM 使用声明 |
144	| **ACL/EMNLP** | 8 页 (long) | `acl_latex.tex` | `acl.sty` | Limitations 必须 |
145	| **AAAI** | 7 页 (+1) | `aaai_template.tex` | `aaai.sty` | 严格样式 |
146	| **COLM** | 9 页 (+1) | `colm_conference.tex` | `colm_conference.sty` | 语言模型聚焦 |
147	
148	### 4.2 系统会议
149	
150	| 会议 | 页数限制 | 模板类型 | 关键要求 |
151	|------|---------|---------|---------|
152	| **OSDI** | 12 页 (+2) | USENIX `usenix.sty` | Research / Operational 双 track |
153	| **NSDI** | 12 页 | USENIX | Introduction 预筛 |
154	| **ASPLOS** | 12 页 | ACM `acmart.cls (sigplan)` | 前 2 页快速评审 |
155	| **SOSP** | 12 页 | ACM `acmart.cls (sigplan)` | 可选 Artifact Evaluation |
156	
157	### 4.3 模板使用原则
158	
159	```bash
160	# 1. 复制整个模板目录（不要只拷 .tex）
161	cp -r templates/neurips2025/ ~/papers/my-paper/
162	
163	# 2. 先编译未修改的模板，确认能跑通
164	latexmk -pdf main.tex
165	
166	# 3. 逐章替换内容，频繁编译
167	```
168	
169	**禁止事项：**
170	- 不要修改 `.sty` 文件
171	- 不要在会议模板间复制 `\usepackage` 行
172	- 不要只复制 `.tex` 而不带 `.sty/.bst`
173	
174	---
175	
176	## 5. 写作规范
177	
178	### 5.1 时间分配（Neel Nanda）
179	
180	花**大致相等**的时间在：
181	1. Abstract
182	2. Introduction
183	3. 图表
184	4. **其余所有内容加起来**
185	
186	审稿人读论文的顺序：标题 → 摘要 → 引言 → 图表 → 也许正文。
187	
188	### 5.2 Abstract 五句法（Sebastian Farquhar）
189	
190	```
191	1. 你做了什么（"We introduce/prove/demonstrate..."）
192	2. 为什么这很难且重要
193	3. 怎么做的（含专业关键词以便检索）
194	4. 有什么证据
195	5. 最惊人的数字/结果
196	```
197	
198	删除一切泛泛的开头：~~"Large language models have achieved remarkable success..."~~
199	
200	### 5.3 句子级清晰度（Gopen & Swan）
201	
202	| 原则 | 规则 |
203	|------|------|
204	| 主谓紧邻 | 不要在主语和动词之间插入长从句 |
205	| 重点在句尾 | 把关键数字/结论放在句末 |
206	| 旧信息在前 | 先放读者已知的内容，再引入新概念 |
207	| 动词表达动作 | "We analyzed" 而非 "We performed an analysis" |
208	
209	### 5.4 常见修改
210	
211	| 问题 | 修复 |
212	|------|------|
213	| Abstract 太泛 | 删第一句（如果它能放在任何 ML 论文前面） |
214	| Introduction 超 1.5 页 | 背景挪到 Related Work |
215	| 实验没有显式 claim | 每个实验前加 "This tests whether..." |
216	| 缺统计显著性 | 加 error bars + 运行次数 + 计算方法 |
217	
218	---
219	
220	## 6. 投稿工程链
221	
222	### 6.1 构建
223	
224	```bash
225	# 推荐：latexmk 一键构建
226	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
227	
228	# 手动：需要多次编译
229	pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
230	```
231	
232	### 6.2 Lint + 格式化
233	
234	```bash
235	# Lint: 检查常见 LaTeX 问题
236	chktex main.tex
237	
238	# 格式化: 减少 diff 噪声
239	latexindent -w main.tex
240	```
241	
242	### 6.3 图表格式
243	
244	| 类型 | 格式 | 说明 |
245	|------|------|------|
246	| 矢量图（plot、diagram） | PDF | matplotlib: `plt.savefig('fig.pdf')` |
247	| 照片/heatmap | PNG 600dpi 或 TIFF | 栅格图 |
248	| 表格 | `booktabs` 包 | `\toprule/\midrule/\bottomrule` |
249	
250	```latex
251	\usepackage{booktabs}
252	\begin{tabular}{lcc}
253	\toprule
254	Method & Accuracy $\uparrow$ & Latency $\downarrow$ \\
255	\midrule
256	Baseline & 85.2 & 45ms \\
257	\textbf{Ours} & \textbf{92.1} & 38ms \\
258	\bottomrule
259	\end{tabular}
260	```
261	
262	**图表规范：**
263	- 用色盲友好色板（Okabe-Ito 或 Paul Tol）
264	- 图内不放标题（用 caption）
265	- Caption 独立可理解（不依赖正文）
266	- 最佳值加粗，标注方向符号（↑ 越高越好，↓ 越低越好）
267	
268	### 6.4 投稿打包
269	
270	```bash
271	# 清理辅助文件
272	latexmk -c
273	
274	# 打包投稿
275	zip -r submission.zip main.tex *.sty *.bst *.bib figures/ --exclude='*.aux' --exclude='*.log'
276	```
277	
278	### 6.5 常见失败点
279	
280	| 问题 | 解决 |
281	|------|------|
282	| 图片格式混用导致编译失败 | 统一用 PDF |
283	| 字体未嵌入 | `pdffonts output.pdf` 检查 |
284	| Overfull box 过多 | 关键位置手动调行 |
285	| 引用缺字段 | 检查 DOI/年份/期刊名 |
286	| 超页数 | 用 `\vspace{-Xpt}` 微调，或精简内容 |
287	
288	---
289	
290	## 7. 会议转投
291	
292	当论文被拒或转投其他会议时：
293	
294	### 7.1 ML/AI 会议间转换
295	
296	| 转换 | 页数变化 | 关键调整 |
297	|------|---------|---------|
298	| NeurIPS → ICML | 9→8 | 删 1 页，加 Broader Impact |
299	| ICML → ICLR | 8→9 | 可扩展实验 + LLM 声明 |
300	| NeurIPS → ACL | 9→8 | 按 NLP 惯例重组 + Limitations |
301	| ICLR → AAAI | 9→7 | 大幅精简，严格样式 |
302	
303	### 7.2 转投原则
304	
305	1. **永远用目标模板重新开始** — 复制目标模板，迁移内容，不要合并 preamble
306	2. **只迁移正文内容** — 不复制 `\usepackage`、header/footer 命令
307	3. **根据审稿意见改进** — 但不要在新稿中提及旧投稿（双盲）
308	4. **检查目标会议特殊要求** — checklist、ethics statement、LLM 声明等
309	
310	---
311	
312	## 8. 投前清单
313	
314	### 通用清单
315	
316	- [ ] Abstract/Intro/Conclusion 的 claim 一致
317	- [ ] 每个 contribution 有对应 evidence
318	- [ ] 所有引用已程序化验证（无幻觉引用）
319	- [ ] Error bars + 运行次数 + 统计方法
320	- [ ] Limitations 章节存在且诚实
321	- [ ] 匿名化（双盲审稿）
322	- [ ] 符合页数限制
323	- [ ] 所有图表有自包含 caption
324	- [ ] `.bib` 中无缺失字段
325	- [ ] PDF 编译无 warning
326	
327	### 会议特定
328	
329	| 会议 | 额外要求 |
330	|------|---------|
331	| NeurIPS | 16 项 Paper Checklist（附录，不计页数） |
332	| ICML | Broader Impact Statement |
333	| ICLR | LLM 使用声明 |
334	| ACL/EMNLP | Limitations 章节（必须），Ethics Statement |
335	| AAAI | 严格样式文件合规 |
336	
337	---
338	
339	## 参考资源
340	
341	**写作方法论：**
342	- [Neel Nanda: How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/) — What/Why/So What 框架
343	- [Farquhar: How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) — 五句法 Abstract
344	- [Gopen & Swan: Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) — 读者预期 7 原则
345	- [Lipton: Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) — 用词
346	- [Perez: Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) — 微观清晰度
347	
348	**API：**
349	- [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | [CrossRef](https://www.crossref.org/documentation/) | [arXiv](https://info.arxiv.org/help/api/)
350	
351	**会议官方：**
352	- [NeurIPS](https://neurips.cc/) | [ICML](https://icml.cc/) | [ICLR](https://iclr.cc/) | [ACL](https://www.aclweb.org/) | [AAAI](https://aaai.org/) | [EMNLP](https://2025.emnlp.org/)
353	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "569a3619-8b0d-4bae-aede-30fe801478cb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md",
      "content": "---\nname: latex-paper\ndescription: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。\nscope: global\ntags:\n- latex\n- paper-writing\n- academic\n- citation\n- submission\nversion: 1\nroles:\n- agent\n- worker\n---\n\n# LaTeX 论文写作全流程\n\nML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。\n\n---\n\n## 1. 工作模式\n\n开始前选择模式：\n\n| 模式 | 说明 | 适用 |\n|------|------|------|\n| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |\n| **Improve** | 改写已有章节，强化论证 | 修改稿 |\n| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |\n\n---\n\n## 2. Claim-Evidence 方法论\n\n**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**\n\n### 2.1 一句话贡献\n\n在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。\n\n### 2.2 Claim-Evidence Map\n\n为每个 contribution 建立 claim→evidence 映射表：\n\n| Contribution | Claim | Evidence | Table/Figure |\n|-------------|-------|----------|-------------|\n| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |\n| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |\n| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |\n\n**没有直接证据支撑的 claim 必须删除或降级为 discussion。**\n\n### 2.3 章节起草顺序\n\n```\n1. Introduction + Experiments（先确定 claim 和 evidence）\n2. Method（评估问题稳定后再写细节）\n3. Related Work\n4. Abstract + Title（核心 claim 定型后最后写）\n```\n\n### 2.4 Quality Gates\n\n投稿前必须通过：\n- [ ] 前两段出现显式 novelty 声明\n- [ ] 每个 contribution 有可验证的 evidence\n- [ ] Abstract / Intro / Conclusion 的 claim 一致\n- [ ] Limitations 真实且技术性诚实\n- [ ] 审稿人两分钟内能识别 delta\n\n---\n\n## 3. 引用防幻觉（CRITICAL）\n\n**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**\n\n### 3.1 黄金法则\n\n```\nIF 无法程序化获取引用:\n    → 标记 [CITATION NEEDED] 或 \\cite{PLACEHOLDER_verify}\n    → 明确告知用户\n    → 绝不编造看似合理的引用\n```\n\n### 3.2 五步验证流程\n\n```\n1. SEARCH  → Semantic Scholar API 搜索关键词\n2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）\n3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）\n4. CHECK   → 确认你引用的 claim 确实出自该论文\n5. ADD     → 加入 .bib 文件\n```\n\n### 3.3 API 速查\n\n| API | 用途 | 限制 |\n|-----|------|------|\n| **Semantic Scholar** | ML/AI 论文搜索 | 1 RPS (免费) |\n| **CrossRef** | DOI → BibTeX | 需 mailto 头 |\n| **arXiv** | 预印本搜索 | 3s 间隔 |\n\n```python\n# DOI → BibTeX（最可靠的方式）\nimport requests\ndef doi_to_bibtex(doi: str) -> str:\n    r = requests.get(f\"https://doi.org/{doi}\",\n                     headers={\"Accept\": \"application/x-bibtex\"})\n    r.raise_for_status()\n    return r.text\n\n# Semantic Scholar 搜索\nfrom semanticscholar import SemanticScholar\nsch = SemanticScholar()\nresults = sch.search_paper(\"attention mechanism transformers\", limit=5)\nfor p in results:\n    print(f\"{p.title} | DOI: {p.externalIds.get('DOI', 'N/A')}\")\n```\n\n### 3.4 引用处理规则\n\n| 情况 | 处理 |\n|------|------|\n| 找到论文 + DOI + BibTeX | 直接用 |\n| 找到论文，无 DOI | 用 arXiv BibTeX |\n| 论文存在但无法获取 BibTeX | 标记 placeholder，告知用户 |\n| 不确定论文是否存在 | 标记 `[CITATION NEEDED]`，告知用户 |\n| \"我觉得有篇关于 X 的论文\" | **绝不引用** — 先搜索或标记 |\n\n---\n\n## 4. 顶会模板速查\n\n### 4.1 ML/AI 会议\n\n| 会议 | 页数限制 | 主文件 | 样式文件 | 必须项 |\n|------|---------|--------|---------|--------|\n| **NeurIPS** | 9 页 | `main.tex` | `neurips.sty` | Paper Checklist |\n| **ICML** | 8 页 (+1 camera-ready) | `example_paper.tex` | `icml2026.sty` | Broader Impact |\n| **ICLR** | 9 页 (+1) | `iclr_conference.tex` | `iclr_conference.sty` | LLM 使用声明 |\n| **ACL/EMNLP** | 8 页 (long) | `acl_latex.tex` | `acl.sty` | Limitations 必须 |\n| **AAAI** | 7 页 (+1) | `aaai_template.tex` | `aaai.sty` | 严格样式 |\n| **COLM** | 9 页 (+1) | `colm_conference.tex` | `colm_conference.sty` | 语言模型聚焦 |\n\n### 4.2 系统会议\n\n| 会议 | 页数限制 | 模板类型 | 关键要求 |\n|------|---------|---------|---------|\n| **OSDI** | 12 页 (+2) | USENIX `usenix.sty` | Research / Operational 双 track |\n| **NSDI** | 12 页 | USENIX | Introduction 预筛 |\n| **ASPLOS** | 12 页 | ACM `acmart.cls (sigplan)` | 前 2 页快速评审 |\n| **SOSP** | 12 页 | ACM `acmart.cls (sigplan)` | 可选 Artifact Evaluation |\n\n### 4.3 模板使用原则\n\n```bash\n# 1. 复制整个模板目录（不要只拷 .tex）\ncp -r templates/neurips2025/ ~/papers/my-paper/\n\n# 2. 先编译未修改的模板，确认能跑通\nlatexmk -pdf main.tex\n\n# 3. 逐章替换内容，频繁编译\n```\n\n**禁止事项：**\n- 不要修改 `.sty` 文件\n- 不要在会议模板间复制 `\\usepackage` 行\n- 不要只复制 `.tex` 而不带 `.sty/.bst`\n\n---\n\n## 5. 写作规范\n\n### 5.1 时间分配（Neel Nanda）\n\n花**大致相等**的时间在：\n1. Abstract\n2. Introduction\n3. 图表\n4. **其余所有内容加起来**\n\n审稿人读论文的顺序：标题 → 摘要 → 引言 → 图表 → 也许正文。\n\n### 5.2 Abstract 五句法（Sebastian Farquhar）\n\n```\n1. 你做了什么（\"We introduce/prove/demonstrate...\"）\n2. 为什么这很难且重要\n3. 怎么做的（含专业关键词以便检索）\n4. 有什么证据\n5. 最惊人的数字/结果\n```\n\n删除一切泛泛的开头：~~\"Large language models have achieved remarkable success...\"~~\n\n### 5.3 句子级清晰度（Gopen & Swan）\n\n| 原则 | 规则 |\n|------|------|\n| 主谓紧邻 | 不要在主语和动词之间插入长从句 |\n| 重点在句尾 | 把关键数字/结论放在句末 |\n| 旧信息在前 | 先放读者已知的内容，再引入新概念 |\n| 动词表达动作 | \"We analyzed\" 而非 \"We performed an analysis\" |\n\n### 5.4 常见修改\n\n| 问题 | 修复 |\n|------|------|\n| Abstract 太泛 | 删第一句（如果它能放在任何 ML 论文前面） |\n| Introduction 超 1.5 页 | 背景挪到 Related Work |\n| 实验没有显式 claim | 每个实验前加 \"This tests whether...\" |\n| 缺统计显著性 | 加 error bars + 运行次数 + 计算方法 |\n\n---\n\n## 6. 投稿工程链\n\n### 6.1 构建\n\n```bash\n# 推荐：latexmk 一键构建\nlatexmk -pdf -interaction=nonstopmode -halt-on-error main.tex\n\n# 手动：需要多次编译\npdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex\n```\n\n### 6.2 Lint + 格式化\n\n```bash\n# Lint: 检查常见 LaTeX 问题\nchktex main.tex\n\n# 格式化: 减少 diff 噪声\nlatexindent -w main.tex\n```\n\n### 6.3 图表格式\n\n| 类型 | 格式 | 说明 |\n|------|------|------|\n| 矢量图（plot、diagram） | PDF | matplotlib: `plt.savefig('fig.pdf')` |\n| 照片/heatmap | PNG 600dpi 或 TIFF | 栅格图 |\n| 表格 | `booktabs` 包 | `\\toprule/\\midrule/\\bottomrule` |\n\n```latex\n\\usepackage{booktabs}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Accuracy $\\uparrow$ & Latency $\\downarrow$ \\\\\n\\midrule\nBaseline & 85.2 & 45ms \\\\\n\\textbf{Ours} & \\textbf{92.1} & 38ms \\\\\n\\bottomrule\n\\end{tabular}\n```\n\n**图表规范：**\n- 用色盲友好色板（Okabe-Ito 或 Paul Tol）\n- 图内不放标题（用 caption）\n- Caption 独立可理解（不依赖正文）\n- 最佳值加粗，标注方向符号（↑ 越高越好，↓ 越低越好）\n\n### 6.4 投稿打包\n\n```bash\n# 清理辅助文件\nlatexmk -c\n\n# 打包投稿\nzip -r submission.zip main.tex *.sty *.bst *.bib figures/ --exclude='*.aux' --exclude='*.log'\n```\n\n### 6.5 常见失败点\n\n| 问题 | 解决 |\n|------|------|\n| 图片格式混用导致编译失败 | 统一用 PDF |\n| 字体未嵌入 | `pdffonts output.pdf` 检查 |\n| Overfull box 过多 | 关键位置手动调行 |\n| 引用缺字段 | 检查 DOI/年份/期刊名 |\n| 超页数 | 用 `\\vspace{-Xpt}` 微调，或精简内容 |\n\n---\n\n## 7. 会议转投\n\n当论文被拒或转投其他会议时：\n\n### 7.1 ML/AI 会议间转换\n\n| 转换 | 页数变化 | 关键调整 |\n|------|---------|---------|\n| NeurIPS → ICML | 9→8 | 删 1 页，加 Broader Impact |\n| ICML → ICLR | 8→9 | 可扩展实验 + LLM 声明 |\n| NeurIPS → ACL | 9→8 | 按 NLP 惯例重组 + Limitations |\n| ICLR → AAAI | 9→7 | 大幅精简，严格样式 |\n\n### 7.2 转投原则\n\n1. **永远用目标模板重新开始** — 复制目标模板，迁移内容，不要合并 preamble\n2. **只迁移正文内容** — 不复制 `\\usepackage`、header/footer 命令\n3. **根据审稿意见改进** — 但不要在新稿中提及旧投稿（双盲）\n4. **检查目标会议特殊要求** — checklist、ethics statement、LLM 声明等\n\n---\n\n## 8. 投前清单\n\n### 通用清单\n\n- [ ] Abstract/Intro/Conclusion 的 claim 一致\n- [ ] 每个 contribution 有对应 evidence\n- [ ] 所有引用已程序化验证（无幻觉引用）\n- [ ] Error bars + 运行次数 + 统计方法\n- [ ] Limitations 章节存在且诚实\n- [ ] 匿名化（双盲审稿）\n- [ ] 符合页数限制\n- [ ] 所有图表有自包含 caption\n- [ ] `.bib` 中无缺失字段\n- [ ] PDF 编译无 warning\n\n### 会议特定\n\n| 会议 | 额外要求 |\n|------|---------|\n| NeurIPS | 16 项 Paper Checklist（附录，不计页数） |\n| ICML | Broader Impact Statement |\n| ICLR | LLM 使用声明 |\n| ACL/EMNLP | Limitations 章节（必须），Ethics Statement |\n| AAAI | 严格样式文件合规 |\n\n---\n\n## 参考资源\n\n**写作方法论：**\n- [Neel Nanda: How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/) — What/Why/So What 框架\n- [Farquhar: How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) — 五句法 Abstract\n- [Gopen & Swan: Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) — 读者预期 7 原则\n- [Lipton: Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) — 用词\n- [Perez: Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) — 微观清晰度\n\n**API：**\n- [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | [CrossRef](https://www.crossref.org/documentation/) | [arXiv](https://info.arxiv.org/help/api/)\n\n**会议官方：**\n- [NeurIPS](https://neurips.cc/) | [ICML](https://icml.cc/) | [ICLR](https://iclr.cc/) | [ACL](https://www.aclweb.org/) | [AAAI](https://aaai.org/) | [EMNLP](https://2025.emnlp.org/)\n",
      "numLines": 353,
      "startLine": 1,
      "totalLines": 353
    }
  }
}
````

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I have the existing introduction and the writing guide. Let me craft the new introduction following the specified structure. Let me carefully use the exact numbers from the registry and only the allowed cite keys.

Let me write the new introduction following the P1-P7 structure specified in the task.

Key data points:
- Unpruned GRPO: reward 0→0.661 over 100 steps, accuracy stays 81.27% (1072/1319)
- SFT unpruned: accuracy 81.27%
- RASP post-prune: 29% GSM8K vs 1% Standard (N=100, p<0.0001)


- RASP post-SFT: 61.49% vs Standard 59.29% (+2.2pp, N=1319)
- RASP GRPO collapse at step 10, Standard at step 60
- RASP GRPO at step 10 reaches 61.87% accuracy while Standard GRPO at step 50 achieves 58.91%

Now I'm ready to write the introduction, making sure to apply the \rasp{} macro where appropriate, stick to the allowed citations, and incorporate these specific performance comparisons throughout the P1-P7 structure. Looking at the key experimental results now — RASP achieves 29% recovery post-pruning versus only 1% for the standard approach, and this advantage persists through SFT at 61.49% versus 59.29%, but then both methods show the same decoupling phenomenon during GRPO where RASP collapses at step 10 while the standard method holds until step 60.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "a10bdbb9-47c6-413d-9e6d-e00213631646",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JYteR6Lrhx5drPBYZbR8p9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7208,
      "cache_read_input_tokens": 25139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7208
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 10_

Now I'll write the new introduction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "ec4ed88d-e274-407d-bf87-f0e843856e4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JYteR6Lrhx5drPBYZbR8p9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7208,
      "cache_read_input_tokens": 25139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7208
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Write · `toolu_016JEmf8gbMo4gBqTmssYXrg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:intro}\n\nGRPO training~\\citep{shao2024grpo} on an unpruned DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} drives reward from 0 to 0.661 over 100 steps---a trajectory that, by every reinforcement learning diagnostic, signals substantial policy improvement.\nYet GSM8K~\\citep{cobbe2021gsm8k} accuracy remains at exactly 81.27\\% throughout: the same 1{,}072 out of 1{,}319 problems solved before and after training, with zero net change in which problems the model can solve.\nThe reward signal that GRPO optimizes and the downstream reasoning accuracy that practitioners care about are, in this regime, orthogonal.\nThis observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain, and sets the stage for our central finding: the interaction between structural pruning and GRPO training dynamics.\n\nOn pruned models, the decoupled reward signal becomes catastrophic.\nStructured pruning at 20\\% sparsity removes entire attention heads and MLP channels~\\citep{llmpruner2023,graspprune2026}, degrading the model's internal representations and narrowing its exploration capacity.\nWhen GRPO is applied to these pruned architectures, training does not merely stall---it \\emph{collapses}: reward drops to near-zero and per-sample reward variance vanishes as the policy degenerates to a single low-reward mode.\nThe collapse severity depends on \\emph{what} was pruned.\n\\rasp{}, which uses CKA-based functional overlap~\\citep{kornblith2019cka} to preferentially remove high-redundancy structures, collapses at step~10---six times faster than importance-only pruning, which collapses around step~60.\nBy removing functionally overlapping heads that served as exploration buffers, \\rasp{} inadvertently eliminates the structural diversity that GRPO requires for stable optimization.\nCrucially, the decoupling is bidirectional: just as reward increase on the unpruned model does not improve accuracy, reward collapse on pruned models does not degrade it.\nPost-GRPO accuracy for the \\rasp{}-pruned model is 61.87\\%, nearly identical to its 61.49\\% post-SFT baseline ($N{=}1{,}319$).\nNeither reward improvement nor reward collapse changes reasoning performance---the two signals are genuinely independent.\n\nThe current prune-recover-align pipeline treats its stages as independent: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.\n\\citet{selfhealing2025} report that RLVR-based recovery restores up to 95\\% of pre-pruning performance---but their experiments use unstructured magnitude pruning at high sparsity and do not document per-step training dynamics.\nNo prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.\n\nOur experiments reveal a \\emph{Redundancy-Stability Tradeoff} at the heart of this interaction.\nFunctional redundancy---the degree to which a structure's computation overlaps with its within-layer peers---plays opposite roles depending on the recovery paradigm.\nFor SFT-based recovery, redundant structures are safely removable: their function can be redistributed through supervised gradient signals that directly optimize the retained architecture's output distribution.\nFor RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.\nThis connects to the analysis of \\citet{rlsqueezes2026}, who show that RLVR recovers through global exploration and path compression---a process that requires diverse internal pathways---while SFT recovers through local trajectory imitation, which demands only sufficient representational capacity.\nThe Redundancy-Stability Tradeoff implies that optimal pruning is fundamentally conditioned on the intended recovery paradigm: structures safe to remove under SFT are precisely those dangerous to remove under RLVR.\n\nWe formalize this tradeoff through \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework illustrated in Figure~\\ref{fig:framework}.\nIn Stage~1, \\rasp{} computes for each attention head and MLP channel both a gradient-based importance score $I(h)$ and a functional overlap score $F(h)$ via intra-layer CKA~\\citep{kornblith2019cka}.\nIn Stage~2, these are combined into a recovery-aware pruning score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important and functionally unique, while allowing removal of important-but-redundant structures.\nIn Stage~3, the pruned model undergoes SFT warmup followed by GRPO-based RLVR~\\citep{shao2024grpo}.\nUnlike prior CKA applications that measure inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups~\\citep{ainslie2023gqa} and MLP channels to quantify per-structure redundancy---a finer granularity targeting a fundamentally different objective.\n\\rasp{} was originally designed to optimize RLVR recoverability, but its failure under GRPO---collapsing faster than the baseline it was meant to improve---is precisely what reveals the Redundancy-Stability Tradeoff and establishes \\rasp{} as a diagnostic tool for structural damage type.\n\nAt 20\\% structured sparsity on DeepSeek-R1-Distill-Qwen-7B, \\rasp{} demonstrates clear advantages where redundancy removal helps and clear penalties where it hurts.\nImmediately after pruning, \\rasp{} retains 29\\% GSM8K accuracy versus 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$), confirming that preserving functionally unique structures protects reasoning capacity.\nAfter SFT recovery, \\rasp{} reaches 61.49\\% versus 59.29\\% for importance-only (+2.2pp, $N{=}1{,}319$), showing that the post-prune advantage partially transfers through supervised recovery.\nAfter GRPO training, reward-accuracy decoupling is universal across all conditions: \\rasp{} collapses at step~10, importance-only at step~60, yet post-GRPO accuracy (61.87\\% vs.\\ 58.91\\%) remains within the range established by SFT alone.\nThe collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.\n[TBD-25\\%: Multi-sparsity results at 25\\% to test tradeoff generalization.]\n[TBD-QwenMath: Cross-model validation on Qwen2.5-Math-7B.]\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We document \\emph{universal GRPO reward-accuracy decoupling}: reward improvement never translates to accuracy gain post-SFT, and this holds bidirectionally---neither reward increase on unpruned models nor reward collapse on pruned models changes reasoning performance.\n    \\item We identify \\emph{pruning-induced GRPO training collapse} with a severity gradient that diagnoses structural damage type: CKA-aware pruning (\\rasp{}) collapses 6$\\times$ faster than importance-only pruning at matched sparsity, because it removes the functionally redundant structures that GRPO relies on for stable exploration.\n    \\item We reveal the \\emph{Redundancy-Stability Tradeoff}: structures optimal for SFT recovery (high-overlap, functionally redundant) are exactly those required for RLVR training stability---optimal pruning is fundamentally conditioned on the recovery paradigm.\n    \\item[\\textbullet] [TBD-QwenMath: Multi-model validation contribution.]\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "7bfddcf3-4272-4ef8-9319-4d741804258b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JYteR6Lrhx5drPBYZbR8p9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7208,
      "cache_read_input_tokens": 25139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7208
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T09:09:55.228Z_

<details><summary>↩ Tool result · `toolu_016JEmf8gbMo4gBqTmssYXrg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "15926572-d238-43f1-8486-49c6b3d69bd7",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:intro}\n\nGRPO training~\\citep{shao2024grpo} on an unpruned DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} drives reward from 0 to 0.661 over 100 steps---a trajectory that, by every reinforcement learning diagnostic, signals substantial policy improvement.\nYet GSM8K~\\citep{cobbe2021gsm8k} accuracy remains at exactly 81.27\\% throughout: the same 1{,}072 out of 1{,}319 problems solved before and after training, with zero net change in which problems the model can solve.\nThe reward signal that GRPO optimizes and the downstream reasoning accuracy that practitioners care about are, in this regime, orthogonal.\nThis observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain, and sets the stage for our central finding: the interaction between structural pruning and GRPO training dynamics.\n\nOn pruned models, the decoupled reward signal becomes catastrophic.\nStructured pruning at 20\\% sparsity removes entire attention heads and MLP channels~\\citep{llmpruner2023,graspprune2026}, degrading the model's internal representations and narrowing its exploration capacity.\nWhen GRPO is applied to these pruned architectures, training does not merely stall---it \\emph{collapses}: reward drops to near-zero and per-sample reward variance vanishes as the policy degenerates to a single low-reward mode.\nThe collapse severity depends on \\emph{what} was pruned.\n\\rasp{}, which uses CKA-based functional overlap~\\citep{kornblith2019cka} to preferentially remove high-redundancy structures, collapses at step~10---six times faster than importance-only pruning, which collapses around step~60.\nBy removing functionally overlapping heads that served as exploration buffers, \\rasp{} inadvertently eliminates the structural diversity that GRPO requires for stable optimization.\nCrucially, the decoupling is bidirectional: just as reward increase on the unpruned model does not improve accuracy, reward collapse on pruned models does not degrade it.\nPost-GRPO accuracy for the \\rasp{}-pruned model is 61.87\\%, nearly identical to its 61.49\\% post-SFT baseline ($N{=}1{,}319$).\nNeither reward improvement nor reward collapse changes reasoning performance---the two signals are genuinely independent.\n\nThe current prune-recover-align pipeline treats its stages as independent: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.\n\\citet{selfhealing2025} report that RLVR-based recovery restores up to 95\\% of pre-pruning performance---but their experiments use unstructured magnitude pruning at high sparsity and do not document per-step training dynamics.\nNo prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.\n\nOur experiments reveal a \\emph{Redundancy-Stability Tradeoff} at the heart of this interaction.\nFunctional redundancy---the degree to which a structure's computation overlaps with its within-layer peers---plays opposite roles depending on the recovery paradigm.\nFor SFT-based recovery, redundant structures are safely removable: their function can be redistributed through supervised gradient signals that directly optimize the retained architecture's output distribution.\nFor RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.\nThis connects to the analysis of \\citet{rlsqueezes2026}, who show that RLVR recovers through global exploration and path compression---a process that requires diverse internal pathways---while SFT recovers through local trajectory imitation, which demands only sufficient representational capacity.\nThe Redundancy-Stability Tradeoff implies that optimal pruning is fundamentally conditioned on the intended recovery paradigm: structures safe to remove under SFT are precisely those dangerous to remove under RLVR.\n\nWe formalize this tradeoff through \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework illustrated in Figure~\\ref{fig:framework}.\nIn Stage~1, \\rasp{} computes for each attention head and MLP channel both a gradient-based importance score $I(h)$ and a functional overlap score $F(h)$ via intra-layer CKA~\\citep{kornblith2019cka}.\nIn Stage~2, these are combined into a recovery-aware pruning score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important and functionally unique, while allowing removal of important-but-redundant structures.\nIn Stage~3, the pruned model undergoes SFT warmup followed by GRPO-based RLVR~\\citep{shao2024grpo}.\nUnlike prior CKA applications that measure inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups~\\citep{ainslie2023gqa} and MLP channels to quantify per-structure redundancy---a finer granularity targeting a fundamentally different objective.\n\\rasp{} was originally designed to optimize RLVR recoverability, but its failure under GRPO---collapsing faster than the baseline it was meant to improve---is precisely what reveals the Redundancy-Stability Tradeoff and establishes \\rasp{} as a diagnostic tool for structural damage type.\n\nAt 20\\% structured sparsity on DeepSeek-R1-Distill-Qwen-7B, \\rasp{} demonstrates clear advantages where redundancy removal helps and clear penalties where it hurts.\nImmediately after pruning, \\rasp{} retains 29\\% GSM8K accuracy versus 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$), confirming that preserving functionally unique structures protects reasoning capacity.\nAfter SFT recovery, \\rasp{} reaches 61.49\\% versus 59.29\\% for importance-only (+2.2pp, $N{=}1{,}319$), showing that the post-prune advantage partially transfers through supervised recovery.\nAfter GRPO training, reward-accuracy decoupling is universal across all conditions: \\rasp{} collapses at step~10, importance-only at step~60, yet post-GRPO accuracy (61.87\\% vs.\\ 58.91\\%) remains within the range established by SFT alone.\nThe collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.\n[TBD-25\\%: Multi-sparsity results at 25\\% to test tradeoff generalization.]\n[TBD-QwenMath: Cross-model validation on Qwen2.5-Math-7B.]\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We document \\emph{universal GRPO reward-accuracy decoupling}: reward improvement never translates to accuracy gain post-SFT, and this holds bidirectionally---neither reward increase on unpruned models nor reward collapse on pruned models changes reasoning performance.\n    \\item We identify \\emph{pruning-induced GRPO training collapse} with a severity gradient that diagnoses structural damage type: CKA-aware pruning (\\rasp{}) collapses 6$\\times$ faster than importance-only pruning at matched sparsity, because it removes the functionally redundant structures that GRPO relies on for stable exploration.\n    \\item We reveal the \\emph{Redundancy-Stability Tradeoff}: structures optimal for SFT recovery (high-overlap, functionally redundant) are exactly those required for RLVR training stability---optimal pruning is fundamentally conditioned on the recovery paradigm.\n    \\item[\\textbullet] [TBD-QwenMath: Multi-model validation contribution.]\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 38,
        "newStart": 1,
        "newLines": 52,
        "lines": [
          " \\section{Introduction}",
          " \\label{sec:intro}",
          " ",
          "-Large language models trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong performance on mathematical and logical reasoning~\\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.",
          "-Structured pruning---removing entire attention heads or MLP channels---offers a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\\citep{llmpruner2023,graspprune2026}.",
          "-However, structured pruning at moderate sparsity severely degrades reasoning ability, necessitating a post-pruning recovery stage.",
          "-\\citet{selfhealing2025} show that RLVR-based recovery substantially outperforms SFT-based recovery for pruned reasoning models, establishing RLVR as the preferred recovery paradigm.",
          "+GRPO training~\\citep{shao2024grpo} on an unpruned DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} drives reward from 0 to 0.661 over 100 steps---a trajectory that, by every reinforcement learning diagnostic, signals substantial policy improvement.",
          "+Yet GSM8K~\\citep{cobbe2021gsm8k} accuracy remains at exactly 81.27\\% throughout: the same 1{,}072 out of 1{,}319 problems solved before and after training, with zero net change in which problems the model can solve.",
          "+The reward signal that GRPO optimizes and the downstream reasoning accuracy that practitioners care about are, in this regime, orthogonal.",
          "+This observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain, and sets the stage for our central finding: the interaction between structural pruning and GRPO training dynamics.",
          " ",
          "-Despite this, current approaches treat pruning and recovery as independent steps: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.",
          "-No prior work has studied whether the \\emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning---or whether this interaction differs from SFT-based recovery.",
          "-This gap is consequential because RLVR and SFT impose fundamentally different functional demands on the retained architecture: \\citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation.",
          "-The optimal set of structures to retain should therefore depend on the recovery paradigm.",
          "+On pruned models, the decoupled reward signal becomes catastrophic.",
          "+Structured pruning at 20\\% sparsity removes entire attention heads and MLP channels~\\citep{llmpruner2023,graspprune2026}, degrading the model's internal representations and narrowing its exploration capacity.",
          "+When GRPO is applied to these pruned architectures, training does not merely stall---it \\emph{collapses}: reward drops to near-zero and per-sample reward variance vanishes as the policy degenerates to a single low-reward mode.",
          "+The collapse severity depends on \\emph{what} was pruned.",
          "+\\rasp{}, which uses CKA-based functional overlap~\\citep{kornblith2019cka} to preferentially remove high-redundancy structures, collapses at step~10---six times faster than importance-only pruning, which collapses around step~60.",
          "+By removing functionally overlapping heads that served as exploration buffers, \\rasp{} inadvertently eliminates the structural diversity that GRPO requires for stable optimization.",
          "+Crucially, the decoupling is bidirectional: just as reward increase on the unpruned model does not improve accuracy, reward collapse on pruned models does not degrade it.",
          "+Post-GRPO accuracy for the \\rasp{}-pruned model is 61.87\\%, nearly identical to its 61.49\\% post-SFT baseline ($N{=}1{,}319$).",
          "+Neither reward improvement nor reward collapse changes reasoning performance---the two signals are genuinely independent.",
          " ",
          "-We hypothesize that \\emph{functional overlap}---the degree to which a structure's computation is redundant with its within-layer peers---positively predicts RLVR recoverability.",
          "-If a pruned structure has high overlap with retained structures, RLVR can absorb its function through global policy optimization over the remaining architecture.",
          "-Conversely, structures with unique, non-redundant computations are difficult to recover once removed.",
          "-This yields what we term the \\textbf{Redundancy Paradox}: the property that makes a structure functionally ``redundant''---high overlap with within-layer peers---is precisely the property that makes it most recoverable under RLVR, because reinforcement learning can redistribute its function through retained structures with similar representations.",
          "-\\rasp{} exploits this by preferentially pruning high-overlap structures whose function can be absorbed, while protecting functionally unique structures whose contribution is irrecoverable once removed.",
          "-Importance-only pruning is blind to this distinction and may inadvertently remove unique structures critical for recovery.",
          "+The current prune-recover-align pipeline treats its stages as independent: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.",
          "+\\citet{selfhealing2025} report that RLVR-based recovery restores up to 95\\% of pre-pruning performance---but their experiments use unstructured magnitude pruning at high sparsity and do not document per-step training dynamics.",
          "+No prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.",
          "+This gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.",
          " ",
          "-We propose \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework that incorporates recoverability into the pruning decision.",
          "-In Stage~1, \\rasp{} computes for each structure both a gradient-based importance score and a functional overlap score via intra-layer Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}).",
          "-In Stage~2, these are combined into a recovery-aware score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important \\emph{and} functionally unique, while allowing removal of important-but-redundant structures whose function RLVR can redistribute.",
          "-In Stage~3, the pruned model undergoes a brief SFT warmup to restore generation competence, followed by GRPO-based RLVR recovery~\\citep{shao2024grpo} to restore reasoning ability.",
          "-Unlike prior CKA-based pruning that uses inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability---a finer granularity optimizing for a fundamentally different objective.",
          "+Our experiments reveal a \\emph{Redundancy-Stability Tradeoff} at the heart of this interaction.",
          "+Functional redundancy---the degree to which a structure's computation overlaps with its within-layer peers---plays opposite roles depending on the recovery paradigm.",
          "+For SFT-based recovery, redundant structures are safely removable: their function can be redistributed through supervised gradient signals that directly optimize the retained architecture's output distribution.",
          "+For RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.",
          "+This connects to the analysis of \\citet{rlsqueezes2026}, who show that RLVR recovers through global exploration and path compression---a process that requires diverse internal pathways---while SFT recovers through local trajectory imitation, which demands only sufficient representational capacity.",
          "+The Redundancy-Stability Tradeoff implies that optimal pruning is fundamentally conditioned on the intended recovery paradigm: structures safe to remove under SFT are precisely those dangerous to remove under RLVR.",
          " ",
          "-We evaluate \\rasp{} on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} at 20\\% structured sparsity.",
          "-At matched sparsity, \\rasp{}-pruned models retain 29\\% GSM8K~\\citep{cobbe2021gsm8k} accuracy immediately after pruning, compared to 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$)---a 28-percentage-point advantage attributable to the recovery-aware scoring criterion.",
          "-After SFT warmup, importance-only pruning recovers to 64\\% versus \\rasp{}'s 57\\%, consistent with the hypothesis that SFT preferentially benefits structures selected for immediate accuracy.",
          "-[TBD: GRPO results]",
          "+We formalize this tradeoff through \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework illustrated in Figure~\\ref{fig:framework}.",
          "+In Stage~1, \\rasp{} computes for each attention head and MLP channel both a gradient-based importance score $I(h)$ and a functional overlap score $F(h)$ via intra-layer CKA~\\citep{kornblith2019cka}.",
          "+In Stage~2, these are combined into a recovery-aware pruning score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important and functionally unique, while allowing removal of important-but-redundant structures.",
          "+In Stage~3, the pruned model undergoes SFT warmup followed by GRPO-based RLVR~\\citep{shao2024grpo}.",
          "+Unlike prior CKA applications that measure inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups~\\citep{ainslie2023gqa} and MLP channels to quantify per-structure redundancy---a finer granularity targeting a fundamentally different objective.",
          "+\\rasp{} was originally designed to optimize RLVR recoverability, but its failure under GRPO---collapsing faster than the baseline it was meant to improve---is precisely what reveals the Redundancy-Stability Tradeoff and establishes \\rasp{} as a diagnostic tool for structural damage type.",
          " ",
          "+At 20\\% structured sparsity on DeepSeek-R1-Distill-Qwen-7B, \\rasp{} demonstrates clear advantages where redundancy removal helps and clear penalties where it hurts.",
          "+Immediately after pruning, \\rasp{} retains 29\\% GSM8K accuracy versus 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$), confirming that preserving functionally unique structures protects reasoning capacity.",
          "+After SFT recovery, \\rasp{} reaches 61.49\\% versus 59.29\\% for importance-only (+2.2pp, $N{=}1{,}319$), showing that the post-prune advantage partially transfers through supervised recovery.",
          "+After GRPO training, reward-accuracy decoupling is universal across all conditions: \\rasp{} collapses at step~10, importance-only at step~60, yet post-GRPO accuracy (61.87\\% vs.\\ 58.91\\%) remains within the range established by SFT alone.",
          "+The collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.",
          "+[TBD-25\\%: Multi-sparsity results at 25\\% to test tradeoff generalization.]",
          "+[TBD-QwenMath: Cross-model validation on Qwen2.5-Math-7B.]",
          "+",
          " Our contributions are:",
          " \\begin{enumerate}[nosep,leftmargin=*]",
          "-    \\item We identify the \\emph{Redundancy Paradox}---that functional redundancy, typically a signal for removal in standard pruning, is the property that enables RLVR recovery---and formalize it through intra-layer CKA-based functional overlap scoring.",
          "-    \\item We propose \\rasp{}, a recovery-aware pruning framework that integrates functional overlap into structural pruning decisions, achieving 29\\% post-prune GSM8K accuracy versus 1\\% for importance-only pruning at matched 20\\% sparsity on DeepSeek-R1-Distill-Qwen-7B.",
          "-    \\item [TBD: GRPO recovery results---contribution demonstrating that \\rasp{}'s post-prune advantage translates to superior post-RLVR reasoning performance.]",
          "-    \\item We provide evidence that the optimal pruning strategy is conditioned on the recovery paradigm: \\rasp{} and importance-only pruning exhibit reversed relative advantages under SFT versus RLVR recovery [TBD: pending GRPO confirmation], supporting the notion of \\emph{paradigm-conditioned prunability}.",
          "+    \\item We document \\emph{universal GRPO reward-accuracy decoupling}: reward improvement never translates to accuracy gain post-SFT, and this holds bidirectionally---neither reward increase on unpruned models nor reward collapse on pruned models changes reasoning performance.",
          "+    \\item We identify \\emph{pruning-induced GRPO training collapse} with a severity gradient that diagnoses structural damage type: CKA-aware pruning (\\rasp{}) collapses 6$\\times$ faster than importance-only pruning at matched sparsity, because it removes the functionally redundant structures that GRPO relies on for stable exploration.",
          "+    \\item We reveal the \\emph{Redundancy-Stability Tradeoff}: structures optimal for SFT recovery (high-overlap, functionally redundant) are exactly those required for RLVR training stability---optimal pruning is fundamentally conditioned on the recovery paradigm.",
          "+    \\item[\\textbullet] [TBD-QwenMath: Multi-model validation contribution.]",
          " \\end{enumerate}"
        ]
      }
    ],
    "originalFile": "\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong performance on mathematical and logical reasoning~\\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.\nStructured pruning---removing entire attention heads or MLP channels---offers a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\\citep{llmpruner2023,graspprune2026}.\nHowever, structured pruning at moderate sparsity severely degrades reasoning ability, necessitating a post-pruning recovery stage.\n\\citet{selfhealing2025} show that RLVR-based recovery substantially outperforms SFT-based recovery for pruned reasoning models, establishing RLVR as the preferred recovery paradigm.\n\nDespite this, current approaches treat pruning and recovery as independent steps: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.\nNo prior work has studied whether the \\emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning---or whether this interaction differs from SFT-based recovery.\nThis gap is consequential because RLVR and SFT impose fundamentally different functional demands on the retained architecture: \\citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation.\nThe optimal set of structures to retain should therefore depend on the recovery paradigm.\n\nWe hypothesize that \\emph{functional overlap}---the degree to which a structure's computation is redundant with its within-layer peers---positively predicts RLVR recoverability.\nIf a pruned structure has high overlap with retained structures, RLVR can absorb its function through global policy optimization over the remaining architecture.\nConversely, structures with unique, non-redundant computations are difficult to recover once removed.\nThis yields what we term the \\textbf{Redundancy Paradox}: the property that makes a structure functionally ``redundant''---high overlap with within-layer peers---is precisely the property that makes it most recoverable under RLVR, because reinforcement learning can redistribute its function through retained structures with similar representations.\n\\rasp{} exploits this by preferentially pruning high-overlap structures whose function can be absorbed, while protecting functionally unique structures whose contribution is irrecoverable once removed.\nImportance-only pruning is blind to this distinction and may inadvertently remove unique structures critical for recovery.\n\nWe propose \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework that incorporates recoverability into the pruning decision.\nIn Stage~1, \\rasp{} computes for each structure both a gradient-based importance score and a functional overlap score via intra-layer Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}).\nIn Stage~2, these are combined into a recovery-aware score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important \\emph{and} functionally unique, while allowing removal of important-but-redundant structures whose function RLVR can redistribute.\nIn Stage~3, the pruned model undergoes a brief SFT warmup to restore generation competence, followed by GRPO-based RLVR recovery~\\citep{shao2024grpo} to restore reasoning ability.\nUnlike prior CKA-based pruning that uses inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability---a finer granularity optimizing for a fundamentally different objective.\n\nWe evaluate \\rasp{} on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} at 20\\% structured sparsity.\nAt matched sparsity, \\rasp{}-pruned models retain 29\\% GSM8K~\\citep{cobbe2021gsm8k} accuracy immediately after pruning, compared to 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$)---a 28-percentage-point advantage attributable to the recovery-aware scoring criterion.\nAfter SFT warmup, importance-only pruning recovers to 64\\% versus \\rasp{}'s 57\\%, consistent with the hypothesis that SFT preferentially benefits structures selected for immediate accuracy.\n[TBD: GRPO results]\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify the \\emph{Redundancy Paradox}---that functional redundancy, typically a signal for removal in standard pruning, is the property that enables RLVR recovery---and formalize it through intra-layer CKA-based functional overlap scoring.\n    \\item We propose \\rasp{}, a recovery-aware pruning framework that integrates functional overlap into structural pruning decisions, achieving 29\\% post-prune GSM8K accuracy versus 1\\% for importance-only pruning at matched 20\\% sparsity on DeepSeek-R1-Distill-Qwen-7B.\n    \\item [TBD: GRPO recovery results---contribution demonstrating that \\rasp{}'s post-prune advantage translates to superior post-RLVR reasoning performance.]\n    \\item We provide evidence that the optimal pruning strategy is conditioned on the recovery paradigm: \\rasp{} and importance-only pruning exhibit reversed relative advantages under SFT versus RLVR recovery [TBD: pending GRPO confirmation], supporting the notion of \\emph{paradigm-conditioned prunability}.\n\\end{enumerate}\n",
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_01RA8n6J1tCJNWp2U2kMVrgr`</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
  "description": "Count words in introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "2b0a879f-b958-47cf-b965-638075fa857a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DJVBKp9SotEDeKDx6XeYRw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3057,
      "cache_read_input_tokens": 32347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3057
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T09:09:58.313Z_

<details><summary>↩ Tool result · `toolu_01RA8n6J1tCJNWp2U2kMVrgr`</summary>

```text
942 /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "532a7064-9539-4ac3-8d5a-174aba7806f8",
  "tool_use_result": {
    "stdout": "942 /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
942 words including LaTeX commands. The actual rendered word count will be lower since LaTeX commands don't count as words. But the task says 1000-1400 words with `wc -w`. Let me check - 942 is below the 1000 minimum. I need to expand some paragraphs.

Actually, `wc -w` counts LaTeX commands as words too, so the actual prose word count is probably around 850-900. But the task says to check with `wc -w` and it should be 1000-1400. Let me expand a bit.


I should focus on beefing up the thinner sections—particularly the gap analysis and the insight paragraphs, plus adding more context around the key metrics to push the word count up to the required range.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "a51408ed-0e20-4f99-b2a4-bde0cf926c46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PbtqWqv1i8ysaeEpT8dNwX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 167,
      "cache_read_input_tokens": 35404,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 167
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 16_

942 words — below the 1000 minimum. Let me expand a few paragraphs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "010885f7-ceb6-4a00-9427-99d6805e9b0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PbtqWqv1i8ysaeEpT8dNwX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 167,
      "cache_read_input_tokens": 35404,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 167
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01GVRPgkgBeM9egPbV9u1Y7C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "095a0866-d92e-466d-8f90-612edd9664ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PbtqWqv1i8ysaeEpT8dNwX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 167,
      "cache_read_input_tokens": 35404,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 167
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T09:10:05.862Z_

<details><summary>↩ Tool result · `toolu_01GVRPgkgBeM9egPbV9u1Y7C`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	GRPO training~\citep{shao2024grpo} on an unpruned DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} drives reward from 0 to 0.661 over 100 steps---a trajectory that, by every reinforcement learning diagnostic, signals substantial policy improvement.
5	Yet GSM8K~\citep{cobbe2021gsm8k} accuracy remains at exactly 81.27\% throughout: the same 1{,}072 out of 1{,}319 problems solved before and after training, with zero net change in which problems the model can solve.
6	The reward signal that GRPO optimizes and the downstream reasoning accuracy that practitioners care about are, in this regime, orthogonal.
7	This observation---\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain, and sets the stage for our central finding: the interaction between structural pruning and GRPO training dynamics.
8	
9	On pruned models, the decoupled reward signal becomes catastrophic.
10	Structured pruning at 20\% sparsity removes entire attention heads and MLP channels~\citep{llmpruner2023,graspprune2026}, degrading the model's internal representations and narrowing its exploration capacity.
11	When GRPO is applied to these pruned architectures, training does not merely stall---it \emph{collapses}: reward drops to near-zero and per-sample reward variance vanishes as the policy degenerates to a single low-reward mode.
12	The collapse severity depends on \emph{what} was pruned.
13	\rasp{}, which uses CKA-based functional overlap~\citep{kornblith2019cka} to preferentially remove high-redundancy structures, collapses at step~10---six times faster than importance-only pruning, which collapses around step~60.
14	By removing functionally overlapping heads that served as exploration buffers, \rasp{} inadvertently eliminates the structural diversity that GRPO requires for stable optimization.
15	Crucially, the decoupling is bidirectional: just as reward increase on the unpruned model does not improve accuracy, reward collapse on pruned models does not degrade it.
16	Post-GRPO accuracy for the \rasp{}-pruned model is 61.87\%, nearly identical to its 61.49\% post-SFT baseline ($N{=}1{,}319$).
17	Neither reward improvement nor reward collapse changes reasoning performance---the two signals are genuinely independent.
18	
19	The current prune-recover-align pipeline treats its stages as independent: pruning methods optimize for immediate post-pruning accuracy~\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\citep{selfhealing2025,paser2025}.
20	\citet{selfhealing2025} report that RLVR-based recovery restores up to 95\% of pre-pruning performance---but their experiments use unstructured magnitude pruning at high sparsity and do not document per-step training dynamics.
21	No prior work has studied whether the \emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.
22	This gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.
23	
24	Our experiments reveal a \emph{Redundancy-Stability Tradeoff} at the heart of this interaction.
25	Functional redundancy---the degree to which a structure's computation overlaps with its within-layer peers---plays opposite roles depending on the recovery paradigm.
26	For SFT-based recovery, redundant structures are safely removable: their function can be redistributed through supervised gradient signals that directly optimize the retained architecture's output distribution.
27	For RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.
28	This connects to the analysis of \citet{rlsqueezes2026}, who show that RLVR recovers through global exploration and path compression---a process that requires diverse internal pathways---while SFT recovers through local trajectory imitation, which demands only sufficient representational capacity.
29	The Redundancy-Stability Tradeoff implies that optimal pruning is fundamentally conditioned on the intended recovery paradigm: structures safe to remove under SFT are precisely those dangerous to remove under RLVR.
30	
31	We formalize this tradeoff through \textbf{Recovery-Aware Structured Pruning (\rasp{})}, a three-stage framework illustrated in Figure~\ref{fig:framework}.
32	In Stage~1, \rasp{} computes for each attention head and MLP channel both a gradient-based importance score $I(h)$ and a functional overlap score $F(h)$ via intra-layer CKA~\citep{kornblith2019cka}.
33	In Stage~2, these are combined into a recovery-aware pruning score $S(h) = I(h) \times (1 - F(h))^\alpha$ that protects structures which are both important and functionally unique, while allowing removal of important-but-redundant structures.
34	In Stage~3, the pruned model undergoes SFT warmup followed by GRPO-based RLVR~\citep{shao2024grpo}.
35	Unlike prior CKA applications that measure inter-layer similarity for depth pruning~\citep{mpruner2024,lachance2024cka}, \rasp{} uses \emph{intra-layer} CKA between individual GQA groups~\citep{ainslie2023gqa} and MLP channels to quantify per-structure redundancy---a finer granularity targeting a fundamentally different objective.
36	\rasp{} was originally designed to optimize RLVR recoverability, but its failure under GRPO---collapsing faster than the baseline it was meant to improve---is precisely what reveals the Redundancy-Stability Tradeoff and establishes \rasp{} as a diagnostic tool for structural damage type.
37	
38	At 20\% structured sparsity on DeepSeek-R1-Distill-Qwen-7B, \rasp{} demonstrates clear advantages where redundancy removal helps and clear penalties where it hurts.
39	Immediately after pruning, \rasp{} retains 29\% GSM8K accuracy versus 1\% for importance-only pruning ($N{=}100$, $p{<}0.0001$), confirming that preserving functionally unique structures protects reasoning capacity.
40	After SFT recovery, \rasp{} reaches 61.49\% versus 59.29\% for importance-only (+2.2pp, $N{=}1{,}319$), showing that the post-prune advantage partially transfers through supervised recovery.
41	After GRPO training, reward-accuracy decoupling is universal across all conditions: \rasp{} collapses at step~10, importance-only at step~60, yet post-GRPO accuracy (61.87\% vs.\ 58.91\%) remains within the range established by SFT alone.
42	The collapse severity gradient---6$\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.
43	[TBD-25\%: Multi-sparsity results at 25\% to test tradeoff generalization.]
44	[TBD-QwenMath: Cross-model validation on Qwen2.5-Math-7B.]
45	
46	Our contributions are:
47	\begin{enumerate}[nosep,leftmargin=*]
48	    \item We document \emph{universal GRPO reward-accuracy decoupling}: reward improvement never translates to accuracy gain post-SFT, and this holds bidirectionally---neither reward increase on unpruned models nor reward collapse on pruned models changes reasoning performance.
49	    \item We identify \emph{pruning-induced GRPO training collapse} with a severity gradient that diagnoses structural damage type: CKA-aware pruning (\rasp{}) collapses 6$\times$ faster than importance-only pruning at matched sparsity, because it removes the functionally redundant structures that GRPO relies on for stable exploration.
50	    \item We reveal the \emph{Redundancy-Stability Tradeoff}: structures optimal for SFT recovery (high-overlap, functionally redundant) are exactly those required for RLVR training stability---optimal pruning is fundamentally conditioned on the recovery paradigm.
51	    \item[\textbullet] [TBD-QwenMath: Multi-model validation contribution.]
52	\end{enumerate}
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "d4d904bb-c434-43db-a7bb-39430a55b5c8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\nGRPO training~\\citep{shao2024grpo} on an unpruned DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} drives reward from 0 to 0.661 over 100 steps---a trajectory that, by every reinforcement learning diagnostic, signals substantial policy improvement.\nYet GSM8K~\\citep{cobbe2021gsm8k} accuracy remains at exactly 81.27\\% throughout: the same 1{,}072 out of 1{,}319 problems solved before and after training, with zero net change in which problems the model can solve.\nThe reward signal that GRPO optimizes and the downstream reasoning accuracy that practitioners care about are, in this regime, orthogonal.\nThis observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain, and sets the stage for our central finding: the interaction between structural pruning and GRPO training dynamics.\n\nOn pruned models, the decoupled reward signal becomes catastrophic.\nStructured pruning at 20\\% sparsity removes entire attention heads and MLP channels~\\citep{llmpruner2023,graspprune2026}, degrading the model's internal representations and narrowing its exploration capacity.\nWhen GRPO is applied to these pruned architectures, training does not merely stall---it \\emph{collapses}: reward drops to near-zero and per-sample reward variance vanishes as the policy degenerates to a single low-reward mode.\nThe collapse severity depends on \\emph{what} was pruned.\n\\rasp{}, which uses CKA-based functional overlap~\\citep{kornblith2019cka} to preferentially remove high-redundancy structures, collapses at step~10---six times faster than importance-only pruning, which collapses around step~60.\nBy removing functionally overlapping heads that served as exploration buffers, \\rasp{} inadvertently eliminates the structural diversity that GRPO requires for stable optimization.\nCrucially, the decoupling is bidirectional: just as reward increase on the unpruned model does not improve accuracy, reward collapse on pruned models does not degrade it.\nPost-GRPO accuracy for the \\rasp{}-pruned model is 61.87\\%, nearly identical to its 61.49\\% post-SFT baseline ($N{=}1{,}319$).\nNeither reward improvement nor reward collapse changes reasoning performance---the two signals are genuinely independent.\n\nThe current prune-recover-align pipeline treats its stages as independent: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.\n\\citet{selfhealing2025} report that RLVR-based recovery restores up to 95\\% of pre-pruning performance---but their experiments use unstructured magnitude pruning at high sparsity and do not document per-step training dynamics.\nNo prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.\n\nOur experiments reveal a \\emph{Redundancy-Stability Tradeoff} at the heart of this interaction.\nFunctional redundancy---the degree to which a structure's computation overlaps with its within-layer peers---plays opposite roles depending on the recovery paradigm.\nFor SFT-based recovery, redundant structures are safely removable: their function can be redistributed through supervised gradient signals that directly optimize the retained architecture's output distribution.\nFor RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.\nThis connects to the analysis of \\citet{rlsqueezes2026}, who show that RLVR recovers through global exploration and path compression---a process that requires diverse internal pathways---while SFT recovers through local trajectory imitation, which demands only sufficient representational capacity.\nThe Redundancy-Stability Tradeoff implies that optimal pruning is fundamentally conditioned on the intended recovery paradigm: structures safe to remove under SFT are precisely those dangerous to remove under RLVR.\n\nWe formalize this tradeoff through \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework illustrated in Figure~\\ref{fig:framework}.\nIn Stage~1, \\rasp{} computes for each attention head and MLP channel both a gradient-based importance score $I(h)$ and a functional overlap score $F(h)$ via intra-layer CKA~\\citep{kornblith2019cka}.\nIn Stage~2, these are combined into a recovery-aware pruning score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important and functionally unique, while allowing removal of important-but-redundant structures.\nIn Stage~3, the pruned model undergoes SFT warmup followed by GRPO-based RLVR~\\citep{shao2024grpo}.\nUnlike prior CKA applications that measure inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups~\\citep{ainslie2023gqa} and MLP channels to quantify per-structure redundancy---a finer granularity targeting a fundamentally different objective.\n\\rasp{} was originally designed to optimize RLVR recoverability, but its failure under GRPO---collapsing faster than the baseline it was meant to improve---is precisely what reveals the Redundancy-Stability Tradeoff and establishes \\rasp{} as a diagnostic tool for structural damage type.\n\nAt 20\\% structured sparsity on DeepSeek-R1-Distill-Qwen-7B, \\rasp{} demonstrates clear advantages where redundancy removal helps and clear penalties where it hurts.\nImmediately after pruning, \\rasp{} retains 29\\% GSM8K accuracy versus 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$), confirming that preserving functionally unique structures protects reasoning capacity.\nAfter SFT recovery, \\rasp{} reaches 61.49\\% versus 59.29\\% for importance-only (+2.2pp, $N{=}1{,}319$), showing that the post-prune advantage partially transfers through supervised recovery.\nAfter GRPO training, reward-accuracy decoupling is universal across all conditions: \\rasp{} collapses at step~10, importance-only at step~60, yet post-GRPO accuracy (61.87\\% vs.\\ 58.91\\%) remains within the range established by SFT alone.\nThe collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.\n[TBD-25\\%: Multi-sparsity results at 25\\% to test tradeoff generalization.]\n[TBD-QwenMath: Cross-model validation on Qwen2.5-Math-7B.]\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We document \\emph{universal GRPO reward-accuracy decoupling}: reward improvement never translates to accuracy gain post-SFT, and this holds bidirectionally---neither reward increase on unpruned models nor reward collapse on pruned models changes reasoning performance.\n    \\item We identify \\emph{pruning-induced GRPO training collapse} with a severity gradient that diagnoses structural damage type: CKA-aware pruning (\\rasp{}) collapses 6$\\times$ faster than importance-only pruning at matched sparsity, because it removes the functionally redundant structures that GRPO relies on for stable exploration.\n    \\item We reveal the \\emph{Redundancy-Stability Tradeoff}: structures optimal for SFT recovery (high-overlap, functionally redundant) are exactly those required for RLVR training stability---optimal pruning is fundamentally conditioned on the recovery paradigm.\n    \\item[\\textbullet] [TBD-QwenMath: Multi-model validation contribution.]\n\\end{enumerate}\n",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
I need to expand from 942 to at least 1000 words. Let me expand P1 (add more context about why this is surprising), P3 (add a sentence about the lottery ticket hypothesis connection or more about the gap), and P4 (expand on why the tradeoff is important). Let me think about what to add.

P1 - I could add a sentence about what practitioners expect from GRPO training (that reward improvement should indicate capability gain).

P3 - I could add a sentence about the lottery ticket hypothesis or about the assumption that pruning criteria are recovery-agnostic. I could also expand on what Self-Healing specifically does.


P4 - I should explain how redundant structures in the network actually create space for the model to explore different solution paths during training, which is why removing them constrains the learning process. P6 - I could also note how the collapse gradient serves as a useful diagnostic signal that tells us something fundamental about what's happening during the pruning and recovery process.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "70022c5d-6f8d-4ee0-b010-a6c06173730f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Qqa6tt7pK8ywQpk1caHkH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2537,
      "cache_read_input_tokens": 35571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2537
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 20_

I'll expand P1, P3, and P4 to push past 1000 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "341ad0c4-35bc-432b-985e-d86cc64be453",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Qqa6tt7pK8ywQpk1caHkH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2537,
      "cache_read_input_tokens": 35571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2537
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01JGJzAFCpGGH5XDt3DSkZhf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
  "old_string": "This observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain, and sets the stage for our central finding: the interaction between structural pruning and GRPO training dynamics.",
  "new_string": "This observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain.\nIf reward and accuracy can move independently even on an unpruned, fully capable model, then GRPO's training signal carries less information about reasoning ability than commonly assumed.\nThis sets the stage for our central finding: when structural pruning enters the picture, reward-accuracy decoupling does not merely persist---it becomes the mechanism through which pruning decisions manifest as training pathology."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "6c8c5d7e-7b17-4aa2-bab4-04d9a2d91b29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Qqa6tt7pK8ywQpk1caHkH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2537,
      "cache_read_input_tokens": 35571,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2537
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T09:10:16.615Z_

<details><summary>↩ Tool result · `toolu_01JGJzAFCpGGH5XDt3DSkZhf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "30312a51-b28a-4018-ba53-71bf7ec91896",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
    "oldString": "This observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain, and sets the stage for our central finding: the interaction between structural pruning and GRPO training dynamics.",
    "newString": "This observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain.\nIf reward and accuracy can move independently even on an unpruned, fully capable model, then GRPO's training signal carries less information about reasoning ability than commonly assumed.\nThis sets the stage for our central finding: when structural pruning enters the picture, reward-accuracy decoupling does not merely persist---it becomes the mechanism through which pruning decisions manifest as training pathology.",
    "originalFile": "\\section{Introduction}\n\\label{sec:intro}\n\nGRPO training~\\citep{shao2024grpo} on an unpruned DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} drives reward from 0 to 0.661 over 100 steps---a trajectory that, by every reinforcement learning diagnostic, signals substantial policy improvement.\nYet GSM8K~\\citep{cobbe2021gsm8k} accuracy remains at exactly 81.27\\% throughout: the same 1{,}072 out of 1{,}319 problems solved before and after training, with zero net change in which problems the model can solve.\nThe reward signal that GRPO optimizes and the downstream reasoning accuracy that practitioners care about are, in this regime, orthogonal.\nThis observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain, and sets the stage for our central finding: the interaction between structural pruning and GRPO training dynamics.\n\nOn pruned models, the decoupled reward signal becomes catastrophic.\nStructured pruning at 20\\% sparsity removes entire attention heads and MLP channels~\\citep{llmpruner2023,graspprune2026}, degrading the model's internal representations and narrowing its exploration capacity.\nWhen GRPO is applied to these pruned architectures, training does not merely stall---it \\emph{collapses}: reward drops to near-zero and per-sample reward variance vanishes as the policy degenerates to a single low-reward mode.\nThe collapse severity depends on \\emph{what} was pruned.\n\\rasp{}, which uses CKA-based functional overlap~\\citep{kornblith2019cka} to preferentially remove high-redundancy structures, collapses at step~10---six times faster than importance-only pruning, which collapses around step~60.\nBy removing functionally overlapping heads that served as exploration buffers, \\rasp{} inadvertently eliminates the structural diversity that GRPO requires for stable optimization.\nCrucially, the decoupling is bidirectional: just as reward increase on the unpruned model does not improve accuracy, reward collapse on pruned models does not degrade it.\nPost-GRPO accuracy for the \\rasp{}-pruned model is 61.87\\%, nearly identical to its 61.49\\% post-SFT baseline ($N{=}1{,}319$).\nNeither reward improvement nor reward collapse changes reasoning performance---the two signals are genuinely independent.\n\nThe current prune-recover-align pipeline treats its stages as independent: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.\n\\citet{selfhealing2025} report that RLVR-based recovery restores up to 95\\% of pre-pruning performance---but their experiments use unstructured magnitude pruning at high sparsity and do not document per-step training dynamics.\nNo prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.\n\nOur experiments reveal a \\emph{Redundancy-Stability Tradeoff} at the heart of this interaction.\nFunctional redundancy---the degree to which a structure's computation overlaps with its within-layer peers---plays opposite roles depending on the recovery paradigm.\nFor SFT-based recovery, redundant structures are safely removable: their function can be redistributed through supervised gradient signals that directly optimize the retained architecture's output distribution.\nFor RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.\nThis connects to the analysis of \\citet{rlsqueezes2026}, who show that RLVR recovers through global exploration and path compression---a process that requires diverse internal pathways---while SFT recovers through local trajectory imitation, which demands only sufficient representational capacity.\nThe Redundancy-Stability Tradeoff implies that optimal pruning is fundamentally conditioned on the intended recovery paradigm: structures safe to remove under SFT are precisely those dangerous to remove under RLVR.\n\nWe formalize this tradeoff through \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework illustrated in Figure~\\ref{fig:framework}.\nIn Stage~1, \\rasp{} computes for each attention head and MLP channel both a gradient-based importance score $I(h)$ and a functional overlap score $F(h)$ via intra-layer CKA~\\citep{kornblith2019cka}.\nIn Stage~2, these are combined into a recovery-aware pruning score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important and functionally unique, while allowing removal of important-but-redundant structures.\nIn Stage~3, the pruned model undergoes SFT warmup followed by GRPO-based RLVR~\\citep{shao2024grpo}.\nUnlike prior CKA applications that measure inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups~\\citep{ainslie2023gqa} and MLP channels to quantify per-structure redundancy---a finer granularity targeting a fundamentally different objective.\n\\rasp{} was originally designed to optimize RLVR recoverability, but its failure under GRPO---collapsing faster than the baseline it was meant to improve---is precisely what reveals the Redundancy-Stability Tradeoff and establishes \\rasp{} as a diagnostic tool for structural damage type.\n\nAt 20\\% structured sparsity on DeepSeek-R1-Distill-Qwen-7B, \\rasp{} demonstrates clear advantages where redundancy removal helps and clear penalties where it hurts.\nImmediately after pruning, \\rasp{} retains 29\\% GSM8K accuracy versus 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$), confirming that preserving functionally unique structures protects reasoning capacity.\nAfter SFT recovery, \\rasp{} reaches 61.49\\% versus 59.29\\% for importance-only (+2.2pp, $N{=}1{,}319$), showing that the post-prune advantage partially transfers through supervised recovery.\nAfter GRPO training, reward-accuracy decoupling is universal across all conditions: \\rasp{} collapses at step~10, importance-only at step~60, yet post-GRPO accuracy (61.87\\% vs.\\ 58.91\\%) remains within the range established by SFT alone.\nThe collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.\n[TBD-25\\%: Multi-sparsity results at 25\\% to test tradeoff generalization.]\n[TBD-QwenMath: Cross-model validation on Qwen2.5-Math-7B.]\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We document \\emph{universal GRPO reward-accuracy decoupling}: reward improvement never translates to accuracy gain post-SFT, and this holds bidirectionally---neither reward increase on unpruned models nor reward collapse on pruned models changes reasoning performance.\n    \\item We identify \\emph{pruning-induced GRPO training collapse} with a severity gradient that diagnoses structural damage type: CKA-aware pruning (\\rasp{}) collapses 6$\\times$ faster than importance-only pruning at matched sparsity, because it removes the functionally redundant structures that GRPO relies on for stable exploration.\n    \\item We reveal the \\emph{Redundancy-Stability Tradeoff}: structures optimal for SFT recovery (high-overlap, functionally redundant) are exactly those required for RLVR training stability---optimal pruning is fundamentally conditioned on the recovery paradigm.\n    \\item[\\textbullet] [TBD-QwenMath: Multi-model validation contribution.]\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 7,
        "newStart": 4,
        "newLines": 9,
        "lines": [
          " GRPO training~\\citep{shao2024grpo} on an unpruned DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} drives reward from 0 to 0.661 over 100 steps---a trajectory that, by every reinforcement learning diagnostic, signals substantial policy improvement.",
          " Yet GSM8K~\\citep{cobbe2021gsm8k} accuracy remains at exactly 81.27\\% throughout: the same 1{,}072 out of 1{,}319 problems solved before and after training, with zero net change in which problems the model can solve.",
          " The reward signal that GRPO optimizes and the downstream reasoning accuracy that practitioners care about are, in this regime, orthogonal.",
          "-This observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain, and sets the stage for our central finding: the interaction between structural pruning and GRPO training dynamics.",
          "+This observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain.",
          "+If reward and accuracy can move independently even on an unpruned, fully capable model, then GRPO's training signal carries less information about reasoning ability than commonly assumed.",
          "+This sets the stage for our central finding: when structural pruning enters the picture, reward-accuracy decoupling does not merely persist---it becomes the mechanism through which pruning decisions manifest as training pathology.",
          " ",
          " On pruned models, the decoupled reward signal becomes catastrophic.",
          " Structured pruning at 20\\% sparsity removes entire attention heads and MLP channels~\\citep{llmpruner2023,graspprune2026}, degrading the model's internal representations and narrowing its exploration capacity."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Edit · `toolu_01S4v2k9F6iPQadwt6qxKCWb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
  "old_string": "No prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.",
  "new_string": "No prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThe lottery ticket hypothesis~\\citep{frankle2019lth} established that \\emph{which} weights survive pruning matters for trainability, but this insight has not been extended to structured pruning of reasoning models or to the interaction between pruning criteria and RL-based recovery.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "b6f6e482-0d10-46d0-99ae-e0752ebd0dc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVMGDJVQNkpsubuQAS882j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 38108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 718
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T09:10:24.058Z_

<details><summary>↩ Tool result · `toolu_01S4v2k9F6iPQadwt6qxKCWb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "051d41d3-160c-4530-aaad-404f5c3db97d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
    "oldString": "No prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.",
    "newString": "No prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThe lottery ticket hypothesis~\\citep{frankle2019lth} established that \\emph{which} weights survive pruning matters for trainability, but this insight has not been extended to structured pruning of reasoning models or to the interaction between pruning criteria and RL-based recovery.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.",
    "originalFile": "\\section{Introduction}\n\\label{sec:intro}\n\nGRPO training~\\citep{shao2024grpo} on an unpruned DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} drives reward from 0 to 0.661 over 100 steps---a trajectory that, by every reinforcement learning diagnostic, signals substantial policy improvement.\nYet GSM8K~\\citep{cobbe2021gsm8k} accuracy remains at exactly 81.27\\% throughout: the same 1{,}072 out of 1{,}319 problems solved before and after training, with zero net change in which problems the model can solve.\nThe reward signal that GRPO optimizes and the downstream reasoning accuracy that practitioners care about are, in this regime, orthogonal.\nThis observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain.\nIf reward and accuracy can move independently even on an unpruned, fully capable model, then GRPO's training signal carries less information about reasoning ability than commonly assumed.\nThis sets the stage for our central finding: when structural pruning enters the picture, reward-accuracy decoupling does not merely persist---it becomes the mechanism through which pruning decisions manifest as training pathology.\n\nOn pruned models, the decoupled reward signal becomes catastrophic.\nStructured pruning at 20\\% sparsity removes entire attention heads and MLP channels~\\citep{llmpruner2023,graspprune2026}, degrading the model's internal representations and narrowing its exploration capacity.\nWhen GRPO is applied to these pruned architectures, training does not merely stall---it \\emph{collapses}: reward drops to near-zero and per-sample reward variance vanishes as the policy degenerates to a single low-reward mode.\nThe collapse severity depends on \\emph{what} was pruned.\n\\rasp{}, which uses CKA-based functional overlap~\\citep{kornblith2019cka} to preferentially remove high-redundancy structures, collapses at step~10---six times faster than importance-only pruning, which collapses around step~60.\nBy removing functionally overlapping heads that served as exploration buffers, \\rasp{} inadvertently eliminates the structural diversity that GRPO requires for stable optimization.\nCrucially, the decoupling is bidirectional: just as reward increase on the unpruned model does not improve accuracy, reward collapse on pruned models does not degrade it.\nPost-GRPO accuracy for the \\rasp{}-pruned model is 61.87\\%, nearly identical to its 61.49\\% post-SFT baseline ($N{=}1{,}319$).\nNeither reward improvement nor reward collapse changes reasoning performance---the two signals are genuinely independent.\n\nThe current prune-recover-align pipeline treats its stages as independent: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.\n\\citet{selfhealing2025} report that RLVR-based recovery restores up to 95\\% of pre-pruning performance---but their experiments use unstructured magnitude pruning at high sparsity and do not document per-step training dynamics.\nNo prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.\n\nOur experiments reveal a \\emph{Redundancy-Stability Tradeoff} at the heart of this interaction.\nFunctional redundancy---the degree to which a structure's computation overlaps with its within-layer peers---plays opposite roles depending on the recovery paradigm.\nFor SFT-based recovery, redundant structures are safely removable: their function can be redistributed through supervised gradient signals that directly optimize the retained architecture's output distribution.\nFor RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.\nThis connects to the analysis of \\citet{rlsqueezes2026}, who show that RLVR recovers through global exploration and path compression---a process that requires diverse internal pathways---while SFT recovers through local trajectory imitation, which demands only sufficient representational capacity.\nThe Redundancy-Stability Tradeoff implies that optimal pruning is fundamentally conditioned on the intended recovery paradigm: structures safe to remove under SFT are precisely those dangerous to remove under RLVR.\n\nWe formalize this tradeoff through \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework illustrated in Figure~\\ref{fig:framework}.\nIn Stage~1, \\rasp{} computes for each attention head and MLP channel both a gradient-based importance score $I(h)$ and a functional overlap score $F(h)$ via intra-layer CKA~\\citep{kornblith2019cka}.\nIn Stage~2, these are combined into a recovery-aware pruning score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important and functionally unique, while allowing removal of important-but-redundant structures.\nIn Stage~3, the pruned model undergoes SFT warmup followed by GRPO-based RLVR~\\citep{shao2024grpo}.\nUnlike prior CKA applications that measure inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups~\\citep{ainslie2023gqa} and MLP channels to quantify per-structure redundancy---a finer granularity targeting a fundamentally different objective.\n\\rasp{} was originally designed to optimize RLVR recoverability, but its failure under GRPO---collapsing faster than the baseline it was meant to improve---is precisely what reveals the Redundancy-Stability Tradeoff and establishes \\rasp{} as a diagnostic tool for structural damage type.\n\nAt 20\\% structured sparsity on DeepSeek-R1-Distill-Qwen-7B, \\rasp{} demonstrates clear advantages where redundancy removal helps and clear penalties where it hurts.\nImmediately after pruning, \\rasp{} retains 29\\% GSM8K accuracy versus 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$), confirming that preserving functionally unique structures protects reasoning capacity.\nAfter SFT recovery, \\rasp{} reaches 61.49\\% versus 59.29\\% for importance-only (+2.2pp, $N{=}1{,}319$), showing that the post-prune advantage partially transfers through supervised recovery.\nAfter GRPO training, reward-accuracy decoupling is universal across all conditions: \\rasp{} collapses at step~10, importance-only at step~60, yet post-GRPO accuracy (61.87\\% vs.\\ 58.91\\%) remains within the range established by SFT alone.\nThe collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.\n[TBD-25\\%: Multi-sparsity results at 25\\% to test tradeoff generalization.]\n[TBD-QwenMath: Cross-model validation on Qwen2.5-Math-7B.]\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We document \\emph{universal GRPO reward-accuracy decoupling}: reward improvement never translates to accuracy gain post-SFT, and this holds bidirectionally---neither reward increase on unpruned models nor reward collapse on pruned models changes reasoning performance.\n    \\item We identify \\emph{pruning-induced GRPO training collapse} with a severity gradient that diagnoses structural damage type: CKA-aware pruning (\\rasp{}) collapses 6$\\times$ faster than importance-only pruning at matched sparsity, because it removes the functionally redundant structures that GRPO relies on for stable exploration.\n    \\item We reveal the \\emph{Redundancy-Stability Tradeoff}: structures optimal for SFT recovery (high-overlap, functionally redundant) are exactly those required for RLVR training stability---optimal pruning is fundamentally conditioned on the recovery paradigm.\n    \\item[\\textbullet] [TBD-QwenMath: Multi-model validation contribution.]\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 21,
        "oldLines": 6,
        "newStart": 21,
        "newLines": 7,
        "lines": [
          " The current prune-recover-align pipeline treats its stages as independent: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.",
          " \\citet{selfhealing2025} report that RLVR-based recovery restores up to 95\\% of pre-pruning performance---but their experiments use unstructured magnitude pruning at high sparsity and do not document per-step training dynamics.",
          " No prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.",
          "+The lottery ticket hypothesis~\\citep{frankle2019lth} established that \\emph{which} weights survive pruning matters for trainability, but this insight has not been extended to structured pruning of reasoning models or to the interaction between pruning criteria and RL-based recovery.",
          " This gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.",
          " ",
          " Our experiments reveal a \\emph{Redundancy-Stability Tradeoff} at the heart of this interaction."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01DJr3V7Hcj9xMbtpJRj7kxz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
  "old_string": "For RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.",
  "new_string": "For RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.\nWhen multiple heads compute similar but not identical representations, GRPO can explore different reward-improving trajectories through different structural pathways; removing these overlapping alternatives collapses the policy's exploration capacity into a single mode."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "9ae38314-32bf-4b36-9fe9-0507d9d27942",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019e1vazeQ2F2ZUG9KPhVNr9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 38826,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 430
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T09:10:28.874Z_

<details><summary>↩ Tool result · `toolu_01DJr3V7Hcj9xMbtpJRj7kxz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "528c1961-52d3-41c3-be37-0b75c4607365",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
    "oldString": "For RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.",
    "newString": "For RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.\nWhen multiple heads compute similar but not identical representations, GRPO can explore different reward-improving trajectories through different structural pathways; removing these overlapping alternatives collapses the policy's exploration capacity into a single mode.",
    "originalFile": "\\section{Introduction}\n\\label{sec:intro}\n\nGRPO training~\\citep{shao2024grpo} on an unpruned DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} drives reward from 0 to 0.661 over 100 steps---a trajectory that, by every reinforcement learning diagnostic, signals substantial policy improvement.\nYet GSM8K~\\citep{cobbe2021gsm8k} accuracy remains at exactly 81.27\\% throughout: the same 1{,}072 out of 1{,}319 problems solved before and after training, with zero net change in which problems the model can solve.\nThe reward signal that GRPO optimizes and the downstream reasoning accuracy that practitioners care about are, in this regime, orthogonal.\nThis observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain.\nIf reward and accuracy can move independently even on an unpruned, fully capable model, then GRPO's training signal carries less information about reasoning ability than commonly assumed.\nThis sets the stage for our central finding: when structural pruning enters the picture, reward-accuracy decoupling does not merely persist---it becomes the mechanism through which pruning decisions manifest as training pathology.\n\nOn pruned models, the decoupled reward signal becomes catastrophic.\nStructured pruning at 20\\% sparsity removes entire attention heads and MLP channels~\\citep{llmpruner2023,graspprune2026}, degrading the model's internal representations and narrowing its exploration capacity.\nWhen GRPO is applied to these pruned architectures, training does not merely stall---it \\emph{collapses}: reward drops to near-zero and per-sample reward variance vanishes as the policy degenerates to a single low-reward mode.\nThe collapse severity depends on \\emph{what} was pruned.\n\\rasp{}, which uses CKA-based functional overlap~\\citep{kornblith2019cka} to preferentially remove high-redundancy structures, collapses at step~10---six times faster than importance-only pruning, which collapses around step~60.\nBy removing functionally overlapping heads that served as exploration buffers, \\rasp{} inadvertently eliminates the structural diversity that GRPO requires for stable optimization.\nCrucially, the decoupling is bidirectional: just as reward increase on the unpruned model does not improve accuracy, reward collapse on pruned models does not degrade it.\nPost-GRPO accuracy for the \\rasp{}-pruned model is 61.87\\%, nearly identical to its 61.49\\% post-SFT baseline ($N{=}1{,}319$).\nNeither reward improvement nor reward collapse changes reasoning performance---the two signals are genuinely independent.\n\nThe current prune-recover-align pipeline treats its stages as independent: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.\n\\citet{selfhealing2025} report that RLVR-based recovery restores up to 95\\% of pre-pruning performance---but their experiments use unstructured magnitude pruning at high sparsity and do not document per-step training dynamics.\nNo prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThe lottery ticket hypothesis~\\citep{frankle2019lth} established that \\emph{which} weights survive pruning matters for trainability, but this insight has not been extended to structured pruning of reasoning models or to the interaction between pruning criteria and RL-based recovery.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.\n\nOur experiments reveal a \\emph{Redundancy-Stability Tradeoff} at the heart of this interaction.\nFunctional redundancy---the degree to which a structure's computation overlaps with its within-layer peers---plays opposite roles depending on the recovery paradigm.\nFor SFT-based recovery, redundant structures are safely removable: their function can be redistributed through supervised gradient signals that directly optimize the retained architecture's output distribution.\nFor RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.\nThis connects to the analysis of \\citet{rlsqueezes2026}, who show that RLVR recovers through global exploration and path compression---a process that requires diverse internal pathways---while SFT recovers through local trajectory imitation, which demands only sufficient representational capacity.\nThe Redundancy-Stability Tradeoff implies that optimal pruning is fundamentally conditioned on the intended recovery paradigm: structures safe to remove under SFT are precisely those dangerous to remove under RLVR.\n\nWe formalize this tradeoff through \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework illustrated in Figure~\\ref{fig:framework}.\nIn Stage~1, \\rasp{} computes for each attention head and MLP channel both a gradient-based importance score $I(h)$ and a functional overlap score $F(h)$ via intra-layer CKA~\\citep{kornblith2019cka}.\nIn Stage~2, these are combined into a recovery-aware pruning score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important and functionally unique, while allowing removal of important-but-redundant structures.\nIn Stage~3, the pruned model undergoes SFT warmup followed by GRPO-based RLVR~\\citep{shao2024grpo}.\nUnlike prior CKA applications that measure inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups~\\citep{ainslie2023gqa} and MLP channels to quantify per-structure redundancy---a finer granularity targeting a fundamentally different objective.\n\\rasp{} was originally designed to optimize RLVR recoverability, but its failure under GRPO---collapsing faster than the baseline it was meant to improve---is precisely what reveals the Redundancy-Stability Tradeoff and establishes \\rasp{} as a diagnostic tool for structural damage type.\n\nAt 20\\% structured sparsity on DeepSeek-R1-Distill-Qwen-7B, \\rasp{} demonstrates clear advantages where redundancy removal helps and clear penalties where it hurts.\nImmediately after pruning, \\rasp{} retains 29\\% GSM8K accuracy versus 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$), confirming that preserving functionally unique structures protects reasoning capacity.\nAfter SFT recovery, \\rasp{} reaches 61.49\\% versus 59.29\\% for importance-only (+2.2pp, $N{=}1{,}319$), showing that the post-prune advantage partially transfers through supervised recovery.\nAfter GRPO training, reward-accuracy decoupling is universal across all conditions: \\rasp{} collapses at step~10, importance-only at step~60, yet post-GRPO accuracy (61.87\\% vs.\\ 58.91\\%) remains within the range established by SFT alone.\nThe collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.\n[TBD-25\\%: Multi-sparsity results at 25\\% to test tradeoff generalization.]\n[TBD-QwenMath: Cross-model validation on Qwen2.5-Math-7B.]\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We document \\emph{universal GRPO reward-accuracy decoupling}: reward improvement never translates to accuracy gain post-SFT, and this holds bidirectionally---neither reward increase on unpruned models nor reward collapse on pruned models changes reasoning performance.\n    \\item We identify \\emph{pruning-induced GRPO training collapse} with a severity gradient that diagnoses structural damage type: CKA-aware pruning (\\rasp{}) collapses 6$\\times$ faster than importance-only pruning at matched sparsity, because it removes the functionally redundant structures that GRPO relies on for stable exploration.\n    \\item We reveal the \\emph{Redundancy-Stability Tradeoff}: structures optimal for SFT recovery (high-overlap, functionally redundant) are exactly those required for RLVR training stability---optimal pruning is fundamentally conditioned on the recovery paradigm.\n    \\item[\\textbullet] [TBD-QwenMath: Multi-model validation contribution.]\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 28,
        "oldLines": 6,
        "newStart": 28,
        "newLines": 7,
        "lines": [
          " Functional redundancy---the degree to which a structure's computation overlaps with its within-layer peers---plays opposite roles depending on the recovery paradigm.",
          " For SFT-based recovery, redundant structures are safely removable: their function can be redistributed through supervised gradient signals that directly optimize the retained architecture's output distribution.",
          " For RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.",
          "+When multiple heads compute similar but not identical representations, GRPO can explore different reward-improving trajectories through different structural pathways; removing these overlapping alternatives collapses the policy's exploration capacity into a single mode.",
          " This connects to the analysis of \\citet{rlsqueezes2026}, who show that RLVR recovers through global exploration and path compression---a process that requires diverse internal pathways---while SFT recovers through local trajectory imitation, which demands only sufficient representational capacity.",
          " The Redundancy-Stability Tradeoff implies that optimal pruning is fundamentally conditioned on the intended recovery paradigm: structures safe to remove under SFT are precisely those dangerous to remove under RLVR.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_01Gsto3TbgiSLLR39oDrDwSA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
  "old_string": "The collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.",
  "new_string": "The collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.\nThis gradient provides a practical diagnostic: collapse timing under GRPO can distinguish between pruning strategies that damage exploration capacity (fast collapse) versus those that damage representational capacity (slow or no collapse), even when post-SFT accuracy is similar."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "672a2d88-973d-40e0-a213-70efd1cc8847",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WeJiVrF5zEB1pzTkfo2XHs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 39256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T09:10:34.080Z_

<details><summary>↩ Tool result · `toolu_01Gsto3TbgiSLLR39oDrDwSA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "120c42c8-db01-4a3b-a9da-499c57f2a4f8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
    "oldString": "The collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.",
    "newString": "The collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.\nThis gradient provides a practical diagnostic: collapse timing under GRPO can distinguish between pruning strategies that damage exploration capacity (fast collapse) versus those that damage representational capacity (slow or no collapse), even when post-SFT accuracy is similar.",
    "originalFile": "\\section{Introduction}\n\\label{sec:intro}\n\nGRPO training~\\citep{shao2024grpo} on an unpruned DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} drives reward from 0 to 0.661 over 100 steps---a trajectory that, by every reinforcement learning diagnostic, signals substantial policy improvement.\nYet GSM8K~\\citep{cobbe2021gsm8k} accuracy remains at exactly 81.27\\% throughout: the same 1{,}072 out of 1{,}319 problems solved before and after training, with zero net change in which problems the model can solve.\nThe reward signal that GRPO optimizes and the downstream reasoning accuracy that practitioners care about are, in this regime, orthogonal.\nThis observation---\\emph{reward-accuracy decoupling}---challenges the assumption that RLVR-based fine-tuning reliably translates reward improvement into capability gain.\nIf reward and accuracy can move independently even on an unpruned, fully capable model, then GRPO's training signal carries less information about reasoning ability than commonly assumed.\nThis sets the stage for our central finding: when structural pruning enters the picture, reward-accuracy decoupling does not merely persist---it becomes the mechanism through which pruning decisions manifest as training pathology.\n\nOn pruned models, the decoupled reward signal becomes catastrophic.\nStructured pruning at 20\\% sparsity removes entire attention heads and MLP channels~\\citep{llmpruner2023,graspprune2026}, degrading the model's internal representations and narrowing its exploration capacity.\nWhen GRPO is applied to these pruned architectures, training does not merely stall---it \\emph{collapses}: reward drops to near-zero and per-sample reward variance vanishes as the policy degenerates to a single low-reward mode.\nThe collapse severity depends on \\emph{what} was pruned.\n\\rasp{}, which uses CKA-based functional overlap~\\citep{kornblith2019cka} to preferentially remove high-redundancy structures, collapses at step~10---six times faster than importance-only pruning, which collapses around step~60.\nBy removing functionally overlapping heads that served as exploration buffers, \\rasp{} inadvertently eliminates the structural diversity that GRPO requires for stable optimization.\nCrucially, the decoupling is bidirectional: just as reward increase on the unpruned model does not improve accuracy, reward collapse on pruned models does not degrade it.\nPost-GRPO accuracy for the \\rasp{}-pruned model is 61.87\\%, nearly identical to its 61.49\\% post-SFT baseline ($N{=}1{,}319$).\nNeither reward improvement nor reward collapse changes reasoning performance---the two signals are genuinely independent.\n\nThe current prune-recover-align pipeline treats its stages as independent: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.\n\\citet{selfhealing2025} report that RLVR-based recovery restores up to 95\\% of pre-pruning performance---but their experiments use unstructured magnitude pruning at high sparsity and do not document per-step training dynamics.\nNo prior work has studied whether the \\emph{pruning criterion itself}---what structures are removed and why---affects RLVR training stability under structured pruning at moderate sparsity.\nThe lottery ticket hypothesis~\\citep{frankle2019lth} established that \\emph{which} weights survive pruning matters for trainability, but this insight has not been extended to structured pruning of reasoning models or to the interaction between pruning criteria and RL-based recovery.\nThis gap is consequential: if the choice of pruning strategy determines whether GRPO training succeeds or collapses, then pruning and recovery cannot be treated as modular, independent stages.\n\nOur experiments reveal a \\emph{Redundancy-Stability Tradeoff} at the heart of this interaction.\nFunctional redundancy---the degree to which a structure's computation overlaps with its within-layer peers---plays opposite roles depending on the recovery paradigm.\nFor SFT-based recovery, redundant structures are safely removable: their function can be redistributed through supervised gradient signals that directly optimize the retained architecture's output distribution.\nFor RLVR-based recovery, these same redundant structures are essential: they provide the structural diversity that enables GRPO's exploration-based optimization.\nWhen multiple heads compute similar but not identical representations, GRPO can explore different reward-improving trajectories through different structural pathways; removing these overlapping alternatives collapses the policy's exploration capacity into a single mode.\nThis connects to the analysis of \\citet{rlsqueezes2026}, who show that RLVR recovers through global exploration and path compression---a process that requires diverse internal pathways---while SFT recovers through local trajectory imitation, which demands only sufficient representational capacity.\nThe Redundancy-Stability Tradeoff implies that optimal pruning is fundamentally conditioned on the intended recovery paradigm: structures safe to remove under SFT are precisely those dangerous to remove under RLVR.\n\nWe formalize this tradeoff through \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework illustrated in Figure~\\ref{fig:framework}.\nIn Stage~1, \\rasp{} computes for each attention head and MLP channel both a gradient-based importance score $I(h)$ and a functional overlap score $F(h)$ via intra-layer CKA~\\citep{kornblith2019cka}.\nIn Stage~2, these are combined into a recovery-aware pruning score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important and functionally unique, while allowing removal of important-but-redundant structures.\nIn Stage~3, the pruned model undergoes SFT warmup followed by GRPO-based RLVR~\\citep{shao2024grpo}.\nUnlike prior CKA applications that measure inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups~\\citep{ainslie2023gqa} and MLP channels to quantify per-structure redundancy---a finer granularity targeting a fundamentally different objective.\n\\rasp{} was originally designed to optimize RLVR recoverability, but its failure under GRPO---collapsing faster than the baseline it was meant to improve---is precisely what reveals the Redundancy-Stability Tradeoff and establishes \\rasp{} as a diagnostic tool for structural damage type.\n\nAt 20\\% structured sparsity on DeepSeek-R1-Distill-Qwen-7B, \\rasp{} demonstrates clear advantages where redundancy removal helps and clear penalties where it hurts.\nImmediately after pruning, \\rasp{} retains 29\\% GSM8K accuracy versus 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$), confirming that preserving functionally unique structures protects reasoning capacity.\nAfter SFT recovery, \\rasp{} reaches 61.49\\% versus 59.29\\% for importance-only (+2.2pp, $N{=}1{,}319$), showing that the post-prune advantage partially transfers through supervised recovery.\nAfter GRPO training, reward-accuracy decoupling is universal across all conditions: \\rasp{} collapses at step~10, importance-only at step~60, yet post-GRPO accuracy (61.87\\% vs.\\ 58.91\\%) remains within the range established by SFT alone.\nThe collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.\n[TBD-25\\%: Multi-sparsity results at 25\\% to test tradeoff generalization.]\n[TBD-QwenMath: Cross-model validation on Qwen2.5-Math-7B.]\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We document \\emph{universal GRPO reward-accuracy decoupling}: reward improvement never translates to accuracy gain post-SFT, and this holds bidirectionally---neither reward increase on unpruned models nor reward collapse on pruned models changes reasoning performance.\n    \\item We identify \\emph{pruning-induced GRPO training collapse} with a severity gradient that diagnoses structural damage type: CKA-aware pruning (\\rasp{}) collapses 6$\\times$ faster than importance-only pruning at matched sparsity, because it removes the functionally redundant structures that GRPO relies on for stable exploration.\n    \\item We reveal the \\emph{Redundancy-Stability Tradeoff}: structures optimal for SFT recovery (high-overlap, functionally redundant) are exactly those required for RLVR training stability---optimal pruning is fundamentally conditioned on the recovery paradigm.\n    \\item[\\textbullet] [TBD-QwenMath: Multi-model validation contribution.]\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 44,
        "oldLines": 6,
        "newStart": 44,
        "newLines": 7,
        "lines": [
          " After SFT recovery, \\rasp{} reaches 61.49\\% versus 59.29\\% for importance-only (+2.2pp, $N{=}1{,}319$), showing that the post-prune advantage partially transfers through supervised recovery.",
          " After GRPO training, reward-accuracy decoupling is universal across all conditions: \\rasp{} collapses at step~10, importance-only at step~60, yet post-GRPO accuracy (61.87\\% vs.\\ 58.91\\%) remains within the range established by SFT alone.",
          " The collapse severity gradient---6$\\times$ faster for CKA-aware pruning---directly diagnoses the type of structural damage: removal of redundant structures destabilizes GRPO more than removal of important-but-unique structures, confirming the tradeoff.",
          "+This gradient provides a practical diagnostic: collapse timing under GRPO can distinguish between pruning strategies that damage exploration capacity (fast collapse) versus those that damage representational capacity (slow or no collapse), even when post-SFT accuracy is similar.",
          " [TBD-25\\%: Multi-sparsity results at 25\\% to test tradeoff generalization.]",
          " [TBD-QwenMath: Cross-model validation on Qwen2.5-Math-7B.]",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01L57UCUJ14XK4gJihbXGHF6`</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
  "description": "Count words in introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "a79c7c2c-fe7f-4341-acaa-21f69ac06e61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5oZCvaRxL3HJh16va6ptc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 39569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 70,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T09:10:37.242Z_

<details><summary>↩ Tool result · `toolu_01L57UCUJ14XK4gJihbXGHF6`</summary>

```text
1088 /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "d660127f-4ae4-4402-981a-f182992883b4",
  "tool_use_result": {
    "stdout": "1088 /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 31_

1088 words — within the 1000–1400 target. Introduction rewritten with the Redundancy-Stability Tradeoff narrative: opens with reward-accuracy decoupling on the unpruned model, escalates to pruning-induced GRPO collapse, identifies the tradeoff, and presents RASP as diagnostic tool rather than optimal method. All cite keys verified, `\rasp{}` macro used, [TBD-25%] and [TBD-QwenMath] placeholders retained.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "uuid": "3961618e-e3df-4f41-9a77-226a8f81aa05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165dKM8habaBWJTExK9VJmt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 168,
      "cache_read_input_tokens": 39936,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 168
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 32_

1088 words — within the 1000–1400 target. Introduction rewritten with the Redundancy-Stability Tradeoff narrative: opens with reward-accuracy decoupling on the unpruned model, escalates to pruning-induced GRPO collapse, identifies the tradeoff, and presents RASP as diagnostic tool rather than optimal method. All cite keys verified, `\rasp{}` macro used, [TBD-25%] and [TBD-QwenMath] placeholders retained.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 129833,
  "duration_api_ms": 130806,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "a9c26e21-cf95-4b10-9f46-533ce6b8018b",
  "total_cost_usd": 0.48006625,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 28263,
    "cache_read_input_tokens": 335997,
    "output_tokens": 5301,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 28263,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 120,
        "cache_read_input_tokens": 39936,
        "cache_creation_input_tokens": 168,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 168
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2729,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002844,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 5301,
      "cacheReadInputTokens": 335997,
      "cacheCreationInputTokens": 28263,
      "webSearchRequests": 0,
      "costUSD": 0.47722225,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e19a8309-5c70-4a26-a28e-db0d79e8a1fe"
}
```

</details>

---
