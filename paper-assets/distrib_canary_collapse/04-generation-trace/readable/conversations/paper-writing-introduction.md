# paper writing introduction

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_paper_writing_introduction_20260515T193353.jsonl`
- **Structured JSON:** [`8a2d087bd712cf6ab618.json`](../../sessions/8a/8a2d087bd712cf6ab618.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-15T19:38:36.621995+00:00_

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
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T19:38:36.622538+00:00_

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
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T19:38:36.622749+00:00_

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
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T19:38:36.623067+00:00_

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
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T19:38:36.623218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T19:38:36.623475+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter autoregressive language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
10	
11	Our protocol follows the full-replacement paradigm of \citet{shumailov2024curse}.
12	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data; (2)~generate 5{,}000 synthetic samples from the fine-tuned model; (3)~fully replace the synthetic pool.
13	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\alpha \in \{0.00, 0.25, 0.50, 0.75, 1.00\}$.
14	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; other conditions use seed~42, with multi-seed replication in progress.
15	
16	We track two \emph{canary metrics}---cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \cite{scheffer2009early}---and three \emph{downstream metrics}.
17	Canary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).
18	Downstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \cite{li2016diversity}) and perplexity.
19	We additionally evaluate effective rank and Self-BLEU as candidate canaries (\S\ref{sec:case_study}).
20	Results for distinct-3 are reported in Appendix~\ref{app:distinct3}.
21	
22	All hypothesis tests apply Benjamini--Hochberg (BH
…[truncated 15234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T19:38:36.623631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T19:38:36.623809+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	The experiments in \S\ref{sec:method_sensitivity}--\ref{sec:consensus_validation} reveal that lead-lag conclusions in iterative training collapse are fragile along multiple axes.
5	This section distills three methodological pitfalls (\S\ref{sec:pitfalls}), proposes a multi-method consensus framework to address them (\S\ref{sec:consensus}), and calibrates the framework's error rates using built-in experimental controls (\S\ref{sec:calibration}).
6	
7	
8	\subsection{Methodological Pitfalls in Lead-Lag Analysis}
9	\label{sec:pitfalls}
10	
11	We identify three pitfalls that, individually or in combination, can produce incorrect conclusions about temporal precedence in iterative training systems.
12	Each is documented below with representative data from our experiments; full results appear in \S\ref{sec:experiments}.
13	
14	\paragraph{Pitfall 1: Method sensitivity.}
15	Applied to the same data ($\alpha{=}1.0$, 4~seeds, 16 canary$\to$downstream pairs), five lead-lag detection methods yield FDR significance rates ranging from 100\% (naive cross-correlation) to 25\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\kappa{=}0.185$---poor agreement (\S\ref{sec:method_sensitivity}).
16	The spurious-signal rate---the fraction of pairs flagged by the most liberal method but not confirmed by the most conservative---is 75\% across all five methods and 62.5\% when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate.
17	This pitfall is dangerous because method choice alone can determine whether a lead-lag relationship is deemed present or absent.
18	In a literature where single-method analyses are the norm, the implicit assumption that method choice does not matter is demonstrably false.
19	
20	\paragraph{Pitfall 2: Spurious regression under shared trends.}
21	A single preprocessing decision---first-differencing to remove shared non-stationary trends---can eliminate an entire ana
…[truncated 8740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T19:38:36.623977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T19:38:36.624121+00:00_

1	\section{Background}
2	\label{sec:background}
3	
4	This section establishes the formal setup and notation used throughout the paper.
5	
6	\paragraph{Iterative training loop.}
7	Let $M_0$ denote a pretrained language model and $\mathcal{D}_\text{real}$ a fixed corpus of human-written text.
8	At each generation $t \geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\mathcal{D}_\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data:
9	\begin{equation}
10	    \mathcal{D}_\text{train}^{(t)} = \alpha \cdot \mathcal{D}_\text{synth}^{(t-1)} \;+\; (1{-}\alpha) \cdot \mathcal{D}_\text{real}, \quad \alpha \in [0, 1].
11	    \label{eq:mixing}
12	\end{equation}
13	The contamination level $\alpha$ controls the fraction of machine-generated text in each training round.
14	At $\alpha{=}1.0$, this reduces to the full-replacement paradigm of \citet{shumailov2024curse}, where each generation trains exclusively on the previous generation's output.
15	Iterating this process for $T$ generations yields a trajectory $M_0 \to M_1 \to \cdots \to M_T$.
16	
17	\paragraph{Metric families.}
18	We distinguish two families of metrics evaluated at each generation~$t$.
19	\emph{Canary metrics} are cheap-to-compute statistics on the model's output distribution, hypothesized to change before downstream quality degrades---analogous to early-warning indicators studied in the context of critical transitions in dynamical systems \cite{scheffer2009early}.
20	We consider two canary metrics: \emph{token entropy}, the average next-token prediction entropy over held-out samples, and \emph{expected calibration error} (ECE), which measures the discrepancy between predicted token probabilities and empirical correctness frequencies.
21	\emph{Downstream metrics} capture generation quality directly.
22	We use \emph{distinct-$n$} ($n \in \{1, 2, 3\}$), the ratio of unique $n$-grams to total $n$-grams in g
…[truncated 2286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T19:38:36.624273+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T19:38:36.624484+00:00_

1	% ============================================================
2	% CORE MODEL COLLAPSE
3	% ============================================================
4	
5	@article{shumailov2024curse,
6	  title     = {The Curse of Recursion: Training on Generated Data Makes Models Forget},
7	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},
8	  journal   = {Nature},
9	  year      = {2024},
10	  url       = {https://arxiv.org/abs/2305.17493},
11	}
12	
13	@inproceedings{alemohammad2024mad,
14	  title     = {Self-Consuming Generative Models Go {MAD}},
15	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard},
16	  booktitle = {International Conference on Learning Representations},
17	  year      = {2024},
18	  url       = {https://arxiv.org/abs/2307.01850},
19	}
20	
21	@inproceedings{dohmatob2024tale,
22	  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},
23	  author    = {Dohmatob, Elvis and Feng, Yunzhen and others},
24	  booktitle = {International Conference on Machine Learning},
25	  year      = {2024},
26	  url       = {https://arxiv.org/abs/2402.07043},
27	}
28	
29	@inproceedings{dohmatob2025strong,
30	  title     = {Strong Model Collapse},
31	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
32	  booktitle = {International Conference on Learning Representations},
33	  year      = {2025},
34	  url       = {https://arxiv.org/abs/2410.04840},
35	}
36	
37	@inproceedings{guo2024linguistic,
38	  title     = {The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},
39	  author    = {Guo, Yanzhu and Shang, Guokan and others},
40	  booktitle = {Findings of the Association for Computational Linguistics: {NAACL}},
41	  year      = {2024},
42	  url       = {https://arxiv.org/abs/2311.0
…[truncated 16326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T19:38:36.624649+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T19:38:36.624769+00:00_

background.tex
experiments.tex
method.tex
references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T19:38:36.625071+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining language models on their own output across successive generations leads to progressive distribution degradation, a phenomenon variously termed model collapse~\\cite{shumailov2024curse} or Model Autophagy Disorder~\\cite{alemohammad2024mad}.\nTail modes vanish, lexical diversity narrows, and calibration deteriorates as each generation's output becomes the next generation's training data.\nAs large language models become ubiquitous content generators, the fraction of machine-generated text on the web grows steadily, making iterative training collapse---where models are unwittingly trained on the output of earlier model generations---a practical concern for the long-term stability of language model ecosystems.\n\nA natural follow-up question is whether cheap-to-compute statistics---\\emph{canary metrics}---can provide early warning of impending collapse, analogous to early-warning signals for critical transitions in ecological and climate systems~\\cite{scheffer2009early,scheffer2012anticipating}.\nSeveral recent studies have pursued this direction: \\citet{du2026geometric} informally observe that expected calibration error rises before accuracy degrades; SIGMA~\\cite{sigma2026spectral} proposes spectral indicators of distributional shift; and DCES~\\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.\nYet the statistical methodology underlying these lead-lag claims---whether a canary metric genuinely \\emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends---has received little scrutiny.\n\nWe identify four methodological deficiencies that pervade existing lead-lag analyses of iterative training collapse:\n(1)~no differencing tests to rule out spurious regression arising from shared non-stationary trends---a well-known hazard when correlating co-trending time series;\n(2)~no multi-method cross-validation---conclusions rest on a single statistical method whose implicit assumptions about stationarity and directionality are rarely examined;\n(3)~no multiple comparison correction (e.g., Benjamini--Hochberg FDR control), increasing the risk of false discoveries when testing many metric pairs simultaneously; and\n(4)~no regime-dependent analysis, despite the possibility that the same statistical test yields opposite conclusions at different contamination levels.\nThe closest predecessor is \\citet{du2026geometric}, who observe that calibration error rises before accuracy degrades in iteratively trained language models.\nTheir analysis, however, is limited to a single metric pair, spans only 1--3 generations, and reports informal visual comparisons without statistical tests---leaving open the question of whether the observed lead is genuine or an artifact of shared trends.\nThe early-warning framework of \\citet{scheffer2009early,scheffer2012anticipating}---widely adopted in ecology for anticipating tipping points---provides the theoretical motivation for canary-based prediction, but has not been systematically applied to iterative training collapse with the methodological rigor that short, noisy time series demand~\\cite{boettiger2012limits}.\n\nWe address these gaps through a systematic case study of canary prediction of diversity collapse---the progressive loss of lexical diversity in model-generated text across training generations.\nUsing Pythia-410M across five contamination levels ($\\alpha \\in \\{0.00, 0.25, 0.50, 0.75, 1.00\\}$) and up to four random seeds, we expose three methodological pitfalls that undermine naive lead-lag analysis:\n\\begin{enumerate}\n    \\item \\textbf{Method sensitivity.} Applied to the same data, five lead-lag detection methods yield FDR significance rates ranging from 100\\% (naive cross-correlation) to 25\\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\\kappa{=}0.185$ (poor agreement).\n    \\item \\textbf{Spurious regression.} Canary$\\to$perplexity associations appear near-universal in undifferenced analysis but vanish entirely after first-differencing ($F{\\approx}0$, $p{=}0.99$), revealing them as artifacts of co-trending rather than genuine temporal precedence.\n    \\item \\textbf{Regime dependence.} Permutation Granger tests find 24/24 canary$\\to$diversity pairs FDR-significant at full synthetic replacement ($\\alpha{=}1.0$) but 0/8 at $\\alpha{\\leq}0.50$, demonstrating that detectability depends sharply on the contamination level.\n\\end{enumerate}\nTo move beyond single-method analysis, we propose a multi-method consensus framework with empirically calibrated thresholds, requiring agreement across multiple independent statistical methods and random seeds before classifying a lead-lag relationship as robust.\n\nThe framework's utility is demonstrated by its calibration on built-in experimental controls.\nNaive cross-correlation identifies 100\\% of canary--collapse metric pairs as FDR-significant; the consensus pipeline (requiring ${\\geq}4/5$ methods and ${\\geq}3/4$ seeds) retains only those pairs independently validated by the first-differencing diagnostic.\nOn reference extremes, the framework achieves a false positive rate of 0\\% at the $\\alpha{=}0.0$ null control (where individual methods reach up to 100\\% FPR) and a false negative rate of 0\\% against six ground-truth pairs at $\\alpha{=}1.0$.\nApplying the framework, we identify token entropy as a robust one-generation-ahead canary for diversity collapse at contamination levels $\\alpha{\\geq}0.75$, with cross-correlation $|r|{>}0.99$ and directional asymmetry confirmed by 0/24 reverse-direction FDR-significant pairs.\nWe note that Granger precedence establishes temporal predictive improvement, not true causality~\\cite{shojaie2022granger}.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Systematic exposure of three methodological pitfalls} in lead-lag analysis of iterative training collapse.\n    We quantify each pitfall: method choice alone swings significance from 100\\% to 25\\% with a spurious-signal rate of 75\\%; first-differencing eliminates canary$\\to$perplexity associations entirely; and the same Granger test shifts from 24/24 FDR-significant pairs to 0/8 across contamination levels.\n    These results demonstrate that single-method, single-regime analyses---the current norm in this literature---are unreliable.\n\n    \\item \\textbf{A multi-method consensus framework} with empirically calibrated thresholds and four-tier practical guidance ranging from exploratory ($K{\\geq}1/5$) to conservative ($K{=}5/5$).\n    The framework achieves FPR${=}$0\\% and FNR${=}$0\\% on reference extremes, providing robustness against miscalibration of any individual method.\n\n    \\item \\textbf{Application of the framework to identify token entropy} as a one-generation-ahead canary for diversity collapse at $\\alpha{\\geq}0.75$, scoped precisely to diversity metrics (distinct-$n$) rather than model collapse broadly, with a tiered practical guide mapping contamination regimes to recommended analysis strategies.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related_work} surveys related work on model collapse, early-warning signals, and lead-lag methodology.\n\\S\\ref{sec:background} establishes the formal setup, notation, and the five detection methods used throughout.\n\\S\\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.\n\\S\\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\\S\\ref{sec:method_sensitivity}), regime-dependent detectability (\\S\\ref{sec:regime}), a case study of canary prediction of diversity collapse (\\S\\ref{sec:case_study}), and consensus framework validation (\\S\\ref{sec:consensus_validation}).\n\\S\\ref{sec:discussion} discusses limitations---including the short time-series constraint, single-model scope, and the distinction between Granger precedence and causality---and outlines directions for future work.\n\\S\\ref{sec:conclusion} concludes.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining language models on their own output across successive generations leads to progressive distribution degradation, a phenomenon variously termed model collapse~\\cite{shumailov2024curse} or Model Autophagy Disorder~\\cite{alemohammad2024mad}.\nTail modes vanish, lexical diversity narrows, and calibration deteriorates as each generation's output becomes the next generation's training data.\nAs large language models become ubiquitous content generators, the fraction of machine-generated text on the web grows steadily, making iterative training collapse---where models are unwittingly trained on the output of earlier model generations---a practical concern for the long-term stability of language model ecosystems.\n\nA natural follow-up question is whether cheap-to-compute statistics---\\emph{canary metrics}---can provide early warning of impending collapse, analogous to early-warning signals for critical transitions in ecological and climate systems~\\cite{scheffer2009early,scheffer2012anticipating}.\nSeveral recent studies have pursued this direction: \\citet{du2026geometric} informally observe that expected calibration error rises before accuracy degrades; SIGMA~\\cite{sigma2026spectral} proposes spectral indicators of distributional shift; and DCES~\\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.\nYet the statistical methodology underlying these lead-lag claims---whether a canary metric genuinely \\emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends---has received little scrutiny.\n\nWe identify four methodological deficiencies that pervade existing lead-lag analyses of iterative training collapse:\n(1)~no differencing tests to rule out spurious regression arising from shared non-stationary trends---a well-known hazard when correlating co-trending time series;\n(2)~no multi-method cross-validation---conclusions rest on a single statistical method whose implicit assumptions about stationarity and directionality are rarely examined;\n(3)~no multiple comparison correction (e.g., Benjamini--Hochberg FDR control), increasing the risk of false discoveries when testing many metric pairs simultaneously; and\n(4)~no regime-dependent analysis, despite the possibility that the same statistical test yields opposite conclusions at different contamination levels.\nThe closest predecessor is \\citet{du2026geometric}, who observe that calibration error rises before accuracy degrades in iteratively trained language models.\nTheir analysis, however, is limited to a single metric pair, spans only 1--3 generations, and reports informal visual comparisons without statistical tests---leaving open the question of whether the observed lead is genuine or an artifact of shared trends.\nThe early-warning framework of \\citet{scheffer2009early,scheffer2012anticipating}---widely adopted in ecology for anticipating tipping points---provides the theoretical motivation for canary-based prediction, but has not been systematically applied to iterative training collapse with the methodological rigor that short, noisy time series demand~\\cite{boettiger2012limits}.\n\nWe address these gaps through a systematic case study of canary prediction of diversity collapse---the progressive loss of lexical diversity in model-generated text across training generations.\nUsing Pythia-410M across five contamination levels ($\\alpha \\in \\{0.00, 0.25, 0.50, 0.75, 1.00\\}$) and up to four random seeds, we expose three methodological pitfalls that undermine naive lead-lag analysis:\n\\begin{enumerate}\n    \\item \\textbf{Method sensitivity.} Applied to the same data, five lead-lag detection methods yield FDR significance rates ranging from 100\\% (naive cross-correlation) to 25\\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\\kappa{=}0.185$ (poor agreement).\n    \\item \\textbf{Spurious regression.} Canary$\\to$perplexity associations appear near-universal in undifferenced analysis but vanish entirely after first-differencing ($F{\\approx}0$, $p{=}0.99$), revealing them as artifacts of co-trending rather than genuine temporal precedence.\n    \\item \\textbf{Regime dependence.} Permutation Granger tests find 24/24 canary$\\to$diversity pairs FDR-significant at full synthetic replacement ($\\alpha{=}1.0$) but 0/8 at $\\alpha{\\leq}0.50$, demonstrating that detectability depends sharply on the contamination level.\n\\end{enumerate}\nTo move beyond single-method analysis, we propose a multi-method consensus framework with empirically calibrated thresholds, requiring agreement across multiple independent statistical methods and random seeds before classifying a lead-lag relationship as robust.\n\nThe framework's utility is demonstrated by its calibration on built-in experimental controls.\nNaive cross-correlation identifies 100\\% of canary--collapse metric pairs as FDR-significant; the consensus pipeline (requiring ${\\geq}4/5$ methods and ${\\geq}3/4$ seeds) retains only those pairs independently validated by the first-differencing diagnostic.\nOn reference extremes, the framework achieves a false positive rate of 0\\% at the $\\alpha{=}0.0$ null control (where individual methods reach up to 100\\% FPR) and a false negative rate of 0\\% against six ground-truth pairs at $\\alpha{=}1.0$.\nApplying the framework, we identify token entropy as a robust one-generation-ahead canary for diversity collapse at contamination levels $\\alpha{\\geq}0.75$, with cross-correlation $|r|{>}0.99$ and directional asymmetry confirmed by 0/24 reverse-direction FDR-significant pairs.\nWe note that Granger precedence establishes temporal predictive improvement, not true causality~\\cite{shojaie2022granger}.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Systematic exposure of three methodological pitfalls} in lead-lag analysis of iterative training collapse.\n    We quantify each pitfall: method choice alone swings significance from 100\\% to 25\\% with a spurious-signal rate of 75\\%; first-differencing eliminates canary$\\to$perplexity associations entirely; and the same Granger test shifts from 24/24 FDR-significant pairs to 0/8 across contamination levels.\n    These results demonstrate that single-method, single-regime analyses---the current norm in this literature---are unreliable.\n\n    \\item \\textbf{A multi-method consensus framework} with empirically calibrated thresholds and four-tier practical guidance ranging from exploratory ($K{\\geq}1/5$) to conservative ($K{=}5/5$).\n    The framework achieves FPR${=}$0\\% and FNR${=}$0\\% on reference extremes, providing robustness against miscalibration of any individual method.\n\n    \\item \\textbf{Application of the framework to identify token entropy} as a one-generation-ahead canary for diversity collapse at $\\alpha{\\geq}0.75$, scoped precisely to diversity metrics (distinct-$n$) rather than model collapse broadly, with a tiered practical guide mapping contamination regimes to recommended analysis strategies.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related_work} surveys related work on model collapse, early-warning signals, and lead-lag methodology.\n\\S\\ref{sec:background} establishes the formal setup, notation, and the five detection methods used throughout.\n\\S\\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.\n\\S\\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\\S\\ref{sec:method_sensitivity}), regime-dependent detectability (\\S\\ref{sec:regime}), a case study of canary prediction of diversity collapse (\\S\\ref{sec:case_study}), and consensus framework validation (\\S\\ref{sec:consensus_validation}).\n\\S\\ref{sec:discussion} discusses limitations---including the short time-series constraint, single-model scope, and the distinction between Granger precedence and causality---and outlines directions for future work.\n\\S\\ref{sec:conclusion} concludes.\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T19:38:36.625303+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T19:38:36.625452+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify introduction.tex",
  "subagent_type": "Explore",
  "prompt": "Verify the file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex against these criteria. Read the file and the references.bib at the same path, then report pass/fail for each:\n\n1. \\label{sec:introduction} exists\n2. All \\cite{} keys exist in references.bib (list each key found and whether it's in bib)\n3. Three contributions are listed in an enumerate environment\n4. Numbers match experiments.tex: 100%→25%, FPR=0%, FNR=0%, 24/24, 0/8, κ=0.185, 75% spurious rate, F≈0 p=0.99, |r|>0.99, 0/24 reverse\n5. No forbidden intensity words: \"consistently outperforms\", \"state-of-the-art\", bare \"significantly\" without statistical test context\n6. No \"phase diagram\" — should use \"regime map\" or similar\n7. Section navigation paragraph exists at the end\n8. PC07 respected: claims \"diversity collapse\" not \"model collapse\" for canary prediction scope\n9. PC11 respected: Granger precedence ≠ true causality disclaimer present\n10. C001: no citation of Phase 2 single-seed TY cross-α trends\n\nReport each as PASS or FAIL with brief explanation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify introduction.tex",
    "subagent_type": "Explore",
    "prompt": "Verify the file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex against these criteria. Read the file and the references.bib at the same path, then report pass/fail for each:\n\n1. \\label{sec:introduction} exists\n2. All \\cite{} keys exist in references.bib (list each key found and whether it's in bib)\n3. Three contributions are listed in an enumerate environment\n4. Numbers match experiments.tex: 100%→25%, FPR=0%, FNR=0%, 24/24, 0/8, κ=0.185, 75% spurious rate, F≈0 p=0.99, |r|>0.99, 0/24 reverse\n5. No forbidden intensity words: \"consistently outperforms\", \"state-of-the-art\", bare \"significantly\" without statistical test context\n6. No \"phase diagram\" — should use \"regime map\" or similar\n7. Section navigation paragraph exists at the end\n8. PC07 respected: claims \"diversity collapse\" not \"model collapse\" for canary prediction scope\n9. PC11 respected: Granger precedence ≠ true causality disclaimer present\n10. C001: no citation of Phase 2 single-seed TY cross-α trends\n\nReport each as PASS or FAIL with brief explanation."
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T19:38:36.625628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T19:38:36.625762+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training language models on their own output across successive generations leads to progressive distribution degradation, a phenomenon variously termed model collapse~\cite{shumailov2024curse} or Model Autophagy Disorder~\cite{alemohammad2024mad}.
5	Tail modes vanish, lexical diversity narrows, and calibration deteriorates as each generation's output becomes the next generation's training data.
6	As large language models become ubiquitous content generators, the fraction of machine-generated text on the web grows steadily, making iterative training collapse---where models are unwittingly trained on the output of earlier model generations---a practical concern for the long-term stability of language model ecosystems.
7	
8	A natural follow-up question is whether cheap-to-compute statistics---\emph{canary metrics}---can provide early warning of impending collapse, analogous to early-warning signals for critical transitions in ecological and climate systems~\cite{scheffer2009early,scheffer2012anticipating}.
9	Several recent studies have pursued this direction: \citet{du2026geometric} informally observe that expected calibration error rises before accuracy degrades; SIGMA~\cite{sigma2026spectral} proposes spectral indicators of distributional shift; and DCES~\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.
10	Yet the statistical methodology underlying these lead-lag claims---whether a canary metric genuinely \emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends---has received little scrutiny.
11	
12	We identify four methodological deficiencies that pervade existing lead-lag analyses of iterative training collapse:
13	(1)~no differencing tests to rule out spurious regression arising from shared non-stationary trends---a well-known hazard when correlating co-trending time series;
14	(2)~no multi-method cross-validation---conclusions rest
…[truncated 6232 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T19:38:36.625918+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T19:38:36.626079+00:00_

1	% ============================================================
2	% CORE MODEL COLLAPSE
3	% ============================================================
4	
5	@article{shumailov2024curse,
6	  title     = {The Curse of Recursion: Training on Generated Data Makes Models Forget},
7	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},
8	  journal   = {Nature},
9	  year      = {2024},
10	  url       = {https://arxiv.org/abs/2305.17493},
11	}
12	
13	@inproceedings{alemohammad2024mad,
14	  title     = {Self-Consuming Generative Models Go {MAD}},
15	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard},
16	  booktitle = {International Conference on Learning Representations},
17	  year      = {2024},
18	  url       = {https://arxiv.org/abs/2307.01850},
19	}
20	
21	@inproceedings{dohmatob2024tale,
22	  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},
23	  author    = {Dohmatob, Elvis and Feng, Yunzhen and others},
24	  booktitle = {International Conference on Machine Learning},
25	  year      = {2024},
26	  url       = {https://arxiv.org/abs/2402.07043},
27	}
28	
29	@inproceedings{dohmatob2025strong,
30	  title     = {Strong Model Collapse},
31	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
32	  booktitle = {International Conference on Learning Representations},
33	  year      = {2025},
34	  url       = {https://arxiv.org/abs/2410.04840},
35	}
36	
37	@inproceedings{guo2024linguistic,
38	  title     = {The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},
39	  author    = {Guo, Yanzhu and Shang, Guokan and others},
40	  booktitle = {Findings of the Association for Computational Linguistics: {NAACL}},
41	  year      = {2024},
42	  url       = {https://arxiv.org/abs/2311.0
…[truncated 16384 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T19:38:36.626219+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T19:38:36.626399+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter autoregressive language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
10	
11	Our protocol follows the full-replacement paradigm of \citet{shumailov2024curse}.
12	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data; (2)~generate 5{,}000 synthetic samples from the fine-tuned model; (3)~fully replace the synthetic pool.
13	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\alpha \in \{0.00, 0.25, 0.50, 0.75, 1.00\}$.
14	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; other conditions use seed~42, with multi-seed replication in progress.
15	
16	We track two \emph{canary metrics}---cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \cite{scheffer2009early}---and three \emph{downstream metrics}.
17	Canary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).
18	Downstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \cite{li2016diversity}) and perplexity.
19	We additionally evaluate effective rank and Self-BLEU as candidate canaries (\S\ref{sec:case_study}).
20	Results for distinct-3 are reported in Appendix~\ref{app:distinct3}.
21	
22	All hypothesis tests apply Benjamini--Hochberg (BH
…[truncated 15234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T19:38:36.626552+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "forbidden intensity words: \"consistently outperforms\"|\"state-of-the-art\"|(?<![a-zA-Z])significantly(?![a-zA-Z])",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Grep",
  "tool_args": {
    "pattern": "forbidden intensity words: \"consistently outperforms\"|\"state-of-the-art\"|(?<![a-zA-Z])significantly(?![a-zA-Z])",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T19:38:36.626668+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T19:38:36.626793+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "phase diagram",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Grep",
  "tool_args": {
    "pattern": "phase diagram",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T19:38:36.626899+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T19:38:36.627011+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "model collapse",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Grep",
  "tool_args": {
    "pattern": "model collapse",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T19:38:36.627117+00:00_

4:Training language models on their own output across successive generations leads to progressive distribution degradation, a phenomenon variously termed model collapse~\cite{shumailov2024curse} or Model Autophagy Disorder~\cite{alemohammad2024mad}.
45:    \item \textbf{Application of the framework to identify token entropy} as a one-generation-ahead canary for diversity collapse at $\alpha{\geq}0.75$, scoped precisely to diversity metrics (distinct-$n$) rather than model collapse broadly, with a tiered practical guide mapping contamination regimes to recommended analysis strategies.
49:\S\ref{sec:related_work} surveys related work on model collapse, early-warning signals, and lead-lag methodology.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T19:38:36.627237+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "diversity collapse",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Grep",
  "tool_args": {
    "pattern": "diversity collapse",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T19:38:36.627366+00:00_

21:We address these gaps through a systematic case study of canary prediction of diversity collapse---the progressive loss of lexical diversity in model-generated text across training generations.
33:Applying the framework, we identify token entropy as a robust one-generation-ahead canary for diversity collapse at contamination levels $\alpha{\geq}0.75$, with cross-correlation $|r|{>}0.99$ and directional asymmetry confirmed by 0/24 reverse-direction FDR-significant pairs.
45:    \item \textbf{Application of the framework to identify token entropy} as a one-generation-ahead canary for diversity collapse at $\alpha{\geq}0.75$, scoped precisely to diversity metrics (distinct-$n$) rather than model collapse broadly, with a tiered practical guide mapping contamination regimes to recommended analysis strategies.
52:\S\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\S\ref{sec:method_sensitivity}), regime-dependent detectability (\S\ref{sec:regime}), a case study of canary prediction of diversity collapse (\S\ref{sec:case_study}), and consensus framework validation (\S\ref{sec:consensus_validation}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T19:38:36.627487+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Granger precedence|true causality",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Granger precedence|true causality",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T19:38:36.627591+00:00_

34:We note that Granger precedence establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}.
53:\S\ref{sec:discussion} discusses limitations---including the short time-series constraint, single-model scope, and the distinction between Granger precedence and causality---and outlines directions for future work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T19:38:36.627709+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Phase 2|single-seed|cross-α",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Phase 2|single-seed|cross-α",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T19:38:36.627819+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T19:38:36.627930+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{([^}]+)\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{([^}]+)\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T19:38:36.628042+00:00_

4:Training language models on their own output across successive generations leads to progressive distribution degradation, a phenomenon variously termed model collapse~\cite{shumailov2024curse} or Model Autophagy Disorder~\cite{alemohammad2024mad}.
8:A natural follow-up question is whether cheap-to-compute statistics---\emph{canary metrics}---can provide early warning of impending collapse, analogous to early-warning signals for critical transitions in ecological and climate systems~\cite{scheffer2009early,scheffer2012anticipating}.
9:Several recent studies have pursued this direction: \citet{du2026geometric} informally observe that expected calibration error rises before accuracy degrades; SIGMA~\cite{sigma2026spectral} proposes spectral indicators of distributional shift; and DCES~\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.
19:The early-warning framework of \citet{scheffer2009early,scheffer2012anticipating}---widely adopted in ecology for anticipating tipping points---provides the theoretical motivation for canary-based prediction, but has not been systematically applied to iterative training collapse with the methodological rigor that short, noisy time series demand~\cite{boettiger2012limits}.
34:We note that Granger precedence establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T19:38:36.628173+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -o '@[a-z]*{[^,}]*' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib | sed 's/@[a-z]*{//' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -o '@[a-z]*{[^,}]*' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib | sed 's/@[a-z]*{//' | sort -u"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T19:38:36.628301+00:00_

alemohammad2024mad
ba2024fill
bakshi2026improvement
barzilai2025consistency
bergsma2026scaling
biderman2023pythia
boettiger2012limits
briesch2024selfconsuming
chen2025scales
dces2026counter
dey2024breaking
dohmatob2024tale
dohmatob2025strong
du2026geometric
feng2025escaping
fu2025selfconsuming
gambetta2024surplexity
gauthier2026alignment
granger1969investigating
guo2024linguistic
he2025closer
he2025golden
jing2022understanding
kalinowski2026topology
kazdan2025collapse
li2016diversity
marcinkevics2022neural
merity2017pointer
noci2024mind
qiu2025spectral
schaeffer2025position
scheffer2009early
scheffer2012anticipating
seddik2024howbad
shi2026pruning
shojaie2022granger
shumailov2024curse
sigma2026spectral
truong2025entropy
tubingen2026diffusion
wang2026contaminated
wright2025epistemic
xu2025mixing
zhu2018texygen

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T19:38:36.628427+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -o '\\\\cite\\([a-z{]*{[^}]*}\\|[a-z]*{[^}]*}\\)' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex | sed 's/.*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^ *//' | sort -u"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -o '\\\\cite\\([a-z{]*{[^}]*}\\|[a-z]*{[^}]*}\\)' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex | sed 's/.*{\\([^}]*\\)}/\\1/' | tr ',' '\\n' | sed 's/^ *//' | sort -u"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T19:38:36.628534+00:00_

alemohammad2024mad
boettiger2012limits
dces2026counter
du2026geometric
scheffer2009early
scheffer2012anticipating
shojaie2022granger
shumailov2024curse
sigma2026spectral

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T19:38:36.628653+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat > /tmp/check_cites.sh << 'EOF'\n#!/bin/bash\ncitations=(alemohammad2024mad boettiger2012limits dces2026counter du2026geometric scheffer2009early scheffer2012anticipating shojaie2022granger shumailov2024curse sigma2026spectral)\nbibfile=\"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib\"\n\nfor cite in \"${citations[@]}\"; do\n  if grep -q \"@[a-z]*{$cite\" \"$bibfile\"; then\n    echo \"✓ $cite\"\n  else\n    echo \"✗ MISSING: $cite\"\n  fi\ndone\nEOF\nbash /tmp/check_cites.sh\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "tool_args": {
    "command": "cat > /tmp/check_cites.sh << 'EOF'\n#!/bin/bash\ncitations=(alemohammad2024mad boettiger2012limits dces2026counter du2026geometric scheffer2009early scheffer2012anticipating shojaie2022granger shumailov2024curse sigma2026spectral)\nbibfile=\"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib\"\n\nfor cite in \"${citations[@]}\"; do\n  if grep -q \"@[a-z]*{$cite\" \"$bibfile\"; then\n    echo \"✓ $cite\"\n  else\n    echo \"✗ MISSING: $cite\"\n  fi\ndone\nEOF\nbash /tmp/check_cites.sh\n"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T19:38:36.628772+00:00_

✓ alemohammad2024mad
✓ boettiger2012limits
✓ dces2026counter
✓ du2026geometric
✓ scheffer2009early
✓ scheffer2012anticipating
✓ shojaie2022granger
✓ shumailov2024curse
✓ sigma2026spectral

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T19:38:36.628892+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "sed -n '36,46p' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "tool_args": {
    "command": "sed -n '36,46p' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T19:38:36.629000+00:00_

Our contributions are:
\begin{enumerate}
    \item \textbf{Systematic exposure of three methodological pitfalls} in lead-lag analysis of iterative training collapse.
    We quantify each pitfall: method choice alone swings significance from 100\% to 25\% with a spurious-signal rate of 75\%; first-differencing eliminates canary$\to$perplexity associations entirely; and the same Granger test shifts from 24/24 FDR-significant pairs to 0/8 across contamination levels.
    These results demonstrate that single-method, single-regime analyses---the current norm in this literature---are unreliable.

    \item \textbf{A multi-method consensus framework} with empirically calibrated thresholds and four-tier practical guidance ranging from exploratory ($K{\geq}1/5$) to conservative ($K{=}5/5$).
    The framework achieves FPR${=}$0\% and FNR${=}$0\% on reference extremes, providing robustness against miscalibration of any individual method.

    \item \textbf{Application of the framework to identify token entropy} as a one-generation-ahead canary for diversity collapse at $\alpha{\geq}0.75$, scoped precisely to diversity metrics (distinct-$n$) rather than model collapse broadly, with a tiered practical guide mapping contamination regimes to recommended analysis strategies.
\end{enumerate}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T19:38:36.629120+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "sed -n '48,54p' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "tool_args": {
    "command": "sed -n '48,54p' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T19:38:36.629226+00:00_

The remainder of this paper is organized as follows.
\S\ref{sec:related_work} surveys related work on model collapse, early-warning signals, and lead-lag methodology.
\S\ref{sec:background} establishes the formal setup, notation, and the five detection methods used throughout.
\S\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.
\S\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\S\ref{sec:method_sensitivity}), regime-dependent detectability (\S\ref{sec:regime}), a case study of canary prediction of diversity collapse (\S\ref{sec:case_study}), and consensus framework validation (\S\ref{sec:consensus_validation}).
\S\ref{sec:discussion} discusses limitations---including the short time-series constraint, single-model scope, and the distinction between Granger precedence and causality---and outlines directions for future work.
\S\ref{sec:conclusion} concludes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T19:38:36.629371+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat << 'EOF'\nNumbers to verify from introduction.tex in experiments.tex:\n- 100%→25% (method ranges)\n- FPR=0%\n- FNR=0%\n- 24/24 (canary→diversity at α=1.0)\n- 0/8 (at low α)\n- κ=0.185 (Cohen's kappa)\n- 75% spurious rate\n- F≈0 p=0.99 (differenced canary→perplexity)\n- |r|>0.99 (cross-correlation)\n- 0/24 reverse (reverse direction non-significant)\nEOF\n\ngrep -n \"100\\|25\\%\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex | head -20\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "tool_args": {
    "command": "cat << 'EOF'\nNumbers to verify from introduction.tex in experiments.tex:\n- 100%→25% (method ranges)\n- FPR=0%\n- FNR=0%\n- 24/24 (canary→diversity at α=1.0)\n- 0/8 (at low α)\n- κ=0.185 (Cohen's kappa)\n- 75% spurious rate\n- F≈0 p=0.99 (differenced canary→perplexity)\n- |r|>0.99 (cross-correlation)\n- 0/24 reverse (reverse direction non-significant)\nEOF\n\ngrep -n \"100\\|25\\%\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex | head -20\n"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T19:38:36.629496+00:00_

Numbers to verify from introduction.tex in experiments.tex:
- 100%→25% (method ranges)
- FPR=0%
- FNR=0%
- 24/24 (canary→diversity at α=1.0)
- 0/8 (at low α)
- κ=0.185 (Cohen's kappa)
- 75% spurious rate
- F≈0 p=0.99 (differenced canary→perplexity)
- |r|>0.99 (cross-correlation)
- 0/24 reverse (reverse direction non-significant)
54:The fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \textbf{16/16} (100\%), differenced cross-correlation \textbf{14/16} (87.5\%), threshold onset detection \textbf{9/16} (56.3\%), permutation Granger causality \textbf{6/16} (37.5\%), and Toda--Yamamoto Granger \textbf{4/16} (25.0\%).
55:Method choice alone swings significance from \textbf{100\% to 25\%}.
72:At $\alpha{=}0.0$ (no synthetic data, serving as null control), naive cross-correlation finds \textbf{100\%} of pairs significant---a textbook spurious-regression outcome in trending time series.
78:At $\alpha{=}0.25$, differenced cross-correlation drops to 25\% and threshold onset to 37.5\%, while naive cross-correlation remains at 100\%---demonstrating that even partial detrending removes marginal associations at low contamination.
90:Naive XCorr     & 100   & 100  & 100  & ---  & 100   & 100  \\
91:Diff.\ XCorr   & 37.5  & 25   & 100  & ---  & 100   & 37.5 \\
92:Threshold       & 62.5  & 37.5 & 100  & ---  & 100   & 62.5 \\
157:The consensus framework reduces the naive 100\% significance rate to the 37.5\% rate supported by the most conservative individual methods (Figure~\ref{fig:consensus_workflow}).
167:Individual-method FPR ranges from \textbf{100\%} (naive cross-correlation: 8/8 pairs) through 62.5\% (threshold) and 37.5\% (differenced) down to \textbf{0\%} (permutation Granger and Toda--Yamamoto).
187:Naive XCorr              & 100\%  & 0\%  \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-15T19:38:36.629632+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"0.185\\|75\\|24/24\\|0/8\\|0.99\\|0/24\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"0.185\\|75\\|24/24\\|0/8\\|0.99\\|0/24\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T19:38:36.629750+00:00_

13:We run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\alpha \in \{0.00, 0.25, 0.50, 0.75, 1.00\}$.
39:0.75 & $-27.7$ & $+1809.5$ & $-32.7$ & $-41.3$ & $+182.1$ \\
56:The spurious-signal rate---the fraction of pairs detected by the most liberal method but not confirmed by the most conservative---is \textbf{75\%} across all five methods and \textbf{62.5\%} when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate (\S\ref{sec:consensus_validation}).
60:For canary$\to$diversity pairs at $\alpha{=}1.0$, both undifferenced and differenced permutation Granger tests yield unanimous FDR significance, with all canary$\to$diversity pairs retaining unanimous FDR significance after differencing (24/24$\to$24/24)---confirming genuine temporal precedence rather than shared-trend confounding.
61:For canary$\to$perplexity, however, undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find \textbf{zero} significant pairs ($F{\approx}0$, $p{=}0.99$; Figure~\ref{fig:differencing_dmax}a).
66:At $d_{\max}{=}0$ (most permissive), approximately 6\% of pairs are rejected; at adaptive $d_{\max}$ determined by ADF unit-root tests, 75\%; at $d_{\max}{=}1$ (most conservative), \textbf{94\%}.
70:Cohen's $\kappa$, averaged over all method pairs, is \textbf{0.185} (poor agreement).
84:\caption{FDR significance rates (\%) for five lead-lag methods across contamination levels. Each cell reports the fraction of 8 primary canary$\to$downstream pairs (token entropy and ECE $\times$ 4 downstream metrics) reaching BH-corrected significance ($q{=}0.05$); failed candidates (effective rank, Self-BLEU) excluded per \S\ref{sec:case_study}. $\alpha{=}0.75$ is analyzed separately as single-seed data (\S\ref{sec:regime}). FPR$_\text{null}$: false positive rate at the $\alpha{=}0.0$ null control.}
88:Method & $\alpha{=}0.0$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\a
…[truncated 1848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-15T19:38:36.629890+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"FPR.*0.*FNR.*0\\|FNR.*0.*FPR.*0\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"FPR.*0.*FNR.*0\\|FNR.*0.*FPR.*0\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-15T19:38:36.630003+00:00_

174:We note a design asymmetry: FPR is validated on method-only data (single seed at $\alpha{=}0.0$), while FNR uses method$\times$seed joint data (4~seeds at $\alpha{=}1.0$).
181:\caption{False positive and false negative rates for individual methods and the consensus framework. FPR: $\alpha{=}0.0$ null control (single seed). FNR: $\alpha{=}1.0$ against 6 ground-truth pairs independently validated by first-differencing. Note dimension asymmetry: FPR is method-only; FNR is method$\times$seed joint (\S\ref{sec:consensus_validation}).}
185:Criterion & FPR ($\alpha{=}0.0$) & FNR ($\alpha{=}1.0$) \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-15T19:38:36.630121+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "sed -n '185,195p' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "tool_args": {
    "command": "sed -n '185,195p' /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-15T19:38:36.630230+00:00_

Criterion & FPR ($\alpha{=}0.0$) & FNR ($\alpha{=}1.0$) \\
\midrule
Naive XCorr              & 100\%  & 0\%  \\
Differenced XCorr        & 37.5\% & 0\%  \\
Threshold Onset          & 62.5\% & 0\%  \\
Permutation Granger      & 0\%    & 0\%  \\
Toda--Yamamoto           & 0\%    & 33.3\% \\
\midrule
Consensus ($K{\geq}4/5$)              & 0\%    & 0\%  \\
Consensus ($K{\geq}4/5$, $S{\geq}3/4$) & 0\%    & 0\%  \\
\bottomrule

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T19:38:36.630410+00:00_

Perfect! Now let me compile a comprehensive verification report.

## Verification Report: introduction.tex against Criteria

**1. \label{sec:introduction} exists** ✓ **PASS**
   - Line 2: `\label{sec:introduction}` is present immediately after `\section{Introduction}`

**2. All \cite{} keys exist in references.bib** ✓ **PASS**
   - Found 9 cited keys in introduction.tex:
     - shumailov2024curse ✓
     - alemohammad2024mad ✓
     - scheffer2009early ✓
     - scheffer2012anticipating ✓
     - du2026geometric ✓
     - sigma2026spectral ✓
     - dces2026counter ✓
     - boettiger2012limits ✓
     - shojaie2022granger ✓
   - All 9 keys verified in references.bib

**3. Three contributions listed in enumerate environment** ✓ **PASS**
   - Lines 37–46: Three items present:
     1. Systematic exposure of three methodological pitfalls
     2. A multi-method consensus framework
     3. Application of the framework to identify token entropy

**4. Numbers match experiments.tex** ✓ **PASS**
   - 100%→25%: experiments.tex line 55 "from \textbf{100\% to 25\%}"
   - FPR=0%: experiments.tex Table (line 193, 194) shows consensus framework achieves 0%
   - FNR=0%: experiments.tex Table (line 193, 194) shows consensus framework achieves 0%
   - 24/24: experiments.tex line 115 "yields \textbf{24/24} canary→diversity pairs"
   - 0/8: experiments.tex line 113 "find 0/8 pairs FDR-significant at α={0.00, 0.25, 0.50}"
   - κ=0.185: experiments.tex line 70 "Cohen's $\kappa$, averaged over all method pairs, is \textbf{0.185}"
   - 75% spurious rate: experiments.tex line 56 "spurious-signal rate...is \textbf{75\%}"
   - F≈0 p=0.99: experiments.tex line 61 "differenced tests find \textbf{zero} significant pairs ($F{\approx}0$, $p{=}0.99$)"
   - |r|>0.99: experiments.tex line 134 "Cross-correlation peaks at lag={+}1 with $|r|{>}0.99$"
   - 0/24 reverse: experiments.tex line 137 "Reverse-direction tests find \textbf{0/24} FDR-significant"

**5. No forbidden intensity words** ✓ **PASS**
   - No in
…[truncated 1643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_introduction_20260515T193353",
  "tool": "Agent",
  "elapsed_ms": 4
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-15T19:38:36.630582+00:00_

All 10 verification criteria pass. Introduction written to `docs/paper/introduction.tex` with:

- 3 contributions in `enumerate`, matching D042 (pitfalls → consensus framework → token entropy canary)
- All 9 `\cite{}` keys verified against `references.bib`
- Numbers exactly match `experiments.tex` (100%→25%, κ=0.185, 75% spurious rate, 24/24 vs 0/8, FPR=0%/FNR=0%, etc.)
- PC07/PC11/PC14/C001 constraints all respected
- Section navigation paragraph at end referencing §2–§7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_introduction_20260515T193353"
}
```

</details>

---
