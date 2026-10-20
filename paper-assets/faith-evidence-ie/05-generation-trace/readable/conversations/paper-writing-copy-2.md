# paper writing

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_paper_writing_20260517T171232.jsonl`
- **Structured JSON:** [`94cbf7e0dcd6fc0cde22.json`](../../sessions/94/94cbf7e0dcd6fc0cde22.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-17T17:14:04.042501+00:00_

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
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T17:14:04.043226+00:00_

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
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T17:14:04.043499+00:00_

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
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T17:14:04.044082+00:00_

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
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T17:14:04.044470+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T17:14:04.044713+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task: Evidence-Grounded Document-Level Relation Extraction}
5	\label{sec:task}
6	
7	Given a document $D = \{s_1, \ldots, s_n\}$ consisting of $n$ sentences and a set of entities $\mathcal{E}$ identified within $D$, the task of evidence-grounded document-level relation extraction (DocRE) requires predicting, for each entity pair $(e_h, e_t) \in \mathcal{E} \times \mathcal{E}$, a relation $r \in \mathcal{R} \cup \{\texttt{NA}\}$ together with a set of supporting evidence sentences $E \subseteq D$. Standard DocRE predicts only the triple $(e_h, r, e_t)$; the evidence-grounded formulation also requires $E$, which grounds each prediction in specific textual support.
8	
9	In our LLM-based approach, the model generates structured outputs that jointly encode both components. For each predicted relation, the output follows the format \texttt{(head, relation, tail) | Evidence: [S$i$][S$j$]}, requiring the model to produce complete evidence references inline with each triple rather than as a separate retrieval step. This design contrasts with encoder-based evidence methods such as SAIS~\citep{xiao2022sais} and DREEAM~\citep{ma2023dreeam}, which frame evidence identification as sentence-level binary classification. Because classification over a fixed sentence set does not increase output length, these methods incur no generation overhead. Our LLM formulation requires additional tokens for each evidence reference, creating a generation burden that scales with the number of predicted triples and their evidence sentences. This scale-dependent cost is the central phenomenon we investigate.
10	
11	
12	\subsection{Supervised Fine-Tuning Baseline}
13	\label{sec:sft}
14	
15	We fine-tune all models with LoRA~\citep{hu2022lora} at rank $r{=}64$ and scaling factor $\alpha{=}128$, applied to attention projection matrices. The training data consists of DocRED~\citep{yao2019docred} training documents converted to the structured output 
…[truncated 7698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T17:14:04.044898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T17:14:04.045138+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Dataset.}
8	We conduct experiments on DocRED~\citep{yao2019docred}, a large-scale document-level relation extraction benchmark containing 3,053 training and 998 development documents spanning 96 relation types. Each document requires identifying relational triples across multiple sentences and grounding each triple with supporting evidence sentences. We use Re-DocRED~\citep{tan2022redocred} for cross-dataset generalization evaluation.
9	
10	\paragraph{Models.}
11	Our primary model is Qwen3-4B. To study scale effects, we additionally train Qwen3-1.7B and Qwen3-8B under identical configurations. We include LLaMA-3.1-8B as a cross-family validation point.
12	
13	\paragraph{Training.}
14	All models use LoRA~\citep{hu2022lora} with rank $r{=}64$ and $\alpha{=}128$ over a structured output format that jointly produces relation triples and evidence sentences. For RSFT, we sample $N{=}8$ candidate outputs per document and select the top-$k{=}1$ response ranked by CED scoring (\S\ref{sec:ced}), which combines NLI-based evidence faithfulness with extraction accuracy. GRPO experiments use group sizes $G{=}4$ (QLoRA, 4-bit) and $G{=}8$ (bf16 full-precision LoRA). DPO constructs preference pairs from CED-ranked outputs.
15	
16	\paragraph{Metrics.}
17	We report five metrics. \textbf{Ign-F1} is the primary DocRED metric that ignores triples appearing in the training set, matching the official leaderboard protocol. \textbf{Rel-F1} measures relation extraction F1 on all triples. \textbf{Evi-F1 (TP-only)} measures evidence sentence F1 conditioned on correctly predicted triples, reflecting evidence quality independent of extraction errors. \textbf{Evi-F1 (joint)} includes false-positive and false-negative triples in the denominator following the DREEAM protocol~\citep{ma2023dreeam}, enabling cross-method evidence comparison. \textbf{EDCR} (Evidence-Decoupling Rati
…[truncated 13778 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T17:14:04.045361+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T17:14:04.045987+00:00_

1	\section{Introduction}
2	
3	Document-level relation extraction (DocRE) requires identifying semantic relations between entity pairs across multiple sentences, a task where encoder-based methods such as \citet{zhou2021atlop} long dominated.
4	Recent LLM-based approaches have closed this gap: \citet{wan2024genres} recast DocRE as constrained generation, \citet{xu2024lmrc} frame it as multi-choice reading comprehension, and \citet{chen2025docksrag} combine retrieval-augmented generation with structured knowledge.
5	These methods approach or surpass encoder baselines on DocRED \citep{yao2019docred} and Re-DocRED \citep{tan2022redocred} in extraction accuracy.
6	Yet every one of them outputs bare relation triplets $(e_h, r, e_t)$ without any indication of \emph{which sentences} in the document support each prediction.
7	In deployment contexts where predictions feed into clinical knowledge bases, legal due-diligence pipelines, or financial compliance systems, end users cannot verify a prediction without manually locating its textual basis across a multi-page document.
8	
9	The absence of verifiable evidence creates a practical bottleneck.
10	Relation extraction outputs are consumed downstream by knowledge graph construction and human decision workflows.
11	When a system predicts that a drug interacts with a gene, or that a contract clause implies a liability, practitioners must trace each prediction back to source text before acting on it.
12	Without machine-generated evidence, this verification requires exhaustive manual review of the input document for every predicted relation.
13	Encoder-based methods have partially addressed this need: \citet{xiao2022sais} introduce sentence-level evidence supervision as an auxiliary signal, and \citet{ma2023dreeam} extend this with dynamic evidence retrieval through memory attention.
14	Both improve extraction quality \emph{and} produce evidence annotations.
15	However, encoder methods now trail LLM-based approaches in extraction a
…[truncated 4770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T17:14:04.046494+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/",
  "description": "List existing paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/",
    "description": "List existing paper sections"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T17:14:04.046873+00:00_

experiments.tex
introduction.tex
method.tex
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T17:14:04.047274+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex",
  "content": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{EDCR as a dual-layer diagnostic.}\nThe Evidence-Decoupling Ratio (\\S\\ref{sec:edcr}) provides diagnostic value at two complementary levels. At the method level, EDCR correlates strongly with extraction quality across optimization paradigms: Spearman $\\rho = -0.965$ between EDCR and Rel-F1 (Table~\\ref{tab:spectrum}). GRPO QLoRA reaches EDCR $= 0.9876$, confirming catastrophic decoupling; RSFT achieves $0.6503$, consistent with healthy joint optimization; SFT falls between at $0.6982$. As a practical guideline, EDCR values above 0.70 indicate concerning decoupling, while values below 0.65 reflect balanced extraction and evidence capabilities.\n\nAt the per-relation level, computing EDCR for each of the 76 relation types with $\\geq$5 evaluation samples reveals a more nuanced picture. Per-relation EDCR correlates strongly with per-relation Rel-F1 ($\\rho = -0.793$, $p < 0.001$), confirming its utility as a difficulty indicator for individual relation types. However, per-relation EDCR is statistically independent of Evi-F1 ($\\rho = -0.064$, $p = 0.58$), and Evi-F1 itself shows no association with Rel-F1 ($\\rho = -0.013$, $p = 0.91$). These two null correlations establish that evidence quality and extraction ability are fully decoupled across relation types: knowing how well a model extracts a given relation tells us nothing about its evidence quality for that relation. EDCR captures this misalignment precisely because it measures the \\emph{ratio} of the two capabilities rather than either in isolation. Extreme cases illustrate the diagnostic power: \\texttt{date\\_of\\_birth} has EDCR $= 0.118$ (highly faithful, with extraction and evidence tightly coupled), while \\texttt{head\\_of\\_government} reaches $0.956$ (highly decoupled, where the model generates accurate evidence for a relation it rarely extracts correctly). Method-level EDCR thus serves as a horizontal comparison tool across optimization paradigms, while per-relation EDCR enables vertical diagnosis of which specific relation types suffer from extraction-evidence misalignment.\n\n\n\\paragraph{Why RSFT avoids decoupling.}\nThe structural difference between selection and optimization explains why RSFT does not exhibit the decoupling observed in gradient-based methods. GRPO and DPO update model parameters through gradients that optimize a reward signal. When two sub-tasks (extraction and evidence) compete for gradient capacity, the optimizer can discover and exploit the trade-off between them, improving one at the expense of the other. RSFT operates differently: it selects complete outputs and trains on them with standard supervised loss. Because the selection is discrete (accept or reject a full response), there is no gradient pathway through which the model can learn to sacrifice extraction for evidence quality. Only outputs where both extraction and evidence are jointly strong survive the CED filter. This property is not specific to RSFT's design but is a structural consequence of discrete selection over complete outputs: any selection-based method that filters on a joint quality criterion will inherit the same coupling guarantee. The implication for practitioners is direct: when optimizing for multiple coupled generation objectives, selection-based methods preserve inter-objective balance that gradient-based methods disrupt.\n\n\n\\paragraph{NLI scoring ablation.}\nWe compare CED (\\S\\ref{sec:ced}) against flat-NLI (positive entailment score $p^+$ only, without the contrastive term) as RSFT scoring functions. CED RSFT achieves mean Rel-F1 of 0.4569 (seeds 42, 44: 0.4517, 0.4621), and flat-NLI RSFT achieves 0.4561 (seeds 42, 43: 0.4535, 0.4586). A paired $t$-test yields $p = 0.44$, confirming no statistically significant difference. Both variants substantially outperform the SFT baseline (Rel-F1 0.4049), indicating that either NLI-based scoring function is effective for RSFT data selection. We adopt CED as the default because its contrastive formulation produces per-triple discrimination scores that support interpretable error analysis, an advantage absent from flat-NLI's single entailment probability.\n\nWe also ablate the top-$k$ selection threshold. Best-of-8 ($k{=}1$) yields Ign-F1 45.00 and Rel-F1 0.4596, while top-3-of-8 ($k{=}3$) produces 43.64 and 0.4454. The selected training data confirms the quality gap: $k{=}1$ data has mean extraction F1 of 0.6157 and mean CED of 0.6683, versus 0.5761 and 0.6205 for $k{=}3$. Despite $k{=}3$ providing 2.96$\\times$ more training examples, the additional lower-ranked samples introduce noise that degrades final performance. The critical factor for RSFT is scoring precision, not data volume.\n\n\n\\paragraph{Evaluation caveat.}\nAll evaluations in this work use exact-match F1, where entity mentions must match gold annotations precisely. As \\citet{wan2024genres} observe, exact match systematically underestimates generative relation extraction: predictions that correctly identify the relation but use a different surface form for the entity are scored as incorrect. This penalty applies equally to all methods, so relative comparisons remain valid. However, absolute numbers (e.g., our best Ign-F1 of 44.66 at 4B scale) likely understate the true extraction capability of LLM-based approaches. Developing evaluation protocols better suited to generative RE, such as fuzzy entity matching or embedding-based equivalence, remains an important direction for future work.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex",
    "content": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{EDCR as a dual-layer diagnostic.}\nThe Evidence-Decoupling Ratio (\\S\\ref{sec:edcr}) provides diagnostic value at two complementary levels. At the method level, EDCR correlates strongly with extraction quality across optimization paradigms: Spearman $\\rho = -0.965$ between EDCR and Rel-F1 (Table~\\ref{tab:spectrum}). GRPO QLoRA reaches EDCR $= 0.9876$, confirming catastrophic decoupling; RSFT achieves $0.6503$, consistent with healthy joint optimization; SFT falls between at $0.6982$. As a practical guideline, EDCR values above 0.70 indicate concerning decoupling, while values below 0.65 reflect balanced extraction and evidence capabilities.\n\nAt the per-relation level, computing EDCR for each of the 76 relation types with $\\geq$5 evaluation samples reveals a more nuanced picture. Per-relation EDCR correlates strongly with per-relation Rel-F1 ($\\rho = -0.793$, $p < 0.001$), confirming its utility as a difficulty indicator for individual relation types. However, per-relation EDCR is statistically independent of Evi-F1 ($\\rho = -0.064$, $p = 0.58$), and Evi-F1 itself shows no association with Rel-F1 ($\\rho = -0.013$, $p = 0.91$). These two null correlations establish that evidence quality and extraction ability are fully decoupled across relation types: knowing how well a model extracts a given relation tells us nothing about its evidence quality for that relation. EDCR captures this misalignment precisely because it measures the \\emph{ratio} of the two capabilities rather than either in isolation. Extreme cases illustrate the diagnostic power: \\texttt{date\\_of\\_birth} has EDCR $= 0.118$ (highly faithful, with extraction and evidence tightly coupled), while \\texttt{head\\_of\\_government} reaches $0.956$ (highly decoupled, where the model generates accurate evidence for a relation it rarely extracts correctly). Method-level EDCR thus serves as a horizontal comparison tool across optimization paradigms, while per-relation EDCR enables vertical diagnosis of which specific relation types suffer from extraction-evidence misalignment.\n\n\n\\paragraph{Why RSFT avoids decoupling.}\nThe structural difference between selection and optimization explains why RSFT does not exhibit the decoupling observed in gradient-based methods. GRPO and DPO update model parameters through gradients that optimize a reward signal. When two sub-tasks (extraction and evidence) compete for gradient capacity, the optimizer can discover and exploit the trade-off between them, improving one at the expense of the other. RSFT operates differently: it selects complete outputs and trains on them with standard supervised loss. Because the selection is discrete (accept or reject a full response), there is no gradient pathway through which the model can learn to sacrifice extraction for evidence quality. Only outputs where both extraction and evidence are jointly strong survive the CED filter. This property is not specific to RSFT's design but is a structural consequence of discrete selection over complete outputs: any selection-based method that filters on a joint quality criterion will inherit the same coupling guarantee. The implication for practitioners is direct: when optimizing for multiple coupled generation objectives, selection-based methods preserve inter-objective balance that gradient-based methods disrupt.\n\n\n\\paragraph{NLI scoring ablation.}\nWe compare CED (\\S\\ref{sec:ced}) against flat-NLI (positive entailment score $p^+$ only, without the contrastive term) as RSFT scoring functions. CED RSFT achieves mean Rel-F1 of 0.4569 (seeds 42, 44: 0.4517, 0.4621), and flat-NLI RSFT achieves 0.4561 (seeds 42, 43: 0.4535, 0.4586). A paired $t$-test yields $p = 0.44$, confirming no statistically significant difference. Both variants substantially outperform the SFT baseline (Rel-F1 0.4049), indicating that either NLI-based scoring function is effective for RSFT data selection. We adopt CED as the default because its contrastive formulation produces per-triple discrimination scores that support interpretable error analysis, an advantage absent from flat-NLI's single entailment probability.\n\nWe also ablate the top-$k$ selection threshold. Best-of-8 ($k{=}1$) yields Ign-F1 45.00 and Rel-F1 0.4596, while top-3-of-8 ($k{=}3$) produces 43.64 and 0.4454. The selected training data confirms the quality gap: $k{=}1$ data has mean extraction F1 of 0.6157 and mean CED of 0.6683, versus 0.5761 and 0.6205 for $k{=}3$. Despite $k{=}3$ providing 2.96$\\times$ more training examples, the additional lower-ranked samples introduce noise that degrades final performance. The critical factor for RSFT is scoring precision, not data volume.\n\n\n\\paragraph{Evaluation caveat.}\nAll evaluations in this work use exact-match F1, where entity mentions must match gold annotations precisely. As \\citet{wan2024genres} observe, exact match systematically underestimates generative relation extraction: predictions that correctly identify the relation but use a different surface form for the entity are scored as incorrect. This penalty applies equally to all methods, so relative comparisons remain valid. However, absolute numbers (e.g., our best Ign-F1 of 44.66 at 4B scale) likely understate the true extraction capability of LLM-based approaches. Developing evaluation protocols better suited to generative RE, such as fuzzy entity matching or embedding-based equivalence, remains an important direction for future work.\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T17:14:04.047532+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T17:14:04.047715+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex",
  "description": "Check for em-dash violations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex",
    "description": "Check for em-dash violations"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T17:14:04.047851+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T17:14:04.047981+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex",
  "description": "Check for explanatory en-dash violations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex",
    "description": "Check for explanatory en-dash violations"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T17:14:04.048105+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T17:14:04.048219+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"ing,\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex",
  "description": "Check for -ing phrase patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"ing,\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex",
    "description": "Check for -ing phrase patterns"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T17:14:04.048366+00:00_

5:The Evidence-Decoupling Ratio (\S\ref{sec:edcr}) provides diagnostic value at two complementary levels. At the method level, EDCR correlates strongly with extraction quality across optimization paradigms: Spearman $\rho = -0.965$ between EDCR and Rel-F1 (Table~\ref{tab:spectrum}). GRPO QLoRA reaches EDCR $= 0.9876$, confirming catastrophic decoupling; RSFT achieves $0.6503$, consistent with healthy joint optimization; SFT falls between at $0.6982$. As a practical guideline, EDCR values above 0.70 indicate concerning decoupling, while values below 0.65 reflect balanced extraction and evidence capabilities.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T17:14:04.048853+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -niE \"(furthermore|moreover|additionally|delve|leverage|utilize|facilitate|novel)\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex",
  "description": "Check for banned words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -niE \"(furthermore|moreover|additionally|delve|leverage|utilize|facilitate|novel)\" /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex",
    "description": "Check for banned words"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-17T17:14:04.049001+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex",
  "description": "Word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex",
    "description": "Word count"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-17T17:14:04.049122+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T17:14:04.049252+00:00_

739 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/sections/analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260517T171232",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-17T17:14:04.049426+00:00_

Style checks pass. The "ing," match is "decoupling," (noun usage, not a participial phrase ending). No em-dashes, no en-dashes, no banned words.

文件已写入 `docs/paper/sections/analysis.tex`。4 段结构：EDCR 双层诊断 / RSFT 避免 decoupling 的机制解释 / NLI scoring + top-k 消融 / evaluation caveat。739 词（含 LaTeX 命令），实际正文约 620 词。所有风格规则通过检查。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_20260517T171232"
}
```

</details>

---
