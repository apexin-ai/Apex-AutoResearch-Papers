# paper writing method

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_paper_writing_method_20260514T194021.jsonl`
- **Structured JSON:** [`a07df651ac121ec10d2c.json`](../../sessions/a0/a07df651ac121ec10d2c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-14T19:41:45.720156+00:00_

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
  "session": "worker_paper_writing_method_20260514T194021",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T19:41:45.720731+00:00_

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
  "session": "worker_paper_writing_method_20260514T194021",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T19:41:45.721182+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260514T194021",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T19:41:45.721509+00:00_

1	---
2	name: red-section
3	description: "当实验结论为 negative / 审稿人指出 core claim 不成立 / 你要写或修改任何 paper/**/*.md 或 .tex 文件时,立即使用本 skill。提供 Framing 调整提案模板、写作规范、审稿攻击面预演。违反即被 Reviewer critical 打回。"
4	always: true
5	roles:
6	  - agent
7	---
8	
9	# Red Section — Narrative Re-framing
10	
11	## 什么时候用
12	- 实验 conclusion = negative
13	- 审稿人指出 core claim 不成立
14	- 写论文前（作为通用写作规范）
15	
16	## Negative 结果的正确心态
17	"不是失败，是发现了 X"。你的输出应该是 framing 调整提案，而不是 failure report。
18	
19	## 产出格式
20	
21	### Framing 调整提案模板
22	1. 原 claim：什么
23	2. 实验结果：什么（客观数字，不加修饰）
24	3. 重新审视：
25	   - 这个结果挑战了哪个 hypothesis？
26	   - 是否暴露了被忽略的变量？
27	   - 在新的 framing 下，哪些已做实验依然有效？哪些要补？
28	4. 新的 narrative 骨架（3 种备选，供 Director 选）
29	5. 对论文各章节的影响（abstract / intro / method / experiments / discussion / conclusion 逐一评估）
30	6. 建议下一步实验（必须至少 3 组备选，填新 framing 下的矩阵空格）
31	
32	### 写作规范（所有写作场景通用）
33	- 禁止 cherry-picking
34	- 所有数字必须追溯到 registry
35	- 强度与 evidence 匹配（1 个数据集 → 不能说 "consistently"）
36	- 每个定量 claim 必须附 exp_id
37	- 限制强度词（"significantly" 必须有统计检验）
38	
39	### 审稿攻击面预演
40	- 这个 section 最容易被审稿人攻击的点
41	- 预写 rebuttal 要点
42	
43	## 输出给谁
44	- Framing 调整提案 → Main Agent 向 Director 汇报
45	- 写作 skill 合规检查 → Reviewer 审查时验证
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260514T194021",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T19:41:45.721670+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260514T194021",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T19:41:45.721798+00:00_

docs/paper/references.bib
docs/paper/acl.sty
docs/paper/acl_natbib.bst
docs/paper/figures/fig_overview.pdf
docs/paper/figures/fig_selection_gap.pdf
docs/paper/figures/fig_signal_heatmap.pdf
docs/paper/figures/fig_reliability.pdf
docs/paper/main.tex
docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260514T194021",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T19:41:45.721941+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260514T194021",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T19:41:45.722070+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260514T194021",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T19:41:45.722229+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260514T194021",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T19:41:45.722455+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances from scientific abstracts annotated for joint NER (6 entity types) and RE (7 relation types), representing a complex schema with overlapping structures.
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences from newswire with 4 entity types, serving as a high-accuracy benchmark where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 test instances from social media with emerging entities, used to probe method boundaries where model capability is insufficient.
12	This gradient---from near-solved (CoNLL) through challenging (SciERC) to infeasible (WNUT-17)---enables systematic characterization of how signal effectiveness varies with task difficulty (\S\ref{sec:complexity_robustness}).
13	
14	\paragraph{Models.}
15	Our primary model is \textbf{Qwen3-8B}, fine-tuned with LoRA ($r{=}32$) separately per dataset.
16	For cross-model validation, we evaluate \textbf{LLaMA-3.1-8B-Instruct} to assess whether structural confidence signals transfer across architectures and training regimes.
17	
18	\paragraph{Sampling and Evaluation.}
19	For each test instance, we draw $N$ independent samples at temperature $T{=}1.0$, with $T{=}0.7$ for robustness analysis.
20	We use $N{=}8$ for both SciERC and CoNLL in the primary evaluation, and $N{=}16$ for SciERC scaling experiments.
21	Quality estimation is measured along two axes: \textit{rank correlation} with instance-level F1 via Spearman $\rho$ and Kendall $\tau$, and \textit{binary discrimination} via AUROC (instances above vs.\ below median F1).
22	Downstream utility is assessed through \textbf{best-of-$N$ selection F1}: the F1 obtained when each signal selects one sample per instan
…[truncated 16805 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260514T194021",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T19:41:45.722604+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260514T194021",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T19:41:45.722837+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	% SUPPLEMENTARY — not cited in main text
12	@article{bates2021rcps,
13	  title = {Distribution-free, Risk-controlling Prediction Sets},
14	  author = {Bates, Stephen and Angelopoulos, Anastasios and Lei, Lihua and Malik, Jitendra and Jordan, Michael},
15	  journal = {Journal of the ACM},
16	  year = {2021},
17	  doi = {10.1145/3478535},
18	  url = {http://dx.doi.org/10.1145/3478535}
19	}
20	
21	@article{brown2024monkeys,
22	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
23	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
24	  journal = {arXiv preprint arXiv:2407.21787},
25	  year = {2024},
26	  url = {https://arxiv.org/abs/2407.21787}
27	}
28	
29	@inproceedings{chen2024usc,
30	  title = {Universal Self-Consistency for Large Language Model Generation},
31	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
32	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
33	  year = {2024},
34	  url = {https://arxiv.org/abs/2311.17311}
35	}
36	
37	@article{cobbe2021verifiers,
38	  title = {Training Verifiers to Solve Math Word Problems},
39	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
40	  journal = {arXiv preprint arXiv:
…[truncated 18708 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260514T194021",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T19:41:45.723059+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
  "content": "\\section{Method}\\label{sec:method}\n\nWe present a framework for evaluating confidence signals in test-time scaling for information extraction.\nThis section formalizes the problem (\\S\\ref{sec:formulation}), defines five confidence signals spanning three families (\\S\\ref{sec:signals}), and introduces the evaluation protocol (\\S\\ref{sec:evaluation}).\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven a language model $\\mathcal{M}$ and an input instance $x$, we independently sample $N$ structured outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$.\nEach $y_i$ is a structured extraction result---an entity set for NER or a relation set for RE---produced via constrained decoding \\cite{willard2023guided} to ensure valid output structure.\nOur goal is to define a confidence signal $c$ that serves two purposes: (a) \\textit{quality estimation}---predicting which instances the model handles reliably, and (b) \\textit{sample selection}---identifying the best output among the $N$ candidates.\n\nA key distinction underlies this framework.\nA \\textbf{per-sample signal} scores each $y_i$ independently, $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$, enabling direct ranking of the $N$ candidates.\nAn \\textbf{instance-level signal} aggregates over all $N$ samples, $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$, producing a single score per input.\nInstance-level signals can estimate overall prediction reliability but do not inherently rank individual samples.\nThis asymmetry---between predicting \\textit{which inputs} are easy and selecting \\textit{which output} is best---is central to the correlation-selection gap we investigate.\n\nTable~\\ref{tab:notation} summarizes our notation.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nWe compare five signals from three families: \\textit{model-internal} (log-probability), \\textit{surface} (exact match, Fleiss' $\\kappa$), and \\textit{structural} (Soft Jaccard, entity voting).\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nThe only per-sample signal in our comparison.\nFor a sample $y_i$ consisting of tokens $t_1, \\ldots, t_{|y_i|}$, we define:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{<j}, x)\n\\end{equation}\nThis is the length-normalized mean log-likelihood, reflecting the model's internal confidence in its generation.\nBecause it scores each sample independently, it can directly rank the $N$ candidates for sample selection.\n\n\\paragraph{Exact match voting (surface, instance-level).}\nFollowing self-consistency \\cite{wang2023selfconsistency}, we measure pairwise agreement across samples at the string level:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i<j} \\mathbb{1}[y_i = y_j]\n\\end{equation}\nEquivalently, this can be expressed as the majority fraction $\\max_y |\\{i : y_i = y\\}| / N$.\nEM treats entire outputs as atomic units: two samples either match exactly or not, with no notion of partial overlap.\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt the inter-rater agreement measure of \\citet{fleiss1971agreement} by treating the $N$ samples as independent annotators, token positions as items, and the token vocabulary as the set of categories:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is the observed agreement rate across token positions and $\\bar{P}_e$ is the agreement expected by chance.\nUnlike EM, FK captures partial agreement---two samples that share most tokens but differ in a few positions receive a high score.\nHowever, FK operates at the string level and does not account for the structure of the extracted output.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nOur core structural signal extends Jaccard similarity \\cite{jaccard1901distribution} to operate on extracted entity or relation \\textit{sets} rather than raw strings.\nFor two samples $y_i$ and $y_j$, we first group extractions by entity type.\nWithin each group, we compute a bipartite matching using the Hungarian algorithm with span overlap as the similarity metric.\nThe pairwise Soft Jaccard score is:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{|M|}{\\max(|A_i|, |A_j|)}\n\\end{equation}\nwhere $|M|$ is the number of matched extraction pairs and $|A_i|$, $|A_j|$ are the extraction counts of each sample.\nThe instance-level signal averages over all sample pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i<j} \\text{SJ}(y_i, y_j)\n\\end{equation}\nTwo design choices distinguish SJ from surface signals.\nFirst, type-aware grouping prevents spurious matches between extractions of different entity types.\nSecond, span-overlap matching tolerates near-synonym variations (e.g., ``machine learning'' vs.\\ ``ML''), which would be penalized by exact string comparison.\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nWhile SJ compares entire extraction sets, entity voting operates at the granularity of individual extractions.\nFor each entity $e$ appearing in the union $E_\\cup$ of all $N$ samples, we compute its frequency:\n\\begin{equation}\\label{eq:freq}\n\\text{freq}(e) = \\frac{|\\{i : e \\in y_i\\}|}{N}\n\\end{equation}\nThe instance-level confidence is the mean frequency across all observed entities:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\nThis adapts majority voting \\cite{wang2023selfconsistency} from discrete answer selection to set-valued extraction.\nEntities that appear consistently across samples contribute high frequency; hallucinated or idiosyncratic extractions that appear in only one or two samples pull the score down.\nThis per-entity granularity enables the signal to distinguish instances where the model reliably extracts a core set of entities (high $c_{\\text{vote}}$) from those where extractions vary widely across samples (low $c_{\\text{vote}}$).\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\nWe assess confidence signals along two complementary dimensions.\n\n\\paragraph{Quality estimation.}\nQuality estimation asks: \\textit{for which instances does the model produce reliable outputs?}\nWe measure rank correlation between the confidence signal and instance-level F1 via Spearman $\\rho$ and Kendall $\\tau$.\nFor binary discrimination, we compute AUROC by classifying instances as above or below median F1.\nThese metrics evaluate whether a signal can identify reliable vs.\\ unreliable predictions without access to gold labels.\n\n\\paragraph{Sample selection.}\nSample selection asks: \\textit{given $N$ candidates for a single instance, which one is best?}\nWe report best-of-$N$ F1: for each instance, the signal selects one sample, and we compute micro F1 over all instances.\nWe compare against an \\textit{oracle} (which always selects the highest-F1 sample) and a \\textit{greedy baseline} ($T{=}0$, $N{=}1$).\nPer-sample signals like log-probability directly rank the $N$ candidates.\nInstance-level signals (SJ, FK, EM, Voting) produce a single score per instance and thus require an auxiliary strategy for sample selection---we select the sample closest to the consensus output, i.e., the one with highest average pairwise similarity to all other samples.\n\n\\paragraph{The two dimensions are complementary, not redundant.}\nA signal with high rank correlation accurately predicts relative instance difficulty, making it useful for quality-aware routing or selective prediction.\nHowever, high correlation does not guarantee effective sample selection: if per-sample variance is low---the model produces $N$ similar outputs for a given input---even a perfect quality estimator cannot distinguish among near-identical candidates.\nWe investigate this decoupling empirically in \\S\\ref{sec:selection_gap}.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260514T194021",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex",
    "content": "\\section{Method}\\label{sec:method}\n\nWe present a framework for evaluating confidence signals in test-time scaling for information extraction.\nThis section formalizes the problem (\\S\\ref{sec:formulation}), defines five confidence signals spanning three families (\\S\\ref{sec:signals}), and introduces the evaluation protocol (\\S\\ref{sec:evaluation}).\n\n\\subsection{Problem Formulation}\\label{sec:formulation}\n\nGiven a language model $\\mathcal{M}$ and an input instance $x$, we independently sample $N$ structured outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$.\nEach $y_i$ is a structured extraction result---an entity set for NER or a relation set for RE---produced via constrained decoding \\cite{willard2023guided} to ensure valid output structure.\nOur goal is to define a confidence signal $c$ that serves two purposes: (a) \\textit{quality estimation}---predicting which instances the model handles reliably, and (b) \\textit{sample selection}---identifying the best output among the $N$ candidates.\n\nA key distinction underlies this framework.\nA \\textbf{per-sample signal} scores each $y_i$ independently, $c_{\\text{ps}}: (x, y_i) \\to \\mathbb{R}$, enabling direct ranking of the $N$ candidates.\nAn \\textbf{instance-level signal} aggregates over all $N$ samples, $c_{\\text{il}}: (x, \\{y_i\\}_{i=1}^N) \\to \\mathbb{R}$, producing a single score per input.\nInstance-level signals can estimate overall prediction reliability but do not inherently rank individual samples.\nThis asymmetry---between predicting \\textit{which inputs} are easy and selecting \\textit{which output} is best---is central to the correlation-selection gap we investigate.\n\nTable~\\ref{tab:notation} summarizes our notation.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\subsection{Confidence Signals}\\label{sec:signals}\n\nWe compare five signals from three families: \\textit{model-internal} (log-probability), \\textit{surface} (exact match, Fleiss' $\\kappa$), and \\textit{structural} (Soft Jaccard, entity voting).\n\n\\paragraph{Log-probability (model-internal, per-sample).}\nThe only per-sample signal in our comparison.\nFor a sample $y_i$ consisting of tokens $t_1, \\ldots, t_{|y_i|}$, we define:\n\\begin{equation}\\label{eq:logprob}\nc_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{j=1}^{|y_i|} \\log p_{\\mathcal{M}}(t_j \\mid t_{<j}, x)\n\\end{equation}\nThis is the length-normalized mean log-likelihood, reflecting the model's internal confidence in its generation.\nBecause it scores each sample independently, it can directly rank the $N$ candidates for sample selection.\n\n\\paragraph{Exact match voting (surface, instance-level).}\nFollowing self-consistency \\cite{wang2023selfconsistency}, we measure pairwise agreement across samples at the string level:\n\\begin{equation}\\label{eq:em}\nc_{\\text{em}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i<j} \\mathbb{1}[y_i = y_j]\n\\end{equation}\nEquivalently, this can be expressed as the majority fraction $\\max_y |\\{i : y_i = y\\}| / N$.\nEM treats entire outputs as atomic units: two samples either match exactly or not, with no notion of partial overlap.\n\n\\paragraph{Fleiss' $\\kappa$ (surface, instance-level).}\nWe adapt the inter-rater agreement measure of \\citet{fleiss1971agreement} by treating the $N$ samples as independent annotators, token positions as items, and the token vocabulary as the set of categories:\n\\begin{equation}\\label{eq:fk}\n\\kappa = \\frac{\\bar{P} - \\bar{P}_e}{1 - \\bar{P}_e}\n\\end{equation}\nwhere $\\bar{P}$ is the observed agreement rate across token positions and $\\bar{P}_e$ is the agreement expected by chance.\nUnlike EM, FK captures partial agreement---two samples that share most tokens but differ in a few positions receive a high score.\nHowever, FK operates at the string level and does not account for the structure of the extracted output.\n\n\\paragraph{Soft Jaccard (structural, instance-level).}\nOur core structural signal extends Jaccard similarity \\cite{jaccard1901distribution} to operate on extracted entity or relation \\textit{sets} rather than raw strings.\nFor two samples $y_i$ and $y_j$, we first group extractions by entity type.\nWithin each group, we compute a bipartite matching using the Hungarian algorithm with span overlap as the similarity metric.\nThe pairwise Soft Jaccard score is:\n\\begin{equation}\\label{eq:sj}\n\\text{SJ}(y_i, y_j) = \\frac{|M|}{\\max(|A_i|, |A_j|)}\n\\end{equation}\nwhere $|M|$ is the number of matched extraction pairs and $|A_i|$, $|A_j|$ are the extraction counts of each sample.\nThe instance-level signal averages over all sample pairs:\n\\begin{equation}\\label{eq:sj_instance}\nc_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i<j} \\text{SJ}(y_i, y_j)\n\\end{equation}\nTwo design choices distinguish SJ from surface signals.\nFirst, type-aware grouping prevents spurious matches between extractions of different entity types.\nSecond, span-overlap matching tolerates near-synonym variations (e.g., ``machine learning'' vs.\\ ``ML''), which would be penalized by exact string comparison.\n\n\\paragraph{Entity voting confidence (structural, instance-level).}\nWhile SJ compares entire extraction sets, entity voting operates at the granularity of individual extractions.\nFor each entity $e$ appearing in the union $E_\\cup$ of all $N$ samples, we compute its frequency:\n\\begin{equation}\\label{eq:freq}\n\\text{freq}(e) = \\frac{|\\{i : e \\in y_i\\}|}{N}\n\\end{equation}\nThe instance-level confidence is the mean frequency across all observed entities:\n\\begin{equation}\\label{eq:voting}\nc_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)\n\\end{equation}\nThis adapts majority voting \\cite{wang2023selfconsistency} from discrete answer selection to set-valued extraction.\nEntities that appear consistently across samples contribute high frequency; hallucinated or idiosyncratic extractions that appear in only one or two samples pull the score down.\nThis per-entity granularity enables the signal to distinguish instances where the model reliably extracts a core set of entities (high $c_{\\text{vote}}$) from those where extractions vary widely across samples (low $c_{\\text{vote}}$).\n\n\\subsection{Evaluation Framework}\\label{sec:evaluation}\n\nWe assess confidence signals along two complementary dimensions.\n\n\\paragraph{Quality estimation.}\nQuality estimation asks: \\textit{for which instances does the model produce reliable outputs?}\nWe measure rank correlation between the confidence signal and instance-level F1 via Spearman $\\rho$ and Kendall $\\tau$.\nFor binary discrimination, we compute AUROC by classifying instances as above or below median F1.\nThese metrics evaluate whether a signal can identify reliable vs.\\ unreliable predictions without access to gold labels.\n\n\\paragraph{Sample selection.}\nSample selection asks: \\textit{given $N$ candidates for a single instance, which one is best?}\nWe report best-of-$N$ F1: for each instance, the signal selects one sample, and we compute micro F1 over all instances.\nWe compare against an \\textit{oracle} (which always selects the highest-F1 sample) and a \\textit{greedy baseline} ($T{=}0$, $N{=}1$).\nPer-sample signals like log-probability directly rank the $N$ candidates.\nInstance-level signals (SJ, FK, EM, Voting) produce a single score per instance and thus require an auxiliary strategy for sample selection---we select the sample closest to the consensus output, i.e., the one with highest average pairwise similarity to all other samples.\n\n\\paragraph{The two dimensions are complementary, not redundant.}\nA signal with high rank correlation accurately predicts relative instance difficulty, making it useful for quality-aware routing or selective prediction.\nHowever, high correlation does not guarantee effective sample selection: if per-sample variance is low---the model produces $N$ similar outputs for a given input---even a perfect quality estimator cannot distinguish among near-identical candidates.\nWe investigate this decoupling empirically in \\S\\ref{sec:selection_gap}.\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T19:41:45.723397+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260514T194021",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-14T19:41:45.723578+00:00_

Method 章节已写入 `docs/paper/sections/method.tex`。

要点：
- 三个小节：Problem Formulation (`sec:formulation`)、Confidence Signals (`sec:signals`)、Evaluation Framework (`sec:evaluation`)，label 与 experiments.tex 中的引用一致
- 信号分类与 experiments.tex 保持一致：Structural (Voting, SJ)、Surface (FK, EM)、Model-internal (logprob)
- 包含记号表（Table 1）
- 所有公式有 label，使用 equation 环境
- 仅引用 references.bib 中已有的 key：`wang2023selfconsistency`、`fleiss1971agreement`、`jaccard1901distribution`、`willard2023guided`
- 末尾自然过渡到 `\S\ref{sec:selection_gap}` 的实验分析
- 约 1000 词，无具体实验数字，无禁忌用语

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_method_20260514T194021"
}
```

</details>

---
