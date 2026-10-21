# paper writing

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_paper_writing_20260521T203945.jsonl`
- **Structured JSON:** [`ef0a406a994479a08f1f.json`](../../sessions/ef/ef0a406a994479a08f1f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-21T20:44:26.280671+00:00_

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
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T20:44:26.281207+00:00_

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
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T20:44:26.281425+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-writing.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-writing.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T20:44:26.281721+00:00_

1	---
2	name: LLM Evaluation Variance — Writing Patterns
3	description: Narrative strategies, figure/table conventions from LLM evaluation variance papers (8 deep-read, 2024-2026)
4	type: writing
5	source_papers: 8
6	---
7	
8	## Story Types
9	
10	- **Breaking limitations** (3/8): Brittlebench, Yuan, ThinkingMachines. "Everyone assumed X, we show it fails." High.
11	- **Simplification** (2/8): Hua, GeneralizIT. "Complex problem, simpler real answer." Medium.
12	- **Unifying framework** (2/8): Kunievsky, Messina. "Scattered observations, one formalism." Medium.
13	- **Cross-domain transfer** (1/8): Mesting (psychometrics→ML). Our paper fits this type — study Mesting's structure. Low but critical.
14	
15	## Hook: Counter-Intuitive Claim Dominates (4/8, high)
16	
17	"Greedy≠deterministic" (Yuan), "80/1000 unique at T=0" (ThinkingMachines), "sensitivity is artifact" (Hua), "95% CIs→79% coverage" (Mesting). **Pattern**: open with a concrete number violating expectations. Avoid vague "X is important."
18	
19	## Tension: "Everyone's Doing It Wrong" (4/8, high)
20	
21	(1) Cite widespread practice, (2) quantified evidence it fails, (3) identify overlooked factor. ThinkingMachines adds a twist: debunk the accepted explanation before presenting the correct one.
22	
23	## Intro: 4 Paragraphs + 3 Contributions (mode)
24	
25	(1) Context, (2) existing approaches + limitation, (3) gap/surprise, (4) contributions. 3 contributions standard: framework + empirical finding + practical tool. **Support: 5/8, high.**
26	
27	## Figure Conventions
28	
29	**Figure 1**: problem_illustration (4/8) — show problem exists before solution. Concrete examples with before/after or divergence visualization. **High.**
30	
31	**Result figures**: bar charts primary (5/8); stacked bars for variance decomposition (2/8, Mesting/Brittlebench — expected idiom for our paper); line plots for trends (3/8); heatmaps for divergence (2/8). **High.**
32	
33	**Figure count**: 4-6 total. **Flow**: problem illustration →
…[truncated 1032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T20:44:26.281870+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T20:44:26.282056+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Generalizability Theory}
5	\label{sec:gtheory}
6	
7	Generalizability theory (G-theory) treats each measurement as one observation from a universe of admissible conditions defined by the crossed facets of an evaluation design \cite{shavelson1991generalizability, brennan2001generalizability}. The \emph{object of measurement} is the entity whose consistency is of interest. In our setting, test items ($p$) serve as the object of measurement, and the goal is to determine how reliably item-level scores generalize across the methodological conditions under which they are collected.
8	
9	A \emph{G-study} decomposes total observed variance into components $\sigma^2_x$ for each facet $x$ and their interactions. Each component quantifies how much variability that source contributes to the overall measurement. Large interaction components (e.g., $\sigma^2_{pM}$ for item-by-model) indicate that facets do not affect items uniformly but instead create differential difficulty profiles. We estimate variance components via Henderson Method~I, an unbiased ANOVA-based estimator for balanced designs \cite[Ch.~3]{brennan2001generalizability}, with 1,000-resample bootstrap confidence intervals \cite{li2023bootstrap}.
10	
11	A \emph{D-study} projects the generalizability coefficient under hypothetical designs with different numbers of conditions per facet:
12	\begin{equation}
13	G_\text{item} = \frac{\sigma^2_p}{\sigma^2_p + \sigma^2_\text{rel}}
14	\label{eq:gcoeff}
15	\end{equation}
16	where $\sigma^2_\text{rel}$ aggregates all item-by-facet interaction variances, each divided by the number of conditions for the corresponding facets \cite[Ch.~4]{brennan2001generalizability}. This prospective capability distinguishes G-theory from classical ANOVA: rather than only attributing variance post hoc, a D-study enables optimization of evaluation designs \emph{before} data collection \cite{shavelson1989gtheory}. Throughout this paper, we use
…[truncated 8643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T20:44:26.282203+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T20:44:26.282456+00:00_

1	\section{Experiments}
2	
3	We apply the G-theory framework from Section~3 to a fully crossed evaluation design spanning multiple models, benchmarks, and methodological facets. All experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on NVIDIA RTX PRO 6000 GPUs (96GB). Binary correctness (1/0) serves as the primary outcome measure throughout; generation-based scoring avoids the log-likelihood artifacts identified by \citet{hua2025flaw}.
4	
5	\subsection{Single-Model Baseline}
6	
7	We first establish the variance structure within a single model (Llama-3.1-8B-Instruct) on MMLU to isolate methodological facet contributions before introducing cross-model variation.
8	
9	\paragraph{Design.} The G-study crosses six facets: 200 items $\times$ 3 numerical precisions (BF16, FP16, FP32) $\times$ 6 prompt templates $\times$ 6 random seeds $\times$ 3 temperature levels (0.0, 0.3, 0.7) $\times$ 4 answer orderings, yielding 239,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).
10	
11	\paragraph{Results.} Under binary scoring, item difficulty (\texttt{item\_id}) accounts for 61.1\% of total variance, with the residual term contributing 19.5\%. All main facet effects are negligible ($<$1\% each): prompt template 0.3\%, temperature 0.2\%, precision 0.1\%, seed $<$0.1\%, ordering $<$0.1\%. The interesting structure appears in item-conditional interactions: precision$\times$item contributes 7.2\%, temperature$\times$item 6.9\%, and prompt$\times$item 5.7\%. This pattern indicates that methodological choices do not shift performance uniformly across items; instead, specific items are differentially sensitive to specific facets.
12	
13	The resulting generalizability coefficient is $G_\text{item} = 0.918$, indicating that 200 items under multi-facet conditions produce highly reliable rankings. A D-study projection shows $G \geq 0.80$ is achievable with as few as 72 items in thi
…[truncated 12502 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T20:44:26.282786+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T20:44:26.282927+00:00_

aaai2026.bst
aaai2026.sty
experiments.tex
main.tex
method.tex
references.bib
sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T20:44:26.283053+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T20:44:26.283186+00:00_

1	\def\aaaianonymous{true}
2	\documentclass[letterpaper]{article}
3	\ifdefined\aaaianonymous
4	    \usepackage[submission]{aaai2026}
5	\else
6	    \usepackage{aaai2026}
7	\fi
8	\usepackage{times}
9	\usepackage{helvet}
10	\usepackage{courier}
11	\usepackage[hyphens]{url}
12	\usepackage{graphicx}
13	\urlstyle{rm}
14	\def\UrlFont{\rm}
15	\usepackage{natbib}
16	\usepackage{caption}
17	\frenchspacing
18	\setlength{\pdfpagewidth}{8.5in}
19	\setlength{\pdfpageheight}{11in}
20	\usepackage{amsmath,amssymb}
21	\usepackage{booktabs}
22	\usepackage{multirow}
23	\usepackage{xcolor}
24	\graphicspath{{../../figures/paper/}}
25	
26	\pdfinfo{
27	/TemplateVersion (2026.1)
28	}
29	
30	\setcounter{secnumdepth}{0}
31	
32	\ifdefined\aaaianonymous
33	    \title{Format-Conditional Variance Structure in LLM Evaluation:\\A Generalizability Theory Approach}
34	    \author{Anonymous Submission}
35	    \affiliations{}
36	\else
37	    \title{Format-Conditional Variance Structure in LLM Evaluation:\\A Generalizability Theory Approach}
38	    \author{Anonymous}
39	    \affiliations{}
40	\fi
41	
42	\begin{document}
43	\maketitle
44	
45	\begin{abstract}
46	% [PLACEHOLDER: Abstract - to be written in Step 4]
47	\end{abstract}
48	
49	% === INTRODUCTION ===
50	\section{Introduction}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T20:44:26.283312+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex",
  "offset": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex",
    "offset": "50"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T20:44:26.283453+00:00_

50	\section{Introduction}
51	% [PLACEHOLDER: Introduction - to be written in Step 4]
52	
53	% === RELATED WORK ===
54	\section{Related Work}
55	% [PLACEHOLDER: Related Work - to be written in Step 4]
56	
57	% === METHOD ===
58	\input{method}
59	
60	% === EXPERIMENTS ===
61	\input{experiments}
62	
63	% === CONCLUSION ===
64	\section{Conclusion}
65	% [PLACEHOLDER: Conclusion - to be written in Step 4]
66	
67	% === LIMITATIONS ===
68	\section{Limitations}
69	% [PLACEHOLDER: Limitations - brief, ~3 points per EMNLP rule]
70	
71	\bibliography{references}
72	
73	\end{document}
74	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T20:44:26.283620+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nOn multiple-choice benchmarks, item selection drives 42--49\\% of evaluation variance while prompt wording is negligible ($<$1\\%). On the free-form reasoning task GSM8K, prompt wording alone accounts for 12\\%, more than item selection. These numbers, drawn from our factorial analysis of 1.27 million evaluation records across four benchmarks, reveal that the variance structure of LLM evaluation is not a fixed property of the pipeline but shifts qualitatively with the response format. Current evaluation practice treats variance sources as independent nuisance factors and controls them one at a time: one study perturbs prompts, another varies precision, a third changes item subsets. This piecemeal approach cannot capture interactions between sources, nor can it predict how the relative importance of each source changes across evaluation settings. Leaderboard rankings built on single-condition evaluations are therefore sensitive to methodological choices that remain unreported and uncontrolled \\citep{rodriguez2021leaderboards, dehghani2021benchmark}. No unified factorial framework exists to decompose these sources simultaneously, quantify their interactions, and compare the resulting variance structure across benchmarks.\n\nExisting studies have examined individual variance sources in isolation, each implicitly assuming separability. \\citet{sclar2024formatting} documented up to 76\\% accuracy swings from prompt formatting perturbations but held hardware and item selection fixed. BrittleBench \\citep{brittlebench2026} found 50\\% variance from prompt perturbation under the same constraint. \\citet{yuan2025layercast} showed that numerical precision and GPU type cause up to 9\\% accuracy variation but provided no factorial attribution to specific sources or their interactions. \\citet{mesting2026hidden} applied Generalizability theory (G-theory) to LLM evaluation and decomposed variance across five methodology facets on a single benchmark; judge identity dominated at 43.8\\%, but the study included no cross-benchmark comparison and excluded infrastructure facets such as numerical precision. Studies of answer ordering \\citep{pezeshkpour2024ordering} and hyperparameter sensitivity \\citep{dodge2020finetuning, henderson2018deep} have documented additional sources of variation, again in isolation from the factors above. Item Response Theory (IRT) approaches \\citep{polo2024tinybenchmarks, lalor2019irt} model item difficulty parameters to construct efficient benchmarks but do not account for prompt, seed, or ordering facets. \\citet{bouthillier2021accounting} established ANOVA-based variance decomposition as a principled template for ML reproducibility, but this work predates the LLM evaluation context where benchmark format introduces an additional structural variable. Three gaps remain: no study has (a) crossed infrastructure and methodology facets in a unified factorial design, (b) compared the resulting variance structure across benchmarks and response formats, or (c) translated variance components into design-dependent reproducibility budgets.\n\nWe address these gaps with a multi-benchmark G-theory study \\citep{shavelson1991generalizability, brennan2001generalizability} that crosses seven facets (item, model, numerical precision, prompt template, random seed, sampling temperature, and answer ordering) across four models and four benchmarks (MMLU, ARC-Challenge, HellaSwag, and GSM8K), totaling 1.27 million records. The central finding is that variance structure is format-conditional. All three multiple-choice benchmarks share an item-dominated structure: item selection accounts for 42--49\\% of total variance (MMLU 42\\%, ARC 49\\%, HellaSwag 45\\%), with model$\\times$item interaction as the second-largest source at 32--38\\%. GSM8K exhibits a qualitatively different profile: model (15\\%), prompt template (12\\%), and item (12\\%) contribute comparable shares, with no single dominant source. This is a dichotomy, not a gradient. The 30-percentage-point gap between the lowest MC item dominance (42\\%) and GSM8K (12\\%) reflects a structural shift in what drives evaluation reliability. In multiple-choice settings, the item pool determines measurement reliability; in free-form settings, prompt design and model selection dominate. A second finding is that model$\\times$item interaction (33.6\\% in cross-model MMLU analysis) is the hidden second-largest variance source, larger than all methodology main effects combined. Models differ not in overall ability but in which specific items they find difficult. D-study projections translate these findings into practical design guidance: the format-conditional structure implies that reliability optimization strategies must differ between MC and free-form benchmarks. Figure~\\ref{fig:cross_benchmark} visualizes the contrast across all four benchmarks.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item \\textbf{Format-conditional variance structure.} We show that the dominant variance source reverses between response formats: item selection dominates multiple-choice benchmarks (42--49\\%) while model and prompt dominate free-form generation. Model$\\times$item interaction (33.6\\%) is the hidden second-largest source in cross-model analysis. D-study cross-validation confirms the structure (predicted $G = 0.816$, observed $G = 0.820$).\n\n    \\item \\textbf{Precision separability.} Under binary scoring, BF16 and FP16 yield functionally identical results ($<$0.1\\% interaction with all other facets). This separability is metric-conditional: text-exact-match scoring reveals a 1.3\\% precision$\\times$temperature interaction absent under binary scoring.\n\n    \\item \\textbf{Design-dependent reproducibility budgets.} Multi-facet evaluation designs require $8.8\\times$ fewer items than single-condition designs to achieve $G \\geq 0.80$ (72 versus 631 items). IRT-selected 116-item subsets yield $G = 0.424$ under single-condition protocols, which confirms that item quality and evaluation design improve reliability through orthogonal mechanisms.\n\n    \\item \\textbf{Open-source G-theory pipeline and D-study calculator.} We release a variance decomposition toolkit and D-study budget calculator for LLM evaluation. Practitioners can compute the number of items, models, and conditions needed for a target reliability before data collection.\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nOn multiple-choice benchmarks, item selection drives 42--49\\% of evaluation variance while prompt wording is negligible ($<$1\\%). On the free-form reasoning task GSM8K, prompt wording alone accounts for 12\\%, more than item selection. These numbers, drawn from our factorial analysis of 1.27 million evaluation records across four benchmarks, reveal that the variance structure of LLM evaluation is not a fixed property of the pipeline but shifts qualitatively with the response format. Current evaluation practice treats variance sources as independent nuisance factors and controls them one at a time: one study perturbs prompts, another varies precision, a third changes item subsets. This piecemeal approach cannot capture interactions between sources, nor can it predict how the relative importance of each source changes across evaluation settings. Leaderboard rankings built on single-condition evaluations are therefore sensitive to methodological choices that remain unreported and uncontrolled \\citep{rodriguez2021leaderboards, dehghani2021benchmark}. No unified factorial framework exists to decompose these sources simultaneously, quantify their interactions, and compare the resulting variance structure across benchmarks.\n\nExisting studies have examined individual variance sources in isolation, each implicitly assuming separability. \\citet{sclar2024formatting} documented up to 76\\% accuracy swings from prompt formatting perturbations but held hardware and item selection fixed. BrittleBench \\citep{brittlebench2026} found 50\\% variance from prompt perturbation under the same constraint. \\citet{yuan2025layercast} showed that numerical precision and GPU type cause up to 9\\% accuracy variation but provided no factorial attribution to specific sources or their interactions. \\citet{mesting2026hidden} applied Generalizability theory (G-theory) to LLM evaluation and decomposed variance across five methodology facets on a single benchmark; judge identity dominated at 43.8\\%, but the study included no cross-benchmark comparison and excluded infrastructure facets such as numerical precision. Studies of answer ordering \\citep{pezeshkpour2024ordering} and hyperparameter sensitivity \\citep{dodge2020finetuning, henderson2018deep} have documented additional sources of variation, again in isolation from the factors above. Item Response Theory (IRT) approaches \\citep{polo2024tinybenchmarks, lalor2019irt} model item difficulty parameters to construct efficient benchmarks but do not account for prompt, seed, or ordering facets. \\citet{bouthillier2021accounting} established ANOVA-based variance decomposition as a principled template for ML reproducibility, but this work predates the LLM evaluation context where benchmark format introduces an additional structural variable. Three gaps remain: no study has (a) crossed infrastructure and methodology facets in a unified factorial design, (b) compared the resulting variance structure across benchmarks and response formats, or (c) translated variance components into design-dependent reproducibility budgets.\n\nWe address these gaps with a multi-benchmark G-theory study \\citep{shavelson1991generalizability, brennan2001generalizability} that crosses seven facets (item, model, numerical precision, prompt template, random seed, sampling temperature, and answer ordering) across four models and four benchmarks (MMLU, ARC-Challenge, HellaSwag, and GSM8K), totaling 1.27 million records. The central finding is that variance structure is format-conditional. All three multiple-choice benchmarks share an item-dominated structure: item selection accounts for 42--49\\% of total variance (MMLU 42\\%, ARC 49\\%, HellaSwag 45\\%), with model$\\times$item interaction as the second-largest source at 32--38\\%. GSM8K exhibits a qualitatively different profile: model (15\\%), prompt template (12\\%), and item (12\\%) contribute comparable shares, with no single dominant source. This is a dichotomy, not a gradient. The 30-percentage-point gap between the lowest MC item dominance (42\\%) and GSM8K (12\\%) reflects a structural shift in what drives evaluation reliability. In multiple-choice settings, the item pool determines measurement reliability; in free-form settings, prompt design and model selection dominate. A second finding is that model$\\times$item interaction (33.6\\% in cross-model MMLU analysis) is the hidden second-largest variance source, larger than all methodology main effects combined. Models differ not in overall ability but in which specific items they find difficult. D-study projections translate these findings into practical design guidance: the format-conditional structure implies that reliability optimization strategies must differ between MC and free-form benchmarks. Figure~\\ref{fig:cross_benchmark} visualizes the contrast across all four benchmarks.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item \\textbf{Format-conditional variance structure.} We show that the dominant variance source reverses between response formats: item selection dominates multiple-choice benchmarks (42--49\\%) while model and prompt dominate free-form generation. Model$\\times$item interaction (33.6\\%) is the hidden second-largest source in cross-model analysis. D-study cross-validation confirms the structure (predicted $G = 0.816$, observed $G = 0.820$).\n\n    \\item \\textbf{Precision separability.} Under binary scoring, BF16 and FP16 yield functionally identical results ($<$0.1\\% interaction with all other facets). This separability is metric-conditional: text-exact-match scoring reveals a 1.3\\% precision$\\times$temperature interaction absent under binary scoring.\n\n    \\item \\textbf{Design-dependent reproducibility budgets.} Multi-facet evaluation designs require $8.8\\times$ fewer items than single-condition designs to achieve $G \\geq 0.80$ (72 versus 631 items). IRT-selected 116-item subsets yield $G = 0.424$ under single-condition protocols, which confirms that item quality and evaluation design improve reliability through orthogonal mechanisms.\n\n    \\item \\textbf{Open-source G-theory pipeline and D-study calculator.} We release a variance decomposition toolkit and D-study budget calculator for LLM evaluation. Practitioners can compute the number of items, models, and conditions needed for a target reliability before data collection.\n\\end{enumerate}\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T20:44:26.283801+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T20:44:26.283937+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper && grep -n \"—\" introduction.tex; echo \"---em-dash check done---\" && grep -n \" – \" introduction.tex; echo \"---en-dash check done---\" && grep -cn \"ing,\" introduction.tex; echo \"---ing-comma check done---\"",
  "description": "Check for prohibited em-dashes, en-dashes, and -ing patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper && grep -n \"—\" introduction.tex; echo \"---em-dash check done---\" && grep -n \" – \" introduction.tex; echo \"---en-dash check done---\" && grep -cn \"ing,\" introduction.tex; echo \"---ing-comma check done---\"",
    "description": "Check for prohibited em-dashes, en-dashes, and -ing patterns"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T20:44:26.284058+00:00_

---em-dash check done---
---en-dash check done---
2
---ing-comma check done---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T20:44:26.284172+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*\\[[^]]*\\]//g; s/\\\\[a-zA-Z]*//g; s/{//g; s/}//g; s/\\$[^$]*\\$//g; s/%.*//g; s/~/ /g' | wc -w",
  "description": "Count approximate word count excluding LaTeX commands"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*\\[[^]]*\\]//g; s/\\\\[a-zA-Z]*//g; s/{//g; s/}//g; s/\\$[^$]*\\$//g; s/%.*//g; s/~/ /g' | wc -w",
    "description": "Count approximate word count excluding LaTeX commands"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T20:44:26.284284+00:00_

186

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T20:44:26.284422+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex | perl -pe 's/\\\\\\\\//g; s/\\\\[a-zA-Z]+(\\{[^}]*\\}|\\[[^\\]]*\\])*/\\n/g; s/\\$[^$]*\\$//g; s/[{}~%]/ /g' | wc -w",
  "description": "Better word count excluding LaTeX markup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex | perl -pe 's/\\\\\\\\//g; s/\\\\[a-zA-Z]+(\\{[^}]*\\}|\\[[^\\]]*\\])*/\\n/g; s/\\$[^$]*\\$//g; s/[{}~%]/ /g' | wc -w",
    "description": "Better word count excluding LaTeX markup"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T20:44:26.284542+00:00_

Unmatched [ in regex; marked by <-- HERE in m/\$[ <-- HERE ^5.040001*\$/ at -e line 1, <> line 1.
0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T20:44:26.284650+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T20:44:26.284767+00:00_

6:[Omitted long matching line]
14:    \item \textbf{Precision separability.} Under binary scoring, BF16 and FP16 yield functionally identical results ($<$0.1\% interaction with all other facets). This separability is metric-conditional: text-exact-match scoring reveals a 1.3\% precision$\times$temperature interaction absent under binary scoring.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T20:44:26.284878+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex | tr -d '\\\\{}$~%' | sed 's/[a-z]*{[^}]*}//g' | wc -w",
  "description": "Approximate word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex | tr -d '\\\\{}$~%' | sed 's/[a-z]*{[^}]*}//g' | wc -w",
    "description": "Approximate word count"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T20:44:26.284984+00:00_

784

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T20:44:26.285123+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex",
  "old_string": "% === INTRODUCTION ===\n\\section{Introduction}\n% [PLACEHOLDER: Introduction - to be written in Step 4]",
  "new_string": "% === INTRODUCTION ===\n\\input{introduction}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex",
    "old_string": "% === INTRODUCTION ===\n\\section{Introduction}\n% [PLACEHOLDER: Introduction - to be written in Step 4]",
    "new_string": "% === INTRODUCTION ===\n\\input{introduction}"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T20:44:26.285251+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260521T203945",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-21T20:44:26.285423+00:00_

Introduction 已写入 `introduction.tex` 并在 `main.tex` 中替换了占位符。

文件结构：4 段 + enumerate 贡献列表，约 850 words。所有关键数字与 experiments.tex 一致（item 42--49%, model×item 33.6%, G=0.820, 8.8× efficiency gap, BF16≈FP16 <0.1%, precision×temperature 1.3%）。无 em-dash、无 -ing 尾句、无 AI 风格词汇。引用了 14 个 citation keys。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_20260521T203945"
}
```

</details>

---
