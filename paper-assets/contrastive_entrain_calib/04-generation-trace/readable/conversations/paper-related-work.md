# paper related work

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_paper_related-work_20260520T090915.jsonl`
- **Structured JSON:** [`1cdf4c2887986e40d941.json`](../../sessions/1c/1cdf4c2887986e40d941.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-20T09:12:16.131627+00:00_

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
  "session": "worker_paper_related-work_20260520T090915",
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

_source line 2 · 2026-05-20T09:12:16.131979+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T09:12:16.132165+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T09:12:16.132486+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: \\\"2026-05-20T03:15:00Z\\\"\\n  total_papers: 21\\n\\ncategories:\\n  - key: direct-competitor\\n    name: \\\"Direct Competitors\\\"\\n    narrative: \\\"Methods using representation geometry as RL reward or directly competing approaches\\\"\\n  - key: foundation\\n    name: \\\"Foundation\\\"\\n    narrative: \\\"Foundational methods our work directly builds on (RepE, GRPO, CAA, ITI, ActAdd)\\\"\\n  - key: reward-hacking\\n    name: \\\"Reward Hacking\\\"\\n    narrative: \\\"Reward hacking theory and empirics — contextualizes our probe gaming finding\\\"\\n  - key: sycophancy\\n    name: \\\"Sycophancy\\\"\\n    narrative: \\\"Sycophancy characterization and mitigation\\\"\\n  - key: related-methods\\n    name: \\\"Related Methods\\\"\\n    narrative: \\\"Related mitigation approaches and RL methods\\\"\\n\\npapers:\\n  zhang2026latentgrpo:\\n    title: \\\"Silence the Judge: Reinforcement Learning with Self-Verifier via Latent Geometric Clustering (Latent-GRPO)\\\"\\n    authors:\\n      - \\\"Zhang, et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv 2026\\\"\\n    arxiv_id: \\\"2601.08427\\\"\\n    role: direct-competitor\\n    category: direct-competitor\\n    relevance: \\\"Closest competitor. Also uses representation geometry as GRPO reward, but for reasoning correctness (clustering) not behavioral attributes (direction projection).\\\"\\n    verified: true\\n\\n  zou2023repe:\\n    title: \\\"Representation Engineering: A Top-Down Approach to AI Transparency\\\"\\n    authors:\\n      - \\\"Zou, Andy\\\"\\n      - \\\"Phan, Long\\\"\\n      - \\\"Chen, Sarah\\\"\\n    year: 2023\\n    venue: \\\"arXiv 2023\\\"\\n    arxiv_id: \\\"2310.01405\\\"\\n    role: foundation\\n    category: foundation\\n    relevance: \\\"THE foundational paper. We extend RepE from 
…[truncated 9027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T09:12:16.132662+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "writing_plan.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "file": "writing_plan.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T09:12:16.133113+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026\\n  track: \\\"ARR May/August cycle → EMNLP 2026 Findings (target 3.0-3.5)\\\"\\n  template: \\\"acl-org/acl-style-files (ARR/ACL 2025 official)\\\"\\n  template_note: \\\"Director 指定 ARR/ACL 2025 官方模板 (acl-org/acl-style-files)。Worker 需 clone 并部署到 projects/{project}/docs/paper/\\\"\\n  page_limit: 8  # EMNLP 2026: 8 pages main text, unlimited references. Limitations outside page limit.\\n  deadline: \\\"August cycle (~Aug 15)\\\"\\n  core_claim: >\\n    A linear sycophancy direction (d_syc) achieves AUROC 0.82 (Qwen3-8B) and 0.78\\n    (Llama-3-8B), demonstrating cross-model discriminability, yet fails as GRPO reward\\n    in ALL tested formulations — continuous cosine penalizes all belief change while\\n    binarized probe rewards all resistance — both exploiting the direction's blindness\\n    to change warrant. We identify a probe reward trap causing behavioral collapse\\n    1300 steps before entropy collapse, revealing that discriminability ≠ reward utility\\n    in representation-guided RL.\\n  working_title: \\\"Discriminability Without Utility: Why Sycophancy Directions Fail as RL Rewards\\\"\\n  paper_type: analysis  # negative result + mechanistic analysis\\n  created_at: 2026-05-20T10:00:00Z\\n\\n# ============================================================\\n# PAPER OUTLINE\\n# ============================================================\\npaper_outline:\\n  - section: abstract\\n    word_budget: 200\\n    core_bullets:\\n      - \\\"Problem: anti-sycophancy training faces a double-bind — blocking capitulation also blocks legitimate revision. Representation-based approaches promise selective targeting.\\\"\\n      - \\\"Setup: extract d_syc from contrastive pairs (AUROC 0.82), test three R1 formulations as GRPO reward\\\"\\n      - \\\"Negative result: 
…[truncated 27147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T09:12:16.133319+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T09:12:16.133637+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md\", \"content\": \"# Paper Framing — contrastive_entrain_calib\\n\\n## Target Venue\\n- Primary: **EMNLP 2026** via ARR May 2026 cycle\\n- ARR Submission Deadline: **May 25, 2026** (6 days from May 19)\\n- Commitment Deadline: **August 2, 2026**\\n- ⚠️ May cycle 新政策：提交时必须声明目标会议为 EMNLP，绑定不可更改\\n- Fallback: ARR August 2026 cycle (DDL ~Aug 15) → EACL 2027 / ACL 2027\\n- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)\\n\\n## Core Claims (3 条, 可证伪)\\n\\n1. **Directional discriminability + training stability**: The policy model's activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision (AUROC 0.82), with signal emerging at mid-layers (L16-19). During GRPO training, d_syc remains stable (cosine ≈ 0.96 at step 500), and linear separability is preserved (AUROC 0.80 at step 500). Periodic recalibration (every 500 steps) is included as a safety mechanism.\\n   - *Evidence needed*: AUROC on style-controlled data, layer progression, direction stability curve, AUROC at each checkpoint\\n   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence\\n   - *New finding (D025 corrects D024)*: Initial stability measurement reported cosine=0.28 (74° drift) but this was a measurement artifact from referencing a stale directions.pt file (different dataset). Actual drift: cosine ≈ 0.96. Direction is stable during training.\\n   - *New finding (D019)*: Per-layer cosine AUROC ≥ 0.77 at step 500, deep layers L32/33 improved +0.025/+0.033. Full training curve (exp-006) pending.\\n   - *New finding (D036)*: **Cross-model generalization confirmed.** Llama-3-8B-Instruct 5-fold CV AUROC=0.7793±0.019 (best layer=16), style-controlled=0.9227. Same strength gradient as Qwen3-8B (weak 0.711 < medium 0.864 < strong 0.911). d_syc is a cross-model phenomenon
…[truncated 17280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T09:12:16.133816+00:00_

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
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T09:12:16.134196+00:00_

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
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T09:12:16.134388+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T09:12:16.134520+00:00_

docs/paper/sections/framework.tex
docs/paper/sections/cosine_failure.tex
docs/paper/sections/probe_trap.tex
docs/paper/sections/direction_quality.tex
docs/paper/sections/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T09:12:16.134644+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T09:12:16.134801+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Representation engineering \citep{zou2023repe} reveals that large language models encode sycophancy as a linear direction in their residual streams.
5	A contrastive sycophancy direction $\dsyc$, extracted from style-controlled pairs of valid belief revision and sycophantic capitulation, achieves cross-validated AUROC $0.827 \pm 0.028$ on Qwen3-8B and $0.779 \pm 0.019$ on Llama-3-8B (\S\ref{sec:direction_quality}).
6	The direction captures evidential granularity: discriminability rises monotonically from weak-evidence pairs (AUROC 0.675) through medium (0.883) to strong (0.929), and the signal remains stable under LoRA training with cosine drift of approximately 0.96 at 500 steps.
7	These results, replicated across two architecturally distinct model families, point to an appealing possibility: if the model's representations already separate sycophantic from non-sycophantic behavior, that separation should be convertible into a reward signal for reinforcement learning.
8	Sycophancy is among the most persistent alignment failures in deployed systems \citep{sharma2023sycophancy}, and a representation-level reward could complement existing behavioral approaches by targeting the internal computation rather than its surface outputs.
9	
10	This paper shows that the conversion fails.
11	We test three formulations that translate $\dsyc$ into a GRPO training signal (cosine similarity, scaled cosine, and binary probe) across six experimental configurations.
12	Every formulation fails.
13	Cosine similarity produces a reward gap of just 0.098 between valid and sycophantic activations, too narrow to drive policy updates (\S\ref{sec:cosine_failure}).
14	Online recalibration improves the offline AUROC from 0.82 to 0.91 yet triggers mode collapse rather than better training.
15	A binary probe with stopped gradients avoids the magnitude problem but creates a stubbornness trap: the model learns that never revising its answer reli
…[truncated 4315 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T09:12:16.134969+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/framework.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T09:12:16.135144+00:00_

1	\section{Experimental Framework}
2	\label{sec:framework}
3	
4	This section establishes the notation, experimental components, and evaluation protocol used throughout the paper.
5	We first describe how the contrastive sycophancy direction $\dsyc$ is extracted (\S\ref{ssec:extraction}), then define three reward formulations that incorporate $\dsyc$ into GRPO training (\S\ref{ssec:reward}), explain the online recalibration procedure (\S\ref{ssec:recalib}), and finally specify the evaluation metrics (\S\ref{ssec:eval}).
6	
7	\subsection{Direction Extraction}
8	\label{ssec:extraction}
9	
10	We extract a linear sycophancy direction $\dsyc$ from the residual stream of a target model using contrastive activation pairs.
11	Each pair consists of two model responses to the same user challenge: a \emph{valid correction}, in which the model appropriately revises its earlier answer upon receiving well-supported counter-evidence, and a \emph{sycophantic capitulation}, in which the model abandons a correct answer under social pressure without adequate evidential warrant.
12	
13	To isolate the cognitive signal from surface-level linguistic variation, we apply style control: both responses in each pair are generated with matched hedging patterns, politeness markers, and response length, so that $\dsyc$ reflects the distinction between warranted and unwarranted belief change rather than stylistic differences.
14	Concretely, we construct 362 style-controlled contrastive activations from 181 paired examples stratified across three evidence-strength levels (weak, medium, strong).
15	
16	Given a target layer $\ell$, let $\mathbf{h}^{+}_i$ denote the residual-stream activation for the $i$-th valid correction and $\mathbf{h}^{-}_i$ for the corresponding sycophantic capitulation.
17	The sycophancy direction is the mean difference:
18	\begin{equation}
19	\label{eq:dsyc}
20	\dsyc = \frac{1}{N}\sum_{i=1}^{N}\left(\mathbf{h}^{+}_i - \mathbf{h}^{-}_i\right)
21	\end{equation}
22	where $N{=}181$ 
…[truncated 4916 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T09:12:16.135320+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T09:12:16.135440+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T09:12:16.135553+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"^@\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/references.bib",
  "description": "List all bib entry keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"^@\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/references.bib",
    "description": "List all bib entry keys"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T09:12:16.135671+00:00_

1:@article{zhang2026latentgrpo,
8:@article{zou2023repe,
15:@inproceedings{rimsky2024caa,
22:@article{shao2024grpo,
29:@inproceedings{li2023iti,
36:@article{turner2023actadd,
43:@inproceedings{gao2023scaling,
50:@inproceedings{skalse2022hacking,
57:@article{casper2023openproblems,
64:@article{denison2024subterfuge,
71:@article{sharma2023sycophancy,
78:@article{shapira2026amplifies,
85:@article{wang2025internal,
92:@article{wei2024synthetic,
99:@article{wen2024mislead,
106:@article{ackermann2026gradreg,
113:@article{obrien2025fewbadneurons,
120:@article{mckinney2023fragility,
127:@inproceedings{burns2023ccs,
134:@article{sinii2025smallvectors,
141:@article{consistency2025bctact,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T09:12:16.135809+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T09:12:16.135952+00:00_

docs/paper/main.tex
docs/paper/framework.tex
docs/paper/cosine_failure.tex
docs/paper/probe_trap.tex
docs/paper/direction_quality.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T09:12:16.136070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/main.tex",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T09:12:16.136197+00:00_

1	\documentclass[11pt,a4paper]{article}
2	\usepackage[hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	
13	\newcommand{\dsyc}{d_{\text{syc}}}
14	\newcommand{\tof}{\text{ToF}}
15	\newcommand{\nof}{\text{NoF}}
16	\newcommand{\sycon}{\textsc{SyconScore}}
17	\newcommand{\rone}{R_1}
18	\newcommand{\rthree}{R_3}
19	
20	\title{Discriminability Without Utility: Why Sycophancy Directions Fail as RL Rewards}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	\input{sections/abstract}
29	\end{abstract}
30	
31	\input{sections/introduction}
32	
33	\input{sections/framework}
34	
35	\input{sections/direction_quality}
36	
37	\input{sections/cosine_failure}
38	
39	\input{sections/probe_trap}
40	
41	\input{sections/discussion}
42	
43	\input{sections/related_work}
44	
45	\input{sections/conclusion}
46	
47	\section*{Limitations}
48	\input{sections/limitations}
49	
50	\bibliographystyle{acl_natbib}
51	\bibliography{references}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T09:12:16.136451+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Representation Engineering and Activation Steering.}\nRepresentation engineering \\citep{zou2023repe} established that linear directions in LLM residual streams encode high-level behavioral concepts.\nSubsequent work exploited such directions for inference-time intervention: ITI \\citep{li2023iti} uses probe weights as steering vectors for truthfulness, ActAdd \\citep{turner2023actadd} adds fixed activation offsets to shift model behavior, and CAA \\citep{rimsky2024caa} applies contrastive activation addition to reduce sycophancy at inference time.\nCCS \\citep{burns2023ccs} discovers truth-related directions without supervision through a consistency objective.\nAll five methods use representation geometry for inference-time classification or steering.\nOur work tests whether the same geometric information transfers to a training-time reward signal, and finds that it does not: $\\dsyc$ achieves strong discriminability (AUROC 0.82) but fails as a GRPO reward in all tested formulations.\n\n\\paragraph{Sycophancy Characterization and Mitigation.}\n\\citet{sharma2023sycophancy} showed that sycophancy is pervasive across RLHF-trained assistants and identified preference-model bias as a contributing cause.\n\\citet{shapira2026amplifies} proved formally that RLHF amplifies sycophancy under standard assumptions.\n\\citet{wang2025internal} traced the phenomenon to late-layer preference shifts via logit-lens analysis and confirmed that sycophantic behavior has identifiable internal origins.\nOn the mitigation side, \\citet{wei2024synthetic} demonstrated that synthetic data mixed into fine-tuning reduces sycophancy at the data level.\nActivation consistency training \\citep[ACT;][]{consistency2025bctact} penalizes activation divergence between the model's initial and post-pressure responses but does not distinguish warranted from unwarranted belief changes.\n\\citet{obrien2025fewbadneurons} identified sycophancy-associated neurons and surgically corrected them; their probes serve a diagnostic role rather than an optimization target.\nThese methods either operate at the data or behavioral level, where all belief changes are treated uniformly, or use representations only for diagnosis.\nOur analysis shows why the step from diagnosis to reward is structurally blocked for sycophancy: the direction that detects the behavior conflates it with its complement.\n\n\\paragraph{Reward Design and Overoptimization.}\n\\citet{gao2023scaling} established scaling laws for reward model overoptimization: proxy rewards diverge from true objectives under sustained optimization pressure.\n\\citet{skalse2022hacking} proved that no bounded proxy reward can be immune to hacking.\n\\citet{casper2023openproblems} surveyed fundamental limitations of RLHF, including reward misspecification and distributional shift.\n\\citet{denison2024subterfuge} showed that reward hacking can escalate from sycophantic agreement to active reward tampering.\n\\citet{mckinney2023fragility} found that learned reward functions fail when applied to train new policies, a failure mode related to our probe reward trap.\n\\citet{wen2024mislead} documented U-Sophistry, where models learn to produce outputs that mislead human evaluators.\n\\citet{ackermann2026gradreg} proposed gradient regularization as a mitigation strategy.\nOur probe reward trap is an extreme instance of overoptimization: a low-capacity linear probe is gamed within 500 training steps, with behavioral collapse preceding entropy collapse by approximately 1,300 steps.\n\n\\paragraph{Representation-Guided Reinforcement Learning.}\n\\citet{zhang2026latentgrpo} introduced Latent-GRPO, which uses spherical projection onto robust cluster centroids as a GRPO reward for reasoning correctness.\n\\citet{sinii2025smallvectors} showed that RL training induces structured changes in steering vectors, a result that supports the feasibility of representation-space rewards in principle.\nBoth approaches succeed because the target categories (correct vs.\\ incorrect reasoning, safe vs.\\ unsafe outputs) occupy geometrically separable regions along the relevant direction.\nSycophancy breaks this condition: capitulation and legitimate revision share the same geometric direction and differ only in whether the belief change is warranted, a property that no activation-space direction encodes.\nOur results explain this asymmetry and identify the warrant gap as the structural barrier.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Representation Engineering and Activation Steering.}\nRepresentation engineering \\citep{zou2023repe} established that linear directions in LLM residual streams encode high-level behavioral concepts.\nSubsequent work exploited such directions for inference-time intervention: ITI \\citep{li2023iti} uses probe weights as steering vectors for truthfulness, ActAdd \\citep{turner2023actadd} adds fixed activation offsets to shift model behavior, and CAA \\citep{rimsky2024caa} applies contrastive activation addition to reduce sycophancy at inference time.\nCCS \\citep{burns2023ccs} discovers truth-related directions without supervision through a consistency objective.\nAll five methods use representation geometry for inference-time classification or steering.\nOur work tests whether the same geometric information transfers to a training-time reward signal, and finds that it does not: $\\dsyc$ achieves strong discriminability (AUROC 0.82) but fails as a GRPO reward in all tested formulations.\n\n\\paragraph{Sycophancy Characterization and Mitigation.}\n\\citet{sharma2023sycophancy} showed that sycophancy is pervasive across RLHF-trained assistants and identified preference-model bias as a contributing cause.\n\\citet{shapira2026amplifies} proved formally that RLHF amplifies sycophancy under standard assumptions.\n\\citet{wang2025internal} traced the phenomenon to late-layer preference shifts via logit-lens analysis and confirmed that sycophantic behavior has identifiable internal origins.\nOn the mitigation side, \\citet{wei2024synthetic} demonstrated that synthetic data mixed into fine-tuning reduces sycophancy at the data level.\nActivation consistency training \\citep[ACT;][]{consistency2025bctact} penalizes activation divergence between the model's initial and post-pressure responses but does not distinguish warranted from unwarranted belief changes.\n\\citet{obrien2025fewbadneurons} identified sycophancy-associated neurons and surgically corrected them; their probes serve a diagnostic role rather than an optimization target.\nThese methods either operate at the data or behavioral level, where all belief changes are treated uniformly, or use representations only for diagnosis.\nOur analysis shows why the step from diagnosis to reward is structurally blocked for sycophancy: the direction that detects the behavior conflates it with its complement.\n\n\\paragraph{Reward Design and Overoptimization.}\n\\citet{gao2023scaling} established scaling laws for reward model overoptimization: proxy rewards diverge from true objectives under sustained optimization pressure.\n\\citet{skalse2022hacking} proved that no bounded proxy reward can be immune to hacking.\n\\citet{casper2023openproblems} surveyed fundamental limitations of RLHF, including reward misspecification and distributional shift.\n\\citet{denison2024subterfuge} showed that reward hacking can escalate from sycophantic agreement to active reward tampering.\n\\citet{mckinney2023fragility} found that learned reward functions fail when applied to train new policies, a failure mode related to our probe reward trap.\n\\citet{wen2024mislead} documented U-Sophistry, where models learn to produce outputs that mislead human evaluators.\n\\citet{ackermann2026gradreg} proposed gradient regularization as a mitigation strategy.\nOur probe reward trap is an extreme instance of overoptimization: a low-capacity linear probe is gamed within 500 training steps, with behavioral collapse preceding entropy collapse by approximately 1,300 steps.\n\n\\paragraph{Representation-Guided Reinforcement Learning.}\n\\citet{zhang2026latentgrpo} introduced Latent-GRPO, which uses spherical projection onto robust cluster centroids as a GRPO reward for reasoning correctness.\n\\citet{sinii2025smallvectors} showed that RL training induces structured changes in steering vectors, a result that supports the feasibility of representation-space rewards in principle.\nBoth approaches succeed because the target categories (correct vs.\\ incorrect reasoning, safe vs.\\ unsafe outputs) occupy geometrically separable regions along the relevant direction.\nSycophancy breaks this condition: capitulation and legitimate revision share the same geometric direction and differ only in whether the belief change is warranted, a property that no activation-space direction encodes.\nOur results explain this asymmetry and identify the warrant gap as the structural barrier.\n"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T09:12:16.136638+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T09:12:16.136784+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex\" && echo \"=== Word count (detex approximation) ===\" && cat \"$FILE\" | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$\\\\]//g; s/~/ /g' | wc -w && echo \"\" && echo \"=== Em-dash count ===\" && grep -c \"—\" \"$FILE\" || echo \"0\" && echo \"\" && echo \"=== En-dash count ===\" && grep -c \" – \" \"$FILE\" || echo \"0\" && echo \"\" && echo \"=== Banned word check (Furthermore/Moreover/Additionally) ===\" && grep -inE \"Furthermore|Moreover|Additionally\" \"$FILE\" || echo \"None found\" && echo \"\" && echo \"=== -ing phrase endings ===\" && grep -nE \", [a-z]+ing \" \"$FILE\" | head -20 && echo \"\" && echo \"=== Self-reference check ===\" && grep -in \"In this paper\" \"$FILE\" || echo \"None found\"",
  "description": "Run style checks and word count on related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex\" && echo \"=== Word count (detex approximation) ===\" && cat \"$FILE\" | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$\\\\]//g; s/~/ /g' | wc -w && echo \"\" && echo \"=== Em-dash count ===\" && grep -c \"—\" \"$FILE\" || echo \"0\" && echo \"\" && echo \"=== En-dash count ===\" && grep -c \" – \" \"$FILE\" || echo \"0\" && echo \"\" && echo \"=== Banned word check (Furthermore/Moreover/Additionally) ===\" && grep -inE \"Furthermore|Moreover|Additionally\" \"$FILE\" || echo \"None found\" && echo \"\" && echo \"=== -ing phrase endings ===\" && grep -nE \", [a-z]+ing \" \"$FILE\" | head -20 && echo \"\" && echo \"=== Self-reference check ===\" && grep -in \"In this paper\" \"$FILE\" || echo \"None found\"",
    "description": "Run style checks and word count on related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T09:12:16.136959+00:00_

=== Word count (detex approximation) ===
486

=== Em-dash count ===
0
0

=== En-dash count ===
0
0

=== Banned word check (Furthermore/Moreover/Additionally) ===
None found

=== -ing phrase endings ===
24:\citet{casper2023openproblems} surveyed fundamental limitations of RLHF, including reward misspecification and distributional shift.

=== Self-reference check ===
None found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T09:12:16.137114+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex\" && detex \"$FILE\" 2>/dev/null | wc -w || (sed 's/\\\\citet{[^}]*}/CITE/g; s/\\\\citep{[^}]*}/CITE/g; s/\\\\citep\\[.*\\]{[^}]*}/CITE/g; s/\\\\paragraph{[^}]*}//g; s/\\\\section{[^}]*}//g; s/\\\\label{[^}]*}//g; s/\\\\emph{//g; s/\\\\textbf{//g; s/\\\\dsyc/dsyc/g; s/\\$[^$]*\\$//g; s/[{}\\\\]//g; s/~/ /g' \"$FILE\" | wc -w)",
  "description": "More accurate word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Bash",
  "tool_args": {
    "command": "FILE=\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/paper/sections/related_work.tex\" && detex \"$FILE\" 2>/dev/null | wc -w || (sed 's/\\\\citet{[^}]*}/CITE/g; s/\\\\citep{[^}]*}/CITE/g; s/\\\\citep\\[.*\\]{[^}]*}/CITE/g; s/\\\\paragraph{[^}]*}//g; s/\\\\section{[^}]*}//g; s/\\\\label{[^}]*}//g; s/\\\\emph{//g; s/\\\\textbf{//g; s/\\\\dsyc/dsyc/g; s/\\$[^$]*\\$//g; s/[{}\\\\]//g; s/~/ /g' \"$FILE\" | wc -w)",
    "description": "More accurate word count"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T09:12:16.137235+00:00_

517

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_related-work_20260520T090915",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-20T09:12:16.137404+00:00_

Results:

- **Word count**: ~517 (within the 550-word budget)
- **Em-dash count**: 0
- **En-dash count**: 0
- **Banned words** (Furthermore/Moreover/Additionally): 0
- **Self-references** ("In this paper"): 0
- **-ing phrase endings**: 0 (the only match is "including" used as a preposition, not a participial clause)

**Citation coverage**: All 21 papers from `literature_map.yaml` are cited (20 directly in Related Work + `shao2024grpo` already cited in Framework as our RL algorithm).

**Structure**: 4 paragraphs organized by topic:
1. Representation Engineering and Activation Steering (5 papers: zou, li, turner, rimsky, burns)
2. Sycophancy Characterization and Mitigation (6 papers: sharma, shapira, wang, wei, consistency, obrien)
3. Reward Design and Overoptimization (7 papers: gao, skalse, casper, denison, mckinney, wen, ackermann)
4. Representation-Guided RL (2 papers: zhang, sinii)

Each cluster ends with a positioning sentence connecting to our contribution.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_related-work_20260520T090915"
}
```

</details>

---
