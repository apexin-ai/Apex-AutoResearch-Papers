# paper expand method section

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_paper_expand_method_section_20260528T174644.jsonl`
- **Structured JSON:** [`9657651f9810c8b45621.json`](../../sessions/96/9657651f9810c8b45621.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-28T17:53:46.518525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/skills/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/skills/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-28T17:53:46.519077+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T17:53:46.519262+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T17:53:46.519445+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\ref{tab:model_properties}; Figure~\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.
8	
9	\textbf{Linear projection} applies a single matrix multiplication per patch. $\pi_{0}$~\cite{black2024pi0} projects 256 patches through a linear layer; $\pi_{0.5}$~\cite{black2025pi05} uses a $\times\!\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\,{<}\,$0.06).
10	
11	\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\,{=}\,$0.215); OFT~\cite{kim2025openoft} shares the same connector (512 tokens; CV$\,{=}\,$0.219).
12	
13	\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\cite{lewis2020bart} (50 tokens). SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).
14	
15	We classify coupling as \emph{independent} when each output token depends on a single input patch, and \emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\cite{liu2023libero}; $\pi_{0}$ and OFT contribute to the CV diagnostic only.
16	
17	\begin{figure*}[t]
18	\centering
19	\includegraphics[width=\textwidth]{figures/paper/fig_architecture_v4.pdf}
20	\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-
…[truncated 3154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T17:53:46.519596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T17:53:46.519821+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
5	
6	\subsection{Taxonomy Overview}
7	\label{sec:taxonomy_overview}
8	
9	Table~\ref{tab:taxonomy} organizes seven models into four response classes. The taxonomy reveals that effective vision-to-LLM pipeline complexity, not the nominal connector label or model scale, is strongly associated with pruning tolerance. Token importance CV tracks this ordering continuously across an 8$\times$ parameter range (450M to 7B): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\sim$0.15, smooth graded at $\sim$0.22, and catastrophic cliff at $>$0.3. A pairwise comparison between $\pi_0$ and OpenVLA (both consuming 256 SigLIP-based~\cite{zhai2023siglip} tokens but differing in connector, backbone, and encoder fusion) yields a 63\,pp gap at $k{=}0.1$; this gap is consistent with the monotonic CV-degradation pattern across all seven models (Section~\ref{sec:linear_results}).
10	
11	The four classes differ qualitatively in their failure mode. Uniformly critical models ($\pi_0$, $\pi_0.5$~\cite{black2025pi05}) distribute importance so evenly that no scoring method can identify dispensable tokens; pruning either preserves random spatial coverage (and survives) or removes a clustered patch (and fails). Threshold-graded models (X-VLA) tolerate removal up to a sharp onset point. Smooth graded models (OpenVLA, OFT, CogACT) degrade proportionally to the fraction removed. Catastrophic cliff models (SmolVLA) collapse at any removal level.
12	
13	\begin{table*}[t]
14	\centering
15	\small
16	\caption{Seven-model connector taxonomy. CV = coefficient of variation of vision token L2 norms. $^\dagger\pi_0$: offline metrics only, no clo
…[truncated 15852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T17:53:46.519982+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T17:53:46.520113+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-28T17:53:46.520297+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-28T17:53:46.520423+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-28T17:53:46.520949+00:00_

&lt;persisted-output>
Output too large (52.3KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5c041521-e8e2-414d-abe9-e8e6614720ac/tool-results/toolu_01GQsGzoo6GSmBfzBfB3g6oc.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md\", \"content\": \"# Paper Framing — importance_margin_vla_compress\\n\\n## Target Venue\\n- Primary: **CoRL 2026** (Austin, Nov 9-12; abstract May 26, paper May 29)\\n- Timeline: 4 days to abstract, 7 days to paper (as of 2026-05-22)\\n\\n## Title (working)\\n\\\"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility\\\"\\n\\n## Core Insight\\n\\n**⚠️ D171 (2026-05-22): Restructured from 4-class taxonomy to 2-axis framework.** Cross-suite data broke the original per-model classification — X-VLA \\\"threshold-graded\\\" on Object becomes catastrophic on Goal (-27.8pp at k=0.9) and Long (-45pp at k=0.95). The same connector produces drastically different pruning outcomes depending on task complexity. Pruning sensitivity is the product of two independent axes:\\n\\n**Axis 1 — Token Coupling (connector architecture):**\\n| Type | Connectors | CV Range | Mechanism |\\n|------|-----------|----------|-----------|\\n| **Token-independent** | Pure linear (π0, π0.5), MLP (OpenVLA, OFT) | 0.038–0.219 | Tokens retain individual spatial meaning; pruning damage is local |\\n| **Token-entangling** | BART post-proc (X-VLA), Pixel-shuffle (SmolVLA) | 0.151–0.314 | Cross-token dependencies; pruning damage cascades |\\n\\n**Axis 2 — Task Complexity:**\\n| Level | Suites | Characteristics |\\n|-------|--------|----------------|\\n| **Simple** | Object, Spatial | Single-step, pruning impact contained |\\n| **Complex** | Goal, Long | Multi-step reasoning, token lo
…[truncated 330 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T17:53:46.521163+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T17:53:46.521299+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5c041521-e8e2-414d-abe9-e8e6614720ac/tool-results/toolu_01GQsGzoo6GSmBfzBfB3g6oc.txt",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5c041521-e8e2-414d-abe9-e8e6614720ac/tool-results/toolu_01GQsGzoo6GSmBfzBfB3g6oc.txt",
    "limit": "300"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T17:53:46.521782+00:00_

1	{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md\", \"content\": \"# Paper Framing — importance_margin_vla_compress\\n\\n## Target Venue\\n- Primary: **CoRL 2026** (Austin, Nov 9-12; abstract May 26, paper May 29)\\n- Timeline: 4 days to abstract, 7 days to paper (as of 2026-05-22)\\n\\n## Title (working)\\n\\\"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility\\\"\\n\\n## Core Insight\\n\\n**⚠️ D171 (2026-05-22): Restructured from 4-class taxonomy to 2-axis framework.** Cross-suite data broke the original per-model classification — X-VLA \\\"threshold-graded\\\" on Object becomes catastrophic on Goal (-27.8pp at k=0.9) and Long (-45pp at k=0.95). The same connector produces drastically different pruning outcomes depending on task complexity. Pruning sensitivity is the product of two independent axes:\\n\\n**Axis 1 — Token Coupling (connector architecture):**\\n| Type | Connectors | CV Range | Mechanism |\\n|------|-----------|----------|-----------|\\n| **Token-independent** | Pure linear (π0, π0.5), MLP (OpenVLA, OFT) | 0.038–0.219 | Tokens retain individual spatial meaning; pruning damage is local |\\n| **Token-entangling** | BART post-proc (X-VLA), Pixel-shuffle (SmolVLA) | 0.151–0.314 | Cross-token dependencies; pruning damage cascades |\\n\\n**Axis 2 — Task Complexity:**\\n| Level | Suites | Characteristics |\\n|-------|--------|----------------|\\n| **Simple** | Object, Spatial | Single-step, pruning impact contained |\\n| **Complex** | Goal, Long | Multi-step reasoning, token loss cascades through action sequence |\\n\\n**Key interaction (D169):** Token-entangling connectors are dramatically more sensitive to task complexity:\\n- X-VLA Object k=0.9: 97.6% → X-VLA Goal k=0.9: 70.2% (-27.8pp, same model/method/k, only task differs)\\n- X-VLA Long k=0.95: ~53% (-45pp from baselin
…[truncated 51521 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T17:53:46.521963+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/skills/**/*.skill.md",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/skills/**/*.skill.md",
    "path": "/home/ubuntu"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T17:53:46.522151+00:00_

/home/ubuntu/agent-ml-research/skills/global/academic-writer.skill.md
/home/ubuntu/agent-ml-research/skills/global/code-survey.skill.md
/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md
/home/ubuntu/agent-ml-research/skills/global/dataset-discovery.skill.md
/home/ubuntu/agent-ml-research/skills/global/director-reviewer-synthesis.skill.md
/home/ubuntu/agent-ml-research/skills/global/data-snapshot.skill.md
/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md
/home/ubuntu/agent-ml-research/skills/global/check-key.skill.md
/home/ubuntu/agent-ml-research/skills/global/distill-session.skill.md
/home/ubuntu/agent-ml-research/skills/global/elastic-gpu.skill.md
/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md
/home/ubuntu/agent-ml-research/skills/global/first-project-entry.skill.md
/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md
/home/ubuntu/agent-ml-research/skills/global/idea-generation.skill.md
/home/ubuntu/agent-ml-research/skills/global/idea-proposal.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-cloud-rental.skill.md
/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-claude-pool.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md
/home/ubuntu/agent-ml-research/skills/global/novelty-check.skill.md
/home/ubuntu/agent-ml-research/skills/global/narrative-animation.skill.md
/home/ubuntu/agent-ml-research/skills/global/mvp-validation.skill.md
/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md
/home/ubuntu/agent-ml-research/skills/global/on-datagen-done.skill.md
/home/ubuntu/agent-ml-research/skills/global/negative-framing-review.skill.md
/home/ubuntu/agent-ml-research/skills/global/on-experiment-pending.skill.md
/home/ubuntu/agent-ml-research/skills/global/on-worker-done.skill.md
/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md
/h
…[truncated 3935 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T17:53:46.522320+00:00_

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
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T17:53:46.522725+00:00_

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
…[truncated 5709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T17:53:46.523092+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "We apply post-connector token pruning at retention ratio $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$, retaining $\\lfloor k \\cdot N \\rfloor$ tokens. Two strategies bracket expected performance: \\textbf{L2 norm selection} retains the top-$k$ fraction by L2 norm, and \\textbf{random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random. The \\emph{importance margin} at ratio $k$ is $\\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$; a positive margin indicates token importance structure is informative. Both strategies physically remove unselected tokens and re-index position IDs. We prune post-connector to isolate the connector's effect on token information structure.",
  "new_string": "Given $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:linear_results}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:openvla_results}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.85, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:linear_results})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "old_string": "We apply post-connector token pruning at retention ratio $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$, retaining $\\lfloor k \\cdot N \\rfloor$ tokens. Two strategies bracket expected performance: \\textbf{L2 norm selection} retains the top-$k$ fraction by L2 norm, and \\textbf{random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random. The \\emph{importance margin} at ratio $k$ is $\\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$; a positive margin indicates token importance structure is informative. Both strategies physically remove unselected tokens and re-index position IDs. We prune post-connector to isolate the connector's effect on token information structure.",
    "new_string": "Given $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:linear_results}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:openvla_results}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.85, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:linear_results})."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T17:53:46.523411+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-28T17:53:46.523600+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "We quantify post-connector token heterogeneity via the coefficient of variation (CV) of L2 norms:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nCV is a single-pass diagnostic requiring one forward pass with no downstream evaluation. It captures a continuous spectrum from $\\pi_{0}$ (CV$\\,{=}\\,$0.038, near-uniform norms) to SmolVLA (CV$\\,{=}\\,$0.314, high heterogeneity). Low-CV models have near-uniform tokens where \\emph{which} tokens are removed matters more than \\emph{how many}; high-CV entangling connectors fail catastrophically under any removal strategy.",
  "new_string": "We seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} \\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{Random} - \\text{L2})$ decreases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "old_string": "We quantify post-connector token heterogeneity via the coefficient of variation (CV) of L2 norms:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nCV is a single-pass diagnostic requiring one forward pass with no downstream evaluation. It captures a continuous spectrum from $\\pi_{0}$ (CV$\\,{=}\\,$0.038, near-uniform norms) to SmolVLA (CV$\\,{=}\\,$0.314, high heterogeneity). Low-CV models have near-uniform tokens where \\emph{which} tokens are removed matters more than \\emph{how many}; high-CV entangling connectors fail catastrophically under any removal strategy.",
    "new_string": "We seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} \\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{Random} - \\text{L2})$ decreases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout."
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T17:53:46.523839+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-28T17:53:46.523980+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T17:53:46.524209+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\ref{tab:model_properties}; Figure~\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.
8	
9	\textbf{Linear projection} applies a single matrix multiplication per patch. $\pi_{0}$~\cite{black2024pi0} projects 256 patches through a linear layer; $\pi_{0.5}$~\cite{black2025pi05} uses a $\times\!\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\,{<}\,$0.06).
10	
11	\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\,{=}\,$0.215); OFT~\cite{kim2025openoft} shares the same connector (512 tokens; CV$\,{=}\,$0.219).
12	
13	\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\cite{lewis2020bart} (50 tokens). SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).
14	
15	We classify coupling as \emph{independent} when each output token depends on a single input patch, and \emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\cite{liu2023libero}; $\pi_{0}$ and OFT contribute to the CV diagnostic only.
16	
17	\begin{figure*}[t]
18	\centering
19	\includegraphics[width=\textwidth]{figures/paper/fig_architecture_v4.pdf}
20	\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-
…[truncated 11738 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-28T17:53:46.524430+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "description": "Check for em-dashes (AI style violation)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "description": "Check for em-dashes (AI style violation)"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-28T17:53:46.524569+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"ing,\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex | head -20",
  "description": "Check for -ing participial phrases"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"ing,\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex | head -20",
    "description": "Check for -ing participial phrases"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-28T17:53:46.524693+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T17:53:46.524813+00:00_

13:\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\cite{lewis2020bart} (50 tokens). SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).
57:The L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\ref{sec:linear_results}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_expand_method_section_20260528T174644",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-28T17:53:46.525008+00:00_

Zero em-dashes. The `ing,` matches are all nouns (scoring, pruning, folding) in normal sentence structure, not dangling participial phrases.

Expansion complete. Summary of changes to `method.tex`:

**§3.2 Pruning Protocol** (was 1 paragraph, now 4 `\paragraph` blocks + 2 equations):
- Formal pruning operation definition with $\lfloor kN \rfloor$ notation
- **L2-norm scoring**: formula (Eq. 3), information density justification, spatial bias analysis
- **Random subsampling**: formula (Eq. 4), null hypothesis framing, spatial preservation property
- **Importance margin**: formal definition $\Delta(k)$, interpretation of positive/negative margins
- **Attention-based alternatives**: column-sum, cross-layer mean, attention rollout with intuitions; why we use L2/random instead
- **Retention ratio design space**: $k$ range rationale, cliff zone concept, per-architecture cliff locations

**§3.3 Compressibility Diagnostic** (was 1 equation + 1 paragraph, now 1 equation + spectrum equation + 4 `\paragraph` blocks):
- **CV spectrum** (Eq. 6): all 6 models ordered with connector-family grouping via `\underbrace`
- **CV as tolerance predictor**: high CV = dispensable tokens exist, low CV = uniform criticality; CV also predicts optimal strategy (L2 vs random)
- **Entropy comparison**: entropy clusters π0.5/X-VLA/OpenVLA (0.61--0.67) despite different pruning behaviors; "reading pattern" vs "writing pattern" distinction

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_expand_method_section_20260528T174644"
}
```

</details>

---
