# paper writing background

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 0
- **Tool calls:** 40
- **Original source:** `logs/chats/worker_paper_writing_background_20260517T134047.jsonl`
- **Structured JSON:** [`e4c869cbf2a87bb82cfa.json`](../../sessions/e4/e4c869cbf2a87bb82cfa.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

81 recorded events

### Tool call

_source line 1 · 2026-05-17T13:44:17.174867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T13:44:17.175718+00:00_

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
94	4. CHECK   → 确认
…[truncated 7201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T13:44:17.175945+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T13:44:17.176312+00:00_

1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **
…[truncated 4866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T13:44:17.176495+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read existing paper sections",
  "subagent_type": "Explore",
  "prompt": "Read the existing paper sections in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/ — I need to see the experiments section and analysis section for consistency. Also check if there's a main.tex or similar file that shows the paper structure. Read all .tex files you find in that sections directory and in the paper directory."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Agent",
  "tool_args": {
    "description": "Read existing paper sections",
    "subagent_type": "Explore",
    "prompt": "Read the existing paper sections in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/ — I need to see the experiments section and analysis section for consistency. Also check if there's a main.tex or similar file that shows the paper structure. Read all .tex files you find in that sections directory and in the paper directory."
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T13:44:17.176668+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-17T13:44:17.176791+00:00_

docs/paper/sections/experiments.tex
docs/paper/experiments.tex
docs/paper/sections/analysis.tex
docs/paper/analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T13:44:17.176916+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper -type f -name \"*.tex\" 2>/dev/null | head -20",
  "description": "Find all .tex files in the paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper -type f -name \"*.tex\" 2>/dev/null | head -20",
    "description": "Find all .tex files in the paper directory"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T13:44:17.177031+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T13:44:17.177183+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T13:44:17.177358+00:00_

1	% experiments.tex -- Section 4: Main Results
2	% Experiment IDs (provenance):
3	%   Baseline 44.8%:              eval_stage1_only
4	%   ACIS k=0.5 zero-mask:       eval_stage1only_object_v2_fixed
5	%   ACIS k=0.7 zero-mask:       eval_k07_zero_mask
6	%   ACIS k=0.9 zero-mask:       eval_stage1only_k09
7	%   Random k=0.5:               eval_random_prune_k05
8	%   True removal k=0.5:         eval_true_removal_k05
9	%   Merge k=0.5:                eval_merge_k05
10	%   Spatial suite:              eval_spatial_prune_k05 (baseline 51.8%)
11	%   Goal suite:                 eval_goal_prune_k05 (baseline 63%)
12	
13	\section{Main Results}
14	\label{sec:results}
15	
16	Vision token pruning in Vision Transformers (ViTs) is widely regarded as a reliable efficiency technique.
17	DynamicViT~\cite{rao2021dynamicvit} removes 30\%--50\% of tokens with less than 0.5\% accuracy loss on ImageNet, and Token Merging (ToMe)~\cite{bolya2023tome} merges up to 40\% of tokens while retaining over 99\% of classification accuracy.
18	EViT~\cite{liang2022evit} similarly discards 50\% of inattentive tokens with negligible degradation.
19	These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\cite{hsu2025vlacache,wang2026vlaiap}.
20	Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\cite{liu2023libero}.
21	The result is unambiguous.
22	Every configuration produces 0\% SR, a complete collapse we term the \emph{cliff edge}.
23	
24	\begin{table}[t]
25	\centering
26	\caption{Ablation matrix across scoring functions, retention ratios, and pruning mechanisms. All six pruning conditions produce 0\% SR. The baseline runs the same checkpoint with pruning disabled (bypass mode). Wilson 95\% confidence intervals (CI) are computed over independent episodes. Experiment IDs are listed for reproducibility
…[truncated 4572 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T13:44:17.177593+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T13:44:17.178030+00:00_

1	% analysis.tex -- Section 5: Analysis
2	% Experiment IDs (provenance):
3	%   Attention entropy analysis:     attention_entropy_analysis
4	%   Single-step action error:       offline_singlestep_action_error
5	%   Action divergence:              action_divergence_v2_clean
6	%   Importance margin (G1):         mvp_imm_v8b_twostage
7	%   Token importance (G3, Spearman): plan_009_token_importance
8	
9	\section{Analysis}
10	\label{sec:analysis}
11	
12	Section~\ref{sec:results} established that all pruning configurations produce 0\% SR.
13	This section investigates \emph{why} the cliff edge occurs.
14	We present three complementary lines of evidence: the LLM backbone attends to vision tokens near-uniformly (\S\ref{sec:uniform_attention}), pruning causes immediate single-step action failures rather than gradual error accumulation (\S\ref{sec:action_disruption}), and standard offline evaluation metrics fail to predict this catastrophic closed-loop collapse (\S\ref{sec:metric_disconnect}).
15	Section~\ref{sec:why_vit_works} synthesizes these findings into a unified mechanistic explanation.
16	
17	\subsection{Uniform Attention Distribution}
18	\label{sec:uniform_attention}
19	
20	Token pruning in ViT classifiers succeeds because attention concentrates on a small set of discriminative patches and leaves most tokens redundant.
21	DynamicViT~\cite{rao2021dynamicvit} and ToMe~\cite{bolya2023tome} exploit this concentration: tokens that receive low attention contribute little to the classification decision and can be safely removed.
22	We test whether VLA models exhibit the same attention pattern.
23	
24	We extract attention weights from the LLM backbone (Qwen2-0.5B~\cite{yang2024qwen2}) over all vision tokens across three LIBERO tasks.
25	The attention entropy ratio reaches 0.98 (observed entropy of 6.86 bits out of a maximum of 7.0 bits for a perfectly uniform distribution).
26	The two camera views receive comparable attention (53.8\% for cam1, 46.2\% for cam2), and this patter
…[truncated 10142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T13:44:17.178248+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T13:44:17.178404+00:00_

1	% experiments.tex — Section 4: Main Results
2	\section{Main Results}
3	\label{sec:results}
4	
5	Vision token pruning in Vision Transformers (ViTs) is widely regarded as a reliable efficiency technique.
6	DynamicViT~\cite{rao2021dynamicvit} removes 30\%--50\% of tokens with less than 0.5\% accuracy loss on ImageNet, and Token Merging (ToMe)~\cite{bolya2023tome} merges up to 40\% of tokens while retaining over 99\% of classification accuracy.
7	EViT~\cite{liang2022evit} similarly discards 50\% of inattentive tokens with negligible degradation.
8	These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\cite{hsu2025vlacache,wang2026vlaiap}.
9	Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\cite{liu2023libero}.
10	The result is unambiguous.
11	Every configuration produces 0\% SR, a complete collapse we term the \emph{cliff edge}.
12	
13	\begin{table}[t]
14	\centering
15	\caption{Ablation matrix across scoring functions, retention ratios, and pruning mechanisms. All six pruning conditions produce 0\% SR. The baseline runs the same checkpoint with pruning disabled (bypass mode). Wilson 95\% confidence intervals (CI) are computed over independent episodes.}
16	\label{tab:ablation_matrix}
17	\small
18	\begin{tabular}{@{}llccrrc@{}}
19	\toprule
20	Method & Scoring & $k$ & Mechanism & SR (\%) & Episodes & Wilson 95\% CI \\
21	\midrule
22	\textbf{Baseline} & \textbf{--} & \textbf{1.0} & \textbf{--} & \textbf{44.8} & \textbf{500} & \textbf{[40.5, 49.2]} \\
23	\midrule
24	ACIS & Learned & 0.5 & Zero-mask & 0.0 & 300+ & [0.0, 1.26] \\
25	ACIS & Learned & 0.7 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\
26	ACIS & Learned & 0.9 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\
27	Random & Random & 0.5 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\
28	ACIS & Learned & 0.5 & True removal & 0.0 & 
…[truncated 3944 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T13:44:17.178590+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-17T13:44:17.178757+00:00_

1	% analysis.tex -- Section 5: Analysis
2	% Experiment IDs (provenance):
3	%   Attention entropy analysis:     attention_entropy_analysis
4	%   Single-step action error:       offline_singlestep_action_error
5	%   Action divergence:              action_divergence_v2_clean
6	%   Importance margin (G1):         mvp_imm_v8b_twostage
7	%   Token importance (G3, Spearman): plan_009_token_importance
8	
9	\section{Analysis}
10	\label{sec:analysis}
11	
12	Section~\ref{sec:results} established that all pruning configurations produce 0\% SR.
13	This section investigates \emph{why} the cliff edge occurs.
14	We present three complementary lines of evidence: the LLM backbone attends to vision tokens near-uniformly (\S\ref{sec:uniform_attention}), pruning causes immediate single-step action failures rather than gradual error accumulation (\S\ref{sec:action_disruption}), and standard offline evaluation metrics fail to predict this catastrophic closed-loop collapse (\S\ref{sec:metric_disconnect}).
15	Section~\ref{sec:why_vit_works} synthesizes these findings into a unified mechanistic explanation.
16	
17	\subsection{Uniform Attention Distribution}
18	\label{sec:uniform_attention}
19	
20	Token pruning in ViT classifiers succeeds because attention concentrates on a small set of discriminative patches and leaves most tokens redundant.
21	DynamicViT~\cite{rao2021dynamicvit} and ToMe~\cite{bolya2023tome} exploit this concentration: tokens that receive low attention contribute little to the classification decision and can be safely removed.
22	We test whether VLA models exhibit the same attention pattern.
23	
24	We extract attention weights from the LLM backbone (Qwen2-0.5B~\cite{yang2024qwen2}) over all vision tokens across three LIBERO tasks.
25	The attention entropy ratio reaches 0.98 (observed entropy of 6.86 bits out of a maximum of 7.0 bits for a perfectly uniform distribution).
26	The two camera views receive comparable attention (53.8\% for cam1, 46.2\% for cam2), and this patter
…[truncated 10137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T13:44:17.178911+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper -maxdepth 2 -name \"main.tex\" -o -name \"*.tex\" -type f | head -30",
  "description": "Find all .tex files including main.tex in paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper -maxdepth 2 -name \"main.tex\" -o -name \"*.tex\" -type f | head -30",
    "description": "Find all .tex files including main.tex in paper directory"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-17T13:44:17.179039+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-17T13:44:17.179476+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/ 2>/dev/null | grep -E \"\\.tex|\\.md\"",
  "description": "List all .tex and .md files in paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/ 2>/dev/null | grep -E \"\\.tex|\\.md\"",
    "description": "List all .tex and .md files in paper directory"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T13:44:17.179740+00:00_

-rw-r--r-- 1 ubuntu ubuntu 11681 May 17 13:39 analysis.tex
-rw-r--r-- 1 ubuntu ubuntu  5733 May 17 13:19 experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-17T13:44:17.180006+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress -type f \\( -name \"main.tex\" -o -name \"introduction.tex\" -o -name \"method.tex\" -o -name \"*.tex\" \\) 2>/dev/null | head -40",
  "description": "Find all .tex files in the project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress -type f \\( -name \"main.tex\" -o -name \"introduction.tex\" -o -name \"method.tex\" -o -name \"*.tex\" \\) 2>/dev/null | head -40",
    "description": "Find all .tex files in the project"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-17T13:44:17.180176+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260516T075046/median/paper.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260516T075046/worst/paper.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260516T075046/best/paper.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-17T13:44:17.180316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260516T075046"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260516T075046"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-17T13:44:17.180446+00:00_

EISDIR: illegal operation on a directory, read '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260516T075046'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-17T13:44:17.180569+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/",
  "description": "List all files in sections directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/",
    "description": "List all files in sections directory"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-17T13:44:17.180693+00:00_

total 28
drwxr-xr-x 2 ubuntu ubuntu  4096 May 17 13:24 .
drwxr-xr-x 3 ubuntu ubuntu  4096 May 17 13:37 ..
-rw-r--r-- 1 ubuntu ubuntu 11682 May 17 13:24 analysis.tex
-rw-r--r-- 1 ubuntu ubuntu  6323 May 17 13:17 experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-17T13:44:17.180817+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "diff /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
  "description": "Compare experiments.tex files between sections and root paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "diff /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
    "description": "Compare experiments.tex files between sections and root paper directory"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-17T13:44:17.180943+00:00_

1,12c1
< % experiments.tex -- Section 4: Main Results
< % Experiment IDs (provenance):
< %   Baseline 44.8%:              eval_stage1_only
< %   ACIS k=0.5 zero-mask:       eval_stage1only_object_v2_fixed
< %   ACIS k=0.7 zero-mask:       eval_k07_zero_mask
< %   ACIS k=0.9 zero-mask:       eval_stage1only_k09
< %   Random k=0.5:               eval_random_prune_k05
< %   True removal k=0.5:         eval_true_removal_k05
< %   Merge k=0.5:                eval_merge_k05
< %   Spatial suite:              eval_spatial_prune_k05 (baseline 51.8%)
< %   Goal suite:                 eval_goal_prune_k05 (baseline 63%)
< 
---
> % experiments.tex — Section 4: Main Results
26c15
< \caption{Ablation matrix across scoring functions, retention ratios, and pruning mechanisms. All six pruning conditions produce 0\% SR. The baseline runs the same checkpoint with pruning disabled (bypass mode). Wilson 95\% confidence intervals (CI) are computed over independent episodes. Experiment IDs are listed for reproducibility.}
---
> \caption{Ablation matrix across scoring functions, retention ratios, and pruning mechanisms. All six pruning conditions produce 0\% SR. The baseline runs the same checkpoint with pruning disabled (bypass mode). Wilson 95\% confidence intervals (CI) are computed over independent episodes.}
85c74
< The phenomenon is not a failure of any particular pruning algorithm but a structural property of how VLA policies consume vision tokens during closed-loop control.
---
> The phenomenon is not a failure of any particular pruning algorithm but a structural property of how VLA policies consume vision tokens during closed-loop control.
\ No newline at end of file

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-17T13:44:17.181085+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "diff /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex",
  "description": "Compare analysis.tex files between sections and root paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "diff /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex",
    "description": "Compare analysis.tex files between sections and root paper directory"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-17T13:44:17.181252+00:00_

141c141
< Together, these findings indicate that token pruning as currently formulated is structurally incompatible with VLA closed-loop control, and that alternative efficiency strategies must preserve the complete vision token sequence.
---
> Together, these findings indicate that token pruning as currently formulated is structurally incompatible with VLA closed-loop control, and that alternative efficiency strategies must preserve the complete vision token sequence.
\ No newline at end of file

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-17T13:44:17.181397+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"44\\.8\\|51\\.8\\|63\\.0\\|0\\.0\\|0\\.41\\|93\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex | head -20",
  "description": "Extract all numeric values from experiments section"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"44\\.8\\|51\\.8\\|63\\.0\\|0\\.0\\|0\\.41\\|93\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex | head -20",
    "description": "Extract all numeric values from experiments section"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-17T13:44:17.181519+00:00_

3:%   Baseline 44.8%:              eval_stage1_only
10:%   Spatial suite:              eval_spatial_prune_k05 (baseline 51.8%)
33:\textbf{Baseline} & \textbf{--} & \textbf{1.0} & \textbf{--} & \textbf{44.8} & \textbf{500} & \textbf{[40.5, 49.2]} \\
35:ACIS & Learned & 0.5 & Zero-mask & 0.0 & 300+ & [0.0, 1.26] \\
36:ACIS & Learned & 0.7 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\
37:ACIS & Learned & 0.9 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\
38:Random & Random & 0.5 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\
39:ACIS & Learned & 0.5 & True removal & 0.0 & 500 & [0.0, 0.80] \\
40:ACIS & Learned & 0.5 & Merge & 0.0 & 500 & [0.0, 0.76] \\
47:The baseline achieves 44.8\% SR across 500 episodes using the identical model checkpoint with pruning disabled.
79:On LIBERO-Object (object manipulation), SR drops from 44.8\% to 0\%.
80:On LIBERO-Spatial (spatial reasoning), SR drops from 51.8\% to 0\%.
81:On LIBERO-Goal (goal-conditioned tasks), SR drops from 63.0\% to 0\%.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-17T13:44:17.181650+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"0\\.98\\|6\\.86\\|7\\.0\\|53\\.8\\|46\\.2\\|0\\.246\\|0\\.414\\|1\\.391\\|3\\.4\\|111\\.5\\|1\\.02\\|0\\.20\\|0\\.25\\|0\\.30\\|0\\.01\\|0\\.02\\|1\\.117\\|93\\|0\\.87\\|0\\.41\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex",
  "description": "Extract all numeric values from analysis section"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"0\\.98\\|6\\.86\\|7\\.0\\|53\\.8\\|46\\.2\\|0\\.246\\|0\\.414\\|1\\.391\\|3\\.4\\|111\\.5\\|1\\.02\\|0\\.20\\|0\\.25\\|0\\.30\\|0\\.01\\|0\\.02\\|1\\.117\\|93\\|0\\.87\\|0\\.41\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex",
    "description": "Extract all numeric values from analysis section"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-17T13:44:17.181775+00:00_

25:The attention entropy ratio reaches 0.98 (observed entropy of 6.86 bits out of a maximum of 7.0 bits for a perfectly uniform distribution).
26:The two camera views receive comparable attention (53.8\% for cam1, 46.2\% for cam2), and this pattern holds across all sampled tasks with entropy values between 6.844 and 6.846 bits.
27:The Gini coefficient of the attention distribution is 0.246, a value that confirms low inequality across tokens.
42:\caption{(a)~LLM attention over vision tokens in the VLA policy. The distribution is near-uniform (entropy ratio 0.98), with both camera views receiving comparable weight. (b)~Typical attention pattern in a ViT classifier (illustrative), where attention concentrates on a small set of discriminative patches. This concentration enables safe token pruning in classification but is absent in VLA action prediction.}
53:Under the baseline (bypass mode, no pruning), the single-step L2 distance between predicted and ground-truth actions is 0.414.
54:Under pruning at $k{=}0.5$, this distance increases to 1.391, a 3.4$\times$ degradation.
55:The per-step relative error is 111.5\%; the error exceeds the magnitude of the action itself.
56:The failure is most severe in the gripper dimension, where the error of 1.02 indicates complete inversion: the policy commands the gripper to open when it should close, or vice versa.
57:Position dimensions show errors of [0.20, 0.25, 0.30] and rotation dimensions show errors of [0.01, 0.02, 0.01].
62:Closed-loop trajectory analysis confirms this interpretation: the L2 divergence between pruned and baseline trajectories has a mean of 1.117, with onset at step~0.
81:The importance margin gain (G1) shows a 93$\times$ improvement over the baseline, which indicates that the Attention-weighted Cumulative Importance Score (ACIS) learns to produce well-separated importance rankings.
82:The action loss ratio (G3) of 0.87 confirms that, on the training data distribution, the model's action loss with pruning is on
…[truncated 1031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-17T13:44:17.181925+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"Fig\\|Table\\|fig_\\|tab_\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex | head -20",
  "description": "Extract figure and table references from experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"Fig\\|Table\\|fig_\\|tab_\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex | head -20",
    "description": "Extract figure and table references from experiments"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-17T13:44:17.182043+00:00_

45:Table~\ref{tab:ablation_matrix} presents the full ablation matrix.
52:It does not: random pruning at $k{=}0.5$ also yields 0\% SR over 500 episodes (Table~\ref{tab:ablation_matrix}, row~5).
58:Yet $k{=}0.9$ also produces 0\% SR (Table~\ref{tab:ablation_matrix}, row~3).
67:All three mechanisms yield 0\% SR (Table~\ref{tab:ablation_matrix}, rows~2, 6, 7).
72:\includegraphics[width=\linewidth]{figures/paper/fig_cliff_edge.pdf}
83:Figure~\ref{fig:cliff_edge} visualizes this collapse pattern.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-17T13:44:17.182188+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"Fig\\|Table\\|fig_\\|tab_\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex",
  "description": "Extract figure and table references from analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"Fig\\|Table\\|fig_\\|tab_\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex",
    "description": "Extract figure and table references from analysis"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-17T13:44:17.182309+00:00_

28:Figure~\ref{fig:attention_heatmap} visualizes this contrast.
41:\includegraphics[width=\linewidth]{figures/paper/fig_attention_heatmap.pdf}
64:Figure~\ref{fig:action_divergence} shows the divergence curves.
71:\includegraphics[width=\linewidth]{figures/paper/fig_action_divergence.pdf}
105:Yet when pruning is actually applied, single-step action error is catastrophic: L2 of 1.391, relative error of 111.5\%, and complete gripper inversion (Table~\ref{tab:offline_vs_closedloop}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-17T13:44:17.182432+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"cliff edge\\|collapse\\|0% SR\\|binary\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex",
  "description": "Check key cliff edge claims in experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"cliff edge\\|collapse\\|0% SR\\|binary\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex",
    "description": "Check key cliff edge claims in experiments"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-17T13:44:17.182547+00:00_

22:Every configuration produces 0\% SR, a complete collapse we term the \emph{cliff edge}.
48:All six pruning conditions collapse to 0\% SR.
53:The cliff edge is therefore not a scoring quality problem.
54:No matter which tokens are selected for removal, the policy collapses.
60:The transition from functional to non-functional is binary, not gradual.
68:The collapse is therefore not caused by OOD activations from a particular masking strategy; it is a property of any alteration to the vision token sequence.
73:\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\% accuracy on classification benchmarks even at aggressive retention ratios~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}
78:To verify that the cliff edge is not an artifact of a single task distribution, we evaluate ACIS pruning at $k{=}0.5$ across three LIBERO suites with distinct characteristics.
82:The cliff edge is consistent across all three suites, and the absolute SR gap is largest for the suite where the baseline performs best (63 percentage points for Goal).
83:Figure~\ref{fig:cliff_edge} visualizes this collapse pattern.
84:These results establish that the cliff edge is method-agnostic: it persists regardless of which tokens are pruned, how aggressively they are pruned, and how the pruning is implemented.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-17T13:44:17.182682+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"cliff edge\\|collapse\\|binary\\|instantaneous\\|uniform\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex",
  "description": "Check key cliff edge claims in analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"cliff edge\\|collapse\\|binary\\|instantaneous\\|uniform\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex",
    "description": "Check key cliff edge claims in analysis"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-17T13:44:17.182804+00:00_

13:This section investigates \emph{why} the cliff edge occurs.
14:We present three complementary lines of evidence: the LLM backbone attends to vision tokens near-uniformly (\S\ref{sec:uniform_attention}), pruning causes immediate single-step action failures rather than gradual error accumulation (\S\ref{sec:action_disruption}), and standard offline evaluation metrics fail to predict this catastrophic closed-loop collapse (\S\ref{sec:metric_disconnect}).
18:\label{sec:uniform_attention}
25:The attention entropy ratio reaches 0.98 (observed entropy of 6.86 bits out of a maximum of 7.0 bits for a perfectly uniform distribution).
36:The practical consequence is clear: when attention is uniform, no subset of tokens is dispensable.
42:\caption{(a)~LLM attention over vision tokens in the VLA policy. The distribution is near-uniform (entropy ratio 0.98), with both camera views receiving comparable weight. (b)~Typical attention pattern in a ViT classifier (illustrative), where attention concentrates on a small set of discriminative patches. This concentration enables safe token pruning in classification but is absent in VLA action prediction.}
49:A natural hypothesis for the cliff edge is that small per-step errors compound over a long trajectory and eventually cause task failure.
67:The cliff edge does not require temporal accumulation; it is instantaneous.
72:\caption{Trajectory divergence between pruned and baseline policies. The L2 distance is large from step~0 and remains elevated throughout the episode. The failure is instantaneous rather than the result of gradual error accumulation.}
120:The three preceding analyses converge on a unified mechanistic explanation for the cliff edge.
128:The attention distribution is near-uniform (\S\ref{sec:uniform_attention}), a direct consequence of the fact that precise continuous action prediction requires the complete spatial layout of the scene.
132:The consequence of this architectural difference is that the failure mode shifts
…[truncated 238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-17T13:44:17.182945+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"Section\\|sec:results\\|sec:analysis\\|sec:uniform\\|sec:action\\|sec:metric\\|sec:why\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex | head -20",
  "description": "Check section references in analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"Section\\|sec:results\\|sec:analysis\\|sec:uniform\\|sec:action\\|sec:metric\\|sec:why\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex | head -20",
    "description": "Check section references in analysis"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-17T13:44:17.183063+00:00_

1:% analysis.tex -- Section 5: Analysis
10:\label{sec:analysis}
12:Section~\ref{sec:results} established that all pruning configurations produce 0\% SR.
14:We present three complementary lines of evidence: the LLM backbone attends to vision tokens near-uniformly (\S\ref{sec:uniform_attention}), pruning causes immediate single-step action failures rather than gradual error accumulation (\S\ref{sec:action_disruption}), and standard offline evaluation metrics fail to predict this catastrophic closed-loop collapse (\S\ref{sec:metric_disconnect}).
15:Section~\ref{sec:why_vit_works} synthesizes these findings into a unified mechanistic explanation.
18:\label{sec:uniform_attention}
47:\label{sec:action_disruption}
77:\label{sec:metric_disconnect}
118:\label{sec:why_vit_works}
128:The attention distribution is near-uniform (\S\ref{sec:uniform_attention}), a direct consequence of the fact that precise continuous action prediction requires the complete spatial layout of the scene.
138:Uniform attention (\S\ref{sec:uniform_attention}) means no tokens are safely dispensable.
139:Instantaneous action disruption (\S\ref{sec:action_disruption}) means that the spatial information loss manifests as immediate qualitative failures, not subtle distributional shifts.
140:The offline metric disconnect (\S\ref{sec:metric_disconnect}) arises because ranking-based metrics evaluate relative importance ordering but cannot detect that all tokens exceed the criticality threshold for the downstream task.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-17T13:44:17.183229+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 10 \"Experiment IDs\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex | head -15",
  "description": "Check experiment IDs in experiments section"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 10 \"Experiment IDs\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex | head -15",
    "description": "Check experiment IDs in experiments section"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-17T13:44:17.183352+00:00_

% Experiment IDs (provenance):
%   Baseline 44.8%:              eval_stage1_only
%   ACIS k=0.5 zero-mask:       eval_stage1only_object_v2_fixed
%   ACIS k=0.7 zero-mask:       eval_k07_zero_mask
%   ACIS k=0.9 zero-mask:       eval_stage1only_k09
%   Random k=0.5:               eval_random_prune_k05
%   True removal k=0.5:         eval_true_removal_k05
%   Merge k=0.5:                eval_merge_k05
%   Spatial suite:              eval_spatial_prune_k05 (baseline 51.8%)
%   Goal suite:                 eval_goal_prune_k05 (baseline 63%)

--
\caption{Ablation matrix across scoring functions, retention ratios, and pruning mechanisms. All six pruning conditions produce 0\% SR. The baseline runs the same checkpoint with pruning disabled (bypass mode). Wilson 95\% confidence intervals (CI) are computed over independent episodes. Experiment IDs are listed for reproducibility.}
\label{tab:ablation_matrix}
\small

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-17T13:44:17.183479+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 10 \"Experiment IDs\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex",
  "description": "Check experiment IDs in analysis section"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 10 \"Experiment IDs\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex",
    "description": "Check experiment IDs in analysis section"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-17T13:44:17.183592+00:00_

% Experiment IDs (provenance):
%   Attention entropy analysis:     attention_entropy_analysis
%   Single-step action error:       offline_singlestep_action_error
%   Action divergence:              action_divergence_v2_clean
%   Importance margin (G1):         mvp_imm_v8b_twostage
%   Token importance (G3, Spearman): plan_009_token_importance

\section{Analysis}
\label{sec:analysis}

Section~\ref{sec:results} established that all pruning configurations produce 0\% SR.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-17T13:44:17.183733+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat > /tmp/consistency_check.txt << 'EOF'\n=== EXPERIMENTS SECTION ANALYSIS ===\n\nKEY NUMERICAL CLAIMS (Experiments Section):\n1. Baseline SR: 44.8% (500 episodes)\n2. All 6 pruning conditions: 0.0% SR\n3. Cross-suite baselines:\n   - LIBERO-Object: 44.8% → 0%\n   - LIBERO-Spatial: 51.8% → 0%\n   - LIBERO-Goal: 63.0% → 0%\n4. Goal suite gap: 63 percentage points\n5. Confidence intervals for baseline: [40.5, 49.2]\n\n=== ANALYSIS SECTION CLAIMS ===\n\nKEY NUMERICAL CLAIMS (Analysis Section):\n1. Attention entropy ratio: 0.98 (6.86 bits / 7.0 bits max)\n2. Camera attention: 53.8% (cam1) and 46.2% (cam2)\n3. Gini coefficient: 0.246\n4. Single-step L2 distance:\n   - Baseline: 0.414\n   - Under pruning (k=0.5): 1.391\n   - Degradation: 3.4x\n5. Per-step relative error: 111.5%\n6. Gripper error: 1.02 (complete inversion)\n7. Position errors: [0.20, 0.25, 0.30]\n8. Rotation errors: [0.01, 0.02, 0.01]\n9. Trajectory L2 divergence mean: 1.117\n10. Offline metrics:\n    - Importance margin gain (G1): 93x\n    - Action loss ratio (G3): 0.87 (87%)\n    - ACIS-gradient Spearman: 0.41\n\n=== NARRATIVE CONSISTENCY CHECK ===\n\nExperiments provides:\n- What happens: All 6 pruning configurations produce 0% SR\n- Evidence: Ablation matrix across 3 axes (scoring, ratio, mechanism)\n- Scope: Verified across 3 LIBERO suites\n- Main finding: \"cliff edge\" - binary collapse, not gradual degradation\n\nAnalysis explains WHY:\n- Section 5.1: Why no tokens are safe to remove (uniform attention)\n- Section 5.2: Why failure is instantaneous, not gradual accumulation\n- Section 5.3: Why offline metrics fail to predict closed-loop collapse\n- Section 5.4: Unified mechanistic explanation\n\nCross-references verify proper linking:\n- Analysis refers back to Section 4 results (sec:results reference)\n- Analysis organizes 3 evidence lines that explain the 0% SR collapse\n- All subsections properly labeled and cross-referenced\n\n=== PROVENANCE TRACKING ===\n\nExperiments section IDs:\n- eval_stage1_only (baseline)\n- eval_stage1only_object_v2_fixed (ACIS k=0.5)\n- eval_k07_zero_mask (ACIS k=0.7)\n- eval_stage1only_k09 (ACIS k=0.9)\n- eval_random_prune_k05 (Random k=0.5)\n- eval_true_removal_k05 (True removal)\n- eval_merge_k05 (Merge)\n- eval_spatial_prune_k05 (Spatial suite baseline)\n- eval_goal_prune_k05 (Goal suite baseline)\n\nAnalysis section IDs:\n- attention_entropy_analysis\n- offline_singlestep_action_error\n- action_divergence_v2_clean\n- mvp_imm_v8b_twostage\n- plan_009_token_importance\nEOF\ncat /tmp/consistency_check.txt\n",
  "description": "Create comprehensive consistency analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "cat > /tmp/consistency_check.txt << 'EOF'\n=== EXPERIMENTS SECTION ANALYSIS ===\n\nKEY NUMERICAL CLAIMS (Experiments Section):\n1. Baseline SR: 44.8% (500 episodes)\n2. All 6 pruning conditions: 0.0% SR\n3. Cross-suite baselines:\n   - LIBERO-Object: 44.8% → 0%\n   - LIBERO-Spatial: 51.8% → 0%\n   - LIBERO-Goal: 63.0% → 0%\n4. Goal suite gap: 63 percentage points\n5. Confidence intervals for baseline: [40.5, 49.2]\n\n=== ANALYSIS SECTION CLAIMS ===\n\nKEY NUMERICAL CLAIMS (Analysis Section):\n1. Attention entropy ratio: 0.98 (6.86 bits / 7.0 bits max)\n2. Camera attention: 53.8% (cam1) and 46.2% (cam2)\n3. Gini coefficient: 0.246\n4. Single-step L2 distance:\n   - Baseline: 0.414\n   - Under pruning (k=0.5): 1.391\n   - Degradation: 3.4x\n5. Per-step relative error: 111.5%\n6. Gripper error: 1.02 (complete inversion)\n7. Position errors: [0.20, 0.25, 0.30]\n8. Rotation errors: [0.01, 0.02, 0.01]\n9. Trajectory L2 divergence mean: 1.117\n10. Offline metrics:\n    - Importance margin gain (G1): 93x\n    - Action loss ratio (G3): 0.87 (87%)\n    - ACIS-gradient Spearman: 0.41\n\n=== NARRATIVE CONSISTENCY CHECK ===\n\nExperiments provides:\n- What happens: All 6 pruning configurations produce 0% SR\n- Evidence: Ablation matrix across 3 axes (scoring, ratio, mechanism)\n- Scope: Verified across 3 LIBERO suites\n- Main finding: \"cliff edge\" - binary collapse, not gradual degradation\n\nAnalysis explains WHY:\n- Section 5.1: Why no tokens are safe to remove (uniform attention)\n- Section 5.2: Why failure is instantaneous, not gradual accumulation\n- Section 5.3: Why offline metrics fail to predict closed-loop collapse\n- Section 5.4: Unified mechanistic explanation\n\nCross-references verify proper linking:\n- Analysis refers back to Section 4 results (sec:results reference)\n- Analysis organizes 3 evidence lines that explain the 0% SR collapse\n- All subsections properly labeled and cross-referenced\n\n=== PROVENANCE TRACKING ===\n\nExperiments section IDs:\n- eval_stage1_only (baseline)\n- eval_stage1only_object_v2_fixed (ACIS k=0.5)\n- eval_k07_zero_mask (ACIS k=0.7)\n- eval_stage1only_k09 (ACIS k=0.9)\n- eval_random_prune_k05 (Random k=0.5)\n- eval_true_removal_k05 (True removal)\n- eval_merge_k05 (Merge)\n- eval_spatial_prune_k05 (Spatial suite baseline)\n- eval_goal_prune_k05 (Goal suite baseline)\n\nAnalysis section IDs:\n- attention_entropy_analysis\n- offline_singlestep_action_error\n- action_divergence_v2_clean\n- mvp_imm_v8b_twostage\n- plan_009_token_importance\nEOF\ncat /tmp/consistency_check.txt\n",
    "description": "Create comprehensive consistency analysis"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-17T13:44:17.183888+00:00_

=== EXPERIMENTS SECTION ANALYSIS ===

KEY NUMERICAL CLAIMS (Experiments Section):
1. Baseline SR: 44.8% (500 episodes)
2. All 6 pruning conditions: 0.0% SR
3. Cross-suite baselines:
   - LIBERO-Object: 44.8% → 0%
   - LIBERO-Spatial: 51.8% → 0%
   - LIBERO-Goal: 63.0% → 0%
4. Goal suite gap: 63 percentage points
5. Confidence intervals for baseline: [40.5, 49.2]

=== ANALYSIS SECTION CLAIMS ===

KEY NUMERICAL CLAIMS (Analysis Section):
1. Attention entropy ratio: 0.98 (6.86 bits / 7.0 bits max)
2. Camera attention: 53.8% (cam1) and 46.2% (cam2)
3. Gini coefficient: 0.246
4. Single-step L2 distance:
   - Baseline: 0.414
   - Under pruning (k=0.5): 1.391
   - Degradation: 3.4x
5. Per-step relative error: 111.5%
6. Gripper error: 1.02 (complete inversion)
7. Position errors: [0.20, 0.25, 0.30]
8. Rotation errors: [0.01, 0.02, 0.01]
9. Trajectory L2 divergence mean: 1.117
10. Offline metrics:
    - Importance margin gain (G1): 93x
    - Action loss ratio (G3): 0.87 (87%)
    - ACIS-gradient Spearman: 0.41

=== NARRATIVE CONSISTENCY CHECK ===

Experiments provides:
- What happens: All 6 pruning configurations produce 0% SR
- Evidence: Ablation matrix across 3 axes (scoring, ratio, mechanism)
- Scope: Verified across 3 LIBERO suites
- Main finding: "cliff edge" - binary collapse, not gradual degradation

Analysis explains WHY:
- Section 5.1: Why no tokens are safe to remove (uniform attention)
- Section 5.2: Why failure is instantaneous, not gradual accumulation
- Section 5.3: Why offline metrics fail to predict closed-loop collapse
- Section 5.4: Unified mechanistic explanation

Cross-references verify proper linking:
- Analysis refers back to Section 4 results (sec:results reference)
- Analysis organizes 3 evidence lines that explain the 0% SR collapse
- All subsections properly labeled and cross-referenced

=== PROVENANCE TRACKING ===

Experiments section IDs:
- eval_stage1_only (baseline)
- eval_stage1only_object_v2_fixed (ACIS k=0.5)
- eval_k07_zero_mask (ACIS k=0.7)
…[truncated 398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-17T13:44:17.184086+00:00_

Perfect. Now let me provide the final report:

## Consistency Analysis Report: Experiments & Analysis Sections

**Status:** CONSISTENT. Both sections maintain strong narrative and numerical coherence.

### Narrative Flow (Section 4 → Section 5)

The two sections form a clean logical progression:
- **Section 4 (Results)**: Establishes the empirical phenomenon — all six pruning configurations collapse to 0% success rate (SR), forming a binary "cliff edge" rather than gradual degradation
- **Section 5 (Analysis)**: Explains the mechanism behind this collapse through three complementary evidence lines

The Analysis section explicitly acknowledges this dependency at its opening: "Section~\ref{sec:results} established that all pruning configurations produce 0\% SR."

### Numerical Consistency Verification

**Experiments baseline values:**
- 44.8% SR (LIBERO-Object, 500 episodes)
- 51.8% SR (LIBERO-Spatial baseline)
- 63.0% SR (LIBERO-Goal baseline)
- All pruning configurations: 0.0% SR

**Analysis uses these same values consistently:**
- References 44.8% → 0% collapse for Object suite ✓
- References 51.8% → 0% collapse for Spatial suite ✓
- References 63.0% → 0% collapse for Goal suite ✓
- References the 63 percentage point gap for Goal suite ✓

**Action error metrics (Analysis Section 5.2):**
All values properly reported: single-step L2 (0.414 → 1.391), relative error (111.5%), gripper inversion (1.02), position errors [0.20, 0.25, 0.30], rotation errors [0.01, 0.02, 0.01], trajectory divergence (1.117).

**Offline metrics (Analysis Section 5.3):**
G1 importance margin (93×), G3 action loss ratio (0.87), ACIS-gradient Spearman (0.41) — all reported consistently in both main text and Table 1.

### Section Structure Coherence

**Three pillars of explanation properly sequenced:**

1. **Uniform Attention Distribution** (5.1): 
   - Entropy ratio 0.98 (near-uniform)
   - Camera split 53.8% / 46.2%
   - Gini coefficient 0.246
   - Explains why *no tokens are dispensable*

2. *
…[truncated 2448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Agent",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-17T13:44:17.184291+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/ 2>/dev/null || echo \"DIR NOT FOUND\"",
  "description": "Check sections directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/ 2>/dev/null || echo \"DIR NOT FOUND\"",
    "description": "Check sections directory"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-17T13:44:17.184419+00:00_

total 28
drwxr-xr-x 2 ubuntu ubuntu  4096 May 17 13:24 .
drwxr-xr-x 3 ubuntu ubuntu  4096 May 17 13:37 ..
-rw-r--r-- 1 ubuntu ubuntu 11682 May 17 13:24 analysis.tex
-rw-r--r-- 1 ubuntu ubuntu  6323 May 17 13:17 experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-17T13:44:17.184536+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-17T13:44:17.184655+00:00_

docs/paper/sections/experiments.tex
docs/paper/experiments.tex
docs/paper/sections/analysis.tex
docs/paper/analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-17T13:44:17.184768+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-17T13:44:17.184920+00:00_

1	% experiments.tex -- Section 4: Main Results
2	% Experiment IDs (provenance):
3	%   Baseline 44.8%:              eval_stage1_only
4	%   ACIS k=0.5 zero-mask:       eval_stage1only_object_v2_fixed
5	%   ACIS k=0.7 zero-mask:       eval_k07_zero_mask
6	%   ACIS k=0.9 zero-mask:       eval_stage1only_k09
7	%   Random k=0.5:               eval_random_prune_k05
8	%   True removal k=0.5:         eval_true_removal_k05
9	%   Merge k=0.5:                eval_merge_k05
10	%   Spatial suite:              eval_spatial_prune_k05 (baseline 51.8%)
11	%   Goal suite:                 eval_goal_prune_k05 (baseline 63%)
12	
13	\section{Main Results}
14	\label{sec:results}
15	
16	Vision token pruning in Vision Transformers (ViTs) is widely regarded as a reliable efficiency technique.
17	DynamicViT~\cite{rao2021dynamicvit} removes 30\%--50\% of tokens with less than 0.5\% accuracy loss on ImageNet, and Token Merging (ToMe)~\cite{bolya2023tome} merges up to 40\% of tokens while retaining over 99\% of classification accuracy.
18	EViT~\cite{liang2022evit} similarly discards 50\% of inattentive tokens with negligible degradation.
19	These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\cite{hsu2025vlacache,wang2026vlaiap}.
20	Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\cite{liu2023libero}.
21	The result is unambiguous.
22	Every configuration produces 0\% SR, a complete collapse we term the \emph{cliff edge}.
23	
24	\begin{table}[t]
25	\centering
26	\caption{Ablation matrix across scoring functions, retention ratios, and pruning mechanisms. All six pruning conditions produce 0\% SR. The baseline runs the same checkpoint with pruning disabled (bypass mode). Wilson 95\% confidence intervals (CI) are computed over independent episodes. Experiment IDs are listed for reproducibility
…[truncated 3903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-17T13:44:17.185059+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-17T13:44:17.185259+00:00_

1	% analysis.tex -- Section 5: Analysis
2	% Experiment IDs (provenance):
3	%   Attention entropy analysis:     attention_entropy_analysis
4	%   Single-step action error:       offline_singlestep_action_error
5	%   Action divergence:              action_divergence_v2_clean
6	%   Importance margin (G1):         mvp_imm_v8b_twostage
7	%   Token importance (G3, Spearman): plan_009_token_importance
8	
9	\section{Analysis}
10	\label{sec:analysis}
11	
12	Section~\ref{sec:results} established that all pruning configurations produce 0\% SR.
13	This section investigates \emph{why} the cliff edge occurs.
14	We present three complementary lines of evidence: the LLM backbone attends to vision tokens near-uniformly (\S\ref{sec:uniform_attention}), pruning causes immediate single-step action failures rather than gradual error accumulation (\S\ref{sec:action_disruption}), and standard offline evaluation metrics fail to predict this catastrophic closed-loop collapse (\S\ref{sec:metric_disconnect}).
15	Section~\ref{sec:why_vit_works} synthesizes these findings into a unified mechanistic explanation.
16	
17	\subsection{Uniform Attention Distribution}
18	\label{sec:uniform_attention}
19	
20	Token pruning in ViT classifiers succeeds because attention concentrates on a small set of discriminative patches and leaves most tokens redundant.
21	DynamicViT~\cite{rao2021dynamicvit} and ToMe~\cite{bolya2023tome} exploit this concentration: tokens that receive low attention contribute little to the classification decision and can be safely removed.
22	We test whether VLA models exhibit the same attention pattern.
23	
24	We extract attention weights from the LLM backbone (Qwen2-0.5B~\cite{yang2024qwen2}) over all vision tokens across three LIBERO tasks.
25	The attention entropy ratio reaches 0.98 (observed entropy of 6.86 bits out of a maximum of 7.0 bits for a perfectly uniform distribution).
26	The two camera views receive comparable attention (53.8\% for cam1, 46.2\% for cam2), and this patter
…[truncated 4333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-17T13:44:17.185428+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex",
  "offset": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/analysis.tex",
    "offset": "80"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-17T13:44:17.185583+00:00_

80	Our offline metrics provide consistently positive signals.
81	The importance margin gain (G1) shows a 93$\times$ improvement over the baseline, which indicates that the Attention-weighted Cumulative Importance Score (ACIS) learns to produce well-separated importance rankings.
82	The action loss ratio (G3) of 0.87 confirms that, on the training data distribution, the model's action loss with pruning is only 87\% of the full-token loss.
83	The Spearman correlation between ACIS scores and gradient magnitudes is 0.41, a moderate agreement between the learned importance scores and the gradient-based ground truth.
84	
85	\begin{table}[t]
86	\centering
87	\caption{Offline evaluation metrics versus closed-loop performance. Offline ranking and loss metrics show positive signals, yet all pruning conditions produce 0\% closed-loop SR. The disconnect demonstrates that standard offline proxies are insufficient for validating VLA token compression.}
88	\label{tab:offline_vs_closedloop}
89	\small
90	\begin{tabular}{@{}lccr@{}}
91	\toprule
92	Metric & Result & Interpretation & SR (\%) \\
93	\midrule
94	Importance margin (G1) & 93$\times$ & Meaningful ranking & -- \\
95	Action loss ratio (G3) & 0.87 & Pruned $<$ full on train data & -- \\
96	ACIS-gradient Spearman & 0.41 & Moderate correlation & -- \\
97	\midrule
98	Single-step L2 (pruned) & 1.391 & 3.4$\times$ degradation & 0.0 \\
99	Relative action error & 111.5\% & Error $>$ action magnitude & 0.0 \\
100	Gripper error & 1.02 & Complete inversion & 0.0 \\
101	\bottomrule
102	\end{tabular}
103	\end{table}
104	
105	Yet when pruning is actually applied, single-step action error is catastrophic: L2 of 1.391, relative error of 111.5\%, and complete gripper inversion (Table~\ref{tab:offline_vs_closedloop}).
106	The disconnect has a specific cause.
107	Ranking metrics (G1, Spearman) evaluate the quality of the importance ordering, not the effect of removing the lowest-ranked tokens.
108	A scorer can produce a perfect ranking yet still
…[truncated 3870 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-17T13:44:17.185773+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex",
  "content": "% background.tex -- Section 2: Background\n\n\\section{Background}\n\\label{sec:background}\n\nThis section describes the two components of our experimental setup: the SmolVLA architecture~\\cite{shukor2025smolvla}, in which we study vision token reduction, and the LIBERO benchmark~\\cite{liu2023libero}, on which we evaluate closed-loop performance.\n\n\\subsection{SmolVLA Architecture}\n\\label{sec:smolvla_arch}\n\nVision-Language-Action (VLA) models cast robotic control as conditional generation: given a camera observation and a language instruction, the model predicts a continuous action.\nSmolVLA~\\cite{shukor2025smolvla} instantiates this paradigm with approximately 451.5M parameters, organized into a vision encoder, a modality connector, a language model backbone, and an action head.\nFigure~\\ref{fig:architecture} illustrates the full architecture and token flow.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_architecture.pdf}\n\\caption{SmolVLA architecture and token flow. Each camera image is encoded by SigLIP into 128 spatial patch tokens. An MLP connector projects these tokens into the LLM embedding space. The Qwen2-0.5B backbone processes the concatenated vision and language tokens, and a flow matching head generates continuous 7-DoF actions.}\n\\label{fig:architecture}\n\\end{figure}\n\n\\paragraph{Vision encoder.}\nSmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\\cite{zhai2023siglip} to process visual input.\nSigLIP divides each camera image into non-overlapping spatial patches and encodes them independently, producing 128 tokens per image.\nTwo properties of this encoding are relevant to our analysis.\nFirst, SigLIP does not include a \\texttt{[CLS]} aggregation token; there is no single summary representation that pools information across patches.\nSecond, because patches are non-overlapping, each token encodes a unique spatial region of the input image, and no two tokens carry redundant information.\nThese design choices mean that the 128-token output is a spatially complete, non-redundant representation of the scene.\n\n\\paragraph{Dual-camera input.}\nSmolVLA receives images from two cameras: a wrist-mounted camera (cam1) and an overhead camera (cam2).\nEach camera image produces 128 vision tokens through the SigLIP encoder, yielding 256 vision tokens total that enter the language model.\nThe two viewpoints are complementary: the wrist camera captures fine-grained end-effector interactions, while the overhead camera provides a global spatial layout of objects on the workspace.\n\n\\paragraph{MLP connector.}\nA multi-layer perceptron (MLP) projects each SigLIP output token from the vision encoder embedding space into the Qwen2-0.5B embedding space.\nThis connector applies a learned linear transformation per token without cross-token interaction, preserving the one-to-one correspondence between spatial patches and tokens.\nThe intervention point for token reduction in our experiments sits immediately after this connector: pruning, masking, or merging operations are applied to the projected vision tokens before they enter the language model.\n\n\\paragraph{LLM backbone.}\nThe Qwen2-0.5B language model~\\cite{yang2024qwen2} serves as the central reasoning module.\nIt receives a concatenated input sequence of 256 projected vision tokens and the tokenized language instruction.\nSelf-attention across this full sequence allows the model to ground language in visual context and to integrate information across both camera views.\nThe backbone must reconcile spatial relationships between the robot gripper, target objects, and obstacles using only the vision tokens, since no other spatial input is provided.\n\n\\paragraph{Flow matching action head.}\nSmolVLA generates actions through conditional flow matching~\\cite{lipman2023flow} rather than autoregressive token prediction.\nThe action head maps the LLM's output representation to a continuous 7-DoF action vector: three position coordinates, three rotation angles, and one gripper open/close value.\nFlow matching learns a vector field that transports a noise distribution to the target action distribution, conditioned on the LLM output.\nThis formulation produces smooth, continuous actions suited to precise manipulation, but it also means that the action output depends holistically on the LLM's internal representation.\nAny corruption of the vision token input propagates through the full LLM computation into the predicted action.\n\nThe overall inference pipeline proceeds as: image $\\rightarrow$ SigLIP patches $\\rightarrow$ 128 tokens per camera $\\rightarrow$ MLP projection $\\rightarrow$ concatenation with language tokens $\\rightarrow$ Qwen2-0.5B forward pass $\\rightarrow$ flow matching action prediction.\nThis architecture shares its high-level structure with larger VLA systems such as OpenVLA~\\cite{kim2024openvla} and $\\pi_0$~\\cite{black2024pi0}, making SmolVLA a representative testbed for studying vision token efficiency in VLA policies.\n\n\\subsection{LIBERO Benchmark}\n\\label{sec:libero_bench}\n\nWe evaluate on the LIBERO benchmark~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks in simulation.\nLIBERO provides standardized task definitions, initial state distributions, and evaluation protocols for reproducible comparison of manipulation policies.\nWe use three of its four suites, each testing a distinct aspect of policy competence.\nLIBERO-Object presents ten tasks focused on object manipulation, requiring the policy to identify and interact with specific objects from visually similar alternatives.\nLIBERO-Spatial presents ten tasks focused on spatial reasoning, requiring correct placement or navigation relative to reference locations.\nLIBERO-Goal presents ten tasks with varied goal conditions applied to a shared environment layout, testing the policy's ability to condition behavior on the language instruction.\n\nEach suite contains 10 tasks, and we run 50 evaluation episodes per task, yielding 500 episodes per suite per experimental condition.\nThe evaluation metric is closed-loop Success Rate (SR): a binary indicator per episode that equals 1 only if the robot completes the full task within the time limit.\nSR is measured through closed-loop execution, where the policy observes the current state, predicts an action, the simulator advances, and the policy re-observes the updated state at every timestep.\nThis closed-loop evaluation is critical because errors at any single step can cascade through subsequent observations and actions.\nA policy that produces even one qualitatively wrong action (for example, opening the gripper when it should close) will likely fail the entire episode.\n\nThe three LIBERO suites span a range of baseline difficulty levels: SmolVLA achieves 44.8\\% SR on Object, 51.8\\% on Spatial, and 63.0\\% on Goal in bypass mode (full vision tokens, no pruning).\nThese baseline numbers are not state-of-the-art; SmolVLA is a compact model designed for efficiency research.\nThe relevant comparison is not the absolute success rate but the change under token reduction: any viable pruning strategy must approximately preserve these baselines rather than collapse to 0\\%.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex",
    "content": "% background.tex -- Section 2: Background\n\n\\section{Background}\n\\label{sec:background}\n\nThis section describes the two components of our experimental setup: the SmolVLA architecture~\\cite{shukor2025smolvla}, in which we study vision token reduction, and the LIBERO benchmark~\\cite{liu2023libero}, on which we evaluate closed-loop performance.\n\n\\subsection{SmolVLA Architecture}\n\\label{sec:smolvla_arch}\n\nVision-Language-Action (VLA) models cast robotic control as conditional generation: given a camera observation and a language instruction, the model predicts a continuous action.\nSmolVLA~\\cite{shukor2025smolvla} instantiates this paradigm with approximately 451.5M parameters, organized into a vision encoder, a modality connector, a language model backbone, and an action head.\nFigure~\\ref{fig:architecture} illustrates the full architecture and token flow.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_architecture.pdf}\n\\caption{SmolVLA architecture and token flow. Each camera image is encoded by SigLIP into 128 spatial patch tokens. An MLP connector projects these tokens into the LLM embedding space. The Qwen2-0.5B backbone processes the concatenated vision and language tokens, and a flow matching head generates continuous 7-DoF actions.}\n\\label{fig:architecture}\n\\end{figure}\n\n\\paragraph{Vision encoder.}\nSmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\\cite{zhai2023siglip} to process visual input.\nSigLIP divides each camera image into non-overlapping spatial patches and encodes them independently, producing 128 tokens per image.\nTwo properties of this encoding are relevant to our analysis.\nFirst, SigLIP does not include a \\texttt{[CLS]} aggregation token; there is no single summary representation that pools information across patches.\nSecond, because patches are non-overlapping, each token encodes a unique spatial region of the input image, and no two tokens carry redundant information.\nThese design choices mean that the 128-token output is a spatially complete, non-redundant representation of the scene.\n\n\\paragraph{Dual-camera input.}\nSmolVLA receives images from two cameras: a wrist-mounted camera (cam1) and an overhead camera (cam2).\nEach camera image produces 128 vision tokens through the SigLIP encoder, yielding 256 vision tokens total that enter the language model.\nThe two viewpoints are complementary: the wrist camera captures fine-grained end-effector interactions, while the overhead camera provides a global spatial layout of objects on the workspace.\n\n\\paragraph{MLP connector.}\nA multi-layer perceptron (MLP) projects each SigLIP output token from the vision encoder embedding space into the Qwen2-0.5B embedding space.\nThis connector applies a learned linear transformation per token without cross-token interaction, preserving the one-to-one correspondence between spatial patches and tokens.\nThe intervention point for token reduction in our experiments sits immediately after this connector: pruning, masking, or merging operations are applied to the projected vision tokens before they enter the language model.\n\n\\paragraph{LLM backbone.}\nThe Qwen2-0.5B language model~\\cite{yang2024qwen2} serves as the central reasoning module.\nIt receives a concatenated input sequence of 256 projected vision tokens and the tokenized language instruction.\nSelf-attention across this full sequence allows the model to ground language in visual context and to integrate information across both camera views.\nThe backbone must reconcile spatial relationships between the robot gripper, target objects, and obstacles using only the vision tokens, since no other spatial input is provided.\n\n\\paragraph{Flow matching action head.}\nSmolVLA generates actions through conditional flow matching~\\cite{lipman2023flow} rather than autoregressive token prediction.\nThe action head maps the LLM's output representation to a continuous 7-DoF action vector: three position coordinates, three rotation angles, and one gripper open/close value.\nFlow matching learns a vector field that transports a noise distribution to the target action distribution, conditioned on the LLM output.\nThis formulation produces smooth, continuous actions suited to precise manipulation, but it also means that the action output depends holistically on the LLM's internal representation.\nAny corruption of the vision token input propagates through the full LLM computation into the predicted action.\n\nThe overall inference pipeline proceeds as: image $\\rightarrow$ SigLIP patches $\\rightarrow$ 128 tokens per camera $\\rightarrow$ MLP projection $\\rightarrow$ concatenation with language tokens $\\rightarrow$ Qwen2-0.5B forward pass $\\rightarrow$ flow matching action prediction.\nThis architecture shares its high-level structure with larger VLA systems such as OpenVLA~\\cite{kim2024openvla} and $\\pi_0$~\\cite{black2024pi0}, making SmolVLA a representative testbed for studying vision token efficiency in VLA policies.\n\n\\subsection{LIBERO Benchmark}\n\\label{sec:libero_bench}\n\nWe evaluate on the LIBERO benchmark~\\cite{liu2023libero}, a suite of language-conditioned tabletop manipulation tasks in simulation.\nLIBERO provides standardized task definitions, initial state distributions, and evaluation protocols for reproducible comparison of manipulation policies.\nWe use three of its four suites, each testing a distinct aspect of policy competence.\nLIBERO-Object presents ten tasks focused on object manipulation, requiring the policy to identify and interact with specific objects from visually similar alternatives.\nLIBERO-Spatial presents ten tasks focused on spatial reasoning, requiring correct placement or navigation relative to reference locations.\nLIBERO-Goal presents ten tasks with varied goal conditions applied to a shared environment layout, testing the policy's ability to condition behavior on the language instruction.\n\nEach suite contains 10 tasks, and we run 50 evaluation episodes per task, yielding 500 episodes per suite per experimental condition.\nThe evaluation metric is closed-loop Success Rate (SR): a binary indicator per episode that equals 1 only if the robot completes the full task within the time limit.\nSR is measured through closed-loop execution, where the policy observes the current state, predicts an action, the simulator advances, and the policy re-observes the updated state at every timestep.\nThis closed-loop evaluation is critical because errors at any single step can cascade through subsequent observations and actions.\nA policy that produces even one qualitatively wrong action (for example, opening the gripper when it should close) will likely fail the entire episode.\n\nThe three LIBERO suites span a range of baseline difficulty levels: SmolVLA achieves 44.8\\% SR on Object, 51.8\\% on Spatial, and 63.0\\% on Goal in bypass mode (full vision tokens, no pruning).\nThese baseline numbers are not state-of-the-art; SmolVLA is a compact model designed for efficiency research.\nThe relevant comparison is not the absolute success rate but the change under token reduction: any viable pruning strategy must approximately preserve these baselines rather than collapse to 0\\%.\n"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-17T13:44:17.185972+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-17T13:44:17.186119+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex\" && echo \"=== Em-dash check ===\" && grep -n \"—\" \"$FILE\" || echo \"PASS: no em-dashes\" && echo \"=== En-dash check ===\" && grep -n \" – \" \"$FILE\" || echo \"PASS: no explanatory en-dashes\" && echo \"=== -ing phrase endings ===\" && grep -n \"ing\\.\" \"$FILE\" | grep -v \"matching\\.\\|string\\.\" || echo \"checked\" && echo \"=== Furthermore/Moreover/Additionally ===\" && grep -ni \"furthermore\\|moreover\\|additionally\" \"$FILE\" || echo \"PASS: none found\" && echo \"=== Blacklisted words ===\" && grep -ni \"delve\\|leverage\\|utilize\\|facilitate\\|myriad\\|plethora\\|paradigm shift\\|in the realm of\" \"$FILE\" || echo \"PASS: none found\" && echo \"=== Word count ===\" && wc -w \"$FILE\"",
  "description": "Check for AI style violations and word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex\" && echo \"=== Em-dash check ===\" && grep -n \"—\" \"$FILE\" || echo \"PASS: no em-dashes\" && echo \"=== En-dash check ===\" && grep -n \" – \" \"$FILE\" || echo \"PASS: no explanatory en-dashes\" && echo \"=== -ing phrase endings ===\" && grep -n \"ing\\.\" \"$FILE\" | grep -v \"matching\\.\\|string\\.\" || echo \"checked\" && echo \"=== Furthermore/Moreover/Additionally ===\" && grep -ni \"furthermore\\|moreover\\|additionally\" \"$FILE\" || echo \"PASS: none found\" && echo \"=== Blacklisted words ===\" && grep -ni \"delve\\|leverage\\|utilize\\|facilitate\\|myriad\\|plethora\\|paradigm shift\\|in the realm of\" \"$FILE\" || echo \"PASS: none found\" && echo \"=== Word count ===\" && wc -w \"$FILE\"",
    "description": "Check for AI style violations and word count"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-17T13:44:17.186288+00:00_

=== Em-dash check ===
PASS: no em-dashes
=== En-dash check ===
PASS: no explanatory en-dashes
=== -ing phrase endings ===
checked
=== Furthermore/Moreover/Additionally ===
PASS: none found
=== Blacklisted words ===
PASS: none found
=== Word count ===
941 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-17T13:44:17.186413+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex\" && echo \"=== -ing, phrase check ===\" && grep -n \"ing,\" \"$FILE\" | head -20",
  "description": "Check for -ing comma patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex\" && echo \"=== -ing, phrase check ===\" && grep -n \"ing,\" \"$FILE\" | head -20",
    "description": "Check for -ing comma patterns"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-17T13:44:17.186533+00:00_

=== -ing, phrase check ===
27:Second, because patches are non-overlapping, each token encodes a unique spatial region of the input image, and no two tokens carry redundant information.
38:The intervention point for token reduction in our experiments sits immediately after this connector: pruning, masking, or merging operations are applied to the projected vision tokens before they enter the language model.
63:LIBERO-Spatial presents ten tasks focused on spatial reasoning, requiring correct placement or navigation relative to reference locations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-17T13:44:17.186663+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex",
  "old_string": "LIBERO-Spatial presents ten tasks focused on spatial reasoning, requiring correct placement or navigation relative to reference locations.",
  "new_string": "LIBERO-Spatial presents ten tasks focused on spatial reasoning, where the policy must place objects correctly or navigate relative to reference locations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex",
    "old_string": "LIBERO-Spatial presents ten tasks focused on spatial reasoning, requiring correct placement or navigation relative to reference locations.",
    "new_string": "LIBERO-Spatial presents ten tasks focused on spatial reasoning, where the policy must place objects correctly or navigate relative to reference locations."
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-17T13:44:17.186947+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-17T13:44:17.187356+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex",
  "offset": "60",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex",
    "offset": "60",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-17T13:44:17.188030+00:00_

60	LIBERO provides standardized task definitions, initial state distributions, and evaluation protocols for reproducible comparison of manipulation policies.
61	We use three of its four suites, each testing a distinct aspect of policy competence.
62	LIBERO-Object presents ten tasks focused on object manipulation, requiring the policy to identify and interact with specific objects from visually similar alternatives.
63	LIBERO-Spatial presents ten tasks focused on spatial reasoning, where the policy must place objects correctly or navigate relative to reference locations.
64	LIBERO-Goal presents ten tasks with varied goal conditions applied to a shared environment layout, testing the policy's ability to condition behavior on the language instruction.
65	
66	Each suite contains 10 tasks, and we run 50 evaluation episodes per task, yielding 500 episodes per suite per experimental condition.
67	The evaluation metric is closed-loop Success Rate (SR): a binary indicator per episode that equals 1 only if the robot completes the full task within the time limit.
68	SR is measured through closed-loop execution, where the policy observes the current state, predicts an action, the simulator advances, and the policy re-observes the updated state at every timestep.
69	This closed-loop evaluation is critical because errors at any single step can cascade through subsequent observations and actions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-17T13:44:17.188363+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex",
  "old_string": "LIBERO-Object presents ten tasks focused on object manipulation, requiring the policy to identify and interact with specific objects from visually similar alternatives.",
  "new_string": "LIBERO-Object presents ten tasks focused on object manipulation; the policy must identify and interact with specific objects from visually similar alternatives."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex",
    "old_string": "LIBERO-Object presents ten tasks focused on object manipulation, requiring the policy to identify and interact with specific objects from visually similar alternatives.",
    "new_string": "LIBERO-Object presents ten tasks focused on object manipulation; the policy must identify and interact with specific objects from visually similar alternatives."
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-17T13:44:17.188719+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-17T13:44:17.188847+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex",
  "old_string": "LIBERO-Goal presents ten tasks with varied goal conditions applied to a shared environment layout, testing the policy's ability to condition behavior on the language instruction.",
  "new_string": "LIBERO-Goal presents ten tasks with varied goal conditions applied to a shared environment layout; these tasks test whether the policy can condition its behavior on the language instruction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex",
    "old_string": "LIBERO-Goal presents ten tasks with varied goal conditions applied to a shared environment layout, testing the policy's ability to condition behavior on the language instruction.",
    "new_string": "LIBERO-Goal presents ten tasks with varied goal conditions applied to a shared environment layout; these tasks test whether the policy can condition its behavior on the language instruction."
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-17T13:44:17.188991+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-17T13:44:17.189109+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex\" && echo \"=== Final -ing, check ===\" && grep -n \"ing,\" \"$FILE\" && echo \"=== Word count ===\" && wc -w \"$FILE\"",
  "description": "Final style checks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex\" && echo \"=== Final -ing, check ===\" && grep -n \"ing,\" \"$FILE\" && echo \"=== Word count ===\" && wc -w \"$FILE\"",
    "description": "Final style checks"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-17T13:44:17.189315+00:00_

=== Final -ing, check ===
27:Second, because patches are non-overlapping, each token encodes a unique spatial region of the input image, and no two tokens carry redundant information.
38:The intervention point for token reduction in our experiments sits immediately after this connector: pruning, masking, or merging operations are applied to the projected vision tokens before they enter the language model.
63:LIBERO-Spatial presents ten tasks focused on spatial reasoning, where the policy must place objects correctly or navigate relative to reference locations.
=== Word count ===
947 /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-17T13:44:17.189459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-17T13:44:17.189631+00:00_

1	% background.tex -- Section 2: Background
2	
3	\section{Background}
4	\label{sec:background}
5	
6	This section describes the two components of our experimental setup: the SmolVLA architecture~\cite{shukor2025smolvla}, in which we study vision token reduction, and the LIBERO benchmark~\cite{liu2023libero}, on which we evaluate closed-loop performance.
7	
8	\subsection{SmolVLA Architecture}
9	\label{sec:smolvla_arch}
10	
11	Vision-Language-Action (VLA) models cast robotic control as conditional generation: given a camera observation and a language instruction, the model predicts a continuous action.
12	SmolVLA~\cite{shukor2025smolvla} instantiates this paradigm with approximately 451.5M parameters, organized into a vision encoder, a modality connector, a language model backbone, and an action head.
13	Figure~\ref{fig:architecture} illustrates the full architecture and token flow.
14	
15	\begin{figure}[t]
16	\centering
17	\includegraphics[width=\linewidth]{figures/paper/fig_architecture.pdf}
18	\caption{SmolVLA architecture and token flow. Each camera image is encoded by SigLIP into 128 spatial patch tokens. An MLP connector projects these tokens into the LLM embedding space. The Qwen2-0.5B backbone processes the concatenated vision and language tokens, and a flow matching head generates continuous 7-DoF actions.}
19	\label{fig:architecture}
20	\end{figure}
21	
22	\paragraph{Vision encoder.}
23	SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\cite{zhai2023siglip} to process visual input.
24	SigLIP divides each camera image into non-overlapping spatial patches and encodes them independently, producing 128 tokens per image.
25	Two properties of this encoding are relevant to our analysis.
26	First, SigLIP does not include a \texttt{[CLS]} aggregation token; there is no single summary representation that pools information across patches.
27	Second, because patches are non-overlapping, each token encodes a unique spatial region of the input 
…[truncated 5426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_background_20260517T134047",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-17T13:44:17.189878+00:00_

Written to `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/background.tex`.

Section structure:
- **2.1 SmolVLA Architecture**: SigLIP encoder (128 tokens/camera, no [CLS], non-overlapping patches), MLP connector, Qwen2-0.5B backbone, flow matching action head, dual-camera setup (256 total tokens), intervention point after connector
- **2.2 LIBERO Benchmark**: Three suites (Object/Spatial/Goal), 500 episodes per condition, closed-loop SR metric, baseline numbers matching experiments section (44.8%/51.8%/63.0%)

Key foreshadowing planted: SigLIP's non-redundant spatial encoding and holistic dependence of flow matching on LLM representation, which the Analysis section later uses to explain the cliff edge.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_background_20260517T134047"
}
```

</details>

---
