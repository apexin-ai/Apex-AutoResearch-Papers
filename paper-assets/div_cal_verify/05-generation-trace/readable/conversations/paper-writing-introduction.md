# paper writing introduction

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_paper_writing_introduction_20260513T191640.jsonl`
- **Structured JSON:** [`c1d5ad6862c72cab4320.json`](../../sessions/c1/c1d5ad6862c72cab4320.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-13T19:20:08.610903+00:00_

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
  "session": "worker_paper_writing_introduction_20260513T191640",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T19:20:08.611494+00:00_

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
  "session": "worker_paper_writing_introduction_20260513T191640",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T19:20:08.611691+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260513T191640",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-13T19:20:08.611836+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260513T191640",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T19:20:08.611957+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260513T191640",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T19:20:08.612093+00:00_

docs/paper/main.tex
docs/paper/methodology.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260513T191640",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T19:20:08.612252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260513T191640",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T19:20:08.612450+00:00_

1	% === 1. Concept Drift / Embedding Drift ===
2	
3	@article{lu2019learning,
4	  title={Learning under Concept Drift: A Review},
5	  author={Lu, Jie and Liu, Anjin and Dong, Fan and Gu, Feng and Gama, Jo{\~a}o and Zhang, Guangquan},
6	  journal={IEEE Transactions on Knowledge and Data Engineering},
7	  volume={31},
8	  number={12},
9	  pages={2346--2363},
10	  year={2019},
11	  publisher={IEEE}
12	}
13	
14	@article{gama2014survey,
15	  title={A Survey on Concept Drift Adaptation},
16	  author={Gama, Jo{\~a}o and {\v{Z}}liobait{\.e}, Indr{\.e} and Bifet, Albert and Pechenizkiy, Mykola and Bouchachia, Abdelhamid},
17	  journal={ACM Computing Surveys},
18	  volume={46},
19	  number={4},
20	  pages={1--37},
21	  year={2014},
22	  publisher={ACM}
23	}
24	
25	@inproceedings{caccia2022new,
26	  title={New Insights on Reducing Abrupt Representation Change in Online Continual Learning},
27	  author={Caccia, Lucas and Aljundi, Rahaf and Asadi, Nader and Tuytelaars, Tinne and Pineau, Jo{\"e}lle and Belilovsky, Eugene},
28	  booktitle={International Conference on Learning Representations},
29	  year={2022}
30	}
31	
32	@inproceedings{davari2022probing,
33	  title={Probing Representation Forgetting in Supervised and Unsupervised Continual Learning},
34	  author={Davari, MohammadReza and Asadi, Nader and Mudur, Sudhir and Aljundi, Rahaf and Belilovsky, Eugene},
35	  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
36	  pages={16712--16721},
37	  year={2022}
38	}
39	
40	% === 2. Active Learning under Distribution Shift ===
41	
42	@inproceedings{ash2020deep,
43	  title={Deep Batch Active Learning by Diverse, Uncertain Gradient Lower Bounds},
44	  author={Ash, Jordan T. and Zhang, Chicheng and Krishnamurthy, Akshay and Langford, John and Agarwal, Alekh},
45	  booktitle={International Conference on Learning Representations},
46	  year={2020}
47	}
48	
49	@inproceedings{kirsch2019batchbald,
50	  title={{BatchBALD}: Efficient and Diverse Batc
…[truncated 10679 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260513T191640",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T19:20:08.612601+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260513T191640",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T19:20:08.612739+00:00_

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
15	\usepackage{xcolor}
16	
17	\title{The Embedding Alignment Gap: Why Diversity-Based Data Selection\\Accelerates Model Collapse in Iterative Self-Training}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\textit{[To be written after Experiments section is complete.]}
26	\end{abstract}
27	
28	\input{introduction}
29	
30	\input{related_work}
31	
32	\input{methodology}
33	
34	% \input{experiments}
35	
36	% \input{conclusion}
37	
38	\section*{Limitations}
39	\textit{[To be written.]}
40	
41	\bibliography{references}
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260513T191640",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T19:20:08.612873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260513T191640",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T19:20:08.613028+00:00_

1	\section{Methodology}
2	
3	We design a controlled iterative self-training experiment to isolate how embedding-based diversity selection interacts with model collapse. The experiment holds the training protocol, data budget, and selection algorithm constant while varying only the source of embeddings used for data selection, enabling direct attribution of observed differences to the embedding alignment gap.
4	
5	\subsection{Base Model and Dataset}
6	
7	We use GPT2-125M (124M parameters) as our base model, loaded from the HuggingFace pretrained checkpoint. We train and evaluate on WikiText-103, which contains 232,588 training samples of long-form Wikipedia articles.
8	
9	We choose GPT2-125M for two reasons. First, its modest size permits running full self-training pipelines across multiple generations, data selection methods, and random seeds---a combinatorial design that would be prohibitively expensive with larger models. Second, despite its size, GPT2-125M exhibits the representation learning dynamics characteristic of transformer architectures, including the embedding drift and dimensional collapse phenomena central to our analysis \citep{jing2022understanding}.
10	
11	\subsection{Self-Training Protocol}
12	
13	We implement iterative self-training in a student-as-generator loop: at each generation, the current model generates synthetic text, a data selection method curates a subset, and the model is fine-tuned on that subset to produce the next-generation model.
14	
15	We run 8 generations (Generation 0 through 7). Generation~0 fine-tunes the pretrained GPT2-125M on the original WikiText-103 training data and serves as the shared starting point for all methods. From Generation~1 onward, each generation proceeds as follows: (1)~the model generates 500K tokens via nucleus sampling; (2)~a data selection method selects a subset; (3)~the model is fine-tuned on the selected data starting from the previous generation's checkpoint (cumulative fine-tuning).
16	
17	All ge
…[truncated 5825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260513T191640",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T19:20:08.613360+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\n\nTraining language models on their own generated data across multiple iterations leads to \\emph{model collapse}---a progressive degradation in both output quality and lexical diversity \\citep{shumailov2024ai, alemohammad2024self}. Each generation of synthetic data carries distributional artifacts from its parent model; when these artifacts compound across iterations, the distribution's tails erode and the model converges toward a narrow, repetitive mode \\citep{seddik2024how, briesch2023large, guo2024curious}. As synthetic data becomes an increasingly prevalent component of training pipelines, understanding this feedback loop---and identifying strategies that avoid it---has become a pressing concern \\citep{dohmatob2025strong, gerstgrasser2024model}.\n\nDiversity-based data curation is a natural mitigation strategy. If model collapse arises from training on redundant or low-quality synthetic samples, then selecting a maximally diverse subset should preserve the distributional richness that iterative training erodes. Submodular maximization over embedding spaces provides a principled framework for this goal: facility location objectives identify representative subsets that maximize geometric coverage of the data distribution \\citep{wei2015submodularity, mirzasoleiman2020coresets}. Embedding-based selection has demonstrated strong results in data pruning \\citep{sorscher2022beyond} and data-efficient training more broadly \\citep{xie2023data, xia2024less, engstrom2024dsdm}. When the model's own representations define the embedding space, diversity selection should---in principle---directly counteract the homogenization that drives collapse.\n\nWe test this intuition in a controlled iterative self-training experiment and find the opposite of the expected outcome. Representation-Guided Diversity Selection (RGDS)---which selects the most diverse 50\\% of synthetic data according to the training model's own last-hidden-layer embeddings---increases Generation~7 perplexity by +74\\% relative to random selection under the same 50\\% data budget (75.07 vs.\\ 43.20, seed=42). Rare n-gram density in RGDS-selected text drops by 47\\% compared to random selection (0.0051 vs.\\ 0.0096). The method designed to preserve diversity accelerates collapse instead. This result replicates across seeds: RGDS produces Generation~7 perplexities of 75.07 (seed=42) and 81.57 (seed=123), while all other methods---random selection, external-embedding selection, and no selection---remain between 41 and 50.\n\nThe failure exposes a gap in the data selection literature. Methods such as SemDeDup [CITATION NEEDED: Abbas et al.\\ 2023], D4 [CITATION NEEDED: Tirumala et al.\\ 2023], and DSIR \\citep{xie2023data} are designed for one-shot curation of static datasets, where the model providing embeddings is fixed and its representation quality is not in question. Active learning methods account for model updates between selection rounds \\citep{ash2020deep, kirsch2019batchbald}, but they do not address the compound effect of selection bias feeding back into the selecting model's own training data across generations. The concept drift literature establishes that learned representations degrade under sustained distribution shift \\citep{lu2019learning, gama2014survey}, but no prior work examines how this degradation interacts with embedding-based data selection in a self-consuming training loop---a setting where the model that selects the data is also the model whose next generation of representations is shaped by that selection.\n\nWe identify the mechanism behind this failure as the \\emph{embedding alignment gap}: a progressive divergence between what the model's internal representations treat as ``diverse'' and what constitutes genuine content diversity. To quantify this divergence, we define the \\emph{selection ratio}---the mean rare n-gram density of the selected subset divided by that of the full generated pool. A selection ratio above~1 indicates that the method preferentially retains content-rich samples; below~1 indicates preferential retention of content-poor samples. For RGDS, the selection ratio follows an overall declining trend from 1.04 at Generation~1 to 0.52 at Generation~7 (seed=42), with a transient rebound in Generations~2--4 before sustained decline. By the final generation, RGDS actively selects for vocabulary-poor samples, and its selected subsets contain 47\\% fewer rare n-grams than random selection produces. The model's internal notion of diversity has inverted relative to content diversity. This trajectory is consistent with dimensional collapse in the embedding space \\citep{jing2022understanding, laurent2024feature}: as the model trains on increasingly homogeneous data, its effective representational dimensionality shrinks, formerly distinct content regions merge, and the selection algorithm maximizes coverage of a space that no longer encodes the distinctions that matter.\n\nThe sharpest evidence for the embedding alignment gap comes from comparing methods that share identical selection budgets and algorithms but differ only in their embedding source. All methods that bypass the model's internal embeddings cluster in a band of moderate degradation at Generation~7: Random~50\\% reaches perplexity 43.20, External-only selection using frozen Contriever \\citep{izacard2022unsupervised} embeddings reaches 45.51, and the Uncurated baseline using 100\\% of generated data reaches 50.28---all at seed=42. The pattern holds with seed=123 (Random 41.75, External-only 49.66, Uncurated 46.15). Only RGDS---the sole method coupling selection to the training model's own representations---produces catastrophic outcomes: 75.07 and 81.57 across the two seeds. The External-only method is particularly informative: it applies the same submodular facility location algorithm as RGDS with the same 50\\% budget, but uses a frozen Contriever encoder whose embeddings do not co-degrade with the training model. Its Generation~7 perplexity (45.51) falls within the normal cluster, confirming that the selection algorithm itself is not at fault. The failure arises specifically from using co-degrading internal embeddings as the selection criterion---a form of Goodhart's law in representation space \\citep{gao2023scaling, karwowski2024goodhart}, where optimizing for diversity as measured by the model's own embeddings ceases to track actual content diversity once those embeddings lose fidelity.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item We define the \\emph{selection ratio}, a diagnostic metric that quantifies the alignment between a selection method's diversity criterion and content diversity, and show that it tracks the onset of catastrophic failure---declining from 1.04 to 0.52 across 8 generations for RGDS.\n    \\item We demonstrate that internal-embedding diversity selection accelerates model collapse by +74\\% in perplexity compared to random selection under the same data budget, while reducing rare n-gram density by 47\\%.\n    \\item We isolate the failure mechanism to internal embeddings specifically: all non-internal methods---random selection, frozen external embeddings, and no selection---avoid catastrophic degradation, confirming that the failure arises from coupling selection to co-degrading representations rather than from the selection algorithm or data budget.\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260513T191640",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\n\nTraining language models on their own generated data across multiple iterations leads to \\emph{model collapse}---a progressive degradation in both output quality and lexical diversity \\citep{shumailov2024ai, alemohammad2024self}. Each generation of synthetic data carries distributional artifacts from its parent model; when these artifacts compound across iterations, the distribution's tails erode and the model converges toward a narrow, repetitive mode \\citep{seddik2024how, briesch2023large, guo2024curious}. As synthetic data becomes an increasingly prevalent component of training pipelines, understanding this feedback loop---and identifying strategies that avoid it---has become a pressing concern \\citep{dohmatob2025strong, gerstgrasser2024model}.\n\nDiversity-based data curation is a natural mitigation strategy. If model collapse arises from training on redundant or low-quality synthetic samples, then selecting a maximally diverse subset should preserve the distributional richness that iterative training erodes. Submodular maximization over embedding spaces provides a principled framework for this goal: facility location objectives identify representative subsets that maximize geometric coverage of the data distribution \\citep{wei2015submodularity, mirzasoleiman2020coresets}. Embedding-based selection has demonstrated strong results in data pruning \\citep{sorscher2022beyond} and data-efficient training more broadly \\citep{xie2023data, xia2024less, engstrom2024dsdm}. When the model's own representations define the embedding space, diversity selection should---in principle---directly counteract the homogenization that drives collapse.\n\nWe test this intuition in a controlled iterative self-training experiment and find the opposite of the expected outcome. Representation-Guided Diversity Selection (RGDS)---which selects the most diverse 50\\% of synthetic data according to the training model's own last-hidden-layer embeddings---increases Generation~7 perplexity by +74\\% relative to random selection under the same 50\\% data budget (75.07 vs.\\ 43.20, seed=42). Rare n-gram density in RGDS-selected text drops by 47\\% compared to random selection (0.0051 vs.\\ 0.0096). The method designed to preserve diversity accelerates collapse instead. This result replicates across seeds: RGDS produces Generation~7 perplexities of 75.07 (seed=42) and 81.57 (seed=123), while all other methods---random selection, external-embedding selection, and no selection---remain between 41 and 50.\n\nThe failure exposes a gap in the data selection literature. Methods such as SemDeDup [CITATION NEEDED: Abbas et al.\\ 2023], D4 [CITATION NEEDED: Tirumala et al.\\ 2023], and DSIR \\citep{xie2023data} are designed for one-shot curation of static datasets, where the model providing embeddings is fixed and its representation quality is not in question. Active learning methods account for model updates between selection rounds \\citep{ash2020deep, kirsch2019batchbald}, but they do not address the compound effect of selection bias feeding back into the selecting model's own training data across generations. The concept drift literature establishes that learned representations degrade under sustained distribution shift \\citep{lu2019learning, gama2014survey}, but no prior work examines how this degradation interacts with embedding-based data selection in a self-consuming training loop---a setting where the model that selects the data is also the model whose next generation of representations is shaped by that selection.\n\nWe identify the mechanism behind this failure as the \\emph{embedding alignment gap}: a progressive divergence between what the model's internal representations treat as ``diverse'' and what constitutes genuine content diversity. To quantify this divergence, we define the \\emph{selection ratio}---the mean rare n-gram density of the selected subset divided by that of the full generated pool. A selection ratio above~1 indicates that the method preferentially retains content-rich samples; below~1 indicates preferential retention of content-poor samples. For RGDS, the selection ratio follows an overall declining trend from 1.04 at Generation~1 to 0.52 at Generation~7 (seed=42), with a transient rebound in Generations~2--4 before sustained decline. By the final generation, RGDS actively selects for vocabulary-poor samples, and its selected subsets contain 47\\% fewer rare n-grams than random selection produces. The model's internal notion of diversity has inverted relative to content diversity. This trajectory is consistent with dimensional collapse in the embedding space \\citep{jing2022understanding, laurent2024feature}: as the model trains on increasingly homogeneous data, its effective representational dimensionality shrinks, formerly distinct content regions merge, and the selection algorithm maximizes coverage of a space that no longer encodes the distinctions that matter.\n\nThe sharpest evidence for the embedding alignment gap comes from comparing methods that share identical selection budgets and algorithms but differ only in their embedding source. All methods that bypass the model's internal embeddings cluster in a band of moderate degradation at Generation~7: Random~50\\% reaches perplexity 43.20, External-only selection using frozen Contriever \\citep{izacard2022unsupervised} embeddings reaches 45.51, and the Uncurated baseline using 100\\% of generated data reaches 50.28---all at seed=42. The pattern holds with seed=123 (Random 41.75, External-only 49.66, Uncurated 46.15). Only RGDS---the sole method coupling selection to the training model's own representations---produces catastrophic outcomes: 75.07 and 81.57 across the two seeds. The External-only method is particularly informative: it applies the same submodular facility location algorithm as RGDS with the same 50\\% budget, but uses a frozen Contriever encoder whose embeddings do not co-degrade with the training model. Its Generation~7 perplexity (45.51) falls within the normal cluster, confirming that the selection algorithm itself is not at fault. The failure arises specifically from using co-degrading internal embeddings as the selection criterion---a form of Goodhart's law in representation space \\citep{gao2023scaling, karwowski2024goodhart}, where optimizing for diversity as measured by the model's own embeddings ceases to track actual content diversity once those embeddings lose fidelity.\n\nOur contributions are as follows:\n\\begin{enumerate}\n    \\item We define the \\emph{selection ratio}, a diagnostic metric that quantifies the alignment between a selection method's diversity criterion and content diversity, and show that it tracks the onset of catastrophic failure---declining from 1.04 to 0.52 across 8 generations for RGDS.\n    \\item We demonstrate that internal-embedding diversity selection accelerates model collapse by +74\\% in perplexity compared to random selection under the same data budget, while reducing rare n-gram density by 47\\%.\n    \\item We isolate the failure mechanism to internal embeddings specifically: all non-internal methods---random selection, frozen external embeddings, and no selection---avoid catastrophic degradation, confirming that the failure arises from coupling selection to co-degrading representations rather than from the selection algorithm or data budget.\n\\end{enumerate}\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T19:20:08.613593+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260513T191640",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-13T19:20:08.613773+00:00_

Introduction 已写入 `docs/paper/introduction.tex`。

要点：
- 6段 + 贡献列表，约1100词
- 所有定量声明均有 seed=42 和 seed=123 数据支撑
- Selection ratio 使用 "overall declining trend"，注明 Generations 2-4 transient rebound
- SemDeDup 和 D4 使用 `[CITATION NEEDED]` 占位
- 未使用 "significantly" 和 "state-of-the-art"
- Novelty framing 为"首次在 iterative self-training 中量化并隔离"，未 overclaim 概念原创性

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_20260513T191640"
}
```

</details>

---
